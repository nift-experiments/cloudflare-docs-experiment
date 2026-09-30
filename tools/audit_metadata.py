#!/usr/bin/env python3
"""Fail-closed CP9 metadata and sitemap audit for every generated HTML page."""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))

from artifact_provenance import tree_digest
from audit_structure import expected_pages, output_path
from page_metadata import DEFAULT_DESCRIPTION, ORIGIN


class HeadParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_head = False
        self.in_title = False
        self.title_parts = []
        self.titles = []
        self.meta = []
        self.links = []
        self.script_type = None
        self.script_parts = []
        self.json_ld = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'head':
            self.in_head = True
        if not self.in_head:
            return
        if tag == 'title':
            self.in_title = True
            self.title_parts = []
        elif tag == 'meta':
            self.meta.append(attrs)
        elif tag == 'link':
            self.links.append(attrs)
        elif tag == 'script':
            self.script_type = attrs.get('type')
            self.script_parts = []

    handle_startendtag = handle_starttag

    def handle_data(self, data):
        if self.in_title:
            self.title_parts.append(data)
        if self.script_type == 'application/ld+json':
            self.script_parts.append(data)

    def handle_endtag(self, tag):
        if tag == 'title' and self.in_title:
            self.titles.append(''.join(self.title_parts).strip())
            self.in_title = False
        elif tag == 'script' and self.script_type:
            if self.script_type == 'application/ld+json':
                self.json_ld.append(''.join(self.script_parts))
            self.script_type = None
            self.script_parts = []
        elif tag == 'head':
            self.in_head = False


def _values(items, key, value, content='content'):
    return [item.get(content, '') for item in items if item.get(key) == value]


def _local_alternate_exists(public, href):
    parsed = urlsplit(href)
    if parsed.netloc and parsed.netloc != 'developers.cloudflare.com':
        return True
    return (public / unquote(parsed.path).lstrip('/')).is_file()


