<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11354.md")
</aside>
<p>This page summarizes supported features, limitations, and best practices.</p>
<h2 id="quick-reference">Quick reference</h2>
<table>
<thead>
<tr>
<th align="left">Feature</th>
<th align="left">Supported</th>
<th align="left">Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">SELECT, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT</td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Column aliases (<code>AS</code>)</td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Expressions (CASE, CAST, LIKE, BETWEEN, IN, arithmetic)</td>
<td align="left">Yes</td>
<td align="left">Full expression support</td>
</tr>
<tr>
<td align="left">EXPLAIN</td>
<td align="left">Yes</td>
<td align="left">Returns execution plan as text or JSON</td>
</tr>
<tr>
<td align="left">Scalar functions</td>
<td align="left">Yes</td>
<td align="left">Math, string, datetime, regex, crypto, array, map, struct, JSON</td>
</tr>
<tr>
<td align="left">Aggregate functions</td>
<td align="left">Yes</td>
<td align="left">Basic, approximate, statistical, bitwise, boolean, positional</td>
</tr>
<tr>
<td align="left">Approximate aggregates</td>
<td align="left">Yes</td>
<td align="left"><code>approx_distinct</code>, <code>approx_median</code>, <code>approx_percentile_cont</code>, <code>approx_top_k</code></td>
</tr>
<tr>
<td align="left">Struct / Array / Map column types</td>
<td align="left">Yes</td>
<td align="left">Bracket notation, <code>get_field()</code>, array functions, map functions</td>
</tr>
<tr>
<td align="left">CTEs (<code>WITH ... AS</code>)</td>
<td align="left">Yes</td>
<td align="left">Can reference different tables and include JOINs</td>
</tr>
<tr>
<td align="left">JOINs (INNER, LEFT, RIGHT, FULL OUTER, CROSS)</td>
<td align="left">Yes</td>
<td align="left">All standard join types</td>
</tr>
<tr>
<td align="left">Implicit joins (comma FROM)</td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Subqueries (<code>IN</code>, <code>NOT IN</code>)</td>
<td align="left">Yes</td>
<td align="left"><code>NOT IN</code> not supported on nullable columns — use <code>NOT EXISTS</code> instead</td>
</tr>
<tr>
<td align="left">Subqueries (<code>EXISTS</code>, <code>NOT EXISTS</code>)</td>
<td align="left">Yes</td>
<td align="left">semi-join and anti-join patterns</td>
</tr>
<tr>
<td align="left">Scalar subqueries</td>
<td align="left">Yes</td>
<td align="left">In SELECT, WHERE, HAVING</td>
</tr>
<tr>
<td align="left">Derived tables (FROM subqueries)</td>
<td align="left">Yes</td>
<td align="left">Can be nested and joined. <code>LATERAL</code> derived tables not supported.</td>
</tr>
<tr>
<td align="left">Self-joins</td>
<td align="left">Yes</td>
<td align="left">Same table with different aliases</td>
</tr>
<tr>
<td align="left">Window functions (<code>OVER</code>)</td>
<td align="left">Yes</td>
<td align="left">Inline <code>OVER (...)</code> only — named <code>WINDOW</code> clause not supported</td>
</tr>
<tr>
<td align="left"><code>QUALIFY</code></td>
<td align="left">Yes</td>
<td align="left">Filter on a window function result</td>
</tr>
<tr>
<td align="left"><code>SELECT DISTINCT</code> / <code>DISTINCT ON</code></td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr>
<td align="left"><code>func(DISTINCT ...)</code></td>
<td align="left">Yes</td>
<td align="left"><code>COUNT</code>, <code>SUM</code>, <code>AVG</code>, and other aggregates</td>
</tr>
<tr>
<td align="left">Set operations (<code>UNION</code>, <code>UNION ALL</code>, <code>INTERSECT</code>, <code>EXCEPT</code>)</td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr>
<td align="left"><code>GROUPING SETS</code> / <code>ROLLUP</code> / <code>CUBE</code></td>
<td align="left">Yes</td>
<td align="left"></td>
</tr>
<tr>
<td align="left"><code>OFFSET</code></td>
<td align="left">No</td>
<td align="left"></td>
</tr>
<tr>
<td align="left"><code>INSERT</code> / <code>UPDATE</code> / <code>DELETE</code></td>
<td align="left">No</td>
<td align="left">Read-only</td>
</tr>
<tr>
<td align="left"><code>CREATE</code> / <code>DROP</code> / <code>ALTER</code></td>
<td align="left">No</td>
<td align="left">Read-only</td>
</tr>
</tbody>
</table>
<p>For the full SQL syntax, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>.</p>
<hr />
<h2 id="unsupported-sql-features">Unsupported SQL features</h2>
<table>
<thead>
<tr>
<th align="left">Feature</th>
<th align="left">Error</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>OFFSET</code></td>
<td align="left"><code>unsupported feature: OFFSET clause is not supported</code></td>
</tr>
<tr>
<td align="left">Named <code>WINDOW</code> clause</td>
<td align="left"><code>unsupported feature: WINDOW clause is not supported</code></td>
</tr>
<tr>
<td align="left"><code>INSERT</code> / <code>UPDATE</code> / <code>DELETE</code></td>
<td align="left"><code>only read-only queries are allowed</code></td>
</tr>
<tr>
<td align="left"><code>CREATE</code> / <code>DROP</code> / <code>ALTER</code></td>
<td align="left"><code>only read-only queries are allowed</code></td>
</tr>
<tr>
<td align="left"><code>UNNEST</code> / <code>PIVOT</code> / <code>UNPIVOT</code></td>
<td align="left">Not supported</td>
</tr>
<tr>
<td align="left">Wildcard modifiers (<code>ILIKE</code>, <code>EXCLUDE</code>, <code>EXCEPT</code>, <code>REPLACE</code>, <code>RENAME</code> on <code>*</code>)</td>
<td align="left">Not supported</td>
</tr>
<tr>
<td align="left">Nested (parenthesized) joins</td>
<td align="left">Not supported</td>
</tr>
<tr>
<td align="left"><code>LATERAL</code> derived tables / <code>LATERAL VIEW</code></td>
<td align="left">Not supported</td>
</tr>
<tr>
<td align="left"><code>PERCENTILE_DISC</code></td>
<td align="left">Not supported — use <code>PERCENTILE_CONT</code></td>
</tr>
</tbody>
</table>
<hr />
<h2 id="unsupported-expression-patterns">Unsupported expression patterns</h2>
<table>
<thead>
<tr>
<th align="left">Pattern</th>
<th align="left">Alternative</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>NOT IN</code> subquery on nullable columns</td>
<td align="left">Use <code>NOT EXISTS</code> with a correlated subquery instead</td>
</tr>
</tbody>
</table>
<p>Exact aggregates such as <code>COUNT(DISTINCT ...)</code>, <code>MEDIAN</code>, <code>PERCENTILE_CONT</code>, <code>ARRAY_AGG</code>, and <code>STRING_AGG</code> are supported. On large datasets, prefer the approximate alternatives (<code>approx_distinct</code>, <code>approx_median</code>, <code>approx_percentile_cont</code>) for lower memory and compute. Refer to <a href="/r2-sql/sql-reference/aggregate-functions/">Aggregate functions</a>.</p>
<hr />
<h2 id="runtime-constraints">Runtime constraints</h2>
<table>
<thead>
<tr>
<th align="left">Constraint</th>
<th align="left">Details</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Resource-intensive queries</td>
<td align="left">During open beta, queries that require high memory or compute may time out. This includes multi-way joins (three or more large tables), <code>COUNT(DISTINCT)</code> and other <code>func(DISTINCT ...)</code> across joins or high-cardinality columns, <code>ARRAY_AGG</code> / <code>STRING_AGG</code>, set operations that deduplicate large inputs, window functions over large partitions, and large sorts or high-cardinality <code>GROUP BY</code>. Add <code>WHERE</code> filters and <code>LIMIT</code>, and prefer <code>approx_*</code> aggregates to reduce the chance of a timeout.</td>
</tr>
<tr>
<td align="left">Budget-gated functions</td>
<td align="left"><code>MEDIAN</code>, <code>PERCENTILE_CONT</code>, <code>ARRAY_AGG</code>, <code>STRING_AGG</code>, <code>NTH_VALUE</code> used as an aggregate, any aggregate with <code>DISTINCT</code>, and window functions (including those used through <code>QUALIFY</code>) are budget-gated up front. R2 SQL estimates the memory required before running the query and rejects it with a <code>400</code> error if too much data would be scanned. Add a <code>GROUP BY</code> or <code>WHERE</code> filters to reduce the rows processed.</td>
</tr>
<tr>
<td align="left">Multi-table queries</td>
<td align="left">JOINs, subqueries (IN, EXISTS, scalar, derived tables), and multi-table CTEs are supported. Performance depends on intermediate result size; use WHERE filters to manage join selectivity.</td>
</tr>
<tr>
<td align="left">Partitioned and unpartitioned tables</td>
<td align="left">Both partitioned and unpartitioned Iceberg tables are supported.</td>
</tr>
<tr>
<td align="left">Parquet format only</td>
<td align="left">No CSV, JSON, or other formats.</td>
</tr>
<tr>
<td align="left">Read-only</td>
<td align="left">R2 SQL is a query engine, not a database. No writes.</td>
</tr>
<tr>
<td align="left"><code>now()</code> / <code>current_time()</code> precision</td>
<td align="left">Quantized to 10ms boundaries and forced to UTC.</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="common-error-codes">Common error codes</h2>
<table>
<thead>
<tr>
<th align="left">Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">40003</td>
<td align="left">Invalid SQL syntax</td>
</tr>
<tr>
<td align="left">40004</td>
<td align="left">Invalid query (unsupported feature, unknown column, type mismatch)</td>
</tr>
<tr>
<td align="left">80001</td>
<td align="left">Edge service connection failure (retry)</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="best-practices">Best practices</h2>
<ol>
<li>Include time-range filters in <code>WHERE</code> to limit data scanned.</li>
<li>Use specific column names instead of <code>SELECT *</code> for better performance.</li>
<li>Use <code>LIMIT</code> to control result set size.</li>
<li>Use approximate aggregation functions (<code>approx_distinct</code>, <code>approx_median</code>, <code>approx_percentile_cont</code>) instead of exact alternatives on large datasets.</li>
<li>Enable compaction in R2 Data Catalog to reduce the number of files scanned per query.</li>
<li>Use <code>EXPLAIN</code> to inspect the execution plan and verify predicate pushdown.</li>
<li>Use <code>WHERE</code> filters with multi-way joins to reduce intermediate result sizes. Joining three or more large tables without filters can exceed resource limits.</li>
<li>Join large fact tables through dimension tables rather than directly joining two large fact tables. For example, join <code>http_requests</code> to <code>firewall_events</code> through a shared <code>zones</code> dimension rather than cross-joining both fact tables.</li>
<li>Be cautious with <code>COUNT(DISTINCT)</code> across multi-way joins. This combination can produce very large intermediate results. Consider using <code>approx_distinct()</code> or breaking the query into smaller steps.</li>
<li>Use explicit <code>JOIN</code> syntax instead of implicit joins (comma-separated <code>FROM</code>) for readability and to ensure the optimizer can choose optimal join ordering.</li>
</ol>
