---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-17-codemode-sdk-v0.2.1/
  description: New updates and improvements at Cloudflare.
  full_title: '@cloudflare/codemode v0.2.1: MCP barrel export, zero-dependency main entry point, and custom sandbox modules · Changelog'
  head_html: '<title>@cloudflare/codemode v0.2.1: MCP barrel export, zero-dependency main entry point, and custom sandbox modules · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-17-codemode-sdk-v0.2.1/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="@cloudflare/codemode v0.2.1: MCP barrel export, zero-dependency main entry point, and custom sandbox modules · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-17-codemode-sdk-v0.2.1/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-17-codemode-sdk-v0.2.1/#page","headline":"@cloudflare/codemode v0.2.1: MCP barrel export, zero-dependency main entry point, and custom sandbox modules \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-17-codemode-sdk-v0.2.1/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>'
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-17-codemode-sdk-v0.2.1/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 17, 2026</time><h2 id="post-title">@cloudflare/codemode v0.2.1: MCP barrel export, zero-dependency main entry point, and custom sandbox modules</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest releases of <a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a> add a new MCP barrel export, remove <code>ai</code> and <code>zod</code> as required peer dependencies from the main entry point, and give you more control over the sandbox.</p>
<h4 id="new-cloudflare-codemode-mcp-export">New <code>@cloudflare/codemode/mcp</code> export</h4>
<p>A new <code>@cloudflare/codemode/mcp</code> entry point provides two functions that wrap MCP servers with Code Mode:</p>
<ul>
<li><strong><code>codeMcpServer({ server, executor })</code></strong> — wraps an existing MCP server with a single <code>code</code> tool where each upstream tool becomes a typed <code>codemode.*</code> method.</li>
<li><strong><code>openApiMcpServer({ spec, executor, request })</code></strong> — creates <code>search</code> and <code>execute</code> MCP tools from an OpenAPI spec with host-side request proxying and automatic <code>$ref</code> resolution.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17652.md")</div>
<h4 id="zero-dependency-main-entry-point">Zero-dependency main entry point</h4>
<p><strong>Breaking change in v0.2.0:</strong> <code>generateTypes</code> and the <code>ToolDescriptor</code> / <code>ToolDescriptors</code> types have moved to <code>@cloudflare/codemode/ai</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17653.md")</div>
<p>The main entry point (<code>@cloudflare/codemode</code>) no longer requires the <code>ai</code> or <code>zod</code> peer dependencies. It now exports:</p>
<table>
<thead>
<tr>
<th>Export</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sanitizeToolName</code></td>
<td>Sanitize tool names into valid JS identifiers</td>
</tr>
<tr>
<td><code>normalizeCode</code></td>
<td>Normalize LLM-generated code into async arrow functions</td>
</tr>
<tr>
<td><code>generateTypesFromJsonSchema</code></td>
<td>Generate TypeScript type definitions from plain JSON Schema</td>
</tr>
<tr>
<td><code>jsonSchemaToType</code></td>
<td>Convert a single JSON Schema to a TypeScript type string</td>
</tr>
<tr>
<td><code>DynamicWorkerExecutor</code></td>
<td>Sandboxed code execution via Dynamic Worker Loader</td>
</tr>
<tr>
<td><code>ToolDispatcher</code></td>
<td>RPC target for dispatching tool calls from sandbox to host</td>
</tr>
</tbody>
</table>
<p>The <code>ai</code> and <code>zod</code> peer dependencies are now optional — only required when importing from <code>@cloudflare/codemode/ai</code>.</p>
<h4 id="custom-sandbox-modules">Custom sandbox modules</h4>
<p><code>DynamicWorkerExecutor</code> now accepts an optional <code>modules</code> option to inject custom ES modules into the sandbox:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17654.md")</div>
<h4 id="internal-normalization-and-sanitization">Internal normalization and sanitization</h4>
<p><code>DynamicWorkerExecutor</code> now normalizes code and sanitizes tool names internally. You no longer need to call <code>normalizeCode()</code> or <code>sanitizeToolName()</code> before passing code and functions to <code>execute()</code>.</p>
<h4 id="upgrade">Upgrade</h4>
<pre tabindex="0"><code class="language-sh">npm i @cloudflare/codemode@latest&#10;</code></pre>
<p>See the <a href="/agents/tools/codemode/">Code Mode documentation</a> for the full API reference.</p>
</div></article></div>
