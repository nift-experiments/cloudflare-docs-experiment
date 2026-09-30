<h1 id="changelog">Changelog</h1>

<h2 id="track-memory-usage-for-workers-and-durable-objects-in-the-dashboard"><a href="/changelog/post/2026-06-30-memory-usage-metrics/">Track memory usage for Workers and Durable Objects in the dashboard</a></h2>
<p><em>2026-06-30</em></p>
<p>You can now monitor how much memory your <a href="/workers/">Workers</a> and <a href="/durable-objects/">Durable Objects</a> consume across invocations with the new <strong>Memory Usage</strong> chart in the Workers Metrics tab, broken down by P50, P90, P99, and P999 percentiles.</p>
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


<h2 id="new-us-jurisdiction-for-durable-objects"><a href="/changelog/post/2026-06-26-durable-objects-us-jurisdiction/">New `us` jurisdiction for Durable Objects</a></h2>
<p><em>2026-06-26</em></p>
<p>Durable Objects now supports a <code>us</code> <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">jurisdiction</a>, letting you create Durable Objects that only run and store data within the United States. Use the <code>us</code> jurisdiction when you need to keep a Durable Object's compute and storage inside the United States to meet data residency requirements.</p>
<p>Create a namespace restricted to the <code>us</code> jurisdiction the same way as any other jurisdiction:</p>
<pre><code class="language-js">// Worker&#10;export default {&#10;	async fetch(request, env) {&#10;		const usSubnamespace = env.MY_DURABLE_OBJECT.jurisdiction(&quot;us&quot;);&#10;		const stub = usSubnamespace.getByName(&quot;general&quot;);&#10;		return stub.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p>Workers may still access Durable Objects constrained to the <code>us</code> jurisdiction from anywhere in the world. The jurisdiction constraint only controls where the Durable Object itself runs and persists data.</p>
<p>For the full list of supported jurisdictions, refer to <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">Data location — Restrict Durable Objects to a jurisdiction</a>.</p>


<h2 id="test-durable-object-eviction-with-new-cloudflare-test-helpers"><a href="/changelog/post/2026-06-25-durable-object-eviction-test-helpers/">Test Durable Object eviction with new cloudflare:test helpers</a></h2>
<p><em>2026-06-25</em></p>
<p>The <code>@cloudflare/vitest-pool-workers</code> package now includes <code>evictDurableObject</code> and <code>evictAllDurableObjects</code> test helpers, exported from <code>cloudflare:test</code>.</p>
<p>These helpers let you test how a Durable Object behaves across evictions, simulating the production lifecycle where an idle Durable Object can be evicted from memory.</p>
<p>For more context, refer to <a href="/durable-objects/concepts/durable-object-lifecycle/">Lifecycle of a Durable Object</a>.</p>
<pre><code class="language-ts">import { evictDurableObject, evictAllDurableObjects } from &quot;cloudflare:test&quot;;&#10;import { env } from &quot;cloudflare:workers&quot;;&#10;&#10;const id = env.COUNTER.idFromName(&quot;my-counter&quot;);&#10;const stub = env.COUNTER.get(id);&#10;&#10;// Evict the Durable Object instance pointed to by a specific stub&#10;await evictDurableObject(stub);&#10;&#10;// Close WebSockets instead of hibernating them&#10;await evictDurableObject(stub, { webSockets: &quot;close&quot; });&#10;&#10;// Evict all currently-running Durable Objects in evictable namespaces&#10;await evictAllDurableObjects();&#10;</code></pre>
<p>These helpers are available in <code>@cloudflare/vitest-pool-workers@0.16.20</code> and later.</p>
<p>Learn more in the <a href="/workers/testing/vitest-integration/test-apis/#durable-objects">Test APIs reference</a> and the <a href="/durable-objects/examples/testing-with-durable-objects/#testing-eviction">Testing Durable Objects guide</a>.</p>


<h2 id="regionalized-ip-bindings-for-regional-services"><a href="/changelog/post/2026-06-23-regionalized-ip-bindings/">Regionalized IP Bindings for Regional Services</a></h2>
<p><em>2026-06-23</em></p>
<p>Regional Services now supports <strong>Regionalized IP Bindings</strong>, letting you regionalize traffic at the IP layer for prefixes you bring to Cloudflare through <a href="/byoip/">Bring Your Own IP (BYOIP)</a>.</p>
<p>Where <a href="/data-localization/regional-services/regional-hostnames/">Regional Hostnames</a> regionalize traffic by hostname, Regionalized IP Bindings let you bind a CIDR from one of your prefixes to a region — ideal for address-map deployments and any service you address by IP rather than hostname. Cloudflare then terminates TLS and processes traffic to those addresses only within the data centers in that region.</p>
<p>Regionalized IP Bindings requires the Regional Services and Regional Services for BYOIP entitlements. Contact your account team to enable them.</p>
<p>To get started, refer to <a href="/data-localization/regional-services/ip-bindings/">Regionalized IP Bindings</a>.</p>


