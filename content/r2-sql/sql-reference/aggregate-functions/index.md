---
cp9:
  canonical: https://developers.cloudflare.com/r2-sql/sql-reference/aggregate-functions/
  description: Reference for the aggregate functions supported in R2 SQL, organized by category.
  full_title: Aggregate functions · R2 SQL docs
  head_html: <title>Aggregate functions · R2 SQL docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference for the aggregate functions supported in R2 SQL, organized by category."><link rel="canonical" href="https://developers.cloudflare.com/r2-sql/sql-reference/aggregate-functions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2-sql/sql-reference/aggregate-functions/index.md"><meta property="og:title" content="Aggregate functions · R2 SQL docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference for the aggregate functions supported in R2 SQL, organized by category."><meta property="og:url" content="https://developers.cloudflare.com/r2-sql/sql-reference/aggregate-functions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2 SQL"><meta name="algolia_product_filter" content="R2 SQL"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="R2 SQL"><meta name="pcx_tags" content="SQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2-sql/sql-reference/aggregate-functions/#page","headline":"Aggregate functions \u00b7 R2 SQL docs","description":"Reference for the aggregate functions supported in R2 SQL, organized by category.","url":"https://developers.cloudflare.com/r2-sql/sql-reference/aggregate-functions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SQL"]}</script>
  markdown: true
  noindex: false
  route: /r2-sql/sql-reference/aggregate-functions/
  schema: 1
