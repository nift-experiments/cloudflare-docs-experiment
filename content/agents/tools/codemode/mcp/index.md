---
cp9:
  canonical: https://developers.cloudflare.com/agents/tools/codemode/mcp/
  description: Expose tools from an existing MCP connection to models through a durable Code Mode runtime.
  full_title: Use MCP tools with Code Mode · Cloudflare Agents docs
  head_html: <title>Use MCP tools with Code Mode · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Expose tools from an existing MCP connection to models through a durable Code Mode runtime."><link rel="canonical" href="https://developers.cloudflare.com/agents/tools/codemode/mcp/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/tools/codemode/mcp/index.md"><meta property="og:title" content="Use MCP tools with Code Mode · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Expose tools from an existing MCP connection to models through a durable Code Mode runtime."><meta property="og:url" content="https://developers.cloudflare.com/agents/tools/codemode/mcp/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/tools/codemode/mcp/#page","headline":"Use MCP tools with Code Mode \u00b7 Cloudflare Agents docs","description":"Expose tools from an existing MCP connection to models through a durable Code Mode runtime.","url":"https://developers.cloudflare.com/agents/tools/codemode/mcp/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/tools/codemode/mcp/
  schema: 1
---
<p>Use <code>McpConnector</code> to expose tools from an existing Model Context Protocol (MCP) client connection inside the Code Mode sandbox. The connector works with the durable runtime, including discovery, approvals, and execution history.</p>
<p>This page covers an Agent consuming an MCP server. To publish Code Mode as an MCP server, refer to <a href="/agents/model-context-protocol/codemode/">Code Mode MCP server patterns</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need:</p>
<ul>
<li>A project with the <a href="/agents/tools/codemode/durable-runtime/">durable Code Mode runtime</a> configured. That setup provides the Worker Loader binding and the <code>CodemodeRuntime</code> export.</li>
<li>An existing Agents SDK MCP connection. To create and authorize the connection, refer to the <a href="/agents/model-context-protocol/apis/client-api/">McpClient API</a>.</li>
</ul>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2670.md")
</div>
<p>When the model calls <code>github.create_issue()</code>, the runtime returns a paused execution. Approve that execution through the runtime to execute the MCP tool and continue the same sandbox program.</p>
<h2 id="use-an-ai-sdk-tool-collection">Use an AI SDK tool collection</h2>
<p>For a smaller integration without durable approvals or <code>codemode.search()</code> and <code>codemode.describe()</code>, pass the Agents SDK tool collection directly to <code>createCodeTool()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2671.md")
</div>
<p>This approach exposes the MCP tools under the default <code>codemode</code> namespace. It does not use the connector runtime's durable pause, approval, and resume flow. Use <code>McpConnector</code> when tools can cause side effects or when the model needs on-demand discovery.</p>
<p><code>getAITools()</code> converts MCP input and output schemas for use by the AI SDK. The Agents SDK reuses those converted schemas while each live connection keeps the same current catalog. Use <code>this.mcp.listTools()</code> instead when you only need to inspect the raw MCP catalog.</p>
