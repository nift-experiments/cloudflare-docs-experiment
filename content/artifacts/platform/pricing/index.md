---
cp9:
  canonical: https://developers.cloudflare.com/artifacts/platform/pricing/
  description: Review Artifacts pricing information.
  full_title: Pricing · Cloudflare Artifacts docs
  head_html: <title>Pricing · Cloudflare Artifacts docs</title><meta name="generator" content="Nift"><meta name="description" content="Review Artifacts pricing information."><link rel="canonical" href="https://developers.cloudflare.com/artifacts/platform/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/artifacts/platform/pricing/index.md"><meta property="og:title" content="Pricing · Cloudflare Artifacts docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review Artifacts pricing information."><meta property="og:url" content="https://developers.cloudflare.com/artifacts/platform/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Artifacts"><meta name="algolia_product_filter" content="Artifacts"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Artifacts"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/artifacts/platform/pricing/#page","headline":"Pricing \u00b7 Cloudflare Artifacts docs","description":"Review Artifacts pricing information.","url":"https://developers.cloudflare.com/artifacts/platform/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /artifacts/platform/pricing/
  schema: 1
---
<p>Artifacts pricing is billed on two dimensions:</p>
<ul>
<li><strong>Operations</strong>: the number of repo operations, such as <code>create</code>, <code>push</code>, <code>pull</code>, and <code>clone</code>.</li>
<li><strong>Storage</strong>: the total amount of stored data, measured in gigabyte-months (<code>GB-mo</code>).</li>
</ul>
<h2 id="artifacts-pricing">Artifacts pricing</h2>
<table>
<thead>
<tr>
<th>Unit</th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Operations (1,000 operations)</td>
<td>Unavailable</td>
<td>First 10,000 per month + $0.15 per additional 1,000 operations</td>
</tr>
<tr>
<td>Storage (GB-mo)</td>
<td>Unavailable</td>
<td>First 1 GB per month + $0.50 per additional GB-mo</td>
</tr>
</tbody>
</table>
<h2 id="storage-usage">Storage usage</h2>
<p>Storage is billed using gigabyte-month (<code>GB-mo</code>) as the billing metric, identical to <a href="/durable-objects/platform/pricing/#sqlite-storage-backend">Durable Objects SQL storage</a>. A <code>GB-mo</code> is calculated by averaging peak storage per day over a 30-day billing period.</p>
<ul>
<li>Storage is calculated across all repositories.</li>
<li>Replicas do not add storage charges. Storage is replicated by default, and you do not need to manage repository availability or uptime.</li>
<li>Repos remain stored until you explicitly delete them.</li>
</ul>
