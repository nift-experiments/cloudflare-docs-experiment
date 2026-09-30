<p>Cloudflare WAN (formerly Magic WAN) can work together with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> to provide easy access between your networks and applications.</p>
<p>By default, <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> proxies and filters TCP, UDP, and ICMP traffic routed through IPsec/GRE tunnels and destined to routes behind Cloudflare Tunnel.</p>
<h2 id="route-evaluation-and-precedence">Route evaluation and precedence</h2>
<p>Cloudflare evaluates private network routes using longest-prefix-match. A prefix combines a base IP address with a prefix length that indicates how many bits define the network portion (for example, <code>192.168.0.0/24</code>). When multiple routes could match a destination IP, Cloudflare selects the route with the longest prefix (most specific match).</p>
<p>For example, if you have routes for both <code>10.0.0.0/16</code> and <code>10.0.1.0/24</code>, traffic destined for <code>10.0.1.50</code> matches the <code>/24</code> route because it is more specific.</p>
<h3 id="route-uniqueness">Route uniqueness</h3>
<p>Within a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">virtual network</a>, each prefix can only appear once in the Zero Trust routing table. You cannot create two Zero Trust routes with the same prefix pointing to different tunnels in the same virtual network.</p>
<p>To route the same prefix to different destinations, use separate <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">virtual networks</a>.</p>
<h3 id="reserved-ip-ranges">Reserved IP ranges</h3>
<p>Cloudflare reserves the following IP ranges for Zero Trust services:</p>
<table>
<thead>
<tr>
<th>IP range</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>100.64.0.0/12</code></td>
<td><a href="/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/">Cloudflare Source IPs</a></td>
</tr>
<tr>
<td><code>100.96.0.0/12</code></td>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-ips/">Device IPs</a></td>
</tr>
<tr>
<td><code>172.64.128.0/20</code></td>
<td><a href="/cloudflare-one/traffic-policies/egress-policies/host-selectors/">Initial resolved IPs</a></td>
</tr>
<tr>
<td><code>100.112.0.0/16</code></td>
<td><a href="/load-balancing/private-network/">Private Load Balancers</a></td>
</tr>
</tbody>
</table>
<p>Do not configure routes that overlap with these reserved ranges.</p>
<h3 id="interaction-with-wan-routes">Interaction with WAN routes</h3>
<p>If your account also uses WAN connections (IPsec, GRE, and CNI), route selection behavior depends on your routing mode.</p>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/traffic-steering/#route-evaluation-with-zero-trust-connections">Route evaluation with Zero Trust connections</a>.</p>
<h2 id="interaction-with-other-route-selection-mechanisms">Interaction with other route selection mechanisms</h2>
<p>Longest-prefix-match routing is the default route selection method. Other mechanisms can bypass or augment route evaluation.</p>
<h3 id="automatic-return-routing-arr">Automatic Return Routing (ARR)</h3>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/traffic-steering/#automatic-return-routing-beta">Automatic Return Routing</a> bypasses route lookup for return traffic.</p>
<p>When ARR is enabled:</p>
<ol>
<li>Cloudflare tags each flow with the source connection (tunnel or interconnect) when the flow is established.</li>
<li>For return traffic, Cloudflare routes packets back to the tagged source connection directly, bypassing the routing table.</li>
<li>This allows multiple sites to use identical private IP ranges without NAT or VRF configuration.</li>
</ol>
<p>ARR requires Unified Routing mode. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/traffic-steering/#automatic-return-routing-beta">Automatic Return Routing</a>.</p>
<h3 id="hostname-routes-initial-resolved-ips">Hostname Routes (Initial resolved IPs)</h3>
<p><a href="/cloudflare-one/traffic-policies/egress-policies/host-selectors/">Hostname-based routing</a> uses Gateway DNS to resolve hostnames to Initial resolved IPs, which then map to specific next hops.</p>
<p>When Hostname Routes are enabled:</p>
<ol>
<li>Gateway DNS resolves the hostname to an Initial resolved IP (from <code>172.64.128.0/20</code> by default).</li>
<li>The client sends traffic to the Initial resolved IP.</li>
<li>Cloudflare looks up the Initial resolved IP to determine the real destination IP and the assigned next hop (specific tunnel or interconnect).</li>
<li>Traffic is forwarded to the assigned next hop, bypassing route evaluation for next-hop selection.</li>
</ol>
<p>This enables hostname-based policies for non-HTTP traffic without requiring you to know destination IPs in advance.</p>
<h2 id="test-cloudflared-tunnel-integration">Test <code>cloudflared</code> tunnel integration</h2>
<p>To verify that a <code>cloudflared</code> tunnel works correctly with your Cloudflare WAN connection:</p>
<ol>
<li>From a host behind your customer premises equipment, open a browser.</li>
<li>Browse to an IP address or hostname that is reachable through a Cloudflare Tunnel private network route, such as the example destination <code>10.1.2.3</code>.</li>
<li>Confirm that the application loads as expected. If it does, Cloudflare Tunnel is handling the traffic as configured.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="run-traceroute">Run <code>traceroute</code></h3>
@markup("md", "content/.markup/bodies/5526.md")
</aside>
