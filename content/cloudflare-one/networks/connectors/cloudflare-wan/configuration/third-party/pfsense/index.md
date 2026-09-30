<p>This tutorial includes the steps required to configure IPsec tunnels to connect a pfSense firewall to Cloudflare WAN (formerly Magic WAN).</p>
<h2 id="software-tested">Software tested</h2>
<table>
<thead>
<tr>
<th>Manufacturer</th>
<th>Firmware revision</th>
</tr>
</thead>
<tbody>
<tr>
<td>pfSense</td>
<td>24.03</td>
</tr>
</tbody>
</table>
<h2 id="prerequisites">Prerequisites</h2>
<p>This tutorial requires the following information:</p>
<ul>
<li>Anycast IP addresses (Cloudflare provides these)</li>
<li>External IP addresses</li>
<li>Internal IP address ranges</li>
<li>Inside tunnel <code>/31</code> ranges</li>
</ul>
<h2 id="example-scenario">Example scenario</h2>
<p>This tutorial uses the following IP addresses. These examples replace legally routable IP addresses with IPv4 Address Blocks Reserved for Documentation (<a href="https://datatracker.ietf.org/doc/html/rfc5737">RFC 5737</a>) addresses within the <code>203.0.113.0/24</code> subnet.</p>
<table>
<thead>
<tr>
<th>Tunnel name</th>
<th><code>PF_TUNNEL_01</code></th>
<th><code>PF_TUNNEL_02</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>Interface address</td>
<td><code>10.252.2.26/31</code></td>
<td><code>10.252.2.28/31</code></td>
</tr>
<tr>
<td>Customer endpoint</td>
<td><code>203.0.113.254</code></td>
<td><code>203.0.113.254</code></td>
</tr>
<tr>
<td>Cloudflare endpoint</td>
<td><code>&lt;YOUR_ANYCAST_IP_ADDRESS_1&gt;</code></td>
<td><code>&lt;YOUR_ANYCAST_IP_ADDRESS_2&gt;</code></td>
</tr>
<tr>
<td>pfSense IPsec Phase 2 Local IP</td>
<td><code>10.252.2.27</code></td>
<td><code>10.252.2.29</code></td>
</tr>
<tr>
<td>pfSense IPsec Phase 2 Remote IP</td>
<td><code>10.252.2.26</code></td>
<td><code>10.252.2.28</code></td>
</tr>
<tr>
<td>Cloudflare WAN static routes - Prefix</td>
<td><code>10.1.100.0/24</code></td>
<td><code>10.1.100.0/24</code></td>
</tr>
<tr>
<td>Cloudflare WAN static routes - Next hop</td>
<td><code>PF_TUNNEL_01</code></td>
<td><code>PF_TUNNEL_02</code></td>
</tr>
</tbody>
</table>
<h2 id="1-configure-cloudflare-wan-ipsec-tunnels"><ol>
<li>Configure Cloudflare WAN IPsec tunnels</li>
</ol></h2>
<p>Use the Cloudflare dashboard or API to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">configure two IPsec tunnels</a>. This guide uses the settings mentioned below for the IPsec tunnels throughout the remainder.</p>
<h3 id="add-ipsec-tunnels">Add IPsec tunnels</h3>
<ol>
<li>Follow the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">Add tunnels</a> instructions to create the required IPsec tunnels with the following options:
<ul>
<li><strong>Tunnel name</strong>: <code>PF_TUNNEL_01</code></li>
<li><strong>Interface address</strong>: <code>10.252.2.26/31</code></li>
<li><strong>Customer endpoint</strong>: <code>203.0.113.254</code></li>
<li><strong>Cloudflare endpoint</strong>: Enter one of the anycast IP addresses assigned to your account, available in <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space">Leased IPs</a>.</li>
<li><strong>Health check rate</strong>: <em>Medium</em></li>
<li><strong>Health check type</strong>: <em>Request</em></li>
<li><strong>Health check direction</strong>: <em>Bidirectional</em></li>
<li><strong>Turn on replay protection</strong>: Enable</li>
</ul>
</li>
<li>Select <strong>Add pre-shared key later</strong> &gt; <strong>Add tunnels</strong>.</li>
<li>Repeat the process to create a second IPsec tunnel with the following options:
<ul>
<li><strong>Tunnel name</strong>: <code>PF_TUNNEL_02</code></li>
<li><strong>Interface address</strong>: <code>10.252.2.28/31</code></li>
<li><strong>Customer endpoint</strong>: <code>203.0.113.254</code></li>
<li><strong>Cloudflare endpoint</strong>: Enter the second anycast IP address assigned to your account.</li>
<li><strong>Health check rate</strong>: <em>Medium</em></li>
<li><strong>Health check type</strong>: <em>Request</em></li>
<li><strong>Health check direction</strong>: <em>Bidirectional</em></li>
<li><strong>Turn on replay protection</strong>: Enable</li>
</ul>
</li>
<li>Select <strong>Add pre-shared key later</strong> &gt; <strong>Add tunnels</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5598.md")
</aside>
<h3 id="generate-pre-shared-keys">Generate pre-shared keys</h3>
<p>When creating IPsec tunnels with the option <strong>Add pre-shared key later</strong>, the Cloudflare dashboard will show a warning indicator.</p>
<ol>
<li>Select <strong>Edit</strong> to edit the properties of each IPsec tunnel.</li>
<li>Select <strong>Generate a new pre-shared key</strong> &gt; <strong>Update and generate pre-shared key</strong>.</li>
<li>Copy the pre-shared key value for each IPsec tunnel, and save these values. Then, select <strong>Done</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5597.md")
</aside>
<h3 id="ipsec-identifier-user-id">IPsec identifier - User ID</h3>
<p>After creating IPsec tunnels, the Cloudflare dashboard will list them under <strong>Tunnels</strong>. To retrieve the IPsec tunnel's user ID:</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In the <strong>IPsec/GRE tunnels</strong> tab, select the IPsec tunnel.</li>
<li>Scroll to <strong>User ID</strong> and copy the string. For example, <code>ipsec@long_string_of_letters_and_numbers</code>.</li>
</ol>
<p>Configuring IKE Phase 1 on the pfSense firewall requires the User ID.</p>
<h2 id="2-create-cloudflare-wan-static-routes"><ol start="2">
<li>Create Cloudflare WAN static routes</li>
</ol></h2>
<p>Create a <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-routes/#create-a-static-route">static route</a> for each of the two IPsec tunnels configured in the previous section, with the following settings (settings not mentioned here can be left with their default values):</p>
<h3 id="tunnel-01">Tunnel 01</h3>
<ul>
<li><strong>Description</strong>: <code>PF_TUNNEL_01</code></li>
<li><strong>Prefix</strong>: <code>10.1.100.0/24</code></li>
<li><strong>Tunnel/Next hop</strong>: <code>PF_TUNNEL_01</code></li>
</ul>
<h3 id="tunnel-02">Tunnel 02</h3>
<ul>
<li><strong>Description</strong>: <code>PF_TUNNEL_02</code></li>
<li><strong>Prefix</strong>: <code>10.1.100.0/24</code></li>
<li><strong>Tunnel/Next hop</strong>: <code>PF_TUNNEL_02</code></li>
</ul>
<h2 id="3-configure-the-pfsense-firewall"><ol start="3">
<li>Configure the pfSense firewall</li>
</ol></h2>
<p>Install pfSense and boot up. Then, assign and set LAN and WAN interfaces, as well as IP addresses. For example:</p>
<ul>
<li><strong>LAN</strong>: <code>203.0.113.254</code></li>
<li><strong>WAN</strong>: <code>&lt;YOUR_WAN_ADDRESS&gt;</code></li>
</ul>
<h3 id="configure-ipsec-phase-1">Configure IPsec Phase 1</h3>
<p>Add a new IPsec tunnel <a href="https://docs.netgate.com/pfsense/en/latest/vpn/ipsec/configure-p1.html">Phase 1 entry</a>, with the following settings:</p>
<ul>
<li><strong>General Information</strong>
<ul>
<li><strong>Description</strong>: <code>CF1_IPsec_P1</code></li>
</ul>
</li>
<li><strong>IKE Endpoint Configuration</strong>
<ul>
<li><strong>Key exchange version</strong>: <em>IKE_v2</em></li>
<li><strong>Internet Protocol</strong>: <em>IPv4</em></li>
<li><strong>Interface</strong>: <em>WAN</em></li>
<li><strong>Remote gateway</strong>: Enter the Cloudflare Anycast IP address.</li>
</ul>
</li>
<li><strong>Phase 1 Proposal (Authentication)</strong>
<ul>
<li><strong>Authentication method</strong>: <em>Mutual PSK</em></li>
<li><strong>My identifier</strong>: <em>User Fully qualified domain name</em> &gt; <code>ipsec@long_string_of_letters_and_numbers</code> <br/> (Find this identifier in the Cloudflare IPsec tunnel configuration &gt; <strong>User ID</strong>)</li>
<li><strong>Peer identifier</strong>: <em>Peer IP Address</em> (Cloudflare Anycast IP)</li>
<li><strong>Pre-Shared Key (PSK)</strong>: Enter the pre-shared key from the Cloudflare IPsec tunnel.</li>
</ul>
</li>
<li><strong>Phase 1 proposal (Encryption algorithm)</strong>
<ul>
<li><strong>Encryption algorithm</strong>: <em>AES 256 bits</em></li>
<li><strong>Key length</strong>: <em>256 bits</em></li>
<li><strong>Hash algorithm</strong>: <em>SHA256</em></li>
<li><strong>DH key group</strong>: <em>20</em></li>
<li><strong>Lifetime</strong>: <code>86400</code></li>
</ul>
</li>
</ul>
<h3 id="configure-ipsec-phase-2">Configure IPsec Phase 2</h3>
<p>Add a new IPsec tunnel <a href="https://docs.netgate.com/pfsense/en/latest/vpn/ipsec/configure-p2.html">Phase 2 entry</a>, with the following settings. Create two separate Phase 2 entries (one for tunnel 1 and one for tunnel 2), adjusting the IP addresses for local and remote networks accordingly:</p>
<ul>
<li><strong>General Information</strong>
<ul>
<li><strong>Description</strong>: <code>CF1_IPsec_P2</code></li>
<li><strong>Mode</strong>: <em>Routed (VTI)</em> (Virtual Tunnel Interface)</li>
</ul>
</li>
<li><strong>Networks</strong>
<ul>
<li><strong>Local Network</strong>: <em>Address</em> &gt; Higher IP address in the <code>/31</code> assigned in Cloudflare tunnel. For example, <code>10.252.2.27</code> for tunnel 1 and <code>10.252.2.29</code> for tunnel 2.</li>
<li><strong>Remote Network</strong>: <em>Address</em> &gt; Lower IP address in the <code>/31</code> for Cloudflare side. For example, <code>10.252.2.26</code> for tunnel 1, and <code>10.252.2.28</code> for tunnel 2.</li>
</ul>
</li>
<li><strong>Phase 2 Proposal (SA/Key Exchange)</strong>
<ul>
<li><strong>Protocol</strong>: <em>ESP</em> (Encapsulating Security Payload)</li>
<li><strong>Encryption algorithm</strong>: <em>AES 256 bits</em></li>
<li><strong>Hash algorithm</strong>: <em>SHA256</em></li>
<li><strong>DH key group</strong>: <em>20</em></li>
<li><strong>Lifetime</strong>: <code>28800</code></li>
</ul>
</li>
</ul>
<p>Apply the changes. Navigate to <strong>Status</strong> &gt; <strong>IPsec</strong> to verify that both Phase 1 and Phase 2 are connected.</p>
<div class="full-img">
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/pfsense/ipsec-overview.png" alt="pfSense IPsec overview" /></p>
</div>
<h3 id="interface-assignments">Interface assignments</h3>
<p>In <strong>Interfaces</strong> &gt; <strong>Assignments</strong> &gt; <strong>Add</strong>, create a new interface to assign to the first IPsec tunnel, with the following settings:</p>
<ul>
<li><strong>General configuration</strong>
<ul>
<li><strong>Description</strong>: <code>CF1_IPsec_1</code></li>
<li><strong>MSS</strong>: <code>1446</code></li>
</ul>
</li>
<li><strong>Interface Assignments</strong>
<ul>
<li><strong>WAN</strong>: Add the WAN interface. For example, <code>vnet1</code>.</li>
<li><strong>LAN</strong>: Add the LAN interface. For example, <code>vnet0</code>.</li>
<li>Add the <strong>CF_IPsec_1</strong> interface from Phase 1 above.</li>
</ul>
</li>
</ul>
<p>Select <strong>Save</strong> to apply the changes.</p>
<div class="full-img">
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/pfsense/interfaces.png" alt="Assign a new interface to the first IPsec tunnel" /></p>
</div>
<div class="full-img">
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/pfsense/interface-assignments.png" alt="Configuring interface assignments" /></p>
</div>
<h3 id="gateway">Gateway</h3>
<p>In <strong>System</strong> &gt; <strong>Routing</strong> &gt; <strong>Gateways</strong> there should already be a gateway. For this example, it is named <code>CF1_IPSEC_1_VTIV4</code>.</p>
<div class="full-img">
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/pfsense/gateways.png" alt="There should already be a gateway configured in the interface" /></p>
</div>
<h3 id="firewall-rules-ipsec">Firewall Rules IPsec</h3>
<ol>
<li>In <strong>Firewall Rules</strong> &gt; <strong>IPsec interface</strong>, allow any type of traffic.</li>
</ol>
<div class="full-img">
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/pfsense/firewall-ipsec.png" alt="Allow all traffic for IPsec" /></p>
</div>
<ol start="2">
<li>Navigate to <strong>Status</strong> &gt; <strong>Gateways</strong>. <code>CF1_IPSEC_1_VTIV4</code> should now be online.</li>
</ol>
<div class="full-img">
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/pfsense/status-gateways.png" alt="The gateway should now be online" /></p>
</div>
<h3 id="firewall-rules-lan">Firewall Rules LAN</h3>
<ol>
<li>In <strong>Firewall</strong> &gt; <strong>Rules</strong> &gt; <strong>LAN</strong>, allow any type of traffic.</li>
<li>Expand the <strong>Advanced</strong> section.</li>
<li>Change the Gateway to <code>CF1_IPSEC_1_VTIV4</code>.</li>
</ol>
<div class="full-img">
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/pfsense/firewall-lan.png" alt="Change the gateway in the firewall rules for LAN traffic" /></p>
</div>
