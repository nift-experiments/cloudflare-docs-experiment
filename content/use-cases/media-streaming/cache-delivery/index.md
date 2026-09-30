---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/media-streaming/cache-delivery/
  description: Deliver media content from edge locations worldwide.
  full_title: Cache and accelerate media delivery · Cloudflare use cases
  head_html: <title>Cache and accelerate media delivery · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Deliver media content from edge locations worldwide."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/media-streaming/cache-delivery/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/media-streaming/cache-delivery/index.md"><meta property="og:title" content="Cache and accelerate media delivery · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deliver media content from edge locations worldwide."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/media-streaming/cache-delivery/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,Cache / CDN,Argo Smart Routing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/media-streaming/cache-delivery/#page","headline":"Cache and accelerate media delivery \u00b7 Cloudflare use cases","description":"Deliver media content from edge locations worldwide.","url":"https://developers.cloudflare.com/use-cases/media-streaming/cache-delivery/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/media-streaming/cache-delivery/
  schema: 1
---
<p>Streaming video and serving images to a global audience requires low-latency delivery from locations close to each viewer. Cloudflare Cache serves media globally, and Argo Smart Routing ensures cache misses take the fastest path back to your origin.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="cache">Cache</h3>
<p>Cache content at Cloudflare's global network of edge locations. <a href="/cache/">Learn more about Cache</a>.</p>
<ul>
<li><strong>Global edge caching</strong> - Media content served from 300+ edge locations to reduce latency for global audiences</li>
<li><strong>Origin offload</strong> - Cached content is served directly from the edge, reducing origin bandwidth and compute costs</li>
<li><strong>Tiered caching</strong> - Regional cache tiers absorb repeated requests before they reach the origin, further reducing load</li>
</ul>
<h3 id="argo-smart-routing">Argo Smart Routing</h3>
<p>Route traffic through the fastest paths across Cloudflare's network. <a href="/argo-smart-routing/">Learn more about Argo Smart Routing</a>.</p>
<ul>
<li><strong>Smart routing</strong> - Requests that miss cache are routed through the fastest available network paths to origin</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/cache/how-to/cache-rules/">Configure Cache Rules</a></li>
<li><a href="/cache/how-to/tiered-cache/">Enable Tiered Cache</a></li>
<li><a href="/argo-smart-routing/get-started/">Enable Argo Smart Routing</a></li>
</ol>
