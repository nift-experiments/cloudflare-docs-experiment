<p>When you use Cloudflare DNS, you can access data about DNS queries through a variety of sources.</p>
<hr />
<h2 id="analytics">Analytics</h2>
<p>DNS analytics allow you to evaluate data about DNS queries to your zone.</p>
<p>You can <a href="#view-on-the-dashboard">use the dashboard</a> to get insights quickly based on a <a href="#available-dimensions">predefined set of dimensions</a>, or <a href="#explore-with-the-api">use the API</a> to have access to all fields available in the GraphQL DNS analytics schemas.</p>
<p>When using GraphQL, you also have the option to get data for DNS queries across all zones within a given Cloudflare account.</p>
<h3 id="availability-and-limits">Availability and limits</h3>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Maximum time interval (zone)</td>
<td>7 days</td>
<td>31 days</td>
<td>31 days</td>
<td>62 days</td>
</tr>
<tr>
<td>Maximum time interval (account)</td>
<td>7 days</td>
<td>7 days</td>
<td>7 days</td>
<td>62 days</td>
</tr>
<tr>
<td>Historical data (zone)</td>
<td>8 days</td>
<td>31 days</td>
<td>31 days</td>
<td>62 days</td>
</tr>
<tr>
<td>Historical data (account)</td>
<td>8 days</td>
<td>8 days</td>
<td>8 days</td>
<td>62 days</td>
</tr>
</tbody>
</table>
<h3 id="view-on-the-dashboard">View on the dashboard</h3>
<p>For a quick summary, view your DNS analytics on the dashboard:</p>
<div class="nb-dash-button"></div>
<p>The DNS analytics dashboard contains <a href="#panels">four main panels</a>. The filters and time frame that you specify at the top of the page apply to all of them.</p>
<h4 id="available-dimensions">Available dimensions</h4>
<ul>
<li>Query name</li>
<li>Query type (same as DNS record type)</li>
<li>Response code</li>
<li>Data center</li>
<li>Source IP</li>
<li>Destination IP</li>
<li>Protocol</li>
<li>IP version</li>
</ul>
<h4 id="panels">Panels</h4>
<ul>
<li>
<p><strong>Query overview</strong>: the number of queries and their distribution over time. This information is segmented by each of the <a href="#available-dimensions">available dimensions</a> and the graph displays the top five values. You can select the dimensions through the different tabs above the graph and quickly filter for or exclude a certain value from the results by hovering over it and selecting <strong>Filter</strong> or <strong>Exclude</strong>.</p>
</li>
<li>
<p><strong>Query statistics</strong>: an overview of query metrics based on your filters and selected time frame. Namely, <strong>Total queries</strong>, <strong>Average queries per second</strong>, and <strong>Average processing time</strong>. The average processing time is displayed in milliseconds and includes upstream queries in the case of <a href="/dns/cname-flattening/">flattened CNAME records</a>.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7731.md")
</aside>
<ul>
<li>
<p><strong>DNS queries by data center</strong>: a map indicating which Cloudflare data centers have handled DNS queries to your zone in the selected time period. You can also find a list of the ten top results and quickly filter for or exclude a certain data center from the results by hovering over it and selecting <strong>Filter</strong> or <strong>Exclude</strong>.</p>
</li>
<li>
<p><strong>Queries by source</strong>: a breakdown of the top five, ten, or fifteen results - based on your selection - and grouped by the <a href="#available-dimensions">available dimensions</a>.</p>
</li>
</ul>
<h3 id="explore-with-the-api">Explore with the API</h3>
<p>For more detailed metrics, use the <a href="/analytics/graphql-api/">GraphQL API</a>. Refer to the GraphQL Analytics API documentation for guidance on how to <a href="/analytics/graphql-api/getting-started/">get started</a>.</p>
<p>The DNS analytics has two <a href="/analytics/graphql-api/getting-started/querying-basics/">schemas</a>:</p>
<ul>
<li><code>dnsAnalyticsAdaptive</code>: Retrieve information about individual DNS queries.</li>
<li><code>dnsAnalyticsAdaptiveGroups</code>: Get reports on aggregate information only.</li>
</ul>
<p>To get account-level data, you can set up queries similar to the following:</p>
<details class="nb-details" open><summary>Get the last 10,000 queries resulting in NXDOMAIN</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7732.md")
</div></details>
<details class="nb-details" open><summary>Get the overall query count per account</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7733.md")
</div></details>
<hr />
<h2 id="logs">Logs</h2>
<p>Logs let Enterprise customers view <a href="/logs/logpush/logpush-job/datasets/zone/dns_logs/">detailed information</a> about individual DNS queries.</p>
<p>For help setting up Logpush, refer to <a href="/logs/logpush/">Logpush</a> documentation.</p>
