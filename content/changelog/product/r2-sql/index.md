<h1 id="changelog">Changelog</h1>

<h2 id="billing-is-now-enabled-for-r2-sql"><a href="/changelog/post/2026-08-03-r2-sql-billing-enabled/">Billing is now enabled for R2 SQL</a></h2>
<p><em>2026-08-03</em></p>
<p>Billing is now enabled for <a href="/r2-sql/">R2 SQL</a> on non-enterprise accounts. R2 SQL usage beyond the included free tier will appear on your next invoice.</p>
<p>R2 SQL charges based on a single dimension:</p>
<ul>
<li><strong>Data scanned</strong>: $0.0025 / GB ($2.50 / TB) of compressed data read from R2 to execute your query.</li>
</ul>
<p>All plans include 10 GB of data scanned per month. Each query is billed for a minimum of 10 MB of data scanned. R2 SQL pricing is additive to standard <a href="/r2/pricing/">R2 storage and operations</a> and <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog</a> charges. R2 does not charge for egress, so there is no additional data transfer cost.</p>
<p>For example, a user who stores 500 GB of Parquet data in R2 Data Catalog and runs queries that scan a total of 50 GB of compressed data during the month would be billed as follows:</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Usage</th>
<th>Included</th>
<th>Billable</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>R2 storage</td>
<td>500 GB-month</td>
<td>10 GB-month</td>
<td>490 GB-month</td>
<td>$7.35</td>
</tr>
<tr>
<td>R2 SQL (data scanned)</td>
<td>50 GB</td>
<td>10 GB</td>
<td>40 GB</td>
<td>$0.10</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$7.45</strong></td>
</tr>
</tbody>
</table>
<p>For full pricing details and billing examples, refer to <a href="/r2-sql/platform/pricing/">R2 SQL pricing</a>.</p>


<h2 id="query-r2-data-catalog-tables-with-r2-sql-from-the-dashboard"><a href="/changelog/post/2026-07-08-query-r2-sql-from-dashboard/">Query R2 Data Catalog tables with R2 SQL from the dashboard</a></h2>
<p><em>2026-07-08</em></p>
<p>You can now query your <a href="/r2-data-catalog/">R2 Data Catalog</a> tables with <a href="/r2-sql/">R2 SQL</a> directly from the Cloudflare dashboard, without installing a CLI or wiring up a client. This makes it easy to explore your <a href="https://iceberg.apache.org/">Apache Iceberg</a> data, validate queries, and inspect results in one place.</p>
<img src="/assets/upstream/images/r2-sql/r2-sql-studio.png" alt="R2 SQL Query Editor" />
<p>To get started, go to <a href="https://dash.cloudflare.com/?to=/:account/data-catalog/overview">R2 Data Catalog</a> in the Cloudflare dashboard and select <strong>Query data</strong> to launch the built-in SQL editor. From there you can:</p>
<ul>
<li><strong>Write and run queries interactively</strong> — Iterate on R2 SQL directly in the browser with syntax highlighting and autocomplete, instead of re-running commands through Wrangler or the REST API.</li>
<li><strong>Explore your data</strong> — Explore your namespaces and tables alongside the editor so you can discover what's queryable without leaving the page or using other tools.</li>
<li><strong>Understand results and performance</strong> — View result sets with per-query statistics, export them, and get helpful <code>EXPLAIN</code> outputs to see exactly how a query runs.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17743.md")</aside>