---
<p>Aggregate functions collapse multiple rows into a single result. They are used with <code>GROUP BY</code> to compute summaries per group, or without <code>GROUP BY</code> to compute a single result across all rows.</p>
<p>Most aggregates accept a <code>DISTINCT</code> modifier, for example <code>COUNT(DISTINCT customer_id)</code> or <code>SUM(DISTINCT total_amount)</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11352.md")
</aside>
<hr />
<h2 id="basic-aggregates">Basic aggregates</h2>
<h3 id="count">COUNT</h3>
<p>Counts rows. <code>COUNT(*)</code> counts all rows. <code>COUNT(column)</code> counts non-NULL values.</p>
<pre tabindex="0"><code class="language-sql">SELECT COUNT(*) AS total_rows&#10;FROM my_namespace.sales_data&#10;&#10;SELECT department, COUNT(*) AS dept_count&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;ORDER BY dept_count DESC&#10;</code></pre>
<h3 id="sum">SUM</h3>
<p>Returns the sum of values in a column.</p>
<pre tabindex="0"><code class="language-sql">SELECT SUM(total_amount) AS grand_total&#10;FROM my_namespace.sales_data&#10;&#10;SELECT department, SUM(total_amount) AS dept_total&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;ORDER BY dept_total DESC&#10;</code></pre>
<h3 id="avg">AVG</h3>
<p>Returns the average of values in a column. Alias: <code>mean</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT AVG(total_amount) AS avg_amount&#10;FROM my_namespace.sales_data&#10;&#10;SELECT department, AVG(total_amount) AS avg_amount&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;ORDER BY avg_amount DESC&#10;</code></pre>
<h3 id="min">MIN</h3>
<p>Returns the minimum value. Works on numeric and string columns.</p>
<pre tabindex="0"><code class="language-sql">SELECT MIN(total_amount) AS min_amount, MIN(customer_id) AS first_customer&#10;FROM my_namespace.sales_data&#10;&#10;SELECT department, MIN(total_amount) AS min_amount&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;</code></pre>
<h3 id="max">MAX</h3>
<p>Returns the maximum value. Works on numeric and string columns.</p>
<pre tabindex="0"><code class="language-sql">SELECT MAX(total_amount) AS max_amount, MAX(customer_id) AS last_customer&#10;FROM my_namespace.sales_data&#10;&#10;SELECT department, MAX(total_amount) AS max_amount&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;</code></pre>
<h3 id="median">MEDIAN</h3>
<p>Returns the exact median value. For large datasets, use <a href="#approx_median"><code>approx_median</code></a> instead.</p>
<pre tabindex="0"><code class="language-sql">SELECT MEDIAN(total_amount) AS median_amount&#10;FROM my_namespace.sales_data&#10;&#10;SELECT department, MEDIAN(total_amount) AS median_amount&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;</code></pre>
<h3 id="percentile-cont">PERCENTILE_CONT</h3>
<p>Returns the exact value at a given percentile using <code>WITHIN GROUP (ORDER BY ...)</code>. The percentile parameter must be between <code>0.0</code> and <code>1.0</code> inclusive. For large datasets, use <a href="#approx_percentile_cont"><code>approx_percentile_cont</code></a> instead.</p>
<pre tabindex="0"><code class="language-sql">SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY total_amount) AS median,&#10;       PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY total_amount) AS p95&#10;FROM my_namespace.sales_data&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11351.md")
</aside>
<hr />
<h2 id="approximate-aggregates">Approximate aggregates</h2>
<p>Approximate aggregation functions produce statistically estimated results while using significantly less memory and compute than their exact counterparts. Use them when analyzing large datasets and an approximate result is acceptable.</p>
<h3 id="approx-percentile-cont">approx_percentile_cont</h3>
<p>Returns the approximate value at a given percentile using a T-Digest algorithm. The percentile parameter must be between <code>0.0</code> and <code>1.0</code> inclusive.</p>
<pre tabindex="0"><code class="language-sql">SELECT approx_percentile_cont(total_amount, 0.5) AS median,&#10;       approx_percentile_cont(total_amount, 0.95) AS p95&#10;FROM my_namespace.sales_data&#10;&#10;SELECT department,&#10;       approx_percentile_cont(total_amount, 0.5) AS median&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;ORDER BY median DESC&#10;</code></pre>
<h3 id="approx-percentile-cont-with-weight">approx_percentile_cont_with_weight</h3>
<p>Returns the approximate weighted percentile. Rows are weighted by the <code>weight</code> column.</p>
<pre tabindex="0"><code class="language-sql">SELECT approx_percentile_cont_with_weight(unit_price, quantity, 0.5) AS weighted_median&#10;FROM my_namespace.sales_data&#10;WHERE unit_price IS NOT NULL AND quantity IS NOT NULL&#10;</code></pre>
<h3 id="approx-median">approx_median</h3>
<p>Returns the approximate median. Equivalent to <code>approx_percentile_cont(column, 0.5)</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT approx_median(total_amount) AS median_amount&#10;FROM my_namespace.sales_data&#10;&#10;SELECT department, approx_median(total_amount) AS median&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;</code></pre>
<h3 id="approx-distinct">approx_distinct</h3>
<p>Returns the approximate count of distinct values using HyperLogLog.</p>
<pre tabindex="0"><code class="language-sql">SELECT approx_distinct(customer_id) AS unique_customers&#10;FROM my_namespace.sales_data&#10;&#10;SELECT department, approx_distinct(customer_id) AS unique_customers&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;</code></pre>
<h3 id="approx-top-k">approx_top_k</h3>
<p>Returns the <em>k</em> most frequent values with their approximate counts.</p>
<pre tabindex="0"><code class="language-sql">SELECT approx_top_k(department, 5) AS top_departments&#10;FROM my_namespace.sales_data&#10;</code></pre>
<hr />
<h2 id="statistical-aggregates">Statistical aggregates</h2>
<h3 id="var-var-samp">var / var_samp</h3>
<p>Returns the sample variance.</p>
<pre tabindex="0"><code class="language-sql">SELECT var(total_amount) AS variance&#10;FROM my_namespace.sales_data&#10;&#10;SELECT department, var(total_amount) AS variance&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;</code></pre>
<h3 id="var-pop">var_pop</h3>
<p>Returns the population variance.</p>
<pre tabindex="0"><code class="language-sql">SELECT var_pop(total_amount) AS pop_variance&#10;FROM my_namespace.sales_data&#10;</code></pre>
<h3 id="stddev-stddev-samp">stddev / stddev_samp</h3>
<p>Returns the sample standard deviation.</p>
<pre tabindex="0"><code class="language-sql">SELECT stddev(total_amount) AS std_dev&#10;FROM my_namespace.sales_data&#10;&#10;SELECT department, stddev(total_amount) AS std_dev&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;</code></pre>
<h3 id="stddev-pop">stddev_pop</h3>
<p>Returns the population standard deviation.</p>
<pre tabindex="0"><code class="language-sql">SELECT stddev_pop(total_amount) AS pop_std_dev&#10;FROM my_namespace.sales_data&#10;</code></pre>
<h3 id="covar-samp">covar_samp</h3>
<p>Returns the sample covariance. Alias: <code>covar</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT covar_samp(total_amount, CAST(quantity AS DOUBLE)) AS covariance&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL AND quantity IS NOT NULL&#10;</code></pre>
<h3 id="covar-pop">covar_pop</h3>
<p>Returns the population covariance.</p>
<pre tabindex="0"><code class="language-sql">SELECT covar_pop(total_amount, CAST(quantity AS DOUBLE)) AS pop_covariance&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL AND quantity IS NOT NULL&#10;</code></pre>
<h3 id="corr">corr</h3>
<p>Returns the Pearson correlation coefficient between two columns.</p>
<pre tabindex="0"><code class="language-sql">SELECT corr(total_amount, CAST(quantity AS DOUBLE)) AS correlation&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL AND quantity IS NOT NULL&#10;</code></pre>
<h3 id="regr-slope">regr_slope</h3>
<p>Returns the slope of the linear regression line.</p>
<pre tabindex="0"><code class="language-sql">SELECT regr_slope(total_amount, CAST(quantity AS DOUBLE)) AS slope&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL AND quantity IS NOT NULL&#10;</code></pre>
<h3 id="regr-intercept">regr_intercept</h3>
<p>Returns the y-intercept of the linear regression line.</p>
<pre tabindex="0"><code class="language-sql">SELECT regr_intercept(total_amount, CAST(quantity AS DOUBLE)) AS intercept&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL AND quantity IS NOT NULL&#10;</code></pre>
<h3 id="regr-count">regr_count</h3>
<p>Returns the count of non-NULL pairs.</p>
<pre tabindex="0"><code class="language-sql">SELECT regr_count(total_amount, CAST(quantity AS DOUBLE)) AS pair_count&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL AND quantity IS NOT NULL&#10;</code></pre>
<h3 id="regr-r2">regr_r2</h3>
<p>Returns the coefficient of determination (R-squared).</p>
<pre tabindex="0"><code class="language-sql">SELECT regr_r2(total_amount, CAST(quantity AS DOUBLE)) AS r_squared&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL AND quantity IS NOT NULL&#10;</code></pre>
<h3 id="regr-avgx">regr_avgx</h3>
<p>Returns the average of the independent variable (x) for non-NULL pairs.</p>
<pre tabindex="0"><code class="language-sql">SELECT regr_avgx(total_amount, CAST(quantity AS DOUBLE)) AS avg_qty&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL AND quantity IS NOT NULL&#10;</code></pre>
<h3 id="regr-avgy">regr_avgy</h3>
<p>Returns the average of the dependent variable (y) for non-NULL pairs.</p>
<pre tabindex="0"><code class="language-sql">SELECT regr_avgy(total_amount, CAST(quantity AS DOUBLE)) AS avg_amount&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL AND quantity IS NOT NULL&#10;</code></pre>
<h3 id="regr-sxx">regr_sxx</h3>
<p>Returns the sum of squares of the independent variable.</p>
<pre tabindex="0"><code class="language-sql">SELECT regr_sxx(total_amount, CAST(quantity AS DOUBLE)) AS sxx&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL AND quantity IS NOT NULL&#10;</code></pre>
<h3 id="regr-syy">regr_syy</h3>
<p>Returns the sum of squares of the dependent variable.</p>
<pre tabindex="0"><code class="language-sql">SELECT regr_syy(total_amount, CAST(quantity AS DOUBLE)) AS syy&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL AND quantity IS NOT NULL&#10;</code></pre>
<h3 id="regr-sxy">regr_sxy</h3>
<p>Returns the sum of products of the paired variables.</p>
<pre tabindex="0"><code class="language-sql">SELECT regr_sxy(total_amount, CAST(quantity AS DOUBLE)) AS sxy&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL AND quantity IS NOT NULL&#10;</code></pre>
<hr />
<h2 id="bitwise-aggregates">Bitwise aggregates</h2>
<h3 id="bit-and">bit_and</h3>
<p>Returns the bitwise AND of all values in a group.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, bit_and(quantity) AS and_result&#10;FROM my_namespace.sales_data&#10;WHERE quantity IS NOT NULL&#10;GROUP BY department&#10;</code></pre>
<h3 id="bit-or">bit_or</h3>
<p>Returns the bitwise OR of all values in a group.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, bit_or(quantity) AS or_result&#10;FROM my_namespace.sales_data&#10;WHERE quantity IS NOT NULL&#10;GROUP BY department&#10;</code></pre>
<h3 id="bit-xor">bit_xor</h3>
<p>Returns the bitwise XOR of all values in a group.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, bit_xor(quantity) AS xor_result&#10;FROM my_namespace.sales_data&#10;WHERE quantity IS NOT NULL&#10;GROUP BY department&#10;</code></pre>
<hr />
<h2 id="boolean-aggregates">Boolean aggregates</h2>
<h3 id="bool-and">bool_and</h3>
<p>Returns true if all values in a group are true.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, bool_and(is_completed) AS all_completed&#10;FROM my_namespace.sales_data&#10;WHERE is_completed IS NOT NULL&#10;GROUP BY department&#10;</code></pre>
<h3 id="bool-or">bool_or</h3>
<p>Returns true if any value in a group is true.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, bool_or(is_completed) AS any_completed&#10;FROM my_namespace.sales_data&#10;WHERE is_completed IS NOT NULL&#10;GROUP BY department&#10;</code></pre>
<hr />
<h2 id="positional-aggregates">Positional aggregates</h2>
<h3 id="first-value">first_value</h3>
<p>Returns the first value in a group according to the specified ordering.</p>
<pre tabindex="0"><code class="language-sql">SELECT department,&#10;       first_value(customer_id ORDER BY total_amount ASC) AS lowest_spender&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;GROUP BY department&#10;</code></pre>
<h3 id="last-value">last_value</h3>
<p>Returns the last value in a group according to the specified ordering.</p>
<pre tabindex="0"><code class="language-sql">SELECT department,&#10;       last_value(customer_id ORDER BY total_amount ASC) AS highest_spender&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;GROUP BY department&#10;</code></pre>
<hr />
<h2 id="collection-aggregates">Collection aggregates</h2>
<p>These aggregates accumulate all input values into a single result. Because they hold every value in memory, use a <code>WHERE</code> filter or <code>GROUP BY</code> to keep group sizes bounded on large datasets.</p>
<h3 id="array-agg">array_agg</h3>
<p>Collects values from a group into an array.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, array_agg(customer_id) AS customers&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;</code></pre>
<h3 id="string-agg">string_agg</h3>
<p>Concatenates values from a group into a single string, separated by the given delimiter.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, string_agg(customer_id, &#x27;, &#x27;) AS customer_list&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;</code></pre>
