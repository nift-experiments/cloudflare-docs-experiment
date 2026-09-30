---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args/
  description: The HTTP URI arguments associated with a request represented as a Map (associative array).
  full_title: http.request.uri.args · Cloudflare Ruleset Engine docs
  head_html: <title>http.request.uri.args · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="The HTTP URI arguments associated with a request represented as a Map (associative array)."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="http.request.uri.args · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The HTTP URI arguments associated with a request represented as a Map (associative array)."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args/#page","headline":"http.request.uri.args \u00b7 Cloudflare Ruleset Engine docs","description":"The HTTP URI arguments associated with a request represented as a Map (associative array).","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.uri.args/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/http.request.uri.args/
  schema: 1
---
<h1 id="http-request-uri-args">http.request.uri.args</h1>

**Data type:** Map<Array<String>>

<p>The HTTP URI arguments associated with a request represented as a Map (associative array).</p>

<p>When an argument repeats, the array contains multiple items in the order they appear in the request.</p>
<p>The values are not pre-processed and retain the original case used in the request.</p>
<ul>
<li><strong>Decoding</strong>: No decoding performed</li>
<li><strong>Non-ASCII</strong>: Preserved</li>
</ul>

**Example value:**

```txt
{"search": ["red+apples"]}
```

**Example usage:**

```txt
any(http.request.uri.args["search"][*] == "red+apples")
```

<h2 id="categories">Categories</h2>

- Request
- URI

**Keywords:** request, uri, url, arguments, query string, client, visitor

