---
cp9:
  canonical: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/
  description: SQL aggregate functions for Analytics Engine queries.
  full_title: SQL Reference · Cloudflare Analytics docs
  head_html: <title>SQL Reference · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="SQL aggregate functions for Analytics Engine queries."><link rel="canonical" href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/index.md"><meta property="og:title" content="SQL Reference · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="SQL aggregate functions for Analytics Engine queries."><meta property="og:url" content="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers Analytics Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/#page","headline":"SQL Reference \u00b7 Cloudflare Analytics docs","description":"SQL aggregate functions for Analytics Engine queries.","url":"https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/analytics-engine/sql-reference/aggregate-functions/
  schema: 1
---
<h2 id="count">count</h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">count()&#10;count(DISTINCT column_name)&#10;</code></pre>
<p><code>count</code> is an aggregation function that returns the number of rows in each group or results set.</p>
<p><code>count</code> can also be used to count the number of distinct (unique) values in each column:</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-sql">&#45;- return the total number of rows&#10;count()&#10;&#45;- return the number of different values in the column&#10;count(DISTINCT column_name)&#10;</code></pre>
<h2 id="sum">sum</h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">sum([DISTINCT] column_name)&#10;</code></pre>
<p><code>sum</code> is an aggregation function that returns the sum of column values across all rows in each group or results set. Sum also supports <code>DISTINCT</code>, but in this case it will only sum the unique values in the column.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-sql">&#45;- return the total cost of all items&#10;sum(item_cost)&#10;&#45;- return the total of all unique item costs&#10;sum(DISTINCT item_cost)&#10;</code></pre>
<h2 id="avg">avg</h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">avg([DISTINCT] column_name)&#10;</code></pre>
<p><code>avg</code> is an aggregation function that returns the mean of column values across all rows in each group or results set. Avg also supports <code>DISTINCT</code>, but in this case it will only average the unique values in the column.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-sql">&#45;- return the mean item cost&#10;avg(item_cost)&#10;&#45;- return the mean of unique item costs&#10;avg(DISTINCT item_cost)&#10;</code></pre>
<h2 id="min">min</h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">min(column_name)&#10;</code></pre>
<p><code>min</code> is an aggregation function that returns the minimum value of a column across all rows.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-sql">&#45;- return the minimum item cost&#10;min(item_cost)&#10;</code></pre>
<h2 id="max">max</h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">max(column_name)&#10;</code></pre>
<p><code>max</code> is an aggregation function that returns the maximum value of a column across all rows.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-sql">&#45;- return the maximum item cost&#10;max(item_cost)&#10;</code></pre>
<h2 id="quantileexactweighted">quantileExactWeighted</h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">quantileExactWeighted(q)(column_name, weight_column_name)&#10;</code></pre>
<p><code>quantileExactWeighted</code> is an aggregation function that returns the value at the q<sup>th</sup> quantile in the named column across all rows in each group or results set. Each row will be weighted by the value in <code>weight_column_name</code>. Typically this would be <code>_sample_interval</code> (refer to <a href="/analytics/analytics-engine/sql-api/#sampling">Sampling</a> for more information).</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-sql">&#45;- estimate the median value of &lt;double1&gt;&#10;quantileExactWeighted(0.5)(double1, _sample_interval)&#10;&#10;&#45;- in a table of query times, estimate the 95th centile query time&#10;quantileExactWeighted(0.95)(query_time, _sample_interval)&#10;</code></pre>
<p>For backwards compatibility, this is also available as <code>quantileWeighted(q, column_name, weight_column_name)</code>.</p>
<h2 id="argmax">argMax <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">argMax(arg, val)&#10;</code></pre>
<p><code>argMax</code> is an aggregation function that returns the <code>arg</code> value that corresponds to the maximum value of <code>val</code>.</p>
<p>If multiple <code>arg</code> values have the maximum value of <code>val</code>, any one will be returned.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-sql">&#45;- find the &lt;blob1&gt; value for the row with the highest &lt;double1&gt;&#10;argMax(blob1, double1)&#10;&#10;&#45;- find the &lt;blob1&gt; value from the most heavily sampled row&#10;argMax(blob1, _sample_interval)&#10;</code></pre>
<h2 id="argmin">argMin <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">argMin(arg, val)&#10;</code></pre>
<p><code>argMin</code> is an aggregation function that returns the <code>arg</code> value that corresponds to the minimum value of <code>val</code>.</p>
<p>If multiple <code>arg</code> values have the minimum value of <code>val</code>, any one will be returned.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-sql">&#45;- find the &lt;blob1&gt; value for the row with the lowest &lt;double1&gt;&#10;argMin(blob1, double1)&#10;&#10;&#45;- find the &lt;blob1&gt; value from the least heavily sampled row&#10;argMin(blob1, _sample_interval)&#10;</code></pre>
<h2 id="first-value">first_value <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">first_value(column_name)&#10;</code></pre>
<p><code>first_value</code> is an aggregation function which returns the first value of the provided column.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-sql">&#45;- find the oldest value of &lt;blob1&gt;&#10;SELECT first_value(blob1) FROM my_dataset ORDER BY timestamp ASC&#10;</code></pre>
<h2 id="last-value">last_value <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">last_value(column_name)&#10;</code></pre>
<p><code>last_value</code> is an aggregation function which returns the last value of the provided column.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-sql">&#45;- find the oldest value of &lt;blob1&gt;&#10;SELECT last_value(blob1) FROM my_dataset ORDER BY timestamp DESC&#10;</code></pre>
<h2 id="topk">topK <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">topK(N)(column)&#10;</code></pre>
<p><code>topK</code> is an aggregation function which returns the most common <code>N</code> values of a column.</p>
<p><code>N</code> is optional and defaults to <code>10</code>.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-sql">&#45;- find the 10 most common values of &lt;double1&gt;&#10;SELECT topK(double1) FROM my_dataset&#10;&#10;&#45;- find the 15 most common values of &lt;blob1&gt;&#10;SELECT topK(15)(blob1) FROM my_dataset&#10;</code></pre>
<h2 id="topkweighted">topKWeighted <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">topKWeighted(N)(column, weight_column)&#10;</code></pre>
<p><code>topKWeighted</code> is an aggregation function which returns the most common <code>N</code> values of a column, weighted by a second column.</p>
<p><code>N</code> is optional and defaults to <code>10</code>.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-sql">&#45;- find the 10 most common values of &lt;double1&gt;, weighted by `_sample_interval`&#10;SELECT topKWeighted(double1, _sample_interval) FROM my_dataset&#10;&#10;&#45;- find the 15 most common values of &lt;blob1&gt;, weighted by `_sample_interval`&#10;SELECT topKWeighted(15)(blob1, _sample_interval) FROM my_dataset&#10;</code></pre>
<h2 id="countif">countIf <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">countIf(&lt;expr&gt;)&#10;</code></pre>
<p><code>countIf</code> is an aggregation function that returns the number of rows in the results set,
but only counting rows where a provided expression evaluates to true.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-sql">&#45;- return the number of rows where `double1` is greater than 5&#10;countIf(double1 &gt; 5)&#10;</code></pre>
<h2 id="sumif">sumIf <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">sumIf(&lt;expr&gt;, &lt;expr&gt;)&#10;</code></pre>
<p><code>sumIf</code> is an aggregation function that returns the sum of a first expression across all rows in the results set,
but only including rows where a second expression evaluates to true.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-sql">&#45;- return the sum of column `item_cost` of all items where another column `in_stock` is not zero&#10;sumIf(item_cost, in_stock &gt; 0)&#10;</code></pre>
<h2 id="avgif">avgIf <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">avgIf(&lt;expr&gt;, &lt;expr&gt;)&#10;</code></pre>
<p><code>avgIf</code> is an aggregation function that returns the mean of an expression across all rows in the results set,
but only including rows where a second expression evaluates to true.</p>
<p>Example:</p>
<pre tabindex="0"><code class="language-sql">&#45;- return the mean of column `item_cost` where another column `in_stock` is not zero&#10;avgIf(item_cost, in_stock &gt; 0)&#10;</code></pre>
