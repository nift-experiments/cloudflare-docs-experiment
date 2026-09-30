<p>You can use Private Network Load Balancing to distribute Cloudflare One Client traffic to private hostnames and IPs connected via <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>.</p>
<p>For example, assume you have an internal application running in two data centers, and you want Cloudflare One Client users to access the application from the data center closest to their geographic location. A typical load balancing configuration is shown in the following diagram:</p>
<pre><code class="language-mermaid">graph LR&#10;    W[WARP clients] --&gt; C{Private load balancer &lt;br&gt; 100.112.0.0}&#10;    C -- Tunnel 1 --&gt; cf1&#10;    C -- Tunnel 2 --&gt; cf2&#10;		subgraph D2[Data center 2]&#10;			cf2@{ shape: processes, label: &quot;cloudflared&quot; }&#10;			subgraph F[Pool 2]&#10;					S3[&quot;Endpoint &lt;br&gt; 10.0.0.1 (VNET-2)&quot;]&#10;					S4[&quot;Endpoint &lt;br&gt; 10.0.0.2 (VNET-2)&quot;]&#10;			end&#10;			cf2--&gt;S3&#10;			cf2--&gt;S4&#10;		end&#10;		subgraph D1[Data center 1]&#10;			cf1@{ shape: processes, label: &quot;cloudflared&quot; }&#10;			subgraph E[Pool 1]&#10;					S1[&quot;Endpoint &lt;br&gt; 10.0.0.1 (VNET-1)&quot;]&#10;					S2[&quot;Endpoint &lt;br&gt; 10.0.0.2 (VNET-1)&quot;]&#10;			end&#10;			cf1--&gt;S1&#10;			cf1--&gt;S2&#10;		end&#10;&#10;		style E stroke-width:2px,stroke-dasharray: 5 5&#10;		style F stroke-width:2px,stroke-dasharray: 5 5&#10;</code></pre>
<p>The components in the diagram include:</p>
<ul>
<li><strong>cloudflared</strong>: Each data center is connected to Cloudflare with its own Cloudflare Tunnel. <code>cloudflared</code> installs on one or <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/#cloudflared-replicas">more</a> host machines in the network.</li>
<li><strong>Private load balancer IP</strong>: End users connect to the application using the load balancer's IP address. This can either be a Cloudflare-assigned IP in <code>100.112.0.0/16</code> or a custom <code>/32</code> IP in an <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918 range</a>.</li>
<li><strong>Load balancer pool</strong>: The load balancer is configured with one <a href="/load-balancing/understand-basics/load-balancing-components/#pools">pool</a> per tunnel.</li>
<li><strong>Load balancer endpoint</strong>: A pool contains one or more endpoints, where each endpoint is a server behind <code>cloudflared</code> that is running the application. If your servers have overlapping IPs, you can assign a distinct <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">virtual network (VNET)</a> per tunnel so that Load Balancer can deterministically route requests to the correct endpoint.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10339.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Your endpoint IP addresses route through Cloudflare Tunnel. To learn how to connect your private network, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">Connect an IP/CIDR</a>.</li>
</ul>
<h2 id="1-create-load-balancer-pools"><ol>
<li>Create load balancer pools</li>
</ol></h2>
<p>Load balancer pools are logical groupings of endpoints, typically organized by physical datacenter or geographic region. The endpoints in the pool are the destinations where traffic is ultimately routed.</p>
<p>Pools can be created using either the Cloudflare dashboard or the API.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10342.md")
</div></div>
<h2 id="2-create-a-private-load-balancer"><ol start="2">
<li>Create a private load balancer</li>
</ol></h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Load Balancing</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create a Load Balancer</strong>.</li>
<li>Select <strong>Private Load Balancer</strong>.</li>
<li>On the next step you can choose to associate this load balancer with either:
<ul>
<li>A Cloudflare-assigned IP from the <code>100.112.0.0/16</code> range</li>
<li>A custom <code>/32</code> IP in an <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918 range</a></li>
</ul>
</li>
<li>Add a descriptive name to identify your load balancer.</li>
<li>Proceed through the setup.</li>
</ol>
<p>After completing the setup, you will be redirected to the Load Balancing dashboard. You can locate your load balancer using the search bar or by filtering for <strong>Private</strong> load balancers. Be sure to note the load balancer IP as it will be required in the following steps.</p>
<h2 id="3-route-the-load-balancer-ip-through-the-cloudflare-one-client"><ol start="3">
<li>Route the load balancer IP through the Cloudflare One Client</li>
</ol></h2>
<p>In order for Cloudflare One Clients to connect to your load balancer, the load balancer's IP address must route through the WARP tunnel in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel settings</a>.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Device profiles</strong>.</li>
<li>Find the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> you would like to modify and select <strong>Edit</strong>.</li>
<li>Under <strong>Split Tunnels</strong>, check whether your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#change-split-tunnels-mode">Split Tunnels mode</a> is set to <strong>Exclude</strong> or <strong>Include</strong>.</li>
<li>Select <strong>Manage</strong>. Depending on the mode:
<ul>
<li><strong>Exclude mode</strong>: Delete the IP range that contains your load balancer IP. For example, if your load balancer has a Cloudflare-assigned CGNAT IP, delete <code>100.64.0.0/10</code>. We recommend <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/#3-route-private-network-ips-through-the-cloudflare-one-client">adding back the IPs</a> that are not being used by your load balancer.</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10337.md")
</aside>
   - **Include mode**: Add your load balancer IP.
<p>Cloudflare One Client traffic can now reach your private load balancer. For example, if your load balancer points to a web application, you can test by running <code>curl &lt;load-balancer-IP&gt;</code> from the device. This traffic will be distributed over Cloudflare Tunnel to your private endpoints according to your configured steering method.</p>
<h2 id="4-optional-assign-a-hostname-to-the-load-balancer"><ol start="4">
<li>(Optional) Assign a hostname to the load balancer</li>
</ol></h2>
<p>If you want your load balancer and its endpoints to be transparently accessible to users via a hostname, you can create a Gateway DNS <a href="/cloudflare-one/traffic-policies/dns-policies/#override">Override policy</a> that maps the hostname to the load balancer's IP address. This ensures that traffic destined for the hostname resolves to the correct IP.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong> &gt; <strong>DNS</strong>.</li>
<li>Select <strong>Add a policy</strong>.</li>
<li>In <strong>Traffic</strong>, create an expression where the <strong>Selector</strong> equals <code>Host</code>, the <strong>Operator</strong> equals <code>is</code>, and <strong>Value</strong> is the hostname you wish to associate with your load balancer. For example,</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td>is</td>
<td><code>app.internal.local</code></td>
</tr>
</tbody>
</table>
<ol start="4">
<li>Set the <strong>Action</strong> to <em>Override</em>.</li>
<li>In <strong>Override Hostname</strong>, enter your private load balancer IP (for example, <code>100.112.0.0</code>).</li>
</ol>
<p>Requests to the hostname will now resolve to your private load balancer.</p>
