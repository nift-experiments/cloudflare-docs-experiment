---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/
  description: Configure Advanced DNS Protection rules and settings using the Cloudflare API.
  full_title: Configure Advanced DNS Protection via API · Cloudflare DDoS Protection docs
  head_html: <title>Configure Advanced DNS Protection via API · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Advanced DNS Protection rules and settings using the Cloudflare API."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/index.md"><meta property="og:title" content="Configure Advanced DNS Protection via API · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Advanced DNS Protection rules and settings using the Cloudflare API."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/#page","headline":"Configure Advanced DNS Protection via API \u00b7 Cloudflare DDoS Protection docs","description":"Configure Advanced DNS Protection rules and settings using the Cloudflare API.","url":"https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/dns-protection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/advanced-ddos-systems/api/dns-protection/
  schema: 1
---
<p>Use the <a href="/api/">Cloudflare API</a> to configure Advanced DNS Protection via API.</p>
<p>For examples of API calls, refer to <a href="/ddos-protection/advanced-ddos-systems/api/dns-protection/examples/">Common API calls</a>.</p>
<h2 id="endpoints">Endpoints</h2>
<p>To obtain the complete endpoint, append the Advanced DNS Protection API endpoints listed below to the Cloudflare API base URL:</p>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4&#10;</code></pre>
<p>The <code>{account_id}</code> argument is the <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> (a hexadecimal string). You can find this value in the Cloudflare dashboard.</p>
<p>The following table summarizes the available operations.</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Verb + Endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td>List DNS protection rules</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules</code></p>Fetches all DNS protection rules in the account.</td>
</tr>
<tr>
<td>Add a DNS protection rule</td>
<td><p><code>POST accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules</code></p>Adds a DNS protection rule to the account.</td>
</tr>
<tr>
<td>Get a DNS protection rule</td>
<td><p><code>GET accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules/{rule_id}</code></p>Fetches the details of an existing DNS protection rule in the account.</td>
</tr>
<tr>
<td>Update a DNS protection rule</td>
<td><p><code>PATCH accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules/{rule_id}</code></p>Updates an existing DNS protection rule in the account.</td>
</tr>
<tr>
<td>Delete a DNS protection rule</td>
<td><p><code>DELETE accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules/{rule_id}</code></p>Deletes an existing DNS protection rule from the account.</td>
</tr>
<tr>
<td>Delete all DNS protection rules</td>
<td><p><code>DELETE accounts/{account_id}/magic/advanced_dns_protection/configs/dns_protection/rules</code></p>Deletes all existing DNS protection rules from the account.</td>
</tr>
</tbody>
</table>
