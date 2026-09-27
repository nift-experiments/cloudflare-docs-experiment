#!/usr/bin/env python3
import importlib.util
import pathlib
import re
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('generate_families', ROOT / 'tools/generate_families.py')
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)


class TestGeneratedFamilyBodies(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.body_dir = pathlib.Path(self.tmp.name)
        gen.mdx_importer.configure_body_output(self.body_dir, reset=True)

    def tearDown(self):
        self.tmp.cleanup()

    def body_ids(self, converted):
        return [int(x) for x in re.findall(r'content/\.markup/bodies/(\d+)\.md', converted)]

    def body_text(self, converted):
        return '\n'.join((self.body_dir / f'{idx}.md').read_text()
                         for idx in self.body_ids(converted))

    def test_stream_media_transformations_keeps_wrangler_and_typescript(self):
        source = (ROOT / 'tests/fixtures/changelog-stream-media-transformations-workers-binding.mdx').read_text()
        converted = gen.convert_mdx_body(
            source, 'changelog/stream/2026-03-18-media-transformations-workers-binding')
        materialized = self.body_text(converted)

        self.assertIn('[media]', materialized)
        self.assertIn('binding = "MEDIA"', materialized)
        self.assertIn('env.MEDIA.input(video.body)', materialized)
        self.assertNotIn('AAAA', materialized)
        self.assertNotIn('DNSKEY', materialized)

    def test_multiple_documents_never_alias_body_ids_or_content(self):
        first = '''import { WranglerConfig } from "~/components";
<WranglerConfig>
```toml
first = "alpha"
```
</WranglerConfig>
'''
        second = '''import { TypeScriptExample } from "~/components";
<TypeScriptExample>
```ts
const second = "beta";
```
</TypeScriptExample>
'''
        first_out = gen.convert_mdx_body(first, 'changelog/test/first')
        second_out = gen.convert_mdx_body(second, 'changelog/test/second')
        first_ids = set(self.body_ids(first_out))
        second_ids = set(self.body_ids(second_out))

        self.assertTrue(first_ids)
        self.assertTrue(second_ids)
        self.assertTrue(first_ids.isdisjoint(second_ids))
        self.assertIn('first = "alpha"', self.body_text(first_out))
        self.assertNotIn('second = "beta"', self.body_text(first_out))
        self.assertIn('second = "beta"', self.body_text(second_out))
        self.assertNotIn('first = "alpha"', self.body_text(second_out))

    def test_clean_ordinary_reset_removes_stale_generated_bodies(self):
        ordinary = 'import { Steps } from "~/components";\n<Steps>ordinary</Steps>\n'
        generated = 'import { Details } from "~/components";\n<Details>generated</Details>\n'
        gen.convert_mdx_body(ordinary, 'ordinary/first')
        gen.mdx_importer.record_ordinary_body_boundary()
        gen.mdx_importer.configure_generated_body_output(self.body_dir)
        gen.convert_mdx_body(generated, 'changelog/test/generated')
        self.assertEqual({'0.md', '1.md'}, {p.name for p in self.body_dir.glob('*.md')})

        gen.mdx_importer.configure_body_output(self.body_dir, reset=True)
        gen.convert_mdx_body(ordinary.replace('ordinary', 'replacement'), 'ordinary/replacement')
        gen.mdx_importer.record_ordinary_body_boundary()
        gen.mdx_importer.configure_generated_body_output(self.body_dir)
        gen.convert_mdx_body(generated.replace('generated', 'new-generated'),
                             'changelog/test/new-generated')

        self.assertEqual({'0.md', '1.md'}, {p.name for p in self.body_dir.glob('*.md')})
        self.assertIn('replacement', (self.body_dir / '0.md').read_text())
        self.assertIn('new-generated', (self.body_dir / '1.md').read_text())

        gen.mdx_importer.configure_generated_body_output(self.body_dir)
        gen.convert_mdx_body(generated.replace('generated', 'rerun-generated'),
                             'changelog/test/rerun-generated')
        self.assertEqual({'0.md', '1.md'}, {p.name for p in self.body_dir.glob('*.md')})
        self.assertIn('rerun-generated', (self.body_dir / '1.md').read_text())


if __name__ == '__main__':
    unittest.main()
