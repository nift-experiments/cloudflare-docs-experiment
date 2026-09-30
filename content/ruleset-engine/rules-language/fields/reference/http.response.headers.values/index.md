---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers.values/
  description: The values of the headers in the HTTP response.
  full_title: http.response.headers.values · Cloudflare Ruleset Engine docs
  head_html: <title>http.response.headers.values · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="The values of the headers in the HTTP response."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers.values/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="http.response.headers.values · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The values of the headers in the HTTP response."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers.values/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers.values/#page","headline":"http.response.headers.values \u00b7 Cloudflare Ruleset Engine docs","description":"The values of the headers in the HTTP response.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.headers.values/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/http.response.headers.values/
  schema: 1
---
<h1 id="http-response-headers-values">http.response.headers.values</h1>

**Data type:** Array<String>

<p>The values of the headers in the HTTP response.</p>

<p>The values are not pre-processed and retain the original case used in the response.</p>
<p>The order of header values is not guaranteed but will match <a href="/ruleset-engine/rules-language/fields/reference/http.response.headers.names/"><code>http.response.headers.names</code></a>.</p>
<p>Duplicate headers are listed multiple times.</p>
<ul>
<li><strong>Decoding</strong>: No decoding performed</li>
<li><strong>Whitespace</strong>: Preserved</li>
<li><strong>Non-ASCII</strong>: Preserved</li>
</ul>
<p><strong>Note</strong>: The availability of HTTP response fields depends on the exact Cloudflare feature and your Cloudflare plan.</p>

**Example value:**

```txt
Example 1: ["application/json"]
Example 2: ["This header value is longer than 10 bytes"]
```

**Example usage:**

```txt
# Example 1: Check for specific header value.
any(http.response.headers.values[*] == "application/json")

# Example 2: Match requests according to the specified operator and the length/size entered for the header value.
any(len(http.response.headers.values[*])[*] gt 10)
```

<h2 id="categories">Categories</h2>

- Response
- Headers

**Keywords:** response

