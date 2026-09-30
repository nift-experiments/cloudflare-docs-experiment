<p>Cloudflare Mesh connects your services and devices with post-quantum encrypted networking. Route traffic privately between servers, laptops, and phones without VPNs or bastion hosts.</p>
<p>Every enrolled device and node receives a private IP address (Mesh IP) and can reach any other participant by IP over TCP, UDP, or ICMP, with traffic routed through Cloudflare's network.</p>
<p>Mesh nodes are Linux servers running the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> (<code>warp-cli</code>) in headless mode. Client devices are laptops and phones running the same client with a UI.</p>
<p><img src="/assets/upstream/images/cloudflare-one/connections/mesh-network-map.gif" alt="The Mesh network map in the Cloudflare dashboard showing nodes and devices connected through Cloudflare" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10794.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>Mesh has two types of participants:</p>
<table>
<thead>
<tr>
<th></th>
<th>Mesh nodes</th>
<th>Client devices</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Runs on</strong></td>
<td>Linux servers, VMs, containers</td>
<td>Laptops, phones, desktops</td>
</tr>
<tr>
<td><strong>Client</strong></td>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> (<code>warp-cli</code>), headless</td>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> (<code>warp-cli</code>) with UI</td>
</tr>
<tr>
<td><strong>Mesh IP</strong></td>
<td>Assigned on enrollment</td>
<td>Assigned on enrollment</td>
</tr>
<tr>
<td><strong>Subnet routing</strong></td>
<td>Can advertise CIDR routes</td>
<td>No — clients reach subnets through nodes</td>
</tr>
<tr>
<td><strong>High availability</strong></td>
<td>Supports active-passive replicas</td>
<td>Not applicable</td>
</tr>
</tbody>
</table>
<p>Any participant can reach any other participant by Mesh IP. Client-to-client connectivity works without deploying any Mesh nodes.</p>
<pre><code class="language-mermaid">flowchart LR&#10;  subgraph nodes[&quot;Mesh nodes&quot;]&#10;    A[&quot;web-server &lt;br&gt; 100.96.0.1&quot;]&#10;    B[&quot;db-replica &lt;br&gt; 100.96.0.2&quot;]&#10;  end&#10;  subgraph devices[&quot;Client devices&quot;]&#10;    C[&quot;MacBook &lt;br&gt; 100.96.0.10&quot;]&#10;    D[&quot;iPhone &lt;br&gt; 100.96.0.11&quot;]&#10;  end&#10;  A &lt;--&gt; CF((Cloudflare &lt;br&gt; network))&#10;  B &lt;--&gt; CF&#10;  CF &lt;--&gt; C&#10;  CF &lt;--&gt; D&#10;</code></pre>
<p>All traffic passes through Cloudflare, so <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a>, <a href="/cloudflare-one/reusable-components/posture-checks/">device posture checks</a>, and access rules apply to every connection.</p>
<h2 id="protocol-requirement">Protocol requirement</h2>
<p>Cloudflare Mesh requires that the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> of each Mesh node is configured to use <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">MASQUE</a>, the default protocol for the Cloudflare One Client. Most deployments do not need to change anything.</p>
<p>If a Mesh node's device profile uses WireGuard instead, the following capabilities will not work:</p>
<ul>
<li><a href="/mesh/features/routes/#hostname-routes">Hostname routes</a></li>
<li><a href="/mesh/features/routes/#manage-cidr-routes">IPv6 CIDR routes</a></li>
<li><a href="/mesh/features/high-availability/">High availability</a></li>
</ul>
<h2 id="mesh-ips">Mesh IPs</h2>
<p>Every participant is assigned a private IP from the <code>100.96.0.0/12</code> range. In other parts of the Cloudflare One documentation, these addresses are referred to as <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-ips/">device IPs</a>.</p>
<p>This range uses <a href="https://datatracker.ietf.org/doc/html/rfc6598">CGNAT address space</a> to avoid conflicts with RFC 1918 private ranges (<code>10.x</code>, <code>172.16.x</code>, <code>192.168.x</code>). If the default range conflicts with your network, you can <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-ips/">configure a custom subnet</a>.</p>
<p>View a device's Mesh IP on the <a href="https://dash.cloudflare.com/?to=/:account/mesh">Mesh overview page</a> or on the node detail page in the dashboard.</p>
<p>For details on reserved ranges, refer to <a href="/cloudflare-one/networks/routes/reserved-ips/">Reserved IP addresses</a>.</p>
<h2 id="mesh-vs-tunnel">Mesh vs. Tunnel</h2>
<p>Both Cloudflare Mesh and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> connect private infrastructure to Cloudflare, but they solve different problems:</p>
<table>
<thead>
<tr>
<th></th>
<th>Cloudflare Mesh</th>
<th>Cloudflare Tunnel</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Traffic direction</strong></td>
<td>Bidirectional — any participant can initiate</td>
<td>Inbound to origin — clients connect to published services</td>
</tr>
<tr>
<td><strong>Addressing</strong></td>
<td>Every participant gets a Mesh IP</td>
<td>Server-side only, no Mesh IPs</td>
</tr>
<tr>
<td><strong>Use case</strong></td>
<td>Private IP connectivity between devices and servers</td>
<td>Publishing specific applications, hostnames, or IP routes</td>
</tr>
<tr>
<td><strong>Connector</strong></td>
<td><code>warp-cli</code></td>
<td><code>cloudflared</code></td>
</tr>
<tr>
<td><strong>Protocols</strong></td>
<td>TCP, UDP, ICMP</td>
<td>HTTP/S, TCP, SSH, RDP, SMB (proxied over WebSocket)</td>
</tr>
</tbody>
</table>
<p>Use Mesh when devices need to reach each other by private IP, or when your workload requires stable, long-lived TCP connections (SAP, database replication, ERP systems, RDP sessions). Mesh operates at L3/L4 and preserves connections end-to-end, making it the recommended software on-ramp for any traffic sensitive to connection interruptions. Use Tunnel when you want to publish services by hostname or proxy traffic to specific IP ranges through <code>cloudflared</code>.</p>
<details class="nb-details"><summary>Coming from another mesh networking product?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10795.md")
</div></details>
<h2 id="next-steps">Next steps</h2>
<ol>
<li><a href="/mesh/get-started/"><strong>Create your first Mesh node</strong></a> — The dashboard wizard handles provisioning. Install the client on a Linux server with two commands.</li>
<li><a href="/mesh/guides/connect-client-devices/"><strong>Connect client devices</strong></a> — Install the Cloudflare One Client on laptops and phones. They can reach each other and any Mesh node by Mesh IP.</li>
<li><a href="/mesh/guides/run-mesh-in-containers/"><strong>Run in Docker / Kubernetes</strong></a> — Deploy a Mesh node as a Docker container for Docker Compose, Kubernetes, and CI/CD environments.</li>
<li><a href="/mesh/features/routes/"><strong>Add routes</strong></a> (optional) — Make subnets behind a Mesh node reachable from any device.</li>
<li><a href="/mesh/features/high-availability/"><strong>Enable high availability</strong></a> (optional) — Run multiple replicas of a node for failover.</li>
<li><a href="/workers-vpc/examples/connect-to-cloudflare-mesh/"><strong>Connect from Workers</strong></a> (optional) — Use VPC Network bindings to reach private services from Cloudflare Workers.</li>
<li><a href="/cloudflare-one/networks/connectors/granular-permissions/"><strong>Delegate access</strong></a> (optional) — Scope member permissions to specific Mesh nodes instead of granting account-wide control.</li>
</ol>
