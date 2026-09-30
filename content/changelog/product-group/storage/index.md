---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/storage/
  description: '2026-09-17'
  full_title: Storage changelog | Cloudflare Docs
  head_html: <title>Storage changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-17"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/storage/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Storage changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-17"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/storage/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/storage/#page","headline":"Storage changelog | Cloudflare Docs","description":"2026-09-17","url":"https://developers.cloudflare.com/changelog/product-group/storage/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/storage/
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


<h2 id="hyperdrive-support-for-python-workers"><a href="/changelog/post/2026-09-16-hyperdrive-python-workers/">Hyperdrive support for Python Workers</a></h2>
<p><em>2026-09-16</em></p>
<p><a href="/workers/languages/python/">Python Workers</a> can now connect to PostgreSQL and MySQL through Hyperdrive.</p>
<p>For setup, code examples, and limitations, refer to <a href="/hyperdrive/examples/python-workers/">Use Hyperdrive from Python Workers</a>.</p>


<h2 id="r2-data-catalog-adds-table-maintenance-visibility-and-manual-queueing"><a href="/changelog/post/2026-09-16-table-maintenance-dashboard/">R2 Data Catalog adds table maintenance visibility and manual queueing</a></h2>
<p><em>2026-09-16</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a> now provides table-level maintenance visibility and manual compaction queueing in the Cloudflare dashboard. These updates make it easier to understand when maintenance is eligible to run, inspect completed operations, and request maintenance without leaving the table view.</p>
<p>To view table maintenance details:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17742.md")</div>
<p><img src="/assets/upstream/images/r2-data-catalog/table-maintenance-view.png" alt="Maintenance tab for an R2 Data Catalog table showing schedules and recent runs" /></p>
<p>The updated dashboard includes:</p>
<ul>
<li><strong>Maintenance tab</strong> — View compaction and snapshot expiration settings, schedules, and next eligibility alongside the table's <strong>Schema</strong> and <strong>Metadata</strong> tabs.</li>
<li><strong>Recent runs</strong> — Review a paginated audit log with job status, duration, and expandable details for manifest rewrites, compaction, and snapshot expiration. Expanded rows include operation metrics for each maintenance operation.</li>
<li><strong>Manual queueing</strong> — Select <strong>Queue maintenance</strong> to request compaction during normal scheduler polling. The dashboard checks permissions and explains when another maintenance job conflicts with the request or the daily accepted-request limit has been reached.</li>
<li><strong>Updated catalog layout</strong> — Find catalog metrics in the <strong>Metrics</strong> tab, use the renamed <strong>Explorer</strong> tab to browse data, and switch between table details using tabs instead of a scroll-to-section sidebar.</li>
<li><strong>Improved schema browser</strong> — For accounts with the schema browser enabled, select a namespace to open its tables in the right pane while also expanding the namespace tree. The tree can now be collapsed to provide more space for table details.</li>
</ul>
<p>For more information about compaction and snapshot expiration, refer to <a href="/r2-data-catalog/table-maintenance/">Table maintenance</a>.</p>


<h2 id="r2-data-access-logs"><a href="/changelog/post/2026-09-04-r2-data-access-logs/">R2 Data Access Logs</a></h2>
<p><em>2026-09-04</em></p>
<p>R2 Data Access Logs are now generally available. Turn on logging for a bucket to record object read, write, list, multipart upload, and delete operations with response status codes below <code>400</code>.</p>
<p>Data Access Logs cover requests made through the S3-compatible API, Cloudflare API and dashboard, Workers bindings, and public buckets through <code>r2.dev</code> or custom domains. Events are available in Workers Observability, where you can filter by bucket, operation, interface, actor, and other request fields.</p>
<p>Log delivery is asynchronous and best effort. Events may be delayed or omitted, so do not rely on Data Access Logs as a complete record of bucket activity.</p>
<p>Data Access Logs are available for non-jurisdictional buckets. For setup instructions, supported operations, and the event field reference, refer to <a href="/r2/buckets/data-access-logs/">R2 Data Access Logs</a>.</p>


