---
cp9:
  canonical: https://developers.cloudflare.com/analytics/custom-dashboards/
  description: Create custom dashboards to monitor log data.
  full_title: Custom dashboards · Cloudflare Analytics docs
  head_html: <title>Custom dashboards · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Create custom dashboards to monitor log data."><link rel="canonical" href="https://developers.cloudflare.com/analytics/custom-dashboards/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/custom-dashboards/index.md"><meta property="og:title" content="Custom dashboards · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create custom dashboards to monitor log data."><meta property="og:url" content="https://developers.cloudflare.com/analytics/custom-dashboards/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Log Explorer"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/custom-dashboards/#page","headline":"Custom dashboards \u00b7 Cloudflare Analytics docs","description":"Create custom dashboards to monitor log data.","url":"https://developers.cloudflare.com/analytics/custom-dashboards/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/custom-dashboards/
  schema: 1
---
<p>Custom dashboards allow you to build personalized views that highlight the metrics most critical to your infrastructure and security posture. Move beyond standard product dashboards and consolidate data from multiple Cloudflare products into a single, unified view.</p>
<div class="nb-dash-button"></div>
<h2 id="what-you-can-do">What you can do</h2>
<p>Monitor security threats by tracking WAF blocks, bot scores, and threat patterns across your zones. Combine HTTP traffic data with security events to correlate attack patterns with traffic spikes.</p>
<p>Analyze application performance by visualizing origin response times, cache hit ratios, and error rates. Identify slow endpoints and understand how latency varies by region or device type.</p>
<p>Track business metrics by monitoring API usage, bandwidth consumption, and traffic patterns. Build executive dashboards that surface the KPIs that matter to your organization.</p>
<p>Investigate incidents so that when something goes wrong, you can create focused dashboards that combine the specific signals relevant to your investigation. Log Explorer customers can select Log Explorer datasets to create charts from raw, unsampled log data.</p>
<h2 id="availability">Availability</h2>
<p>Custom Dashboards are available to all Cloudflare customers.</p>
<table>
<thead>
<tr>
<th>Customer type</th>
<th>Dashboard limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>All Cloudflare customers</td>
<td>Up to 25 dashboards</td>
</tr>
<tr>
<td>Log Explorer customers</td>
<td>Up to 100 dashboards</td>
</tr>
</tbody>
</table>
<h2 id="get-started">Get started</h2>
<h3 id="start-from-a-template">Start from a template</h3>
<p>Templates are the fastest way to get value from Custom Dashboards. Each template is designed around a specific use case and includes pre-configured charts that surface the most relevant metrics.</p>
<table>
<thead>
<tr>
<th>Template</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Bot monitoring</strong></td>
<td>Understand what automated traffic is hitting your site — distinguish good bots (search engines, monitoring) from bad actors</td>
</tr>
<tr>
<td><strong>API Security</strong></td>
<td>Monitor your API endpoints for anomalies, track data transfer volumes, and identify unexpected access patterns</td>
</tr>
<tr>
<td><strong>Account takeover</strong></td>
<td>Watch for credential stuffing attacks by tracking failed login attempts, leaked credential usage, and suspicious authentication patterns</td>
</tr>
<tr>
<td><strong>API Performance</strong></td>
<td>Identify slow API endpoints, track error rates by endpoint, and monitor latency percentiles to catch regressions before users complain</td>
</tr>
<tr>
<td><strong>Performance monitoring</strong></td>
<td>Find bottlenecks in your origin infrastructure — which hosts are slow, which paths have high TTFB, and how performance trends over time</td>
</tr>
</tbody>
</table>
<p>After selecting a template, you can customize it by adding, removing, or modifying charts to fit your specific needs.</p>
<h3 id="build-from-scratch">Build from scratch</h3>
<p>For specialized monitoring needs, create a blank dashboard and add charts that query exactly the data you need.</p>
<p>Custom Dashboards support over 100 datasets available via the Cloudflare GraphQL API, including HTTP traffic, security events, Workers analytics, R2 Storage metrics, Load Balancing health, Zero Trust logs, DNS queries, and more.</p>
<h2 id="create-charts">Create charts</h2>
<h3 id="natural-language-prompts">Natural language prompts</h3>
<p>Describe what you want to see in plain English, and AI will construct the appropriate visualization:</p>
<ul>
<li>&quot;Show me error rates by country for the last 24 hours.&quot;</li>
<li>&quot;Compare cached vs uncached requests over time.&quot;</li>
<li>&quot;What are my top 10 paths by request volume?&quot;</li>
<li>&quot;Display WAF blocks grouped by rule ID.&quot;</li>
</ul>
<p>This is the fastest way to explore your data when you have a question but are not sure which dataset or metric to use.</p>
<h3 id="manual-configuration">Manual configuration</h3>
<p>For precise control, configure each element of your chart:</p>
<ul>
<li><strong>Dataset</strong> — The data source to query (HTTP requests, security events, Workers metrics, etc.)</li>
<li><strong>Metrics</strong> — What to measure (requests, bytes, duration) and how to aggregate it (sum, average, percentiles)</li>
<li><strong>Dimensions</strong> — How to break down the data (by country, status code, hostname, etc.)</li>
<li><strong>Filters</strong> — Conditions to narrow the data (specific paths, IP ranges, user agents, etc.)</li>
</ul>
<h3 id="chart-types">Chart types</h3>
<p>Choose the visualization that best fits your data:</p>
<table>
<thead>
<tr>
<th>Chart type</th>
<th>Best for</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Timeseries</strong></td>
<td>Trends and patterns over time — traffic spikes, latency changes, error rate fluctuations</td>
</tr>
<tr>
<td><strong>Bar</strong></td>
<td>Comparing values across categories — requests by country, errors by status code</td>
</tr>
<tr>
<td><strong>Donut</strong></td>
<td>Understanding proportions — cache hit ratio, traffic distribution by content type</td>
</tr>
<tr>
<td><strong>Map</strong></td>
<td>Geographic patterns — where your traffic originates, regional performance differences</td>
</tr>
<tr>
<td><strong>Stat</strong></td>
<td>Single important numbers — total requests today, current error rate, p99 latency</td>
</tr>
<tr>
<td><strong>Percentage</strong></td>
<td>Ratios and rates — cache hit percentage, bot traffic proportion</td>
</tr>
<tr>
<td><strong>Top N</strong></td>
<td>Rankings — busiest endpoints, most blocked IPs, top user agents</td>
</tr>
</tbody>
</table>
<h4 id="example-build-a-security-overview-chart">Example: Build a security overview chart</h4>
<p>To track blocked requests by WAF rule:</p>
<ol>
<li>Select the <strong>Security Events</strong> dataset.</li>
<li>Choose <strong>Events</strong> as the metric with <strong>Total</strong> aggregation.</li>
<li>Add <strong>Rule ID</strong> as a dimension to group by rule.</li>
<li>Filter to <strong>Action equals Block</strong> to focus on blocked traffic.</li>
<li>Select <strong>Bar</strong> chart to compare rule effectiveness.</li>
</ol>
<p>The result shows which WAF rules are triggering most frequently, helping you understand your threat landscape and tune your security configuration.</p>
<h2 id="dashboard-filters">Dashboard filters</h2>
<p>Dashboard filters apply to all charts at once, making it easy to focus your entire dashboard on a specific segment of traffic.</p>
<p>Common uses:</p>
<ul>
<li><strong>Time range</strong> — Zoom into a specific incident window across all charts</li>
<li><strong>Hostname</strong> — Focus on a single domain when you manage multiple properties</li>
<li><strong>Country</strong> — Analyze traffic patterns for a specific region</li>
<li><strong>Status code</strong> — Investigate error spikes by filtering to <code>5xx</code> responses</li>
</ul>
<p>When you add a filter, every chart on the dashboard updates to reflect the narrowed scope.</p>
<h2 id="log-explorer-data">Log Explorer data</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1546.md")
</aside>
<p>Log Explorer customers can create charts and dashboards using their raw, unsampled log data. This is useful when precision matters — for example, when monitoring for specific error conditions, tracking exact request counts for compliance reporting, or analyzing low-volume but high-impact events that might be missed in sampled data.</p>
<p>Standard analytics datasets use sampled data, which provides fast, accurate trends for high-volume metrics. But for use cases like:</p>
<ul>
<li><strong>Exact counts</strong> — &quot;How many requests from this specific IP hit our API today?&quot;</li>
<li><strong>Rare events</strong> — Monitoring for specific error codes or attack signatures that occur infrequently</li>
<li><strong>Compliance and auditing</strong> — When you need precise numbers, not estimates</li>
<li><strong>Low-traffic endpoints</strong> — Analyzing paths that do not generate enough volume for reliable sampling</li>
</ul>
<p>Log Explorer data gives you charts built from every logged event, not a statistical sample.</p>
<p>When creating a chart, Log Explorer customers can select from Log Explorer datasets alongside the standard GraphQL analytics datasets.</p>
<h2 id="manage-dashboards">Manage dashboards</h2>
<p>Dashboards are organized in a list view where you can see all dashboards in your account. From any dashboard, you can add, remove, or rearrange charts, and changes are saved automatically when you exit edit mode.</p>
<p>Each chart has a menu with options to edit its configuration, duplicate it, or drill down into related data in Security Analytics or Log Search.</p>
<h2 id="further-analysis">Further analysis</h2>
<p>Custom Dashboards are designed to work alongside other Cloudflare analytics tools:</p>
<ul>
<li><strong>Security Analytics</strong> — When a chart reveals suspicious traffic, drill down to investigate individual requests and see full request details</li>
<li><strong>Log Search</strong> — Move from aggregated metrics to raw logs when you need to understand exactly what happened during an incident</li>
</ul>
<p>This workflow supports the typical investigation pattern: start with high-level dashboards to identify anomalies, then drill into detailed logs to understand root cause.</p>
