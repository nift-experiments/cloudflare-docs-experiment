---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/zone-transfers/
  description: Transfer DNS zones between Cloudflare and other providers.
  full_title: DNS Zone transfers · Cloudflare DNS docs
  head_html: <title>DNS Zone transfers · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Transfer DNS zones between Cloudflare and other providers."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/zone-transfers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/zone-transfers/index.md"><meta property="og:title" content="DNS Zone transfers · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Transfer DNS zones between Cloudflare and other providers."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/zone-transfers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/zone-transfers/#page","headline":"DNS Zone transfers \u00b7 Cloudflare DNS docs","description":"Transfer DNS zones between Cloudflare and other providers.","url":"https://developers.cloudflare.com/dns/zone-setups/zone-transfers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/zone-transfers/
  schema: 1
---
<p>Zone transfers allow you to use multiple DNS providers for the same domain to increase availability and fault tolerance. If one provider has an outage, the other can still answer DNS queries, keeping your domain available.</p>
<p>With zone transfers, your providers synchronize DNS records between themselves using one of two protocols:</p>
<ul>
<li><strong>Authoritative zone transfer (<a href="https://www.rfc-editor.org/rfc/rfc5936.html">AXFR</a>)</strong>: Copies the entire zone from the primary to the secondary provider, even if only one record changes.</li>
<li><strong>Incremental zone transfer (<a href="https://www.rfc-editor.org/rfc/rfc1995.html">IXFR</a>)</strong>: Transfers only the changes since the last transfer, rather than the entire zone.</li>
</ul>
<p>Cloudflare supports both protocols.</p>
<p>You have two configuration options for zone transfers:</p>
<ul>
<li><a href="/dns/zone-setups/zone-transfers/cloudflare-as-primary/">Cloudflare as Primary</a>: Cloudflare is your primary DNS provider and performs outgoing zone transfers to your secondary DNS provider(s).</li>
<li><a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Cloudflare as Secondary</a>: Cloudflare is your secondary DNS provider and initiates incoming zone transfers from your primary DNS provider.</li>
</ul>
<h2 id="peer-dns-server">Peer DNS server</h2>
<p>A peer DNS server is the external DNS provider that participates in zone transfers with Cloudflare. The same peer can be linked to multiple primary and secondary zones. Each peer can be associated with only one Transaction Signature (TSIG) — an authentication mechanism that uses a shared secret to verify zone transfer messages between providers.</p>
<p>The maximum number of linked peers per zone is 30.</p>
<p>You can manage peers via the <a href="/api/resources/dns/subresources/zone_transfers/subresources/peers/methods/list/">API</a> or the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the account <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Refer to <strong>DNS Settings</strong> &gt; <strong>DNS Zone Transfers</strong>.</li>
</ol>
<p>The fields below configure how Cloudflare communicates with the peer. When Cloudflare is primary, it sends NOTIFY messages to alert the peer that zone data has changed. When Cloudflare is secondary, it sends AXFR/IXFR requests to retrieve updated records from the peer.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Cloudflare as Primary (Outgoing)</th>
<th>Cloudflare as Secondary (Incoming)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Name</td>
<td>Human readable name of peer</td>
<td>Human readable name of peer</td>
</tr>
<tr>
<td>IP</td>
<td>If configured, where Cloudflare sends the NOTIFY to</td>
<td>Where Cloudflare sends the AXFR/IXFR transfer request to</td>
</tr>
<tr>
<td>Port</td>
<td>IP Port for NOTIFY IP</td>
<td>IP Port for transfer IP</td>
</tr>
<tr>
<td>TSIG ID</td>
<td>Attached TSIG object</td>
<td>Attached TSIG object</td>
</tr>
<tr>
<td>IXFR enabled</td>
<td>Cloudflare always supports IXFR for outgoing zone transfers</td>
<td>Specifies if Cloudflare only sends AXFR or AXFR and IXFR</td>
</tr>
</tbody>
</table>
<h2 id="availability">Availability</h2>
<p>Zone transfers are only available to customers on an Enterprise plan.</p>