<h2 id="d1-enforces-free-tier-daily-query-limits"><a href="/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/">D1 enforces free tier daily query limits</a></h2>
<p><em>2026-09-01</em></p>
<p>Beginning September 1, 2026, D1 queries on the <a href="/workers/platform/pricing/#workers">Workers Free plan</a> will fail when an account exceeds the daily <a href="/d1/platform/pricing/">row read or row write limits</a>. Queries via the <a href="/d1/worker-api/">Workers Binding API</a> and the <a href="/d1/rest-api/">REST API</a> will return errors until the limit resets at midnight UTC. Stored data is not affected.</p>
<p>You will receive email alerts when the daily limit is reached. The following errors indicate that a limit has been exceeded:</p>
<table>
<thead>
<tr>
<th>Error</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Your account has exceeded D1's free tier daily row read limit. Upgrade to a paid plan or wait until tomorrow (midnight UTC) to continue.</td>
<td>The account has reached its daily row read limit.</td>
</tr>
<tr>
<td>Your account has exceeded D1's free tier daily row write limit. Upgrade to a paid plan or wait until tomorrow (midnight UTC) to continue.</td>
<td>The account has reached its daily row write limit.</td>
</tr>
</tbody>
</table>
<p>Inspect database query activity before the enforcement date to identify queries that may exceed these limits. To reduce row reads, add <a href="/d1/best-practices/use-indexes/">indexes</a> to tables and review queries that perform full table scans. If usage requires higher limits after optimization, upgrade to a <a href="/workers/platform/pricing/#workers">Workers Paid plan</a>.</p>
<p>For more information on D1 errors and how to handle them, refer to the <a href="/d1/observability/debug-d1/#error-list">D1 error list</a>.</p>


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


<h2 id="new-us-jurisdiction-for-r2"><a href="/changelog/post/2026-08-17-r2-us-jurisdiction/">New `us` jurisdiction for R2</a></h2>
<p><em>2026-08-17</em></p>
<p>R2 now supports a <code>us</code> <a href="/r2/reference/data-location/#jurisdictional-restrictions">jurisdiction</a>, which guarantees that bucket data is stored and processed within the United States. Use this jurisdiction when you need explicit US data residency guarantees.</p>
<p>Use the jurisdiction-specific S3 endpoint to create and access buckets in the <code>us</code> jurisdiction:</p>
<p><code>https://&lt;ACCOUNT_ID&gt;.us.r2.cloudflarestorage.com</code></p>
<p>To access a bucket in the <code>us</code> jurisdiction from Workers, set <code>jurisdiction</code> in your R2 binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17741.md")</div>
<p>Once an R2 bucket is created, its jurisdiction cannot be changed.</p>
<p>For setup instructions and the full list of supported jurisdictions, refer to <a href="/r2/reference/data-location/#jurisdictional-restrictions">R2 data location</a>.</p>


<h2 id="mysql-support-in-hyperdrive-is-now-generally-available"><a href="/changelog/post/2026-08-07-hyperdrive-mysql-ga/">MySQL support in Hyperdrive is now generally available</a></h2>
<p><em>2026-08-07</em></p>
<p>Support for MySQL in Hyperdrive is now generally available. You can connect to any MySQL database from your Workers using Hyperdrive.</p>
<p>Hyperdrive makes your regional, MySQL databases fast when connecting from Cloudflare Workers. It eliminates unnecessary network roundtrips during connection setup, pools database connections globally, and can cache query results to provide the fastest possible response times.</p>
<p>You can connect using your existing drivers, ORMs, and query builders with Hyperdrive's secure credentials, with no code changes required. MySQL support is available at the same <a href="/hyperdrive/platform/pricing/">pricing</a> as Postgres.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17733.md")</div>
<p>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">how Hyperdrive works</a> and <a href="/hyperdrive/get-started/">get started building Workers that connect to MySQL with Hyperdrive</a>.</p>


<h2 id="restart-a-hyperdrive-configuration-from-the-dashboard"><a href="/changelog/post/2026-08-07-hyperdrive-restart-configuration-dashboard/">Restart a Hyperdrive configuration from the dashboard</a></h2>
<p><em>2026-08-07</em></p>
<p>You can now restart a Hyperdrive configuration from the Cloudflare dashboard. Restarting drains the connection pool and forces Hyperdrive to establish new connections to your origin database.</p>
<p>Restarting is a break-glass action. Hyperdrive automatically detects and recovers from most database failovers. Use a manual restart only when you need to force the pool to drain immediately.</p>
<p>To restart, select your Hyperdrive configuration in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>, go to the <strong>Settings</strong> tab, and select <strong>Restart</strong> under <strong>Danger zone</strong>. Restarting requires the <a href="/fundamentals/manage-members/roles/"><strong>Hyperdrive Admin</strong> role</a>. After a restart, the <strong>Settings</strong> tab shows when the configuration was last manually restarted.</p>
<p><img src="/assets/upstream/images/hyperdrive/dashboard-restart-danger-zone.png" alt="The Danger zone section of the Hyperdrive Settings tab, showing the Restart and Delete actions." /></p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17734.md")</aside>
<p>For more information, refer to <a href="/hyperdrive/concepts/connection-pooling/">Connection pooling</a>.</p>


