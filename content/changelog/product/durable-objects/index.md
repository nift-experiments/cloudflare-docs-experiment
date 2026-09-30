---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/durable-objects/
  description: '2026-09-17'
  full_title: durable-objects changelog | Cloudflare Docs
  head_html: <title>durable-objects changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-17"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/durable-objects/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="durable-objects changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-17"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/durable-objects/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/durable-objects/#page","headline":"durable-objects changelog | Cloudflare Docs","description":"2026-09-17","url":"https://developers.cloudflare.com/changelog/product/durable-objects/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/durable-objects/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="workers-traces-now-automatically-include-javascript-rpc-session-spans"><a href="/changelog/post/2026-09-17-javascript-rpc-session-spans/">Workers traces now automatically include JavaScript RPC session spans</a></h2>
<p><em>2026-09-17</em></p>
<p>Workers traces can now follow JavaScript RPC calls across Worker boundaries and into Durable Objects. Previously, a trace stopped at the caller's RPC boundary. The dashboard now shows the caller-side session and method calls alongside the callee invocation, nested calls, and callbacks into another Worker.</p>
<p>A session span covers the lifetime of a caller-side session and groups calls that reuse it. Individual call spans show each method invocation. Execution colors distinguish the Workers or Durable Object entrypoints involved, while arrows mark outgoing and incoming calls. Together, these details show where time was spent, which calls reused a session, and how returned stubs and callbacks fit into the request.</p>
<p><img src="/assets/upstream/images/workers/changelog/jsrpc-session-spans.png" alt="A Workers trace of a Worker-to-Worker RPC session, showing the session span, the caller's getCounter and increment call spans, and the callee's invocation and matching call spans" /></p>
<p>Enable tracing with one setting in your <a href="/workers/wrangler/configuration/#observability">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17815.md")</div>
<p>Cloudflare records these spans automatically. You do not need to change your application code or add an observability SDK.</p>
<p>For supported spans and attributes, refer to <a href="/workers/observability/traces/spans-and-attributes/">Spans and attributes</a>.</p>


<h2 id="durable-objects-can-use-up-to-ten-dynamic-workers-concurrently"><a href="/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/">Durable Objects can use up to ten Dynamic Workers concurrently</a></h2>
<p><em>2026-08-28</em></p>
<p><a href="/durable-objects/">Durable Objects</a> can have up to ten distinct <a href="/dynamic-workers/">Dynamic Workers</a> with in-flight requests, increased from four. This limit applies across all concurrent requests to the same Durable Object because they share an input/output (I/O) context. Other Workers can have up to four distinct Dynamic Workers with in-flight requests per request.</p>
<p>Multiple in-flight requests to the same Dynamic Worker count as one toward this limit.</p>
<p>For more information, refer to <a href="/dynamic-workers/platform/limits/">Dynamic Workers limits</a>.</p>


<h2 id="prevent-durable-object-alarm-retries-when-using-ctx-abort"><a href="/changelog/post/2026-08-25-durable-object-alarm-abort-no-retry/">Prevent Durable Object alarm retries when using `ctx.abort()`</a></h2>
<p><em>2026-08-25</em></p>
<p>By default, an alarm interrupted by <code>ctx.abort()</code> retries after the Durable Object resets. Pass <code>{ retryAlarm: false }</code> when the alarm should stop instead:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17720.md")</div>
<p>For example, an alarm that deletes its storage can use this option to avoid repeating the cleanup or re-running the Durable Object constructor.</p>
<p>Alarms can run concurrently with other requests to the same Durable Object. If another request calls <code>ctx.abort()</code> while an alarm is running, the <code>retryAlarm</code> option on that call also controls whether the alarm retries.</p>
<p>The default retry prevents an unrelated request from permanently canceling the alarm. Set <code>retryAlarm: false</code> on every abort path that should stop an in-progress alarm, not only on calls from the alarm handler. Existing calls to <code>ctx.abort()</code> keep retrying alarms.</p>
<p>For local development, <code>retryAlarm</code> requires Wrangler 4.126.0 or later.</p>
<p>For more information, refer to <a href="/durable-objects/api/state/#abort"><code>ctx.abort()</code></a>.</p>


