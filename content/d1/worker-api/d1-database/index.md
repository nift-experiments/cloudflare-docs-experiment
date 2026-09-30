<p>To interact with your D1 database from your Worker, you need to access it through the environment bindings provided to the Worker (<code>env</code>).</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7223.md")
</div></div>
<p>A D1 binding has the type <code>D1Database</code>, and supports a number of methods, as listed below.</p>
<h2 id="methods">Methods</h2>
<h3 id="prepare"><code>prepare()</code></h3>
<p>Prepares a query statement to be later executed.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7226.md")
</div></div>
<h4 id="parameters">Parameters</h4>
<ul>
<li><code>query</code>: <span class="nb-type">String</span> <span class="nb-metainfo">Required</span>
<ul>
<li>The SQL query you wish to execute on the database.</li>
</ul>
</li>
</ul>
<h4 id="return-values">Return values</h4>
<ul>
<li><code>D1PreparedStatement</code>: <span class="nb-type">Object</span>
<ul>
<li>An object which only contains methods. Refer to <a href="/d1/worker-api/prepared-statements/">Prepared statement methods</a>.</li>
</ul>
</li>
</ul>
<h4 id="guidance">Guidance</h4>
<p>You  can use the <code>bind</code> method to dynamically bind a value into the query statement, as shown below.</p>
<ul>
<li>Example of a static statement without using <code>bind</code>:</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7229.md")
</div></div>
<ul>
<li>Example of an ordered statement using <code>bind</code>:</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7232.md")
</div></div>
<p>Refer to the <a href="/d1/worker-api/prepared-statements/#bind"><code>bind</code> method documentation</a> for more information.</p>
<h3 id="batch"><code>batch()</code></h3>
<p>Sends multiple SQL statements inside a single call to the database. This can have a huge performance impact as it reduces latency from network round trips to D1. D1 operates in auto-commit. Our implementation guarantees that each statement in the list will execute and commit, sequentially, non-concurrently.</p>
<p>Batched statements are <a href="https://www.sqlite.org/lang_transaction.html">SQL transactions</a>. If a statement in the sequence fails, then an error is returned for that specific statement, and it aborts or rolls back the entire sequence.</p>
<p>To send batch statements, provide <code>D1Database::batch</code> a list of prepared statements and get the results in the same order.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7235.md")
</div></div>
<h4 id="parameters-1">Parameters</h4>
<ul>
<li><code>statements</code>: <span class="nb-type">Array</span>
<ul>
<li>An array of <a href="#prepare"><code>D1PreparedStatement</code></a>s.</li>
</ul>
</li>
</ul>
<h4 id="return-values-1">Return values</h4>
<ul>
<li><code>results</code>: <span class="nb-type">Array</span>
<ul>
<li>An array of <code>D1Result</code> objects containing the results of the <a href="#prepare"><code>D1Database::prepare</code></a> statements. Each object is in the array position corresponding to the array position of the initial <a href="#prepare"><code>D1Database::prepare</code></a> statement within the <code>statements</code>.</li>
<li>Refer to <a href="/d1/worker-api/return-object/#d1result"><code>D1Result</code></a> for more information about this object.</li>
</ul>
</li>
</ul>
<details class="nb-details"><summary>Example of return values</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7242.md")
</div></details>
<h4 id="guidance-1">Guidance</h4>
<ul>
<li>You can construct batches reusing the same prepared statement:</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7245.md")
</div></div>
<h3 id="exec"><code>exec()</code></h3>
<p>Executes one or more queries directly without prepared statements or parameter bindings.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7248.md")
</div></div>
<h4 id="parameters-2">Parameters</h4>
<ul>
<li><code>query</code>: <span class="nb-type">String</span> <span class="nb-metainfo">Required</span>
<ul>
<li>The SQL query statement without parameter binding.</li>
</ul>
</li>
</ul>
<h4 id="return-values-2">Return values</h4>
<ul>
<li><code>D1ExecResult</code>: <span class="nb-type">Object</span>
<ul>
<li>The <code>count</code> property contains the number of executed queries.</li>
<li>The <code>duration</code> property contains the duration of operation in milliseconds.
<ul>
<li>Refer to <a href="/d1/worker-api/return-object/#d1execresult"><code>D1ExecResult</code></a> for more information.</li>
</ul>
</li>
</ul>
</li>
</ul>
<details class="nb-details"><summary>Example of return values</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7252.md")
</div></details>
<h4 id="guidance-2">Guidance</h4>
<ul>
<li>If an error occurs, an exception is thrown with the query and error messages, execution stops and further statements are not executed. Refer to <a href="/d1/observability/debug-d1/#error-list">Errors</a> to learn more.</li>
<li>This method can have poorer performance (prepared statements can be reused in some cases) and, more importantly, is less safe.</li>
<li>Only use this method for maintenance and one-shot tasks (for example, migration jobs).</li>
<li>The input can be one or multiple queries separated by <code>\n</code>.</li>
</ul>
<h3 id="dump"><code>dump</code></h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7220.md")
</aside>
<p>Dumps the entire D1 database to an SQLite compatible file inside an ArrayBuffer.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7255.md")
</div></div>
<h4 id="parameters-3">Parameters</h4>
<ul>
<li>None.</li>
</ul>
<h4 id="return-values-3">Return values</h4>
<ul>
<li>None.</li>
</ul>
<h3 id="withsession"><code>withSession()</code></h3>
<p>Starts a D1 session which maintains sequential consistency among queries executed on the returned <code>D1DatabaseSession</code> object.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7258.md")
</div></div>
<h4 id="parameters-4">Parameters</h4>
<ul>
<li>
<p><code>first-primary</code>: <span class="nb-type">String</span><span class="nb-metainfo">Optional</span></p>
<ul>
<li>Directs the first query in the Session (whether read or write) to the primary database instance. Use this option if you need to start the Session with the most up-to-date data from the primary database instance.</li>
<li>Subsequent queries in the Session may use read replicas.</li>
<li>Subsequent queries in the Session have sequential consistency.</li>
</ul>
</li>
<li>
<p><code>first-unconstrained</code>: <span class="nb-type">String</span><span class="nb-metainfo">Optional</span></p>
<ul>
<li>Directs the first query in the Session (whether read or write) to any database instance. Use this option if you do not need to start the Session with the most up-to-date data, and wish to prioritize minimizing query latency from the very start of the Session.</li>
<li>Subsequent queries in the Session have sequential consistency.</li>
<li>This is the default behavior when no parameter is provided.</li>
</ul>
</li>
<li>
<p><code>bookmark</code>: <span class="nb-type">String</span><span class="nb-metainfo">Optional</span></p>
<ul>
<li>A <a href="/d1/reference/time-travel/#bookmarks"><code>bookmark</code></a> from a previous D1 Session. This allows you to start a new Session from at least the provided <code>bookmark</code>.</li>
<li>Subsequent queries in the Session have sequential consistency.</li>
</ul>
</li>
</ul>
<h4 id="return-values-4">Return values</h4>
<ul>
<li><code>D1DatabaseSession</code>: <span class="nb-type">Object</span>
<ul>
<li>An object which contains the methods <a href="/d1/worker-api/d1-database#prepare"><code>prepare()</code></a> and <a href="/d1/worker-api/d1-database#batch"><code>batch()</code></a> similar to <code>D1Database</code>, along with the additional <a href="/d1/worker-api/d1-database#getbookmark"><code>getBookmark</code></a> method.</li>
</ul>
</li>
</ul>
<h4 id="guidance-3">Guidance</h4>
<ul>
<li>To use read replication, you have to use the D1 Sessions API, otherwise all queries will continue to be executed only by the primary database.</li>
<li>You can return the last encountered <code>bookmark</code> for a given Session using <a href="/d1/worker-api/d1-database/#getbookmark"><code>session.getBookmark()</code></a>.</li>
</ul>
<h2 id="d1databasesession-methods"><code>D1DatabaseSession</code> methods</h2>
<h3 id="getbookmark"><code>getBookmark</code></h3>
<p>Retrieves the latest <code>bookmark</code> from the D1 Session.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7261.md")
</div></div>
<h4 id="parameters-5">Parameters</h4>
<ul>
<li>None</li>
</ul>
<h4 id="return-values-5">Return values</h4>
<ul>
<li><code>bookmark</code>: <span class="nb-type">String | null</span>
<ul>
<li>A <a href="/d1/reference/time-travel/#bookmarks"><code>bookmark</code></a> which identifies the latest version of the database seen by the last query executed within the Session.</li>
<li>Returns <code>null</code> if no query is executed within a Session.</li>
</ul>
</li>
</ul>
<h3 id="prepare-1"><code>prepare()</code></h3>
<p>This method is equivalent to <a href="/d1/worker-api/d1-database/#prepare"><code>D1Database::prepare</code></a>.</p>
<h3 id="batch-1"><code>batch()</code></h3>
<p>This method is equivalent to <a href="/d1/worker-api/d1-database/#batch"><code>D1Database::batch</code></a>.</p>
