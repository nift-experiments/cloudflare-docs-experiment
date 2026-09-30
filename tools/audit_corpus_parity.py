#!/usr/bin/env python3
"""Compare structural content for every manifest route across two servers."""
from __future__ import annotations

import argparse
import collections
import concurrent.futures
import hashlib
import json
import os
import re
import signal
import socket
import subprocess
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
VOID_ELEMENTS = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
                 'link', 'meta', 'param', 'source', 'track', 'wbr'}


class ContentStructure(HTMLParser):
    def __init__(self, scope_tag):
        super().__init__(convert_charrefs=True)
        self.scope_tag = scope_tag
        self.scope_depth = 0
        self.scope_count = 0
        self.ignored_depth = 0
        self.heading = None
        self.heading_text = []
        self.headings = []
        self.text = []
        self.counts = collections.Counter()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == self.scope_tag:
            if not self.scope_depth:
                self.scope_count += 1
            self.scope_depth += 1
        if self.ignored_depth:
            if tag not in VOID_ELEMENTS:
                self.ignored_depth += 1
            return
        if tag in {'script', 'style', 'noscript'} or 'data-changelog-product-nav' in attrs:
            self.ignored_depth = 1
            return
        if self.scope_depth and (tag != 'img' or (attrs.get('alt') or '').strip()):
            self.counts[tag] += 1
        if self.scope_depth and tag in {'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}:
            self.heading = tag
            self.heading_text = []

    handle_startendtag = handle_starttag

    def handle_endtag(self, tag):
        if self.ignored_depth:
            self.ignored_depth -= 1
            return
        if tag == self.heading:
            value = ' '.join(self.heading_text).strip()
            self.headings.append((tag, value))
            self.heading = None
            self.heading_text = []
        if tag == self.scope_tag and self.scope_depth:
            self.scope_depth -= 1

    def handle_data(self, data):
        if not self.scope_depth or self.ignored_depth:
            return
        value = ' '.join(data.split())
        if value:
            self.text.append(value)
            if self.heading:
                self.heading_text.append(value)


def normalize_heading(value):
    value = re.sub(r'^\d+\.\s*', '', value.casefold()).strip()
    return ' '.join(re.findall(r'[a-z0-9]+', value))


def vocabulary(text):
    # Standalone dates, counters, and generated numeric IDs are not vocabulary.
    return sorted({token for token in re.findall(r'[a-z0-9]+', text.casefold())
                   if re.search(r'[a-z]', token)})


def parse_html(body):
    main_parser = ContentStructure('main')
    article_parser = ContentStructure('article')
    main_parser.feed(body)
    article_parser.feed(body)
    # A single outer article is the semantic document body. Multiple peer
    # articles are usually cards on a splash page, where main is the content.
    parser = article_parser if article_parser.scope_count == 1 else main_parser
    text = ' '.join(parser.text)
    return {
        'mainCount': main_parser.scope_count,
        'words': vocabulary(text),
        'headings': [(level, normalize_heading(value)) for level, value in parser.headings],
        'elements': {tag: parser.counts[tag] for tag in ('table', 'pre', 'img', 'iframe')},
    }


def parse_text(body):
    # Link destinations vary with the serving origin and are not reader-visible
    # prose. Compare labels and text without counting host/path tokens.
    body = re.sub(r'\]\([^)]*\)', ']', body)
    body = re.sub(r'https?://\S+', '', body)
    return {'words': vocabulary(body)}


def longest_common_subsequence(left, right):
    row = [0] * (len(right) + 1)
    for left_value in left:
        previous = 0
        for index, right_value in enumerate(right, 1):
            saved = row[index]
            if left_value == right_value:
                row[index] = previous + 1
            else:
                row[index] = max(row[index], row[index - 1])
            previous = saved
    return row[-1]


def compare(upstream, nift):
    reasons = []
    if upstream['status'] != 200:
        reasons.append('upstream-non-200')
    if nift['status'] != 200:
        reasons.append('nift-non-200')
    if upstream['kind'] != nift['kind']:
        reasons.append('response-kind-mismatch')
    if reasons:
        return reasons

    if upstream['kind'] == 'text':
        upstream_words = set(upstream['structure']['words'])
        nift_words = set(nift['structure']['words'])
        if len(upstream_words) >= 20:
            shared = upstream_words.intersection(nift_words)
            if len(shared) / len(upstream_words) < 0.75:
                reasons.append('upstream-text-word-coverage-below-75-percent')
            if len(shared) / max(1, len(nift_words)) < 0.75:
                reasons.append('text-word-precision-below-75-percent')
        return reasons
    if upstream['kind'] != 'html':
        return reasons

    upstream_structure = upstream['structure']
    nift_structure = nift['structure']
    if upstream_structure['mainCount'] and not nift_structure['mainCount']:
        reasons.append('missing-main')

    upstream_words = set(upstream_structure['words'])
    nift_words = set(nift_structure['words'])
    if len(upstream_words) >= 80:
        shared = upstream_words.intersection(nift_words)
        if len(shared) / len(upstream_words) < 0.7:
            reasons.append('upstream-word-coverage-below-70-percent')
        if len(shared) / max(1, len(nift_words)) < 0.7:
            reasons.append('word-precision-below-70-percent')

    upstream_headings = upstream_structure['headings']
    nift_headings = nift_structure['headings']
    if len(upstream_headings) >= 3:
        if longest_common_subsequence(upstream_headings, nift_headings) / len(upstream_headings) < 0.7:
            reasons.append('heading-order-coverage-below-70-percent')

    for tag, count in upstream_structure['elements'].items():
        if count and nift_structure['elements'][tag] / count < 0.5:
            reasons.append(f'{tag}-count-below-50-percent')
    return reasons


def fetch_once(base, route, timeout):
    url = urljoin(base.rstrip('/') + '/', route.lstrip('/'))
    request = urllib.request.Request(url, headers={'User-Agent': 'nift-corpus-parity/1'})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body_bytes = response.read()
            content_type = response.headers.get_content_type()
            body = body_bytes.decode('utf8', 'replace')
            if content_type == 'text/html' or '<html' in body[:1000].casefold():
                kind = 'html'
            elif content_type.startswith('text/'):
                kind = 'text'
            else:
                kind = 'other'
            return {
                'status': response.status,
                'kind': kind,
                'bytes': len(body_bytes),
                'structure': (parse_html(body) if kind == 'html' else
                              parse_text(body) if kind == 'text' else None),
            }
    except urllib.error.HTTPError as error:
        return {'status': error.code, 'kind': 'error', 'bytes': 0, 'structure': None}
    except Exception as error:
        return {'status': None, 'kind': 'error', 'bytes': 0, 'structure': None,
                'error': str(error)}


def fetch(base, route, timeout):
    result = None
    for attempt in range(3):
        result = fetch_once(base, route, timeout)
        if result['status'] == 200:
            return result
        if attempt < 2:
            time.sleep(1)
    return result


def load_routes(ordinary_manifest, generated_manifest):
    ordinary = json.loads(Path(ordinary_manifest).read_text())['routes']
    generated_manifest = json.loads(Path(generated_manifest).read_text())
    generated = generated_manifest['routes']
    text_routes = generated_manifest.get('text_routes', [])
    return sorted(set(ordinary) | {'/'} | set(generated) | set(text_routes))


def stale_classification_routes(classifications, finding_routes):
    return sorted(
        route for route, disposition in classifications.items()
        if route not in finding_routes and disposition.get('required', True))


def check_route(route, upstream_base, nift_base, timeout):
    upstream = fetch(upstream_base, route, timeout)
    nift = fetch(nift_base, route, timeout)
    return route, upstream, nift, compare(upstream, nift)


def stop_process(process):
    if process.poll() is not None:
        return
    os.killpg(process.pid, signal.SIGTERM)
    try:
        process.wait(timeout=30)
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGKILL)
        process.wait(timeout=30)


