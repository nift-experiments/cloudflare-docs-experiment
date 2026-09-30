---
cp9:
  canonical: https://developers.cloudflare.com/rules/origin-rules/faq/
  description: Answers to common questions about origin rules.
  full_title: Origin Rules FAQ · Cloudflare Rules docs
  head_html: <title>Origin Rules FAQ · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Answers to common questions about origin rules."><link rel="canonical" href="https://developers.cloudflare.com/rules/origin-rules/faq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/origin-rules/faq/index.md"><meta property="og:title" content="Origin Rules FAQ · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Answers to common questions about origin rules."><meta property="og:url" content="https://developers.cloudflare.com/rules/origin-rules/faq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Faq"><meta name="algolia_content_type" content="Faq"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/origin-rules/faq/#page","headline":"Origin Rules FAQ \u00b7 Cloudflare Rules docs","description":"Answers to common questions about origin rules.","url":"https://developers.cloudflare.com/rules/origin-rules/faq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/origin-rules/faq/
  schema: 1
---
<p>Below you will find answers to the most commonly asked questions regarding Origin Rules.</p>
<h2 id="what-happens-if-i-use-both-an-origin-rule-and-a-page-rule-to-perform-a-host-header-dns-record-override">What happens if I use both an origin rule and a page rule to perform a Host header/DNS record override?</h2>
<p>In this situation the origin rule parameters will override the <a href="/rules/page-rules/">page rule</a> parameters.</p>
<p>Consider the following example scenarios:</p>
<ul>
<li>A page rule defines a Host header override, but not a resolve override (or DNS record override). An origin rule defines a DNS record override, but not a Host header override. The resulting request will have the <code>Host</code> header defined by the page rule and the origin hostname defined by the origin rule.</li>
<li>A page rule defines a Host header override, and an origin rule also defines a Host header override. The resulting request will have the <code>Host</code> header defined by the origin rule.</li>
</ul>
<h2 id="will-cloudflare-automatically-migrate-my-page-rules-with-host-header-and-dns-record-overrides-to-origin-rules">Will Cloudflare automatically migrate my Page Rules with Host header and DNS record overrides to origin rules?</h2>
<p>Yes. Refer to the <a href="/rules/reference/page-rules-migration/">Page Rules migration guide</a> for any updates on the migration process.</p>
<h2 id="what-happens-if-more-than-one-origin-rule-matches-the-current-request">What happens if more than one origin rule matches the current request?</h2>
<p>If two or more origin rules match a request, the configuration of those rules is merged. While merging two configurations, the settings of later rules will override the settings defined in previous rules, updating or adding configuration properties. The final configuration applied by Cloudflare will be this merged version.</p>
<p>For example, if you configure the following two <a href="/rules/origin-rules/">origin rules</a> and both rules match, Cloudflare will use the destination port set by the first rule, and the DNS hostname override and <code>Host</code> header value set by the second rule.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/12963.md")
</div>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/12964.md")
</div>
<details class="nb-details"><summary>JSON example for API users</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/12965.md")
</div></details>
<p>The merged configuration to apply would be the following:</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set <code>Host</code> header</td>
<td><code>example.net</code></td>
</tr>
<tr>
<td>Set destination port</td>
<td><code>8081</code></td>
</tr>
<tr>
<td>Set DNS hostname</td>
<td><code>example.net</code></td>
</tr>
</tbody>
</table>
<p>If you also configured a destination port in rule #2, that value would override the <code>8081</code> destination port defined in rule #1.</p>
