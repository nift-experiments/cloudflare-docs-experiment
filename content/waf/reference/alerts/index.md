<p>Cloudflare provides two types of security alerts that inform you of any spikes in security events:</p>
<ul>
<li><strong>Security Events Alert</strong>: Alerts about spikes across all services that generate log entries in Security Events.</li>
<li><strong>Advanced Security Events Alert</strong>: Similar to Security Events Alert with support for additional filtering options.</li>
</ul>
<p>For details on alert types and their availability, refer to <a href="#alert-types">Alert types</a>.</p>
<p>To receive security alerts, you must configure a <a href="/notifications/">notification</a>. Notifications help you stay up to date with your Cloudflare account through email, PagerDuty, or webhooks, depending on your Cloudflare plan.</p>
<h2 id="set-up-a-notification-for-security-alerts">Set up a notification for security alerts</h2>
<p>For instructions on how to set up a notification for a security alert, refer to <a href="/notifications/get-started/#create-a-notification">Create a Notification</a>.</p>
<hr />
<h2 id="alert-logic">Alert logic</h2>
<p>Security alerts use a static threshold together with a <a href="https://en.wikipedia.org/wiki/Standard_score">z-score</a> calculation over the last six hours and five-minute buckets of events. An alert is triggered whenever the z-score value is above 3.5 and the spike crosses a threshold of 200 security events. You will not receive duplicate alerts within the same two-hour time frame.</p>
<h2 id="alert-types">Alert types</h2>
<details><summary>Advanced Security Events Alert</summary><strong>Who is it for?</strong><p>Enterprise customers who want to receive alerts about spikes in specific services that generate log entries in <a href="/waf/analytics/security-events/">Security Events</a>. For more information, refer to <a href="/waf/reference/alerts/">WAF alerts</a>.</p>
<strong>Other options / filters</strong><p>A mandatory <a href="/api/resources/alerting/subresources/policies/methods/create/"><code>filters</code></a> selection is needed when you create a notification policy which includes the list of services and zones that you want to be alerted on.</p>
<ul>
<li>You can search for and add domains from your list of Enterprise zones.</li>
<li>You can choose which services the alert should monitor (Managed Firewall, Rate Limiting, etc.).</li>
<li>You can filter events by a targeted action.</li>
</ul>
<strong>Included with</strong><p>Enterprise plans.</p>
<strong>What should you do if you receive one?</strong><p>Review the information in <a href="/waf/analytics/security-events/">Security Events</a> to identify any possible attack or misconfiguration.</p>
<strong>Additional information</strong><p>The mean time to detection is five minutes.</p>
<p>When setting up this alert, you can select the services that will be monitored. Each selected service is monitored separately and can be selected as a filter.</p>
<strong>Limitations</strong><p>Security Events (WAF) alerts are not sent for each individual events, but only when a spike in traffic reaches the threshold for an alert to be sent.</p>
<p>These thresholds cannot be configured. Z-score is used to determine the threshold.</p>
</details><details><summary>Security Events Alert</summary><strong>Who is it for?</strong><p>Business and Enterprise customers who want to receive alerts about spikes across all services that generate log entries in <a href="/waf/analytics/security-events/">Security Events</a>. For more information, refer to <a href="/waf/reference/alerts/">WAF alerts</a>.</p>
<strong>Other options / filters</strong><p>A mandatory <a href="/api/resources/alerting/subresources/policies/methods/create/"><code>filters</code></a> selection is needed when you create a notification policy which includes the list of zones that you want to be alerted on.</p>
<ul>
<li>You can also search for and add domains from your list of business or enterprise zones. The notification will be sent for the domains chosen.</li>
<li>You can filter events by a targeted action.</li>
</ul>
<strong>Included with</strong><p>Business and Enterprise plans.</p>
<strong>What should you do if you receive one?</strong><p>Review the information in <a href="/waf/analytics/security-events/">Security Events</a> to identify any possible attack or misconfiguration.</p>
<strong>Additional information</strong><p>The mean time to detection is five minutes.</p>
<p>When setting up this alert, you can select the services that will be monitored. Each selected service is monitored separately.</p>
<strong>Limitations</strong><p>Security Events (WAF) alerts are not sent for each individual events, but only when a spike in traffic reaches the threshold for an alert to be sent.</p>
<p>These thresholds cannot be configured. Z-score is used to determine the threshold.</p>
</details>
