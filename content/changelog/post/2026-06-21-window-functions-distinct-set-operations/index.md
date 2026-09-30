---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-21-window-functions-distinct-set-operations/
  description: New updates and improvements at Cloudflare.
  full_title: R2 SQL now supports window functions, DISTINCT, and set operations · Changelog
  head_html: <title>R2 SQL now supports window functions, DISTINCT, and set operations · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-21-window-functions-distinct-set-operations/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="R2 SQL now supports window functions, DISTINCT, and set operations · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-21-window-functions-distinct-set-operations/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-21-window-functions-distinct-set-operations/#page","headline":"R2 SQL now supports window functions, DISTINCT, and set operations \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-21-window-functions-distinct-set-operations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-21-window-functions-distinct-set-operations/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 22, 2026</time><h2 id="post-title">R2 SQL now supports window functions, DISTINCT, and set operations</h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p>R2 SQL now supports window functions, <code>SELECT DISTINCT</code>, set operations, and additional aggregates, making it easier to write analytical queries without preprocessing your data elsewhere.</p>
<p><a href="/r2-sql/">R2 SQL</a> is Cloudflare's serverless, distributed SQL engine for querying <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<h4 id="new-capabilities">New capabilities</h4>
<ul>
<li><strong>Window functions</strong> — <code>ROW_NUMBER</code>, <code>RANK</code>, <code>DENSE_RANK</code>, <code>PERCENT_RANK</code>, <code>CUME_DIST</code>, <code>NTILE</code>, <code>LAG</code>, <code>LEAD</code>, <code>FIRST_VALUE</code>, <code>LAST_VALUE</code>, <code>NTH_VALUE</code>, and aggregates with an <code>OVER (...)</code> clause, including <code>PARTITION BY</code> and explicit frames</li>
<li><strong>QUALIFY</strong> — filter rows based on a window function result</li>
<li><strong>DISTINCT</strong> — <code>SELECT DISTINCT</code>, <code>DISTINCT ON (...)</code>, and the <code>DISTINCT</code> modifier on aggregates such as <code>COUNT(DISTINCT ...)</code></li>
<li><strong>Set operations</strong> — <code>UNION</code>, <code>UNION ALL</code>, <code>INTERSECT</code>, and <code>EXCEPT</code></li>
<li><strong>Grouping extensions</strong> — <code>GROUPING SETS</code>, <code>ROLLUP</code>, and <code>CUBE</code></li>
<li><strong>Exact aggregates</strong> — <code>MEDIAN</code>, <code>PERCENTILE_CONT</code>, <code>ARRAY_AGG</code>, and <code>STRING_AGG</code></li>
</ul>
<h4 id="examples">Examples</h4>
<h4 id="rank-rows-with-a-window-function">Rank rows with a window function</h4>
<pre tabindex="0"><code class="language-sql">SELECT customer_id, region,&#10;       ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) AS rank_in_region&#10;FROM my_namespace.sales_data&#10;</code></pre>
<h4 id="filter-with-qualify">Filter with QUALIFY</h4>
<pre tabindex="0"><code class="language-sql">SELECT customer_id, region, total_amount&#10;FROM my_namespace.sales_data&#10;QUALIFY ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) &lt;= 3&#10;</code></pre>
<h4 id="combine-tables-with-a-set-operation">Combine tables with a set operation</h4>
<pre tabindex="0"><code class="language-sql">SELECT customer_id FROM my_namespace.sales_data&#10;EXCEPT&#10;SELECT customer_id FROM my_namespace.archived_sales&#10;</code></pre>
<p>The named <code>WINDOW</code> clause is not supported — inline the <code>OVER (...)</code> specification at each call site. For the full syntax reference, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>. For supported features and performance guidance, refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a>.</p>
</div></article></div>
