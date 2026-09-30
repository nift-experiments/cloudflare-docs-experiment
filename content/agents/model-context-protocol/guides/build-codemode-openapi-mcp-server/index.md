---
cp9:
  canonical: https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-openapi-mcp-server/
  description: Create Code Mode search and execute MCP tools from an OpenAPI document while keeping credentials in the host Worker.
  full_title: Build a search and execute MCP server · Cloudflare Agents docs
  head_html: <title>Build a search and execute MCP server · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Create Code Mode search and execute MCP tools from an OpenAPI document while keeping credentials in the host Worker."><link rel="canonical" href="https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-openapi-mcp-server/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-openapi-mcp-server/index.md"><meta property="og:title" content="Build a search and execute MCP server · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create Code Mode search and execute MCP tools from an OpenAPI document while keeping credentials in the host Worker."><meta property="og:url" content="https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-openapi-mcp-server/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agents"><meta name="pcx_tags" content="AI,MCP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-openapi-mcp-server/#page","headline":"Build a search and execute MCP server \u00b7 Cloudflare Agents docs","description":"Create Code Mode search and execute MCP tools from an OpenAPI document while keeping credentials in the host Worker.","url":"https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-openapi-mcp-server/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI","MCP"]}</script>
  markdown: true
  noindex: false
  route: /agents/model-context-protocol/guides/build-codemode-openapi-mcp-server/
  schema: 1
---
<p>Use <code>openApiMcpServer()</code> to publish a large OpenAPI service through two Model Context Protocol (MCP) tools:</p>
<ul>
<li><code>search</code> runs model-written code against the OpenAPI document.</li>
<li><code>execute</code> adds a host-provided <code>codemode.request()</code> function.</li>
</ul>
<p>The OpenAPI document stays outside the model context unless search code returns part of it. Authentication remains in the host Worker.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2235.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need a Cloudflare Workers project, an OpenAPI 3.x document, and a host-side method for authenticating API requests.</p>
<p><code>openApiMcpServer()</code> currently returns an SDK v1 server. Serve it through the explicit legacy <code>createLegacyMcpHandler</code> API.</p>
<h2 id="publish-the-service">Publish the service</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2238.md")
</div>
<h2 id="search-the-openapi-document">Search the OpenAPI document</h2>
<p>Call <code>search</code> before <code>execute</code>. Search code can inspect the document without making API requests:</p>
<pre tabindex="0"><code class="language-js">async () =&gt; {&#10;	const spec = await codemode.spec();&#10;	return Object.entries(spec.paths)&#10;		.filter(([path]) =&gt; path.includes(&quot;/orders&quot;))&#10;		.map(([path, operations]) =&gt; ({&#10;			path,&#10;			methods: Object.keys(operations),&#10;		}));&#10;};&#10;</code></pre>
<p>Local OpenAPI <code>$ref</code> values resolve inside the sandbox when code calls <code>codemode.spec()</code>. External references remain unresolved.</p>
<h2 id="call-the-api">Call the API</h2>
<p>The <code>execute</code> tool includes the same <code>codemode.spec()</code> method and the host-provided <code>codemode.request()</code> method:</p>
<pre tabindex="0"><code class="language-js">async () =&gt; {&#10;	const response = await codemode.request({&#10;		method: &quot;GET&quot;,&#10;		path: &quot;/orders&quot;,&#10;		query: { status: &quot;processing&quot;, limit: 20 },&#10;	});&#10;&#10;	return response.items.map(({ id, status }) =&gt; ({ id, status }));&#10;};&#10;</code></pre>
<p>The host callback receives <code>method</code>, <code>path</code>, optional <code>query</code>, optional <code>body</code>, optional <code>contentType</code>, and optional <code>rawBody</code> fields. For exact types, refer to the <a href="/agents/tools/codemode/api-reference/#openapimcpserver"><code>openApiMcpServer()</code> API</a>.</p>
<p>The <code>search</code> and <code>execute</code> tools use fixed example snippets. An optional <code>description</code> is appended to the <code>execute</code> tool description. This function does not use the <code>{{types}}</code> or <code>{{example}}</code> placeholders supported by <a href="/agents/model-context-protocol/guides/build-codemode-mcp-server/"><code>codeMcpServer()</code></a>.</p>
<h2 id="protect-the-api">Protect the API</h2>
<p>The example reads the bearer token before creating the MCP server. Its request callback adds that token to outbound requests. The token never enters the sandbox.</p>
<p><code>openApiMcpServer()</code> does not provide durable approval for each request inside <code>execute</code>. Enforce authorization and any required per-operation approval in the host callback before applying side effects. Validate paths instead of accepting arbitrary origins.</p>
<p>Do not include secrets in the OpenAPI document or API results. Both are available to model-written code.</p>
<p><code>DynamicWorkerExecutor</code> blocks direct external <code>fetch()</code> and <code>connect()</code> calls by default. Generated code reaches the service only through the host request callback.</p>
<h2 id="limit-results">Limit results</h2>
<p>Have model-written code select, map, aggregate, or paginate data before returning. The publisher limits final MCP responses to approximately 6,000 estimated tokens and marks truncated responses with <code>--- TRUNCATED ---</code>.</p>
<p>Truncation does not reduce API work already performed. Return focused identifiers, status fields, counts, and errors that support the model's next decision.</p>
