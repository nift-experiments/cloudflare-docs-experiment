<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 15, 2026</time><h2 id="post-title">Hyperdrive exposes database connection pool size metrics</h2>
<div class="changelog-badges"><span>hyperdrive</span><span>workers</span></div><div class="changelog-body"><p>You can now view the size of your Hyperdrive database connection pools, giving you the ability to self-diagnose connection issues. Using the Cloudflare dashboard or the <code>hyperdrivePoolSizesAdaptiveGroups</code> dataset in the <a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API</a>, you can see <code>waitingClients</code>, <code>currentPoolSize</code>, <code>availablePoolSlots</code>, and <code>maxPoolSize</code> for each of your configurations.</p>
<p>A new <strong>Pool connections</strong> chart has been added to the <strong>Metrics</strong> tab of each Hyperdrive configuration in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>. You can use the location selector to drill down into specific locations hosting your connection pool by airport code.</p>
<p><img src="/assets/upstream/images/hyperdrive/changelog/hyperdrive-pool-size-metrics-chart.png" alt="Hyperdrive pool size metrics chart" /></p>
<p>The chart shows:</p>
<ul>
<li><strong>Waiting clients</strong>: Client requests waiting for an available connection.</li>
<li><strong>Open connections</strong>: Active connections to your database.</li>
<li><strong>Pool size maximum</strong>: Your configured origin connection limit.</li>
</ul>
<p>Connection contention appears as a spike in waiting clients, or when open connections consistently approach the pool size maximum. If your open connections regularly approach this limit, consider contacting Cloudflare to <a href="/hyperdrive/platform/limits/#request-a-limit-increase">increase your Hyperdrive connection limit</a>.</p>
<h4 id="pool-size-metrics">Pool size metrics</h4>
<p>The <code>hyperdrivePoolSizesAdaptiveGroups</code> dataset in the <a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API</a> exposes the following key connection pool metrics for each Hyperdrive configuration:</p>
<p>Under <code>avg</code>:</p>
<ul>
<li><strong><code>currentPoolSize</code></strong> — Average number of connections currently open in the pool.</li>
<li><strong><code>availablePoolSlots</code></strong> — Average number of pool connections available for checkout.</li>
<li><strong><code>waitingClients</code></strong> — Average number of clients waiting for a connection from the pool.</li>
</ul>
<p>Under <code>max</code>:</p>
<ul>
<li><strong><code>maxPoolSize</code></strong> — Configured maximum size of the connection pool.</li>
<li><strong><code>currentPoolSize</code></strong> — Peak number of connections open in the pool.</li>
<li><strong><code>waitingClients</code></strong> — Peak number of clients waiting for a connection from the pool.</li>
</ul>
<p>For more information, refer to <a href="/hyperdrive/observability/metrics/">Metrics and analytics</a> and <a href="/hyperdrive/concepts/connection-pooling/">Connection pooling</a>.</p>
</div></article></div>
