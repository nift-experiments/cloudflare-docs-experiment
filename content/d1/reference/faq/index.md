<h2 id="pricing">Pricing</h2>
<h3 id="will-d1-always-have-a-free-plan">Will D1 always have a Free plan?</h3>
<p>Yes, the <a href="/workers/platform/pricing/#workers">Workers Free plan</a> will always include the ability to prototype and experiment with D1 for free.</p>
<h3 id="what-happens-if-i-exceed-the-daily-limits-on-reads-and-writes-or-the-total-storage-limit-on-the-free-plan">What happens if I exceed the daily limits on reads and writes, or the total storage limit, on the Free plan?</h3>
<p>When your account hits the daily read and/or write limits, you will not be able to run queries against D1. D1 API will return errors to your client indicating that your daily limits have been exceeded. Once you have reached your included storage limit, you will need to delete unused databases or clean up stale data before you can insert new data, create or alter tables or create indexes and triggers.</p>
<p>Upgrading to the Workers Paid plan will remove these limits, typically within minutes.</p>
<h3 id="what-happens-if-i-exceed-the-monthly-included-reads-writes-and-or-storage-on-the-paid-tier">What happens if I exceed the monthly included reads, writes and/or storage on the paid tier?</h3>
<p>You will be billed for the additional reads, writes and storage according to <a href="/d1/platform/pricing/#billing-metrics">D1's pricing metrics</a>.</p>
<h3 id="how-can-i-estimate-my-eventual-bill">How can I estimate my (eventual) bill?</h3>
<p>Every query returns a <code>meta</code> object that contains a total count of the rows read (<code>rows_read</code>) and rows written (<code>rows_written</code>) by that query. For example, a query that performs a full table scan (for instance, <code>SELECT * FROM users</code>) from a table with 5000 rows would return a <code>rows_read</code> value of <code>5000</code>:</p>
<pre><code class="language-json">&quot;meta&quot;: {&#10;  &quot;duration&quot;: 0.20472300052642825,&#10;  &quot;size_after&quot;: 45137920,&#10;  &quot;rows_read&quot;: 5000,&#10;  &quot;rows_written&quot;: 0&#10;}&#10;</code></pre>
<p>These are also included in the D1 <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and the <a href="/d1/observability/metrics-analytics/">analytics API</a>, allowing you to attribute read and write volumes to specific databases, time periods, or both.</p>
<h3 id="does-d1-charge-for-data-transfer-egress">Does D1 charge for data transfer / egress?</h3>
<p>No.</p>
<h3 id="does-d1-charge-additional-for-additional-compute">Does D1 charge additional for additional compute?</h3>
<p>D1 itself does not charge for additional compute. Workers querying D1 and computing results: for example, serializing results into JSON and/or running queries, are billed per <a href="/workers/platform/pricing/#workers">Workers pricing</a>, in addition to your D1 specific usage.</p>
<h3 id="do-queries-i-run-from-the-dashboard-or-wrangler-the-cli-count-as-billable-usage">Do queries I run from the dashboard or Wrangler (the CLI) count as billable usage?</h3>
<p>Yes, any queries you run against your database, including inserting (<code>INSERT</code>) existing data into a new database, table scans (<code>SELECT * FROM table</code>), or creating indexes count as either reads or writes.</p>
<h3 id="can-i-use-an-index-to-reduce-the-number-of-rows-read-by-a-query">Can I use an index to reduce the number of rows read by a query?</h3>
<p>Yes, you can use an index to reduce the number of rows read by a query. <a href="/d1/best-practices/use-indexes/">Creating indexes</a> for your most queried tables and filtered columns reduces how much data is scanned and improves query performance at the same time. If you have a read-heavy workload (most common), this can be particularly advantageous. Writing to columns referenced in an index will add at least one (1) additional row written to account for updating the index, but this is typically offset by the reduction in rows read due to the benefits of an index.</p>
<h3 id="does-a-freshly-created-database-and-or-an-empty-table-with-no-rows-contribute-to-my-storage">Does a freshly created database, and/or an empty table with no rows, contribute to my storage?</h3>
<p>Yes, although minimal. An empty table consumes at least a few kilobytes, based on the number of columns (table width) in the table. An empty database consumes approximately 12 KB of storage.</p>
<h2 id="limits">Limits</h2>
<h3 id="how-much-work-can-a-d1-database-do">How much work can a D1 database do?</h3>
<p>D1 is designed for horizontal scale out across multiple, smaller (10 GB) databases, such as per-user, per-tenant or per-entity databases.
D1 allows you to build applications with thousands of databases at no extra cost, as the pricing is based only on query and storage costs.</p>
<h4 id="storage">Storage</h4>
<p>Each D1 database can store up to 10 GB of data.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7337.md")
</aside>
<h4 id="concurrency-and-throughput">Concurrency and throughput</h4>
<p>Each individual D1 database is inherently single-threaded, and processes queries one at a time.</p>
<p>Your maximum throughput is directly related to the duration of your queries.</p>
<ul>
<li>If your average query takes 1 ms, you can run approximately 1,000 queries per second.</li>
<li>If your average query takes 100 ms, you can run 10 queries per second.</li>
</ul>
<p>A database that receives too many concurrent requests will first attempt to queue them. If the queue becomes full, the database will return an <a href="/d1/observability/debug-d1/#error-list">&quot;overloaded&quot; error</a>.</p>
<p>Each individual D1 database is backed by a single <a href="/durable-objects/concepts/what-are-durable-objects/">Durable Object</a>. When using <a href="https://developers.cloudflare.com/d1/best-practices/read-replication/#primary-database-instance-vs-read-replicas">D1 read replication</a> each replica instance is a different Durable Object and the guidelines apply to each replica instance independently.</p>
<h4 id="query-performance">Query performance</h4>
<p>Query performance is the most important factor for throughput. As a rough guideline:</p>
<ul>
<li>Read queries like <code>SELECT name FROM users WHERE id = ?</code> with an appropriate index on <code>id</code> will take less than a millisecond for SQL duration.</li>
<li>Write queries like <code>INSERT</code> or <code>UPDATE</code> can take several milliseconds for SQL duration, and depend on the number of rows written. Writes need to be durably persisted across several locations - learn more on <a href="https://blog.cloudflare.com/d1-read-replication-beta/#under-the-hood-how-d1-read-replication-is-implemented">how D1 persists data under the hood</a>.</li>
<li>Data migrations like a large <code>UPDATE</code> or <code>DELETE</code> affecting millions of rows must be run in batches. A single query that attempts to modify hundreds of thousands of rows or hundreds of MBs of data at once will exceed execution limits. Break the work into smaller chunks (e.g., processing 1,000 rows at a time) to stay within platform limits.</li>
</ul>
<p>To ensure your queries are fast and efficient, <a href="/d1/best-practices/use-indexes/">use appropriate indexes in your SQL schema</a>.</p>
<h4 id="cpu-and-memory">CPU and memory</h4>
<p>Operations on a D1 database, including query execution and result serialization, run within the <a href="/workers/platform/limits/#memory">Workers platform CPU and memory limits</a>.</p>
<p>Exceeding these limits, or hitting other platform limits, will generate errors. Refer to the <a href="/d1/observability/debug-d1/#error-list">D1 error list for more details</a>.</p>
<h3 id="how-many-simultaneous-connections-can-a-worker-open-to-d1">How many simultaneous connections can a Worker open to D1?</h3>
<p>You can open up to six connections (to D1) simultaneously for each invocation of your Worker.</p>
<p>For more information on a Worker's simultaneous connections, refer to <a href="/workers/platform/limits/#simultaneous-open-connections">Simultaneous open connections</a>.</p>
