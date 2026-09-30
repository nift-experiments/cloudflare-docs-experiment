---
cp9:
  canonical: https://developers.cloudflare.com/r2-sql/troubleshooting/
  description: Troubleshoot common R2 SQL errors including query structure, type, and timeout issues.
  full_title: Troubleshooting guide · R2 SQL docs
  head_html: <title>Troubleshooting guide · R2 SQL docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot common R2 SQL errors including query structure, type, and timeout issues."><link rel="canonical" href="https://developers.cloudflare.com/r2-sql/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2-sql/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting guide · R2 SQL docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot common R2 SQL errors including query structure, type, and timeout issues."><meta property="og:url" content="https://developers.cloudflare.com/r2-sql/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2 SQL"><meta name="algolia_product_filter" content="R2 SQL"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="R2 SQL"><meta name="pcx_tags" content="SQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2-sql/troubleshooting/#page","headline":"Troubleshooting guide \u00b7 R2 SQL docs","description":"Troubleshoot common R2 SQL errors including query structure, type, and timeout issues.","url":"https://developers.cloudflare.com/r2-sql/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SQL"]}</script>
  markdown: true
  noindex: false
  route: /r2-sql/troubleshooting/
  schema: 1
---
<p>This guide covers potential errors and limitations you may encounter when using R2 SQL. R2 SQL is in open beta, and supported functionality will evolve and change over time.</p>
<h2 id="query-structure-errors">Query structure errors</h2>
<h3 id="missing-required-clauses">Missing required clauses</h3>
<div className="error-box">
<pre tabindex="0"><code>**Error**: `expected exactly 1 table in FROM clause`&#10;</code></pre>
</div>
<p><strong>Problem</strong>: R2 SQL requires a <code>FROM</code> clause in your query.</p>
<pre tabindex="0"><code class="language-sql">&#45;- Invalid - Missing FROM clause&#10;SELECT user_id WHERE status = 200;&#10;&#10;&#45;- Valid&#10;SELECT user_id&#10;FROM my_namespace.http_requests&#10;WHERE status = 200 AND timestamp BETWEEN &#x27;2025-09-24T01:00:00Z&#x27; AND &#x27;2025-09-25T01:00:00Z&#x27;;&#10;</code></pre>
<p><strong>Solution</strong>: Always include <code>FROM</code> with a fully qualified table name (<code>namespace_name.table_name</code>).</p>
<hr />
<h2 id="from-clause-issues">FROM clause issues</h2>
<h3 id="join-performance-issues">Join performance issues</h3>
<p><strong>Symptom</strong>: Query returns 502 Bad Gateway or times out.</p>
<p><strong>Problem</strong>: Multi-way joins across large tables can exceed resource limits, especially with <code>COUNT(DISTINCT)</code> or other memory-intensive aggregations.</p>
<pre tabindex="0"><code class="language-sql">&#45;- May timeout: cross-joining two large fact tables&#10;SELECT COUNT(DISTINCT h.ray_id), COUNT(DISTINCT f.event_id)&#10;FROM my_namespace.http_requests h&#10;INNER JOIN my_namespace.firewall_events f ON h.zone_id = f.zone_id&#10;</code></pre>
<p><strong>Solution</strong>:</p>
<ul>
<li>Add <code>WHERE</code> filters to reduce intermediate result sizes.</li>
<li>Join through dimension tables instead of directly joining fact tables.</li>
<li>Use <code>approx_distinct()</code> instead of <code>COUNT(DISTINCT)</code> for approximate counts.</li>
<li>Break complex multi-way joins into smaller queries using CTEs or sequential queries.</li>
</ul>
<pre tabindex="0"><code class="language-sql">&#45;- Better: filter both sides and use approx_distinct&#10;SELECT z.plan,&#10;       approx_distinct(h.ray_id) AS unique_requests&#10;FROM my_namespace.zones z&#10;INNER JOIN my_namespace.http_requests h ON z.zone_id = h.zone_id&#10;WHERE z.plan = &#x27;enterprise&#x27;&#10;  AND h.status_code &gt;= 400&#10;GROUP BY z.plan&#10;</code></pre>
<h3 id="not-in-on-nullable-columns"><code>NOT IN</code> on nullable columns</h3>
<p><strong>Symptom</strong>: <code>NOT IN</code> subquery returns unexpected results or errors.</p>
<p><strong>Problem</strong>: <code>NOT IN</code> subqueries are not supported when the subquery column can contain <code>NULL</code> values.</p>
<pre tabindex="0"><code class="language-sql">&#45;- Fails: nullable_col may contain NULLs&#10;SELECT zone_id&#10;FROM my_namespace.http_requests&#10;WHERE zone_id NOT IN (&#10;    SELECT nullable_col FROM my_namespace.other_table&#10;)&#10;LIMIT 20&#10;</code></pre>
<p><strong>Solution</strong>: Use <code>NOT EXISTS</code> with a correlated subquery instead.</p>
<pre tabindex="0"><code class="language-sql">&#45;- Works: NOT EXISTS handles NULLs correctly&#10;SELECT h.zone_id&#10;FROM my_namespace.http_requests h&#10;WHERE NOT EXISTS (&#10;    SELECT 1 FROM my_namespace.other_table o&#10;    WHERE o.nullable_col = h.zone_id&#10;)&#10;LIMIT 20&#10;</code></pre>
<h3 id="correlated-subquery-performance">Correlated subquery performance</h3>
<p><strong>Symptom</strong>: <code>EXISTS</code> or <code>NOT EXISTS</code> subquery runs slowly.</p>
<p><strong>Problem</strong>: Correlated subqueries with complex conditions can be slow because the inner query is evaluated for each row of the outer query.</p>
<pre tabindex="0"><code class="language-sql">&#45;- Slower: multiple filter conditions in correlated subquery&#10;SELECT z.domain&#10;FROM my_namespace.zones z&#10;WHERE EXISTS (&#10;    SELECT 1 FROM my_namespace.firewall_events f&#10;    WHERE f.zone_id = z.zone_id&#10;      AND f.risk_score &gt; 0.9&#10;      AND f.colo = &#x27;SJC&#x27;&#10;)&#10;LIMIT 20&#10;</code></pre>
<p><strong>Solution</strong>:</p>
<ul>
<li>Simplify correlated conditions where possible.</li>
<li>Consider rewriting as a <code>JOIN</code> with <code>GROUP BY</code> instead of <code>EXISTS</code>.</li>
<li>Use an <code>IN</code> subquery with pre-aggregated results instead of <code>EXISTS</code>.</li>
</ul>
<hr />
<h2 id="where-clause-issues">WHERE clause issues</h2>
<h3 id="json-object-filtering">JSON object filtering</h3>
<div className="error-box">
<pre tabindex="0"><code>**Error**: `unsupported binary operator` or `Error during planning: could not&#10;parse compound`&#10;</code></pre>
</div>
<p><strong>Problem</strong>: JSON functions are not yet implemented. You cannot filter on fields inside JSON objects using JSON path operators.</p>
<pre tabindex="0"><code class="language-sql">&#45;- Invalid - JSON path operators not supported&#10;SELECT * FROM my_namespace.requests WHERE json_data-&gt;&gt;&#x27;level&#x27; = &#x27;error&#x27;&#10;&#10;&#45;- Valid - Filter on the entire JSON column&#10;SELECT * FROM my_namespace.logs WHERE json_data IS NOT NULL LIMIT 100&#10;</code></pre>
<p><strong>Solution</strong>:</p>
<ul>
<li>Denormalize frequently queried JSON fields into separate columns.</li>
<li>Filter on the entire JSON field, and handle parsing in your application.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/506.md")
</aside>
<hr />
<h2 id="limit-clause-issues">LIMIT clause issues</h2>
<h3 id="invalid-limit-values">Invalid limit values</h3>
<div className="error-box">
<p><strong>Error</strong>: <code>maximum LIMIT is 10000</code></p>
</div>
<p><strong>Problem</strong>: LIMIT values must be between 1 and 10,000.</p>
<pre tabindex="0"><code class="language-sql">&#45;- Invalid - Out of range&#10;SELECT * FROM my_namespace.events LIMIT 50000&#10;&#10;&#45;- Valid&#10;SELECT * FROM my_namespace.events LIMIT 10000&#10;</code></pre>
<p><strong>Solution</strong>: Use LIMIT values between 1 and 10,000.</p>
<h3 id="pagination-attempts">Pagination attempts</h3>
<div className="error-box">
<pre tabindex="0"><code>**Error**: `unsupported feature: OFFSET clause is not supported`&#10;</code></pre>
</div>
<p><strong>Problem</strong>: OFFSET is not supported.</p>
<pre tabindex="0"><code class="language-sql">&#45;- Invalid - Pagination not supported&#10;SELECT * FROM my_namespace.events LIMIT 100 OFFSET 200&#10;&#10;&#45;- Valid - Use cursor-based pagination with ORDER BY and WHERE&#10;&#45;- Page 1&#10;SELECT * FROM my_namespace.events&#10;WHERE timestamp &gt;= &#x27;2024-01-01&#x27;&#10;ORDER BY timestamp&#10;LIMIT 100&#10;&#10;&#45;- Page 2 - Use the last timestamp from the previous page&#10;SELECT * FROM my_namespace.events&#10;WHERE timestamp &gt; &#x27;2024-01-01T10:30:00Z&#x27;&#10;ORDER BY timestamp&#10;LIMIT 100&#10;</code></pre>
<p><strong>Solution</strong>: Implement cursor-based pagination using <code>ORDER BY</code> and <code>WHERE</code> conditions.</p>
<hr />
<h2 id="schema-issues">Schema issues</h2>
<h3 id="ddl-and-dml-operations">DDL and DML operations</h3>
<div className="error-box">
<p><strong>Error</strong>: <code>only read-only queries are allowed</code></p>
</div>
<p><strong>Problem</strong>: R2 SQL is a read-only query engine. DDL and DML statements are not supported.</p>
<pre tabindex="0"><code class="language-sql">&#45;- Invalid - Schema changes not supported&#10;ALTER TABLE my_namespace.events ADD COLUMN new_field STRING&#10;UPDATE my_namespace.events SET status = 200 WHERE user_id = &#x27;123&#x27;&#10;CREATE TABLE my_namespace.test (id INT)&#10;DROP TABLE my_namespace.events&#10;</code></pre>
<p><strong>Solution</strong>: Manage your schema through your data ingestion pipeline and R2 Data Catalog.</p>
<hr />
<h2 id="performance-optimization">Performance optimization</h2>
<h3 id="query-performance-issues">Query performance issues</h3>
<p>If your queries are running slowly:</p>
<ol>
<li><strong>Always include partition (timestamp) filters</strong>: This is the most important optimization.</li>
</ol>
<pre tabindex="0"><code class="language-sql">&#45;- Good - Narrows data scan to one day&#10;SELECT * FROM my_namespace.events&#10;WHERE timestamp BETWEEN &#x27;2024-01-01&#x27; AND &#x27;2024-01-02&#x27;&#10;LIMIT 100&#10;</code></pre>
<ol start="2">
<li><strong>Use selective filtering</strong>: Include specific conditions to reduce result sets.</li>
</ol>
<pre tabindex="0"><code class="language-sql">&#45;- Good - Multiple filters reduce scanned data&#10;SELECT * FROM my_namespace.events&#10;WHERE status = 200 AND region = &#x27;US&#x27; AND timestamp &gt; &#x27;2024-01-01&#x27;&#10;LIMIT 100&#10;</code></pre>
<ol start="3">
<li><strong>Select specific columns</strong>: Avoid <code>SELECT *</code> when you only need a few fields.</li>
</ol>
<pre tabindex="0"><code class="language-sql">&#45;- Good - Only reads the columns you need&#10;SELECT user_id, status, timestamp&#10;FROM my_namespace.events&#10;WHERE timestamp &gt; &#x27;2024-01-01&#x27;&#10;LIMIT 100&#10;</code></pre>
<ol start="4">
<li><strong>Use EXPLAIN to inspect the execution plan</strong>: Verify that predicate pushdown and file pruning are working.</li>
</ol>
<pre tabindex="0"><code class="language-sql">EXPLAIN SELECT user_id, status&#10;FROM my_namespace.events&#10;WHERE timestamp &gt; &#x27;2024-01-01&#x27; AND status = 200&#10;</code></pre>
<ol start="5">
<li><strong>Enable compaction</strong>: Enable compaction in R2 Data Catalog to reduce the number of small files scanned per query.</li>
</ol>
