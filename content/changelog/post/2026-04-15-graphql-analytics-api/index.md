<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 15, 2026</time><h2 id="post-title">Privacy Proxy metrics now available via GraphQL Analytics API</h2>
<div class="changelog-badges"><span>privacy-proxy</span></div><div class="changelog-body"><p>Privacy Proxy metrics are now queryable through Cloudflare's <a href="/privacy-proxy/reference/metrics/graphql/">GraphQL Analytics API</a>, the new default method for accessing Privacy Proxy observability data. All metrics are available through a single endpoint:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/graphql \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;query&quot;: &quot;{ viewer { accounts(filter: { accountTag: $accountTag }) { privacyProxyRequestMetricsAdaptiveGroups(filter: { date_geq: $startDate, date_leq: $endDate }, limit: 10000, orderBy: [date_ASC]) { count dimensions { date } } } } }&quot;,&#10;    &quot;variables&quot;: {&#10;      &quot;accountTag&quot;: &quot;&lt;YOUR_ACCOUNT_TAG&gt;&quot;,&#10;      &quot;startDate&quot;: &quot;2026-04-04&quot;,&#10;      &quot;endDate&quot;: &quot;2026-04-06&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h4 id="available-nodes">Available nodes</h4>
<p>Four GraphQL nodes are now live, providing aggregate metrics across all key dimensions of your Privacy Proxy deployment:</p>
<ul>
<li><strong><code>privacyProxyRequestMetricsAdaptiveGroups</code></strong> — Request volume, error rates, status codes, and proxy status breakdowns.</li>
<li><strong><code>privacyProxyIngressConnMetricsAdaptiveGroups</code></strong> — Client-to-proxy connection counts, bytes transferred, and latency percentiles.</li>
<li><strong><code>privacyProxyEgressConnMetricsAdaptiveGroups</code></strong> — Proxy-to-origin connection counts, bytes transferred, and latency percentiles.</li>
<li><strong><code>privacyProxyAuthMetricsAdaptiveGroups</code></strong> — Authentication attempt counts by method and result.</li>
</ul>
<p>All nodes support filtering by time, data center (<code>coloCode</code>), and endpoint, with additional node-specific dimensions such as transport protocol and authentication method.</p>
<h4 id="what-this-means-for-existing-opentelemetry-users">What this means for existing OpenTelemetry users</h4>
<p>OpenTelemetry-based metrics export remains available. The GraphQL Analytics API is now the recommended default method — a plug-and-play method that requires no collector infrastructure, saving engineering overhead.</p>
<h4 id="learn-more">Learn more</h4>
<ul>
<li><a href="/privacy-proxy/reference/metrics/graphql/">GraphQL Analytics API for Privacy Proxy</a></li>
<li><a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API — getting started</a></li>
</ul>
</div></article></div>
