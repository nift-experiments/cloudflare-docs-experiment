<p>This tutorial explains how to analyze Cloudflare metrics using the <a href="https://docs.datadoghq.com/integrations/cloudflare/">Cloudflare Integration tile for Datadog</a>.</p>
<h2 id="overview">Overview</h2>
<p>Before viewing the Cloudflare dashboard in Datadog, note that this integration:</p>
<ul>
<li>Is available to all Cloudflare customer plans (Free, Pro, Business and Enterprise)</li>
<li>Is based on the Cloudflare Analytics API</li>
<li>Provides Cloudflare web traffic and DNS metrics only</li>
<li>Does not feature data coming from request logs stored in Cloudflare Logs</li>
</ul>
<h2 id="task-1-install-the-cloudflare-app">Task 1 - Install the Cloudflare App</h2>
<p>To install the Cloudflare App for Datadog:</p>
<ol>
<li>
<p>Log in to <strong>Datadog</strong>.</p>
</li>
<li>
<p>Click the <strong>Integrations</strong> tab.</p>
</li>
<li>
<p>In the <strong>search box</strong>, start typing <em>Cloudflare</em>. The app tile should appear below the search box.
<img src="/assets/upstream/images/fundamentals/datadog/screenshots/datadog-integrations.png" alt="Searching for Cloudflare App in the Datadog Integrations tab" /></p>
</li>
<li>
<p>Click the <strong>Cloudflare</strong> tile to begin the installation.</p>
</li>
<li>
<p>Next, click <strong>Configuration</strong> and then complete the following:</p>
<ul>
<li>
<p><strong>Account name</strong>: (Optional) This can be any value. It has not impact on the site data pulled from Cloudflare.</p>
</li>
<li>
<p><strong>Email</strong>: This value helps keep your account safe. We recommend creating a dedicated Cloudflare user for analytics with the <a href="/fundamentals/manage-members/roles/"><em>Analytics</em> role</a> (read-only). Note that the <em>Analytics</em> role is available to Enterprise customers only.</p>
</li>
<li>
<p><strong>API Key</strong>: Enter your Cloudflare Global API key. For details refer to <a href="/fundamentals/api/get-started/keys/">API Keys</a>.</p>
</li>
</ul>
</li>
<li>
<p>Click <strong>Install Integration</strong>.
<img src="/assets/upstream/images/fundamentals/datadog/screenshots/cloudflare-tile-datadog-fill-details.png" alt="Configuring and installing the Datadog integration" /></p>
</li>
</ol>
<p>The Cloudflare App for Datadog should be installed now and you can view the dashboard.</p>
<h2 id="task-2-view-the-dashboard">Task 2 - View the dashboard</h2>
<p>By default, the dashboard displays metrics for all sites in your Cloudflare account. Use the dashboard filters see metrics for a specific domain.</p>
<p>The dashboard displays the following metrics:</p>
<ul>
<li><strong>Threats</strong> (threats by type, threats by country)</li>
<li><strong>Requests</strong> (total requests, cached requests, uncached requests, top countries by request, requests by IP class, top content types)</li>
<li><strong>Bandwidth</strong> (total bandwidth, encrypted and unencrypted traffic cached bandwidth, uncached bandwidth)</li>
<li><strong>Caching</strong> (Cache hit rate, request caching rate over time)</li>
<li><strong>HTTP response status errors</strong></li>
<li><strong>Page views</strong></li>
<li><strong>Search Engine Bot Traffic</strong></li>
<li><strong>DNS</strong> (DNS queries, response time, top hostnames, queries by type, stale vs. uncached queries)</li>
</ul>
<p><img src="/assets/upstream/images/fundamentals/datadog/dashboards/cloudflare-dashboard-datadog.png" alt="Dashboard displaying metrics for a site on a Cloudflare account" /></p>
