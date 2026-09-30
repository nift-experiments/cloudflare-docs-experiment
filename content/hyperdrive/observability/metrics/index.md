<p>Hyperdrive exposes analytics that allow you to inspect query volume, query latency, cache hit ratios, and connection pool metrics for each Hyperdrive configuration in your account.</p>
<h2 id="metrics">Metrics</h2>
<p>Hyperdrive currently exports metrics via the <code>hyperdriveQueriesAdaptiveGroups</code> and <code>hyperdrivePoolSizesAdaptiveGroups</code> GraphQL datasets.</p>
<h3 id="query-metrics">Query metrics</h3>
<p>The <code>hyperdriveQueriesAdaptiveGroups</code> dataset contains the following metrics:</p>
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
<td>Queries</td>
<td><code>count</code></td>
<td>The number of queries issued against your Hyperdrive in the given time period.</td>
</tr>
<tr>
<td>Cache Status</td>
<td><code>cacheStatus</code></td>
<td>Whether the query was cached or not. Can be one of <code>disabled</code>, <code>hit</code>, <code>miss</code>, <code>uncacheable</code>, <code>multiplestatements</code>, <code>notaquery</code>, <code>oversizedquery</code>, <code>oversizedresult</code>, <code>parseerror</code>, <code>transaction</code>, and <code>volatile</code>.</td>
</tr>
<tr>
<td>Query Bytes</td>
<td><code>queryBytes</code></td>
<td>The size of your queries, in bytes.</td>
</tr>
<tr>
<td>Result Bytes</td>
<td><code>resultBytes</code></td>
<td>The size of your query <em>results</em>, in bytes.</td>
</tr>
<tr>
<td>Connection Latency</td>
<td><code>connectionLatency</code></td>
<td>The time (in milliseconds) required to establish new connections from Hyperdrive to your database, as measured from your Hyperdrive connection pool(s).</td>
</tr>
<tr>
<td>Query Latency</td>
<td><code>queryLatency</code></td>
<td>The time (in milliseconds) required to query (and receive results) from your database, as measured from your Hyperdrive connection pool(s).</td>
</tr>
<tr>
<td>Event Status</td>
<td><code>eventStatus</code></td>
<td>Whether a query responded successfully (<code>complete</code>) or failed (<code>error</code>).</td>
</tr>
</tbody>
</table>
<p>The <code>volatile</code> cache status indicates the query contains a PostgreSQL function categorized as <code>STABLE</code> or <code>VOLATILE</code> (for example, <code>NOW()</code>, <code>RANDOM()</code>). Refer to <a href="/hyperdrive/concepts/query-caching/">Query caching</a> for details on which functions affect cacheability.</p>
<h3 id="pool-size-metrics">Pool size metrics</h3>
<p>The <code>hyperdrivePoolSizesAdaptiveGroups</code> dataset contains the following connection pool metrics:</p>
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
<td>Avg. open connections</td>
<td><code>avg.currentPoolSize</code></td>
<td>Average number of connections currently open in the pool.</td>
</tr>
<tr>
<td>Avg. available slots</td>
<td><code>avg.availablePoolSlots</code></td>
<td>Average number of pool connections available for checkout.</td>
</tr>
<tr>
<td>Avg. waiting clients</td>
<td><code>avg.waitingClients</code></td>
<td>Average number of clients waiting for a connection from the pool.</td>
</tr>
<tr>
<td>Pool size maximum</td>
<td><code>max.maxPoolSize</code></td>
<td>Configured maximum size of the connection pool.</td>
</tr>
<tr>
<td>Peak open connections</td>
<td><code>max.currentPoolSize</code></td>
<td>Peak number of connections open in the pool.</td>
</tr>
<tr>
<td>Peak waiting clients</td>
<td><code>max.waitingClients</code></td>
<td>Peak number of clients waiting for a connection from the pool.</td>
</tr>
</tbody>
</table>
<p>Connection contention appears as a spike in waiting clients, or when open connections consistently approach the pool size maximum. If your open connections regularly approach this limit, consider <a href="/hyperdrive/platform/limits/#request-a-limit-increase">increasing your Hyperdrive connection limit</a>.</p>
<p>Metrics can be queried (and are retained) for the past 31 days.</p>
<h2 id="view-metrics-in-the-dashboard">View metrics in the dashboard</h2>
<p>Per-database analytics for Hyperdrive are available in the Cloudflare dashboard. To view current and historical metrics for a Hyperdrive configuration:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Hyperdrive</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select an existing Hyperdrive configuration.</li>
<li>Select the <strong>Metrics</strong> tab.</li>
</ol>
<p>You can optionally select a time window to query. This defaults to the last 24 hours.</p>
<p>The dashboard includes a <strong>Pool connections</strong> chart, which displays waiting connections, open connections, and the pool size maximum. You can use the location selector to filter by specific Cloudflare locations.</p>
<h2 id="query-via-the-graphql-api">Query via the GraphQL API</h2>
<p>You can programmatically query analytics for your Hyperdrive configurations via the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. This API queries the same datasets as the Cloudflare dashboard, and supports GraphQL <a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a>.</p>
<p>Hyperdrive's GraphQL datasets require an <code>accountTag</code> filter with your Cloudflare account ID. Hyperdrive exposes the <code>hyperdriveQueriesAdaptiveGroups</code> and <code>hyperdrivePoolSizesAdaptiveGroups</code> datasets.</p>
<h2 id="write-graphql-queries">Write GraphQL queries</h2>
<p>Examples of how to explore your Hyperdrive metrics.</p>
<h3 id="get-the-number-of-queries-handled-via-your-hyperdrive-config-by-cache-status">Get the number of queries handled via your Hyperdrive config by cache status</h3>
<pre><code class="language-graphql">query HyperdriveQueries(&#10;	$accountTag: string!&#10;	$configId: string!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			hyperdriveQueriesAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					configId: $configId&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;			) {&#10;				count&#10;				dimensions {&#10;					cacheStatus&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="get-the-average-query-and-connection-latency-for-queries-handled-via-your-hyperdrive-config-within-a-range-of-time-excluding-queries-that-failed-due-to-an-error">Get the average query and connection latency for queries handled via your Hyperdrive config within a range of time, excluding queries that failed due to an error</h3>
<pre><code class="language-graphql">query AverageHyperdriveLatencies(&#10;	$accountTag: string!&#10;	$configId: string!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			hyperdriveQueriesAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					configId: $configId&#10;					eventStatus: &quot;complete&quot;&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;			) {&#10;				avg {&#10;					connectionLatency&#10;					queryLatency&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="get-the-total-amount-of-query-and-result-bytes-flowing-through-your-hyperdrive-config">Get the total amount of query and result bytes flowing through your Hyperdrive config</h3>
<pre><code class="language-graphql">query HyperdriveQueryAndResultBytesForSuccessfulQueries(&#10;	$accountTag: string!&#10;	$configId: string!&#10;	$datetimeStart: Date!&#10;	$datetimeEnd: Date!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			hyperdriveQueriesAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					configId: $configId&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;			) {&#10;				sum {&#10;					queryBytes&#10;					resultBytes&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="get-the-pool-size-metrics-for-your-hyperdrive-config">Get the pool size metrics for your Hyperdrive config</h3>
<pre><code class="language-graphql">query HyperdrivePoolSizes(&#10;	$accountTag: string!&#10;	$configId: string!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			hyperdrivePoolSizesAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					configId: $configId&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;			) {&#10;				avg {&#10;					currentPoolSize&#10;					availablePoolSlots&#10;					waitingClients&#10;				}&#10;				max {&#10;					maxPoolSize&#10;					currentPoolSize&#10;					waitingClients&#10;				}&#10;				dimensions {&#10;					coloCode&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
