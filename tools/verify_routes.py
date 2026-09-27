#!/usr/bin/env python3
"""Verify ordinary/generated routes and report local-reference integrity."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HREF = re.compile(r'''(?:href|src)=["']([^"'#?]+)''', re.I)


def load_manifest(path):
    return json.loads(Path(path).read_text())


def index_routes(public):
    routes = set()
    for page in public.rglob('index.html'):
        parent = page.parent.relative_to(public).as_posix().strip('/')
        routes.add('/' if not parent or parent == '.' else f'/{parent}/')
    return routes


def broken_category(url):
    if url.startswith('/api/'):
        return 'external-api-application'
    if url.startswith('/logs/logpush/'):
        return 'live-logpush-dataset'
    if url.startswith('/workers-ai/models/'):
        return 'live-or-proxied-workers-ai-model'
    return 'upstream-stale-or-unclassified'


def verify(public, ordinary_manifest, generated_manifest):
    ordinary = load_manifest(ordinary_manifest)
    generated = load_manifest(generated_manifest)
    expected_routes = set(ordinary['routes']) | {'/'} | set(generated['routes'])
    expected_static = set(generated.get('static_files', []))
    if ordinary.get('markdown_endpoints'):
        expected_static.update(route.rstrip('/') + '/index.md'
                               for route in ordinary['routes'])
    actual_routes = index_routes(public)
    missing_routes = sorted(expected_routes - actual_routes)
    missing_static = sorted(path for path in expected_static
                            if not (public / path.lstrip('/')).is_file())

    broken = []
    categories = {}
    for source in public.rglob('*.html'):
        for url in HREF.findall(source.read_text(errors='ignore')):
            if url.startswith(('http:', 'https:', 'mailto:', 'tel:', 'data:', '//',
                               'chrome:', 'blob:', 'ws:', 'wss:')):
                continue
            target = public / url.lstrip('/') if url.startswith('/') else source.parent / url
            if url.endswith('/') or target.is_dir():
                target = target / 'index.html'
            if not target.exists():
                item = (str(source.relative_to(public)), url)
                broken.append(item)
                category = broken_category(url)
                categories[category] = categories.get(category, 0) + 1

    return {
        'expected_index_routes': len(expected_routes),
        'expected_static_files': len(expected_static),
        'actual_index_routes': len(actual_routes),
        'missing_routes': missing_routes,
        'missing_static_files': missing_static,
        'broken_local_refs': broken[:500],
        'broken_count': len(broken),
        'broken_categories': categories,
    }


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--public', default=str(ROOT / 'public'))
    parser.add_argument('--ordinary-manifest',
                        default=str(ROOT / 'reports/cp6/expected-routes.json'))
    parser.add_argument('--generated-manifest',
                        default=str(ROOT / 'reports/cp6/expected-generated-routes.json'))
    parser.add_argument('--fail-broken', action='store_true',
                        help='also fail for references outside the reproduced surface')
    args = parser.parse_args(argv)
    report = verify(Path(args.public), args.ordinary_manifest, args.generated_manifest)
    print(json.dumps(report, indent=2))
    missing = report['missing_routes'] or report['missing_static_files']
    return 2 if missing or (args.fail_broken and report['broken_count']) else 0


if __name__ == '__main__':
    raise SystemExit(main())
