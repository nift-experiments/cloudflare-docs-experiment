---
cp9:
  canonical: https://developers.cloudflare.com/rules/normalization/examples/
  description: Examples of the impact of different URL normalization settings in the URLs of incoming requests.
  full_title: URL normalization examples · Cloudflare Rules docs
  head_html: <title>URL normalization examples · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Examples of the impact of different URL normalization settings in the URLs of incoming requests."><link rel="canonical" href="https://developers.cloudflare.com/rules/normalization/examples/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/normalization/examples/index.md"><meta property="og:title" content="URL normalization examples · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Examples of the impact of different URL normalization settings in the URLs of incoming requests."><meta property="og:url" content="https://developers.cloudflare.com/rules/normalization/examples/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/normalization/examples/#page","headline":"URL normalization examples \u00b7 Cloudflare Rules docs","description":"Examples of the impact of different URL normalization settings in the URLs of incoming requests.","url":"https://developers.cloudflare.com/rules/normalization/examples/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/normalization/examples/
  schema: 1
---
<p>The following table shows how different <a href="/rules/normalization/settings/">URL normalization settings</a> affect request URLs before they pass to other Cloudflare features and to the origin server:</p>
<table>
<thead>
<tr>
<th>Incoming URL</th>
<th>Normalization type</th>
<th>Normalize incoming URLs</th>
<th>Normalize URLs to origin</th>
<th>URL at Cloudflare's network</th>
<th>URL passed to origin server</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>www.example.com/hello</code></td>
<td>(any)</td>
<td><em>Off</em></td>
<td><em>Off</em></td>
<td><code>www.example.com/hello</code></td>
<td><code>www.example.com/hello</code></td>
</tr>
<tr>
<td><code>www.example.com/hello</code></td>
<td>(any)</td>
<td><em>On</em></td>
<td><em>Off</em></td>
<td><code>www.example.com/hello</code></td>
<td><code>www.example.com/hello</code></td>
</tr>
<tr>
<td><code>www.example.com/hello</code></td>
<td>(any)</td>
<td><em>On</em></td>
<td><em>On</em></td>
<td><code>www.example.com/hello</code></td>
<td><code>www.example.com/hello</code></td>
</tr>
<tr>
<td><code>example.com/%68ello</code></td>
<td>(any)</td>
<td><em>Off</em></td>
<td><em>Off</em></td>
<td><code>example.com/%68ello</code></td>
<td><code>example.com/%68ello</code></td>
</tr>
<tr>
<td><code>example.com/%68ello</code></td>
<td>(any)</td>
<td><em>On</em></td>
<td><em>Off</em></td>
<td><code>example.com/hello</code></td>
<td><code>example.com/%68ello</code></td>
</tr>
<tr>
<td><code>example.com/%68ello</code></td>
<td>(any)</td>
<td><em>On</em></td>
<td><em>On</em></td>
<td><code>example.com/hello</code></td>
<td><code>example.com/hello</code></td>
</tr>
<tr>
<td><code>example.com/%68ello//pa\th</code></td>
<td><em>RFC-3986</em></td>
<td><em>Off</em></td>
<td><em>Off</em></td>
<td><code>example.com/%68ello//pa\th</code></td>
<td><code>example.com/%68ello//pa\th</code></td>
</tr>
<tr>
<td><code>example.com/%68ello//pa\th</code></td>
<td><em>RFC-3986</em></td>
<td><em>On</em></td>
<td><em>Off</em></td>
<td><code>example.com/hello//pa%5Cth</code></td>
<td><code>example.com/%68ello//pa\th</code></td>
</tr>
<tr>
<td><code>example.com/%68ello//pa\th</code></td>
<td><em>RFC-3986</em></td>
<td><em>On</em></td>
<td><em>On</em></td>
<td><code>example.com/hello//pa%5Cth</code></td>
<td><code>example.com/hello//pa%5Cth</code></td>
</tr>
<tr>
<td><code>example.com/%68ello//pa\th</code></td>
<td><em>Cloudflare</em></td>
<td><em>Off</em></td>
<td><em>Off</em></td>
<td><code>example.com/%68ello//pa\th</code></td>
<td><code>example.com/%68ello//pa\th</code></td>
</tr>
<tr>
<td><code>example.com/%68ello//pa\th</code></td>
<td><em>Cloudflare</em></td>
<td><em>On</em></td>
<td><em>Off</em></td>
<td><code>example.com/hello/pa/th</code></td>
<td><code>example.com/%68ello//pa\th</code></td>
</tr>
<tr>
<td><code>example.com/%68ello//pa\th</code></td>
<td><em>Cloudflare</em></td>
<td><em>On</em></td>
<td><em>On</em></td>
<td><code>example.com/hello/pa/th</code></td>
<td><code>example.com/hello/pa/th</code></td>
</tr>
<tr>
<td><code>example.com/hello//../path</code></td>
<td><em>RFC-3986</em></td>
<td><em>On</em></td>
<td><em>On</em></td>
<td><code>example.com/hello/path</code></td>
<td><code>example.com/hello/path</code></td>
</tr>
<tr>
<td><code>example.com/hello//../path</code></td>
<td><em>Cloudflare</em></td>
<td><em>On</em></td>
<td><em>On</em></td>
<td><code>example.com/path</code></td>
<td><code>example.com/path</code></td>
</tr>
<tr>
<td><code>example.com/hello/\../path</code></td>
<td><em>RFC-3986</em></td>
<td><em>On</em></td>
<td><em>On</em></td>
<td><code>example.com/hello/%5C../path</code></td>
<td><code>example.com/hello/%5C../path</code></td>
</tr>
<tr>
<td><code>example.com/hello/\../path</code></td>
<td><em>Cloudflare</em></td>
<td><em>On</em></td>
<td><em>On</em></td>
<td><code>example.com/path</code></td>
<td><code>example.com/path</code></td>
</tr>
</tbody>
</table>
