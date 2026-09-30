---
cp9:
  canonical: https://developers.cloudflare.com/agents/model-context-protocol/guides/connect-mcp-client/
  description: Create a Cloudflare Agent that connects to an external MCP server and uses its tools.
  full_title: Connect to an MCP server · Cloudflare Agents docs
  head_html: <title>Connect to an MCP server · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a Cloudflare Agent that connects to an external MCP server and uses its tools."><link rel="canonical" href="https://developers.cloudflare.com/agents/model-context-protocol/guides/connect-mcp-client/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/model-context-protocol/guides/connect-mcp-client/index.md"><meta property="og:title" content="Connect to an MCP server · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a Cloudflare Agent that connects to an external MCP server and uses its tools."><meta property="og:url" content="https://developers.cloudflare.com/agents/model-context-protocol/guides/connect-mcp-client/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Agents"><meta name="pcx_tags" content="MCP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/model-context-protocol/guides/connect-mcp-client/#page","headline":"Connect to an MCP server \u00b7 Cloudflare Agents docs","description":"Create a Cloudflare Agent that connects to an external MCP server and uses its tools.","url":"https://developers.cloudflare.com/agents/model-context-protocol/guides/connect-mcp-client/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["MCP"]}</script>
  markdown: true
  noindex: false
  route: /agents/model-context-protocol/guides/connect-mcp-client/
  schema: 1
---
<p>Your Agent can connect to external <a href="https://modelcontextprotocol.io">Model Context Protocol (MCP)</a> servers to access their tools and extend your Agent's capabilities. In this tutorial, you'll create an Agent that connects to an MCP server and uses one of its tools.</p>
<h2 id="what-you-will-build">What you will build</h2>
<p>An Agent with endpoints to:</p>
<ul>
<li>Connect to an MCP server</li>
<li>List available tools from connected servers</li>
<li>Get the connection status</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<p>An MCP server to connect to (or use the public example in this tutorial).</p>
<h2 id="1-create-a-basic-agent"><ol>
<li>Create a basic Agent</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2229.md")
</div>
<h2 id="2-add-mcp-connection-endpoint"><ol start="2">
<li>Add MCP connection endpoint</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2231.md")
</div>
<p>The <code>addMcpServer()</code> method connects to an MCP server. If the server requires OAuth authentication, it returns an <code>authUrl</code> that users must visit to complete authorization.</p>
<h2 id="3-test-the-connection"><ol start="3">
<li>Test the connection</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2232.md")
</div>
<h2 id="4-list-available-tools"><ol start="4">
<li>List available tools</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2234.md")
</div>
<h2 id="summary">Summary</h2>
<p>You created an Agent that can:</p>
<ul>
<li>Connect to external MCP servers dynamically</li>
<li>Handle OAuth authentication flows when required</li>
<li>List all available tools from connected servers</li>
<li>Monitor connection status</li>
</ul>
<p>Connections persist in the Agent's <a href="/agents/runtime/lifecycle/state/">SQL storage</a>, so they remain active across requests.</p>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-handle-oauth-flows-agents-model-context-protocol-guides-oauth-mcp-client"><a href="/agents/model-context-protocol/guides/oauth-mcp-client/">Handle OAuth flows</a></h3><p>Configure OAuth callbacks and error handling.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-mcp-client-api-agents-model-context-protocol-apis-client-api"><a href="/agents/model-context-protocol/apis/client-api/">MCP Client API</a></h3><p>Complete API documentation for MCP clients.</p></div>
