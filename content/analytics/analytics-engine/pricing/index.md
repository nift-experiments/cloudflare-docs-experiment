---
cp9:
  canonical: https://developers.cloudflare.com/analytics/analytics-engine/pricing/
  description: Workers Analytics Engine is priced based on two metrics — data points written, and read queries.
  full_title: Workers Analytics Engine — Pricing · Cloudflare Analytics docs
  head_html: <title>Workers Analytics Engine — Pricing · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Workers Analytics Engine is priced based on two metrics — data points written, and read queries."><link rel="canonical" href="https://developers.cloudflare.com/analytics/analytics-engine/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/analytics-engine/pricing/index.md"><meta property="og:title" content="Workers Analytics Engine — Pricing · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Workers Analytics Engine is priced based on two metrics — data points written, and read queries."><meta property="og:url" content="https://developers.cloudflare.com/analytics/analytics-engine/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers Analytics Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/analytics-engine/pricing/#page","headline":"Workers Analytics Engine \u2014\u00a0Pricing \u00b7 Cloudflare Analytics docs","description":"Workers Analytics Engine is priced based on two metrics \u2014 data points written, and read queries.","url":"https://developers.cloudflare.com/analytics/analytics-engine/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/analytics-engine/pricing/
  schema: 1
---
<p>Workers Analytics Engine is priced based on two metrics — data points written, and read queries.</p>
<table>
<thead>
<tr>
<th>Plan</th>
<th>Data points written</th>
<th>Read queries</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Workers Paid</strong></td>
<td>10 million included per month <br /> (+$0.25 per additional million)</td>
<td>1 million included per month (+$1.00 per additional million)</td>
</tr>
<tr>
<td><strong>Workers Free</strong></td>
<td>100,000 included per day</td>
<td>10,000 included per day</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="pricing-availability">Pricing availability</h3>
@markup("md", "content/.markup/bodies/3136.md")
</aside>
<h3 id="data-points-written">Data points written</h3>
<p>Every time you call <a href="/analytics/analytics-engine/get-started/#2-write-data-points-from-your-worker"><code>writeDataPoint()</code></a> in a Worker, this counts as one data point written.</p>
<p>Each data point written costs the same amount. There is no extra cost to add dimensions or cardinality, and no additional cost for writing more data in a single data point.</p>
<h3 id="read-queries">Read queries</h3>
<p>Every time you post to Workers Analytics Engine's <a href="/analytics/analytics-engine/sql-api/">SQL API</a>, this counts as one read query.</p>
<p>Each read query costs the same amount. There is no extra cost for more or less complex queries, and no extra cost for reading only a few rows of data versus many rows of data.</p>
