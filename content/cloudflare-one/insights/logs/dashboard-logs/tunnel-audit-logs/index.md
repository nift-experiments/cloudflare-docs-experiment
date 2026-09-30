<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> creates outbound-only connections between your infrastructure and Cloudflare. Tunnel audit logs record when these connections start, stop, or register new DNS records.</p>
<p>Audit logs for Tunnel are available in the <a href="https://dash.cloudflare.com/?account=audit-log">account section of the Cloudflare dashboard</a>, which you can find by selecting your name or email in the upper right-hand corner of the dashboard. For general audit log features such as filtering and retention, refer to <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs</a>. The following actions are logged:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Registered</td>
<td>A tunnel connector (<code>cloudflared</code>) started and connected to Cloudflare's global network.</td>
</tr>
<tr>
<td>Unregistered</td>
<td>A tunnel connector disconnected from Cloudflare's global network.</td>
</tr>
<tr>
<td>CNAME add</td>
<td>A tunnel registered a new DNS record (CNAME or AAAA) to route traffic to an application behind the tunnel.</td>
</tr>
</tbody>
</table>
