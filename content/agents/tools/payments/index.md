---
cp9:
  canonical: https://developers.cloudflare.com/agents/tools/payments/
  description: Let AI agents pay for services with x402 or Machine Payments Protocol (MPP) through Cloudflare's Agents SDK.
  full_title: Agentic Payments · Cloudflare Agents docs
  head_html: <title>Agentic Payments · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Let AI agents pay for services with x402 or Machine Payments Protocol (MPP) through Cloudflare&#x27;s Agents SDK."><link rel="canonical" href="https://developers.cloudflare.com/agents/tools/payments/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/tools/payments/index.md"><meta property="og:title" content="Agentic Payments · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Let AI agents pay for services with x402 or Machine Payments Protocol (MPP) through Cloudflare&#x27;s Agents SDK."><meta property="og:url" content="https://developers.cloudflare.com/agents/tools/payments/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/agents/tools/payments/#page","headline":"Agentic Payments \u00b7 Cloudflare Agents docs","description":"Let AI agents pay for services with x402 or Machine Payments Protocol (MPP) through Cloudflare's Agents SDK.","url":"https://developers.cloudflare.com/agents/tools/payments/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/tools/payments/
  schema: 1
---
<p>AI agents need to discover, pay for, and consume resources and services programmatically. Traditional onboarding requires account creation, a payment method, and an API key before an agent can pay for a service. Agentic payments let AI agents purchase resources and services directly through the HTTP <code>402 Payment Required</code> response code.</p>
<p>Cloudflare's <a href="/agents/">Agents SDK</a> supports agentic payments through two protocols built on the HTTP <code>402 Payment Required</code> status code: <strong>x402</strong> and <strong>Machine Payments Protocol (MPP)</strong>. Both follow the same core flow:</p>
<ol>
<li>A client requests a resource or calls a tool.</li>
<li>The server returns a payment Challenge describing what to pay, how much, and where.</li>
<li>The client fulfills the payment and retries the request with a payment credential.</li>
<li>The server verifies the payment (optionally through a facilitator service) and returns the resource along with a receipt.</li>
</ol>
<p>No pre-created service account or pre-shared API key is required. Agents handle the payment exchange programmatically.</p>
<h2 id="x402-and-machine-payments-protocol">x402 and Machine Payments Protocol</h2>
<h3 id="x402">x402</h3>
<p><a href="https://www.x402.org/">x402</a> is a payment standard created by Coinbase. It uses on-chain stablecoin payments (USDC on Base, Ethereum, Solana, and other networks) and defines three HTTP headers — <code>PAYMENT-REQUIRED</code>, <code>PAYMENT-SIGNATURE</code>, and <code>PAYMENT-RESPONSE</code> — to carry challenges, credentials, and receipts. Servers can offload verification and settlement to a <strong>facilitator</strong> service so they do not need direct blockchain connectivity. It is governed by Coinbase and Cloudflare, two of the founding members of the x402 Foundation.</p>
<p>The Agents SDK provides first-class x402 integration:</p>
<ul>
<li><strong>Server-side</strong>: <code>withX402</code> and <code>paidTool</code> for Model Context Protocol (MCP) servers, plus <code>x402-hono</code> middleware for HTTP Workers.</li>
<li><strong>Client-side</strong>: <code>withX402Client</code> wraps MCP connections with automatic <code>402</code> handling and optional human approval.</li>
</ul>
<h3 id="machine-payments-protocol">Machine Payments Protocol</h3>
<p><a href="https://mpp.dev">Machine Payments Protocol (MPP)</a> is an open payment protocol. It adds the <code>WWW-Authenticate: Payment</code> and <code>Authorization: Payment</code> headers to HTTP <code>402</code> responses.</p>
<p>MPP supports multiple payment methods beyond blockchains, including cards (via Stripe) and stablecoins. The <code>mppx</code> SDK supports one-time, usage-based, and recurring payments. MPP is also backwards-compatible with x402: MPP clients can consume existing x402 services without modification.</p>
<h2 id="build-with-agentic-payments">Build with agentic payments</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/2658.md")
</div>
<h2 id="related">Related</h2>
<ul>
<li><a href="https://x402.org">x402.org</a> — x402 protocol specification</li>
<li><a href="https://mpp.dev">mpp.dev</a> — MPP protocol specification</li>
<li><a href="/ai-crawl-control/features/pay-per-crawl/">Pay Per Crawl</a> — Cloudflare-native monetization for web content</li>
<li><a href="https://github.com/cloudflare/agents/tree/main/examples">x402 examples</a> — Complete working code</li>
</ul>
