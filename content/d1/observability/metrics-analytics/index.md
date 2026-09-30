<p>D1 exposes database analytics that allow you to inspect query volume, query latency, and storage size across all and/or each database in your account.</p>
<p>The metrics displayed in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> charts are queried from Cloudflare’s <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. You can access the metrics <a href="#query-via-the-graphql-api">programmatically</a> via GraphQL or HTTP client.</p>
<h2 id="metrics">Metrics</h2>
<p>D1 currently exports the below metrics:</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>GraphQL Field Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Read Queries (qps)</td>
<td><code>readQueries</code></td>
<td>The number of read queries issued against a database. This is the raw number of read queries, and is not used for billing.</td>
</tr>
<tr>
<td>Write Queries (qps)</td>
<td><code>writeQueries</code></td>
<td>The number of write queries issued against a database. This is the raw number of write queries, and is not used for billing.</td>
</tr>
<tr>
<td>Rows read (count)</td>
<td><code>rowsRead</code></td>
<td>The number of rows read (scanned) across your queries. See <a href="/d1/platform/pricing/">Pricing</a> for more details on how rows are counted.</td>
</tr>
<tr>
<td>Rows written (count)</td>
<td><code>rowsWritten</code></td>
<td>The number of rows written across your queries.</td>
</tr>
<tr>
<td>Query Response (bytes)</td>
<td><code>queryBatchResponseBytes</code></td>
<td>The total response size of the serialized query response, including any/all column names, rows and metadata. Reported in bytes.</td>
</tr>
<tr>
<td>Query Latency (ms)</td>
<td><code>queryBatchTimeMs</code></td>
<td>The total query response time, including response serialization, on the server-side. Reported in milliseconds.</td>
</tr>
<tr>
<td>Storage (Bytes)</td>
<td><code>databaseSizeBytes</code></td>
<td>Maximum size of a database. Reported in bytes.</td>
</tr>
</tbody>
</table>
<p>Metrics can be queried (and are retained) for the past 31 days.</p>
<h3 id="row-counts">Row counts</h3>
<p>D1 returns the number of rows read, rows written (or both) in response to each individual query via <a href="/d1/worker-api/return-object/">the Workers Binding API</a>.</p>
<p>Row counts are a precise count of how many rows were read (scanned) or written by that query.
Inspect row counts to understand the performance and cost of a given query, including whether you can reduce the rows read <a href="/d1/best-practices/use-indexes/">using indexes</a>. Use query counts to understand the total volume of traffic against your databases and to discern which databases are actively in-use.</p>
<p>Refer to the <a href="/d1/platform/pricing/">Pricing documentation</a> for more details on how rows are counted.</p>
<h2 id="view-metrics-in-the-dashboard">View metrics in the dashboard</h2>
<p>Per-database analytics for D1 are available in the Cloudflare dashboard. To view current and historical metrics for a database:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>D1</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select an existing D1 database.
3. Select the **Metrics** tab.
<p>You can optionally select a time window to query. This defaults to the last 24 hours.</p>
<h2 id="query-via-the-graphql-api">Query via the GraphQL API</h2>
<p>You can programmatically query analytics for your D1 databases via the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. This API queries the same datasets as the Cloudflare dashboard, and supports GraphQL <a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a>.</p>
<p>D1's GraphQL datasets require an <code>accountTag</code> filter with your Cloudflare account ID and include:</p>
<ul>
<li><code>d1AnalyticsAdaptiveGroups</code></li>
<li><code>d1StorageAdaptiveGroups</code></li>
<li><code>d1QueriesAdaptiveGroups</code></li>
</ul>
<h3 id="examples">Examples</h3>
<p>To query the sum of <code>readQueries</code>, <code>writeQueries</code> for a given <code>$databaseId</code>, grouping by <code>databaseId</code> and <code>date</code>:</p>
<pre><code class="language-graphql">query D1ObservabilitySampleQuery(&#10;	$accountTag: string!&#10;	$start: Date&#10;	$end: Date&#10;	$databaseId: string&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			d1AnalyticsAdaptiveGroups(&#10;				limit: 10000&#10;				filter: { date_geq: $start, date_leq: $end, databaseId: $databaseId }&#10;				orderBy: [date_DESC]&#10;			) {&#10;				sum {&#10;					readQueries&#10;					writeQueries&#10;				}&#10;				dimensions {&#10;					date&#10;					databaseId&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>To query both the average <code>queryBatchTimeMs</code> and the 90th percentile <code>queryBatchTimeMs</code> per database:</p>
<pre><code class="language-graphql">query D1ObservabilitySampleQuery2(&#10;	$accountTag: string!&#10;	$start: Date&#10;	$end: Date&#10;	$databaseId: string&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountId }) {&#10;			d1AnalyticsAdaptiveGroups(&#10;				limit: 10000&#10;				filter: { date_geq: $start, date_leq: $end, databaseId: $databaseId }&#10;				orderBy: [date_DESC]&#10;			) {&#10;				quantiles {&#10;					queryBatchTimeMsP90&#10;				}&#10;				dimensions {&#10;					date&#10;					databaseId&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>To query your account-wide <code>readQueries</code> and <code>writeQueries</code>:</p>
<pre><code class="language-graphql">query D1ObservabilitySampleQuery3(&#10;	$accountTag: string!&#10;	$start: Date&#10;	$end: Date&#10;	$databaseId: string&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			d1AnalyticsAdaptiveGroups(&#10;				limit: 10000&#10;				filter: { date_geq: $start, date_leq: $end, databaseId: $databaseId }&#10;			) {&#10;				sum {&#10;					readQueries&#10;					writeQueries&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h2 id="query-insights">Query <code>insights</code></h2>
<p>D1 provides metrics that let you understand and debug query performance. You can access these via GraphQL's <code>d1QueriesAdaptiveGroups</code> or <code>wrangler d1 insights</code> command.</p>
<p>D1 captures your query strings to make it easier to analyze metrics across query executions. <a href="/d1/worker-api/prepared-statements/#guidance">Bound parameters</a> are not captured to remove any sensitive information.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7348.md")
</aside>
<table>
<thead>
<tr>
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>--timePeriod</code></td>
<td>Fetch data from now to the provided time period (default: <code>1d</code>).</td>
</tr>
<tr>
<td><code>--sort-type</code></td>
<td>The operation you want to sort insights by. Select between <code>sum</code> and <code>avg</code> (default: <code>sum</code>).</td>
</tr>
<tr>
<td><code>--sort-by</code></td>
<td>The field you want to sort insights by. Select between <code>time</code>, <code>reads</code>, <code>writes</code>, and <code>count</code> (default: <code>time</code>).</td>
</tr>
<tr>
<td><code>--sort-direction</code></td>
<td>The sort direction. Select between <code>ASC</code> and <code>DESC</code> (default: <code>DESC</code>).</td>
</tr>
<tr>
<td><code>--json</code></td>
<td>A boolean value to specify whether to return the result as clean JSON (default: <code>false</code>).</td>
</tr>
<tr>
<td><code>--limit</code></td>
<td>The maximum number of queries to be fetched.</td>
</tr>
</tbody>
</table>
<details class="nb-details"><summary>To find top 3 queries by execution count:</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7349.md")
</div></details>
<details class="nb-details"><summary>To find top 3 queries by average execution time:</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7350.md")
</div></details>
<details class="nb-details"><summary>To find top 10 queries by rows written in last 7 days:</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7351.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7347.md")
</aside>
