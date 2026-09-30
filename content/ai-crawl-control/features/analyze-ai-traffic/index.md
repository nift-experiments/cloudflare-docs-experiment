<p>AI Crawl Control metrics provide you with insight on how AI crawlers are interacting with your website (<a href="/fundamentals/concepts/accounts-and-zones/#zones">Cloudflare zone</a>).</p>
<p>To view AI Crawl Control metrics:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<p>You can find meaningful information across the <strong>Overview</strong>, <strong>Crawlers</strong>, and <strong>Metrics</strong> tabs.</p>
<h2 id="view-the-overview-tab">View the Overview tab</h2>
<p>The <strong>Overview</strong> tab provides a snapshot of AI crawler activity:</p>
<table>
<thead>
<tr>
<th>Component</th>
<th>What you can do</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Executive summary</strong></td>
<td>Review total request volume, volume change, most common status code, most popular path, and high-volume crawler activity.</td>
</tr>
<tr>
<td><strong>Managed robots.txt status</strong></td>
<td>Check whether <a href="/bots/additional-configurations/managed-robots-txt/">Cloudflare managed robots.txt</a> is enabled for your zone.</td>
</tr>
<tr>
<td><strong>Metrics with trend charts</strong></td>
<td>Monitor total requests, allowed requests, unsuccessful requests, and total referrals (paid plans only).</td>
</tr>
<tr>
<td><strong>Crawlers grouped by operators</strong></td>
<td>Explore crawlers organized by company (OpenAI, Microsoft, Google, ByteDance, Anthropic, Meta) with allowed requests, referrals (paid plans only), and activity change percentages. Select a crawler or operator to drill down in the <strong>Crawlers</strong> tab.</td>
</tr>
<tr>
<td><strong>Filters</strong></td>
<td>Customize your view by date range, crawler, operator, hostname, or path. All metrics update dynamically.</td>
</tr>
</tbody>
</table>
<h2 id="view-the-crawlers-tab">View the Crawlers tab</h2>
<p>The <strong>Crawlers</strong> tab provides detailed information about individual AI crawlers and allows you to set <strong>Block</strong> or <strong>Allow</strong> controls:</p>
<table>
<thead>
<tr>
<th>Column</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Crawler</strong></td>
<td>The name of the AI crawler.</td>
</tr>
<tr>
<td><strong>Operator</strong></td>
<td>The company that operates the crawler.</td>
</tr>
<tr>
<td><strong>Data transfer</strong></td>
<td>Total bandwidth consumed by this crawler's requests. Formatted as KB, MB, or GB.</td>
</tr>
<tr>
<td><strong>Requests</strong></td>
<td>Total number of requests from this crawler.</td>
</tr>
<tr>
<td><strong>Action</strong></td>
<td>Current access control setting (Allow or Block).</td>
</tr>
</tbody>
</table>
<p>For more information on managing crawler access, refer to <a href="/ai-crawl-control/features/manage-ai-crawlers/">Manage AI crawlers</a>.</p>
<h2 id="view-the-metrics-tab">View the Metrics tab</h2>
<p>The <strong>Metrics</strong> tab provides detailed analytics and charts to help you understand how AI crawlers are interacting with your website.</p>
<h3 id="requests-over-time">Requests over time</h3>
<p>Visualize crawler activity patterns over the selected time period. Use the view selector to switch between metrics:</p>
<table>
<thead>
<tr>
<th>View</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>All requests</strong></td>
<td>Total requests including blocked and error responses.</td>
</tr>
<tr>
<td><strong>Allowed requests</strong></td>
<td>Requests that received a successful response (status 200-299).</td>
</tr>
<tr>
<td><strong>Data transfer</strong></td>
<td>Bandwidth consumption for allowed requests over time, formatted as KB, MB, or GB.</td>
</tr>
</tbody>
</table>
<p>You can group the data by different dimensions:</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Crawler</strong></td>
<td>Track activity from individual AI crawlers (such as GPTBot, ClaudeBot, Bytespider).</td>
</tr>
<tr>
<td><strong>Category</strong></td>
<td>Analyze crawlers by their purpose or type.</td>
</tr>
<tr>
<td><strong>Operator</strong></td>
<td>Discover which companies (such as OpenAI, Anthropic, ByteDance) are crawling your site.</td>
</tr>
<tr>
<td><strong>Host</strong></td>
<td>Break down activity across multiple subdomains.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2745.md")
</aside>
<h3 id="status-code-distribution">Status code distribution</h3>
<p>The <strong>Status code distribution</strong> chart shows HTTP response codes for AI crawler requests over time:</p>
<ul>
<li><strong>2xx</strong> — Successful responses</li>
<li><strong>3xx</strong> — Redirects</li>
<li><strong>4xx</strong> — Client errors (including 403 blocked and 402 payment required)</li>
<li><strong>5xx</strong> — Server errors</li>
</ul>
<p>Use this chart to identify patterns in how your site responds to AI crawlers, including the distribution of error codes and the volume of redirects.</p>
<h3 id="content-format">Content Format</h3>
<p>The <strong>Content Format</strong> chart shows what content types AI systems request versus what your origin serves. This visibility helps you understand content negotiation patterns and optimize how your content is delivered to AI systems.</p>
<p>The chart includes three views:</p>
<table>
<thead>
<tr>
<th>View</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Comparison</strong></td>
<td>A grouped bar chart comparing requested content types versus served content types</td>
</tr>
<tr>
<td><strong>Request Type</strong></td>
<td>Breakdown of requests by Accept header</td>
</tr>
<tr>
<td><strong>Response Type</strong></td>
<td>Breakdown of responses by Content-Type header</td>
</tr>
</tbody>
</table>
<h3 id="top-referrers">Top referrers</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2744.md")
</aside>
<p>Identify traffic sources with referrer analytics to understand discovery patterns and content popularity from AI operators.</p>
<table>
<thead>
<tr>
<th>View</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Referral sources</strong></td>
<td>Top domains sending AI-driven referral traffic to your site (for example, <code>chatgpt.com</code>, <code>perplexity.ai</code>).</td>
</tr>
<tr>
<td><strong>Destination patterns</strong></td>
<td>Which site areas receive the most AI-driven referral traffic, grouped by pattern (for example, <code>/blog/*</code>, <code>/api/*</code>).</td>
</tr>
</tbody>
</table>
<p>Toggle between views using the tabs in the Top referrers section.</p>
<h3 id="referrals-over-time">Referrals over time</h3>
<p>Track referral traffic trends over your selected time period. Group by:</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Operator</strong></td>
<td>Stacked area chart showing referrals by company (OpenAI, Anthropic, etc.).</td>
</tr>
<tr>
<td><strong>Source</strong></td>
<td>Top referral URLs driving traffic.</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td>Aggregate referral volume.</td>
</tr>
</tbody>
</table>
<h3 id="most-popular-paths">Most popular paths</h3>
<p>The <strong>Most popular paths</strong> table shows which pages on your site are most frequently requested by AI crawlers.</p>
<table>
<thead>
<tr>
<th>Column</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Path</strong></td>
<td>The page path that was requested.</td>
</tr>
<tr>
<td><strong>Hostname</strong></td>
<td>The hostname of the requested page.</td>
</tr>
<tr>
<td><strong>Referrals</strong></td>
<td>Number of referral visits to this path from AI platforms.</td>
</tr>
<tr>
<td><strong>Allowed requests</strong></td>
<td>Number of successful requests to this path.</td>
</tr>
</tbody>
</table>
<p>To see a breakdown by crawler per path, use the top-level filters.</p>
<h4 id="analyze-site-areas-with-pattern-grouping">Analyze site areas with pattern grouping</h4>
<p>Select the <strong>Patterns</strong> tab to see requests grouped by URI pattern (such as <code>/blog/*</code>, <code>/api/v1/*</code>, or <code>/docs/*</code>). This helps you quickly identify which areas of your site AI crawlers target most.</p>
<p>Pattern grouping aggregates individual paths into site areas:</p>
<ul>
<li>Patterns include up to 2 levels of depth (for example, <code>/api/*</code>, <code>/api/v1/*</code>)</li>
<li>The root pattern <code>/*</code> shows total traffic across your site</li>
<li>Patterns are not aggregated across hostnames</li>
<li>Single-path patterns display without wildcards (for example, <code>sitemap.xml</code> instead of <code>sitemap.xml/*</code>)</li>
</ul>
<p>Additional tabs include:</p>
<ul>
<li><strong>All</strong> — Combined content and media requests (individual paths, not patterns)</li>
<li><strong>Content</strong> — HTML, JSON, and text content</li>
<li><strong>Media</strong> — Images, videos, and other media files</li>
</ul>
<h2 id="filter-and-export-data">Filter and export data</h2>
<p>Use the filter bar to narrow your analysis by multiple criteria:</p>
<table>
<thead>
<tr>
<th>Filter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Date range</strong></td>
<td>Select the time period to analyze.</td>
</tr>
<tr>
<td><strong>Crawler</strong></td>
<td>Filter to specific AI crawlers.</td>
</tr>
<tr>
<td><strong>Operator</strong></td>
<td>Filter to specific companies.</td>
</tr>
<tr>
<td><strong>Hostname</strong></td>
<td>Filter to specific subdomains.</td>
</tr>
<tr>
<td><strong>Path</strong></td>
<td>Filter to specific URL paths or patterns.</td>
</tr>
</tbody>
</table>
<p>Combine multiple filters for complex analysis. All metrics and charts update dynamically based on your filter selection.</p>
<p>To export your data, select <strong>Download CSV</strong> or <strong>Download image</strong>. Downloads include all applied filters and groupings.</p>
<h2 id="per-crawler-drilldowns">Per-crawler drilldowns</h2>
<p>The <strong>Crawlers</strong> tab includes an actions menu for each crawler with the following options:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>View Metrics</strong></td>
<td>Filter the <strong>Metrics</strong> tab to the selected crawler.</td>
</tr>
<tr>
<td><strong>View on Cloudflare Radar</strong></td>
<td>Learn more about each verified crawler on Cloudflare Radar.</td>
</tr>
<tr>
<td><strong>View in Security Analytics</strong></td>
<td>Filter Security Analytics by detection IDs (<a href="/bots/get-started/bot-management/">Bot Management</a> customers).</td>
</tr>
<tr>
<td><strong>Copy User Agent</strong></td>
<td>Copy user agent strings for use in <a href="/waf/custom-rules/">WAF custom rules</a>, <a href="/rules/url-forwarding/">Redirect Rules</a>, or robots.txt files.</td>
</tr>
<tr>
<td><strong>Copy Detection ID</strong></td>
<td>Copy detection IDs for use in <a href="/waf/custom-rules/">WAF custom rules</a> (<a href="/bots/get-started/bot-management/">Bot Management</a> customers).</td>
</tr>
</tbody>
</table>
<h2 id="programmatic-access">Programmatic access</h2>
<p>For programmatic access to AI Crawl Control analytics, use the <a href="/ai-crawl-control/reference/graphql-api/">GraphQL Analytics API</a>. The API provides access to the same data available in the dashboard, including detection IDs, referrer data, and data transfer metrics.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/ai-crawl-control/reference/graphql-api/">GraphQL API reference</a></li>
<li><a href="/ai-crawl-control/features/manage-ai-crawlers/">Manage AI crawlers</a></li>
<li><a href="/ai-crawl-control/features/track-robots-txt/">Track robots.txt</a></li>
</ul>
