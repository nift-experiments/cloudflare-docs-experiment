<p>Cloudflare measures Cloudflare WAN (formerly Magic WAN) usage based on the 95th percentile of bandwidth utilized by your configured network. This measurement reflects your overall network capacity consumption.</p>
<h2 id="how-bandwidth-is-measured">How bandwidth is measured</h2>
<p>Cloudflare WAN bandwidth includes the sum of traffic routed to and from the Cloudflare WAN network namespace across all your connections. This measurement includes traffic from the following tunnel types:</p>
<ul>
<li><a href="https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/">GRE (Generic Routing Encapsulation)</a></li>
<li><a href="https://www.cloudflare.com/learning/network-layer/what-is-ipsec/">IPsec (Internet Protocol Security)</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/zero-trust/cloudflare-tunnel/">Cloudflare Tunnel</a></li>
<li><a href="/network-interconnect/">Cloudflare Network Interconnect</a></li>
</ul>
<p>For each tunnel, Cloudflare uses the highest 95th percentile value (ingress or egress traffic). The usage measurement excludes <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> traffic.</p>
<h2 id="95th-percentile-calculation">95th percentile calculation</h2>
<p>The 95th percentile method is an industry-standard approach to bandwidth measurement that accounts for short traffic spikes. By discarding the highest 5% of samples, the measurement reflects your sustained bandwidth usage rather than momentary peaks.</p>
<p>To calculate the 95th percentile, Cloudflare records bandwidth to and from the global network at five-minute intervals, sorts these measurements in descending order, and discards the top 5% of recorded measurements. The highest remaining value is the 95th percentile bandwidth measurement for that time period.</p>
