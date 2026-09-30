---
cp9:
  canonical: https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-mcp-server/
  description: Replace an MCP server's individual tools with one sandboxed Code Mode tool on Cloudflare Workers.
  full_title: Build a single-tool Code Mode MCP server · Cloudflare Agents docs
  head_html: <title>Build a single-tool Code Mode MCP server · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Replace an MCP server&#x27;s individual tools with one sandboxed Code Mode tool on Cloudflare Workers."><link rel="canonical" href="https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-mcp-server/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-mcp-server/index.md"><meta property="og:title" content="Build a single-tool Code Mode MCP server · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Replace an MCP server&#x27;s individual tools with one sandboxed Code Mode tool on Cloudflare Workers."><meta property="og:url" content="https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-mcp-server/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agents"><meta name="pcx_tags" content="AI,MCP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-mcp-server/#page","headline":"Build a single-tool Code Mode MCP server \u00b7 Cloudflare Agents docs","description":"Replace an MCP server's individual tools with one sandboxed Code Mode tool on Cloudflare Workers.","url":"https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-mcp-server/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI","MCP"]}</script>
  markdown: true
  noindex: false
  route: /agents/model-context-protocol/guides/build-codemode-mcp-server/
  schema: 1
---
<p>Use <code>codeMcpServer()</code> to wrap an existing Model Context Protocol (MCP) server. MCP clients receive one <code>code</code> tool instead of every upstream tool.</p>
<p>The <code>code</code> tool contains generated type definitions for the upstream tools. Model-written JavaScript can call several tools, process their results, and return one focused value.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2239.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need a Cloudflare Workers project and an existing <code>McpServer</code>.</p>
<p><code>codeMcpServer()</code> currently returns an SDK v1 server. Serve it through the explicit legacy <code>createLegacyMcpHandler</code> API.</p>
<h2 id="wrap-the-server">Wrap the server</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2242.md")
</div>
<p>The model can use the generated <code>codemode</code> namespace inside the <code>code</code> tool:</p>
<pre tabindex="0"><code class="language-js">async () =&gt; {&#10;	const order = await codemode.get_order({ orderId: &quot;order-123&quot; });&#10;	return { id: order.id, status: order.status };&#10;};&#10;</code></pre>
<p>When an upstream tool returns <code>structuredContent</code>, Code Mode exposes that value directly. Text-only content is joined and parsed as JSON when possible. Upstream MCP errors become exceptions that model-written code can catch. Mixed text and binary content remains in its MCP result structure.</p>
<p>If you provide a custom <code>description</code>, use <code>{{types}}</code> where the generated TypeScript declarations should appear. Use <code>{{example}}</code> where the SDK should insert an example call based on the first upstream MCP tool. Both placeholders are optional.</p>
<h2 id="protect-upstream-operations">Protect upstream operations</h2>
<p><code>codeMcpServer()</code> does not provide durable approval for each upstream tool call. It invokes upstream handlers from inside the outer <code>code</code> tool.</p>
<p>Enforce authorization and any required per-operation approval in each upstream handler before applying side effects. Do not include credentials in tool results.</p>
<p><code>DynamicWorkerExecutor</code> blocks external <code>fetch()</code> and <code>connect()</code> calls by default. Generated code can reach external systems only through the upstream MCP tools.</p>
<h2 id="limit-results">Limit results</h2>
<p>Model-written code can select, map, aggregate, or paginate upstream data before returning. This prevents large intermediate results from entering the model context.</p>
<p>The publisher limits the final MCP response to approximately 6,000 estimated tokens. A larger response is cut off and includes a <code>--- TRUNCATED ---</code> marker. This does not reduce work already performed by upstream tools.</p>
<p>To publish an OpenAPI service with separate <code>search</code> and <code>execute</code> tools, refer to <a href="/agents/model-context-protocol/guides/build-codemode-openapi-mcp-server/">Build a search and execute MCP server</a>.</p>