<h2 id="view-deployments-for-durable-objects-in-the-dashboard"><a href="/changelog/post/2026-08-20-durable-objects-deployments-tab/">View deployments for Durable Objects in the dashboard</a></h2>
<p><em>2026-08-20</em></p>
<p>Durable Object namespaces now have a <strong>Deployments</strong> tab in the Cloudflare dashboard, showing the <a href="/workers/versions-and-deployments/#versions">versions</a> of the backing Worker that are currently live and the traffic split between them.</p>
<p><img src="/assets/upstream/images/changelog/durable-objects/durable-objects-deployments-tab.png" alt="The Deployments tab for a Durable Object namespace, showing two versions with their traffic %, requests/sec, error rate, and median wall time" /></p>
<div class="nb-dash-button"></div>
<p>A Durable Object namespace is backed by a Worker script, so its deployments are the same as that Worker's deployments. Previously, checking on a <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployment</a> in progress for a Durable Object meant navigating to the backing Worker. The new tab surfaces that information directly on the namespace, alongside the metrics that matter for it: requests, error rate, and wall time per version.</p>
<p>The tab is read-only — promoting, rolling back, or splitting traffic on a deployment is still managed from the backing Worker's Deployments tab.</p>
<h4 id="2026-08-20-durable-objects-deployments-tab-actual-vs-configured-traffic-split">Actual vs. configured traffic split</h4>
<p>The <strong>Traffic %</strong> column, for both Workers and Durable Objects, now shows the actual, observed traffic share for each version next to the percentage you configured. Previously, this column only showed the configured percentage. If you moved a deployment from 50/50 to 100% on a new version, the configured number updated immediately, but requests take time to catch up, and there was no way to tell how far along that shift was without checking metrics elsewhere.</p>
<p>The configured split assigns Worker versions to individual Durable Objects, not to individual requests. Because <a href="/workers/versions-and-deployments/gradual-deployments/with-durable-objects/">each Durable Object is pinned to the version it started on until you create a new deployment</a> and some objects naturally receive more traffic than others, the observed split can differ from the configured one for as long as multiple versions are active.</p>
<p>Actual traffic share is calculated from the same <a href="/analytics/graphql-api/">GraphQL Analytics API</a> data that powers other Workers and Durable Objects metrics, so standard ingestion delay and <a href="/analytics/faq/graphql-api-inconsistent-results/">sampling</a> apply. Durable Objects analytics can lag Workers analytics by several minutes, so a version's actual share may take a little longer to catch up after a change.</p>
<p>To view this, go to <strong>Workers &amp; Pages</strong> &gt; <strong>Durable Objects</strong>, select a namespace, then select the <strong>Deployments</strong> tab. For more on how gradual deployments work, refer to <a href="/workers/versions-and-deployments/gradual-deployments/">Gradual deployments</a>.</p>


<h2 id="inspect-worker-startup-performance-with-wrangler"><a href="/changelog/post/2026-07-31-wrangler-startup-profile-summary/">Inspect Worker startup performance with Wrangler</a></h2>
<p><em>2026-07-31</em></p>
<p><code>wrangler check startup</code> now reports your Worker's raw and compressed bundle sizes. It also summarizes local CPU activity during startup directly in your terminal.</p>
<p>Large bundles and costly startup work can introduce cold-start latency, so use this command to find code and large dependencies that slow your Worker before it handles requests.</p>
<p>The summary includes sampled, active, garbage collection, and idle time. Wrangler continues to save a <code>.cpuprofile</code> file for detailed flamegraph analysis in Chrome DevTools or VS Code.</p>
<pre tabindex="0"><code class="language-bash">⛅️ wrangler 4.116.0&#10;───────────────────────────────────────────────&#10;├ Building your Worker&#10;│ Worker Built! 🎉&#10;│&#10;├ Analysing&#10;│ Startup phase analysed&#10;│&#10;│ Bundle: 7171.25 KiB / gzip: 2197.00 KiB&#10;│&#10;│ Local startup profile:&#10;│   Profile window: 70.3 ms&#10;│   Sampled time: 70.3 ms&#10;│   Active: 38.5 ms (including 3.7 ms garbage collection)&#10;│   Idle: 31.8 ms&#10;│   Samples: 36&#10;│&#10;│ CPU Profile has been written to worker-startup.cpuprofile. Load it into the Chrome DevTools profiler (or directly in VSCode) to view a flamegraph.&#10;│&#10;│ Note that the CPU Profile was measured on your Worker running locally on your machine, which has a different CPU than when your Worker runs on Cloudflare.&#10;│&#10;│ As such, CPU Profile can be used to understand where time is spent at startup, but the overall startup time in the profile should not be expected to exactly match what your Worker&#x27;s startup time will be when deploying to Cloudflare.&#10;</code></pre>
<p>The profile runs locally, so its duration will differ from startup time on Cloudflare. For authoritative startup time, deploy your Worker or upload a version.</p>
<p>Available in Wrangler version 4.116.0 or later. For more information, refer to <a href="/workers/wrangler/commands/workers/#startup"><code>wrangler check startup</code></a>.</p>


