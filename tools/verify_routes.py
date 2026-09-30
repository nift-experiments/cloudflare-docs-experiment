#!/usr/bin/env python3
"""Verify ordinary/generated routes and report local-reference integrity."""
import argparse
import functools
import json
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFERENCE_CLASSIFICATIONS = ROOT / 'parity/cp8-reference-classifications.json'


class ReferenceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, _tag, attrs):
        for name, value in attrs:
            if name in ('href', 'src') and value and not value.startswith(('#', '?')):
                self.urls.append(value.split('#', 1)[0].split('?', 1)[0])


@functools.lru_cache(maxsize=1)
def reference_classifications():
    if not REFERENCE_CLASSIFICATIONS.is_file():
        return {}
    return json.loads(REFERENCE_CLASSIFICATIONS.read_text())


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
    classifications = reference_classifications()
    if url in classifications.get('liveLogpushRoutes', []):
        return 'live-logpush-dataset'
    if url in classifications.get('liveOrProxiedWorkersAiModelRoutes', []):
        return 'live-or-proxied-workers-ai-model'
    if url in classifications.get('routes', []):
        return 'upstream-stale-reference'
    return 'unclassified-broken-reference'


def verify(public, ordinary_manifest, generated_manifest):
    ordinary = load_manifest(ordinary_manifest)
    generated = load_manifest(generated_manifest)
    upstream_sha = ordinary.get('upstream_sha')
    if not upstream_sha or generated.get('upstream_sha') != upstream_sha:
        raise RuntimeError('ordinary/generated manifest upstream SHA mismatch')
    reference_data = reference_classifications()
    if reference_data.get('upstreamSha') != upstream_sha:
        raise RuntimeError('reference classification upstream SHA mismatch')
    expected_routes = set(ordinary['routes']) | {'/'} | set(generated['routes'])
    expected_static = set(generated.get('static_files', []))
    if ordinary.get('markdown_endpoints'):
        expected_static.update(route.rstrip('/') + '/index.md'
                               for route in ordinary['routes'])
    actual_routes = index_routes(public)
    missing_routes = sorted(expected_routes - actual_routes)
    unexpected_routes = sorted(actual_routes - expected_routes)
    missing_static = sorted(path for path in expected_static
                            if not (public / path.lstrip('/')).is_file())

    broken = []
    categories = {}
    unclassified = []
    for source in public.rglob('*.html'):
        parser = ReferenceParser()
        parser.feed(source.read_text(errors='ignore'))
        for url in parser.urls:
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
                if category == 'unclassified-broken-reference':
                    unclassified.append(item)
    navigation = public / 'assets/navigation'
    navigation_sources = list(navigation.glob('*.json')) if navigation.is_dir() else []
    root_navigation = public / 'assets/navigation.json'
    if root_navigation.is_file():
        navigation_sources.append(root_navigation)
    for source in navigation_sources:
        data = json.loads(source.read_text())
        stack = [data]
        while stack:
            value = stack.pop()
            if isinstance(value, dict):
                href = value.get('href')
                if isinstance(href, str) and href.startswith('/') and not href.startswith('/api/'):
                    url = href.split('#', 1)[0].split('?', 1)[0]
                    target = public / url.lstrip('/')
                    target = target / 'index.html' if url.endswith('/') or target.is_dir() else target
                    if not target.exists():
                        item = (str(source.relative_to(public)), url)
                        broken.append(item)
                        category = broken_category(url)
                        categories[category] = categories.get(category, 0) + 1
                        if category == 'unclassified-broken-reference':
                            unclassified.append(item)
                stack.extend(value.values())
            elif isinstance(value, list):
                stack.extend(value)

    return {
        'upstream_sha': upstream_sha,
        'expected_index_routes': len(expected_routes),
        'expected_static_files': len(expected_static),
        'actual_index_routes': len(actual_routes),
        'missing_routes': missing_routes,
        'unexpected_routes': unexpected_routes,
        'missing_static_files': missing_static,
        'broken_local_refs': broken[:500],
        'broken_count': len(broken),
        'broken_categories': categories,
        'unclassified_broken_refs': unclassified,
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
    parser.add_argument('--candidate-provenance', type=Path)
    args = parser.parse_args(argv)
    report = verify(Path(args.public), args.ordinary_manifest, args.generated_manifest)
    if args.candidate_provenance:
        provenance = json.loads(args.candidate_provenance.read_text())
        if provenance.get('upstreamSha') != report['upstream_sha']:
            parser.error('candidate provenance upstream SHA mismatch')
        from artifact_provenance import tree_digest
        digest, file_count = tree_digest(Path(args.public))
        if (provenance.get('publicTreeSha256') != digest or
                provenance.get('publicFileCount') != file_count):
            parser.error('candidate provenance public tree mismatch')
        report['candidateProvenance'] = provenance
    print(json.dumps(report, indent=2))
    missing = (report['missing_routes'] or report['unexpected_routes'] or
               report['missing_static_files'] or
               report['broken_categories'].get('unclassified-broken-reference'))
    return 2 if missing or (args.fail_broken and report['broken_count']) else 0


if __name__ == '__main__':
    raise SystemExit(main())