<h2 id="new-asia-pacific-location-hints-apac-ne-and-apac-se"><a href="/changelog/post/2026-06-19-apac-ne-apac-se-location-hints/">New Asia-Pacific location hints: apac-ne and apac-se</a></h2>
<p><em>2026-06-19</em></p>
<p>Durable Objects now supports two new location hints for Asia-Pacific: <code>apac-ne</code> (Northeast Asia-Pacific) and <code>apac-se</code> (Southeast Asia-Pacific). Use <code>apac-ne</code> or <code>apac-se</code> when you want finer-grained placement within Asia-Pacific rather than the broader <code>apac</code> hint.</p>
<p>Use the new hints the same way as any other <code>locationHint</code>:</p>
<pre><code class="language-js">// Northeast Asia-Pacific (Japan, Korea, etc.)&#10;const stubNE = env.MY_DURABLE_OBJECT.get(id, { locationHint: &quot;apac-ne&quot; });&#10;&#10;// Southeast Asia-Pacific (Singapore, Indonesia, etc.)&#10;const stubSE = env.MY_DURABLE_OBJECT.get(id, { locationHint: &quot;apac-se&quot; });&#10;</code></pre>
<p>If your users are spread across all of Asia-Pacific, the existing <code>apac</code> hint remains the right choice. Only reach for <code>apac-ne</code> or <code>apac-se</code> when your traffic is clearly concentrated in one sub-region and you want to minimize round-trip time to that audience. The default behavior and what we generally recommended is not adding a location hint unless absolutely needed, this will create the Durable Object as close to the initializing request as possible to reduce latency.</p>
<p>As with all location hints, these are best-effort suggestions. Cloudflare will place the Durable Object in a nearby data center, not necessarily the exact hinted location.</p>
<p>For the full list of supported hints, refer to <a href="/durable-objects/reference/data-location/#provide-a-location-hint">Data location — Provide a location hint</a>.</p>


<h2 id="outbound-connections-keep-durable-objects-alive"><a href="/changelog/post/2026-06-19-outbound-connections-keep-dos-alive/">Outbound connections keep Durable Objects alive</a></h2>
<p><em>2026-06-19</em></p>
<p>Durable Objects now remain alive for the duration of active outbound connections created via <a href="/workers/runtime-apis/tcp-sockets/"><code>connect()</code></a> or an outbound WebSocket. Previously, a Durable Object would be evicted after 70-140 seconds of no incoming traffic, even if the object had an open outbound connection, which is a common pattern when streaming responses from a large language model (LLM) over TCP or an outbound WebSocket.</p>
<p>With this change, each active outbound connection prevents eviction. Once all outbound connections close, the standard 70-140 second inactivity window applies before the Durable Object is evicted.</p>
<h4 id="2026-06-19-outbound-connections-keep-dos-alive-before-streaming-connections-were-cut-off-by-eviction">Before: streaming connections were cut off by eviction</h4>
<p><img src="/assets/upstream/images/durable-objects/outbound-connection-before.svg" alt="Timeline showing a Durable Object evicted 70-140 seconds after the last incoming request, cutting off an in-flight LLM stream while the outbound connection is still open" /></p>
<h4 id="2026-06-19-outbound-connections-keep-dos-alive-after-active-outbound-connections-keep-the-durable-object-alive">After: active outbound connections keep the Durable Object alive</h4>
<p><img src="/assets/upstream/images/durable-objects/outbound-connection-after.svg" alt="Timeline showing the same outbound stream completing because the active connection keeps the Durable Object alive, with the inactivity window starting only after the connection closes" /></p>
<p>If you are <a href="/agents/">building agents on Cloudflare</a>, this is especially relevant. An agent that streams tokens from an LLM while <a href="/agents/concepts/calling-llms/">calling models</a>, or that performs <a href="/agents/concepts/agentic-patterns/long-running-agents/">long-running tasks</a> over an outbound connection, now stays alive for the duration of that connection instead of being evicted mid-stream.</p>
<p><strong>Limits:</strong></p>
<ul>
<li>Each outbound connection keeps the Durable Object alive for a maximum of <strong>15 minutes</strong>. After 15 minutes, the connection stops preventing eviction (the connection itself continues operating), and the <a href="/durable-objects/concepts/durable-object-lifecycle/">standard eviction rules</a> resume.</li>
<li>The Durable Object's existing <a href="/durable-objects/platform/limits/">per-account instance limits</a> still apply.</li>
</ul>
<p>For more information, refer to <a href="/durable-objects/concepts/durable-object-lifecycle/">Lifecycle of a Durable Object</a>.</p>


