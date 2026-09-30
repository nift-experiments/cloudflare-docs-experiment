---
cp9:
  canonical: https://developers.cloudflare.com/security-center/investigate/scan-limits/
  description: Limits
  full_title: Scan limits · Cloudflare Security Center docs
  head_html: <title>Scan limits · Cloudflare Security Center docs</title><meta name="generator" content="Nift"><meta name="description" content="Limits"><link rel="canonical" href="https://developers.cloudflare.com/security-center/investigate/scan-limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/security-center/investigate/scan-limits/index.md"><meta property="og:title" content="Scan limits · Cloudflare Security Center docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Limits"><meta property="og:url" content="https://developers.cloudflare.com/security-center/investigate/scan-limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Security Center"><meta name="algolia_product_filter" content="Security Center"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Security Center"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/security-center/investigate/scan-limits/#page","headline":"Scan limits \u00b7 Cloudflare Security Center docs","description":"Limits","url":"https://developers.cloudflare.com/security-center/investigate/scan-limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /security-center/investigate/scan-limits/
  schema: 1
---
<p>URL scans are limited by search history, Public and Unlisted visibility, and requests per second across different Cloudflare plans.</p>
<table>
<thead>
<tr>
<th>Cloudflare Plan</th>
<th>Search history</th>
<th>Public scans (per month)</th>
<th>Unlisted scans (per month)</th>
<th>Rate limit</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Free / Radar</strong></td>
<td>last 50 scans</td>
<td>5,000</td>
<td>none</td>
<td>1 per 10 seconds</td>
</tr>
<tr>
<td><strong>Self serve</strong></td>
<td>30 days</td>
<td>5,000</td>
<td>500</td>
<td>1 per 10 seconds</td>
</tr>
<tr>
<td><strong>Enterprise</strong></td>
<td>12 months</td>
<td>10,000</td>
<td>5,000</td>
<td>12 per second</td>
</tr>
<tr>
<td><strong>Cloudforce One</strong></td>
<td>Unlimited</td>
<td>75,000</td>
<td>20,000</td>
<td>12 per second</td>
</tr>
</tbody>
</table>
