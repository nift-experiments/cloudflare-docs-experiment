#!/usr/bin/env python3
"""Fail-closed static accessibility audit over the complete generated corpus."""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))

from artifact_provenance import tree_digest
from audit_structure import expected_pages, output_path


class AccessibilityParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.html_lang = None
        self.ids = set()
        self.aria_refs = []
        self.controls = []
        self.labels_for = set()
        self.iframes_without_title = 0
        self.heading_levels = []
        self.main_count = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        node = {'tag': tag, 'attrs': attrs, 'text': [], 'wrapped_label': False}
        if tag == 'html':
            self.html_lang = attrs.get('lang')
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        for attribute in ('aria-labelledby', 'aria-describedby', 'aria-controls'):
            if attrs.get(attribute):
                self.aria_refs.extend((attribute, value) for value in attrs[attribute].split())
        if tag == 'label' and attrs.get('for'):
            self.labels_for.add(attrs['for'])
        if tag == 'main':
            self.main_count += 1
        if re.fullmatch(r'h[1-6]', tag):
            self.heading_levels.append(int(tag[1]))
        if tag == 'iframe' and not (attrs.get('title') or '').strip():
            self.iframes_without_title += 1
        if tag == 'img' and attrs.get('alt'):
            for parent in self.stack:
                parent['text'].append(attrs['alt'])
        if tag in {'input', 'select', 'textarea'}:
            node['wrapped_label'] = any(parent['tag'] == 'label' for parent in self.stack)
        self.stack.append(node)
        if tag in {'input', 'img', 'meta', 'link', 'br', 'hr', 'source'}:
            self._finish(tag)

    handle_startendtag = handle_starttag

    def handle_data(self, data):
        for node in self.stack:
            node['text'].append(data)

    def handle_endtag(self, tag):
        self._finish(tag)

    def _finish(self, tag):
        index = next((i for i in range(len(self.stack) - 1, -1, -1)
                      if self.stack[i]['tag'] == tag), None)
        if index is None:
            return
        nodes = self.stack[index:]
        self.stack = self.stack[:index]
        for node in reversed(nodes):
            attrs = node['attrs']
            node_tag = node['tag']
            role = attrs.get('role')
            is_link = node_tag == 'a' and bool(attrs.get('href'))
            if node_tag in {'button', 'input', 'select', 'textarea'} or is_link or role == 'button':
                text = re.sub(r'\s+', ' ', ''.join(node['text'])).strip()
                self.controls.append({
                    'tag': node_tag,
                    'role': role,
                    'id': attrs.get('id'),
                    'type': attrs.get('type', '').lower(),
                    'href': attrs.get('href'),
                    'name': (attrs.get('aria-label') or attrs.get('title') or
                             attrs.get('value') or text).strip(),
                    'labelledby': attrs.get('aria-labelledby'),
                    'wrapped_label': node['wrapped_label'],
                    'tabindex': attrs.get('tabindex'),
                })


def audit(public, ordinary_manifest, generated_manifest):
    ordinary = json.loads(Path(ordinary_manifest).read_text())
    generated = json.loads(Path(generated_manifest).read_text())
    upstream_sha = ordinary.get('upstream_sha')
    if not upstream_sha or generated.get('upstream_sha') != upstream_sha:
        raise RuntimeError('ordinary/generated manifest upstream SHA mismatch')
    routes = expected_pages(ordinary_manifest, generated_manifest)
    findings = collections.defaultdict(list)
    advisories = collections.defaultdict(list)
    totals = collections.Counter()

    for route in routes:
        page = output_path(public, route)
        if not page.is_file():
            findings['missing_html'].append(route)
            continue
        parser = AccessibilityParser()
        try:
            parser.feed(page.read_text(errors='replace'))
        except Exception as exc:
            findings['parse_errors'].append({'route': route, 'error': str(exc)})
            continue
        totals['pages'] += 1
        totals['controls'] += len(parser.controls)
        if parser.html_lang != 'en':
            findings['document_language'].append({'route': route, 'lang': parser.html_lang})
        if parser.main_count != 1:
            findings['main_landmark'].append({'route': route, 'count': parser.main_count})
        dangling = sorted({f'{attribute}:{target}' for attribute, target in parser.aria_refs
                           if target not in parser.ids})
        if dangling:
            findings['dangling_aria_reference'].append({'route': route, 'references': dangling})
        unnamed = []
        fake_buttons = []
        for control in parser.controls:
            if control['tag'] == 'input' and control['type'] == 'hidden':
                continue
            labelled = (control['name'] or control['labelledby'] or
                        control['wrapped_label'] or
                        (control['id'] and control['id'] in parser.labels_for))
            if not labelled:
                unnamed.append({key: control[key] for key in ('tag', 'role', 'id', 'type', 'href')})
            if control['role'] == 'button' and control['tag'] not in {'button', 'input'}:
                if control['tabindex'] not in {'0', 0}:
                    fake_buttons.append({key: control[key] for key in ('tag', 'id', 'tabindex')})
        if unnamed:
            findings['unnamed_control'].append({'route': route, 'controls': unnamed})
        if fake_buttons:
            findings['non_keyboard_button_role'].append({'route': route, 'controls': fake_buttons})
        if parser.iframes_without_title:
            findings['iframe_without_title'].append(
                {'route': route, 'count': parser.iframes_without_title})
        skips = [(previous, current) for previous, current in
                 zip(parser.heading_levels, parser.heading_levels[1:])
                 if current > previous + 1]
        if skips:
            advisories['heading_level_skips'].append({'route': route, 'transitions': skips})

    fatal_count = sum(len(values) for values in findings.values())
    return {
        'schemaVersion': 1,
        'upstreamSha': upstream_sha,
        'expectedPages': len(routes),
        'totals': dict(totals),
        'fatalFindingCount': fatal_count,
        'findings': {key: value for key, value in sorted(findings.items())},
        'advisories': {key: value for key, value in sorted(advisories.items())},
    }


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--public', type=Path, default=ROOT / 'public')
    parser.add_argument('--ordinary-manifest', default=ROOT / 'reports/cp6/expected-routes.json')
    parser.add_argument('--generated-manifest', default=ROOT / 'reports/cp6/expected-generated-routes.json')
    parser.add_argument('--output', type=Path, default=ROOT / 'reports/cp9/accessibility-static.json')
    parser.add_argument('--candidate-provenance', type=Path)
    args = parser.parse_args(argv)
    report = audit(args.public, args.ordinary_manifest, args.generated_manifest)
    if args.candidate_provenance:
        provenance = json.loads(args.candidate_provenance.read_text())
        digest, file_count = tree_digest(args.public)
        if (provenance.get('upstreamSha') != report['upstreamSha'] or
                provenance.get('publicTreeSha256') != digest or
                provenance.get('publicFileCount') != file_count):
            parser.error('candidate provenance mismatch')
        report['candidateProvenance'] = provenance
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: report[key] for key in (
        'expectedPages', 'totals', 'fatalFindingCount')}, indent=2))
    return 1 if report['fatalFindingCount'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
