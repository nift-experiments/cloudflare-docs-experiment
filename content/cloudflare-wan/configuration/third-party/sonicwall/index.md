<p>This tutorial shows you how to use Cloudflare WAN (formerly Magic WAN) with the following versions of the SonicWall appliances:</p>
<ul>
<li><strong>Hardware tested</strong>:
<ul>
<li>SonicWall NSv 470</li>
<li>SonicWall 3700</li>
</ul>
</li>
<li><strong>Software versions tested</strong>:
<ul>
<li>SonicOS 7.0.1</li>
</ul>
</li>
</ul>
<p>You can connect your SonicWall appliance through <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">IPsec tunnels</a> to Cloudflare WAN. Generic Routing Encapsulation (GRE) is not supported on SonicWall.</p>
<h2 id="topology">Topology</h2>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sonicwall/topology.png" alt="Topology diagram showing how to connect SonicWall appliances to Cloudflare WAN" /></p>
<p><em>Note: Labels in this image may reflect previous product names.</em></p>
<p>The following instructions show how to set up an IPsec connection on your SonicWall device. We will use the IP ranges from the above topology example to create the connections needed. Settings not explicitly mentioned can be left with their default values.</p>
<h2 id="1-create-an-ipsec-tunnel-on-your-cloudflare-account"><ol>
<li>Create an IPsec tunnel on your Cloudflare account</li>
</ol></h2>
<ol>
<li>
<p>Start by <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">creating your IPsec tunnels</a> on Cloudflare. Name and describe the tunnels as needed, and add the following settings:</p>
<ul>
<li><strong>Interface address</strong>: Enter the internal tunnel IP on the Cloudflare side of the IPsec tunnel. In this example, it is <code>10.200.1.0/31</code>.</li>
<li><strong>Customer endpoint</strong>: Enter the WAN IP address of your SonicWall device. In our example, this is <code>198.51.100.2</code>.</li>
<li><strong>Cloudflare endpoint</strong>: Enter one of the Cloudflare anycast IP addresses assigned to your account, available in <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space">Leased IPs</a>. In our example, this is <code>1.2.3.4</code>.</li>
<li><strong>Pre-shared key</strong>: Select <strong>Use my own pre-shared key</strong> and paste a secure key of your own.</li>
</ul>
</li>
<li>
<p>Select <strong>Add tunnels</strong> when you are finished.</p>
</li>
<li>
<p>After you create your tunnel, Cloudflare dashboard will load a list of tunnels set up for your account. Select the arrow to expand the tunnels you have just created, and check the following settings:</p>
<ul>
<li><strong>Customer endpoint</strong>: Refers to the SonicWall WAN IP that the VPN policy is bound to (in red).</li>
<li><strong>Cloudflare endpoint</strong>: Refers to the Cloudflare anycast IP address (in blue).</li>
<li><strong>FQDN ID</strong>: The ID used in the VPN policy for the SonicWall's Local IKE ID. Copy this ID and save it. You will need it when configuring the tunnel on your SonicWall (in green).</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sonicwall/step3.png" alt="An example of what your IPsec tunnel should look like" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6826.md")
</aside>
<h2 id="2-create-static-routes-on-cloudflare-dashboard"><ol start="2">
<li>Create static routes on Cloudflare dashboard</li>
</ol></h2>
<p>Static routes are required for any networks that will be reached via the IPsec tunnel. In our example, there are two networks: <code>172.31.3.0/24</code> and the tunnel network <code>10.200.1.0/31</code>.</p>
<ol>
<li>
<p><a href="/cloudflare-wan/configuration/how-to/configure-routes/#create-a-static-route">Create your static routes</a>. Name and describe them as needed, and add the following settings:</p>
<ul>
<li><strong>First tunnel</strong>: Following our example, add <code>10.200.1.0/31</code> as the <strong>Prefix</strong> and <code>10.200.1.1</code> for the <strong>Tunnel/Next hop</strong>.</li>
<li><strong>Second tunnel</strong>: Following our example, add <code>172.31.3.0/24</code> as the <strong>Prefix</strong> and <code>10.200.1.1</code> for the <strong>Tunnel/Next hop</strong>.</li>
</ul>
</li>
<li>
<p>Select <strong>Add routes</strong> when you are finished.</p>
</li>
</ol>
<h2 id="3-add-a-vpn-configuration-in-sonicwall"><ol start="3">
<li>Add a VPN configuration in SonicWall</li>
</ol></h2>
<ol>
<li>Go to <strong>Network</strong> &gt; <strong>IPsec VPN</strong> &gt; <strong>Rules and Settings</strong>.</li>
<li>Select <strong>Add</strong>.</li>
<li>In <strong>General</strong> &gt; <strong>Security Policy</strong> group, add the following settings:
<ul>
<li><strong>Authentication Method</strong>: <em>IKE Using Preshared Secret</em>.</li>
<li><strong>IPsec Primary Gateway Name or Address</strong>: Enter Cloudflare's anycast IP address for the primary gateway (in blue).</li>
</ul>
</li>
<li>In the <strong>IKE Authentication</strong> group, add the following settings:
<ul>
<li><strong>Shared secret</strong>: Paste the pre-shared key you use to create the IPsec tunnel in step 1 (in purple).</li>
<li><strong>Local IKE ID</strong>: Select <em>Domain name</em> from the drop-down menu, and paste here the <strong>FQDN ID</strong> you saved from step 1, after creating the IPsec tunnel (in green).</li>
<li><strong>Peer IKE IDE</strong>: Select <em>IPv4</em> Address from the drop-down menu, and enter the Cloudflare anycast IP address (in blue).</li>
</ul>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sonicwall/3-vpn-config.png" alt="Configure a VPN policy on your SonicWall device" /></p>
</div>
<ol start="5">
<li>Select <strong>Proposals</strong>. VPN Policy is somewhat flexible. Adjust these settings to match your organization's preferred security policy. As an example, you can use the settings in the examples below.</li>
<li>In the <strong>IKE (Phase 1) Proposal</strong> group, select the following settings:
<ul>
<li><strong>Exchange</strong>: <em>IKEv2 Mode</em></li>
<li><strong>DH Group</strong>: <em>Group 20</em></li>
<li><strong>Encryption</strong>: <em>AES-256</em></li>
<li><strong>Authentication</strong>: <em>SHA256</em></li>
<li><strong>Life Time (seconds)</strong>: <code>86400</code></li>
</ul>
</li>
<li>In the <strong>IPsec (Phase 2) Proposal</strong> group, add the following settings:
<ul>
<li><strong>Protocol</strong>: <em>ESP</em></li>
<li><strong>Encryption</strong>: <em>AESGCM16-256</em></li>
<li><strong>Authentication</strong>: <em>None</em></li>
<li><strong>Enable Perfect Forward Secrecy</strong>: Enabled</li>
<li><strong>DH Group</strong>: <em>Group 20</em></li>
<li><strong>Life Time (seconds)</strong>: <code>28800</code></li>
</ul>
</li>
<li>Select <strong>Advanced</strong>.</li>
<li>Enable <strong>Disable IPsec Anti-Replay</strong>.</li>
<li>In <strong>VPN Policy bound to</strong> select your WAN interface from the drop-down menu, to bind it to your VPN.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sonicwall/5-anti-replay.png" alt="Enable anti-replay on your SonicWall device" /></p>
</div>
<h2 id="4-add-a-vpn-tunnel-interface"><ol start="4">
<li>Add a VPN tunnel interface</li>
</ol></h2>
<p>SonicOS requires a VPN tunnel interface to route traffic via Cloudflare WAN. When creating the interface, use the prefix <code>10.200.1.1/31</code>. This matches with the Cloudflare side for this tunnel, which is <code>10.200.1.0</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6825.md")
</aside>
<ol>
<li>Go to <strong>Network</strong> &gt; <strong>System</strong> &gt; <strong>Interfaces</strong>.</li>
<li>Select <strong>Add interface</strong> &gt; <strong>VPN Tunnel Interface</strong>.</li>
<li>For IP Address, use <code>10.200.1.1</code>.</li>
<li>Enable <strong>Ping</strong>. This is required so the interface can be pinged for debugging and Cloudflare WAN health checks.</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sonicwall/6-vpn-ping.png" alt="Enable ping so that your interface can be pinged for debugging and Cloudflare WAN health checks" /></p>
</div>
<ol start="5">
<li>Select <strong>Advanced</strong>.</li>
<li>Enable the <strong>Enable Asymmetric Route Support</strong> option. This is required for the IPsec tunnel health check.</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sonicwall/6-vpn-assymetric.png" alt="Enable Asymmetric Route Support. It is required for Cloudflare WAN health checks" /></p>
</div>
<ol start="7">
<li>Select <strong>OK</strong>.</li>
</ol>
<h2 id="5-add-address-object-s"><ol start="5">
<li>Add address object(s)</li>
</ol></h2>
<p>Address objects are necessary for route policies. In our example, we have one other site that will be reached via Cloudflare WAN. First, you need to create address objects for each network. Then, you need to create an address group that contains all the remote networks. This address group will be used in the next step to create the correct route policies.</p>
<p>To add an address object:</p>
<ol>
<li>Select <strong>Object</strong> &gt; <strong>Match Objects</strong> &gt; <strong>Addresses</strong>.</li>
<li>Select <strong>Address Objects</strong> &gt; <strong>Add</strong>.</li>
<li>Enter the information for your address object - refer to the topology image for the examples this tutorial is using. Since the addresses are in the VPN zone, set the <strong>Zone Assignment</strong> for the object to <em>VPN</em>.</li>
<li>Select <strong>Save</strong>. The window will stay on to facilitate multiple entries. Select <strong>X</strong> to close it.</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sonicwall/7-address-objects-settings.png" alt="Enter the appropriate settings for your object" /></p>
</div>
<ol start="5">
<li>Select <strong>Address Groups</strong> &gt; <strong>Add</strong> to add a new address group.</li>
<li>Enter a <strong>Name</strong> for your address group.</li>
<li>Select the individual network objects you have created on the left menu, and add them to the group by selecting the right-facing arrow in the middle column.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sonicwall/7-add-objects-group.png" alt="Copy the individual network objects and add them to your group" /></p>
</div>
<h2 id="6-set-up-routing"><ol start="6">
<li>Set up routing</li>
</ol></h2>
<p>Add a route using the address object or group just created as the destination.</p>
<ol>
<li>Select <strong>Policy</strong> &gt; <strong>Rules and Policies</strong> &gt; <strong>Routing Rules</strong>.</li>
<li>Select <strong>Add</strong> to add your route policy.</li>
<li>The <strong>Next Hop</strong> should be the VPN tunnel interface that was previously created in the interface panel.</li>
</ol>
<h2 id="7-add-access-rule-for-health-checks"><ol start="7">
<li>Add access rule for health checks</li>
</ol></h2>
<p>An additional access rule is required for Cloudflare WAN health checks to work properly. This will enable the WAN IP to receive ICMP pings via the tunnel, and return them over the WAN.</p>
<ol>
<li>Select <strong>Policy</strong> &gt; <strong>Rules and Policies</strong>.</li>
<li>Select <strong>Access Rules</strong> &gt; <strong>Add</strong>.</li>
<li>Enter a descriptive name for your policy.</li>
<li>In <strong>Source / Destination</strong> &gt; <strong>Destination &gt; Port/Services</strong>, select <em>ICMP</em> from the drop-down menu.</li>
<li>Select <strong>Optional Settings</strong>.</li>
<li>In <strong>Others</strong>, enable <strong>Allow Management traffic</strong>.</li>
</ol>
<h2 id="8-setup-health-checks"><ol start="8">
<li>Setup health checks</li>
</ol></h2>
<p>You have to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">configure Cloudflare WAN health checks</a> correctly. Here is an example of how to set up health checks:</p>
<pre><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/ipsec_tunnels/{tunnel_id} \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;health_check&quot;: {&#10;    &quot;direction&quot;: &quot;bidirectional&quot;,&#10;    &quot;enabled&quot;: true,&#10;    &quot;type&quot;: &quot;request&quot;,&#10;    &quot;rate&quot;: &quot;low&quot;&#10;  }&#10;}&#x27;&#10;</code></pre>
<p>Health checks might take some time to stabilize after the configuration is changed.</p>
<h2 id="9-verify-tunnel-status-on-cloudflare-dashboard"><ol start="9">
<li>Verify tunnel status on Cloudflare dashboard</li>
</ol></h2>
<p>The Cloudflare dashboard monitors the health of all anycast tunnels on your account that route traffic from Cloudflare to your origin network. Refer to <a href="/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/">Check tunnel health in the dashboard</a> for more information.</p>
