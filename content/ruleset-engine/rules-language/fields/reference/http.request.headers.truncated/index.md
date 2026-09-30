---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/
  description: Indicates whether the HTTP request contains too many headers.
  full_title: http.request.headers.truncated · Cloudflare Ruleset Engine docs
  head_html: <title>http.request.headers.truncated · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Indicates whether the HTTP request contains too many headers."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="http.request.headers.truncated · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Indicates whether the HTTP request contains too many headers."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/#page","headline":"http.request.headers.truncated \u00b7 Cloudflare Ruleset Engine docs","description":"Indicates whether the HTTP request contains too many headers.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/http.request.headers.truncated/
  schema: 1
---
<h1 id="http-request-headers-truncated">http.request.headers.truncated</h1>

**Data type:** Boolean

<p>Indicates whether the HTTP request contains too many headers.</p>

<p>When <code>true</code>, <a href="/ruleset-engine/rules-language/fields/reference/http.request.headers/"><code>http.request.headers</code></a>, <a href="/ruleset-engine/rules-language/fields/reference/http.request.headers.names/"><code>http.request.headers.names</code></a>, and <a href="/ruleset-engine/rules-language/fields/reference/http.request.headers.values/"><code>http.request.headers.values</code></a> may not contain all of the headers sent in the HTTP request.</p>

<h2 id="categories">Categories</h2>

- Request
- Headers

**Keywords:** request, client, visitor

