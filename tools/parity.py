#!/usr/bin/env python3
"""Measured DOM/layout/screenshot comparison for CP8."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit


class Structure(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = {}
        self.headings = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        self.tags[tag] = self.tags.get(tag, 0) + 1
        if tag in {'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}:
            self.headings.append(tag)

    def handle_data(self, data):
        value = ' '.join(data.split())
        if value:
            self.text.append(value)


def fetch(base, route):
    url = urljoin(base.rstrip('/') + '/', route.lstrip('/'))
    request = urllib.request.Request(url, headers={'User-Agent': 'nift-parity/2'})
    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                body = response.read().decode('utf8', 'replace')
                return {'status': response.status, 'url': response.url,
                        'bytes': len(body.encode()), 'html': body}
        except Exception:
            if attempt:
                raise


def signature(html):
    parser = Structure()
    parser.feed(html)
    text = '\n'.join(parser.text)
    return {
        'tags': dict(sorted(parser.tags.items())),
        'headings': parser.headings,
        'textSha256': hashlib.sha256(text.encode()).hexdigest(),
        'textBytes': len(text.encode()),
    }


def browser_capture(browser, base, route, viewport, output):
    context = browser.new_context(
        viewport={'width': viewport['width'], 'height': viewport['height']},
        color_scheme='light', reduced_motion='reduce', device_scale_factor=1,
    )
    context.add_init_script("localStorage.setItem('ui-mode','light')")
    page = context.new_page()
    errors = []
    failed_local = []
    failed_external = []
    bad_local_responses = []
    bad_external_responses = []
    origin = urlsplit(base).netloc

    def record_failed(request):
        target = failed_local if urlsplit(request.url).netloc == origin else failed_external
        target.append(request.url)

    def record_bad_response(response):
        if response.status < 400:
            return
        target = bad_local_responses if urlsplit(response.url).netloc == origin else bad_external_responses
        target.append({'url': response.url, 'status': response.status})

    page.on('console', lambda message: errors.append(message.text) if message.type == 'error' else None)
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.on('requestfailed', record_failed)
    page.on('response', record_bad_response)
    url = urljoin(base.rstrip('/') + '/', route.lstrip('/'))
    response = page.goto(url, wait_until='domcontentloaded', timeout=120000)
    page.wait_for_load_state('load', timeout=120000)
    page.evaluate("document.fonts && document.fonts.ready")
    page.evaluate("""async () => {
      const visibleImages = [...document.images].filter((image) => {
        const rect = image.getBoundingClientRect();
        return rect.top < innerHeight && rect.bottom > 0;
      });
      await Promise.all(visibleImages.map((image) => image.decode().catch(() => {})));
    }""")
    page.add_style_tag(content='*,*::before,*::after{animation:none!important;transition:none!important;caret-color:transparent!important}')
    probes = page.evaluate("""() => {
       const rect = (selector) => { const e=document.querySelector(selector); if(!e)return null; const r=e.getBoundingClientRect(); const s=getComputedStyle(e); return {x:Math.round(r.x),y:Math.round(r.y),width:Math.round(r.width),height:Math.round(r.height),display:s.display,flex:s.flex,flexDirection:s.flexDirection,minWidth:s.minWidth,parent:e.parentElement&&e.parentElement.className,fontSize:s.fontSize,fontWeight:s.fontWeight,lineHeight:s.lineHeight}; };
      const overflowing = [...document.querySelectorAll('body *')].filter((e) => { const r=e.getBoundingClientRect(); return r.right > document.documentElement.clientWidth + 1 || r.left < -1; }).slice(0,5).map((e) => ({tag:e.tagName.toLowerCase(),class:e.className||'',id:e.id||'',right:Math.round(e.getBoundingClientRect().right),scrollWidth:e.scrollWidth,clientWidth:e.clientWidth}));
      const main=document.querySelector('main');
      const mainText=(main?.innerText||'').trim();
       const mainWords=[...new Set((mainText.toLowerCase().match(/[a-z0-9]+/g)||[]))];
       return {header:rect('.nb-header'),pageRow:rect('.page-row'),bodyColumn:rect('.body-column'),contentRow:rect('.content-row'),mobileToc:rect('.mobile-toc'),sidebar:rect('.sidebar'),main:rect('main'),article:rect('.article-wrap'),toc:rect('.toc'),h1:rect('h1'),body:rect('body'),mainTextBytes:new TextEncoder().encode(mainText).length,mainWords,headingText:[...(main?.querySelectorAll('h1,h2,h3,h4,h5,h6')||[])].map((e)=>e.innerText.trim()),horizontalOverflow:document.documentElement.scrollWidth>document.documentElement.clientWidth,overflowing};
    }""")
    page.screenshot(path=str(output), full_page=False)
    result = {'status': response.status if response else None, 'finalUrl': page.url,
              'consoleErrors': list(errors), 'failedLocalRequests': list(failed_local),
              'failedExternalRequests': list(failed_external),
              'badLocalResponses': list(bad_local_responses),
              'badExternalResponses': list(bad_external_responses), 'probes': probes}
    context.close()
    return result


def browser_capture_with_retry(browser, base, route, viewport, output):
    for attempt in range(2):
        try:
            return browser_capture(browser, base, route, viewport, output)
        except Exception:
            if attempt:
                raise


def image_metrics(left, right):
    from PIL import Image, ImageChops, ImageStat
    first, second = Image.open(left).convert('RGB'), Image.open(right).convert('RGB')
    if first.size != second.size:
        return {'sameSize': False, 'upstreamSize': first.size, 'niftSize': second.size}
    difference = ImageChops.difference(first, second)
    histogram = difference.convert('L').histogram()
    changed = sum(histogram[1:])
    significant = sum(histogram[16:])
    pixels = first.width * first.height
    mean = sum(ImageStat.Stat(difference).mean) / 3
    return {'sameSize': True, 'changedPixelRatio': round(changed / pixels, 6),
            'significantPixelRatio': round(significant / pixels, 6),
            'meanAbsoluteChannelDelta': round(mean, 3)}


def load_sample(path):
    data = json.loads(Path(path).read_text())
    return data['routes'], data['viewports'], data.get('upstreamSha')


def parity_failures(upstream, nift, viewport, image=None):
    reasons = []
    probes = nift['probes']
    upstream_probes = upstream['probes']
    if upstream.get('status') != 200:
        reasons.append('upstream-non-200')
    if nift.get('status') != 200:
        reasons.append('nift-non-200')
    if nift['consoleErrors']:
        reasons.append('console-errors')
    if nift['failedLocalRequests']:
        reasons.append('failed-local-requests')
    if nift['badLocalResponses']:
        reasons.append('bad-local-responses')
    upstream_external_failures = set(upstream.get('failedExternalRequests') or [])
    if set(nift.get('failedExternalRequests') or []) - upstream_external_failures:
        reasons.append('nift-exclusive-external-request-failures')
    upstream_external_responses = {
        (item['url'], item['status']) for item in upstream.get('badExternalResponses') or []}
    nift_external_responses = {
        (item['url'], item['status']) for item in nift.get('badExternalResponses') or []}
    if nift_external_responses - upstream_external_responses:
        reasons.append('nift-exclusive-bad-external-responses')
    if probes['horizontalOverflow']:
        reasons.append('horizontal-overflow')
    if upstream_probes['h1'] and not probes['h1']:
        reasons.append('missing-h1')

    upstream_bytes = upstream_probes['mainTextBytes']
    nift_bytes = probes['mainTextBytes']
    if upstream_bytes >= 100 and nift_bytes / upstream_bytes < 0.65:
        reasons.append('main-text-below-65-percent')
    # Very short navigation pages are mostly shell chrome upstream, so token
    # overlap is meaningful only once the reference has substantive content.
    if upstream_bytes >= 500:
        upstream_words = set(upstream_probes.get('mainWords') or [])
        nift_words = set(probes.get('mainWords') or [])
        shared_words = upstream_words.intersection(nift_words)
        if upstream_words and len(shared_words) / len(upstream_words) < 0.55:
            reasons.append('upstream-word-coverage-below-55-percent')
        if nift_words and len(shared_words) / len(nift_words) < 0.75:
            reasons.append('nift-word-precision-below-75-percent')

    normalize_heading = lambda value: re.sub(r'^\d+\.\s*', '', value.casefold()).strip()
    upstream_headings = [normalize_heading(value) for value in upstream_probes['headingText'] if value]
    nift_headings = [normalize_heading(value) for value in probes['headingText'] if value]
    if len(upstream_headings) >= 2 and len(nift_headings) / len(upstream_headings) < 0.85:
        reasons.append('heading-count-below-85-percent')
    if len(upstream_headings) >= 3:
        shared = len(set(upstream_headings).intersection(nift_headings))
        if shared / len(set(upstream_headings)) < 0.85:
            reasons.append('heading-labels-below-85-percent')

    minimum_width = viewport['width'] * 0.45
    if not probes.get('main'):
        reasons.append('missing-main-geometry')
    for key in ('bodyColumn', 'main'):
        box = probes.get(key)
        if box and box['display'] != 'none' and box['width'] < minimum_width:
            reasons.append(f'collapsed-{key}')
    for key in ('header', 'h1', 'article'):
        upstream_box = upstream_probes.get(key)
        nift_box = probes.get(key)
        if not upstream_box or not nift_box:
            continue
        if abs(upstream_box['y'] - nift_box['y']) > 64:
            reasons.append(f'{key}-vertical-offset-above-64px')
        if key != 'h1' and abs(upstream_box['width'] - nift_box['width']) / viewport['width'] > 0.15:
            reasons.append(f'{key}-width-delta-above-15-percent')
    if image:
        if not image.get('sameSize'):
            reasons.append('screenshot-size-mismatch')
        else:
            # Raw changed pixels are diagnostic only because font anti-aliasing
            # changes nearly every white pixel. Perceptible and mean deltas gate.
            significant = image.get('significantPixelRatio', 0)
            mean_delta = image.get('meanAbsoluteChannelDelta', 0)
            if significant >= 0.20:
                reasons.append('significant-pixels-above-20-percent')
            if mean_delta >= 30:
                reasons.append('mean-channel-delta-above-30')
    return reasons


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--upstream', required=True)
    parser.add_argument('--nift', required=True)
    parser.add_argument('--sample', default='parity/cp8-sample.json')
    parser.add_argument('--out', default='reports/cp8/parity')
    parser.add_argument('--screenshots', action='store_true')
    parser.add_argument('--chromium-executable')
    parser.add_argument('--upstream-workdir', type=Path)
    parser.add_argument('--candidate-provenance', type=Path)
    parser.add_argument('--deployment-attestation', type=Path)
    parser.add_argument('--route', action='append', dest='selected_routes')
    parser.add_argument('--viewport', action='append', dest='selected_viewports')
    args = parser.parse_args(argv)
    if not args.screenshots:
        parser.error('--screenshots is required for CP8 parity verification')
    routes, viewports, upstream_sha = load_sample(args.sample)
    verified_sha = None
    if args.upstream_workdir:
        verified_sha = subprocess.check_output(
            ['git', '-C', str(args.upstream_workdir), 'rev-parse', 'HEAD'], text=True).strip()
        if verified_sha != upstream_sha:
            parser.error(f'upstream checkout {verified_sha} != sample SHA {upstream_sha}')
    from certification import validate_deployment
    candidate_provenance, deployment_attestation = validate_deployment(
        parser, args.candidate_provenance, args.deployment_attestation, args.nift, upstream_sha)
    if args.selected_routes:
        wanted = set(args.selected_routes)
        routes = [item for item in routes if item['route'] in wanted]
        missing = wanted.difference(item['route'] for item in routes)
        if missing:
            parser.error('unknown selected routes: ' + ', '.join(sorted(missing)))
    if args.selected_viewports:
        wanted = set(args.selected_viewports)
        viewports = [item for item in viewports if item['name'] in wanted]
        missing = wanted.difference(item['name'] for item in viewports)
        if missing:
            parser.error('unknown selected viewports: ' + ', '.join(sorted(missing)))
    if not routes or not viewports:
        parser.error('parity requires at least one route and one viewport')
    output = Path(args.out)
    output.mkdir(parents=True, exist_ok=True)
    rows = []
    failures = 0
    playwright = browser = None
    if args.screenshots:
        from playwright.sync_api import sync_playwright
        playwright = sync_playwright().start()
        launch = {'headless': True, 'args': ['--no-sandbox']}
        if args.chromium_executable:
            launch['executable_path'] = args.chromium_executable
        browser = playwright.chromium.launch(**launch)
    try:
        for route_index, item in enumerate(routes):
            route = item['route']
            row = {'route': route, 'reasons': item['reasons']}
            try:
                upstream = fetch(args.upstream, route)
                nift = fetch(args.nift, route)
                row['http'] = {
                    'upstream': {key: upstream[key] for key in ('status', 'url', 'bytes')},
                    'nift': {key: nift[key] for key in ('status', 'url', 'bytes')},
                }
                row['structure'] = {'upstream': signature(upstream['html']), 'nift': signature(nift['html'])}
                row['textEqual'] = row['structure']['upstream']['textSha256'] == row['structure']['nift']['textSha256']
                if upstream['status'] != 200 or nift['status'] != 200:
                    failures += 1
                if browser:
                    row['viewports'] = []
                    for viewport in viewports:
                        stem = f'{route_index:03d}-{viewport["name"]}'
                        upstream_image = output / f'{stem}-upstream.png'
                        nift_image = output / f'{stem}-nift.png'
                        upstream_browser = browser_capture_with_retry(
                            browser, args.upstream, route, viewport, upstream_image)
                        nift_browser = browser_capture_with_retry(
                            browser, args.nift, route, viewport, nift_image)
                        metrics = image_metrics(upstream_image, nift_image)
                        row['viewports'].append({'viewport': viewport, 'upstream': upstream_browser,
                                                 'nift': nift_browser, 'image': metrics})
                        viewport_failures = parity_failures(
                            upstream_browser, nift_browser, viewport, metrics)
                        row['viewports'][-1]['failures'] = viewport_failures
                        if viewport_failures:
                            failures += 1
            except Exception as exc:
                row['error'] = str(exc)
                failures += 1
            rows.append(row)
            print(route, 'ERROR' if row.get('error') else 'checked')
    finally:
        if browser:
            browser.close()
        if playwright:
            playwright.stop()
    report = {'schemaVersion': 2, 'upstreamSha': upstream_sha,
              'verifiedUpstreamSha': verified_sha, 'upstreamWorkdir': str(args.upstream_workdir) if args.upstream_workdir else None,
              'candidateProvenance': candidate_provenance,
              'deploymentAttestation': deployment_attestation,
              'upstream': args.upstream,
              'nift': args.nift, 'routeCount': len(rows), 'viewportCount': len(viewports),
              'failureCount': failures, 'routes': rows}
    (output / 'summary.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: report[key] for key in ('routeCount', 'viewportCount', 'failureCount')}, indent=2))
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
