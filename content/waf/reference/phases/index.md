---
cp9:
  canonical: https://developers.cloudflare.com/waf/reference/phases/
  description: WAF rule execution phases and their order of evaluation.
  full_title: WAF phases · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>WAF phases · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="WAF rule execution phases and their order of evaluation."><link rel="canonical" href="https://developers.cloudflare.com/waf/reference/phases/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/reference/phases/index.md"><meta property="og:title" content="WAF phases · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="WAF rule execution phases and their order of evaluation."><meta property="og:url" content="https://developers.cloudflare.com/waf/reference/phases/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/reference/phases/#page","headline":"WAF phases \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"WAF rule execution phases and their order of evaluation.","url":"https://developers.cloudflare.com/waf/reference/phases/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/reference/phases/
  schema: 1
---
<p>The Web Application Firewall provides the following <a href="/ruleset-engine/about/phases/">phases</a> where you can create rulesets and rules:</p>
<ul>
<li><code>http_request_firewall_custom</code></li>
<li><code>http_ratelimit</code></li>
<li><code>http_request_firewall_managed</code></li>
</ul>
<p>These phases exist both at the account level and at the zone level. Considering the available phases and the two different levels, rules will be evaluated in the following order:</p>
<table>
<thead>
<tr>
<th>Security feature</th>
<th>Scope</th>
<th>Phase</th>
<th>Ruleset kind</th>
<th>Location in the dashboard</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/waf/account/custom-rulesets/">Custom rulesets</a><br/></td>
<td>Account</td>
<td><code>http_request_firewall_custom</code></td>
<td><code>custom</code> (create)<br/><code>root</code> (deploy)</td>
<td><span class="nb-dash-button"></span> &gt; <strong>Custom rulesets</strong> tab</td>
</tr>
<tr>
<td><a href="/waf/custom-rules/">Custom rules</a></td>
<td>Zone</td>
<td><code>http_request_firewall_custom</code></td>
<td><code>zone</code></td>
<td><span class="nb-dash-button"></span></td>
</tr>
<tr>
<td><a href="/waf/account/rate-limiting-rulesets/">Rate limiting rulesets</a></td>
<td>Account</td>
<td><code>http_ratelimit</code></td>
<td><code>root</code></td>
<td><span class="nb-dash-button"></span> &gt; <strong>Rate limiting rulesets</strong> tab</td>
</tr>
<tr>
<td><a href="/waf/rate-limiting-rules/">Rate limiting rules</a></td>
<td>Zone</td>
<td><code>http_ratelimit</code></td>
<td><code>zone</code></td>
<td><span class="nb-dash-button"></span></td>
</tr>
<tr>
<td><a href="/waf/account/managed-rulesets/">Managed rulesets</a></td>
<td>Account</td>
<td><code>http_request_firewall_managed</code></td>
<td><code>root</code></td>
<td><span class="nb-dash-button"></span> &gt; <strong>Managed rulesets</strong> tab</td>
</tr>
<tr>
<td><a href="/waf/managed-rules/">Managed rules</a></td>
<td>Zone</td>
<td><code>http_request_firewall_managed</code></td>
<td><code>zone</code></td>
<td><span class="nb-dash-button"></span></td>
</tr>
</tbody>
</table>
<p>To learn more about phases, refer to <a href="/ruleset-engine/about/phases/">Phases</a> in the Ruleset Engine documentation.</p>
