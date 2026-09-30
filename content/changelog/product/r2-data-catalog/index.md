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


<h2 id="r2-data-catalog-snapshot-expiration-now-removes-unreferenced-data-files"><a href="/changelog/post/2026-04-22-snapshot-expiration-cleans-data-files/">R2 Data Catalog snapshot expiration now removes unreferenced data files</a></h2>
<p><em>2026-04-22</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a>, a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> catalog built into R2, now removes unreferenced data files during automatic snapshot expiration. This improvement reduces storage costs and eliminates the need to run manual maintenance jobs to reclaim space from deleted data.</p>
<p>Previously, snapshot expiration only cleaned up Iceberg metadata files such as manifests and manifest lists. Data files that were no longer referenced by active snapshots remained in R2 storage until you manually ran <code>remove_orphan_files</code> or <code>expire_snapshots</code> through an engine like Spark. This required extra operational overhead and left stale data files consuming storage.</p>
<p>Snapshot expiration now handles both metadata and data file cleanup automatically. When a snapshot is expired, any data files that are no longer referenced by retained snapshots are removed from R2 storage.</p>
<pre><code class="language-bash">&#35; Enable catalog-level snapshot expiration&#10;npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket \&#10;  &#45;-older-than-days 7 \&#10;  &#45;-retain-last 10&#10;</code></pre>
<p>For more information, refer to the <a href="/r2-data-catalog/table-maintenance/">table maintenance documentation</a>.</p>


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


<h2 id="r2-data-catalog-is-a-managed-apache-iceberg-data-catalog-built-directly-into-r2-buckets"><a href="/changelog/post/2025-04-10-r2-data-catalog-beta/">R2 Data Catalog is a managed Apache Iceberg data catalog built directly into R2 buckets</a></h2>
<p><em>2025-04-10</em></p>
<p>Today, we are launching <a href="/r2-data-catalog/">R2 Data Catalog</a> in open beta, a managed Apache Iceberg catalog built directly into your <a href="/r2/">Cloudflare R2</a> bucket.</p>
<p>If you are not already familiar with it, <a href="https://iceberg.apache.org/">Apache Iceberg</a> is an open table format designed to handle large-scale analytics datasets stored in object storage, offering ACID transactions and schema evolution. R2 Data Catalog exposes a standard Iceberg REST catalog interface, so you can connect engines like <a href="/r2-data-catalog/config-examples/spark-scala/">Spark</a>, <a href="/r2-data-catalog/config-examples/snowflake/">Snowflake</a>, and <a href="/r2-data-catalog/config-examples/pyiceberg/">PyIceberg</a> to start querying your tables using the tools you already know.</p>
<p>To enable a data catalog on your R2 bucket, find <strong>R2 Data Catalog</strong> in your buckets settings in the dashboard, or run:</p>
<pre><code class="language-bash">npx wrangler r2 bucket catalog enable my-bucket&#10;</code></pre>
<p>And that's it. You'll get a catalog URI and warehouse you can plug into your favorite Iceberg engines.</p>
<p>Visit our <a href="/r2-data-catalog/get-started/">getting started guide</a> for step-by-step instructions on enabling R2 Data Catalog, creating tables, and running your first queries.</p>



