<p>Cloudflare One offers observability tools to monitor and troubleshoot your environment:</p>
<ul>
<li><a href="/cloudflare-one/insights/analytics-overview/">Analytics Overview</a> to monitor overall Cloudflare One usage.</li>
<li><a href="/cloudflare-one/insights/analytics/">Analytics Dashboards</a> to review organizational traffic trends and policy insights.</li>
<li><a href="/cloudflare-one/insights/logs/">Logs</a> for event-level investigation.</li>
<li><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> for device, network, and application performance.</li>
</ul>
<h2 id="troubleshooting-workflow-example">Troubleshooting workflow example</h2>
<p>A user reports they cannot reach an internal application behind <a href="/cloudflare-one/">Cloudflare Access</a>. To address the issue:</p>
<ol>
<li>Check the <a href="/cloudflare-one/insights/analytics-overview/">Analytics overview dashboard</a> to review if other users are experiencing similar issues.</li>
<li>Review <a href="/cloudflare-one/insights/logs/">Logs</a> to examine the user's authentication attempts and blocked requests.</li>
<li>Use <a href="/cloudflare-one/insights/dex/">DEX</a> to evaluate the user's device health and network performance.</li>
</ol>
<h2 id="how-to-use-these-tools-together">How to use these tools together</h2>
<h3 id="onboarding">Onboarding</h3>
<p>After onboarding your devices and users, use these tools to confirm everything is set up correctly and to monitor your organization's activity.</p>
<ol>
<li>Start with <a href="/cloudflare-one/insights/logs/">Logs</a> to validate initial configuration and confirm that authentication is successful.</li>
<li>Use <a href="/cloudflare-one/insights/analytics-overview/">Analytics Overview</a> to confirm expected patterns and policy activity.</li>
</ol>
<p>If your device is experiencing connectivity issues, Cloudflare recommends starting with <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/troubleshooting-guide/">troubleshooting WARP</a> as WARP misconfiguration is the most common cause of connectivity issues.</p>
<h3 id="daily-monitoring">Daily monitoring</h3>
<ol>
<li>
<p>Use <a href="/cloudflare-one/insights/analytics/">Analytics Dashboards</a> to understand trends and for visualizations of your log data.</p>
<p>Administrators typically start with Analytics Dashboards because they offer:</p>
<ul>
<li>A high-level view of activity across your products, like Access, or security use cases, such as AI and shadow IT.</li>
<li>Visibility into trends, provided through time-series graphs, to track the evolution of key metrics (such as <a href="/cloudflare-one/insights/analytics/gateway/#dns-query-analytics">DNS queries</a>, <a href="/cloudflare-one/insights/analytics/gateway/#network-session-analytics">network sessions</a>, <a href="/cloudflare-one/insights/analytics/gateway/#http-request-analytics">HTTP requests</a>, and <a href="/cloudflare-one/insights/analytics/data-analytics/">CASB posture/content findings</a>) over time.</li>
</ul>
</li>
<li>
<p>Use <a href="/cloudflare-one/insights/logs/">Logs</a> as needed for event-level verification.</p>
<p>Use Logs when you need to:</p>
<ul>
<li>Investigate a specific event; for example, a user's <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/">failed authentication attempt</a> when trying to log in to an application.</li>
<li>Validate identity or device details; for example, confirming which user made the request, how they authenticated, and whether their device met required <a href="/cloudflare-one/insights/logs/dashboard-logs/posture-logs/">posture conditions</a>.</li>
<li>Confirm policy matches; for example, verifying which <a href="/cloudflare-one/access-controls/policies/#rule-types">specific rule</a> allowed, blocked, or challenged a user's request and why it was applied.</li>
</ul>
</li>
</ol>
<h3 id="user-reported-issues">User-reported issues</h3>
<p>Users may report problems like slow or failing connections to internal apps.</p>
<ol>
<li>Start with <a href="/cloudflare-one/insights/analytics/">Analytics Dashboards</a> to review whether the issue impacts others.</li>
<li>Check <a href="/cloudflare-one/insights/logs/">Logs</a> for failed authentication attempts, blocked requests, or unexpected policy matches.</li>
<li>Use <a href="/cloudflare-one/insights/dex/">DEX</a> to diagnose device- or network-level causes with <a href="/cloudflare-one/insights/dex/tests/">synthetic tests</a> and <a href="/cloudflare-one/insights/dex/monitoring/">device monitoring</a>.</li>
</ol>
