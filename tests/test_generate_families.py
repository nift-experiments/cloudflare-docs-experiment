#!/usr/bin/env python3
import importlib.util
import datetime
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


class TestAgentSetupFamily(unittest.TestCase):
    def test_agents_are_read_from_frozen_typescript_data(self):
        source = '''export const AGENTS = [
{
  name: "Example Agent",
  vendor: "Example",
  slug: "example-agent",
  icon: "example",
  description: "An example agent.",
  capabilities: { ide: true, terminal: false, cloud: true, extension: false, open_source: true },
  pricing_model: "byok",
  model_flexibility: "multi_provider",
  context_approach: "project_memory",
},
];
'''
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / 'agents.ts'
            path.write_text(source)
            agents = gen.load_agents(path)

        self.assertEqual('Example Agent', agents[0]['name'])
        self.assertTrue(agents[0]['capabilities']['ide'])
        self.assertFalse(agents[0]['capabilities']['terminal'])

    def test_landing_contains_catalog_comparison_and_primer(self):
        agent = {
            'name': 'Example Agent', 'vendor': 'Example', 'slug': 'example-agent',
            'icon': 'example', 'description': 'An example agent.',
            'pricing_model': 'byok', 'model_flexibility': 'multi_provider',
            'context_approach': 'project_memory',
            'capabilities': {'terminal': True, 'ide': False, 'extension': False,
                             'cloud': True, 'open_source': True},
        }
        page = gen.agent_setup_landing([agent])
        self.assertIn('<h1>Agent setup</h1>', page)
        self.assertIn('data-agent-card', page)
        self.assertIn('<h2 id="compare-agents">Compare agents</h2>', page)
        self.assertIn('<h2 id="understanding-agents">Understanding agents</h2>', page)


class TestChangelogFamily(unittest.TestCase):
    def test_future_entries_require_explicit_publication(self):
        today = datetime.date(2026, 9, 28)
        self.assertTrue(gen.changelog_entry_visible({'date': '2026-09-28'}, today))
        self.assertFalse(gen.changelog_entry_visible({'date': '2026-09-29'}, today))
        self.assertTrue(gen.changelog_entry_visible({
            'date': '2026-09-29', 'publish_future_dated_entry': True,
        }, today))
        self.assertFalse(gen.changelog_entry_visible({'date': 'not-a-date'}, today))

    def test_pagination_links_preserve_family_base(self):
        middle = gen.pagination_markup('/changelog/product/workers/', 2, 3)
        self.assertIn('href="/changelog/product/workers/"', middle)
        self.assertIn('href="/changelog/product/workers/3/"', middle)
        self.assertIn('Page 2 of 3', middle)
        self.assertEqual('', gen.pagination_markup('/changelog/', 1, 1))


class TestModelFamily(unittest.TestCase):
    def test_catalog_detail_renders_each_example_snippet_and_output_image(self):
        model = {
            'name': 'image-model', 'description': 'Generates images.',
            'task': 'Text-to-Image',
            'examples': [{
                'name': 'Landscape',
                'description': 'Generate a landscape.',
                'code_snippets': [
                    {'language': 'javascript', 'code': 'await env.AI.run();'},
                    {'language': 'python', 'code': 'await ai.run()'},
                ],
                'output': {
                    'image': 'https://example.com/landscape.png',
                    'images': ['https://example.com/alternate.png'],
                },
            }],
        }
        page = gen.model_detail_body(model, '/ai/models', 'image-model', catalog=True)
        self.assertEqual(1, page.count('await env.AI.run();'))
        self.assertEqual(1, page.count('await ai.run()'))
        self.assertIn('src="https://example.com/landscape.png"', page)
        self.assertIn('src="https://example.com/alternate.png"', page)

    def test_legacy_detail_includes_usage_parameters_and_schema_links(self):
        model = {
            'name': '@cf/example/text-model', 'description': 'Generates text.',
            'task': {'name': 'Text Generation'},
            'properties': [
                {'property_id': 'context_window', 'value': '32000'},
                {'property_id': 'price', 'value': [
                    {'currency': 'USD', 'price': 0.1, 'unit': 'per M input tokens'},
                ]},
            ],
            'schema': {
                'input': {'type': 'object', 'required': ['prompt'], 'properties': {
                    'prompt': {'type': 'string', 'description': 'Input prompt.'},
                }},
                'output': {'type': 'object', 'properties': {
                    'response': {'type': 'string', 'description': 'Generated text.'},
                }},
            },
        }
        page = gen.model_detail_body(model, '/workers-ai/models', 'text-model')
        self.assertIn('# text-model', page)
        self.assertIn('## Playground', page)
        self.assertIn('## Usage', page)
        self.assertIn('## Parameters', page)
        self.assertIn('<code>prompt</code>', page)
        self.assertIn('Required. Input prompt.', page)
        self.assertIn('Unit pricing', page)
        self.assertIn('Worker (Streaming)', page)
        self.assertIn('Python', page)
        self.assertIn('/workers-ai/models/text-model/schema-input.json', page)

    def test_legacy_image_detail_includes_runnable_worker_example(self):
        model = {
            'name': '@cf/example/image-model',
            'description': 'Generates images.',
            'task': {'name': 'Text-to-Image'},
            'schema': {'input': {'type': 'object', 'properties': {}}},
        }
        page = gen.model_detail_body(model, '/workers-ai/models', 'image-model')
        self.assertIn('Uint8Array.from', page)
        self.assertIn('content-type', page)
        self.assertEqual(3, page.count('<pre><code'))


if __name__ == '__main__':
    unittest.main()
