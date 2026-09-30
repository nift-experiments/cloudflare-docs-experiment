<p>Cloudflare continuously monitors whether each tunnel connecting your network to Cloudflare is reachable and performing well. When a tunnel becomes unhealthy, Cloudflare automatically steers traffic to an alternate path — without requiring manual intervention. This monitoring relies on tunnel health check probes.</p>
<p>A tunnel health check probe consists of an <a href="https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/">ICMP (Internet Control Message Protocol)</a> payload encapsulated in the protocol of the tunnel being tested. For example, if the tunnel is an Internet Protocol Security (IPsec) tunnel, the ICMP <a href="https://www.cloudflare.com/learning/network-layer/what-is-a-packet/">packet</a> is encrypted within the Encapsulating Security Payload (ESP) packet of the tunnel.</p>
<p>A tunnel health check probe travels from Cloudflare to the tunnel origin, then returns a response to Cloudflare. Cloudflare uses this response to determine the probe outcome and calculate the tunnel state (the following sections explain this in greater detail).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5548.md")
</aside>
<h2 id="types-of-health-checks">Types of health checks</h2>
<p>Cloudflare WAN uses two types of health checks:</p>
<h3 id="tunnel-health-checks">Tunnel health checks</h3>
<p>Tunnel health checks monitor the status of the tunnels that route traffic from Cloudflare to your origin network. Cloudflare WAN relies on these checks to steer traffic to the best available routes. During onboarding, you <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">specify the tunnel endpoints</a> or tunnel health check targets the tunnel probes originating from Cloudflare's global network will target.</p>
<p>You can access tunnel health check results <a href="/analytics/graphql-api/tutorials/querying-magic-transit-tunnel-healthcheck-results/">through the API</a>. Cloudflare aggregates these results from individual health check results from Cloudflare servers.</p>
<h3 id="endpoint-health-checks">Endpoint health checks</h3>
<p>Endpoint health checks evaluate connectivity from Cloudflare distributed data centers to your origin network. Unlike tunnel health checks, endpoint probes are designed to provide a broad picture of Internet health between Cloudflare and your network. They flow over available tunnels but do not inform tunnel selection or steering logic.</p>
<p>Cloudflare global network servers issue endpoint health checks outside of customer network namespaces and typically target endpoints beyond the tunnel-terminating border router. During onboarding, you specify IP addresses to configure endpoint health checks.</p>
<h2 id="tunnel-health-check-attributes">Tunnel health check attributes</h2>
<p>A tunnel health check probe has the following attributes.</p>
<h3 id="target">Target</h3>
<p>A tunnel health check probe tests whether Cloudflare can successfully connect to a specific address or endpoint through the tunnel. The target is the address you want to verify is reachable. It is optional, and defaults vary depending on the direction of the health check (refer to <a href="#direction">Direction</a> for more information).</p>
<h3 id="direction">Direction</h3>
<p>A tunnel health check probe can have two possible directions — unidirectional and bidirectional.</p>
<h4 id="unidirectional">Unidirectional</h4>
<p>A unidirectional health check probe stays encapsulated in one direction and comes into the origin through the tunnel (from Cloudflare to the origin). The response comes back to Cloudflare unencapsulated and routes outside of the tunnel following standard Internet <a href="https://www.cloudflare.com/learning/network-layer/what-is-routing/">routing</a>.</p>
<p>The target defaults to the publicly routable origin specified as the <code>customer_endpoint</code> on the tunnel, if present. Otherwise, you can use a custom target.</p>
<h4 id="bidirectional">Bidirectional</h4>
<p>A bidirectional probe stays encapsulated in both directions. The probe comes in through the tunnel and the response also leaves encapsulated through the tunnel. The ICMP reply from your router destined for the anycast IP address on Cloudflare's network arrives at the closest Cloudflare data center and lands on one of the servers using Equal-Cost Multi-Path (ECMP), ensuring the response takes the most efficient path.</p>
<p><strong>Default packet addressing</strong></p>
<p>By default, Cloudflare destinations these packets for the Cloudflare side of the interface address field set on the tunnel, and sources them from the client side of the tunnel. For example, if the interface address is <code>10.100.0.8/31</code>, Cloudflare destinations the packet for <code>10.100.0.9</code> and sources it from <code>10.100.0.8</code>.</p>
<p><strong>Interface address ranges</strong></p>
<p>The interface address field uses either a <code>/30</code> or <code>/31</code> CIDR range:</p>
<ul>
<li><strong><code>/31</code> range</strong>: The IP you provide is the Cloudflare side, and the other IP is the client side. For example, if the interface address is <code>10.100.0.8/31</code>, then <code>10.100.0.8</code> is the Cloudflare side and <code>10.100.0.9</code> is the client side.</li>
<li><strong><code>/30</code> range</strong>: The IP you provide is the Cloudflare side, and the other IP (excluding the broadcast and network identifier) is the client side. For example, if the interface address is <code>10.100.0.9/30</code>, then <code>10.100.0.9</code> is the Cloudflare side and <code>10.100.0.10</code> is the client side.</li>
</ul>
<p>You can also configure a bidirectional health check with a custom public target, which is the recommended approach for an Azure Active Standby tunnel setup.</p>
<p>These packets flow to and from Cloudflare over the tunnels you have configured to provide full visibility into the traffic path between Cloudflare's network and your sites. You need to configure traffic selectors to accept the health check packets for IPsec tunnels.</p>
<p>Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">Add tunnels</a> to learn how to configure bidirectional or unidirectional health checks.</p>
<h4 id="legacy-bidirectional-health-checks">Legacy bidirectional health checks</h4>
<p>For customers using the legacy health check system with a public IP range, Cloudflare recommends:</p>
<ul>
<li>Configuring the tunnel health check target IP address to one within the <code>172.64.240.252/30</code> prefix range.</li>
<li>Applying a policy-based route that matches packets with a source IP address equal to the configured tunnel health check target (for example <code>172.64.240.253/32</code>), and route them over the tunnel back to Cloudflare.</li>
</ul>
<h3 id="type">Type</h3>
<p>A tunnel health check probe can have two possible types: request and reply. For each type, the source and destination address depends on the direction. Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">Add tunnels</a> to learn how to change this setting.</p>
<h4 id="request-style">Request style</h4>
<p>In a request style health check the payload probe is an ICMP request.</p>
<p>For a unidirectional probe, the source address is the Cloudflare side of the tunnel (a publicly routable address) and the destination is the origin router (also publicly routable). The origin router receives the probe and produces an ICMP response with the opposite source and destination, and sends it outside of the tunnel.</p>
<p>For a bidirectional probe, the source address is the interface address of the Cloudflare side of the tunnel (a privately routable address) and the destination is the interface address of the tunnel (also privately routable). The origin router receives the probe and produces an ICMP response with the opposite source and destination and sends it into the tunnel.</p>
<h4 id="reply-style">Reply style</h4>
<p>In a reply style health check the payload probe is an ICMP response.</p>
<p>For a unidirectional probe, the destination address is the Cloudflare side of the tunnel (a publicly routable address) and the source is the origin router (also publicly routable). The origin router receives the probe and sends it back as the response, unchanged, outside of the tunnel.</p>
<p>For a bidirectional probe, the destination address is the interface address of the Cloudflare side of the tunnel (a privately routable address) and the source is the interface address of the tunnel (also privately routable). The origin router receives the probe packet and sends the probe packet back as the response (unchanged) into the tunnel because the destination routes through the tunnel.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5547.md")
</aside>
<h3 id="summary-table-with-tunnel-health-check-probe-types">Summary table with tunnel health check probe types</h3>
<table>
<thead>
<tr>
<th align="center">Attribute</th>
<th align="center">Type</th>
<th align="center">Unidirectional health checks</th>
<th align="center">Bidirectional health checks</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">Source Address</td>
<td align="center">Request Style</td>
<td align="center">Cloudflare Address (Publicly Routable)</td>
<td align="center">Cloudflare Interface Address (Privately Routable)</td>
</tr>
<tr>
<td align="center">Destination Address</td>
<td align="center">Request Style</td>
<td align="center">Origin Tunnel Endpoint (Publicly Routable)</td>
<td align="center">Origin Interface Address (Privately Routable) / Custom Target</td>
</tr>
<tr>
<td align="center">Source Address</td>
<td align="center">Reply Style</td>
<td align="center">Origin Tunnel Endpoint (Publicly Routable)</td>
<td align="center">Origin Interface Address (Privately Routable) / Custom Target</td>
</tr>
<tr>
<td align="center">Destination Address</td>
<td align="center">Reply Style</td>
<td align="center">Cloudflare Address (Publicly Routable)</td>
<td align="center">Cloudflare Interface Address (Privately Routable)</td>
</tr>
</tbody>
</table>
<h3 id="graphics-summarizing-health-check-types">Graphics summarizing health check types</h3>
<h4 id="bidirectional-request-style">Bidirectional request style</h4>
<pre><code class="language-mermaid">flowchart TB&#10;accTitle: Bidirectional request style&#10;accDescr: Shows the flow of a bidirectional request-style tunnel health check probe and response between Cloudflare and the origin.&#10;   subgraph Tunnel Healthcheck Probe&#10;   cloudflare(Cloudflare) --- bare_echo_request([ICMP Echo Request])&#10;   bare_echo_request --&gt; tunnel[Tunnel]&#10;   tunnel --- encapsulated_echo_request([Tunnel Protocol &lt; ICMP Echo Request &gt;])&#10;   encapsulated_echo_request --&gt; Internet([Internet])&#10;   Internet --- encapsulated_echo_request_2([Tunnel Protocol &lt; ICMP Echo Request &gt;])&#10;   encapsulated_echo_request_2 --&gt; origin_tunnel(Tunnel)&#10;   origin_tunnel --- received_bare_echo_request([ICMP Echo Request])&#10;   received_bare_echo_request --&gt; origin(Origin)&#10;   end&#10;   subgraph Tunnel Healthcheck Response&#10;   origin --&gt; bare_echo_reply([ICMP Echo Reply])&#10;   bare_echo_reply --- origin_tunnel_2(Tunnel)&#10;   origin_tunnel_2 --- encapsulated_echo_reply([Tunnel Protocol &lt; ICMP Echo Reply &gt;])&#10;   encapsulated_echo_reply --- Internet_2([Internet])&#10;   Internet_2 --&gt; encapsulated_echo_reply_2([Tunnel Protocol &lt; ICMP Echo Reply &gt;])&#10;   encapsulated_echo_reply_2 --&gt; tunnel_2[Tunnel]&#10;   tunnel_2 --&gt; bare_echo_reply_2([ICMP Echo Reply])&#10;   bare_echo_reply_2 --&gt; cloudflare&#10;   end&#10;</code></pre>
<h4 id="bidirectional-reply-style">Bidirectional reply style</h4>
<pre><code class="language-mermaid">flowchart TB&#10;accTitle: Bidirectional reply style&#10;accDescr: Shows the flow of a bidirectional reply-style tunnel health check probe and response between Cloudflare and the origin.&#10;   subgraph Tunnel Healthcheck Probe&#10;   cloudflare(Cloudflare) --- bare_echo_probe([ICMP Echo Reply])&#10;   bare_echo_probe --&gt; tunnel[Tunnel]&#10;   tunnel --- encapsulated_echo_probe([Tunnel Protocol &lt; ICMP Echo Reply &gt;])&#10;   encapsulated_echo_probe --&gt; Internet([Internet])&#10;   Internet --- encapsulated_echo_probe_2([Tunnel Protocol &lt; ICMP Echo Reply &gt;])&#10;   encapsulated_echo_probe_2 --&gt; origin_tunnel(Tunnel)&#10;   origin_tunnel --- received_bare_echo_reply([ICMP Echo Reply])&#10;   received_bare_echo_reply --&gt; origin(Origin)&#10;   end&#10;   subgraph Tunnel Healthcheck Response&#10;   origin --&gt; bare_echo_reply([ICMP Echo Reply])&#10;   bare_echo_reply --- origin_tunnel_2(Tunnel)&#10;   origin_tunnel_2 --- encapsulated_echo_reply([Tunnel Protocol &lt; ICMP Echo Reply &gt;])&#10;   encapsulated_echo_reply --- Internet_2([Internet])&#10;   Internet_2 --&gt; encapsulated_echo_reply_2([Tunnel Protocol &lt; ICMP Echo Reply &gt;])&#10;   encapsulated_echo_reply_2 --&gt; tunnel_2[Tunnel]&#10;   tunnel_2 --&gt; bare_echo_reply_2([ICMP Echo Reply])&#10;   bare_echo_reply_2 --&gt; cloudflare&#10;   end&#10;</code></pre>
<h4 id="unidirectional-echo-request">Unidirectional echo request</h4>
<pre><code class="language-mermaid">flowchart TB&#10;accTitle: Unidirectional echo request&#10;accDescr: Shows the flow of a unidirectional echo request health check from Cloudflare to the origin and back.&#10;   cloudflare(Cloudflare) --- bare_echo_probe([ICMP Echo Request])&#10;   bare_echo_probe --&gt; tunnel[Tunnel]&#10;   tunnel --- encapsulated_echo_probe([Tunnel Protocol &lt; ICMP Echo Request &gt;])&#10;   encapsulated_echo_probe --&gt; Internet([Internet])&#10;   Internet --- encapsulated_echo_probe_2([Tunnel Protocol &lt; ICMP Echo Request &gt;])&#10;   encapsulated_echo_probe_2 --&gt; origin_tunnel(Tunnel)&#10;   origin_tunnel --- received_bare_echo_reply([ICMP Echo Request])&#10;   received_bare_echo_reply --&gt; origin(Origin)&#10;   origin --- received_bare_echo_reply_2([ICMP Echo Reply])&#10;   received_bare_echo_reply_2 --&gt; Internet_2([Internet])&#10;   Internet_2 --&gt; cloudflare&#10;</code></pre>
<h4 id="unidirectional-echo-reply">Unidirectional echo reply</h4>
<pre><code class="language-mermaid">flowchart TB&#10;accTitle: Unidirectional echo reply&#10;accDescr: Shows the flow of a unidirectional echo reply health check from Cloudflare to the origin and back.&#10;   cloudflare(Cloudflare) --- bare_echo_probe([ICMP Echo Reply])&#10;   bare_echo_probe --&gt; tunnel[Tunnel]&#10;   tunnel --- encapsulated_echo_probe([Tunnel Protocol &lt; ICMP Echo Reply &gt;])&#10;   encapsulated_echo_probe --&gt; Internet([Internet])&#10;   Internet --- encapsulated_echo_probe_2([Tunnel Protocol &lt; ICMP Echo Reply &gt;])&#10;   encapsulated_echo_probe_2 --&gt; origin_tunnel(Tunnel)&#10;   origin_tunnel --- received_bare_echo_reply([ICMP Echo Reply])&#10;   received_bare_echo_reply --&gt; origin(Origin)&#10;   origin --- received_bare_echo_reply_2([ICMP Echo Reply])&#10;   received_bare_echo_reply_2 --&gt; Internet_2([Internet])&#10;   Internet_2 --&gt; cloudflare&#10;</code></pre>
<h3 id="rate">Rate</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5546.md")
</aside>
<p>Every Cloudflare data center configured to process your traffic sends tunnel health check probes. The rate at which Cloudflare sends these probes varies based on tunnel and location. You can tune this rate on a per-tunnel basis by modifying the <code>health_check</code> rate with the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/update-tunnel-health-checks-frequency/">API or the dashboard</a>. You can set the rate as <em>low</em>, <em>mid</em>, or <em>high</em>, with <em>mid</em> being the default.</p>
<p>The actual rate formula considers the number of servers in a Cloudflare data center or the number of servers with the customer namespace provisioned on them for dynamically provisioned namespaces. The rate is dynamic and depends on the size of Cloudflare's network.</p>
<p>When a probe attempt fails for a <a href="#health-state-and-prioritization">healthy tunnel</a>, each server detecting the failure quickly probes up to two more times to obtain an accurate result. Cloudflare does the same if a tunnel has been down and probes start returning success. Because Cloudflare global network servers send probes up to every second, your network will receive several hundred health check packets per second. Each Cloudflare data center sends only one health check packet as part of a probe, representing a relatively trivial amount of traffic.</p>
<h2 id="health-state-and-prioritization">Health state and prioritization</h2>
<p>There are three tunnel health states: healthy, degraded, and down.</p>
<p>Healthy tunnels are preferred to degraded tunnels, and degraded tunnels are preferred to those that are down.</p>
<p>Cloudflare WAN steers traffic to tunnels based on priorities you set when you <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-routes/">assign tunnel route priorities during onboarding</a>. Tunnel routes with lower values have priority over those with higher values.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5544.md")
</aside>
<h2 id="tunnel-state-determination">Tunnel state determination</h2>
<h3 id="degraded">Degraded</h3>
<ul>
<li>When at least 0.1% of tunnel health checks fail in the previous five minutes (with at least two failures), Cloudflare WAN considers the link lossy and sets the tunnel state to degraded (assuming the tunnel is not down).</li>
<li>Cloudflare WAN requires two failures so that a single lost packet does not trigger a penalty.</li>
<li>Cloudflare WAN then immediately sets the tunnel status to degraded and applies a priority penalty.</li>
</ul>
<h3 id="down">Down</h3>
<ul>
<li>When all health checks of at least three samples in the last one second fail, Cloudflare WAN immediately transitions the tunnel from healthy or degraded to down, and applies a priority penalty to routes through that tunnel.</li>
<li>A down state determination takes precedence over a degraded state determination. This means that a tunnel can only be one of the following: down, degraded, or healthy.</li>
</ul>
<p>When Cloudflare WAN identifies a route that is not healthy, it applies these penalties:</p>
<ul>
<li><strong>Degraded</strong>: Add <code>500,000</code> to priority.</li>
<li><strong>Down</strong>: Add <code>1,000,000</code> to priority.</li>
</ul>
<p>The values for failure penalties are intentionally extreme so that they always exceed the priority values assigned during <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-routes/">routing configuration</a>.</p>
<p>Applying a penalty instead of removing the route altogether preserves redundancy and maintains options for customers with only one tunnel. Penalties also support the case when multiple tunnels are unhealthy.</p>
<h2 id="cloudflare-data-centers-and-tunnels">Cloudflare data centers and tunnels</h2>
<p>In the event a Cloudflare data center is down, Cloudflare's global network does not advertise your prefixes, and Cloudflare routes your packets to the next closest data center. To check the system status for Cloudflare's global network and dashboard, refer to <a href="https://www.cloudflarestatus.com/">Cloudflare System Status</a>.</p>
<h2 id="recovery">Recovery</h2>
<p>Once a tunnel is in the down state, global network servers continue to emit probes according to the cadence described earlier. When a probe returns healthy, the global network server that received the healthy packet immediately sends two more probes. If the two probes return healthy, Cloudflare WAN sets the tunnel status to degraded (as three consecutive successful probes no longer satisfy the condition for a down state).</p>
<p>Tunnels in a degraded state transition to healthy when the failure rate for the previous 30 probes is less than 0.1%. This transition may take up to 30 minutes.</p>
<p>Cloudflare WAN's tunnel health check system allows a tunnel to quickly transition from healthy to degraded or down, but transitions slowly from degraded or down to healthy. This behavior is called hysteresis and prevents routing changes caused by flapping and other intermittent network failures.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5543.md")
</aside>
<h2 id="example">Example</h2>
<p>Consider two tunnels and their associated routing priorities. Remember that lower route values have priority.</p>
<ul>
<li>Tunnel 1, route priority <code>100</code></li>
<li>Tunnel 2, route priority <code>200</code></li>
</ul>
<p>When both tunnels are in a healthy state, routing priority directs traffic exclusively to Tunnel 1 because its route priority of <code>100</code> beats that of Tunnel 2. Tunnel 2 does not receive any traffic, except for tunnel health check probes. Endpoint health checks only flow over Tunnel 1 to their destination inside the origin network.</p>
<h3 id="failure-response">Failure response</h3>
<p>If the link between Tunnel 1 and Cloudflare becomes unusable, Cloudflare global network servers discover the failure on their next health check probe, and immediately issue two more probes (assuming the tunnel was initially healthy).</p>
<p>When a global network server does not receive the proper ICMP reply packets from these two additional probes, the global network server labels Tunnel 1 as down, and downgrades Tunnel 1 priority to <code>1,000,100</code>. The priority then shifts to Tunnel 2, and Cloudflare WAN immediately steers packets arriving at that global network server to Tunnel 2.</p>
<h3 id="recovery-response">Recovery response</h3>
<p>Suppose the connectivity issue that set Tunnel 1 health to down becomes resolved. At the next health check interval, the issuing global network server receives a successful probe and immediately sends two more probes to validate tunnel health.</p>
<p>When all three probes return successfully, Cloudflare WAN transitions the tunnel from down to degraded. As part of this transition, Cloudflare reduces the priority penalty for that route so that its priority becomes <code>500,100</code>. Because Tunnel 2 has a priority of <code>200</code>, traffic continues to flow over Tunnel 2.</p>
<p>Global network servers continue probing Tunnel 1. When the health check failure rate drops below 0.1% for a five-minute period, Cloudflare WAN sets tunnel status to healthy. Cloudflare fully restores Tunnel 1's routing priority to <code>100</code>, and traffic steering returns the data flow to Tunnel 1.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>For help resolving tunnel health issues, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/tunnel-health/">Troubleshoot tunnel health</a>.</p>
