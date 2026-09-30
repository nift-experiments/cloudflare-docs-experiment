<p>Workers Analytics Engine is priced based on two metrics — data points written, and read queries.</p>
<table>
<thead>
<tr>
<th>Plan</th>
<th>Data points written</th>
<th>Read queries</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Workers Paid</strong></td>
<td>10 million included per month <br /> (+$0.25 per additional million)</td>
<td>1 million included per month (+$1.00 per additional million)</td>
</tr>
<tr>
<td><strong>Workers Free</strong></td>
<td>100,000 included per day</td>
<td>10,000 included per day</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="pricing-availability">Pricing availability</h3>
@markup("md", "content/.markup/bodies/3136.md")
</aside>
<h3 id="data-points-written">Data points written</h3>
<p>Every time you call <a href="/analytics/analytics-engine/get-started/#2-write-data-points-from-your-worker"><code>writeDataPoint()</code></a> in a Worker, this counts as one data point written.</p>
<p>Each data point written costs the same amount. There is no extra cost to add dimensions or cardinality, and no additional cost for writing more data in a single data point.</p>
<h3 id="read-queries">Read queries</h3>
<p>Every time you post to Workers Analytics Engine's <a href="/analytics/analytics-engine/sql-api/">SQL API</a>, this counts as one read query.</p>
<p>Each read query costs the same amount. There is no extra cost for more or less complex queries, and no extra cost for reading only a few rows of data versus many rows of data.</p>
