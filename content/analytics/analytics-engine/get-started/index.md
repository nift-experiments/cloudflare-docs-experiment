---
cp9:
  canonical: https://developers.cloudflare.com/analytics/analytics-engine/get-started/
  description: Set up and access Network Analytics.
  full_title: Get started with Workers Analytics Engine · Cloudflare Analytics docs
  head_html: <title>Get started with Workers Analytics Engine · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up and access Network Analytics."><link rel="canonical" href="https://developers.cloudflare.com/analytics/analytics-engine/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/analytics-engine/get-started/index.md"><meta property="og:title" content="Get started with Workers Analytics Engine · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up and access Network Analytics."><meta property="og:url" content="https://developers.cloudflare.com/analytics/analytics-engine/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers Analytics Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/analytics-engine/get-started/#page","headline":"Get started with Workers Analytics Engine \u00b7 Cloudflare Analytics docs","description":"Set up and access Network Analytics.","url":"https://developers.cloudflare.com/analytics/analytics-engine/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/analytics-engine/get-started/
  schema: 1
---
<h2 id="1-name-your-dataset-and-add-it-to-your-worker"><ol>
<li>Name your dataset and add it to your Worker</li>
</ol></h2>
<p>Add the following to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to create a <a href="/workers/runtime-apis/bindings/">binding</a> to a Workers Analytics Engine dataset. A dataset is like a table in SQL: the rows and columns should have consistent meaning.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3140.md")
</aside>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3141.md")
</div>
<h2 id="2-write-data-points-from-your-worker"><ol start="2">
<li>Write data points from your Worker</li>
</ol></h2>
<p>You can write data points to your Worker by calling the <code>writeDataPoint()</code> method that is exposed on the binding that you just created.</p>
<pre tabindex="0"><code class="language-js">async fetch(request, env) {&#10;  env.WEATHER.writeDataPoint({&#10;    &#x27;blobs&#x27;: [&quot;Seattle&quot;, &quot;USA&quot;, &quot;pro_sensor_9000&quot;], // City, State&#10;    &#x27;doubles&#x27;: [25, 0.5],&#10;    &#x27;indexes&#x27;: [&quot;a3cd45&quot;]&#10;  });&#10;  return new Response(&quot;OK!&quot;);&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3139.md")
</aside>
<p>A data point is a structured event that consists of:</p>
<ul>
<li><strong>Blobs</strong> (strings) — The dimensions used for grouping and filtering. Sometimes called labels in other metrics systems.</li>
<li><strong>Doubles</strong> (numbers) — The numeric values that you want to record in your data point.</li>
<li><strong>Indexes</strong> — (strings) — Used as a <a href="/analytics/analytics-engine/sql-api/#sampling">sampling</a> key.</li>
</ul>
<p>In the example above, suppose you are collecting air quality samples. Each data point written represents a reading from your weather sensor. The blobs define city, state, and sensor model — the dimensions you want to be able to filter queries on later. The doubles define the numeric temperature and air pressure readings. And the index is the ID of your customer. You may want to include <a href="/workers/runtime-apis/request/">context about the incoming request</a>, such as geolocation, to add additional data to your datapoint.</p>
<p>Currently, the <code>writeDataPoint()</code> API accepts ordered arrays of values. This means that you must provide fields in a consistent order. While the <code>indexes</code> field accepts an array, you currently must only provide a single index. If you attempt to provide multiple indexes, your data point will not be recorded.</p>
<h2 id="3-query-data-using-the-sql-api"><ol start="3">
<li>Query data using the SQL API</li>
</ol></h2>
<p>You can query the data you have written in two ways:</p>
<ul>
<li><a href="/analytics/analytics-engine/sql-api"><strong>SQL API</strong></a> — Best for writing your own queries and integrating with external tools like Grafana.</li>
<li><a href="/analytics/graphql-api/"><strong>GraphQL API</strong></a> — This is the same API that powers the Cloudflare dashboard.</li>
</ul>
<p>For the purpose of this example, we will use the SQL API.</p>
<h3 id="create-an-api-token">Create an API token</h3>
<p>Create an <a href="https://dash.cloudflare.com/profile/api-tokens">API Token</a> that has the <code>Account Analytics Read</code> permission.</p>
<h3 id="write-your-first-query">Write your first query</h3>
<p>The following query returns the top 10 cities that had the highest average humidity readings when the temperature was above zero:</p>
<pre tabindex="0"><code class="language-sql">SELECT&#10;  blob1 AS city,&#10;  SUM(_sample_interval * double2) / SUM(_sample_interval) AS avg_humidity&#10;FROM WEATHER&#10;WHERE double1 &gt; 0&#10;GROUP BY city&#10;ORDER BY avg_humidity DESC&#10;LIMIT 10&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3138.md")
</aside>
<p>You can run this query by making an HTTP request to the SQL API:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/analytics_engine/sql&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-data &quot;SELECT blob1 AS city, SUM(_sample_interval * double2) / SUM(_sample_interval) AS avg_humidity FROM WEATHER WHERE double1 &gt; 0 GROUP BY city ORDER BY avg_humidity DESC LIMIT 10&quot;&#10;</code></pre>
<p>Refer to the <a href="/analytics/analytics-engine/sql-reference/">Workers Analytics Engine SQL Reference</a> for a full list of supported SQL functionality.</p>
<h3 id="working-with-time-series-data">Working with time series data</h3>
<p>Workers Analytics Engine is optimized for powering time series analytics that can be visualized using tools like Grafana. Every event written from the runtime is automatically populated with a <code>timestamp</code> field. It is expected that most time series will round, and then <code>GROUP BY</code> the <code>timestamp</code>. For example:</p>
<pre tabindex="0"><code class="language-sql">SELECT&#10;  intDiv(toUInt32(timestamp), 300) * 300 AS t,&#10;  blob1 AS city,&#10;  SUM(_sample_interval * double2) / SUM(_sample_interval) AS avg_humidity&#10;FROM WEATHER&#10;WHERE&#10;  timestamp &gt;= NOW() - INTERVAL &#x27;1&#x27; DAY&#10;  AND double1 &gt; 0&#10;GROUP BY t, city&#10;ORDER BY t, avg_humidity DESC&#10;</code></pre>
<p>This query first rounds the <code>timestamp</code> field to the nearest five minutes. Then, it groups by that field and city and calculates the average humidity in each city for a five minute period.</p>
<p>Refer to <a href="/analytics/analytics-engine/grafana/">Querying Workers Analytics Engine from Grafana</a> for more details on how to create efficient Grafana queries against Workers Analytics Engine.</p>
<h2 id="further-reading">Further reading</h2>
<ul class="directory-listing"><li><a href="/analytics/analytics-engine/get-started/">Get started</a></li><li><a href="/analytics/analytics-engine/recipes/">Examples</a></li><li><a href="/analytics/analytics-engine/sql-api/">SQL API</a></li><li><a href="/analytics/analytics-engine/sql-reference/">SQL Reference</a></li><li><a href="/analytics/analytics-engine/grafana/">Querying from Grafana</a></li><li><a href="/analytics/analytics-engine/worker-querying/">Querying from a Worker</a></li><li><a href="/analytics/analytics-engine/sampling/">Sampling with WAE</a></li><li><a href="/analytics/analytics-engine/pricing/">Pricing</a></li><li><a href="/analytics/analytics-engine/limits/">Limits</a></li></ul>
