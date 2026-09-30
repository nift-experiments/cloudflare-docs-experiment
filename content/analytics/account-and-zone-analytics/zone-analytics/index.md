<p>The Cloudflare zone analytics is a major component of the overall Cloudflare Analytics product line.  Specifically, this app gives you access to a wide range of metrics, collected at the website or domain level.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3144.md")
</aside>
<hr />
<h2 id="view-your-website-analytics">View your website analytics</h2>
<p>To view metrics for your website, in the Cloudflare dashboard, go to the <strong>Analytics &amp; Logs</strong> page.</p>
<div class="nb-dash-button"></div>
<p>Once it loads, you can find tabs for <strong>Traffic</strong>, <strong>Security</strong>, <strong>Performance</strong>, <strong>Workers</strong>, and <strong>Logs</strong> (Enterprise domains only). To understand the various metrics available, refer to <em>Review your website metrics</em> below.</p>
<hr />
<h2 id="review-your-website-metrics">Review your website metrics</h2>
<p>This section outlines the metrics available under each Analytics app tab. Before proceeding, note that each tab may contain:</p>
<ul>
<li>One or more panels to further categorize the underlying metrics.</li>
<li>A dropdown (on the panel's top right) to filter metrics for a specific time period. The time period you can select may vary based on the Cloudflare plan that your domain is associated with.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3143.md")
</aside>
<p>Below is a summary of each Analytics app tab.</p>
<h3 id="http-traffic">HTTP Traffic</h3>
<h4 id="free-plan">Free plan</h4>
<p>These metrics include legitimate user requests as well as crawlers and threats. The HTTP Traffic tab features the following panels: </p>
<ul>
<li><strong>Web Traffic</strong> - Displays metrics for <em>Requests</em>, <em>Bandwidth</em>, and <em>Unique Visitors</em>. If you are using Cloudflare Workers, subrequests data will not be visible in zone Traffic Analytics. Instead, you can find subrequests analytics under the <strong>Workers &amp; Pages</strong> tab in the <strong>Overview</strong> section. Refer to <a href="/analytics/account-and-zone-analytics/analytics-with-workers/#worker-analytics">Worker Analytics</a> for more information.</li>
<li><strong>Web Traffic Requests by Country</strong> - Is an interactive map that breaks down the number of requests by country.  This panel also includes a data table for <strong>Top Traffic Countries / Regions</strong> that display the countries with the most number of requests (up to five, if the data exists).</li>
</ul>
<h4 id="pro-business-or-enterprise-plan">Pro, Business, or Enterprise plan</h4>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3142.md")
</aside>
<p>Analytics are based on Cloudflare's edge logs, with no need for third party scripts or trackers. The HTTP Traffic tab features the following metrics:</p>
<ul>
<li><strong>Requests</strong> - An HTTP request. A typical page view requires many requests. If you are using Cloudflare Workers, subrequests data will not be visible in zone HTTP Traffic Analytics. Instead, you can find subrequests analytics under the <strong>Workers &amp; Pages</strong> tab in the <strong>Overview</strong> section. Refer to <a href="/analytics/account-and-zone-analytics/analytics-with-workers/#worker-analytics">Worker Analytics</a> for more information.</li>
<li><strong>Data Transfer</strong> - Total HTTP data transferred in responses.</li>
<li><a id="page-views" /> <strong>Page views</strong> - A page view is defined as a successful
HTTP response with a content-type of HTML.</li>
<li><strong>Visits</strong> - A visit is defined as a <a href="#page-views">page view</a> that originated from a different website, or direct link. Cloudflare checks where the HTTP referer does not match the hostname. One visit can consist of multiple page views.</li>
<li><strong>API Requests</strong> - An HTTP request for API data.</li>
</ul>
<p>To receive more detailed metrics, <strong>Add filter</strong>. You can also filter each metric by:</p>
<ul>
<li>Cache status</li>
<li>Data center</li>
<li>Source ASN</li>
<li>Country</li>
<li>Source device type</li>
<li>Source IP</li>
<li>Referer host</li>
<li>Host</li>
<li>HTTP method</li>
<li>HTTP version</li>
<li>Path</li>
<li>Query string</li>
<li>Content type</li>
<li>Edge status code</li>
<li>Origin status code</li>
<li>Security Action</li>
<li>Security Source</li>
<li>Source browser</li>
<li>Source operating system</li>
<li>Source user agent</li>
<li>X-Requested-With header</li>
</ul>
<p>In addition, the following filters are available to Enterprise <a href="/bots/get-started/bot-management/">Bot Management</a> customers only.</p>
<ul>
<li>Source JA4 fingerprint</li>
<li>Source JA3 fingerprint</li>
</ul>
<p>To change the time period, use the dropdown menu on the right-hand side above the graph. You can also drag to zoom on the graph.</p>
<h3 id="security">Security</h3>
<p>For this tab, the number and type of charts may vary based on existing data and customer plan. Most of the metrics in this tab come from the Cloudflare Firewall app. The panels available include:</p>
<ul>
<li><strong>Threats</strong> - Displays a data summary and an area chart showing threats against the site.</li>
<li><strong>Threats by Country</strong> - Is an interactive map highlighting the countries where threats originated. It also includes data tables with statistics on <strong>Top Threat Countries / Regions</strong> and <strong>Top Crawlers / Bots.</strong></li>
<li><strong>Rate Limiting</strong> (add-on service) - Features a line chart highlighting matching and blocked requests, based on rate limits.  To learn more, consult <a href="/waf/reference/legacy/old-rate-limiting/#analytics">Rate Limiting Analytics</a>.</li>
<li><strong>Overview</strong> - Displays a set of pie charts for: <strong>Total Threats Stopped</strong>, <strong>Traffic Served Over SSL</strong>, and <strong>Types of Threats Mitigated</strong>. If available, the expandable <strong>Details</strong> link display a table with numerical data.</li>
</ul>
<h3 id="performance">Performance</h3>
<p>The metrics aggregated under this tab span multiple Cloudflare services.  The panels available include:</p>
<ul>
<li><strong>Origin Performance (Argo)</strong> (add-on service) - Displays metrics related to response time between the Cloudflare edge network and origin servers for the last 48 hours.  For additional details, refer to <a href="/argo-smart-routing/analytics/">Argo Analytics</a>.</li>
<li><strong>Overview</strong> - Displays a set of pie charts for: <strong>Client HTTP Version Used</strong>, <strong>Bandwidth Saved</strong>, and <strong>Content Type Breakdown</strong>. If available, the expandable <strong>Details</strong> link display a table with numerical data.</li>
</ul>
<h3 id="workers">Workers</h3>
<p>This panel features metrics for Cloudflare Workers. To learn more, read <a href="/analytics/account-and-zone-analytics/analytics-with-workers/">Cloudflare analytics with Workers</a>.</p>
<h3 id="logs">Logs</h3>
<p>The Logs tab is not a metrics feature. Instead, Customers in the Enterprise plan can enable the <a href="/logs/logpush/">Cloudflare Logs Logpush</a> service. You can use Logpush to download and analyze data using any analytics tool of your choice. </p>
