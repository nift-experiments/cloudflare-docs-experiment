<h1 id="changelog">Changelog</h1>

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


<h2 id="sippy-now-supports-azure-blob-storage-and-s3-compatible-storage-providers"><a href="/changelog/post/2026-07-24-r2-sippy-azure-s3-compatible-support/">Sippy now supports Azure Blob Storage and S3-compatible storage providers</a></h2>
<p><em>2026-07-24</em></p>
<p><a href="/r2/data-migration/sippy/">Sippy</a> can now incrementally migrate data from Azure Blob Storage and any S3-compatible object storage provider to <a href="/r2/">Cloudflare R2</a>, in addition to Amazon S3 and Google Cloud Storage. Sippy copies objects to R2 as your application requests them, so you can start serving data from R2 without first moving your entire dataset or paying migration-specific egress fees.</p>
<h4 id="2026-07-24-r2-sippy-azure-s3-compatible-support-enable-sippy">Enable Sippy</h4>
<p>Run the following command and follow the prompts to select and configure your source storage provider:</p>
<pre><code class="language-sh">npx wrangler r2 bucket sippy enable &lt;BUCKET_NAME&gt;&#10;</code></pre>
<p>For Azure Blob Storage, provide your storage account name, container name, and either an account key or a shared access signature (SAS) token with read and list permissions. For an S3-compatible provider, provide the S3 API endpoint URL and read-only Access Key ID and Secret Access Key.</p>
<p><img src="/assets/upstream/images/r2/sippy-azure-source-configuration.png" alt="Azure Blob Storage source configuration in the R2 dashboard" /></p>
<p>After you enable Sippy, requests for objects that are not yet in R2 are served from your source bucket and copied to R2. Subsequent requests for those objects are served from R2.</p>
<p>For setup instructions and credential requirements, refer to the <a href="/r2/data-migration/sippy/">Sippy documentation</a>.</p>


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


<h2 id="r2-data-catalog-warns-before-you-delete-data-manually"><a href="/changelog/post/2026-07-06-r2-data-catalog-delete-warnings/">R2 Data Catalog warns before you delete data manually</a></h2>
<p><em>2026-07-07</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a> is a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> catalog built directly into your R2 bucket. Iceberg tracks your data through a tree of metadata files, so every insert, update, and delete must go through a catalog transaction. Manually adding, modifying, or deleting objects outside the catalog can leave pointers referencing files that no longer exist, corrupting the table into an inconsistent state that is difficult to recover from.</p>
<p>To help prevent this, the R2 dashboard and Wrangler now warn you when you attempt a manual delete operation on a Data Catalog-enabled bucket.</p>
<h4 id="2026-07-06-r2-data-catalog-delete-warnings-dashboard">Dashboard</h4>
<p>When you try to delete objects from a bucket that has R2 Data Catalog enabled, the dashboard displays a warning explaining that the operation could leave the catalog in an invalid state, with a link to the documentation for deleting data correctly. You can cancel the operation or choose to proceed anyway.</p>
<p><img src="/assets/upstream/images/r2-data-catalog/data-catalog-delete-warning.png" alt="R2 dashboard warning shown before deleting objects from a Data Catalog-enabled bucket" /></p>
<h4 id="2026-07-06-r2-data-catalog-delete-warnings-wrangler">Wrangler</h4>
<p>Wrangler now checks whether a bucket is Data Catalog-enabled before running a delete and warns you before continuing:</p>
<pre><code class="language-txt">Data Catalog is enabled for this bucket. &#10;Proceeding may leave the data catalog in an invalid state. Continue?&#10;</code></pre>
<p>To learn how to safely manage and delete data in your tables, refer to the <a href="/r2-data-catalog/">R2 Data Catalog documentation</a>.</p>


<h2 id="billable-usage-and-budget-alerts-now-in-product-sidebars"><a href="/changelog/post/2026-06-04-billable-usage-product-sidebar/">Billable usage and budget alerts now in product sidebars</a></h2>
<p><em>2026-06-04</em></p>
<p>Pay-as-you-go customers can now view billable usage and create <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">budget alerts</a> directly from the product overview pages for <a href="/workers/">Workers &amp; Pages</a>, <a href="/d1/">D1</a>, <a href="/r2/">R2</a>, <a href="/kv/">Workers KV</a>, <a href="/queues/">Queues</a>, <a href="/vectorize/">Vectorize</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/containers/">Containers</a>. A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.</p>
<p>The widget pulls from the same data as the <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Billable Usage dashboard</a> and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-06-04-billable-usage-product-sidebar.png" alt="Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service" /></p>
<p>Selecting <strong>Create budget alert</strong> opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.</p>
<p>For more information, refer to the <a href="/billing/">Usage-based billing documentation</a>.</p>


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


