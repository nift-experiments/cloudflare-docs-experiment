<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 15, 2026</time><h2 id="post-title">R2 SQL now supports JOINs, subqueries, and multi-table queries</h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p><a href="/r2-sql/">R2 SQL</a> is Cloudflare's serverless, distributed SQL engine for querying <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>. R2 SQL runs directly on Cloudflare's global network with no infrastructure to manage, so you can analyze data in R2 without exporting it to an external warehouse.</p>
<p>R2 SQL now supports joining multiple Iceberg tables in a single query. You can combine tables with JOINs, filter with subqueries, and define multi-table CTEs to build complex analytical queries.</p>
<h4 id="new-capabilities">New capabilities</h4>
<ul>
<li><strong>JOINs</strong> — <code>INNER JOIN</code>, <code>LEFT JOIN</code>, <code>RIGHT JOIN</code>, <code>FULL OUTER JOIN</code>, <code>CROSS JOIN</code>, and implicit joins (comma-separated <code>FROM</code> with conditions in <code>WHERE</code>)</li>
<li><strong>Subqueries</strong> — <code>IN</code> / <code>NOT IN</code>, <code>EXISTS</code> / <code>NOT EXISTS</code>, scalar subqueries in <code>SELECT</code> / <code>WHERE</code> / <code>HAVING</code>, and derived tables (subqueries in <code>FROM</code>)</li>
<li><strong>Multi-table CTEs</strong> — <code>WITH</code> clauses can reference different tables and include JOINs</li>
<li><strong>Self-joins</strong> — join a table with itself using different aliases</li>
<li><strong>Multi-way joins</strong> — join three or more tables in a single query</li>
</ul>
<h4 id="examples">Examples</h4>
<h4 id="two-table-join-with-aggregation">Two-table JOIN with aggregation</h4>
<pre><code class="language-sql">SELECT z.domain, z.plan, COUNT(*) AS request_count&#10;FROM my_namespace.zones z&#10;INNER JOIN my_namespace.http_requests h ON z.zone_id = h.zone_id&#10;WHERE z.plan = &#x27;enterprise&#x27;&#10;GROUP BY z.domain, z.plan&#10;ORDER BY request_count DESC&#10;LIMIT 20&#10;</code></pre>
<h4 id="exists-subquery"><code>EXISTS</code> subquery</h4>
<pre><code class="language-sql">SELECT z.domain, z.plan&#10;FROM my_namespace.zones z&#10;WHERE EXISTS (&#10;    SELECT 1 FROM my_namespace.firewall_events f&#10;    WHERE f.zone_id = z.zone_id AND f.action = &#x27;block&#x27;&#10;)&#10;ORDER BY z.domain&#10;LIMIT 20&#10;</code></pre>
<h4 id="multi-table-cte-with-join">Multi-table CTE with JOIN</h4>
<pre><code class="language-sql">WITH top_zones AS (&#10;    SELECT zone_id, COUNT(*) AS req_count&#10;    FROM my_namespace.http_requests&#10;    GROUP BY zone_id&#10;    ORDER BY req_count DESC&#10;    LIMIT 50&#10;),&#10;zone_threats AS (&#10;    SELECT zone_id, COUNT(*) AS threat_count&#10;    FROM my_namespace.firewall_events&#10;    WHERE risk_score &gt; 0.5&#10;    GROUP BY zone_id&#10;)&#10;SELECT tz.zone_id, tz.req_count, COALESCE(zt.threat_count, 0) AS threat_count&#10;FROM top_zones tz&#10;LEFT JOIN zone_threats zt ON tz.zone_id = zt.zone_id&#10;ORDER BY tz.req_count DESC&#10;LIMIT 20&#10;</code></pre>
<p>For the full syntax reference, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>. For performance guidance with joins, refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a>.</p>
</div></article></div>
