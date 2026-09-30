<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4279.md")
</aside>
<p>This tutorial gives administrators an easy way to allow their users to change their egress IP address between any of your assigned dedicated egress IP addresses. Your users can choose which egress IP to use by switching virtual networks directly from in the Cloudflare One Client.</p>
<p>Changing egress IPs can be useful in quality assurance (QA) and other similar scenarios in which users both use their local egress location and either switch to or simulate other remote locations.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Make sure you have:</p>
<ul>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">Deployed the Cloudflare One Client</a> on your users' devices.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/">Configured tunnels</a> to connect your private network to Cloudflare. This tutorial assumes you have:
<ul>
<li>Created two tunnels <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">through the dashboard</a>.</li>
<li>Routed <code>10.0.0.0/8</code> through one tunnel.</li>
<li>Routed <code>192.168.88.0/24</code> through the other tunnel.</li>
</ul>
</li>
<li>Received multiple <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">dedicated egress IP addresses</a>.</li>
</ul>
<h2 id="create-a-virtual-network-for-each-egress-route">Create a virtual network for each egress route</h2>
<p>First, create <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">virtual networks</a> corresponding to your dedicated egress IPs.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4282.md")
</div></div>
<h2 id="assign-each-virtual-network-to-each-tunnel">Assign each virtual network to each tunnel</h2>
<p>After creating your virtual networks, route your private network CIDRs over each virtual network. This ensures that users can reach all services on your network regardless of which egress IP they use.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4285.md")
</div></div>
<p>Each tunnel connected to your private network should have each of your virtual networks assigned to it. For example, if you have tunnels routing <code>10.0.0.0/8</code> and <code>192.168.88.0/24</code>, both tunnels should have the <code>vnet-AMER</code> and <code>vnet-EMEA</code> virtual networks assigned.</p>
<table>
<thead>
<tr>
<th>Tunnel</th>
<th>CIDR</th>
<th>Virtual network</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Tunnel 1</strong></td>
<td><code>10.0.0.0/8</code></td>
<td><code>vnet-AMER</code></td>
</tr>
<tr>
<td></td>
<td><code>10.0.0.0/8</code></td>
<td><code>vnet-EMEA</code></td>
</tr>
<tr>
<td><strong>Tunnel 2</strong></td>
<td><code>192.168.88.0/24</code></td>
<td><code>vnet-AMER</code></td>
</tr>
<tr>
<td></td>
<td><code>192.168.88.0/24</code></td>
<td><code>vnet-EMEA</code></td>
</tr>
</tbody>
</table>
<h2 id="create-virtual-network-egress-policies">Create virtual network egress policies</h2>
<p>Next, assign your dedicated egress IPs to each virtual network using Gateway egress policies.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4288.md")
</div></div>
<p>Each policy you create should correspond to a different primary dedicated egress IP.</p>
<h2 id="test-virtual-network-egress">Test virtual network egress</h2>
<details class="nb-details"><summary>Windows, macOS, and Linux</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4290.md")
</div></details>
<details class="nb-details"><summary>iOS and Android</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4291.md")
</div></details>
<p>While your users are connected to a virtual network, their traffic will route via the dedicated egress IP specified. You can repeat these steps to test that each virtual network is egressing from the correct IP.</p>