<h2 id="vectorize-indexes-now-support-up-to-20-million-vectors"><a href="/changelog/post/2026-08-04-index-capacity-20-million/">Vectorize indexes now support up to 20 million vectors</a></h2>
<p><em>2026-08-04</em></p>
<p>You can now store up to 20 million vectors in a single Vectorize index, doubling the previous limit of 10 million vectors. This enables larger-scale semantic search, recommendation systems, and retrieval-augmented generation (RAG) applications without splitting data across multiple indexes.</p>
<p>Vectorize continues to support indexes with up to 1,536 dimensions per vector at 32-bit precision. Refer to the <a href="/vectorize/platform/limits/">Vectorize limits documentation</a> for complete details.</p>


<h2 id="billing-is-now-enabled-for-r2-data-catalog"><a href="/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/">Billing is now enabled for R2 Data Catalog</a></h2>
<p><em>2026-08-03</em></p>
<p>Billing is now enabled for <a href="/r2-data-catalog/">R2 Data Catalog</a> on non-enterprise accounts. R2 Data Catalog usage beyond the included free tier will appear on your next invoice.</p>
<p>R2 Data Catalog charges based on two dimensions, in addition to standard <a href="/r2/pricing/">R2 storage and operations</a>:</p>
<ul>
<li><strong>Catalog operations</strong>: $9.00 / million operations for metadata requests such as creating tables, reading table metadata, and updating table properties.</li>
<li><strong>Compaction</strong>: $0.005 / GB processed and $2.00 / million objects processed. These charges only apply when <a href="/r2-data-catalog/table-maintenance/">automatic compaction</a> is turned on for a table.</li>
</ul>
<p>Each dimension includes a monthly free tier: 1 million catalog operations, 10 GB of compaction data processed, and 1 million compaction objects processed.</p>
<p>For example, a single Iceberg table with 50 GB of data, 500,000 catalog operations per month, and compaction turned on that processes 20 GB across 200,000 files would be billed as follows:</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Usage</th>
<th>Included</th>
<th>Billable</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>Catalog operations</td>
<td>500,000</td>
<td>1,000,000</td>
<td>0</td>
<td>$0.00</td>
</tr>
<tr>
<td>Compaction (data processed)</td>
<td>20 GB</td>
<td>10 GB</td>
<td>10 GB</td>
<td>$0.05</td>
</tr>
<tr>
<td>Compaction (objects)</td>
<td>200,000</td>
<td>1,000,000</td>
<td>0</td>
<td>$0.00</td>
</tr>
<tr>
<td><strong>Total (Data Catalog)</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$0.05</strong></td>
</tr>
</tbody>
</table>
<p>Standard R2 storage charges ($0.015 / GB-month) apply separately for the 50 GB of data stored.</p>
<p>For full pricing details and billing examples, refer to <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog pricing</a>.</p>


