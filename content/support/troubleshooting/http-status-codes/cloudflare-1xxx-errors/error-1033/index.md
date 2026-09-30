<h2 id="error-1033-cloudflare-tunnel-error">Error 1033: Cloudflare Tunnel error</h2>
<p>This error indicates an issue with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>.</p>
<h3 id="common-cause">Common cause</h3>
<p>You have requested a page on a website (<code>tunnel.example.com</code>) that is on the Cloudflare network. The host (<code>tunnel.example.com</code>) is configured with Cloudflare Tunnel, and Cloudflare is currently unable to resolve it.</p>
<h3 id="resolution">Resolution</h3>
<p>A <code>1033</code> error indicates your tunnel is not connected to Cloudflare's network because Cloudflare's network cannot find a healthy <code>cloudflared</code> instance to receive the traffic.</p>
<p>First, review whether your tunnel is listed as <code>Active</code> in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> by going to <strong>Networking</strong> &gt; <strong>Tunnels</strong> or run <code>cloudflared tunnel list</code>. If the tunnel is not <code>Active</code>, review the following and take the action necessary for your tunnel status:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Meaning</th>
<th>Recommended Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Healthy</strong></td>
<td>The tunnel is active and serving traffic through four connections to the Cloudflare global network.</td>
<td>No action is required. Your tunnel is running correctly.</td>
</tr>
<tr>
<td><strong>Inactive</strong></td>
<td>The tunnel has been created (via the API or dashboard) but the <code>cloudflared</code> connector has never been run to establish a connection.</td>
<td>Install and run <code>cloudflared</code> on your origin server to connect the tunnel to Cloudflare. You can find the installation command in the Cloudflare dashboard under <strong>Networking</strong> &gt; <strong>Tunnels</strong> — select your tunnel, then on the <strong>Overview</strong> tab select <strong>Add a replica</strong>. For API-based setup, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/#4-install-and-run-the-tunnel">Install and run the tunnel</a>.</td>
</tr>
<tr>
<td><strong>Down</strong></td>
<td>The tunnel was previously connected but is currently disconnected because the <code>cloudflared</code> process has stopped.</td>
<td>1. Ensure the <code>cloudflared</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/">service</a> or process is actively running on your server. <br /> 2. Check for server-side issues, such as the machine being powered off, an application crash, or recent network changes.</td>
</tr>
<tr>
<td><strong>Degraded</strong></td>
<td>The <code>cloudflared</code> connector is running and the tunnel is serving traffic, but at least one individual connection has failed. Further degradation in <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">tunnel availability</a> could risk the tunnel going down and failing to serve traffic.</td>
<td>1. Review your <code>cloudflared</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">logs</a> for connection failures or error messages. <br /> 2. Investigate local network and firewall rules to ensure they are not blocking connections to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/">Cloudflare Tunnel IPs and ports</a>. <br /></td>
</tr>
</tbody>
</table>
