<div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/8171.md")
</div> expose analytics for Durable Object namespace-level and request-level metrics.
<p>The metrics displayed in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> charts are queried from Cloudflare's <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. You can access the metrics <a href="#query-via-the-graphql-api">programmatically via GraphQL</a> or HTTP client.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="durable-object-namespace">Durable Object namespace</h3>
@markup("md", "content/.markup/bodies/8170.md")
</aside>
<h2 id="view-metrics-and-analytics">View metrics and analytics</h2>
<p>Per-namespace analytics for Durable Objects are available in the Cloudflare dashboard. To view current and historical metrics for a namespace:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8172.md")
</div>
<p>You can optionally select a time window to query. This defaults to the last 24 hours.</p>
<p>You can also filter the charts to a single Durable Object by entering its <a href="/durable-objects/api/id/">ID</a> or <a href="/durable-objects/api/id/#name">name</a> and selecting a match. Clear the filter to return to namespace-level metrics.</p>
<h2 id="memory-usage">Memory usage</h2>
<p>The <strong>Memory usage</strong> chart on the <strong>Metrics</strong> tab shows V8 <a href="/workers/reference/how-workers-works/#isolates">isolate</a> memory usage, sampled periodically while your Durable Objects are active, broken down into P50, P90, P99, and P999 percentiles. Each isolate is subject to a <a href="/workers/platform/limits/#memory">128 MB memory limit</a>.</p>
<p>This memory holds the in-memory state your objects accumulate — such as class properties, caches, and active WebSocket connections — which persists across requests until an object is <a href="/durable-objects/concepts/durable-object-lifecycle/">hibernated or evicted</a>. This state is not preserved across eviction, hibernation, or a crash, so persist anything important to <a href="/durable-objects/best-practices/access-durable-objects-storage/">storage</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="memory-is-measured-per-isolate-not-per-durable-object">Memory is measured per isolate, not per Durable Object</h3>
@markup("md", "content/.markup/bodies/8169.md")
</aside>
<p>What the chart shows depends on whether you filter:</p>
<ul>
<li><strong>Without a filter (namespace view):</strong> the percentiles are computed across the periodic memory samples of every Durable Object in the namespace, showing the distribution of isolate memory across the namespace.</li>
<li><strong>Filtered by <a href="/durable-objects/api/id/">ID</a> or <a href="/durable-objects/api/id/#name">name</a>:</strong> the percentiles are computed only from the periodic samples reported for that one Durable Object. Each sample is still the memory of the entire isolate hosting it — which may include other Durable Objects sharing that isolate — so this is not a measurement of that single object's memory in isolation.</li>
</ul>
<p>Memory usage is powered by the <a href="#query-via-the-graphql-api"><code>durableObjectsPeriodicGroups</code></a> GraphQL dataset, which exposes the <code>memoryUsageBytes</code> metric. Percentile values are available as <code>quantiles.memoryUsageBytesP50</code> through <code>quantiles.memoryUsageBytesP999</code>, in bytes.</p>
<p>If you see memory usage trending upward over time, this may indicate a memory leak. Use <a href="/workers/observability/dev-tools/memory-usage/">memory profiling with DevTools</a> locally to take heap snapshots and identify specific objects causing high memory consumption.</p>
<h2 id="view-logs">View logs</h2>
<p>You can view Durable Object logs from the Cloudflare dashboard. Logs are aggregated by the script name and the Durable Object class name.</p>
<p>To start using Durable Object logging:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8174.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8168.md")
</aside>
<h2 id="query-via-the-graphql-api">Query via the GraphQL API</h2>
<p>Durable Object metrics are powered by GraphQL.</p>
<p>The datasets that include Durable Object metrics include:</p>
<ul>
<li><code>durableObjectsInvocationsAdaptiveGroups</code></li>
<li><code>durableObjectsPeriodicGroups</code></li>
<li><code>durableObjectsStorageGroups</code></li>
<li><code>durableObjectsSubrequestsAdaptiveGroups</code></li>
</ul>
<p>Use <a href="/analytics/graphql-api/features/discovery/introspection/">GraphQL Introspection</a> to get information on the fields exposed by each datasets.</p>
<h3 id="websocket-metrics">WebSocket metrics</h3>
<p>Durable Objects using <a href="/durable-objects/best-practices/websockets/">WebSockets</a> will see request metrics across several GraphQL datasets because WebSockets have different types of requests.</p>
<ul>
<li>Metrics for a WebSocket connection itself is represented in <code>durableObjectsInvocationsAdaptiveGroups</code> once the connection closes. Since WebSocket connections are long-lived, connections often do not terminate until the Durable Object terminates.</li>
<li>Metrics for incoming and outgoing WebSocket messages on a WebSocket connection are available in <code>durableObjectsPeriodicGroups</code>. If a WebSocket connection uses <a href="/durable-objects/best-practices/websockets/#durable-objects-hibernation-websocket-api">WebSocket Hibernation</a>, incoming WebSocket messages are instead represented in <code>durableObjectsInvocationsAdaptiveGroups</code>.</li>
</ul>
<h2 id="example-graphql-query-for-durable-objects">Example GraphQL query for Durable Objects</h2>
<pre><code class="language-js">  viewer {&#10;    /*&#10;    Replace with your account tag, the 32 hex character id visible at the beginning of any url&#10;    when logged in to dash.cloudflare.com or under &quot;Account ID&quot; on the sidebar of the Workers &amp; Pages Overview&#10;    &#42;/&#10;    accounts(filter: {accountTag: &quot;your account tag here&quot;}) {&#10;      // Replace dates with a recent date&#10;      durableObjectsInvocationsAdaptiveGroups(filter: {date_gt: &quot;2023-05-23&quot;}, limit: 1000) {&#10;        sum {&#10;          // Any other fields found through introspection can be added here&#10;          requests&#10;          responseBodySize&#10;        }&#10;      }&#10;      durableObjectsPeriodicGroups(filter: {date_gt: &quot;2023-05-23&quot;}, limit: 1000) {&#10;        sum {&#10;          cpuTime&#10;        }&#10;      }&#10;      durableObjectsStorageGroups(filter: {date_gt: &quot;2023-05-23&quot;}, limit: 1000) {&#10;        max {&#10;          storedBytes&#10;        }&#10;      }&#10;    }&#10;  }&#10;</code></pre>
<p>Refer to the <a href="/analytics/graphql-api/tutorials/querying-workers-metrics/">Querying Workers Metrics with GraphQL</a> tutorial for authentication and to learn more about querying Workers datasets.</p>
<h2 id="additional-resources">Additional resources</h2>
<ul>
<li>For instructions on setting up a Grafana dashboard to query Cloudflare's GraphQL Analytics API, refer to <a href="https://github.com/TimoWilhelm/grafana-do-dashboard">Grafana Dashboard starter for Durable Object metrics</a>.</li>
</ul>
<h2 id="faqs">FAQs</h2>
<h3 id="how-can-i-identify-which-durable-object-instance-generated-a-log-entry">How can I identify which Durable Object instance generated a log entry?</h3>
<p>Durable Object request logs include the instance ID in <code>$workers.durableObjectId</code>. Filter on this field to isolate a specific instance for debugging.</p>
