---
cp9:
  canonical: https://developers.cloudflare.com/agents/harnesses/think/getting-started/
  description: Build a Think chat agent with persistent memory, built-in file tools, custom tools, and streaming, step by step.
  full_title: Getting started · Cloudflare Agents docs
  head_html: <title>Getting started · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Build a Think chat agent with persistent memory, built-in file tools, custom tools, and streaming, step by step."><link rel="canonical" href="https://developers.cloudflare.com/agents/harnesses/think/getting-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/harnesses/think/getting-started/index.md"><meta property="og:title" content="Getting started · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build a Think chat agent with persistent memory, built-in file tools, custom tools, and streaming, step by step."><meta property="og:url" content="https://developers.cloudflare.com/agents/harnesses/think/getting-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/harnesses/think/getting-started/#page","headline":"Getting started \u00b7 Cloudflare Agents docs","description":"Build a Think chat agent with persistent memory, built-in file tools, custom tools, and streaming, step by step.","url":"https://developers.cloudflare.com/agents/harnesses/think/getting-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/harnesses/think/getting-started/
  schema: 1
---
<p>Build a chat agent with persistent memory, built-in file tools, and streaming — step by step.</p>
<p>If you are brand new to Cloudflare Agents, skim <a href="/agents/concepts/what-are-agents/">What are agents?</a> first for the core ideas. Otherwise, you can follow along here from scratch.</p>
<p>By the end of this tutorial you will have a Think agent that:</p>
<ul>
<li>Streams responses to a React chat UI</li>
<li>Has persistent memory the model can read and write</li>
<li>Includes workspace file tools (read, write, edit, find, grep, delete)</li>
<li>Supports custom server-side tools</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Node.js 24+</li>
<li>A Cloudflare account with Workers AI access</li>
<li>Familiarity with TypeScript and Cloudflare Workers</li>
</ul>
<h2 id="1-create-a-project"><ol>
<li>Create a project</li>
</ol></h2>
<pre tabindex="0"><code class="language-sh">mkdir my-think-agent &amp;&amp; cd my-think-agent&#10;npm init -y&#10;</code></pre>
<p>Install dependencies:</p>
<pre tabindex="0"><code class="language-sh">npm install @cloudflare/think @cloudflare/ai-chat agents ai @cloudflare/shell zod workers-ai-provider react react-dom&#10;npm install -D wrangler @cloudflare/vite-plugin @cloudflare/workers-types @vitejs/plugin-react @tailwindcss/vite tailwindcss typescript vite&#10;</code></pre>
<h2 id="2-configure-wrangler"><ol start="2">
<li>Configure wrangler</li>
</ol></h2>
<p>Create <code>wrangler.jsonc</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2161.md")
</div>
<p>Create <code>vite.config.ts</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2162.md")
</div>
<p>Create <code>tsconfig.json</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;extends&quot;: &quot;agents/tsconfig&quot;&#10;}&#10;</code></pre>
<h2 id="3-define-the-agent"><ol start="3">
<li>Define the agent</li>
</ol></h2>
<p>Create <code>src/server.ts</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2163.md")
</div>
<p>This is a working agent. Think automatically provides:</p>
<ul>
<li>WebSocket chat protocol (compatible with <code>useAgentChat</code>)</li>
<li>Message persistence in SQLite</li>
<li>Resumable streaming (page refresh replays buffered chunks)</li>
<li>Workspace file tools (read, write, edit, list, find, grep, delete)</li>
<li>Abort/cancel support</li>
<li>Error handling with partial message persistence</li>
</ul>
<h2 id="4-connect-a-react-client"><ol start="4">
<li>Connect a React client</li>
</ol></h2>
<p>Create <code>src/client.tsx</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2164.md")
</div>
<p>Create <code>index.html</code>:</p>
<pre tabindex="0"><code class="language-html">&lt;!doctype html&gt;&#10;&lt;html lang=&quot;en&quot;&gt;&#10;	&lt;head&gt;&#10;		&lt;meta charset=&quot;UTF-8&quot; /&gt;&#10;		&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot; /&gt;&#10;		&lt;title&gt;Think Agent&lt;/title&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;		&lt;div id=&quot;root&quot;&gt;&lt;/div&gt;&#10;		&lt;script type=&quot;module&quot; src=&quot;/src/client.tsx&quot;&gt;&lt;/script&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<h2 id="5-run-it"><ol start="5">
<li>Run it</li>
</ol></h2>
<pre tabindex="0"><code class="language-sh">npx vite dev&#10;</code></pre>
<p>Open the browser and send a message. The agent responds with streaming text, and workspace file tools are available to the model automatically.</p>
<h2 id="6-add-persistent-memory"><ol start="6">
<li>Add persistent memory</li>
</ol></h2>
<p>Override <code>configureSession</code> to give the model writable memory that survives restarts:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2165.md")
</div>
<p>Now the model sees a <code>MEMORY</code> section in its system prompt and gets a <code>set_context</code> tool to update it. Facts written to memory persist in SQLite and survive Durable Object hibernation and restarts.</p>
<p>When you use <code>configureSession</code>, the system prompt is built from context blocks rather than <code>getSystemPrompt()</code>. The <code>&quot;soul&quot;</code> block above acts as the system identity — it is read-only and always appears first. The <code>&quot;memory&quot;</code> block is writable, and the model proactively updates it when it learns something useful.</p>
<p>Refer to the <a href="/agents/runtime/lifecycle/sessions/">Sessions documentation</a> for context blocks, compaction, search, skills, and multi-session support.</p>
<h2 id="7-add-custom-tools"><ol start="7">
<li>Add custom tools</li>
</ol></h2>
<p>Override <code>getTools()</code> to add your own tools alongside the built-in workspace tools:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2166.md")
</div>
<p>Think merges tools from multiple sources automatically. On every turn, the model has access to:</p>
<ol>
<li><strong>Workspace tools</strong> — read, write, edit, list, find, grep, delete, bash (built-in)</li>
<li><strong>Your tools</strong> — from <code>getTools()</code></li>
<li><strong>Extension tools</strong> — from loaded extensions</li>
<li><strong>Session tools</strong> — set_context, load_context, search_context (from <code>configureSession</code>)</li>
<li><strong>Skill tools</strong> — activate_skill, read_skill_resource, and optional run_skill_script (from <code>getSkills()</code>)</li>
<li><strong>MCP tools</strong> — from connected MCP servers (if any)</li>
<li><strong>Client tools</strong> — from the browser (if any)</li>
</ol>
<h2 id="8-add-lifecycle-hooks"><ol start="8">
<li>Add lifecycle hooks</li>
</ol></h2>
<p>Think provides hooks that fire on every turn, regardless of entry path:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2167.md")
</div>
<p>Refer to <a href="/agents/harnesses/think/lifecycle-hooks/">Lifecycle hooks</a> for the full reference.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/agents/harnesses/think/lifecycle-hooks/">Lifecycle hooks</a> — control model behavior, switch models per-turn, restrict tools</li>
<li><a href="/agents/harnesses/think/tools/">Tools</a> — workspace tools, code execution, extensions</li>
<li><a href="/agents/harnesses/think/client-tools/">Client tools</a> — browser-side tools, approval flows, concurrency</li>
<li><a href="/agents/harnesses/think/sub-agents/">Sub-agent RPC and programmatic turns</a> — RPC streaming, scheduled turns, recovery</li>
<li><a href="/agents/runtime/lifecycle/sessions/">Sessions</a> — context blocks, compaction, search, multi-session</li>
</ul>
