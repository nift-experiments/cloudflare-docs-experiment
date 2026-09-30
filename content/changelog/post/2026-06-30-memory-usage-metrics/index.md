<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 30, 2026</time><h2 id="post-title">Track memory usage for Workers and Durable Objects in the dashboard</h2>
<div class="changelog-badges"><span>workers</span><span>durable-objects</span></div><div class="changelog-body"><p>You can now monitor how much memory your <a href="/workers/">Workers</a> and <a href="/durable-objects/">Durable Objects</a> consume across invocations with the new <strong>Memory Usage</strong> chart in the Workers Metrics tab, broken down by P50, P90, P99, and P999 percentiles.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-06-26-memory-usage.png" alt="Memory usage chart showing P50, P90, P99, and P999 percentiles with deployment markers" /></p>
<p>Memory usage measures the V8 <a href="/workers/reference/how-workers-works/#isolates">isolate</a> memory at the time of each invocation, subject to the <a href="/workers/platform/limits/#memory">128 MB per-isolate limit</a> — a single isolate can handle many concurrent requests and shares memory across them.</p>
<p>Use the Memory Usage chart to:</p>
<ul>
<li><strong>Track memory trends</strong> — Spot gradual increases that may indicate a memory leak before they cause <code>Exceeded Memory</code> errors.</li>
<li><strong>Correlate with deployments</strong> — Deployment markers on the chart help you identify whether a new version introduced a memory regression.</li>
<li><strong>Right-size your Worker</strong> — Understand your baseline memory footprint and how much headroom you have before hitting the 128 MB limit.</li>
</ul>
<p>For Durable Objects, memory usage reflects the in-memory state an object holds (class properties, caches, active WebSocket connections), which persists across invocations until the object is <a href="/durable-objects/concepts/durable-object-lifecycle/">hibernated or evicted</a>. This state is not preserved across eviction, hibernation, or a crash, so persist anything important to <a href="/durable-objects/best-practices/access-durable-objects-storage/">storage</a>.</p>
<p>To view memory usage, open the <strong>Metrics</strong> tab for your <a href="https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/metrics">Worker</a> or <a href="https://dash.cloudflare.com/?to=/:account/workers/durable-objects">Durable Object namespace</a>. For Durable Objects, you can filter by DO ID or name to drill down into memory usage for a specific object. You can also query memory usage programmatically via the <a href="/analytics/graphql-api/tutorials/querying-workers-metrics/">GraphQL Analytics API</a> using the <code>workersInvocationsAdaptive</code> dataset — the <code>quantiles.memoryUsageBytesP50</code> through <code>quantiles.memoryUsageBytesP999</code> fields return percentile values in bytes.</p>
<p>For local memory debugging, you can also <a href="/workers/observability/dev-tools/memory-usage/">profile memory with DevTools</a> to take heap snapshots and identify specific objects causing high memory usage.</p>
</div></article></div>
