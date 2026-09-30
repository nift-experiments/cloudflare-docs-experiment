---
cp9:
  canonical: https://developers.cloudflare.com/dns/private-origins/private-network-routing/
  description: Route DNS record traffic to private origins through tunnels.
  full_title: Private network routing · Cloudflare DNS docs
  head_html: <title>Private network routing · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Route DNS record traffic to private origins through tunnels."><link rel="canonical" href="https://developers.cloudflare.com/dns/private-origins/private-network-routing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/private-origins/private-network-routing/index.md"><meta property="og:title" content="Private network routing · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route DNS record traffic to private origins through tunnels."><meta property="og:url" content="https://developers.cloudflare.com/dns/private-origins/private-network-routing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/private-origins/private-network-routing/#page","headline":"Private network routing \u00b7 Cloudflare DNS docs","description":"Route DNS record traffic to private origins through tunnels.","url":"https://developers.cloudflare.com/dns/private-origins/private-network-routing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /dns/private-origins/private-network-routing/
  schema: 1
---
<p>Private network routing allows you to proxy HTTP/HTTPS traffic from public hostnames to origins in your private network. When you enable this setting on a DNS record, Cloudflare routes traffic through your configured tunnel instead of over the public Internet.</p>
<p>For an end-to-end setup walkthrough using Cloudflare WAN (formerly Magic WAN) IPsec, refer to <a href="/dns/private-origins/set-up-via-cloudflare-wan/">Set up a private origin via Cloudflare WAN</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="closed-beta">Closed beta</h3>
@markup("md", "content/.markup/bodies/7599.md")
</aside>
<h2 id="aspects-to-consider">Aspects to consider</h2>
<p>Before you enable private network routing, consider the following:</p>
<ul>
<li>You need an active tunnel connection to Cloudflare through one of the supported on-ramp methods. Refer to <a href="/cloudflare-wan/on-ramps/">Cloudflare WAN</a> for further guidance.</li>
<li>Private network routing is available for <code>A</code> (IPv4) and <code>AAAA</code> (IPv6) records only. Records must be <a href="/dns/proxy-status/">proxied</a>.</li>
<li>If you have multiple <code>A</code> or <code>AAAA</code> records on the same name, and at least one of them has private network routing enabled, all records on that name will use private network routing. This is consistent with the <a href="/dns/proxy-status/#mix-proxied-and-unproxied">proxy status behavior</a> in these cases.</li>
</ul>
<h2 id="ip-ranges">IP ranges</h2>
<p>The following private address ranges are automatically detected:</p>
<table>
<thead>
<tr>
<th>Range</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>10.0.0.0/8</code></td>
<td>Private (<a href="https://www.rfc-editor.org/rfc/rfc1918.html">RFC 1918</a>)</td>
</tr>
<tr>
<td><code>172.16.0.0/12</code></td>
<td>Private (<a href="https://www.rfc-editor.org/rfc/rfc1918.html">RFC 1918</a>)</td>
</tr>
<tr>
<td><code>192.168.0.0/16</code></td>
<td>Private (<a href="https://www.rfc-editor.org/rfc/rfc1918.html">RFC 1918</a>)</td>
</tr>
<tr>
<td><code>fc00::/7</code></td>
<td>Private (<a href="https://www.rfc-editor.org/rfc/rfc4193.html">RFC 4193</a>)</td>
</tr>
<tr>
<td><code>100.64.0.0/10</code></td>
<td>CGNAT (<a href="https://www.rfc-editor.org/rfc/rfc6598.html">RFC 6598</a>)</td>
</tr>
</tbody>
</table>
<p>When you use an IP address from one of these ranges, the <strong>Use private network routing</strong> toggle turns on automatically. You can also turn it on manually for public IP addresses that are only reachable through your tunnel.</p>
<h2 id="enable-private-network-routing">Enable private network routing</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="virtual-networks">Virtual networks</h3>
@markup("md", "content/.markup/bodies/7598.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7602.md")
</div></div>
<h3 id="api-field-behavior">API field behavior</h3>
<p>If you use the API to create or edit DNS records with private network routing, consider the following:</p>
<table>
<thead>
<tr>
<th>Scenario</th>
<th><code>private_routing</code> value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Proxied <code>A</code>/<code>AAAA</code> record with private IP</td>
<td>Auto-set to <code>true</code></td>
</tr>
<tr>
<td>Proxied <code>A</code>/<code>AAAA</code> record with public IP</td>
<td>Defaults to <code>false</code></td>
</tr>
<tr>
<td>Non-<code>A</code>/<code>AAAA</code> record types</td>
<td>Field not supported</td>
</tr>
</tbody>
</table>
<p>Also, if you manually set <code>private_routing: false</code> on a proxied <code>A</code>/<code>AAAA</code> record with private IP, the API will return an error.</p>
