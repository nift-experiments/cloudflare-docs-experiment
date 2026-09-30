---
cp9:
  canonical: https://developers.cloudflare.com/flagship/reference/limits/
  description: Platform limits for Flagship, including maximum apps per account, flags per app, condition nesting depth, and configuration size.
  full_title: Limits · Cloudflare Flagship docs
  head_html: <title>Limits · Cloudflare Flagship docs</title><meta name="generator" content="Nift"><meta name="description" content="Platform limits for Flagship, including maximum apps per account, flags per app, condition nesting depth, and configuration size."><link rel="canonical" href="https://developers.cloudflare.com/flagship/reference/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/flagship/reference/limits/index.md"><meta property="og:title" content="Limits · Cloudflare Flagship docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Platform limits for Flagship, including maximum apps per account, flags per app, condition nesting depth, and configuration size."><meta property="og:url" content="https://developers.cloudflare.com/flagship/reference/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Flagship"><meta name="algolia_product_filter" content="Flagship"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Flagship"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/flagship/reference/limits/#page","headline":"Limits \u00b7 Cloudflare Flagship docs","description":"Platform limits for Flagship, including maximum apps per account, flags per app, condition nesting depth, and configuration size.","url":"https://developers.cloudflare.com/flagship/reference/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /flagship/reference/limits/
  schema: 1
---
<p>Flagship enforces the following limits.</p>
<h2 id="platform-limits">Platform limits</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Apps per account</td>
<td>10,000</td>
</tr>
<tr>
<td>Flags per app</td>
<td>5,000</td>
</tr>
<tr>
<td>Flag, app, and variant keys</td>
<td>64 chars</td>
</tr>
<tr>
<td>Condition attribute names</td>
<td>64 chars</td>
</tr>
<tr>
<td>Condition string values</td>
<td>256 chars</td>
</tr>
<tr>
<td>Variant value size</td>
<td>10 KB</td>
</tr>
<tr>
<td>Condition nesting depth</td>
<td>5 levels</td>
</tr>
<tr>
<td>Flag description</td>
<td>512 chars</td>
</tr>
<tr>
<td>Flag configuration size per app</td>
<td>25 MB</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8730.md")
</aside>
<h2 id="notes">Notes</h2>
<ul>
<li>Condition nesting depth counts from the top-level condition group. A flat list of conditions (no nesting) has a depth of 1.</li>
<li>Flag keys, app names, condition set names, and variant keys can contain letters, numbers, hyphens, and underscores.</li>
<li>All variants on a flag must use the same value type: boolean, string, number, or JSON.</li>
<li>Flag configuration size refers to the total serialized size of all flags within a single app, including their variants and rules.</li>
</ul>
