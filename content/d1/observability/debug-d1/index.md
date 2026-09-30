<p>D1 allows you to capture exceptions and log errors returned when querying a database. To debug D1, you will use the same tools available when <a href="/workers/observability/">debugging Workers</a>.</p>
<p>D1's <a href="/d1/worker-api/prepared-statements/"><code>stmt.</code></a> and <a href="/d1/worker-api/d1-database/"><code>db.</code></a> methods throw an <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error">Error object</a> whenever an error occurs. To capture exceptions, log the <code>e.message</code> value.</p>
<p>For example, the code below has a query with an invalid keyword - <code>INSERTZ</code> instead of <code>INSERT</code>:</p>
<pre><code class="language-js">try {&#10;    // This is an intentional misspelling&#10;    await db.exec(&quot;INSERTZ INTO my_table (name, employees) VALUES ()&quot;);&#10;} catch (e: any) {&#10;    console.error({&#10;        message: e.message&#10;    });&#10;}&#10;</code></pre>
<p>The code above throws the following error message:</p>
<pre><code class="language-json">{&#10;	&quot;message&quot;: &quot;D1_EXEC_ERROR: Error in line 1: INSERTZ INTO my_table (name, employees) VALUES (): sql error: near \&quot;INSERTZ\&quot;: syntax error in INSERTZ INTO my_table (name, employees) VALUES () at offset 0&quot;&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7354.md")
</aside>
<h2 id="error-list">Error list</h2>
<p>D1 returns the following error constants, in addition to the extended (detailed) error message:</p>
<table>
<thead>
<tr>
<th>Error message</th>
<th>Description</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>D1_ERROR</code></td>
<td>Prefix of a specific D1 error.</td>
<td>Refer to &quot;List of D1_ERRORs&quot; below for more detail about your specific error.</td>
</tr>
<tr>
<td><code>D1_EXEC_ERROR</code></td>
<td>Exec error in line x: y error.</td>
<td></td>
</tr>
<tr>
<td><code>D1_TYPE_ERROR</code></td>
<td>Returned when there is a mismatch in the type between a column and a value. A common cause is supplying an <code>undefined</code> variable (unsupported) instead of <code>null</code>.</td>
<td>Ensure the type of the value and the column match.</td>
</tr>
<tr>
<td><code>D1_COLUMN_NOTFOUND</code></td>
<td>Column not found.</td>
<td>Ensure you have selected a column which exists in the database.</td>
</tr>
</tbody>
</table>
<p>The following table lists specific instances of <code>D1_ERROR</code>.</p>
<div class="nb-example"><h3 class="nb-component-title" id="list-of-d1-errors">List of D1_ERRORs</h3>
@input("content/.markup/bodies/7355.md")
</div>
<h2 id="automatic-retries">Automatic retries</h2>
<p>D1 detects read-only queries and automatically attempts up to two retries to execute those queries in the event of failures with retryable errors.</p>
<p>D1 ensures that any retry attempt does not cause database writes, making the automatic retries safe from side-effects, even if a query causing modifications slips through the read-only detection. D1 achieves this by checking for modifications after every query execution, and if any write occurred due to a retry attempt, the query is rolled back.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7352.md")
</aside>
<h2 id="view-logs">View logs</h2>
<p>View a stream of live logs from your Worker by using <a href="/workers/observability/logs/real-time-logs#view-logs-using-wrangler-tail"><code>wrangler tail</code></a> or via the <a href="/workers/observability/logs/real-time-logs#view-logs-from-the-dashboard">Cloudflare dashboard</a>.</p>
<h2 id="report-issues">Report issues</h2>
<ul>
<li>To report bugs or request features, go to the <a href="https://community.cloudflare.com/c/developers/d1/85">Cloudflare Community Forums</a>.</li>
<li>To give feedback, go to the <a href="https://discord.com/invite/cloudflaredev">D1 Discord channel</a>.</li>
<li>If you are having issues with Wrangler, report issues in the <a href="https://github.com/cloudflare/workers-sdk/issues/new/choose">Wrangler GitHub repository</a>.</li>
</ul>
<p>You should include as much of the following in any bug report:</p>
<ul>
<li>The ID of your database. Use <code>wrangler d1 list</code> to match a database name to its ID.</li>
<li>The query (or queries) you ran when you encountered an issue. Ensure you redact any personally identifying information (PII).</li>
<li>The Worker code that makes the query, including any calls to <code>bind()</code> using the <a href="/d1/worker-api/">Workers Binding API</a>.</li>
<li>The full error text, including the content of <a href="#error-list"><code>error.cause.message</code></a>.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Learn <a href="/workers/observability/">how to debug Workers</a>.</li>
<li>Understand how to <a href="/workers/observability/logs/">access logs</a> generated from your Worker and D1.</li>
<li>Use <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> to run your Worker and D1 locally and <a href="/workers/local-development/">debug issues before deploying</a>.</li>
</ul>
