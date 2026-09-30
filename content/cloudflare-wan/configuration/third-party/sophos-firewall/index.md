<p>This tutorial shows you how to use Cloudflare WAN (formerly Magic WAN) with the following versions of the Sophos Firewall:</p>
<ul>
<li>
<p><strong>Sophos form factor tested:</strong></p>
<ul>
<li>Sophos Firewall XGS and XG series hardware</li>
<li>Sophos Firewall virtual appliance on VMware</li>
</ul>
</li>
<li>
<p><strong>Sophos software versions tested:</strong></p>
<ul>
<li>SFOS Version 19.0 MR2-Build 472</li>
<li>SFOS Version 19.5.1 MR1-Build 278</li>
</ul>
</li>
</ul>
<p>You can connect through <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Generic Routing Encapsulation (GRE) or IPsec tunnels</a> to Cloudflare WAN.</p>
<h2 id="ipsec-connection">IPsec connection</h2>
<p>The following instructions show how to setup an IPsec connection on your Sophos Firewall device. Settings not explicitly mentioned can be left with their default values.</p>
<h3 id="1-add-an-ipsec-profile"><ol>
<li>Add an IPsec profile</li>
</ol></h3>
<ol>
<li>Go to <strong>System</strong> &gt; <strong>Profiles</strong>.</li>
<li>In <strong>IPsec profiles</strong>, select <strong>Add</strong>.</li>
<li>In the <strong>General settings</strong> group, make sure you have the following settings:
<ul>
<li><strong>Name</strong>: Give your profile a descriptive name.</li>
<li><strong>Key exchange</strong>: <strong>IKEv2</strong></li>
<li><strong>Authentication mode</strong>: <strong>Main mode</strong></li>
</ul>
</li>
<li>In the <strong>Phase 1</strong> group, make sure you have the following settings:
<ul>
<li><strong>DH group (key group)</strong>: <em>20</em></li>
<li><strong>Encryption</strong>: <em>AES256</em></li>
<li><strong>Authentication</strong>: <em>SHA2 256</em></li>
</ul>
</li>
<li>In the <strong>Phase 2</strong> group, select the following:
<ul>
<li><strong>PFS group (DH group)</strong>: <em>Same as phase-1</em></li>
<li><strong>Key life</strong>: <em>28800</em></li>
<li><strong>Encryption</strong>: <em>AES256</em></li>
<li><strong>Authentication</strong>: <em>SHA2 256</em></li>
</ul>
</li>
<li>Enable <strong>Dead Peer Detection</strong>.</li>
<li>In <strong>When peer unreachable</strong>, select <em>Re-initiate</em>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h3 id="2-create-ipsec-connection-tunnel"><ol start="2">
<li>Create IPsec connection tunnel</li>
</ol></h3>
<p>The next step involves configuring a site-to-site IPsec VPN connection on your Sophos Firewall device.</p>
<ol>
<li>Go to <strong>Configure</strong> &gt; <strong>Site-to-site VPN</strong>.</li>
<li>In <strong>IPsec</strong>, select <strong>Add</strong>.</li>
<li>In the <strong>General settings</strong> group, make sure you have the following settings:
<ul>
<li><strong>Name</strong>: Give your site-to-site VPN a descriptive name.</li>
<li><strong>Connection type</strong>: <em>Tunnel interface</em></li>
<li><strong>Gateway type</strong>: <em>Initiate the connection</em></li>
</ul>
</li>
<li>In the <strong>Encryption</strong> group, make sure you have the following settings:
<ul>
<li><strong>Authentication type</strong>: <strong>Preshared key</strong></li>
</ul>
</li>
<li>In <strong>Gateway settings</strong>, make sure you have the following settings:
<ul>
<li><strong>Gateway address</strong>: Enter one of the Cloudflare anycast IP addresses assigned to your account, available in <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space">Leased IPs</a>.</li>
<li><strong>Local ID type</strong>: Add the <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/#supported-ike-id-formats">IKE ID</a> provided by Cloudflare.</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/2-ipsec-tunnel.png" alt="Configure an IPsec tunnel." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<p>After setting up your IPsec tunnel, it will show up on the IPsec connections list with an <strong>Active</strong> status.</p>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/2b-ipsec-tunnel.png" alt="The IPsec tunnel should show up on the IPsec connections list." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<h3 id="3-assign-the-xfrm-interface-address"><ol start="3">
<li>Assign the XFRM interface address</li>
</ol></h3>
<p>You must use an interface address from the <code>/31</code> subnet required to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">configure tunnel endpoints</a> on Cloudflare WAN.</p>
<ol>
<li>Go to <strong>Configure</strong> &gt; <strong>Network</strong>.</li>
<li>In <strong>Interfaces</strong>, select the corresponding interface to the IPsec tunnel you created in <a href="#2-create-ipsec-connection-tunnel">step 2</a>.</li>
<li>Edit the interface to assign an address from the <code>/31</code> subnet required to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">configure tunnel endpoints</a>. When you are finished, it should look similar to the following:</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/3-xfrm-interface.png" alt="Configure a XFRM interface." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<h3 id="4-add-a-firewall-rule"><ol start="4">
<li>Add a firewall rule</li>
</ol></h3>
<ol>
<li>Go to <strong>Protect</strong> &gt; <strong>Rules and policies</strong>.</li>
<li>In <strong>Firewall rules</strong>, create a firewall rule with the criteria and security policies from your company that allows traffic to flow between Sophos and Cloudflare WAN.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/4-firewall-rule.png" alt="Create a firewall rule with the criteria and security policies from your company" /></p>
<h3 id="5-disable-ipsec-anti-replay"><ol start="5">
<li>Disable IPsec anti-replay</li>
</ol></h3>
<p>Disable IPsec Anti-Replay on your Sophos Firewall. Changing the anti-replay settings restarts the IPsec service, which causes tunnel-flap for all IPsec tunnels. This will also disable IPsec anti-replay protection for all VPN connections globally. Plan these changes accordingly.</p>
<p>Below are instructions on how to achieve this on SFOS version 19 and SFOS version 19.5:</p>
<h4 id="sfos-19-0-mr2-build-472-or-19-5-mr1-build278-or-later-versions">SFOS 19.0 MR2-Build 472 or 19.5 MR1-Build278 or later versions:</h4>
<ol>
<li>Sign in to the CLI.</li>
<li>Enter <strong>4</strong> to choose <strong>Device console</strong>, and enter the following command:</li>
</ol>
<pre><code class="language-bash">set vpn ipsec-performance anti-replay window-size 0&#10;</code></pre>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/5-sfos-19.png" alt="Access the CLI to disable anti-replay" /></p>
<h4 id="older-sfos-versions">Older SFOS versions</h4>
<p>Contact Sophos support.</p>
<h2 id="gre-connection">GRE connection</h2>
<h3 id="1-configure-a-gre-tunnel-between-sfos-and-cloudflare"><ol>
<li>Configure a GRE tunnel between SFOS and Cloudflare</li>
</ol></h3>
<p>Start by configuring a GRE tunnel between SFOS and the Cloudflare anycast IP address.</p>
<ol>
<li>Sign in to the CLI.</li>
<li>Enter <strong>4</strong> to choose <strong>Device console</strong>, and enter the following command:</li>
</ol>
<pre><code class="language-bash">system gre tunnel add name &lt;NAME_OF_YOUR_GRE_TUNNEL&gt; local-gw &lt;WAN_PORT&gt; remote-gw &lt;REMOTE_GATEWAY_IP_ADDRESS&gt; local-ip &lt;LOCAL_IP_ADDRESS&gt; remote-ip &lt;REMOTE_IP_ADDRESS&gt;&#10;</code></pre>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/1-gre-connection.png" alt="Access the CLI to configure a GRE tunnel" /></p>
<p>For more details, refer to the <a href="https://support.sophos.com/support/s/article/KB-000035813?language=en_US">Sophos Firewall knowledge base</a>.</p>
<h3 id="2-add-a-gre-or-sd-wan-route-to-redirect-traffic-through-the-gre-tunnel"><ol start="2">
<li>Add a GRE or SD-WAN route to redirect traffic through the GRE tunnel</li>
</ol></h3>
<p>Refer to <a href="#traffic-redirection-mechanism-on-sophos-firewall">Traffic redirection mechanism on Sophos Firewall</a> for information on how to add a GRE or SD-WAN route to redirect traffic through the GRE tunnel.</p>
<h3 id="3-add-a-firewall-rule-for-lan-dmz-to-vpn"><ol start="3">
<li>Add a firewall rule for LAN/DMZ to VPN</li>
</ol></h3>
<p>Create a firewall rule with the criteria and security policies from your company that allows traffic to flow between Sophos and Cloudflare WAN. This firewall rule should include the required networks and services.</p>
<ol>
<li>Go to <strong>Protect</strong> &gt; <strong>Rules and policies</strong>.</li>
<li>In <strong>Firewall rules</strong>, select <strong>IPv4</strong> &gt; <strong>Add firewall rule</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/4-firewall-rule.png" alt="Create a firewall rule with the criteria and security policies from your company" /></p>
<h2 id="traffic-redirection-mechanism-on-sophos-firewall">Traffic redirection mechanism on Sophos Firewall</h2>
<p>To redirect traffic, you can add a static or an SD-WAN route.</p>
<h3 id="ipsec">IPsec</h3>
<h4 id="static-route">Static route</h4>
<p>Go to <strong>Configure</strong> &gt; <strong>Routing</strong> &gt; <strong>Static routes</strong> to add an XFRM interface-based route. The interface will be automatically created when you set up a tunnel interface based on IPsec (such as the Cloudflare_MWAN example from above).</p>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/static-route.png" alt="Go to static routes to add an XFRM interface-based route" /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<h4 id="sd-wan-route">SD-WAN route</h4>
<ol>
<li>Go to <strong>Configure</strong> &gt; <strong>Routing</strong> &gt; <strong>Gateways</strong> to create a custom gateway on the XFRM interface. The interface will be automatically created when you set up a tunnel interface based on IPsec (such as the Cloudflare_MWAN example from above).</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/1-sd-wan-gateway.png" alt="Go to Gateways to add an XFRM interface-based route" /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<ol start="2">
<li>In <strong>Configure</strong> &gt; <strong>Routing</strong> &gt; <strong>SD-WAN routes</strong>, select <strong>Add</strong> to add the desired networks and services in the route to redirect traffic to Cloudflare. Enter a descriptive name for your connection, and the IP addresses you set up for your IPsec tunnels in <strong>Incoming interface</strong> and <strong>Source networks</strong>. Do not forget to choose the correct <strong>Primary gateway</strong> option.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/2-sd-wan-routes.png" alt="Go to SD-WAN to add the desired networks and services in the route." /></p>
<h3 id="gre">GRE</h3>
<p>Add a GRE route, an SD-WAN route, or both depending on your routing requirements.</p>
<h4 id="gre-route">GRE route</h4>
<p>Add the route on the CLI.</p>
<ol>
<li>Sign in to the CLI.</li>
<li>Enter <strong>4</strong> to choose <strong>Device console</strong>, and enter the following command to create the tunnel:</li>
</ol>
<pre><code class="language-bash">system gre route add net &lt;IP_ADDRESS&gt; tunnelname &lt;TUNNEL_NAME&gt;&#10;</code></pre>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/gre-route-cli.png" alt="Add the route on the CLI." /></p>
<h4 id="sd-wan-route-1">SD-WAN route</h4>
<ol>
<li>Add a custom gateway on GRE with the peer IP address (from the <code>/31</code> subnet you chose earlier) as the Gateway IP address, and disable <strong>Health check</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/sd-wan-1-gre.png" alt="Add a custom gateway on GRE." /></p>
<ol start="2">
<li>Add an SD-WAN route with the desired networks and services in the route to redirect traffic to Cloudflare.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/2-sd-wan-routes.png" alt="Add an SD-WAN route." /></p>
<h2 id="verify-tunnel-status-on-cloudflare-dashboard">Verify tunnel status on Cloudflare dashboard</h2>
<p>The Cloudflare dashboard monitors the health of all anycast tunnels on your account that route traffic from Cloudflare to your origin network. Refer to <a href="/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/">Check tunnel health in the dashboard</a> for more information.</p>
<h3 id="configure-cloudflare-health-checks">Configure Cloudflare health checks</h3>
<ol>
<li>The ICMP probe packet from Cloudflare must be the type ICMP request, with anycast source IP. In the following example, we have used <code>172.64.240.252</code> as a target example:</li>
</ol>
<pre><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/ipsec_tunnels/{tunnel_id} \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;health_check&quot;: {&#10;    &quot;enabled&quot;: true,&#10;    &quot;target&quot;: &quot;172.64.240.252&quot;,&#10;    &quot;type&quot;: &quot;request&quot;,&#10;    &quot;rate&quot;: &quot;mid&quot;&#10;  }&#10;}&#x27;&#10;</code></pre>
<ol start="2">
<li>Go to <strong>Configure</strong> &gt; <strong>Network</strong> &gt; <strong>Interfaces</strong> &gt; <strong>Add alias</strong>. Add the IP address provided by Cloudflare for the ICMP probe traffic. This is needed to prevent Sophos firewall from dropping them as spoof packets. This is not the same IP used to create VPN. This is the special IP address for probe traffic only.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/2-icmp-probe-firewall.png" alt="Add the IP address provided by Cloudflare to prevent the probe from being dropped by the firewall." /></p>
<ol start="3">
<li>ICMP reply from SFOS should go back via the same tunnel on which the probe packets are received. You will need to create an additional SD-WAN policy route.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/3-icmp-probe-reply.png" alt="Configure an SD-WAN route so the ICMP reply goes back to Cloudflare via the same tunnel." /></p>
<p>Packet flow will look like the following:</p>
<pre><code class="language-sh">tcpdump -nn proto 1&#10;</code></pre>
<pre><code class="language-sh">tcpdump: verbose output suppressed, use -v or -vv for full protocol decode&#10;listening on any, link-type LINUX_SLL (Linux cooked v1), capture size 262144 bytes&#10;&#10;13:09:55.500453 xfrm1, IN: IP 172.70.51.31 &gt; 172.64.240.252: ICMP echo request, id 33504, seq 0, length 64&#10;13:09:55.500480 xfrm1, OUT: IP 172.64.240.252 &gt; 172.70.51.31: ICMP echo reply, id 33504, seq 0, length 64&#10;&#10;13:09:55.504669 xfrm1, IN: IP 172.71.29.66 &gt; 172.64.240.252: ICMP echo request, id 60828, seq 0, length 64&#10;13:09:55.504695 xfrm1, OUT: IP 172.64.240.252 &gt; 172.71.29.66: ICMP echo reply, id 60828, seq 0, length 64&#10;</code></pre>
<h2 id="verify-tunnel-status-on-sophos-firewall-dashboard">Verify tunnel status on Sophos Firewall dashboard</h2>
<h3 id="ipsec-1">IPsec</h3>
<p>When the tunnel is working, its <strong>Status</strong> will be green.</p>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/2b-ipsec-tunnel.png" alt="If the tunnel is working, it will show up with a green status." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<p>The corresponding XFRM interface will also show a <strong>Connected</strong> status.</p>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/1-sd-wan-gateway.png" alt="The XFRM interface will also show a connected status." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<h3 id="gre-1">GRE</h3>
<p>Access the CLI and type <code>system gre tunnel show</code> to check the status of a GRE tunnel. When the tunnel is working, its status will show up as <strong>Enabled</strong>.</p>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/gre-status-enabled.png" alt="The GRE tunnel will show a status of Enabled when working." /></p>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/sophos-firewall/gre-status-enabled-b.png" alt="The GRE tunnel will show a status of Enabled when working." /></p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If a tunnel shows a connected status at both ends, but is not established:</p>
<ul>
<li>Check if the IPsec profile configuration is correct.</li>
<li>Make sure the corresponding tunnel interfaces are up.</li>
<li>Make sure routing configuration and route precedence are correctly set on SFOS.</li>
<li>Make sure a static back route is added on Cloudflare.</li>
<li>Firewall rules for specific zones and host or service must be added in SFOS. GRE and IPsec belong to the VPN zone.</li>
<li>Perform <code>tcpdump</code> to check if packets are going through the VPN or GRE tunnel as expected.</li>
<li>Perform a packet capture on Cloudflare to see if traffic is reaching the Cloudflare platform.</li>
</ul>
