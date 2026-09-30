---
cp9:
  canonical: https://developers.cloudflare.com/analytics/faq/graphql-api-inconsistent-results/
  description: Understand why GraphQL API results may vary slightly.
  full_title: GraphQL API inconsistent results · Cloudflare Analytics docs
  head_html: <title>GraphQL API inconsistent results · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand why GraphQL API results may vary slightly."><link rel="canonical" href="https://developers.cloudflare.com/analytics/faq/graphql-api-inconsistent-results/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/faq/graphql-api-inconsistent-results/index.md"><meta property="og:title" content="GraphQL API inconsistent results · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand why GraphQL API results may vary slightly."><meta property="og:url" content="https://developers.cloudflare.com/analytics/faq/graphql-api-inconsistent-results/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Faq"><meta name="algolia_content_type" content="Faq"><meta name="pcx_additional_products" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/faq/graphql-api-inconsistent-results/#page","headline":"GraphQL API inconsistent results \u00b7 Cloudflare Analytics docs","description":"Understand why GraphQL API results may vary slightly.","url":"https://developers.cloudflare.com/analytics/faq/graphql-api-inconsistent-results/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/faq/graphql-api-inconsistent-results/
  schema: 1
---
<p>If you run the same GraphQL Analytics API query multiple times and receive slightly different results, this is caused by Adaptive Bit Rate (ABR) sampling. ABR dynamically adjusts data resolution based on query complexity and timing, which can result in slight variations between query runs.</p>
<p>To reduce variation, query shorter timeframes (daily or weekly instead of monthly), use aggregated datasets (nodes with the <code>Groups</code> suffix), and request confidence intervals to understand data quality. For more information, refer to <a href="/analytics/graphql-api/sampling/">Sampling</a>.</p>
<h2 id="what-is-sampling">What is sampling?</h2>
<p>Cloudflare's data pipeline handles over 700 million events per second across the global network. Processing all this data in real-time for every query would be prohibitively expensive and time-consuming.</p>
<p>Sampling analyzes a subset of data rather than every individual data point. Cloudflare uses Adaptive Bit Rate (ABR) sampling to ensure queries complete quickly, even when working with large datasets.</p>
<p>ABR stores data at multiple resolutions:</p>
<ul>
<li><strong>100%</strong> — Full data (used for smaller datasets)</li>
<li><strong>10%</strong> — 10% sample (medium resolution)</li>
<li><strong>1%</strong> — 1% sample (lower resolution)</li>
</ul>
<p>When you run a query, ABR dynamically selects the best resolution based on query complexity, time range requested, number of rows to retrieve, and current system load.</p>
<h2 id="why-do-results-vary-between-query-runs">Why do results vary between query runs?</h2>
<p>Results can vary for several reasons:</p>
<ul>
<li><strong>Dynamic resolution selection</strong> — ABR may choose different sampling resolutions on different query runs based on system conditions.</li>
<li><strong>Long time ranges</strong> — Querying 30 days at once is an expensive operation that triggers more aggressive sampling.</li>
<li><strong>High query complexity</strong> — Complex queries with many filters or aggregations may be sampled differently.</li>
<li><strong>System load</strong> — During high-traffic periods, the system may apply more aggressive sampling to ensure fair resource distribution.</li>
</ul>
<p>For example, running the same 30-day query twice might return 3,500 objects one time and 3,600 objects another time. This indicates different sampling resolutions were used.</p>
<h2 id="can-i-trust-sampled-data">Can I trust sampled data?</h2>
<p>Yes. Sampled data is highly reliable and provides insights as dependable as those derived from full datasets. Cloudflare's sampling techniques capture the essential characteristics of the entire dataset.</p>
<p>Aggregated metrics (totals, averages, percentiles) are extrapolated based on the sample size, so reported metrics accurately represent the entire dataset. Results based on thousands of rows are highly likely to be representative.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3130.md")
</aside>
<h2 id="how-can-i-reduce-variation-in-my-query-results">How can I reduce variation in my query results?</h2>
<h3 id="query-shorter-time-ranges">Query shorter time ranges</h3>
<p>Instead of querying an entire month at once, break queries into smaller intervals (daily or weekly).</p>
<p>Before (more variable):</p>
<pre tabindex="0"><code class="language-graphql">datetime_geq: &quot;2024-09-01T00:00:00Z&quot;&#10;datetime_lt: &quot;2024-10-01T00:00:00Z&quot;&#10;</code></pre>
<p>After (more consistent):</p>
<pre tabindex="0"><code class="language-graphql">datetime_geq: &quot;2024-09-01T00:00:00Z&quot;&#10;datetime_lt: &quot;2024-09-02T00:00:00Z&quot;&#10;</code></pre>
<p>Then aggregate the results client-side. Smaller time windows are less likely to trigger aggressive sampling thresholds.</p>
<h3 id="use-aggregated-datasets">Use aggregated datasets</h3>
<p>Prefer data nodes with the <code>Groups</code> suffix over raw adaptive datasets. Aggregated data is pre-processed and less subject to sampling variability.</p>
<p>For example, use <code>httpRequestsAdaptiveGroups</code> instead of raw event data.</p>
<h3 id="add-explicit-sorting">Add explicit sorting</h3>
<p>Always include <code>orderBy</code> in your queries to ensure consistent result ordering:</p>
<pre tabindex="0"><code class="language-graphql">orderBy: [datetime_ASC]&#10;</code></pre>
<h3 id="use-confidence-intervals">Use confidence intervals</h3>
<p>For adaptive datasets, request <a href="/analytics/graphql-api/features/confidence-intervals/">confidence intervals</a> to understand data quality and verify sampling:</p>
<pre tabindex="0"><code class="language-graphql">confidence(level: 0.95) {&#10;  count {&#10;    estimate&#10;    lower&#10;    upper&#10;    sampleSize&#10;  }&#10;}&#10;</code></pre>
<p>A higher <code>sampleSize</code> indicates more reliable results.</p>
<h2 id="quick-reference">Quick reference</h2>
<table>
<thead>
<tr>
<th>Issue</th>
<th>Mitigation</th>
</tr>
</thead>
<tbody>
<tr>
<td>Results vary between runs</td>
<td>Query shorter time ranges (daily or weekly instead of monthly)</td>
</tr>
<tr>
<td>Aggressive sampling on large queries</td>
<td>Break queries into smaller time intervals and aggregate client-side</td>
</tr>
<tr>
<td>Need consistent ordering</td>
<td>Add <code>orderBy</code> clause to all queries</td>
</tr>
<tr>
<td>Need to verify data quality</td>
<td>Request <code>confidence</code> intervals to check sample size and accuracy</td>
</tr>
<tr>
<td>Using raw adaptive data</td>
<td>Switch to aggregated datasets (nodes with <code>Groups</code> suffix)</td>
</tr>
</tbody>
</table>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/analytics/sampling/">Understanding Sampling in Cloudflare Analytics</a></li>
<li><a href="/analytics/graphql-api/sampling/">GraphQL API Sampling</a></li>
<li><a href="/analytics/graphql-api/features/confidence-intervals/">Confidence Intervals</a></li>
<li><a href="/analytics/graphql-api/limits/">GraphQL API Limits</a></li>
<li><a href="https://blog.cloudflare.com/explaining-cloudflares-abr-analytics/">Adaptive Bit Rate blog post</a></li>
</ul>
