---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/
  description: Cloudflare WAN uses a static configuration to route traffic through anycast tunnels using the Generic Routing Encapsulation (GRE) and Internet Protocol Security (IPsec) protocols from Cloudflare's global network to your network.
  full_title: Traffic steering · Cloudflare WAN docs
  head_html: <title>Traffic steering · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare WAN uses a static configuration to route traffic through anycast tunnels using the Generic Routing Encapsulation (GRE) and Internet Protocol Security (IPsec) protocols from Cloudflare&#x27;s global network to your network."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/index.md"><meta property="og:title" content="Traffic steering · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare WAN uses a static configuration to route traffic through anycast tunnels using the Generic Routing Encapsulation (GRE) and Internet Protocol Security (IPsec) protocols from Cloudflare&#x27;s global network to your network."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#page","headline":"Traffic steering \u00b7 Cloudflare WAN docs","description":"Cloudflare WAN uses a static configuration to route traffic through anycast tunnels using the Generic Routing Encapsulation (GRE) and Internet Protocol Security (IPsec) protocols from Cloudflare's global network to your network.","url":"https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/reference/traffic-steering/
  schema: 1
---
<h2 id="cloudflare-virtual-network-routing-table">Cloudflare Virtual Network routing table</h2>
<p>When traffic enters Cloudflare's network, it needs to reach the correct destination in your infrastructure — a specific data center, office, or cloud environment. Traffic steering controls how Cloudflare makes these routing decisions.</p>
<p>The Cloudflare Virtual Network is a virtual network overlay, private to your account, that spans all Cloudflare data centers globally. This overlay network provides:</p>
<ul>
<li>Magic Transit delivery for <a href="/ddos-protection/">Denial of Service (DoS)</a> and <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> filtered Internet traffic, from the entry data center where the traffic ingressed, to your publicly addressed edge/border network.</li>
<li>Cloudflare WAN packet transport between IPsec/GRE tunnels, interconnects, <a href="/load-balancing/">Cloudflare Load Balancer</a>, and <a href="/cloudflare-one/">Zero Trust</a> connections such as <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>, <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation</a>, <a href="/cloudflare-one/access-controls/policies/">Access</a>, and <a href="/cloudflare-one/traffic-policies/">Gateway</a>.</li>
</ul>
<p>The Cloudflare Virtual Network supports routing the Cloudflare WAN traffic through anycast tunnels using <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/">GRE and Internet Protocol Security (IPsec)</a> or <a href="/network-interconnect/">CNI with Dataplane v2</a>. You can add entries to the Cloudflare Virtual Network routing table through static route configuration or through routes learned through BGP peering (beta). Traffic can also be routed automatically according to tracked flow state.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6778.md")
</aside>
<h3 id="allowed-ip-ranges">Allowed IP ranges</h3>
<p>The following IPv4 address ranges are allowed in the Cloudflare Virtual Network routing table:</p>
<ul>
<li><a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918</a> address space, specifically <code>10.0.0.0/8</code>, <code>172.16.0.0/12</code>, and <code>192.168.0.0/16</code>.</li>
</ul>
<p>When using Cloudflare WAN and Cloudflare Tunnel together, consider the IP ranges utilized in the static routes of Cloudflare Tunnel when selecting static routes for Cloudflare WAN. For more information, refer to <a href="/cloudflare-wan/zero-trust/cloudflare-tunnel/">Cloudflare Tunnel</a>.</p>
<p>For prefixes outside RFC 1918, contact your Cloudflare customer service manager.</p>
<h3 id="default-routing">Default routing</h3>
<p>If traffic does not match any route you have configured in the virtual network, Cloudflare applies default behavior based on the destination address type:</p>
<ul>
<li><strong>Public (Internet-routable) addresses</strong>: Traffic exits to the Internet.</li>
<li><strong>Private addresses</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918</a> or <a href="https://datatracker.ietf.org/doc/html/rfc6598">CGNAT/RFC 6598</a>): Traffic is dropped (null routed), because private addresses are not routable on the public Internet and Cloudflare has no path to deliver them without a matching route.</li>
</ul>
<h3 id="route-prioritization">Route prioritization</h3>
<p>Cloudflare WAN steers traffic along tunnel routes based on route entry priorities.</p>
<ul>
<li>Lower values have greater priority.</li>
<li>When the priority values for prefix entries match, Cloudflare uses <a href="#equal-cost-multi-path-routing">equal-cost multi-path (ECMP)</a> packet forwarding to route traffic. You can apply an optional weight value to static routes to <a href="#set-priority-and-weights-for-static-routes">modify ECMP tunnel distribution</a>.</li>
<li>Cloudflare routing applies longest-prefix match. A more specific static route (like <code>/30</code>) always takes precedence over a less specific one (like <code>/29</code>), regardless of tunnel priority — unless you remove the more specific route.</li>
<li>When BGP and static routes have the same prefix and priority, Cloudflare enforces priority by preferring static routes over BGP routes. This ensures that manually configured static routes take precedence unless you explicitly deprioritize them.</li>
</ul>
<h3 id="set-priority-and-weights-for-static-routes">Set priority and weights for static routes</h3>
<p>The priority value for static routes is directly configured as part of the route object in the Cloudflare <a href="/cloudflare-wan/configuration/how-to/configure-routes/#create-a-static-route">dashboard or through the API</a>. For example:</p>
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
<p>When BGP advertises a route, Cloudflare automatically adds it to the Cloudflare Virtual Network routing table with a default priority of <code>100</code> which applies to <a href="#scoping-routes-to-specific-regions">all regions</a>. However, if a static route exists with the same prefix and priority, the static route always takes precedence over the BGP route. Set a different priority for static routes (more or less than <code>100</code>) depending on which you want to prioritize. Lower values have greater priority.</p>
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
<pre tabindex="0"><code class="language-txt">&#35; No change to base priority.&#10;AS_PATH: 65000 65200&#10;&#10;&#35; Add 10 to base priority for 1 prepend of 65000&#10;AS_PATH: 65000 65000 65200&#10;&#10;&#35; Add 20 to base priority for 2 prepend of 65000&#10;AS_PATH: 65000 65000 65000 65200&#10;</code></pre>
<h4 id="how-communities-and-prepends-work-together">How communities and prepends work together</h4>
<p>Cloudflare adjusts route priority when using AS prepending with communities. For example, if a route is tagged with <code>13335:60150</code>, the base priority is set to <code>150</code>. If you prepend your ASN twice, Cloudflare adds <code>10</code> for each prepend, increasing the route priority to <code>180</code>.</p>
<h2 id="automatic-return-routing-beta">Automatic Return Routing (beta)</h2>
<p>Automatic Return Routing (ARR) allows Cloudflare to track network flows from your Cloudflare WAN (formerly Magic WAN) connected locations, ensuring return traffic is routed back to the connection where it was received without requiring static or dynamic routes. This functionality requires the new <a href="#unified-routing-mode-beta">Unified Routing mode (beta)</a>.</p>
<p>Instead of relying on static or dynamic routes for the return path, Cloudflare WAN learns flows and remembers which connection a given flow arrived on. For any matching return traffic, Cloudflare WAN uses this learned state to choose the next hop. This simplifies configuration, reduces the number of routes you must manage, and helps preserve symmetry for stateful traffic.</p>
<p>ARR provides the following benefits:</p>
<ul>
<li><strong>Removes the need for return routes</strong>: For supported traffic types like new TCP connections (TCP SYN), UDP, and ICMP echo traffic, Cloudflare WAN no longer requires a routing table entry to return traffic to the originating tunnel or interconnect.</li>
<li><strong>Maintains symmetric routing for flows</strong>: Responses to a given flow (for example, a TCP session) return over the same Cloudflare WAN connection that carried the initial request — important for stateful firewalls and middleboxes.</li>
<li><strong>Supports overlapping IP space</strong>: Because the return path is tied to the learned connection state instead of a destination prefix in the routing table, Automatic Return Routing can support scenarios where different sites use overlapping private address space.</li>
<li><strong>Operates per connection</strong>: You decide which IPsec / GRE tunnels or network interconnects should use this behavior by enabling the feature on each connection.</li>
</ul>
<h3 id="how-arr-works">How ARR works</h3>
<p>When traffic that is eligible for Automatic Return Routing (ARR) arrives on a connection with ARR enabled, Cloudflare WAN creates a flow entry that records:</p>
<ul>
<li>The source and destination IP addresses</li>
<li>The relevant ports or identifiers, depending on the protocol</li>
<li>The connection (tunnel or interconnect) that the traffic arrived on</li>
</ul>
<p>For any subsequent packets that match this flow and require a next hop, Cloudflare WAN:</p>
<ol>
<li>Checks for a matching Automatic Return Routing flow.</li>
<li>If a match exists, routes the packet back to the same connection where the flow was learned, instead of consulting the Cloudflare Virtual Network routing table.</li>
</ol>
<p>The initial request from your network to the Internet still uses your configured static or BGP routes. ARR only affects the return path for supported traffic after the flow is learned.</p>
<h3 id="traffic-and-destinations-affected">Traffic and destinations affected</h3>
<p>Automatic Return Routing applies when:</p>
<ul>
<li>Traffic is received on a tunnel or network interconnect where the feature is enabled.</li>
<li>The received traffic is one of:
<ul>
<li>New TCP connections (TCP SYN)</li>
<li>UDP</li>
<li>ICMP echo (ping) requests</li>
</ul>
</li>
<li>The traffic is destined for:
<ul>
<li>Internet egress through Cloudflare</li>
<li>A Cloudflare One Client</li>
<li>A private network connected to Cloudflare through Cloudflare Tunnel</li>
<li>A private network connected to Cloudflare through Cloudflare Mesh</li>
</ul>
</li>
</ul>
<p>In this initial release, ARR does not change routing for traffic between Cloudflare WAN connections (for example, traffic from one IPsec/GRE tunnel or interconnect to another). That traffic continues to follow your configured Cloudflare WAN routes.</p>
<h2 id="unified-routing-mode-beta">Unified Routing mode (beta)</h2>
<p>The Unified Routing mode is the newer Cloudflare One data plane that uses a single routing fabric for all supported connection types. Unified Routing mode routes traffic across the Cloudflare One Client, Cloudflare Tunnel, IPsec, GRE, and Cloudflare Network Interconnect (CNI) in a single system, making it easier to set up your Cloudflare One connections.</p>
<p>In the Cloudflare WAN dashboard, routing mode appears where you manage routes:</p>
<ul>
<li><strong>Routing mode: Unified</strong> — your account is on the unified data plane and supports the new routing features.</li>
<li><strong>Routing mode: Legacy</strong> — your account uses the previous data plane and does not support all unified routing features.</li>
</ul>
<h3 id="why-use-unified-routing">Why use Unified Routing</h3>
<p>Unified Routing is the future of the dedicated virtual network overlay that powers Magic Transit and Cloudflare One network connectivity.</p>
<p>For Cloudflare One customers, there are several reasons to consider moving to Unified Routing, as it is a prerequisite for several new capabilities:</p>
<ul>
<li><a href="#automatic-return-routing-beta">Automatic Return Routing</a></li>
<li><a href="#release-status">BGP over IPsec/GRE</a></li>
<li><a href="/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/">Cloudflare Source IPs</a> using private IP space with customizable IPv4 range</li>
<li>Customizable Cloudflare One Client IPv4 ranges</li>
<li>IPv6 support</li>
<li>Improved performance between Cloudflare One Client and IPsec/GRE/CNI</li>
<li>Support for Cloudflare Mesh and IPsec/GRE/CNI connectivity in the same account.</li>
</ul>
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
<h2 id="route-evaluation-with-zero-trust-connections">Route evaluation with Zero Trust connections</h2>
<p>When your account uses both Zero Trust routes (Cloudflare Tunnel, Cloudflare Mesh) and WAN routes (IPsec, GRE, CNI), route selection behavior depends on your <a href="#unified-routing-mode-beta">routing mode</a>.</p>
<h3 id="terminology">Terminology</h3>
<table>
<thead>
<tr>
<th>Route type</th>
<th>Connection methods</th>
</tr>
</thead>
<tbody>
<tr>
<td>Zero Trust routes</td>
<td>Cloudflare Tunnel, Cloudflare Mesh</td>
</tr>
<tr>
<td>WAN routes</td>
<td>IPsec, GRE, and CNI</td>
</tr>
</tbody>
</table>
<h3 id="unified-routing-mode">Unified Routing mode</h3>
<p>Unified Routing uses a single routing fabric for all connection types. Route selection applies longest-prefix-match consistently across all traffic types and connection methods.</p>
<table>
<thead>
<tr>
<th>Zero Trust route</th>
<th>WAN route</th>
<th>Traffic destination</th>
<th>Selected route</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>10.0.0.0/24</code></td>
<td><code>10.0.0.64/28</code></td>
<td><code>10.0.0.70</code></td>
<td>WAN (more specific)</td>
</tr>
<tr>
<td><code>10.0.0.0/28</code></td>
<td><code>10.0.0.0/24</code></td>
<td><code>10.0.0.10</code></td>
<td>Zero Trust (more specific)</td>
</tr>
<tr>
<td><code>10.0.0.0/24</code></td>
<td><code>10.0.0.0/24</code></td>
<td><code>10.0.0.10</code></td>
<td>Zero Trust (same prefix length)</td>
</tr>
</tbody>
</table>
<p>When routes have the same prefix length, Zero Trust routes take precedence over WAN routes.</p>
<p>For scenarios with overlapping IP space across sites, enable <a href="#automatic-return-routing-beta">Automatic Return Routing</a> to ensure return traffic reaches the correct origin.</p>
<h3 id="legacy-routing-mode">Legacy Routing mode</h3>
<p>For accounts using Legacy Routing, route selection depends on the traffic source.</p>
<h4 id="cloudflare-one-client-to-private-network">Cloudflare One Client to private network</h4>
<p>For accounts using only Zero Trust, Cloudflare One Client traffic is routed using the Zero Trust IP routing table only, following longest-prefix-match logic.</p>
<p>If your account has Cloudflare WAN enabled, traffic from Cloudflare One Client follows the same route selection behavior as <a href="#site-to-site-traffic-with-gateway">site-to-site traffic with Gateway</a>. Contact your account team if you want Cloudflare One Client to continue to behave as if WAN is not enabled.</p>
<h4 id="site-to-site-traffic-wan-to-wan">Site-to-site traffic (WAN to WAN)</h4>
<p>For traffic between WAN connections (IPsec to IPsec, GRE to GRE, and CNI to CNI) that does not require Gateway filtering, longest-prefix-match applies within the WAN routing table. This traffic does not interact with Zero Trust routing.</p>
<h4 id="site-to-site-traffic-with-gateway">Site-to-site traffic with Gateway</h4>
<p>When <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a> are applied to site-to-site WAN traffic, route selection follows these rules:</p>
<table>
<thead>
<tr>
<th>Scenario</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>More specific Zero Trust route than WAN route</td>
<td><strong>Works</strong> — longest-prefix-match honored for both inbound and outbound traffic</td>
</tr>
<tr>
<td>More specific WAN route than Zero Trust route</td>
<td><strong>Not guaranteed</strong> — Zero Trust route can take precedence regardless of prefix length</td>
</tr>
<tr>
<td>Equal prefix length</td>
<td>Zero Trust route wins (by design)</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6779.md")
</aside>
<h4 id="cross-system-traffic-wan-to-zero-trust-or-zero-trust-to-wan">Cross-system traffic (WAN to Zero Trust or Zero Trust to WAN)</h4>
<p>Legacy Routing uses two routing components:</p>
<ul>
<li><strong>Zero Trust routing</strong> (handles Cloudflare One Client, Cloudflare Tunnel, and Cloudflare Mesh)</li>
<li><strong>WAN routing</strong> (handles IPsec, GRE, and CNI)</li>
</ul>
<p>Cross-system traffic follows the same rules as <a href="#site-to-site-traffic-with-gateway">site-to-site traffic with Gateway</a>. A more specific Zero Trust route works correctly; a more specific WAN route is not guaranteed to be selected.</p>
<p><strong>Recommendation:</strong> If overlap is required, migrate to <a href="#unified-routing-mode-beta">Unified Routing</a> or contact your account team.</p>
<h3 id="check-your-routing-mode">Check your routing mode</h3>
<p>To determine the routing mode for your account:</p>
<ol>
<li>Go to <strong>Routes</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Check the banner at the top of the page:
<ul>
<li><strong>Your account is using Unified Routing mode.</strong> — Your account uses Unified Routing.</li>
<li><strong>Unified routing is available.</strong> — Your account uses Legacy Routing.</li>
</ul>
</li>
</ol>
<p>To migrate to Unified Routing, contact your account team.</p>
<h2 id="scoping-routes-to-specific-regions">Scoping routes to specific regions</h2>
<p>If you have multiple connectivity paths to a network segment and want to apply different route prioritization based on where traffic arrives at the Cloudflare network, you can scope routes to specific Cloudflare data center regions. This is useful if you run your own anycast network and want your end-user traffic to arrive at your network location closest to the user.</p>
<p>When you scope a route to a Cloudflare data center region, it only shows up in the Cloudflare Virtual Network routing table in that region, along with all global routes that do not have any region scope. Route prioritization and ECMP logic apply across both region-scoped and global routes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6777.md")
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
<p>Configure scoping for your traffic in the <strong>Region code</strong> section when adding or editing a static route. Refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/#create-a-static-route">Create a static route</a> and <a href="/cloudflare-wan/configuration/how-to/configure-routes/#edit-a-static-route">Edit a static route</a> for more information.</p>
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
@markup("md", "content/.markup/bodies/6776.md")
</aside>
<h3 id="examples">Examples</h3>
<p>This diagram illustrates how ECMP distributes traffic equally across two paths with the same prefix and priority.</p>
<h4 id="normal-traffic-flow">Normal traffic flow</h4>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;accTitle: Tunnels diagram&#10;accDescr: This example has three tunnel routes, with traffic equally distributed across two paths.&#10;&#10;subgraph Cloudflare&#10;direction LR&#10;B[Cloudflare &lt;br&gt; data center]&#10;C[Cloudflare &lt;br&gt; data center]&#10;D[Cloudflare &lt;br&gt; data center]&#10;end&#10;&#10;Z(&quot;Load balancing for some &lt;br&gt; priority tunnels uses ECMP &lt;br&gt; (hashing on src IP, dst IP, &lt;br&gt; scr port, dst port)&quot;) --- Cloudflare&#10;A((User)) --&gt; Cloudflare --- E[Anycast IP]&#10;E[Anycast IP] --&gt; F[/&quot;GRE Tunnel 1 / &lt;br&gt; priority 1 / &lt;br&gt; ~50% of flows&quot;/] --&gt; I{{Customer &lt;br&gt; data center/ &lt;br&gt; network 1}}&#10;E[Anycast IP] --&gt; G[/&quot;GRE Tunnel 2 / &lt;br&gt; priority 1 / &lt;br&gt; ~50% of flows&quot;/] --&gt; J{{Customer &lt;br&gt; data center/ &lt;br&gt; network 2}}&#10;E[Anycast IP] --&gt; H[/GRE Tunnel 3 / &lt;br&gt; priority 2 / &lt;br&gt; 0% of flows/] --o K{{Customer &lt;br&gt; data center/ &lt;br&gt; network 3}}&#10;</code></pre>
<h4 id="failover-traffic-flow-scenario-1">Failover traffic flow: Scenario 1</h4>
<p><strong>Customer router failure</strong></p>
<p>When Cloudflare WAN health checks determine that Tunnel 2 is unhealthy, Cloudflare WAN dynamically de-prioritizes that route, leaving Tunnel 1 as the sole top-priority route. As a result, Cloudflare WAN steers traffic away from Tunnel 2, and all traffic flows to Tunnel 1.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;accTitle: Tunnels diagram&#10;accDescr: This example has Tunnel 2 unhealthy, and all traffic prioritized to Tunnel 1.&#10;&#10;subgraph Cloudflare&#10;direction LR&#10;B[Cloudflare &lt;br&gt; data center]&#10;C[Cloudflare &lt;br&gt; data center]&#10;D[Cloudflare &lt;br&gt; data center]&#10;end&#10;&#10;Z(Tunnel health is &lt;br&gt; determined by &lt;br&gt; health checks that &lt;br&gt; run from all Cloudflare &lt;br&gt; data centers) --- Cloudflare&#10;A((User)) --&gt; Cloudflare --- E[Anycast IP]&#10;E[Anycast IP] --&gt; F[/&quot;Tunnel 1 / &lt;br&gt; priority 1 / &lt;br&gt; ~100% of flows&quot;/]:::green --&gt; I{{Customer &lt;br&gt; data center/ &lt;br&gt; network 1}}&#10;E[Anycast IP] --&gt; G[/Tunnel 2 / &lt;br&gt; priority 3 / &lt;br&gt; unhealthy / 0% of flows/]:::red --x J{{Customer &lt;br&gt; data center/ &lt;br&gt; network 2}}&#10;E[Anycast IP] --&gt; H[/Tunnel 3 / &lt;br&gt; priority 2 / &lt;br&gt; 0% of flows/] --o K{{Customer &lt;br&gt; data center/ &lt;br&gt; network 3}}&#10;classDef red fill:#EE4B2B,color: black&#10;classDef green fill:#00FF00,color: black&#10;</code></pre>
<h4 id="failover-traffic-flow-scenario-2">Failover traffic flow: Scenario 2</h4>
<p><strong>Intermediary Internet Service Provider (ISP) failure</strong></p>
<p>When Cloudflare WAN determines that Tunnel 1 is unhealthy as well, that route is also de-prioritized, leaving Tunnel 3 with the top priority route. In that case, all traffic flows to Tunnel 3.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;accTitle: Tunnels diagram&#10;accDescr: This example has Tunnel 1 and 2 unhealthy, and all traffic prioritized to Tunnel 3.&#10;&#10;subgraph Cloudflare&#10;direction LR&#10;B[Cloudflare &lt;br&gt; data center]&#10;C[Cloudflare &lt;br&gt; data center]&#10;D[Cloudflare &lt;br&gt; data center]&#10;end&#10;&#10;Z(Lower-priority tunnels &lt;br&gt; are used when &lt;br&gt; higher-priority tunnels &lt;br&gt; are unhealthy) --- Cloudflare&#10;A((User)) --&gt; Cloudflare --- E[Anycast IP]&#10;E[Anycast IP]  -- Intermediary &lt;br&gt; network issue --&gt;  F[/Tunnel 1 / &lt;br&gt; priority 3 / &lt;br&gt; unhealthy / 0% of flows/]:::red --x I{{Customer &lt;br&gt; data center/ &lt;br&gt; network 1}}&#10;E[Anycast IP]  -- Intermediary &lt;br&gt; network issue --&gt;  G[/Tunnel 2 / &lt;br&gt; priority 3 / &lt;br&gt; unhealthy / 0% of flows/]:::red --x J{{Customer &lt;br&gt; data center/ &lt;br&gt; network 2}}&#10;E[Anycast IP] --&gt;  H[/Tunnel 3 / &lt;br&gt; priority 2 / &lt;br&gt; 100% of flows/]:::green --&gt; K{{Customer &lt;br&gt; data center/ &lt;br&gt; network 3}}&#10;classDef red fill:#EE4B2B,color: black&#10;classDef green fill:#00FF00,color: black&#10;</code></pre>
<p>When Cloudflare WAN determines that Tunnels 1 and 2 are healthy again, it re-prioritizes those routes, and traffic flow returns to normal.</p>
<h3 id="ecmp-and-bandwidth-utilization">ECMP and bandwidth utilization</h3>
<p>Because ECMP is probabilistic, the algorithm routes roughly the same number of flows through each tunnel. However, it does not consider the amount of traffic already sent through a tunnel when deciding where to route the next packet.</p>
<p>For example, consider a scenario with many very low-bandwidth TCP connections and one very high-bandwidth TCP connection. Packets for the high-bandwidth connection have the same hash and thus use the same tunnel. As a result, that tunnel utilizes greater bandwidth than the others.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6775.md")
</aside>
<h2 id="bgp-information">BGP information</h2>
<p>Using BGP peering with your Cloudflare One or Magic Transit Virtual Network routing table allows you to:</p>
<ul>
<li>Automate the process of adding or removing networks and subnets.</li>
<li>Take advantage of failure detection and session recovery features.</li>
</ul>
<p>With this functionality, you can:</p>
<ul>
<li>Establish an eBGP session between your devices and the Cloudflare WAN service when connected through CNI, GRE or IPsec tunnels.</li>
<li>Secure the session by MD5 authentication to prevent misconfigurations.</li>
<li>Exchange routes dynamically between your devices and your Cloudflare Virtual Network routing table.</li>
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
<p>Cloudflare Virtual Network makes a one-pass, per-packet routing decision at the Cloudflare data center that first processes the packet (the ingress node). This ensures that even when a packet traverses multiple nodes within the Cloudflare backbone, its path is determined at the point of entry for maximum efficiency.</p>
<p>Your BGP session over IPsec, GRE, or CNI is established with the Cloudflare data center closest to your BGP peer device. Routes learned here must propagate to Cloudflare's global edge to govern how traffic is routed across the entire network.</p>
<ul>
<li><strong>Convergence time</strong>: Global route convergence typically completes within 20 seconds.</li>
<li><strong>Visibility</strong>: You can monitor learned routes and their propagation status through the Cloudflare dashboard or API.</li>
</ul>
<h4 id="centralized-route-propagation">Centralized route propagation</h4>
<p>Cloudflare Virtual Network uses a centralized control plane for route propagation, functioning similarly to a BGP Route Reflector. This architecture decouples the physical BGP session from global route distribution:</p>
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
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="traffic-persistence-during-bgp-resets">Traffic persistence during BGP resets</h3>
@markup("md", "content/.markup/bodies/6774.md")
</aside>
<h4 id="system-recovery-and-re-synchronization">System recovery and re-synchronization</h4>
<p>Once connectivity between the Cloudflare edge and the centralized relay is restored, the system automatically exits Edge Resiliency Mode and performs a stateful re-synchronization:</p>
<ol>
<li><strong>RIB-to-relay sync</strong>: The edge pushes all currently held BGP updates (the current RIB state) to the relay.</li>
<li><strong>Global update</strong>: The relay reconciles these updates and propagates any changes to the rest of the Cloudflare global network.</li>
<li><strong>FIB unfreeze</strong>: The local forwarding tables at the edge are unfrozen and updated with the latest validated routing instructions.</li>
</ol>
<h3 id="bgp-peering-with-the-cloudflare-virtual-network-routing-table">BGP peering with the Cloudflare Virtual Network routing table</h3>
<p>Cloudflare WAN BGP peering is with the Cloudflare Virtual Network routing table (as opposed to peering with the Cloudflare Internet global network). BGP peers configured by following this guide will receive advertisements for all prefixes in the Cloudflare Virtual Network routing table plus any additional prefixes configured in the on-ramp <a href="/cloudflare-wan/configuration/how-to/configure-routes/#set-up-bgp-peering">Advertised prefix list</a>.</p>
<p>If instead you are seeking to do public peering with the Cloudflare ASN 13335 at one of the Cloudflare data centers, refer to <a href="/network-interconnect/">PNI and peering setup</a>. It is not currently possible to share Cloudflare Virtual Network BGP peering and PNI on the same physical interconnect port.</p>
<h3 id="bgp-route-distribution-and-convergence">BGP route distribution and convergence</h3>
<p>Cloudflare redistributes routes received from your device into the Cloudflare Virtual Network routing table, which both Cloudflare WAN and Magic Transit use.</p>
<p>All routes in the Cloudflare Virtual Network routing table are advertised to BGP peers. Each BGP peer receives each prefix route along with the full <code>AS_PATH</code>, with the selected Cloudflare side <a href="https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/">ASN</a> prepended. This is so that the peer can accurately perform <a href="https://datatracker.ietf.org/doc/html/rfc4271#section-9.1.2">loop prevention</a>.</p>
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
<h3 id="tunnel-health-checks">Tunnel health checks</h3>
<p>You need to enable <a href="/cloudflare-wan/reference/tunnel-health-checks/#legacy-bidirectional-health-checks">legacy health checks</a> alongside BGP. This is essential to determine if a specific Cloudflare data center is reachable from your device. <a href="/cloudflare-wan/reference/tunnel-health-checks/">Tunnel health checks</a> modify the route priorities for dynamically learned BGP routes.</p>
<h2 id="application-aware-policies">Application-aware policies</h2>
<p>By default, Cloudflare balances and steers traffic based on network-layer characteristics (IP, port etc). If you are using the Cloudflare WAN Connector, you can also steer traffic based on well-known applications. Application-aware policies provide easier management and more granularity over traffic flows.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/application-app-types/">Applications and app types</a>.</p>