<h2 id="r2-data-catalog-snapshot-expiration-now-removes-unreferenced-data-files"><a href="/changelog/post/2026-04-22-snapshot-expiration-cleans-data-files/">R2 Data Catalog snapshot expiration now removes unreferenced data files</a></h2>
<p><em>2026-04-22</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a>, a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> catalog built into R2, now removes unreferenced data files during automatic snapshot expiration. This improvement reduces storage costs and eliminates the need to run manual maintenance jobs to reclaim space from deleted data.</p>
<p>Previously, snapshot expiration only cleaned up Iceberg metadata files such as manifests and manifest lists. Data files that were no longer referenced by active snapshots remained in R2 storage until you manually ran <code>remove_orphan_files</code> or <code>expire_snapshots</code> through an engine like Spark. This required extra operational overhead and left stale data files consuming storage.</p>
<p>Snapshot expiration now handles both metadata and data file cleanup automatically. When a snapshot is expired, any data files that are no longer referenced by retained snapshots are removed from R2 storage.</p>
<pre><code class="language-bash">&#35; Enable catalog-level snapshot expiration&#10;npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket \&#10;  &#45;-older-than-days 7 \&#10;  &#45;-retain-last 10&#10;</code></pre>
<p>For more information, refer to the <a href="/r2-data-catalog/table-maintenance/">table maintenance documentation</a>.</p>


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


<h2 id="improve-global-upload-performance-with-r2-local-uploads-now-in-open-beta"><a href="/changelog/post/2026-02-03-r2-local-uploads/">Improve Global Upload Performance with R2 Local Uploads - Now in Open Beta</a></h2>
<p><em>2026-02-03</em></p>
<p><a href="/r2/buckets/local-uploads/">Local Uploads</a> is now available in open beta. Enable it on your <a href="/r2/">R2</a> bucket to improve upload performance when clients upload data from a different region than your bucket. With Local Uploads enabled, object data is written to storage infrastructure near the client, then asynchronously replicated to your bucket. The object is immediately accessible and remains strongly consistent throughout. Refer to <a href="/r2/how-r2-works/">How R2 works</a> for details on how data is written to your bucket.</p>
<p>In our tests, we observed <strong>up to 75% reduction in Time to Last Byte (TTLB)</strong> for upload requests when Local Uploads is enabled.</p>
<p><img src="/assets/upstream/images/r2/local-uploads-latency.png" alt="Local Uploads latency comparison showing p50 TTLB dropping from around 2 seconds to 500ms after enabling Local Uploads" /></p>
<p>This feature is ideal when:</p>
<ul>
<li>Your users are globally distributed</li>
<li>Upload performance and reliability is critical to your application</li>
<li>You want to optimize write performance without changing your bucket's primary location</li>
</ul>
<p>To enable Local Uploads on your bucket, find <strong>Local Uploads</strong> in your bucket settings in the <a href="https://dash.cloudflare.com/?to=/:account/r2/overview">Cloudflare Dashboard</a>, or run:</p>
<pre><code class="language-sh">npx wrangler r2 bucket local-uploads enable &lt;BUCKET_NAME&gt;&#10;</code></pre>
<p>Enabling Local Uploads on a bucket is seamless: existing uploads will complete as expected and there’s no interruption to traffic. There is no additional cost to enable Local Uploads. Upload requests incur the standard <a href="/r2/pricing/">Class A operation costs</a> same as upload requests made without Local Uploads.</p>
<p>For more information, refer to <a href="/r2/buckets/local-uploads/">Local Uploads</a>.</p>