<h2 id="create-planetscale-postgres-and-mysql-databases-billed-to-your-cloudflare-account"><a href="/changelog/post/2026-06-18-planetscale-databases-cloudflare-billing/">Create PlanetScale Postgres and MySQL databases, billed to your Cloudflare account</a></h2>
<p><em>2026-06-18</em></p>
<p>You can create PlanetScale Postgres and MySQL databases from Cloudflare and bill PlanetScale database usage through your Cloudflare account as a pay-as-you-go customer. Cloudflare contract customers will be able to add PlanetScale usage to their contract in July so reach out to your Cloudflare account team if interested.</p>
<p>Create a PlanetScale database from the Cloudflare dashboard to check out globally distributed Workers optimized for regional data access.</p>
<div class="nb-dash-button"></div>
<p><img src="/assets/upstream/images/hyperdrive/planetscale-request-flow.svg" alt="Request flow from a user to Workers, Hyperdrive caches, connection pools, and PlanetScale." /></p>
<p>PlanetScale databases created from Cloudflare work with <a href="/workers/">Workers</a> through <a href="/hyperdrive/">Hyperdrive</a>. Hyperdrive manages database connection pools and query caching, so you can use PlanetScale as a centralized relational database for Workers applications without changing your database drivers, object-relational mapping (ORM) libraries, or SQL tooling.</p>
<p>PlanetScale usage appears on your Cloudflare invoice each billing period as a dollar total at PlanetScale's standard <a href="https://planetscale.com/pricing">pricing</a>. You can introspect per-database billing usage via PlanetScale's <a href="https://planetscale.com/docs/billing#organization-usage-and-billing-page">dashboard</a>.</p>
<p>When you create a PlanetScale database from the Cloudflare dashboard, you receive the same PlanetScale developer experience, including development branches, query insights, and Model Context Protocol (MCP) server support for agents.</p>
<p>To get started, refer to <a href="/hyperdrive/planetscale/">PlanetScale Postgres and MySQL with Hyperdrive</a>.</p>


<h2 id="filter-durable-objects-metrics-by-object-id-or-name"><a href="/changelog/post/2026-06-12-durable-objects-metrics-filter-by-id-name/">Filter Durable Objects metrics by object ID or name</a></h2>
<p><em>2026-06-12</em></p>
<p>You can now filter the <strong>Metrics</strong> tab for a Durable Objects namespace by an individual Durable Object's <a href="/durable-objects/api/id/">ID</a> or <a href="/durable-objects/api/id/#name">name</a> in the Cloudflare dashboard. Previously, metrics charts only showed aggregate, namespace-level data, making it difficult to isolate the behavior of a specific object.</p>
<div class="nb-dash-button"></div>
<p><img src="/assets/upstream/images/changelog/durable-objects/durable-objects-metrics-dashboard.png" alt="The Durable Objects Metrics tab filtered to a single object by ID, showing per-object requests and errors by invocation status." /></p>
<p>Start typing an ID or name into the filter and select a match from the autocomplete dropdown. The autocomplete only shows objects with invocations during the selected time range, so an object that does not appear has not been invoked in that window. This does not necessarily mean the object has been deleted. Every chart on the page updates to reflect only the selected object. This makes it easier to identify and investigate a single Durable Object when debugging a high-traffic object, an error spike, or unexpected storage usage. Clear the filter to return to namespace-level metrics.</p>
<p>Metrics are powered by the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>, so standard analytics behavior such as ingestion delay and <a href="/analytics/faq/graphql-api-inconsistent-results/">sampling</a> applies.</p>
<p>For more information, refer to <a href="/durable-objects/observability/metrics-and-analytics/">Metrics and analytics</a>.</p>


<h2 id="billable-usage-and-budget-alerts-now-in-product-sidebars"><a href="/changelog/post/2026-06-04-billable-usage-product-sidebar/">Billable usage and budget alerts now in product sidebars</a></h2>
<p><em>2026-06-04</em></p>
<p>Pay-as-you-go customers can now view billable usage and create <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">budget alerts</a> directly from the product overview pages for <a href="/workers/">Workers &amp; Pages</a>, <a href="/d1/">D1</a>, <a href="/r2/">R2</a>, <a href="/kv/">Workers KV</a>, <a href="/queues/">Queues</a>, <a href="/vectorize/">Vectorize</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/containers/">Containers</a>. A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.</p>
<p>The widget pulls from the same data as the <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Billable Usage dashboard</a> and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-06-04-billable-usage-product-sidebar.png" alt="Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service" /></p>
<p>Selecting <strong>Create budget alert</strong> opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.</p>
<p>For more information, refer to the <a href="/billing/">Usage-based billing documentation</a>.</p>


