<p>Indexes enable D1 to improve query performance over the indexed columns for common (popular) queries by reducing the amount of data (number of rows) the database has to scan when running a query.</p>
<h2 id="when-is-an-index-useful">When is an index useful?</h2>
<p>Indexes are useful:</p>
<ul>
<li>When you want to improve the read performance over columns that are regularly used in predicates - for example, a <code>WHERE email_address = ?</code> or <code>WHERE user_id = 'a793b483-df87-43a8-a057-e5286d3537c5'</code> - email addresses, usernames, user IDs, and dates are good choices for columns to index in typical web applications or services.</li>
<li>For enforcing uniqueness constraints on a column or columns - for example, an email address or user ID via the <code>CREATE UNIQUE INDEX</code>.</li>
<li>In cases where you query over multiple columns together - <code>(customer_id, transaction_date)</code>.</li>
<li>For columns used to join tables together - for example, the <code>ON orders.customer_id = customers.id</code> in a <code>JOIN</code>. A suitable index can avoid repeated scans or the creation of a temporary index. Use <a href="#test-an-index"><code>EXPLAIN QUERY PLAN</code></a> to verify the query plan.</li>
</ul>
<p>Indexes are automatically updated when the table and column(s) they reference are inserted, updated or deleted. You do not need to manually update an index after you write to the table it references.</p>
<h2 id="create-an-index">Create an index</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7375.md")
</aside>
<p>To create an index on a D1 table, use the <code>CREATE INDEX</code> SQL command and specify the table and column(s) to create the index over.</p>
<p>For example, given the following <code>orders</code> table, you may want to create an index on <code>customer_id</code>. Nearly all of your queries against that table filter on <code>customer_id</code>, and you would see a performance improvement by creating an index for it.</p>
<pre><code class="language-sql">CREATE TABLE IF NOT EXISTS orders (&#10;    order_id INTEGER PRIMARY KEY,&#10;    customer_id STRING NOT NULL, -- for example, a unique ID aba0e360-1e04-41b3-91a0-1f2263e1e0fb&#10;    order_date STRING NOT NULL,&#10;    status INTEGER NOT NULL,&#10;    last_updated_date STRING NOT NULL&#10;)&#10;</code></pre>
<p>To create the index on the <code>customer_id</code> column, execute the below statement against your database:</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7374.md")
</aside>
<pre><code class="language-sql">CREATE INDEX IF NOT EXISTS idx_orders_customer_id ON orders(customer_id)&#10;</code></pre>
<p>Queries that reference the <code>customer_id</code> column will now benefit from the index:</p>
<pre><code class="language-sql">&#45;- Uses the index: the indexed column is referenced by the query.&#10;SELECT * FROM orders WHERE customer_id = ?&#10;&#10;&#45;- Does not use the index: customer_id is not in the query.&#10;SELECT * FROM orders WHERE order_date = &#x27;2023-05-01&#x27;&#10;</code></pre>
<p>In more complex cases, you can confirm whether an index was used by D1 by <a href="#test-an-index">analyzing a query</a> directly.</p>
<h3 id="run-pragma-optimize">Run <code>PRAGMA optimize</code></h3>
<p>After creating an index, run the <code>PRAGMA optimize</code> command to improve your database performance.</p>
<p><code>PRAGMA optimize</code> runs <code>ANALYZE</code> command on each table in the database, which collects statistics on the tables and indices. These statistics allows the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7376.md")
</div> to generate the most efficient query plan when executing the user query.
<p>For more information, refer to <a href="/d1/sql-api/sql-statements/#pragma-optimize"><code>PRAGMA optimize</code></a>.</p>
<h2 id="list-indexes">List indexes</h2>
<p>List the indexes on a database, as well as the SQL definition, by querying the <code>sqlite_schema</code> system table:</p>
<pre><code class="language-sql">SELECT name, type, sql FROM sqlite_schema WHERE type IN (&#x27;index&#x27;);&#10;</code></pre>
<p>This will return output resembling the below:</p>
<pre><code class="language-txt">┌──────────────────────────────────┬───────┬────────────────────────────────────────┐&#10;│ name                             │ type  │ sql                                    │&#10;├──────────────────────────────────┼───────┼────────────────────────────────────────┤&#10;│ idx_users_id                     │ index │ CREATE INDEX idx_users_id ON users(id) │&#10;└──────────────────────────────────┴───────┴────────────────────────────────────────┘&#10;</code></pre>
<p>Note that you cannot modify this table, or an existing index. To modify an index, <a href="#remove-indexes">delete it first</a> and <a href="#create-an-index">create a new index</a> with the updated definition.</p>
<h2 id="test-an-index">Test an index</h2>
<p>Validate that an index was used for a query by prepending a query with <a href="https://www.sqlite.org/eqp.html"><code>EXPLAIN QUERY PLAN</code></a>. This will output a query plan for the succeeding statement, including which (if any) indexes were used.</p>
<p>For example, if you assume the <code>users</code> table has an <code>email_address TEXT</code> column and you created an index <code>CREATE UNIQUE INDEX idx_email_address ON users(email_address)</code>, any query with a predicate on <code>email_address</code> should use your index.</p>
<pre><code class="language-sql">EXPLAIN QUERY PLAN SELECT * FROM users WHERE email_address = &#x27;foo@example.com&#x27;;&#10;QUERY PLAN&#10;`--SEARCH users USING INDEX idx_email_address (email_address=?)&#10;</code></pre>
<p>Review the <code>USING INDEX &lt;INDEX_NAME&gt;</code> output from the query planner, confirming the index was used.</p>
<p>This is also a fairly common use-case for an index. Finding a user based on their email address is often a very common query type for login (authentication) systems.</p>
<p>Using an index can reduce the number of rows read by a query. Use the <code>meta</code> object to estimate your usage. Refer to <a href="/d1/platform/pricing/#can-i-use-an-index-to-reduce-the-number-of-rows-read-by-a-query">&quot;Can I use an index to reduce the number of rows read by a query?&quot;</a> and <a href="/d1/platform/pricing/#how-can-i-estimate-my-eventual-bill">&quot;How can I estimate my (eventual) bill?&quot;</a>.</p>
<h2 id="indexes-and-your-bill">Indexes and your bill</h2>
<p>D1 <a href="/d1/platform/pricing/">bills by the number of rows read and rows written</a>, not by the number of rows your query returns. A query that scans an entire table to return a single row is billed for every row it scans. Adding an index so that D1 can jump straight to the rows it needs is therefore one of the most effective ways to reduce both latency <strong>and</strong> cost.</p>
<p>Most unexpectedly large D1 bills come from a small number of frequently run queries that each read (or write) far more rows than they return. The following table lists common patterns that touch too many rows, along with how to fix them. Use <a href="#test-an-index"><code>EXPLAIN QUERY PLAN</code></a> to check whether a query does a full <code>SCAN</code> (reads every row) or a <code>SEARCH ... USING INDEX</code> (jumps to matching rows).</p>
<table>
<thead>
<tr>
<th>Pattern</th>
<th>Why it reads or writes too many rows</th>
<th>Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>WHERE column = ?</code> on an unindexed column</td>
<td>D1 scans the whole table on every call.</td>
<td>Create an index on the filtered column.</td>
</tr>
<tr>
<td><code>WHERE a = ? AND b = ?</code> with no index on either column</td>
<td>D1 scans the whole table. An index on just one of the two columns avoids the full scan, but D1 still reads every row matching that column before filtering on the other.</td>
<td>Create a <a href="#multi-column-indexes">multi-column index</a> on <code>(a, b)</code> so D1 can narrow on both columns at once.</td>
</tr>
<tr>
<td><code>JOIN other ON other.x = main.y</code> where <code>other.x</code> is unindexed</td>
<td>Depending on the query plan, D1 may scan the joined table repeatedly or create a temporary index.</td>
<td>Index the column used in the join's <code>ON</code> condition (here, <code>other.x</code>), then verify the plan with <code>EXPLAIN QUERY PLAN</code>.</td>
</tr>
<tr>
<td>A correlated subquery such as <code>WHERE id = (SELECT ... WHERE inner.key = outer.key ...)</code></td>
<td>Depending on the query plan, D1 may evaluate the inner query for each candidate row. A scan in the inner query can multiply the number of rows read.</td>
<td>Index the column(s) the subquery filters and joins on, then verify the plan with <code>EXPLAIN QUERY PLAN</code>.</td>
</tr>
<tr>
<td><code>ORDER BY RANDOM() LIMIT 1</code></td>
<td>D1 must read and sort the entire result set to pick a random row - an index cannot help.</td>
<td>Avoid <code>ORDER BY RANDOM()</code> on large tables. Choose a sampling strategy that fits the primary key type, distribution, and required randomness.</td>
</tr>
<tr>
<td><code>WHERE column LIKE '%term%'</code> (leading wildcard), including inside <code>COUNT(*)</code></td>
<td>A leading <code>%</code> prevents a regular B-tree index from optimizing <code>LIKE</code>, so the query usually requires a full scan.</td>
<td>Remove the leading wildcard where possible. A prefix search such as <code>LIKE 'term%'</code> can use an index in some cases. For arbitrary substring searches, consider <a href="https://www.sqlite.org/fts5.html#the_trigram_tokenizer">FTS5 with the trigram tokenizer</a>, which can optimize patterns containing at least three consecutive non-wildcard Unicode characters. FTS5 indexes increase storage and write costs, so benchmark them for your workload. Verify either approach with <code>EXPLAIN QUERY PLAN</code>.</td>
</tr>
<tr>
<td>Re-running <code>CREATE INDEX</code> (or other schema changes) on every request</td>
<td>Building an index writes a row for every row it indexes, and writes are billed at a higher rate than reads. Doing this per request repeats that cost.</td>
<td>Run schema changes once with <a href="/d1/reference/migrations/">D1 migrations</a>, not on your application's hot path.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7373.md")
</aside>
<h2 id="multi-column-indexes">Multi-column indexes</h2>
<p>For a multi-column index (an index that specifies multiple columns), queries will only use the index if they specify either <em>all</em> of the columns, or a subset of the columns provided all columns to the &quot;left&quot; are also within the query.</p>
<p>Given an index of <code>CREATE INDEX idx_customer_id_transaction_date ON transactions(customer_id, transaction_date)</code>, the following table shows when the index is used (or not):</p>
<table>
<thead>
<tr>
<th>Query</th>
<th>Index Used?</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>SELECT * FROM transactions WHERE customer_id = '1234' AND transaction_date = '2023-03-25'</code></td>
<td>Yes: specifies both columns in the index.</td>
</tr>
<tr>
<td><code>SELECT * FROM transactions WHERE transaction_date = '2023-03-28'</code></td>
<td>No: only specifies <code>transaction_date</code>, and does not include other leftmost columns from the index.</td>
</tr>
<tr>
<td><code>SELECT * FROM transactions WHERE customer_id = '56789'</code></td>
<td>Yes: specifies <code>customer_id</code>, which is the leftmost column in the index.</td>
</tr>
</tbody>
</table>
<p>Notes:</p>
<ul>
<li>If you created an index over three columns instead — <code>customer_id</code>, <code>transaction_date</code>, and <code>shipping_status</code> — a query that uses both <code>customer_id</code> and <code>transaction_date</code> would use the index, as you are including all columns &quot;to the left&quot;.</li>
<li>With the same index, a query that uses only <code>transaction_date</code> and <code>shipping_status</code> would <em>not</em> use the index, as you have not used <code>customer_id</code> (the leftmost column) in the query.</li>
</ul>
<h2 id="partial-indexes">Partial indexes</h2>
<p>Partial indexes are indexes over a subset of rows in a table. Partial indexes are defined by the use of a <code>WHERE</code> clause when creating the index. A partial index can be useful to omit certain rows, such as those where values are <code>NULL</code> or where rows with a specific value are present across queries.</p>
<ul>
<li>A concrete example of a partial index would be on a table with a <code>order_status INTEGER</code> column, where <code>6</code> might represent <code>&quot;order complete&quot;</code> in your application code.</li>
<li>This would allow queries against orders that are unfulfilled, in-progress, or shipped, which are likely to be some of the most common queries (users checking their order status).</li>
<li>Partial indexes also keep the index from growing unbounded over time. The index does not need to keep a row for every completed order, and completed orders are likely to be queried far fewer times than in-progress orders.</li>
</ul>
<p>A partial index that filters out completed orders from the index would resemble the following:</p>
<pre><code class="language-sql">CREATE INDEX idx_order_status_not_complete ON orders(order_status) WHERE order_status != 6&#10;</code></pre>
<p>Partial indexes can be faster at read time (less rows in the index) and at write time (fewer writes to the index) than full indexes. You can also combine a partial index with a <a href="#multi-column-indexes">multi-column index</a>.</p>
<h2 id="remove-indexes">Remove indexes</h2>
<p>Use <code>DROP INDEX</code> to remove an index. Dropped indexes cannot be restored.</p>
<h2 id="considerations">Considerations</h2>
<p>Take note of the following considerations when creating indexes:</p>
<ul>
<li>Indexes are not always a free performance boost. You should create indexes only on columns that reflect your most-queried columns. Indexes themselves need to be maintained. When you write to an indexed column, the database needs to write to the table and the index. The performance benefit of an index and reduction in rows read will, in nearly all cases, offset this additional write.</li>
<li>You cannot create indexes that reference other tables or use non-deterministic functions, since the index would not be stable.</li>
<li>Indexes cannot be updated. To add or remove a column from an index, <a href="#remove-indexes">remove</a> the index and then <a href="#create-an-index">create a new index</a> with the new columns. Apply these schema changes once through a versioned system such as <a href="/d1/reference/migrations/">D1 migrations</a>.</li>
<li>Indexes contribute to the overall storage required by your database: an index is effectively a table itself.</li>
</ul>