<h2 id="r2-data-catalog-now-supports-automatic-snapshot-expiration"><a href="/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/">R2 Data Catalog now supports automatic snapshot expiration</a></h2>
<p><em>2025-12-18</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a> now supports automatic snapshot expiration for Apache Iceberg tables.</p>
<p>In Apache Iceberg, a snapshot is metadata that represents the state of a table at a given point in time. Every mutation creates a new snapshot which enable powerful features like time travel queries and rollback capabilities but will accumulate over time.</p>
<p>Without regular cleanup, these accumulated snapshots can lead to:</p>
<ul>
<li>Metadata overhead</li>
<li>Slower table operations</li>
<li>Increased storage costs.</li>
</ul>
<p>Snapshot expiration in R2 Data Catalog automatically removes old table snapshots based on your configured retention policy, improving performance and storage costs.</p>
<pre><code class="language-bash">&#35; Enable catalog-level snapshot expiration&#10;&#35; Expire snapshots older than 7 days, always retain at least 10 recent snapshots&#10;npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket \&#10;  &#45;-older-than-days 7 \&#10;  &#45;-retain-last 10&#10;</code></pre>
<p>Snapshot expiration uses two parameters to determine which snapshots to remove:</p>
<ul>
<li><code>--older-than-days</code>: age threshold in days</li>
<li><code>--retain-last</code>: minimum snapshot count to retain</li>
</ul>
<p>Both conditions must be met before a snapshot is expired, ensuring you always retain recent snapshots even if they exceed the age threshold.</p>
<p>This feature complements <a href="/r2-data-catalog/table-maintenance/">automatic compaction</a>, which optimizes query performance by combining small data files into larger ones. Together, these automatic maintenance operations keep your Iceberg tables performant and cost-efficient without manual intervention.</p>
<p>For more information, refer to <a href="/r2-data-catalog/table-maintenance/">Table maintenance</a> or <a href="/r2-data-catalog/manage-catalogs/">Manage catalogs</a>.</p>


<h2 id="mount-r2-buckets-in-containers"><a href="/changelog/post/2025-11-21-fuse-support-in-containers/">Mount R2 buckets in Containers</a></h2>
<p><em>2025-11-21</em></p>
<p><a href="/containers/">Containers</a> now support mounting R2 buckets as FUSE (Filesystem in Userspace) volumes, allowing applications to interact with <a href="/r2/">R2</a> using standard filesystem operations.</p>
<p>Common use cases include:</p>
<ul>
<li>Bootstrapping containers with datasets, models, or dependencies for <a href="/sandbox/">sandboxes</a> and <a href="/agents/">agent</a> environments</li>
<li>Persisting user configuration or application state without managing downloads</li>
<li>Accessing large static files without bloating container images or downloading at startup</li>
</ul>
<p>FUSE adapters like <a href="https://github.com/tigrisdata/tigrisfs">tigrisfs</a>, <a href="https://github.com/s3fs-fuse/s3fs-fuse">s3fs</a>, and <a href="https://github.com/GoogleCloudPlatform/gcsfuse">gcsfuse</a> can be installed in your container image and configured to mount buckets at startup.</p>
<pre><code class="language-dockerfile">FROM alpine:3.20&#10;&#10;&#35; Install FUSE and dependencies&#10;RUN apk update &amp;&amp; \&#10;    apk add --no-cache ca-certificates fuse curl bash&#10;&#10;&#35; Install tigrisfs&#10;RUN ARCH=$(uname -m) &amp;&amp; \&#10;    if [ &quot;$ARCH&quot; = &quot;x86_64&quot; ]; then ARCH=&quot;amd64&quot;; fi &amp;&amp; \&#10;    if [ &quot;$ARCH&quot; = &quot;aarch64&quot; ]; then ARCH=&quot;arm64&quot;; fi &amp;&amp; \&#10;    VERSION=$(curl -s https://api.github.com/repos/tigrisdata/tigrisfs/releases/latest | grep -o &#x27;&quot;tag_name&quot;: &quot;[^&quot;]*&#x27; | cut -d&#x27;&quot;&#x27; -f4) &amp;&amp; \&#10;    curl -L &quot;https://github.com/tigrisdata/tigrisfs/releases/download/${VERSION}/tigrisfs_${VERSION#v}_linux_${ARCH}.tar.gz&quot; -o /tmp/tigrisfs.tar.gz &amp;&amp; \&#10;    tar -xzf /tmp/tigrisfs.tar.gz -C /usr/local/bin/ &amp;&amp; \&#10;    rm /tmp/tigrisfs.tar.gz &amp;&amp; \&#10;    chmod +x /usr/local/bin/tigrisfs&#10;&#10;&#35; Create startup script that mounts bucket&#10;RUN printf &#x27;#!/bin/sh\n\&#10;    set -e\n\&#10;    mkdir -p /mnt/r2\n\&#10;    R2_ENDPOINT=&quot;https://${R2_ACCOUNT_ID}.r2.cloudflarestorage.com&quot;\n\&#10;    /usr/local/bin/tigrisfs --endpoint &quot;${R2_ENDPOINT}&quot; -f &quot;${BUCKET_NAME}&quot; /mnt/r2 &amp;\n\&#10;    sleep 3\n\&#10;    ls -lah /mnt/r2\n\&#10;    &#x27; &gt; /startup.sh &amp;&amp; chmod +x /startup.sh&#10;&#10;CMD [&quot;/startup.sh&quot;]&#10;</code></pre>
<p>See the <a href="/containers/examples/r2-fuse-mount/">Mount R2 buckets with FUSE</a> example for a complete guide on mounting R2 buckets and/or other S3-compatible storage buckets within your containers.</p>


