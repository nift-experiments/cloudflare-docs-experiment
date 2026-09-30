---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/
  description: Configure Programmable Flow Protection programs and rules using the Cloudflare API.
  full_title: Configure Programmable Flow Protection via API · Cloudflare DDoS Protection docs
  head_html: <title>Configure Programmable Flow Protection via API · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Programmable Flow Protection programs and rules using the Cloudflare API."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/index.md"><meta property="og:title" content="Configure Programmable Flow Protection via API · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Programmable Flow Protection programs and rules using the Cloudflare API."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/#page","headline":"Configure Programmable Flow Protection via API \u00b7 Cloudflare DDoS Protection docs","description":"Configure Programmable Flow Protection programs and rules using the Cloudflare API.","url":"https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/
  schema: 1
---
<p>Use the <a href="/api/">Cloudflare API</a> to configure Programmable Flow Protection.</p>
<p>For examples of API calls, refer to <a href="/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/examples/">Common API calls</a>.</p>
<h2 id="endpoints">Endpoints</h2>
<p>To obtain the complete endpoint, append the Programmable Flow Protection API endpoints listed below to the Cloudflare API base URL:</p>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4&#10;</code></pre>
<p>The <code>{account_id}</code> argument is the <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> (a hexadecimal string). You can find this value in the Cloudflare dashboard.</p>
<p>The tables in the following sections summarize the available operations.</p>
<h3 id="program-operations">Program operations</h3>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method and endpoint / Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>List programs</td>
<td><p><code>GET accounts/{account_id}/magic/programmable_flow_protection/configs/programs</code></p>Fetches all Programmable Flow Protection programs in the account.</td>
</tr>
<tr>
<td>Upload a program</td>
<td><p><code>POST accounts/{account_id}/magic/programmable_flow_protection/configs/programs</code></p>Uploads a new program to the account. Include the optional <code>X-Program-Name</code> header to specify a human-readable program name. If omitted, the API generates a UUID as the program name.</td>
</tr>
<tr>
<td>Get a program</td>
<td><p><code>GET accounts/{account_id}/magic/programmable_flow_protection/configs/programs/{program_id}</code></p>Fetches the details of an existing program.</td>
</tr>
<tr>
<td>Update a program</td>
<td><p><code>PATCH accounts/{account_id}/magic/programmable_flow_protection/configs/programs/{program_id}</code></p>Updates an existing program.</td>
</tr>
<tr>
<td>Delete a program</td>
<td><p><code>DELETE accounts/{account_id}/magic/programmable_flow_protection/configs/programs/{program_id}</code></p>Deletes an existing program from the account.</td>
</tr>
<tr>
<td>Delete all programs</td>
<td><p><code>DELETE accounts/{account_id}/magic/programmable_flow_protection/configs/programs</code></p>Deletes all existing programs from the account.</td>
</tr>
</tbody>
</table>
<h3 id="rule-operations">Rule operations</h3>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method and endpoint / Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>List rules</td>
<td><p><code>GET accounts/{account_id}/magic/programmable_flow_protection/configs/rules</code></p>Fetches all Programmable Flow Protection rules in the account.</td>
</tr>
<tr>
<td>Create a rule</td>
<td><p><code>POST accounts/{account_id}/magic/programmable_flow_protection/configs/rules</code></p>Creates a new rule in the account.</td>
</tr>
<tr>
<td>Get a rule</td>
<td><p><code>GET accounts/{account_id}/magic/programmable_flow_protection/configs/rules/{rule_id}</code></p>Fetches the details of an existing rule.</td>
</tr>
<tr>
<td>Update a rule</td>
<td><p><code>PATCH accounts/{account_id}/magic/programmable_flow_protection/configs/rules/{rule_id}</code></p>Updates an existing rule in the account.</td>
</tr>
<tr>
<td>Delete a rule</td>
<td><p><code>DELETE accounts/{account_id}/magic/programmable_flow_protection/configs/rules/{rule_id}</code></p>Deletes an existing rule from the account.</td>
</tr>
<tr>
<td>Delete all rules</td>
<td><p><code>DELETE accounts/{account_id}/magic/programmable_flow_protection/configs/rules</code></p>Deletes all existing rules from the account.</td>
</tr>
</tbody>
</table>
<h3 id="debug-operations">Debug operations</h3>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method and endpoint / Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Debug with PCAP</td>
<td><p><code>POST accounts/{account_id}/magic/programmable_flow_protection/configs/programs/{program_id}/pcap</code></p>Runs a program against a PCAP file and returns an annotated PCAP with program verdicts.</td>
</tr>
</tbody>
</table>
<h2 id="pagination">Pagination</h2>
<p>The API operations that return a list of items use pagination. For more information on the available pagination query parameters, refer to <a href="/fundamentals/api/how-to/make-api-calls/#pagination">Pagination</a>.</p>
