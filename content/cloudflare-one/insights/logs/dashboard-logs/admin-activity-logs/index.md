<p>Admin activity logs record configuration changes made by members of your Cloudflare account. These logs are useful for auditing who changed a policy or setting and investigating unexpected configuration changes. Use these logs to monitor when a member creates, updates, or deletes configurations in your <a href="/cloudflare-one/setup/#create-a-zero-trust-organization">Zero Trust organization</a>.</p>
<p>To view admin activity logs, log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Admin activity logs</strong>.</p>
<h2 id="explanation-of-the-fields">Explanation of the fields</h2>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
<th>Example Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Email</td>
<td>User who performed the action</td>
<td><a href="mailto:josephli@cloudflare.com">josephli@cloudflare.com</a></td>
</tr>
<tr>
<td>Product</td>
<td>Cloudflare product being modified</td>
<td>Tunnel</td>
</tr>
<tr>
<td>Resource</td>
<td>Specific resource type within the product</td>
<td>Route</td>
</tr>
<tr>
<td>Event</td>
<td>Action performed (Create, Update, Delete)</td>
<td>Create</td>
</tr>
<tr>
<td>Date</td>
<td>Timestamp of when the action occurred</td>
<td>April 30, 2026 • 12:19 AM</td>
</tr>
<tr>
<td>User IP Address</td>
<td>IP address of the user who made the change</td>
<td>2a09:bac6:6447:523::83:30</td>
</tr>
<tr>
<td>Interface</td>
<td>How the change was initiated</td>
<td>API</td>
</tr>
<tr>
<td>Audit record</td>
<td>Unique identifier for the audit log entry</td>
<td>caf1a547-17cc-484a-b4ce-5d3b32771a8f</td>
</tr>
<tr>
<td>Old value</td>
<td>Previous configuration state (empty for creates)</td>
<td>{}</td>
</tr>
<tr>
<td>New value</td>
<td>New configuration state after the change</td>
<td>JSON object with fields like comment, network, tun_type, tunnel_id, virtual_network_id</td>
</tr>
</tbody>
</table>
<h2 id="export-admin-activity-logs">Export admin activity logs</h2>
<p>Enterprise users can export admin activity logs to a third-party storage destination or SIEM using <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a>. For a list of all available fields, refer to <a href="/logs/logpush/logpush-job/datasets/account/audit_logs_v2/">Audit Logs V2</a>.</p>
