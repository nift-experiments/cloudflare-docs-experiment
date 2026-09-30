---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.headers.values/
  description: The values of the headers in the HTTP response without any transformation.
  full_title: raw.http.response.headers.values · Cloudflare Ruleset Engine docs
  head_html: <title>raw.http.response.headers.values · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="The values of the headers in the HTTP response without any transformation."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.headers.values/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="raw.http.response.headers.values · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The values of the headers in the HTTP response without any transformation."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.headers.values/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.headers.values/#page","headline":"raw.http.response.headers.values \u00b7 Cloudflare Ruleset Engine docs","description":"The values of the headers in the HTTP response without any transformation.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.headers.values/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/raw.http.response.headers.values/
  schema: 1
---
<h1 id="raw-http-response-headers-values">raw.http.response.headers.values</h1>

**Data type:** Array<String>

<p>The values of the headers in the HTTP response without any transformation.</p>

<p>This is the raw field version of the <a href="/ruleset-engine/rules-language/fields/reference/http.response.headers.values/"><code>http.response.headers.values</code></a> field. Raw fields, prefixed with <code>raw.</code>, preserve original response values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.</p>

**Example value:**

```txt
Example 1: ["application/json"]
Example 2: ["This header value is longer than 10 bytes"]
```

**Example usage:**

```txt
# Example 1: Check for specific header value.
any(raw.http.response.headers.values[*] == "application/json")

# Example 2: Match requests according to the specified operator and the length/size entered for the header value.
any(len(raw.http.response.headers.values[*])[*] gt 10)
```

<h2 id="categories">Categories</h2>

- Response
- Headers
- Raw fields

**Keywords:** response, raw

