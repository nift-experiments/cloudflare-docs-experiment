<p>Connect a Ubiquiti UniFi Gateway to Cloudflare's network using Cloudflare WAN (formerly Magic WAN). These steps use the Cloud Gateway Max (UCG-Max) but work with other UniFi gateways supporting route-based IPsec (Internet Protocol Security) VPNs (Virtual Private Networks), like the Dream Machine series.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Cloudflare account with Cloudflare WAN enabled (contact your account team)</li>
<li>UniFi Cloud Gateway or Dream Machine with IPsec support</li>
<li>UniFi Network Application (self-hosted or cloud)</li>
<li>Static public IP from your ISP</li>
<li>Admin access to both Cloudflare and UniFi</li>
<li>Gather a <strong>Magic Anycast IPv4</strong> address from the <strong>Leased IPs</strong> section in the dashboard
<ul>
<li>
<div class="nb-dash-button"></div>
</li>
<li>Contact your account team if you do not see any IP addresses listed.</li>
</ul>
</li>
</ul>
<h2 id="1-configure-cloudflare-wan"><ol>
<li>Configure Cloudflare WAN</li>
</ol></h2>
<ol>
<li>
<p>Refer to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">Add tunnels</a> to learn how to add IPsec tunnels.</p>
</li>
<li>
<p>Select <strong>IPsec tunnel</strong> &gt; <strong>Next</strong>, and fill in the following settings:
- <strong>Name</strong>: <code>unifi-gw-primary</code>
- <strong>IPv4 Interface Address</strong>: <code>10.252.2.28/31</code> or refer to the <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Tunnel endpoints documentation</a>
- <strong>Customer Endpoint</strong>: This should be your UniFi Gateway's WAN IP (for example, <code>203.0.113.10</code>)</p>
<ul>
<li><strong>Cloudflare Endpoint</strong>: This should be one of the IPv4 addresses gathered from Leased IPs.</li>
<li>Under <strong>Tunnel Health checks</strong>, select:
<ul>
<li><strong>Health check rate</strong>: Set to desired level</li>
<li><strong>Health check type</strong>: <em>Request</em></li>
<li><strong>Health check direction</strong>: <em>Bidirectional</em></li>
<li><strong>Health check target</strong>: <em>Default</em></li>
</ul>
</li>
<li>Under <strong>Pre-shared key</strong>:
<ul>
<li>Select <strong>Add pre-shared key later</strong>. This key will be given during the UniFi site-to-site VPN configuration.</li>
</ul>
</li>
</ul>
</li>
</ol>
<h2 id="2-configure-site-to-site-vpn-on-unifi"><ol start="2">
<li>Configure site-to-site VPN on UniFi</li>
</ol></h2>
<ol>
<li>In UniFi Network, go to <strong>Settings</strong> &gt; <strong>VPN</strong> &gt; <strong>Site-to-Site VPN</strong>.</li>
<li>Select <strong>Create New</strong>.</li>
<li>Configure the following settings:
<ul>
<li><strong>VPN Type:</strong> <code>IPsec</code>.</li>
<li><strong>Name:</strong> <code>Cloudflare-Magic-WAN</code>.</li>
<li><strong>Pre-shared key:</strong> Copy this key. You need it for the IPsec tunnel.</li>
<li><strong>Local IP:</strong> Select the WAN interface (for example, <code>WAN1</code>).</li>
<li><strong>Remote IP:</strong> Enter the Cloudflare endpoint IP from <a href="#1-configure-cloudflare-wan">Step 1</a>.</li>
<li><strong>VPN Method:</strong> Route Based.</li>
<li><strong>Tunnel IP:</strong> <code>10.252.2.29/31</code> or refer to the <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Tunnel endpoints documentation</a>.</li>
<li><strong>Remote Networks:</strong> Inside Cloudflare tunnel address (for example, <code>10.252.2.28/31</code>) and other remote subnets to access through Cloudflare WAN.</li>
</ul>
</li>
<li>Set Advanced settings:
<ul>
<li><strong>Key Exchange Version</strong>: IKEv2.</li>
<li><strong>IKE Encryption</strong>: AES-256.</li>
<li><strong>IKE Hash</strong>: SHA256.</li>
<li><strong>IKE DH Group</strong>: 14.</li>
<li><strong>IKE Lifetime</strong>: 28800.</li>
<li><strong>ESP Encryption</strong>: AES-256.</li>
<li><strong>ESP Hash</strong>: SHA256.</li>
<li><strong>ESP DH Group</strong>: 14.</li>
<li><strong>ESP Lifetime</strong>: 28800.</li>
<li><strong>PFS</strong>: Enabled.</li>
<li><strong>Local Authentication ID</strong>: Auto.</li>
<li><strong>Remote Authentication ID</strong>: Uncheck <strong>Auto</strong>, and enter the Cloudflare Endpoint IP from <a href="#1-configure-cloudflare-wan">Step 1</a>.</li>
<li><strong>MTU</strong>: 1436.</li>
</ul>
</li>
<li>Select <strong>Apply</strong></li>
</ol>
<h2 id="3-add-pre-shared-key-to-cloudflare"><ol start="3">
<li>Add pre-shared key to Cloudflare</li>
</ol></h2>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>In the <strong>IPsec/GRE tunnels</strong> tab, find the IPsec tunnel you have just created.</p>
</li>
<li>
<p>Select your tunnel and then <strong>Edit</strong>.</p>
</li>
<li>
<p>Paste the preshared key from <a href="#2-configure-site-to-site-vpn-on-unifi">Step 2</a>.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<h2 id="4-configure-routes"><ol start="4">
<li>Configure Routes</li>
</ol></h2>
<ol>
<li>Go to the <strong>Routes</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create static route</strong>.</p>
</li>
<li>
<p>Enter the following settings:</p>
<ul>
<li><strong>Prefix</strong>: Your local network (for example, <code>192.168.1.0/24</code>).</li>
<li><strong>Tunnel/Next hop</strong>: Select your tunnel.</li>
<li><strong>Priority</strong>: <code>100</code>.</li>
</ul>
</li>
<li>
<p>Select <strong>Add routes</strong> to add your static route.</p>
</li>
</ol>
<h2 id="verify-connections">Verify connections</h2>
<p>Wait a few minutes, then access both Cloudflare and UniFi to verify the tunnel's status:</p>
<details class="nb-details"><summary>Cloudflare</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6823.md")
</div></details>
<details class="nb-details"><summary>UniFi</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6824.md")
</div></details>
<h2 id="troubleshooting">Troubleshooting</h2>
<p><strong>Tunnel down:</strong></p>
<ul>
<li>Verify Peer IP, pre-shared key, and IPsec settings match on both sides</li>
<li>Check that the ISP is not blocking UDP ports <code>500</code>/<code>4500</code></li>
</ul>
<p><strong>Traffic not routing:</strong></p>
<ul>
<li>Verify Remote Subnets setting in UniFi VPN configuration</li>
<li>Check firewall rules are not blocking VPN traffic</li>
</ul>
<p><strong>Health check fails:</strong></p>
<ul>
<li>Allow ICMP from Cloudflare to the customer-side tunnel IP</li>
<li>Target should be the <code>/31</code> interface IP, not your LAN gateway</li>
</ul>
<h2 id="policy-based-routing">Policy-based routing</h2>
<p>To route only specific devices through Cloudflare (UniFi Network Application):</p>
<ol>
<li>Remove unnecessary routes from Remote Subnets in your VPN configuration.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Policy Table</strong>.</li>
<li>Under <strong>Policy Engine</strong> select <strong>Create New Policy</strong> with the following settings:
<ul>
<li>Select <code>Route</code>.</li>
<li><strong>Name</strong>: Provide a name for the policy.</li>
<li><strong>Type</strong>: <em>Policy-Based</em>.</li>
<li><strong>Interface/VPN Tunnel</strong>: Select the VPN Tunnel (for example, <code>Cloudflare-Magic-WAN</code>).</li>
<li><strong>Kill Switch</strong>: <em>Enabled</em> (recommended).</li>
<li><strong>Source</strong>: Select <code>Device/Network</code> and then choose the Device(s) or Network(s).</li>
<li><strong>Destination</strong>: <em>Any</em>.</li>
<li><strong>Interface</strong>: Your VPN tunnel.</li>
</ul>
</li>
</ol>
<h2 id="next-steps">Next Steps</h2>
<ul>
<li>Use <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> for network policies.</li>
<li>Configure a second tunnel for redundancy.</li>
<li>Monitor traffic in the Cloudflare WAN dashboard.</li>
</ul>
<hr />
<p>You are now routing traffic through Cloudflare's network using Cloudflare WAN.</p>
