---
cp9:
  canonical: https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/
  description: Skip WAF managed rules for specific requests with exceptions.
  full_title: Create WAF exceptions · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Create WAF exceptions · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Skip WAF managed rules for specific requests with exceptions."><link rel="canonical" href="https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/index.md"><meta property="og:title" content="Create WAF exceptions · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Skip WAF managed rules for specific requests with exceptions."><meta property="og:url" content="https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/#page","headline":"Create WAF exceptions \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Skip WAF managed rules for specific requests with exceptions.","url":"https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/managed-rules/waf-exceptions/
  schema: 1
---
<p>Create an exception to skip the execution of WAF managed rulesets or some of their rules. The exception configuration includes an expression that defines the skip conditions, and the rules or rulesets to skip under those conditions.</p>
<h2 id="types-of-exceptions">Types of exceptions</h2>
<p>An exception can have one of the following behaviors (from highest to lowest priority):</p>
<ul>
<li>Skip all remaining rules (belonging to WAF managed rulesets)</li>
<li>Skip one or more WAF managed rulesets</li>
<li>Skip one or more rules of WAF managed rulesets</li>
</ul>
<p>For more information on exceptions, refer to <a href="/ruleset-engine/managed-rulesets/create-exception/">Create an exception</a> in the Ruleset Engine documentation.</p>
<h2 id="scope-and-execution-order">Scope and execution order</h2>
<p>You can define exceptions at the account level and at the zone level. The scope of an exception determines which rules it affects:</p>
<ul>
<li>An account-level exception only skips rules configured at the account level. It does not affect zone-level rules.</li>
<li>A zone-level exception only skips rules configured at the zone level. It does not affect account-level rules.</li>
</ul>
<p>Within each phase, account-level rulesets run before zone-level rulesets. This means that if you deploy managed rules at both the account level and the zone level, a request is evaluated against account-level rules first. An exception defined at the zone level will not prevent a match at the account level.</p>
<p>For more information on how WAF features run in sequence, refer to <a href="/waf/feature-interoperability/">Security features interoperability</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15586.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<p>Add exceptions <a href="/waf/managed-rules/waf-exceptions/define-dashboard/">in the Cloudflare dashboard</a> or <a href="/waf/managed-rules/waf-exceptions/define-api/">via API</a>.</p>
