<p>You can configure alerts to receive notifications for changes in your network.</p>
<details><summary>Network Flow - Auto Advertisement</summary><strong>Who is it for?</strong><p><a href="/magic-transit/on-demand/">Magic Transit on-demand</a> customers who use Flow-Based Monitoring and want alerts when Magic Transit is automatically enabled.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Magic Transit.</p>
<strong>What should you do if you receive one?</strong><p>No action is needed. You can go to the <a href="https://dash.cloudflare.com/?to=/:account/magic-transit">Cloudflare dashboard</a> to review the health and status of your tunnels.</p>
</details><details><summary>Network Flow - DDoS Attack</summary><strong>Who is it for?</strong><p><a href="/byoip/">BYOIP</a> and <a href="/spectrum/">Spectrum</a> customers with <a href="/analytics/network-analytics/">Network Analytics</a> who want to receive a notification when Cloudflare has mitigated attacks that generate an average of at least 12,000 packets per second over a five-second period, with a duration of one minute or more.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Magic Transit and/or BYOIP.</p>
<strong>What should you do if you receive one?</strong><p>No action needed. Refer to <a href="/ddos-protection/reference/alerts/">DDoS alerts</a> for more information.</p>
</details><details><summary>Network Flow - Volumetric Attack</summary><strong>Who is it for?</strong><p><a href="/magic-transit/on-demand/">Magic Transit on-demand</a> customers who are using Flow-Based Monitoring to detect attacks when Magic Transit is disabled.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Magic Transit.</p>
<strong>What should you do if you receive one?</strong><p>If you do not have auto advertisement enabled, you need to advertise your IP prefixes to enable Magic Transit. For more information, refer to <a href="/byoip/concepts/dynamic-advertisement/">Dynamic advertisement</a>.</p>
</details><details><summary>Magic Tunnel Health Check Alert</summary><strong>Who is it for?</strong><p>Magic Transit and Cloudflare WAN customers who wish to receive alerts when the percentage of tunnel states meeting the selected service-level objective (SLO) drops below the defined threshold for a Magic Tunnel.</p>
<strong>Other options / filters</strong><ul>
<li>Notification Name: A custom name for the notification.</li>
<li>Description (optional): A custom description for the notification.</li>
<li>Notification Email (can be multiple emails): The email address of recipient for the notification.</li>
<li>Webhooks</li>
<li>Tunnels: Choose one or more tunnels to monitor.</li>
<li>SLO: Define SLO threshold for Magic Tunnel health alerts. Available options are <em>High</em>, <em>Medium</em>, and <em>Low</em>.</li>
</ul>
<strong>Included with</strong><p>Purchase of Magic Transit and Cloudflare WAN.</p>
<strong>What should you do if you receive one?</strong><p>Refer to the <a href="/magic-transit/network-health/check-tunnel-health-dashboard/">Magic Transit tunnel health</a> or <a href="/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/">Cloudflare WAN IPsec/GRE tunnel health</a> for more information on what the issue might be.</p>
</details>
<p>Refer to <a href="/notifications/get-started/">Cloudflare Notifications</a> for more information on how to set up an alert.</p>