<h2 id="inspect-worker-startup-performance-with-wrangler"><a href="/changelog/post/2026-07-31-wrangler-startup-profile-summary/">Inspect Worker startup performance with Wrangler</a></h2>
<p><em>2026-07-31</em></p>
<p><code>wrangler check startup</code> now reports your Worker's raw and compressed bundle sizes. It also summarizes local CPU activity during startup directly in your terminal.</p>
<p>Large bundles and costly startup work can introduce cold-start latency, so use this command to find code and large dependencies that slow your Worker before it handles requests.</p>
<p>The summary includes sampled, active, garbage collection, and idle time. Wrangler continues to save a <code>.cpuprofile</code> file for detailed flamegraph analysis in Chrome DevTools or VS Code.</p>
<pre tabindex="0"><code class="language-bash">⛅️ wrangler 4.116.0&#10;───────────────────────────────────────────────&#10;├ Building your Worker&#10;│ Worker Built! 🎉&#10;│&#10;├ Analysing&#10;│ Startup phase analysed&#10;│&#10;│ Bundle: 7171.25 KiB / gzip: 2197.00 KiB&#10;│&#10;│ Local startup profile:&#10;│   Profile window: 70.3 ms&#10;│   Sampled time: 70.3 ms&#10;│   Active: 38.5 ms (including 3.7 ms garbage collection)&#10;│   Idle: 31.8 ms&#10;│   Samples: 36&#10;│&#10;│ CPU Profile has been written to worker-startup.cpuprofile. Load it into the Chrome DevTools profiler (or directly in VSCode) to view a flamegraph.&#10;│&#10;│ Note that the CPU Profile was measured on your Worker running locally on your machine, which has a different CPU than when your Worker runs on Cloudflare.&#10;│&#10;│ As such, CPU Profile can be used to understand where time is spent at startup, but the overall startup time in the profile should not be expected to exactly match what your Worker&#x27;s startup time will be when deploying to Cloudflare.&#10;</code></pre>
<p>The profile runs locally, so its duration will differ from startup time on Cloudflare. For authoritative startup time, deploy your Worker or upload a version.</p>
<p>Available in Wrangler version 4.116.0 or later. For more information, refer to <a href="/workers/wrangler/commands/workers/#startup"><code>wrangler check startup</code></a>.</p>


<h2 id="sippy-now-supports-azure-blob-storage-and-s3-compatible-storage-providers"><a href="/changelog/post/2026-07-24-r2-sippy-azure-s3-compatible-support/">Sippy now supports Azure Blob Storage and S3-compatible storage providers</a></h2>
<p><em>2026-07-24</em></p>
<p><a href="/r2/data-migration/sippy/">Sippy</a> can now incrementally migrate data from Azure Blob Storage and any S3-compatible object storage provider to <a href="/r2/">Cloudflare R2</a>, in addition to Amazon S3 and Google Cloud Storage. Sippy copies objects to R2 as your application requests them, so you can start serving data from R2 without first moving your entire dataset or paying migration-specific egress fees.</p>
<h4 id="2026-07-24-r2-sippy-azure-s3-compatible-support-enable-sippy">Enable Sippy</h4>
<p>Run the following command and follow the prompts to select and configure your source storage provider:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket sippy enable &lt;BUCKET_NAME&gt;&#10;</code></pre>
<p>For Azure Blob Storage, provide your storage account name, container name, and either an account key or a shared access signature (SAS) token with read and list permissions. For an S3-compatible provider, provide the S3 API endpoint URL and read-only Access Key ID and Secret Access Key.</p>
<p><img src="/assets/upstream/images/r2/sippy-azure-source-configuration.png" alt="Azure Blob Storage source configuration in the R2 dashboard" /></p>
<p>After you enable Sippy, requests for objects that are not yet in R2 are served from your source bucket and copied to R2. Subsequent requests for those objects are served from R2.</p>
<p>For setup instructions and credential requirements, refer to the <a href="/r2/data-migration/sippy/">Sippy documentation</a>.</p>


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


<h2 id="subscribe-to-email-sending-events-with-queues"><a href="/changelog/post/2026-07-15-event-subscriptions/">Subscribe to Email Sending events with Queues</a></h2>
<p><em>2026-07-15</em></p>
<p>You can now subscribe to <strong><a href="/email-service/api/send-emails/">Email Sending</a> events</strong> through <a href="/queues/event-subscriptions/">Queues event subscriptions</a> and receive outbound transactional email lifecycle events on a queue. Each subscription is scoped to one sending domain — either the zone apex, such as <code>example.com</code>, or a verified sending subdomain, such as <code>send.example.com</code>.</p>
<p>Six event types are published: <code>message.delivered</code>, <code>message.deferred</code>, <code>message.bounced</code>, <code>message.failed</code>, <code>message.rejected</code>, and <code>message.complained</code>. Use them to track deliverability, react to bounces and complaints, and drive suppression or retry logic. Email Routing events are not published on this source.</p>
<p>Each event includes the message details, delivery status, and SMTP response:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;type&quot;: &quot;cf.email.sending.message.delivered&quot;,&#10;	&quot;source&quot;: {&#10;		&quot;type&quot;: &quot;email.sending&quot;,&#10;		&quot;zoneId&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353&quot;,&#10;		&quot;domain&quot;: &quot;example.com&quot;&#10;	},&#10;	&quot;payload&quot;: {&#10;		&quot;messageId&quot;: &quot;0101018f7d0c4d9a-msg-deadbeef&quot;,&#10;		&quot;recipient&quot;: &quot;user@example.net&quot;,&#10;		&quot;terminal&quot;: true,&#10;		&quot;delivery&quot;: {&#10;			&quot;status&quot;: &quot;delivered&quot;,&#10;			&quot;smtpStatusCode&quot;: &quot;250&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Refer to <a href="/email-service/platform/event-subscriptions/">Event subscriptions</a> to see all event types and example payloads.</p>


