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
  self.assertIn('<API_TOKEN>',out); self.assertIn('<SomePlaceholder>stay literal</SomePlaceholder>',out)
 def test_prose_apostrophe_does_not_break_pairing(self):
  src='Text with SDK\'s and Don\'t survive.\n\n<Steps>\n1. First step.\n</Steps>\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('nb-steps',out); self.assertIn("SDK's",out)
 def test_fence_variable_and_indented_close(self):
  src='<TypeScriptExample filename="x.ts">\n```ts\ncode with <T> type\n````\n</TypeScriptExample>\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('nb-type-script-example',out); self.assertIn('code with <T> type',out)
 def test_fence_after_list_marker(self):
  src='<Steps>\n1. One\n2. ```diff lang=ts\n+ add\n```\n3. Three\n</Steps>\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('nb-steps',out); self.assertIn('+ add',out)
 def test_blockquote_multiline_component(self):
  src='> Example:\n> <PackageManagers\n> \ttype="create"\n> \tpkg="vike@latest"\n> />\n> End.\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('nb-tabs',out)
 def test_space_in_closing_tag(self):
  src='<GlossaryTooltip term="CAA record">CAA records</ GlossaryTooltip> end.\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('data-cf-component="GlossaryTooltip"',out)
if __name__=='__main__': unittest.main()
