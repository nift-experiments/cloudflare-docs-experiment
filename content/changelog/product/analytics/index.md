<h1 id="changelog">Changelog</h1>

<h2 id="websocket-reporting-now-includes-full-connection-data-transfer-and-duration"><a href="/changelog/post/2026-08-14-websocket-data-transfer-reporting/">WebSocket reporting now includes full connection data transfer and duration</a></h2>
<p><em>2026-08-14</em></p>
<p>Cloudflare has fixed an issue affecting WebSocket data transfer and session duration reporting. HTTP Traffic Analytics and HTTP request logs now correctly report data transferred throughout a WebSocket connection and the duration of the full session. During the affected period, reporting captured only the bytes and duration of the initial <code>101 Switching Protocols</code> handshake for some WebSocket connections.</p>
<p>Customers with WebSocket traffic will see the correct <strong>Data Transfer</strong> in the dashboard and <code>EdgeResponseBytes</code> in analytics and HTTP request logs. Reported session duration now reflects the full WebSocket session rather than only the handshake. These changes restore the accounting of existing WebSocket traffic and duration. They do not indicate an increase in traffic or alter WebSocket connection behavior.</p>
<p>The separate <a href="/logs/logpush/logpush-job/datasets/zone/websocket_analytics/">WebSocket Analytics Logpush dataset</a> continues to provide per-connection directional byte counts, timestamps, and close details.</p>
<p>For more information about HTTP Traffic Analytics, refer to <a href="/analytics/account-and-zone-analytics/zone-analytics/#http-traffic">Zone Analytics</a>.</p>


<h2 id="custom-dashboards-available-to-all-customers"><a href="/changelog/post/2026-04-22-custom-dashboards-ga/">Custom dashboards available to all customers</a></h2>
<p><em>2026-04-22</em></p>
<p>Custom Dashboards are now available to all Cloudflare customers. Build personalized views that highlight the metrics most critical to your infrastructure and security posture, moving beyond standard product dashboards.</p>
<p>This update significantly expands the data available for visualization. Build charts based on any of the <strong>100+ datasets</strong> available via the Cloudflare GraphQL API, covering everything from WAF events and Workers metrics to Load Balancing and Zero Trust logs.</p>
<h4 id="2026-04-22-custom-dashboards-ga-log-explorer-integration">Log Explorer integration</h4>
<p>Log Explorer customers can select Log Explorer datasets to create charts from raw, unsampled log data.</p>
<h4 id="2026-04-22-custom-dashboards-ga-key-benefits">Key benefits</h4>
<ul>
<li><strong>Unified visibility</strong>: Consolidate signals from different Cloudflare products (for example, HTTP Traffic and R2 Storage) into a single view.</li>
<li><strong>Flexible monitoring</strong>: Create charts that focus on specific status codes, ASN regions, or security actions that matter to your business.</li>
<li><strong>Expanded limits</strong>: Log Explorer customers can create up to <strong>100 dashboards</strong> (up from 25 for standard customers).</li>
</ul>
<p><img src="/assets/upstream/images/analytics/customdashboardshome.jpg" alt="Custom Dashboards home page showing dashboard list and chart previews" /></p>
<p>To get started, refer to the <a href="/analytics/custom-dashboards/">Custom Dashboards documentation</a>.</p>


<h2 id="new-cfworker-metric-in-server-timing-header"><a href="/changelog/post/2026-02-18-cfworker-server-timing/">New cfWorker metric in Server-Timing header</a></h2>
<p><em>2026-02-18</em></p>
<p>The Server-Timing header now includes a new <code>cfWorker</code> metric that measures time spent executing Cloudflare Workers, including any subrequests performed by the Worker. This helps developers accurately identify whether high Time to First Byte (TTFB) is caused by Worker processing or slow upstream dependencies.</p>
<p>Previously, Worker execution time was included in the <code>edge</code> metric, making it harder to identify true edge performance. The new <code>cfWorker</code> metric provides this visibility:</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>edge</code></td>
<td>Total time spent on the Cloudflare edge, including Worker execution</td>
</tr>
<tr>
<td><code>origin</code></td>
<td>Time spent fetching from the origin server</td>
</tr>
<tr>
<td><code>cfWorker</code></td>
<td>Time spent in Worker execution, including subrequests but excluding origin fetch time</td>
</tr>
</tbody>
</table>
<h4 id="2026-02-18-cfworker-server-timing-example-response">Example response</h4>
<pre><code class="language-txt">Server-Timing: cdn-cache; desc=DYNAMIC, edge; dur=20, origin; dur=100, cfWorker; dur=7&#10;</code></pre>
<p>In this example, the edge took 20ms, the origin took 100ms, and the Worker added just 7ms of processing time.</p>
<h4 id="2026-02-18-cfworker-server-timing-availability">Availability</h4>
<p>The <code>cfWorker</code> metric is enabled by default if you have <a href="/web-analytics/">Real User Monitoring (RUM)</a> enabled. Otherwise, you can enable it using <a href="/rules/">Rules</a>.</p>
<p>This metric is particularly useful for:</p>
<ul>
<li><strong>Performance debugging</strong>: Quickly determine if latency is caused by Worker code, external API calls within Workers, or slow origins.</li>
<li><strong>Optimization targeting</strong>: Identify which component of your request path needs optimization.</li>
<li><strong>Real User Monitoring (RUM)</strong>: Access detailed timing breakdowns directly from response headers for client-side analytics.</li>
</ul>
<p>For more information about Server-Timing headers, refer to the <a href="https://www.w3.org/TR/server-timing/">W3C Server Timing specification</a>.</p>


