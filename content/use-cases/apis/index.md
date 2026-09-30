---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/apis/
  description: Build, protect, and monitor APIs with Cloudflare Workers, API Shield, rate limiting, mTLS, and Logpush.
  full_title: APIs and microservices · Use cases · Cloudflare use cases
  head_html: <title>APIs and microservices · Use cases · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Build, protect, and monitor APIs with Cloudflare Workers, API Shield, rate limiting, mTLS, and Logpush."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/apis/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/apis/index.md"><meta property="og:title" content="APIs and microservices · Use cases · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build, protect, and monitor APIs with Cloudflare Workers, API Shield, rate limiting, mTLS, and Logpush."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/apis/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Use cases,Workers,API Shield,WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/use-cases/apis/#page","headline":"APIs and microservices \u00b7 Use cases \u00b7 Cloudflare use cases","description":"Build, protect, and monitor APIs with Cloudflare Workers, API Shield, rate limiting, mTLS, and Logpush.","url":"https://developers.cloudflare.com/use-cases/apis/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/apis/
  schema: 1
---
<p>Build, secure, and manage Application Programming Interfaces (APIs) with rate limiting, authentication, and observability. Cloudflare Workers deploys API handlers globally with automatic scaling. API Shield validates requests against your OpenAPI specification. Rate Limiting prevents abuse. mTLS authenticates machine-to-machine communication. Cloudflare Tunnel and Access secure internal microservices. Logpush and Workers Analytics Engine provide monitoring.</p>
<ul class="directory-listing"><li><a href="/use-cases/apis/deploy-apis/">Deploy APIs at the edge</a></li><li><a href="/use-cases/apis/protect-apis/">Protect your APIs</a></li><li><a href="/use-cases/apis/internal-services/">Connect your internal network services</a></li><li><a href="/use-cases/apis/monitor-apis/">Monitor your APIs</a></li></ul>
<h2 id="architecture-patterns">Architecture patterns</h2>
<h3 id="secure-api-gateway">Secure API gateway</h3>
<p>Protect your APIs with defense in depth:</p>
<ul>
<li><strong>API Shield</strong> validates requests against your OpenAPI schema</li>
<li><strong>Security rules</strong> managed rulesets block SQL injection, XSS, and OWASP Top 10 vulnerabilities</li>
<li><strong>Rate Limiting</strong> prevents abuse and Distributed Denial of Service (DDoS) attacks</li>
<li><strong>mTLS</strong> (mutual TLS) authenticates known clients with certificates</li>
</ul>
<h3 id="edge-native-apis">Edge-native APIs</h3>
<p>Build APIs that run entirely on Cloudflare:</p>
<ul>
<li><strong>Workers</strong> handles request routing and business logic</li>
<li><strong>D1</strong> or <strong>KV</strong> stores application data</li>
<li><strong>Queues</strong> handles async processing and webhooks</li>
</ul>
<h3 id="microservices-mesh">Microservices mesh</h3>
<p>Connect and secure internal services:</p>
<ul>
<li><strong>Cloudflare Tunnel</strong> exposes services without public IPs</li>
<li><strong>Access</strong> enforces identity-based policies between services</li>
<li><strong>Workers</strong> acts as an API gateway for external consumers</li>
</ul>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<h3 id="create-a-new-application">Create a new application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li><a href="https://nodejs.org/">Node.js</a> (version 16.17.0 or later) installed on your machine.</li>
<li><a href="/workers/wrangler/install-and-update/">Wrangler</a> installed.</li>
</ul>
<h3 id="use-an-existing-application">Use an existing application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>A domain <a href="/fundamentals/manage-domains/add-site/">added to Cloudflare</a> with DNS records proxied through Cloudflare. This is required for API Shield, rate limiting, and application security.</li>
<li>For securing internal services with Cloudflare Tunnel and Access: a <a href="/cloudflare-one/setup/">Cloudflare One organization</a> created in the Cloudflare dashboard.</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/15246.md")
</div>
