---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/juniper/
  description: Connect HPE Juniper SRX to Cloudflare WAN.
  full_title: HPE Juniper Networking SRX Series Firewalls · Cloudflare WAN docs
  head_html: <title>HPE Juniper Networking SRX Series Firewalls · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect HPE Juniper SRX to Cloudflare WAN."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/juniper/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/juniper/index.md"><meta property="og:title" content="HPE Juniper Networking SRX Series Firewalls · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect HPE Juniper SRX to Cloudflare WAN."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/juniper/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare WAN"><meta name="pcx_tags" content="IPsec"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/juniper/#page","headline":"HPE Juniper Networking SRX Series Firewalls \u00b7 Cloudflare WAN docs","description":"Connect HPE Juniper SRX to Cloudflare WAN.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/juniper/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["IPsec"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/third-party/juniper/
  schema: 1
---
<h2 id="overview">Overview</h2>
<p>This guide provides step-by-step instructions for configuring HPE Juniper Networking SRX Series Firewalls to establish IPsec VPN tunnels to Cloudflare WAN. It is intended for network engineers who are familiar with HPE Juniper Networking SRX Series Firewalls administration and have an active Cloudflare WAN subscription.</p>
<h2 id="test-environment">Test Environment</h2>
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
<td>HPE Juniper Networking</td>
</tr>
<tr>
<td>Model</td>
<td>SRX 320</td>
</tr>
<tr>
<td>Release</td>
<td>JUNOS 23.4R2-S3.9</td>
</tr>
<tr>
<td>Date Tested</td>
<td>March 2026</td>
</tr>
</tbody>
</table>
<h2 id="ike-ipsec-crypto-relevant-settings">IKE/IPsec Crypto &amp; Relevant Settings</h2>
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
<td>Not Tested</td>
</tr>
<tr>
<td>NAT-T Port</td>
<td>Not Applicable</td>
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
</tbody>
</table>
<h2 id="cloudflare-wan-and-hpe-juniper-networking-srx-series-firewalls-configuration-settings">Cloudflare WAN and HPE Juniper Networking SRX Series Firewalls - Configuration Settings</h2>
<ul>
<li>While following these steps, ensure you update all object names and IP addresses to match your environment.</li>
<li>Aligning these elements with your actual naming conventions and network scheme ensures the configuration works correctly in your production setup.</li>
<li>Use Find and Replace to parse the examples below, update the names and addresses accordingly, and maintain consistency.</li>
</ul>
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
<td>CF_WAN_TUN_01</td>
</tr>
<tr>
<td>Description</td>
<td>---</td>
</tr>
<tr>
<td>IPv4 Interface Address (required)</td>
<td>169.254.250.0/31</td>
</tr>
<tr>
<td>IPv6 Interface Address</td>
<td>---</td>
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
<td>---</td>
<td>---</td>
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
<ul>
<li>IKE Identity and Pre-shared Key (obtained after tunnel creation):</li>
</ul>
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
<td>Cloudflare-WAN-T1-PSK-1234!</td>
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
<td>CF_WAN_TUN_02</td>
</tr>
<tr>
<td>Description</td>
<td>---</td>
</tr>
<tr>
<td>IPv4 Interface Address (required)</td>
<td>169.254.250.2/31</td>
</tr>
<tr>
<td>IPv6 Interface Address</td>
<td>---</td>
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
<td>---</td>
<td>---</td>
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
<ul>
<li>IKE Identity and Pre-shared Key (obtained after tunnel creation):</li>
</ul>
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
<td>Cloudflare-WAN-T2-PSK-1234!</td>
</tr>
</tbody>
</table>
<h2 id="customer-premise-equipment-hpe-juniper-networking">Customer Premise Equipment - HPE Juniper Networking</h2>
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
<td>ge-0/0/0.0</td>
<td>ge-0/0/0.0</td>
</tr>
<tr>
<td>IP Address</td>
<td>203.0.113.100/24</td>
<td>203.0.113.100/24</td>
</tr>
<tr>
<td>Security Zone</td>
<td>untrust</td>
<td>untrust</td>
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
<td>st0.1</td>
<td>st0.2</td>
</tr>
<tr>
<td>IP Address</td>
<td>169.254.250.1/31</td>
<td>169.254.250.3/31</td>
</tr>
<tr>
<td>Security Zone</td>
<td>cloudflare</td>
<td>cloudflare</td>
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
<td>ge-0/0/1.0</td>
<td>ge-0/0/1.0</td>
</tr>
<tr>
<td>IP Address</td>
<td>192.168.125.1/24</td>
<td>192.168.125.1/24</td>
</tr>
<tr>
<td>Security Zone</td>
<td>trust</td>
<td>trust</td>
</tr>
</tbody>
</table>
<h3 id="hpe-juniper-networking-srx-object-names">HPE Juniper Networking SRX Object Names</h3>
<table>
<thead>
<tr>
<th><strong>Element</strong></th>
<th><strong>Object Hierarchy</strong></th>
<th><strong>Name</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Security Zone - Trust</td>
<td>[ security zones security-zone ]</td>
<td>trust</td>
</tr>
<tr>
<td>Security Zone - Untrust</td>
<td>[ security zones security-zone ]</td>
<td>untrust</td>
</tr>
<tr>
<td>Security Zone - Cloudflare WAN</td>
<td>[ security zones security-zone ]</td>
<td>cloudflare</td>
</tr>
<tr>
<td>IKE Proposal (only one required)</td>
<td>[ security ike proposal ]</td>
<td>ike-aes256cbc-sha256-dh20</td>
</tr>
<tr>
<td>IKE Policy - Tunnel 1</td>
<td>[ security ike policy ]</td>
<td>cf-wan-ike-pol-01</td>
</tr>
<tr>
<td>IKE Policy - Tunnel 2</td>
<td>[ security ike policy ]</td>
<td>cf-wan-ike-pol-02</td>
</tr>
<tr>
<td>IKE Gateway - Tunnel 1</td>
<td>[ security ike gateway ]</td>
<td>cf-wan-ike-gw-01</td>
</tr>
<tr>
<td>IKE Gateway - Tunnel 2</td>
<td>[ security ike gateway ]</td>
<td>cf-wan-ike-gw-02</td>
</tr>
<tr>
<td>IPsec Proposal (only one required)</td>
<td>[ security ipsec proposal ]</td>
<td>esp-aes256cbc-sha256-128</td>
</tr>
<tr>
<td>IPsec Policy (only one required)</td>
<td>[ security ipsec policy ]</td>
<td>ipsec-aes256cbc-sha256-128-dh20</td>
</tr>
<tr>
<td>IPsec Tunnel - Tunnel 1</td>
<td>[ security ipsec vpn ]</td>
<td>cf-wan-ipsec-vpn-01</td>
</tr>
<tr>
<td>IPsec Tunnel - Tunnel 2</td>
<td>[ security ipsec vpn ]</td>
<td>cf-wan-ipsec-vpn-02</td>
</tr>
</tbody>
</table>
<h2 id="assumptions">Assumptions</h2>
<p>This guide assumes the following apply:</p>
<ul>
<li>Already configured <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">IPsec tunnels</a> and <a href="/cloudflare-wan/configuration/how-to/configure-routes/">static routes</a> in the Cloudflare dashboard</li>
<li>Used the Cloudflare Dashboard to obtain the Local Identifier (FQDN/hostname) and generate a Pre-Shared Key for each of the IPsec tunnels</li>
<li>Understand the importance of <a href="/cloudflare-wan/reference/mtu-mss/#mss-clamping">MSS clamping</a> and adjusting it based on the traffic flows traversing the Cloudflare WAN IPsec Tunnels</li>
</ul>
<h2 id="high-level-steps">High-Level Steps</h2>
<ul>
<li>Add Virtual Tunnel Interfaces</li>
<li>Create a Security Zone (Recommended)</li>
<li>Add VTIs to Security Zone</li>
<li>Define IKE Policy and Proposals (Phase 1)</li>
<li>Add IKE Gateways</li>
<li>IPsec Policy and Proposal (Phase 2)</li>
<li>IPsec Tunnel Configuration</li>
<li>Define Security policy to permit traffic to/from Cloudflare WAN</li>
<li>Define Policy-Based Forwarding rules to selectively route traffic across the IPsec tunnels</li>
</ul>
<h2 id="hpe-juniper-networking-srx-configuration">HPE Juniper Networking SRX - Configuration</h2>
<p>All examples are provided via the Junos Command-Line Interface (CLI). J-Web examples are not provided.</p>
<h3 id="junos-modes">Junos Modes</h3>
<p>Junos OS operates with two main command-line interface (CLI) modes, Operational Mode and Configuration Mode, which serve distinct purposes in managing Juniper network devices.</p>
<h4 id="operational-mode">Operational Mode (&gt;)</h4>
<p><a href="https://www.juniper.net/documentation/us/en/software/junos/cli/topics/topic-map/junos-cli-operational-overview.html">Operational mode</a> is the default state upon logging into a Junos device, used for monitoring, troubleshooting, and displaying device status.</p>
<ul>
<li>Prompt: <code>user@host&gt;</code></li>
<li>Purpose: View real-time information, check interface status, view routing tables, test connectivity (ping/traceroute), and restart processes.</li>
<li>Key Commands: show, monitor, ping, traceroute, request.</li>
<li>Action: Changes made here do not affect the persistent device configuration.</li>
</ul>
<h4 id="configuration-mode">Configuration Mode (#)</h4>
<p><a href="https://www.juniper.net/documentation/us/en/software/junos/cli/topics/topic-map/cli-configuration.html">Configuration mode</a> is used to make changes to the device's configuration, such as defining interfaces, routing protocols, and system properties.</p>
<ul>
<li>Prompt: <code>user@host#</code></li>
<li>Purpose: Edit, add, or remove configuration statements.</li>
<li>Key Commands: edit, set, delete, commit, rollback.</li>
<li>Action: Changes are made to a &quot;candidate configuration&quot; and are not active until explicitly committed at which point they become part of the &quot;running configuration&quot;.</li>
</ul>
<p>Each section will indicate whether the commands are applicable to configuration mode or operational mode.</p>
<h3 id="virtual-tunnel-interfaces">Virtual Tunnel Interfaces</h3>
<p><em>Perform in Configuration Mode</em></p>
<pre tabindex="0"><code class="language-txt">set interfaces st0 unit 1 family inet address 169.254.250.1/31&#10;set interfaces st0 unit 2 family inet address 169.254.250.3/31&#10;</code></pre>
<h3 id="security-zone">Security Zone</h3>
<p><em>Perform in Configuration Mode</em></p>
<p>Add <code>st0.1</code> and <code>st0.2</code> to the Security Zone <code>cloudflare</code> and permit <code>system-services ping</code>. This is required to ensure the Cloudflare WAN IPsec Tunnel Health Checks are able to verify reachability across the Virtual Tunnel Interfaces.</p>
<pre tabindex="0"><code class="language-txt">set security zones security-zone cloudflare interfaces st0.1 host-inbound-traffic system-services ping&#10;set security zones security-zone cloudflare interfaces st0.2 host-inbound-traffic system-services ping&#10;</code></pre>
<h3 id="ike-phase-1">IKE - Phase 1</h3>
<p><em>Perform in Configuration Mode</em></p>
<p>Configure the following:</p>
<ul>
<li>IKE Proposal</li>
<li>IKE Policies (one required per Cloudflare WAN IPsec Tunnel)</li>
<li>IKE Gateways (one required per Cloudflare WAN IPsec Tunnel)</li>
</ul>
<h4 id="ike-proposal">IKE Proposal</h4>
<p>Define an IKE Proposal with the following settings:</p>
<table>
<thead>
<tr>
<th><strong>Attribute</strong></th>
<th><strong>Value</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>authentication-method</td>
<td>pre-shared-keys</td>
</tr>
<tr>
<td>dh-group</td>
<td>group20</td>
</tr>
<tr>
<td>authentication-algorithm</td>
<td>sha256</td>
</tr>
<tr>
<td>encryption-algorithm</td>
<td>aes-256-cbc</td>
</tr>
<tr>
<td>lifetime-seconds</td>
<td>28800</td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code class="language-txt">set security ike proposal ike-aes256cbc-sha256-dh20 authentication-method pre-shared-keys&#10;set security ike proposal ike-aes256cbc-sha256-dh20 dh-group group20&#10;set security ike proposal ike-aes256cbc-sha256-dh20 authentication-algorithm sha-256&#10;set security ike proposal ike-aes256cbc-sha256-dh20 encryption-algorithm aes-256-cbc&#10;set security ike proposal ike-aes256cbc-sha256-dh20 lifetime-seconds 28800&#10;</code></pre>
<h4 id="ike-policies">IKE Policies</h4>
<p>Configure one IKE policy per IPsec tunnel:</p>
<table>
<thead>
<tr>
<th><strong>Attribute</strong></th>
<th><strong>Value</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>mode</td>
<td>main</td>
</tr>
<tr>
<td>proposals</td>
<td>ike-aes256cbc-sha256-dh20</td>
</tr>
<tr>
<td>pre-shared-key ascii-text</td>
<td><em>specify pre-shared-key</em></td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code class="language-txt">set security ike policy cf-wan-ike-pol-01 mode main&#10;set security ike policy cf-wan-ike-pol-01 proposals ike-aes256cbc-sha256-dh20&#10;set security ike policy cf-wan-ike-pol-01 pre-shared-key ascii-text &quot;Cloudflare-WAN-T1-PSK-1234!&quot;&#10;&#10;set security ike policy cf-wan-ike-pol-02 mode main&#10;set security ike policy cf-wan-ike-pol-02 proposals ike-aes256cbc-sha256-dh20&#10;set security ike policy cf-wan-ike-pol-02 pre-shared-key ascii-text &quot;Cloudflare-WAN-T2-PSK-1234!&quot;&#10;</code></pre>
<h4 id="ike-gateways">IKE Gateways</h4>
<p>Configure one IKE Gateway per IPsec tunnel:</p>
<pre tabindex="0"><code class="language-txt">set security ike gateway cf-wan-ike-gw-01 ike-policy cf-wan-ike-pol-01&#10;set security ike gateway cf-wan-ike-gw-01 address 162.159.135.1&#10;set security ike gateway cf-wan-ike-gw-01 local-identity hostname bf6c493d03&lt;REDACTED&gt;.ipsec.cloudflare.com&#10;set security ike gateway cf-wan-ike-gw-01 external-interface ge-0/0/0.0&#10;set security ike gateway cf-wan-ike-gw-01 local-address 203.0.113.100&#10;set security ike gateway cf-wan-ike-gw-01 version v2-only&#10;&#10;set security ike gateway cf-wan-ike-gw-02 ike-policy cf-wan-ike-pol-02&#10;set security ike gateway cf-wan-ike-gw-02 address 172.64.135.1&#10;set security ike gateway cf-wan-ike-gw-02 local-identity hostname 0287844e9d&lt;REDACTED&gt;.ipsec.cloudflare.com&#10;set security ike gateway cf-wan-ike-gw-02 external-interface ge-0/0/0.0&#10;set security ike gateway cf-wan-ike-gw-02 local-address 203.0.113.100&#10;set security ike gateway cf-wan-ike-gw-02 version v2-only&#10;</code></pre>
<h3 id="ipsec-phase-2">IPsec - Phase 2</h3>
<p><em>Perform in Configuration Mode</em></p>
<p>Configure the following:</p>
<ul>
<li>IPsec Proposal</li>
<li>IPsec Policy</li>
<li>IPsec Tunnels (one required per Cloudflare WAN IPsec Tunnel)</li>
</ul>
<h4 id="ipsec-proposal">IPsec Proposal</h4>
<p>Define an IPsec Proposal with the following settings:</p>
<table>
<thead>
<tr>
<th><strong>Attribute</strong></th>
<th><strong>Value</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>protocol</td>
<td>esp</td>
</tr>
<tr>
<td>authentication-algorithm</td>
<td>hmac-sha-256-128</td>
</tr>
<tr>
<td>encryption-algorithm</td>
<td>aes-256-cbc</td>
</tr>
<tr>
<td>lifetime-seconds</td>
<td>28800</td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code class="language-txt">set security ipsec proposal esp-aes256cbc-sha256-128 protocol esp&#10;set security ipsec proposal esp-aes256cbc-sha256-128 authentication-algorithm hmac-sha-256-128&#10;set security ipsec proposal esp-aes256cbc-sha256-128 encryption-algorithm aes-256-cbc&#10;set security ipsec proposal esp-aes256cbc-sha256-128 lifetime-seconds 28800&#10;</code></pre>
<h4 id="ipsec-policy">IPsec Policy</h4>
<pre tabindex="0"><code class="language-txt">set security ipsec policy ipsec-aes256cbc-sha256-128-dh20 perfect-forward-secrecy keys group20&#10;set security ipsec policy ipsec-aes256cbc-sha256-128-dh20 proposals esp-aes256cbc-sha256-128&#10;</code></pre>
<h4 id="ipsec-vpn-tunnels">IPsec VPN Tunnels</h4>
<p>Create two IPsec VPN tunnels - each corresponding to its respective IKE Gateway.</p>
<pre tabindex="0"><code class="language-txt">set security ipsec vpn cf-wan-ipsec-vpn-01 bind-interface st0.1&#10;set security ipsec vpn cf-wan-ipsec-vpn-01 ike gateway cf-wan-ike-gw-01&#10;set security ipsec vpn cf-wan-ipsec-vpn-01 ike no-anti-replay&#10;set security ipsec vpn cf-wan-ipsec-vpn-01 ike ipsec-policy ipsec-aes256cbc-sha256-128-dh20&#10;set security ipsec vpn cf-wan-ipsec-vpn-01 establish-tunnels immediately&#10;&#10;set security ipsec vpn cf-wan-ipsec-vpn-02 bind-interface st0.2&#10;set security ipsec vpn cf-wan-ipsec-vpn-02 ike gateway cf-wan-ike-gw-02&#10;set security ipsec vpn cf-wan-ipsec-vpn-02 ike no-anti-replay&#10;set security ipsec vpn cf-wan-ipsec-vpn-02 ike ipsec-policy ipsec-aes256cbc-sha256-128-dh20&#10;set security ipsec vpn cf-wan-ipsec-vpn-02 establish-tunnels immediately&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6837.md")
</aside>
<h3 id="mss-clamping">MSS Clamping</h3>
<p><em>Perform in Configuration Mode</em></p>
<p>The SRX platform is unique in that it allows you to configure MSS Clamping that only applies to IPsec tunnels as opposed to per interface or globally.</p>
<p>This ensures the overhead associated with IKE/IPsec packet headers is factored in and will minimize opportunities for fragmentation as traffic ingresses and egresses the IPsec tunnels.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6836.md")
</aside>
<pre tabindex="0"><code class="language-txt">set security flow tcp-mss ipsec-vpn mss 1360&#10;</code></pre>
<p>See <a href="https://supportportal.juniper.net/s/article/SRX-How-to-change-the-MSS-of-TCP-traffic-passing-through-an-IPsec-VPN">How to change the MSS of TCP traffic passing through an IPsec VPN</a> for more details.</p>
<h3 id="security-policies">Security Policies</h3>
<p><em>Perform in Configuration Mode</em></p>
<ul>
<li>Security policies are required to permit traffic between zones</li>
<li>The Ethernet interface <code>ge-0/0/1.0</code> is in the <code>trust</code> security zone</li>
<li>The tunnel interfaces <code>st0.1</code> and <code>st0.2</code> are in the <code>cloudflare</code> security zone</li>
</ul>
<p>The following example allows all source &amp; destination IPs, ports, and protocols/services between <code>cloudflare</code> and <code>trust</code> as well as between <code>trust</code> and <code>cloudflare</code>.</p>
<table>
<thead>
<tr>
<th><strong>Attribute</strong></th>
<th><strong>Value</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>source-address</td>
<td>any</td>
</tr>
<tr>
<td>destination-address</td>
<td>any</td>
</tr>
<tr>
<td>application</td>
<td>any</td>
</tr>
<tr>
<td>action</td>
<td>permit</td>
</tr>
<tr>
<td>log</td>
<td>session-close</td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code class="language-txt">set security policies from-zone cloudflare to-zone trust policy cloudflare-to-trust-permit match source-address any&#10;set security policies from-zone cloudflare to-zone trust policy cloudflare-to-trust-permit match destination-address any&#10;set security policies from-zone cloudflare to-zone trust policy cloudflare-to-trust-permit match application any&#10;set security policies from-zone cloudflare to-zone trust policy cloudflare-to-trust-permit then permit&#10;set security policies from-zone cloudflare to-zone trust policy cloudflare-to-trust-permit then log session-close&#10;&#10;set security policies from-zone trust to-zone cloudflare policy trust-to-cloudflare-permit match source-address any&#10;set security policies from-zone trust to-zone cloudflare policy trust-to-cloudflare-permit match destination-address any&#10;set security policies from-zone trust to-zone cloudflare policy trust-to-cloudflare-permit match application any&#10;set security policies from-zone trust to-zone cloudflare policy trust-to-cloudflare-permit then permit&#10;set security policies from-zone trust to-zone cloudflare policy trust-to-cloudflare-permit then log session-close&#10;</code></pre>
<h3 id="filter-based-forwarding-policy-based-routing">Filter-Based Forwarding - Policy-Based Routing</h3>
<p><em>Perform in Configuration Mode</em></p>
<p>HPE Juniper Networking provides multiple methods for performing Policy-Based Routing. <a href="https://www.juniper.net/documentation/us/en/software/junos/routing-policy/topics/concept/firewall-filter-option-filter-based-forwarding-overview.html">Filter-Based Forwarding</a> is the preferred method as it permits selectively routing traffic based on source, destination, protocol (and a wide variety of other matching criteria) through Cloudflare WAN or local Internet breakout with ease.</p>
<p>This example assumes traffic originating from 192.168.125.0/24 (ingress interface <code>ge-0/0/1.0</code> zone <code>trust</code>) to any destination will be routed via the Cloudflare WAN IPsec Tunnels.</p>
<p>Implementing Filter-Based Forwarding (FBF) requires four steps:</p>
<ol>
<li>Create a Forwarding Routing Instance
<ul>
<li>Think of the Routing Instance as a &quot;bucket&quot; containing an alternate routing table</li>
<li>The Routing Instance contains the destination prefix(es) and next hop addresses (VTI on Cloudflare side of the tunnels)</li>
</ul>
</li>
<li>Create a Firewall Filter
<ul>
<li>Think of a Firewall Filter as the &quot;brain&quot; that determines which packets to send to the &quot;bucket&quot;</li>
<li>The Firewall Filter acts as a &quot;classifier&quot; that identifies the traffic you want to divert to the Routing Instance</li>
</ul>
</li>
<li>Configure the RIB Group and Bind Routes
<ul>
<li>Think of this as the &quot;bridge&quot; that copies interface routes to the &quot;bucket&quot;</li>
<li>The Routing Instance is not part of the default routing table.</li>
<li>This step instructs the SRX how to reach directly connected networks and resolve next-hops found in the main table (<code>inet.0</code>) and the Cloudflare WAN Routing Instance's routing table <code>CF_WAN_RI.inet.0</code></li>
</ul>
</li>
<li>Apply the Firewall Filter to the ingress traffic interface(s)
<ul>
<li>Think of this as the &quot;trigger&quot; that starts processing packets as they enter the ingress interface</li>
<li>As traffic ingresses the interface(s) to which it is applied, traffic is processed in a top-down fashion</li>
</ul>
</li>
</ol>
<h4 id="define-a-routing-instance">Define a Routing Instance</h4>
<p>The Routing Instance defines the destination for your steered traffic. Unlike a standard VRF, FBF typically uses an instance type of <code>forwarding</code>.</p>
<p>This example effectively sets the default gateway (0.0.0.0/0) for any traffic landing on this Routing Instance to get routed to the IP address of the VTIs on the Cloudflare side of the IPsec tunnels:</p>
<pre tabindex="0"><code class="language-txt">set routing-instances CF_WAN_RI instance-type forwarding&#10;set routing-instances CF_WAN_RI routing-options static route 0.0.0.0/0 next-hop 169.254.250.0&#10;set routing-instances CF_WAN_RI routing-options static route 0.0.0.0/0 next-hop 169.254.250.2&#10;</code></pre>
<h4 id="create-a-firewall-filter">Create a Firewall Filter</h4>
<p>Add a firewall filter called <code>CF_WAN_FBF_ALL</code> with two <code>terms</code> (rules):</p>
<p>The first term <code>CF_WAN_FWD_RI</code> ensures any traffic originating from the LAN subnet (192.168.125.0/24) to any destination address (0.0.0.0/0) is processed against the <code>CF_WAN_RI</code> routing instance.</p>
<p>The second term <code>EVERYTHING_ELSE</code> effectively instructs the SRX to continue processing any traffic not matching the term <code>CF_WAN_FWD_RI</code> via the default routing table (<code>inet.0</code>).</p>
<p>Note the addition of the action <code>count</code> in both statements. This option defines a counter you can view to determine how many packets are processed on each <code>term</code>.</p>
<pre tabindex="0"><code class="language-txt">set firewall family inet filter CF_WAN_FBF_ALL term CF_WAN_FWD_RI from source-address 192.168.125.0/24&#10;set firewall family inet filter CF_WAN_FBF_ALL term CF_WAN_FWD_RI from destination-address 0.0.0.0/0&#10;set firewall family inet filter CF_WAN_FBF_ALL term CF_WAN_FWD_RI then count CF_WAN_FWD_RI_count&#10;set firewall family inet filter CF_WAN_FBF_ALL term CF_WAN_FWD_RI then routing-instance CF_WAN_RI&#10;set firewall family inet filter CF_WAN_FBF_ALL term EVERYTHING_ELSE then count EVERYTHING_ELSE_count&#10;set firewall family inet filter CF_WAN_FBF_ALL term EVERYTHING_ELSE then accept&#10;</code></pre>
<h4 id="configure-the-rib-group-and-bind-interface-routes">Configure the RIB Group and Bind Interface Routes</h4>
<p>Create a RIB Group and import both the default route table (<code>inet.0</code>) and the route table associated with the newly created Forwarding Routing Instance:</p>
<pre tabindex="0"><code class="language-txt">set routing-options rib-groups CF_WAN_RG import-rib inet.0&#10;set routing-options rib-groups CF_WAN_RG import-rib CF_WAN_RI.inet.0&#10;</code></pre>
<p>Bind the RIB Group to the Interface Routes:</p>
<pre tabindex="0"><code class="language-txt">set routing-options interface-routes rib-group inet CF_WAN_RG&#10;</code></pre>
<h4 id="apply-the-firewall-filter-to-the-ingress-interface">Apply the Firewall Filter to the Ingress Interface</h4>
<ul>
<li>Traffic originating on the LAN subnet will ingress interface <code>ge-0/0/1.0</code></li>
<li>Apply the Firewall Filter <code>CF_WAN_FBF_ALL</code> as an <code>input</code> filter</li>
</ul>
<pre tabindex="0"><code class="language-txt">set interfaces ge-0/0/1 unit 0 family inet filter input CF_WAN_FBF_ALL&#10;</code></pre>
<p>Commit changes, then test traffic from a host on the 192.168.125.0/24 subnet to ensure it is forwarded through the Cloudflare WAN IPsec Tunnels.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6835.md")
</aside>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="common-issues">Common issues</h3>
<ul>
<li>Always check IKE Phase 1 &amp; IPsec Phase 2 negotiated successfully - look for &quot;no proposal chosen&quot; in logs</li>
<li>Verify Pre-Shared-Key and/or Local-Identity values are accurate and assigned to the correct tunnel</li>
<li>Use ping to determine reachability between the CPE and Cloudflare sides of the VTI
<ul>
<li>Tunnel 1: CPE VTI to Cloudflare VTI: <code>ping source 169.254.250.1 169.254.250.0</code></li>
<li>Tunnel 2: CPE VTI to Cloudflare VTI: <code>ping source 169.254.250.3 169.254.250.2</code></li>
</ul>
</li>
</ul>
<h3 id="view-ike-security-associations">View IKE Security Associations</h3>
<p><em>Perform in Operational Mode</em></p>
<p>Use the CLI to verify IKE (Phase 1) and IPsec (Phase 2) security associations established.</p>
<pre tabindex="0"><code class="language-txt">admin@srx&gt; show security ike security-associations&#10;Index   State  Initiator cookie  Responder cookie  Mode           Remote Address&#10;403838  UP     a2d16e54c9d83ad5  873b1da714f0ca8f  IKEv2          162.159.135.1&#10;403839  UP     476288ac95d878e2  e72ef64e00b623e6  IKEv2          172.64.135.1&#10;</code></pre>
<h3 id="view-ipsec-security-associations">View IPsec Security Associations</h3>
<p><em>Perform in Operational Mode</em></p>
<pre tabindex="0"><code class="language-txt">admin@srx&gt; show ipsec security associations&#10;  Total active tunnels: 2&#10;  ID    Algorithm       SPI      Life:sec/kb  Mon lsys Port  Gateway&#10;  &lt;131073 ESP:aes-cbc-256/sha256-96 9b429dd3 27739/unlim - root 500 162.159.135.1&#10;  &gt;131073 ESP:aes-cbc-256/sha256-96 28931d57 27739/unlim - root 500 162.159.135.1&#10;  &lt;131074 ESP:aes-cbc-256/sha256-96 eb2a275e 27739/unlim - root 500 172.64.135.1&#10;  &gt;131074 ESP:aes-cbc-256/sha256-96 4134d7a8 27739/unlim - root 500 172.64.135.1&#10;</code></pre>
<h3 id="enable-debug-logging-traceoptions-for-ike-phase-1-and-ipsec-phase-2">Enable Debug Logging (traceoptions) for IKE (Phase 1) and IPsec (Phase 2)</h3>
<p>In the event you encounter issues with IPsec tunnel negotiation, you can enable <code>traceoptions</code> for IKE and/or IPsec.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6834.md")
</aside>
<h4 id="enable-ike-traceoptions">Enable IKE Traceoptions</h4>
<p><em>Perform in Configuration Mode</em></p>
<pre tabindex="0"><code class="language-txt">set security ike traceoptions file ike-debug.log&#10;set security ike traceoptions file size 1m&#10;set security ike traceoptions file files 3&#10;set security ike traceoptions file world-readable&#10;set security ike traceoptions flag all&#10;</code></pre>
<h4 id="view-ike-debug-log">View IKE Debug Log</h4>
<p><em>Perform in Operational Mode</em></p>
<p>View the log with the following command:</p>
<pre tabindex="0"><code class="language-txt">admin@srx&gt; show log ike-debug.log&#10;</code></pre>
<p>Press <code>CTRL + C</code> to stop viewing the log.</p>
<h4 id="disable-ike-traceoptions">Disable IKE Traceoptions</h4>
<p><em>Perform in Configuration Mode</em></p>
<pre tabindex="0"><code class="language-txt">delete security ike traceoptions&#10;commit&#10;</code></pre>
<h4 id="enable-ipsec-traceoptions">Enable IPsec Traceoptions</h4>
<p><em>Perform in Configuration Mode</em></p>
<pre tabindex="0"><code class="language-txt">set security ipsec traceoptions file ipsec-debug.log&#10;set security ipsec traceoptions file size 1m&#10;set security ipsec traceoptions file files 3&#10;set security ipsec traceoptions file world-readable&#10;set security ipsec traceoptions flag all&#10;</code></pre>
<h4 id="view-ipsec-debug-logging">View IPsec Debug Logging</h4>
<p><em>Perform in Operational Mode</em></p>
<p>View the log with the following command:</p>
<pre tabindex="0"><code class="language-txt">admin@srx&gt; show log ipsec-debug.log&#10;</code></pre>
<p>Press <code>CTRL + C</code> to stop viewing the log.</p>
<h4 id="disable-ipsec-debug-logging">Disable IPsec Debug Logging</h4>
<p><em>Perform in Configuration Mode</em></p>
<pre tabindex="0"><code class="language-txt">delete security ipsec traceoptions&#10;commit&#10;</code></pre>
<h3 id="disable-enable-ike-gateways-and-or-ipsec-vpn-tunnels">Disable/Enable IKE Gateways and/or IPsec VPN Tunnels</h3>
<p><em>Perform in Configuration Mode</em></p>
<p>Junos provides the ability to administratively enable/disable IKE gateways and IPsec tunnels independently. This allows you to forcefully set up and tear down VPN tunnels which can be very useful during troubleshooting.</p>
<h4 id="deactivate-ike-gateway">Deactivate IKE Gateway</h4>
<pre tabindex="0"><code class="language-txt">deactivate security ike gateway cf-wan-ike-gw-01&#10;</code></pre>
<h4 id="deactivate-ipsec-vpn">Deactivate IPsec VPN</h4>
<pre tabindex="0"><code class="language-txt">deactivate security ipsec vpn cf-wan-ipsec-vpn-01&#10;</code></pre>
<p>Perform a <code>commit</code> to ensure the IKE Gateway and IPSec VPN objects are disabled.</p>
<h4 id="verify-inactive-state">Verify Inactive State</h4>
<p>Note the presence of <code>inactive: security ike gateway cf-wan-ike-gw-01</code> at the top of the IKE gateway stanza:</p>
<pre tabindex="0"><code class="language-txt">admin@srx# show security ike gateway cf-wan-ike-gw-01&#10;&#35;#&#10;&#35;# inactive: security ike gateway cf-wan-ike-gw-01&#10;&#35;#&#10;ike-policy cf-wan-ike-pol-01;&#10;address 162.159.135.1;&#10;local-identity hostname bf6c493d03&lt;REDACTED&gt;.ipsec.cloudflare.com;&#10;external-interface ge-0/0/0.0;&#10;local-address 203.0.113.100;&#10;version v2-only;&#10;</code></pre>
<p>Note the presence of <code>inactive: security ipsec vpn cf-wan-ike-gw-01</code> at the top of the IPsec VPN stanza:</p>
<pre tabindex="0"><code class="language-txt">[edit]&#10;admin@srx# show security ipsec vpn cf-wan-ipsec-vpn-01&#10;&#35;#&#10;&#35;# inactive: security ipsec vpn cf-wan-ipsec-vpn-01&#10;&#35;#&#10;bind-interface st0.1;&#10;ike {&#10;    gateway cf-wan-ike-gw-01;&#10;    no-anti-replay;&#10;    ipsec-policy ipsec-aes256cbc-sha256-128-dh20;&#10;}&#10;establish-tunnels immediately;&#10;</code></pre>
<h4 id="activate-ike-gateway-and-ipsec-vpn-objects">Activate IKE Gateway and IPsec VPN Objects</h4>
<p>Reverse the process with the <code>activate</code> command:</p>
<pre tabindex="0"><code class="language-txt">activate security ike gateway cf-wan-ike-gw-01&#10;&#10;activate security ipsec vpn cf-wan-ipsec-vpn-01&#10;&#10;commit&#10;</code></pre>
<h3 id="restart-ipsec-daemon">Restart IPsec Daemon</h3>
<p><em>Perform in Operational Mode</em></p>
<p>The IKE and IPsec lifetimes are set to 28800 seconds (8 hours). You can force tunnel establishment by restarting the IPsec daemon (kmd). This will invalidate the IKE and IPsec security associations and forcefully reconnect the IPsec VPN tunnels.</p>
<p>This can be accomplished with the following command:</p>
<pre tabindex="0"><code class="language-txt">admin@srx&gt; restart ipsec-key-management&#10;</code></pre>
<h3 id="ensure-reachability-across-ipsec-tunnels">Ensure Reachability Across IPsec Tunnels</h3>
<p><em>Perform in Operational Mode</em></p>
<p>Use ping to verify connectivity to the Cloudflare side of the Virtual Tunnel Interface</p>
<pre tabindex="0"><code class="language-txt">admin@srx&gt; ping 169.254.250.0 source 169.254.250.1&#10;admin@srx&gt; ping 169.254.250.2 source 169.254.250.3&#10;</code></pre>
<h3 id="show-tunnel-event-statistics">Show Tunnel Event Statistics</h3>
<p><em>Perform in Operational Mode</em></p>
<pre tabindex="0"><code class="language-txt">admin@srx&gt; show security ipsec tunnel-events-statistics&#10;</code></pre>
<p>Resulting output:</p>
<pre tabindex="0"><code class="language-txt">External interface&#x27;s zone received. Information updated                     : 2&#10;Bind-interface&#x27;s zone received. Information updated                         : 2&#10;Bind-interface&#x27;s address received. Information updated                      : 2&#10;IKE SA negotiation successfully completed                                   : 2&#10;IPSec SA negotiation successfully completed                                 : 2&#10;Tunnel is ready. Waiting for trigger event or peer to trigger negotiation   : 2&#10;</code></pre>
<h3 id="display-route-tables">Display Route Tables</h3>
<p><em>Perform in Operational Mode</em></p>
<h4 id="default-route-table-inet-0">Default Route Table - inet.0</h4>
<pre tabindex="0"><code class="language-txt">show route table inet.0&#10;&#10;inet.0: 11 destinations, 11 routes (11 active, 0 holddown, 0 hidden)&#10;&#43; = Active Route, - = Last Active, * = Both&#10;&#10;169.254.247.0/31   *[Direct/0] 00:02:10&#10;                    &gt; via st0.1&#10;169.254.247.1/32   *[Local/0] 1d 05:35:54&#10;                      Local via st0.1&#10;169.254.247.2/31   *[Direct/0] 00:02:09&#10;                    &gt; via st0.2&#10;169.254.247.3/32   *[Local/0] 1d 05:35:54&#10;                      Local via st0.2&#10;169.254.250.0/31   *[Direct/0] 00:02:09&#10;                    &gt; via st0.1&#10;169.254.250.1/32   *[Local/0] 00:02:09&#10;                      Local via st0.1&#10;169.254.250.2/31   *[Direct/0] 00:02:09&#10;                    &gt; via st0.2&#10;169.254.250.3/32   *[Local/0] 00:02:09&#10;                      Local via st0.2&#10;192.168.125.0/24   *[Direct/0] 00:02:10&#10;                    &gt; via ge-0/0/1.0&#10;192.168.125.1/32   *[Local/0] 00:02:10&#10;                      Local via ge-0/0/1.0&#10;203.0.113.100/32   *[Local/0] 00:02:10&#10;                      Reject&#10;</code></pre>
<h4 id="routing-instance-route-table-cf-wan-ri-inet-0">Routing Instance Route Table (CF_WAN_RI.inet.0)</h4>
<pre tabindex="0"><code class="language-txt">show route table CF_WAN_RI.inet.0&#10;&#10;CF_WAN_RI.inet.0: 12 destinations, 12 routes (12 active, 0 holddown, 0 hidden)&#10;&#43; = Active Route, - = Last Active, * = Both&#10;&#10;0.0.0.0/0          *[Static/5] 00:01:04&#10;                    &gt; to 169.254.250.0 via st0.1&#10;                      to 169.254.250.2 via st0.2&#10;169.254.247.0/31   *[Direct/0] 00:02:58&#10;                    &gt; via st0.1&#10;169.254.247.1/32   *[Local/0] 00:02:58&#10;                      Local via st0.1&#10;169.254.247.2/31   *[Direct/0] 00:02:57&#10;                    &gt; via st0.2&#10;169.254.247.3/32   *[Local/0] 00:02:57&#10;                      Local via st0.2&#10;169.254.250.0/31   *[Direct/0] 00:02:57&#10;                    &gt; via st0.1&#10;169.254.250.1/32   *[Local/0] 00:02:57&#10;                      Local via st0.1&#10;169.254.250.2/31   *[Direct/0] 00:02:57&#10;                    &gt; via st0.2&#10;169.254.250.3/32   *[Local/0] 00:02:57&#10;                      Local via st0.2&#10;192.168.125.0/24   *[Direct/0] 00:02:58&#10;                    &gt; via ge-0/0/1.0&#10;192.168.125.1/32   *[Local/0] 00:02:58&#10;                      Local via ge-0/0/1.0&#10;203.0.113.100/32   *[Local/0] 00:02:58&#10;                      Reject&#10;</code></pre>
<h3 id="display-firewall-filter-counters">Display Firewall Filter Counters</h3>
<pre tabindex="0"><code class="language-txt">admin@srx&gt; show firewall counter filter CF_WAN_FBF_ALL CF_WAN_FWD_RI_count&#10;&#10;Filter: CF_WAN_FBF_ALL&#10;Counters:&#10;Name                                Bytes              Packets&#10;CF_WAN_FWD_RI_count                 14855935          189746&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">admin@srx&gt; show firewall counter filter CF_WAN_FBF_ALL EVERYTHING_ELSE_count&#10;&#10;Filter: CF_WAN_FBF_ALL&#10;Counters:&#10;Name                                Bytes              Packets&#10;EVERYTHING_ELSE_count               4371377            18732&#10;</code></pre>
<h2 id="resources-juniper-product-documentation">Resources - Juniper Product Documentation</h2>
<p>Refer to the CLI Reference Guide for further details on each command referenced within this document:</p>
<ul>
<li>
<p><a href="https://www.juniper.net/documentation/us/en/software/junos/cli-reference/">CLI Reference Guide</a></p>
</li>
<li>
<p><a href="https://www.juniper.net/documentation/us/en/software/junos/vpn-ipsec/topics/topic-map/security-route-based-ipsec-vpns.html">Route-Based IPsec VPNs</a></p>
</li>
<li>
<p><a href="https://www.juniper.net/documentation/us/en/software/junos/vpn-ipsec/topics/topic-map/security-vpns-for-ikev2.html">Route-Based VPN with IKEv2</a></p>
</li>
<li>
<p><a href="https://www.juniper.net/documentation/us/en/software/junos/vpn-ipsec/topics/topic-map/security-route-based-and-policy-based-vpns-with-nat-t.html">Route-Based and Policy-Based VPNs with NAT-T</a></p>
</li>
<li>
<p><a href="https://www.juniper.net/documentation/us/en/software/junos/routing-policy/topics/example/filter-based-forwarding-example.html">Configuring Filter-Based Forwarding</a></p>
</li>
</ul>
<h2 id="resources-juniper-knowledge-base">Resources - Juniper Knowledge Base</h2>
<p>Valid support credentials may be required to view some/all of the following documents:</p>
<ul>
<li>
<p><a href="https://supportportal.juniper.net/s/article/SRX-How-do-I-tell-if-a-VPN-Tunnel-SA-Security-Association-is-active">[SRX] How do I tell if a VPN Tunnel SA (Security Association) is active - KB10090</a></p>
</li>
<li>
<p><a href="https://supportportal.juniper.net/s/article/SRX-How-to-configure-syslog-to-display-VPN-status-messages">[SRX] How to configure syslog to display VPN status messages - KB10097</a></p>
</li>
<li>
<p><a href="https://supportportal.juniper.net/s/article/SRX-How-to-troubleshoot-IKE-Phase-2-VPN-connection-issues">[SRX] How to troubleshoot IKE Phase 2 VPN connection issues - KB10099</a></p>
</li>
<li>
<p><a href="https://supportportal.juniper.net/s/article/SRX-How-to-enable-VPN-IKE-IPsec-traceoptions-for-specific-SAs-Security-Associations">[SRX] How to enable VPN (IKE/IPsec) traceoptions for specific SAs (Security Associations) - KB19943</a></p>
</li>
</ul>
