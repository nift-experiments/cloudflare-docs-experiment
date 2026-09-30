---
cp9:
  canonical: https://developers.cloudflare.com/dynamic-workers/platform/limits/
  description: Limits for concurrent Dynamic Worker requests.
  full_title: Limits · Cloudflare Dynamic Workers docs
  head_html: <title>Limits · Cloudflare Dynamic Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Limits for concurrent Dynamic Worker requests."><link rel="canonical" href="https://developers.cloudflare.com/dynamic-workers/platform/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dynamic-workers/platform/limits/index.md"><meta property="og:title" content="Limits · Cloudflare Dynamic Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Limits for concurrent Dynamic Worker requests."><meta property="og:url" content="https://developers.cloudflare.com/dynamic-workers/platform/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Dynamic Workers"><meta name="algolia_product_filter" content="Dynamic Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Dynamic Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dynamic-workers/platform/limits/#page","headline":"Limits \u00b7 Cloudflare Dynamic Workers docs","description":"Limits for concurrent Dynamic Worker requests.","url":"https://developers.cloudflare.com/dynamic-workers/platform/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dynamic-workers/platform/limits/
  schema: 1
---
<p>Cloudflare limits the number of distinct Dynamic Workers with in-flight requests. Multiple in-flight requests to the same Dynamic Worker count as one toward this limit.</p>
<table>
<thead>
<tr>
<th>Context</th>
<th>Concurrent Dynamic Workers</th>
</tr>
</thead>
<tbody>
<tr>
<td>Worker request</td>
<td>4</td>
</tr>
<tr>
<td><a href="/durable-objects/">Durable Object</a></td>
<td>10 (previously 4)</td>
</tr>
</tbody>
</table>
<p>In a Worker, each request has its own input/output (I/O) context. Each request can therefore have up to four distinct Dynamic Workers with in-flight requests.</p>
<p>A Durable Object shares one I/O context across all concurrent requests to the same object. Those requests can collectively have up to ten distinct Dynamic Workers with in-flight requests. To set lower CPU time or subrequest limits, refer to <a href="/dynamic-workers/usage/limits/">Custom resource limits</a>.</p>
