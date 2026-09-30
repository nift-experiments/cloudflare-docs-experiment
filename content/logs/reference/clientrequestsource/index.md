---
cp9:
  canonical: https://developers.cloudflare.com/logs/reference/clientrequestsource/
  description: Understand ClientRequestSource field values in logs.
  full_title: ClientRequestSource field · Cloudflare Logs docs
  head_html: <title>ClientRequestSource field · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand ClientRequestSource field values in logs."><link rel="canonical" href="https://developers.cloudflare.com/logs/reference/clientrequestsource/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/reference/clientrequestsource/index.md"><meta property="og:title" content="ClientRequestSource field · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand ClientRequestSource field values in logs."><meta property="og:url" content="https://developers.cloudflare.com/logs/reference/clientrequestsource/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Logs"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/reference/clientrequestsource/#page","headline":"ClientRequestSource field \u00b7 Cloudflare Logs docs","description":"Understand ClientRequestSource field values in logs.","url":"https://developers.cloudflare.com/logs/reference/clientrequestsource/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/reference/clientrequestsource/
  schema: 1
---
<p>The possible values for the <code>ClientRequestSource</code> field are the following:</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Request source</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>0</code></td>
<td>unknown</td>
<td>Should never happen.</td>
</tr>
<tr>
<td><code>1</code></td>
<td>eyeball</td>
<td>A request from an end user. If you want to count requests made the Cloudflare Edge, the query should filter on <code>requestSource=eyeball</code>.</td>
</tr>
<tr>
<td><code>2</code></td>
<td>purge</td>
<td>A request made by Cloudflare's purge system.</td>
</tr>
<tr>
<td><code>3</code></td>
<td>alwaysOnline</td>
<td>A request made by Cloudflare's Always Online crawler.</td>
</tr>
<tr>
<td><code>4</code></td>
<td>healthcheck</td>
<td>A request made by Cloudflare's Health Check system.</td>
</tr>
<tr>
<td><code>5</code></td>
<td>edgeWorkerFetch</td>
<td>A fetch request made from an edge Worker.</td>
</tr>
<tr>
<td><code>6</code></td>
<td>edgeWorkerCacheAPI</td>
<td>A cache API call made from an edge Worker.</td>
</tr>
<tr>
<td><code>7</code></td>
<td>edgeWorkerKV</td>
<td>A KV call made from an edge Worker.</td>
</tr>
<tr>
<td><code>8</code></td>
<td>imageResizing</td>
<td>Requests made by Cloudflare's Image Resizing product.</td>
</tr>
<tr>
<td><code>9</code></td>
<td>orangeToOrange</td>
<td>A request that comes from another orange clouded zone.</td>
</tr>
<tr>
<td><code>10</code></td>
<td>sslDetector</td>
<td>A request made by Cloudflare's <a href="https://blog.cloudflare.com/ssl-tls-recommender/">SSL Detector system</a>.</td>
</tr>
<tr>
<td><code>11</code></td>
<td>earlyHintsCache</td>
<td>An <a href="https://blog.cloudflare.com/early-hints/">Early Hint request</a>.</td>
</tr>
<tr>
<td><code>12</code></td>
<td>inBrowserChallenge</td>
<td>An end user request caused by a Cloudflare security product (Challenges, JavaScript Detections). These requests never reach the origin.</td>
</tr>
</tbody>
</table>
