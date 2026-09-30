---
cp9:
  canonical: https://developers.cloudflare.com/analytics/network-analytics/
  description: Monitor network and transport-layer traffic and DDoS attacks.
  full_title: Cloudflare Network Analytics · Cloudflare Analytics docs
  head_html: <title>Cloudflare Network Analytics · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Monitor network and transport-layer traffic and DDoS attacks."><link rel="canonical" href="https://developers.cloudflare.com/analytics/network-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/network-analytics/index.md"><meta property="og:title" content="Cloudflare Network Analytics · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Monitor network and transport-layer traffic and DDoS attacks."><meta property="og:url" content="https://developers.cloudflare.com/analytics/network-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/analytics/network-analytics/#page","headline":"Cloudflare Network Analytics \u00b7 Cloudflare Analytics docs","description":"Monitor network and transport-layer traffic and DDoS attacks.","url":"https://developers.cloudflare.com/analytics/network-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/network-analytics/
  schema: 1
---
<p>Cloudflare Network Analytics (version 2) provides near real-time visibility into network and transport-layer traffic patterns and DDoS attacks. Network Analytics visualizes packet and bit-level data, the same data available via the Network Analytics dataset of the GraphQL Analytics API.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="requirements">Requirements</h3>
@markup("md", "content/.markup/bodies/3126.md")
</aside>
<p>For a technical deep-dive into Network Analytics, refer to our <a href="https://blog.cloudflare.com/building-network-analytics-v2/">blog post</a>.</p>
<h2 id="remarks">Remarks</h2>
<ul>
<li>
<p>The Network Analytics logs refer to IP traffic of Magic Transit customer prefixes/leased IP addresses or Spectrum applications. These logs are not directly associated with the <a href="/fundamentals/concepts/accounts-and-zones/#zones">zones</a> in your Cloudflare account.</p>
</li>
<li>
<p>The data retention for Network Analytics is 16 weeks. Additionally, data older than eight weeks might have lower resolution when using narrow time frames.</p>
</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/analytics/graphql-api/">Cloudflare GraphQL API</a></li>
<li><a href="/logs/logpush/">Cloudflare Logpush</a></li>
<li><a href="/analytics/graphql-api/migration-guides/network-analytics-v2/">Migrating from Network Analytics v1 to Network Analytics v2</a></li>
</ul>
