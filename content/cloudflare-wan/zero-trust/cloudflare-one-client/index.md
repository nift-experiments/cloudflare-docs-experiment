<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6752.md")
</aside>
<p>Use <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">WARP</a> as an <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/6753.md")
</div> to Cloudflare WAN (formerly Magic WAN) and route traffic from user devices with the Cloudflare One Client installed to any network connected with Cloudflare Tunnel or IP-layer tunnels (<div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/6754.md")
</div> [GRE, IPsec](/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels), or [CNI](/network-interconnect/)). Take advantage of the integration between Cloudflare WAN and [Cloudflare Network Firewall](/cloudflare-network-firewall/) and enforce policies at Cloudflare's global network.
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you can begin using the Cloudflare One Client as an on-ramp to Cloudflare WAN, you must set up your <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Zero Trust account</a>.</p>
<h2 id="ip-ranges">IP ranges</h2>
<p>When connecting a device to Cloudflare WAN, you will have virtual IP addresses from the Cloudflare One Client, in the <code>100.96.0.0/12</code> range.</p>
<hr />
<h2 id="set-up-the-cloudflare-one-client-with-cloudflare-wan">Set up the Cloudflare One Client with Cloudflare WAN</h2>
<h3 id="1-route-packets-back-to-cloudflare-one-client-devices"><ol>
<li>Route packets back to Cloudflare One Client devices</li>
</ol></h3>
<p>Route packets back to Cloudflare One Client devices from services behind an anycast GRE or other type tunnel. Complete this configuration before installing WARP. Otherwise, your infrastructure will not route packets correctly to Cloudflare global network and connectivity will fail.</p>
<p>Cloudflare will assign IP addresses from the virtual IP (VIP) space to your devices. To view your virtual IP address, go to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select <strong>Zero Trust</strong> &gt; <strong>My Team &gt; Devices</strong>.</p>
<p>All packets with a destination IP in the VIP space need to be routed back through the tunnel. For example, with a single GRE tunnel named <code>gre1</code>, in Linux, the following command would add a routing rule that would route such packets:</p>
<pre><code class="language-sh">ip route add 100.96.0.0/12 dev gre1&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/6751.md")
</aside>
<h3 id="2-configure-split-tunnels"><ol start="2">
<li>Configure Split Tunnels</li>
</ol></h3>
<p>Configure <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a> from your Zero Trust account to only include traffic from the private IP addresses you want to access.</p>
<p>Optionally, you can configure Split Tunnels to include IP ranges or domains you want to use for connecting to public IP addresses.</p>
<h3 id="3-install-the-cloudflare-one-client-on-your-device"><ol start="3">
<li>Install the Cloudflare One Client on your device</li>
</ol></h3>
<p>Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">Deploy the Cloudflare One Client to your organization</a> for more information on whether to choose a manual or managed deployment.</p>
<p>You can now access private IP addresses specified in the Split Tunnel configuration.</p>
<p>You must log out and log back in with at least one device to ensure the configuration updates on your device.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="run-traceroute">Run <code>traceroute</code></h3>
@markup("md", "content/.markup/bodies/6750.md")
</aside>
<h2 id="double-encapsulation">Double encapsulation</h2>
<p>When a Cloudflare One Client user connects from a location (such as an office) with an IPsec/GRE tunnel already set up, Cloudflare One Client traffic is doubly encapsulated - first by the Cloudflare One Client and then by Cloudflare WAN. This is unnecessary, since each on-ramp method provides full Zero Trust protection.</p>
<p>Since Cloudflare One Client traffic is already protected on its own, set up Cloudflare WAN to exclude Cloudflare One Client traffic, sending it to the Internet through regular connections.</p>
<p>To learn which IP addresses and UDP ports you should exclude to accomplish this, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/#warp-ingress-ip">WARP ingress IP</a>.</p>
<h3 id="the-cloudflare-one-client-and-cloudflare-one-appliance">The Cloudflare One Client and Cloudflare One Appliance</h3>
<p>If you have Cloudflare One Appliance (formerly Magic WAN Connector) and Cloudflare One Clients deployed in your premises, Cloudflare One Appliance automatically routes Cloudflare One Client traffic to the Internet rather than Cloudflare WAN IPsec tunnels. This prevents traffic from being encapsulated twice.</p>
<p>You may need to configure your firewall to allow this new traffic. Make sure to allow the following IPs and ports:</p>
<ul>
<li><strong>Destination IPs</strong>: <code>162.159.193.0/24</code>, <code>162.159.197.0/24</code></li>
<li><strong>Destination ports</strong>: <code>443</code>, <code>500</code>, <code>1701</code>, <code>2408</code>, <code>4443</code>, <code>4500</code>, <code>8095</code>, <code>8443</code></li>
</ul>
<p>Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">Cloudflare One Client with firewall</a> for more information on this topic.</p>
<h2 id="test-cloudflare-one-client-integration">Test Cloudflare One Client integration</h2>
<p>Before testing, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#add-a-domain">configure domain fallback</a> for the server or service in the Cloudflare One Client settings. This is needed because by default Cloudflare Zero Trust excludes common top level domains used for local resolution from being sent to Gateway for processing.</p>
<p>If WARP integration has been enabled for the account within the last day, log off and on again in the Cloudflare One Client before testing.</p>
<p>To check if the Cloudflare One Client is working correctly as an on-ramp, you can do a resolution test on a <a href="https://en.wikipedia.org/wiki/Fully_qualified_domain_name">fully qualified domain name (FQDN)</a> for a server or service in the Cloudflare WAN. Test this from a user with a device.</p>
<p>For example:</p>
<pre><code class="language-sh">nslookup &lt;SERVER_BEHIND_CLOUDFLARE_WAN&gt;&#10;</code></pre>
<p>This DNS lookup should return a valid IP address associated with the server or service you are testing for.</p>
<p>Next, test with a browser that you can connect to a service on the WAN by opening a webpage that is only accessible on the WAN. Use the same server from the DNS lookup or another server in the WAN. Connecting using an IP address instead of a domain name should work.</p>
