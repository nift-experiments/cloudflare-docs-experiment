---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-09-approximate-aggregation-functions/
  description: New updates and improvements at Cloudflare.
  full_title: R2 SQL now supports approximate aggregation functions · Changelog
  head_html: <title>R2 SQL now supports approximate aggregation functions · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-09-approximate-aggregation-functions/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="R2 SQL now supports approximate aggregation functions · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-09-approximate-aggregation-functions/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-09-approximate-aggregation-functions/#page","headline":"R2 SQL now supports approximate aggregation functions \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-09-approximate-aggregation-functions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-09-approximate-aggregation-functions/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 9, 2026</time><h2 id="post-title">R2 SQL now supports approximate aggregation functions</h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p>R2 SQL now supports five approximate aggregation functions for fast analysis of large datasets. These functions trade minor precision for improved performance on high-cardinality data.</p>
<h4 id="new-functions">New functions</h4>
<ul>
<li><code>APPROX_PERCENTILE_CONT(column, percentile)</code> — Returns the approximate value at a given percentile (0.0 to 1.0). Works on integer and decimal columns.</li>
<li><code>APPROX_PERCENTILE_CONT_WITH_WEIGHT(column, weight, percentile)</code> — Weighted percentile calculation where each row contributes proportionally to its weight column value.</li>
<li><code>APPROX_MEDIAN(column)</code> — Returns the approximate median. Equivalent to <code>APPROX_PERCENTILE_CONT(column, 0.5)</code>.</li>
<li><code>APPROX_DISTINCT(column)</code> — Returns the approximate number of distinct values. Works on any column type.</li>
<li><code>APPROX_TOP_K(column, k)</code> — Returns the <code>k</code> most frequent values with their counts as a JSON array.</li>
</ul>
<p>All functions support <code>WHERE</code> filters. All except <code>APPROX_TOP_K</code> support <code>GROUP BY</code>.</p>
<h4 id="examples">Examples</h4>
<pre tabindex="0"><code class="language-sql">&#45;- Percentile analysis on revenue data&#10;SELECT approx_percentile_cont(total_amount, 0.25),&#10;       approx_percentile_cont(total_amount, 0.5),&#10;       approx_percentile_cont(total_amount, 0.75)&#10;FROM my_namespace.sales_data&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Median per department&#10;SELECT department, approx_median(total_amount)&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Approximate distinct customers by region&#10;SELECT region, approx_distinct(customer_id)&#10;FROM my_namespace.sales_data&#10;GROUP BY region&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Top 5 most frequent departments&#10;SELECT approx_top_k(department, 5)&#10;FROM my_namespace.sales_data&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Combine approximate and standard aggregations&#10;SELECT COUNT(*),&#10;       AVG(total_amount),&#10;       approx_percentile_cont(total_amount, 0.5),&#10;       approx_distinct(customer_id)&#10;FROM my_namespace.sales_data&#10;WHERE region = &#x27;North&#x27;&#10;</code></pre>
<p>For the full syntax and additional examples, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>.</p>
</div></article></div>
