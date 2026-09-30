<p>Gateway analytics include three separate dashboards:</p>
<ul>
<li>HTTP request analytics.</li>
<li>DNS query analytics.</li>
<li>Network policy analytics.</li>
</ul>
<p>To review Gateway analytics:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong>.</li>
<li>Go to <strong>Dashboards</strong>.</li>
<li>Select your desired dashboard.</li>
</ol>
<p>Refer to <a href="/cloudflare-one/insights/">Insights overview</a> to learn how to use Analytics dashboards together with <a href="/cloudflare-one/insights/analytics-overview/">Analytics Overview</a> and <a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> for complete visibility and troubleshooting.</p>
<h2 id="http-request-analytics">HTTP request analytics</h2>
<p>Your <a href="/cloudflare-one/traffic-policies/http-policies/">Gateway HTTP policies</a> power the HTTP request analytics dashboard. If you are not using Gateway HTTP policies, the dashboard will appear empty.</p>
<p>The HTTP request analytics dashboard helps you identify trends in how your HTTP policies apply over time. By visualizing allowed, <a href="/cloudflare-one/remote-browser-isolation/">isolated</a> (rendered in a remote browser), and <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">Do Not Inspect</a> (bypassing TLS decryption) requests, the dashboard provides insights into traffic behavior and policy trends, making it easier to spot anomalies or shifts in usage patterns.</p>
<p>To review a detailed description of an HTTP request and its associated policy:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong>.</li>
<li>Select <strong>Logs</strong>.</li>
<li>Select <strong>HTTP request logs</strong>.</li>
<li>Use the <strong>Policy</strong> filter to view HTTP requests that triggered a policy or other filters to narrow down your results.</li>
</ol>
<h3 id="provided-analytics">Provided analytics</h3>
<ul>
<li>HTTP Requests over time
<ul>
<li>Time series view of HTTP requests</li>
</ul>
</li>
<li>Top Actions</li>
<li>Top Countries</li>
<li>Top Blocked Users</li>
<li>Top Bandwidth Consumers</li>
<li>Top Devices</li>
<li>Top Source IPs</li>
</ul>
<h2 id="dns-query-analytics">DNS query analytics</h2>
<p>Your <a href="/cloudflare-one/traffic-policies/dns-policies/">Gateway DNS policies</a> power the DNS query analytics dashboard. If you are not using Gateway DNS policies, the dashboard will appear empty.</p>
<p>The DNS query analytics dashboard helps you identify trends in how your DNS policies apply over time. By visualizing allowed, blocked, and overridden (DNS response replaced by a policy-defined address) queries, the dashboard provides insights into traffic behavior and policy trends, making it easier to spot anomalies or shifts in usage patterns.</p>
<p>To review a detailed description of a DNS query and its associated policy:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong>.</li>
<li>Select <strong>Logs</strong>.</li>
<li>Select <strong>DNS query logs</strong>.</li>
<li>Use the <strong>Policy</strong> filter to view DNS queries that triggered a policy or other filters to narrow down your results.</li>
</ol>
<h3 id="provided-analytics-1">Provided analytics</h3>
<ul>
<li>DNS Queries over time
<ul>
<li>Time series view of DNS queries</li>
</ul>
</li>
<li>Top Actions</li>
<li>Top Countries</li>
<li>Top Blocked Users</li>
<li>Top Allowed Users</li>
<li>Top Blocked Devices</li>
</ul>
<h2 id="network-policy-analytics">Network policy analytics</h2>
<p>Your <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a> power the Network policy analytics dashboard. If you are not using Gateway network policies, the dashboard will appear empty.</p>
<p>The Network policy analytics dashboard helps you identify trends in how your Gateway network policies apply over time. By visualizing allowed, blocked, and overridden (traffic rerouted by a policy-defined rule) sessions, the dashboard provides insights into traffic behavior and policy trends, making it easier to spot anomalies or shifts in usage patterns.</p>
<p>To review a detailed description of a network session and its associated policy:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong>.</li>
<li>Select <strong>Logs</strong>.</li>
<li>Select <strong>Network logs</strong>.</li>
<li>Use the <strong>Policy</strong> filter to view network sessions that triggered a policy or other filters to narrow down your results.</li>
</ol>
<h3 id="provided-analytics-2">Provided analytics</h3>
<ul>
<li>Network Sessions over time
<ul>
<li>Time series view of network sessions</li>
</ul>
</li>
<li>Top Actions</li>
<li>Top Countries</li>
<li>Top Blocked Users</li>
<li>Top Bandwidth Consumers</li>
<li>Top Devices</li>
<li>Top Source IPs</li>
</ul>
<h2 id="graphql-queries">GraphQL queries</h2>
<p>You can use the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> to query your Gateway Analytics data. Available <a href="/analytics/graphql-api/features/data-sets/">datasets</a> for Gateway include:</p>
<table>
<thead>
<tr>
<th>Dataset</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gatewayL4DownstreamSessionsAdaptiveGroups</code></td>
<td>Metrics for Gateway network sessions from user devices to the Cloudflare global network.</td>
</tr>
<tr>
<td><code>gatewayL4UpstreamSessionsAdaptiveGroups</code></td>
<td>Metrics for Gateway network sessions from the Cloudflare global network to user devices.</td>
</tr>
<tr>
<td><code>gatewayL4SessionsAdaptiveGroups</code></td>
<td>Metrics for Gateway network sessions with adaptive sampling.</td>
</tr>
<tr>
<td><code>gatewayL7RequestsAdaptiveGroups</code></td>
<td>Metrics for Gateway HTTP requests with adaptive sampling.</td>
</tr>
<tr>
<td><code>gatewayResolverQueriesAdaptiveGroups</code></td>
<td>Metrics for Gateway DNS queries with adaptive sampling.</td>
</tr>
<tr>
<td><code>gatewayResolverByRuleExecutionPerformanceAdaptiveGroups</code></td>
<td>Time to execute Gateway DNS policies on the Cloudflare global network.</td>
</tr>
<tr>
<td><code>gatewayResolverByCustomResolverGroups</code></td>
<td>Metrics for Gateway DNS queries resolved using custom resolvers.</td>
</tr>
<tr>
<td><code>gatewayResolverByCategoryAdaptiveGroups</code></td>
<td>Metrics for Gateway DNS queries sorted by <a href="/cloudflare-one/traffic-policies/domain-categories/">domain category</a> with adaptive sampling.</td>
</tr>
</tbody>
</table>
<p>To explore the schema, you can use a GraphQL client such as <a href="https://github.com/graphql/graphiql/tree/main/packages/graphiql#readme">GraphiQL</a> or <a href="https://altairgraphql.dev/">Altair</a>.</p>
<ol>
<li><a href="/analytics/graphql-api/getting-started/authentication/api-token-auth/">Create an API token</a> with the following permissions:</li>
</ol>
<table>
<thead>
<tr>
<th>Type</th>
<th>Item</th>
<th>Permission</th>
</tr>
</thead>
<tbody>
<tr>
<td>Account</td>
<td>Account Analytics</td>
<td>Read</td>
</tr>
</tbody>
</table>
<ol start="2">
<li>In your GraphQL client, <a href="/analytics/graphql-api/getting-started/authentication/graphql-client-headers/">add your API token</a> as an Authorization header.</li>
<li>Compose a query to access your Gateway Analytics datasets. For example, you can query the <code>gatewayResolverQueriesAdaptiveGroups</code> dataset to return the adaptive groups of DNS queries resolved by Gateway:</li>
</ol>
<pre><code class="language-graphql">query GatewaySampleQuery($accountTag: string!, $start: Time) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			gatewayResolverQueriesAdaptiveGroups(&#10;				filter: { datetime_gt: $start }&#10;				limit: 10&#10;			) {&#10;				count&#10;				dimensions {&#10;					queryNameReversed&#10;					resolverDecision&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>For more information, refer to <a href="/analytics/graphql-api/getting-started/compose-graphql-query/">Compose a query in GraphiQL</a>.</p>
