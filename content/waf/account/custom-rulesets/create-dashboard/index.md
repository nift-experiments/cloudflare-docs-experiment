---
cp9:
  canonical: https://developers.cloudflare.com/waf/account/custom-rulesets/create-dashboard/
  description: Create and manage account-level custom rulesets in the dashboard.
  full_title: Work with WAF custom rulesets in the dashboard · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Work with WAF custom rulesets in the dashboard · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and manage account-level custom rulesets in the dashboard."><link rel="canonical" href="https://developers.cloudflare.com/waf/account/custom-rulesets/create-dashboard/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/account/custom-rulesets/create-dashboard/index.md"><meta property="og:title" content="Work with WAF custom rulesets in the dashboard · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and manage account-level custom rulesets in the dashboard."><meta property="og:url" content="https://developers.cloudflare.com/waf/account/custom-rulesets/create-dashboard/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/account/custom-rulesets/create-dashboard/#page","headline":"Work with WAF custom rulesets in the dashboard \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Create and manage account-level custom rulesets in the dashboard.","url":"https://developers.cloudflare.com/waf/account/custom-rulesets/create-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/account/custom-rulesets/create-dashboard/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/15447.md")
</aside>
<h2 id="quota-limits">Quota limits</h2>
<p>Account-level custom rulesets have the following quota limits:</p>
<ul>
<li><strong>Maximum rulesets:</strong> 10</li>
<li><strong>Maximum rules per ruleset:</strong> 100</li>
<li><strong>Total rule quota:</strong> 1,000 rules across all rulesets on the request path</li>
</ul>
<p>The total rule quota of 1,000 rules is a hard limit that applies to all plans and cannot be increased. This limit applies across all rulesets that a request traverses, not just account-level custom rulesets.</p>
<h3 id="redistribute-rules-across-rulesets">Redistribute rules across rulesets</h3>
<p>If you need to change the distribution of rules across your rulesets (for example, to create fewer rulesets with more rules per ruleset), contact Cloudflare Support. Only Cloudflare Support can update account-level entitlements to change the ruleset and rule distribution.</p>
<p>Before contacting Support, consider the following optimizations:</p>
<ul>
<li><strong>Consolidate rules:</strong> Combine rules with similar conditions or actions into a single rule with broader matching criteria.</li>
<li><strong>Remove unused rules:</strong> Audit your rulesets and remove rules that are no longer triggering or are duplicating functionality.</li>
<li><strong>Use IP lists:</strong> Instead of creating multiple rules for individual IP addresses, use <a href="/waf/tools/lists/">IP lists</a> to group IPs and reference them in a single rule.</li>
</ul>
<h2 id="create-and-deploy-a-custom-ruleset">Create and deploy a custom ruleset</h2>
<p>To create and deploy a custom ruleset at the account level:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15448.md")
</div>
<h2 id="edit-a-custom-ruleset">Edit a custom ruleset</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15449.md")
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15445.md")
</aside>
<h2 id="delete-a-custom-ruleset">Delete a custom ruleset</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15450.md")
</div>
<h2 id="configure-a-custom-response-for-blocked-requests">Configure a custom response for blocked requests</h2>
<p>When you select the <em>Block</em> action in a rule you can optionally define a custom response.</p>
<p>The custom response has three settings:</p>
<ul>
<li><strong>With response type</strong>: Choose a content type or the default WAF block response from the list. The available custom response types are the following:</li>
</ul>
<table>
<thead>
<tr>
<th>Dashboard value</th>
<th>API value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Custom HTML</td>
<td><code>&quot;text/html&quot;</code></td>
</tr>
<tr>
<td>Custom Text</td>
<td><code>&quot;text/plain&quot;</code></td>
</tr>
<tr>
<td>Custom JSON</td>
<td><code>&quot;application/json&quot;</code></td>
</tr>
<tr>
<td>Custom XML</td>
<td><code>&quot;text/xml&quot;</code></td>
</tr>
</tbody>
</table>
<ul>
<li>
<p><strong>With response code</strong>: Choose an HTTP status code for the response, in the range 400-499. The default response code is 403.</p>
</li>
<li>
<p><strong>Response body</strong>: The body of the response. Configure a valid body according to the response type you selected. The maximum field size is 2 KB.</p>
</li>
</ul>
