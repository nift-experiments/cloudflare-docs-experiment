<h2 id="scheduled-maintenance-windows">Scheduled maintenance windows</h2>
<p>Planned maintenance is published on the <a href="https://www.cloudflarestatus.com/">Cloudflare Status page</a>.</p>
<p>During these maintenance windows, customers may experience a slight increase in latency to the edge location which is under maintenance.</p>
<h3 id="notifications">Notifications</h3>
<p>There are two ways to be notified about scheduled maintenance.</p>
<p>Status page notifications are delivered independently of Cloudflare infrastructure and fire even if Cloudflare itself is down. You can subscribe by email, webhook, Slack, Discord, or Google Chat. For more information, refer to <a href="https://www.cloudflarestatus.com/docs/notifications">status page notifications</a>.</p>
<p>You can also receive maintenance updates through <a href="/notifications/">Cloudflare Notifications</a>, which delivers to the destinations configured on your account.</p>
<details><summary>Maintenance Notification</summary><strong>Who is it for?</strong><p>Customers interested in knowing about planned <a href="/support/troubleshooting/disruptive-maintenance/">Cloudflare maintenance</a> for specific data centers. The notification lets you know when maintenance has been scheduled, changed, or canceled on an entire point of presence.</p>
<strong>Other options / filters</strong><p>You can filter maintenance notifications for specific points of presence and updates (scheduled, changed, canceled).</p>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>If the notification is announcing new scheduled maintenance, you may want to add the maintenance to your calendar. During these maintenance windows, you may experience a slight increase in latency to the edge location which is under maintenance.</p>
</details>
<p>Refer to <a href="/notifications/get-started/">Cloudflare Notifications</a> for more information on how to set up an alert.</p>
<h2 id="unplanned-maintenance">Unplanned maintenance</h2>
<p>Cloudflare operates a redundant <a href="https://www.cloudflare.com/en-gb/learning/cdn/glossary/anycast-network/">anycast network</a> that is capable of automatically removing locations from our network if they require unplanned maintenance or experience an emergency event. In such cases, traffic will be rerouted automatically to alternative locations.</p>
<p>To check for unplanned maintenance, confirm whether a location was re-routed by checking if its status is listed as <strong>Re-routed</strong> in the <a href="https://www.cloudflarestatus.com/locations">status page locations view</a>. Exceptionally, an incident may be declared for maintenance at a location, in which case updates are available on the <a href="https://www.cloudflarestatus.com/">Cloudflare Status page</a>.</p>
<h2 id="interconnections-at-locations-under-maintenance">Interconnections at locations under maintenance</h2>
<p>If you have a <a href="/network-interconnect/">CNI connection</a> with Cloudflare at a re-routed location, it may become temporarily unavailable during planned or unplanned maintenance, and regular Internet routing may be used instead to reach your network.</p>
<p>In the Magic family of products, the routing is defined explicitly using <a href="/cloudflare-wan/configuration/how-to/configure-routes/#create-a-static-route">static routes</a> to send traffic to the specified tunnels, with customer-configured priorities. If you have a CNI tunnel, we strongly recommend that you also add routes to an alternative tunnel, such as a fallback Internet tunnel, to make sure your traffic can be routed at all times.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/fundamentals/new-features/available-rss-feeds/">Available RSS feeds</a> (for the <a href="/changelog/">Cloudflare changelog</a>)</li>
<li><a href="/support/cloudflare-status/">Subscribe to Cloudflare Status</a></li>
<li><a href="/fundamentals/api/reference/deprecations/">API deprecations</a></li>
</ul>
