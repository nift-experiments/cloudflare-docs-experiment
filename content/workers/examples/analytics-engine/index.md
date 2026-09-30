---
cp9:
  canonical: https://developers.cloudflare.com/workers/examples/analytics-engine/
  description: Write custom analytics events to Workers Analytics Engine for high-cardinality, time-series data.
  full_title: Write to Analytics Engine · Cloudflare Workers docs
  head_html: <title>Write to Analytics Engine · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Write custom analytics events to Workers Analytics Engine for high-cardinality, time-series data."><link rel="canonical" href="https://developers.cloudflare.com/workers/examples/analytics-engine/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/examples/analytics-engine/index.md"><meta property="og:title" content="Write to Analytics Engine · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Write custom analytics events to Workers Analytics Engine for high-cardinality, time-series data."><meta property="og:url" content="https://developers.cloudflare.com/workers/examples/analytics-engine/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/examples/analytics-engine/#page","headline":"Write to Analytics Engine \u00b7 Cloudflare Workers docs","description":"Write custom analytics events to Workers Analytics Engine for high-cardinality, time-series data.","url":"https://developers.cloudflare.com/workers/examples/analytics-engine/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/examples/analytics-engine/
  schema: 1
---
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
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/analytics_engine/sql&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-data &quot;SELECT blob1 AS path, SUM(_sample_interval) AS views FROM my_dataset WHERE timestamp &gt; NOW() - INTERVAL &#x27;1&#x27; HOUR GROUP BY path ORDER BY views DESC LIMIT 10&quot;&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/analytics/analytics-engine/">Analytics Engine documentation</a> - Full reference for Workers Analytics Engine.</li>
<li><a href="/analytics/analytics-engine/sql-api/">SQL API reference</a> - Query syntax and available functions.</li>
<li><a href="/analytics/analytics-engine/grafana/">Grafana integration</a> - Visualize Analytics Engine data in Grafana.</li>
</ul>
