---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/connection-methods/
  description: Compare Cloudflare Mesh and Tunnel options.
  full_title: Choose a connection method · Cloudflare Learning Paths
  head_html: <title>Choose a connection method · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Compare Cloudflare Mesh and Tunnel options."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/connection-methods/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/connection-methods/index.md"><meta property="og:title" content="Choose a connection method · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Compare Cloudflare Mesh and Tunnel options."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/connection-methods/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare One,Access,Cloudflare Tunnel,Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/connection-methods/#page","headline":"Choose a connection method \u00b7 Cloudflare Learning Paths","description":"Compare Cloudflare Mesh and Tunnel options.","url":"https://developers.cloudflare.com/learning-paths/replace-vpn/connect-private-network/connection-methods/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/replace-vpn/connect-private-network/connection-methods/
  schema: 1
---
<p>There are <a href="/reference-architecture/architectures/sase/#connecting-networks">multiple ways</a> to onramp traffic from your private networks to Cloudflare. This page covers the two software-based methods commonly used for VPN replacement: Cloudflare Mesh and Cloudflare Tunnel. Both involve installing lightweight software on a host machine in your network to create a secure connection to Cloudflare's global network.</p>
<h2 id="cloudflare-mesh">Cloudflare Mesh</h2>
<p><a href="/mesh/">Cloudflare Mesh</a> (formerly WARP Connector) runs the Cloudflare One Client (<code>warp-cli</code>) in headless mode on a Linux server. It operates as a Layer 3 proxy, supports bidirectional traffic (TCP, UDP, ICMP), and assigns a private Mesh IP to every participant. Use Mesh when you need:</p>
<ul>
<li>User-to-network access (replacing a VPN)</li>
<li>Network-to-network / site-to-site connectivity</li>
<li>Server-initiated connections (VoIP, SIP, AD updates, SCCM, DevOps)</li>
<li>Client-to-client connectivity between enrolled devices</li>
</ul>
<h2 id="cloudflare-tunnel">Cloudflare Tunnel</h2>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> runs the <code>cloudflared</code> daemon on a host machine. It creates an outbound-only connection and proxies traffic from Cloudflare to your internal applications or network. Use Tunnel when you need:</p>
<ul>
<li>Publishing specific applications by hostname</li>
<li>Outbound-only connectivity (no inbound ports opened)</li>
<li>Proxying HTTP/S, TCP, or SSH traffic to specific services</li>
<li>Running on non-Linux platforms (macOS, Windows)</li>
</ul>
<h2 id="comparison-table">Comparison table</h2>
<table>
<thead>
<tr>
<th></th>
<th>Cloudflare Mesh</th>
<th>Cloudflare Tunnel</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bidirectional traffic</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>High availability</td>
<td>✅ (active-passive)</td>
<td>✅ (active-active replicas)</td>
</tr>
<tr>
<td>Source IP of request</td>
<td>Virtual IP of requesting device</td>
<td><code>cloudflared</code> host machine</td>
</tr>
<tr>
<td>Host machine</td>
<td>Linux (amd64, arm64)</td>
<td>Linux, macOS, Windows</td>
</tr>
<tr>
<td>IPv4</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>IPv6</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>OSI layer</td>
<td>L3</td>
<td>L7</td>
</tr>
<tr>
<td>Protocol</td>
<td>MASQUE</td>
<td>QUIC or HTTP/2</td>
</tr>
<tr>
<td>Protocols proxied</td>
<td>TCP, UDP, ICMP</td>
<td>HTTP/S, TCP, SSH, RDP, SMB</td>
</tr>
<tr>
<td>Connection handling</td>
<td>End-to-end — preserves long-lived TCP connections across the full path</td>
<td>Proxied — TCP connections are terminated and re-established at Cloudflare, which can interrupt long-lived sessions (for example, SAP transactions, database replication streams, or persistent RDP sessions may drop when <code>cloudflared</code> reconnects)</td>
</tr>
</tbody>
</table>
<h2 id="recommendation">Recommendation</h2>
<p>For most VPN replacement scenarios, <a href="/learning-paths/replace-vpn/connect-private-network/cloudflared/">Cloudflare Tunnel</a> is the easiest way to get started. It runs on all platforms (Linux, macOS, Windows, containers, Raspberry Pi), does not require return route configuration (traffic is source-NATed to the <code>cloudflared</code> host), and does not interfere with existing VPN software on the same machine.</p>
<p>Use <a href="/learning-paths/replace-vpn/connect-private-network/cloudflare-mesh/">Cloudflare Mesh</a> when you need bidirectional connectivity with server-initiated traffic (VoIP, SIP, AD updates, SCCM), site-to-site networking between multiple locations, deployments where preserving the original source IP is important, or workloads with long-lived TCP connections sensitive to interruptions (SAP, database replication, ERP systems).</p>
<p>Both methods can be used together. For example, use Tunnel for straightforward user-to-application access and add Mesh nodes where you need bidirectional or site-to-site connectivity.</p>
