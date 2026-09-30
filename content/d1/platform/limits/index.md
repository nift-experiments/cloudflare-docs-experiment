<table>
<thead>
<tr>
<th>Feature</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Databases per account</td>
<td>50,000 (Workers Paid) <sup><a href="#footnote-1">1</a></sup> / 10 (Free)</td>
</tr>
<tr>
<td>Maximum database size</td>
<td>10 GB (Workers Paid) / 500 MB (Free)</td>
</tr>
<tr>
<td>Maximum storage per account</td>
<td>1 TB (Workers Paid) <sup><a href="#footnote-2">2</a></sup> / 5 GB (Free)</td>
</tr>
<tr>
<td><a href="/d1/reference/time-travel/">Time Travel</a> duration (point-in-time recovery)</td>
<td>30 days (Workers Paid) / 7 days (Free)</td>
</tr>
<tr>
<td>Maximum Time Travel restore operations</td>
<td>10 restores per 10 minutes (per database)</td>
</tr>
<tr>
<td>Queries per Worker invocation (read <a href="/workers/platform/limits/#subrequests">subrequest limits</a>)</td>
<td>1000 (Workers Paid) / 50 (Free)</td>
</tr>
<tr>
<td>Maximum number of columns per table</td>
<td>100</td>
</tr>
<tr>
<td>Maximum number of rows per table</td>
<td>Unlimited (excluding per-database storage limits)</td>
</tr>
<tr>
<td>Maximum string, <code>BLOB</code> or table row size</td>
<td>2,000,000 bytes (2 MB)</td>
</tr>
<tr>
<td>Maximum SQL statement length</td>
<td>100,000 bytes (100 KB)</td>
</tr>
<tr>
<td>Maximum bound parameters per query</td>
<td>100</td>
</tr>
<tr>
<td>Maximum arguments per SQL function</td>
<td>32</td>
</tr>
<tr>
<td>Maximum characters (bytes) in a <code>LIKE</code> or <code>GLOB</code> pattern</td>
<td>50 bytes</td>
</tr>
<tr>
<td>Maximum bindings per Workers script</td>
<td>Approximately 5,000 <sup><a href="#footnote-3">3</a></sup></td>
</tr>
<tr>
<td>Maximum SQL query duration</td>
<td>30 seconds <sup><a href="#footnote-4">4</a></sup></td>
</tr>
<tr>
<td>Maximum file import (<code>d1 execute</code>) size</td>
<td>5 GB <sup><a href="#footnote-5">5</a></sup></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="batch-limits">Batch limits</h3>
@markup("md", "content/.markup/bodies/7345.md")
</aside>
<p>Cloudflare also offers other storage solutions such as <a href="/kv/api/">Workers KV</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/r2/get-started/">R2</a>. Each product has different advantages and limits. Refer to <a href="/workers/platform/storage-options/">Choose a data or storage product</a> to review which storage option is right for your use case.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/7344.md")
</aside>
<h2 id="frequently-asked-questions">Frequently Asked Questions</h2>
<p>Frequently asked questions related to D1 limits:</p>
<h3 id="how-much-work-can-a-d1-database-do">How much work can a D1 database do?</h3>
<p>D1 is designed for horizontal scale out across multiple, smaller (10 GB) databases, such as per-user, per-tenant or per-entity databases.
D1 allows you to build applications with thousands of databases at no extra cost, as the pricing is based only on query and storage costs.</p>
<h4 id="storage">Storage</h4>
<p>Each D1 database can store up to 10 GB of data.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7343.md")
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
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">The maximum number of databases per account can be increased by request on Workers Paid and Enterprise plans, with support for millions to tens-of-millions of databases (or more) per account. Refer to the guidance on limit increases on this page to request an increase.</li>
<li id="footnote-2">The maximum storage per account can be increased by request on Workers Paid and Enterprise plans. Refer to the guidance on limit increases on this page to request an increase.</li>
<li id="footnote-3">A single Worker script can have up to 1 MB of script metadata. A binding is defined as a binding to a resource, such as a D1 database, KV namespace, [environmental variable](/workers/configuration/environment-variables/), or secret. Each resource binding is approximately 150-bytes, however environmental variables and secrets are controlled by the size of the value you provide. Excluding environmental variables, you can bind up to \~5,000 D1 databases to a single Worker script.</li>
<li id="footnote-4">Requests to Cloudflare API must resolve in 30 seconds. Therefore, this duration limit also applies to the entire batch call.</li>
<li id="footnote-5">The imported file is uploaded to R2. Refer to [R2 upload limit](/r2/platform/limits).</li></ol></section>
