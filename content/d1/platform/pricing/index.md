<p>D1 bills based on:</p>
<ul>
<li><strong>Usage</strong>: Queries you run against D1 will count as rows read, rows written, or both (for transactions or batches).</li>
<li><strong>Scale-to-zero</strong>: You are not billed for hours or capacity units. If you are not running queries against your database, you are not billed for compute.</li>
<li><strong>Storage</strong>: You are only billed for storage above the included <a href="/d1/platform/limits/">limits</a> of your plan.</li>
</ul>
<h2 id="billing-metrics">Billing metrics</h2>
<table>
<thead>
<tr>
<th></th>
<th><a href="/workers/platform/pricing/#workers">Workers Free</a></th>
<th><a href="/workers/platform/pricing/#workers">Workers Paid</a></th>
</tr>
</thead>
<tbody>
<tr>
<td>Rows read</td>
<td>5 million / day</td>
<td>First 25 billion / month included + $0.001 / million rows</td>
</tr>
<tr>
<td>Rows written</td>
<td>100,000 / day</td>
<td>First 50 million / month included + $1.00 / million rows</td>
</tr>
<tr>
<td>Storage (per GB stored)</td>
<td>5 GB (total)</td>
<td>First 5 GB included + $0.75 / GB-mo</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="track-your-d1-usage">Track your D1 usage</h3>
@markup("md", "content/.markup/bodies/7342.md")
</aside>
<h3 id="definitions">Definitions</h3>
<ol>
<li>Rows read measure how many rows a query reads (scans), regardless of the size of each row. For example, if you have a table with 5000 rows and run a <code>SELECT * FROM table</code> as a full table scan, this would count as 5,000 rows read. A query that filters on an <a href="/d1/best-practices/use-indexes/">unindexed column</a> may return fewer rows to your Worker, but is still required to read (scan) more rows to determine which subset to return.</li>
<li>Rows written measure how many rows were written to D1 database. Write operations include <code>INSERT</code>, <code>UPDATE</code>, and <code>DELETE</code>. Each of these operations contribute towards rows written. A query that <code>INSERT</code> 10 rows into a <code>users</code> table would count as 10 rows written.</li>
<li>DDL operations (for example, <code>CREATE</code>, <code>ALTER</code>, and <code>DROP</code>) are used to define or modify the structure of a database. They may contribute to a mix of read rows and write rows. Ensure you are accurately tracking your usage through the available tools (<a href="/d1/worker-api/return-object/">meta object</a>, <a href="/d1/observability/metrics-analytics/#query-via-the-graphql-api">GraphQL Analytics API</a>, or the <a href="https://dash.cloudflare.com/?to=/:account/workers/d1/">Cloudflare dashboard</a>).</li>
<li>Row size or the number of columns in a row does not impact how rows are counted. A row that is 1 KB and a row that is 100 KB both count as one row.</li>
<li>Defining <a href="/d1/best-practices/use-indexes/">indexes</a> on your table(s) reduces the number of rows read by a query when filtering on that indexed field. For example, if the <code>users</code> table has an index on a timestamp column <code>created_at</code>, the query <code>SELECT * FROM users WHERE created_at &gt; ?1</code> would only need to read a subset of the table.</li>
<li>Indexes will add an additional written row when writes include the indexed column, as there are two rows written: one to the table itself, and one to the index. The performance benefit of an index and reduction in rows read will, in nearly all cases, offset this additional write.</li>
<li>Storage is based on gigabytes stored per month, and is based on the sum of all databases in your account. Tables and indexes both count towards storage consumed.</li>
<li>Free limits reset daily at 00:00 UTC. Monthly included limits reset based on your monthly subscription renewal date, which is determined by the day you first subscribed.</li>
<li>There are no data transfer (egress) or throughput (bandwidth) charges for data accessed from D1.</li>
<li><a href="/d1/best-practices/read-replication/">Read replication</a> does not charge extra for read replicas. You incur the same usage billing based on <code>rows_read</code> and <code>rows_written</code> by your queries.</li>
</ol>
<h2 id="frequently-asked-questions">Frequently Asked Questions</h2>
<p>Frequently asked questions related to D1 pricing:</p>
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
