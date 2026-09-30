<p>Virtual networks provide routing isolation within your Cloudflare account. Each virtual network maintains its own routing table, allowing you to separate traffic between different environments, partners, or applications.</p>
<p>For example, an organization may have separate &quot;production&quot; and &quot;staging&quot; VPC networks that both use the same private IP range (such as <code>10.128.0.0/24</code>). Without virtual networks, Cloudflare cannot distinguish between <code>10.128.0.1</code> in production and <code>10.128.0.1</code> in staging. By creating two virtual networks, you can deterministically route traffic to the correct environment. Users select which virtual network they want to connect to in the Cloudflare One Client.</p>
<p>For a conceptual overview of virtual networks, including how they work across Cloudflare products, refer to <a href="/cloudflare-one/networks/virtual-networks/">Virtual networks</a>.</p>
<h2 id="example">Example</h2>
<p>This example illustrates best practices for managing overlapping subnets. For this example, assume that you are connecting two different private networks: a production VPC that uses the <code>10.0.0.0/8</code> space holistically and a staging VPC that uses the <code>10.0.1.0/24</code> space. These networks are served by Tunnel-A and Tunnel-B respectively.</p>
<p>The following table shows the default configuration without a virtual network assigned:</p>
<table>
<thead>
<tr>
<th>Routes in Tunnel-A</th>
<th>Virtual network</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>10.0.0.0/8</code></td>
<td>default</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Routes in Tunnel-B</th>
<th>Virtual network</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>10.0.1.0/24</code></td>
<td>default</td>
</tr>
</tbody>
</table>
<p>In the above configuration, all user traffic to <code>10.0.1.0/24</code> takes the most specific path and routes to the staging VPC (Tunnel-B). All other <code>10.0.0.0/8</code> traffic routes to the production VPC (Tunnel-A). Users would not be able to reach the <code>10.0.1.0/24</code> subnet for the network served by Tunnel-A.</p>
<p>To solve this problem, add a <code>10.0.1.0/24</code> route to Tunnel-A and assign it the <code>production</code> virtual network. Next, assign the <code>staging</code> virtual network to <code>10.0.1.0/24</code> in Tunnel-B.</p>
<table>
<thead>
<tr>
<th>Routes in Tunnel-A</th>
<th>Virtual network</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>10.0.0.0/8</code></td>
<td>default</td>
</tr>
<tr>
<td><code>10.0.1.0/24</code></td>
<td>production</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Routes in Tunnel-B</th>
<th>Virtual network</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>10.0.1.0/24</code></td>
<td>staging</td>
</tr>
</tbody>
</table>
<p>The user can now <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/#connect-to-a-virtual-network">toggle between the two virtual networks</a> in their Cloudflare One Client, similar to the concept of switching VPN profiles in a VPN client. When a user selects <code>production</code>, they can connect to the entire <code>10.0.0.0/8</code> range served by Tunnel-A. When they select <code>staging</code>, they can connect to all of <code>10.0.0.0/8</code> in Tunnel-A except for <code>10.0.1.0/24</code>, which will be served by Tunnel-B.</p>
<h2 id="set-up-virtual-networks">Set up virtual networks</h2>
<p>For setup instructions, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/#create-a-virtual-network">Create a virtual network</a>.</p>
