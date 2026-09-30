---
cp9:
  canonical: https://developers.cloudflare.com/radar/concepts/aggregation-intervals/
  description: Configure Cloudflare Radar aggregation intervals to control the frequency of returned data, from 15 minutes to one week.
  full_title: Aggregation intervals · Cloudflare Radar docs
  head_html: <title>Aggregation intervals · Cloudflare Radar docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Cloudflare Radar aggregation intervals to control the frequency of returned data, from 15 minutes to one week."><link rel="canonical" href="https://developers.cloudflare.com/radar/concepts/aggregation-intervals/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/radar/concepts/aggregation-intervals/index.md"><meta property="og:title" content="Aggregation intervals · Cloudflare Radar docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Cloudflare Radar aggregation intervals to control the frequency of returned data, from 15 minutes to one week."><meta property="og:url" content="https://developers.cloudflare.com/radar/concepts/aggregation-intervals/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Radar"><meta name="algolia_product_filter" content="Radar"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Radar"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/radar/concepts/aggregation-intervals/#page","headline":"Aggregation intervals \u00b7 Cloudflare Radar docs","description":"Configure Cloudflare Radar aggregation intervals to control the frequency of returned data, from 15 minutes to one week.","url":"https://developers.cloudflare.com/radar/concepts/aggregation-intervals/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /radar/concepts/aggregation-intervals/
  schema: 1
---
<p>Aggregation intervals allow you to return data in a specified interval (or frequency). If no interval is defined, data will be returned in the default aggregation interval (or frequency). As a general principle, the longer the date range, the bigger the aggregation interval.</p>
<p>For example, when requesting one day of data, the default aggregation interval is 15 minutes. When requesting more than one month of data, the default is one day.</p>
<h2 id="method">Method</h2>
<table>
<thead>
<tr>
<th>Aggregation Interval</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>15m</code></td>
<td>15 minutes frequency.</td>
</tr>
<tr>
<td><code>1h</code></td>
<td>One hour frequency.</td>
</tr>
<tr>
<td><code>1d</code></td>
<td>One day frequency.</td>
</tr>
<tr>
<td><code>1w</code></td>
<td>One week frequency.</td>
</tr>
</tbody>
</table>
