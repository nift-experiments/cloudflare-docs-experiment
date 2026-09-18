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
  with self.assertRaisesRegex(ValueError,'UnknownThing'): mod.convert('<UnknownThing />','fixture')
if __name__=='__main__': unittest.main()
