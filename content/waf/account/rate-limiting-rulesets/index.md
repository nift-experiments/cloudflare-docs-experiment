---
cp9:
  canonical: https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/
  description: Create rate limiting rulesets at the account level for multiple Enterprise zones.
  full_title: Rate limiting rulesets · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Rate limiting rulesets · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Create rate limiting rulesets at the account level for multiple Enterprise zones."><link rel="canonical" href="https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/index.md"><meta property="og:title" content="Rate limiting rulesets · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create rate limiting rulesets at the account level for multiple Enterprise zones."><meta property="og:url" content="https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/#page","headline":"Rate limiting rulesets \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Create rate limiting rulesets at the account level for multiple Enterprise zones.","url":"https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/account/rate-limiting-rulesets/
  schema: 1
---
<p><a href="/waf/rate-limiting-rules/">Rate limiting rules</a> allow you to define a <span class="nb-glossary-tooltip" title="rate limiting">rate limit</span> for requests matching an <a href="/ruleset-engine/rules-language/expressions/">expression</a>, and the action to perform when that rate limit is reached. You can configure rate limiting rules for a single zone or at the account level.</p>
<p>Account-level rate limiting rulesets allow you to define rate limiting rules once and deploy them to multiple Enterprise zones. Instead of configuring the same rules in each zone, you create a ruleset at the account level and control which zones it applies to.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15417.md")
</aside>
<p>To apply a rate limiting ruleset at the account level:</p>
<ol>
<li>Create a rate limiting ruleset with one or more rate limiting rules.</li>
<li>Deploy the ruleset to one or more zones on an Enterprise plan.</li>
</ol>
<p>For more information on how Cloudflare calculates request rates, refer to <a href="/waf/rate-limiting-rules/request-rate/">Request rate calculation</a>.</p>
<h2 id="next-steps">Next steps</h2>
<p>For instructions on creating and deploying a rate limiting ruleset, refer to the following pages:</p>
<ul>
<li><a href="/waf/account/rate-limiting-rulesets/create-dashboard/">Create a rate limiting ruleset in the dashboard</a></li>
<li><a href="/waf/account/rate-limiting-rulesets/create-api/">Create a rate limiting ruleset using the API</a></li>
</ul>
<p>For Terraform examples, refer to <a href="/terraform/additional-configurations/rate-limiting-rules/">Rate limiting rules configuration using Terraform</a>.</p>
