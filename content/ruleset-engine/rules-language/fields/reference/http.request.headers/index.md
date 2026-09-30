---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers/
  description: The HTTP request headers represented as a Map (or associative array).
  full_title: http.request.headers · Cloudflare Ruleset Engine docs
  head_html: <title>http.request.headers · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="The HTTP request headers represented as a Map (or associative array)."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="http.request.headers · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The HTTP request headers represented as a Map (or associative array)."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers/#page","headline":"http.request.headers \u00b7 Cloudflare Ruleset Engine docs","description":"The HTTP request headers represented as a Map (or associative array).","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/http.request.headers/
  schema: 1
---
<h1 id="http-request-headers">http.request.headers</h1>

**Data type:** Map<Array<String>>

<p>The HTTP request headers represented as a Map (or associative array).</p>

<p>The keys of the associative array are the names of HTTP request headers converted to lowercase.</p>
<p>When there are repeating headers, the array includes them in the order they appear in the request.</p>
<p>The request header values are not pre-processed and retain the original case used in the request.</p>
<ul>
<li><strong>Decoding</strong>: No decoding performed</li>
<li><strong>Whitespace</strong>: Preserved</li>
<li><strong>Non-ASCII</strong>: Preserved</li>
</ul>
<p>When the HTTP request contains too many headers, this field may not contain all of the headers sent in the HTTP request. In this situation, the <a href="/ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/"><code>http.request.headers.truncated</code></a> field will be set to <code>true</code>.</p>

**Example value:**

```txt
{"content-type": ["application/json"]}
```

**Example usage:**

```txt
any(http.request.headers["content-type"][*] == "application/json")
```

<h2 id="categories">Categories</h2>

- Request
- Headers

**Keywords:** request, client, visitor

