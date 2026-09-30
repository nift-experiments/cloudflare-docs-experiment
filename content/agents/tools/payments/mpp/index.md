---
cp9:
  canonical: https://developers.cloudflare.com/agents/tools/payments/mpp/
  description: Accept and make payments using Machine Payments Protocol (MPP) with Cloudflare Workers and the Agents SDK.
  full_title: MPP (Machine Payments Protocol) · Cloudflare Agents docs
  head_html: <title>MPP (Machine Payments Protocol) · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Accept and make payments using Machine Payments Protocol (MPP) with Cloudflare Workers and the Agents SDK."><link rel="canonical" href="https://developers.cloudflare.com/agents/tools/payments/mpp/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/tools/payments/mpp/index.md"><meta property="og:title" content="MPP (Machine Payments Protocol) · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Accept and make payments using Machine Payments Protocol (MPP) with Cloudflare Workers and the Agents SDK."><meta property="og:url" content="https://developers.cloudflare.com/agents/tools/payments/mpp/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/agents/tools/payments/mpp/#page","headline":"MPP (Machine Payments Protocol) \u00b7 Cloudflare Agents docs","description":"Accept and make payments using Machine Payments Protocol (MPP) with Cloudflare Workers and the Agents SDK.","url":"https://developers.cloudflare.com/agents/tools/payments/mpp/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/tools/payments/mpp/
  schema: 1
---
<p><a href="https://mpp.dev">Machine Payments Protocol (MPP)</a> is an open protocol for machine-to-machine payments. It standardizes the HTTP <code>402 Payment Required</code> status code with a formal authentication scheme proposed to the <a href="https://paymentauth.org">IETF</a>. MPP gives agents, applications, and people one interface to pay for a service in the same HTTP request.</p>
<p>MPP is payment-method agnostic. It supports stablecoins, cards through Stripe, and custom payment methods. A service can offer more than one method.</p>
<h2 id="how-it-works">How it works</h2>
<ol>
<li>An Agent or HTTP client requests a paid resource.</li>
<li>The service returns <code>402 Payment Required</code> with a payment Challenge.</li>
<li>The client fulfills the payment.</li>
<li>The client retries with a payment Credential.</li>
<li>The service returns the resource with a payment Receipt.</li>
</ol>
<p>HTTP services exchange payment data in authentication headers. Model Context Protocol (MCP) tools use the same flow through JSON-RPC.</p>
<h2 id="payment-intents">Payment intents</h2>
<p>MPP defines three payment intents:</p>
<ul>
<li><strong><code>charge</code></strong> — Collect a one-time payment.</li>
<li><strong><code>session</code></strong> — Charge for measured usage.</li>
<li><strong><code>subscription</code></strong> — Sell recurring access.</li>
</ul>
<p>For more information, refer to <a href="https://mpp.dev/intents/">MPP payment intents</a>.</p>
<h2 id="compatibility-with-x402">Compatibility with x402</h2>
<p>MPP is backwards-compatible with <a href="/agents/tools/payments/x402/">x402</a>. MPP clients can consume existing x402 services without changes to those services.</p>
<h2 id="build-on-cloudflare">Build on Cloudflare</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/2707.md")
</div>
<h2 id="sdks">SDKs</h2>
<p>MPP provides SDKs for TypeScript, Python, Rust, Go, and Ruby. The Cloudflare guides use the TypeScript <a href="https://mpp.dev/sdk/typescript/"><code>mppx</code> SDK</a>.</p>
<p>For current packages and integrations, refer to the <a href="https://mpp.dev/sdk/">MPP SDK documentation</a>.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="https://mpp.dev">mpp.dev</a> — Protocol documentation and guides</li>
<li><a href="https://paymentauth.org">IETF specification</a> — Payment HTTP Authentication Scheme</li>
<li><a href="/ai-crawl-control/features/pay-per-crawl/">Pay Per Crawl</a> — Cloudflare-native web content monetization</li>
</ul>
