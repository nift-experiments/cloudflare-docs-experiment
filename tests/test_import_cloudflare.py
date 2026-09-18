#!/usr/bin/env python3
import importlib.util, pathlib, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('imp',ROOT/'tools/import_cloudflare.py'); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
class TestImporter(unittest.TestCase):
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
  _,out=mod.convert(src,'fixture'); self.assertIn('nb-type-script-example',out); self.assertIn('language-ts',out); self.assertIn('&lt;T&gt;',out)
 def test_fence_after_list_marker(self):
  src='<Steps>\n1. One\n2. ```diff lang=ts\n+ add\n```\n3. Three\n</Steps>\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('nb-steps',out); self.assertIn('One',out)
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
  _,out=mod.convert(src,'fixture'); self.assertIn('<strong>Bold</strong>',out); self.assertIn('nb-aside-title',out); self.assertNotIn(':::',out)
 def test_unclosed_directive_auto_closes(self):
  src=':::caution[Warning]\nContent here without closing delimiter.\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('nb-aside caution',out); self.assertNotIn(':::',out)
if __name__=='__main__': unittest.main()
