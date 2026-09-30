---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/
  description: Learn how to configure IPsec or GRE tunnels for Cloudflare WAN.
  full_title: Configure tunnel endpoints · Cloudflare WAN docs
  head_html: <title>Configure tunnel endpoints · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to configure IPsec or GRE tunnels for Cloudflare WAN."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/index.md"><meta property="og:title" content="Configure tunnel endpoints · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to configure IPsec or GRE tunnels for Cloudflare WAN."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#page","headline":"Configure tunnel endpoints \u00b7 Cloudflare WAN docs","description":"Learn how to configure IPsec or GRE tunnels for Cloudflare WAN.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/
  schema: 1
---
<p>Cloudflare assigns an IPv4 anycast address to your account for use as the tunnel destination for your network's routers. You can find this address in the Cloudflare dashboard under <strong>Address Space</strong> &gt; <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space"><strong>Leased IPs</strong></a>. To request additional endpoint addresses, contact your account team.</p>
<p>Cloudflare handles failures on its network automatically by advertising your endpoint IP from multiple nodes across many globally distributed data centers. To handle failures on your network, configure two tunnels from separate routers.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Before creating a tunnel, make sure you have the following information:</p>
<ul>
<li><strong>Cloudflare endpoint address</strong>: The anycast IP address assigned to your account. You can find it in the Cloudflare dashboard under <strong>Address Space</strong> &gt; <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space"><strong>Leased IPs</strong></a>.</li>
<li><strong>Customer endpoint IP</strong>: A public Internet routable IP address outside of the prefixes Cloudflare will advertise on your behalf (typically provided by your ISP). Not required if using <a href="/network-interconnect/">Cloudflare Network Interconnect</a> or for <span class="nb-glossary-tooltip" title="IPsec tunnel">IPsec</span> tunnels (unless your router uses an <span class="nb-glossary-tooltip" title="Internet key exchange (IKE)">IKE</span> ID of type <code>ID_IPV4_ADDR</code>).</li>
<li><strong>Interface address</strong>: A <code>/31</code> (recommended) or <code>/30</code> subnet from RFC 1918 private IP space (<code>10.0.0.0/8</code>, <code>172.16.0.0/12</code>, <code>192.168.0.0/16</code>) or <code>169.254.240.0/20</code>(this address space is also a link-local address).</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6882.md")
</aside>
<h2 id="ways-to-onboard-traffic-to-cloudflare">Ways to onboard traffic to Cloudflare</h2>
<h3 id="gre-and-ipsec-tunnels">GRE and IPsec tunnels</h3>
<p>You can use GRE or IPsec tunnels to onboard your traffic to Cloudflare WAN, and set them up through the Cloudflare dashboard or the API. If you use the API, you need your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> and <a href="/fundamentals/api/get-started/keys/#view-your-global-api-key">API key</a>.</p>
<h4 id="choose-between-gre-and-ipsec">Choose between GRE and IPsec</h4>
<table>
<thead>
<tr>
<th>Feature</th>
<th>GRE</th>
<th>IPsec</th>
</tr>
</thead>
<tbody>
<tr>
<td>Encryption</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Authentication</td>
<td>No</td>
<td>Pre-shared key (PSK)</td>
</tr>
<tr>
<td>Setup complexity</td>
<td>Simpler</td>
<td>Requires PSK exchange</td>
</tr>
<tr>
<td>Best for</td>
<td>Trusted networks, CNI connections</td>
<td>Internet-facing connections requiring encryption</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/">Tunnels and encapsulation</a> to learn more about the technical requirements for both tunnel types.</p>
<h4 id="ipsec-supported-ciphers">IPsec supported ciphers</h4>
<p>Refer to <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/#supported-configuration-parameters">supported ciphers for IPsec</a> for a complete list. IPsec tunnels only support Internet Key Exchange version 2 (IKEv2).</p>
<h4 id="anti-replay-protection">Anti-replay protection</h4>
<p>If you use Cloudflare WAN and <span class="nb-glossary-tooltip" title="anycast">anycast</span> IPsec tunnels, we recommend disabling anti-replay protection. Cloudflare disables this setting by default. However, you can enable it through the API or the Cloudflare dashboard for devices that do not support disabling it, including Cisco Meraki, Velocloud, and AWS VPN Gateway.</p>
<p>Refer to <a href="/cloudflare-wan/reference/anti-replay-protection/">Anti-replay protection</a> for more information on this topic, or <a href="#add-ipsec-tunnel">Add IPsec tunnels</a> to learn how to enable this feature.</p>
<h3 id="network-interconnect-cni">Network Interconnect (CNI)</h3>
<p>Beyond GRE and IPsec tunnels, you can also use Network Interconnect (CNI) to onboard your traffic to Cloudflare WAN. Refer to <a href="/cloudflare-wan/network-interconnect/">Network Interconnect (CNI)</a> for more information.</p>
<h2 id="add-tunnels">Add tunnels</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6881.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6895.md")
</div></div>
<h2 id="bidirectional-vs-unidirectional-health-checks">Bidirectional vs unidirectional health checks</h2>
<p>To check for tunnel health, Cloudflare sends a <a href="/cloudflare-wan/reference/tunnel-health-checks/">health check probe</a> consisting of ICMP (Internet Control Message Protocol) reply <a href="https://www.cloudflare.com/learning/network-layer/what-is-a-packet/">packets</a> to your network. Cloudflare needs to receive these probes to know if your tunnel is healthy.</p>
<p>Cloudflare defaults to bidirectional health checks for Cloudflare WAN, and unidirectional health checks for Magic Transit (direct server return). However, routing unidirectional ICMP reply packets over the Internet to Cloudflare is sometimes subject to drops by intermediate network devices, such as stateful firewalls. Magic Transit customers with egress traffic can modify this setting to bidirectional.</p>
<h3 id="legacy-bidirectional-health-checks">Legacy bidirectional health checks</h3>
<p>For customers using the legacy health check system with a public IP range, Cloudflare recommends:</p>
<ul>
<li>Configuring the tunnel health check target IP address to one within the <code>172.64.240.252/30</code> prefix range.</li>
<li>Applying a policy-based route that matches <a href="https://www.cloudflare.com/learning/network-layer/what-is-a-packet/">packets</a> with a source IP address equal to the configured tunnel health check target (for example <code>172.64.240.253/32</code>), and route them over the tunnel back to Cloudflare.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<p>Now that you have set up your tunnel endpoints, you need to configure routes to direct your traffic through Cloudflare. You have two routing options:</p>
<ul>
<li><strong>Static routes</strong>: Best for simple, stable networks where routes rarely change. You manually define each route.</li>
<li><strong>BGP peering</strong>: Best for dynamic environments with frequently changing routes, multiple prefixes, or when you need automatic failover. Requires enabling BGP on your tunnel during creation.</li>
</ul>
<p>Refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/">Configure routes</a> for detailed instructions on both options.</p>
<p>After configuring your routes, you need to <a href="/cloudflare-wan/configuration/common-settings/sites/">set up a site</a>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you experience issues with your tunnels:</p>
<ul>
<li>For tunnel health check problems, refer to <a href="/cloudflare-wan/troubleshooting/tunnel-health/">Troubleshoot tunnel health</a>.</li>
<li>For IPsec tunnel establishment issues, refer to <a href="/cloudflare-wan/troubleshooting/ipsec-troubleshoot/">Troubleshoot with IPsec logs</a>.</li>
</ul>
