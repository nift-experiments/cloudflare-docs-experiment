---
cp9:
  canonical: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/literals/
  description: Supported literal types in Analytics Engine SQL.
  full_title: Workers Analytics Engine SQL Reference · Cloudflare Analytics docs
  head_html: <title>Workers Analytics Engine SQL Reference · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Supported literal types in Analytics Engine SQL."><link rel="canonical" href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/literals/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/literals/index.md"><meta property="og:title" content="Workers Analytics Engine SQL Reference · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Supported literal types in Analytics Engine SQL."><meta property="og:url" content="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/literals/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers Analytics Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/literals/#page","headline":"Workers Analytics Engine SQL Reference \u00b7 Cloudflare Analytics docs","description":"Supported literal types in Analytics Engine SQL.","url":"https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/literals/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/analytics-engine/sql-reference/literals/
  schema: 1
---
<p>The following literals are supported:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Syntax</th>
</tr>
</thead>
<tbody>
<tr>
<td>integer</td>
<td><code>42</code>, <code>-42</code></td>
</tr>
<tr>
<td>double</td>
<td><code>4.2</code>, <code>-4.2</code></td>
</tr>
<tr>
<td>string</td>
<td><code>'so long and thanks for all the fish'</code></td>
</tr>
<tr>
<td>boolean</td>
<td><code>true</code> or <code>false</code></td>
</tr>
<tr>
<td>time interval</td>
<td><code>INTERVAL '42' DAY</code><br/>Intervals of <code>YEAR</code>, <code>MONTH</code>, <code>DAY</code>, <code>HOUR</code>, <code>MINUTE</code> and <code>SECOND</code> are supported</td>
</tr>
</tbody>
</table>
