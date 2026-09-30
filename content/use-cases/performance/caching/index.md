---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/performance/caching/
  description: Reduce origin load and latency by caching static and dynamic content at 300+ Cloudflare edge locations.
  full_title: Cache content globally · Cloudflare use cases
  head_html: <title>Cache content globally · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Reduce origin load and latency by caching static and dynamic content at 300+ Cloudflare edge locations."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/performance/caching/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/performance/caching/index.md"><meta property="og:title" content="Cache content globally · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reduce origin load and latency by caching static and dynamic content at 300+ Cloudflare edge locations."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/performance/caching/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/performance/caching/#page","headline":"Cache content globally \u00b7 Cloudflare use cases","description":"Reduce origin load and latency by caching static and dynamic content at 300+ Cloudflare edge locations.","url":"https://developers.cloudflare.com/use-cases/performance/caching/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/performance/caching/
  schema: 1
---
<p>Every request that reaches your origin server adds latency and costs. Cloudflare Cache serves static and dynamic content globally, reducing round-trip times for visitors and offloading traffic from your origin.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="cache">Cache</h3>
<p>Cache content at Cloudflare's global network of edge locations. <a href="/cache/">Learn more about Cache</a>.</p>
<ul>
<li><strong>Global distribution</strong> - Content cached in 300+ edge locations so visitors are served from the location nearest to them</li>
<li><strong>Reduced latency</strong> - Cache hits are served directly from the edge, eliminating round-trips to your origin</li>
<li><strong>Customizable cache rules</strong> - Create rules that change how Cloudflare caches content, or transforms requests</li>
<li><strong>Origin offload</strong> - Regional cache tiers intercept repeated requests before they reach your origin server</li>
<li><strong>Persistent caching</strong> - Long-tail content that would normally expire is kept in durable storage, reducing origin fetches for infrequently accessed assets</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/cache/how-to/cache-rules/">Configure Cache Rules</a></li>
<li><a href="/cache/how-to/tiered-cache/">Enable Tiered Cache</a></li>
<li><a href="/cache/advanced-configuration/cache-reserve/">Set up Cache Reserve</a></li>
</ol>
