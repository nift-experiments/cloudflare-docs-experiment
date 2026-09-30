<p>Administrators can receive an alert when Cloudflare Tunnels in an account change their health or deployment status. Notifications can be delivered via email, webhook, and third-party services.</p>
<h2 id="manage-notifications">Manage notifications</h2>
<p>Tunnel notifications are configured on the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>. For more information, refer to <a href="/notifications/get-started/#create-a-notification">Create a notification</a>.</p>
<h2 id="available-notifications">Available notifications</h2>
<details><summary>Tunnel Creation or Deletion Event</summary><strong>Who is it for?</strong><p>Customers who want to receive a notification when Cloudflare Tunnels are created or deleted in their account.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>All Cloudflare Zero Trust plans.</p>
<strong>What should you do if you receive one?</strong><p>No action is needed.</p>
</details><details><summary>Tunnel Health Alert</summary><strong>Who is it for?</strong><p>Customers who want to be warned about changes in health status for their Cloudflare Tunnels.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>All Cloudflare Zero Trust plans.</p>
<strong>What should you do if you receive one?</strong><p>Monitor tunnel health over time and consider deploying <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/"><code>cloudflared</code> replicas or load balancers</a>.</p>
<strong>Additional information</strong><p>Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status">Tunnel status</a> to review the list of possible tunnel statuses (<code>Healthy</code>, <code>Inactive</code>, <code>Down</code> and <code>Degraded</code>).</p>
</details>
