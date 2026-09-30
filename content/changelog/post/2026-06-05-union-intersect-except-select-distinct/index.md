---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/
  description: New updates and improvements at Cloudflare.
  full_title: R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT · Changelog
  head_html: <title>R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/#page","headline":"R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-05-union-intersect-except-select-distinct/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 8, 2026</time><h2 id="post-title">R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT</h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p><a href="/r2-sql/">R2 SQL</a> now supports set operations (<code>UNION</code>, <code>INTERSECT</code>, <code>EXCEPT</code>) and <code>SELECT DISTINCT</code>, expanding the range of analytical queries you can run directly on <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables in <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<h4 id="set-operations">Set operations</h4>
<p>Combine the results of multiple <code>SELECT</code> statements:</p>
<ul>
<li><strong><code>UNION</code></strong> — returns all rows from both queries, removing duplicates</li>
<li><strong><code>UNION ALL</code></strong> — returns all rows from both queries, including duplicates</li>
<li><strong><code>INTERSECT</code></strong> — returns only rows that appear in both queries</li>
<li><strong><code>EXCEPT</code></strong> — returns rows from the first query that do not appear in the second</li>
</ul>
<pre tabindex="0"><code class="language-sql">&#45;- Find zones that had either firewall blocks OR high-risk requests&#10;SELECT zone_id FROM my_namespace.firewall_events WHERE action = &#x27;block&#x27;&#10;UNION&#10;SELECT zone_id FROM my_namespace.http_requests WHERE risk_score &gt; 0.8&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Find zones with both firewall blocks AND high traffic&#10;SELECT zone_id FROM my_namespace.firewall_events WHERE action = &#x27;block&#x27;&#10;INTERSECT&#10;SELECT zone_id FROM my_namespace.http_requests&#10;GROUP BY zone_id&#10;HAVING COUNT(*) &gt; 10000&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Find enterprise zones that have not been compacted&#10;SELECT zone_id FROM my_namespace.zones WHERE plan = &#x27;enterprise&#x27;&#10;EXCEPT&#10;SELECT zone_id FROM my_namespace.compaction_history&#10;</code></pre>
<h4 id="select-distinct">Select distinct</h4>
<p>Eliminate duplicate rows from query results:</p>
<pre tabindex="0"><code class="language-sql">SELECT DISTINCT region, department&#10;FROM my_namespace.sales_data&#10;WHERE total_amount &gt; 1000&#10;ORDER BY region, department&#10;LIMIT 100&#10;</code></pre>
<p>For large datasets where approximate results are acceptable, <code>approx_distinct()</code> remains a faster alternative for counting unique values.</p>
<p>For the full syntax reference, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>. For performance guidance, refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a>.</p>
</div></article></div>
