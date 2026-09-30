<p>Cloudflare account analytics lets you access a wide range of aggregated metrics from all the sites under a specific Cloudflare account.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3149.md")
</aside>
<hr />
<h2 id="view-your-account-analytics">View your account analytics</h2>
<p>To view metrics for your site, in the Cloudflare dashboard, go to the <strong>Account Analytics</strong> page.</p>
<div class="nb-dash-button"></div>
<p>Once it loads, the Account Analytics app displays a collection of categorized charts with aggregated metrics for your account. To understand the various metrics available, refer to <em>Review your account metrics</em> below.</p>
<hr />
<h2 id="review-your-account-metrics">Review your account metrics</h2>
<p>This section outlines the aggregated metrics under each category. Before reviewing your metrics, let's define a couple of concepts used in some panels:</p>
<ul>
<li><em>Rate</em> -  Reflects the ratio between the amount for a specific data category and the total.</li>
<li><em>Bandwidth</em> - Refers to the number of bytes sent from the Cloudflare edge network to the requesting client.</li>
</ul>
<p>Also, note that:</p>
<ul>
<li>To filter metrics for a specific time period, use the dropdown in the top right.</li>
<li>Most metrics are grouped into panels representing different aspects of the underlying data.</li>
</ul>
<h3 id="summary-of-metrics">Summary of metrics</h3>
<p>Below is a brief description of the major elements comprising the metrics available.</p>
<h4 id="http-traffic">HTTP Traffic</h4>
<p>These charts aggregate data for HTTP traffic, and include:</p>
<p><img src="/assets/upstream/images/support/hc-dash-account-analytics-map.png" alt="Chart showing last week's data for HTTP traffic" /></p>
<ul>
<li>Spark lines for <em>Requests</em>, <em>Bandwidth</em>, <em>Page views</em>, and <em>Visitors</em> (<em>Unique IPs)</em></li>
<li>An interactive map that breaks down the number of requests by country</li>
<li>A table combining numerical and spark line data, sorted by total number of requests per country</li>
</ul>
<h4 id="security">Security</h4>
<p><img src="/assets/upstream/images/support/hc-dash-account-analytics_security_panel.png" alt="Panel displaying lines highlighting encryption metrics: requests, requests rate, bandwidth, and bandwidth rate" /></p>
<p>This panel features spark lines highlighting various encryption metrics, including: <em>requests</em>, <em>requests rate</em>, <em>bandwidth</em>, and <em>bandwidth rate</em>.  These also include a comparative percentage change based on the previous period.</p>
<h4 id="cache">Cache</h4>
<p><img src="/assets/upstream/images/support/hc-dash-account-analytics_cache_card.png" alt="Panel displaying lines for caching metrics: requests, requests rate, bandwidth, and bandwidth rate" /></p>
<p>This panel features spark lines for various caching metrics, including: <em>requests</em>, <em>requests rate</em>, <em>bandwidth</em>, and <em>bandwidth rate</em>.  These also include a comparative percentage change based on the previous equivalent period.  For example, if you selected <em>Last week</em> as your time period, the previous period refers to the <em>week</em> before.</p>
<h4 id="errors">Errors</h4>
<p><img src="/assets/upstream/images/support/hc-account-analytics_errors_card.png" alt="Panel displaying lines for 4xx and 5xx error rates" /></p>
<p>This panel displays spark lines for 4xx and 5xx error rates, respectively. Learn more about <a href="/support/troubleshooting/http-status-codes/">HTTP Status Codes</a>. </p>
<h4 id="network">Network</h4>
<p><img src="/assets/upstream/images/support/hc-dash-account-analytics_network_card.png" alt="Statistics showing the percentage of requests that use a specific version of HTTP" /></p>
<h4 id="client-http-version-used">Client HTTP Version Used</h4>
<p>These statistics show the percentage of requests that use a specific version of HTTP.</p>
<h4 id="traffic-served-over-ssl">Traffic Served Over SSL</h4>
<p>These statistics show the percentage of traffic that is encrypted using a specific version of SSL or TLS.</p>
<h4 id="content-type-breakdown">Content Type Breakdown</h4>
<p>These statistics show the number of requests based on the resource content type.</p>
