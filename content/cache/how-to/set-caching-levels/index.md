---
cp9:
  canonical: https://developers.cloudflare.com/cache/how-to/set-caching-levels/
  description: Set caching levels to control query string behavior.
  full_title: Caching levels · Cloudflare Cache (CDN) docs
  head_html: <title>Caching levels · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Set caching levels to control query string behavior."><link rel="canonical" href="https://developers.cloudflare.com/cache/how-to/set-caching-levels/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/how-to/set-caching-levels/index.md"><meta property="og:title" content="Caching levels · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set caching levels to control query string behavior."><meta property="og:url" content="https://developers.cloudflare.com/cache/how-to/set-caching-levels/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/how-to/set-caching-levels/#page","headline":"Caching levels \u00b7 Cloudflare Cache (CDN) docs","description":"Set caching levels to control query string behavior.","url":"https://developers.cloudflare.com/cache/how-to/set-caching-levels/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/how-to/set-caching-levels/
  schema: 1
---
<p>Caching levels determine how much of your website’s static content Cloudflare should cache. Cloudflare’s CDN caches static content according to the levels below.</p>
<ul>
<li><strong>No Query String</strong>: Delivers resources from cache when there is no query string. Example URL: <code>example.com/pic.jpg</code></li>
<li><strong>Ignore Query String</strong>: Delivers the same resource to everyone independent of the query string. Example URL: <code>example.com/pic.jpg?ignore=this-query-string</code></li>
<li><strong>Standard (Default)</strong>: Delivers a different resource each time the query string changes. Example URL: <code>example.com/pic.jpg?with=query</code></li>
</ul>
<p>You can adjust the caching level from the dashboard under <strong>Caching</strong> &gt; <strong>Configuration</strong> &gt; <strong>Caching level</strong>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3810.md")
</aside>
<h2 id="api-caching-level-values">API Caching level values</h2>
<p>If you are using the API to change the cache level, the values will differ from those shown in the dashboard. Refer to the table below to see how the API values map to the values shown in the dashboard.</p>
<table>
<thead>
<tr>
<th>Dashboard</th>
<th>API</th>
</tr>
</thead>
<tbody>
<tr>
<td>No Query String</td>
<td>Basic</td>
</tr>
<tr>
<td>Ignore Query String</td>
<td>Simplified</td>
</tr>
<tr>
<td>Standard (Default)</td>
<td>Aggressive</td>
</tr>
</tbody>
</table>
