<p>Magic Transit uses endpoint health checks to determine the overall health of your <a href="/magic-transit/reference/gre-ipsec-tunnels/">inter-network connections</a>. Probes originate from Cloudflare infrastructure, outside customer network namespaces, and target IP addresses deep within your network, beyond the tunnel-terminating border router. These &quot;long distance&quot; probes are purely diagnostic.</p>
<p>When choosing which endpoint IP addresses to monitor with health checks, use these guidelines:</p>
<ul>
<li>Provide one IP address for each of the prefixes Cloudflare advertises.</li>
<li>Redundant IPs routed through the same ISP (Internet Service Provider) and infrastructure are not necessary but are useful when troubleshooting.</li>
</ul>
<p>Cloudflare pings health check IPs from within the <a href="https://www.cloudflare.com/ips/">published Cloudflare IP range</a>, which is also available through the <a href="/api/resources/ips/methods/list/">Cloudflare API</a>.</p>
<p>When configuring an endpoint health check for an IP prefix, select an IP address within the range of that IP prefix. Refer to the table for an example of an endpoint health check configuration.</p>
<table>
<thead>
<tr>
<th>Prefix</th>
<th>Endpoint IP address</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>103.21.244.0/24</code></td>
<td><code>103.21.244.100</code></td>
</tr>
<tr>
<td><code>103.21.245.0/24</code></td>
<td><code>103.21.245.100</code></td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/magic-transit/reference/tunnel-health-checks/">Tunnel health checks</a> for more information.</p>
<h2 id="configure-endpoint-health-checks-beta">Configure endpoint health checks (beta)</h2>
<p>You can only configure endpoint health checks through the Cloudflare API. They are not available in the dashboard. Currently, configuring health checks is a beta feature.</p>
<p>Refer to the <a href="/api/resources/diagnostics/subresources/endpoint-healthchecks/">API documentation</a> to learn how to create, list, and delete endpoint health checks. The following example creates a new endpoint health check.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10638.md")
</aside>
<pre><code class="language-bash">curl --request POST --url https://api.cloudflare.com/client/v4/accounts/account_id/diagnostics/endpoint-healthchecks</code></pre>
<pre><code class="language-json">{&#10;    &quot;result&quot;: {&#10;        &quot;id&quot;: &quot;&lt;HEALTH_CHECK_ID&gt;&quot;,&#10;        &quot;check_type&quot;: &quot;icmp&quot;,&#10;        &quot;endpoint&quot;: &quot;8.31.160.1&quot;,&#10;        &quot;name&quot;: &quot;Datacenter 1 - primary&quot;&#10;    },&#10;    &quot;success&quot;: true,&#10;    &quot;errors&quot;: [],&#10;    &quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="query-endpoint-health-checks-with-graphql">Query endpoint health checks with GraphQL</h2>
<p>Use the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> to query endpoint health check results for your account. The <code>magicEndpointHealthCheckAdaptiveGroups</code> dataset returns probe results aggregated by the dimensions and time interval you specify.</p>
<p>Send all GraphQL queries as HTTP <code>POST</code> requests to <code>https://api.cloudflare.com/client/v4/graphql</code>.</p>
<h3 id="prerequisites">Prerequisites</h3>
<p>You need the following to query endpoint health check data:</p>
<ul>
<li>Your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a>.</li>
<li>An <a href="/fundamentals/api/get-started/create-token/">API token</a> with <code>Account &gt; Account Analytics &gt; Read</code> permissions. For details, refer to <a href="/analytics/graphql-api/getting-started/authentication/api-token-auth/">Configure an Analytics API token</a>.</li>
</ul>
<h3 id="query-parameters">Query parameters</h3>
<p>The following parameters are some of the most common ones in the <code>filter</code> object:</p>
<table>
<thead>
<tr>
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>date_geq</code></td>
<td align="left">Start date for the query in <code>YYYY-MM-DD</code> format (for example, <code>2026-01-01</code>). When used with a date-based truncation dimension, returns results from this date onward. You can also use a full ISO 8601 timestamp (for example, <code>2026-01-01T00:00:00Z</code>).</td>
</tr>
<tr>
<td align="left"><code>date_leq</code></td>
<td align="left"><em>(Optional)</em> End date for the query. Uses the same format as <code>date_geq</code>.</td>
</tr>
<tr>
<td align="left"><code>datetime_geq</code></td>
<td align="left"><em>(Optional)</em> Start timestamp in ISO 8601 format (for example, <code>2026-01-01T00:00:00Z</code>). Use instead of <code>date_geq</code> for time-based truncation dimensions.</td>
</tr>
<tr>
<td align="left"><code>datetime_leq</code></td>
<td align="left"><em>(Optional)</em> End timestamp in ISO 8601 format.</td>
</tr>
<tr>
<td align="left"><code>limit</code></td>
<td align="left">Maximum number of result groups to return.</td>
</tr>
</tbody>
</table>
<p>You can also filter on any dimension listed in the <a href="#available-dimensions">Available dimensions</a> table. Append an operator suffix to the dimension name to create a filter — for example, <code>endpoint_in</code> to filter by a list of endpoints, or <code>checkType_neq</code> to exclude a specific check type. Using a dimension name without a suffix filters for equality. For the full list of supported operators, refer to <a href="/analytics/graphql-api/features/filtering/">Filtering</a>.</p>
<h3 id="available-dimensions">Available dimensions</h3>
<p>You can query the following dimensions in the <code>dimensions</code> field:</p>
<table>
<thead>
<tr>
<th align="left">Dimension</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>checkId</code></td>
<td align="left">The unique ID of the configured health check.</td>
</tr>
<tr>
<td align="left"><code>checkType</code></td>
<td align="left">The type of health check (for example, <code>icmp</code>).</td>
</tr>
<tr>
<td align="left"><code>endpoint</code></td>
<td align="left">The IP address of the endpoint being checked.</td>
</tr>
<tr>
<td align="left"><code>name</code></td>
<td align="left">The name assigned to the health check when configured (may be empty if not set).</td>
</tr>
<tr>
<td align="left"><code>date</code></td>
<td align="left">Event timestamp truncated to the day.</td>
</tr>
<tr>
<td align="left"><code>datetime</code></td>
<td align="left">Full event timestamp.</td>
</tr>
<tr>
<td align="left"><code>datetimeMinute</code></td>
<td align="left">Event timestamp truncated to the minute.</td>
</tr>
<tr>
<td align="left"><code>datetimeFiveMinutes</code></td>
<td align="left">Event timestamp truncated to five-minute intervals.</td>
</tr>
<tr>
<td align="left"><code>datetimeFifteenMinutes</code></td>
<td align="left">Event timestamp truncated to 15-minute intervals.</td>
</tr>
<tr>
<td align="left"><code>datetimeHalfOfHour</code></td>
<td align="left">Event timestamp truncated to 30-minute intervals.</td>
</tr>
<tr>
<td align="left"><code>datetimeHour</code></td>
<td align="left">Event timestamp truncated to the hour.</td>
</tr>
</tbody>
</table>
<h3 id="available-metrics">Available metrics</h3>
<table>
<thead>
<tr>
<th align="left">Metric</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>count</code></td>
<td align="left">Total number of health check events in the group.</td>
</tr>
<tr>
<td align="left"><code>sum.total</code></td>
<td align="left">Total number of health check probes sent.</td>
</tr>
<tr>
<td align="left"><code>sum.failures</code></td>
<td align="left">Number of failed health check probes.</td>
</tr>
<tr>
<td align="left"><code>avg.lossPercentage</code></td>
<td align="left">Average calculated loss percentage (0-100).</td>
</tr>
</tbody>
</table>
<h3 id="api-call">API call</h3>
<p>The following example queries endpoint health check results for a specific account, returning probe counts aggregated in five-minute intervals. Replace <code>&lt;ACCOUNT_ID&gt;</code> with your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> and <code>&lt;API_TOKEN&gt;</code> with your <a href="/analytics/graphql-api/getting-started/authentication/api-token-auth/">API token</a>.</p>
<pre><code class="language-bash">echo &#x27;{ &quot;query&quot;:&#10;  &quot;query GetEndpointHealthCheckResults($accountTag: string, $datetimeStart: string) {&#10;    viewer {&#10;      accounts(filter: {accountTag: $accountTag}) {&#10;        magicEndpointHealthCheckAdaptiveGroups(&#10;          filter: {&#10;            datetime_geq: $datetimeStart&#10;          }&#10;          limit: 10&#10;        ) {&#10;          count&#10;          dimensions {&#10;            checkId&#10;            checkType&#10;            endpoint&#10;            datetimeFiveMinutes&#10;          }&#10;          sum {&#10;            failures&#10;            total&#10;          }&#10;        }&#10;      }&#10;    }&#10;  }&quot;,&#10;  &quot;variables&quot;: {&#10;    &quot;accountTag&quot;: &quot;&lt;ACCOUNT_ID&gt;&quot;,&#10;    &quot;datetimeStart&quot;: &quot;2026-01-21T00:00:00Z&quot;&#10;  }&#10;}&#x27; | tr -d &#x27;\n&#x27; | curl --silent \&#10;https://api.cloudflare.com/client/v4/graphql \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Accept: application/json&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data @-&#10;</code></pre>
<p>Pipe the output to <code>jq</code> to format the JSON response for easier reading:</p>
<pre><code class="language-bash">... | curl --silent \&#10;https://api.cloudflare.com/client/v4/graphql \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Accept: application/json&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data @- | jq .&#10;</code></pre>
<h3 id="example-response">Example response</h3>
<pre><code class="language-json">{&#10;  &quot;data&quot;: {&#10;    &quot;viewer&quot;: {&#10;      &quot;accounts&quot;: [&#10;        {&#10;          &quot;magicEndpointHealthCheckAdaptiveGroups&quot;: [&#10;            {&#10;              &quot;count&quot;: 288,&#10;              &quot;dimensions&quot;: {&#10;                &quot;checkId&quot;: &quot;90b478c7-bb51-4640-b94b-2c3050e9fa00&quot;,&#10;                &quot;checkType&quot;: &quot;icmp&quot;,&#10;                &quot;datetimeFiveMinutes&quot;: &quot;2026-01-21T12:00:00Z&quot;,&#10;                &quot;endpoint&quot;: &quot;103.21.244.100&quot;&#10;              },&#10;              &quot;sum&quot;: {&#10;                &quot;failures&quot;: 0,&#10;                &quot;total&quot;: 288&#10;              }&#10;            },&#10;            {&#10;              &quot;count&quot;: 288,&#10;              &quot;dimensions&quot;: {&#10;                &quot;checkId&quot;: &quot;90b478c7-bb51-4640-b94b-2c3050e9fa00&quot;,&#10;                &quot;checkType&quot;: &quot;icmp&quot;,&#10;                &quot;datetimeFiveMinutes&quot;: &quot;2026-01-21T12:05:00Z&quot;,&#10;                &quot;endpoint&quot;: &quot;103.21.244.100&quot;&#10;              },&#10;              &quot;sum&quot;: {&#10;                &quot;failures&quot;: 2,&#10;                &quot;total&quot;: 288&#10;              }&#10;            }&#10;          ]&#10;        }&#10;      ]&#10;    }&#10;  },&#10;  &quot;errors&quot;: null&#10;}&#10;</code></pre>
<p>In this response, <code>sum.total</code> is the number of probes sent during the interval and <code>sum.failures</code> is the number that did not receive a reply. A <code>failures</code> value of <code>0</code> indicates the endpoint was fully reachable during that period.</p>
<h2 id="configure-alerts-for-endpoint-health-checks">Configure alerts for endpoint health checks</h2>
<p>You can set up alerts to be notified when the state of your endpoint's health is below a threshold defined by you.</p>
<ol>
<li>Make a <code>GET</code> request to get a list of IDs for all of the endpoint health checks configured:</li>
</ol>
<pre><code class="language-bash">curl --request GET --url https://api.cloudflare.com/client/v4/accounts/account_id/diagnostics/endpoint-healthchecks</code></pre>
<pre><code class="language-json">{&#10;    &quot;result&quot;: [&#10;        {&#10;            &quot;id&quot;: &quot;&lt;HEALTH_CHECK_ID&gt;&quot;,&#10;            &quot;check_type&quot;: &quot;icmp&quot;,&#10;            &quot;endpoint&quot;: &quot;8.31.160.1&quot;,&#10;            &quot;name&quot;: &quot;Datacenter 1 - primary&quot;&#10;        }&#10;    ],&#10;    &quot;success&quot;: true,&#10;    &quot;errors&quot;: [],&#10;    &quot;messages&quot;: []&#10;}&#10;</code></pre>
<ol start="2">
<li>Take note of the <code>id</code> value for the endpoint you want to get alerts for.</li>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="4">
<li>Select <strong>Add</strong>.</li>
<li>From the drop-down menu, select <em>Magic Transit</em>.</li>
<li>Select <strong>Magic Endpoint Health Check Alert</strong>.</li>
<li>Provide a name for your new notification and optionally provide a description.</li>
<li>In the <em>Service Level Objective (SLO)</em> drop-down menu, select the SLO threshold for your notification. The SLO defines the percentage of endpoint health checks that must pass. If the number of passing endpoint health checks falls below the SLO, Cloudflare generates an alert:
<ul>
<li><strong>High</strong> - 99%</li>
<li><strong>Medium</strong> - 98%</li>
<li><strong>Low</strong> - 97%</li>
</ul>
</li>
<li>In the drop-down menu below SLOs, select the <code>id</code> value that matches the <code>id</code> you got through the API in step 1. This <code>id</code> should match the endpoint health check you want to get notifications for.</li>
<li>Select your preferred notification method (such as email or webhooks).</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>You will now receive notifications through your preferred method whenever the SLO for your endpoint health checks falls below your chosen threshold.</p>
