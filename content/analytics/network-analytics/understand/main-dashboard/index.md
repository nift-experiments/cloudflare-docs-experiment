<p>The following sections are a guide on the different sections of the main Network Analytics dashboard.</p>
<h2 id="available-tabs">Available tabs</h2>
<p>The <strong>All traffic</strong> tab displays global information about layer 3/4 traffic, DNS traffic, and DDoS attacks. The dashboard has additional tabs with specific information (and specific filters) for different mitigation systems.</p>
<p>The following table contains a summary of what is shown in each tab:</p>
<table>
<thead>
<tr>
<th>Tab name</th>
<th>For Magic Transit users</th>
<th>For Spectrum users</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>All traffic</strong></td>
<td>Traffic dropped by DDoS managed rules, Advanced TCP Protection, Advanced DNS Protection, and Cloudflare Network Firewall, and traffic passed to the origin server.</td>
<td>Traffic dropped and passed by DDoS managed rules.</td>
</tr>
<tr>
<td><strong>DDoS managed <br/>rules</strong></td>
<td>Traffic dropped and passed by <a href="/ddos-protection/managed-rulesets/">DDoS managed rules</a>.</td>
<td>Traffic dropped and passed by <a href="/ddos-protection/managed-rulesets/">DDoS managed rules</a>.</td>
</tr>
<tr>
<td><strong>TCP <br/>Protection</strong></td>
<td>Traffic dropped and passed by the <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a> system. Does not include traffic dropped by DDoS managed rules.</td>
<td>N/A</td>
</tr>
<tr>
<td><strong>DNS <br/>Protection</strong></td>
<td>Traffic dropped and passed by the <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS Protection</a> system. Does not include traffic dropped by DDoS managed rules.</td>
<td>N/A</td>
</tr>
<tr>
<td><strong>Cloudflare Network Firewall</strong></td>
<td>Traffic dropped by <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> and traffic passed to the origin server. Does not include traffic dropped by DDoS managed rules, Advanced TCP Protection, or Advanced DNS Protection.</td>
<td>N/A</td>
</tr>
</tbody>
</table>
<p>Use these tabs to better understand the decisions made by each mitigation system, and which rules are being applied to mitigate attacks.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3183.md")
</aside>
<h2 id="high-level-metrics">High-level metrics</h2>
<p>The side panels in the Network Analytics page provide a summary of activity over the period selected in the time frame drop-down list.</p>
<p><img src="/assets/upstream/images/analytics/network-analytics/high-level-metrics.png" alt="Available high-level metrics in the Network Analytics dashboard" /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<p>Selecting one of the metrics in the sidebar will define the base unit (packets or bits/bytes) for the data displayed in the dashboard.</p>
<h2 id="executive-summary">Executive summary</h2>
<p><img src="/assets/upstream/images/analytics/network-analytics/executive-summary-card.png" alt="Executive summary card in the Network Analytics dashboard." /></p>
<p>The executive summary provides top insights and trends about DDoS attacks targeting your network, including the amount of attacks, percentage of attacks traffic mitigated relative to your traffic, largest attack rates, total mitigated attack bytes, top source, and estimated duration of the attacks.</p>
<p>These insights are adaptive based on the selected time frame and the <strong>Packets</strong> or <strong>Bytes</strong> <a href="#high-level-metrics">metrics</a> selector. The insights are also accompanied by the trends relative to the selected time period, visualized as period-over-period change in percentage and indicator arrows.</p>
<p>The executive summary also features a one-liner summary at the top, informing you about recent and ongoing attacks.</p>
<h3 id="total-attacks">Total attacks</h3>
<p>The total number of attacks is based on unique attack IDs of mitigations issued by the <a href="/ddos-protection/managed-rulesets/network/">Network-layer DDoS Attack Protection managed ruleset</a>.</p>
<p>Since the mitigation system may generate several mitigation rules (and therefore several attack IDs) for a single attack, the actual number of attacks may seem higher in some cases.</p>
<p>To obtain the metadata of recently mitigated DDoS attacks, query the <a href="/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/#dosdattackanalyticsgroups"><code>dosdAttackAnalyticsGroups</code></a> GraphQL node.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-about-attack-rates">Note about attack rates</h3>
@markup("md", "content/.markup/bodies/3182.md")
</aside>
<h2 id="filters">Filters</h2>
<p>In the main dashboard card you can apply filters to the displayed data.</p>
<p>You can filter by the following parameters:</p>
<ul>
<li>Mitigation action taken by Cloudflare</li>
<li>Mitigation system that performed the action</li>
<li>Source IP, port, ASN, tunnel</li>
<li><a href="#traffic-direction">Direction</a></li>
<li>Destination IP, port, IP range (description or CIDR of provisioned prefixes), tunnel</li>
<li>Source Cloudflare data center and data center country of where the traffic was observed</li>
<li>Packet size</li>
<li>TCP flag</li>
<li>TTL</li>
</ul>
<p>Note that the IP Range filter currently has a limitation that only supports filtering /24 IPv4 Ranges and /64 IPv6 Ranges.</p>
<p>Dashboard tabs for <a href="/analytics/network-analytics/understand/main-dashboard/#available-tabs">specific mitigation systems</a> (DDoS managed rules, Advanced TCP Protection, or Cloudflare Network Firewall) may have additional filter parameters.</p>
<h3 id="traffic-direction">Traffic direction</h3>
<p>The available values in the <strong>Direction</strong> filter have the following meaning, from the point of view of a specific customer's network:</p>
<ul>
<li><strong>Ingress</strong>: Incoming traffic from the public Internet (ingress) to the customer's network via Cloudflare's network (for example, through <a href="/magic-transit/">Magic Transit</a>);</li>
<li><strong>Egress</strong>: Outgoing traffic leaving the customer's network through Cloudflare's network to the public Internet (for example, through <a href="/magic-transit/reference/egress/">Magic Transit deployed with the egress option</a>);</li>
<li><strong>Lateral</strong>: Traffic that stayed within the customer's network, routed through Cloudflare's network (for example, traffic between customer office branches or data centers routed through <a href="/cloudflare-wan/">Cloudflare WAN</a>).</li>
</ul>
<h2 id="packets-summary-or-bits-summary">Packets summary or Bits summary</h2>
<p>Displays a plot of the traffic (in terms of bits or packets) in the selected time range according to the values of a given dimension. By default, Network Analytics displays data broken down by <strong>Action</strong>.</p>
<h3 id="available-dimensions">Available dimensions</h3>
<p>You can choose one of the following dimensions:</p>
<ul>
<li>Action</li>
<li>Destination IP</li>
<li>Destination IP range</li>
<li>Destination port</li>
<li>Destination tunnels</li>
<li>Mitigation system</li>
<li>Source ASN</li>
<li>Data center country</li>
<li>Source data center</li>
<li>Source IP</li>
<li>Source port</li>
<li>Source tunnels</li>
<li>Packet size</li>
<li>Protocol</li>
<li>TCP flag</li>
</ul>
<p>Dashboard tabs for <a href="/analytics/network-analytics/understand/main-dashboard/#available-tabs">specific mitigation systems</a> (DDoS managed rules, Advanced TCP Protection, or Cloudflare Network Firewall) may have additional dimensions.</p>
<h2 id="mitigation-system-distribution">Mitigation system distribution</h2>
<p>The <strong>Mitigation System Distribution</strong> card displays the amount of traffic (in terms of packets or bits) that was mitigated by each mitigation system.</p>
<h2 id="packet-sample-log">Packet sample log</h2>
<p>The Network Analytics <strong>Packet sample log</strong> shows up to 100 log events — including both allowed and dropped packets — in the currently selected time range, paginated with 10 results per page per time range view (the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> does not have this limitation).</p>
<p>Expand each row to display event details, including the full packet headers and metadata.</p>
<p>Dashboard tabs for <a href="/analytics/network-analytics/understand/main-dashboard/#available-tabs">specific mitigation systems</a> (DDoS managed rules, Advanced TCP Protection, or Cloudflare Network Firewall) may have additional fields in the expanded event details.</p>
<h2 id="data-center-country-source-data-center">Data center country/Source data center</h2>
<p>Displays the top source <a href="https://www.cloudflare.com/en-gb/network/">Cloudflare data centers</a> where the displayed traffic was ingested. The same card can also display the country associated with these top source data centers.</p>
<p>To switch between <strong>Data center country</strong> and <strong>Source data center</strong> information, use the dropdown in the card.</p>
<h2 id="top-insights">Top insights</h2>
<p>The different panels in <strong>Top insights</strong> display the top items in each dimension. To filter by a given value or exclude a value from displayed data, hover the value stats and select <strong>Filter</strong> or <strong>Exclude</strong>.</p>
<p>To set the number of items to display for each dimension, open the drop-down list associated with the view and select the desired number of items.</p>
<h2 id="tcp-flag">TCP flag</h2>
<p>The <strong>TCP Flag</strong> panel displays the TCP flags set for all the traffic currently displayed in the dashboard, including both allowed and mitigated traffic.</p>
