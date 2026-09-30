<p>The User Insights dashboard shows how much your organization spends on AI, which identities are responsible for that spend, and which users deviate from their typical usage. It uses the traffic already flowing through your gateway, so there is no additional setup.</p>
<h2 id="attribute-usage-to-identities">Attribute usage to identities</h2>
<p>User Insights is available to all AI Gateway customers at no additional cost and works on any traffic through your gateway. Without an identity or custom metadata on your requests, all usage is grouped under a single anonymous identifier, and User Insights cannot distinguish between individual users.</p>
<p>To attribute usage to individual users, add a user identifier with <a href="/ai-gateway/observability/custom-metadata/">custom metadata</a>, or put your gateway behind <a href="/cloudflare-one/access-controls/">Cloudflare Access</a>. With Access, each authenticated request carries a verified identity you can filter spend and analytics by.</p>
<h2 id="key-metrics">Key metrics</h2>
<p>At the top of the User Insights page, you can view the following organization-wide metrics for the selected time range:</p>
<ul>
<li><strong>Active users</strong>: Identities with gateway usage.</li>
<li><strong>Total requests</strong>: Gateway requests in this range.</li>
<li><strong>Adoption rate</strong>: IdP identities with at least one request.</li>
<li><strong>Tokens per active user</strong>: Median over this time range.</li>
<li><strong>Median spend / active user</strong>: Observed spend per attributed identity.</li>
<li><strong>Top 10% request activity</strong>: Share of attributed requests made by the most active users.</li>
<li><strong>Users to review</strong>: Users whose cost is at least 2x the median spend.</li>
<li><strong>Identity coverage</strong>: Share of requests attributed to users.</li>
</ul>
<h2 id="anomaly-detection">Anomaly detection</h2>
<p>User Insights baselines each user's normal usage and flags sessions that fall outside it, which can indicate a compromised credential or a misbehaving agent.</p>
<p>Baselines are calculated per session, not per request. For each user, User Insights uses the 95th percentile (p95) session cost over the last 30 days. The baseline is rolling and updates as usage changes.</p>
<p>A session is flagged when it exceeds both of the following thresholds:</p>
<ul>
<li><strong>Relative</strong>: More than 2x the user's own p95 session cost.</li>
<li><strong>Absolute</strong>: Above the organization-level p99 session cost across all users.</li>
</ul>
<p>Both thresholds must be met. This avoids flagging small spikes from low-usage users and routine high-cost sessions from heavy users.</p>
<p>Flagged users appear in a filtered view with the sessions that triggered the flag and their cost. User Insights does not block requests.</p>
<h2 id="user-view">User view</h2>
<p>Select a user to see their usage in detail:</p>
<ul>
<li><strong>Spend</strong>: Total observed spend for the user in this range.</li>
<li><strong>Requests</strong>: Total gateway requests made by the user.</li>
<li><strong>Tokens</strong>: Total tokens consumed by the user.</li>
<li><strong>Gateway cached requests</strong>: Number of requests served from cache.</li>
<li><strong>Errored requests</strong>: Number of requests that returned an error.</li>
<li><strong>Cache hit rate</strong>: Share of requests served from cache.</li>
<li><strong>Sessions</strong>: Approximate session count from request metadata.</li>
<li><strong>Top model</strong>: The model the user sent the most requests to.</li>
<li><strong>Top provider</strong>: The provider the user sent the most requests to.</li>
<li><strong>Last seen</strong>: Most recent activity, from the daily spend trend.</li>
<li><strong>Active days</strong>: Number of days the user sent traffic in this range.</li>
<li><strong>Identity coverage</strong>: Share of the user's requests attributed to an identity.</li>
</ul>
