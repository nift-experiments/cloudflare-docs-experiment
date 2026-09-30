---
cp9:
  canonical: https://developers.cloudflare.com/waf/tools/lists/managed-lists/
  description: Pre-built lists managed by Cloudflare for use in rule expressions.
  full_title: Managed Lists · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Managed Lists · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Pre-built lists managed by Cloudflare for use in rule expressions."><link rel="canonical" href="https://developers.cloudflare.com/waf/tools/lists/managed-lists/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/tools/lists/managed-lists/index.md"><meta property="og:title" content="Managed Lists · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Pre-built lists managed by Cloudflare for use in rule expressions."><meta property="og:url" content="https://developers.cloudflare.com/waf/tools/lists/managed-lists/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/tools/lists/managed-lists/#page","headline":"Managed Lists \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Pre-built lists managed by Cloudflare for use in rule expressions.","url":"https://developers.cloudflare.com/waf/tools/lists/managed-lists/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/tools/lists/managed-lists/
  schema: 1
---
<p>Cloudflare provides Managed Lists you can use in rule expressions. These lists are regularly updated.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15711.md")
</aside>
<h2 id="managed-ip-lists">Managed IP Lists</h2>
<p>Use Managed IP Lists to access Cloudflare's IP threat intelligence.</p>
<p>Cloudflare provides the following Managed IP Lists:</p>
<table>
<thead>
<tr>
<th>Display name</th>
<th>Name in expressions</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Open Proxies</td>
<td><code>cf.open_proxies</code></td>
<td>IP addresses of known open HTTP and SOCKS proxy endpoints, which are frequently used to launch attacks and hide attackers identity.</td>
</tr>
<tr>
<td>Cloudflare Anonymizers</td>
<td><code>cf.anonymizer</code></td>
<td>IP addresses of known anonymizers (Open SOCKS Proxies, VPNs, and TOR nodes).</td>
</tr>
<tr>
<td>Cloudflare VPNs</td>
<td><code>cf.vpn</code></td>
<td>IP addresses of known VPN servers.</td>
</tr>
<tr>
<td>Cloudflare Malware</td>
<td><code>cf.malware</code></td>
<td>IP addresses of known sources of malware.</td>
</tr>
<tr>
<td>Cloudflare Botnets, Command and Control Servers</td>
<td><code>cf.botnetcc</code></td>
<td>IP addresses of known botnet command-and-control servers.</td>
</tr>
</tbody>
</table>
<br />
