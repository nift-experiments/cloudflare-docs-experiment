#!/usr/bin/env python3
"""CP9 Chromium accessibility, keyboard, and responsive-boundary gates."""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))

from certification import validate_deployment

AXE_CORE_VERSION = '4.10.3'
AXE_SCRIPT_SHA256 = '880970c081707360e64f34cea25ff91892f5bc95675b0776925b9709dd8a68bb'
SAMPLE_SHA256 = '27b4a4d415e584bbc8836f4aebc39371278d3ac76455ecb0e2c0c98e3eabb20a'
SAMPLE_ROUTE_COUNT = 41


def executable_identity(path):
    executable = pathlib.Path(path).absolute()
    payload = pathlib.Path('/snap/chromium/current/usr/lib/chromium-browser/chrome')
    if executable != pathlib.Path('/snap/bin/chromium') or not payload.is_file():
        payload = executable.resolve()
    version = subprocess.check_output([str(executable), '--version'], text=True).strip()
    return {'path': str(executable), 'resolvedPath': str(executable.resolve()),
            'version': version,
            'launcherSha256': hashlib.sha256(executable.read_bytes()).hexdigest(),
            'payloadPath': str(payload),
            'sha256': hashlib.sha256(payload.read_bytes()).hexdigest()}


def load_sample_routes(sample_path):
    raw = sample_path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != SAMPLE_SHA256:
        raise RuntimeError('accessibility sample SHA-256 mismatch')
    sample = json.loads(raw)
    routes = [entry['route'] for entry in sample['routes']]
    if len(routes) != SAMPLE_ROUTE_COUNT or len(set(routes)) != SAMPLE_ROUTE_COUNT:
        raise RuntimeError('accessibility sample route count or uniqueness mismatch')
    return routes


