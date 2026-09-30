<p>The Application Access Report provides a high-level summary of <a href="/cloudflare-one/access-controls/policies/">Access</a> usage across your organization. This dashboard helps administrators monitor authentication patterns, identity provider usage, and Access configuration metrics. If Access is not configured in your account, the dashboard appears empty.</p>
<p>The Application Access Report is powered by <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/">Access authentication logs</a>.</p>
<p>To view the Application Access Report dashboard:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong>.</li>
<li>Go to <strong>Dashboards</strong>.</li>
<li>Select <strong>Application Access Report</strong>.</li>
</ol>
<p>The <a href="/cloudflare-one/insights/analytics/application-access/">Application Access Report</a> dashboard offers a summary of overall Access activity, while <a href="/cloudflare-one/insights/analytics/access/">Access event analytics</a> dashboard provides a view of login events. You can export the Application Access Report to a PDF to share with stakeholders.</p>
<p>Refer to <a href="/cloudflare-one/insights/">Insights overview</a> to learn how to use Analytics dashboards together with <a href="/cloudflare-one/insights/analytics-overview/">Analytics Overview</a> and <a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> for complete visibility and troubleshooting.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To populate the Application Access Report dashboard, you must have:</p>
<ul>
<li>At least one <a href="/cloudflare-one/access-controls/applications/">Access application</a> configured in your account.</li>
<li>Users authenticating to these applications through Cloudflare Access.</li>
</ul>
<h2 id="available-insights">Available insights</h2>
<p>The Application Access Report dashboard includes the following panels and metrics:</p>
<ul>
<li><a href="#summary-of-access-activity">Summary of Access activity</a></li>
<li><a href="#access-events">Access events</a></li>
<li><a href="#access-decisions-by-event-count">Access decisions by event count</a></li>
<li><a href="#access-applications-by-event-count">Access applications by event count</a></li>
<li><a href="#access-events-by-type">Access events by type</a></li>
<li><a href="#top-counts-of-event-details">Top counts of event details</a></li>
<li><a href="#access-admin-metrics">Access admin metrics</a></li>
</ul>
<h3 id="summary-of-access-activity">Summary of Access activity</h3>
<p>The Summary of Access activity section shows a time series of Access login events over a selected period and a summary of login events. You can filter a time period in the upper right corner of the dashboard.</p>
<h3 id="access-events">Access events</h3>
<p>Shows a time series of Access login events over a selected period. Each bar represents the number of login events in the x-axis time interval.
You can use this graph to review user authentication activity and detect unusual login spikes.</p>
<h3 id="access-decisions-by-event-count">Access decisions by event count</h3>
<p>Displays the total number of Access decisions made, grouped by outcome (for example, <strong>Granted</strong> or <strong>Denied</strong>).</p>
<h3 id="access-applications-by-event-count">Access applications by event count</h3>
<p>Shows a breakdown of authentication events by application type (for example, <strong>Self-hosted</strong>, <strong>SaaS</strong>, <strong>Private network</strong>, <strong>Infrastructure</strong> or <strong>MCP Portal</strong>).<br />
Use this view to determine which application types users most frequently access.</p>
<h3 id="access-events-by-type">Access events by type</h3>
<p>Categorizes authentication events by method, such as <strong>SSO</strong> or <strong>Login</strong> (direct credential-based authentication).<br />
This panel helps administrators understand how users are authenticating across applications and identity providers.</p>
<h3 id="top-counts-of-event-details">Top counts of event details</h3>
<p>Lists the most common Access event attributes, including:</p>
<ul>
<li>Application name — Displays the top accessed applications.</li>
<li>Identity provider — Shows which identity providers (IdPs) were most used.</li>
<li>Users — Lists top users by number of login events.</li>
<li>Countries — Displays top countries where users logged in.</li>
<li>IP addresses — Lists the top source IPs associated with login events.</li>
</ul>
<p>These insights help administrators identify usage patterns and trends.</p>
<h3 id="access-admin-metrics">Access admin metrics</h3>
<p>Provides a summary of Access configurations made by admin in your organization, including:</p>
<ul>
<li>Applications configured — Total number of Access-protected applications, broken down by type (for example, Self-hosted, SaaS, RDP, SSH, Private network, and <a href="/fundamentals/manage-members/dashboard-sso/">Cloudflare Dashboard SSO</a>).</li>
<li>Policies configured — Total number of Access policies, grouped by <a href="/cloudflare-one/access-controls/policies/#actions">policy action</a> (for example, Allow, Block, Bypass, or Service Auth).</li>
</ul>
<p>This section helps administrators audit their Access setup and verify that expected resources and policies are in place.</p>
