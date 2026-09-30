---
cp9:
  canonical: https://developers.cloudflare.com/privacy-gateway/reference/metrics/
  description: Query Privacy Gateway traffic and performance data using the GraphQL Analytics API.
  full_title: Privacy Gateway Metrics · Cloudflare Privacy Gateway docs
  head_html: <title>Privacy Gateway Metrics · Cloudflare Privacy Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Query Privacy Gateway traffic and performance data using the GraphQL Analytics API."><link rel="canonical" href="https://developers.cloudflare.com/privacy-gateway/reference/metrics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/privacy-gateway/reference/metrics/index.md"><meta property="og:title" content="Privacy Gateway Metrics · Cloudflare Privacy Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Query Privacy Gateway traffic and performance data using the GraphQL Analytics API."><meta property="og:url" content="https://developers.cloudflare.com/privacy-gateway/reference/metrics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Privacy Gateway"><meta name="algolia_product_filter" content="Privacy Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Privacy Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/privacy-gateway/reference/metrics/#page","headline":"Privacy Gateway Metrics \u00b7 Cloudflare Privacy Gateway docs","description":"Query Privacy Gateway traffic and performance data using the GraphQL Analytics API.","url":"https://developers.cloudflare.com/privacy-gateway/reference/metrics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /privacy-gateway/reference/metrics/
  schema: 1
---
<p>Privacy Gateway now supports enhanced monitoring through our GraphQL API, providing detailed insights into your gateway traffic and performance. To access these metrics, ensure you have:</p>
<ul>
<li>A relay gateway proxy implementation where Cloudflare acts as the oblivious relay party.</li>
<li>An API token with Analytics Read permissions.
We offer two GraphQL nodes to retrieve metrics: <code>ohttpMetricsAdaptive</code> and <code>ohttpMetricsAdaptiveGroups</code>. The first node provides comprehensive request data, while the second facilitates grouped analytics.</li>
</ul>
<h2 id="ohttpmetricsadaptive">ohttpMetricsAdaptive</h2>
<p>The <code>ohttpMetricsAdaptive</code> node is designed for detailed insights into individual OHTTP requests with adaptive sampling. This node can help in understanding the performance and load on your server and client setup.</p>
<h3 id="key-arguments">Key Arguments</h3>
<ul>
<li><code>filter</code> required
<ul>
<li>Apply filters to narrow down your data set. <code>accountTag</code> is a required filter.</li>
</ul>
</li>
<li><code>limit</code>  optional
<ul>
<li>Specify the maximum number of records to return.</li>
</ul>
</li>
<li><code>orderBy</code> optional
<ul>
<li>Choose how to sort your data, with options for various dimensions and metrics.</li>
</ul>
</li>
</ul>
<h3 id="available-fields">Available Fields</h3>
<ul>
<li><code>bytesToClient</code> int optional
<ul>
<li>The number of bytes returned to the client.</li>
</ul>
</li>
<li><code>bytesToGateway</code> int optional
<ul>
<li>Total bytes received from the client.</li>
</ul>
</li>
<li><code>colo</code> string optional
<ul>
<li>Airport code of the Cloudflare data center that served the request.</li>
</ul>
</li>
<li><code>datetime</code> Time optional
<ul>
<li>The date and time when the event was recorded.</li>
</ul>
</li>
<li><code>gatewayStatusCode</code> int optional
<ul>
<li>Status code returned by the gateway.</li>
</ul>
</li>
<li><code>relayStatusCode</code> int optional
<ul>
<li>Status code returned by the relay.</li>
</ul>
</li>
</ul>
<p>This node is useful for a granular view of traffic, helping you identify patterns, performance issues, or anomalies in your data flow.</p>
<h2 id="ohttpmetricsadaptivegroups">ohttpMetricsAdaptiveGroups</h2>
<p>The <code>ohttpMetricsAdaptiveGroups</code> node allows for aggregated analysis of OHTTP request metrics with adaptive sampling. This node is particularly useful for identifying trends and patterns across different dimensions of your traffic and operations.</p>
<h3 id="key-arguments-1">Key Arguments</h3>
<ul>
<li><code>filter</code> required
<ul>
<li>Apply filters to narrow down your data set. <code>accountTag</code> is a required filter.</li>
</ul>
</li>
<li><code>limit</code>  optional
<ul>
<li>Specify the maximum number of records to return.</li>
</ul>
</li>
<li><code>orderBy</code> optional
<ul>
<li>Choose how to sort your data, with options for various dimensions and metrics.</li>
</ul>
</li>
</ul>
<h3 id="available-fields-1">Available Fields</h3>
<ul>
<li><code>count</code> int optional
<ul>
<li>The number of records that meet the criteria.</li>
</ul>
</li>
<li><code>dimensions</code> optional
<ul>
<li>Specifies the grouping dimensions for your data.</li>
</ul>
</li>
<li><code>sum</code> optional
<ul>
<li>Aggregated totals for various metrics, per dimension.</li>
</ul>
</li>
</ul>
<p><strong>Dimensions</strong></p>
<p>You can group your metrics by various dimensions to get a more segmented view of your data:</p>
<ul>
<li><code>colo</code> string optional
<ul>
<li>The airport code of the Cloudflare data center.</li>
</ul>
</li>
<li><code>date</code> Date optional
<ul>
<li>The date of OHTTP request metrics.</li>
</ul>
</li>
<li><code>datetimeFifteenMinutes</code> Time optional
<ul>
<li>Timestamp truncated to fifteen minutes.</li>
</ul>
</li>
<li><code>datetimeFiveMinutes</code> Time optional
<ul>
<li>Timestamp truncated to five minutes.</li>
</ul>
</li>
<li><code>datetimeHour</code> Time optional
<ul>
<li>Timestamp truncated to the hour.</li>
</ul>
</li>
<li><code>datetimeMinute</code> Time optional
<ul>
<li>Timestamp truncated to the minute.</li>
</ul>
</li>
<li><code>endpoint</code> string optional
<ul>
<li>The appId that generated traffic.</li>
</ul>
</li>
<li><code>gatewayStatusCode</code> int optional
<ul>
<li>Status code returned by the gateway.</li>
</ul>
</li>
<li><code>relayStatusCode</code> int optional
<ul>
<li>Status code returned by the relay.</li>
</ul>
</li>
</ul>
<p><strong>Sum Fields</strong></p>
<p>Sum fields offer a cumulative view of various metrics over your selected time period:</p>
<ul>
<li><code>bytesToClient</code> int optional
<ul>
<li>Total bytes sent from the gateway to the client.</li>
</ul>
</li>
<li><code>bytesToGateway</code> int optional
<ul>
<li>Total bytes from the client to the gateway.</li>
</ul>
</li>
<li><code>clientRequestErrors</code> int optional
<ul>
<li>Total number of client request errors.</li>
</ul>
</li>
<li><code>gatewayResponseErrors</code> int optional
<ul>
<li>Total number of gateway response errors.</li>
</ul>
</li>
</ul>
<p>Utilize the ohttpMetricsAdaptiveGroups node to gain comprehensive, aggregated insights into your traffic patterns, helping you optimize performance and user experience.</p>
