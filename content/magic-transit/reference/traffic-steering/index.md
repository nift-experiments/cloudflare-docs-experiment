<h2 id="magic-transit-virtual-network-routing-table">Magic Transit Virtual Network routing table</h2>
<p>When traffic enters Cloudflare's network, it needs to reach the correct destination in your infrastructure — a specific data center, office, or cloud environment. Traffic steering controls how Cloudflare makes these routing decisions.</p>
<p>The Magic Transit Virtual Network is a virtual network overlay, private to your account, that spans all Cloudflare data centers globally. This overlay network provides:</p>
<ul>
<li>Magic Transit delivery for <a href="/ddos-protection/">Denial of Service (DoS)</a> and <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> filtered Internet traffic, from the entry data center where the traffic ingressed, to your publicly addressed edge/border network.</li>
<li>Magic Transit packet transport between IPsec/GRE tunnels, interconnects, <a href="/load-balancing/">Cloudflare Load Balancer</a>, and <a href="/cloudflare-one/">Zero Trust</a> connections such as <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>, <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation</a>, <a href="/cloudflare-one/access-controls/policies/">Access</a>, and <a href="/cloudflare-one/traffic-policies/">Gateway</a>.</li>
</ul>
<p>The Magic Transit Virtual Network supports routing the Magic Transit traffic through anycast tunnels using <a href="/magic-transit/reference/gre-ipsec-tunnels/">GRE and Internet Protocol Security (IPsec)</a> or <a href="/network-interconnect/">CNI with Dataplane v2</a>. You can add entries to the Magic Transit Virtual Network routing table through static route configuration or through routes learned through BGP peering (beta).</p>
<h3 id="allowed-ip-ranges">Allowed IP ranges</h3>
<p>The following IPv4 address ranges are allowed in the Magic Transit Virtual Network routing table:</p>
<ul>
<li><a href="/byoip/">BYOIP</a> public address space which you have onboarded to Cloudflare Magic Transit.</li>
<li>Cloudflare <a href="/magic-transit/cloudflare-ips/">leased IPs</a> assigned to your account.</li>
</ul>
<h3 id="default-routing">Default routing</h3>
<p>If traffic does not match any route you have configured in the virtual network, Cloudflare applies default behavior based on the destination address type:</p>
<ul>
<li><strong>Public (Internet-routable) addresses</strong>: Traffic exits to the Internet.</li>
<li><strong>Private addresses</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918</a> or <a href="https://datatracker.ietf.org/doc/html/rfc6598">CGNAT/RFC 6598</a>): Traffic is dropped (null routed), because private addresses are not routable on the public Internet and Cloudflare has no path to deliver them without a matching route.</li>
</ul>
<h3 id="route-prioritization">Route prioritization</h3>
<p>Magic Transit steers traffic along tunnel routes based on route entry priorities.</p>
<ul>
<li>Lower values have greater priority.</li>
<li>When the priority values for prefix entries match, Cloudflare uses <a href="#equal-cost-multi-path-routing">equal-cost multi-path (ECMP)</a> packet forwarding to route traffic. You can apply an optional weight value to static routes to <a href="#set-priority-and-weights-for-static-routes">modify ECMP tunnel distribution</a>.</li>
<li>Cloudflare routing applies longest-prefix match. A more specific static route (like <code>/30</code>) always takes precedence over a less specific one (like <code>/29</code>), regardless of tunnel priority — unless you remove the more specific route.</li>
<li>When BGP and static routes have the same prefix and priority, Cloudflare enforces priority by preferring static routes over BGP routes. This ensures that manually configured static routes take precedence unless you explicitly deprioritize them.</li>
</ul>
<h3 id="set-priority-and-weights-for-static-routes">Set priority and weights for static routes</h3>
<p>The priority value for static routes is directly configured as part of the route object in the Cloudflare <a href="/magic-transit/how-to/configure-routes/#create-a-static-route">dashboard or through the API</a>. For example:</p>
<table>
<thead>
<tr>
<th>Prefix</th>
<th>NextHop</th>
<th>Priority</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>10.10.10.100/24</code></td>
<td><code>TUNNEL_1_IAD</code></td>
<td><code>200</code></td>
</tr>
<tr>
<td><code>10.10.10.100/24</code></td>
<td><code>TUNNEL_2_IAD</code></td>
<td><code>200</code></td>
</tr>
<tr>
<td><code>10.10.10.100/24</code></td>
<td><code>TUNNEL_3_ATL</code></td>
<td><code>100</code></td>
</tr>
<tr>
<td><code>10.10.10.100/24</code></td>
<td><code>TUNNEL_4_ATL</code></td>
<td><code>100</code></td>
</tr>
</tbody>
</table>
<p>In this example, tunnels with priority of <code>100</code> are preferred to tunnels with priority of <code>200</code> because lower numbers have greater priority.</p>
<p>Optionally, you can assign weights to distribute traffic more effectively among multiple tunnels. Weight values determine traffic proportion, with higher weights receiving more traffic. The maximum weight value is <code>256</code>.</p>
<p>In the following example, <code>TUNNEL_2_IAD</code> is likely to receive twice as much traffic as <code>TUNNEL_1_IAD</code>.</p>
<table>
<thead>
<tr>
<th>Prefix</th>
<th>NextHop</th>
<th>Priority</th>
<th>Weight</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>10.10.10.100/24</code></td>
<td><code>TUNNEL_1_IAD</code></td>
<td><code>100</code></td>
<td><code>64</code></td>
</tr>
<tr>
<td><code>10.10.10.100/24</code></td>
<td><code>TUNNEL_2_IAD</code></td>
<td><code>100</code></td>
<td><code>128</code></td>
</tr>
<tr>
<td><code>10.10.10.100/24</code></td>
<td><code>TUNNEL_3_ATL</code></td>
<td><code>100</code></td>
<td><code>192</code></td>
</tr>
<tr>
<td><code>10.10.10.100/24</code></td>
<td><code>TUNNEL_4_ATL</code></td>
<td><code>100</code></td>
<td><code>255</code></td>
</tr>
</tbody>
</table>
<p>Aside from priority, scoping static routes to specific geographic regions also impacts how traffic is steered. Refer to <a href="#scoping-routes-to-specific-regions">Scoping routes to specific regions</a> for more details.</p>
<h3 id="set-priority-for-bgp-routes">Set priority for BGP routes</h3>
<p>When BGP advertises a route, Cloudflare automatically adds it to the Magic Transit Virtual Network routing table with a default priority of <code>100</code> which applies to <a href="#scoping-routes-to-specific-regions">all regions</a>. However, if a static route exists with the same prefix and priority, the static route always takes precedence over the BGP route. Set a different priority for static routes (more or less than <code>100</code>) depending on which you want to prioritize. Lower values have greater priority.</p>
<p>Additionally, when multiple BGP routes exist with the same prefix length and priority, ECMP distributes traffic across them using <a href="#equal-cost-multi-path-routing">equal-cost multi-path (ECMP) routing</a>.</p>
<h3 id="change-route-priorities-with-bgp-attributes">Change route priorities with BGP attributes</h3>
<p>Cloudflare supports traffic engineering through BGP communities and AS prepending. You can use these traffic routing techniques to set route priorities and perform traffic engineering across multiple interconnects.</p>
<h4 id="bgp-communities-for-setting-route-priority">BGP communities for setting route priority</h4>
<p>The default BGP route priority is <code>100</code>. This base priority can be adjusted using communities. For example, when a route is tagged with the community <code>13335:60010</code> its priority is set to <code>10</code>. This makes it a higher priority than the default of <code>100</code> because lower numeric priorities are preferred.</p>
<p>The community values supported for setting base route priority are:</p>
<ul>
<li><code>13335:60010</code>: Set base route priority to <code>10</code></li>
<li><code>13335:60050</code>: Set base route priority to <code>50</code></li>
<li><code>UNSET</code>: Set base route priority to <code>100</code></li>
<li><code>13335:60150</code>: Set base route priority to <code>150</code></li>
<li><code>13335:60200</code>: Set base route priority to <code>200</code></li>
<li><code>13335:60901</code>: Set base route priority to <code>501000</code></li>
<li><code>13335:60902</code>: Set base route priority to <code>1001000</code></li>
</ul>
<p>Setting multiple base priority communities in the same prefix update message is a misconfiguration. In this situation, Cloudflare prefers the highest priority (lowest integer value).</p>
<h4 id="as-path-prepending-for-adjusting-route-priority">AS path prepending for adjusting route priority</h4>
<p>For each additional mention of your ASN in the received AS path, Cloudflare adds <code>10</code> to the route's base priority. By increasing the priority number, the route becomes less preferred.</p>
<p>For example, if your ASN is <code>65000</code> then the <code>BGP UPDATE</code> to Cloudflare will be:</p>
<pre><code class="language-txt">&#35; No change to base priority.&#10;AS_PATH: 65000 65200&#10;&#10;&#35; Add 10 to base priority for 1 prepend of 65000&#10;AS_PATH: 65000 65000 65200&#10;&#10;&#35; Add 20 to base priority for 2 prepend of 65000&#10;AS_PATH: 65000 65000 65000 65200&#10;</code></pre>
<h4 id="how-communities-and-prepends-work-together">How communities and prepends work together</h4>
<p>Cloudflare adjusts route priority when using AS prepending with communities. For example, if a route is tagged with <code>13335:60150</code>, the base priority is set to <code>150</code>. If you prepend your ASN twice, Cloudflare adds <code>10</code> for each prepend, increasing the route priority to <code>180</code>.</p>
<h2 id="unified-routing-mode-beta">Unified Routing mode (beta)</h2>
<p>The Unified Routing mode is the newer Cloudflare One data plane that uses a single routing fabric for all supported connection types. Unified Routing mode routes traffic across the Cloudflare One Client, Cloudflare Tunnel, IPsec, GRE, and Cloudflare Network Interconnect (CNI) in a single system, making it easier to set up your Cloudflare One connections.</p>
<p>In the Magic Transit dashboard, routing mode appears where you manage routes:</p>
<ul>
<li><strong>Routing mode: Unified</strong> — your account is on the unified data plane and supports the new routing features.</li>
<li><strong>Routing mode: Legacy</strong> — your account uses the previous data plane and does not support all unified routing features.</li>
</ul>
<h3 id="why-use-unified-routing">Why use Unified Routing</h3>
<p>Unified Routing is the future of the dedicated virtual network overlay that powers Magic Transit and Cloudflare One network connectivity.</p>
<p>For Magic Transit customers, the primary reason to consider Unified Routing is to evaluate <a href="#release-status">BGP for IPsec/GRE tunnels</a>, which depends on Unified Routing.</p>
<h3 id="beta-limitations">Beta limitations</h3>
<p>The following limitations apply to accounts using Unified Routing mode. This list will get shorter as Cloudflare adds support for additional features.</p>
<table>
<thead>
<tr>
<th>Current beta limitations</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr>
<td>Performance</td>
<td>Typically around 150 Mbps for each onramp</td>
</tr>
<tr>
<td>Basic packet captures</td>
<td>Captures exclude Automatic Return Routing or BGP-over-tunnels traffic</td>
</tr>
<tr>
<td>Full packet captures</td>
<td>Not yet supported</td>
</tr>
<tr>
<td>Cloudflare Advanced Network Firewall features: ASN Lists, Rate Limiting, Managed Rulesets</td>
<td>Not yet supported</td>
</tr>
<tr>
<td>Gateway filtering rules</td>
<td>Not supported on traffic where both the onramp and offramp is IPsec/GRE/CNI</td>
</tr>
<tr>
<td>Load Balancer</td>
<td>Public-to-private use case is supported to IPsec/GRE/CNI destinations. Private-to-private use case does not yet support Cloudflare Source IPs</td>
</tr>
<tr>
<td>IPv6 Support</td>
<td>IPv6 is supported for IPsec and GRE. Basic Network Firewall support for IPv6 is limited to src/dst IP filtering</td>
</tr>
</tbody>
</table>
<h3 id="enroll-in-the-unified-routing-beta">Enroll in the Unified Routing beta</h3>
<p>Unified Routing is currently in closed beta. To sign up:</p>
<ul>
<li><strong>Existing Cloudflare WAN or Magic Transit customers</strong>: Cloudflare recommends you evaluate the new functionality with your use case in a non-production account. Contact your account team to enable Unified Routing.</li>
<li><strong>New customers</strong>: Contact your account team to enable Unified Routing in a proof-of-concept for your use case.</li>
</ul>
<h2 id="scoping-routes-to-specific-regions">Scoping routes to specific regions</h2>
<p>If you have multiple connectivity paths to a network segment and want to apply different route prioritization based on where traffic arrives at the Cloudflare network, you can scope routes to specific Cloudflare data center regions. This is useful if you run your own anycast network and want your end-user traffic to arrive at your network location closest to the user.</p>
<p>When you scope a route to a Cloudflare data center region, it only shows up in the Magic Transit Virtual Network routing table in that region, along with all global routes that do not have any region scope. Route prioritization and ECMP logic apply across both region-scoped and global routes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10599.md")
</aside>
<p>When using region-scoped routes, ensure that all prefixes have routes covering all regions. Otherwise, traffic may arrive at a Cloudflare region that is not covered by any route, in which case Cloudflare drops the traffic.</p>
<p>The following table exemplifies how to use geographic scoping for routes:</p>
<table>
<thead>
<tr>
<th>Prefix</th>
<th>NextHop</th>
<th>Priority</th>
<th>Region code</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>10.10.10.100/24</code></td>
<td><code>TUNNEL_1_IAD</code></td>
<td><code>100</code></td>
<td><code>AFR</code></td>
</tr>
<tr>
<td><code>10.10.10.100/24</code></td>
<td><code>TUNNEL_2_IAD</code></td>
<td><code>100</code></td>
<td><code>EEUR</code></td>
</tr>
<tr>
<td><code>10.10.10.100/24</code></td>
<td><code>TUNNEL_3_ATL</code></td>
<td><code>100</code></td>
<td><code>ENAM</code></td>
</tr>
<tr>
<td><code>10.10.10.100/24</code></td>
<td><code>TUNNEL_4_ATL</code></td>
<td><code>100</code></td>
<td><code>ME</code></td>
</tr>
<tr>
<td><code>10.10.10.100/24</code></td>
<td><code>TUNNEL_5_ATL</code></td>
<td><code>100</code></td>
<td><code>WNAM</code></td>
</tr>
<tr>
<td><code>10.10.10.100/24</code></td>
<td><code>TUNNEL_4_ATL</code></td>
<td><code>100</code></td>
<td><code>ENAM</code></td>
</tr>
</tbody>
</table>
<p>When there are multiple routes to the same prefix with equal priority, and those routes are assigned to different geographic regions (like WNAM and ENAM), traffic entering the network in a specific region — for example, WNAM — egresses through the route associated with that same region.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="anycast-routing">Anycast routing</h3>
@markup("md", "content/.markup/bodies/10598.md")
</aside>
<h3 id="region-codes-and-associated-regions">Region codes and associated regions</h3>
<p>Cloudflare has nine geographic regions:</p>
<table>
<thead>
<tr>
<th>Region code</th>
<th>Region</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>AFR</code></td>
<td>Africa</td>
</tr>
<tr>
<td><code>APAC</code></td>
<td>Asia Pacific</td>
</tr>
<tr>
<td><code>EEUR</code></td>
<td>Eastern Europe</td>
</tr>
<tr>
<td><code>ENAM</code></td>
<td>Eastern North America</td>
</tr>
<tr>
<td><code>ME</code></td>
<td>Middle East</td>
</tr>
<tr>
<td><code>OC</code></td>
<td>Oceania</td>
</tr>
<tr>
<td><code>SAM</code></td>
<td>South America</td>
</tr>
<tr>
<td><code>WEUR</code></td>
<td>Western Europe</td>
</tr>
<tr>
<td><code>WNAM</code></td>
<td>Western North America</td>
</tr>
</tbody>
</table>
<p>Configure scoping for your traffic in the <strong>Region code</strong> section when adding or editing a static route. Refer to <a href="/magic-transit/how-to/configure-routes/#create-a-static-route">Create a static route</a> and <a href="/magic-transit/how-to/configure-routes/#edit-a-static-route">Edit a static route</a> for more information.</p>
<h2 id="magic-transit-prefix-mapping">Magic Transit prefix mapping</h2>
<h3 id="map-route-prefixes-smaller-than-24">Map route prefixes smaller than /24</h3>
<p>You must provide your prefixes and the tunnels that should be mapped to for Cloudflare to route your traffic from our global network to your data centers through anycast tunnels. Use the following table as reference.</p>
<table>
<thead>
<tr>
<th>Prefix</th>
<th>NextHop</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>103.21.244.0/29</code></td>
<td><code>TUNNEL_1_IAD</code></td>
</tr>
<tr>
<td><code>103.21.244.8/29</code></td>
<td><code>TUNNEL_2_ATL</code></td>
</tr>
</tbody>
</table>
<p>The minimum advertising prefix is <code>/24</code>, but because Cloudflare uses anycast tunnels as an outer wrapper for your traffic, Cloudflare can route prefixes within that <code>/24</code> to different tunnel endpoints. For example, you can send <code>x.x.x.0/29</code> to Data Center 1 and <code>x.x.x.8/29</code> to Data Center 2. This is helpful when you operate in an environment with constrained IP resources.</p>
<h3 id="map-route-prefixes-bigger-than-onboarded-prefixes">Map route prefixes bigger than onboarded prefixes</h3>
<p>If you have multiple onboarded <code>/24</code> subnets that belong to a larger contiguous block, you can configure a summary static route for the corresponding supernet (like a <code>/23</code> or a <code>/22</code>) instead of adding each <code>/24</code> individually. This eliminates the need to configure each <code>/24</code> route, as all traffic will be routed through the same GRE tunnels.</p>
<p>For example, if you have two tunnels:</p>
<ul>
<li><code>192.0.2.0/24</code></li>
<li><code>192.0.3.0/24</code></li>
</ul>
<p>You can summarize these into a single <code>192.0.2.0/23</code>.</p>
<p>Refer to <a href="/magic-transit/how-to/configure-tunnel-endpoints/#add-tunnels">Add tunnels</a> to learn more about configuring GRE tunnels.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10600.md")
</aside>
<h2 id="equal-cost-multi-path-routing">Equal-cost multi-path routing</h2>
<p>Equal-cost multi-path routing uses hashes calculated from <a href="https://www.cloudflare.com/learning/network-layer/what-is-a-packet/">packet</a> data to determine the route chosen. The hash always uses the source and destination IP addresses. For TCP and UDP packets, the hash includes the source and destination ports as well. The ECMP algorithm divides the hash for each packet by the number of equal-cost next hops. The modulus (remainder) determines the route the packet takes.</p>
<p>Using ECMP has a number of consequences:</p>
<ul>
<li>Routing to equal-cost paths is probabilistic.</li>
<li>Packets in the same session with the same source and destination have the same hash. The packets also use the same next hop.</li>
<li>Routing changes in the number of equal-cost next hops can cause traffic to use different tunnels. For example, dynamic reprioritization triggered by health check events can cause traffic to use different tunnels.</li>
</ul>
<p>As a result, ECMP provides load balancing across tunnels with the same prefix and priority.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10597.md")
</aside>
<h3 id="examples">Examples</h3>
<p>This diagram illustrates how ECMP distributes traffic equally across two paths with the same prefix and priority.</p>
<h4 id="normal-traffic-flow">Normal traffic flow</h4>
<pre><code class="language-mermaid">flowchart LR&#10;accTitle: Tunnels diagram&#10;accDescr: This example has three tunnel routes, with traffic equally distributed across two paths.&#10;&#10;subgraph Cloudflare&#10;direction LR&#10;B[Cloudflare &lt;br&gt; data center]&#10;C[Cloudflare &lt;br&gt; data center]&#10;D[Cloudflare &lt;br&gt; data center]&#10;end&#10;&#10;Z(&quot;Load balancing for some &lt;br&gt; priority tunnels uses ECMP &lt;br&gt; (hashing on src IP, dst IP, &lt;br&gt; scr port, dst port)&quot;) --- Cloudflare&#10;A((User)) --&gt; Cloudflare --- E[Anycast IP]&#10;E[Anycast IP] --&gt; F[/&quot;GRE Tunnel 1 / &lt;br&gt; priority 1 / &lt;br&gt; ~50% of flows&quot;/] --&gt; I{{Customer &lt;br&gt; data center/ &lt;br&gt; network 1}}&#10;E[Anycast IP] --&gt; G[/&quot;GRE Tunnel 2 / &lt;br&gt; priority 1 / &lt;br&gt; ~50% of flows&quot;/] --&gt; J{{Customer &lt;br&gt; data center/ &lt;br&gt; network 2}}&#10;E[Anycast IP] --&gt; H[/GRE Tunnel 3 / &lt;br&gt; priority 2 / &lt;br&gt; 0% of flows/] --o K{{Customer &lt;br&gt; data center/ &lt;br&gt; network 3}}&#10;</code></pre>
<h4 id="failover-traffic-flow-scenario-1">Failover traffic flow: Scenario 1</h4>
<p><strong>Customer router failure</strong></p>
<p>When Magic Transit health checks determine that Tunnel 2 is unhealthy, Magic Transit dynamically de-prioritizes that route, leaving Tunnel 1 as the sole top-priority route. As a result, Magic Transit steers traffic away from Tunnel 2, and all traffic flows to Tunnel 1.</p>
<pre><code class="language-mermaid">flowchart LR&#10;accTitle: Tunnels diagram&#10;accDescr: This example has Tunnel 2 unhealthy, and all traffic prioritized to Tunnel 1.&#10;&#10;subgraph Cloudflare&#10;direction LR&#10;B[Cloudflare &lt;br&gt; data center]&#10;C[Cloudflare &lt;br&gt; data center]&#10;D[Cloudflare &lt;br&gt; data center]&#10;end&#10;&#10;Z(Tunnel health is &lt;br&gt; determined by &lt;br&gt; health checks that &lt;br&gt; run from all Cloudflare &lt;br&gt; data centers) --- Cloudflare&#10;A((User)) --&gt; Cloudflare --- E[Anycast IP]&#10;E[Anycast IP] --&gt; F[/&quot;Tunnel 1 / &lt;br&gt; priority 1 / &lt;br&gt; ~100% of flows&quot;/]:::green --&gt; I{{Customer &lt;br&gt; data center/ &lt;br&gt; network 1}}&#10;E[Anycast IP] --&gt; G[/Tunnel 2 / &lt;br&gt; priority 3 / &lt;br&gt; unhealthy / 0% of flows/]:::red --x J{{Customer &lt;br&gt; data center/ &lt;br&gt; network 2}}&#10;E[Anycast IP] --&gt; H[/Tunnel 3 / &lt;br&gt; priority 2 / &lt;br&gt; 0% of flows/] --o K{{Customer &lt;br&gt; data center/ &lt;br&gt; network 3}}&#10;classDef red fill:#EE4B2B,color: black&#10;classDef green fill:#00FF00,color: black&#10;</code></pre>
<h4 id="failover-traffic-flow-scenario-2">Failover traffic flow: Scenario 2</h4>
<p><strong>Intermediary Internet Service Provider (ISP) failure</strong></p>
<p>When Magic Transit determines that Tunnel 1 is unhealthy as well, that route is also de-prioritized, leaving Tunnel 3 with the top priority route. In that case, all traffic flows to Tunnel 3.</p>
<pre><code class="language-mermaid">flowchart LR&#10;accTitle: Tunnels diagram&#10;accDescr: This example has Tunnel 1 and 2 unhealthy, and all traffic prioritized to Tunnel 3.&#10;&#10;subgraph Cloudflare&#10;direction LR&#10;B[Cloudflare &lt;br&gt; data center]&#10;C[Cloudflare &lt;br&gt; data center]&#10;D[Cloudflare &lt;br&gt; data center]&#10;end&#10;&#10;Z(Lower-priority tunnels &lt;br&gt; are used when &lt;br&gt; higher-priority tunnels &lt;br&gt; are unhealthy) --- Cloudflare&#10;A((User)) --&gt; Cloudflare --- E[Anycast IP]&#10;E[Anycast IP]  -- Intermediary &lt;br&gt; network issue --&gt;  F[/Tunnel 1 / &lt;br&gt; priority 3 / &lt;br&gt; unhealthy / 0% of flows/]:::red --x I{{Customer &lt;br&gt; data center/ &lt;br&gt; network 1}}&#10;E[Anycast IP]  -- Intermediary &lt;br&gt; network issue --&gt;  G[/Tunnel 2 / &lt;br&gt; priority 3 / &lt;br&gt; unhealthy / 0% of flows/]:::red --x J{{Customer &lt;br&gt; data center/ &lt;br&gt; network 2}}&#10;E[Anycast IP] --&gt;  H[/Tunnel 3 / &lt;br&gt; priority 2 / &lt;br&gt; 100% of flows/]:::green --&gt; K{{Customer &lt;br&gt; data center/ &lt;br&gt; network 3}}&#10;classDef red fill:#EE4B2B,color: black&#10;classDef green fill:#00FF00,color: black&#10;</code></pre>
<p>When Magic Transit determines that Tunnels 1 and 2 are healthy again, it re-prioritizes those routes, and traffic flow returns to normal.</p>
<h3 id="ecmp-and-bandwidth-utilization">ECMP and bandwidth utilization</h3>
<p>Because ECMP is probabilistic, the algorithm routes roughly the same number of flows through each tunnel. However, it does not consider the amount of traffic already sent through a tunnel when deciding where to route the next packet.</p>
<p>For example, consider a scenario with many very low-bandwidth TCP connections and one very high-bandwidth TCP connection. Packets for the high-bandwidth connection have the same hash and thus use the same tunnel. As a result, that tunnel utilizes greater bandwidth than the others.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10596.md")
</aside>
<h2 id="bgp-information">BGP information</h2>
<p>Using BGP peering with your Cloudflare One or Magic Transit Virtual Network routing table allows you to:</p>
<ul>
<li>Automate the process of adding or removing networks and subnets.</li>
<li>Take advantage of failure detection and session recovery features.</li>
</ul>
<p>With this functionality, you can:</p>
<ul>
<li>Establish an eBGP session between your devices and the Magic Transit service when connected through CNI, GRE or IPsec tunnels.</li>
<li>Secure the session by MD5 authentication to prevent misconfigurations.</li>
<li>Exchange routes dynamically between your devices and your Magic Transit Virtual Network routing table.</li>
</ul>
<h3 id="release-status">Release status</h3>
<p>The following table outlines the current availability and recommended use cases for BGP across different connectivity methods.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Release stage</th>
<th>Recommended use</th>
<th>Prerequisites</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>BGP over CNI</strong></td>
<td>Closed Beta</td>
<td>Not available to new customers — contact your account team</td>
<td>Cloudflare Network Interconnect (CNI) v2</td>
</tr>
<tr>
<td><strong>BGP over Anycast IPsec/GRE</strong></td>
<td>Open Beta</td>
<td>Non-production workloads</td>
<td><a href="#unified-routing-mode-beta">Unified Routing (beta)</a> - contact your account team to enroll</td>
</tr>
</tbody>
</table>
<h3 id="bgp-architecture">BGP architecture</h3>
<h4 id="global-routing-and-anycast-edge">Global routing and anycast edge</h4>
<p>Magic Transit Virtual Network makes a one-pass, per-packet routing decision at the Cloudflare data center that first processes the packet (the ingress node). This ensures that even when a packet traverses multiple nodes within the Cloudflare backbone, its path is determined at the point of entry for maximum efficiency.</p>
<p>Your BGP session over IPsec, GRE, or CNI is established with the Cloudflare data center closest to your BGP peer device. Routes learned here must propagate to Cloudflare's global edge to govern how traffic is routed across the entire network.</p>
<ul>
<li><strong>Convergence time</strong>: Global route convergence typically completes within 20 seconds.</li>
<li><strong>Visibility</strong>: You can monitor learned routes and their propagation status through the Cloudflare dashboard or API.</li>
</ul>
<h4 id="centralized-route-propagation">Centralized route propagation</h4>
<p>Magic Transit Virtual Network uses a centralized control plane for route propagation, functioning similarly to a BGP Route Reflector. This architecture decouples the physical BGP session from global route distribution:</p>
<ul>
<li><strong>Session termination</strong>: BGP peering sessions are terminated at the Cloudflare edge location closest to your router.</li>
<li><strong>SDN conversion</strong>: Ingress BGP updates are converted into Software-Defined Networking (SDN) state and transmitted to a centralized relay function.</li>
<li><strong>Global dissemination</strong>: The relay propagates these instructions to every Cloudflare data center globally, updating the local Forwarding Information Base (FIB) at each site.</li>
</ul>
<h4 id="edge-resiliency-mode-non-stop-forwarding">Edge Resiliency Mode (Non-Stop Forwarding)</h4>
<p>Cloudflare's data plane is designed for high availability. If the edge location loses communication with the centralized relay, the system enters Edge Resiliency Mode, mimicking Non-Stop Forwarding (NSF) behavior:</p>
<ul>
<li><strong>Forwarding continuity</strong>: Edge locations continue to route traffic using the last-known-good forwarding table (FIB). Data plane traffic remains uninterrupted.</li>
<li><strong>Stale path retention</strong>: Because the FIB is frozen during this mode, forwarding decisions remain active even if the underlying BGP session with your router flaps or resets.</li>
<li><strong>Continuous health monitoring</strong>: While BGP updates are frozen, tunnel health checks remain active. These are sent from all Cloudflare data centers, allowing the edge at any ingress node to detect if a physical connection to your router has failed. If a health check fails, the ingress node at the edge will deprioritize that specific path, preventing traffic from being sent into a black hole despite the frozen routing state.</li>
<li><strong>Update freeze</strong>: During this state, the global control plane is frozen. New BGP updates received from your router will be held locally at the edge and will not propagate globally until connectivity to the centralized relay is restored.</li>
<li><strong>Magic Transit edge announcement</strong>: During this frozen state, your BYOIP prefix(es) will continue to be announced at Cloudflare's global edge. You can manually change this announcement status through the API or dashboard.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="traffic-persistence-during-bgp-resets">Traffic persistence during BGP resets</h3>
@markup("md", "content/.markup/bodies/10595.md")
</aside>
<h4 id="system-recovery-and-re-synchronization">System recovery and re-synchronization</h4>
<p>Once connectivity between the Cloudflare edge and the centralized relay is restored, the system automatically exits Edge Resiliency Mode and performs a stateful re-synchronization:</p>
<ol>
<li><strong>RIB-to-relay sync</strong>: The edge pushes all currently held BGP updates (the current RIB state) to the relay.</li>
<li><strong>Global update</strong>: The relay reconciles these updates and propagates any changes to the rest of the Cloudflare global network.</li>
<li><strong>FIB unfreeze</strong>: The local forwarding tables at the edge are unfrozen and updated with the latest validated routing instructions.</li>
</ol>
<h3 id="bgp-peering-with-the-magic-transit-virtual-network-routing-table">BGP peering with the Magic Transit Virtual Network routing table</h3>
<p>Magic Transit BGP peering is with the Magic Transit Virtual Network routing table (as opposed to peering with the Cloudflare Internet global network). BGP peers configured by following this guide will receive advertisements for all prefixes in the Magic Transit Virtual Network routing table plus any additional prefixes configured in the on-ramp <a href="/magic-transit/how-to/configure-routes/#set-up-bgp-peering">Advertised prefix list</a>.</p>
<p>If instead you are seeking to do public peering with the Cloudflare ASN 13335 at one of the Cloudflare data centers, refer to <a href="/network-interconnect/">PNI and peering setup</a>. It is not currently possible to share Magic Transit Virtual Network BGP peering and PNI on the same physical interconnect port.</p>
<h3 id="bgp-route-distribution-and-convergence">BGP route distribution and convergence</h3>
<p>Cloudflare redistributes routes received from your device into the Magic Transit Virtual Network routing table.</p>
<p>All routes in the Magic Transit Virtual Network routing table are advertised to BGP peers. Each BGP peer receives each prefix route along with the full <code>AS_PATH</code>, with the selected Cloudflare side <a href="https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/">ASN</a> prepended. This is so that the peer can accurately perform <a href="https://datatracker.ietf.org/doc/html/rfc4271#section-9.1.2">loop prevention</a>.</p>
<p>BGP peering sessions can advertise reachable prefixes to a peer and withdraw previously advertised prefixes. This propagation takes no more than a few minutes.</p>
<h3 id="bgp-timers-and-settings">BGP timers and settings</h3>
<p>Cloudflare uses the following timers, which are not configurable:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Hold timer</strong></td>
<td>240 seconds for CNI and 90 seconds for GRE and IPsec tunnels<br /> (<em>To establish a session, Cloudflare compares its hold timer and the peer's hold timer, and uses the smaller of the two values to establish the BGP session.</em>)</td>
</tr>
<tr>
<td><strong>Keepalive timer</strong></td>
<td>One third of the hold timer.</td>
</tr>
<tr>
<td><strong>Graceful restart</strong></td>
<td>120 seconds (currently, only supported on CNI)</td>
</tr>
</tbody>
</table>
<ul>
<li><strong>Hold timer</strong>: Specifies the maximum amount of time that a BGP peer waits to receive a keepalive, update, or notification message before declaring the BGP session down. Cloudflare uses the smaller of this default hold timer and that received from the peer in the open message.</li>
<li><strong>Keepalive timer</strong>: BGP systems exchange keepalive messages to determine whether the peer router is reachable. If keepalive messages are not received within the hold timer, the session is assumed to be down, indicating that the peer is no longer reachable at the BGP protocol level.</li>
<li><strong>Graceful restart timer</strong>: Tracks how long a router waits for a peer to re-establish a BGP session after the peer initiates a graceful restart. If the peer does not reconnect within this time, the router declares the session down and removes stale routes.</li>
</ul>
<h3 id="bgp-capabilities-and-limitations">BGP capabilities and limitations</h3>
<p>BGP multipath is supported. If BGP learns the same prefix on two different interconnects, Cloudflare distributes traffic destined for that prefix across each interconnect according to the usual ECMP behavior.</p>
<p>BGP Graceful Restart is supported in a passive (helper/aware) mode. Cloudflare maintains forwarding state for a restarting neighbor.</p>
<p>BGP support currently has the following limitations:</p>
<ul>
<li>The Cloudflare account ASN and your device ASN must be different. Only eBGP is supported.</li>
<li>Cloudflare always injects routes with a priority of <code>100</code>.</li>
<li>Bidirectional Forwarding Detection (BFD) is not supported.</li>
<li>If you are using BGP with IPsec/CNI (beta), you must set the ASN on the Cloudflare side to <code>13335</code>. Private ASNs are not yet supported.</li>
</ul>
<p>For Magic Transit customers, BGP with the Magic Transit Virtual Network routing table is separated from the announcement of anycast prefixes at the Cloudflare edge. Anycast withdrawal must be controlled with existing methods documented in <a href="/magic-transit/how-to/advertise-prefixes/">Advertise prefixes</a>.</p>
<h3 id="tunnel-health-checks">Tunnel health checks</h3>
<p>You need to enable <a href="/magic-transit/reference/tunnel-health-checks/#legacy-bidirectional-health-checks">legacy health checks</a> alongside BGP. This is essential to determine if a specific Cloudflare data center is reachable from your device. <a href="/magic-transit/reference/tunnel-health-checks/">Tunnel health checks</a> modify the route priorities for dynamically learned BGP routes.</p>
