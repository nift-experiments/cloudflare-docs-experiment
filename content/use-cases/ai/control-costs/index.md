---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/ai/control-costs/
  description: Reduce AI inference costs and improve reliability with response caching, rate limiting, and unified provider analytics.
  full_title: Control costs and improve quality · Cloudflare use cases
  head_html: <title>Control costs and improve quality · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Reduce AI inference costs and improve reliability with response caching, rate limiting, and unified provider analytics."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/ai/control-costs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/ai/control-costs/index.md"><meta property="og:title" content="Control costs and improve quality · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reduce AI inference costs and improve reliability with response caching, rate limiting, and unified provider analytics."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/ai/control-costs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,AI Gateway,Workers Analytics Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/ai/control-costs/#page","headline":"Control costs and improve quality \u00b7 Cloudflare use cases","description":"Reduce AI inference costs and improve reliability with response caching, rate limiting, and unified provider analytics.","url":"https://developers.cloudflare.com/use-cases/ai/control-costs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/ai/control-costs/
  schema: 1
---
<p>AI inference costs can grow unpredictably as your application scales, especially when using multiple providers. Cloudflare AI Gateway caches identical queries to avoid redundant inference calls, applies rate limits per user or API key, and provides unified analytics across all providers.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="ai-gateway">AI Gateway</h3>
<p>Cache responses, rate limit requests, and monitor usage across providers. <a href="/ai-gateway/">Learn more about AI Gateway</a>.</p>
<ul>
<li><strong>Response caching</strong> - Cache identical queries so repeated prompts do not trigger a new inference call</li>
<li><strong>Rate limiting</strong> - Set request limits per user or Application Programming Interface (API) key to prevent abuse and control spending</li>
<li><strong>Unified analytics</strong> - Track usage, latency, and cost across all AI providers from one dashboard</li>
</ul>
<h3 id="workers-analytics-engine">Workers Analytics Engine</h3>
<p>Store and query time-series analytics data from Workers. <a href="/analytics/analytics-engine/">Learn more about Workers Analytics Engine</a>.</p>
<ul>
<li><strong>Custom metrics</strong> - Build AI-specific dashboards tracking tokens, latency distributions, and error rates</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/ai-gateway/get-started/">AI Gateway get started</a></li>
<li><a href="/ai-gateway/features/caching/">Configure caching</a></li>
<li><a href="/analytics/analytics-engine/get-started/">Workers Analytics Engine get started</a></li>
</ol>
