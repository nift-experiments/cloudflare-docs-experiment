---
cp9:
  canonical: https://developers.cloudflare.com/agents/tools/mcp/
  description: Connect agents to external Model Context Protocol servers and use their tools in model calls.
  full_title: MCP · Cloudflare Agents docs
  head_html: <title>MCP · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect agents to external Model Context Protocol servers and use their tools in model calls."><link rel="canonical" href="https://developers.cloudflare.com/agents/tools/mcp/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/tools/mcp/index.md"><meta property="og:title" content="MCP · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect agents to external Model Context Protocol servers and use their tools in model calls."><meta property="og:url" content="https://developers.cloudflare.com/agents/tools/mcp/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/tools/mcp/#page","headline":"MCP \u00b7 Cloudflare Agents docs","description":"Connect agents to external Model Context Protocol servers and use their tools in model calls.","url":"https://developers.cloudflare.com/agents/tools/mcp/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/tools/mcp/
  schema: 1
---
<p>Agents can use <a href="/agents/model-context-protocol/">Model Context Protocol (MCP)</a> as clients. Connect an agent to external MCP servers, discover the tools those servers expose, and pass those tools into model calls.</p>
<p>Use MCP when you want an agent to:</p>
<ul>
<li>Call tools exposed by external MCP servers.</li>
<li>Reuse tools across agents, IDEs, and other AI clients.</li>
<li>Connect to services that already expose an MCP endpoint.</li>
<li>Add OAuth or token-based authorization around external tool access.</li>
</ul>
<p>To build an MCP server instead, refer to <a href="/agents/model-context-protocol/">Model Context Protocol (MCP)</a>.</p>
<h2 id="basic-pattern">Basic pattern</h2>
<p>Call <code>addMcpServer()</code> to connect to a remote MCP server, then pass <code>this.mcp.getAITools()</code> to the AI SDK.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1843.md")
</div>
<p>If the server requires OAuth, <code>addMcpServer()</code> returns an authentication state and authorization URL. The connection is persisted in the agent's <a href="/agents/runtime/lifecycle/state/">SQL storage</a>.</p>
<h2 id="configuration">Configuration</h2>
<p>For public MCP servers, no binding configuration is required. Store server URLs, API tokens, or OAuth settings as environment variables or secrets.</p>
<p>For MCP servers that require bearer tokens or Cloudflare Access headers, pass custom transport headers when connecting.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1844.md")
</div>
<h2 id="related-resources">Related resources</h2>
<div class="nb-card nb-link-card"><h3 id="card-mcpclient-api-agents-model-context-protocol-apis-client-api"><a href="/agents/model-context-protocol/apis/client-api/">McpClient API</a></h3><p>Connect Agents to external MCP servers and use their tools, resources, and prompts.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-connect-to-an-mcp-server-agents-model-context-protocol-guides-connect-mcp-client"><a href="/agents/model-context-protocol/guides/connect-mcp-client/">Connect to an MCP server</a></h3><p>Create an Agent that connects to an external MCP server and uses its tools.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-use-mcp-tools-with-code-mode-agents-tools-codemode-mcp"><a href="/agents/tools/codemode/mcp/">Use MCP tools with Code Mode</a></h3><p>Use progressive discovery, code-based composition, and durable approvals with MCP tools.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-model-context-protocol-specification-https-modelcontextprotocol-io"><a href="https://modelcontextprotocol.io/">Model Context Protocol specification</a></h3><p>Learn about the open protocol for connecting AI applications to external tools and data.</p></div>
