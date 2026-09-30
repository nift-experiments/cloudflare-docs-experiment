---
cp9:
  canonical: https://developers.cloudflare.com/waf/
  description: The Cloudflare Web Application Firewall (WAF) provides automatic protection from vulnerabilities and the flexibility to create custom rules.
  full_title: Overview · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Overview · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="The Cloudflare Web Application Firewall (WAF) provides automatic protection from vulnerabilities and the flexibility to create custom rules."><link rel="canonical" href="https://developers.cloudflare.com/waf/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/index.md"><meta property="og:title" content="Overview · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The Cloudflare Web Application Firewall (WAF) provides automatic protection from vulnerabilities and the flexibility to create custom rules."><meta property="og:url" content="https://developers.cloudflare.com/waf/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/waf/#page","headline":"Overview \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"The Cloudflare Web Application Firewall (WAF) provides automatic protection from vulnerabilities and the flexibility to create custom rules.","url":"https://developers.cloudflare.com/waf/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/137.md")
</div>
<div class="nb-plan">
<p>Available on all plans</p>
</div>
<p>The Cloudflare Web Application Firewall (Cloudflare WAF) checks incoming web and API requests and filters undesired traffic based on sets of rules called rulesets. The WAF uses the <a href="/ruleset-engine/rules-language/">Rules language</a>, a flexible expression syntax that lets you filter traffic by request properties such as IP address, URL path, headers, and body content.</p>
<p>Learn how to <a href="/waf/get-started/">get started</a>.</p>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/81d50c9845612128e65bf6d04bcf9e3a/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2F5de3fd69-4208-41db-a1ef-076a523f6d00%2Fpublic" title="Application Security dashboard walkthrough" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/138.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/139.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/140.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/141.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/142.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/143.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/144.md")
</div>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Attack score</td>
<td>No</td>
<td>No</td>
<td>Yes (one field)</td>
<td>Yes</td>
</tr>
<tr>
<td>Leaked credentials detection</td>
<td>Yes (one field)</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Malicious uploads detection</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Paid add-on</td>
</tr>
<tr>
<td>AI Security for Apps</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Paid add-on</td>
</tr>
<tr>
<td>Custom rules</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Rate limiting rules</td>
<td>Yes (one rule)</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Advanced Rate Limiting</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Paid add-on</td>
</tr>
<tr>
<td>WAF Managed Rules</td>
<td>Free Managed Ruleset only</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Sensitive Data Detection (SDD)</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Account-level WAF configuration</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Custom lists</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Managed IP Lists</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Email Address Obfuscation</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Hotlink Protection</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Replace insecure JS libraries</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>IP Access rules</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>User Agent Blocking</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Zone Lockdown</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Security Analytics (zone)</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Security Analytics (account)</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Security Events</td>
<td>Yes (sampled logs only)</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Security Events alerts</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Advanced Security Events alerts</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<p>This is a summary of available features per Cloudflare plan. Refer to the documentation of individual features for more details.</p>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/145.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/146.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/147.md")
</div>
