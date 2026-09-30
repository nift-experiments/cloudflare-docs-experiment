---
cp9:
  canonical: https://developers.cloudflare.com/workers/observability/metrics-and-analytics/
  description: Diagnose issues with Workers metrics, and review request data for a zone with Workers analytics.
  full_title: Metrics and analytics · Cloudflare Workers docs
  head_html: <title>Metrics and analytics · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Diagnose issues with Workers metrics, and review request data for a zone with Workers analytics."><link rel="canonical" href="https://developers.cloudflare.com/workers/observability/metrics-and-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/observability/metrics-and-analytics/index.md"><meta property="og:title" content="Metrics and analytics · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Diagnose issues with Workers metrics, and review request data for a zone with Workers analytics."><meta property="og:url" content="https://developers.cloudflare.com/workers/observability/metrics-and-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/observability/metrics-and-analytics/#page","headline":"Metrics and analytics \u00b7 Cloudflare Workers docs","description":"Diagnose issues with Workers metrics, and review request data for a zone with Workers analytics.","url":"https://developers.cloudflare.com/workers/observability/metrics-and-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/observability/metrics-and-analytics/
  schema: 1
---
<p>There are two graphical sources of information about your Workers traffic at a given time: Workers metrics and zone-based Workers analytics.</p>
<p>Workers metrics can help you diagnose issues and understand your Workers' workloads by showing the performance and usage of your Workers. If your Worker runs on a route on a zone, or on a few zones, Workers metrics will show how much traffic your Worker is handling on a per-zone basis, and how many requests your site is getting.</p>
<p>Zone analytics show how much traffic all Workers assigned to a zone are handling.</p>
<h2 id="workers-metrics">Workers metrics</h2>
<p>Workers metrics aggregate request data for an individual Worker (if your Worker is running across multiple domains, and on <code>*.workers.dev</code>, metrics will aggregate requests across them). To view your Worker's metrics:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16250.md")
</div>
<p>There are two metrics that can help you understand the health of your Worker in a given moment: requests success and error metrics, and invocation statuses.</p>
<h3 id="requests">Requests</h3>
<p>The first graph shows historical request counts from the Workers runtime broken down into successful requests, errored requests, and subrequests.</p>
<ul>
<li><strong>Total</strong>: All incoming requests registered by a Worker. Requests blocked by <a href="https://www.cloudflare.com/waf/">WAF</a> or other security features will not count.</li>
<li><strong>Success</strong>: Requests that returned a Success or Client Disconnected invocation status.</li>
<li><strong>Errors</strong>: Requests that returned a Script Threw Exception, Exceeded Resources, or Internal Error invocation status — refer to <a href="/workers/observability/metrics-and-analytics/#invocation-statuses">Invocation Statuses</a> for a breakdown of where your errors are coming from.</li>
</ul>
<p>Request traffic data may display a drop off near the last few minutes displayed in the graph for time ranges less than six hours. This does not reflect a drop in traffic, but a slight delay in aggregation and metrics delivery.</p>
<h3 id="subrequests">Subrequests</h3>
<p>Subrequests are requests triggered by calling <code>fetch</code> from within a Worker. A subrequest that throws an uncaught error will not be counted.</p>
<ul>
<li><strong>Total</strong>: All subrequests triggered by calling <code>fetch</code> from within a Worker.</li>
<li><strong>Cached</strong>: The number of cached responses returned.</li>
<li><strong>Uncached</strong>: The number of uncached responses returned.</li>
</ul>
<h3 id="wall-time-per-execution">Wall time per execution</h3>
<p><span class="nb-glossary-tooltip" title="wall-clock time">Wall time</span> represents
the elapsed time in milliseconds between the start of a Worker invocation, and
when the Workers runtime determines that no more JavaScript needs to run.
Specifically, wall time per execution chart measures the wall time that the
JavaScript context remained open — including time spent waiting on I/O, and time
spent executing in your Worker's
<a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil()</code></a> handler. Wall time is
not the same as the time it takes your Worker to send the final byte of a
response back to the client - wall time can be higher, if tasks within
<code>waitUntil()</code> are still running after the response has been sent, or it can be
lower. For example, when returning a response with a large body, the Workers
runtime can, in some cases, determine that no more JavaScript needs to run, and
closes the JavaScript context before all the bytes have passed through and been
sent.</p>
<p>The Wall Time per execution chart shows historical wall time data broken down into relevant quantiles using <a href="https://en.wikipedia.org/wiki/Reservoir_sampling">reservoir sampling</a>. Learn more about <a href="https://www.statisticshowto.com/quantile-definition-find-easy-steps/">interpreting quantiles</a>.</p>
<h3 id="cpu-time-per-execution">CPU Time per execution</h3>
<p>The CPU Time per execution chart shows historical CPU time data broken down into relevant quantiles using <a href="https://en.wikipedia.org/wiki/Reservoir_sampling">reservoir sampling</a>. Learn more about <a href="https://www.statisticshowto.com/quantile-definition-find-easy-steps/">interpreting quantiles</a>. In some cases, higher quantiles may appear to exceed <a href="/workers/platform/limits/#cpu-time">CPU time limits</a> without generating invocation errors because of a mechanism in the Workers runtime that allows rollover CPU time for requests below the CPU limit.</p>
<h3 id="execution-duration-gb-seconds">Execution duration (GB-seconds)</h3>
<p>The Duration per request chart shows historical <a href="/workers/platform/limits/#duration">duration</a> per Worker invocation. The data is broken down into relevant quantiles, similar to the CPU time chart. Learn more about <a href="https://www.statisticshowto.com/quantile-definition-find-easy-steps/">interpreting quantiles</a>. Understanding duration on your Worker is especially useful when you are intending to do a significant amount of computation on the Worker itself.</p>
<h3 id="memory-usage">Memory usage</h3>
<p>The Memory usage chart shows how much V8 isolate memory your Worker uses at the time of each invocation, broken down into P50, P90, P99, and P999 percentiles using <a href="https://en.wikipedia.org/wiki/Reservoir_sampling">reservoir sampling</a>. For more information, refer to <a href="https://www.statisticshowto.com/quantile-definition-find-easy-steps/">Interpreting quantiles</a>.</p>
<p>Workers run in V8 <a href="/workers/reference/how-workers-works/#isolates">isolates</a>, each with a <a href="/workers/platform/limits/#memory">128 MB memory limit</a>. A single isolate can handle many concurrent requests and shares memory across them. The memory usage metric reflects how much of this shared memory is in use at the time of each invocation.</p>
<p>Deployment markers on the chart let you correlate memory changes with specific code deployments, making it easier to identify whether a new version introduced a memory regression.</p>
<p>If you see memory usage trending upward over time, this may indicate a memory leak. Use <a href="/workers/observability/dev-tools/memory-usage/">memory profiling with DevTools</a> locally to take heap snapshots and identify specific objects causing high memory consumption.</p>
<h3 id="invocation-statuses">Invocation statuses</h3>
<p>To review invocation statuses:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16252.md")
</div>
<p>Worker invocation statuses indicate whether a Worker executed successfully or failed to generate a response in the Workers runtime. Invocation statuses differ from <a href="/support/troubleshooting/http-status-codes/">HTTP status codes</a>. In some cases, a Worker invocation succeeds but does not generate a successful HTTP status because of another error encountered outside of the Workers runtime. Some invocation statuses result in a <a href="/workers/observability/errors/#error-pages-generated-by-workers">Workers error code</a> being returned to the client.</p>
<table>
<thead>
<tr>
<th>Invocation status</th>
<th>Definition</th>
<th>Workers error code</th>
<th>GraphQL field</th>
</tr>
</thead>
<tbody>
<tr>
<td>Success</td>
<td>Worker executed successfully</td>
<td></td>
<td><code>success</code></td>
</tr>
<tr>
<td>Client disconnected</td>
<td>HTTP client (that is, the browser) disconnected before the request completed</td>
<td></td>
<td><code>clientDisconnected</code></td>
</tr>
<tr>
<td>Worker threw exception</td>
<td>Worker threw an unhandled JavaScript exception</td>
<td>1101</td>
<td><code>scriptThrewException</code></td>
</tr>
<tr>
<td>Exceeded resources¹</td>
<td>Worker exceeded runtime limits</td>
<td>1102, 1027</td>
<td><code>exceededResources</code></td>
</tr>
<tr>
<td>Internal error²</td>
<td>Workers runtime encountered an error</td>
<td></td>
<td><code>internalError</code></td>
</tr>
</tbody>
</table>
<p>¹ The Exceeded Resources status may appear when the Worker exceeds a <a href="/workers/platform/limits/#request-and-response-limits">runtime limit</a>. The most common cause is excessive CPU time, but is also caused by a Worker exceeding startup time or free tier limits.</p>
<p>² The Internal Error status may appear when the Workers runtime fails to process a request due to an internal failure in our system. These errors are not caused by any issue with the Worker code nor any resource limit. While requests with Internal Error status are rare, some may appear during normal operation. These requests are not counted towards usage for billing purposes. If you notice an elevated rate of requests with Internal Error status, review <a href="https://www.cloudflarestatus.com/">www.cloudflarestatus.com</a>.</p>
<p>To further investigate exceptions, use <a href="/workers/wrangler/commands/general/#tail"><code>wrangler tail</code></a>.</p>
<h3 id="request-duration">Request duration</h3>
<p>The request duration chart shows how long it took your Worker to respond to requests, including code execution and time spent waiting on I/O. The request duration chart is currently only available when your Worker has <a href="/workers/configuration/placement/">Smart Placement</a> enabled.</p>
<p>In contrast to <a href="/workers/observability/metrics-and-analytics/#execution-duration-gb-seconds">execution duration</a>, which measures only the time a Worker is active, request duration measures from the time a request comes into a data center until a response is delivered.</p>
<p>The data shows the duration for requests with Smart Placement enabled compared to those with Smart Placement disabled (by default, 1% of requests are routed with Smart Placement disabled). The chart shows a histogram with duration across the x-axis and the percentage of requests that fall into the corresponding duration on the y-axis.</p>
<h3 id="metrics-retention">Metrics retention</h3>
<p>Worker metrics can be inspected for up to three months in the past in maximum increments of one week.</p>
<h2 id="zone-analytics">Zone analytics</h2>
<p>Zone analytics aggregate request data for all Workers assigned to any <a href="/workers/configuration/routing/routes/">routes</a> defined for a zone.</p>
<p>To review zone metrics:</p>
<p>In the Cloudflare dashboard, go to the <strong>Workers Analytics</strong> page for your zone.</p>
<div class="nb-dash-button"></div>
<p>Zone data can be scoped by time range within the last 30 days. The dashboard includes charts and information described below.</p>
<h3 id="subrequests-1">Subrequests</h3>
<p>This chart shows subrequests — requests triggered by calling <code>fetch</code> from within a Worker — broken down by cache status.</p>
<ul>
<li><strong>Uncached</strong>: Requests answered directly by your origin server or other servers responding to subrequests.</li>
<li><strong>Cached</strong>: Requests answered by Cloudflare’s <a href="https://www.cloudflare.com/learning/cdn/what-is-caching/">cache</a>. As Cloudflare caches more of your content, it accelerates content delivery and reduces load on your origin.</li>
</ul>
<h3 id="bandwidth">Bandwidth</h3>
<p>This chart shows historical bandwidth usage for all Workers on a zone broken down by cache status.</p>
<h3 id="status-codes">Status codes</h3>
<p>This chart shows historical requests for all Workers on a zone broken down by HTTP status code.</p>
<h3 id="total-requests">Total requests</h3>
<p>This chart shows historical data for all Workers on a zone broken down by successful requests, failed requests, and subrequests. These request types are categorized by HTTP status code where <code>200</code>-level requests are successful and <code>400</code> to <code>500</code>-level requests are failed.</p>
<h2 id="graphql">GraphQL</h2>
<p>Worker metrics are powered by GraphQL. Learn more about querying our data sets in the <a href="/analytics/graphql-api/tutorials/querying-workers-metrics/">Querying Workers Metrics with GraphQL tutorial</a>.</p>
<h2 id="custom-analytics-with-analytics-engine">Custom analytics with Analytics Engine</h2>
<p>The metrics described above provide insight into Worker performance and runtime behavior. For custom, application-specific analytics, use <a href="/analytics/analytics-engine/">Workers Analytics Engine</a>.</p>
<p>Analytics Engine is useful for:</p>
<ul>
<li><strong>Custom business metrics</strong> - Track events specific to your application, such as signups, purchases, or feature usage.</li>
<li><strong>Per-customer analytics</strong> - Record data with high-cardinality dimensions like customer IDs or API keys.</li>
<li><strong>Usage-based billing</strong> - Count API calls, compute units, or other billable events per customer.</li>
<li><strong>Performance tracking</strong> - Measure response times, cache hit rates, or error rates with custom dimensions.</li>
</ul>
<p>Writes to Analytics Engine are non-blocking and do not add latency to your Worker. Query your data using SQL through the <a href="/analytics/analytics-engine/sql-api/">Analytics Engine SQL API</a> or visualize it in <a href="/analytics/analytics-engine/grafana/">Grafana</a>.</p>
<p>Refer to the <a href="/workers/examples/analytics-engine/">Analytics Engine example</a> to get started.</p>
