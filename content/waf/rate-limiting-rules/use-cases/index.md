---
cp9:
  canonical: https://developers.cloudflare.com/waf/rate-limiting-rules/use-cases/
  description: Sample rate limiting rule configurations for login pages, APIs, and geographic restrictions.
  full_title: Rate limiting rule examples · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Rate limiting rule examples · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Sample rate limiting rule configurations for login pages, APIs, and geographic restrictions."><link rel="canonical" href="https://developers.cloudflare.com/waf/rate-limiting-rules/use-cases/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/rate-limiting-rules/use-cases/index.md"><meta property="og:title" content="Rate limiting rule examples · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Sample rate limiting rule configurations for login pages, APIs, and geographic restrictions."><meta property="og:url" content="https://developers.cloudflare.com/waf/rate-limiting-rules/use-cases/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Rate limiting"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/rate-limiting-rules/use-cases/#page","headline":"Rate limiting rule examples \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Sample rate limiting rule configurations for login pages, APIs, and geographic restrictions.","url":"https://developers.cloudflare.com/waf/rate-limiting-rules/use-cases/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/rate-limiting-rules/use-cases/
  schema: 1
---
<p>The examples below include sample rate limiting rule configurations.</p>
<h2 id="example-1">Example 1</h2>
<p>The following <a href="/waf/rate-limiting-rules/create-zone-dashboard/">rate limiting rule</a> performs rate limiting on incoming requests from the US addressed at the login page, except for one allowed IP address.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/15346.md")
</div>
<h2 id="example-2">Example 2</h2>
<p>The following <a href="/waf/rate-limiting-rules/create-zone-dashboard/">rate limiting rule</a> performs rate limiting on incoming requests with a given base URI path, incrementing on the IP address and the provided API key.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-3">Example</h3>
@markup("md", "content/.markup/bodies/15347.md")
</div>
<h2 id="example-3-1">Example 3</h2>
<p>The following <a href="/waf/rate-limiting-rules/create-zone-dashboard/">rate limiting rule</a> performs rate limiting on requests targeting multiple URI paths in two hosts, excluding known bots. The request rate is based on IP address and <code>User-Agent</code> values.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-4">Example</h3>
@markup("md", "content/.markup/bodies/15348.md")
</div>
<h2 id="example-4-1">Example 4</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15345.md")
</aside>
<p>The following <a href="/waf/rate-limiting-rules/create-zone-dashboard/">rate limiting rule</a> performs complexity-based rate limiting. The rule takes into account the <code>my-score</code> HTTP response header provided by the origin server to calculate a total complexity score for the client with the provided API key.</p>
<p>The counter with the total score is updated when there is a match for the rate limiting rule's <a href="/waf/rate-limiting-rules/parameters/#increment-counter-when">counting expression</a> (in this case, the same as the rule expression since a counting expression was not provided). When this total score becomes larger than <code>400</code> during a period of one minute, any later client requests will be blocked for a period of 10 minutes.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-5">Example</h3>
@markup("md", "content/.markup/bodies/15349.md")
</div>
<p>For an API example with this rule configuration, refer to <a href="/waf/rate-limiting-rules/create-api/#example-d---complexity-based-rate-limiting-rule">Create a rate limiting rule via API</a>.</p>
