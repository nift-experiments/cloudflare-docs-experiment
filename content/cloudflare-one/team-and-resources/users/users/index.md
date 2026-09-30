<p>User logs show a list of all users who have authenticated to Cloudflare One. For each user who has logged in, you can view their enrolled devices, login history, seat usage, and identity used for policy enforcement.</p>
<h2 id="view-user-logs">View user logs</h2>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Users</strong>.</p>
<p>This page lists all users who have registered the Cloudflare One Client or authenticated to a Cloudflare Access application. You can select a user's name to view detailed logs, <a href="/cloudflare-one/access-controls/access-settings/session-management/#revoke-user-sessions">revoke their session</a>, or <a href="/cloudflare-one/team-and-resources/users/seat-management/">remove their seat</a>.</p>
<h3 id="available-logs">Available logs</h3>
<ul>
<li><strong>User Registry identity</strong>: Select the user's name to view their last seen identity. This identity is used to evaluate Gateway policies and Cloudflare One Client <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profiles</a>. A refresh occurs when the user re-authenticates the device client, logs into an Access application, or has their IdP group membership updated via <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/5952.md")
</div>. To track how the user's identity has changed over time, go to the **Audit logs** tab.
* **Session identities**: The user's active sessions, the identity used to authenticate each session, and when each session will [expire](/cloudflare-one/access-controls/access-settings/session-management/).
* **Devices**: Devices registered to the user via the Cloudflare One Client.
* **Recent activities**: The user's five most recent Access login attempts. For more details, refer to your [authentication audit logs](/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/#authentication-logs).
