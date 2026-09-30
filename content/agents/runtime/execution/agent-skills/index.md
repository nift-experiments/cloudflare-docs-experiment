---
cp9:
  canonical: https://developers.cloudflare.com/agents/runtime/execution/agent-skills/
  description: Give an agent a catalog of on-demand instructions, resources, and scripts with agents/skills, activated by the model only when a task matches.
  full_title: Agent Skills · Cloudflare Agents docs
  head_html: <title>Agent Skills · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Give an agent a catalog of on-demand instructions, resources, and scripts with agents/skills, activated by the model only when a task matches."><link rel="canonical" href="https://developers.cloudflare.com/agents/runtime/execution/agent-skills/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/runtime/execution/agent-skills/index.md"><meta property="og:title" content="Agent Skills · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Give an agent a catalog of on-demand instructions, resources, and scripts with agents/skills, activated by the model only when a task matches."><meta property="og:url" content="https://developers.cloudflare.com/agents/runtime/execution/agent-skills/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/runtime/execution/agent-skills/#page","headline":"Agent Skills \u00b7 Cloudflare Agents docs","description":"Give an agent a catalog of on-demand instructions, resources, and scripts with agents/skills, activated by the model only when a task matches.","url":"https://developers.cloudflare.com/agents/runtime/execution/agent-skills/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/runtime/execution/agent-skills/
  schema: 1
---
<p>Agent Skills are on-demand instructions, resources, and scripts. A skill source provides a catalog of skill names and descriptions; the agent adds that catalog to the system prompt and exposes tools the model can use when a user task matches a skill — so a large library of capabilities does not bloat every prompt.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2561.md")
</aside>
<p>The skills engine lives in <code>agents/skills</code> and is framework-agnostic, so any agent (including a plain <a href="/agents/communication-channels/chat/chat-agents/"><code>AIChatAgent</code></a> <code>onChatMessage</code>) can build a <code>SkillRegistry</code>. <a href="/agents/harnesses/think/"><code>@cloudflare/think</code></a> re-exports it as the <code>skills</code> namespace and wires <code>getSkills()</code> into the turn automatically.</p>
<h2 id="using-skills-with-think">Using skills with Think</h2>
<p>Bundled skills are usually imported with the Agents Vite plugin:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2562.md")
</div>
<p><code>agents:skills</code> resolves to a <code>./skills</code> directory next to the importing file; use <code>agents:skills/&lt;dir&gt;</code> to point at a differently named sibling directory. The <code>agents:skills</code> import is typed by ambient declarations that ship with <code>agents</code>, so importing <code>Think</code> in the same file brings the type into scope (for a file that imports only the specifier, add <code>/// &lt;reference types=&quot;agents/skills-module&quot; /&gt;</code>). If you are not using the Agents Vite plugin, build a source with <code>skills.fromManifest(...)</code> instead.</p>
<p>Sources are applied in order; the first source to register a skill name wins, and later duplicates (or a source that fails to load) are skipped with a logged warning rather than failing the agent.</p>
<p>The imported directory should contain one child directory per skill:</p>
<pre tabindex="0"><code class="language-text">src/skills/release-notes/SKILL.md&#10;src/skills/release-notes/scripts/format-release-notes.ts&#10;src/skills/release-notes/references/style-guide.md&#10;</code></pre>
<h2 id="skill-tools">Skill tools</h2>
<p>When skills are available, the agent exposes:</p>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>activate_skill</code></td>
<td>Load a matching skill's instructions and bundled resource list</td>
</tr>
<tr>
<td><code>read_skill_resource</code></td>
<td>Read a bundled resource by <code>{ name, path }</code> or <code>skill-name/path</code></td>
</tr>
<tr>
<td><code>run_skill_script</code></td>
<td>Run a bundled script when <code>getSkillScriptRunner()</code> returns a runner</td>
</tr>
</tbody>
</table>
<p>Skills are not always-on system prompt text. Use <code>getSystemPrompt()</code> or a Session context block for behavior that should apply to every turn. Use skills for task-specific procedures, references, scripts, templates, and assets that should be loaded only when relevant.</p>
<h2 id="script-execution">Script execution</h2>
<p>Script execution is opt-in and requires a Worker Loader binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2563.md")
</div>
<p><code>skills.runner()</code> is experimental and runs JavaScript, TypeScript, Python, and Bash scripts under <code>scripts/</code>. TypeScript is compiled with <code>@cloudflare/worker-bundler</code>; Python runs as Python Dynamic Workers; Bash runs through <code>just-bash</code>.</p>
<p>JavaScript and TypeScript scripts are function-style:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2564.md")
</div>
<p><code>ctx</code> is <code>{ skill, files, workspace, tools, output }</code>. <code>ctx.files</code> holds bundled text resources by relative path, <code>ctx.workspace</code> is gated by the workspace permission, <code>ctx.tools</code> only exposes tools the runner was given, and <code>ctx.output.writeFile(name, content)</code> returns scratch artifacts to the model (it does not mutate the workspace). Python and Bash use the path-based contract instead: <code>/input.json</code>, <code>/context.json</code>, bundled resources under <code>/skill</code>, and <code>/output</code> for artifacts.</p>
<p>Passing <code>workspaceInstance</code> gives scripts read-only workspace access by default. Network access, tools, and workspace writes are opt-in. The default timeout is 30 seconds.</p>
<h2 id="example">Example</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2565.md")
</div>
<p>Refer to the <a href="https://github.com/cloudflare/agents/tree/main/examples/agent-skills"><code>agent-skills</code> example</a> for bundled skills, R2-backed skills, and script execution.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/agents/harnesses/think/">Think</a> — wires <code>getSkills()</code> and <code>getSkillScriptRunner()</code> into the agentic loop</li>
<li><a href="/agents/harnesses/think/tools/">Think tools</a> — how skill tools merge with workspace, custom, MCP, and client tools</li>
</ul>