<h2 id="r2-sql-now-supports-window-functions-distinct-and-set-operations"><a href="/changelog/post/2026-06-21-window-functions-distinct-set-operations/">R2 SQL now supports window functions, DISTINCT, and set operations</a></h2>
<p><em>2026-06-22</em></p>
<p>R2 SQL now supports window functions, <code>SELECT DISTINCT</code>, set operations, and additional aggregates, making it easier to write analytical queries without preprocessing your data elsewhere.</p>
<p><a href="/r2-sql/">R2 SQL</a> is Cloudflare's serverless, distributed SQL engine for querying <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<h4 id="2026-06-21-window-functions-distinct-set-operations-new-capabilities">New capabilities</h4>
<ul>
<li><strong>Window functions</strong> — <code>ROW_NUMBER</code>, <code>RANK</code>, <code>DENSE_RANK</code>, <code>PERCENT_RANK</code>, <code>CUME_DIST</code>, <code>NTILE</code>, <code>LAG</code>, <code>LEAD</code>, <code>FIRST_VALUE</code>, <code>LAST_VALUE</code>, <code>NTH_VALUE</code>, and aggregates with an <code>OVER (...)</code> clause, including <code>PARTITION BY</code> and explicit frames</li>
<li><strong>QUALIFY</strong> — filter rows based on a window function result</li>
<li><strong>DISTINCT</strong> — <code>SELECT DISTINCT</code>, <code>DISTINCT ON (...)</code>, and the <code>DISTINCT</code> modifier on aggregates such as <code>COUNT(DISTINCT ...)</code></li>
<li><strong>Set operations</strong> — <code>UNION</code>, <code>UNION ALL</code>, <code>INTERSECT</code>, and <code>EXCEPT</code></li>
<li><strong>Grouping extensions</strong> — <code>GROUPING SETS</code>, <code>ROLLUP</code>, and <code>CUBE</code></li>
<li><strong>Exact aggregates</strong> — <code>MEDIAN</code>, <code>PERCENTILE_CONT</code>, <code>ARRAY_AGG</code>, and <code>STRING_AGG</code></li>
</ul>
<h4 id="2026-06-21-window-functions-distinct-set-operations-examples">Examples</h4>
<h4 id="2026-06-21-window-functions-distinct-set-operations-rank-rows-with-a-window-function">Rank rows with a window function</h4>
<pre><code class="language-sql">SELECT customer_id, region,&#10;       ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) AS rank_in_region&#10;FROM my_namespace.sales_data&#10;</code></pre>
<h4 id="2026-06-21-window-functions-distinct-set-operations-filter-with-qualify">Filter with QUALIFY</h4>
<pre><code class="language-sql">SELECT customer_id, region, total_amount&#10;FROM my_namespace.sales_data&#10;QUALIFY ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) &lt;= 3&#10;</code></pre>
<h4 id="2026-06-21-window-functions-distinct-set-operations-combine-tables-with-a-set-operation">Combine tables with a set operation</h4>
<pre><code class="language-sql">SELECT customer_id FROM my_namespace.sales_data&#10;EXCEPT&#10;SELECT customer_id FROM my_namespace.archived_sales&#10;</code></pre>
<p>The named <code>WINDOW</code> clause is not supported — inline the <code>OVER (...)</code> specification at each call site. For the full syntax reference, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>. For supported features and performance guidance, refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a>.</p>


<h2 id="r2-sql-now-supports-union-intersect-except-and-select-distinct"><a href="/changelog/post/2026-06-05-union-intersect-except-select-distinct/">R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT</a></h2>
<p><em>2026-06-08</em></p>
<p><a href="/r2-sql/">R2 SQL</a> now supports set operations (<code>UNION</code>, <code>INTERSECT</code>, <code>EXCEPT</code>) and <code>SELECT DISTINCT</code>, expanding the range of analytical queries you can run directly on <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables in <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<h4 id="2026-06-05-union-intersect-except-select-distinct-set-operations">Set operations</h4>
<p>Combine the results of multiple <code>SELECT</code> statements:</p>
<ul>
<li><strong><code>UNION</code></strong> — returns all rows from both queries, removing duplicates</li>
<li><strong><code>UNION ALL</code></strong> — returns all rows from both queries, including duplicates</li>
<li><strong><code>INTERSECT</code></strong> — returns only rows that appear in both queries</li>
<li><strong><code>EXCEPT</code></strong> — returns rows from the first query that do not appear in the second</li>
</ul>
<pre><code class="language-sql">&#45;- Find zones that had either firewall blocks OR high-risk requests&#10;SELECT zone_id FROM my_namespace.firewall_events WHERE action = &#x27;block&#x27;&#10;UNION&#10;SELECT zone_id FROM my_namespace.http_requests WHERE risk_score &gt; 0.8&#10;</code></pre>
<pre><code class="language-sql">&#45;- Find zones with both firewall blocks AND high traffic&#10;SELECT zone_id FROM my_namespace.firewall_events WHERE action = &#x27;block&#x27;&#10;INTERSECT&#10;SELECT zone_id FROM my_namespace.http_requests&#10;GROUP BY zone_id&#10;HAVING COUNT(*) &gt; 10000&#10;</code></pre>
<pre><code class="language-sql">&#45;- Find enterprise zones that have not been compacted&#10;SELECT zone_id FROM my_namespace.zones WHERE plan = &#x27;enterprise&#x27;&#10;EXCEPT&#10;SELECT zone_id FROM my_namespace.compaction_history&#10;</code></pre>
<h4 id="2026-06-05-union-intersect-except-select-distinct-select-distinct">Select distinct</h4>
<p>Eliminate duplicate rows from query results:</p>
<pre><code class="language-sql">SELECT DISTINCT region, department&#10;FROM my_namespace.sales_data&#10;WHERE total_amount &gt; 1000&#10;ORDER BY region, department&#10;LIMIT 100&#10;</code></pre>
<p>For large datasets where approximate results are acceptable, <code>approx_distinct()</code> remains a faster alternative for counting unique values.</p>
<p>For the full syntax reference, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>. For performance guidance, refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a>.</p>


