---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/storage/5/
  description: '2024-12-11'
  full_title: Storage changelog - page 5 | Cloudflare Docs
  head_html: <title>Storage changelog - page 5 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2024-12-11"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/storage/5/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Storage changelog - page 5"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2024-12-11"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/storage/5/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/storage/5/#page","headline":"Storage changelog - page 5 | Cloudflare Docs","description":"2024-12-11","url":"https://developers.cloudflare.com/changelog/product-group/storage/5/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/storage/5/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="up-to-10x-faster-cached-queries-for-hyperdrive"><a href="/changelog/post/2024-12-11-hyperdrive-caching-at-edge/">Up to 10x faster cached queries for Hyperdrive</a></h2>
<p><em>2024-12-11</em></p>
<p>Hyperdrive now caches queries in all Cloudflare locations, decreasing cache hit latency by up to 90%.</p>
<p>When you make a query to your database and Hyperdrive has cached the query results, Hyperdrive will now return the results from the nearest cache. By caching data closer to your users, the latency for cache hits reduces by up to 90%.</p>
<p>This reduction in cache hit latency is reflected in a reduction of the session duration for all queries (cached and uncached) from Cloudflare Workers to Hyperdrive, as illustrated below.</p>
<p><img src="/assets/upstream/images/hyperdrive/changelog/hyperdrive-edge-caching-metrics.png" alt="Hyperdrive edge caching improves average session duration for database queries" /></p>
<p><em>P50, P75, and P90 Hyperdrive session latency for all client connection sessions (both cached and uncached queries) for Hyperdrive configurations with caching enabled during the rollout period.</em></p>
<p>This performance improvement is applied to all new and existing Hyperdrive configurations that have caching enabled.</p>
<p>For more details on how Hyperdrive performs query caching, refer to the <a href="/hyperdrive/concepts/how-hyperdrive-works/#3-query-caching">Hyperdrive documentation</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/storage/4/">Previous</a><span>Page 5 of 5</span></nav>