<h2 id="filter-durable-object-logs-and-traces-by-instance-id"><a href="/changelog/post/2026-07-24-durable-object-instance-observability/">Filter Durable Object logs and traces by instance ID</a></h2>
<p><em>2026-07-24</em></p>
<p><a href="/workers/observability/logs/workers-logs/">Workers Logs</a> and <a href="/workers/observability/exporting-opentelemetry-data/">OpenTelemetry</a> spans for <a href="/durable-objects/">Durable Object</a> requests include the Durable Object instance ID.</p>
<p>Use <code>$workers.durableObjectId</code> to filter logs for a specific instance. Root and child spans include the same ID in <code>cloudflare.durable_object.id</code>.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-07-24-durable-object-trace-filter.png" alt="Query Builder filtering traces by Durable Object instance ID" /></p>
<p>Use these fields to isolate a specific instance and correlate its logs and traces.</p>
<p>For more information, refer to <a href="/durable-objects/observability/metrics-and-analytics/">Durable Objects metrics and analytics</a> and <a href="/workers/observability/traces/spans-and-attributes/">Workers tracing spans and attributes</a>.</p>


<h2 id="view-total-sqlite-storage-for-durable-object-namespaces"><a href="/changelog/post/2026-07-20-durable-objects-total-storage-metrics/">View total SQLite storage for Durable Object namespaces</a></h2>
<p><em>2026-07-20</em></p>
<p>You can now monitor the total SQLite storage used by a Durable Object namespace over time in the Cloudflare dashboard. The new <strong>Total storage</strong> chart shows the maximum storage reported during each hour. This helps you identify storage growth, validate data cleanup, and investigate unexpected usage.</p>
<p><img src="/assets/upstream/images/changelog/durable-objects/durable-objects-total-storage.png" alt="The Total storage chart showing a Durable Object namespace growing to 260.1 MB of storage over time." /></p>
<div class="nb-dash-button"></div>
<p>The chart appears only for SQLite-backed Durable Object namespaces. It does not appear for namespaces that use the legacy key-value storage backend. Viewing storage for individual Durable Objects by ID or name is not supported.</p>
<p>For more information, refer to <a href="/durable-objects/observability/metrics-and-analytics/#total-storage">Metrics and analytics</a>.</p>


<h2 id="new-durable-object-namespaces-must-use-the-sqlite-storage-backend"><a href="/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/">New Durable Object namespaces must use the SQLite storage backend</a></h2>
<p><em>2026-07-09</em></p>
<p>If your account does not already have a key-value (KV) backed Durable Object namespace, you can no longer create new ones. New Durable Object namespaces must use the <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">SQLite storage backend</a>, which has been recommended for all new Durable Objects since it became <a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">generally available</a> in 2024.</p>
<p>Create a new class with a <code>new_sqlite_classes</code> migration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17719.md")</div>
<p>SQLite-backed Durable Objects have feature parity with the key-value backend — including the <a href="/durable-objects/api/sqlite-storage-api/#synchronous-kv-api">key-value storage API</a> — and additionally support relational <a href="/durable-objects/api/sqlite-storage-api/#sql-api">SQL queries</a> and <a href="/durable-objects/api/sqlite-storage-api/#pitr-point-in-time-recovery-api">point-in-time recovery</a> to restore an object's storage to any point in the past 30 days.</p>
<p>If you attempt to create a new key-value backed namespace (a <code>new_classes</code> migration) on an affected account, the deployment fails with the following error:</p>
<pre tabindex="0"><code class="language-txt">Creating new key-value backed Durable Object namespaces is no longer supported on this account. Please create a namespace using a `new_sqlite_classes` migration instead.&#10;</code></pre>
<p>This change only affects accounts that are not already using the key-value storage backend. Accounts with at least one existing key-value backed namespace can still create new ones for now, and the Workers Free plan has only ever supported SQLite-backed Durable Objects. It is part of a broader move toward SQLite as the single storage backend for Durable Objects, ahead of a future migration path for existing key-value backed objects.</p>
<p>For more information, refer to <a href="/durable-objects/reference/durable-objects-migrations/">Durable Objects migrations</a>.</p>


