---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.sec/
  description: The timestamp when Cloudflare received the request, expressed as UNIX time in seconds.
  full_title: http.request.timestamp.sec · Cloudflare Ruleset Engine docs
  head_html: <title>http.request.timestamp.sec · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="The timestamp when Cloudflare received the request, expressed as UNIX time in seconds."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.sec/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="http.request.timestamp.sec · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The timestamp when Cloudflare received the request, expressed as UNIX time in seconds."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.sec/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.sec/#page","headline":"http.request.timestamp.sec \u00b7 Cloudflare Ruleset Engine docs","description":"The timestamp when Cloudflare received the request, expressed as UNIX time in seconds.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.timestamp.sec/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/http.request.timestamp.sec/
  schema: 1
---
<h1 id="http-request-timestamp-sec">http.request.timestamp.sec</h1>

**Data type:** Integer

<p>The timestamp when Cloudflare received the request, expressed as UNIX time in seconds.</p>

<p>The field value is 10 digits long.</p>
<p>When validating HMAC tokens in an expression, pass this field as the <code>currentTimestamp</code> argument to the <a href="/ruleset-engine/rules-language/functions/#hmac-validation"><code>is_timed_hmac_valid_v0()</code></a> validation function.</p>
<p>To obtain the timestamp milliseconds, use the <a href="/ruleset-engine/rules-language/fields/reference/http.request.timestamp.msec/"><code>http.request.timestamp.msec</code></a> field.</p>

**Example value:**

```txt
1484063137
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, timestamp, client, visitor