<h2 id="r2-data-catalog-table-level-compaction"><a href="/changelog/post/2025-10-06-data-catalog-table-compaction/">R2 Data Catalog table-level compaction</a></h2>
<p><em>2025-10-06</em></p>
<p>You can now enable compaction for individual <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables in <a href="/r2-data-catalog/">R2 Data Catalog</a>, giving you fine-grained control over different workloads.</p>
<pre><code class="language-bash">&#35; Enable compaction for a specific table (no token required)&#10;npx wrangler r2 bucket catalog compaction enable &lt;BUCKET&gt; &lt;NAMESPACE&gt; &lt;TABLE&gt; --target-size 256&#10;</code></pre>
<p>This allows you to:</p>
<ul>
<li>Apply different target file sizes per table</li>
<li>Disable compaction for specific tables</li>
<li>Optimize based on table-specific access patterns</li>
</ul>
<p>Learn more at <a href="/r2-data-catalog/manage-catalogs/">Manage catalogs</a>.</p>


<h2 id="r2-data-catalog-now-supports-compaction"><a href="/changelog/post/2025-09-25-data-catalog-compaction/">R2 Data Catalog now supports compaction</a></h2>
<p><em>2025-09-25</em></p>
<p>You can now enable automatic compaction for <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables in <a href="/r2-data-catalog/">R2 Data Catalog</a> to improve query performance.</p>
<p>Compaction is the process of taking a group of small files and combining them into fewer larger files. This is an important maintenance operation as it helps ensure that query performance remains consistent by reducing the number of files that needs to be scanned.</p>
<p>To enable automatic compaction in R2 Data Catalog, find it under <strong>R2 Data Catalog</strong> in your R2 bucket settings in the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/r2/compaction.png" alt="compaction-dash" /></p>
<p>Or with <a href="/workers/wrangler/">Wrangler</a>, run:</p>
<pre><code class="language-bash">npx wrangler r2 bucket catalog compaction enable &lt;BUCKET_NAME&gt;  --target-size 128 --token &lt;API_TOKEN&gt;&#10;</code></pre>
<p>To get started with compaction, check out <a href="/r2-data-catalog/manage-catalogs/">manage catalogs</a>. For best practices and limitations, refer to <a href="/r2-data-catalog/table-maintenance/">about compaction</a>.</p>


<h2 id="r2-dashboard-experience-gets-new-updates"><a href="/changelog/post/2025-05-01-r2-dashboard-updates/">R2 Dashboard experience gets new updates</a></h2>
<p><em>2025-05-01</em></p>
<p>We're excited to announce several improvements to the <a href="/r2/">Cloudflare R2</a> dashboard experience that make managing your object storage easier and more intuitive:</p>
<p><img src="/assets/upstream/images/r2/r2-dashboard-updates.png" alt="Cloudflare R2 Dashboard" /></p>
<h4 id="2025-05-01-r2-dashboard-updates-all-new-settings-page">All-new settings page</h4>
<p>We've redesigned the bucket settings page, giving you a centralized location to manage all your bucket configurations in one place.</p>
<h4 id="2025-05-01-r2-dashboard-updates-improved-navigation-and-sharing">Improved navigation and sharing</h4>
<ul>
<li>Deeplink support for prefix directories: Navigate through your bucket hierarchy without losing your state. Your browser's back button now works as expected, and you can share direct links to specific prefix directories with teammates.</li>
<li>Objects as clickable links: Objects are now proper links that you can copy or <code>CMD + Click</code> to open in a new tab.</li>
</ul>
<h4 id="2025-05-01-r2-dashboard-updates-clearer-public-access-controls">Clearer public access controls</h4>
<ul>
<li>Renamed &quot;r2.dev domain&quot; to &quot;Public Development URL&quot; for better clarity when exposing bucket contents for non-production workloads.</li>
<li>Public Access status now clearly displays &quot;Enabled&quot; when your bucket is exposed to the internet (via Public Development URL or Custom Domains).</li>
</ul>
<p>We've also made numerous other usability improvements across the board to make your R2 experience smoother and more productive.</p>


