---
cp9:
  canonical: https://developers.cloudflare.com/web-analytics/limits/
  description: Rate limits and data retention for Web Analytics.
  full_title: Web Analytics - Limits · Cloudflare Web Analytics docs
  head_html: <title>Web Analytics - Limits · Cloudflare Web Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Rate limits and data retention for Web Analytics."><link rel="canonical" href="https://developers.cloudflare.com/web-analytics/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/web-analytics/limits/index.md"><meta property="og:title" content="Web Analytics - Limits · Cloudflare Web Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Rate limits and data retention for Web Analytics."><meta property="og:url" content="https://developers.cloudflare.com/web-analytics/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Web Analytics"><meta name="algolia_product_filter" content="Cloudflare Web Analytics"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Web Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/web-analytics/limits/#page","headline":"Web Analytics - Limits \u00b7 Cloudflare Web Analytics docs","description":"Rate limits and data retention for Web Analytics.","url":"https://developers.cloudflare.com/web-analytics/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /web-analytics/limits/
  schema: 1
---
<p>Cloudflare limits the number of sites for which you can track web analytics, as well as the number of rules allowed for each plan type. Refer to the following tables for more information.</p>
<h2 id="site-limits">Site limits</h2>
<p>Cloudflare limits the number of sites for which you can track web analytics when they are not proxied by Cloudflare.</p>
<table>
<thead>
<tr>
<th>Site type</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Not proxied through Cloudflare</td>
<td>10</td>
</tr>
<tr>
<td>Proxied through Cloudflare</td>
<td>No limit</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/92.md")
</aside>
<h2 id="rules-limits">Rules limits</h2>
<p>Cloudflare limits the number of Web Analytics rules you can have by plan type. For plans with a limit of zero, Web Analytics injects the JS snippet on all subdomains.</p>
<p>Rules are only available for sites proxied through Cloudflare.</p>
<table>
<thead>
<tr>
<th>Plan type</th>
<th>Rules limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Free</td>
<td>0</td>
</tr>
<tr>
<td>Pro</td>
<td>5</td>
</tr>
<tr>
<td>Business</td>
<td>20</td>
</tr>
<tr>
<td>Enterprise</td>
<td>100</td>
</tr>
</tbody>
</table>
