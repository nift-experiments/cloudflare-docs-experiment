---
cp9:
  canonical: https://developers.cloudflare.com/agents/tools/payments/mpp/accept-payments/
  description: Accept Machine Payments Protocol (MPP) payments from an origin, Cloudflare Worker route, or Model Context Protocol (MCP) tool.
  full_title: Accept payments with MPP · Cloudflare Agents docs
  head_html: <title>Accept payments with MPP · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Accept Machine Payments Protocol (MPP) payments from an origin, Cloudflare Worker route, or Model Context Protocol (MCP) tool."><link rel="canonical" href="https://developers.cloudflare.com/agents/tools/payments/mpp/accept-payments/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/tools/payments/mpp/accept-payments/index.md"><meta property="og:title" content="Accept payments with MPP · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Accept Machine Payments Protocol (MPP) payments from an origin, Cloudflare Worker route, or Model Context Protocol (MCP) tool."><meta property="og:url" content="https://developers.cloudflare.com/agents/tools/payments/mpp/accept-payments/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/tools/payments/mpp/accept-payments/#page","headline":"Accept payments with MPP \u00b7 Cloudflare Agents docs","description":"Accept Machine Payments Protocol (MPP) payments from an origin, Cloudflare Worker route, or Model Context Protocol (MCP) tool.","url":"https://developers.cloudflare.com/agents/tools/payments/mpp/accept-payments/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/tools/payments/mpp/accept-payments/
  schema: 1
---
<p>Use Cloudflare Workers to accept Machine Payments Protocol (MPP) payments. Choose an integration based on the service you want to protect:</p>
<ul>
<li><a href="https://github.com/cloudflare/mpp-proxy"><code>mpp-proxy</code></a> — Charge for HTTP content without changing your origin code. Refer to <a href="/agents/tools/payments/mpp-charge-for-http-content/">Charge for HTTP content</a>.</li>
<li><strong>Worker route</strong> — Add <code>mppx</code> payment middleware to a Worker application.</li>
<li><strong>MCP tool</strong> — Require payment before an MCP tool returns its result.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<p>Create a <a href="/fundamentals/account/create-account/">Cloudflare account</a>. You also need a payment recipient and an MPP secret key.</p>
<p>The examples use a stablecoin payment method on testnet. For other methods, refer to <a href="https://mpp.dev/payment-methods/">MPP payment methods</a>.</p>
<h2 id="charge-for-a-worker-route">Charge for a Worker route</h2>
<p>Add <code>mppx</code> middleware when you control the Worker application:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2709.md")
</div>
<h2 id="charge-for-an-mcp-tool">Charge for an MCP tool</h2>
<p>Add the MPP transport to an <a href="/agents/model-context-protocol/apis/agent-api/"><code>McpAgent</code></a>:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2712.md")
</div>
<p>To test both payment flows from a Cloudflare Agent, refer to <a href="/agents/tools/payments/mpp/pay-from-agents-sdk/">Pay from the Agents SDK</a>. For production billing patterns, refer to <a href="https://mpp.dev/intents/">MPP payment intents</a>.</p>
