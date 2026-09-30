<p class="article-summary">Write custom analytics events to Workers Analytics Engine.</p>
<p><a href="/analytics/analytics-engine/">Workers Analytics Engine</a> provides time-series analytics at scale. Use it to track custom metrics, build usage-based billing, or understand service health on a per-customer basis.</p>
<p>Unlike logs, Analytics Engine is designed for aggregated queries over high-cardinality data. Writes are non-blocking and do not impact request latency.</p>
<h2 id="configure-the-binding">Configure the binding</h2>
<p>Add an Analytics Engine dataset binding to your Wrangler configuration file. The dataset is created automatically when you first write to it.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16560.md")
</div>
<h2 id="write-data-points">Write data points</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16561.md")
</div>
<h2 id="data-point-structure">Data point structure</h2>
<p>Each data point consists of:</p>
<ul>
<li><strong>blobs</strong> (strings) - Dimensions for grouping and filtering. Use for paths, regions, status codes, or customer IDs.</li>
<li><strong>doubles</strong> (numbers) - Numeric values to record, such as counts, durations, or sizes.</li>
<li><strong>indexes</strong> (strings) - A single string used as the <a href="/analytics/analytics-engine/sql-api/#sampling">sampling key</a>. Group related events under the same index.</li>
</ul>
<h2 id="query-your-data">Query your data</h2>
<p>Query your data using the <a href="/analytics/analytics-engine/sql-api/">SQL API</a>:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/analytics_engine/sql&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-data &quot;SELECT blob1 AS path, SUM(_sample_interval) AS views FROM my_dataset WHERE timestamp &gt; NOW() - INTERVAL &#x27;1&#x27; HOUR GROUP BY path ORDER BY views DESC LIMIT 10&quot;&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/analytics/analytics-engine/">Analytics Engine documentation</a> - Full reference for Workers Analytics Engine.</li>
<li><a href="/analytics/analytics-engine/sql-api/">SQL API reference</a> - Query syntax and available functions.</li>
<li><a href="/analytics/analytics-engine/grafana/">Grafana integration</a> - Visualize Analytics Engine data in Grafana.</li>
</ul>