<h2 id="d1-migrations-support-nested-layouts-via-migrations-pattern"><a href="/changelog/post/2026-06-04-migrations-pattern/">D1 migrations support nested layouts via `migrations_pattern`</a></h2>
<p><em>2026-05-29</em></p>
<p>You can now point <code>wrangler d1 migrations apply</code> at a nested migrations layout — such as the one produced by <a href="https://orm.drizzle.team/">Drizzle</a> (<code>migrations/0001_init/migration.sql</code>) — using the new <code>migrations_pattern</code> D1 binding config:</p>
<pre><code class="language-jsonc">{&#10;	&quot;d1_databases&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;DB&quot;,&#10;			&quot;database_name&quot;: &quot;my-database&quot;,&#10;			&quot;database_id&quot;: &quot;&lt;UUID&gt;&quot;,&#10;			&quot;migrations_dir&quot;: &quot;migrations&quot;,&#10;			&quot;migrations_pattern&quot;: &quot;migrations/*/migration.sql&quot;,&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p><code>migrations_pattern</code> is a glob (relative to your Wrangler config file) used to discover migration files. It defaults to <code>${migrations_dir}/*.sql</code>, so existing projects keep working unchanged. Each migration's name is recorded in the migrations table as a path relative to <code>migrations_dir</code>.</p>
<p>To learn more, visit D1's <a href="/d1/reference/migrations/#nested-migration-layouts">migrations documentation</a>.</p>


<h2 id="r2-data-catalog-pricing-announced"><a href="/changelog/post/2026-05-11-r2-data-catalog-pricing-announced/">R2 Data Catalog pricing announced</a></h2>
<p><em>2026-05-28</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a> is a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> data catalog built directly into R2 buckets, queryable by any Iceberg-compatible engine such as Spark, Snowflake, and DuckDB. R2 Data Catalog now has published pricing for catalog operations and table compaction, in addition to standard <a href="/r2/pricing/">R2 storage and operations</a>.</p>
<p>Billing is not yet enabled. We will provide at least 30 days notice before we start charging for R2 Data Catalog usage.</p>
<p>Pricing is based on two dimensions:</p>
<ul>
<li><strong>Catalog operations</strong>: $9.00 / million operations for metadata requests such as creating tables, reading table metadata, and updating table properties.</li>
<li><strong>Compaction</strong>: $0.005 / GB processed and $2.00 / million objects processed. These charges only apply when automatic compaction is turned on for a table.</li>
</ul>
<p>Both dimensions include a monthly free tier: 1 million catalog operations, 10 GB of compaction data processed, and 1 million compaction objects processed.</p>
<p>For full pricing details and billing examples, refer to <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog pricing</a>.</p>


<h2 id="r2-data-catalog-gets-a-dedicated-dashboard-experience"><a href="/changelog/post/2026-05-28-r2-data-catalog-dashboard/">R2 Data Catalog gets a dedicated dashboard experience</a></h2>
<p><em>2026-05-28</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a> is a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> data catalog built directly into your R2 bucket. It exposes a standard Iceberg REST catalog interface so you can connect query engines like <a href="/r2-data-catalog/config-examples/spark-scala/">Spark</a>, <a href="/r2-data-catalog/config-examples/snowflake/">Snowflake</a>, <a href="/r2-data-catalog/config-examples/duckdb/">DuckDB</a>, and <a href="/r2-sql/">R2 SQL</a> to your data in R2.</p>
<p>R2 Data Catalog now has a dedicated section in the Cloudflare dashboard, replacing the previous settings panel embedded in R2 bucket configuration. The new experience includes:</p>
<p><img src="/assets/upstream/images/r2-data-catalog/data-catalog-dashboard.png" alt="R2 Data Catalog dashboard overview" /></p>
<ul>
<li><strong>Catalog overview</strong> — View all your catalogs in one place with catalog request counts, bucket sizes, and table maintenance status at a glance.</li>
<li><strong>Guided setup wizard</strong> — Create a catalog in three steps: choose or create an R2 bucket, configure table maintenance (compaction and snapshot expiration), and review. The wizard creates the bucket and generates a service credential automatically.</li>
<li><strong>Settings management</strong> — A dedicated settings page for each catalog with sections for general configuration, table maintenance, service credentials, and disabling the catalog. You can now enable and configure <a href="/r2-data-catalog/table-maintenance/">snapshot expiration</a> directly from the dashboard.</li>
<li><strong>Built-in metrics</strong> — Five charts on each catalog's metrics tab: bytes compacted, files compacted, catalog requests, storage size, and snapshots expired.</li>
</ul>
<p>To get started, go to <strong>R2 Data Catalog</strong> in the Cloudflare dashboard or refer to the <a href="/r2-data-catalog/get-started/">getting started guide</a> and <a href="/r2-data-catalog/manage-catalogs/">manage catalogs documentation</a>.</p>


<h2 id="event-subscriptions-for-artifacts-lifecycle-events"><a href="/changelog/post/2026-05-19-event-subscriptions/">Event subscriptions for Artifacts lifecycle events</a></h2>
<p><em>2026-05-19</em></p>
<p>You can now receive <a href="/queues/event-subscriptions/">event notifications</a> for <a href="/artifacts/">Artifacts</a> repository changes and consume them from a Worker to build commit-driven automation.</p>
<p>This allows you to:</p>
<ul>
<li>Run custom workflows when a repository is created or imported</li>
<li>Kick off a build and deploy a change when an agent pushes to a repo</li>
<li>Trigger a review agent on every push</li>
</ul>
<p>Available events include:</p>
<ul>
<li><strong>Account-level events</strong> (<code>artifacts</code> source) — <code>repo.created</code>, <code>repo.deleted</code>, <code>repo.forked</code>, <code>repo.imported</code></li>
<li><strong>Repository-level events</strong> (<code>artifacts.repo</code> source) — <code>pushed</code>, <code>cloned</code>, <code>fetched</code></li>
</ul>
<p>To learn more, refer to <a href="/artifacts/guides/event-subscriptions/">Artifacts documentation</a>.</p>


<h2 id="hyperdrive-exposes-database-connection-pool-size-metrics"><a href="/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/">Hyperdrive exposes database connection pool size metrics</a></h2>
<p><em>2026-05-15</em></p>
<p>You can now view the size of your Hyperdrive database connection pools, giving you the ability to self-diagnose connection issues. Using the Cloudflare dashboard or the <code>hyperdrivePoolSizesAdaptiveGroups</code> dataset in the <a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API</a>, you can see <code>waitingClients</code>, <code>currentPoolSize</code>, <code>availablePoolSlots</code>, and <code>maxPoolSize</code> for each of your configurations.</p>
<p>A new <strong>Pool connections</strong> chart has been added to the <strong>Metrics</strong> tab of each Hyperdrive configuration in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>. You can use the location selector to drill down into specific locations hosting your connection pool by airport code.</p>
<p><img src="/assets/upstream/images/hyperdrive/changelog/hyperdrive-pool-size-metrics-chart.png" alt="Hyperdrive pool size metrics chart" /></p>
<p>The chart shows:</p>
<ul>
<li><strong>Waiting clients</strong>: Client requests waiting for an available connection.</li>
<li><strong>Open connections</strong>: Active connections to your database.</li>
<li><strong>Pool size maximum</strong>: Your configured origin connection limit.</li>
</ul>
<p>Connection contention appears as a spike in waiting clients, or when open connections consistently approach the pool size maximum. If your open connections regularly approach this limit, consider contacting Cloudflare to <a href="/hyperdrive/platform/limits/#request-a-limit-increase">increase your Hyperdrive connection limit</a>.</p>
<h4 id="2026-05-15-hyperdrive-pool-size-metrics-pool-size-metrics">Pool size metrics</h4>
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


<h2 id="r2-data-catalog-now-exposes-metrics-via-the-graphql-analytics-api"><a href="/changelog/post/2026-05-12-r2-data-catalog-graphql-analytics/">R2 Data Catalog now exposes metrics via the GraphQL Analytics API</a></h2>
<p><em>2026-05-12</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a> is a managed Apache Iceberg data catalog built directly into your R2 bucket that allows you to connect query engines like <a href="/r2-sql/">R2 SQL</a>, Spark, Snowflake, and DuckDB to your data in R2.</p>
<p>You can now query analytics for your R2 Data Catalog warehouses via Cloudflare's <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. Two new datasets are available:</p>
<ul>
<li><strong><code>r2CatalogDataOperationsAdaptiveGroups</code></strong> tracks Iceberg REST API requests made to your catalog, including operation type, request duration, HTTP status, and request body bytes. Use this to monitor request volume and latency across warehouses, namespaces, and tables.</li>
<li><strong><code>r2CatalogTableMaintenanceAdaptiveGroups</code></strong> tracks table maintenance jobs such as compaction and snapshot expiration. Use this to monitor job success rates, files processed, bytes read and written, and job duration.</li>
</ul>
<p>Both datasets support filtering by warehouse name, namespace, table name, and time range. They also include percentile aggregations for duration metrics.</p>
<p>For detailed schema information and example queries, refer to the <a href="/r2-data-catalog/observability/metrics/">R2 Data Catalog metrics and analytics documentation</a>.</p>


<h2 id="empty-buckets-and-delete-folders-from-the-r2-dashboard"><a href="/changelog/post/2026-04-30-r2-empty-bucket-folder-delete/">Empty buckets and delete folders from the R2 dashboard</a></h2>
<p><em>2026-04-30</em></p>
<p>You can now empty an entire <a href="/r2/">R2</a> bucket or delete folders directly from the dashboard. Emptying a bucket is required before you can delete it. Previously, this required scripting or configuring <a href="/r2/buckets/object-lifecycles/">lifecycle rules</a>. Now, the dashboard can handle it in a single action.</p>
<h4 id="2026-04-30-r2-empty-bucket-folder-delete-empty-a-bucket">Empty a bucket</h4>
<p>Go to your bucket's <strong>Settings</strong> tab and select <strong>Empty</strong> under the <strong>Empty Bucket</strong> section. This deletes all objects in the bucket while preserving the bucket and its configuration. For large buckets, the operation runs in the background and the dashboard displays progress.</p>
<p>Emptying a bucket is also a prerequisite for deleting it. The dashboard now guides you through both steps in one place.</p>
<p><img src="/assets/upstream/images/r2/empty-bucket-changelog.png" alt="Empty Bucket and Delete Bucket sections in the R2 dashboard Settings tab" /></p>
<h4 id="2026-04-30-r2-empty-bucket-folder-delete-delete-folders">Delete folders</h4>
<p>R2 uses a flat object structure. The dashboard groups objects that share a common prefix into folders when the <strong>View prefixes as directories</strong> checkbox is selected. Deleting a folder removes every object under that prefix.</p>
<p>From the <strong>Objects</strong> tab, you can select one or more folders and delete them alongside individual objects.</p>
<p>For step-by-step instructions, refer to <a href="/r2/buckets/delete-buckets/">Delete buckets</a> and <a href="/r2/objects/delete-objects/">Delete objects</a>.</p>


<h2 id="hyperdrive-support-for-private-databases-with-workers-vpc"><a href="/changelog/post/2026-04-29-hyperdrive-vpc-private-databases/">Hyperdrive support for private databases with Workers VPC</a></h2>
<p><em>2026-04-29</em></p>
<p>You can now connect Hyperdrive to a private database through a <a href="/workers-vpc/">Workers VPC service</a>. This is the recommended way to connect Hyperdrive to a private database that is not exposed to the public Internet.</p>
<p>When creating a Hyperdrive configuration in the Cloudflare dashboard, choose <strong>Connect to private database</strong> and then <strong>Workers VPC</strong>. From there, you can select an existing VPC service or create a new one inline by picking a Cloudflare Tunnel and entering your origin host and TCP port.</p>
<p>You can also create a Hyperdrive configuration backed by a Workers VPC service from the command line:</p>
<pre><code class="language-sh">npx wrangler hyperdrive create my-vpc-database \&#10;  &#45;-service-id &lt;YOUR_VPC_SERVICE_ID&gt; \&#10;  &#45;-database &lt;DATABASE_NAME&gt; \&#10;  &#45;-user &lt;DATABASE_USER&gt; \&#10;  &#45;-password &lt;DATABASE_PASSWORD&gt; \&#10;  &#45;-scheme postgresql&#10;</code></pre>
<p>Workers VPC services are reusable across Hyperdrive configurations and can also be bound directly to Workers, so you can share the same private connection across multiple products.</p>
<p>To get started, refer to <a href="/hyperdrive/configuration/connect-to-private-database-vpc/">Connect Hyperdrive to a private database using Workers VPC</a>.</p>


<h2 id="realtime-backlog-metrics-now-available-for-queues"><a href="/changelog/post/2026-04-28-improved-queues-metrics/">Realtime backlog metrics now available for Queues</a></h2>
<p><em>2026-04-28</em></p>
<p><a href="/queues/">Queues</a>, Cloudflare's managed message queue, now exposes realtime backlog metrics via the dashboard, REST API, and JavaScript API. Three new fields are available:</p>
<ul>
<li><strong><code>backlog_count</code></strong> — the number of unacknowledged messages in the queue</li>
<li><strong><code>backlog_bytes</code></strong> — the total size of those messages in bytes</li>
<li><strong><code>oldest_message_timestamp_ms</code></strong> — the timestamp of the oldest unacknowledged message</li>
</ul>
<p>The following endpoints also now include a <code>metadata.metrics</code> object on the result field after successful message consumption:</p>
<ul>
<li><code>/accounts/{account_id}/queues/{queue_id}/messages/pull</code></li>
<li><code>/accounts/{account_id}/queues/{queue_id}/messages</code></li>
<li><code>/accounts/{account_id}/queues/{queue_id}/messages/batch</code></li>
</ul>
<h4 id="2026-04-28-improved-queues-metrics-javascript-apis">Javascript APIs</h4>
<p>Call <code>env.QUEUE.metrics()</code> to get realtime backlog metrics:</p>
<pre><code class="language-ts">const {&#10;	backlogCount, // number&#10;	backlogBytes, // number&#10;	oldestMessageTimestamp, // Date | undefined&#10;} = await env.QUEUE.metrics();&#10;</code></pre>
<p><code>env.QUEUE.send()</code> and <code>env.QUEUE.sendBatch()</code> also now return a metrics object on the response.</p>
<p>You can also query these fields via the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> or view realtime backlog on the <a href="https://dash.cloudflare.com/?to=/:account/workers/queues">dashboard</a>.</p>
<p><img src="/assets/upstream/images/changelog/queues/2026-04-28-queues-metrics.png" alt="Queues realtime backlog" /></p>
<p>For more information, refer to <a href="/queues/observability/metrics/">Queues metrics</a>.</p>


<h2 id="r2-data-catalog-snapshot-expiration-now-removes-unreferenced-data-files"><a href="/changelog/post/2026-04-22-snapshot-expiration-cleans-data-files/">R2 Data Catalog snapshot expiration now removes unreferenced data files</a></h2>
<p><em>2026-04-22</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a>, a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> catalog built into R2, now removes unreferenced data files during automatic snapshot expiration. This improvement reduces storage costs and eliminates the need to run manual maintenance jobs to reclaim space from deleted data.</p>
<p>Previously, snapshot expiration only cleaned up Iceberg metadata files such as manifests and manifest lists. Data files that were no longer referenced by active snapshots remained in R2 storage until you manually ran <code>remove_orphan_files</code> or <code>expire_snapshots</code> through an engine like Spark. This required extra operational overhead and left stale data files consuming storage.</p>
<p>Snapshot expiration now handles both metadata and data file cleanup automatically. When a snapshot is expired, any data files that are no longer referenced by retained snapshots are removed from R2 storage.</p>
<pre><code class="language-bash">&#35; Enable catalog-level snapshot expiration&#10;npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket \&#10;  &#45;-older-than-days 7 \&#10;  &#45;-retain-last 10&#10;</code></pre>
<p>For more information, refer to the <a href="/r2-data-catalog/table-maintenance/">table maintenance documentation</a>.</p>


<h2 id="access-durable-object-jurisdiction-via-ctx-id-jurisdiction"><a href="/changelog/post/2026-03-26-durable-object-id-jurisdiction/">Access Durable Object jurisdiction via `ctx.id.jurisdiction`</a></h2>
<p><em>2026-03-26</em></p>
<p><code>ctx.id.jurisdiction</code> inside a Durable Object now reports the <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">jurisdiction</a> the object was created in — for example <code>&quot;eu&quot;</code> when accessed through <code>env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;)</code> — so you can make region-aware decisions without passing the jurisdiction through method arguments or persisting it in storage. For the full list of ID-construction paths that preserve <code>jurisdiction</code>, refer to the <a href="/durable-objects/api/id/#jurisdiction">Durable Object ID documentation</a>.</p>
<pre><code class="language-js">export class RegionalRoom extends DurableObject {&#10;	async fetch(request) {&#10;		// &quot;eu&quot; when accessed through env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;)&#10;		const region = this.ctx.id.jurisdiction;&#10;		return new Response(`Hello from ${region ?? &quot;the default region&quot;}!`);&#10;	}&#10;}&#10;&#10;// Worker&#10;export default {&#10;	async fetch(request, env) {&#10;		const stub = env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;).getByName(&quot;general&quot;);&#10;		return stub.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p><code>ctx.id.jurisdiction</code> is <code>undefined</code> for Durable Objects that were not created in a jurisdiction-restricted namespace. Alarms scheduled before 2026-03-15 also do not have <code>jurisdiction</code> stored; to backfill the value, reschedule the alarm from a <code>fetch()</code> or RPC handler.</p>


<h2 id="hyperdrive-now-supports-custom-tls-ssl-certificates-for-mysql"><a href="/changelog/post/2026-03-19-hyperdrive-mysql-custom-certificate-support/">Hyperdrive now supports custom TLS/SSL certificates for MySQL</a></h2>
<p><em>2026-03-19</em></p>
<p>Hyperdrive now supports custom TLS/SSL certificates for MySQL databases, bringing the same certificate options previously available for PostgreSQL to MySQL connections.</p>
<p>You can now configure:</p>
<ul>
<li><strong>Server certificate verification</strong> with <code>VERIFY_CA</code> or <code>VERIFY_IDENTITY</code> SSL modes to verify that your MySQL database server's certificate is signed by the expected certificate authority (CA).</li>
<li><strong>Client certificates</strong> (mTLS) for Hyperdrive to authenticate itself to your MySQL database with credentials beyond username and password.</li>
</ul>
<p>Create a Hyperdrive configuration with custom certificates for MySQL:</p>
<pre><code class="language-bash">&#35; Upload a CA certificate&#10;npx wrangler cert upload certificate-authority --ca-cert your-ca-cert.pem --name your-custom-ca-name&#10;&#10;&#35; Create a Hyperdrive with VERIFY_IDENTITY mode&#10;npx wrangler hyperdrive create your-hyperdrive-config \&#10;  &#45;-connection-string=&quot;mysql://user:password@hostname:port/database&quot; \&#10;  &#45;-ca-certificate-id &lt;CA_CERT_ID&gt; \&#10;  &#45;-sslmode VERIFY_IDENTITY&#10;</code></pre>
<p>For more information, refer to <a href="/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/">SSL/TLS certificates for Hyperdrive</a> and <a href="/hyperdrive/examples/connect-to-mysql/">MySQL TLS/SSL modes</a>.</p>


<h2 id="return-up-to-50-query-results-with-values-or-metadata"><a href="/changelog/post/2026-03-16-topk-limit-increased-to-50/">Return up to 50 query results with values or metadata</a></h2>
<p><em>2026-03-16</em></p>
<p>You can now set <code>topK</code> up to <code>50</code> when a Vectorize query returns values or full metadata. This raises the previous limit of <code>20</code> for queries that use <code>returnValues: true</code> or <code>returnMetadata: &quot;all&quot;</code>.</p>
<p>Use the higher limit when you need more matches in a single query response without dropping values or metadata. Refer to the <a href="/vectorize/reference/client-api/">Vectorize API reference</a> for query options and current <code>topK</code> limits.</p>


<h2 id="access-durable-object-name-via-ctx-id-name"><a href="/changelog/post/2026-03-15-durable-object-id-name/">Access Durable Object name via `ctx.id.name`</a></h2>
<p><em>2026-03-15</em></p>
<p>When your Worker accesses a Durable Object via <code>idFromName()</code> or <code>getByName()</code>, the same name is now available on <code>ctx.id.name</code> inside the object — no need to pass it through method arguments or persist it in storage. This brings the runtime behavior in line with the <a href="/workers/languages/typescript/">Workers runtime types</a>.</p>
<p>This is especially useful for <a href="/durable-objects/api/alarms/">alarms</a>, where there is no calling client to pass the name as an argument. When an alarm handler runs, <code>ctx.id.name</code> will hold the same name the object was originally accessed with.</p>
<pre><code class="language-js">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;export class ChatRoom extends DurableObject {&#10;  async getRoomName() {&#10;    // ctx.id.name returns the name passed to getByName() or idFromName()&#10;    return this.ctx.id.name;&#10;  }&#10;}&#10;&#10;// Worker&#10;export default {&#10;  async fetch(request, env) {&#10;    const stub = env.CHAT_ROOM.getByName(&quot;general&quot;);&#10;    const roomName = await stub.getRoomName();&#10;    return new Response(`Welcome to ${roomName}!`);&#10;  },&#10;};&#10;</code></pre>
<p><code>ctx.id.name</code> is <code>undefined</code> in the following cases:</p>
<ul>
<li>For Durable Objects created with <code>newUniqueId()</code>.</li>
<li>When accessed via <code>idFromString()</code>, even if the ID was originally created from a name.</li>
<li>For <a href="/durable-objects/api/id/#name">names longer than 1,024 bytes</a>.</li>
</ul>
<p>This works the same way in local development with <code>wrangler dev</code> as it does in production. Run <code>npm update wrangler</code> to ensure you are on a version with this support.</p>
<p>For more information, refer to the <a href="/durable-objects/api/id/#name">Durable Object ID documentation</a>.</p>


<h2 id="deleteall-now-deletes-durable-object-alarm"><a href="/changelog/post/2026-02-24-deleteall-deletes-alarms/">deleteAll() now deletes Durable Object alarm</a></h2>
<p><em>2026-02-24</em></p>
<p><code>deleteAll()</code> now deletes a Durable Object alarm in addition to stored data for Workers with a compatibility date of <code>2026-02-24</code> or later. This change simplifies clearing a Durable Object's storage with a single API call.</p>
<p>Previously, <code>deleteAll()</code> only deleted user-stored data for an object. Alarm usage stores metadata in an object's storage, which required a separate <code>deleteAlarm()</code> call to fully clean up all storage for an object. The <code>deleteAll()</code> change applies to both KV-backed and SQLite-backed Durable Objects.</p>
<pre><code class="language-js">// Before: two API calls required to clear all storage&#10;await this.ctx.storage.deleteAlarm();&#10;await this.ctx.storage.deleteAll();&#10;&#10;// Now: a single call clears both data and the alarm&#10;await this.ctx.storage.deleteAll();&#10;</code></pre>
<p>For more information, refer to the <a href="/durable-objects/api/sqlite-storage-api/#deleteall">Storage API documentation</a>.</p>


<h2 id="backup-and-restore-api-for-sandbox-sdk"><a href="/changelog/post/2026-02-23-sandbox-backup-restore-api/">Backup and restore API for Sandbox SDK</a></h2>
<p><em>2026-02-23</em></p>
<p><a href="/sandbox/">Sandboxes</a> now support <code>createBackup()</code> and <code>restoreBackup()</code> methods for creating and restoring point-in-time snapshots of directories.</p>
<p>This allows you to restore environments quickly. For instance, in order to develop in a sandbox, you may need to include a user's codebase and run a build step.
Unfortunately <code>git clone</code> and <code>npm install</code> can take minutes, and you don't want to run these steps every time the user starts their sandbox.</p>
<p>Now, after the initial setup, you can just call <code>createBackup()</code>, then <code>restoreBackup()</code> the next time this environment is needed. This makes it practical to pick up exactly
where a user left off, even after days of inactivity, without repeating expensive setup steps.</p>
<pre><code class="language-ts">const sandbox = getSandbox(env.Sandbox, &quot;my-sandbox&quot;);&#10;&#10;// Make non-trivial changes to the file system&#10;await sandbox.gitCheckout(endUserRepo, { targetDir: &quot;/workspace&quot; });&#10;await sandbox.exec(&quot;npm install&quot;, { cwd: &quot;/workspace&quot; });&#10;&#10;// Create a point-in-time backup of the directory&#10;const backup = await sandbox.createBackup({ dir: &quot;/workspace&quot; });&#10;&#10;// Store the handle for later use&#10;await env.KV.put(`backup:${userId}`, JSON.stringify(backup));&#10;&#10;// ... in a future session...&#10;&#10;// Restore instead of re-cloning and reinstalling&#10;await sandbox.restoreBackup(backup);&#10;</code></pre>
<p>Backups are stored in <a href="/r2">R2</a> and can take advantage of <a href="/sandbox/guides/backup-restore/#configure-r2-lifecycle-rules-for-automatic-cleanup">R2 object lifecycle rules</a> to ensure they do not persist forever.</p>
<p>Key capabilities:</p>
<ul>
<li><strong>Persist and reuse across sandbox sessions</strong> — Easily store backup handles in KV, D1, or Durable Object storage for use in subsequent sessions</li>
<li><strong>Usable across multiple instances</strong> — Fork a backup across many sandboxes for parallel work</li>
<li><strong>Named backups</strong> — Provide optional human-readable labels for easier management</li>
<li><strong>TTLs</strong> — Set time-to-live durations so backups are automatically removed from storage once they are no longer needed</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17640.md")</aside>
<p>To get started, refer to the <a href="/sandbox/guides/backup-restore/">backup and restore guide</a> for setup instructions and usage patterns, or the <a href="/sandbox/api/backups/">Backups API reference</a> for full method documentation.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/storage/">Previous</a><span>Page 2 of 5</span><a class="pagination-next" rel="next" href="/changelog/product-group/storage/3/">Next</a></nav>
