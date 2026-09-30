---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.content_type.media_type/
  description: The lowercased content type (including subtype and suffix) without any extra parameters, based on the response's Content-Type header.
  full_title: http.response.content_type.media_type · Cloudflare Ruleset Engine docs
  head_html: <title>http.response.content_type.media_type · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="The lowercased content type (including subtype and suffix) without any extra parameters, based on the response&#x27;s Content-Type header."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.content_type.media_type/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="http.response.content_type.media_type · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The lowercased content type (including subtype and suffix) without any extra parameters, based on the response&#x27;s Content-Type header."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.content_type.media_type/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.content_type.media_type/#page","headline":"http.response.content_type.media_type \u00b7 Cloudflare Ruleset Engine docs","description":"The lowercased content type (including subtype and suffix) without any extra parameters, based on the response's Content-Type header.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.content_type.media_type/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/http.response.content_type.media_type/
  schema: 1
---
<h1 id="http-response-content-type-media-type">http.response.content_type.media_type</h1>

**Data type:** String

<p>The lowercased content type (including subtype and suffix) without any extra parameters, based on the response's <code>Content-Type</code> header.</p>

<p>The field value will not include parameters such as <code>charset</code>.</p>
<p>Example values:</p>
<table>
<thead>
<tr>
<th>Content-Type header</th>
<th>Field value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>text/html</code></td>
<td><code>&quot;text/html&quot;</code></td>
</tr>
<tr>
<td><code>text/html; charset=utf-8</code></td>
<td><code>&quot;text/html&quot;</code></td>
</tr>
<tr>
<td><code>text/html+extra</code></td>
<td><code>&quot;text/html+extra&quot;</code></td>
</tr>
<tr>
<td><code>text/html+extra; charset=utf-8</code></td>
<td><code>&quot;text/html+extra&quot;</code></td>
</tr>
<tr>
<td><code>text/HTML</code></td>
<td><code>&quot;text/html&quot;</code></td>
</tr>
<tr>
<td><code>text/html; charset=utf-8; other=value</code></td>
<td><code>&quot;text/html&quot;</code></td>
</tr>
</tbody>
</table>
<p><strong>Note</strong>: The availability of HTTP response fields depends on the exact Cloudflare feature and your Cloudflare plan.</p>

<h2 id="categories">Categories</h2>

- Response
- Headers

**Keywords:** response

