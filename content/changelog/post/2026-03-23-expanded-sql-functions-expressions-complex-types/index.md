<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 23, 2026</time><h2 id="post-title">R2 SQL now supports over 190 new functions, expressions, and complex types</h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p><a href="/r2-sql/">R2 SQL</a> now supports an expanded SQL grammar so you can write richer analytical queries without exporting data. This release adds CASE expressions, column aliases, arithmetic in clauses, 163 scalar functions, 33 aggregate functions, EXPLAIN, Common Table Expressions (CTEs),and full struct/array/map access. R2 SQL is Cloudflare's serverless, distributed, analytics query engine for querying <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>. This page documents the supported SQL syntax.</p>
<h4 id="highlights">Highlights</h4>
<ul>
<li><strong>Column aliases</strong> — <code>SELECT col AS alias</code> now works in all clauses</li>
<li><strong>CASE expressions</strong> — conditional logic directly in SQL (searched and simple forms)</li>
<li><strong>Scalar functions</strong> — 163 new functions across math, string, datetime, regex, crypto, encoding, and type inspection categories</li>
<li><strong>Aggregate functions</strong> — statistical (variance, stddev, correlation, regression), bitwise, boolean, and positional aggregates join the existing basic and approximate functions</li>
<li><strong>Complex types</strong> — query struct fields with bracket notation, use 46 array functions, and extract map keys/values</li>
<li><strong>Common table expressions (CTEs)</strong> — use <code>WITH ... AS</code> to define named temporary result sets. Chained CTEs are supported. All CTEs must reference the same single table.</li>
<li><strong>Full expression support</strong> — arithmetic, type casting (<code>CAST</code>, <code>TRY_CAST</code>, <code>::</code> shorthand), and <code>EXTRACT</code> in SELECT, WHERE, GROUP BY, HAVING, and ORDER BY</li>
</ul>
<h4 id="examples">Examples</h4>
<h4 id="case-expressions-with-statistical-aggregates">CASE expressions with statistical aggregates</h4>
<pre><code class="language-sql">SELECT source,&#10;    CASE&#10;        WHEN AVG(price) &gt; 30 THEN &#x27;premium&#x27;&#10;        WHEN AVG(price) &gt; 10 THEN &#x27;mid-tier&#x27;&#10;        ELSE &#x27;budget&#x27;&#10;    END AS tier,&#10;    round(stddev(price), 2) AS price_volatility,&#10;    approx_percentile_cont(price, 0.95) AS p95_price&#10;FROM my_namespace.sales_data&#10;GROUP BY source&#10;</code></pre>
<h4 id="struct-and-array-access">Struct and array access</h4>
<pre><code class="language-sql">SELECT product_name,&#10;    pricing[&#x27;price&#x27;] AS price,&#10;    array_to_string(tags, &#x27;, &#x27;) AS tag_list&#10;FROM my_namespace.products&#10;WHERE array_has(tags, &#x27;Action&#x27;)&#10;ORDER BY pricing[&#x27;price&#x27;] DESC&#10;LIMIT 10&#10;</code></pre>
<h4 id="chained-ctes-with-time-series-analysis">Chained CTEs with time-series analysis</h4>
<pre><code class="language-sql">WITH monthly AS (&#10;    SELECT date_trunc(&#x27;month&#x27;, sale_timestamp) AS month,&#10;        department,&#10;        COUNT(*) AS transactions,&#10;        round(AVG(total_amount), 2) AS avg_amount&#10;    FROM my_namespace.sales_data&#10;    WHERE sale_timestamp BETWEEN &#x27;2025-01-01T00:00:00Z&#x27; AND &#x27;2025-12-31T23:59:59Z&#x27;&#10;    GROUP BY date_trunc(&#x27;month&#x27;, sale_timestamp), department&#10;),&#10;ranked AS (&#10;    SELECT month, department, transactions, avg_amount,&#10;        CASE&#10;            WHEN avg_amount &gt; 1000 THEN &#x27;high-value&#x27;&#10;            WHEN avg_amount &gt; 500 THEN &#x27;mid-value&#x27;&#10;            ELSE &#x27;standard&#x27;&#10;        END AS tier&#10;    FROM monthly&#10;    WHERE transactions &gt; 100&#10;)&#10;SELECT * FROM ranked&#10;ORDER BY month, avg_amount DESC&#10;</code></pre>
<p>For the full function reference and syntax details, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>. For limitations and best practices, refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a>.</p>
</div></article></div>
