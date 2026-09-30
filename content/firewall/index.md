---
cp9:
  canonical: https://developers.cloudflare.com/firewall/
  description: Create rules to inspect and act on incoming HTTP traffic.
  full_title: Cloudflare Firewall Rules (deprecated) · Cloudflare Firewall Rules (deprecated) docs
  head_html: <title>Cloudflare Firewall Rules (deprecated) · Cloudflare Firewall Rules (deprecated) docs</title><meta name="generator" content="Nift"><meta name="description" content="Create rules to inspect and act on incoming HTTP traffic."><link rel="canonical" href="https://developers.cloudflare.com/firewall/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/firewall/index.md"><meta property="og:title" content="Cloudflare Firewall Rules (deprecated) · Cloudflare Firewall Rules (deprecated) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create rules to inspect and act on incoming HTTP traffic."><meta property="og:url" content="https://developers.cloudflare.com/firewall/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Firewall Rules (deprecated)"><meta name="algolia_product_filter" content="Firewall Rules (deprecated)"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Firewall Rules (deprecated)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/firewall/#page","headline":"Cloudflare Firewall Rules (deprecated) \u00b7 Cloudflare Firewall Rules (deprecated) docs","description":"Create rules to inspect and act on incoming HTTP traffic.","url":"https://developers.cloudflare.com/firewall/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /firewall/
  schema: 1
---
<p>Cloudflare Firewall Rules allows you to create rules that inspect incoming traffic and block, challenge, log, or allow specific requests.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/1022.md")
</aside>
<h2 id="main-features">Main features</h2>
<ul>
<li><strong>Rule-based protection</strong>: Use pre-defined rulesets provided by Cloudflare, or define your own firewall rules. Create rules in the Cloudflare dashboard or via API.</li>
<li><strong>Complex custom rules</strong>: Each rule's expression can reference multiple fields from all the available HTTP request parameters and fields, allowing you to create complex rules.</li>
</ul>
<h2 id="availability">Availability</h2>
<p>This table outlines the Firewall Rules features and entitlements available with each customer plan:</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Number of rules</td>
<td>5</td>
<td>20</td>
<td>100</td>
<td>1,000</td>
</tr>
<tr>
<td>Supported actions</td>
<td>All except Log</td>
<td>All except Log</td>
<td>All except Log</td>
<td>All</td>
</tr>
<tr>
<td>Regex support</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>
<p>Unless you are already an advanced user, refer to <a href="/ruleset-engine/rules-language/expressions/">Expressions</a> and <a href="/firewall/cf-firewall-rules/actions/">Actions</a> to learn more about the basic elements of firewall rules.</p>
</li>
<li>
<p>To start building your own firewall rules, refer to one of the following pages:</p>
<ul>
<li><a href="/firewall/cf-dashboard/create-edit-delete-rules/">Manage firewall rules in the dashboard</a></li>
<li><a href="/firewall/api/">Manage firewall rules via the APIs</a></li>
</ul>
</li>
<li>
<p>You can also manage firewall rules through Terraform. For more information, refer to <a href="https://blog.cloudflare.com/getting-started-with-terraform-and-cloudflare-part-1/">Getting Started with Terraform</a>.</p>
</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/ruleset-engine/rules-language/">Cloudflare Rules language</a></li>
</ul>
