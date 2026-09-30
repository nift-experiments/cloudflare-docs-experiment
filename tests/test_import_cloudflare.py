#!/usr/bin/env python3
import importlib.util, pathlib, tempfile, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('imp',ROOT/'tools/import_cloudflare.py'); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
class TestImporter(unittest.TestCase):
 def setUp(self):
  self._tmp=tempfile.TemporaryDirectory(); self._body_dir=pathlib.Path(self._tmp.name); mod.configure_body_output(self._body_dir,reset=True); mod.configure_resources([]); mod.configure_partials(None); mod.configure_pages_build_presets({}); mod.configure_pages_build_environments([]); mod.configure_glossaries({}); mod.configure_release_notes({}); mod.configure_wrangler_commands({}); mod.configure_videos([])
 def tearDown(self):
  self._tmp.cleanup()
 def _conv(self, src, path='fixture'):
  before={p.name for p in self._body_dir.glob('*.md')}; fm,out=mod.convert(src,path)
  bodies=[p.read_text() for p in sorted(self._body_dir.glob('*.md'),key=lambda p:int(p.stem)) if p.name not in before]
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
  _,out=mod.convert(src,'fixture'); self.assertIn('nb-package-managers',out); self.assertIn('npm create vike@latest',out); self.assertIn('yarn create vike',out)
 def test_space_in_closing_tag(self):
  src='<GlossaryTooltip term="CAA record">CAA records</ GlossaryTooltip> end.\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('<span class="nb-glossary-tooltip"',out)
 def test_multiline_import_stripped(self):
  src='import {\n\tCardGrid,\n\tDescription,\n} from "~/components";\nimport { Foo } from "@cloudflare/realtimekit";\n\n<div class="nb-description">Body.</div>\n'
  _,out=mod.convert(src,'fixture'); self.assertNotIn('~/components',out); self.assertNotIn('realtimekit',out); self.assertIn('nb-description',out)
 def test_markdown_renders_inside_components(self):
   src='<Steps>1. **Bold** and `code`.</Steps>\n:::note[Title]\nA **note**.\n:::\n'
   _,out=mod.convert(src,'fixture'); self.assertIn('nb-aside-title',out); self.assertNotIn(':::',out)
 def test_gfm_tables_render_as_tables(self):
  _,out=mod.convert('| Value | Meaning |\n| --- | --- |\n| server | update |\n','fixture'); self.assertIn('<table>',out); self.assertNotIn('| Value',out)
 def test_gfm_footnotes_render_section_and_definition(self):
  _,out=mod.convert('A statement.[^1]\n\n[^1]: Supporting detail.\n','fixture')
  self.assertIn('<h2 id="footnotes">Footnotes</h2>',out)
  self.assertIn('Supporting detail.',out)
  self.assertNotIn('[^1]',out)
 def test_gfm_tables_inside_component_bodies_are_materialized(self):
  _,_,bodies=self._conv('<Tabs><TabItem label="One">\n| Value | Meaning |\n| --- | --- |\n| server | update |\n</TabItem></Tabs>\n'); self.assertTrue(any('<table>' in body for body in bodies)); self.assertFalse(any('| Value' in body for body in bodies))
 def test_video_components_materialize_iframes(self):
  src='import { YouTube, Stream } from "~/components";\n<YouTube id="abc" />\n<Stream id="def" title="Demo" thumbnail="https://example.com/poster.jpg" />\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('<iframe src="https://www.youtube-nocookie.com/embed/abc"',out); self.assertIn('<iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/def/iframe',out); self.assertIn('title="Demo"',out)
 def test_raw_iframe_gets_accessible_title(self):
  _,out=mod.convert('<iframe src="https://example.com/embed"></iframe>','fixture')
  self.assertIn('<iframe title="Embedded media" src="https://example.com/embed">',out)
 def test_glossary_tooltip_preserves_inline_accessible_text(self):
  src='import { GlossaryTooltip } from "~/components";\n<a href="/target/"><GlossaryTooltip term="LLM">language model</GlossaryTooltip></a>\n'
  _,out=mod.convert(src,'fixture')
  self.assertIn('<a href="/target/"><span class="nb-glossary-tooltip" title="LLM">language model</span></a>',out)
 def test_plan_materializes_availability_label(self):
  _,out=mod.convert('<Plan type="all" />\n','fixture'); self.assertIn('<div class="nb-plan">',out); self.assertIn('Available on all plans',out)
 def test_stream_timestamp_becomes_remote_thumbnail(self):
  _,out=mod.convert('<Stream id="abc" title="Demo" thumbnail="1m37s" />\n','fixture')
  self.assertIn('abc/iframe?preload=true&amp;letterboxColor=transparent',out)
  self.assertIn('abc%2Fthumbnails%2Fthumbnail.jpg%3Ffit%3Dcrop%26time%3D1m37s',out)
  self.assertIn('&amp;poster=https%3A%2F%2Fcustomer-1mwganm1ma0xgnmj.cloudflarestream.com',out)
 def test_stream_materializes_source_defined_chapter_thumbnails(self):
  _,out=mod.convert('<Stream id="abc" title="Demo" chapters={{ Intro: "3s", "Next step": "1m2s", Odd: "6m:59s", Partial: "5m36" }} />\n','fixture')
  self.assertIn('<details class="nb-details video-chapters"><summary>Chapters</summary>',out)
  self.assertIn('abc/thumbnails/thumbnail.jpg?fit=crop&amp;time=3s',out)
  self.assertIn('data-video-time="62"',out)
  self.assertIn('data-video-time="0"',out)
  self.assertIn('data-video-time="300"',out)
  self.assertIn('alt="Next step"',out)
  self.assertEqual(4,out.count('<img'))
 def test_stream_file_resolves_frozen_video_metadata(self):
  mod.configure_videos([{'url':'demo-video','id':'abc','title':'Demo',
                         'thumbnail':{'timestamp':'4s'},'chapters':{'Intro':'5s'}}])
  _,out=mod.convert('<Stream file="demo-video" />\n','fixture')
  self.assertIn('/abc/iframe?',out)
  self.assertIn('title="Demo"',out)
  self.assertIn('data-video-time="5"',out)
 def test_agent_shared_components_render_substantive_content(self):
  src='import ExamplePromptsList from "~/components/agent-setup/ExamplePromptsList.astro";\nimport BuildAgentsCallout from "~/components/agent-setup/BuildAgentsCallout.astro";\n<ExamplePromptsList />\n<BuildAgentsCallout />\n'
  _,out=mod.convert(src,'fixture')
  self.assertEqual(5,out.count('language-txt'))
  self.assertIn('persistent conversation history',out)
  self.assertIn('Build an MCP server',out)
 def test_ai_gateway_code_snippets_render_all_provider_variants(self):
  _,out=mod.convert('import CodeSnippets from "~/components/ai-gateway/code-examples.astro";\n<CodeSnippets forceClient="aisdk" />\n','fixture')
  self.assertEqual(24,out.count('language-javascript'))
  self.assertIn('workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast',out)
 def test_pages_build_environment_renders_each_version_table(self):
  mod.configure_pages_build_environments([
   {'id':'v1','languages':[{'name':'Node.js','default':'18','supported':'Any version','environment_variable':'NODE_VERSION','file':['.nvmrc']}]},
   {'id':'v2','languages':[{'name':'Node.js','default':'22','supported':'Any version','environment_variable':'NODE_VERSION','file':['.nvmrc']}]},
  ])
  _,out=mod.convert('<PagesBuildEnvironmentLanguages />\n','fixture')
  self.assertEqual(2,out.count('<table>'))
  self.assertIn('NODE_VERSION',out)
 def test_pre_blocks_are_opaque_to_outer_markdown_pass(self):
  _,out=mod.convert('```ts\nconst first = 1;\n\nconst second = 2;\n```\n','fixture')
  self.assertNotIn('\n',out[out.index('<pre'):out.index('</pre>')])
  self.assertIn('&#10;',out)
 def test_jsx_template_literal_attribute_is_materialized(self):
  _,out=mod.convert('<a href={`https://example.com/feed`}>RSS feed</a>\n','fixture')
  self.assertIn('<a href="https://example.com/feed">RSS feed</a>',out)
 def test_components_usage_materializes_component_sections(self):
  _,out=mod.convert('import { ComponentsUsage } from "~/components";\n<ComponentsUsage />\n','fixture')
  self.assertIn('<h2 id="anchorheading">AnchorHeading</h2>',out); self.assertIn('<h2 id="wranglernamespace">WranglerNamespace</h2>',out)
 def test_nested_link_card_html_is_not_indented_code(self):
  src='<CardGrid>\n      <LinkCard title="Example" href="/example/" />\n</CardGrid>\n'
  _,_,bodies=self._conv(src); combined='\n'.join(bodies)
  self.assertIn('\n<div class="nb-card nb-link-card"',combined)
  self.assertNotIn('\n      <div class="nb-card nb-link-card"',combined)
 def test_api_request_materializes_code_example(self):
  src='import { APIRequest } from "~/components";\n<APIRequest path="/accounts/{account_id}/access/groups" method="POST" />\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('<pre tabindex="0" class="nb-api-request"><code class="language-bash">',out); self.assertIn('curl --request POST',out); self.assertIn('/accounts/{account_id}/access/groups',out)
 def test_unclosed_directive_auto_closes(self):
  src=':::caution[Warning]\nContent here without closing delimiter.\n'
  _,out=mod.convert(src,'fixture'); self.assertIn('nb-aside caution',out); self.assertNotIn(':::',out)
 # ---- CP6B nested @markup boundary fixtures (Phase 2) ----
 def test_component_body_emits_atmarkup(self):
  src='<Steps>\n1. **Install**\n2. Run `foo`.\n</Steps>\n'
  _,out,bodies=self._conv(src); self.assertIn('nb-steps',out); self.assertTrue(bodies); self.assertIn('**Install**',bodies[0])
 def test_component_body_requires_materialization_output(self):
  mod._BODY_DIR=None
  with self.assertRaisesRegex(RuntimeError,'configure_body_output'):
   mod.convert('<Steps>\n1. Install\n</Steps>\n','fixture')
  mod.configure_body_output(self._body_dir)
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
  _,out,bodies=self._conv(src); self.assertIn('<pre tabindex="0"><code class="language-txt">',out); self.assertIn('nb-details',out); self.assertIn('postgres://USERNAME',out)
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

 def test_imported_astro_images_are_native_and_rewritten(self):
  src='import shot from "~/assets/images/shot.png";\n\n<Image src={shot} alt="Shot" />\n<img src={shot.src} alt="Shot 2" />\n'
  _,out,_=self._conv(src)
  self.assertEqual(out.count('<img src="/assets/upstream/images/shot.png"'),2)
  self.assertNotIn('{shot',out)

 def test_content_h1_is_demoted_beneath_template_title(self):
  _,out,_=self._conv('# Repeated page title\n')
  self.assertIn('<h2 id="repeated-page-title">Repeated page title</h2>',out)
  self.assertNotIn('<h1',out)

 def test_component_body_headings_are_demoted_and_addressable(self):
  _,_,bodies=self._conv('<Details>\n# Nested title\n\n## Nested section\n</Details>')
  rendered='\n'.join(bodies)
  self.assertIn('<h2 id="body-0-nested-title">Nested title</h2>',rendered)
  self.assertIn('<h2 id="body-0-nested-section">Nested section</h2>',rendered)

 def test_component_body_common_indent_is_not_code(self):
  _,_,bodies=self._conv('<Description>\n\tIndented description.\n</Description>')
  self.assertIn('Indented description.',bodies[0])
  self.assertNotIn('\tIndented description.',bodies[0])

 def test_indented_fence_markers_cannot_become_headings(self):
  src='<Details>\n   ```python\n   # comment\n   ---\n   ```\n</Details>'
  _,_,bodies=self._conv(src)
  rendered='\n'.join(bodies)
  self.assertIn('&#35; comment',rendered)
  self.assertIn('&#45;--',rendered)

 def test_card_without_href_is_not_placeholder_link(self):
  _,out,_=self._conv('<Card title="Status">Body</Card>')
  self.assertIn('<div class="nb-card">',out)
  self.assertNotIn('href="#"',out)
 def test_link_title_card_preserves_heading_semantics(self):
  _,out,_=self._conv('<LinkTitleCard title="Get started" href="/start/">Begin.</LinkTitleCard>')
  self.assertIn('<h3 id="card-get-started-start"><a href="/start/">Get started</a></h3>',out)
  self.assertIn('href="/start/"',out)
 def test_top_level_markdown_rendered_by_importer(self):
  src='Some *prose* and `code`.\n\n## Heading\n\n- a\n- b\n'
  _,out,bodies=self._conv(src); self.assertIn('<em>prose</em>',out); self.assertIn('<h2 id="heading">Heading</h2>',out); self.assertIn('<ul>',out)
 def test_empty_navigation_page_keeps_frontmatter_description(self):
  src='---\ntitle: Overview\ndescription: Learn the product fundamentals.\n---\n'
  fm,out,_=self._conv(src)
  self.assertEqual('Learn the product fundamentals.',fm['description'])
  self.assertIn('<p>Learn the product fundamentals.</p>',out)
 def test_details_header_open_and_body(self):
  src='<Details header="**Advanced** options" open>\nUse `value`.\n</Details>\n'
  _,out,bodies=self._conv(src); self.assertIn('<details class="nb-details" open>',out); self.assertIn('<summary><strong>Advanced</strong> options</summary>',out); self.assertIn('Use `value`.',bodies[0])
 def test_tabs_emit_sync_and_labels(self):
  src='<Tabs syncKey="language"><TabItem label="JavaScript">JS</TabItem><TabItem value="Python">PY</TabItem></Tabs>\n'
  _,out,bodies=self._conv(src); joined='\n'.join(bodies); self.assertIn('data-nb-sync-key="language"',out); self.assertIn('data-nb-tab-label="JavaScript"',joined); self.assertIn('data-nb-tab-label="Python"',joined)
 def test_heading_ids_are_stable_and_unique(self):
  _,out,_=self._conv('## Hello, world!\n\n## Hello world\n\n### Another section\n')
  self.assertIn('<h2 id="hello-world">',out); self.assertIn('<h2 id="hello-world-1">',out); self.assertIn('<h3 id="another-section">',out)
 def test_duplicate_existing_heading_ids_are_rewritten(self):
  out=mod.add_heading_ids('<h3 id="card-same">Same</h3><h3 id="card-same">Same</h3>'); self.assertEqual(1,out.count('id="card-same"')); self.assertIn('id="card-same-1"',out)
 def test_resources_by_selector_materializes_matching_docs(self):
  mod.configure_resources([
   {'id':'sandbox/guides/alpha','route':'/sandbox/guides/alpha/','title':'Alpha guide','description':'First guide.','pcx_content_type':'how-to','products':['sandbox'],'reviewed':'2026-01-01'},
   {'id':'sandbox/tutorials/beta','route':'/sandbox/tutorials/beta/','title':'Beta tutorial','description':'Other.','pcx_content_type':'tutorial','products':['sandbox'],'reviewed':'2026-01-02'},
  ])
  src='import { ResourcesBySelector } from "~/components";\n<ResourcesBySelector directory="sandbox/guides/" types={["how-to"]} />\n'
  _,out,_=self._conv(src)
  self.assertIn('Alpha guide',out); self.assertIn('/sandbox/guides/alpha/',out); self.assertIn('First guide.',out); self.assertNotIn('Beta tutorial',out)
 def test_resources_by_selector_fails_closed_when_empty(self):
  src='import { ResourcesBySelector } from "~/components";\n<ResourcesBySelector directory="missing/" types={["how-to"]} />\n'
  with self.assertRaisesRegex(ValueError,'no resources match'): self._conv(src)
 def test_link_buttons_inside_raw_div_remain_balanced(self):
  src='import { LinkButton } from "~/components";\n<div>\n\t<LinkButton href="/one/">One</LinkButton>\n\t<LinkButton href="/two/" target="_blank">Two</LinkButton>\n</div>\n'
  _,out,_=self._conv(src)
  self.assertEqual(out.count('<div'),out.count('</div>'))
  self.assertEqual(2,out.count('class="nb-link-button"'))
  self.assertNotIn('&lt;div',out)
  self.assertIn('rel="noopener noreferrer"',out)
 def test_render_expands_nested_frozen_partials(self):
  partials=self._body_dir/'partials'; product=partials/'example'; product.mkdir(parents=True)
  (product/'inner.mdx').write_text('Inner **content**.\n')
  (product/'outer.mdx').write_text('Outer content.\n\n<Render file="inner" product="example" />\n')
  mod.configure_partials(partials)
  src='import { Render } from "~/components";\n<Render file="outer" product="example" />\n'
  _,out,_=self._conv(src)
  self.assertIn('Outer content.',out); self.assertIn('Inner <strong>content</strong>.',out)
  self.assertNotIn('data-cf-component="Render"',out)
 def test_render_missing_upstream_partial_retains_explicit_shell(self):
  partials=self._body_dir/'partials'; partials.mkdir()
  mod.configure_partials(partials)
  _,out,_=self._conv('<Render file="missing" product="example" />')
  self.assertIn('data-cf-component="Render"',out)
 def test_render_literal_params_expand_runtime_props(self):
  partials=self._body_dir/'partials'; product=partials/'example'; product.mkdir(parents=True)
  (product/'dynamic.mdx').write_text('Value: {props.label}\n\n<a href={props.url}>Open</a>\n')
  mod.configure_partials(partials)
  _,out,_=self._conv('<Render file="dynamic" product="example" params={{label: "A", url: "/a/"}} />')
  self.assertNotIn('data-cf-component="Render"',out)
  self.assertIn('Value: A',out)
  self.assertIn('href="/a/"',out)
  self.assertNotIn('props.label',out)
 def test_render_array_params_expand_runtime_props(self):
  partials=self._body_dir/'partials'; product=partials/'example'; product.mkdir(parents=True)
  (product/'dynamic.mdx').write_text('<SubtractIPCalculator defaults={{ subtract: props.items }} />\n')
  mod.configure_partials(partials)
  _,out,_=self._conv('<Render file="dynamic" product="example" params={{items: ["10.0.0.1", "10.0.0.0/24"]}} />')
  self.assertNotIn('data-cf-component="Render"',out)
  self.assertIn('SubtractIPCalculator',out)
 def test_pages_build_preset_renders_configuration_table(self):
  mod.configure_pages_build_presets({'astro': {'build_command': 'npm run build', 'build_output_directory': 'dist'}})
  _,out,_=self._conv('<PagesBuildPreset framework="astro" />')
  self.assertIn('<table>',out); self.assertIn('npm run build',out); self.assertIn('<code>dist</code>',out)
 def test_render_forwards_params_to_nested_partial(self):
  partials=self._body_dir/'partials'; product=partials/'example'; product.mkdir(parents=True)
  (product/'inner.mdx').write_text('Inner {props.label}.\n')
  (product/'outer.mdx').write_text('<Render file="inner" product="example" params={{ label: props.label }} />\n')
  mod.configure_partials(partials)
  _,out,_=self._conv('<Render file="outer" product="example" params={{ label: "forwarded" }} />')
  self.assertIn('Inner forwarded.',out); self.assertNotIn('data-cf-component="Render"',out)
 def test_glossary_renders_configured_terms(self):
  mod.configure_glossaries({'workers': {'productName': 'Workers', 'entries': [{'term': 'isolate', 'general_definition': 'a lightweight runtime'}]}})
  _,out,_=self._conv('<Glossary product="workers" />')
  self.assertIn('<table',out); self.assertIn('isolate',out); self.assertIn('A lightweight runtime',out)
 def test_glossary_definition_renders_configured_term(self):
  mod.configure_glossaries({'workers': {'entries': [{'term': 'isolate', 'general_definition': 'a **lightweight** runtime'}]}})
  _,out,_=self._conv('<GlossaryDefinition term="isolate" prepend="In Workers, " />')
  self.assertIn('In Workers, a <strong>lightweight</strong> runtime',out)
 def test_api_request_renders_nested_json(self):
  src='''<APIRequest path="/zones/{zone_id}/rulesets" method="PUT" json={{ rules: [{ action: "compress_response", enabled: true }], count: 2 }} />'''
  _,out,_=self._conv(src)
  self.assertIn('compress_response',out); self.assertIn('&quot;enabled&quot;: true',out)
 def test_rule_id_renders_visible_suffix(self):
  _,out,_=self._conv('<RuleID id="00000000-1111-2222-3333-abcdef123456" />')
  self.assertIn('ef123456',out); self.assertIn('00000000-1111-2222-3333-abcdef123456',out)
 def test_product_release_notes_render_configured_entries(self):
  mod.configure_release_notes({'sdk': {'entries': [{'publish_date': '2026-01-02', 'title': 'SDK 2', 'description': 'Added **support**.'}]}})
  fm,out=mod.convert('<ProductReleaseNotes />','fixture',metadata={'release_notes_file_name':['sdk']})
  self.assertIn('<h2',out); self.assertIn('2026-01-02',out); self.assertIn('<strong>support</strong>',out)
 def test_wrangler_namespace_renders_commands_and_arguments(self):
  mod.configure_wrangler_commands({'d1': [{'command':'wrangler d1 create','metadata':{'description':'Create a database'},'args':{'name':{'description':'Database name','demandOption':True}},'positionalArgs':['name']}]})
  _,out,_=self._conv('<WranglerNamespace namespace="d1" />')
  self.assertIn('d1 create',out); self.assertIn('<pre tabindex="0">',out); self.assertIn('Database name',out)
if __name__=='__main__': unittest.main()
