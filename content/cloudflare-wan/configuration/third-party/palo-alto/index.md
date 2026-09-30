<h2 id="overview">Overview</h2>
<p>This guide provides step-by-step instructions for configuring Palo Alto Networks Next-Generation Firewall (NGFW) to establish IPsec VPN tunnels to Cloudflare WAN. The configuration has been validated by Cloudflare with the documented firmware release and is intended for network engineers who are familiar with Palo Alto Networks NGFW Firewalls administration and have an active Cloudflare WAN subscription.</p>
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
<td>Palo Alto Networks</td>
</tr>
<tr>
<td>Model</td>
<td>PA-440</td>
</tr>
<tr>
<td>Release</td>
<td>PAN-OS 11.2.8</td>
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
<h2 id="cloudflare-wan-and-palo-alto-networks-ngfw-configuration-settings">Cloudflare WAN and Palo Alto Networks NGFW - Configuration Settings</h2>
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
<h2 id="customer-premise-equipment-palo-alto-networks">Customer Premise Equipment - Palo Alto Networks</h2>
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
<td>ethernet1/1</td>
<td>ethernet1/1</td>
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
<td>tunnel.1</td>
<td>tunnel.2</td>
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
<td>ethernet1/2</td>
<td>ethernet1/2</td>
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
<h3 id="palo-alto-networks-ngfw-object-names">Palo Alto Networks NGFW Object Names</h3>
<table>
<thead>
<tr>
<th><strong>Role</strong></th>
<th><strong>Label/Name</strong></th>
<th><strong>Address</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>CPE Security Zone - Trust</td>
<td>Zone</td>
<td>trust</td>
</tr>
<tr>
<td>CPE Security Zone - Untrust</td>
<td>Zone</td>
<td>untrust</td>
</tr>
<tr>
<td>CPE Security Zone - Cloudflare WAN</td>
<td>Zone</td>
<td>cloudflare</td>
</tr>
<tr>
<td>CPE IKE Crypto Profile Name</td>
<td>IKE Crypto Profile</td>
<td>ike-aes256cbc-sha256-dh20</td>
</tr>
<tr>
<td>CPE IPsec Crypto Profile Name</td>
<td>IPsec Crypto Profile</td>
<td>ipsec-aes256cbc-sha256-dh20</td>
</tr>
</tbody>
</table>
<h2 id="assumptions">Assumptions</h2>
<p>This guide assumes the following apply:</p>
<ul>
<li>Already configured <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">IPsec tunnels</a> and <a href="/cloudflare-wan/configuration/how-to/configure-routes/">static routes</a> in the Cloudflare dashboard</li>
<li>Used the Cloudflare Dashboard to obtain the Local Identifier (FQDN/hostname) and generate a Pre-Shared Key for each of the IPsec tunnels</li>
<li>Understand the importance of <a href="/cloudflare-wan/reference/mtu-mss/#mss-clamping">MSS clamping</a> and adjusting it based on the traffic flows traversing the Cloudflare WAN IPsec Tunnels</li>
<li>Highly Available/Fault Tolerant Palo Alto Networks NGFW configurations, while possible, are out of scope.</li>
</ul>
<h2 id="high-level-steps">High-Level Steps</h2>
<ul>
<li>Create Address Objects for:
<ul>
<li>Virtual Tunnel Interfaces (2x) - Local (/31 netmask) and Remote (/32 netmask)</li>
<li>Cloudflare Anycast IPs (2x)</li>
<li>Local Subnet(s)</li>
<li>Remote Cloudflare WAN Subnet(s)</li>
</ul>
</li>
<li>Create Interface Management Profile</li>
<li>Create a Security Zone (Recommended)</li>
<li>Define Tunnel interfaces</li>
<li>Define IKE and IPsec Crypto Profiles</li>
<li>Add two IKE Gateways - one for each of the two Cloudflare IPsec Tunnels</li>
<li>Add two IPsec Tunnels - one for each of the two Cloudflare IPsec Tunnels</li>
<li>Define Security policy to permit traffic to/from Cloudflare WAN</li>
<li>Define Policy-Based Forwarding rules to selectively route traffic across the IPsec tunnels</li>
</ul>
<h2 id="palo-alto-networks-ngfw-configuration">Palo Alto Networks NGFW - Configuration</h2>
<p>There are examples for both the Command-Line Interface (CLI) and Web UI wherever possible.</p>
<h3 id="objects-addressing">Objects &amp; Addressing</h3>
<p>Define Address Objects to represent the attribute/value pairs throughout the remainder of the configuration.</p>
<h4 id="cli">CLI</h4>
<pre><code class="language-txt">set address cf_wan_anycast_01 ip-netmask 162.159.135.1&#10;set address cf_wan_anycast_02 ip-netmask 172.64.135.1&#10;set address cf-wan-ipsec-vti-01-local ip-netmask 169.254.250.1/31&#10;set address cf-wan-ipsec-vti-02-local ip-netmask 169.254.250.3/31&#10;set address cf-wan-ipsec-vti-01-remote ip-netmask 169.254.250.0/32&#10;set address cf-wan-ipsec-vti-02-remote ip-netmask 169.254.250.2/32&#10;set address lan-net-192-168-125-0--24 ip-netmask 192.168.125.0/24&#10;set address internet_203-0-113-100--24 ip-netmask 203.0.113.100/24&#10;</code></pre>
<h4 id="web-ui">Web UI</h4>
<ol>
<li>Go to <strong>Objects</strong> &gt; <strong>Addresses</strong>.</li>
<li>Select <strong>Add</strong>.</li>
<li>Create objects of type <code>IP Netmask</code> for the following networks:
<ul>
<li><code>cf_wan_anycast_01</code> - specify 162.159.135.1 (or 162.159.135.1/32)</li>
<li><code>cf_wan_anycast_02</code> - specify 172.64.135.1 (or 172.64.135.1/32)</li>
<li><code>cf-wan-ipsec-vti-01-local</code> - specify 169.254.250.1/31</li>
<li><code>cf-wan-ipsec-vti-02-local</code> - specify 169.254.250.3/31</li>
<li><code>cf-wan-ipsec-vti-01-remote</code> - specify 169.254.250.0 (or 169.254.250.0/32)</li>
<li><code>cf-wan-ipsec-vti-02-remote</code> - specify 169.254.250.2 (or 169.254.250.2/32)</li>
</ul>
</li>
</ol>
<h3 id="interface-management-profile">Interface Management Profile</h3>
<p>Allow the applicable network interfaces to respond to pings (ICMP Echo Request). This is required to ensure the Cloudflare WAN Tunnel Health Checks are able to verify reachability across the Virtual Tunnel Interfaces.</p>
<h4 id="cli-1">CLI</h4>
<pre><code class="language-txt">set network profiles interface-management-profile allow_ping ping yes&#10;</code></pre>
<h4 id="web-ui-1">Web UI</h4>
<ol>
<li>Go to <strong>Network</strong> &gt; <strong>Network Profiles</strong> &gt; <strong>Interface Mgmt</strong>.</li>
<li>Select <strong>Add</strong>.</li>
<li>Name: <code>allow_ping</code></li>
<li>Select <code>Ping</code> under <code>Network Services</code>.</li>
<li>Select <strong>OK</strong>.</li>
</ol>
<h3 id="virtual-tunnel-interfaces-vtis">Virtual Tunnel Interfaces (VTIs)</h3>
<p>Add two tunnel interfaces - one for each of the two Cloudflare IPsec tunnels.</p>
<p>Note: The workflows for the CLI and Web UI can vary.</p>
<h4 id="cli-add-tunnel-interfaces">CLI - Add Tunnel Interfaces</h4>
<p>Add two tunnel interfaces taking advantage of the Address objects and Interface Management Profile configured earlier.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6832.md")
</aside>
<pre><code class="language-txt">set network interface tunnel units tunnel.1 ip cf-wan-ipsec-vti-01-local&#10;set network interface tunnel units tunnel.1 interface-management-profile allow_ping&#10;&#10;set network interface tunnel units tunnel.2 ip cf-wan-ipsec-vti-02-local&#10;set network interface tunnel units tunnel.2 interface-management-profile allow_ping&#10;</code></pre>
<h4 id="cli-assign-tunnel-interfaces-to-the-virtual-router">CLI - Assign Tunnel Interfaces to the Virtual Router</h4>
<p>Assign both <code>tunnel</code> interfaces to the default Virtual Router:</p>
<pre><code class="language-txt">set network virtual-router default interface tunnel.1&#10;set network virtual-router default interface tunnel.2&#10;</code></pre>
<h4 id="cli-assign-tunnel-interfaces-to-security-zone">CLI - Assign Tunnel Interfaces to Security Zone</h4>
<p>Create the <code>cloudflare</code> security zone if it does not already exist and bind <code>tunnel.1</code> and <code>tunnel.2</code> interfaces.</p>
<pre><code class="language-txt">set zone cloudflare network layer3  [ tunnel.1 tunnel.2 ]&#10;</code></pre>
<h4 id="web-ui-add-tunnel-interfaces">Web UI - Add Tunnel Interfaces</h4>
<ol>
<li>Go to <strong>Network</strong> &gt; <strong>Interfaces</strong> &gt; <strong>Tunnel</strong>.</li>
<li>Select <strong>Add</strong>.</li>
<li>Enter 1 in the field to the right of &quot;Interface Name&quot;.</li>
<li>Config Tab &gt; Virtual Router: <code>default</code>.</li>
<li>Config Tab &gt; Security Zone: <code>cloudflare</code> (or assign to <code>trust</code> based on your security policy).</li>
<li>IPv4 Tab &gt; Select <code>cf-wan-ipsec-vti-01-local</code> from the drop-down.</li>
<li>Advanced tab &gt; Management Profile: <code>allow_ping</code>.</li>
<li>Select <strong>OK</strong>.</li>
</ol>
<p>Repeat steps for tunnel 2</p>
<ol>
<li>Go to <strong>Network</strong> &gt; <strong>Interfaces</strong> &gt; <strong>Tunnel</strong>.</li>
<li>Select <strong>Add</strong>.</li>
<li>Enter 2 in the field to the right of &quot;Interface Name&quot;.</li>
<li>Config Tab &gt; Virtual Router: <code>default</code>.</li>
<li>Config Tab &gt; Security Zone: <code>cloudflare</code> (or assign to <code>trust</code> based on your security policy).</li>
<li>IPv4 Tab &gt; Select <code>cf-wan-ipsec-vti-02-local</code> from the drop-down.</li>
<li>Advanced tab &gt; Management Profile: <code>allow_ping</code>.</li>
<li>Select <strong>OK</strong>.</li>
</ol>
<h3 id="ipsec-tunnel-configuration">IPsec Tunnel Configuration</h3>
<h4 id="phase-1-ike">Phase 1 - IKE</h4>
<h5 id="define-cryptographic-settings">Define Cryptographic Settings</h5>
<p>Define an IKE Crypto Profile with the following settings:</p>
<table>
<thead>
<tr>
<th><strong>Attribute</strong></th>
<th><strong>Value</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>hash</td>
<td>sha256</td>
</tr>
<tr>
<td>dh-group</td>
<td>group20</td>
</tr>
<tr>
<td>encryption</td>
<td>aes-256-cbc</td>
</tr>
<tr>
<td>lifetime hours</td>
<td>8</td>
</tr>
</tbody>
</table>
<h6 id="cli-2">CLI</h6>
<pre><code class="language-txt">set network ike crypto-profiles ike-crypto-profiles ike-aes256cbc-sha256-dh20 hash sha256&#10;set network ike crypto-profiles ike-crypto-profiles ike-aes256cbc-sha256-dh20 dh-group group20&#10;set network ike crypto-profiles ike-crypto-profiles ike-aes256cbc-sha256-dh20 encryption aes-256-cbc&#10;set network ike crypto-profiles ike-crypto-profiles ike-aes256cbc-sha256-dh20 lifetime hours 8&#10;</code></pre>
<h6 id="web-ui-2">Web UI</h6>
<ol>
<li>Go to <strong>Network</strong> &gt; <strong>Network Profiles</strong> &gt; <strong>IKE Crypto</strong>.</li>
<li>Select <strong>Add</strong>.</li>
<li>Name: <code>ike-aes256cbc-sha256-dh20</code></li>
<li>DH Group: <code>group20</code></li>
<li>Authentication: <code>sha256</code></li>
<li>Encryption: <code>aes-256-cbc</code></li>
<li>Timers - Key Lifetime: 8 hours</li>
</ol>
<h5 id="define-ike-gateway-objects">Define IKE Gateway Objects</h5>
<p>Each tunnel will have its own Pre-Shared Key and Local ID (FQDN/hostname) - ensure you obtain/update the values from the Cloudflare Dashboard.</p>
<h6 id="cli-3">CLI</h6>
<pre><code class="language-txt">set network ike gateway cf-wan-ike-gw-01 authentication pre-shared-key key &quot;Cloudflare-WAN-T1-PSK-1234!&quot;&#10;set network ike gateway cf-wan-ike-gw-01 protocol ikev2 pq-ppk enabled no&#10;set network ike gateway cf-wan-ike-gw-01 protocol ikev2 pq-ppk negotiation-mode preferred&#10;set network ike gateway cf-wan-ike-gw-01 protocol ikev2 pq-kem enable no&#10;set network ike gateway cf-wan-ike-gw-01 protocol ikev2 pq-kem block-vulnerable-cipher yes&#10;set network ike gateway cf-wan-ike-gw-01 protocol ikev2 ikev2-fragment enable no&#10;set network ike gateway cf-wan-ike-gw-01 protocol ikev2 dpd enable yes&#10;set network ike gateway cf-wan-ike-gw-01 protocol ikev2 ike-crypto-profile ike-aes256cbc-sha256-dh20&#10;set network ike gateway cf-wan-ike-gw-01 protocol ikev1 dpd enable yes&#10;set network ike gateway cf-wan-ike-gw-01 protocol version ikev2&#10;set network ike gateway cf-wan-ike-gw-01 local-address interface ethernet1/1 ip internet_203-0-113-100--24&#10;set network ike gateway cf-wan-ike-gw-01 protocol-common nat-traversal enable no&#10;set network ike gateway cf-wan-ike-gw-01 protocol-common fragmentation enable no&#10;set network ike gateway cf-wan-ike-gw-01 peer-address ip cf_wan_anycast_01&#10;set network ike gateway cf-wan-ike-gw-01 local-id type fqdn id &quot;bf6c493d03&lt;REDACTED&gt;.ipsec.cloudflare.com&quot;&#10;&#10;set network ike gateway cf-wan-ike-gw-02 authentication pre-shared-key key &quot;Cloudflare-WAN-T2-PSK-1234!&quot;&#10;set network ike gateway cf-wan-ike-gw-02 protocol ikev2 pq-ppk enabled no&#10;set network ike gateway cf-wan-ike-gw-02 protocol ikev2 pq-ppk negotiation-mode preferred&#10;set network ike gateway cf-wan-ike-gw-02 protocol ikev2 pq-kem enable no&#10;set network ike gateway cf-wan-ike-gw-02 protocol ikev2 pq-kem block-vulnerable-cipher yes&#10;set network ike gateway cf-wan-ike-gw-02 protocol ikev2 ikev2-fragment enable no&#10;set network ike gateway cf-wan-ike-gw-02 protocol ikev2 dpd enable yes&#10;set network ike gateway cf-wan-ike-gw-02 protocol ikev2 ike-crypto-profile ike-aes256cbc-sha256-dh20&#10;set network ike gateway cf-wan-ike-gw-02 protocol ikev1 dpd enable yes&#10;set network ike gateway cf-wan-ike-gw-02 protocol version ikev2&#10;set network ike gateway cf-wan-ike-gw-02 local-address interface ethernet1/1 ip internet_203-0-113-100--24&#10;set network ike gateway cf-wan-ike-gw-02 protocol-common nat-traversal enable no&#10;set network ike gateway cf-wan-ike-gw-02 protocol-common fragmentation enable no&#10;set network ike gateway cf-wan-ike-gw-02 peer-address ip cf_wan_anycast_02&#10;set network ike gateway cf-wan-ike-gw-02 local-id type fqdn id &quot;0287844e9d&lt;REDACTED&gt;.ipsec.cloudflare.com&quot;&#10;</code></pre>
<h5 id="web-ui-3">Web UI</h5>
<ol>
<li>Go to <strong>Network</strong> &gt; <strong>Network Profiles</strong> &gt; <strong>IKE Gateways</strong>.</li>
<li>Select <strong>Add</strong>.</li>
<li>Name: <code>cf-wan-ike-gw-01</code></li>
<li>Version: <code>IKEv2 only mode</code></li>
<li>Address Type: <code>IPv4</code></li>
<li>Interface: <code>ethernet1/1</code></li>
<li>Local IP Address: <code>internet_203-0-113-100--24</code></li>
<li>Peer IP Address Type: <code>IP</code></li>
<li>Authentication: <code>Pre-Shared Key</code></li>
<li>Enter Pre-shared key and confirm value (obtain from the Cloudflare Dashboard).</li>
<li>Local Identification: <code>FQDN (hostname)</code> (obtain FQDN value for Tunnel 1 from the Cloudflare Dashboard).</li>
<li>Advanced Options tab &gt; General &gt; IKE Crypto Profile: <code>ike-aes256cbc-sha256-dh20</code>.</li>
<li>Select <strong>OK</strong>.</li>
</ol>
<p>Repeat steps for tunnel 2</p>
<ol>
<li>Go to <strong>Network</strong> &gt; <strong>Network Profiles</strong> &gt; <strong>IKE Gateways</strong>.</li>
<li>Select <strong>Add</strong>.</li>
<li>Name: <code>cf-wan-ike-gw-02</code></li>
<li>Version: <code>IKEv2 only mode</code></li>
<li>Address Type: <code>IPv4</code></li>
<li>Interface: <code>ethernet1/1</code></li>
<li>Local IP Address: <code>internet_203-0-113-100--24</code></li>
<li>Peer IP Address Type: <code>IP</code></li>
<li>Authentication: <code>Pre-Shared Key</code></li>
<li>Enter Pre-shared key and confirm value (obtain from the Cloudflare Dashboard).</li>
<li>Local Identification: <code>FQDN (hostname)</code> (obtain FQDN value for Tunnel 2 from the Cloudflare Dashboard).</li>
<li>Advanced Options tab &gt; General &gt; IKE Crypto Profile: <code>ike-aes256cbc-sha256-dh20</code>.</li>
<li>Select <strong>OK</strong>.</li>
</ol>
<h4 id="ipsec-phase-2">IPsec (Phase 2)</h4>
<h5 id="define-cryptographic-settings-1">Define Cryptographic Settings</h5>
<p>Define an IPsec Crypto Profile with the following settings:</p>
<table>
<thead>
<tr>
<th><strong>Attribute</strong></th>
<th><strong>Value</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>dh-group</td>
<td>group20</td>
</tr>
<tr>
<td>esp encryption</td>
<td>aes-256-cbc</td>
</tr>
<tr>
<td>esp authentication</td>
<td>sha256</td>
</tr>
<tr>
<td>lifetime hours</td>
<td>8</td>
</tr>
</tbody>
</table>
<h6 id="cli-4">CLI</h6>
<pre><code class="language-txt">set network ike crypto-profiles ipsec-crypto-profiles ipsec-aes256cbc-sha256-dh20 esp authentication sha256&#10;set network ike crypto-profiles ipsec-crypto-profiles ipsec-aes256cbc-sha256-dh20 esp encryption aes-256-cbc&#10;set network ike crypto-profiles ipsec-crypto-profiles ipsec-aes256cbc-sha256-dh20 lifetime hours 8&#10;set network ike crypto-profiles ipsec-crypto-profiles ipsec-aes256cbc-sha256-dh20 dh-group group20&#10;</code></pre>
<h6 id="web-ui-4">Web UI</h6>
<ol>
<li>Go to <strong>Network</strong> &gt; <strong>Network Profiles</strong> &gt; <strong>IPsec Crypto</strong>.</li>
<li>Select <strong>Add</strong>.</li>
<li>Name: <code>ipsec-aes256cbc-sha256-dh20</code></li>
<li>IPsec Protocol: <code>ESP</code></li>
<li>Encryption: <code>aes-256-cbc</code></li>
<li>Authentication: <code>sha256</code></li>
<li>DH Group: <code>group20</code></li>
<li>Lifetime (Hours): <code>8</code></li>
</ol>
<h5 id="define-ipsec-tunnel-objects">Define IPsec tunnel objects</h5>
<h6 id="cli-define-ipsec-tunnels">CLI - Define IPsec tunnels</h6>
<ul>
<li>Tunnel 1</li>
</ul>
<pre><code class="language-txt">set network tunnel ipsec cf-wan-ipsec-tun-01 auto-key ike-gateway cf-wan-ike-gw-01&#10;set network tunnel ipsec cf-wan-ipsec-tun-01 auto-key ipsec-crypto-profile ipsec-aes256cbc-sha256-dh20&#10;set network tunnel ipsec cf-wan-ipsec-tun-01 tunnel-monitor enable no&#10;set network tunnel ipsec cf-wan-ipsec-tun-01 tunnel-interface tunnel.1&#10;set network tunnel ipsec cf-wan-ipsec-tun-01 anti-replay no&#10;&#10;set network tunnel ipsec cf-wan-ipsec-tun-02 auto-key ike-gateway cf-wan-ike-gw-02&#10;set network tunnel ipsec cf-wan-ipsec-tun-02 auto-key ipsec-crypto-profile ipsec-aes256cbc-sha256-dh20&#10;set network tunnel ipsec cf-wan-ipsec-tun-02 tunnel-monitor enable no&#10;set network tunnel ipsec cf-wan-ipsec-tun-02 tunnel-interface tunnel.2&#10;set network tunnel ipsec cf-wan-ipsec-tun-02 anti-replay no&#10;</code></pre>
<h6 id="web-ui-define-ipsec-tunnels">Web UI - Define IPsec Tunnels</h6>
<ol>
<li>Go to <strong>Network</strong> &gt; <strong>IPsec Tunnels</strong>.</li>
<li>Select <strong>Add</strong>.</li>
<li>Name: <code>cf-wan-ipsec-tun-01</code></li>
<li>Tunnel interface: <code>tunnel.1</code></li>
<li>Type: <code>Auto Key</code></li>
<li>Address Type: <code>IPv4</code></li>
<li>IKE Gateway: <code>cf-wan-ike-gw-01</code></li>
<li>IPsec Crypto Profile: <code>ipsec-aes256cbc-sha256-dh20</code></li>
<li>Show Advanced Options - check the box.</li>
<li>Uncheck <code>Enable Replay Protection</code>.</li>
<li>IPsec Mode: <code>Tunnel</code></li>
</ol>
<p>Repeat steps for tunnel 2</p>
<ol>
<li>Go to <strong>Network</strong> &gt; <strong>IPsec Tunnels</strong>.</li>
<li>Select <strong>Add</strong>.</li>
<li>Name: <code>cf-wan-ipsec-tun-02</code></li>
<li>Tunnel interface: <code>tunnel.2</code></li>
<li>Type: <code>Auto Key</code></li>
<li>Address Type: <code>IPv4</code></li>
<li>IKE Gateway: <code>cf-wan-ike-gw-02</code></li>
<li>IPsec Crypto Profile: <code>ipsec-aes256cbc-sha256-dh20</code></li>
<li>Show Advanced Options - check the box.</li>
<li>Uncheck <code>Enable Replay Protection</code>.</li>
<li>IPsec Mode: <code>Tunnel</code></li>
</ol>
<h3 id="commit-changes">Commit Changes</h3>
<p>This is a good place to stop and perform a <code>Commit</code> to apply the configuration settings. You should be able to validate that tunnel connectivity is established.</p>
<h3 id="ipsec-tunnel-verification">IPSec Tunnel Verification</h3>
<h4 id="web-ui-view-ipsec-tunnel-status">Web UI - View IPsec Tunnel Status</h4>
<ol>
<li>Go to <strong>Network</strong> &gt; <strong>IPsec Tunnels</strong>.</li>
</ol>
<p>View the status of the red/green indicators - select <strong>Tunnel Info</strong> and <strong>IKE Info</strong> to obtain real-time status indicators.</p>
<h4 id="web-ui-view-ipsec-log-details">Web UI - View IPsec Log Details</h4>
<ol>
<li>Go to <strong>Monitor</strong> &gt; <strong>Logs</strong> &gt; <strong>System</strong>.</li>
<li>Add the following to the filter/search dialog across the top: <code>( subtype eq vpn )</code></li>
</ol>
<p>This will provide valuable information as to IKE/IPsec Phase 1 and Phase 2 status and error messages.</p>
<h3 id="security-policy">Security Policy</h3>
<p>Palo Alto Networks NGFW automatically permits traffic originating from and destined to the same zone (intra-zone traffic). If you opted to add <code>tunnel.1</code> and <code>tunnel.2</code> into a separate Security Zone, you will require explicit firewall rules to allow traffic to flow from <code>trust</code> to <code>cloudflare</code> as well as from <code>cloudflare</code> to <code>trust</code>.</p>
<h3 id="cli-add-security-policy-from-trust-to-cloudflare">CLI - Add Security Policy from <code>trust</code> to <code>cloudflare</code></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6831.md")
</aside>
<p>Use the <code>move rulebase security rules</code> <code>&lt;RULE_NAME&gt;</code> <code>[after|before|top|bottom]</code> <code>&lt;RULE_NAME - Desired position&gt;</code></p>
<pre><code class="language-txt">set rulebase security rules trust-to-cloudflare to cloudflare&#10;set rulebase security rules trust-to-cloudflare from trust&#10;set rulebase security rules trust-to-cloudflare source any&#10;set rulebase security rules trust-to-cloudflare destination any&#10;set rulebase security rules trust-to-cloudflare application any&#10;set rulebase security rules trust-to-cloudflare service application-default&#10;set rulebase security rules trust-to-cloudflare action allow&#10;set rulebase security rules trust-to-cloudflare log-start no&#10;set rulebase security rules trust-to-cloudflare log-end yes&#10;set rulebase security rules trust-to-cloudflare rule-type universal&#10;</code></pre>
<h3 id="web-ui-add-security-policy-from-trust-to-cloudflare">Web UI - Add Security Policy from <code>trust</code> to <code>cloudflare</code></h3>
<ol>
<li>Go to <strong>Policies</strong> &gt; <strong>Security</strong>.</li>
<li>Select <strong>Add</strong>.</li>
<li>General &gt; Name: <code>trust-to-cloudflare</code></li>
<li>Rule Type: <code>universal (default)</code> or <code>interzone</code></li>
<li>Source &gt; Source Zone: <code>trust</code></li>
<li>Destination &gt; Destination Zone: <code>cloudflare</code></li>
<li>Application &gt; <code>Any</code></li>
<li>Service/URL Category &gt; <code>application-default</code></li>
<li>Actions &gt; Action setting: <code>Allow</code></li>
<li>Log Setting: <code>Log at Session End</code></li>
</ol>
<h3 id="cli-add-security-policy-from-cloudflare-to-trust">CLI - Add Security Policy from <code>cloudflare</code> to <code>trust</code></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6830.md")
</aside>
<p>Use the <code>move rulebase security rules</code> <code>&lt;RULE_NAME&gt;</code> <code>[after|before|top|bottom]</code> <code>&lt;RULE_NAME - Desired position&gt;</code></p>
<pre><code class="language-txt">set rulebase security rules cloudflare-to-trust to trust&#10;set rulebase security rules cloudflare-to-trust from cloudflare&#10;set rulebase security rules cloudflare-to-trust source any&#10;set rulebase security rules cloudflare-to-trust destination any&#10;set rulebase security rules cloudflare-to-trust application any&#10;set rulebase security rules cloudflare-to-trust service application-default&#10;set rulebase security rules cloudflare-to-trust action allow&#10;set rulebase security rules cloudflare-to-trust log-start no&#10;set rulebase security rules cloudflare-to-trust log-end yes&#10;set rulebase security rules cloudflare-to-trust rule-type universal&#10;</code></pre>
<h3 id="web-ui-add-security-policy-from-cloudflare-to-trust">Web UI - Add Security Policy from <code>cloudflare</code> to <code>trust</code></h3>
<ol>
<li>Go to <strong>Policies</strong> &gt; <strong>Security</strong>.</li>
<li>Select <strong>Add</strong>.</li>
<li>General &gt; Name: <code>cloudflare-to-trust</code></li>
<li>Rule Type: <code>universal (default)</code> or <code>interzone</code></li>
<li>Source &gt; Source Zone: <code>cloudflare</code></li>
<li>Destination &gt; Destination Zone: <code>trust</code></li>
<li>Application &gt; <code>Any</code></li>
<li>Service/URL Category &gt; <code>application-default</code></li>
<li>Actions &gt; Action setting: <code>Allow</code></li>
<li>Log Setting: <code>Log at Session End</code></li>
</ol>
<h2 id="policy-based-forwarding">Policy Based Forwarding</h2>
<p><a href="https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/policy/policy-based-forwarding">Policy Based Forwarding</a> (aka Policy-Based Routing) allows you to apply additional matching criteria to specific traffic flows that will override routes defined within the Virtual Router.</p>
<p>You may only want to direct traffic through Cloudflare WAN if destined for another Cloudflare WAN site, while Internet-bound traffic continues to get forwarded directly through local Internet breakout.</p>
<p>The following example routes <em>ALL</em> traffic from the LAN subnet behind NGFW (192.168.125.0/24) through the Cloudflare WAN IPsec tunnels. This lets you use the Cloudflare Secure Web Gateway functionality.</p>
<p>You can route traffic to specific destinations simply by adding subnets to the Destination match criteria.</p>
<p>Ensure any traffic flows processed by Policy Based Forwarding is exempted from NAT policies. Cloudflare Gateway will ensure NAT is applied to Internet bound traffic without the need for policy on local devices.</p>
<h3 id="cli-add-policy-based-forwarding-rules">CLI - Add Policy Based Forwarding Rules</h3>
<ul>
<li>Tunnel 1</li>
</ul>
<pre><code class="language-txt">set rulebase pbf rules cf-wan-to-internet-01 action forward nexthop ip-address cf-wan-ipsec-vti-01-remote&#10;set rulebase pbf rules cf-wan-to-internet-01 action forward egress-interface tunnel.1&#10;set rulebase pbf rules cf-wan-to-internet-01 from zone trust&#10;set rulebase pbf rules cf-wan-to-internet-01 enforce-symmetric-return enabled no&#10;set rulebase pbf rules cf-wan-to-internet-01 source lan-net-192-168-125-0--24&#10;set rulebase pbf rules cf-wan-to-internet-01 destination any&#10;set rulebase pbf rules cf-wan-to-internet-01 source-user any&#10;set rulebase pbf rules cf-wan-to-internet-01 application any&#10;set rulebase pbf rules cf-wan-to-internet-01 service any&#10;</code></pre>
<ul>
<li>Tunnel 2</li>
</ul>
<pre><code class="language-txt">set rulebase pbf rules cf-wan-to-internet-02 action forward nexthop ip-address cf-wan-ipsec-vti-02-remote&#10;set rulebase pbf rules cf-wan-to-internet-02 action forward egress-interface tunnel.2&#10;set rulebase pbf rules cf-wan-to-internet-02 from zone trust&#10;set rulebase pbf rules cf-wan-to-internet-02 enforce-symmetric-return enabled no&#10;set rulebase pbf rules cf-wan-to-internet-02 source lan-net-192-168-125-0--24&#10;set rulebase pbf rules cf-wan-to-internet-02 destination any&#10;set rulebase pbf rules cf-wan-to-internet-02 source-user any&#10;set rulebase pbf rules cf-wan-to-internet-02 application any&#10;set rulebase pbf rules cf-wan-to-internet-02 service any&#10;</code></pre>
<h3 id="web-ui-add-policy-based-forwarding-rules">Web UI - Add Policy Based Forwarding Rules</h3>
<ul>
<li>Tunnel 1:</li>
</ul>
<ol>
<li>Go to <strong>Policies</strong> &gt; <strong>Policy Based Forwarding</strong>.</li>
<li>Select <strong>Add</strong>.</li>
<li>Name: <code>cf-wan-to-internet-01</code></li>
<li>Source Zone: <code>trust</code></li>
<li>Source Address: <code>lan-net-192-168-125-0--24</code></li>
<li>Destination/Application/Service - Any/Any/Any</li>
<li>Forwarding &gt; Action: Forward, Egress Interface: tunnel.1, Next Hop - IP Address: <code>cf-wan-ipsec-vti-01-remote</code></li>
</ol>
<ul>
<li>Tunnel 2:</li>
</ul>
<ol>
<li>Go to <strong>Policies</strong> &gt; <strong>Policy Based Forwarding</strong>.</li>
<li>Select <strong>Add</strong>.</li>
<li>Name: <code>cf-wan-to-internet-02</code></li>
<li>Source Zone: <code>trust</code></li>
<li>Source Address: <code>lan-net-192-168-125-0--24</code></li>
<li>Destination/Application/Service - Any/Any/Any</li>
<li>Forwarding &gt; Action: Forward, Egress Interface: tunnel.2, Next Hop - IP Address: <code>cf-wan-ipsec-vti-02-remote</code></li>
</ol>
<p>Commit changes, then test traffic from a host on the 192.168.125.0/24 subnet to ensure it is forwarded through the Cloudflare WAN IPsec Tunnels.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6829.md")
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
<h3 id="quick-reference-guide">Quick Reference Guide</h3>
<h4 id="display-ike-ipsec-security-associations">Display IKE &amp; IPsec Security Associations</h4>
<p>Use <a href="https://docs.paloaltonetworks.com/network-security/ipsec-vpn/administration/troubleshooting/troubleshooting-site-to-site-vpn-issues-using-cli">show</a> commands to display Phase 1 and Phase 2 security associations:</p>
<pre><code class="language-txt">admin@panfw01&gt; show vpn ike-sa&#10;&#10;IKEv2 SAs&#10;Gateway ID      Peer-Address       Gateway Name       Role SN    Algorithm             Established     Expiration      Xt Child  ST&#10;&#45;---------      ------------       ------------       ---- --    ---------             -----------     ----------      -- -----  --&#10;1               162.159.135.1      cf-wan-ike-gw-01   Init 46    PSK/DH14/A256/SHA256  Mar.22 23:14:24 Mar.23 07:14:24 0  1      Established&#10;2               172.64.135.1       cf-wan-ike-gw-02   Init 45    PSK/DH14/A256/SHA256  Mar.22 23:05:02 Mar.23 07:05:02 0  1      Established&#10;</code></pre>
<pre><code class="language-txt">IKEv2 IPSec Child SAs&#10;Gateway Name                   TnID     Tunnel                     ID       Parent   Role SPI(in)  SPI(out) MsgID    ST              &#10;&#45;-----------                   ----     ------                     --       ------   ---- -------  -------- -----    --              &#10;cf-wan-ike-gw-01               1        cf-wan-ipsec-tun-01        452741   97       Init B7D055D3 4CB26B43 00000001 Mature           &#10;cf-wan-ike-gw-02               2        cf-wan-ipsec-tun-02        452742   98       Init B4629A07 165D416C 00000001 Mature           &#10;&#10;Show IKEv2 SA: Total 2 gateways found. 2 ike sa found.&#10;</code></pre>
<h4 id="manually-initiate-ike-ipsec-security-associations">Manually Initiate IKE &amp; IPsec Security Associations</h4>
<p>Use <a href="https://docs.paloaltonetworks.com/network-security/ipsec-vpn/administration/troubleshooting/troubleshooting-site-to-site-vpn-issues-using-cli">test</a> commands to force Phase 1 and Phase 2 security associations:</p>
<pre><code class="language-txt">admin@panfw01&gt; test vpn ike-sa gateway cf-wan-ike-gw-01 &#10;&#10;Start time: Mar.30 21:23:23&#10;Initiate 1 IKE SA.&#10;&#10;admin@panfw01&gt; test vpn ike-sa gateway cf-wan-ike-gw-02&#10;&#10;Start time: Mar.30 21:23:24&#10;Initiate 1 IKE SA.&#10;</code></pre>
<pre><code class="language-txt">admin@panfw01&gt; test vpn ipsec-sa tunnel cf-wan-ipsec-tun-01 &#10;&#10;Start time: Mar.30 21:26:50&#10;Initiate 1 IPSec SA for tunnel cf-wan-ipsec-tun-01.&#10;&#10;admin@panfw01&gt; test vpn ipsec-sa tunnel cf-wan-ipsec-tun-02&#10;&#10;Start time: Mar.30 21:26:52&#10;Initiate 1 IPSec SA for tunnel cf-wan-ipsec-tun-02.&#10;</code></pre>
<h3 id="palo-alto-networks-documentation">Palo Alto Networks Documentation</h3>
<ul>
<li>
<p><a href="https://docs.paloaltonetworks.com/network-security/ipsec-vpn/administration/troubleshooting/test-vpn-connectivity">Troubleshoot your IPSec VPN tunnel connection</a></p>
</li>
<li>
<p><a href="https://docs.paloaltonetworks.com/network-security/ipsec-vpn/administration/troubleshooting/troubleshooting-site-to-site-vpn-issues-using-cli">Troubleshoot site-to-site VPN issues using CLI</a></p>
</li>
</ul>
<h3 id="palo-alto-networks-knowledge-base">Palo Alto Networks Knowledge Base</h3>
<ul>
<li><a href="https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClivCAC">How to troubleshoot IPSec VPN connectivity issues</a></li>
</ul>