def run(base, sample_path, axe_script, chromium_executable, provenance=None,
        attestation=None):
    from playwright.sync_api import expect, sync_playwright

    routes = load_sample_routes(sample_path)
    axe_source = axe_script.read_text()
    if 'axe.run' not in axe_source:
        raise RuntimeError('axe script does not contain axe.run')
    axe_digest = hashlib.sha256(axe_source.encode()).hexdigest()
    if axe_digest != AXE_SCRIPT_SHA256:
        raise RuntimeError(f'axe-core {AXE_CORE_VERSION} script SHA-256 mismatch')
    base = base.rstrip('/')
    browser_identity = executable_identity(chromium_executable)
    console_errors = []
    violations = []
    advisories = []
    checks = []
    boundaries = []

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True, executable_path=chromium_executable,
            args=['--no-sandbox', f'--unsafely-treat-insecure-origin-as-secure={base}'])
        context = browser.new_context(viewport={'width': 1440, 'height': 1000})
        page = context.new_page()
        page.on('console', lambda message: console_errors.append(message.text)
                if message.type == 'error' else None)
        page.on('pageerror', lambda error: console_errors.append(str(error)))

        for route in routes:
            response = page.goto(base + route, wait_until='networkidle')
            if not response or response.status != 200:
                raise AssertionError(f'{route}: expected HTTP 200')
            page.add_script_tag(content=axe_source)
            result = page.evaluate('''async () => await axe.run(document, {
              runOnly: {type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']}
            })''')
            for violation in result['violations']:
                item = {
                    'route': route,
                    'id': violation['id'],
                    'impact': violation['impact'],
                    'description': violation['description'],
                    'nodes': [node['target'] for node in violation['nodes']],
                }
                violations.append(item)
        checks.append(f'axe WCAG A/AA on {len(routes)} routes')

        page.goto(base + '/workers/get-started/guide/', wait_until='networkidle')
        page.locator('body').press('Tab')
        expect(page.locator('.skip')).to_be_focused()
        expect(page.locator('.skip')).to_be_visible()
        page.locator('.skip').press('Enter')
        expect(page.locator('#main-content')).to_be_focused()
        checks.append('skip link focus/activation')

        trigger = page.locator('[data-search-trigger]')
        trigger.focus()
        page.keyboard.press('Control+k')
        expect(page.locator('[data-search-dialog]')).to_be_visible()
        expect(page.locator('[data-search-input]')).to_be_focused()
        page.keyboard.press('Escape')
        expect(page.locator('[data-search-dialog]')).not_to_be_visible()
        expect(trigger).to_be_focused()
        checks.append('search dialog focus/escape/return')

        page.goto(base + '/sandbox/', wait_until='networkidle')
        tabs = page.locator('[data-nb-tabs]').first
        tab_items = tabs.locator('[role="tab"]')
        if tab_items.count() < 2:
            raise AssertionError('/sandbox/: expected a tablist with at least two tabs')
        tab_items.first.focus()
        tab_items.first.press('End')
        expect(tab_items.last).to_be_focused()
        tab_items.last.press('Home')
        expect(tab_items.first).to_be_focused()
        tab_items.first.press('ArrowLeft')
        expect(tab_items.last).to_be_focused()
        checks.append('tablist Home/End/Arrow keyboard behavior')

        for width in (639, 640, 700, 701, 1023, 1024, 1439, 1440):
            boundary = browser.new_context(viewport={'width': width, 'height': 900})
            boundary_page = boundary.new_page()
            boundary_page.goto(base + '/workers/get-started/guide/', wait_until='networkidle')
            state = boundary_page.evaluate('''() => ({
              overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
              topNav: getComputedStyle(document.querySelector('.top-nav')).display,
              menu: getComputedStyle(document.querySelector('[data-menu-btn]')).display,
              sidebar: getComputedStyle(document.querySelector('[data-sidebar-home]')).display
            })''')
            state['width'] = width
            if state['overflow']:
                raise AssertionError(f'horizontal overflow at {width}px')
            if width <= 700 and state['topNav'] != 'none':
                raise AssertionError(f'top navigation visible at {width}px')
            if width <= 700 and state['menu'] == 'none':
                raise AssertionError(f'mobile menu hidden at {width}px')
            if 701 <= width <= 1023 and state['topNav'] == 'none':
                raise AssertionError(f'top navigation hidden at {width}px')
            if width > 700 and state['menu'] != 'none':
                raise AssertionError(f'mobile menu visible at {width}px')
            if width < 1024 and state['sidebar'] != 'none':
                raise AssertionError(f'desktop sidebar visible at {width}px')
            if width >= 1024 and state['sidebar'] == 'none':
                raise AssertionError(f'desktop sidebar hidden at {width}px')
            boundaries.append(state)
            boundary.close()
        checks.append('responsive boundary matrix')
        context.close()
        browser.close()

    report = {
        'schemaVersion': 1,
        'base': base,
        'candidateProvenance': provenance,
        'deploymentAttestation': attestation,
        'browser': browser_identity,
        'axeCoreVersion': AXE_CORE_VERSION,
        'axeScriptSha256': axe_digest,
        'routes': len(routes),
        'checks': checks,
        'boundaries': boundaries,
        'fatalViolationCount': len(violations),
        'violations': violations,
        'advisories': advisories,
        'consoleErrors': console_errors,
    }
    if console_errors:
        report['fatalViolationCount'] += len(console_errors)
    return report


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--base', required=True)
    parser.add_argument('--sample', type=pathlib.Path, default=ROOT / 'parity/cp8-sample.json')
    parser.add_argument('--axe-script', type=pathlib.Path, required=True)
    parser.add_argument('--chromium-executable', required=True)
    parser.add_argument('--candidate-provenance', type=pathlib.Path, required=True)
    parser.add_argument('--deployment-attestation', type=pathlib.Path, required=True)
    parser.add_argument('--output', type=pathlib.Path, required=True)
    args = parser.parse_args(argv)
    provenance, attestation = validate_deployment(
        parser, args.candidate_provenance, args.deployment_attestation,
        args.base, 'bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf')
    report = run(args.base, args.sample, args.axe_script,
                 args.chromium_executable, provenance, attestation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: report[key] for key in (
        'routes', 'checks', 'fatalViolationCount', 'consoleErrors')}, indent=2))
    return 1 if report['fatalViolationCount'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
