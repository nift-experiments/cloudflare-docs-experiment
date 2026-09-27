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
            ordinary = base / 'ordinary.json'
            ordinary.write_text(json.dumps({'routes': ['/docs/']}))
            generated = base / 'generated.json'
            generated.write_text(json.dumps({
                'routes': ['/generated/'],
                'static_files': ['/data/feed.json'],
            }))

            report = routes.verify(public, ordinary, generated)
            self.assertEqual([], report['missing_routes'])
            self.assertEqual([], report['missing_static_files'])
            self.assertEqual(3, report['broken_categories']['external-api-application'])

            static.unlink()
            report = routes.verify(public, ordinary, generated)
            self.assertEqual(['/data/feed.json'], report['missing_static_files'])


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


if __name__ == '__main__':
    unittest.main()
