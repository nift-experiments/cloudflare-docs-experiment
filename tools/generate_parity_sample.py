#!/usr/bin/env python3
"""Generate the deterministic CP8 browser comparison sample."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

PIN = 'bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf'
FEATURES = {
    'tabs': r'<Tabs\b',
    'package-managers': r'<PackageManagers\b',
    'details': r'<Details\b',
    'steps': r'<Steps\b',
    'cards': r'<(?:Card|CardGrid|LinkCard)\b',
    'asides': r':::(?:note|tip|caution|warning|info)',
    'tables': r'^\|.+\|$',
    'images': r'!\[[^]]*\]\(',
    'code': r'^```',
    'file-tree': r'<FileTree\b',
}
GENERATED = [
    '/directory/', '/glossary/',
    '/ruleset-engine/rules-language/fields/reference/http.cookie/',
    '/workers-ai/models/llama-3.1-8b-instruct-fp8/',
    '/changelog/', '/changelog/2/',
    '/changelog/post/2026-03-18-media-transformations-workers-binding/',
    '/agent-setup/', '/videos/app-sec-dashboard/',
]
MAJOR = ['fundamentals', 'workers', 'cloudflare-one', 'dns', 'r2', 'waf', 'ssl',
         'cache', 'realtime', 'learning-paths', 'pages', 'workers-ai']


def route_for(relative):
    value = relative.as_posix().lower().rsplit('.', 1)[0]
    if value.endswith('/index'):
        value = value[:-6]
    return '/' if value == 'index' else '/' + value.strip('/') + '/'


def rank(route, reason):
    return hashlib.sha256(f'{PIN}\0{reason}\0{route}'.encode()).hexdigest()


def generate(upstream):
    docs = upstream / 'src/content/docs'
    records = []
    for path in sorted(docs.rglob('*')):
        if path.suffix not in {'.md', '.mdx'}:
            continue
        route = route_for(path.relative_to(docs))
        records.append((route, path.read_text(errors='replace')))
    selected = {'/': {'homepage'}}

    def add(route, reason):
        selected.setdefault(route, set()).add(reason)

    for product in MAJOR:
        candidates = [route for route, _text in records if route.startswith(f'/{product}/')]
        root = f'/{product}/'
        add(root if root in candidates else min(candidates, key=lambda value: rank(value, product)), 'major-product')
    for depth in range(1, 10):
        candidates = [route for route, _text in records if len([part for part in route.split('/') if part]) == depth]
        if candidates:
            add(min(candidates, key=lambda value: rank(value, f'depth-{depth}')), f'depth-{depth}')
    for feature, pattern in FEATURES.items():
        candidates = [route for route, text in records if re.search(pattern, text, re.M)]
        if candidates:
            add(min(candidates, key=lambda value: rank(value, feature)), feature)
    for route in GENERATED:
        add(route, 'generated-family')
    return {
        'schemaVersion': 1,
        'upstreamSha': PIN,
        'selection': 'fixed major products + seeded minimum-hash depth/feature strata + generated families',
        'viewports': [
            {'name': 'mobile', 'width': 390, 'height': 844},
            {'name': 'tablet', 'width': 768, 'height': 1024},
            {'name': 'sidebar-breakpoint', 'width': 1024, 'height': 900},
            {'name': 'desktop', 'width': 1440, 'height': 1200},
        ],
        'routes': [{'route': route, 'reasons': sorted(reasons)}
                   for route, reasons in sorted(selected.items())],
    }


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('upstream', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    document = generate(args.upstream.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, indent=2) + '\n')
    print(f"selected {len(document['routes'])} routes across {len(document['viewports'])} viewports")


if __name__ == '__main__':
    main()