<h2 id="deprecate-legacy-workers-kv-namespace-api-routes"><a href="/changelog/post/2026-07-15-kv-legacy-namespace-routes-deprecation/">Deprecate legacy Workers KV namespace API routes</a></h2>
<p><em>2026-07-15</em></p>
<p>The legacy Workers KV API routes under <code>/accounts/{account_id}/workers/namespaces/*</code> are deprecated as of July 15, 2026, and will stop working on October 15, 2026. Migrate to the documented <a href="/api/resources/kv/">Workers KV API</a> routes under <code>/accounts/{account_id}/storage/kv/namespaces/*</code> before that date.</p>
<p>The legacy and replacement routes are interchangeable. They accept the same request parameters and return the same response payloads. To migrate, update the URL path from <code>/workers/namespaces/</code> to <code>/storage/kv/namespaces/</code>.</p>
<h4 id="2026-07-15-kv-legacy-namespace-routes-deprecation-what-you-need-to-do">What you need to do</h4>
<p>Update any integration that calls a route under <code>/accounts/{account_id}/workers/namespaces/</code> to use the equivalent route under <code>/accounts/{account_id}/storage/kv/namespaces/</code>. The migration is a direct URL path substitution — request parameters and response payloads are identical:</p>
<ul>
<li><code>GET</code> and <code>POST /accounts/{account_id}/workers/namespaces</code> → <code>GET</code> and <code>POST /accounts/{account_id}/storage/kv/namespaces</code></li>
<li><code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/workers/namespaces/{namespace_id}</code> → <code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}</code></li>
<li><code>GET /accounts/{account_id}/workers/namespaces/{namespace_id}/keys</code> → <code>GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys</code></li>
<li><code>GET /accounts/{account_id}/workers/namespaces/{namespace_id}/metadata/{key_name}</code> → <code>GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}</code></li>
<li><code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/workers/namespaces/{namespace_id}/values/{key_name}</code> → <code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}</code></li>
</ul>
<p>For more information about the deprecation timeline, refer to <a href="/fundamentals/api/reference/deprecations/">API deprecations</a>.</p>


<h2 id="r2-data-catalog-now-supports-read-only-api-tokens"><a href="/changelog/post/2026-07-09-r2-data-catalog-read-only-tokens/">R2 Data Catalog now supports read-only API tokens</a></h2>
<p><em>2026-07-13</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a> now accepts read-only API tokens, so query engines and clients that only read data no longer need a read-write token. Previously, every catalog operation required an <strong>Admin Read &amp; Write</strong> token, which granted read-only clients more access than they needed.</p>
<p>You can now authenticate your Iceberg engine based on your workload:</p>
<ul>
<li><strong>Read-only</strong> operations (such as listing namespaces, loading tables, and querying data) work with an <strong>Admin Read only</strong> token (R2 Data Catalog read and R2 storage read).</li>
<li><strong>Write</strong> operations (such as creating or dropping tables and committing transactions) continue to require an <strong>Admin Read &amp; Write</strong> token.</li>
</ul>
<p>This lets you follow the principle of least privilege — for example, using a read-write token for the pipeline that writes to your tables and read-only tokens for engines like <a href="/r2-sql/">R2 SQL</a>, <a href="/r2-data-catalog/config-examples/duckdb/">DuckDB</a>, or <a href="/r2-data-catalog/config-examples/pyiceberg/">PyIceberg</a> that query them.</p>
<p>Note that credentials vended by the catalog inherit the R2 storage permissions of the token used to authenticate. To ensure read-only access to your underlying data, scope the R2 storage permission to read-only as well.</p>
<p>For details on choosing and creating the right token, refer to <a href="/r2-data-catalog/manage-catalogs/#authenticate-your-iceberg-engine">Authenticate your Iceberg engine</a>.</p>


<h2 id="r2-data-catalog-compaction-now-optimizes-manifest-files"><a href="/changelog/post/2026-07-13-r2-data-catalog-manifest-optimization/">R2 Data Catalog compaction now optimizes manifest files</a></h2>
<p><em>2026-07-13</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a>, a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> catalog built into R2, now automatically optimizes manifest files as part of <a href="/r2-data-catalog/table-maintenance/">compaction</a>.</p>
<p>Manifest files track the data files that make up an Iceberg table. As a table accumulates many small or fragmented manifests, query engines must read more metadata during query planning, which slows down queries even before any data is scanned.</p>
<p>When compaction runs, R2 Data Catalog now rewrites and clusters manifest files by partition as a best-effort pre-step. This consolidates fragmented manifests, reduces the number of manifests a query engine must open, and lowers metadata I/O overhead. Tables that are already well-clustered are skipped, so the operation only runs when it provides a benefit.</p>
<p>This happens automatically for tables with compaction enabled — no configuration changes are required.</p>
<p>For more information, refer to <a href="/r2-data-catalog/table-maintenance/">Table maintenance</a>.</p>


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


<h2 id="r2-data-catalog-warns-before-you-delete-data-manually"><a href="/changelog/post/2026-07-06-r2-data-catalog-delete-warnings/">R2 Data Catalog warns before you delete data manually</a></h2>
<p><em>2026-07-07</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a> is a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> catalog built directly into your R2 bucket. Iceberg tracks your data through a tree of metadata files, so every insert, update, and delete must go through a catalog transaction. Manually adding, modifying, or deleting objects outside the catalog can leave pointers referencing files that no longer exist, corrupting the table into an inconsistent state that is difficult to recover from.</p>
<p>To help prevent this, the R2 dashboard and Wrangler now warn you when you attempt a manual delete operation on a Data Catalog-enabled bucket.</p>
<h4 id="2026-07-06-r2-data-catalog-delete-warnings-dashboard">Dashboard</h4>
<p>When you try to delete objects from a bucket that has R2 Data Catalog enabled, the dashboard displays a warning explaining that the operation could leave the catalog in an invalid state, with a link to the documentation for deleting data correctly. You can cancel the operation or choose to proceed anyway.</p>
<p><img src="/assets/upstream/images/r2-data-catalog/data-catalog-delete-warning.png" alt="R2 dashboard warning shown before deleting objects from a Data Catalog-enabled bucket" /></p>
<h4 id="2026-07-06-r2-data-catalog-delete-warnings-wrangler">Wrangler</h4>
<p>Wrangler now checks whether a bucket is Data Catalog-enabled before running a delete and warns you before continuing:</p>
<pre tabindex="0"><code class="language-txt">Data Catalog is enabled for this bucket. &#10;Proceeding may leave the data catalog in an invalid state. Continue?&#10;</code></pre>
<p>To learn how to safely manage and delete data in your tables, refer to the <a href="/r2-data-catalog/">R2 Data Catalog documentation</a>.</p>


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


<h2 id="reduced-end-to-end-latency-for-vector-changes"><a href="/changelog/post/2026-06-30-improved-wal-throughput/">Reduced end-to-end latency for vector changes</a></h2>
<p><em>2026-07-01</em></p>
<p>We have greatly improved the throughput of the Vectorize <a href="https://blog.cloudflare.com/building-vectorize-a-distributed-vector-database-on-cloudflare-developer-platform/#the-wal">write-ahead log (WAL)</a>. As a result, we have significantly reduced the end-to-end latency for a vector change to become queryable: median latency has dropped from 2 minutes to under 30 seconds, and p99 latency from 5 minutes to under 2 minutes.</p>
<p><img src="/assets/upstream/images/vectorize/vectorize-p99-wal-batch-end-to-end-latency-improvement.png" alt="Vectorize p99 WAL batch end-to-end latency improved" /></p>
<p>This means inserts, upserts, and deletes are reflected in query results faster, improving the freshness of semantic search, recommendation, and retrieval-augmented generation (RAG) workloads. You do not need to change your code or configuration to benefit from this improvement.</p>
<p>For more information, refer to the <a href="/vectorize/">Vectorize documentation</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 5</span><a class="pagination-next" rel="next" href="/changelog/product-group/storage/2/">Next</a></nav>
