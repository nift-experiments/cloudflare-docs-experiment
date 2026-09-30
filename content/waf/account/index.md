---
cp9:
  canonical: https://developers.cloudflare.com/waf/account/
  description: Configure WAF settings at the account level for multiple zones.
  full_title: Account-level WAF configuration · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Account-level WAF configuration · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure WAF settings at the account level for multiple zones."><link rel="canonical" href="https://developers.cloudflare.com/waf/account/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/account/index.md"><meta property="og:title" content="Account-level WAF configuration · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure WAF settings at the account level for multiple zones."><meta property="og:url" content="https://developers.cloudflare.com/waf/account/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/account/#page","headline":"Account-level WAF configuration \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Configure WAF settings at the account level for multiple zones.","url":"https://developers.cloudflare.com/waf/account/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/account/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15416.md")
</aside>
<p>The account-level Web Application Firewall (WAF) configuration allows you to define a configuration once and apply it to multiple Enterprise zones in your account. Instead of configuring each zone individually, you create rulesets at the account level and use expressions to control which zones and traffic they apply to.</p>
<p>For example, you can deploy a single ruleset that applies to <code>/admin/*</code> URI paths across both <code>example.com</code> and <code>example.net</code>. Rulesets can target all incoming traffic or a specific subset.</p>
<p>At the account level, WAF rules are grouped into rulesets. You can perform the following operations:</p>
<ul>
<li>Create and deploy <a href="/waf/account/custom-rulesets/">custom rulesets</a></li>
<li>Create and deploy <a href="/waf/account/rate-limiting-rulesets/">rate limiting rulesets</a></li>
<li>Deploy <a href="/waf/account/managed-rulesets/">managed rulesets</a></li>
</ul>
