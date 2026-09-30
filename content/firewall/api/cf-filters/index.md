---
cp9:
  canonical: https://developers.cloudflare.com/firewall/api/cf-filters/
  description: Manage filters for firewall rules via the API.
  full_title: Cloudflare Filters API · Cloudflare Firewall Rules (deprecated) docs
  head_html: <title>Cloudflare Filters API · Cloudflare Firewall Rules (deprecated) docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage filters for firewall rules via the API."><link rel="canonical" href="https://developers.cloudflare.com/firewall/api/cf-filters/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/firewall/api/cf-filters/index.md"><meta property="og:title" content="Cloudflare Filters API · Cloudflare Firewall Rules (deprecated) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage filters for firewall rules via the API."><meta property="og:url" content="https://developers.cloudflare.com/firewall/api/cf-filters/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Firewall Rules (deprecated)"><meta name="algolia_product_filter" content="Firewall Rules (deprecated)"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Firewall Rules (deprecated)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/firewall/api/cf-filters/#page","headline":"Cloudflare Filters API \u00b7 Cloudflare Firewall Rules (deprecated) docs","description":"Manage filters for firewall rules via the API.","url":"https://developers.cloudflare.com/firewall/api/cf-filters/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /firewall/api/cf-filters/
  schema: 1
---
<p><strong>Cloudflare Filters</strong> is an API-only component of firewall rules for designing complex criteria that rely on boolean operators and other logic to examine incoming HTTP traffic and look for a match.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/8708.md")
</aside>
<p>For example, a filter matching:</p>
<ul>
<li>An HTTP user agent, and</li>
<li>The HTTP path, and</li>
<li>The source IP address</li>
</ul>
<p>Associate a filter with a firewall rule to define the scope of that rule.</p>
<p>Use IP lists within a filter to refer collectively to a group of IP addresses. Refer to the <a href="/waf/tools/lists/lists-api/">Lists API</a> for more information.</p>
<p>Before getting started with the Cloudflare Filters API, familiarize yourself with rule <a href="/ruleset-engine/rules-language/expressions/">expressions</a>. For a complete reference, refer to <a href="/ruleset-engine/rules-language/">Rules language</a>.</p>
<h2 id="differences-from-other-cloudflare-apis">Differences from other Cloudflare APIs</h2>
<p>The Firewall Rules API behaves differently from most Cloudflare APIs in two ways:</p>
<ul>
<li>API calls accept and return multiple items, and allow applying data changes to multiple items.</li>
<li>Although API calls return the <a href="/fundamentals/api/">standard response</a>, the error object follows the <a href="http://jsonapi.org/format/#errors">JSON API standard</a>, such that in an error condition, it is clear which item produced the error and why.</li>
</ul>
<p>To get started, review <a href="/firewall/api/cf-filters/what-is-a-filter/">What is a filter?</a>, followed by the Cloudflare Filters <a href="/firewall/api/cf-firewall-rules/json-object/">JSON object</a> and <a href="/firewall/api/cf-firewall-rules/endpoints/">Endpoints</a>.</p>
