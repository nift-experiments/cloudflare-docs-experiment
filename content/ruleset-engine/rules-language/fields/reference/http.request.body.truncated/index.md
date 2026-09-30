---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.truncated/
  description: Indicates whether the HTTP request body is truncated.
  full_title: http.request.body.truncated · Cloudflare Ruleset Engine docs
  head_html: <title>http.request.body.truncated · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Indicates whether the HTTP request body is truncated."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.truncated/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="http.request.body.truncated · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Indicates whether the HTTP request body is truncated."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.truncated/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.truncated/#page","headline":"http.request.body.truncated \u00b7 Cloudflare Ruleset Engine docs","description":"Indicates whether the HTTP request body is truncated.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.truncated/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ruleset-engine/rules-language/fields/reference/http.request.body.truncated/
  schema: 1
---
<h1 id="http-request-body-truncated">http.request.body.truncated</h1>

**Data type:** Boolean

<p>Indicates whether the HTTP request body is truncated.</p>

<p>When <code>true</code>, <code>http.request.body.*</code> fields may not contain all of the HTTP request body.</p>
<p>Requires a Cloudflare Enterprise plan.</p>

<aside class="nb-aside nb-aside-caution"><p>All <code>http.request.body.*</code> fields (except <a href="/ruleset-engine/rules-language/fields/reference/http.request.body.size/"><code>http.request.body.size</code></a>) handle a given maximum body size, which varies per plan. For Enterprise customers, the maximum body size is 128 KB. For other paid plans, the limit is lower by default. For users in the Free plan, the limit is 1 MB.</p>
<p>You cannot define expressions that rely on request body data beyond the maximum size set for your plan. If the request body is larger, body fields contain a truncated value and <a href="/ruleset-engine/rules-language/fields/reference/http.request.body.truncated/"><code>http.request.body.truncated</code></a> is set to <code>true</code>. The <code>http.request.body.size</code> field contains the full request size without truncation.</p>
<p>The maximum body size applies only to HTTP body field values; the origin server still receives the complete request body.</p></aside>

<h2 id="categories">Categories</h2>

- Request
- Body

**Keywords:** request, body, client, visitor

