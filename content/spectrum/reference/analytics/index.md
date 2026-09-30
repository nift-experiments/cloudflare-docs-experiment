<p>Cloudflare measures the following metrics for every connection.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Name</th>
<th>Example</th>
<th>Unit</th>
</tr>
</thead>
<tbody>
<tr>
<td>count</td>
<td>Count of total events</td>
<td><code>1000</code></td>
<td>Count</td>
</tr>
<tr>
<td>bytesIngress</td>
<td>Sum of ingress bytes</td>
<td><code>1000</code></td>
<td>Sum</td>
</tr>
<tr>
<td>bytesEgress</td>
<td>Sum of egress bytes</td>
<td><code>1000</code></td>
<td>Sum</td>
</tr>
<tr>
<td>durationAvg</td>
<td>Average connection duration</td>
<td><code>1.0</code></td>
<td>Time in milliseconds</td>
</tr>
<tr>
<td>durationMedian</td>
<td>Median connection duration</td>
<td><code>1.0</code></td>
<td>Time in milliseconds</td>
</tr>
<tr>
<td>duration90th</td>
<td>90th percentile connection duration</td>
<td><code>1.0</code></td>
<td>Time in milliseconds</td>
</tr>
<tr>
<td>duration99th</td>
<td>99th percentile connection duration</td>
<td><code>1.0</code></td>
<td>Time in milliseconds</td>
</tr>
</tbody>
</table>
<h2 id="additional-dimensions">Additional dimensions</h2>
<p>You can divide your analytics further by the following dimensions.</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Name</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>event</td>
<td>Connection Event</td>
<td><code>connect</code>, <code>progress</code>, <code>disconnect</code>, <code>originError</code>, <code>clientFiltered</code></td>
</tr>
<tr>
<td>appID</td>
<td>Application ID</td>
<td><code>40d67c87c6cd4b889a4fd57805225e85</code></td>
</tr>
<tr>
<td>coloName</td>
<td>Colo Name</td>
<td><code>SFO</code></td>
</tr>
<tr>
<td>ipVersion</td>
<td>IP version used by the client</td>
<td><code>4</code>, <code>6</code></td>
</tr>
</tbody>
</table>
<h2 id="operators-for-filtering">Operators for filtering</h2>
<p>Use the operators below to filter data.</p>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Name</th>
<th>URL Encoded</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>==</code></td>
<td>Equals</td>
<td><code>%3D%3D</code></td>
</tr>
<tr>
<td><code>!=</code></td>
<td>Does not equal</td>
<td><code>!%3D</code></td>
</tr>
<tr>
<td><code>&gt;</code></td>
<td>Greater Than</td>
<td><code>%3E</code></td>
</tr>
<tr>
<td><code>&lt;</code></td>
<td>Less Than</td>
<td><code>%3C</code></td>
</tr>
<tr>
<td><code>&gt;=</code></td>
<td>Greater than or equal to</td>
<td><code>%3E%3D</code></td>
</tr>
<tr>
<td><code>&lt;=</code></td>
<td>Less than or equal to</td>
<td><code>%3C%3D</code></td>
</tr>
</tbody>
</table>
<p>Combine filters using <code>OR</code> and <code>AND</code> boolean logic:</p>
<ul>
<li><code>AND</code> takes precedence over <code>OR</code> in all expressions.</li>
<li>The <code>OR</code> operator is defined using a comma <code>,</code> or the <code>OR</code> keyword surrounded by whitespace.</li>
<li>The <code>AND</code> operator is defined using a semicolon <code>;</code> or the <code>AND</code> keyword surrounded by whitespace.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13873.md")
</aside>
<h2 id="analytics-request-structure">Analytics request structure</h2>
<pre><code class="language-txt">/api/v4/zones/{zone_id}/spectrum/analytics/events/summary?metrics=METRICS&amp;dimensions=DIMENSIONS&amp;filters=FILTERS&amp;since=FROM_TS&amp;sort=SORT&amp;until=TO_TS&amp;limit=LIMIT&#10;/api/v4/zones/{zone_id}/spectrum/analytics/events/bytime?metrics=METRICS&amp;dimensions=DIMENSIONS&amp;filters=FILTERS&amp;since=FROM_TS&amp;sort=SORT&amp;until=TO_TS&amp;limit=LIMIT&#10;</code></pre>
<ul>
<li>METRICS is one or more metrics (such as count) to compute</li>
<li>DIMENSIONS can be used to break down the data by given attributes</li>
<li>FILTERS used to filter rows by one or more dimensions (see Filters section below)</li>
<li>SORT is the sort order for the result set; sort fields must be included in METRICS or DIMENSIONS</li>
<li>TO_TS is that end of time interval to query, defaults to current time</li>
<li>FROM_TS is that start of time interval to query, defaults to TO_TS - 6 hours</li>
<li>STEP is used to select time series resolution when using endpoint:</li>
<li>auto or omitted - selects time step most appropriate to time interval
<ul>
<li>year</li>
<li>quarter</li>
<li>month</li>
<li>week</li>
<li>day</li>
<li>hour</li>
</ul>
</li>
</ul>
<h2 id="analytics-query-example">Analytics query example</h2>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/spectrum/analytics/events/summary \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<p>Refer to the <a href="/api/resources/spectrum/subresources/analytics/subresources/aggregates/subresources/currents/methods/get/">Spectrum API documentation</a> for more examples of API requests.</p>
