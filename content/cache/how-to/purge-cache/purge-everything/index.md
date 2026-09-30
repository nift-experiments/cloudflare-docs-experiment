---
cp9:
  canonical: https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/
  description: Purge all cached content for your entire zone.
  full_title: ​Purge everything · Cloudflare Cache (CDN) docs
  head_html: <title>​Purge everything · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Purge all cached content for your entire zone."><link rel="canonical" href="https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/index.md"><meta property="og:title" content="​Purge everything · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Purge all cached content for your entire zone."><meta property="og:url" content="https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/#page","headline":"\u200bPurge everything \u00b7 Cloudflare Cache (CDN) docs","description":"Purge all cached content for your entire zone.","url":"https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/how-to/purge-cache/purge-everything/
  schema: 1
---
<p>To maintain optimal site performance, Cloudflare strongly recommends using single-file (by URL) purging instead of a complete cache purge.</p>
<p>Purging everything instantly clears all resources from your CDN cache in all Cloudflare data centers. Each new request for a purged resource returns to your origin server to validate the resource. If the cached version is no longer valid, Cloudflare fetches the latest version from your origin server and caches it.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3867.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Configuration</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Under <strong>Purge Cache</strong>, select <strong>Purge Everything</strong>. A warning window appears.</li>
<li>If you agree, select <strong>Purge Everything</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3866.md")
</aside>
<p>For information on rate limits, refer to the <a href="/cache/how-to/purge-cache/#availability-and-limits">Availability and limits</a> section.</p>
<h2 id="resulting-cache-status">Resulting cache status</h2>
<p>Purge Everything invalidates the resource, resulting in the <code>CF-Cache-Status</code> header indicating <a href="/cache/concepts/cache-responses/#expired"><code>EXPIRED</code></a> for subsequent requests.</p>
