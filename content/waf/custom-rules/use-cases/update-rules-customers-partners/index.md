---
cp9:
  canonical: https://developers.cloudflare.com/waf/custom-rules/use-cases/update-rules-customers-partners/
  description: Manage custom rules for customer and partner traffic.
  full_title: Update custom rules for customers or partners · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Update custom rules for customers or partners · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage custom rules for customer and partner traffic."><link rel="canonical" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/update-rules-customers-partners/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/update-rules-customers-partners/index.md"><meta property="og:title" content="Update custom rules for customers or partners · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage custom rules for customer and partner traffic."><meta property="og:url" content="https://developers.cloudflare.com/waf/custom-rules/use-cases/update-rules-customers-partners/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/custom-rules/use-cases/update-rules-customers-partners/#page","headline":"Update custom rules for customers or partners \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Manage custom rules for customer and partner traffic.","url":"https://developers.cloudflare.com/waf/custom-rules/use-cases/update-rules-customers-partners/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/custom-rules/use-cases/update-rules-customers-partners/
  schema: 1
---
<p>You may want to adjust your <a href="/waf/custom-rules/create-dashboard/">custom rules</a> to increase access by customers or partners.</p>
<p>Potential examples include:</p>
<ul>
<li>Removing rate limiting for an API</li>
<li>Sharing brand assets and marketing materials</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15454.md")
</aside>
<h2 id="use-asn-in-custom-rules">Use ASN in custom rules</h2>
<p>If a customer or partner is large enough, you could set up a custom rule based on an <a href="https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/">autonomous system number (ASN)</a>.</p>
<h3 id="allow-traffic-by-asn">Allow traffic by ASN</h3>
<p>This example uses:</p>
<ul>
<li>The <a href="/ruleset-engine/rules-language/fields/reference/ip.src.asnum/"><code>ip.src.asnum</code></a> field to specify the general region.</li>
<li>The <a href="/ruleset-engine/rules-language/fields/reference/cf.bot_management.score/"><code>cf.bot_management.score</code></a> field to ensure partner traffic does not come from bots.</li>
</ul>
<p>Example custom rule:</p>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>AS Num</td>
<td>equals</td>
<td><code>64496</code></td>
<td>And</td>
</tr>
<tr>
<td>Bot Score</td>
<td>greater than</td>
<td><code>30</code></td>
<td></td>
</tr>
</tbody>
</table>
<p>If you are using the expression editor:<br/>
<code>(ip.src.asnum eq 64496 and cf.bot_management.score gt 30)</code></p>
<ul>
<li><strong>Then take action</strong>: <em>Skip:</em>
<ul>
<li><em>All remaining custom rules</em></li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15453.md")
</aside>
<h3 id="adjust-rules-by-asn">Adjust rules by ASN</h3>
<p>This example custom rule uses:</p>
<ul>
<li>The <a href="/ruleset-engine/rules-language/fields/reference/ip.src.asnum/"><code>ip.src.asnum</code></a> field to specify the general region.</li>
<li>The <a href="/ruleset-engine/rules-language/fields/reference/cf.bot_management.score/"><code>cf.bot_management.score</code></a> field to check if the request comes from a human.</li>
</ul>
<p>If a request meets these criteria, the custom rule will skip <a href="/waf/tools/user-agent-blocking/">User Agent Blocking</a> rules.</p>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>AS Num</td>
<td>equals</td>
<td><code>64496</code></td>
<td>And</td>
</tr>
<tr>
<td>Bot Score</td>
<td>greater than</td>
<td><code>50</code></td>
<td></td>
</tr>
</tbody>
</table>
<p>If you are using the expression editor:<br/>
<code>(ip.src.asnum eq 64496 and cf.bot_management.score gt 50)</code></p>
<ul>
<li><strong>Then take action</strong>: <em>Skip:</em>
<ul>
<li><em>User Agent Blocking</em></li>
</ul>
</li>
</ul>
<h2 id="use-ip-addresses-in-custom-rules">Use IP addresses in custom rules</h2>
<p>For smaller organizations, you could set up custom rules based on IP addresses.</p>
<h3 id="allow-traffic-by-ip-address">Allow traffic by IP address</h3>
<p>This example:</p>
<ul>
<li>Specifies the source IP address and the host.</li>
<li>Uses the <a href="/ruleset-engine/rules-language/fields/reference/cf.bot_management.score/"><code>cf.bot_management.score</code></a> field to ensure requests are not high-risk traffic.</li>
</ul>
<p>Example custom rule:</p>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>IP Source Address</td>
<td>equals</td>
<td><code>203.0.113.1</code></td>
<td>And</td>
</tr>
<tr>
<td>Hostname</td>
<td>equals</td>
<td><code>example.com</code></td>
<td>And</td>
</tr>
<tr>
<td>Bot Score</td>
<td>greater than</td>
<td><code>30</code></td>
<td></td>
</tr>
</tbody>
</table>
<p>If you are using the expression editor:<br/>
<code>(ip.src eq 203.0.113.1 and http.host eq &quot;example.com&quot; and cf.bot_management.score gt 30)</code></p>
<ul>
<li><strong>Then take action</strong>: <em>Skip:</em>
<ul>
<li><em>All remaining custom rules</em></li>
</ul>
</li>
</ul>
<h3 id="adjust-rules-by-ip-address">Adjust rules by IP address</h3>
<p>This example custom rule specifies the source IP address and the host.</p>
<p>If a request meets these criteria, the custom rule will skip <a href="/waf/rate-limiting-rules/">rate limiting rules</a>.</p>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>IP Source Address</td>
<td>equals</td>
<td><code>203.0.113.1</code></td>
<td>And</td>
</tr>
<tr>
<td>Hostname</td>
<td>equals</td>
<td><code>example.com</code></td>
<td></td>
</tr>
</tbody>
</table>
<p>If you are using the expression editor:<br/>
<code>(ip.src eq 203.0.113.1 and http.host eq &quot;example.com&quot;)</code></p>
<ul>
<li><strong>Then take action</strong>: <em>Skip:</em>
<ul>
<li><em>All remaining custom rules</em></li>
</ul>
</li>
</ul>
