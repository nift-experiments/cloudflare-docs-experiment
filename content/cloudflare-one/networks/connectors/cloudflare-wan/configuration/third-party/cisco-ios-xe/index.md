---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-ios-xe/
  description: Integrate Cisco IOS XE with Zero Trust networking.
  full_title: Cisco IOS XE · Cloudflare One docs
  head_html: <title>Cisco IOS XE · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Cisco IOS XE with Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-ios-xe/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-ios-xe/index.md"><meta property="og:title" content="Cisco IOS XE · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Cisco IOS XE with Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-ios-xe/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="IPsec"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-ios-xe/#page","headline":"Cisco IOS XE \u00b7 Cloudflare One docs","description":"Integrate Cisco IOS XE with Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-ios-xe/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["IPsec"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-ios-xe/
  schema: 1
---
<p>This tutorial provides a comprehensive configuration example for establishing a secure Internet Protocol Security (IPsec) tunnel between Cisco IOS XE and Cloudflare using Post-Quantum Cryptography (PQC).</p>
<p>Interconnecting your Cisco IOS XE infrastructure with Cloudflare Anycast IPsec tunnels delivers a highly resilient connectivity solution with two primary benefits:</p>
<ol>
<li><strong>Post-Quantum Encryption:</strong> Your connection is protected by ML-KEM post-quantum encryption, protecting data in transit against harvest-now, decrypt-later attacks, to provide long-term confidentiality against emerging quantum-computing threats.</li>
<li><strong>Anycast-Powered Resilience &amp; Global Reach:</strong> Cloudflare's distributed Anycast IP network simplifies your architecture by allowing you to interconnect routers that are not physically co-located or directly linked. Traffic is automatically routed to the nearest optimal Cloudflare data center, providing built-in active/active path redundancy, automated failover, and high availability.</li>
</ol>
<p>This guide covers everything required to deploy this architecture, including Virtual Tunnel Interfaces (VTIs), IKEv2 profiles utilizing quantum-safe parameters, and diagnostic validation.</p>
<h2 id="test-environment">Test environment</h2>
<table>
<thead>
<tr>
<th><strong>Field</strong></th>
<th><strong>Value</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Vendor</td>
<td>Cisco</td>
</tr>
<tr>
<td>Model</td>
<td>Cisco Series 8000 Router</td>
</tr>
<tr>
<td>Release</td>
<td>IOS-XE 26.1.1</td>
</tr>
<tr>
<td>Date tested</td>
<td>May 2026</td>
</tr>
</tbody>
</table>
<h2 id="ike-ipsec-crypto-and-relevant-settings">IKE/IPsec crypto and relevant settings</h2>
<table>
<thead>
<tr>
<th><strong>Field</strong></th>
<th><strong>Value</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Traffic Selection Criteria</td>
<td>Route-Based VPN</td>
</tr>
<tr>
<td>Routing</td>
<td>Static</td>
</tr>
<tr>
<td>Redundant Tunnels</td>
<td>Yes</td>
</tr>
<tr>
<td>Tunnel Load Balancing</td>
<td>Active/Active</td>
</tr>
<tr>
<td>IKE Version</td>
<td>IKEv2</td>
</tr>
<tr>
<td>Authentication</td>
<td>Pre-Shared Key</td>
</tr>
<tr>
<td>Anti-Replay Protection</td>
<td>Disabled</td>
</tr>
<tr>
<td>NAT Traversal (NAT-T)</td>
<td>Validated</td>
</tr>
<tr>
<td>NAT-T Port</td>
<td>4500/udp</td>
</tr>
<tr>
<td>Phase 1 - DH-Group</td>
<td>Group 20</td>
</tr>
<tr>
<td>Phase 1 - Encryption</td>
<td>AES-256-CBC</td>
</tr>
<tr>
<td>Phase 1 - Authentication/Integrity</td>
<td>SHA-256</td>
</tr>
<tr>
<td>Phase 2 - DH-Group</td>
<td>Group 20</td>
</tr>
<tr>
<td>Phase 2 - Transport</td>
<td>ESP</td>
</tr>
<tr>
<td>Phase 2 - Encryption</td>
<td>AES-256-CBC</td>
</tr>
<tr>
<td>Post-Quantum Cryptography</td>
<td>ML-KEM 768</td>
</tr>
</tbody>
</table>
<h2 id="supported-platforms">Supported platforms</h2>
<p>Support for ML-KEM is available on <a href="https://www.cisco.com/site/us/en/products/networking/sdwan-routers/8000-secure-routers/index.html">Cisco 8000 Series Secure Routers</a>.</p>
<h2 id="cloudflare-wan-and-cisco-ios-xe-configuration-settings">Cloudflare WAN and Cisco IOS XE configuration settings</h2>
<p>While following these steps, ensure you update any object names and IP addresses to match your environment. Aligning these elements with your actual naming conventions and network scheme ensures the configuration integrates seamlessly with your production setup. Use <strong>Find &amp; Replace</strong> on the examples below to update names and addresses, maintaining consistency throughout.</p>
<h3 id="cloudflare-wan-tunnel-01-of-02">Cloudflare WAN - Tunnel 01 of 02</h3>
<table>
<thead>
<tr>
<th><strong>Attribute</strong></th>
<th><strong>Value/Address</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Name (required)</td>
<td><code>CF_WAN_TUN_01</code></td>
</tr>
<tr>
<td>Description</td>
<td>---</td>
</tr>
<tr>
<td>IPv4 Interface Address (required)</td>
<td><code>169.254.250.0/31</code></td>
</tr>
<tr>
<td>IPv6 Interface Address</td>
<td>---</td>
</tr>
<tr>
<td>Customer Endpoint</td>
<td><code>203.0.113.100</code></td>
</tr>
<tr>
<td>Cloudflare Endpoint</td>
<td><code>162.159.135.1</code></td>
</tr>
<tr>
<td>Tunnel health checks</td>
<td>True</td>
</tr>
<tr>
<td>Rate</td>
<td>Medium</td>
</tr>
<tr>
<td><strong>Type</strong></td>
<td><strong>Request</strong></td>
</tr>
<tr>
<td><strong>Direction</strong></td>
<td><strong>Bidirectional</strong></td>
</tr>
<tr>
<td>Target</td>
<td>Default</td>
</tr>
<tr>
<td>Turn on replay protection</td>
<td>False</td>
</tr>
<tr>
<td><strong>Automatic return routing</strong></td>
<td><strong>True</strong></td>
</tr>
</tbody>
</table>
<p>IKE Identity and Pre-shared Key (obtained after tunnel creation):</p>
<table>
<thead>
<tr>
<th><strong>Attribute</strong></th>
<th><strong>Value/Address</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>FQDN ID</td>
<td><code>bf6c493d03REDACTED.ipsec.cloudflare.com</code></td>
</tr>
<tr>
<td>Pre-shared key</td>
<td><code>Cloudflare-WAN-T1-PSK-1234!</code></td>
</tr>
</tbody>
</table>
<h3 id="cloudflare-wan-tunnel-02-of-02">Cloudflare WAN - Tunnel 02 of 02</h3>
<table>
<thead>
<tr>
<th><strong>Attribute</strong></th>
<th><strong>Value/Address</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Name (required)</td>
<td><code>CF_WAN_TUN_02</code></td>
</tr>
<tr>
<td>Description</td>
<td>---</td>
</tr>
<tr>
<td>IPv4 Interface Address (required)</td>
<td><code>169.254.250.2/31</code></td>
</tr>
<tr>
<td>IPv6 Interface Address</td>
<td>---</td>
</tr>
<tr>
<td>Customer Endpoint</td>
<td><code>203.0.113.100</code></td>
</tr>
<tr>
<td>Cloudflare Endpoint</td>
<td><code>172.64.135.1</code></td>
</tr>
<tr>
<td>Tunnel health checks</td>
<td>True</td>
</tr>
<tr>
<td>Rate</td>
<td>Medium</td>
</tr>
<tr>
<td><strong>Type</strong></td>
<td><strong>Request</strong></td>
</tr>
<tr>
<td><strong>Direction</strong></td>
<td><strong>Bidirectional</strong></td>
</tr>
<tr>
<td>Target</td>
<td>Default</td>
</tr>
<tr>
<td>Turn on replay protection</td>
<td>False</td>
</tr>
<tr>
<td><strong>Automatic return routing</strong></td>
<td><strong>True</strong></td>
</tr>
</tbody>
</table>
<p>IKE Identity and Pre-shared Key (obtained after tunnel creation):</p>
<table>
<thead>
<tr>
<th><strong>Attribute</strong></th>
<th><strong>Value/Address</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>FQDN ID</td>
<td><code>0287844e9dREDACTED.ipsec.cloudflare.com</code></td>
</tr>
<tr>
<td>Pre-shared key</td>
<td><code>Cloudflare-WAN-T2-PSK-1234!</code></td>
</tr>
</tbody>
</table>
<h2 id="customer-premise-equipment-cisco-ios-xe">Customer premise equipment - Cisco IOS XE</h2>
<table>
<thead>
<tr>
<th><strong>WAN Interface</strong></th>
<th><strong>Tunnel 01 of 02</strong></th>
<th><strong>Tunnel 02 of 02</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>WAN Interface</td>
<td><code>GigabitEthernet2</code></td>
<td><code>GigabitEthernet2</code></td>
</tr>
<tr>
<td>IP Address</td>
<td><code>203.0.113.100/24</code></td>
<td><code>203.0.113.100/24</code></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th><strong>Virtual Tunnel Interface (VTI)</strong></th>
<th><strong>Tunnel 01 of 02</strong></th>
<th><strong>Tunnel 02 of 02</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Tunnel interface</td>
<td><code>Tunnel01</code></td>
<td><code>Tunnel02</code></td>
</tr>
<tr>
<td>IP Address</td>
<td><code>169.254.250.1/31</code></td>
<td><code>169.254.250.3/31</code></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th><strong>LAN Interface</strong></th>
<th><strong>Tunnel 01 of 02</strong></th>
<th><strong>Tunnel 02 of 02</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>LAN Interface</td>
<td><code>ge-0/0/1.0</code></td>
<td><code>ge-0/0/1.0</code></td>
</tr>
<tr>
<td>IP Address</td>
<td><code>192.168.125.1/24</code></td>
<td><code>192.168.125.1/24</code></td>
</tr>
<tr>
<td>Security Zone</td>
<td>trust</td>
<td>trust</td>
</tr>
</tbody>
</table>
<h2 id="configuration">Configuration</h2>
<p>The process to establish IPsec tunnels on Cisco IOS XE involves the following steps:</p>
<ul>
<li>Virtual Tunnel Interfaces (one per tunnel)</li>
<li>IKEv2 Proposal</li>
<li>IKEv2 Policy</li>
<li>IKEv2 Keyring (one per tunnel)</li>
<li>IKEv2 Profile (one per tunnel)</li>
<li>IKEv2 Profile with NAT-T Support (optional)</li>
<li>IPsec Profile (one per tunnel)</li>
<li>Bind IPsec Profiles to Virtual Tunnel Interfaces</li>
<li>Policy-Based Routing (recommended)</li>
<li>Health Tracking - IP SLA (recommended)</li>
</ul>
<h3 id="virtual-tunnel-interfaces">Virtual tunnel interfaces</h3>
<p>Add one Virtual Tunnel Interface per IPsec tunnel to facilitate routing to Cloudflare.</p>
<h4 id="tunnel1">Tunnel1</h4>
<pre tabindex="0"><code class="language-txt">interface Tunnel1&#10; ip address 169.254.250.1 255.255.255.254&#10; ip proxy-arp&#10; ip mtu 1450&#10; ip tcp adjust-mss 1350&#10; tunnel source 203.0.113.100&#10; tunnel mode ipsec ipv4&#10; tunnel destination 162.159.135.1&#10; tunnel path-mtu-discovery&#10;</code></pre>
<h4 id="tunnel2">Tunnel2</h4>
<pre tabindex="0"><code class="language-txt">interface Tunnel2&#10; ip address 169.254.250.3 255.255.255.254&#10; ip proxy-arp&#10; ip mtu 1450&#10; ip tcp adjust-mss 1350&#10; tunnel source 203.0.113.100&#10; tunnel mode ipsec ipv4&#10; tunnel destination 172.64.135.1&#10; tunnel path-mtu-discovery&#10;</code></pre>
<h3 id="ike-phase-1">IKE - Phase 1</h3>
<p>Configure the following to facilitate IKEv2 Phase 1 negotiation:</p>
<ul>
<li>IKEv2 Proposal</li>
<li>IKEv2 Policy</li>
<li>IKEv2 Keyring (one required per Cloudflare WAN IPsec tunnel)</li>
<li>IKEv2 Profile (one required per Cloudflare WAN IPsec tunnel)</li>
</ul>
<h4 id="ikev2-proposal">IKEv2 Proposal</h4>
<p>Define an IKEv2 Proposal as follows:</p>
<pre tabindex="0"><code class="language-txt">crypto ikev2 proposal CF_WAN_IKEV2_PROP&#10; pqc mlkem768&#10; encryption aes-cbc-256&#10; prf sha512 sha384 sha256&#10; group 20&#10; exit&#10;</code></pre>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/5634.md")
</aside>
<h4 id="ikev2-policy">IKEv2 Policy</h4>
<p>Configure one IKEv2 Policy per tunnel:</p>
<pre tabindex="0"><code class="language-txt">crypto ikev2 policy CF_WAN_IKEV2_POL&#10; match fvrf any&#10; proposal CF_WAN_IKEV2_PROP&#10; exit&#10;</code></pre>
<h4 id="ikev2-keyrings">IKEv2 Keyrings</h4>
<p>Add one keyring per tunnel:</p>
<h5 id="cf-wan-tun-01-ikev2-peer"><code>CF_WAN_TUN_01_IKEV2_PEER</code></h5>
<pre tabindex="0"><code class="language-txt">crypto ikev2 keyring CF_WAN_TUN_01_IKEV2_KEYRING&#10; peer CF_WAN_TUN_01_IKEV2_PEER&#10;  address 162.159.135.1&#10;  pre-shared-key 0 Cloudflare-WAN-T1-PSK-1234!&#10;exit&#10;</code></pre>
<h5 id="cf-wan-tun-02-ikev2-peer"><code>CF_WAN_TUN_02_IKEV2_PEER</code></h5>
<pre tabindex="0"><code class="language-txt">crypto ikev2 keyring CF_WAN_TUN_02_IKEV2_KEYRING&#10; peer CF_WAN_TUN_02_IKEV2_PEER&#10;  address 172.64.135.1&#10;  pre-shared-key 0 Cloudflare-WAN-T2-PSK-1234!&#10;exit&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5633.md")
</aside>
<h4 id="ikev2-profiles">IKEv2 Profiles</h4>
<p>Configure one IKEv2 Profile per tunnel:</p>
<h5 id="cf-wan-tun-01-ikev2-prof"><code>CF_WAN_TUN_01_IKEV2_PROF</code></h5>
<pre tabindex="0"><code class="language-txt">crypto ikev2 profile CF_WAN_TUN_01_IKEV2_PROF&#10; match identity remote address 162.159.135.1 255.255.255.255&#10; identity local fqdn bf6c493d03REDACTED.ipsec.cloudflare.com&#10; authentication remote pre-share&#10; authentication local pre-share&#10; keyring local CF_WAN_TUN_01_IKEV2_KEYRING&#10; no config-exchange request&#10; exit&#10;</code></pre>
<h5 id="cf-wan-tun-02-ikev2-prof"><code>CF_WAN_TUN_02_IKEV2_PROF</code></h5>
<pre tabindex="0"><code class="language-txt">crypto ikev2 profile CF_WAN_TUN_02_IKEV2_PROF&#10; match identity remote address 172.64.135.1 255.255.255.255&#10; identity local fqdn 0287844e9dREDACTED.ipsec.cloudflare.com&#10; authentication remote pre-share&#10; authentication local pre-share&#10; keyring local CF_WAN_TUN_02_IKEV2_KEYRING&#10; no config-exchange request&#10; exit&#10;</code></pre>
<h4 id="ikev2-profiles-with-nat-t-support-optional">IKEv2 Profiles with NAT-T support (optional)</h4>
<p>If the WAN interface on the Cisco IOS XE device is behind a device performing Network Address Translation (NAT), you can add <code>nat force-encap</code> under <code>crypto ikev2 profile</code> to force IKE Phase 1 to use UDP port <code>4500</code>.</p>
<p>This is only needed when you want to force encapsulation instead of using the standard NAT-T flow, which starts on UDP port <code>500</code> and switches to UDP port <code>4500</code> after NAT is detected.</p>
<h5 id="cf-wan-tun-01-ikev2-prof-with-nat-t"><code>CF_WAN_TUN_01_IKEV2_PROF</code> with NAT-T</h5>
<pre tabindex="0"><code class="language-txt">crypto ikev2 profile CF_WAN_TUN_01_IKEV2_PROF&#10; match identity remote address 162.159.135.1 255.255.255.255&#10; identity local fqdn bf6c493d03REDACTED.ipsec.cloudflare.com&#10; authentication remote pre-share&#10; authentication local pre-share&#10; keyring local CF_WAN_TUN_01_IKEV2_KEYRING&#10; no config-exchange request&#10; nat force-encap&#10; exit&#10;</code></pre>
<h5 id="cf-wan-tun-02-ikev2-prof-with-nat-t"><code>CF_WAN_TUN_02_IKEV2_PROF</code> with NAT-T</h5>
<pre tabindex="0"><code class="language-txt">crypto ikev2 profile CF_WAN_TUN_02_IKEV2_PROF&#10; match identity remote address 172.64.135.1 255.255.255.255&#10; identity local fqdn 0287844e9dREDACTED.ipsec.cloudflare.com&#10; authentication remote pre-share&#10; authentication local pre-share&#10; keyring local CF_WAN_TUN_02_IKEV2_KEYRING&#10; no config-exchange request&#10; nat force-encap&#10; exit&#10;</code></pre>
<h3 id="ipsec-phase-2">IPsec - Phase 2</h3>
<h4 id="ipsec-profile">IPsec Profile</h4>
<p>Add one IPsec Profile per tunnel:</p>
<h5 id="cf-wan-tun-01-ipsec-prof"><code>CF_WAN_TUN_01_IPSEC_PROF</code></h5>
<pre tabindex="0"><code class="language-txt">crypto ipsec profile CF_WAN_TUN_01_IPSEC_PROF&#10; set security-association lifetime kilobytes disable&#10; set security-association replay disable&#10; set pfs group20&#10; set ikev2-profile CF_WAN_TUN_01_IKEV2_PROF&#10; exit&#10;</code></pre>
<h5 id="cf-wan-tun-02-ipsec-prof"><code>CF_WAN_TUN_02_IPSEC_PROF</code></h5>
<pre tabindex="0"><code class="language-txt">crypto ipsec profile CF_WAN_TUN_02_IPSEC_PROF&#10; set security-association lifetime kilobytes disable&#10; set security-association replay disable&#10; set pfs group20&#10; set ikev2-profile CF_WAN_TUN_02_IKEV2_PROF&#10; exit&#10;</code></pre>
<h3 id="bind-ipsec-profiles-to-tunnel-interfaces">Bind IPsec profiles to tunnel interfaces</h3>
<p>Bind the IPsec profiles to the corresponding Virtual Tunnel Interfaces to instantiate the IPsec tunnels:</p>
<h4 id="tunnel1-1">Tunnel1</h4>
<pre tabindex="0"><code class="language-txt">interface Tunnel1&#10; tunnel protection ipsec profile CF_WAN_TUN_01_IPSEC_PROF&#10; exit&#10;</code></pre>
<h4 id="tunnel2-1">Tunnel2</h4>
<pre tabindex="0"><code class="language-txt">interface Tunnel2&#10; tunnel protection ipsec profile CF_WAN_TUN_02_IPSEC_PROF&#10; exit&#10;</code></pre>
<h3 id="policy-based-routing">Policy-Based Routing</h3>
<p>Use this section when the router must keep its existing default route in the global routing table — for example, to preserve IPsec underlay reachability or support other non-LAN traffic. This approach lets you direct only a specific source subnet across both Cloudflare WAN tunnels while keeping the global default route unchanged.</p>
<p>If your deployment can use Cloudflare as the global default route, you can use a simpler design with two equal-cost static default routes in the global table. In that case, this section is not required.</p>
<p>In this example, the router already uses a global-table default route for IPsec underlay reachability and other non-LAN traffic. To send only traffic sourced from <code>192.168.125.0/24</code> across <code>Tunnel1</code> and <code>Tunnel2</code>, configure Policy-Based Routing (PBR) to match that source subnet and forward the matched traffic into a dedicated VRF. Inside that VRF, configure two equal-cost static default routes — one through each tunnel. CEF then performs per-flow load sharing across both tunnels.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5632.md")
</aside>
<h4 id="create-vrf-as-local-pbr-forwarding-target">Create VRF as local PBR forwarding target</h4>
<pre tabindex="0"><code class="language-txt">ip vrf CF_WAN_PBR_VRF&#10;exit&#10;</code></pre>
<h4 id="define-equal-cost-static-default-routes">Define equal-cost static default routes</h4>
<pre tabindex="0"><code class="language-txt">ip route vrf CF_WAN_PBR_VRF 0.0.0.0 0.0.0.0 169.254.250.0 global track 1&#10;ip route vrf CF_WAN_PBR_VRF 0.0.0.0 0.0.0.0 169.254.250.2 global track 2&#10;</code></pre>
<h4 id="match-traffic-to-steer-to-cloudflare">Match traffic to steer to Cloudflare</h4>
<pre tabindex="0"><code class="language-txt">ip access-list extended CF_WAN_PBR_ALL&#10; permit ip 192.168.125.0 0.0.0.255 any&#10;</code></pre>
<h4 id="define-route-map-to-associate-matched-traffic-to-pbr-vrf">Define route map to associate matched traffic to PBR VRF</h4>
<pre tabindex="0"><code class="language-txt">route-map CF_WAN_PBR_RM permit 10&#10; match ip address CF_WAN_PBR_ALL&#10; set vrf CF_WAN_PBR_VRF&#10; exit&#10;</code></pre>
<h4 id="apply-route-map-to-lan-interface">Apply route map to LAN interface</h4>
<p>Assuming the IP address assigned to the LAN interface is <code>192.168.125.1/24</code>:</p>
<pre tabindex="0"><code class="language-txt">interface GigabitEthernet1&#10; description LAN interface&#10; ip address 192.168.125.1 255.255.255.0&#10; ip policy route-map CF_WAN_PBR_RM&#10;</code></pre>
<h4 id="configure-cisco-express-forwarding-cef-for-load-sharing-universal-algorithm">Configure Cisco Express Forwarding (CEF) for load sharing (universal algorithm)</h4>
<p>Set the load-sharing algorithm to universal:</p>
<pre tabindex="0"><code class="language-txt">ip cef load-sharing algorithm universal&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5631.md")
</aside>
<h3 id="health-tracking-ip-sla-recommended">Health Tracking - IP SLA (recommended)</h3>
<p>The PBR and VRF-based ECMP design described above installs both static default routes in <code>CF_WAN_PBR_VRF</code> as long as line protocol is <code>up</code> on the corresponding tunnel interfaces.</p>
<p>On Cisco IOS XE, a Virtual Tunnel Interface (VTI) remains <code>up/up</code> based on its tunnel source and destination configuration, not on the state of the underlying IKE/IPsec security associations. As a result, a tunnel can appear available to the routing table even when its IKE/IPsec SAs have failed. In this condition, CEF can continue to hash traffic toward the failed tunnel, which can silently drop a portion of flows.</p>
<p>To prevent this, configure an IP SLA <code>icmp-echo</code> probe for each tunnel, using the local VTI address as the source and the remote tunnel IP address as the destination. If a probe stops receiving responses, its associated <code>track</code> object changes to <code>down</code>, and the corresponding static route is removed from the VRF forwarding table.</p>
<p>CEF then removes that path from the ECMP set, and all matched traffic shifts to the remaining healthy tunnel. When the failed tunnel recovers, the probe succeeds, the <code>track</code> object returns to <code>up</code>, the route is reinstalled, and traffic is automatically balanced across both tunnels again.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5630.md")
</aside>
<h4 id="define-ip-sla-probes">Define IP SLA probes</h4>
<p>Instantiate an IP SLA probe (type <code>icmp-echo</code>) with <code>Tunnel1</code> source IP <code>169.254.250.1</code> and destination IP <code>169.254.250.0</code> - send a probe every five seconds:</p>
<pre tabindex="0"><code class="language-txt">ip sla 1&#10; icmp-echo 169.254.250.0 source-interface Tunnel1&#10; frequency 5&#10;ip sla schedule 1 life forever start-time now&#10;</code></pre>
<p>Instantiate an IP SLA probe (type <code>icmp-echo</code>) with <code>Tunnel2</code> source IP <code>169.254.250.3</code> and destination IP <code>169.254.250.2</code> - send a probe every five seconds:</p>
<pre tabindex="0"><code class="language-txt">ip sla 2&#10; icmp-echo 169.254.250.2 source-interface Tunnel2&#10; frequency 5&#10;ip sla schedule 2 life forever start-time now&#10;</code></pre>
<h4 id="define-track-objects">Define track objects</h4>
<p>The following <code>track</code> objects dampen short-lived packet loss to avoid route flaps on transient events:</p>
<pre tabindex="0"><code class="language-txt">track 1 ip sla 1 reachability&#10; delay down 3 up 3&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">track 2 ip sla 2 reachability&#10; delay down 3 up 3&#10;</code></pre>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="ikev2-ipsec-diagnostics">IKEv2/IPsec diagnostics</h3>
<ul>
<li>Display IKE (Phase 1) Security Associations detail:</li>
</ul>
<pre tabindex="0"><code class="language-txt">show crypto ikev2 sa detailed&#10;</code></pre>
<pre tabindex="0"><code class="language-txt"> IPv4 Crypto IKEv2  SA&#10;&#10;Tunnel-id Local                 Remote                fvrf/ivrf            Status&#10;1     203.0.113.100/500     162.159.135.1/500     none/none            READY&#10;      Encr: AES-GCM, keysize: 256, PRF: SHA512, Hash: None, DH Grp:20, Auth sign: PSK, Auth verify: PSK&#10;      PQC Key Exchange: ML-KEM-768&#10;      Life/Active Time: 86400/501 sec&#10;      CE id: 0, Session-id: 3&#10;      Local spi: 9BEA9E397377D9BB       Remote spi: 0830302A3CD0A874&#10;      Status Description: Negotiation done&#10;      Local id: bf6c493d03REDACTED.ipsec.cloudflare.com&#10;      Remote id: 162.159.135.1&#10;      Local req msg id:  3              Remote req msg id:  0&#10;      Local next msg id: 3              Remote next msg id: 0&#10;      Local req queued:  3              Remote req queued:  0&#10;      Local window:      20             Remote window:      1&#10;      DPD configured for 0 seconds, retry 0&#10;      IETF Std Fragmentation  enabled.&#10;      Quantum-safe Encryption using PQC: ML-KEM-768&#10;      Dynamic Route Update: disabled&#10;      IETF Std Fragmentation MTU in use: 1372 bytes.&#10;      Extended Authentication not configured.&#10;      NAT-T is detected inside&#10;      Cisco Trust Security SGT is disabled&#10;      Initiator of SA : Yes&#10;      PEER TYPE: Other&#10;</code></pre>
<ul>
<li>Clear security associations:</li>
</ul>
<pre tabindex="0"><code class="language-txt">clear crypto session remote &lt;peer-ip-address&gt;&#10;</code></pre>
<p>Another option to restart the IPsec tunnels is to administratively disable and re-enable the tunnel interfaces using <code>shutdown</code> and <code>no shutdown</code>:</p>
<pre tabindex="0"><code class="language-txt">int Tunnel1&#10;shutdown&#10;&#10;no shutdown&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">int Tunnel2&#10;shutdown&#10;&#10;no shutdown&#10;</code></pre>
<h3 id="policy-based-routing-1">Policy-based routing</h3>
<ul>
<li>Display Route Map details. Ensure the counters increment to confirm whether traffic matches the policy (<code>CF_WAN_PBR_ALL</code>):</li>
</ul>
<pre tabindex="0"><code class="language-txt">show route-map CF_WAN_PBR_RM&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">route-map CF_WAN_PBR_RM, permit, sequence 10&#10;  Match clauses:&#10;    ip address (access-lists): CF_WAN_PBR_ALL&#10;  Set clauses:&#10;    vrf CF_WAN_PBR_VRF&#10;  Policy routing matches: 12077 packets, 4639582 bytes&#10;</code></pre>
<ul>
<li>List routes in the VRF (<code>CF_WAN_PBR_VRF</code>):</li>
</ul>
<pre tabindex="0"><code class="language-txt">show ip route vrf CF_WAN_PBR_VRF&#10;&#10;Routing Table: CF_WAN_PBR_VRF&#10;Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP&#10;       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area&#10;       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2&#10;       E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP&#10;       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA&#10;       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2&#10;       ia - IS-IS inter area, * - candidate default, U - per-user static route&#10;       H - NHRP, G - NHRP registered, g - NHRP registration summary&#10;       o - ODR, P - periodic downloaded static route, l - LISP&#10;       a - application route&#10;       &#43; - replicated route, % - next hop override, p - overrides from PfR&#10;       &amp; - replicated local route overrides by connected&#10;&#10;Gateway of last resort is 169.254.244.6 to network 0.0.0.0&#10;&#10;S*    0.0.0.0/0 [1/0] via 169.254.250.0&#10;                [1/0] via 169.254.250.2&#10;</code></pre>
<ul>
<li>List routes matching <code>0.0.0.0/0</code> in the CEF table:</li>
</ul>
<pre tabindex="0"><code class="language-txt">show ip cef vrf CF_WAN_PBR_VRF 0.0.0.0/0&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">0.0.0.0/0&#10;  nexthop 169.254.250.0 Tunnel1&#10;  nexthop 169.254.250.2 Tunnel2&#10;</code></pre>
<h4 id="health-tracking-ip-sla">Health tracking - IP SLA</h4>
<ul>
<li>Display <code>track</code> object state:</li>
</ul>
<pre tabindex="0"><code class="language-txt">show track brief&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">Track Type        Instance                   Parameter        State Last Change&#10;1     ip sla      1                          reachability     Up    00:15:13&#10;2     ip sla      2                          reachability     Up    01:16:08&#10;</code></pre>
<ul>
<li>Display IP SLA statistics:</li>
</ul>
<pre tabindex="0"><code class="language-txt">show ip sla statistics&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">IPSLAs Latest Operation Statistics&#10;&#10;IPSLA operation id: 1&#10;        Latest RTT: 6 milliseconds&#10;Latest operation start time: 15:23:03 CDT Mon Jun 1 2026&#10;Latest operation return code: OK&#10;Number of successes: 380&#10;Number of failures: 1&#10;Operation time to live: Forever&#10;&#10;IPSLA operation id: 2&#10;        Latest RTT: 6 milliseconds&#10;Latest operation start time: 15:23:00 CDT Mon Jun 1 2026&#10;Latest operation return code: OK&#10;Number of successes: 376&#10;Number of failures: 0&#10;Operation time to live: Forever&#10;</code></pre>
<h4 id="validate-tunnel-failover">Validate tunnel failover</h4>
<p>To validate failover, administratively shut one tunnel interface or block ICMP across one of the tunnel paths. Within a few seconds the affected track transitions to <code>Down</code>, the corresponding route is removed from <code>CF_WAN_PBR_VRF</code>, and the remaining tunnel carries all LAN traffic. Restoring the tunnel reverses the change automatically.</p>
<h2 id="references">References</h2>
<ul>
<li><a href="https://www.cisco.com/c/en/us/td/docs/routers/secure-routers/cisco-8000-series-secure-routers-release-26-1-x.html">Release Notes for Cisco 8000 Series Secure Routers, Release 26.1.x</a></li>
<li><a href="https://learningnetwork.cisco.com/s/article/understanding-quantum-safe-encryption-on-cisco-ios-xe-platforms">Understanding Quantum-Safe Encryption on Cisco IOS XE Platforms</a></li>
<li><a href="https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/sec-vpn/b-security-vpn/m-sec-cfg-quantum-encryption-ppk.html">Configuring Quantum-Safe Encryption Using Postquantum Keys - Cisco IOS XE 17.x</a></li>
<li><a href="https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/sec-vpn/b-security-vpn.html">Security and VPN Configuration Guide - Cisco IOS XE 17.x</a></li>
<li><a href="https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/sec-vpn/b-security-vpn/m_sec-ipsec-virt-tunnl-0.html">IPsec Virtual Tunnel Interfaces - Cisco IOS XE 17.x</a></li>
<li><a href="https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/sec-vpn/b-security-vpn/m_sec-cfg-vpn-ipsec-0.html">Configuring Security for VPNs with IPsec - Cisco IOS XE 17.x</a></li>
</ul>
