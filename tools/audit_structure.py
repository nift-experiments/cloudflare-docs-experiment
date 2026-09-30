#!/usr/bin/env python3
"""Fail-closed structural audit for every generated HTML page."""
from __future__ import annotations

import argparse
import collections
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.counts = collections.Counter()
        self.ids = []
        self.heading_ids = []
        self.heading_levels = []
        self.images = []
        self.resources = []
        self.placeholder_links = 0
        self.component_shells = collections.Counter()
        self.article_depth = 0
        self.splash_main = False
        self.docs_articles = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.counts[tag] += 1
        if tag == 'article':
            self.article_depth += 1
            if 'docs-content' in set((attrs.get('class') or '').split()):
                self.docs_articles += 1
        if tag == 'main' and 'splash-main' in set((attrs.get('class') or '').split()):
            self.splash_main = True
        if attrs.get('id'):
            self.ids.append(attrs['id'])
        if tag in {'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}:
            self.heading_levels.append(int(tag[1]))
            classes = set((attrs.get('class') or '').split())
            if (self.article_depth and tag != 'h1' and not attrs.get('id') and
                    'nb-aside-title' not in classes):
                self.heading_ids.append(tag)
        if tag == 'img':
            self.images.append((attrs.get('src'), 'alt' in attrs))
        if tag == 'a' and attrs.get('href') == '#':
            self.placeholder_links += 1
        resource_attributes = ('src', 'poster') + (('href',) if tag == 'link' else ())
        for attribute in resource_attributes:
            value = attrs.get(attribute)
            if value:
                self.resources.append(value)
        classes = set((attrs.get('class') or '').split())
        for marker in ('nb-interactive-component', 'nb-data-component'):
            if marker in classes:
                self.component_shells[marker] += 1

    handle_startendtag = handle_starttag

    def handle_endtag(self, tag):
        if tag == 'article' and self.article_depth:
            self.article_depth -= 1


def expected_pages(ordinary_manifest, generated_manifest):
    ordinary = json.loads(Path(ordinary_manifest).read_text())
    generated = json.loads(Path(generated_manifest).read_text())
    return sorted(set(ordinary['routes']) | {'/'} | set(generated['routes']))


def output_path(public, route):
    return public / ('index.html' if route == '/' else route.strip('/') + '/index.html')


def local_resource_exists(public, page, value):
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc or value.startswith(('data:', 'mailto:', 'tel:', '//', '#')):
        return True
    path = unquote(parsed.path)
    if not path:
        return True
    target = public / path.lstrip('/') if path.startswith('/') else page.parent / path
    if path.endswith('/') or target.is_dir():
        target = target / 'index.html'
    return target.exists()


def audit(public, ordinary_manifest, generated_manifest):
    ordinary_data = json.loads(Path(ordinary_manifest).read_text())
    generated_data = json.loads(Path(generated_manifest).read_text())
    upstream_sha = ordinary_data.get('upstream_sha')
    if not upstream_sha or generated_data.get('upstream_sha') != upstream_sha:
        raise RuntimeError('ordinary/generated manifest upstream SHA mismatch')
    routes = expected_pages(ordinary_manifest, generated_manifest)
    findings = collections.defaultdict(list)
    totals = collections.Counter()
    shell_counts = collections.Counter()

    for route in routes:
        page = output_path(public, route)
        if not page.is_file():
            findings['missing_html'].append(route)
            continue
        parser = PageParser()
        try:
            parser.feed(page.read_text(errors='replace'))
        except Exception as exc:
            findings['parse_errors'].append({'route': route, 'error': str(exc)})
            continue
        totals['pages'] += 1
        totals['images'] += len(parser.images)
        totals['tables'] += parser.counts['table']
        totals['interactive_component_shells'] += parser.component_shells['nb-interactive-component']
        totals['data_component_shells'] += parser.component_shells['nb-data-component']
        duplicate_ids = sorted(key for key, count in collections.Counter(parser.ids).items() if count > 1)
        if duplicate_ids:
            findings['duplicate_ids'].append({'route': route, 'ids': duplicate_ids})
        if parser.counts['h1'] != 1:
            findings['h1_count'].append({'route': route, 'count': parser.counts['h1']})
        if parser.heading_ids:
            findings['headings_without_ids'].append({'route': route, 'tags': parser.heading_ids})
        if parser.counts['main'] != 1:
            findings['main_count'].append({'route': route, 'count': parser.counts['main']})
        if route != '/' and not parser.splash_main and parser.docs_articles != 1:
            findings['article_count'].append({'route': route, 'count': parser.docs_articles})
        for tag in ('header', 'footer', 'nav'):
            if parser.counts[tag]:
                shell_counts[tag] += 1
            elif tag != 'nav':
                findings[f'missing_{tag}'].append(route)
        missing_alt = [src for src, has_alt in parser.images if not has_alt]
        if missing_alt:
            findings['images_without_alt'].append({'route': route, 'sources': missing_alt})
        if parser.placeholder_links:
            findings['placeholder_links'].append({'route': route, 'count': parser.placeholder_links})
        missing_resources = sorted({value for value in parser.resources
                                    if not local_resource_exists(public, page, value)})
        if missing_resources:
            findings['missing_local_resources'].append({'route': route, 'resources': missing_resources})

    fatal_keys = {
        'missing_html', 'parse_errors', 'duplicate_ids', 'h1_count',
        'headings_without_ids', 'main_count', 'article_count', 'missing_header',
        'missing_footer', 'images_without_alt',
        'missing_local_resources',
    }
    fatal_count = sum(len(findings[key]) for key in fatal_keys)
    return {
        'schemaVersion': 1,
        'upstreamSha': upstream_sha,
        'expectedPages': len(routes),
        'totals': dict(totals),
        'shellCoverage': dict(shell_counts),
        'fatalFindingCount': fatal_count,
        'findings': {key: value for key, value in sorted(findings.items())},
    }


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--public', type=Path, default=ROOT / 'public')
    parser.add_argument('--ordinary-manifest', default=ROOT / 'reports/cp6/expected-routes.json')
    parser.add_argument('--generated-manifest', default=ROOT / 'reports/cp6/expected-generated-routes.json')
    parser.add_argument('--output', type=Path, default=ROOT / 'reports/cp8/structural-audit.json')
    parser.add_argument('--candidate-provenance', type=Path, required=True)
    args = parser.parse_args(argv)
    report = audit(args.public, args.ordinary_manifest, args.generated_manifest)
    provenance = json.loads(args.candidate_provenance.read_text())
    if provenance.get('upstreamSha') != report['upstreamSha']:
        parser.error('candidate provenance upstream SHA mismatch')
    from artifact_provenance import tree_digest
    digest, file_count = tree_digest(args.public)
    if (provenance.get('publicTreeSha256') != digest or
            provenance.get('publicFileCount') != file_count):
        parser.error('candidate provenance public tree mismatch')
    report['candidateProvenance'] = provenance
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: report[key] for key in ('expectedPages', 'totals', 'shellCoverage', 'fatalFindingCount')}, indent=2))
    return 1 if report['fatalFindingCount'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
