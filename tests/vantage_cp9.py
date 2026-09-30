#!/usr/bin/env python3
"""CP9 display-backed Vantage/WebKitGTK representative browser gate."""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))

from certification import validate_deployment


ROUTES = (
    '/workers/get-started/guide/',
    '/changelog/',
    '/glossary/',
    '/sandbox/',
)


def call(vantage, *args):
    output = subprocess.check_output(
        [vantage, 'agent', *args], text=True, stderr=subprocess.PIPE)
    return json.loads(output)


def wait_for_agent(vantage, deadline):
    while time.monotonic() < deadline:
        try:
            if call(vantage, 'status').get('running'):
                return
        except (subprocess.CalledProcessError, json.JSONDecodeError):
            pass
        time.sleep(.2)
    raise RuntimeError('Vantage agent did not become ready')


def wait_for_page(vantage, tab, url, deadline):
    while time.monotonic() < deadline:
        tabs = call(vantage, 'tabs')
        current = next((item for item in tabs if item['id'] == tab), None)
        if current and current['uri'] == url and not current['loading']:
            time.sleep(.4)
            return current
        time.sleep(.2)
    raise RuntimeError(f'Vantage did not finish loading {url}')


def run(base, vantage, provenance=None, attestation=None):
    base = base.rstrip('/')
    executable = pathlib.Path(vantage).resolve()
    process = subprocess.Popen(
        [str(executable), base + ROUTES[0]],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pages = []
    fatal = []
    try:
        wait_for_agent(str(executable), time.monotonic() + 15)
        version = call(str(executable), 'version')
        capabilities = call(str(executable), 'capabilities')
        tabs = call(str(executable), 'tabs')
        if len(tabs) != 1:
            raise RuntimeError(f'expected one Vantage tab, found {len(tabs)}')
        tab = tabs[0]['id']
        for route in ROUTES:
            url = base + route
            call(str(executable), 'open', url, str(tab))
            wait_for_page(str(executable), tab, url, time.monotonic() + 20)
            state = call(str(executable), 'js', '''JSON.stringify((() => {
              const visible = element => {
                const style = getComputedStyle(element);
                return style.display !== 'none' && style.visibility !== 'hidden';
              };
              const name = element => (element.getAttribute('aria-label') ||
                element.getAttribute('title') || element.textContent || '').trim();
              const trigger = document.querySelector('[data-search-trigger]');
              trigger.focus(); trigger.click();
              const dialog = document.querySelector('[data-search-dialog]');
              const search = {open: dialog.open,
                inputFocused: document.activeElement === document.querySelector('[data-search-input]')};
              document.querySelector('[data-search-close]').click();
              search.focusReturned = document.activeElement === trigger;
              return {
                url: location.href,
                title: document.title,
                canonical: document.querySelector('link[rel="canonical"]')?.href || '',
                mainCount: document.querySelectorAll('main').length,
                h1Count: document.querySelectorAll('h1').length,
                overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
                unnamedVisibleLinks: [...document.querySelectorAll('a[href]')]
                  .filter(element => visible(element) && !name(element)).length,
                unfocusableScrollRegions: [...document.querySelectorAll('pre, .home-card code, .mermaid, .video-transcript')]
                  .filter(element => visible(element) && element.tabIndex < 0).length,
                search,
                fontFamily: getComputedStyle(document.body).fontFamily
              };
            })())''')
            snapshot = call(str(executable), 'snapshot', str(tab))
            roles = collections.Counter(item.get('role') for item in snapshot.get('elements', []))
            state['semanticRoles'] = dict(sorted(roles.items()))
            state['diagnostics'] = call(str(executable), 'diagnostics', str(tab))
            page_failures = []
            expected_canonical = 'https://developers.cloudflare.com' + route
            if state['url'] != url:
                page_failures.append('url')
            if not state['title']:
                page_failures.append('title')
            if state['canonical'] != expected_canonical:
                page_failures.append('canonical')
            if state['mainCount'] != 1:
                page_failures.append('main')
            if state['h1Count'] != 1:
                page_failures.append('h1')
            if state['overflow']:
                page_failures.append('horizontal-overflow')
            if state['unnamedVisibleLinks']:
                page_failures.append('unnamed-visible-links')
            if state['unfocusableScrollRegions']:
                page_failures.append('unfocusable-scroll-regions')
            if state['search'] != {'open': True, 'inputFocused': True, 'focusReturned': True}:
                page_failures.append('search-focus')
            if state['semanticRoles'].get('main') != 1 or not state['semanticRoles'].get('link'):
                page_failures.append('semantic-snapshot')
            if state['diagnostics'].get('events'):
                page_failures.append('diagnostics')
            state['route'] = route
            state['failures'] = page_failures
            pages.append(state)
            if page_failures:
                fatal.append({'route': route, 'failures': page_failures})
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()

    return {
        'schemaVersion': 1,
        'base': base,
        'candidateProvenance': provenance,
        'deploymentAttestation': attestation,
        'browser': {
            **version,
            'path': str(executable),
            'sha256': hashlib.sha256(executable.read_bytes()).hexdigest(),
        },
        'capabilities': capabilities,
        'routes': len(pages),
        'pages': pages,
        'fatalFindingCount': len(fatal),
        'fatalFindings': fatal,
    }


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--base', required=True)
    parser.add_argument('--vantage-executable', default='/usr/local/bin/vant')
    parser.add_argument('--candidate-provenance', type=pathlib.Path, required=True)
    parser.add_argument('--deployment-attestation', type=pathlib.Path, required=True)
    parser.add_argument('--output', type=pathlib.Path, required=True)
    args = parser.parse_args(argv)
    provenance, attestation = validate_deployment(
        parser, args.candidate_provenance, args.deployment_attestation,
        args.base, 'bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf')
    report = run(args.base, args.vantage_executable, provenance, attestation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: report[key] for key in (
        'routes', 'browser', 'fatalFindingCount', 'fatalFindings')}, indent=2))
    return 1 if report['fatalFindingCount'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
