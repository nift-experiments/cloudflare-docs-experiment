---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.query/
  description: The entire query string without the ? delimiter and without any transformation.
  full_title: raw.http.request.uri.query · Cloudflare Ruleset Engine docs
  head_html: <title>raw.http.request.uri.query · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="The entire query string without the ? delimiter and without any transformation."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.query/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="raw.http.request.uri.query · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The entire query string without the ? delimiter and without any transformation."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.query/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.query/#page","headline":"raw.http.request.uri.query \u00b7 Cloudflare Ruleset Engine docs","description":"The entire query string without the ? delimiter and without any transformation.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.request.uri.query/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/raw.http.request.uri.query/
  schema: 1
---
<h1 id="raw-http-request-uri-query">raw.http.request.uri.query</h1>

**Data type:** String

<p>The entire query string without the <code>?</code> delimiter and without any transformation.</p>

<p>This is the raw field version of the <a href="/ruleset-engine/rules-language/fields/reference/http.request.uri.query/"><code>http.request.uri.query</code></a> field. Raw fields, prefixed with <code>raw.</code>, preserve original request values for later evaluations. These fields are immutable during the entire request evaluation workflow, and they are not affected by the actions of previously matched rules.</p>
<p><strong>Note</strong>: This raw field may include some basic normalization done by Cloudflare's HTTP server. However, this can change in the future.</p>

<h2 id="categories">Categories</h2>

- Request
- URI
- Raw fields

**Keywords:** request, uri, url, query, query string, raw, client, visitor

