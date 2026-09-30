---
cp9:
  canonical: https://developers.cloudflare.com/agents/tools/payments/mpp/pay-from-agents-sdk/
  description: Configure a Cloudflare Agent to pay HTTP services and Model Context Protocol (MCP) tools with Machine Payments Protocol (MPP).
  full_title: Pay from the Agents SDK · Cloudflare Agents docs
  head_html: <title>Pay from the Agents SDK · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure a Cloudflare Agent to pay HTTP services and Model Context Protocol (MCP) tools with Machine Payments Protocol (MPP)."><link rel="canonical" href="https://developers.cloudflare.com/agents/tools/payments/mpp/pay-from-agents-sdk/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/tools/payments/mpp/pay-from-agents-sdk/index.md"><meta property="og:title" content="Pay from the Agents SDK · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure a Cloudflare Agent to pay HTTP services and Model Context Protocol (MCP) tools with Machine Payments Protocol (MPP)."><meta property="og:url" content="https://developers.cloudflare.com/agents/tools/payments/mpp/pay-from-agents-sdk/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/tools/payments/mpp/pay-from-agents-sdk/#page","headline":"Pay from the Agents SDK \u00b7 Cloudflare Agents docs","description":"Configure a Cloudflare Agent to pay HTTP services and Model Context Protocol (MCP) tools with Machine Payments Protocol (MPP).","url":"https://developers.cloudflare.com/agents/tools/payments/mpp/pay-from-agents-sdk/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/tools/payments/mpp/pay-from-agents-sdk/
  schema: 1
---
<p>Use the Cloudflare Agents SDK to pay MPP services. The <code>mppx</code> SDK handles payment retries for HTTP requests and Model Context Protocol (MCP) tool calls.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Create a <a href="/agents/getting-started/">Cloudflare Agents project</a>. Fund an account for the payment method that the service accepts.</p>
<h2 id="configure-payments">Configure payments</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2704.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2702.md")
</aside>
<h2 id="pay-an-http-service">Pay an HTTP service</h2>
<p>Create a payment-aware client in <code>onStart()</code>. Restrict automatic payments to trusted origins:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2705.md")
</div>
<p>Free endpoints pass through unchanged. Paid endpoints trigger the payment retry and return a <code>Payment-Receipt</code> header.</p>
<h2 id="pay-an-mcp-tool">Pay an MCP tool</h2>
<p>Connect the Agent with <code>addMcpServer()</code>. Wait for the connection before wrapping its client:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2706.md")
</div>
<p>If <code>paidSearch()</code> returns an <code>authUrl</code>, send the user to that URL and retry after authorization.</p>
<p>The wrapper retries a paid tool call with an MPP Credential. The result includes the MPP Receipt as <code>result.receipt</code>.</p>
<p>By default, both clients pay compatible Challenges automatically. Use <code>onChallenge</code> for HTTP or <code>onPaymentRequired</code> for MCP when a payment needs approval. Challenge amounts are integer base units, not decimal display values.</p>
<h2 id="pay-x402-services">Pay x402 services</h2>
<p>The <code>mppx</code> HTTP client also recognizes x402 Challenges. Configure an x402-compatible EVM method next to the MPP method. The service does not need changes. For configuration, refer to <a href="https://mpp.dev/guides/use-mpp-with-x402">Use MPP with x402</a>.</p>
<p>To accept payments, refer to <a href="/agents/tools/payments/mpp/accept-payments/">Accept payments with MPP</a>. For MCP connection options, refer to the <a href="/agents/model-context-protocol/apis/client-api/">MCP client API</a>.</p>