<h2 id="improved-accuracy-of-cached-request-classification-in-analytics"><a href="/changelog/post/2025-12-18-cached-request-classification/">Improved accuracy of cached request classification in analytics</a></h2>
<p><em>2025-12-18</em></p>
<p>The cached/uncached classification logic used in Zone Overview analytics has been updated to improve accuracy.</p>
<p>Previously, requests were classified as &quot;cached&quot; based on an overly broad condition that included blocked 403 responses, Snippets requests, and other non-cache request types. This caused inflated cache hit ratios — in some cases showing near-100% cached — and affected approximately 15% of requests classified as cached in rollups.</p>
<p>The condition has been removed from the Zone Overview page. Cached/uncached classification now aligns with the heuristics used in <a href="/analytics/account-and-zone-analytics/zone-analytics/">HTTP Analytics</a>, so only requests genuinely served from cache are counted as cached.</p>
<p><strong>What changed:</strong></p>
<ul>
<li><strong>Zone Overview</strong> — Cache ratios now reflect actual cache performance.</li>
<li><strong>HTTP Analytics</strong> — No change. HTTP Analytics already used the correct classification logic.</li>
<li><strong>Historical data</strong> — This fix applies to new requests only. Previously logged data is not retroactively updated.</li>
</ul>


<h2 id="new-confidence-intervals-in-graphql-analytics-api"><a href="/changelog/post/2025-10-01-confidence-intervals/">New Confidence Intervals in GraphQL Analytics API</a></h2>
<p><em>2025-10-01</em></p>
<p>The GraphQL Analytics API now supports confidence intervals for <code>sum</code> and <code>count</code> fields on adaptive (sampled) datasets. Confidence intervals provide a statistical range around sampled results, helping verify accuracy and quantify uncertainty.</p>
<ul>
<li><strong>Supported datasets</strong>: Adaptive (sampled) datasets only.</li>
<li><strong>Supported fields</strong>: All <code>sum</code> and <code>count</code> fields.</li>
<li><strong>Usage</strong>: The confidence <code>level</code> must be provided as a decimal between 0 and 1 (e.g. <code>0.90</code>, <code>0.95</code>, <code>0.99</code>).</li>
<li><strong>Default</strong>: If no confidence level is specified, no intervals are returned.</li>
</ul>
<p>For examples and more details, see the <a href="/analytics/graphql-api/features/confidence-intervals/">GraphQL Analytics API documentation</a>.</p>


<h2 id="new-graphql-analytics-api-explorer-and-mcp-server"><a href="/changelog/post/2025-05-23-graphql-api-explorer/">New GraphQL Analytics API Explorer and MCP Server</a></h2>
<p><em>2025-05-23</em></p>
<p>We’ve launched two powerful new tools to make the GraphQL Analytics API more accessible:</p>
<h4 id="2025-05-23-graphql-api-explorer-graphql-api-explorer">GraphQL API Explorer</h4>
<p>The new <a href="https://graphql.cloudflare.com/explorer">GraphQL API Explorer</a> helps you build, test, and run queries directly in your browser. Features include:</p>
<ul>
<li>In-browser schema documentation to browse available datasets and fields</li>
<li>Interactive query editor with autocomplete and inline documentation</li>
<li>A &quot;Run in GraphQL API Explorer&quot; button to execute example queries from our docs</li>
<li>Seamless OAuth authentication — no manual setup required</li>
</ul>
<p><img src="/assets/upstream/images/changelog/analytics/graphql-api-explorer.png" alt="GraphQL API Explorer" /></p>
<h4 id="2025-05-23-graphql-api-explorer-graphql-model-context-protocol-mcp-server">GraphQL Model Context Protocol (MCP) Server</h4>
<p>MCP Servers let you use natural language tools like Claude to generate structured queries against your data. See our <a href="https://blog.cloudflare.com/thirteen-new-mcp-servers-from-cloudflare/">blog post</a> for details on how they work and which servers are available. The new <a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/graphql">GraphQL MCP server</a> helps you discover and generate useful queries for the GraphQL Analytics API. With this server, you can:</p>
<ul>
<li>Explore what data is available to query</li>
<li>Generate and refine queries using natural language, with one-click links to run them in the API Explorer</li>
<li>Build dashboards and visualizations from structured query outputs</li>
</ul>
<p>Example prompts include:</p>
<ul>
<li>“Show me HTTP traffic for the last 7 days for example.com”</li>
<li>“What GraphQL node returns firewall events?”</li>
<li>“Can you generate a link to the Cloudflare GraphQL API Explorer with a pre-populated query and variables?”</li>
</ul>
<p>We’re continuing to expand these tools, and your feedback helps shape what’s next. <a href="/analytics/graphql-api/">Explore the documentation</a> to learn more and get started.</p>