<h2 id="cloudflare-pipelines-now-available-in-beta"><a href="/changelog/post/2025-04-10-launching-pipelines/">Cloudflare Pipelines now available in beta</a></h2>
<p><em>2025-04-10</em></p>
<p><a href="/pipelines">Cloudflare Pipelines</a> is now available in beta, to all users with a <a href="/workers/platform/pricing">Workers Paid</a> plan.</p>
<p>Pipelines let you ingest high volumes of real time data, without managing the underlying infrastructure. A single pipeline can ingest up to 100 MB of data per second, via HTTP or from a <a href="/workers">Worker</a>. Ingested data is automatically batched, written to output files, and delivered to an <a href="/r2">R2 bucket</a> in your account. You can use Pipelines to build a data lake of clickstream data, or to store events from a Worker.</p>
<p>Create your first pipeline with a single command:</p>
<pre><code class="language-bash">$ npx wrangler@latest pipelines create my-clickstream-pipeline --r2-bucket my-bucket&#10;&#10;🌀 Authorizing R2 bucket &quot;my-bucket&quot;&#10;🌀 Creating pipeline named &quot;my-clickstream-pipeline&quot;&#10;✅ Successfully created pipeline my-clickstream-pipeline&#10;&#10;Id:    0e00c5ff09b34d018152af98d06f5a1xvc&#10;Name:  my-clickstream-pipeline&#10;Sources:&#10;  HTTP:&#10;    Endpoint:        https://0e00c5ff09b34d018152af98d06f5a1xvc.pipelines.cloudflare.com/&#10;    Authentication:  off&#10;    Format:          JSON&#10;  Worker:&#10;    Format:  JSON&#10;Destination:&#10;  Type:         R2&#10;  Bucket:       my-bucket&#10;  Format:       newline-delimited JSON&#10;  Compression:  GZIP&#10;Batch hints:&#10;  Max bytes:     100 MB&#10;  Max duration:  300 seconds&#10;  Max records:   100,000&#10;&#10;🎉 You can now send data to your pipeline!&#10;&#10;Send data to your pipeline&#x27;s HTTP endpoint:&#10;curl &quot;https://0e00c5ff09b34d018152af98d06f5a1xvc.pipelines.cloudflare.com/&quot; -d &#x27;[{ ...JSON_DATA... }]&#x27;&#10;&#10;To send data to your pipeline from a Worker, add the following configuration to your config file:&#10;{&#10;  &quot;pipelines&quot;: [&#10;    {&#10;      &quot;pipeline&quot;: &quot;my-clickstream-pipeline&quot;,&#10;      &quot;binding&quot;: &quot;PIPELINE&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>Head over to our <a href="/pipelines/getting-started">getting started guide</a> for an in-depth tutorial to building with Pipelines.</p>


<h2 id="r2-data-catalog-is-a-managed-apache-iceberg-data-catalog-built-directly-into-r2-buckets"><a href="/changelog/post/2025-04-10-r2-data-catalog-beta/">R2 Data Catalog is a managed Apache Iceberg data catalog built directly into R2 buckets</a></h2>
<p><em>2025-04-10</em></p>
<p>Today, we are launching <a href="/r2-data-catalog/">R2 Data Catalog</a> in open beta, a managed Apache Iceberg catalog built directly into your <a href="/r2/">Cloudflare R2</a> bucket.</p>
<p>If you are not already familiar with it, <a href="https://iceberg.apache.org/">Apache Iceberg</a> is an open table format designed to handle large-scale analytics datasets stored in object storage, offering ACID transactions and schema evolution. R2 Data Catalog exposes a standard Iceberg REST catalog interface, so you can connect engines like <a href="/r2-data-catalog/config-examples/spark-scala/">Spark</a>, <a href="/r2-data-catalog/config-examples/snowflake/">Snowflake</a>, and <a href="/r2-data-catalog/config-examples/pyiceberg/">PyIceberg</a> to start querying your tables using the tools you already know.</p>
<p>To enable a data catalog on your R2 bucket, find <strong>R2 Data Catalog</strong> in your buckets settings in the dashboard, or run:</p>
<pre><code class="language-bash">npx wrangler r2 bucket catalog enable my-bucket&#10;</code></pre>
<p>And that's it. You'll get a catalog URI and warehouse you can plug into your favorite Iceberg engines.</p>
<p>Visit our <a href="/r2-data-catalog/get-started/">getting started guide</a> for step-by-step instructions on enabling R2 Data Catalog, creating tables, and running your first queries.</p>


