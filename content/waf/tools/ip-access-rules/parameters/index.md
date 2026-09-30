---
cp9:
  canonical: https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/
  description: Configurable parameters for IP Access rules.
  full_title: IP Access rules parameters · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>IP Access rules parameters · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Configurable parameters for IP Access rules."><link rel="canonical" href="https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/index.md"><meta property="og:title" content="IP Access rules parameters · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configurable parameters for IP Access rules."><meta property="og:url" content="https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="IPv4,IPv6,Geolocation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/#page","headline":"IP Access rules parameters \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Configurable parameters for IP Access rules.","url":"https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["IPv4","IPv6","Geolocation"]}</script>
  markdown: true
  noindex: false
  route: /waf/tools/ip-access-rules/parameters/
  schema: 1
---
<p>An IP Access rule will apply a certain action to incoming traffic based on the visitor's IP address, IP range, Autonomous System Number (ASN), or country.</p>
<h2 id="ip-address">IP address</h2>
<table>
<thead>
<tr>
<th>Type</th>
<th>Example value</th>
</tr>
</thead>
<tbody>
<tr>
<td>IPv4 address</td>
<td><code>192.0.2.3</code></td>
</tr>
<tr>
<td>IPv6 address</td>
<td><code>2001:db8::</code></td>
</tr>
</tbody>
</table>
<h2 id="ip-range">IP range</h2>
<table>
<thead>
<tr>
<th>Type</th>
<th>Example value</th>
<th>Start of range</th>
<th>End of range</th>
<th align="right">Number of addresses</th>
</tr>
</thead>
<tbody>
<tr>
<td>IPv4 <code>/24</code> range</td>
<td><code>192.0.2.0/24</code></td>
<td><code>192.0.2.0</code></td>
<td><code>192.0.2.255</code></td>
<td align="right">256</td>
</tr>
<tr>
<td>IPv4 <code>/16</code> range</td>
<td><code>192.168.0.0/16</code></td>
<td><code>192.168.0.0</code></td>
<td><code>192.168.255.255</code></td>
<td align="right">65,536</td>
</tr>
<tr>
<td>IPv6 <code>/128</code> range</td>
<td><code>2001:db8::/128</code></td>
<td><code>2001:db8::</code></td>
<td><code>2001:db8::</code></td>
<td align="right">1</td>
</tr>
<tr>
<td>IPv6 <code>/64</code> range</td>
<td><code>2001:db8::/64</code></td>
<td><code>2001:db8::</code></td>
<td><code>2001:db8:0000:0000:ffff:ffff:ffff:ffff</code></td>
<td align="right">18,446,744,073,709,551,616</td>
</tr>
<tr>
<td>IPv6 <code>/48</code> range</td>
<td><code>2001:db8::/48</code></td>
<td><code>2001:db8::</code></td>
<td><code>2001:db8:0000:ffff:ffff:ffff:ffff:ffff</code></td>
<td align="right">1,208,925,819,614,629,174,706,176</td>
</tr>
<tr>
<td>IPv6 <code>/32</code> range</td>
<td><code>2001:db8::/32</code></td>
<td><code>2001:db8::</code></td>
<td><code>2001:db8:ffff:ffff:ffff:ffff:ffff:ffff</code></td>
<td align="right">79,228,162,514,264,337,593,543,950,336</td>
</tr>
</tbody>
</table>
<h2 id="autonomous-system-number-asn">Autonomous System Number (ASN)</h2>
<table>
<thead>
<tr>
<th>Type</th>
<th>Example value</th>
</tr>
</thead>
<tbody>
<tr>
<td>ASN</td>
<td><code>AS13335</code></td>
</tr>
</tbody>
</table>
<h2 id="country">Country</h2>
<p>Specify a country using two-letter <a href="https://www.iso.org/iso-3166-country-codes.html">ISO-3166-1 alpha-2 codes</a>. Additionally, the Cloudflare dashboard accepts country names. For example:</p>
<ul>
<li><code>US</code></li>
<li><code>CN</code></li>
<li><code>germany</code> (dashboard only)</li>
</ul>
<p>Cloudflare uses the following special country alpha-2 codes that are not part of the ISO:</p>
<ul>
<li><code>T1</code>: <a href="/network/onion-routing/">Tor exit nodes</a> (country name: <code>Tor</code>)</li>
<li><code>XX</code>: Unknown/reserved</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/15726.md")
</aside>
