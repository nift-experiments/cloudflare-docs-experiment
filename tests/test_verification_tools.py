#!/usr/bin/env python3
import importlib.util
import contextlib
import io
import json
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_tool(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / f'tools/{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


routes = load_tool('verify_routes')
leaks = load_tool('leak_scan')
parity = load_tool('parity')
corpus_parity = load_tool('audit_corpus_parity')


class TestRouteVerification(unittest.TestCase):
    def test_generated_routes_and_static_files_are_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = pathlib.Path(tmp)
            public = base / 'public'
            for route in ('', 'docs', 'generated'):
                page = public / route / 'index.html'
                page.parent.mkdir(parents=True, exist_ok=True)
                page.write_text('<a href="/api/resources/live/">external</a>')
            static = public / 'data/feed.json'
            static.parent.mkdir(parents=True)
            static.write_text('{}')
            markdown = public / 'docs/index.md'
            markdown.write_text('# Docs\n')
            ordinary = base / 'ordinary.json'
            ordinary.write_text(json.dumps({'upstream_sha': 'bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf', 'routes': ['/docs/'], 'markdown_endpoints': 1}))
            generated = base / 'generated.json'
            generated.write_text(json.dumps({
                'upstream_sha': 'bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf',
                'routes': ['/generated/'],
                'static_files': ['/data/feed.json'],
            }))

            report = routes.verify(public, ordinary, generated)
            self.assertEqual([], report['missing_routes'])
            self.assertEqual([], report['unexpected_routes'])
            self.assertEqual([], report['missing_static_files'])
            self.assertEqual(3, report['broken_categories']['external-api-application'])

            static.unlink()
            markdown.unlink()
            report = routes.verify(public, ordinary, generated)
            self.assertEqual(['/data/feed.json', '/docs/index.md'], report['missing_static_files'])

            extra = public / 'stale/index.html'
            extra.parent.mkdir()
            extra.write_text('stale')
            report = routes.verify(public, ordinary, generated)
            self.assertEqual(['/stale/'], report['unexpected_routes'])

    def test_navigation_json_references_are_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = pathlib.Path(tmp)
            public = base / 'public'
            (public / 'index.html').parent.mkdir(parents=True)
            (public / 'index.html').write_text('home')
            navigation = public / 'assets/navigation'
            navigation.mkdir(parents=True)
            (navigation / 'product.json').write_text(json.dumps({
                'children': [{'href': '/missing/', 'label': 'Missing'}],
                'valid': {'href': '/?example=true#top'},
                'external': {'href': 'https://example.com/'},
            }))
            (public / 'assets/navigation.json').write_text(json.dumps({
                'home': [{'links': [{'href': '/root-missing/'}]}],
            }))
            ordinary = base / 'ordinary.json'
            generated = base / 'generated.json'
            ordinary.write_text(json.dumps({
                'upstream_sha': 'bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf', 'routes': []}))
            generated.write_text(json.dumps({
                'upstream_sha': 'bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf', 'routes': []}))

            report = routes.verify(public, ordinary, generated)

            self.assertEqual(
                [('assets/navigation/product.json', '/missing/'),
                 ('assets/navigation.json', '/root-missing/')],
                report['unclassified_broken_refs'],
            )


class TestLeakScan(unittest.TestCase):
    def test_missing_or_empty_output_cannot_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = pathlib.Path(tmp)
            with self.assertRaisesRegex(RuntimeError, 'does not exist'):
                leaks.scan_public(base / 'missing')
            with self.assertRaisesRegex(RuntimeError, 'no HTML files'):
                leaks.scan_public(base)

    def test_real_leakage_fails_and_write_classified_is_real_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = pathlib.Path(tmp)
            public = base / 'public'
            public.mkdir()
            (public / 'index.html').write_text('<html><body>:::note[Leaked]</body></html>')
            output = base / 'classified.json'

            with contextlib.redirect_stdout(io.StringIO()):
                result = leaks.main([str(public), '--write-classified', str(output)])
            self.assertEqual(1, result)
            report = json.loads(output.read_text())
            self.assertEqual(1, report['REAL_leakage']['mdx-directive'])
            self.assertEqual(1, report['REAL_leakage_files_affected'])

    def test_intentional_code_does_not_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            public = pathlib.Path(tmp)
            (public / 'index.html').write_text(
                '<html><body><pre>\nimport x from "pkg";</pre></body></html>')
            report = leaks.scan_public(public)
            self.assertEqual({}, report['REAL_leakage'])
            self.assertEqual(1, report['INTENTIONAL_text']['code-import'])

    def test_every_known_component_is_detected_outside_code(self):
        for component in leaks.KNOWN_COMPONENTS:
            with self.subTest(component=component):
                report = leaks.scan(f'<main>&lt;{component} prop="value"&gt;</main>')
                self.assertIn('component-open', report['real'])


class TestParityPolicy(unittest.TestCase):
    def capture(self, text_bytes=1000, headings=None, width=800):
        return {
            'status': 200, 'consoleErrors': [], 'failedLocalRequests': [], 'badLocalResponses': [],
            'failedExternalRequests': [], 'badExternalResponses': [],
            'probes': {
                'horizontalOverflow': False, 'h1': {'width': 100, 'y': 100},
                'mainTextBytes': text_bytes, 'headingText': headings or ['Title', 'Usage', 'Parameters'],
                'mainWords': ['title', 'usage', 'parameters', 'shared'],
                'bodyColumn': {'display': 'block', 'width': width},
                'main': {'display': 'block', 'width': width},
            },
        }

    def test_severe_text_heading_and_geometry_divergence_fail(self):
        upstream = self.capture()
        nift = self.capture(text_bytes=100, headings=['Title'], width=200)
        failures = parity.parity_failures(upstream, nift, {'width': 1440, 'height': 900})
        self.assertIn('main-text-below-65-percent', failures)
        self.assertIn('heading-count-below-85-percent', failures)
        self.assertIn('heading-labels-below-85-percent', failures)
        self.assertIn('collapsed-bodyColumn', failures)
        self.assertIn('collapsed-main', failures)

    def test_comparable_page_passes(self):
        upstream = self.capture()
        nift = self.capture(text_bytes=700, headings=['Title', 'Usage', 'Parameters'], width=800)
        self.assertEqual([], parity.parity_failures(
            upstream, nift, {'width': 1440, 'height': 900}))

    def test_padded_replacement_content_and_missing_main_fail(self):
        upstream = self.capture()
        nift = self.capture()
        nift['probes']['mainWords'] = ['unrelated', 'replacement', 'padding', 'only']
        nift['probes']['main'] = None
        failures = parity.parity_failures(upstream, nift, {'width': 1440, 'height': 900})
        self.assertIn('upstream-word-coverage-below-55-percent', failures)
        self.assertIn('nift-word-precision-below-75-percent', failures)
        self.assertIn('missing-main-geometry', failures)

    def test_image_divergence_is_enforced(self):
        upstream = self.capture()
        nift = self.capture()
        failures = parity.parity_failures(
            upstream, nift, {'width': 1440, 'height': 900},
            {'sameSize': True, 'changedPixelRatio': 0.98,
             'significantPixelRatio': 0.36,
             'meanAbsoluteChannelDelta': 40})
        self.assertIn('significant-pixels-above-20-percent', failures)
        self.assertIn('mean-channel-delta-above-30', failures)

    def test_significant_pixel_threshold_is_independent_of_mean_delta(self):
        upstream = self.capture()
        nift = self.capture()
        failures = parity.parity_failures(
            upstream, nift, {'width': 1440, 'height': 900},
            {'sameSize': True, 'changedPixelRatio': 0.25,
             'significantPixelRatio': 0.21,
             'meanAbsoluteChannelDelta': 5})
        self.assertIn('significant-pixels-above-20-percent', failures)

    def test_heading_geometry_divergence_is_enforced(self):
        upstream = self.capture()
        nift = self.capture()
        nift['probes']['h1']['y'] = 200
        failures = parity.parity_failures(upstream, nift, {'width': 1440, 'height': 900})
        self.assertIn('h1-vertical-offset-above-64px', failures)

    def test_nift_exclusive_external_failure_is_enforced(self):
        upstream = self.capture()
        nift = self.capture()
        nift['failedExternalRequests'] = ['https://media.invalid/video']
        failures = parity.parity_failures(upstream, nift, {'width': 1440, 'height': 900})
        self.assertIn('nift-exclusive-external-request-failures', failures)

    def test_non_200_capture_is_enforced(self):
        upstream = self.capture()
        nift = self.capture()
        upstream['status'] = 404
        nift['status'] = 500
        failures = parity.parity_failures(upstream, nift, {'width': 1440, 'height': 900})
        self.assertIn('upstream-non-200', failures)
        self.assertIn('nift-non-200', failures)

    def test_visual_step_numbers_do_not_create_false_heading_mismatches(self):
        upstream = self.capture(headings=['Guide', '1. Install', '2. Deploy'])
        nift = self.capture(headings=['Guide', 'Install', 'Deploy'])
        self.assertEqual([], parity.parity_failures(
            upstream, nift, {'width': 1440, 'height': 900}))

    def test_unknown_viewport_cannot_pass_with_zero_captures(self):
        with tempfile.TemporaryDirectory() as tmp:
            sample = pathlib.Path(tmp) / 'sample.json'
            sample.write_text(json.dumps({
                'routes': [{'route': '/', 'reasons': []}],
                'viewports': [{'name': 'mobile', 'width': 390, 'height': 844}],
            }))
            with self.assertRaises(SystemExit):
                parity.main(['--upstream', 'http://upstream.invalid',
                             '--nift', 'http://nift.invalid', '--sample', str(sample),
                             '--viewport', 'missing', '--screenshots'])

    def test_screenshot_capture_is_mandatory(self):
        with tempfile.TemporaryDirectory() as tmp:
            sample = pathlib.Path(tmp) / 'sample.json'
            sample.write_text(json.dumps({
                'routes': [{'route': '/', 'reasons': []}],
                'viewports': [{'name': 'mobile', 'width': 390, 'height': 844}],
            }))
            with self.assertRaises(SystemExit):
                parity.main(['--upstream', 'http://upstream.invalid',
                             '--nift', 'http://nift.invalid', '--sample', str(sample)])


class TestCorpusParityPolicy(unittest.TestCase):
    def test_only_required_absent_classifications_are_stale(self):
        classifications = {
            '/deterministic/': {'reasons': ['difference']},
            '/live/': {'reasons': ['difference'], 'required': False},
            '/observed/': {'reasons': ['difference']},
        }
        self.assertEqual(
            ['/deterministic/'],
            corpus_parity.stale_classification_routes(classifications, {'/observed/'}),
        )

    def page(self, words=None, headings=None, elements=None):
        return {
            'status': 200,
            'kind': 'html',
            'structure': {
                'mainCount': 1,
                'words': words or [f'word{index}' for index in range(100)],
                'headings': headings or [('h1', 'title'), ('h2', 'usage'), ('h2', 'parameters')],
                'elements': {'table': 0, 'pre': 0, 'img': 0, 'iframe': 0} | (elements or {}),
            },
        }

    def test_replacement_content_heading_order_and_missing_elements_fail(self):
        upstream = self.page(elements={'table': 1})
        nift = self.page(words=[f'replacement{index}' for index in range(100)],
                         headings=[('h1', 'different')])
        failures = corpus_parity.compare(upstream, nift)
        self.assertIn('upstream-word-coverage-below-70-percent', failures)
        self.assertIn('word-precision-below-70-percent', failures)
        self.assertIn('heading-order-coverage-below-70-percent', failures)
        self.assertIn('table-count-below-50-percent', failures)

    def test_matching_structure_passes(self):
        page = self.page(elements={'pre': 1})
        self.assertEqual([], corpus_parity.compare(page, page))

    def test_changelog_product_navigation_is_not_counted_as_content(self):
        structure = corpus_parity.parse_html('''
            <main><h1>Changelog</h1>
            <div data-changelog-product-nav>
              <input value="hidden"><span>Search products</span><div><span>Hidden product</span></div>
            </div>
            <p>Visible release notes</p></main>
        ''')
        self.assertEqual(['changelog', 'notes', 'release', 'visible'], structure['words'])
        self.assertEqual([('h1', 'changelog')], structure['headings'])

    def test_article_excludes_main_shell_chrome(self):
        structure = corpus_parity.parse_html('''
            <main><nav>Breadcrumb words</nav><article><h1>Title</h1><p>Body copy</p></article>
            <aside>Was this helpful?</aside></main>
        ''')
        self.assertEqual(['body', 'copy', 'title'], structure['words'])

    def test_multiple_card_articles_keep_the_main_scope(self):
        structure = corpus_parity.parse_html('''
            <main><h1>Directory</h1><article>First card</article><article>Second card</article></main>
        ''')
        self.assertEqual(['card', 'directory', 'first', 'second'], structure['words'])

    def test_replacement_text_content_fails(self):
        upstream = {'status': 200, 'kind': 'text',
                    'structure': {'words': [f'upstream{index}' for index in range(30)]}}
        nift = {'status': 200, 'kind': 'text',
                'structure': {'words': [f'replacement{index}' for index in range(30)]}}
        failures = corpus_parity.compare(upstream, nift)
        self.assertIn('upstream-text-word-coverage-below-75-percent', failures)
        self.assertIn('text-word-precision-below-75-percent', failures)

    def test_generated_text_routes_are_audited(self):
        with tempfile.TemporaryDirectory() as tmp:
            ordinary = pathlib.Path(tmp) / 'ordinary.json'
            generated = pathlib.Path(tmp) / 'generated.json'
            ordinary.write_text(json.dumps({'routes': ['/docs/']}))
            generated.write_text(json.dumps({
                'routes': ['/generated/'],
                'text_routes': ['/llms.txt'],
            }))
            self.assertEqual(
                ['/', '/docs/', '/generated/', '/llms.txt'],
                corpus_parity.load_routes(ordinary, generated),
            )


if __name__ == '__main__':
    unittest.main()