<h2 id="set-retention-polices-for-your-r2-bucket-with-bucket-locks"><a href="/changelog/post/2025-03-06-r2-bucket-locks/">Set retention polices for your R2 bucket with bucket locks</a></h2>
<p><em>2025-03-06</em></p>
<p>You can now use <a href="/r2/buckets/bucket-locks/">bucket locks</a> to set retention policies on your <a href="/r2/buckets/">R2 buckets</a> (or specific prefixes within your buckets) for a specified period — or indefinitely. This can help ensure compliance by protecting important data from accidental or malicious deletion.</p>
<p>Locks give you a few ways to ensure your objects are retained (not deleted or overwritten). You can:</p>
<ul>
<li>Lock objects for a specific duration, for example 90 days.</li>
<li>Lock objects until a certain date, for example January 1, 2030.</li>
<li>Lock objects indefinitely, until the lock is explicitly removed.</li>
</ul>
<p>Buckets can have up to 1,000 <a href="/r2/buckets/">bucket lock rules</a>. Each rule specifies which objects it covers (via prefix) and how long those objects must remain retained.</p>
<p>Here are a couple of examples showing how you can configure bucket lock rules using <a href="/workers/wrangler/">Wrangler</a>:</p>
<h4 id="2025-03-06-r2-bucket-locks-ensure-all-objects-in-a-bucket-are-retained-for-at-least-180-days">Ensure all objects in a bucket are retained for at least 180 days</h4>
<pre><code class="language-sh">npx wrangler r2 bucket lock add &lt;bucket&gt; --name 180-days-all --retention-days 180&#10;</code></pre>
<h4 id="2025-03-06-r2-bucket-locks-prevent-deletion-or-overwriting-of-all-logs-indefinitely-via-prefix">Prevent deletion or overwriting of all logs indefinitely (via prefix)</h4>
<pre><code class="language-sh">npx wrangler r2 bucket lock add &lt;bucket&gt; --name indefinite-logs --prefix logs/ --retention-indefinite&#10;</code></pre>
<p>For more information on bucket locks and how to set retention policies for objects in your R2 buckets, refer to our <a href="/r2/buckets/bucket-locks/">documentation</a>.</p>


<h2 id="super-slurper-now-supports-migrations-from-all-s3-compatible-storage-providers"><a href="/changelog/post/2025-02-24-r2-super-slurper-s3-compatible-support/">Super Slurper now supports migrations from all S3-compatible storage providers</a></h2>
<p><em>2025-02-24</em></p>
<p><a href="/r2/data-migration/super-slurper/">Super Slurper</a> can now migrate data from any S3-compatible object storage provider to <a href="/r2/">Cloudflare R2</a>. This includes transfers from services like MinIO, Wasabi, Backblaze B2, and DigitalOcean Spaces.</p>
<p><img src="/assets/upstream/images/changelog/r2/super-slurper-s3-compat-screenshot-border.png" alt="Super Slurper S3-Compatible Source" /></p>
<p>For more information on Super Slurper and how to migrate data from your existing S3-compatible storage buckets to R2, refer to our <a href="/r2/data-migration/super-slurper/">documentation</a>.</p>


<h2 id="super-slurper-now-transfers-data-to-r2-up-to-5x-faster"><a href="/changelog/post/2025-02-14-r2-super-slurper-faster-migrations/">Super Slurper now transfers data to R2 up to 5x faster</a></h2>
<p><em>2025-02-14</em></p>
<p><a href="/r2/data-migration/super-slurper/">Super Slurper</a> now transfers data from cloud object storage providers like AWS S3 and Google Cloud Storage to <a href="/r2/">Cloudflare R2</a> up to 5x faster than it did before.</p>
<p>We moved from a centralized service to a distributed system built on the Cloudflare Developer Platform — using <a href="/workers/">Cloudflare Workers</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/queues/">Queues</a> — to both improve performance and increase system concurrency capabilities (and we'll share more details about how we did it soon!)</p>
<p><img src="/assets/upstream/images/r2/slurper-objects-over-time-border.png" alt="Super Slurper Objects Migrated" /></p>
<p><em>Time to copy 75,000 objects from AWS S3 to R2 decreased from 15 minutes 30 seconds (old) to 3 minutes 25 seconds (after performance improvements)</em></p>
<p>For more information on Super Slurper and how to migrate data from existing object storage to R2, refer to our <a href="/r2/data-migration/super-slurper/">documentation</a>.</p>



