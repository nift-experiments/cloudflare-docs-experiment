---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-meraki-static/
  description: Integrate Cisco Meraki MX with Zero Trust networking using static routing.
  full_title: Cisco Meraki MX (static routing) · Cloudflare One docs
  head_html: <title>Cisco Meraki MX (static routing) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Cisco Meraki MX with Zero Trust networking using static routing."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-meraki-static/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-meraki-static/index.md"><meta property="og:title" content="Cisco Meraki MX (static routing) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Cisco Meraki MX with Zero Trust networking using static routing."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-meraki-static/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="IPsec"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-meraki-static/#page","headline":"Cisco Meraki MX (static routing) \u00b7 Cloudflare One docs","description":"Integrate Cisco Meraki MX with Zero Trust networking using static routing.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-meraki-static/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["IPsec"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-meraki-static/
  schema: 1
---
<p>This guide provides step-by-step instructions for configuring Cisco Meraki MX appliances to establish IPsec VPN tunnels to Cloudflare WAN. It is intended for network engineers who are familiar with Cisco Meraki administration and have an active Cloudflare WAN subscription.</p>
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
<td>Cisco Meraki</td>
</tr>
<tr>
<td>Model</td>
<td>MX68</td>
</tr>
<tr>
<td>Release</td>
<td>MX 19.2.7</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5629.md")
</aside>
<h2 id="ike-and-ipsec-crypto-settings">IKE and IPsec crypto settings</h2>
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
<td>Active/Standby</td>
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
<td>Enabled</td>
</tr>
<tr>
<td>NAT Traversal (NAT-T)</td>
<td>Not Tested</td>
</tr>
<tr>
<td>NAT-T Port</td>
<td>Not Applicable</td>
</tr>
<tr>
<td>Phase 1 — DH-Group</td>
<td>Group 14</td>
</tr>
<tr>
<td>Phase 1 — Encryption</td>
<td>AES-256-CBC</td>
</tr>
<tr>
<td>Phase 1 — Authentication/Integrity</td>
<td>SHA-256</td>
</tr>
<tr>
<td>Phase 2 — DH-Group</td>
<td>Group 14</td>
</tr>
<tr>
<td>Phase 2 — Transport</td>
<td>ESP</td>
</tr>
<tr>
<td>Phase 2 — Encryption</td>
<td>AES-256-CBC</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5628.md")
</aside>
<h2 id="cloudflare-wan-and-cisco-meraki-mx-configuration">Cloudflare WAN and Cisco Meraki MX configuration</h2>
<p>Replace all object names and IP addresses in the examples below to match your environment.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5627.md")
</aside>
<h3 id="cloudflare-wan-tunnel-1-of-2">Cloudflare WAN tunnel 1 of 2</h3>
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
<td>CF_WAN_TUN_01</td>
</tr>
<tr>
<td>Description</td>
<td>—</td>
</tr>
<tr>
<td>IPv4 Interface Address (required)</td>
<td>169.254.250.0/31</td>
</tr>
<tr>
<td>IPv6 Interface Address</td>
<td>—</td>
</tr>
<tr>
<td>Customer Endpoint</td>
<td>203.0.113.100</td>
</tr>
<tr>
<td>Cloudflare Endpoint</td>
<td>162.159.135.1</td>
</tr>
<tr>
<td>Tunnel health checks</td>
<td>True</td>
</tr>
<tr>
<td>Rate</td>
<td>Low</td>
</tr>
<tr>
<td>Type</td>
<td>Request</td>
</tr>
<tr>
<td>Direction</td>
<td>Bidirectional</td>
</tr>
<tr>
<td>Target</td>
<td>Custom</td>
</tr>
<tr>
<td>Target address</td>
<td>192.168.125.1 (MX LAN Interface IP)</td>
</tr>
<tr>
<td>Turn on replay protection</td>
<td>True</td>
</tr>
<tr>
<td>Automatic return routing</td>
<td>True</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5626.md")
</aside>
<p>Obtain the IKE identity and pre-shared key after tunnel creation:</p>
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
<td><code>bf6c493d03&lt;REDACTED&gt;.ipsec.cloudflare.com</code></td>
</tr>
<tr>
<td>Pre-shared key</td>
<td><code>Cloudflare-WAN-T1-PSK-1234!</code></td>
</tr>
</tbody>
</table>
<h3 id="cloudflare-wan-tunnel-2-of-2">Cloudflare WAN tunnel 2 of 2</h3>
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
<td>CF_WAN_TUN_02</td>
</tr>
<tr>
<td>Description</td>
<td>—</td>
</tr>
<tr>
<td>IPv4 Interface Address (required)</td>
<td>169.254.250.2/31</td>
</tr>
<tr>
<td>IPv6 Interface Address</td>
<td>—</td>
</tr>
<tr>
<td>Customer Endpoint</td>
<td>203.0.113.100</td>
</tr>
<tr>
<td>Cloudflare Endpoint</td>
<td>172.64.135.1</td>
</tr>
<tr>
<td>Tunnel health checks</td>
<td>True</td>
</tr>
<tr>
<td>Rate</td>
<td>Low</td>
</tr>
<tr>
<td>Type</td>
<td>Request</td>
</tr>
<tr>
<td>Direction</td>
<td>Bidirectional</td>
</tr>
<tr>
<td>Target</td>
<td>Custom</td>
</tr>
<tr>
<td>Target address</td>
<td>192.168.125.1 (MX LAN Interface IP)</td>
</tr>
<tr>
<td>Turn on replay protection</td>
<td>True</td>
</tr>
<tr>
<td>Automatic return routing</td>
<td>True</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5625.md")
</aside>
<p>Obtain the IKE identity and pre-shared key after tunnel creation:</p>
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
<td><code>0287844e9d&lt;REDACTED&gt;.ipsec.cloudflare.com</code></td>
</tr>
<tr>
<td>Pre-shared key</td>
<td><code>Cloudflare-WAN-T2-PSK-1234!</code></td>
</tr>
</tbody>
</table>
<h2 id="customer-premise-equipment-cisco-meraki">Customer premise equipment: Cisco Meraki</h2>
<p>Mode: Routed</p>
<table>
<thead>
<tr>
<th><strong>WAN Interface (Port 1)</strong></th>
<th><strong>Tunnel 1 of 2</strong></th>
<th><strong>Tunnel 2 of 2</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>WAN Interface</td>
<td>WAN 1</td>
<td>WAN 1</td>
</tr>
<tr>
<td>IP Address</td>
<td>203.0.113.100/24</td>
<td>203.0.113.100/24</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th><strong>LAN Interface (Port 3)</strong></th>
<th><strong>Tunnel 1 of 2</strong></th>
<th><strong>Tunnel 2 of 2</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>LAN Interface</td>
<td>LAN</td>
<td>LAN</td>
</tr>
<tr>
<td>IP Address</td>
<td>192.168.125.1/24</td>
<td>192.168.125.1/24</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5624.md")
</aside>
<h2 id="assumptions-and-constraints">Assumptions and constraints</h2>
<h3 id="meraki-implementation-and-compatibility-notes">Meraki implementation and compatibility notes</h3>
<ul>
<li><strong>Firmware prerequisite</strong>: The minimum required firmware for this configuration is MX 19.2.7.</li>
<li><strong>Hardware compatibility</strong>: Older Meraki hardware may be physically incapable of running 19.2.7. Route-Based VPN support is required for this architecture. Refer to <a href="https://documentation.meraki.com/Platform_Management/Product_Information/Compatibility_and_Firmware/Firmware_Upgrades/Product_Firmware_Version_Restrictions">Product firmware restrictions</a> to determine whether your MX platform supports firmware release 19.2.7 or later.</li>
<li><strong>Active/Standby configuration</strong>: Redundant tunnels associated with Non-Meraki VPN connections are Active/Standby. Both tunnels are established, but Meraki only routes traffic via the primary IPsec VPN peer and dynamically fails over to the secondary IPsec VPN peer based on tunnel monitoring probes.
<ul>
<li><strong>Anycast and tunnel redundancy</strong>: Despite the Active/Standby nature of IPsec VPN tunnels on the MX platform, high availability is maintained at the network layer because the Cloudflare remote endpoint IPs are advertised via BGP anycast across the Cloudflare global network and provide inherent geographic and logical redundancy.</li>
</ul>
</li>
<li><strong>Route-Based VPN support</strong>: While often associated with specific cloud integrations, version 19.2.7 supports Route-Based IPsec VPN for third-party devices generally, including Cloudflare WAN.</li>
<li><strong>Redundancy and Multi-Uplink</strong>: This documentation specifically covers Active/Standby tunnel configurations.
<ul>
<li><strong>Multi-Uplink IPsec VPN</strong>: The Meraki <a href="https://documentation.meraki.com/SASE_and_SD-WAN/MX/Design_and_Configure/Configuration_Guides/Site-to-site_VPN/Multi-Uplink_IPsec_VPN">Multi-Uplink IPsec VPN</a> feature is outside the scope of this guide.</li>
</ul>
</li>
<li><strong>Anti-Replay Protection</strong>: Cloudflare recommends <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/anti-replay-protection/">disabling Anti-Replay Protection</a> for optimal performance with Cloudflare WAN. The Cisco Meraki MX platform does not permit administrators to disable this feature.
<ul>
<li>This is a known Meraki platform limitation.</li>
<li>In environments with high jitter or out-of-order packet delivery on the underlay (ISP network), this may cause intermittent packet drops on the MX side of the IPsec VPN tunnels.</li>
</ul>
</li>
<li><strong>MSS Clamping</strong>: Cloudflare recommends specific Maximum Segment Size (MSS) <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/mtu-mss/#mss-clamping">clamping</a> values to account for IPsec overhead and prevent fragmentation.
<ul>
<li>The Meraki Dashboard does not provide a user-accessible field to modify the MSS clamping value for third-party VPN tunnels.</li>
<li>Customers must contact Meraki Technical Support to request a manual backend modification of the MSS value (approximately 1360; the value may vary) for the specific network or tunnel.</li>
</ul>
</li>
<li><strong>ISP scope</strong>: The provided configuration is validated for a single Internet Service Provider (ISP). The logic can be extended to accommodate redundant ISPs, but multi-homed configuration is outside the scope of this guide.</li>
</ul>
<h3 id="cloudflare">Cloudflare</h3>
<ul>
<li>This configuration requires the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> dataplane to support <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/traffic-steering/#automatic-return-routing-beta">Automatic Return Routing</a>.</li>
<li>You have already configured IPsec tunnels and static routes in the Cloudflare dashboard.</li>
<li>You have used the Cloudflare dashboard to obtain the local identifier (FQDN/hostname) and generate a pre-shared key for each IPsec tunnel.</li>
<li>You understand the importance of <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/mtu-mss/#mss-clamping">MSS clamping</a> and adjusting it based on the traffic flows traversing the Cloudflare WAN IPsec tunnels.</li>
</ul>
<h2 id="prerequisites-mx-platform-site-to-site-vpn-configuration">Prerequisites: MX platform site-to-site VPN configuration</h2>
<p>The following details from the Cloudflare configuration are required before proceeding with the Meraki configuration:</p>
<ul>
<li>IPv4 interface address values (in Classless Inter-Domain Routing (CIDR) notation)</li>
<li>Cloudflare anycast IPs</li>
<li>Local ID (FQDN/hostname)</li>
<li>Pre-shared keys</li>
<li>Remote subnets</li>
</ul>
<h3 id="cf-wan-tun-01">CF_WAN_TUN_01</h3>
<table>
<thead>
<tr>
<th><strong>Attribute</strong></th>
<th><strong>Value/Address</strong></th>
<th><strong>Meraki — Applies To</strong></th>
<th><strong>Required to</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>IPv4 Interface Address</td>
<td>169.254.250.0/31</td>
<td>Private subnets</td>
<td>Support Cloudflare tunnel health checks</td>
</tr>
<tr>
<td>Cloudflare Endpoint</td>
<td>162.159.135.1</td>
<td>Public IP or hostname</td>
<td>Tunnel peer IP — primary IPsec peer</td>
</tr>
<tr>
<td></td>
<td>162.159.135.1</td>
<td>Remote ID</td>
<td>IKE remote ID — primary IPsec peer</td>
</tr>
<tr>
<td>FQDN ID</td>
<td><code>bf6c493d03&lt;REDACTED&gt;.ipsec.cloudflare.com</code></td>
<td>Local ID</td>
<td>IKE local ID — primary IPsec peer</td>
</tr>
<tr>
<td>Pre-Shared Key</td>
<td><code>Cloudflare-WAN-T1-PSK-1234!</code></td>
<td>Shared secret</td>
<td>Shared secret — primary IPsec peer</td>
</tr>
<tr>
<td>Remote subnets</td>
<td>172.16.10.0/24, 172.16.11.0/24</td>
<td>Private subnets</td>
<td>Add routes for east/west traffic flows</td>
</tr>
</tbody>
</table>
<h3 id="cf-wan-tun-02">CF_WAN_TUN_02</h3>
<table>
<thead>
<tr>
<th><strong>Attribute</strong></th>
<th><strong>Value/Address</strong></th>
<th><strong>Meraki Setting</strong></th>
<th><strong>Required to</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>IPv4 Interface Address</td>
<td>169.254.250.2/31</td>
<td>Private subnets</td>
<td>Support Cloudflare tunnel health checks</td>
</tr>
<tr>
<td>Cloudflare Endpoint</td>
<td>172.64.135.1</td>
<td>Public IP or hostname</td>
<td>Tunnel peer IP — secondary IPsec peer</td>
</tr>
<tr>
<td></td>
<td>172.64.135.1</td>
<td>Remote ID</td>
<td>IKE remote ID — secondary IPsec peer</td>
</tr>
<tr>
<td>FQDN ID</td>
<td><code>0287844e9d&lt;REDACTED&gt;.ipsec.cloudflare.com</code></td>
<td>Local ID</td>
<td>IKE local ID — secondary IPsec peer</td>
</tr>
<tr>
<td>Pre-Shared Key</td>
<td><code>Cloudflare-WAN-T2-PSK-1234!</code></td>
<td>Shared secret</td>
<td>Shared secret — secondary IPsec peer</td>
</tr>
<tr>
<td>Remote subnets</td>
<td>172.16.10.0/24, 172.16.11.0/24</td>
<td>Private subnets</td>
<td>Add routes for east/west traffic flows</td>
</tr>
</tbody>
</table>
<h3 id="remote-subnets">Remote subnets</h3>
<p>In the MX platform, &quot;Private subnets&quot; refers to the remote networks the MX appliance routes through the IPsec tunnels.</p>
<p>This document assumes the following subnets are remote subnets:</p>
<ul>
<li>172.16.10.0/24</li>
<li>172.16.11.0/24</li>
</ul>
<h2 id="cloudflare-1">Cloudflare</h2>
<h3 id="authorize-the-meraki-tunnel-health-probe-source-ip">Authorize the Meraki tunnel health probe source IP</h3>
<p>The MX platform uses tunnel monitoring to enable failover between primary and secondary IPsec VPN tunnels. Tunnel monitoring detects connectivity through the tunnels (not supported on BGP-enabled tunnels). Tunnel monitoring operates independently of Dead Peer Detection, which determines the status of the IPsec tunnels.</p>
<p>The tunnel health probes are used in addition to Dead Peer Detection to determine overall reachability of resources on the remote side of the IPsec tunnels.</p>
<p>Meraki reserves the IP address <code>192.0.2.3/32</code> (part of TEST-NET-1, defined in <a href="https://datatracker.ietf.org/doc/html/rfc5737">RFC 5737</a>) as the source IP for tunnel monitor probes. Refer to <a href="https://documentation.meraki.com/SASE_and_SD-WAN/MX/Design_and_Configure/Configuration_Guides/Site-to-site_VPN/Primary_and_Secondary_IPsec_VPN_Tunnels">Primary and secondary IPsec tunnels</a> for details.</p>
<p>As <code>192.0.2.3/32</code> falls outside the traditional <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918</a> address space, you must add it to the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> dataplane associated with your Cloudflare account.</p>
<p>Contact Cloudflare to request assistance with adding the <code>internal_authorized_prefixes</code> option to your account, with <code>192.0.2.3/32</code> included.</p>
<h3 id="cloudflare-gateway-http-policy">Cloudflare Gateway HTTP policy</h3>
<p>Define an <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policy</a> to permit the tunnel monitoring probe source IP address to reach the IP/URL (HTTP — port 80/tcp).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5623.md")
</aside>
<p>In the Cloudflare dashboard, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong> &gt; <strong>HTTP</strong>.</p>
<ol>
<li>Add a new rule.</li>
<li>For <strong>Policy Name</strong>, enter <code>Meraki Tunnel Health Checks - HTTP Policy</code>.</li>
<li>Build an expression of type <strong>Traffic</strong>.</li>
<li>For <strong>Selector</strong>, enter <code>Source Internal IP is 192.0.2.3</code>.</li>
<li>For <strong>Action</strong>, select <strong>Do Not Inspect</strong>.</li>
</ol>
<p>Position this policy at or near the top of the HTTP policy rulebase.</p>
<h3 id="diagram-meraki-tunnel-monitoring-with-cloudflare-wan">Diagram: Meraki tunnel monitoring with Cloudflare WAN</h3>
<p>The following diagram shows the traffic flow from the tunnel monitoring reserved IP (<code>192.0.2.3/32</code>) as it traverses the IPsec tunnels to Cloudflare WAN, then through Cloudflare Gateway as the requests egress to the Internet. The response path is fully symmetric.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;accTitle: Meraki tunnel monitoring with Cloudflare WAN&#10;accDescr: Traffic flow from the tunnel monitoring source IP through the Meraki MX, IPsec tunnels, Cloudflare WAN, and Cloudflare Gateway to an HTTP target on the public internet.&#10; subgraph CPE[&quot;Cisco Meraki (CPE) Active/Standby Model&quot;]&#10;    direction TB&#10;        FW[&quot;Cisco Meraki MX&#10;        WAN: 203.0.113.100/24&#10;        &#45;--&#10;        LAN: 192.168.125.1/24&#10;        &#45;--&#10;        LAN Subnet: 192.168.125.0/24&quot;]&#10;        L7_Health_Check[&quot;L7 Health Check&#10;        &#45;--&#10;        Internal Src IP: 192.0.2.3/32&quot;]&#10;  end&#10; subgraph T1[&quot;Active - IPsec Tunnel 1&quot;]&#10;    direction LR&#10;        T1_CPE[&quot;CPE VTI 1&#10;        Internal to MX&quot;]&#10;        T1_CF[&quot;Cloudflare VTI 1&#10;        169.254.250.0/31&quot;]&#10;  end&#10; subgraph T2[&quot;Standby - IPsec Tunnel 2&quot;]&#10;    direction LR&#10;        T2_CPE[&quot;CPE VTI 2&#10;        Internal to MX&quot;]&#10;        T2_CF[&quot;Cloudflare VTI 2&#10;        169.254.250.2/31&quot;]&#10;  end&#10; subgraph CF[&quot;Cloudflare WAN&quot;]&#10;    direction TB&#10;        EP1[&quot;Anycast Endpoint 1&#10;        162.159.135.1&quot;]&#10;        EP2[&quot;Anycast Endpoint 2&#10;        172.64.135.1&quot;]&#10;  end&#10; subgraph CF_GW[&quot;Cloudflare Gateway&quot;]&#10;    direction TB&#10;        GW[&quot;Policy&#10;        Src IP 192.0.2.3&#10;        Allow&quot;]&#10;  end&#10;    L7HCT[&quot;HTTP Target&quot;]&#10;&#10;    T1_CPE === T1_CF&#10;    T2_CPE === T2_CF&#10;    FW &lt;==&gt; T1_CPE &amp; T2_CPE&#10;    T1_CF &lt;==&gt; EP1&#10;    T2_CF &lt;==&gt; EP2&#10;&#10;    L7_Health_Check -.-&gt; FW&#10;    FW -.-&gt; T1_CPE&#10;    FW -.-&gt; T2_CPE&#10;    T1_CPE -.-&gt; T1_CF&#10;    T2_CPE -.-&gt; T2_CF&#10;    T1_CF -.-&gt; EP1&#10;    T2_CF -.-&gt; EP2&#10;    EP1 -.-&gt; GW&#10;    EP2 -.-&gt; GW&#10;    GW -.-&gt; L7HCT&#10;    FW@{ shape: stadium}&#10;    T1_CPE@{ shape: stadium}&#10;    T1_CF@{ shape: stadium}&#10;    T2_CPE@{ shape: stadium}&#10;    T2_CF@{ shape: stadium}&#10;    EP1@{ shape: stadium}&#10;    EP2@{ shape: stadium}&#10;    GW@{ shape: stadium}&#10;</code></pre>
<h2 id="meraki-configuration">Meraki configuration</h2>
<h3 id="meraki-management-model-and-cloudflare-wan-integration">Meraki management model and Cloudflare WAN integration</h3>
<p>The Meraki configuration management is built on a two-tier hierarchy. Objects and their associated settings are defined as either:</p>
<ul>
<li><strong>Organization-wide</strong>: Global objects defined once for the entire tenant.</li>
<li><strong>Network-specific</strong>: Settings applied to an individual site or device.</li>
</ul>
<p>The Non-Meraki VPN configuration is an Organization-tier object. It is pushed to specific MX appliances when they are associated with a corresponding Network Tag. This inheritance model is a critical factor: the tag controls which physical hardware attempts to establish tunnels to Cloudflare.</p>
<h3 id="meraki-organization">Meraki Organization</h3>
<p><code>Orbital Path Ventures</code> is a fictitious company referenced throughout the configuration to represent an Organization defined in the Meraki Dashboard.</p>
<p>The company manages a single Meraki MX appliance at their Austin, TX branch office, which is associated with a Network named <code>Orbital Path Ventures - Austin TX</code>.</p>
<p>A Network Tag labeled <code>Orbital_Path_AUS_Office</code> is associated with the <code>Orbital Path Ventures - Austin TX</code> Network.</p>
<table>
<thead>
<tr>
<th>Organization</th>
<th>Network</th>
<th>Tag</th>
</tr>
</thead>
<tbody>
<tr>
<td>Orbit Path Ventures</td>
<td>Orbit Path Ventures - Austin TX</td>
<td><code>Orbital_Path_AUS_Office</code></td>
</tr>
</tbody>
</table>
<h3 id="network-tag">Network Tag</h3>
<p>Go to <strong>Network</strong> &gt; <strong>Networks</strong>, then select the Organization.</p>
<ul>
<li><strong>Orbit Path Ventures</strong> (substitute your Organization name).</li>
<li><strong>Network</strong>: <code>Orbit Path Ventures - Austin TX</code> (substitute your Network name).</li>
<li><strong>Tag</strong>: <code>Orbital_Path_AUS_Office</code> (substitute the Tag associated with the Network name).</li>
</ul>
<h3 id="traffic-steering">Traffic steering</h3>
<p>When integrating with Cloudflare WAN, the Meraki Network Tag determines which appliances inherit the Cloudflare tunnel configuration.</p>
<p>The Non-Meraki VPN configuration is a global object: any MX appliance with the associated Network Tag attempts to establish tunnels to Cloudflare using the same IPsec VPN peers.</p>
<p>To ensure predictable traffic flows and prevent routing conflicts, Cloudflare recommends the following best practices:</p>
<ul>
<li><strong>Strict tunnel correlation</strong>: Maintain a 1-to-1 mapping between the redundant IPsec tunnel pairs defined in Cloudflare and the specific MX appliance initiating those tunnels.</li>
<li><strong>Site-specific Network Tags</strong>: Use granular, site-specific tags (for example, <code>Orbital_Path_AUS_Office</code>) rather than broad, generic tags to ensure only the intended MX inherits the tunnel configuration.</li>
<li><strong>Unique IPsec VPN peer objects</strong>: Create distinct Non-Meraki VPN peer objects at the Organization level for different physical geographic locations. Use the <strong>Availability</strong> option to establish the 1-to-1 mapping.</li>
</ul>
<p>Return traffic from Cloudflare WAN is steered based on the Cloudflare virtual network routing table (refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/traffic-steering/">Traffic steering</a> for details). Routes are specified based on the MX LAN prefix and corresponding IPsec tunnels.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5622.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5621.md")
</aside>
<h4 id="source-based-default-routing">Source-based default routing</h4>
<p><a href="https://documentation.meraki.com/SASE_and_SD-WAN/MX/Design_and_Configure/Configuration_Guides/Networks_and_Routing/Source_Based_Default_Routing">Source-Based Default Routing</a> enables an administrator to create a source-based default route and specify a next hop as a security appliance over Auto VPN or on a device on the LAN.</p>
<p>Source-Based Default Routing cannot be used in conjunction with Non-Meraki VPN endpoints, including Cloudflare WAN.</p>
<p>Define private subnets in the IPsec VPN peer configuration to control how MX appliances steer traffic through the respective tunnels.</p>
<h4 id="routing-with-private-subnets">Routing with private subnets</h4>
<p>Any IP prefixes defined as private subnets in the IPsec VPN peer configuration control what traffic is routed across the primary and secondary VPN tunnels. They are visible in the routing table corresponding to a given MX appliance.</p>
<p>This document considers three route topologies:</p>
<ol>
<li>East/west only:
<ul>
<li>Private traffic via Cloudflare WAN.</li>
<li>Internet via local Internet.</li>
</ul>
</li>
<li>Internet only via Cloudflare Gateway:
<ul>
<li>Only route Internet traffic through Cloudflare WAN.</li>
</ul>
</li>
<li>All traffic via Cloudflare WAN and Gateway:
<ul>
<li>East/west and Internet traffic routed via Cloudflare WAN.</li>
</ul>
</li>
</ol>
<p>All three topologies are covered in the <a href="#ipsec-vpn-peers">IPsec VPN peers</a> section.</p>
<h2 id="mx-site-to-site-vpn-configuration">MX site-to-site VPN configuration</h2>
<p>Go to <strong>Security &amp; SD-WAN</strong> &gt; <strong>Site-to-site VPN</strong>.</p>
<h3 id="type">Type</h3>
<p>Select <strong>Hub (Mesh)</strong>.</p>
<h3 id="vpn-settings">VPN settings</h3>
<h4 id="local-networks">Local networks</h4>
<p>Turn on VPN mode for the local network behind the MX devices.</p>
<p>From:</p>
<table>
<thead>
<tr>
<th><strong>Name</strong></th>
<th><strong>VPN Mode</strong></th>
<th><strong>Subnet</strong></th>
<th><strong>Uplink</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Default</td>
<td><strong>Disabled</strong></td>
<td>192.168.125.0/24</td>
<td>—</td>
</tr>
</tbody>
</table>
<p>To:</p>
<table>
<thead>
<tr>
<th><strong>Name</strong></th>
<th><strong>VPN Mode</strong></th>
<th><strong>Subnet</strong></th>
<th><strong>Uplink</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Default</td>
<td><strong>Enabled</strong></td>
<td>192.168.125.0/24</td>
<td>—</td>
</tr>
</tbody>
</table>
<h4 id="ipsec-vpn-peers">IPsec VPN peers</h4>
<p>Go to <strong>Security &amp; SD-WAN</strong> &gt; <strong>Site-to-site VPN</strong> &gt; <strong>Organization Wide Settings</strong>.</p>
<h5 id="configure-health-checks">Configure health checks</h5>
<p>Configure a Layer 7 health check HTTP probe that the MX platform uses to determine reachability of resources through the IPsec VPN tunnels:</p>
<ol>
<li>Select <strong>Configure Health Checks</strong>.</li>
<li>Provide the following values:</li>
</ol>
<table>
<thead>
<tr>
<th><strong>Name</strong></th>
<th><strong>Endpoint</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Google</td>
<td><code>http://www.google.com</code></td>
</tr>
</tbody>
</table>
<ol start="3">
<li>Select <strong>OK</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5620.md")
</aside>
<h5 id="add-primary-and-secondary-ipsec-vpn-peers">Add primary and secondary IPsec VPN peers</h5>
<p>IPsec VPN peer configurations are provided for the following topologies:</p>
<ul>
<li>East/west traffic only</li>
<li>Internet only via Cloudflare Gateway</li>
<li>All traffic via Cloudflare WAN and Gateway</li>
</ul>
<h6 id="topology-east-west-traffic-only">Topology: east/west traffic only</h6>
<p>Routing east/west traffic via Cloudflare WAN requires:</p>
<ul>
<li>Cloudflare routes specified for the LAN subnet behind the MX appliance (<code>192.168.125.0/24</code>) via <code>CF_WAN_TUN_01</code> and <code>CF_WAN_TUN_02</code>.</li>
<li>Remote subnets (<code>172.16.10.0/24</code> and <code>172.16.11.0/24</code>) specified as private subnets on the Meraki primary and secondary IPsec VPN peers.</li>
<li>The IPv4 interface address prefixes specified on both <code>CF_WAN_TUN_01</code> and <code>CF_WAN_TUN_02</code> (<code>169.254.250.0/31</code> and <code>169.254.250.2/31</code>) specified as private subnets on the Meraki primary and secondary IPsec VPN peers.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5619.md")
</aside>
<p>This ensures that:</p>
<ul>
<li>Cloudflare routes traffic destined for the LAN subnet behind the MX appliance via <code>CF_WAN_TUN_01</code> and <code>CF_WAN_TUN_02</code>.</li>
<li>The MX appliance explicitly routes traffic destined for the remote subnets (<code>172.16.10.0/24</code> and <code>172.16.11.0/24</code>) via the primary and secondary IPsec VPN peers respectively.</li>
<li>The MX appliance explicitly routes ICMP Reply packets associated with Cloudflare tunnel health checks to the IPv4 interface addresses (<code>169.254.250.0/31</code> and <code>169.254.250.2/31</code>) specified on <code>CF_WAN_TUN_01</code> and <code>CF_WAN_TUN_02</code> via the primary and secondary IPsec VPN peers respectively.</li>
<li>Internet traffic from the LAN subnet behind the MX appliance is routed via the WAN uplink.</li>
<li>The MX appliance establishes IPsec tunnels to Cloudflare endpoints (<code>162.159.135.1</code> and <code>172.64.135.1</code>) via the WAN uplink.</li>
</ul>
<p>Configure the following:</p>
<p>Cloudflare IPsec tunnels — automatic return routing:</p>
<table>
<thead>
<tr>
<th><strong>Tunnel</strong></th>
<th><strong>Automatic Return Routing</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>CF_WAN_TUN_01</td>
<td>Disabled</td>
</tr>
<tr>
<td>CF_WAN_TUN_02</td>
<td>Disabled</td>
</tr>
</tbody>
</table>
<p>Cloudflare routes:</p>
<table>
<thead>
<tr>
<th><strong>Prefix</strong></th>
<th><strong>Description</strong></th>
<th><strong>Next hop</strong></th>
<th><strong>Priority</strong></th>
<th><strong>Region code</strong></th>
<th><strong>Type</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>192.168.125.0/24</td>
<td>CF_WAN_TUN_01</td>
<td>CF_WAN_TUN_01</td>
<td>100</td>
<td>All regions</td>
<td>Static</td>
</tr>
<tr>
<td>192.168.125.0/24</td>
<td>CF_WAN_TUN_02</td>
<td>CF_WAN_TUN_02</td>
<td>100</td>
<td>All regions</td>
<td>Static</td>
</tr>
</tbody>
</table>
<p>Meraki private subnets:</p>
<table>
<thead>
<tr>
<th><strong>Private Subnet</strong></th>
<th><strong>Scope</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>172.16.10.0/24</td>
<td>Remote site</td>
</tr>
<tr>
<td>172.16.11.0/24</td>
<td>Remote site</td>
</tr>
<tr>
<td>169.254.250.0/31</td>
<td>CF_WAN_TUN_01 — tunnel health check ICMP Reply packets</td>
</tr>
<tr>
<td>169.254.250.2/31</td>
<td>CF_WAN_TUN_02 — tunnel health check ICMP Reply packets</td>
</tr>
</tbody>
</table>
<h6 id="primary-ipsec-vpn-peer-east-west-traffic-only">Primary IPsec VPN peer: east/west traffic only</h6>
<ol>
<li>Select <strong>+ Add a peer</strong>.</li>
<li>Provide the following values:</li>
</ol>
<table>
<thead>
<tr>
<th><strong>Attribute</strong></th>
<th><strong>Value</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Name</td>
<td><code>cf-wan-tun-01</code></td>
</tr>
<tr>
<td>IKE Version</td>
<td>IKEv2</td>
</tr>
<tr>
<td>Public IP or Hostname</td>
<td>162.159.135.1</td>
</tr>
<tr>
<td>Local ID</td>
<td><code>bf6c493d03&lt;REDACTED&gt;.ipsec.cloudflare.com</code></td>
</tr>
<tr>
<td>Remote ID</td>
<td>—</td>
</tr>
<tr>
<td>Shared Secret</td>
<td><code>Cloudflare-WAN-T1-PSK-1234!</code></td>
</tr>
<tr>
<td>Routing</td>
<td>Static</td>
</tr>
<tr>
<td>Private Subnets</td>
<td>169.254.250.0/31, 169.254.250.2/31, 172.16.10.0/24, 172.16.11.0/24</td>
</tr>
<tr>
<td>Availability</td>
<td><code>Orbital_Path_AUS_Office</code></td>
</tr>
<tr>
<td>Tunnel Monitoring</td>
<td>Google Health Check</td>
</tr>
<tr>
<td>Failover directly to internet</td>
<td>—</td>
</tr>
<tr>
<td>IPsec Policy</td>
<td>—</td>
</tr>
<tr>
<td>Preset</td>
<td>Custom</td>
</tr>
<tr>
<td>Phase 1 — Encryption</td>
<td>AES 256</td>
</tr>
<tr>
<td>Phase 1 — Authentication</td>
<td>SHA256</td>
</tr>
<tr>
<td>Phase 1 — Pseudo-Random Function</td>
<td>SHA256</td>
</tr>
<tr>
<td>Phase 1 — Diffie-Hellman group</td>
<td>14</td>
</tr>
<tr>
<td>Phase 1 — Lifetime (sec)</td>
<td>28800</td>
</tr>
<tr>
<td>Phase 2 — Encryption</td>
<td>AES256</td>
</tr>
<tr>
<td>Phase 2 — Authentication</td>
<td>SHA256</td>
</tr>
<tr>
<td>Phase 2 — PFS Group</td>
<td>14</td>
</tr>
<tr>
<td>Phase 2 — Lifetime (sec)</td>
<td>28800</td>
</tr>
</tbody>
</table>
<ol start="3">
<li>Select <strong>Save</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5618.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5617.md")
</aside>
<h6 id="secondary-ipsec-vpn-peer-east-west-traffic-only">Secondary IPsec VPN peer: east/west traffic only</h6>
<ol>
<li>Select the <code>---</code> icon in the settings column.</li>
<li>Select <strong>+ Add secondary peer</strong>.</li>
<li>Do not select <strong>Inherit primary peer configurations</strong>. This ensures the <strong>Public IP or Hostname</strong>, <strong>Local ID</strong>, <strong>Remote ID</strong>, and <strong>Shared secret</strong> are configured with the settings required to successfully negotiate an IPsec tunnel <code>CF_WAN_TUN_02</code>.</li>
<li>Provide the following values:</li>
</ol>
<table>
<thead>
<tr>
<th><strong>Attribute</strong></th>
<th><strong>Value</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Name</td>
<td><code>cf-wan-tun-02</code></td>
</tr>
<tr>
<td>IKE Version</td>
<td>IKEv2 (Inherited)</td>
</tr>
<tr>
<td>Public IP or Hostname</td>
<td>172.64.135.1</td>
</tr>
<tr>
<td>Local ID</td>
<td><code>0287844e9d&lt;REDACTED&gt;.ipsec.cloudflare.com</code></td>
</tr>
<tr>
<td>Remote ID</td>
<td>172.64.135.1</td>
</tr>
<tr>
<td>Shared Secret</td>
<td><code>Cloudflare-WAN-T2-PSK-1234!</code></td>
</tr>
<tr>
<td>Routing</td>
<td>Static (Inherited)</td>
</tr>
<tr>
<td>Private Subnets</td>
<td>169.254.250.0/31, 169.254.250.2/31, 172.16.10.0/24, 172.16.11.0/24 (Inherited)</td>
</tr>
<tr>
<td>Availability</td>
<td><code>Orbital_Path_AUS_Office</code> (Inherited)</td>
</tr>
<tr>
<td>Tunnel Monitoring</td>
<td>Google Health Check</td>
</tr>
<tr>
<td>Failover directly to internet</td>
<td>—</td>
</tr>
<tr>
<td>IPsec Policy</td>
<td>—</td>
</tr>
<tr>
<td>Preset</td>
<td>Custom</td>
</tr>
<tr>
<td>Phase 1 — Encryption</td>
<td>AES 256</td>
</tr>
<tr>
<td>Phase 1 — Authentication</td>
<td>SHA256</td>
</tr>
<tr>
<td>Phase 1 — Pseudo-Random Function</td>
<td>SHA256</td>
</tr>
<tr>
<td>Phase 1 — Diffie-Hellman group</td>
<td>14</td>
</tr>
<tr>
<td>Phase 1 — Lifetime (sec)</td>
<td>28800</td>
</tr>
<tr>
<td>Phase 2 — Encryption</td>
<td>AES256</td>
</tr>
<tr>
<td>Phase 2 — Authentication</td>
<td>SHA256</td>
</tr>
<tr>
<td>Phase 2 — PFS Group</td>
<td>14</td>
</tr>
<tr>
<td>Phase 2 — Lifetime (sec)</td>
<td>28800</td>
</tr>
</tbody>
</table>
<ol start="5">
<li>Select <strong>Save</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5616.md")
</aside>
<h5 id="route-table-east-west-traffic-only">Route table: east/west traffic only</h5>
<p>Confirm the MX appliance route table includes routes for the private subnets defined in the primary and secondary IPsec VPN peer configuration.</p>
<p>Go to <strong>Security &amp; SD-WAN</strong> &gt; <strong>Monitor</strong> &gt; <strong>Route table</strong>.</p>
<p>The Meraki route table reflects routes via <code>cf-wan-tun-01</code> and <code>cf-wan-tun-02</code> as follows:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Version</th>
<th>Subnet</th>
<th>Name</th>
<th>VLAN</th>
<th>Next-Hop</th>
<th>Destination</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>—</td>
<td>4</td>
<td>0.0.0.0/0</td>
<td>Default</td>
<td>—</td>
<td>—</td>
<td>WAN uplink</td>
<td>Default WAN Route</td>
</tr>
<tr>
<td>—</td>
<td>4</td>
<td>169.254.250.0/31</td>
<td>cf-wan-tun-01</td>
<td>—</td>
<td>cf-wan-tun-01</td>
<td>—</td>
<td>IPsec Peer</td>
</tr>
<tr>
<td>—</td>
<td>4</td>
<td>169.254.250.0/31</td>
<td>cf-wan-tun-02</td>
<td>—</td>
<td>cf-wan-tun-02</td>
<td>—</td>
<td>IPsec Peer</td>
</tr>
<tr>
<td>—</td>
<td>4</td>
<td>169.254.250.2/31</td>
<td>cf-wan-tun-01</td>
<td>—</td>
<td>cf-wan-tun-01</td>
<td>—</td>
<td>IPsec Peer</td>
</tr>
<tr>
<td>—</td>
<td>4</td>
<td>169.254.250.2/31</td>
<td>cf-wan-tun-02</td>
<td>—</td>
<td>cf-wan-tun-02</td>
<td>—</td>
<td>IPsec Peer</td>
</tr>
<tr>
<td>—</td>
<td>4</td>
<td>172.16.10.0/24</td>
<td>cf-wan-tun-01</td>
<td>—</td>
<td>cf-wan-tun-01</td>
<td>—</td>
<td>IPsec Peer</td>
</tr>
<tr>
<td>—</td>
<td>4</td>
<td>172.16.10.0/24</td>
<td>cf-wan-tun-02</td>
<td>—</td>
<td>cf-wan-tun-02</td>
<td>—</td>
<td>IPsec Peer</td>
</tr>
<tr>
<td>—</td>
<td>4</td>
<td>172.16.11.0/24</td>
<td>cf-wan-tun-01</td>
<td>—</td>
<td>cf-wan-tun-01</td>
<td>—</td>
<td>IPsec Peer</td>
</tr>
<tr>
<td>—</td>
<td>4</td>
<td>172.16.11.0/24</td>
<td>cf-wan-tun-02</td>
<td>—</td>
<td>cf-wan-tun-02</td>
<td>—</td>
<td>IPsec Peer</td>
</tr>
<tr>
<td>🟢</td>
<td>4</td>
<td>192.168.125.0/24</td>
<td>LAN</td>
<td>1</td>
<td>192.168.125.1</td>
<td>192.168.125.1</td>
<td>Local VLAN</td>
</tr>
</tbody>
</table>
<h4 id="tunnel-health-and-failover">Tunnel health and failover</h4>
<p>Meraki uses tunnel monitoring to determine when to fail over automatically to the secondary IPsec VPN peer. Meraki uses Dead Peer Detection to determine the overall health of the IPsec tunnels.</p>
<p>Non-Meraki VPN peers support an Active/Standby model. Traffic is sent via <code>cf-wan-tun-01</code> until a failover event occurs, at which point <code>cf-wan-tun-02</code> becomes active. Traffic is dynamically reverted to <code>cf-wan-tun-01</code> once its tunnel is reconnected.</p>
<p>Failover testing indicates traffic may be disrupted for a few seconds. Cloudflare has observed some failover events taking 15 to 20 seconds, but these incidents are rare.</p>
<h5 id="cloudflare-tunnel-health">Cloudflare tunnel health</h5>
<p>Cloudflare tunnel health checks indicate 100% failure on the tunnel marked as standby. This ensures traffic is only steered through the active tunnel.</p>
<table>
<thead>
<tr>
<th><strong>Active Peer</strong></th>
<th><strong>Tunnel health</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Primary IPsec VPN peer</td>
<td><strong>CF_WAN_TUN_01</strong>: 🟢 0%</td>
<td><strong>CF_WAN_TUN_02</strong>: 🔴 100%</td>
</tr>
<tr>
<td>Secondary IPsec VPN peer</td>
<td><strong>CF_WAN_TUN_01</strong>: 🔴 100%</td>
<td><strong>CF_WAN_TUN_02</strong>: 🟢 0%</td>
</tr>
</tbody>
</table>
<h5 id="meraki-tunnel-health">Meraki tunnel health</h5>
<p>Use the Meraki Dashboard to determine the status of the IPsec tunnels:</p>
<ol>
<li>Go to <strong>Security &amp; SD-WAN</strong> &gt; <strong>Monitor</strong> &gt; <strong>VPN Status</strong>.</li>
<li>Scroll to the <strong>Overview</strong> section.</li>
<li>Select the filter labeled <strong>2 IPsec peers</strong>.</li>
</ol>
<h6 id="east-west-traffic-only">East/west traffic only</h6>
<p>Active tunnel: <code>cf-wan-tun-01</code>:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Name</th>
<th>Public IP</th>
<th>Subnets</th>
<th>Tunnel monitor</th>
</tr>
</thead>
<tbody>
<tr>
<td>🟢 IPsec</td>
<td>cf-wan-tun-01</td>
<td>162.159.135.1</td>
<td>169.254.250.0/31</td>
<td>Details (link)</td>
</tr>
<tr>
<td>🟢 Health check</td>
<td></td>
<td></td>
<td>169.254.250.2/31</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>172.16.10.0/24</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>172.16.11.0/24</td>
<td></td>
</tr>
<tr>
<td>🟢 IPsec</td>
<td>cf-wan-tun-02</td>
<td>172.64.135.1</td>
<td>169.254.250.0/31</td>
<td>Details (link)</td>
</tr>
<tr>
<td>🟢 Health check</td>
<td></td>
<td></td>
<td>169.254.250.2/31</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>172.16.10.0/24</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>172.16.11.0/24</td>
<td></td>
</tr>
</tbody>
</table>
<p>Active tunnel: <code>cf-wan-tun-02</code>:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Name</th>
<th>Public IP</th>
<th>Subnets</th>
<th>Tunnel monitor</th>
</tr>
</thead>
<tbody>
<tr>
<td>🟢 IPsec</td>
<td>cf-wan-tun-01</td>
<td>162.159.135.1</td>
<td>169.254.250.0/31</td>
<td>Details (link)</td>
</tr>
<tr>
<td>🔴 Health check</td>
<td></td>
<td></td>
<td>169.254.250.2/31</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>172.16.10.0/24</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>172.16.11.0/24</td>
<td></td>
</tr>
<tr>
<td>🟢 IPsec</td>
<td>cf-wan-tun-02</td>
<td>172.64.135.1</td>
<td>169.254.250.0/31</td>
<td>Details (link)</td>
</tr>
<tr>
<td>🟢 Health check</td>
<td></td>
<td></td>
<td>169.254.250.2/31</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>172.16.10.0/24</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>172.16.11.0/24</td>
<td></td>
</tr>
</tbody>
</table>
<h6 id="internet-only-via-cloudflare-gateway">Internet only via Cloudflare Gateway</h6>
<p>Active tunnel: <code>cf-wan-tun-01</code>:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Name</th>
<th>Public IP</th>
<th>Subnets</th>
<th>Tunnel monitor</th>
</tr>
</thead>
<tbody>
<tr>
<td>🟢 IPsec</td>
<td>cf-wan-tun-01</td>
<td>162.159.135.1</td>
<td>0.0.0.0/0</td>
<td>Details (link)</td>
</tr>
<tr>
<td>🟢 Health check</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>🟢 IPsec</td>
<td>cf-wan-tun-02</td>
<td>172.64.135.1</td>
<td>0.0.0.0/0</td>
<td>Details (link)</td>
</tr>
<tr>
<td>🟢 Health check</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>Active tunnel: <code>cf-wan-tun-02</code>:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Name</th>
<th>Public IP</th>
<th>Subnets</th>
<th>Tunnel monitor</th>
</tr>
</thead>
<tbody>
<tr>
<td>🟢 IPsec</td>
<td>cf-wan-tun-01</td>
<td>162.159.135.1</td>
<td>0.0.0.0/0</td>
<td>Details (link)</td>
</tr>
<tr>
<td>🔴 Health check</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>🟢 IPsec</td>
<td>cf-wan-tun-02</td>
<td>172.64.135.1</td>
<td>0.0.0.0/0</td>
<td>Details (link)</td>
</tr>
<tr>
<td>🟢 Health check</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h6 id="all-traffic-via-cloudflare-wan-and-gateway">All traffic via Cloudflare WAN and Gateway</h6>
<p>Active tunnel: <code>cf-wan-tun-01</code>:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Name</th>
<th>Public IP</th>
<th>Subnets</th>
<th>Tunnel monitor</th>
</tr>
</thead>
<tbody>
<tr>
<td>🟢 IPsec</td>
<td>cf-wan-tun-01</td>
<td>162.159.135.1</td>
<td>0.0.0.0/0</td>
<td>Details (link)</td>
</tr>
<tr>
<td>🟢 Health check</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>🟢 IPsec</td>
<td>cf-wan-tun-02</td>
<td>172.64.135.1</td>
<td>0.0.0.0/0</td>
<td>Details (link)</td>
</tr>
<tr>
<td>🟢 Health check</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>Active tunnel: <code>cf-wan-tun-02</code>:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Name</th>
<th>Public IP</th>
<th>Subnets</th>
<th>Tunnel monitor</th>
</tr>
</thead>
<tbody>
<tr>
<td>🟢 IPsec</td>
<td>cf-wan-tun-01</td>
<td>162.159.135.1</td>
<td>0.0.0.0/0</td>
<td>Details (link)</td>
</tr>
<tr>
<td>🔴 Health check</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>🟢 IPsec</td>
<td>cf-wan-tun-02</td>
<td>172.64.135.1</td>
<td>0.0.0.0/0</td>
<td>Details (link)</td>
</tr>
<tr>
<td>🟢 Health check</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="mx-platform-routing-table">MX platform routing table</h3>
<p>Review the MX route table to determine what traffic is routed over the IPsec tunnels compared to direct internet routing.</p>
<p>Go to <strong>Security &amp; SD-WAN</strong> &gt; <strong>Monitor</strong> &gt; <strong>Route Table</strong>.</p>
<h3 id="mx-tunnel-monitoring">MX tunnel monitoring</h3>
<p>VPN Status reports that the health checks are failing on both tunnels:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Name</th>
<th>Public IP</th>
<th>Subnets</th>
<th>Tunnel monitor</th>
</tr>
</thead>
<tbody>
<tr>
<td>🟢 IPsec</td>
<td>cf-wan-tun-01</td>
<td>162.159.135.1</td>
<td>169.254.250.0/31</td>
<td>Details (link)</td>
</tr>
<tr>
<td>🔴 Health check</td>
<td></td>
<td></td>
<td>169.254.250.2/31</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>172.16.10.0/24</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>172.16.11.0/24</td>
<td></td>
</tr>
<tr>
<td>🟢 IPsec</td>
<td>cf-wan-tun-02</td>
<td>172.64.135.1</td>
<td>169.254.250.0/31</td>
<td>Details (link)</td>
</tr>
<tr>
<td>🔴 Health check</td>
<td></td>
<td></td>
<td>169.254.250.2/31</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>172.16.10.0/24</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>172.16.11.0/24</td>
<td></td>
</tr>
</tbody>
</table>
<p>Check the Cloudflare Gateway logs and policy to determine if HTTP requests originating from <code>192.0.2.3/32</code> are being blocked.</p>
<p>If blocked, create a rule to restore tunnel monitoring HTTP requests. Refer to <a href="#cloudflare-gateway-http-policy">Cloudflare Gateway HTTP policy</a> for details.</p>
<h3 id="cloudflare-and-meraki-ipsec-logs">Cloudflare and Meraki IPsec logs</h3>
<p>Available in:</p>
<ul>
<li><a href="/log-explorer/">Log Explorer</a></li>
<li><a href="/logs/logpush/">Logpush</a> &gt; <a href="/logs/logpush/logpush-job/datasets/account/ipsec_logs/">IPsec logs</a></li>
</ul>
<p>IPsec logs can help diagnose a variety of issues related to IPsec tunnels, including:</p>
<ul>
<li>Using unsupported Phase 1 or Phase 2 encryption or integrity settings — look for messages indicating <code>No proposal chosen</code>.
<ul>
<li>Confirm that the Phase 1 and Phase 2 encryption or integrity values defined are supported by Cloudflare WAN.</li>
<li>Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/gre-ipsec-tunnels/#supported-configuration-parameters">Supported configuration parameters</a>.</li>
</ul>
</li>
<li>IKE/IPsec identity: local or remote identity not defined or with incorrect values.
<ul>
<li>Refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/palo-alto/">Palo Alto third-party integration guide</a> for an example of FQDN-based local identification.</li>
</ul>
</li>
<li>Authentication failures: wrong pre-shared key.</li>
</ul>
<p>Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">Configure tunnel endpoints</a> for more details.</p>
<h3 id="cloudflare-tunnel-health-checks">Cloudflare tunnel health checks</h3>
<p>Ensure tunnel health checks for both <code>CF_WAN_TUN_01</code> and <code>CF_WAN_TUN_02</code> are configured with the following settings:</p>
<table>
<thead>
<tr>
<th><strong>Attribute</strong></th>
<th><strong>Value</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Enabled</td>
<td>True</td>
<td>Ensure the indicator displays 🟢 Enabled.</td>
</tr>
<tr>
<td>Type</td>
<td>Request</td>
<td>A stateful firewall drops ICMP Reply probes.</td>
</tr>
<tr>
<td>Direction</td>
<td>Bidirectional</td>
<td>Ensures probes are sent and received via the tunnel.</td>
</tr>
<tr>
<td>Target</td>
<td>Custom</td>
<td>The MX platform does not support VTIs, so probes must target an alternate IP.</td>
</tr>
<tr>
<td>Target address</td>
<td>192.168.125.1</td>
<td>Send probes to the LAN interface on the MX appliance.</td>
</tr>
</tbody>
</table>
<h2 id="meraki-references">Meraki references</h2>
<ul>
<li><a href="https://documentation.meraki.com/SASE_and_SD-WAN/MX/Design_and_Configure/Configuration_Guides/Firewall_and_Traffic_Shaping/Connection_Monitoring_for_WAN_Failover#Enhanced_WAN_Failover_and_Failback">Connection Monitoring for WAN Failover</a></li>
<li><a href="https://documentation.meraki.com/SASE_and_SD-WAN/MX/Design_and_Configure/Configuration_Guides/Networks_and_Routing/MX_Routing_Behavior">MX Routing Behavior</a></li>
<li><a href="https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Operate_and_Maintain/Inventory_and_Devices/Organization_Overview">Organization Overview</a></li>
<li><a href="https://documentation.meraki.com/SASE_and_SD-WAN/MX/Design_and_Configure/Configuration_Guides/Site-to-site_VPN/Primary_and_Secondary_IPsec_VPN_Tunnels">Primary and Secondary IPsec VPN Tunnels</a></li>
<li><a href="https://documentation.meraki.com/SASE_and_SD-WAN/MX/Design_and_Configure/Configuration_Guides/Site-to-site_VPN/Site-to-Site_VPN_Settings#Peer_availability">Site-to-Site VPN</a></li>
</ul>