<h2 id="declare-durable-object-class-lifecycle-with-exports"><a href="/changelog/post/2026-06-30-declarative-do-class-exports/">Declare Durable Object class lifecycle with `exports`</a></h2>
<p><em>2026-07-04</em></p>
<p>A new declarative <a href="/durable-objects/reference/durable-objects-migrations/"><code>exports</code></a> field in your Wrangler configuration file replaces the imperative <a href="/durable-objects/reference/durable-object-class-migrations-legacy/"><code>migrations</code></a> array for managing Durable Object class lifecycle. Instead of writing an ordered list of migration steps with unique tags, you declare each Durable Object class your Worker exports and Cloudflare compares that against what's already deployed to determine what Durable Object state needs to be created, renamed, or deleted.</p>
<p>With legacy migrations, renaming <code>ChatRoom</code> to <code>Room</code> requires retaining both tagged steps:</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;migrations&quot;: [&#10;		{ &quot;tag&quot;: &quot;v1&quot;, &quot;new_sqlite_classes&quot;: [&quot;ChatRoom&quot;] },&#10;		{&#10;			&quot;tag&quot;: &quot;v2&quot;,&#10;			&quot;renamed_classes&quot;: [{ &quot;from&quot;: &quot;ChatRoom&quot;, &quot;to&quot;: &quot;Room&quot; }],&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p>With <code>exports</code>, you instead declare <code>Room</code> as the current class and mark <code>ChatRoom</code> as renamed:</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;exports&quot;: {&#10;		&quot;ChatRoom&quot;: {&#10;			&quot;type&quot;: &quot;durable-object&quot;,&#10;			&quot;state&quot;: &quot;renamed&quot;,&#10;			&quot;renamed_to&quot;: &quot;Room&quot;,&#10;		},&#10;		&quot;Room&quot;: { &quot;type&quot;: &quot;durable-object&quot;, &quot;storage&quot;: &quot;sqlite&quot; },&#10;	},&#10;}&#10;</code></pre>
<p>Each entry is keyed by class name. The <code>state</code> field carries the lifecycle (<code>created</code> by default — a live class — plus tombstone states <code>deleted</code>, <code>renamed</code>, and <code>transferred</code>, and the <code>expecting-transfer</code> receiving state for cross-Worker transfers).</p>
<p>Key improvements over the legacy <code>migrations</code> array:</p>
<ul>
<li><strong>No migration tags.</strong> The current <code>exports</code> map is the source of truth — there is no historical chain of <code>v1</code>, <code>v2</code>, <code>v3</code> entries to maintain.</li>
<li><strong>Structured deployment output.</strong> Wrangler reports when it creates, updates, deletes, renames, or transfers Durable Object classes. It also identifies stale configuration entries that are safe to remove. Deployments with no changes or notices do not print this output.</li>
<li><strong>Zero-downtime rename and transfer patterns are first-class.</strong> Tombstones may coexist with the source class still in code, enabling a <a href="/durable-objects/reference/durable-objects-migrations/#avoid-downtime-during-a-rename">three-deploy rename</a> and a <a href="/durable-objects/reference/durable-objects-migrations/#transfer-a-durable-object-class-between-workers">four-deploy cross-Worker transfer</a> without runtime errors during the rollout window.</li>
<li><strong>Cross-Worker safety.</strong> When you delete or rename a class, Cloudflare lists every other Worker in your account whose bindings still reference the namespace, so you can redeploy them before the change goes live.</li>
</ul>
<p>Existing Workers using the legacy <a href="/durable-objects/reference/durable-object-class-migrations-legacy/"><code>migrations</code></a> array continue to work unchanged. To move to <code>exports</code>, refer to the <a href="/durable-objects/reference/durable-objects-migrations/#migrate-from-the-legacy-migrations-flow">migration guide</a>. <code>exports</code> and <code>migrations</code> are mutually exclusive within a single Worker.</p>
<p>For the full reference, refer to <a href="/durable-objects/reference/durable-objects-migrations/">Durable Object class exports</a>.</p>


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
<pre tabindex="0"><code class="language-js">// Worker&#10;export default {&#10;	async fetch(request, env) {&#10;		const usSubnamespace = env.MY_DURABLE_OBJECT.jurisdiction(&quot;us&quot;);&#10;		const stub = usSubnamespace.getByName(&quot;general&quot;);&#10;		return stub.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p>Workers may still access Durable Objects constrained to the <code>us</code> jurisdiction from anywhere in the world. The jurisdiction constraint only controls where the Durable Object itself runs and persists data.</p>
<p>For the full list of supported jurisdictions, refer to <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">Data location — Restrict Durable Objects to a jurisdiction</a>.</p>


<h2 id="test-durable-object-eviction-with-new-cloudflare-test-helpers"><a href="/changelog/post/2026-06-25-durable-object-eviction-test-helpers/">Test Durable Object eviction with new cloudflare:test helpers</a></h2>
<p><em>2026-06-25</em></p>
<p>The <code>@cloudflare/vitest-pool-workers</code> package now includes <code>evictDurableObject</code> and <code>evictAllDurableObjects</code> test helpers, exported from <code>cloudflare:test</code>.</p>
<p>These helpers let you test how a Durable Object behaves across evictions, simulating the production lifecycle where an idle Durable Object can be evicted from memory.</p>
<p>For more context, refer to <a href="/durable-objects/concepts/durable-object-lifecycle/">Lifecycle of a Durable Object</a>.</p>
<pre tabindex="0"><code class="language-ts">import { evictDurableObject, evictAllDurableObjects } from &quot;cloudflare:test&quot;;&#10;import { env } from &quot;cloudflare:workers&quot;;&#10;&#10;const id = env.COUNTER.idFromName(&quot;my-counter&quot;);&#10;const stub = env.COUNTER.get(id);&#10;&#10;// Evict the Durable Object instance pointed to by a specific stub&#10;await evictDurableObject(stub);&#10;&#10;// Close WebSockets instead of hibernating them&#10;await evictDurableObject(stub, { webSockets: &quot;close&quot; });&#10;&#10;// Evict all currently-running Durable Objects in evictable namespaces&#10;await evictAllDurableObjects();&#10;</code></pre>
<p>These helpers are available in <code>@cloudflare/vitest-pool-workers@0.16.20</code> and later.</p>
<p>Learn more in the <a href="/workers/testing/vitest-integration/test-apis/#durable-objects">Test APIs reference</a> and the <a href="/durable-objects/examples/testing-with-durable-objects/#testing-eviction">Testing Durable Objects guide</a>.</p>


<h2 id="new-asia-pacific-location-hints-apac-ne-and-apac-se"><a href="/changelog/post/2026-06-19-apac-ne-apac-se-location-hints/">New Asia-Pacific location hints: apac-ne and apac-se</a></h2>
<p><em>2026-06-19</em></p>
<p>Durable Objects now supports two new location hints for Asia-Pacific: <code>apac-ne</code> (Northeast Asia-Pacific) and <code>apac-se</code> (Southeast Asia-Pacific). Use <code>apac-ne</code> or <code>apac-se</code> when you want finer-grained placement within Asia-Pacific rather than the broader <code>apac</code> hint.</p>
<p>Use the new hints the same way as any other <code>locationHint</code>:</p>
<pre tabindex="0"><code class="language-js">// Northeast Asia-Pacific (Japan, Korea, etc.)&#10;const stubNE = env.MY_DURABLE_OBJECT.get(id, { locationHint: &quot;apac-ne&quot; });&#10;&#10;// Southeast Asia-Pacific (Singapore, Indonesia, etc.)&#10;const stubSE = env.MY_DURABLE_OBJECT.get(id, { locationHint: &quot;apac-se&quot; });&#10;</code></pre>
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


<h2 id="access-durable-object-jurisdiction-via-ctx-id-jurisdiction"><a href="/changelog/post/2026-03-26-durable-object-id-jurisdiction/">Access Durable Object jurisdiction via `ctx.id.jurisdiction`</a></h2>
<p><em>2026-03-26</em></p>
<p><code>ctx.id.jurisdiction</code> inside a Durable Object now reports the <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">jurisdiction</a> the object was created in — for example <code>&quot;eu&quot;</code> when accessed through <code>env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;)</code> — so you can make region-aware decisions without passing the jurisdiction through method arguments or persisting it in storage. For the full list of ID-construction paths that preserve <code>jurisdiction</code>, refer to the <a href="/durable-objects/api/id/#jurisdiction">Durable Object ID documentation</a>.</p>
<pre tabindex="0"><code class="language-js">export class RegionalRoom extends DurableObject {&#10;	async fetch(request) {&#10;		// &quot;eu&quot; when accessed through env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;)&#10;		const region = this.ctx.id.jurisdiction;&#10;		return new Response(`Hello from ${region ?? &quot;the default region&quot;}!`);&#10;	}&#10;}&#10;&#10;// Worker&#10;export default {&#10;	async fetch(request, env) {&#10;		const stub = env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;).getByName(&quot;general&quot;);&#10;		return stub.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p><code>ctx.id.jurisdiction</code> is <code>undefined</code> for Durable Objects that were not created in a jurisdiction-restricted namespace. Alarms scheduled before 2026-03-15 also do not have <code>jurisdiction</code> stored; to backfill the value, reschedule the alarm from a <code>fetch()</code> or RPC handler.</p>


<h2 id="access-durable-object-name-via-ctx-id-name"><a href="/changelog/post/2026-03-15-durable-object-id-name/">Access Durable Object name via `ctx.id.name`</a></h2>
<p><em>2026-03-15</em></p>
<p>When your Worker accesses a Durable Object via <code>idFromName()</code> or <code>getByName()</code>, the same name is now available on <code>ctx.id.name</code> inside the object — no need to pass it through method arguments or persist it in storage. This brings the runtime behavior in line with the <a href="/workers/languages/typescript/">Workers runtime types</a>.</p>
<p>This is especially useful for <a href="/durable-objects/api/alarms/">alarms</a>, where there is no calling client to pass the name as an argument. When an alarm handler runs, <code>ctx.id.name</code> will hold the same name the object was originally accessed with.</p>
<pre tabindex="0"><code class="language-js">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;export class ChatRoom extends DurableObject {&#10;  async getRoomName() {&#10;    // ctx.id.name returns the name passed to getByName() or idFromName()&#10;    return this.ctx.id.name;&#10;  }&#10;}&#10;&#10;// Worker&#10;export default {&#10;  async fetch(request, env) {&#10;    const stub = env.CHAT_ROOM.getByName(&quot;general&quot;);&#10;    const roomName = await stub.getRoomName();&#10;    return new Response(`Welcome to ${roomName}!`);&#10;  },&#10;};&#10;</code></pre>
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
<pre tabindex="0"><code class="language-js">// Before: two API calls required to clear all storage&#10;await this.ctx.storage.deleteAlarm();&#10;await this.ctx.storage.deleteAll();&#10;&#10;// Now: a single call clears both data and the alarm&#10;await this.ctx.storage.deleteAll();&#10;</code></pre>
<p>For more information, refer to the <a href="/durable-objects/api/sqlite-storage-api/#deleteall">Storage API documentation</a>.</p>


<h2 id="new-best-practices-guide-for-durable-objects"><a href="/changelog/post/2025-12-15-rules-of-durable-objects/">New Best Practices guide for Durable Objects</a></h2>
<p><em>2025-12-15</em></p>
<p>A new <a href="/durable-objects/best-practices/rules-of-durable-objects/">Rules of Durable Objects</a> guide is now available, providing opinionated best practices for building effective Durable Objects applications. This guide covers design patterns, storage strategies, concurrency, and common anti-patterns to avoid.</p>
<p>Key guidance includes:</p>
<ul>
<li><strong>Design around your &quot;atom&quot; of coordination</strong> — Create one Durable Object per logical unit (chat room, game session, user) instead of a global singleton that becomes a bottleneck.</li>
<li><strong>Use SQLite storage with RPC methods</strong> — SQLite-backed Durable Objects with typed RPC methods provide the best developer experience and performance.</li>
<li><strong>Understand input and output gates</strong> — Learn how Cloudflare's runtime prevents data races by default, how write coalescing works, and when to use <code>blockConcurrencyWhile()</code>.</li>
<li><strong>Leverage Hibernatable WebSockets</strong> — Reduce costs for real-time applications by allowing Durable Objects to sleep while maintaining WebSocket connections.</li>
</ul>
<p>The <a href="/durable-objects/examples/testing-with-durable-objects/">testing documentation</a> has also been updated with modern patterns using <code>@cloudflare/vitest-pool-workers</code>, including examples for testing SQLite storage, alarms, and direct instance access:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17718.md")</div>


<h2 id="billing-for-sqlite-storage"><a href="/changelog/post/2025-12-12-durable-objects-sqlite-storage-billing/">Billing for SQLite Storage</a></h2>
<p><em>2025-12-12</em></p>
<p>Storage billing for SQLite-backed Durable Objects will be enabled in January 2026, with a target date of January 7, 2026 (no earlier).</p>
<p>To view your SQLite storage usage, go to the <strong>Durable Objects</strong> page</p>
<div class="nb-dash-button"></div>
<p>If you do not want to incur costs, please take action such as optimizing queries or deleting unnecessary stored data in order to reduce your SQLite storage usage ahead of the January 7th target. Only usage on and after the billing target date will incur charges.</p>
<p>Developers on the Workers Paid plan with Durable Object's SQLite storage usage beyond included limits will incur charges according to <a href="/durable-objects/platform/pricing/#sqlite-storage-backend">SQLite storage pricing</a> announced in September 2024 with the <a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">public beta</a>. Developers on the Workers Free plan will not be charged.</p>
<p>Compute billing for SQLite-backed Durable Objects has been enabled since the initial public beta. SQLite-backed Durable Objects currently incur <a href="/durable-objects/platform/pricing/#compute-billing">charges for requests and duration</a>, and no changes are being made to compute billing.</p>
<p>For more information about SQLite storage pricing and limits, refer to the <a href="/durable-objects/platform/pricing/#sqlite-storage-backend">Durable Objects pricing documentation</a>.</p>


<h2 id="workers-websocket-message-size-limit-increased-from-1-mib-to-32-mib"><a href="/changelog/post/2025-10-31-increased-websocket-message-size-limit/">Workers WebSocket message size limit increased from 1 MiB to 32 MiB</a></h2>
<p><em>2025-10-31</em></p>
<p>Workers, including those using <a href="/durable-objects/">Durable Objects</a> and <a href="/browser-run/">Browser Rendering</a>, may now process WebSocket messages up to 32 MiB in size. Previously, this limit was 1 MiB.</p>
<p>This change allows Workers to handle use cases requiring large message sizes, such as processing Chrome Devtools Protocol messages.</p>
<p>For more information, please see the <a href="/durable-objects/platform/limits/#sqlite-backed-durable-objects-general-limits">Durable Objects startup limits</a>.</p>


<h2 id="view-and-edit-durable-object-data-in-ui-with-data-studio-beta"><a href="/changelog/post/2025-10-16-durable-objects-data-studio/">View and edit Durable Object data in UI with Data Studio (Beta)</a></h2>
<p><em>2025-10-16</em></p>
<p><img src="/assets/upstream/images/workers/changelog/do-data-studio.png" alt="Screenshot of Durable Objects Data Studio" /></p>
<p>You can now view and write to each Durable Object's storage using a UI editor on the Cloudflare dashboard. Only Durable Objects using <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">SQLite storage</a> can use Data Studio.</p>
<div class="nb-dash-button"></div>
<p>Data Studio unlocks easier data access with Durable Objects for prototyping application data models to debugging production storage usage. Before, querying your Durable Objects data required deploying a Worker.</p>
<p>To access a Durable Object, you can provide an object's unique name or ID generated by Cloudflare. Data Studio requires you to have at least the <code>Workers Platform Admin</code> role, and all queries are captured with audit logging for your security and compliance needs. Queries executed by Data Studio send requests to your remote, deployed objects and incur normal usage billing.</p>
<p>To learn more, visit the Data Studio <a href="/durable-objects/observability/data-studio/">documentation</a>. If you have feedback or suggestions for the new Data Studio, please share your experience on <a href="https://discord.com/channels/595317990191398933/773219443911819284">Discord</a></p>


<h2 id="new-getbyname-api-to-access-durable-objects"><a href="/changelog/post/2025-08-21-durable-objects-get-by-name/">New getByName() API to access Durable Objects</a></h2>
<p><em>2025-08-21</em></p>
<p>You can now create a client (a <a href="/durable-objects/api/stub/">Durable Object stub</a>) to a Durable Object with the new <code>getByName</code> method, removing the need to convert Durable Object names to IDs and then create a stub.</p>
<pre tabindex="0"><code class="language-js">// Before: (1) translate name to ID then (2) get a client &#10;const objectId = env.MY_DURABLE_OBJECT.idFromName(&quot;foo&quot;); // or .newUniqueId()&#10;const stub = env.MY_DURABLE_OBJECT.get(objectId); &#10;&#10;// Now: retrieve client to Durable Object directly via its name &#10;const stub = env.MY_DURABLE_OBJECT.getByName(&quot;foo&quot;);&#10;&#10;// Use client to send request to the remote Durable Object&#10;const rpcResponse = await stub.sayHello();&#10;</code></pre>
<p>Each Durable Object has a globally-unique name, which allows you to send requests to a specific object from anywhere in the world. Thus, a Durable Object can be used to coordinate between multiple clients who need to work together. You can have billions of Durable Objects, providing isolation between application tenants.</p>
<p>To learn more, visit the Durable Objects <a href="/durable-objects/api/namespace/#getbyname">API Documentation</a> or the <a href="/durable-objects/get-started/">getting started guide</a>.</p>


<h2 id="cloudflare-actors-library-sdk-for-durable-objects-in-beta"><a href="/changelog/post/2025-06-25-actors-package-alpha/">@cloudflare/actors library - SDK for Durable Objects in beta</a></h2>
<p><em>2025-06-25</em></p>
<p>The new <a href="https://www.npmjs.com/package/@cloudflare/actors">@cloudflare/actors</a> library is now in beta!</p>
<p>The <code>@cloudflare/actors</code> library is a new SDK for Durable Objects and provides a powerful set of abstractions for building real-time, interactive, and multiplayer applications on top of Durable Objects. With beta usage and feedback, <code>@cloudflare/actors</code> will become the recommended way to build on Durable Objects and draws upon Cloudflare's experience building products/features on Durable Objects.</p>
<p>The name &quot;actors&quot; originates from the <a href="/durable-objects/concepts/what-are-durable-objects/#actor-programming-model">actor programming model</a>, which closely ties to how Durable Objects are modelled.</p>
<p>The <code>@cloudflare/actors</code> library includes:</p>
<ul>
<li>Storage helpers for querying embeddeded, per-object SQLite storage</li>
<li>Storage helpers for managing SQL schema migrations</li>
<li>Alarm helpers for scheduling multiple alarms provided a date, delay in seconds, or cron expression</li>
<li><code>Actor</code> class for using Durable Objects with a defined pattern</li>
<li>Durable Objects <a href="https://developers.cloudflare.com/durable-objects/api/base/">Workers API</a> is always available for your application as needed</li>
</ul>
<p>Storage and alarm helper methods can be combined with <a href="https://github.com/cloudflare/actors?tab=readme-ov-file#storage--alarms-with-durableobject-class">any Javascript class</a> that defines your Durable Object, i.e, ones that extend <code>DurableObject</code> including the <code>Actor</code> class.</p>
<pre tabindex="0"><code class="language-js">import { Storage } from &quot;@cloudflare/actors/storage&quot;;&#10;&#10;export class ChatRoom extends DurableObject&lt;Env&gt; {&#10;    storage: Storage;&#10;&#10;    constructor(ctx: DurableObjectState, env: Env) {&#10;        super(ctx, env)&#10;        this.storage = new Storage(ctx.storage);&#10;        this.storage.migrations = [{&#10;            idMonotonicInc: 1,&#10;            description: &quot;Create users table&quot;,&#10;            sql: &quot;CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY)&quot;&#10;        }]&#10;    }&#10;    async fetch(request: Request): Promise&lt;Response&gt; {&#10;        // Run migrations before executing SQL query&#10;        await this.storage.runMigrations();&#10;&#10;        // Query with SQL template&#10;        let userId = new URL(request.url).searchParams.get(&quot;userId&quot;);&#10;        const query = this.storage.sql`SELECT * FROM users WHERE id = ${userId};`&#10;        return new Response(`${JSON.stringify(query)}`);&#10;    }&#10;}&#10;</code></pre>
<p><code>@cloudflare/actors</code> library introduces the <code>Actor</code> class pattern. <code>Actor</code> lets you access Durable Objects without writing the Worker that communicates with your Durable Object (the Worker is created for you). By default, requests are routed to a Durable Object named &quot;default&quot;.</p>
<pre tabindex="0"><code class="language-js">export class MyActor extends Actor&lt;Env&gt; {&#10;    async fetch(request: Request): Promise&lt;Response&gt; {&#10;        return new Response(&#x27;Hello, World!&#x27;)&#10;    }&#10;}&#10;&#10;export default handler(MyActor);&#10;</code></pre>
<p>You can <a href="/durable-objects/get-started/#3-instantiate-and-communicate-with-a-durable-object">route</a> to different Durable Objects by name within your <code>Actor</code> class using <a href="https://github.com/cloudflare/actors?tab=readme-ov-file#actor-with-custom-name"><code>nameFromRequest</code></a>.</p>
<pre tabindex="0"><code class="language-js">export class MyActor extends Actor&lt;Env&gt; {&#10;    static nameFromRequest(request: Request): string {&#10;        let url = new URL(request.url);&#10;        return url.searchParams.get(&quot;userId&quot;) ?? &quot;foo&quot;;&#10;    }&#10;&#10;    async fetch(request: Request): Promise&lt;Response&gt; {&#10;        return new Response(`Actor identifier (Durable Object name): ${this.identifier}`);&#10;    }&#10;}&#10;&#10;export default handler(MyActor);&#10;</code></pre>
<p>For more examples, check out the library <a href="https://github.com/cloudflare/actors?tab=readme-ov-file#getting-started">README</a>. <code>@cloudflare/actors</code> library is a place for more helpers and built-in patterns, like retry handling and Websocket-based applications, to reduce development overhead for common Durable Objects functionality. Please share feedback and what more you would like to see on our <a href="https://discord.com/channels/595317990191398933/773219443911819284">Discord channel</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 2</span><a class="pagination-next" rel="next" href="/changelog/product/durable-objects/2/">Next</a></nav>
