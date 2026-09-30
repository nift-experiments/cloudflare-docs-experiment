<p>KV exposes analytics that allow you to inspect requests and storage across all namespaces in your account.</p>
<p>The metrics displayed in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> charts are queried from Cloudflare’s <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. You can access the metrics <a href="#query-via-the-graphql-api">programmatically</a> via GraphQL or HTTP client.</p>
<h2 id="metrics">Metrics</h2>
<p>KV currently exposes the below metrics:</p>
<table>
<thead>
<tr>
<th>Dataset</th>
<th>GraphQL Dataset Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Operations</td>
<td><code>kvOperationsAdaptiveGroups</code></td>
<td>This dataset consists of the operations made to your KV namespaces.</td>
</tr>
<tr>
<td>Storage</td>
<td><code>kvStorageAdaptiveGroups</code></td>
<td>This dataset consists of the storage details of your KV namespaces.</td>
</tr>
</tbody>
</table>
<p>Metrics can be queried (and are retained) for the past 31 days.</p>
<h2 id="view-metrics-in-the-dashboard">View metrics in the dashboard</h2>
<p>Per-namespace analytics for KV are available in the Cloudflare dashboard. To view current and historical metrics for a database:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers KV</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select an existing namespace.
3. Select the **Metrics** tab.
<p>You can optionally select a time window to query. This defaults to the last 24 hours.</p>
<h2 id="query-via-the-graphql-api">Query via the GraphQL API</h2>
<p>You can programmatically query analytics for your KV namespaces via the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. This API queries the same datasets as the Cloudflare dashboard, and supports GraphQL <a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a>.</p>
<p>To get started using the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>, follow the documentation to setup <a href="/analytics/graphql-api/getting-started/authentication/">Authentication for the GraphQL Analytics API</a>.</p>
<p>To use the GraphQL API to retrieve KV's datasets, you must provide the <code>accountTag</code> filter with your Cloudflare Account ID. The GraphQL datasets for KV include:</p>
<ul>
<li><code>kvOperationsAdaptiveGroups</code></li>
<li><code>kvStorageAdaptiveGroups</code></li>
</ul>
<h3 id="examples">Examples</h3>
<p>The following are common GraphQL queries that you can use to retrieve information about KV analytics. These queries make use of variables <code>$accountTag</code>, <code>$date_geq</code>, <code>$date_leq</code>, and <code>$namespaceId</code>, which should be set as GraphQL variables or replaced in line. These variables should look similar to these:</p>
<pre><code class="language-json">{&#10;	&quot;accountTag&quot;: &quot;&lt;YOUR_ACCOUNT_ID&gt;&quot;,&#10;	&quot;namespaceId&quot;: &quot;&lt;YOUR_KV_NAMESPACE_ID&gt;&quot;,&#10;	&quot;date_geq&quot;: &quot;2024-07-15&quot;,&#10;	&quot;date_leq&quot;: &quot;2024-07-30&quot;&#10;}&#10;</code></pre>
<h4 id="operations">Operations</h4>
<p>To query the sum of read, write, delete, and list operations for a given <code>namespaceId</code> and for a given date range (<code>start</code> and <code>end</code>), grouped by <code>date</code> and <code>actionType</code>:</p>
<pre><code class="language-graphql">query KvOperationsSample(&#10;	$accountTag: string!&#10;	$namespaceId: string&#10;	$start: Date&#10;	$end: Date&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			kvOperationsAdaptiveGroups(&#10;				filter: { namespaceId: $namespaceId, date_geq: $start, date_leq: $end }&#10;				limit: 10000&#10;				orderBy: [date_DESC]&#10;			) {&#10;				sum {&#10;					requests&#10;				}&#10;				dimensions {&#10;					date&#10;					actionType&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>To query the distribution of the latency for read operations for a given <code>namespaceId</code> within a given date range (<code>start</code>, <code>end</code>):</p>
<pre><code class="language-graphql">query KvOperationsSample2(&#10;	$accountTag: string!&#10;	$namespaceId: string&#10;	$start: Date&#10;	$end: Date&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			kvOperationsAdaptiveGroups(&#10;				filter: {&#10;					namespaceId: $namespaceId&#10;					date_geq: $start&#10;					date_leq: $end&#10;					actionType: &quot;read&quot;&#10;				}&#10;				limit: 10000&#10;			) {&#10;				sum {&#10;					requests&#10;				}&#10;				dimensions {&#10;					actionType&#10;				}&#10;				quantiles {&#10;					latencyMsP25&#10;					latencyMsP50&#10;					latencyMsP75&#10;					latencyMsP90&#10;					latencyMsP99&#10;					latencyMsP999&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>To query your account-wide read, write, delete, and list operations across all KV namespaces:</p>
<pre><code class="language-graphql">query KvOperationsAllSample($accountTag: string!, $start: Date, $end: Date) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			kvOperationsAdaptiveGroups(&#10;				filter: { date_geq: $start, date_leq: $end }&#10;				limit: 10000&#10;			) {&#10;				sum {&#10;					requests&#10;				}&#10;				dimensions {&#10;					actionType&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h4 id="storage">Storage</h4>
<p>To query the storage details (<code>keyCount</code> and <code>byteCount</code>) of a KV namespace for every day of a given date range:</p>
<pre><code class="language-graphql">query Viewer(&#10;	$accountTag: string!&#10;	$namespaceId: string&#10;	$start: Date&#10;	$end: Date&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			kvStorageAdaptiveGroups(&#10;				filter: { date_geq: $start, date_leq: $end, namespaceId: $namespaceId }&#10;				limit: 10000&#10;				orderBy: [date_DESC]&#10;			) {&#10;				max {&#10;					keyCount&#10;					byteCount&#10;				}&#10;				dimensions {&#10;					date&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
