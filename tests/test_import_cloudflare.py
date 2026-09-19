#!/usr/bin/env python3
import importlib.util, pathlib, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('imp',ROOT/'tools/import_cloudflare.py'); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
class TestImporter(unittest.TestCase):
 def _conv(self, src, path='fixture'):
  import tempfile, pathlib
  d = tempfile.mkdtemp()
  mod._BODY_DIR = pathlib.Path(d)
  try:
   fm, out = mod.convert(src, path)
  finally:
   mod._BODY_DIR = None
  bodies = sorted([pathlib.Path(p).read_text() for p in pathlib.Path(d).glob('*.md')])
  return fm, out, bodies
 def test_primitives(self):
  fm,out=mod.convert((ROOT/'tests/fixtures/primitives.mdx').read_text(),'fixture'); self.assertEqual(fm['title'],'Fixture'); self.assertIn('nb-aside warning',out); self.assertIn('nb-card-grid',out); self.assertIn('nb-step',out)
 def test_interactive(self):
  _,out=mod.convert((ROOT/'tests/fixtures/interactive.mdx').read_text(),'fixture'); self.assertIn('nb-tabs',out); self.assertIn('data-cf-component="TunnelCalculator"',out); self.assertIn('data-cf-component="CompatibilityFlags"',out)
 def test_unknown_is_fatal(self):
  with self.assertRaisesRegex(ValueError,'UnknownThing'): mod.convert('import { UnknownThing } from "~/components/UnknownThing";\n<UnknownThing />','fixture')
 def test_unimported_cap_tag_is_prose(self):
  _,out=mod.convert('Text <API_TOKEN> and <SomePlaceholder>stay literal</SomePlaceholder>.','fixture')
  self.assertIn('&lt;API_TOKEN&gt;',out); self.assertIn('<SomePlaceholder>stay literal</SomePlaceholder>',out)
 def test_prose_apostrophe_does_not_break_pairing(self):
  src='Text with SDK\'s and Don\'t survive.\n\n<Steps>\n1. First step.\n</Steps>\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('nb-steps',out); self.assertIn("SDK's",out)
 def test_fence_variable_and_indented_close(self):
  src='<TypeScriptExample filename="x.ts">\n```ts\ncode with <T> type\n````\n</TypeScriptExample>\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('nb-type-script-example',out); self.assertIn('content/.markup/bodies/',out)
 def test_fence_after_list_marker(self):
  src='<Steps>\n1. One\n2. ```diff lang=ts\n+ add\n```\n3. Three\n</Steps>\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('nb-steps',out); self.assertIn('content/.markup/bodies/',out)
 def test_blockquote_multiline_component(self):
  src='> Example:\n> <PackageManagers\n> \ttype="create"\n> \tpkg="vike@latest"\n> />\n> End.\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('nb-tabs',out)
 def test_space_in_closing_tag(self):
  src='<GlossaryTooltip term="CAA record">CAA records</ GlossaryTooltip> end.\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('data-cf-component="GlossaryTooltip"',out)
 def test_multiline_import_stripped(self):
  src='import {\n\tCardGrid,\n\tDescription,\n} from "~/components";\nimport { Foo } from "@cloudflare/realtimekit";\n\n<div class="nb-description">Body.</div>\n'
  _,out=mod.convert(src,'fixture'); self.assertNotIn('~/components',out); self.assertNotIn('realtimekit',out); self.assertIn('nb-description',out)
 def test_markdown_renders_inside_components(self):
  src='<Steps>1. **Bold** and `code`.</Steps>\n:::note[Title]\nA **note**.\n:::\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('nb-aside-title',out); self.assertNotIn(':::',out)
 def test_unclosed_directive_auto_closes(self):
  src=':::caution[Warning]\nContent here without closing delimiter.\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('nb-aside caution',out); self.assertNotIn(':::',out)
 # ---- CP6B nested @markup boundary fixtures (Phase 2) ----
 def test_component_body_emits_atmarkup(self):
  src='<Steps>\n1. **Install**\n2. Run `foo`.\n</Steps>\n'
  _,out,bodies=self._conv(src); self.assertIn('nb-steps',out); self.assertTrue(bodies); self.assertIn('**Install**',bodies[0])
 def test_atmarkup_wraps_markdown_paragraph(self):
  src='<Details title="More">\nA **bold** paragraph with `code`.\n</Details>\n'
  _,out,bodies=self._conv(src); self.assertTrue(bodies); self.assertIn('**bold**',bodies[0]); self.assertIn('`code`',bodies[0])
 def test_atmarkup_fenced_code_in_body(self):
  src='<TypeScriptExample filename="x.ts">\n```ts\ncode with {x} braces\n```\n</TypeScriptExample>\n'
  _,out,bodies=self._conv(src); self.assertTrue(bodies); self.assertIn('```ts',bodies[0]); self.assertIn('{x}',bodies[0])
 def test_atmarkup_balanced_prose_braces(self):
  src='<Steps>\nText { balanced } braces.\n</Steps>\n'
  _,out,bodies=self._conv(src); self.assertIn('{ balanced }',bodies[0])
 def test_atmarkup_inline_code_braces(self):
  src='<Details title="T">\nUse `a { b }` inline.\n</Details>\n'
  _,out,bodies=self._conv(src); self.assertIn('`a { b }`',bodies[0])
 def test_atmarkup_literal_at_sigil(self):
  src='<Steps>\nInstall `@cloudflare/sandbox` and contact user@example.com.\n</Steps>\n'
  _,out,bodies=self._conv(src); self.assertIn('@cloudflare/sandbox',bodies[0]); self.assertIn('user@example.com',bodies[0])
 def test_atmarkup_markdown_after_fence(self):
  src='<Steps>\n```js\nconst x = 1;\n```\n\nText **after** the fence.\n</Steps>\n'
  _,out,bodies=self._conv(src); self.assertIn('```js',bodies[0]); self.assertIn('**after**',bodies[0])
 def test_atmarkup_nested_components(self):
  src='<Tabs>\n<TabItem label="a">\n**bold** content\n</TabItem>\n</Tabs>\n'
  _,out,bodies=self._conv(src); self.assertIn('nb-tabs',out); self.assertTrue(any('nb-tab-panel' in b for b in bodies)); self.assertIn('**bold** content',bodies[0])
 def test_atmarkup_tabs_tabitem_steps(self):
  src='<Tabs>\n<TabItem label="a">\n<Steps>\n1. **Step** one\n</Steps>\n</TabItem>\n</Tabs>\n'
  _,out,bodies=self._conv(src); self.assertIn('nb-tabs',out); self.assertTrue(any('nb-steps' in b for b in bodies))
 def test_atmarkup_directive_inside_component(self):
  src='<Details title="T">\n:::note\nA **note** inside.\n:::\n</Details>\n'
  _,out,bodies=self._conv(src); self.assertTrue(any('nb-aside note' in b for b in bodies))
 def test_atmarkup_outer_template_composes(self):
  # docs template @content composes top-level (importer-rendered) markdown
  # with file-based @markup body references for component bodies
  src='<Steps>\n1. **Install**\n</Steps>\n\nTop level **bold**.\n'
  _,out,bodies=self._conv(src); self.assertTrue(bodies); self.assertIn('Top level <strong>bold</strong>.',out); self.assertIn('content/.markup/bodies/',out); self.assertIn('**Install**',bodies[0])
 def test_atmarkup_guard_unbalanced_prose_brace(self):
  # a genuinely unmatched prose brace must be rejected by the guard, not emitted broken
  src='<Steps>\nText with an unmatched } brace.\n</Steps>\n'
  with self.assertRaises(ValueError): mod.convert(src,'fixture')
 def test_atmarkup_selfclosing_no_body(self):
  src='<DashButton url="/?to=/foo" />\n'
  _,out,bodies=self._conv(src); self.assertIn('nb-dash-button',out); self.assertFalse(bodies)
  _,out=mod.convert(src,'fixture'); self.assertIn('nb-dash-button',out); self.assertNotIn('@markup("md", "content/.markup/bodies/',out)
 def test_nested_directive_not_double_processed(self):
  # a :::caution inside a :::note must not be reordered by stale line indices
  src=':::note[Outer]\nText one.\n\n:::caution\nInner caution.\n:::\n\nText two.\n:::\n'
  _,out,bodies=self._conv(src); self.assertIn('nb-aside note',out); joined='\n'.join(bodies); self.assertIn('nb-aside caution',joined); self.assertIn('Inner caution.',joined); self.assertIn('Text two.',joined); self.assertLess(joined.find('Inner caution.'),joined.find('Text two.'),'caution must precede later prose')
 def test_irregular_fence_closer_indented(self):
  # closing fence indented deeper than the opener is not a CommonMark closer;
  # it must be pre-rendered so it cannot swallow following component HTML
  src='  ```txt ins="database_name"\n  postgres://USERNAME:PASSWORD@HOST\n   ```   \n\n<Details>\ncontent\n</Details>\n'
  _,out,bodies=self._conv(src); self.assertIn('<pre><code class="language-txt">',out); self.assertIn('nb-details',out); self.assertIn('postgres://USERNAME',out)
 def test_multiline_html_tag_joined(self):
  src='<a\n\thref="https://x/"\n\ttarget="_blank"\n>\n\t<InlineBadge text="beta" />\n</a>\n'
  _,out,bodies=self._conv(src); self.assertIn('nb-badge',out); self.assertNotIn('&lt;a',out)
 def test_pure_container_uses_input(self):
  # a pure-HTML composition body is referenced via @input, not @markup, so Nift
  # does not re-convert already-rendered nested bodies
  src='<Tabs>\n<TabItem label="One">\n```js\nconst x = 1;\n```\n</TabItem>\n</Tabs>\n'
  _,out,bodies=self._conv(src); self.assertIn('@input("content/.markup/bodies/',out); self.assertIn('nb-tab-panel','\n'.join(bodies))
 def test_asset_refs_rewritten_in_bodies(self):
  src='<Details>\n![alt](~/assets/images/x.png)\n</Details>\n'
  _,out,bodies=self._conv(src); self.assertTrue(any('/assets/upstream/images/x.png' in b for b in bodies),'~/assets must be rewritten inside body files')
 def test_top_level_markdown_rendered_by_importer(self):
  src='Some *prose* and `code`.\n\n## Heading\n\n- a\n- b\n'
  _,out,bodies=self._conv(src); self.assertIn('<em>prose</em>',out); self.assertIn('<h2>Heading</h2>',out); self.assertIn('<ul>',out)
if __name__=='__main__': unittest.main()