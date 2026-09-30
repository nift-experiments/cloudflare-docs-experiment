<p>This tutorial explains how to analyze Cloudflare metrics using the <a href="https://newrelic.com/instant-observability/cloudflare/fc2bb0ac-6622-43c6-8c1f-6a4c26ab5434">New Relic One Cloudflare Quickstart</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before sending your Cloudflare log data to New Relic, make sure that you:</p>
<ul>
<li>Have a Cloudflare Enterprise account with Cloudflare Logs enabled.</li>
<li>Have a New Relic account.</li>
<li>Configure <a href="/logs/logpush/logpush-job/enable-destinations/new-relic/">Logpush to New Relic</a>.</li>
</ul>
<h2 id="task-1-install-the-cloudflare-network-logs-quickstart">Task 1 - Install the Cloudflare Network Logs quickstart</h2>
<ol>
<li>Log in to New Relic.</li>
<li>Click the Instant Observability button (top right).</li>
<li>Search for <strong>Cloudflare Network Logs</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/fundamentals/new-relic/screenshots/cloudflare-network-logs.png" alt="Cloudflare Network Logs install screen" /></p>
<ol start="4">
<li>Click <strong>Install this quickstart</strong>.</li>
<li>Follow the steps to deploy.</li>
</ol>
<h2 id="task-2-view-the-cloudflare-dashboards">Task 2 - View the Cloudflare Dashboards</h2>
<p>You can view your dashboards on the New Relic dashboard page. The dashboards include the following information:</p>
<h3 id="overview">Overview</h3>
<p>Get a quick overview of the most important metrics from your websites and applications on the Cloudflare network.</p>
<p><img src="/assets/upstream/images/fundamentals/new-relic/dashboard/dash-1.png" alt="Cloudflare Network Logs install screen" /></p>
<h3 id="security">Security</h3>
<p>Get insights on threats to your websites and applications, including number of threats taken action on by the Web Application Firewall (WAF), threats over time, top threat countries, and more.</p>
<p><img src="/assets/upstream/images/fundamentals/new-relic/dashboard/dash-2.png" alt="Cloudflare Network security metrics screen" /></p>
<h3 id="performance">Performance</h3>
<p>Identify and address performance issues and caching misconfigurations. Metrics include total requests, total versus cached requests, total versus origin requests.</p>
<p><img src="/assets/upstream/images/fundamentals/new-relic/dashboard/dash-3.png" alt="Cloudflare Network Logs performance metrics screen" /></p>
<h3 id="reliability">Reliability</h3>
<p>Get insights on the availability of your websites and Applications. Metrics include, edge response status over time, percentage of <code>3xx</code>/<code>4xx</code>/<code>5xx</code> errors over time, and more.</p>
<p><img src="/assets/upstream/images/fundamentals/new-relic/dashboard/dash-4.png" alt="Cloudflare Network Logs reliability metrics screen" /></p>
