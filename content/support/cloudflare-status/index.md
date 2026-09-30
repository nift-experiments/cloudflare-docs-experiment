<p>Cloudflare provides updates on the status of our services and network on the <a href="https://www.cloudflarestatus.com/">Cloudflare Status page</a>, which you should check if you notice unexpected behavior with Cloudflare.</p>
<p>Beyond looking at the page itself, there are programmatic ways to consume this information.</p>
<h2 id="configure-notifications">Configure notifications</h2>
<p>There are two ways to be notified about Cloudflare incidents and maintenance.</p>
<h3 id="status-page-notifications">Status page notifications</h3>
<p>The status page has its own notification system, delivered independently of Cloudflare infrastructure, so these notifications fire even if Cloudflare itself is down. You can subscribe by email, webhook, Slack, Discord, or Google Chat.</p>
<p>For more information, refer to <a href="https://www.cloudflarestatus.com/docs/notifications">status page notifications</a>.</p>
<h3 id="cloudflare-notifications">Cloudflare Notifications</h3>
<p>Cloudflare offers a dedicated notification called <strong>Incident Alerts</strong>, which lets you know when Cloudflare is experiencing an incident. Because it runs on your account, it delivers to the destinations you have already configured and can be filtered to the impact levels and components you care about.</p>
<p>You can configure this notification to send via <a href="/notifications/get-started/">email</a>, <a href="/notifications/get-started/configure-webhooks/">Webhooks</a>, or <a href="/notifications/get-started/configure-pagerduty/">PagerDuty</a>.</p>
<p>A separate <strong>Maintenance Notification</strong> covers planned maintenance. For more information, refer to <a href="/support/disruptive-maintenance/">Disruptive Maintenance</a>.</p>
<h2 id="check-location-status">Check location status</h2>
<p>The <a href="https://www.cloudflarestatus.com/locations">locations view</a> lists the status of each Cloudflare data center as <strong>Operational</strong>, <strong>Re-routed</strong>, or <strong>Partially Re-routed</strong>. A location that has been removed from the network for planned or unplanned maintenance is listed as <strong>Re-routed</strong>.</p>
<h2 id="use-the-api">Use the API</h2>
<p>Cloudflare also provides status information through the <a href="https://www.cloudflarestatus.com/api">Cloudflare Status API</a>.</p>
<p>Incidents and maintenance are published as separate feeds, each available in RSS and Atom:</p>
<table>
<thead>
<tr>
<th>Feed</th>
<th>RSS</th>
<th>Atom</th>
</tr>
</thead>
<tbody>
<tr>
<td>Incidents</td>
<td><code>https://www.cloudflarestatus.com/api/v3/incidents.rss</code></td>
<td><code>https://www.cloudflarestatus.com/api/v3/incidents.atom</code></td>
</tr>
<tr>
<td>Maintenance</td>
<td><code>https://www.cloudflarestatus.com/api/v3/maintenance.rss</code></td>
<td><code>https://www.cloudflarestatus.com/api/v3/maintenance.atom</code></td>
</tr>
</tbody>
</table>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/fundamentals/new-features/available-rss-feeds/">Available RSS feeds</a> (for the <a href="/changelog/">Cloudflare changelog</a>)</li>
<li><a href="/fundamentals/api/reference/deprecations/">API deprecations</a></li>
<li><a href="/support/disruptive-maintenance/">Planned maintenance windows</a></li>
</ul>
