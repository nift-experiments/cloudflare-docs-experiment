---
cp9:
  canonical: https://developers.cloudflare.com/logs/reference/waf-fields/
  description: Review WAF action and rule field values in logs.
  full_title: WAF fields · Cloudflare Logs docs
  head_html: <title>WAF fields · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Review WAF action and rule field values in logs."><link rel="canonical" href="https://developers.cloudflare.com/logs/reference/waf-fields/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/reference/waf-fields/index.md"><meta property="og:title" content="WAF fields · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review WAF action and rule field values in logs."><meta property="og:url" content="https://developers.cloudflare.com/logs/reference/waf-fields/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Logs"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/reference/waf-fields/#page","headline":"WAF fields \u00b7 Cloudflare Logs docs","description":"Review WAF action and rule field values in logs.","url":"https://developers.cloudflare.com/logs/reference/waf-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/reference/waf-fields/
  schema: 1
---
<p>The Web Application Firewall (WAF) contains rules managed by Cloudflare to block requests that contain malicious content.</p>
<h2 id="waf-action">WAF Action</h2>
<table>
<thead>
<tr>
<th>Value</th>
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><span style="font-weight: 400;"><code>0</code></span></td>
<td>Unknown</td>
<td>Take no other action.</td>
</tr>
<tr>
<td><span style="font-weight: 400;"><code>1</code></span></td>
<td>Allow</td>
<td>Bypass all subsequent WAF rules.</td>
</tr>
<tr>
<td><span style="font-weight: 400;"><code>2</code></span></td>
<td>Drop</td>
<td>Block with an HTTP 403 response.</td>
</tr>
<tr>
<td><span style="font-weight: 400;"><code>3</code></span></td>
<td>Challenge Allow</td>
<td>Issue a Managed Challenge.</td>
</tr>
<tr>
<td><span style="font-weight: 400;"><code>4</code></span></td>
<td>Challenge Drop</td>
<td>Unused.</td>
</tr>
<tr>
<td><span style="font-weight: 400;"><code>5</code></span></td>
<td>Log</td>
<td>Take no action other than logging the event.</td>
</tr>
</tbody>
</table>
<h2 id="deprecated-fields-for-internal-cloudflare-use">Deprecated fields for internal Cloudflare use</h2>
<p>The values of these fields are subject to change by Cloudflare at any time and are irrelevant for customer data analysis:</p>
<ul>
<li>WAFFlags</li>
<li>WAFMatchedVar</li>
</ul>
