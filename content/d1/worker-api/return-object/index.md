<p>Some D1 Worker Binding APIs return a typed object.</p>
<table>
<thead>
<tr>
<th>D1 Worker Binding API</th>
<th>Return object</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/d1/worker-api/prepared-statements/#run"><code>D1PreparedStatement::run</code></a>, <a href="/d1/worker-api/d1-database/#batch"><code>D1Database::batch</code></a></td>
<td><code>D1Result</code></td>
</tr>
<tr>
<td><a href="/d1/worker-api/d1-database/#exec"><code>D1Database::exec</code></a></td>
<td><code>D1ExecResult</code></td>
</tr>
</tbody>
</table>
<h2 id="d1result"><code>D1Result</code></h2>
<p>The methods <a href="/d1/worker-api/prepared-statements/#run"><code>D1PreparedStatement::run</code></a> and <a href="/d1/worker-api/d1-database/#batch"><code>D1Database::batch</code></a> return a typed <a href="#d1result"><code>D1Result</code></a> object for each query statement. This object contains:</p>
<ul>
<li>The success status</li>
<li>A meta object with the internal duration of the operation in milliseconds</li>
<li>The results (if applicable) as an array</li>
</ul>
<pre><code class="language-js">{&#10;  success: boolean, // true if the operation was successful, false otherwise&#10;  meta: {&#10;    served_by: string // the version of Cloudflare&#x27;s backend Worker that returned the result&#10;    served_by_region: string // the region of the database instance that executed the query&#10;    served_by_primary: boolean // true if (and only if) the database instance that executed the query was the primary&#10;    timings: {&#10;      sql_duration_ms: number // the duration of the SQL query execution by the database instance (not including any network time)&#10;    }&#10;    duration: number, // the duration of the SQL query execution only, in milliseconds&#10;		changes: number, // the number of changes made to the database&#10;		last_row_id: number, // the last inserted row ID, only applies when the table is defined without the `WITHOUT ROWID` option&#10;		changed_db: boolean, // true if something on the database was changed&#10;    size_after: number, // the size of the database after the query is successfully applied&#10;    rows_read: number, // the number of rows read (scanned) by this query&#10;    rows_written: number // the number of rows written by this query&#10;    total_attempts: number //the number of total attempts to successfully execute the query, including retries&#10;  }&#10;  results: array | null, // [] if empty, or null if it does not apply&#10;}&#10;</code></pre>
<h3 id="example">Example</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7163.md")
</div></div>
<pre><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;meta&quot;: {&#10;    &quot;served_by&quot;: &quot;miniflare.db&quot;,&#10;    &quot;served_by_region&quot;: &quot;WEUR&quot;,&#10;    &quot;served_by_primary&quot;: true,&#10;    &quot;timings&quot;: {&#10;      &quot;sql_duration_ms&quot;: 0.2552&#10;    },&#10;    &quot;duration&quot;: 0.2552,&#10;    &quot;changes&quot;: 0,&#10;    &quot;last_row_id&quot;: 0,&#10;    &quot;changed_db&quot;: false,&#10;    &quot;size_after&quot;: 16384,&#10;    &quot;rows_read&quot;: 4,&#10;    &quot;rows_written&quot;: 0&#10;  },&#10;  &quot;results&quot;: [&#10;    {&#10;      &quot;CustomerId&quot;: 11,&#10;      &quot;CompanyName&quot;: &quot;Bs Beverages&quot;,&#10;      &quot;ContactName&quot;: &quot;Victoria Ashworth&quot;&#10;    },&#10;    {&#10;      &quot;CustomerId&quot;: 13,&#10;      &quot;CompanyName&quot;: &quot;Bs Beverages&quot;,&#10;      &quot;ContactName&quot;: &quot;Random Name&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<h2 id="d1execresult"><code>D1ExecResult</code></h2>
<p>The method <a href="/d1/worker-api/d1-database/#exec"><code>D1Database::exec</code></a> returns a typed <a href="#d1execresult"><code>D1ExecResult</code></a> object for each query statement. This object contains:</p>
<ul>
<li>The number of executed queries</li>
<li>The duration of the operation in milliseconds</li>
</ul>
<pre><code class="language-js">{&#10;	&quot;count&quot;: number, // the number of executed queries&#10;	&quot;duration&quot;: number // the duration of the operation, in milliseconds&#10;}&#10;</code></pre>
<h3 id="example-1">Example</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7166.md")
</div></div>
<pre><code class="language-json">{&#10;  &quot;count&quot;: 1,&#10;  &quot;duration&quot;: 1&#10;}&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="storing-large-numbers">Storing large numbers</h3>
@markup("md", "content/.markup/bodies/7160.md")
</aside>