<h2 id="r2-sql-pricing-announced"><a href="/changelog/post/2026-05-11-r2-sql-pricing-announced/">R2 SQL pricing announced</a></h2>
<p><em>2026-05-28</em></p>
<p><a href="/r2-sql/">R2 SQL</a> is a serverless, distributed query engine that runs SQL against <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>. R2 SQL now has published pricing based on a single dimension: the volume of compressed data scanned to execute your queries. At $2.50 / TB ($0.0025 / GB), R2 SQL is priced at half the cost of AWS Athena and less than half of Google BigQuery on-demand.</p>
<p>Billing is not yet enabled. We will provide at least 30 days notice before we start charging for R2 SQL usage.</p>
<p>Data scanned is measured on compressed bytes read from R2 object storage. This matches what you see in your R2 bucket — if a Parquet file is 100 MB on disk, scanning that file bills for 100 MB. Each query has a minimum billing increment of 10 MB.</p>
<p>All plans include 10 GB of data scanned per month. Standard <a href="/r2/pricing/">R2 storage and operations</a> and <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog</a> charges apply separately.</p>
<p>For full pricing details and billing examples, refer to <a href="/r2-sql/platform/pricing/">R2 SQL pricing</a>.</p>


<h2 id="r2-sql-now-supports-joins-subqueries-and-multi-table-queries"><a href="/changelog/post/2026-05-14-joins-subqueries-multi-table-queries/">R2 SQL now supports JOINs, subqueries, and multi-table queries</a></h2>
<p><em>2026-05-15</em></p>
<p><a href="/r2-sql/">R2 SQL</a> is Cloudflare's serverless, distributed SQL engine for querying <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>. R2 SQL runs directly on Cloudflare's global network with no infrastructure to manage, so you can analyze data in R2 without exporting it to an external warehouse.</p>
<p>R2 SQL now supports joining multiple Iceberg tables in a single query. You can combine tables with JOINs, filter with subqueries, and define multi-table CTEs to build complex analytical queries.</p>
<h4 id="2026-05-14-joins-subqueries-multi-table-queries-new-capabilities">New capabilities</h4>
<ul>
<li><strong>JOINs</strong> — <code>INNER JOIN</code>, <code>LEFT JOIN</code>, <code>RIGHT JOIN</code>, <code>FULL OUTER JOIN</code>, <code>CROSS JOIN</code>, and implicit joins (comma-separated <code>FROM</code> with conditions in <code>WHERE</code>)</li>
<li><strong>Subqueries</strong> — <code>IN</code> / <code>NOT IN</code>, <code>EXISTS</code> / <code>NOT EXISTS</code>, scalar subqueries in <code>SELECT</code> / <code>WHERE</code> / <code>HAVING</code>, and derived tables (subqueries in <code>FROM</code>)</li>
<li><strong>Multi-table CTEs</strong> — <code>WITH</code> clauses can reference different tables and include JOINs</li>
<li><strong>Self-joins</strong> — join a table with itself using different aliases</li>
<li><strong>Multi-way joins</strong> — join three or more tables in a single query</li>
</ul>
<h4 id="2026-05-14-joins-subqueries-multi-table-queries-examples">Examples</h4>
<h4 id="2026-05-14-joins-subqueries-multi-table-queries-two-table-join-with-aggregation">Two-table JOIN with aggregation</h4>
<pre><code class="language-sql">SELECT z.domain, z.plan, COUNT(*) AS request_count&#10;FROM my_namespace.zones z&#10;INNER JOIN my_namespace.http_requests h ON z.zone_id = h.zone_id&#10;WHERE z.plan = &#x27;enterprise&#x27;&#10;GROUP BY z.domain, z.plan&#10;ORDER BY request_count DESC&#10;LIMIT 20&#10;</code></pre>
<h4 id="2026-05-14-joins-subqueries-multi-table-queries-exists-subquery"><code>EXISTS</code> subquery</h4>
<pre><code class="language-sql">SELECT z.domain, z.plan&#10;FROM my_namespace.zones z&#10;WHERE EXISTS (&#10;    SELECT 1 FROM my_namespace.firewall_events f&#10;    WHERE f.zone_id = z.zone_id AND f.action = &#x27;block&#x27;&#10;)&#10;ORDER BY z.domain&#10;LIMIT 20&#10;</code></pre>
<h4 id="2026-05-14-joins-subqueries-multi-table-queries-multi-table-cte-with-join">Multi-table CTE with JOIN</h4>
<pre><code class="language-sql">WITH top_zones AS (&#10;    SELECT zone_id, COUNT(*) AS req_count&#10;    FROM my_namespace.http_requests&#10;    GROUP BY zone_id&#10;    ORDER BY req_count DESC&#10;    LIMIT 50&#10;),&#10;zone_threats AS (&#10;    SELECT zone_id, COUNT(*) AS threat_count&#10;    FROM my_namespace.firewall_events&#10;    WHERE risk_score &gt; 0.5&#10;    GROUP BY zone_id&#10;)&#10;SELECT tz.zone_id, tz.req_count, COALESCE(zt.threat_count, 0) AS threat_count&#10;FROM top_zones tz&#10;LEFT JOIN zone_threats zt ON tz.zone_id = zt.zone_id&#10;ORDER BY tz.req_count DESC&#10;LIMIT 20&#10;</code></pre>
<p>For the full syntax reference, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>. For performance guidance with joins, refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a>.</p>


<h2 id="r2-sql-adds-json-functions-explain-format-json-and-unpartitioned-table-support"><a href="/changelog/post/2026-04-20-r2-sql-json-functions-explain-format/">R2 SQL adds JSON functions, EXPLAIN FORMAT JSON, and unpartitioned table support</a></h2>
<p><em>2026-04-20</em></p>
<p><a href="/r2-sql/">R2 SQL</a> is Cloudflare's serverless, distributed, analytics query engine for querying <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<p>R2 SQL now supports functions for querying JSON data stored in Apache Iceberg tables, an easier way to parse query plans with <code>EXPLAIN FORMAT JSON</code>, and querying tables without partition keys stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<p>JSON functions extract and manipulate JSON values directly in SQL without client-side processing:</p>
<pre><code class="language-sql">SELECT&#10;  json_get_str(doc, &#x27;name&#x27;) AS name,&#10;  json_get_int(doc, &#x27;user&#x27;, &#x27;profile&#x27;, &#x27;level&#x27;) AS level,&#10;  json_get_bool(doc, &#x27;active&#x27;) AS is_active&#10;FROM my_namespace.sales_data&#10;WHERE json_contains(doc, &#x27;email&#x27;)&#10;</code></pre>
<p>For a full list of available functions, refer to <a href="/r2-sql/sql-reference/scalar-functions/#json-functions">JSON functions</a>.</p>
<p><code>EXPLAIN FORMAT JSON</code> returns query execution plans as structured JSON for programmatic analysis and observability integrations:</p>
<pre><code class="language-bash">npx wrangler r2 sql query &quot;${WAREHOUSE}&quot; &quot;EXPLAIN FORMAT JSON SELECT * FROM logpush.requests LIMIT 10;&quot;&#10;&#10;┌──────────────────────────────────────┐&#10;│ plan                                 │&#10;├──────────────────────────────────────┤&#10;│ {                                    │&#10;│   &quot;name&quot;: &quot;CoalescePartitionsExec&quot;,  │&#10;│   &quot;output_partitions&quot;: 1,            │&#10;│   &quot;rows&quot;: 10,                        │&#10;│   &quot;size_approx&quot;: &quot;310B&quot;,             │&#10;│   &quot;children&quot;: [                      │&#10;│     {                                │&#10;│       &quot;name&quot;: &quot;DataSourceExec&quot;,      │&#10;│       &quot;output_partitions&quot;: 4,        │&#10;│       &quot;rows&quot;: 28951,                 │&#10;│       &quot;size_approx&quot;: &quot;900.0KB&quot;,      │&#10;│       &quot;table&quot;: &quot;logpush.requests&quot;,   │&#10;│       &quot;files&quot;: 7,                    │&#10;│       &quot;bytes&quot;: 900019,               │&#10;│       &quot;projection&quot;: [                │&#10;│         &quot;__ingest_ts&quot;,               │&#10;│         &quot;CPUTimeMs&quot;,                 │&#10;│         &quot;DispatchNamespace&quot;,         │&#10;│         &quot;Entrypoint&quot;,                │&#10;│         &quot;Event&quot;,                     │&#10;│         &quot;EventTimestampMs&quot;,          │&#10;│         &quot;EventType&quot;,                 │&#10;│         &quot;Exceptions&quot;,                │&#10;│         &quot;Logs&quot;,                      │&#10;│         &quot;Outcome&quot;,                   │&#10;│         &quot;ScriptName&quot;,                │&#10;│         &quot;ScriptTags&quot;,                │&#10;│         &quot;ScriptVersion&quot;,             │&#10;│         &quot;WallTimeMs&quot;                 │&#10;│       ],                             │&#10;│       &quot;limit&quot;: 10                    │&#10;│     }                                │&#10;│   ]                                  │&#10;│ }                                    │&#10;└──────────────────────────────────────┘&#10;</code></pre>
<p>For more details, refer to <a href="/r2-sql/sql-reference/#explain">EXPLAIN</a>.</p>
<p>Unpartitioned Iceberg tables can now be queried directly, which is useful for smaller datasets or data without natural time dimensions. For tables with more than 1000 files, partitioning is still recommended for better performance.</p>
<p>Refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a> for the latest guidance on using R2 SQL.</p>


<h2 id="r2-sql-now-supports-over-190-new-functions-expressions-and-complex-types"><a href="/changelog/post/2026-03-23-expanded-sql-functions-expressions-complex-types/">R2 SQL now supports over 190 new functions, expressions, and complex types</a></h2>
<p><em>2026-03-23</em></p>
<p><a href="/r2-sql/">R2 SQL</a> now supports an expanded SQL grammar so you can write richer analytical queries without exporting data. This release adds CASE expressions, column aliases, arithmetic in clauses, 163 scalar functions, 33 aggregate functions, EXPLAIN, Common Table Expressions (CTEs),and full struct/array/map access. R2 SQL is Cloudflare's serverless, distributed, analytics query engine for querying <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>. This page documents the supported SQL syntax.</p>
<h4 id="2026-03-23-expanded-sql-functions-expressions-complex-types-highlights">Highlights</h4>
<ul>
<li><strong>Column aliases</strong> — <code>SELECT col AS alias</code> now works in all clauses</li>
<li><strong>CASE expressions</strong> — conditional logic directly in SQL (searched and simple forms)</li>
<li><strong>Scalar functions</strong> — 163 new functions across math, string, datetime, regex, crypto, encoding, and type inspection categories</li>
<li><strong>Aggregate functions</strong> — statistical (variance, stddev, correlation, regression), bitwise, boolean, and positional aggregates join the existing basic and approximate functions</li>
<li><strong>Complex types</strong> — query struct fields with bracket notation, use 46 array functions, and extract map keys/values</li>
<li><strong>Common table expressions (CTEs)</strong> — use <code>WITH ... AS</code> to define named temporary result sets. Chained CTEs are supported. All CTEs must reference the same single table.</li>
<li><strong>Full expression support</strong> — arithmetic, type casting (<code>CAST</code>, <code>TRY_CAST</code>, <code>::</code> shorthand), and <code>EXTRACT</code> in SELECT, WHERE, GROUP BY, HAVING, and ORDER BY</li>
</ul>
<h4 id="2026-03-23-expanded-sql-functions-expressions-complex-types-examples">Examples</h4>
<h4 id="2026-03-23-expanded-sql-functions-expressions-complex-types-case-expressions-with-statistical-aggregates">CASE expressions with statistical aggregates</h4>
<pre><code class="language-sql">SELECT source,&#10;    CASE&#10;        WHEN AVG(price) &gt; 30 THEN &#x27;premium&#x27;&#10;        WHEN AVG(price) &gt; 10 THEN &#x27;mid-tier&#x27;&#10;        ELSE &#x27;budget&#x27;&#10;    END AS tier,&#10;    round(stddev(price), 2) AS price_volatility,&#10;    approx_percentile_cont(price, 0.95) AS p95_price&#10;FROM my_namespace.sales_data&#10;GROUP BY source&#10;</code></pre>
<h4 id="2026-03-23-expanded-sql-functions-expressions-complex-types-struct-and-array-access">Struct and array access</h4>
<pre><code class="language-sql">SELECT product_name,&#10;    pricing[&#x27;price&#x27;] AS price,&#10;    array_to_string(tags, &#x27;, &#x27;) AS tag_list&#10;FROM my_namespace.products&#10;WHERE array_has(tags, &#x27;Action&#x27;)&#10;ORDER BY pricing[&#x27;price&#x27;] DESC&#10;LIMIT 10&#10;</code></pre>
<h4 id="2026-03-23-expanded-sql-functions-expressions-complex-types-chained-ctes-with-time-series-analysis">Chained CTEs with time-series analysis</h4>
<pre><code class="language-sql">WITH monthly AS (&#10;    SELECT date_trunc(&#x27;month&#x27;, sale_timestamp) AS month,&#10;        department,&#10;        COUNT(*) AS transactions,&#10;        round(AVG(total_amount), 2) AS avg_amount&#10;    FROM my_namespace.sales_data&#10;    WHERE sale_timestamp BETWEEN &#x27;2025-01-01T00:00:00Z&#x27; AND &#x27;2025-12-31T23:59:59Z&#x27;&#10;    GROUP BY date_trunc(&#x27;month&#x27;, sale_timestamp), department&#10;),&#10;ranked AS (&#10;    SELECT month, department, transactions, avg_amount,&#10;        CASE&#10;            WHEN avg_amount &gt; 1000 THEN &#x27;high-value&#x27;&#10;            WHEN avg_amount &gt; 500 THEN &#x27;mid-value&#x27;&#10;            ELSE &#x27;standard&#x27;&#10;        END AS tier&#10;    FROM monthly&#10;    WHERE transactions &gt; 100&#10;)&#10;SELECT * FROM ranked&#10;ORDER BY month, avg_amount DESC&#10;</code></pre>
<p>For the full function reference and syntax details, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>. For limitations and best practices, refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a>.</p>


<h2 id="r2-sql-now-supports-approximate-aggregation-functions"><a href="/changelog/post/2026-02-09-approximate-aggregation-functions/">R2 SQL now supports approximate aggregation functions</a></h2>
<p><em>2026-02-09</em></p>
<p>R2 SQL now supports five approximate aggregation functions for fast analysis of large datasets. These functions trade minor precision for improved performance on high-cardinality data.</p>
<h4 id="2026-02-09-approximate-aggregation-functions-new-functions">New functions</h4>
<ul>
<li><code>APPROX_PERCENTILE_CONT(column, percentile)</code> — Returns the approximate value at a given percentile (0.0 to 1.0). Works on integer and decimal columns.</li>
<li><code>APPROX_PERCENTILE_CONT_WITH_WEIGHT(column, weight, percentile)</code> — Weighted percentile calculation where each row contributes proportionally to its weight column value.</li>
<li><code>APPROX_MEDIAN(column)</code> — Returns the approximate median. Equivalent to <code>APPROX_PERCENTILE_CONT(column, 0.5)</code>.</li>
<li><code>APPROX_DISTINCT(column)</code> — Returns the approximate number of distinct values. Works on any column type.</li>
<li><code>APPROX_TOP_K(column, k)</code> — Returns the <code>k</code> most frequent values with their counts as a JSON array.</li>
</ul>
<p>All functions support <code>WHERE</code> filters. All except <code>APPROX_TOP_K</code> support <code>GROUP BY</code>.</p>
<h4 id="2026-02-09-approximate-aggregation-functions-examples">Examples</h4>
<pre><code class="language-sql">&#45;- Percentile analysis on revenue data&#10;SELECT approx_percentile_cont(total_amount, 0.25),&#10;       approx_percentile_cont(total_amount, 0.5),&#10;       approx_percentile_cont(total_amount, 0.75)&#10;FROM my_namespace.sales_data&#10;</code></pre>
<pre><code class="language-sql">&#45;- Median per department&#10;SELECT department, approx_median(total_amount)&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;</code></pre>
<pre><code class="language-sql">&#45;- Approximate distinct customers by region&#10;SELECT region, approx_distinct(customer_id)&#10;FROM my_namespace.sales_data&#10;GROUP BY region&#10;</code></pre>
<pre><code class="language-sql">&#45;- Top 5 most frequent departments&#10;SELECT approx_top_k(department, 5)&#10;FROM my_namespace.sales_data&#10;</code></pre>
<pre><code class="language-sql">&#45;- Combine approximate and standard aggregations&#10;SELECT COUNT(*),&#10;       AVG(total_amount),&#10;       approx_percentile_cont(total_amount, 0.5),&#10;       approx_distinct(customer_id)&#10;FROM my_namespace.sales_data&#10;WHERE region = &#x27;North&#x27;&#10;</code></pre>
<p>For the full syntax and additional examples, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>.</p>


<h2 id="r2-sql-now-supports-aggregations-and-schema-discovery"><a href="/changelog/post/2025-12-12-aggregation-support-and-more/">R2 SQL now supports aggregations and schema discovery</a></h2>
<p><em>2025-12-12</em></p>
<p>R2 SQL now supports aggregation functions, <code>GROUP BY</code>, <code>HAVING</code>, along with schema discovery commands to make it easy to explore your data catalog.</p>
<h4 id="2025-12-12-aggregation-support-and-more-aggregation-functions">Aggregation Functions</h4>
<p>You can now perform aggregations on Apache Iceberg tables in <a href="/r2-data-catalog/">R2 Data Catalog</a> using standard SQL functions including <code>COUNT(*)</code>, <code>SUM()</code>, <code>AVG()</code>, <code>MIN()</code>, and <code>MAX()</code>. Combine these with <code>GROUP BY</code> to analyze data across dimensions, and use <code>HAVING</code> to filter aggregated results.</p>
<pre><code class="language-sql">&#45;- Calculate average transaction amounts by department&#10;SELECT department, COUNT(*), AVG(total_amount)&#10;FROM my_namespace.sales_data&#10;WHERE region = &#x27;North&#x27;&#10;GROUP BY department&#10;HAVING COUNT(*) &gt; 50&#10;ORDER BY AVG(total_amount) DESC&#10;</code></pre>
<pre><code class="language-sql">&#45;- Find high-value departments&#10;SELECT department, SUM(total_amount)&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;HAVING SUM(total_amount) &gt; 50000&#10;</code></pre>
<h4 id="2025-12-12-aggregation-support-and-more-schema-discovery">Schema Discovery</h4>
<p>New metadata commands make it easy to explore your data catalog and understand table structures:</p>
<ul>
<li><code>SHOW DATABASES</code> or <code>SHOW NAMESPACES</code> - List all available namespaces</li>
<li><code>SHOW TABLES IN namespace_name</code> - List tables within a namespace</li>
<li><code>DESCRIBE namespace_name.table_name</code> - View table schema and column types</li>
</ul>
<pre><code class="language-bash">❯ npx wrangler r2 sql query &quot;{ACCOUNT_ID}_{BUCKET_NAME}&quot; &quot;DESCRIBE default.sales_data;&quot;&#10;&#10; ⛅️ wrangler 4.54.0&#10;─────────────────────────────────────────────&#10;&#10;┌──────────────────┬────────────────┬──────────┬─────────────────┬───────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────┐&#10;│ column_name      │ type           │ required │ initial_default │ write_default │ doc                                                                                               │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ sale_id          │ BIGINT         │ false    │                 │               │ Unique identifier for each sales transaction                                                      │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ sale_timestamp   │ TIMESTAMPTZ    │ false    │                 │               │ Exact date and time when the sale occurred (used for partitioning)                                │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ department       │ TEXT           │ false    │                 │               │ Product department (8 categories: Electronics, Beauty, Home, Toys, Sports, Food, Clothing, Books) │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ category         │ TEXT           │ false    │                 │               │ Product category grouping (4 categories: Premium, Standard, Budget, Clearance)                    │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ region           │ TEXT           │ false    │                 │               │ Geographic sales region (5 regions: North, South, East, West, Central)                            │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ product_id       │ INT            │ false    │                 │               │ Unique identifier for the product sold                                                            │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ quantity         │ INT            │ false    │                 │               │ Number of units sold in this transaction (range: 1-50)                                            │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ unit_price       │ DECIMAL(10, 2) │ false    │                 │               │ Price per unit in dollars (range: $5.00-$500.00)                                                  │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ total_amount     │ DECIMAL(10, 2) │ false    │                 │               │ Total sale amount before tax (quantity × unit_price with discounts applied)                       │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ discount_percent │ INT            │ false    │                 │               │ Discount percentage applied to this sale (0-50%)                                                  │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ tax_amount       │ DECIMAL(10, 2) │ false    │                 │               │ Tax amount collected on this sale                                                                 │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ profit_margin    │ DECIMAL(10, 2) │ false    │                 │               │ Profit margin on this sale as a decimal percentage                                                │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ customer_id      │ INT            │ false    │                 │               │ Unique identifier for the customer who made the purchase                                          │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ is_online_sale   │ BOOLEAN        │ false    │                 │               │ Boolean flag indicating if sale was made online (true) or in-store (false)                        │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ sale_date        │ DATE           │ false    │                 │               │ Calendar date of the sale (extracted from sale_timestamp)                                         │&#10;└──────────────────┴────────────────┴──────────┴─────────────────┴───────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────┘&#10;Read 0 B across 0 files from R2&#10;On average, 0 B / s&#10;</code></pre>
<p>To learn more about the new aggregation capabilities and schema discovery commands, check out the <a href="/r2-sql/sql-reference/">SQL reference</a>. If you're new to R2 SQL, visit our <a href="/r2-sql/get-started/">getting started guide</a> to begin querying your data.</p>


<h2 id="announcing-r2-sql"><a href="/changelog/post/2025-09-25-announcing-r2-sql-open-beta/">Announcing R2 SQL</a></h2>
<p><em>2025-09-25T13:00:00</em></p>
<p>Today, we're launching the <strong>open beta</strong> for <a href="/r2-sql/">R2 SQL</a>: A serverless, distributed query engine that can efficiently analyze petabytes of data in <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables managed by <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<p>R2 SQL is ideal for exploring analytical and time-series data stored in R2, such as logs, events from <a href="/pipelines/">Pipelines</a>, or clickstream and user behavior data.</p>
<p>If you already have a table in R2 Data Catalog, running queries is as simple as:</p>
<pre><code class="language-bash">npx wrangler r2 sql query YOUR_WAREHOUSE &quot;&#10;SELECT&#10;    user_id,&#10;    event_type,&#10;    value&#10;FROM events.user_events&#10;WHERE event_type = &#x27;CHANGELOG&#x27; or event_type = &#x27;BLOG&#x27;&#10;  AND __ingest_ts &gt; &#x27;2025-09-24T00:00:00Z&#x27;&#10;ORDER BY __ingest_ts DESC&#10;LIMIT 100&quot;&#10;</code></pre>
<p>To get started with R2 SQL, check out our <a href="/r2-sql/get-started/">getting started guide</a> or learn more about supported features in the <a href="/r2-sql/sql-reference/">SQL reference</a>. For a technical deep dive into how we built R2 SQL, read our <a href="https://blog.cloudflare.com/r2-sql-deep-dive/">blog post</a>.</p>



