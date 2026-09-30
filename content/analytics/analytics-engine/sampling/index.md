---
cp9:
  canonical: https://developers.cloudflare.com/analytics/analytics-engine/sampling/
  description: How data written to Workers Analytics Engine is automatically sampled at scale
  full_title: Sampling with Workers Analytics Engine · Cloudflare Analytics docs
  head_html: <title>Sampling with Workers Analytics Engine · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="How data written to Workers Analytics Engine is automatically sampled at scale"><link rel="canonical" href="https://developers.cloudflare.com/analytics/analytics-engine/sampling/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/analytics-engine/sampling/index.md"><meta property="og:title" content="Sampling with Workers Analytics Engine · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How data written to Workers Analytics Engine is automatically sampled at scale"><meta property="og:url" content="https://developers.cloudflare.com/analytics/analytics-engine/sampling/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers Analytics Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/analytics-engine/sampling/#page","headline":"Sampling with Workers Analytics Engine \u00b7 Cloudflare Analytics docs","description":"How data written to Workers Analytics Engine is automatically sampled at scale","url":"https://developers.cloudflare.com/analytics/analytics-engine/sampling/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/analytics-engine/sampling/
  schema: 1
---
<p>Workers Analytics Engine offers the ability to write an extensive amount of data and retrieve it quickly, at minimal or no cost. To facilitate writing large amounts of data at a reasonable cost, Workers Analytics Engine employs weighted adaptive <a href="https://en.wikipedia.org/wiki/Sampling_(statistics)">sampling</a>.</p>
<p>When utilizing sampling, you do not need every single data point to answer questions about a dataset. For a sufficiently large dataset, the <a href="https://select-statistics.co.uk/blog/importance-effect-sample-size/">necessary sample size</a> does not depend on the size of the original population. Necessary sample size depends on the variance of your measure, the size of the subgroups you analyze, and how accurate your estimate must be.</p>
<p>The implication for Analytics Engine is that we can compress very large datasets into many fewer observations, yet still answer most queries with very high accuracy. This enables us to offer an analytics service that can measure very high rates of usage, with unbounded cardinality, at a low and predictable price.</p>
<p>At a high level, the way sampling works is:</p>
<ol>
<li>At write time, we sample if data points are written too quickly into one index.</li>
<li>We sample again at query time if the query is too complex.</li>
</ol>
<p>In the following sections, you will learn:</p>
<ul>
<li><a href="/analytics/analytics-engine/sampling/#how-sampling-works">How sampling works</a>.</li>
<li><a href="/analytics/analytics-engine/sampling/#how-to-read-sampled-data">How to read sampled data</a>.</li>
<li><a href="/analytics/analytics-engine/sampling/#how-is-data-sampled">How is data sampled</a>.</li>
<li><a href="/analytics/analytics-engine/sampling/#adaptive-bit-rate-sampling-at-read-time">How Adaptive Bit Rate Sampling works</a>.</li>
<li><a href="/analytics/analytics-engine/sampling/#how-to-select-an-index">How to pick your index such that your data is sampled in a usable way</a>.</li>
</ul>
<h2 id="how-sampling-works">How sampling works</h2>
<p>Cloudflare's data sampling is similar to how online mapping services like Google Maps render maps at different zoom levels. When viewing satellite imagery of a whole continent, the mapping service provides appropriately sized images based on the user's screen and Internet speed.</p>
<p><img src="/assets/upstream/images/analytics/zoom-less-pixels.png" alt="The image on the left shows a satellite view from OpenStreetMap. On the right, the same image is zoomed in. In these two images, each pixel represents the same area; however the image on the right has many fewer pixels." /></p>
<p>Each pixel on the map represents a large area, such as several square kilometers. If a user tries to zoom in using a screenshot, the resulting image would be blurry. Instead, the mapping service selects higher-resolution images when a user zooms in on a specific city. The total number of pixels remains relatively constant, but each pixel now represents a smaller area, like a few square meters.</p>
<p><img src="/assets/upstream/images/analytics/zoom-more-pixels.png" alt="Now the image on the right is of a much higher resolution. Each pixel represents a much smaller area; however, the total number of pixels in both images is roughly the same." /></p>
<p>The key point is that the map's quality does not solely depend on the resolution or the area represented by each pixel. It is determined by the total number of pixels used to render the final view.</p>
<p>There are similarities between the how a mapping services handles resolution and Cloudflare Analytics delivers analytics using adaptive samples:</p>
<ul>
<li><strong>How data is stored</strong>:
<ul>
<li><strong>Mapping service</strong>: Imagery stored at different resolutions.</li>
<li><strong>Cloudflare Analytics</strong>: Events stored at different sample rates.</li>
</ul>
</li>
<li><strong>How data is displayed to user</strong>:
<ul>
<li><strong>Mapping service</strong>: The total number of pixels is ~constant for a given screen size, regardless of the area selected.</li>
<li><strong>Cloudflare Analytics</strong>: A similar number of events are read for each query, regardless of the size of the dataset or length of time selected.</li>
</ul>
</li>
<li><strong>How a resolution is selected</strong>:
<ul>
<li><strong>Mapping service</strong>: The area represented by each pixel will depend on the size of the map being rendered. In a more zoomed out map, each pixel will represent a larger area.</li>
<li><strong>Cloudflare Analytics</strong>: The sample interval of each event in the result depends on the size of the underlying dataset and length of time selected. For a query over a large dataset or long length of time, each sampled event may stand in for many similar events.</li>
</ul>
</li>
</ul>
<h2 id="how-to-read-sampled-data">How to read sampled data</h2>
<p>To effectively write queries and analyze the data, it is helpful to first learn how sampled data is read in Workers Analytics Engine.</p>
<p>In Workers Analytics Engine, every event is recorded with the <code>_sample_interval</code> field. The sample interval is the inverse of the sample rate. For example, if a one percent (1%) sample rate is applied, the <code>sample_interval</code> will be set to <code>100</code>.</p>
<p>Using the mapping example in simple terms, the sample interval represents the &quot;number of unsampled data points&quot; (kilometers or meters) that a given sampled data point (pixel) represents.</p>
<p>The sample interval is a property associated with each individual row stored in Workers Analytics Engine. Due to the implementation of equitable sampling, the sample interval can vary for each row. As a result, when querying the data, you need to consider the sample interval field. Simply multiplying the query result by a constant sampling factor is not sufficient.</p>
<p>Here are some examples of how to express some common queries over sampled data.</p>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Example without sampling</th>
<th>Example with sampling</th>
</tr>
</thead>
<tbody>
<tr>
<td>Count events in a dataset</td>
<td><code>count()</code></td>
<td><code>sum(_sample_interval)</code></td>
</tr>
<tr>
<td>Sum a quantity, for example, bytes</td>
<td><code>sum(bytes)</code></td>
<td><code>sum(bytes * _sample_interval)</code></td>
</tr>
<tr>
<td>Average a quantity</td>
<td><code>avg(bytes)</code></td>
<td><code>sum(bytes * _sample_interval) / sum(_sample_interval)</code></td>
</tr>
<tr>
<td>Compute quantiles</td>
<td><code>quantile(0.50)(bytes)</code></td>
<td><code>quantileExactWeighted(0.50)(bytes, _sample_interval)</code></td>
</tr>
</tbody>
</table>
<p>Note that the accuracy of results is not determined by the sample interval, similar to the mapping analogy mentioned earlier. A high sample interval can still provide precise results. Instead, accuracy depends on the total number of data points queried and their distribution.</p>
<h2 id="how-is-data-sampled">How is data sampled</h2>
<p>To determine the sample interval for each event, note that most analytics have some important type of subgroup that must be analyzed with accurate results. For example, you may want to analyze user usage or traffic to specific hostnames. Analytics Engine users can define these groups by populating the <code>index</code> field when writing an event. This allows for more targeted and precise analysis within the specified groups.</p>
<p>The next observation is that these index values likely have a very different number of events written to them. In fact, the usage of most web services follows a <a href="https://en.wikipedia.org/wiki/Pareto_distribution">Pareto distribution</a>, meaning that the top few users will account for the vast majority of the usage. Pareto distributions are common and look like this:</p>
<p><img src="/assets/upstream/images/analytics/total-usage.png" alt="In this graphic, each bar represents a user; the height of the bar is their total usage." /></p>
<p>If we took a <a href="https://en.wikipedia.org/wiki/Simple_random_sample">simple random sample</a> of one percent (1%) of this data, and we applied that to the whole population, you may be able to track your largest customers accurately — but you would lose visibility into what your smaller customers are doing:</p>
<p><img src="/assets/upstream/images/analytics/sample-data.png" alt="The same graphic as above, but now based on a 1% sample of the data." /></p>
<p>Notice that the larger bars look more or less unchanged, and yet they are still quite accurate. But as you analyze smaller customers, results get <a href="https://en.wikipedia.org/wiki/Quantization_(signal_processing)">quantized</a> and may even be rounded to 0 entirely.</p>
<p>This shows that while a one percent (1%) or even smaller sample of a large population may be sufficient, we may need to store a larger proportion of events for a small population to get accurate results.</p>
<p>We do this through a technique called equitable sampling. This means that we will equalize the number of events we store for each unique index value. For relatively uncommon index values, we may write all of the data points that we get via <code>writeDataPoint()</code>.  But if you write lots of data points to a single index value, we will start to sample.</p>
<p>Here is the same distribution, but now with (a simulation of) equitable sampling applied:</p>
<p><img src="/assets/upstream/images/analytics/equitable-sampling.png" alt="This graphic shows the same population, but with equitable sampling." /></p>
<p>You may notice that this graphic is very similar to the first graph. However, it only requires <code>&lt;10%</code> of the data to be stored overall. The sample rate is actually much lower than <code>10%</code> for the larger series (that is, we store larger sample intervals), but the sample rate is higher for the smaller series.</p>
<p>Refer back to the mapping analogy above. Regardless of the map area shown, the total number of pixels in the map stays constant. Similarly, we always want to store a similar number of data points for each index value. However, the resolution of the map — how much area is represented by each pixel — will change based on the area being shown. Similarly here, the amount of data represented by each stored data point will vary, based on the total number of data points in the index.</p>
<h2 id="adaptive-bit-rate-sampling-at-read-time">Adaptive Bit Rate Sampling at Read Time</h2>
<p>Equitable sampling ensures that an equal amount of data is maintained for each index within a specific time frame. However, queries can vary significantly in the duration of time they target. Some queries may only require a 10-minute data snapshot, while others might need to analyze data spanning 10 weeks — a period which is 10,000 times longer.</p>
<p>To address this issue, we employ a method called <a href="https://blog.cloudflare.com/explaining-cloudflares-abr-analytics/">adaptive bit rate</a> (ABR). With ABR, queries that cover longer time ranges will retrieve data from a higher sample interval, allowing them to be completed within a fixed time limit. In simpler terms, just as screen size or bandwidth is a fixed resource in our mapping analogy, the time required to complete a query is also fixed. Therefore, irrespective of the volume of data involved, we need to limit the total number of rows scanned to provide an answer to the query. This helps to ensure fairness: regardless of the size of the underlying dataset being queried, we ensure that all queries receive an equivalent share of the available computing time.</p>
<p>To achieve this, we store the data in multiple resolutions (that is, with different levels of detail, for instance, 100%, 10%, 1%) derived from the equitably sampled data. At query time, we select the most suitable data resolution to read based on the query's complexity. The query's complexity is determined by the number of rows to be retrieved and the probability of the query completing within a specified time limit of N seconds. By dynamically selecting the appropriate resolution, we optimize the query performance and ensure it stays within the allotted time budget.</p>
<p>ABR offers a significant advantage by enabling us to consistently provide query results within a fixed query budget, regardless of the data size or time span involved. This sets it apart from systems that struggle with timeouts, errors, or high costs when dealing with extensive datasets.</p>
<h2 id="how-to-select-an-index">How to select an index</h2>
<p>In order to get accurate results with sampled data, select an appropriate value to use as your index. The index should match how users will query and view data. For example, if users frequently view data based on a specific device or hostname, it is recommended to incorporate those attributes into your index.</p>
<p>The index has the following properties, which are important to consider when choosing an index:</p>
<ul>
<li>Get accurate summary statistics about your entire dataset, across all index values.</li>
<li>Get an accurate count of the number of unique values of your index.</li>
<li>Get accurate summary statistics (for example, count, sum) within a particular index value.</li>
<li>See the <code>Top N</code> values of specific fields that are not in your index.</li>
<li>Filter on most fields.</li>
<li>Run other aggregations like quantiles.</li>
</ul>
<p>Some limitations and trade-offs to consider are:</p>
<ul>
<li>You may not be able to get accurate unique counts of fields that are not in your index.
<ul>
<li>For example, if you index on <code>hostname</code>, you may not be able to count the number of unique URLs.</li>
</ul>
</li>
<li>You may not be able to observe very rare values of fields not in the index.
<ul>
<li>For example, a particular URL for a hostname, if you index on host and have millions of unique URLs.</li>
</ul>
</li>
<li>You may not be able to run accurate queries across multiple indices at once.
<ul>
<li>For example, you may only be able to query for one host at a time (or all of them) and expect accurate results.</li>
</ul>
</li>
<li>There is no guarantee you can retrieve any one individual record.</li>
<li>You cannot necessarily reconstruct exact sequences of events.</li>
</ul>
<p>It is not recommended to write a unique index value on every row (like a UUID) for most use cases. While this will make it possible to retrieve individual data points very quickly, it will slow down most queries for aggregations and time series.</p>
<p>Refer to the Workers Analytics Engine FAQs, for common question about <a href="/analytics/faq/wae-faqs/#sampling">Sampling</a>.</p>