def start_astro(workdir, upstream_base, timeout):
    parsed = urlsplit(upstream_base)
    executable = Path(workdir) / 'node_modules/.bin/astro'
    subprocess.run([str(executable), 'dev', 'stop'], cwd=workdir,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    environment = os.environ.copy()
    environment['ASTRO_DEV_BACKGROUND'] = '0'
    process = subprocess.Popen(
        [str(executable), 'dev', '--host', parsed.hostname or '127.0.0.1',
         '--port', str(parsed.port or 4321)],
        cwd=workdir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        env=environment, start_new_session=True,
    )
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError('Astro reference server exited during startup')
        try:
            with socket.create_connection((parsed.hostname or '127.0.0.1', parsed.port or 4321), timeout=2):
                return process
        except OSError:
            time.sleep(1)
    stop_process(process)
    raise RuntimeError('Astro reference server did not become ready')


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--upstream', required=True)
    parser.add_argument('--nift', required=True)
    parser.add_argument('--ordinary-manifest', default=ROOT / 'reports/cp6/expected-routes.json')
    parser.add_argument('--generated-manifest', default=ROOT / 'reports/cp6/expected-generated-routes.json')
    parser.add_argument('--output', type=Path, default=ROOT / 'reports/cp8/corpus-parity.json')
    parser.add_argument('--workers', type=int, default=8)
    parser.add_argument('--timeout', type=int, default=60)
    parser.add_argument('--route', action='append', dest='selected_routes')
    parser.add_argument('--retry-report', type=Path)
    parser.add_argument('--astro-workdir', type=Path)
    parser.add_argument('--restart-upstream-every', type=int, default=500)
    parser.add_argument('--checkpoint-every', type=int, default=250)
    parser.add_argument('--resume', action='store_true')
    parser.add_argument('--classifications', type=Path)
    parser.add_argument('--candidate-provenance', type=Path)
    parser.add_argument('--deployment-attestation', type=Path)
    args = parser.parse_args(argv)
    if args.checkpoint_every < 1:
        parser.error('--checkpoint-every must be positive')

    ordinary_data = json.loads(Path(args.ordinary_manifest).read_text())
    generated_data = json.loads(Path(args.generated_manifest).read_text())
    manifest_sha = ordinary_data.get('upstream_sha')
    if not manifest_sha or generated_data.get('upstream_sha') != manifest_sha:
        parser.error('ordinary/generated manifest upstream SHA mismatch')
    verified_sha = None
    if args.astro_workdir:
        verified_sha = subprocess.check_output(
            ['git', '-C', str(args.astro_workdir), 'rev-parse', 'HEAD'], text=True).strip()
        if verified_sha != manifest_sha:
            parser.error(f'upstream checkout {verified_sha} != manifest SHA {manifest_sha}')
    from certification import validate_deployment
    candidate_provenance, deployment_attestation = validate_deployment(
        parser, args.candidate_provenance, args.deployment_attestation, args.nift, manifest_sha)

    routes = load_routes(args.ordinary_manifest, args.generated_manifest)
    if args.retry_report:
        retry_report = json.loads(args.retry_report.read_text())
        retry_routes = {finding['route'] for finding in retry_report.get('findings', [])}
        routes = [route for route in routes if route in retry_routes]
    if args.selected_routes:
        selected = set(args.selected_routes)
        routes = [route for route in routes if route in selected]
        missing = selected - set(routes)
        if missing:
            parser.error('unknown selected routes: ' + ', '.join(sorted(missing)))
    if not routes:
        parser.error('route selection is empty')

    total_routes = len(routes)
    route_digest = hashlib.sha256('\n'.join(routes).encode()).hexdigest()
    findings = []
    checked = 0
    if args.resume and args.output.is_file():
        checkpoint = json.loads(args.output.read_text())
        if checkpoint.get('routeCount') != total_routes:
            parser.error('resume report route count does not match current manifests')
        if checkpoint.get('routeDigest') != route_digest:
            parser.error('resume report route list does not match current manifests')
        checked = checkpoint.get('checkedRouteCount', 0)
        findings = checkpoint.get('findings', [])
        routes = routes[checked:]
        action = 'reclassifying' if checked == total_routes else 'resuming'
        print(f'{action} at {checked}/{total_routes}; findings={len(findings)}', flush=True)
    batch_size = args.restart_upstream_every if args.astro_workdir else len(routes)
    for offset in range(0, len(routes), batch_size):
        astro_process = start_astro(args.astro_workdir, args.upstream, args.timeout) if args.astro_workdir else None
        batch = routes[offset:offset + batch_size]
        try:
            for checkpoint_offset in range(0, len(batch), args.checkpoint_every):
                checkpoint_batch = batch[
                    checkpoint_offset:checkpoint_offset + args.checkpoint_every]
                if astro_process and astro_process.poll() is not None:
                    astro_process = start_astro(
                        args.astro_workdir, args.upstream, args.timeout)
                for attempt in range(2):
                    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
                        futures = [executor.submit(
                            check_route, route, args.upstream, args.nift, args.timeout)
                            for route in checkpoint_batch]
                        results = [future.result()
                                   for future in concurrent.futures.as_completed(futures)]
                    failed_upstream = sum(result[1]['status'] != 200 for result in results)
                    if astro_process and attempt == 0 and failed_upstream:
                        stop_process(astro_process)
                        astro_process = start_astro(
                            args.astro_workdir, args.upstream, args.timeout)
                        continue
                    break
                for route, upstream, nift, reasons in results:
                    checked += 1
                    if reasons:
                        findings.append({'route': route, 'reasons': reasons,
                                         'upstream': upstream, 'nift': nift})
                print(f'checked {checked}/{total_routes}; findings={len(findings)}', flush=True)
                checkpoint = {
                    'schemaVersion': 1,
                    'upstreamSha': manifest_sha,
                    'verifiedUpstreamSha': verified_sha,
                    'candidateProvenance': candidate_provenance,
                    'deploymentAttestation': deployment_attestation,
                    'complete': checked == total_routes,
                    'routeCount': total_routes,
                    'routeDigest': route_digest,
                    'checkedRouteCount': checked,
                    'findingCount': len(findings),
                    'findings': sorted(findings, key=lambda item: item['route']),
                }
                args.output.parent.mkdir(parents=True, exist_ok=True)
                args.output.write_text(json.dumps(checkpoint, indent=2) + '\n')
        finally:
            if astro_process:
                stop_process(astro_process)

    report = {
        'schemaVersion': 1,
        'upstreamSha': manifest_sha,
        'verifiedUpstreamSha': verified_sha,
        'candidateProvenance': candidate_provenance,
        'deploymentAttestation': deployment_attestation,
        'complete': True,
        'routeCount': total_routes,
        'routeDigest': route_digest,
        'checkedRouteCount': checked,
        'findingCount': len(findings),
        'findings': sorted(findings, key=lambda item: item['route']),
    }
    classifications = {}
    if args.classifications:
        classification_data = json.loads(args.classifications.read_text())
        if classification_data.get('upstreamSha') != manifest_sha:
            parser.error('classification upstream SHA mismatch')
        classifications = classification_data.get('routes', {})
    classified_count = 0
    for finding in report['findings']:
        disposition = classifications.get(finding['route'])
        if disposition and set(finding['reasons']) == set(disposition.get('reasons', [])):
            finding['disposition'] = disposition
            classified_count += 1
    finding_routes = {finding['route'] for finding in report['findings']}
    stale_classifications = stale_classification_routes(classifications, finding_routes)
    report['classifiedFindingCount'] = classified_count
    report['unclassifiedFindingCount'] = len(findings) - classified_count
    report['staleClassificationRoutes'] = stale_classifications
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: report[key] for key in (
        'routeCount', 'findingCount', 'classifiedFindingCount', 'unclassifiedFindingCount')}, indent=2))
    return 1 if report['unclassifiedFindingCount'] or stale_classifications else 0


if __name__ == '__main__':
    raise SystemExit(main())