def audit(public, ordinary_manifest, generated_manifest):
    ordinary = json.loads(Path(ordinary_manifest).read_text())
    generated = json.loads(Path(generated_manifest).read_text())
    upstream_sha = ordinary.get('upstream_sha')
    if not upstream_sha or generated.get('upstream_sha') != upstream_sha:
        raise RuntimeError('ordinary/generated manifest upstream SHA mismatch')
    routes = expected_pages(ordinary_manifest, generated_manifest)
    findings = collections.defaultdict(list)
    totals = collections.Counter()
    indexed_routes = set()

    sitemap_index = public / 'sitemap-index.xml'
    sitemap_chunk = public / 'sitemap-0.xml'
    if not sitemap_index.is_file() or not sitemap_chunk.is_file():
        findings['sitemap_missing'].append('/sitemap-index.xml or /sitemap-0.xml')
    else:
        try:
            index_root = ET.parse(sitemap_index).getroot()
            index_locs = [node.text for node in index_root.findall('.//{*}loc')]
            if index_locs != [ORIGIN + '/sitemap-0.xml']:
                findings['sitemap_index'].append(index_locs)
            chunk_root = ET.parse(sitemap_chunk).getroot()
            for node in chunk_root.findall('.//{*}loc'):
                if node.text and node.text.startswith(ORIGIN):
                    indexed_routes.add(urlsplit(node.text).path)
        except (ET.ParseError, OSError) as exc:
            findings['sitemap_parse'].append(str(exc))
    robots = public / 'robots.txt'
    if not robots.is_file() or f'Sitemap: {ORIGIN}/sitemap-index.xml' not in robots.read_text():
        findings['robots_sitemap'].append('/robots.txt')

    for route in routes:
        page = output_path(public, route)
        if not page.is_file():
            findings['missing_html'].append(route)
            continue
        parsed = HeadParser()
        try:
            parsed.feed(page.read_text(errors='replace'))
        except Exception as exc:
            findings['parse_errors'].append({'route': route, 'error': str(exc)})
            continue
        totals['pages'] += 1
        if len(parsed.titles) != 1 or not parsed.titles[0]:
            findings['title'].append({'route': route, 'values': parsed.titles})
        canonicals = _values(parsed.links, 'rel', 'canonical', 'href')
        if len(canonicals) != 1 or not canonicals[0].startswith(ORIGIN + '/'):
            findings['canonical'].append({'route': route, 'values': canonicals})
            canonical = None
        else:
            canonical = canonicals[0]
        sitemap_links = _values(parsed.links, 'rel', 'sitemap', 'href')
        if sitemap_links != ['/sitemap-index.xml']:
            findings['sitemap_link'].append({'route': route, 'values': sitemap_links})
        descriptions = _values(parsed.meta, 'name', 'description')
        og_descriptions = _values(parsed.meta, 'property', 'og:description')
        if descriptions != og_descriptions:
            findings['description_mismatch'].append(
                {'route': route, 'description': descriptions, 'og': og_descriptions})
        if descriptions == [DEFAULT_DESCRIPTION]:
            findings['invented_generic_description'].append(route)
        required_meta = {
            'og:title': _values(parsed.meta, 'property', 'og:title'),
            'og:type': _values(parsed.meta, 'property', 'og:type'),
            'og:site_name': _values(parsed.meta, 'property', 'og:site_name'),
            'og:locale': _values(parsed.meta, 'property', 'og:locale'),
            'og:url': _values(parsed.meta, 'property', 'og:url'),
            'og:image': _values(parsed.meta, 'property', 'og:image'),
            'twitter:card': _values(parsed.meta, 'name', 'twitter:card'),
            'twitter:site': _values(parsed.meta, 'name', 'twitter:site'),
            'twitter:image': _values(parsed.meta, 'property', 'twitter:image'),
        }
        invalid = {key: values for key, values in required_meta.items()
                   if len(values) != 1 or not values[0]}
        if invalid:
            findings['social_metadata'].append({'route': route, 'invalid': invalid})
        expected_page_url = ORIGIN + route
        if required_meta['og:url'] != [expected_page_url]:
            findings['og_url'].append({'route': route, 'values': required_meta['og:url']})
        robots_values = _values(parsed.meta, 'name', 'robots')
        robots_tokens = {
            token.lower()
            for value in robots_values
            for token in re.split(r'[\s,]+', value)
            if token
        }
        noindex = 'noindex' in robots_tokens
        if len(robots_values) > 1:
            findings['robots_metadata'].append({'route': route, 'values': robots_values})
        if noindex and parsed.json_ld:
            findings['noindex_json_ld'].append(route)
        if noindex:
            totals['noindex_pages'] += 1
        else:
            if len(parsed.json_ld) != 1:
                findings['json_ld_count'].append({'route': route, 'count': len(parsed.json_ld)})
            for raw in parsed.json_ld:
                try:
                    data = json.loads(raw)
                except json.JSONDecodeError as exc:
                    findings['json_ld_parse'].append({'route': route, 'error': str(exc)})
                    continue
                if (data.get('@context') != 'https://schema.org' or
                        data.get('url') != canonical or
                        data.get('@id') != f'{canonical}#page' or
                        data.get('headline') != (parsed.titles[0] if parsed.titles else None)):
                    findings['json_ld_contract'].append(route)
        markdown_links = [link.get('href', '') for link in parsed.links
                          if link.get('rel') == 'alternate' and
                          link.get('type') == 'text/markdown']
        missing_markdown = [href for href in markdown_links
                            if not _local_alternate_exists(public, href)]
        if missing_markdown:
            findings['missing_markdown_alternate'].append(
                {'route': route, 'values': missing_markdown})
        excluded = noindex or '/style-guide/' in route or route.endswith('/404/')
        if excluded and route in indexed_routes:
            findings['sitemap_includes_excluded'].append(route)
        if not excluded and route not in indexed_routes:
            findings['sitemap_omits_page'].append(route)

    unexpected_sitemap = sorted(indexed_routes - set(routes))
    if unexpected_sitemap:
        findings['sitemap_unexpected'].extend(unexpected_sitemap)
    fatal_count = sum(len(values) for values in findings.values())
    return {
        'schemaVersion': 1,
        'upstreamSha': upstream_sha,
        'expectedPages': len(routes),
        'totals': dict(totals),
        'sitemapRoutes': len(indexed_routes),
        'fatalFindingCount': fatal_count,
        'findings': {key: value for key, value in sorted(findings.items())},
    }


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--public', type=Path, default=ROOT / 'public')
    parser.add_argument('--ordinary-manifest', default=ROOT / 'reports/cp6/expected-routes.json')
    parser.add_argument('--generated-manifest', default=ROOT / 'reports/cp6/expected-generated-routes.json')
    parser.add_argument('--output', type=Path, default=ROOT / 'reports/cp9/metadata.json')
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
        'expectedPages', 'totals', 'sitemapRoutes', 'fatalFindingCount')}, indent=2))
    return 1 if report['fatalFindingCount'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
