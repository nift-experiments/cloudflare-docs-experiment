<p>Privacy Proxy exposes metrics through Cloudflare's <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. All metrics are queryable through a single endpoint:</p>
<pre><code class="language-txt">POST https://api.cloudflare.com/client/v4/graphql&#10;</code></pre>
<p>Before you begin, you will need:</p>
<ul>
<li><strong>API token</strong> — Create a token with <em>Account Analytics</em> read permissions. For more information, refer to our Analytics API token documentation: <a href="/analytics/graphql-api/getting-started/authentication/api-token-auth/">Configure an Analytics API token</a>.</li>
<li><strong>Account ID</strong> — Your Cloudflare account ID, passed as <code>accountTag</code> in queries. For more information, refer to <a href="/fundamentals/account/find-account-and-zone-ids/">Find account and zone IDs</a>.</li>
</ul>
<hr />
<h2 id="making-a-request">Making a request</h2>
<p>The following example shows how to query your Privacy Proxy metrics daily request volume using curl. Replace the placeholder values with your own.</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/graphql \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;query&quot;: &quot;query DailyRequestVolume($accountTag: String!, $startDate: Date!, $endDate: Date!) { viewer { accounts(filter: { accountTag: $accountTag }) { privacyProxyRequestMetricsAdaptiveGroups(filter: { date_geq: $startDate, date_leq: $endDate }, limit: 10000, orderBy: [date_ASC]) { count dimensions { date } } } } }&quot;,&#10;    &quot;variables&quot;: {&#10;      &quot;accountTag&quot;: &quot;&lt;YOUR_ACCOUNT_TAG&gt;&quot;,&#10;      &quot;startDate&quot;: &quot;2026-04-04&quot;,&#10;      &quot;endDate&quot;: &quot;2026-04-06&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<hr />
<h2 id="available-nodes">Available nodes</h2>
<p>Four GraphQL nodes are available. All four return aggregate data only — no raw per-connection records are exposed.</p>
<ol>
<li><code>privacyProxyRequestMetricsAdaptiveGroups</code> — Query aggregate request volume and error rates, filterable by time, location, endpoint, status code, and proxy status dimensions.</li>
<li><code>privacyProxyIngressConnMetricsAdaptiveGroups</code> — Query client-to-proxy connection counts, bytes transferred, and latency percentiles, filterable by time, location, endpoint, and transport dimensions.</li>
<li><code>privacyProxyEgressConnMetricsAdaptiveGroups</code> — Query proxy-to-origin connection counts, bytes transferred, and latency percentiles, filterable by time, location, endpoint, and transport dimensions.</li>
<li><code>privacyProxyAuthMetricsAdaptiveGroups</code> — Query authentication attempt counts, filterable by time, location, endpoint, auth method, and auth result dimensions.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="adaptive-sampling">Adaptive sampling</h3>
@markup("md", "content/.markup/bodies/11117.md")
</aside>
<hr />
<h2 id="schema">Schema</h2>
<details class="nb-details"><summary>Metrics</summary><div class="nb-details-body">
@input("content/.markup/bodies/11121.md")
</div></details>
<details class="nb-details"><summary>Dimensions</summary><div class="nb-details-body">
@input("content/.markup/bodies/11127.md")
</div></details>
<details class="nb-details"><summary>Arguments</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11128.md")
</div></details>
<hr />
<h2 id="sample-queries">Sample queries</h2>
<details class="nb-details"><summary>privacyProxyRequestMetricsAdaptiveGroups node</summary><div class="nb-details-body">
@input("content/.markup/bodies/11133.md")
</div></details>
<details class="nb-details"><summary>privacyProxyIngressConnMetricsAdaptiveGroups node</summary><div class="nb-details-body">
@input("content/.markup/bodies/11137.md")
</div></details>
<details class="nb-details"><summary>privacyProxyEgressConnMetricsAdaptiveGroups node</summary><div class="nb-details-body">
@input("content/.markup/bodies/11141.md")
</div></details>
<details class="nb-details"><summary>privacyProxyAuthMetricsAdaptiveGroups node</summary><div class="nb-details-body">
@input("content/.markup/bodies/11145.md")
</div></details>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API — getting started</a></li>
<li><a href="/analytics/graphql-api/features/filtering/">GraphQL Analytics API — filtering</a></li>
<li><a href="/privacy-proxy/reference/proxy-status/">Proxy status reference</a> — All possible <code>proxyStatus</code> values and their meanings.</li>
</ul>
