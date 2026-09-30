---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.path.extension/
  description: The lowercased file extension in the URI path without the dot (.) character.
  full_title: http.request.uri.path.extension · Cloudflare Ruleset Engine docs
  head_html: <title>http.request.uri.path.extension · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="The lowercased file extension in the URI path without the dot (.) character."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.path.extension/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="http.request.uri.path.extension · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The lowercased file extension in the URI path without the dot (.) character."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.path.extension/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.path.extension/#page","headline":"http.request.uri.path.extension \u00b7 Cloudflare Ruleset Engine docs","description":"The lowercased file extension in the URI path without the dot (.) character.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.path.extension/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/http.request.uri.path.extension/
  schema: 1
---
<h1 id="http-request-uri-path-extension">http.request.uri.path.extension</h1>

**Data type:** String

<p>The lowercased file extension in the URI path without the dot (<code>.</code>) character.</p>

<p>This corresponds to the string after the last dot in the URI path, excluding the query string.</p>
<p>If the first character of the last path segment is a dot and the segment does not contain other dot characters, the field value will be an empty string (<code>&quot;&quot;</code>). Having a dot as the first character does not represent a file extension and is commonly used in UNIX-like systems to denote a hidden file or directory.</p>
<p>Example values:</p>
<ul>
<li>If the URI path is <code>/articles/index.html</code>, the field value will be <code>&quot;html&quot;</code>.</li>
<li>If the URI path is <code>/articles/index.</code>, the field value will be an empty string (<code>&quot;&quot;</code>).</li>
</ul>
<p>Example values:</p>
<table>
<thead>
<tr>
<th>URI path</th>
<th>Field value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/foo</code></td>
<td><code>&quot;&quot;</code></td>
</tr>
<tr>
<td><code>/foo.mp3</code></td>
<td><code>&quot;mp3&quot;</code></td>
</tr>
<tr>
<td><code>/.mp3</code></td>
<td><code>&quot;&quot;</code></td>
</tr>
<tr>
<td><code>/.foo.mp3</code></td>
<td><code>&quot;mp3&quot;</code></td>
</tr>
<tr>
<td><code>/foo.tar.bz2</code></td>
<td><code>&quot;bz2&quot;</code></td>
</tr>
<tr>
<td><code>/foo.</code></td>
<td><code>&quot;&quot;</code></td>
</tr>
<tr>
<td><code>/foo.MP3</code></td>
<td><code>&quot;mp3&quot;</code></td>
</tr>
</tbody>
</table>

<h2 id="categories">Categories</h2>

- Request
- URI

**Keywords:** request, uri, url, path, client, visitor

