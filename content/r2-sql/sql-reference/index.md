<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11350.md")
</aside>
<p>R2 SQL is Cloudflare's serverless, distributed, analytics query engine for querying <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>. This page documents the supported SQL syntax.</p>
<hr />
<h2 id="query-syntax">Query syntax</h2>
<pre><code class="language-sql">SELECT [DISTINCT] column_list | expression | aggregate_function | window_function&#10;FROM namespace_name.table_name&#10;[JOIN namespace_name.table_name ON condition]&#10;[WHERE conditions]&#10;[GROUP BY column_list]&#10;[HAVING conditions]&#10;[QUALIFY window_condition]&#10;[ORDER BY expression [ASC | DESC]]&#10;[LIMIT number]&#10;</code></pre>
<p>Two or more queries can be combined with <a href="#set-operations">set operations</a> (<code>UNION</code>, <code>UNION ALL</code>, <code>INTERSECT</code>, <code>EXCEPT</code>).</p>
<hr />
<h2 id="schema-discovery-commands">Schema discovery commands</h2>
<h3 id="show-databases">SHOW DATABASES</h3>
<p>Lists all available namespaces.</p>
<pre><code class="language-sql">SHOW DATABASES;&#10;</code></pre>
<h3 id="show-namespaces">SHOW NAMESPACES</h3>
<p>Alias for <code>SHOW DATABASES</code>. Lists all available namespaces.</p>
<pre><code class="language-sql">SHOW NAMESPACES;&#10;</code></pre>
<h3 id="show-tables">SHOW TABLES</h3>
<p>Lists all tables within a specific namespace.</p>
<pre><code class="language-sql">SHOW TABLES IN namespace_name;&#10;</code></pre>
<h3 id="describe">DESCRIBE</h3>
<p>Describes the structure of a table, showing column names and data types.</p>
<pre><code class="language-sql">DESCRIBE namespace_name.table_name;&#10;</code></pre>
<hr />
<h2 id="select-clause">SELECT clause</h2>
<h3 id="syntax">Syntax</h3>
<pre><code class="language-sql">SELECT [DISTINCT] column_specification [, column_specification, ...]&#10;</code></pre>
<h3 id="column-specification">Column specification</h3>
<ul>
<li><strong>Column name</strong>: <code>column_name</code></li>
<li><strong>All columns</strong>: <code>*</code></li>
<li><strong>Qualified wildcard</strong>: <code>table_name.*</code></li>
<li><strong>Column alias</strong>: <code>column_name AS alias</code></li>
<li><strong>Expressions</strong>: arithmetic, function calls, CASE expressions, and casts</li>
</ul>
<h3 id="examples">Examples</h3>
<pre><code class="language-sql">SELECT * FROM my_namespace.sales_data LIMIT 10&#10;SELECT customer_id, region, total_amount FROM my_namespace.sales_data LIMIT 10&#10;SELECT region, total_amount * 1.1 AS total_with_tax FROM my_namespace.sales_data LIMIT 10&#10;</code></pre>
<h3 id="distinct">DISTINCT</h3>
<p><code>SELECT DISTINCT</code> returns unique rows. <code>DISTINCT ON (...)</code> returns the first row for each combination of the listed expressions, using the <code>ORDER BY</code> clause to determine which row is kept.</p>
<pre><code class="language-sql">&#45;- Unique combinations&#10;SELECT DISTINCT region, department FROM my_namespace.sales_data&#10;&#10;&#45;- First row per region by amount&#10;SELECT DISTINCT ON (region) region, customer_id, total_amount&#10;FROM my_namespace.sales_data&#10;ORDER BY region, total_amount DESC&#10;</code></pre>
<p>For counting unique values on large datasets, <code>approx_distinct()</code> is a faster alternative.</p>
<hr />
<h2 id="common-table-expressions-ctes">Common table expressions (CTEs)</h2>
<p>CTEs let you define named temporary result sets using <code>WITH</code> that you can reference in the main query. CTEs can reference different tables and can include JOINs. A CTE can also be joined with other CTEs or regular tables in the main query.</p>
<h3 id="syntax-1">Syntax</h3>
<pre><code class="language-sql">WITH cte_name AS (&#10;    SELECT ...&#10;    FROM namespace_name.table_name&#10;    [WHERE ...]&#10;)&#10;SELECT ... FROM cte_name&#10;</code></pre>
<h3 id="chained-ctes">Chained CTEs</h3>
<p>A CTE can reference a previously defined CTE.</p>
<pre><code class="language-sql">WITH filtered AS (&#10;    SELECT customer_id, department, total_amount&#10;    FROM my_namespace.sales_data&#10;    WHERE total_amount &gt; 0&#10;),&#10;summary AS (&#10;    SELECT department,&#10;           COUNT(*) AS order_count,&#10;           round(AVG(total_amount), 2) AS avg_amount&#10;    FROM filtered&#10;    GROUP BY department&#10;)&#10;SELECT *&#10;FROM summary&#10;WHERE order_count &gt; 100&#10;ORDER BY avg_amount DESC&#10;</code></pre>
<h3 id="cte-joined-with-another-table">CTE joined with another table</h3>
<pre><code class="language-sql">WITH enterprise_zones AS (&#10;    SELECT zone_id, domain, plan&#10;    FROM my_namespace.zones&#10;    WHERE plan = &#x27;enterprise&#x27;&#10;)&#10;SELECT ez.domain, f.action, COUNT(*) AS cnt&#10;FROM enterprise_zones ez&#10;INNER JOIN my_namespace.firewall_events f ON ez.zone_id = f.zone_id&#10;GROUP BY ez.domain, f.action&#10;ORDER BY cnt DESC&#10;LIMIT 20&#10;</code></pre>
<h3 id="two-ctes-joined-together">Two CTEs joined together</h3>
<pre><code class="language-sql">WITH top_zones AS (&#10;    SELECT zone_id, COUNT(*) AS req_count&#10;    FROM my_namespace.http_requests&#10;    GROUP BY zone_id&#10;    ORDER BY req_count DESC&#10;    LIMIT 50&#10;),&#10;zone_threats AS (&#10;    SELECT zone_id, COUNT(*) AS threat_count&#10;    FROM my_namespace.firewall_events&#10;    WHERE risk_score &gt; 0.5&#10;    GROUP BY zone_id&#10;)&#10;SELECT tz.zone_id, tz.req_count, COALESCE(zt.threat_count, 0) AS threat_count&#10;FROM top_zones tz&#10;LEFT JOIN zone_threats zt ON tz.zone_id = zt.zone_id&#10;ORDER BY tz.req_count DESC&#10;LIMIT 20&#10;</code></pre>
<hr />
<h2 id="from-clause">FROM clause</h2>
<h3 id="syntax-2">Syntax</h3>
<pre><code class="language-sql">SELECT * FROM namespace_name.table_name&#10;</code></pre>
<p>R2 SQL queries can reference one or more tables. Tables are specified as <code>namespace_name.table_name</code>. Multiple tables can be combined using JOINs or comma-separated syntax. Refer to the <a href="#join-clause">JOIN clause</a> section for details.</p>
<hr />
<h2 id="join-clause">JOIN clause</h2>
<p>R2 SQL supports joining multiple Iceberg tables in a single query. All join types use standard SQL syntax.</p>
<h3 id="supported-join-types">Supported join types</h3>
<table>
<thead>
<tr>
<th align="left">Join type</th>
<th align="left">Syntax</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Inner join</td>
<td align="left"><code>INNER JOIN ... ON</code></td>
<td align="left">Returns rows that match in both tables</td>
</tr>
<tr>
<td align="left">Left outer join</td>
<td align="left"><code>LEFT JOIN ... ON</code></td>
<td align="left">Returns all rows from the left table, NULLs for non-matching right</td>
</tr>
<tr>
<td align="left">Right outer join</td>
<td align="left"><code>RIGHT JOIN ... ON</code></td>
<td align="left">Returns all rows from the right table, NULLs for non-matching left</td>
</tr>
<tr>
<td align="left">Full outer join</td>
<td align="left"><code>FULL OUTER JOIN ... ON</code></td>
<td align="left">Returns all rows from both tables, NULLs where no match</td>
</tr>
<tr>
<td align="left">Cross join</td>
<td align="left"><code>CROSS JOIN</code></td>
<td align="left">Cartesian product of both tables</td>
</tr>
<tr>
<td align="left">Implicit join</td>
<td align="left"><code>FROM t1, t2 WHERE t1.id = t2.id</code></td>
<td align="left">Comma-separated tables with join condition in <code>WHERE</code></td>
</tr>
</tbody>
</table>
<h3 id="syntax-3">Syntax</h3>
<pre><code class="language-sql">&#45;- Explicit JOIN&#10;SELECT columns&#10;FROM namespace.table1 alias1&#10;[INNER | LEFT | RIGHT | FULL OUTER | CROSS] JOIN namespace.table2 alias2&#10;  ON alias1.column = alias2.column&#10;[WHERE conditions]&#10;&#10;&#45;- Implicit join&#10;SELECT columns&#10;FROM namespace.table1 alias1, namespace.table2 alias2&#10;WHERE alias1.column = alias2.column&#10;</code></pre>
<h3 id="multi-way-joins">Multi-way joins</h3>
<p>You can join three or more tables in a single query:</p>
<pre><code class="language-sql">SELECT z.domain, h.method, f.action, COUNT(*) AS cnt&#10;FROM my_namespace.zones z&#10;INNER JOIN my_namespace.http_requests h ON z.zone_id = h.zone_id&#10;INNER JOIN my_namespace.firewall_events f ON z.zone_id = f.zone_id&#10;WHERE h.status_code &gt;= 400&#10;GROUP BY z.domain, h.method, f.action&#10;ORDER BY cnt DESC&#10;LIMIT 20&#10;</code></pre>
<h3 id="self-joins">Self-joins</h3>
<p>A table can be joined with itself using different aliases:</p>
<pre><code class="language-sql">SELECT f1.source_ip, f1.zone_id AS zone1, f2.zone_id AS zone2&#10;FROM my_namespace.firewall_events f1&#10;INNER JOIN my_namespace.firewall_events f2&#10;  ON f1.source_ip = f2.source_ip&#10;  AND f1.zone_id &lt; f2.zone_id&#10;WHERE f1.action = &#x27;block&#x27;&#10;LIMIT 20&#10;</code></pre>
<h3 id="join-conditions">Join conditions</h3>
<ul>
<li>Join conditions use the <code>ON</code> clause with equality (<code>=</code>) or expression-based predicates.</li>
<li>Functions are supported in join predicates (for example, <code>ON LOWER(a.col) = LOWER(b.col)</code>).</li>
<li>Multiple conditions can be combined with <code>AND</code>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11349.md")
</aside>
<h3 id="best-practices-for-joins">Best practices for joins</h3>
<ul>
<li>Include <code>WHERE</code> filters to reduce intermediate result sizes, especially for multi-way joins.</li>
<li>Join large fact tables through a shared dimension table rather than directly cross-joining two large tables.</li>
<li>Use <code>LIMIT</code> to cap result sizes.</li>
</ul>
<hr />
<h2 id="subqueries">Subqueries</h2>
<p>R2 SQL supports subqueries in multiple positions within a query.</p>
<h3 id="subqueries-in-from-derived-tables">Subqueries in FROM (derived tables)</h3>
<p>A subquery in the <code>FROM</code> clause creates a derived table that can be referenced in the outer query:</p>
<pre><code class="language-sql">SELECT sub.domain, sub.total_requests&#10;FROM (&#10;    SELECT z.domain, COUNT(*) AS total_requests&#10;    FROM my_namespace.zones z&#10;    INNER JOIN my_namespace.http_requests h ON z.zone_id = h.zone_id&#10;    GROUP BY z.domain&#10;) sub&#10;WHERE sub.total_requests &gt; 1000&#10;ORDER BY sub.total_requests DESC&#10;LIMIT 20&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11348.md")
</aside>
<p>Derived tables can be joined with other derived tables or regular tables:</p>
<pre><code class="language-sql">SELECT req.domain, req.total_reqs, fw.total_events&#10;FROM (&#10;    SELECT zone_id, domain, COUNT(*) AS total_reqs&#10;    FROM my_namespace.zones z&#10;    INNER JOIN my_namespace.http_requests h ON z.zone_id = h.zone_id&#10;    GROUP BY zone_id, domain&#10;) req&#10;INNER JOIN (&#10;    SELECT zone_id, COUNT(*) AS total_events&#10;    FROM my_namespace.firewall_events&#10;    GROUP BY zone_id&#10;) fw ON req.zone_id = fw.zone_id&#10;ORDER BY fw.total_events DESC&#10;LIMIT 20&#10;</code></pre>
<h3 id="in-not-in-subqueries"><code>IN</code> / <code>NOT IN</code> subqueries</h3>
<p>Filter rows based on whether a value exists in the result of a subquery:</p>
<pre><code class="language-sql">&#45;- Find requests from enterprise zones&#10;SELECT method, status_code, COUNT(*) AS cnt&#10;FROM my_namespace.http_requests&#10;WHERE zone_id IN (&#10;    SELECT zone_id FROM my_namespace.zones WHERE plan = &#x27;enterprise&#x27;&#10;)&#10;GROUP BY method, status_code&#10;ORDER BY cnt DESC&#10;LIMIT 20&#10;</code></pre>
<pre><code class="language-sql">&#45;- NOT IN example&#10;SELECT zone_id, COUNT(*) AS cnt&#10;FROM my_namespace.http_requests&#10;WHERE zone_id NOT IN (&#10;    SELECT zone_id FROM my_namespace.firewall_events WHERE action = &#x27;block&#x27;&#10;)&#10;GROUP BY zone_id&#10;LIMIT 10&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11347.md")
</aside>
<h3 id="exists-not-exists-subqueries"><code>EXISTS</code> / <code>NOT EXISTS</code> subqueries</h3>
<p>Test for the existence of rows matching a correlated condition:</p>
<pre><code class="language-sql">&#45;- Find zones with blocked firewall events (semi-join)&#10;SELECT z.domain, z.plan&#10;FROM my_namespace.zones z&#10;WHERE EXISTS (&#10;    SELECT 1 FROM my_namespace.firewall_events f&#10;    WHERE f.zone_id = z.zone_id AND f.action = &#x27;block&#x27;&#10;)&#10;ORDER BY z.domain&#10;LIMIT 20&#10;</code></pre>
<pre><code class="language-sql">&#45;- Find zones with NO firewall events (anti-join)&#10;SELECT z.domain, z.plan&#10;FROM my_namespace.zones z&#10;WHERE NOT EXISTS (&#10;    SELECT 1 FROM my_namespace.firewall_events f&#10;    WHERE f.zone_id = z.zone_id&#10;)&#10;ORDER BY z.domain&#10;LIMIT 20&#10;</code></pre>
<h3 id="scalar-subqueries">Scalar subqueries</h3>
<p>A subquery that returns a single value can be used in <code>SELECT</code>, <code>WHERE</code>, or <code>HAVING</code>:</p>
<pre><code class="language-sql">&#45;- In SELECT (constant value per row)&#10;SELECT z.domain, z.plan,&#10;       (SELECT COUNT(*) FROM my_namespace.zones) AS total_zones&#10;FROM my_namespace.zones z&#10;WHERE z.plan = &#x27;enterprise&#x27;&#10;LIMIT 10&#10;</code></pre>
<pre><code class="language-sql">&#45;- In WHERE (comparison)&#10;SELECT z.domain, z.plan, z.requests_30d&#10;FROM my_namespace.zones z&#10;WHERE z.requests_30d &gt; (&#10;    SELECT AVG(requests_30d) FROM my_namespace.zones&#10;)&#10;ORDER BY z.requests_30d DESC&#10;LIMIT 20&#10;</code></pre>
<hr />
<h2 id="where-clause">WHERE clause</h2>
<h3 id="syntax-4">Syntax</h3>
<pre><code class="language-sql">SELECT * FROM namespace_name.table_name WHERE condition [AND | OR condition ...]&#10;</code></pre>
<h3 id="conditions">Conditions</h3>
<h4 id="comparison-operators">Comparison operators</h4>
<p><code>=</code>, <code>!=</code>, <code>&lt;&gt;</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&lt;=</code>, <code>&gt;=</code></p>
<h4 id="null-checks">Null checks</h4>
<ul>
<li><code>column_name IS NULL</code></li>
<li><code>column_name IS NOT NULL</code></li>
</ul>
<h4 id="boolean-checks">Boolean checks</h4>
<ul>
<li><code>IS TRUE</code>, <code>IS FALSE</code>, <code>IS NOT TRUE</code>, <code>IS NOT FALSE</code></li>
<li><code>IS UNKNOWN</code>, <code>IS NOT UNKNOWN</code></li>
</ul>
<h4 id="range">Range</h4>
<ul>
<li><code>column_name BETWEEN value1 AND value2</code></li>
<li><code>column_name NOT BETWEEN value1 AND value2</code></li>
</ul>
<h4 id="list-membership">List membership</h4>
<ul>
<li><code>column_name IN ('value1', 'value2')</code></li>
<li><code>column_name NOT IN ('value1', 'value2')</code></li>
</ul>
<h4 id="pattern-matching">Pattern matching</h4>
<ul>
<li><code>column_name LIKE 'pattern'</code></li>
<li><code>column_name NOT LIKE 'pattern'</code></li>
<li><code>column_name ILIKE 'pattern'</code> (case-insensitive)</li>
<li><code>column_name NOT ILIKE 'pattern'</code></li>
<li><code>column_name SIMILAR TO 'regex_pattern'</code></li>
</ul>
<h4 id="logical-operators">Logical operators</h4>
<ul>
<li><code>AND</code></li>
<li><code>OR</code></li>
<li><code>NOT</code></li>
</ul>
<h3 id="examples-1">Examples</h3>
<pre><code class="language-sql">SELECT * FROM my_namespace.sales_data&#10;WHERE timestamp BETWEEN &#x27;2025-09-24T01:00:00Z&#x27; AND &#x27;2025-09-25T01:00:00Z&#x27;&#10;&#10;SELECT * FROM my_namespace.sales_data&#10;WHERE status = 200 AND response_time &gt; 1000&#10;&#10;SELECT * FROM my_namespace.sales_data&#10;WHERE (region = &#x27;North&#x27; OR region = &#x27;South&#x27;)&#10;  AND total_amount IS NOT NULL&#10;&#10;SELECT * FROM my_namespace.sales_data&#10;WHERE department ILIKE &#x27;%eng%&#x27;&#10;</code></pre>
<hr />
<h2 id="group-by-clause">GROUP BY clause</h2>
<h3 id="syntax-5">Syntax</h3>
<pre><code class="language-sql">SELECT column_list, aggregation_function(column)&#10;FROM namespace_name.table_name&#10;[WHERE conditions]&#10;GROUP BY column_list&#10;</code></pre>
<h3 id="examples-2">Examples</h3>
<pre><code class="language-sql">SELECT department, COUNT(*) AS dept_count&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;&#10;SELECT department, category, SUM(total_amount) AS total&#10;FROM my_namespace.sales_data&#10;GROUP BY department, category&#10;</code></pre>
<h3 id="grouping-sets-rollup-and-cube">GROUPING SETS, ROLLUP, and CUBE</h3>
<p>These extensions compute multiple groupings, including subtotals and grand totals, in a single query.</p>
<ul>
<li><strong><code>GROUPING SETS</code></strong>: Computes exactly the groupings you list. <code>()</code> produces the grand total.</li>
<li><strong><code>ROLLUP</code></strong>: Computes hierarchical subtotals from left to right. <code>ROLLUP(a, b)</code> groups by <code>(a, b)</code>, <code>(a)</code>, and <code>()</code>.</li>
<li><strong><code>CUBE</code></strong>: Computes every combination of the listed columns. <code>CUBE(a, b)</code> groups by <code>(a, b)</code>, <code>(a)</code>, <code>(b)</code>, and <code>()</code>.</li>
</ul>
<pre><code class="language-sql">&#45;- Subtotals per department plus a grand total&#10;SELECT department, SUM(total_amount) AS total&#10;FROM my_namespace.sales_data&#10;GROUP BY ROLLUP(department)&#10;&#10;&#45;- Every combination of department and category&#10;SELECT department, category, SUM(total_amount) AS total&#10;FROM my_namespace.sales_data&#10;GROUP BY CUBE(department, category)&#10;&#10;&#45;- Explicit groupings&#10;SELECT department, category, SUM(total_amount) AS total&#10;FROM my_namespace.sales_data&#10;GROUP BY GROUPING SETS ((department, category), (department), ())&#10;</code></pre>
<hr />
<h2 id="having-clause">HAVING clause</h2>
<h3 id="syntax-6">Syntax</h3>
<pre><code class="language-sql">SELECT column_list, aggregation_function(column) AS alias&#10;FROM namespace_name.table_name&#10;GROUP BY column_list&#10;HAVING aggregation_function(column) comparison_operator value&#10;</code></pre>
<h3 id="examples-3">Examples</h3>
<pre><code class="language-sql">SELECT department, COUNT(*) AS dept_count&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;HAVING COUNT(*) &gt; 1000&#10;&#10;SELECT region, SUM(total_amount) AS total&#10;FROM my_namespace.sales_data&#10;GROUP BY region&#10;HAVING SUM(total_amount) &gt; 1000000&#10;</code></pre>
<hr />
<h2 id="order-by-clause">ORDER BY clause</h2>
<h3 id="syntax-7">Syntax</h3>
<pre><code class="language-sql">ORDER BY expression [ASC | DESC] [, expression [ASC | DESC], ...]&#10;</code></pre>
<ul>
<li><strong>ASC</strong>: Ascending order (default)</li>
<li><strong>DESC</strong>: Descending order</li>
<li>Multi-column ordering is supported</li>
</ul>
<h3 id="examples-4">Examples</h3>
<pre><code class="language-sql">SELECT customer_id, total_amount&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;ORDER BY total_amount DESC&#10;LIMIT 50&#10;&#10;SELECT department, COUNT(*) AS dept_count&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;ORDER BY dept_count DESC, department ASC&#10;</code></pre>
<hr />
<h2 id="limit-clause">LIMIT clause</h2>
<h3 id="syntax-8">Syntax</h3>
<pre><code class="language-sql">LIMIT number&#10;</code></pre>
<ul>
<li><strong>Type</strong>: Integer only</li>
<li><strong>Default</strong>: 500</li>
</ul>
<h3 id="examples-5">Examples</h3>
<pre><code class="language-sql">SELECT * FROM my_namespace.sales_data LIMIT 100&#10;</code></pre>
<hr />
<h2 id="window-functions">Window functions</h2>
<p>Window functions compute a value across a set of rows related to the current row without collapsing them into a single output row. The window is defined inline with an <code>OVER (...)</code> clause containing an optional <code>PARTITION BY</code>, <code>ORDER BY</code>, and frame specification.</p>
<h3 id="syntax-9">Syntax</h3>
<pre><code class="language-sql">function(args) OVER (&#10;    [PARTITION BY expression [, ...]]&#10;    [ORDER BY expression [ASC | DESC] [, ...]]&#10;    [frame_specification]&#10;)&#10;</code></pre>
<h3 id="supported-functions">Supported functions</h3>
<table>
<thead>
<tr>
<th align="left">Category</th>
<th align="left">Functions</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Ranking</td>
<td align="left"><code>ROW_NUMBER</code>, <code>RANK</code>, <code>DENSE_RANK</code>, <code>PERCENT_RANK</code>, <code>CUME_DIST</code>, <code>NTILE</code></td>
</tr>
<tr>
<td align="left">Offset</td>
<td align="left"><code>LAG</code>, <code>LEAD</code>, <code>FIRST_VALUE</code>, <code>LAST_VALUE</code>, <code>NTH_VALUE</code></td>
</tr>
<tr>
<td align="left">Aggregate</td>
<td align="left"><code>SUM</code>, <code>AVG</code>, <code>COUNT</code>, <code>MIN</code>, <code>MAX</code>, and other aggregates used with <code>OVER</code></td>
</tr>
</tbody>
</table>
<h3 id="examples-6">Examples</h3>
<pre><code class="language-sql">&#45;- Rank rows within each partition&#10;SELECT customer_id, region,&#10;       ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) AS rank_in_region,&#10;       LAG(total_amount) OVER (PARTITION BY region ORDER BY total_amount DESC) AS prev_amount&#10;FROM my_namespace.sales_data&#10;&#10;&#45;- Running total with an explicit frame&#10;SELECT customer_id, total_amount,&#10;       SUM(total_amount) OVER (ORDER BY total_amount ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS running_total&#10;FROM my_namespace.sales_data&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11346.md")
</aside>
<h3 id="qualify">QUALIFY</h3>
<p><code>QUALIFY</code> filters rows based on the result of a window function, similar to how <code>HAVING</code> filters grouped rows.</p>
<pre><code class="language-sql">&#45;- Keep only the top 3 customers by amount in each region&#10;SELECT customer_id, region, total_amount&#10;FROM my_namespace.sales_data&#10;QUALIFY ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) &lt;= 3&#10;</code></pre>
<hr />
<h2 id="set-operations">Set operations</h2>
<p>Set operations combine the results of two or more <code>SELECT</code> statements.</p>
<h3 id="syntax-10">Syntax</h3>
<pre><code class="language-sql">SELECT ... FROM table1&#10;UNION | UNION ALL | INTERSECT | EXCEPT&#10;SELECT ... FROM table2&#10;</code></pre>
<h3 id="supported-operations">Supported operations</h3>
<table>
<thead>
<tr>
<th align="left">Operation</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>UNION</code></td>
<td align="left">Returns all rows from both queries, removing duplicates</td>
</tr>
<tr>
<td align="left"><code>UNION ALL</code></td>
<td align="left">Returns all rows from both queries, including duplicates</td>
</tr>
<tr>
<td align="left"><code>INTERSECT</code></td>
<td align="left">Returns only rows that appear in both query results</td>
</tr>
<tr>
<td align="left"><code>EXCEPT</code></td>
<td align="left">Returns rows from the first query that do not appear in the second</td>
</tr>
</tbody>
</table>
<h3 id="examples-7">Examples</h3>
<h4 id="union">Union</h4>
<pre><code class="language-sql">&#45;- Find zones that had either firewall blocks OR high-risk requests&#10;SELECT zone_id FROM my_namespace.firewall_events WHERE action = &#x27;block&#x27;&#10;UNION&#10;SELECT zone_id FROM my_namespace.http_requests WHERE risk_score &gt; 0.8&#10;</code></pre>
<h4 id="intersect">Intersect</h4>
<pre><code class="language-sql">&#45;- Find zones with both firewall blocks AND entries in the zones table&#10;SELECT zone_id FROM my_namespace.firewall_events WHERE action = &#x27;block&#x27;&#10;INTERSECT&#10;SELECT zone_id FROM my_namespace.zones WHERE plan = &#x27;enterprise&#x27;&#10;</code></pre>
<h4 id="except">Except</h4>
<pre><code class="language-sql">&#45;- Find enterprise zones that have no firewall events&#10;SELECT zone_id FROM my_namespace.zones WHERE plan = &#x27;enterprise&#x27;&#10;EXCEPT&#10;SELECT zone_id FROM my_namespace.firewall_events&#10;</code></pre>
<h3 id="requirements">Requirements</h3>
<ul>
<li>All queries in a set operation must return the same number of columns.</li>
<li>Corresponding columns must have compatible data types.</li>
<li>Column names in the result are taken from the first query.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11345.md")
</aside>
<hr />
<h2 id="explain">EXPLAIN</h2>
<p>Returns the execution plan for a query without running it.</p>
<pre><code class="language-sql">EXPLAIN SELECT department, COUNT(*) AS dept_count&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;GROUP BY department;&#10;</code></pre>
<h3 id="explain-format-json">EXPLAIN FORMAT JSON</h3>
<p>Returns the execution plan as structured JSON for programmatic analysis.</p>
<pre><code class="language-sql">EXPLAIN FORMAT JSON SELECT * FROM my_namespace.sales_data LIMIT 10;&#10;</code></pre>
<hr />
<h2 id="expressions">Expressions</h2>
<p>Expressions can be used in <code>SELECT</code>, <code>WHERE</code>, <code>GROUP BY</code>, <code>HAVING</code>, and <code>ORDER BY</code> clauses.</p>
<h3 id="literals">Literals</h3>
<pre><code class="language-sql">SELECT 42 AS int_val, 3.14 AS float_val, &#x27;hello&#x27; AS str_val, TRUE AS bool_val, NULL AS null_val&#10;FROM my_namespace.sales_data LIMIT 1&#10;</code></pre>
<h3 id="arithmetic-operators">Arithmetic operators</h3>
<p><code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>, <code>%</code></p>
<pre><code class="language-sql">SELECT customer_id, total_amount * 1.1 AS total_with_tax, total_amount % 10 AS remainder&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="string-concatenation">String concatenation</h3>
<pre><code class="language-sql">SELECT customer_id || &#x27; - &#x27; || region AS label&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="case-expressions">CASE expressions</h3>
<p>Searched form:</p>
<pre><code class="language-sql">SELECT customer_id,&#10;    CASE&#10;        WHEN total_amount &gt; 1000 THEN &#x27;high&#x27;&#10;        WHEN total_amount &gt; 100 THEN &#x27;medium&#x27;&#10;        ELSE &#x27;low&#x27;&#10;    END AS tier&#10;FROM my_namespace.sales_data&#10;LIMIT 10&#10;</code></pre>
<p>Simple form:</p>
<pre><code class="language-sql">SELECT customer_id,&#10;    CASE region&#10;        WHEN &#x27;North&#x27; THEN &#x27;N&#x27;&#10;        WHEN &#x27;South&#x27; THEN &#x27;S&#x27;&#10;        ELSE &#x27;Other&#x27;&#10;    END AS region_code&#10;FROM my_namespace.sales_data&#10;LIMIT 10&#10;</code></pre>
<h3 id="type-casting">Type casting</h3>
<pre><code class="language-sql">&#45;- CAST&#10;SELECT CAST(total_amount AS INT) AS amount_int FROM my_namespace.sales_data LIMIT 5&#10;&#10;&#45;- TRY_CAST (returns NULL on failure instead of error)&#10;SELECT TRY_CAST(customer_id AS INT) AS id_int FROM my_namespace.sales_data LIMIT 5&#10;&#10;&#45;- Shorthand (::)&#10;SELECT total_amount::INT AS amount_int FROM my_namespace.sales_data LIMIT 5&#10;</code></pre>
<h3 id="extract">EXTRACT</h3>
<pre><code class="language-sql">SELECT EXTRACT(YEAR FROM timestamp) AS yr,&#10;       EXTRACT(MONTH FROM timestamp) AS mo,&#10;       EXTRACT(DAY FROM timestamp) AS dy&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<hr />
<h2 id="data-type-reference">Data type reference</h2>
<table>
<thead>
<tr>
<th align="left">Type</th>
<th align="left">Description</th>
<th align="left">Example Values</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>integer</code></td>
<td align="left">Whole numbers</td>
<td align="left"><code>1</code>, <code>42</code>, <code>-10</code>, <code>0</code></td>
</tr>
<tr>
<td align="left"><code>float</code></td>
<td align="left">Decimal numbers</td>
<td align="left"><code>1.5</code>, <code>3.14</code>, <code>-2.7</code>, <code>0.0</code></td>
</tr>
<tr>
<td align="left"><code>string</code></td>
<td align="left">Text values</td>
<td align="left"><code>'hello'</code>, <code>'GET'</code>, <code>'2024-01-01'</code></td>
</tr>
<tr>
<td align="left"><code>boolean</code></td>
<td align="left">Boolean values</td>
<td align="left"><code>true</code>, <code>false</code></td>
</tr>
<tr>
<td align="left"><code>timestamp</code></td>
<td align="left">RFC3339</td>
<td align="left"><code>'2025-09-24T01:00:00Z'</code></td>
</tr>
<tr>
<td align="left"><code>date</code></td>
<td align="left">Date values</td>
<td align="left"><code>'2025-09-24'</code></td>
</tr>
<tr>
<td align="left"><code>struct</code></td>
<td align="left">Named fields</td>
<td align="left"><code>struct_col['field_name']</code></td>
</tr>
<tr>
<td align="left"><code>array</code></td>
<td align="left">Ordered list</td>
<td align="left"><code>array_col[1]</code> (1-indexed)</td>
</tr>
<tr>
<td align="left"><code>map</code></td>
<td align="left">Key-value pairs</td>
<td align="left"><code>map_keys(map_col)</code></td>
</tr>
</tbody>
</table>
<hr />
<h2 id="operator-precedence">Operator precedence</h2>
<ol>
<li><strong>Comparison operators</strong>: <code>=</code>, <code>!=</code>, <code>&lt;</code>, <code>&lt;=</code>, <code>&gt;</code>, <code>&gt;=</code>, <code>LIKE</code>, <code>BETWEEN</code>, <code>IS NULL</code>, <code>IS NOT NULL</code></li>
<li><strong>AND</strong> (higher precedence)</li>
<li><strong>OR</strong> (lower precedence)</li>
</ol>
<p>Use parentheses to override default precedence:</p>
<pre><code class="language-sql">SELECT * FROM my_namespace.sales_data WHERE (status = 404 OR status = 500) AND region = &#x27;North&#x27;&#10;</code></pre>
<hr />
<h2 id="complete-query-examples">Complete query examples</h2>
<h3 id="basic-query">Basic query</h3>
<pre><code class="language-sql">SELECT *&#10;FROM my_namespace.sales_data&#10;WHERE timestamp BETWEEN &#x27;2025-09-24T01:00:00Z&#x27; AND &#x27;2025-09-25T01:00:00Z&#x27;&#10;LIMIT 100&#10;</code></pre>
<h3 id="filtered-query-with-sorting">Filtered query with sorting</h3>
<pre><code class="language-sql">SELECT customer_id, timestamp, status, total_amount&#10;FROM my_namespace.sales_data&#10;WHERE status &gt;= 400 AND total_amount &gt; 5000&#10;ORDER BY total_amount DESC&#10;LIMIT 50&#10;</code></pre>
<h3 id="aggregation-with-having">Aggregation with HAVING</h3>
<pre><code class="language-sql">SELECT region, COUNT(*) AS region_count, AVG(total_amount) AS avg_amount&#10;FROM my_namespace.sales_data&#10;WHERE status = &#x27;completed&#x27;&#10;GROUP BY region&#10;HAVING COUNT(*) &gt; 1000&#10;ORDER BY avg_amount DESC&#10;LIMIT 20&#10;</code></pre>
<h3 id="conditional-categorization">Conditional categorization</h3>
<pre><code class="language-sql">SELECT customer_id,&#10;    CASE&#10;        WHEN total_amount &gt;= 1000 THEN &#x27;Premium&#x27;&#10;        WHEN total_amount &gt;= 100 THEN &#x27;Standard&#x27;&#10;        ELSE &#x27;Basic&#x27;&#10;    END AS tier,&#10;    total_amount&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;ORDER BY total_amount DESC&#10;LIMIT 20&#10;</code></pre>
