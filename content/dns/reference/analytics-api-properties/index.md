---
cp9:
  canonical: https://developers.cloudflare.com/dns/reference/analytics-api-properties/
  description: API properties that you can use in API requests for Cloudflare DNS analytics.
  full_title: Analytics API properties · Cloudflare DNS docs
  head_html: <title>Analytics API properties · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="API properties that you can use in API requests for Cloudflare DNS analytics."><link rel="canonical" href="https://developers.cloudflare.com/dns/reference/analytics-api-properties/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/reference/analytics-api-properties/index.md"><meta property="og:title" content="Analytics API properties · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API properties that you can use in API requests for Cloudflare DNS analytics."><meta property="og:url" content="https://developers.cloudflare.com/dns/reference/analytics-api-properties/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/reference/analytics-api-properties/#page","headline":"Analytics API properties \u00b7 Cloudflare DNS docs","description":"API properties that you can use in API requests for Cloudflare DNS analytics.","url":"https://developers.cloudflare.com/dns/reference/analytics-api-properties/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/reference/analytics-api-properties/
  schema: 1
---
<p>This page describes API properties that you can use in requests to the <a href="/api/resources/dns/subresources/analytics/subresources/reports/methods/get/">DNS analytics API</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/7570.md")
</aside>
<h2 id="metrics">Metrics</h2>
<p>A metric is a numerical value based on an attribute of the data, for example a query count.</p>
<p>In API requests, metrics are set in the <code>metrics</code> parameter. If you need to list multiple metrics, separate them with commas.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Name</th>
<th>Example</th>
<th>Unit</th>
</tr>
</thead>
<tbody>
<tr>
<td>queryCount</td>
<td>Query count</td>
<td><code>1000</code></td>
<td>Count</td>
</tr>
<tr>
<td>uncachedCount</td>
<td>Uncached query count</td>
<td><code>1</code></td>
<td>Count</td>
</tr>
<tr>
<td>staleCount</td>
<td>Stale query count</td>
<td><code>1</code></td>
<td>Count</td>
</tr>
<tr>
<td>responseTimeAvg</td>
<td>Average response time</td>
<td><code>1.0</code></td>
<td>Time in milliseconds</td>
</tr>
<tr>
<td>responseTimeMedian</td>
<td>Median response time</td>
<td><code>1.0</code></td>
<td>Time in milliseconds</td>
</tr>
<tr>
<td>responseTime90th</td>
<td>90th percentile response time</td>
<td><code>1.0</code></td>
<td>Time in milliseconds</td>
</tr>
<tr>
<td>responseTime99th</td>
<td>99th percentile response time</td>
<td><code>1.0</code></td>
<td>Time in milliseconds</td>
</tr>
</tbody>
</table>
<h2 id="dimensions">Dimensions</h2>
<p>Dimensions can be used to break down the data by given attributes.</p>
<p>In API requests, dimensions are set in the <code>dimensions</code> parameter. If you need to list multiple dimensions, separate them with commas.</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Name</th>
<th>Example</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>queryName</td>
<td>Query Name</td>
<td><code>example.com</code></td>
<td></td>
</tr>
<tr>
<td>queryType</td>
<td>Query Type</td>
<td><code>AAAA</code></td>
<td><a href="http://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4">Types defined by IANA</a>. Unknown types are empty.</td>
</tr>
<tr>
<td>responseCode</td>
<td>Response Code</td>
<td><code>NOERROR</code></td>
<td><a href="http://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6">Response codes defined by IANA</a>. Always uppercase.</td>
</tr>
<tr>
<td>responseCached</td>
<td>Response Cached</td>
<td><code>Cached</code></td>
<td>Either <code>Cached</code> or <code>Uncached</code>.</td>
</tr>
<tr>
<td>coloName</td>
<td>Colo Name</td>
<td><code>SJC</code></td>
<td>PoP code.</td>
</tr>
<tr>
<td>origin</td>
<td>Origin</td>
<td><code>2001:db8::1</code></td>
<td>Origin used to resolve the query. Empty if N/A or if the query was answered from cache.</td>
</tr>
<tr>
<td>dayOfWeek</td>
<td>Day Of Week</td>
<td><code>1</code></td>
<td>Break down by day of week. Monday is <code>1</code>, and Sunday is <code>7</code>.</td>
</tr>
<tr>
<td>tcp</td>
<td>TCP</td>
<td><code>1</code></td>
<td>Either <code>1</code> or <code>0</code> depending on the protocol used.</td>
</tr>
<tr>
<td>ipVersion</td>
<td>IP Version</td>
<td><code>6</code></td>
<td>IP protocol version used (currently <code>4</code> or <code>6</code>).</td>
</tr>
<tr>
<td>querySizeBucket</td>
<td>Query Size Bucket</td>
<td><code>16-31</code></td>
<td>Query size bucket by multiples of 16.</td>
</tr>
<tr>
<td>responseSizeBucket</td>
<td>Response Size Bucket</td>
<td><code>16-31</code></td>
<td>Response size bucket by multiples of 16.</td>
</tr>
</tbody>
</table>
<h2 id="filters">Filters</h2>
<p>Filters use the form <code>dimension operator expression</code>, where each part corresponds to the following:</p>
<ul>
<li><strong>Dimension</strong>: Specifies the <a href="#dimensions">dimension</a> to filter on. For example, <code>queryName</code>.</li>
<li><strong>Operator</strong>: Defines the type of filter match to use. Operators are specific to dimensions.</li>
<li><strong>Expression</strong>: States the values to include or exclude from the results. Expressions use regular expression (regex) syntax.</li>
</ul>
<h3 id="filter-operators">Filter operators</h3>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Name</th>
<th>Example</th>
<th>Description</th>
<th>URL Encoded</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>==</code></td>
<td>Equals</td>
<td><code>queryName==&quot;example.com&quot;</code></td>
<td>Return results where <code>queryName</code> is exactly <code>example.com</code>.</td>
<td><code>%3D%3D</code></td>
</tr>
<tr>
<td><code>!=</code></td>
<td>Does not equal</td>
<td><code>responseCode!=&quot;NOERROR&quot;</code></td>
<td>Return results where <code>responseCode</code> is different from <code>NOERROR</code>.</td>
<td><code>!%3D</code></td>
</tr>
<tr>
<td><code>&gt;</code></td>
<td>Greater than</td>
<td><code>dimension&gt;1000</code></td>
<td>Return results where a dimension is greater than <code>1000</code>.</td>
<td><code>%3E</code></td>
</tr>
<tr>
<td><code>&lt;</code></td>
<td>Less than</td>
<td><code>dimension&lt;1000</code></td>
<td>Return results where a dimension is less than <code>1000</code>.</td>
<td><code>%3C</code></td>
</tr>
<tr>
<td><code>&gt;=</code></td>
<td>Greater than or equal to</td>
<td><code>dimension&gt;=1000</code></td>
<td>Return results where a dimension is greater than or equal to <code>1000</code>.</td>
<td><code>%3E%3D</code></td>
</tr>
<tr>
<td><code>&lt;=</code></td>
<td>Less than or equal to</td>
<td><code>dimension&lt;=1000</code></td>
<td>Return results where a dimension is less than or equal to <code>1000</code>.</td>
<td><code>%3C%3D</code></td>
</tr>
</tbody>
</table>
<h3 id="combining-filters">Combining filters</h3>
<p>Combine filters using <code>OR</code> and <code>AND</code> boolean logic:</p>
<ul>
<li><code>AND</code> takes precedence over <code>OR</code> in all expressions.</li>
<li>The <code>OR</code> operator is defined using a comma <code>,</code> or the <code>OR</code> keyword surrounded by whitespace.</li>
<li>The <code>AND</code> operator is defined using a semicolon <code>;</code> or the <code>AND</code> keyword surrounded by whitespace.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7569.md")
</aside>
<details class="nb-details"><summary>Examples using OR</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7571.md")
</div></details>
<details class="nb-details"><summary>Examples using AND</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7572.md")
</div></details>
