---
cp9:
  canonical: https://developers.cloudflare.com/waf/tools/lists/lists-api/
  description: Manage lists programmatically with the Lists API.
  full_title: Lists API · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Lists API · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage lists programmatically with the Lists API."><link rel="canonical" href="https://developers.cloudflare.com/waf/tools/lists/lists-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/tools/lists/lists-api/index.md"><meta property="og:title" content="Lists API · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage lists programmatically with the Lists API."><meta property="og:url" content="https://developers.cloudflare.com/waf/tools/lists/lists-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/waf/tools/lists/lists-api/#page","headline":"Lists API \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Manage lists programmatically with the Lists API.","url":"https://developers.cloudflare.com/waf/tools/lists/lists-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/tools/lists/lists-api/
  schema: 1
---
<p>The <a href="/api/resources/rules/subresources/lists/">Lists API</a> provides an interface for programmatically managing the following types of lists:</p>
<ul>
<li>
<p><a href="/waf/tools/lists/custom-lists/">Custom lists</a>: Contain one or more strings of the same type (such as IP addresses or hostnames) that you can reference collectively, by name, in rule expressions.</p>
</li>
<li>
<p><a href="/rules/url-forwarding/bulk-redirects/concepts/#bulk-redirect-lists">Bulk Redirect Lists</a>: Contain URL redirects that you enable by creating a Bulk Redirect Rule.</p>
</li>
</ul>
<p>To use a list in a rule expression, refer to <a href="/ruleset-engine/rules-language/values/#lists">Lists</a> in the Rules language documentation.</p>
<h2 id="get-started">Get started</h2>
<p>To get started, review the Lists <a href="/waf/tools/lists/lists-api/json-object/">JSON object</a> and <a href="/waf/tools/lists/lists-api/endpoints/">Endpoints</a>.</p>
<hr />
<h2 id="rate-limiting-for-lists-api-requests">Rate limiting for Lists API requests</h2>
<p>Cloudflare may apply rate limiting to your API requests creating, modifying, or deleting list items in custom lists and Bulk Redirect Lists.</p>
<p>Each operation (create, edit, or delete) on a list item counts as a modification. The following limits apply:</p>
<ul>
<li>You can make a maximum of 1,000,000 list item modifications in API requests over 12 hours.</li>
<li>You can make a maximum of 30,000 API requests over 12 hours doing list item modifications.</li>
</ul>
<p>If a write operation is still being processed — which happens asynchronously — and you submit a new request, you will receive a <code>429</code> HTTP status code. When this happens, submit your request again later.</p>
