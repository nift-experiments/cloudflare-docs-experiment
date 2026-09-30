<p>This page lists the most commonly used commands for managing local tunnels.</p>
<p>To view all CLI commands, refer to the CLI help text in your terminal. For example, to view all options for the <code>cloudflared tunnel</code> subcommand, type <code>cloudflared tunnel help</code>.</p>
<h2 id="manage-cloudflared">Manage <code>cloudflared</code></h2>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared update</code></td>
<td>Looks for a new version on the official download server. If a new version exists, it updates the agent binary and quits. Otherwise, no action is performed. This command only works if <code>cloudflared</code> was installed from GitHub binaries or from source. For more information, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/update-cloudflared/">update instructions</a>.</td>
</tr>
<tr>
<td><code>cloudflared version</code></td>
<td>Prints the <code>cloudflared</code> version number and build date.</td>
</tr>
<tr>
<td><code>cloudflared help</code></td>
<td>Shows a list of all top-level commands for <code>cloudflared</code>.</td>
</tr>
</tbody>
</table>
<h2 id="manage-tunnels">Manage tunnels</h2>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel login</code></td>
<td>Prompts a browser window where you can authenticate your tunnel to your Cloudflare account.</td>
</tr>
<tr>
<td><code>cloudflared tunnel list</code></td>
<td>Displays all active tunnels, their creation time, and associated connections. Use the <code>-d</code> flag to include deleted tunnels.</td>
</tr>
<tr>
<td><code>cloudflared tunnel create &lt;NAME or UUID&gt;</code></td>
<td>Creates a tunnel, registers it with the Cloudflare edge and generates a credential file to run this tunnel.</td>
</tr>
<tr>
<td><code>cloudflared tunnel --config path/config.yaml run &lt;NAME or UUID&gt;</code></td>
<td>Runs a tunnel, creating highly available connections between your server and the Cloudflare edge. You can provide name or UUID of the tunnel to run either as the last command line argument or in the configuration file using <code>tunnel: &lt;NAME&gt;</code>.</td>
</tr>
<tr>
<td><code>cloudflared tunnel info &lt;NAME or UUID&gt;</code></td>
<td>Displays details about the active connectors for a given tunnel identified by name of UUID.</td>
</tr>
<tr>
<td><code>cloudflared tunnel cleanup &lt;NAME or UUID&gt;</code></td>
<td>Deletes connections for tunnels with the given UUIDs or names. This is useful if you get an error trying to delete or run a tunnel after <code>cloudflared</code> is not shut down gracefully (for example, if a <code>kill</code> command is issued).</td>
</tr>
<tr>
<td><code>cloudflared tunnel cleanup --connector-id &lt;CONNECTOR-ID&gt; &lt;NAME or UUID&gt;</code></td>
<td>Disconnects and deletes a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/"><code>cloudflared</code> replica</a> with the given connector ID. You can view all replicas for a tunnel by running <code>cloudflared tunnel info &lt;NAME or UUID&gt;</code>.</td>
</tr>
<tr>
<td><code>cloudflared tunnel delete &lt;NAME or UUID&gt;</code></td>
<td>Deletes tunnels with the given name or UUID. A tunnel cannot be deleted if it has active connections. To delete the tunnel unconditionally, use the <code>-f</code> flag.</td>
</tr>
<tr>
<td><code>cloudflared tail &lt;UUID&gt;</code></td>
<td>Start a session to livestream logs from a specific tunnel. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel logs</a>.</td>
</tr>
</tbody>
</table>
<h2 id="manage-published-applications">Manage published applications</h2>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel route dns</code></td>
<td>Creates a DNS CNAME record hostname that points to the tunnel.</td>
</tr>
<tr>
<td><code>cloudflared tunnel route lb &lt;NAME or UUID&gt; &lt;hostname&gt; &lt;load balancer pool&gt;</code></td>
<td>Adds a tunnel as an endpoint in a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/public-load-balancers/">load balancer pool</a>. A new load balancer and pool will be created if necessary. <ul> <li> <code>&lt;hostname&gt;</code>: the public-facing hostname of the load balancer, for example <code>lb.example.com</code> </li> <li> <code>&lt;load balancer pool&gt;</code>: the name of the <a href="/load-balancing/pools/create-pool/#create-a-pool">pool</a> that will contain the tunnel endpoint </li> </ul> To load balance traffic to a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/configuration-file/#file-structure-for-published-applications">published application</a>, you will also need to specify the application hostname in the <a href="/load-balancing/additional-options/override-http-host-headers/">endpoint host header</a> using the dashboard or API.</td>
</tr>
</tbody>
</table>
<h2 id="manage-private-networks">Manage private networks</h2>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cloudflared tunnel route ip add &lt;IP/CIDR&gt; &lt;NAME or UUID&gt;</code></td>
<td>Adds any network route space (represented as a CIDR) to your routing table. That network space becomes reachable for requests egressing from a user's machine as long as it is using the Cloudflare One Client and is enrolled in the same account that is running the tunnel chosen here. Further, those requests will be proxied to the specified tunnel, and reach an IP in the given CIDR, as long as that IP is reachable from the tunnel. To assign the IP route to a specific <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">Virtual Network</a>, use the <code>--vnet</code> option.</td>
</tr>
<tr>
<td><code>cloudflared tunnel route ip show</code> (or <code>list</code>)</td>
<td>Shows your organization's private routing table. You can use additional flags to filter the results.</td>
</tr>
<tr>
<td><code>cloudflared tunnel route ip delete</code></td>
<td>Deletes the row for a given CIDR from your routing table. That portion of your network will no longer be reachable by the Cloudflare One Client.</td>
</tr>
<tr>
<td><code>cloudflared tunnel route ip get &lt;IP/CIDR&gt;</code></td>
<td>Checks which row of the routing table will be used to proxy a given IP. This helps check and validate your configuration.</td>
</tr>
<tr>
<td><code>cloudflared tunnel vnet add &lt;NAME or UUID&gt;</code></td>
<td>Creates a Virtual Network to which IP routes can be assigned. To make this Virtual Network the default for your Zero Trust organization, use the <code>-d</code> flag.</td>
</tr>
<tr>
<td><code>cloudflared tunnel vnet delete &lt;NAME or UUID&gt;</code></td>
<td>Deletes the Virtual Network with the given name or UUID. Before you can delete a Virtual Network, you must first delete all IP routes assigned to the Virtual Network.</td>
</tr>
<tr>
<td><code>cloudflared tunnel vnet list</code></td>
<td>Displays all active Virtual Networks, the default Virtual Network, and their creation times.</td>
</tr>
</tbody>
</table>
