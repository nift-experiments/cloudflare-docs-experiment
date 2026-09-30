#!/usr/bin/env python3
"""CP7 browser interaction smoke tests against an already-built public tree."""
from __future__ import annotations

import argparse
import functools
import http.server
import json
import pathlib
import threading

from playwright.sync_api import expect, sync_playwright


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, _format, *_args):
        pass


def run(public: pathlib.Path | None, base: str | None = None,
        chromium_executable: str | None = None, provenance=None):
    server = thread = None
    if base is None:
        handler = functools.partial(QuietHandler, directory=public)
        server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        base = f'http://127.0.0.1:{server.server_port}'
    base = base.rstrip('/')
    checks = []
    console_errors = []

    try:
        with sync_playwright() as playwright:
            launch_args = ['--no-sandbox']
            if base.startswith('http://') and not base.startswith('http://127.0.0.1'):
                launch_args.append(f'--unsafely-treat-insecure-origin-as-secure={base}')
            launch = {'headless': True, 'args': launch_args}
            if chromium_executable:
                launch['executable_path'] = chromium_executable
            browser = playwright.chromium.launch(**launch)
            context = browser.new_context(viewport={'width': 1440, 'height': 900})
            context.grant_permissions(['clipboard-read', 'clipboard-write'], origin=base)
            page = context.new_page()
            page.on('console', lambda message: console_errors.append(message.text)
                    if message.type == 'error' else None)
            page.on('pageerror', lambda error: console_errors.append(str(error)))

            page.goto(base + '/workers/get-started/guide/', wait_until='networkidle')
            expect(page.locator('[data-sidebar-product]')).to_have_text('Workers')
            expect(page.locator('[data-sidebar-tree] [aria-current="page"]')).to_have_count(1)
            active_label = page.locator('[data-sidebar-tree] [aria-current="page"]').inner_text()
            page.locator('[data-sidebar-filter]').fill(active_label)
            expect(page.locator('[data-sidebar-tree] [aria-current="page"]')).to_be_visible()
            page.locator('[data-sidebar-filter]').fill('')
            checks.append('navigation/filter/active state')

            preference = page.locator('html').get_attribute('data-nb-pref')
            page.locator('[data-theme-toggle]').click()
            expect(page.locator('html')).not_to_have_attribute('data-nb-pref', preference)
            selected_theme = page.locator('html').get_attribute('data-nb-pref')
            page.reload(wait_until='networkidle')
            expect(page.locator('html')).to_have_attribute('data-nb-pref', selected_theme)
            checks.append('theme cycle/persistence')

            expect(page.locator('[data-nb-toc-list] a')).not_to_have_count(0)
            page.locator('[data-copy-page]:visible').first.click()
            expect(page.locator('[data-copy-page-status]:visible').first).to_contain_text('copied')
            checks.append('generated TOC/page Markdown copy')

            page.keyboard.press('Control+k')
            expect(page.locator('[data-search-dialog]')).to_be_visible()
            page.locator('[data-search-input]').fill('workers cron')
            page.locator('[data-search-form]').press('Enter')
            expect(page.locator('[data-search-results] a')).to_have_attribute(
                'href', 'https://developers.cloudflare.com/search/?q=workers%20cron')
            page.locator('[data-search-close]').click()
            checks.append('search dialog/fallback')

            page.goto(base + '/sandbox/', wait_until='networkidle')
            tabs = page.locator('[data-nb-tabs]').first
            expect(tabs.locator('[role="tab"]')).not_to_have_count(0)
            if tabs.locator('[role="tab"]').count() > 1:
                tabs.locator('[role="tab"]').first.focus()
                tabs.locator('[role="tab"]').first.press('ArrowRight')
                expect(tabs.locator('[role="tabpanel"]').nth(1)).to_be_visible()
            checks.append('content tabs')

            page.goto(base + '/agent-memory/get-started/', wait_until='networkidle')
            managers = page.locator('[data-nb-pm]').first
            expect(managers.locator('[data-nb-pm-tab]')).not_to_have_count(0)
            if managers.locator('[data-nb-pm-tab]').count() > 1:
                managers.locator('[data-nb-pm-tab]').first.focus()
                managers.locator('[data-nb-pm-tab]').first.press('ArrowRight')
                expect(managers.locator('[data-nb-pm-panel]').nth(1)).to_be_visible()
            managers.locator('[data-nb-pm-copy]:visible').click()
            expect(managers.locator('[data-nb-pm-copy]:visible')).to_have_text('Copied')
            checks.append('package-manager tabs/copy')

            page.goto(base + '/stream/stream-live/troubleshooting/', wait_until='networkidle')
            details = page.locator('details.nb-details').first
            expect(details).to_have_count(1)
            initial = details.get_attribute('open') is not None
            details.locator('summary').click()
            if initial:
                expect(details).not_to_have_attribute('open', '')
            else:
                expect(details).to_have_attribute('open', '')
            checks.append('native disclosure')

            page.goto(base + '/china-network/', wait_until='networkidle')
            chapters = page.locator('details.video-chapters')
            expect(chapters).not_to_have_attribute('open', '')
            page.route('https://embed.cloudflarestream.com/embed/sdk.latest.js', lambda route: route.fulfill(
                content_type='application/javascript', body='window.Stream=()=>({set currentTime(value){window.__streamChapterTime=value}});'))
            chapters.locator('summary').click()
            chapters.locator('[data-video-time]').first.click()
            expect(page.locator('[data-stream-sdk]')).to_have_count(1)
            assert page.evaluate('window.__streamChapterTime') == 3
            checks.append('stream chapter disclosure/seek')

            mobile = browser.new_context(viewport={'width': 390, 'height': 844})
            mobile_page = mobile.new_page()
            mobile_page.goto(base + '/workers/get-started/guide/', wait_until='networkidle')
            expect(mobile_page.locator('[data-article-tools]')).to_be_visible()
            expect(mobile_page.locator('[data-mobile-toc]')).to_be_visible()
            mobile_geometry = mobile_page.evaluate('''() => {
              const box = (selector) => document.querySelector(selector).getBoundingClientRect();
              return {h1: box('h1'), tools: box('[data-article-tools]'), toc: box('[data-mobile-toc]')};
            }''')
            assert mobile_geometry['tools']['top'] >= mobile_geometry['h1']['bottom']
            assert mobile_geometry['toc']['top'] >= mobile_geometry['tools']['bottom']
            mobile_page.locator('[data-menu-btn]').click()
            expect(mobile_page.locator('[data-mobile-sidebar]')).to_be_visible()
            expect(mobile_page.locator('[data-mobile-sidebar] [data-shared-sidebar-nav]')).to_be_visible()
            mobile_page.keyboard.press('Escape')
            expect(mobile_page.locator('[data-mobile-sidebar]')).not_to_be_visible()
            expect(mobile_page.locator('[data-sidebar-home] [data-shared-sidebar-nav]')).to_have_count(1)
            checks.append('mobile navigation open/close/restore')
            mobile.close()

            tablet = browser.new_context(viewport={'width': 768, 'height': 1024})
            tablet_page = tablet.new_page()
            tablet_page.goto(base + '/workers/get-started/guide/', wait_until='networkidle')
            expect(tablet_page.locator('.top-nav')).to_be_visible()
            expect(tablet_page.locator('[data-menu-btn]')).not_to_be_visible()
            expect(tablet_page.locator('[data-sidebar-home]')).not_to_be_visible()
            expect(tablet_page.locator('[data-article-tools]')).to_be_visible()
            expect(tablet_page.locator('[data-mobile-toc]')).to_be_visible()
            tablet_geometry = tablet_page.evaluate('''() => {
              const box = (selector) => document.querySelector(selector).getBoundingClientRect();
              return {h1: box('h1'), tools: box('[data-article-tools]'), toc: box('[data-mobile-toc]'),
                overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth};
            }''')
            assert tablet_geometry['tools']['top'] >= tablet_geometry['h1']['bottom']
            assert tablet_geometry['toc']['top'] >= tablet_geometry['tools']['bottom']
            assert not tablet_geometry['overflow']
            checks.append('tablet navigation breakpoint')
            tablet.close()

            sidebar_breakpoint = browser.new_context(viewport={'width': 1024, 'height': 900})
            sidebar_page = sidebar_breakpoint.new_page()
            sidebar_page.goto(base + '/workers/get-started/guide/', wait_until='networkidle')
            expect(sidebar_page.locator('[data-sidebar-home]')).to_be_visible()
            expect(sidebar_page.locator('[data-menu-btn]')).not_to_be_visible()
            checks.append('sidebar breakpoint')
            sidebar_breakpoint.close()
            context.close()
            browser.close()
    finally:
        if server:
            server.shutdown()
            thread.join()

    if console_errors:
        raise AssertionError('browser console errors: ' + json.dumps(console_errors))
    print(json.dumps({'base': base, 'candidateProvenance': provenance,
                      'checks': checks, 'console_errors': console_errors}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--public', type=pathlib.Path,
                        default=pathlib.Path(__file__).resolve().parents[1] / 'public')
    parser.add_argument('--base')
    parser.add_argument('--chromium-executable')
    parser.add_argument('--candidate-provenance', type=pathlib.Path)
    parser.add_argument('--deployment-attestation', type=pathlib.Path)
    args = parser.parse_args()
    provenance = (json.loads(args.candidate_provenance.read_text())
                  if args.candidate_provenance else None)
    if bool(args.candidate_provenance) != bool(args.deployment_attestation):
        parser.error('--candidate-provenance and --deployment-attestation must be used together')
    if args.deployment_attestation:
        attestation = json.loads(args.deployment_attestation.read_text())
        if not attestation.get('verified') or attestation.get('candidateProvenance') != provenance:
            parser.error('deployment attestation does not verify candidate provenance')
        if not args.base or attestation.get('url', '').rstrip('/') != args.base.rstrip('/'):
            parser.error('deployment attestation URL mismatch')
    run(args.public.resolve() if not args.base else None, args.base,
        args.chromium_executable, provenance)
