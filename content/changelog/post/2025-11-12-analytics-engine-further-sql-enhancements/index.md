<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 12, 2025</time><h2 id="post-title">More SQL aggregate, date and time functions available in Workers Analytics Engine</h2>
<div class="changelog-badges"><span>workers-analytics-engine</span><span>workers</span></div><div class="changelog-body"><p>You can now perform more powerful queries directly in <a href="https://developers.cloudflare.com/analytics/analytics-engine/">Workers Analytics Engine</a> with a major expansion of our SQL function library.</p>
<p>Workers Analytics Engine allows you to ingest and store high-cardinality data at scale (such as custom analytics) and query your data through a simple SQL API.</p>
<p>Today, we've expanded Workers Analytics Engine's SQL capabilities with several new functions:</p>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/"><strong>New aggregate functions:</strong></a></p>
<ul>
<li><code>countIf()</code> - count the number of rows which satisfy a provided condition</li>
<li><code>sumIf()</code> - calculate a sum from rows which satisfy a provided condition</li>
<li><code>avgIf()</code> - calculate an average from rows which satisfy a provided condition</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/date-time-functions/"><strong>New date and time functions:</strong></a></p>
<ul>
<li><code>toYear()</code></li>
<li><code>toMonth()</code></li>
<li><code>toDayOfMonth()</code></li>
<li><code>toDayOfWeek()</code></li>
<li><code>toHour()</code></li>
<li><code>toMinute()</code></li>
<li><code>toSecond()</code></li>
<li><code>toStartOfYear()</code></li>
<li><code>toStartOfMonth()</code></li>
<li><code>toStartOfWeek()</code></li>
<li><code>toStartOfDay()</code></li>
<li><code>toStartOfHour()</code></li>
<li><code>toStartOfFifteenMinutes()</code></li>
<li><code>toStartOfTenMinutes()</code></li>
<li><code>toStartOfFiveMinutes()</code></li>
<li><code>toStartOfMinute()</code></li>
<li><code>today()</code></li>
<li><code>toYYYYMM()</code></li>
</ul>
<h4 id="ready-to-get-started">Ready to get started?</h4>
Whether you're building usage-based billing systems, customer analytics dashboards, or other custom analytics, these functions let you get the most out of your data. [Get started ](/analytics/analytics-engine/get-started/) with Workers Analytics Engine and explore all available functions in our [SQL reference documentation](/analytics/analytics-engine/sql-reference/).
</div></article></div>
