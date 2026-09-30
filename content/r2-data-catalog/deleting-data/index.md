<p>Deleting data from R2 Data Catalog or any Apache Iceberg catalog requires that operations are done in a transaction through the catalog itself. Manually deleting metadata or data files directly can lead to data catalog corruption.</p>
<h2 id="automatic-table-maintenance">Automatic table maintenance</h2>
<p>R2 Data Catalog can automatically manage table maintenance operations such as snapshot expiration and compaction. These continuous operations help keep latency and storage costs down.</p>
<ul>
<li><strong>Snapshot expiration</strong>: Automatically removes old snapshots and the respective unreferenced data files. This reduces both metadata overhead and storage costs.</li>
<li><strong>Compaction</strong>: Merges small data files into larger ones. This optimizes read performance and reduces the number of files read during queries.</li>
</ul>
<p>Without enabling automatic maintenance, you need to manually handle these operations.</p>
<p>Learn more in the <a href="/r2-data-catalog/table-maintenance/">table maintenance</a> documentation.</p>
<h2 id="examples-of-enabling-automatic-table-maintenance-in-r2-data-catalog">Examples of enabling automatic table maintenance in R2 Data Catalog</h2>
<pre><code class="language-bash">&#35; Enable automatic snapshot expiration for entire catalog&#10;npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket \&#10;	&#45;-older-than-days 30 \&#10;	&#45;-retain-last 5&#10;&#10;&#35; Enable automatic compaction for entire catalog&#10;npx wrangler r2 bucket catalog compaction enable my-bucket \&#10;	&#45;-target-size 256&#10;</code></pre>
<p>Refer to additional examples in the <a href="/r2-data-catalog/manage-catalogs/">manage catalogs</a> documentation.</p>
<h2 id="manually-deleting-and-removing-data">Manually deleting and removing data</h2>
<p>You need to manually delete data for:</p>
<ul>
<li>Complying with data retention policies such as GDPR or CCPA.</li>
<li>Selective based deletes using conditional logic.</li>
<li>Removing stale or unreferenced files that R2 Data Catalog does not manage.</li>
</ul>
<p>The following are basic examples using PySpark but similar operations can be performed using other Iceberg-compatible engines. To configure PySpark, refer to our <a href="/r2-data-catalog/config-examples/spark-python/">example</a> or the official <a href="https://spark.apache.org/docs/latest/api/python/getting_started/index.html">PySpark documentation</a>.</p>
<h3 id="deleting-rows-from-a-table">Deleting rows from a table</h3>
<pre><code class="language-py">&#35; Creates new snapshots and marks old files for cleanup&#10;spark.sql(&quot;&quot;&quot;&#10;	DELETE FROM r2dc.namespace.table_name&#10;	WHERE column_name = &#x27;value&#x27;&#10;&quot;&quot;&quot;)&#10;&#10;&#35; The following is effectively a TRUNCATE operation&#10;spark.sql(&quot;DELETE FROM r2dc.namespace.table_name&quot;)&#10;&#10;&#35; For large deletes, use partitioned tables and delete entire partitions for faster performance:&#10;spark.sql(&quot;&quot;&quot;&#10;    DELETE FROM r2dc.namespace.table_name&#10;    WHERE date_partition &lt; &#x27;2024-01-01&#x27;&#10;&quot;&quot;&quot;)&#10;</code></pre>
<h3 id="dropping-tables-and-namespaces">Dropping tables and namespaces</h3>
<pre><code class="language-py">&#35; Removes table from catalog but keeps data files in R2 storage&#10;spark.sql(&quot;DROP TABLE r2dc.namespace.table_name&quot;)&#10;&#10;&#35; ⚠️  DANGER: Permanently deletes all data files from R2&#10;&#35; This operation cannot be undone&#10;spark.sql(&quot;DROP TABLE r2dc.namespace.table_name PURGE&quot;)&#10;&#10;&#35; Use CASCADE to drop all tables within the namespace&#10;spark.sql(&quot;DROP NAMESPACE r2dc.namespace_name CASCADE&quot;)&#10;&#10;&#35; You will need to PURGE the tables before running CASCADE to permanently delete data files&#10;&#35; This can be done with a loop over all tables in the namespace&#10;tables = spark.sql(&quot;SHOW TABLES IN r2dc.namespace_name&quot;).collect()&#10;for row in tables:&#10;    table_name = row[&#x27;tableName&#x27;]&#10;    spark.sql(f&quot;DROP TABLE r2dc.namespace_name.{table_name} PURGE&quot;)&#10;spark.sql(&quot;DROP NAMESPACE r2dc.namespace_name CASCADE&quot;)&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="data-loss-warning">Data loss warning</h3>
@markup("md", "content/.markup/bodies/570.md")
</aside>
<h3 id="manual-maintenance-operations">Manual maintenance operations</h3>
<pre><code class="language-py">&#35; Remove old metadata and data files marked for deletion&#10;&#35; The following retains the last 5 snapshots and deletes files older than Nov 28, 2024&#10;spark.sql(&quot;&quot;&quot;&#10;	CALL r2dc.system.expire_snapshots(&#10;    table =&gt; &#x27;r2dc.namespace_name.table_name&#x27;,&#10;    older_than =&gt; TIMESTAMP &#x27;2024-11-28 00:00:00&#x27;,&#10;     retain_last =&gt; 5&#10;  )&#10;&quot;&quot;&quot;)&#10;&#10;&#35; Removes unreferenced data files from R2 storage (orphan files)&#10;spark.sql(&quot;&quot;&quot;&#10;  CALL r2dc.system.remove_orphan_files(&#10;    table =&gt; &#x27;namespace.table_name&#x27;&#10;  )&#10;&quot;&quot;&quot;)&#10;&#10;&#35; Rewrite data files with a target file size (e.g., 512 MB)&#10;spark.sql(&quot;&quot;&quot;&#10;  CALL r2dc.system.rewrite_data_files(&#10;    table =&gt; &#x27;r2dc.namespace_name.table_name&#x27;,&#10;    options =&gt; map(&#x27;target-file-size-bytes&#x27;, &#x27;536870912&#x27;)&#10;  )&#10;&quot;&quot;&quot;)&#10;</code></pre>
<h2 id="about-apache-iceberg-metadata">About Apache Iceberg metadata</h2>
<p>Apache Iceberg uses a layered metadata structure to manage table data efficiently. Here are the key components and file structure:</p>
<ul>
<li><strong>metadata.json</strong>: Top-level JSON file pointing to the current snapshot</li>
<li><strong>snapshot-*</strong>: Immutable table state for a given point in time</li>
<li><strong>manifest-list-*.avro</strong>: An Avro file listing all manifest files for a given snapshot</li>
<li><strong>manifest-file-*.avro</strong>: An Avro file tracking data files and their statistics</li>
<li><strong>data-*.parquet</strong>: Parquet files containing actual table data</li>
<li><strong>Note</strong>: Unchanged manifest files are reused across snapshots</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/569.md")
</aside>
<pre class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/571.md")&#10;&#10;&#10;</pre>
<h3 id="what-happens-during-deletion">What happens during deletion</h3>
<p>Apache Iceberg supports two deletion modes: <strong>Copy-on-Write (COW)</strong> and <strong>Merge-on-Read (MOR)</strong>. Both create a new snapshot and mark old files for cleanup, but handle the deletion differently:</p>
<table>
<thead>
<tr>
<th>Aspect</th>
<th>Copy-on-Write (COW)</th>
<th>Merge-on-Read (MOR)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>How deletes work</strong></td>
<td>Rewrites data files without deleted rows</td>
<td>Creates delete files marking rows to skip</td>
</tr>
<tr>
<td><strong>Query performance</strong></td>
<td>Fast (no merge needed)</td>
<td>Slower (requires read-time merge)</td>
</tr>
<tr>
<td><strong>Write performance</strong></td>
<td>Slower (rewrites data files)</td>
<td>Fast (only writes delete markers)</td>
</tr>
<tr>
<td><strong>Storage impact</strong></td>
<td>Creates new data files immediately</td>
<td>Accumulates delete files over time</td>
</tr>
<tr>
<td><strong>Maintenance needs</strong></td>
<td>Snapshot expiration</td>
<td>Snapshot expiration + compaction (<code>rewrite_data_files</code>)</td>
</tr>
<tr>
<td><strong>Best for</strong></td>
<td>Read-heavy workloads</td>
<td>Write-heavy workloads with frequent small mutations</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="important-for-all-deletion-modes">Important for all deletion modes</h3>
@markup("md", "content/.markup/bodies/568.md")
</aside>
<h3 id="common-deletion-operations">Common deletion operations</h3>
<p>These operations work the same way for both COW and MOR tables:</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>What it does</th>
<th>Data deleted?</th>
<th>Reversible?</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>DELETE FROM</code></td>
<td>Removes rows matching condition</td>
<td>No (marked for cleanup)</td>
<td>Via time travel<sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td><code>DROP TABLE</code></td>
<td>Removes table from catalog</td>
<td>No</td>
<td>Yes (if data files exist)</td>
</tr>
<tr>
<td><code>DROP TABLE ... PURGE</code></td>
<td>Removes table and deletes data</td>
<td><strong>Yes</strong></td>
<td><strong>No</strong></td>
</tr>
<tr>
<td><code>expire_snapshots</code></td>
<td>Cleans up old snapshots/files</td>
<td><strong>Yes</strong></td>
<td><strong>No</strong></td>
</tr>
<tr>
<td><code>remove_orphan_files</code></td>
<td>Removes unreferenced files</td>
<td><strong>Yes</strong></td>
<td><strong>No</strong></td>
</tr>
</tbody>
</table>
<h3 id="mor-specific-operations">MOR-specific operations</h3>
<p>For Merge-on-Read tables, you may need to manually apply deletes for performance:</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>What it does</th>
<th>When to use</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>rewrite_data_files</code> (compaction)</td>
<td>Applies deletes and consolidates files</td>
<td>When query performance degrades due to many delete files</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/567.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/r2-data-catalog/table-maintenance/">Table maintenance</a> - Learn about automatic maintenance operations</li>
<li><a href="/r2-data-catalog/">R2 Data Catalog</a> - Overview and getting started guide</li>
<li><a href="/r2-sql/query-data">Query data</a> - Query tables with R2 SQL</li>
<li><a href="https://iceberg.apache.org/docs/latest/maintenance/">Apache Iceberg Maintenance</a> - Official Iceberg documentation on table maintenance</li>
</ul>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Time travel available until `expire_snapshots` is called</li></ol></section>
