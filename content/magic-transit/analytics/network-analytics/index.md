<p><a href="/analytics/network-analytics/">Network Analytics</a> provides real-time insights into Magic Transit traffic that enters and leaves Cloudflare's network through GRE or IPsec tunnels.</p>
<p>Data is aggregated into time intervals that vary based on the selected zoom level. For example, a daily view shows 24-hour averages, which can flatten short-term traffic spikes. As a result, longer time intervals display lower peak bandwidth values compared to more granular views like five-minute intervals.</p>
<p>For details, refer to the <a href="/analytics/network-analytics/">Network Analytics</a> documentation.</p>
<h2 id="network-traffic-data-filters">Network traffic data filters</h2>
<p>With Magic Transit, you can account for traffic flows that enter Cloudflare's network, are blocked by DDoS rules or Cloudflare Network Firewall, and leave Cloudflare's network. This insight lets you track the total packets and bytes that traverse Cloudflare's network and are ultimately destined for your network. It also provides increased insight into traffic flows that are unaccounted for.</p>
<p>The complete list of filters includes:</p>
<ul>
<li>A list of your top tunnels by traffic volume.</li>
<li>Traffic source and destination by traffic type, on-ramps and off-ramps, <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/10707.md")
</div>, and ports.
- Destination IP ranges and ASNs.
- Protocols and packet sizes.
- Samples of all GRE or IPsec tunnel traffic entering or leaving Cloudflare's network.
- Mitigations applied (such as DDoS and Cloudflare Network Firewall) to traffic entering Cloudflare's network.
<p>For instructions, refer to <a href="#access-tunnel-traffic-analytics">Access tunnel traffic analytics</a>.</p>
<h2 id="access-tunnel-traffic-analytics">Access tunnel traffic analytics</h2>
<ol>
<li>Go to the <strong>Network Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In the <strong>All Traffic</strong> tab, scroll to <strong>Top Insights</strong> to access network traffic filters. By default, the dashboard displays five items, but you can display up to 25 items at once. To change the number of items, select the drop-down menu.</li>
<li>(Optional) Hover over a traffic type. You can then filter for that traffic or exclude it from the results.</li>
<li>To adjust the scope of information, scroll to <strong>All traffic</strong> &gt; <strong>Add filter</strong>.</li>
<li>In the <strong>New filter</strong> popover, select the data type from the left drop-down menu, an operator from the middle drop-down menu, and an action from the right drop-down menu. For example:</li>
</ol>
<pre><code class="language-txt">&lt;DESTINATION_TUNNELS&gt; | _equals_ | &lt;NAME_OF_YOUR_TUNNEL&gt;&#10;</code></pre>
<p>This lets you examine traffic from specific Source tunnels and/or Destination tunnels.</p>
<h2 id="feature-notes">Feature notes</h2>
<ul>
<li>For Magic Transit, <code>Non-Tunnel traffic</code> often represents traffic from the public Internet or traffic via <a href="/network-interconnect/">CNIs</a>.</li>
</ul>
<p>The label <code>Non-Tunnel traffic</code> is a placeholder, and Cloudflare will apply more specific labels to this category of traffic in the future.</p>
