---
cp9:
  canonical: https://developers.cloudflare.com/waf/rate-limiting-rules/find-rate-limit/
  description: Use Security Analytics request rate data to determine an appropriate rate limit.
  full_title: Find an appropriate rate limit · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Find an appropriate rate limit · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Security Analytics request rate data to determine an appropriate rate limit."><link rel="canonical" href="https://developers.cloudflare.com/waf/rate-limiting-rules/find-rate-limit/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/rate-limiting-rules/find-rate-limit/index.md"><meta property="og:title" content="Find an appropriate rate limit · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Security Analytics request rate data to determine an appropriate rate limit."><meta property="og:url" content="https://developers.cloudflare.com/waf/rate-limiting-rules/find-rate-limit/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Rate limiting"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/rate-limiting-rules/find-rate-limit/#page","headline":"Find an appropriate rate limit \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Use Security Analytics request rate data to determine an appropriate rate limit.","url":"https://developers.cloudflare.com/waf/rate-limiting-rules/find-rate-limit/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/rate-limiting-rules/find-rate-limit/
  schema: 1
---
<p>The <strong>Request rate analysis</strong> tab in <a href="/waf/analytics/security-analytics/">Security Analytics</a> displays data on the request rate for traffic matching the selected filters and time period. Use this tab to determine the most appropriate rate limit for incoming traffic matching the applied filters.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15365.md")
</aside>
<h2 id="user-interface-overview">User interface overview</h2>
<p>The <strong>Request rate analysis</strong> tab is available at the zone level in the <strong>Analytics</strong> page.</p>
<p><img src="/assets/upstream/images/waf/rate-limit-analytics.png" alt="Screenshot of the Request rate analysis tab in Security Analytics" /></p>
<p>The main chart displays the distribution of request rates for the top 50 unique clients observed during the selected time interval (for example, <code>1 minute</code>) in descending order. You can group the request rates by the following unique request properties:</p>
<ul>
<li><strong>IP address</strong></li>
<li><a href="/bots/additional-configurations/ja3-ja4-fingerprint/"><strong>JA3 fingerprint</strong></a> (only available to customers with Bot Management)</li>
<li><strong>IP &amp; JA3</strong> (only available to customers with Bot Management)</li>
<li><a href="/bots/additional-configurations/ja3-ja4-fingerprint/"><strong>JA4 fingerprint</strong></a> (only available to customers with Bot Management)</li>
<li><strong>IP &amp; JA4</strong> (only available to customers with Bot Management)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15364.md")
</aside>
<hr />
<h2 id="determine-an-appropriate-rate-limit">Determine an appropriate rate limit</h2>
<h3 id="1-define-the-scope"><ol>
<li>Define the scope</li>
</ol></h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15366.md")
</div>
<h3 id="2-find-the-rate"><ol start="2">
<li>Find the rate</li>
</ol></h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15367.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15363.md")
</aside>
<h3 id="3-validate-your-rate"><ol start="3">
<li>Validate your rate</li>
</ol></h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15368.md")
</div>
<h3 id="4-create-a-rate-limiting-rule"><ol start="4">
<li>Create a rate limiting rule</li>
</ol></h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15369.md")
</div>
