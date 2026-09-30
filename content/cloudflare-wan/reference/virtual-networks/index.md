<p>A virtual network is a private routing domain within your Cloudflare account. It defines which private resources are reachable from the Cloudflare network and keeps traffic separated between different environments, partners, or applications.</p>
<p>Every Cloudflare account has a default virtual network. You can create additional virtual networks to isolate routing between different parts of your infrastructure.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6767.md")
</aside>
<h2 id="when-to-use-virtual-networks">When to use virtual networks</h2>
<ul>
<li><strong>Environment separation</strong> — Keep production and staging networks isolated. Traffic destined for <code>10.0.0.1</code> in production routes to a different destination than <code>10.0.0.1</code> in staging.</li>
<li><strong>Partner isolation</strong> — Connect multiple partners to your Cloudflare account without allowing them to reach each other. Each partner gets its own virtual network.</li>
<li><strong>Overlapping IP space</strong> — When different networks use the same IP ranges (common with RFC 1918 addresses), virtual networks let you route to the correct destination based on context, not just IP address.</li>
<li><strong>Private application connectivity</strong> — Connect Cloudflare Workers or CDN to backends in your private network. The virtual network tells Cloudflare where to route traffic for private IP addresses.</li>
<li><strong>Public TCP/UDP to private origins</strong> — Expose a private backend to the Internet for TCP or UDP traffic through a <a href="/spectrum/get-started/#create-a-spectrum-application-using-a-virtual-network-origin">Spectrum application</a>, without requiring a Load Balancer. The virtual network determines which tunnel or WAN connection carries the traffic to your origin.</li>
</ul>
<h2 id="how-virtual-networks-work">How virtual networks work</h2>
<p>When traffic enters Cloudflare destined for a private IP address, Cloudflare looks up the route in the virtual network routing table. The virtual network determines:</p>
<ul>
<li>Which private destinations are reachable.</li>
<li>Which connector (Tunnel or WAN connection) carries the traffic.</li>
<li>How overlapping IP addresses are disambiguated.</li>
</ul>
<pre><code class="language-mermaid">flowchart TD&#10;accTitle: Virtual network routing&#10;accDescr: Shows how a Cloudflare account contains three virtual networks, each with their own routing table and connectors pointing to separate destinations. The same CIDR can exist in each virtual network as isolated routing domains.&#10;&#10;    subgraph account [&quot;Your Cloudflare account&quot;]&#10;        direction LR&#10;&#10;        subgraph vnet_default [&quot;Virtual Network: default&quot;]&#10;            routes_d(&quot;10.0.0.0/8 via Tunnel&#10;            192.168.1.0/24 via IPsec&quot;)&#10;            routes_d --&gt; tunnel_d([&quot;Tunnel&quot;])&#10;            routes_d --&gt; ipsec_d([&quot;IPsec&quot;])&#10;        end&#10;&#10;        subgraph vnet_prod [&quot;Virtual Network: production&quot;]&#10;            routes_p(&quot;10.0.0.0/8 via Tunnel&quot;)&#10;            routes_p --&gt; tunnel_p([&quot;Tunnel (prod)&quot;])&#10;        end&#10;&#10;        subgraph vnet_stg [&quot;Virtual Network: staging&quot;]&#10;            routes_s(&quot;10.0.0.0/8 via Tunnel&quot;)&#10;            routes_s --&gt; tunnel_s([&quot;Tunnel (stg)&quot;])&#10;        end&#10;    end&#10;&#10;    tunnel_d --&gt; dc_legacy(&quot;Legacy DC&#10;    10.0.0.0/8&quot;)&#10;    ipsec_d --&gt; dc_branch(&quot;Branch (IPsec)&#10;    192.168.1.0/24&quot;)&#10;    tunnel_p --&gt; dc_prod(&quot;Production DC&#10;    10.0.0.0/8&quot;)&#10;    tunnel_s --&gt; dc_stg(&quot;Staging DC&#10;    10.0.0.0/8&quot;)&#10;&#10;    classDef orange fill:#f48120,stroke:#d6710e,color:#fff&#10;    classDef blue fill:#4b9fd5,stroke:#3a8bc2,color:#fff&#10;&#10;    class tunnel_d,tunnel_p,tunnel_s orange&#10;    class ipsec_d blue&#10;&#10;    style vnet_default stroke:#999,stroke-width:2px,stroke-dasharray: 5 5&#10;    style vnet_prod stroke:#f48120,stroke-width:2px&#10;    style vnet_stg stroke:#f48120,stroke-width:2px&#10;</code></pre>
<p>The same CIDR (<code>10.0.0.0/8</code>) can exist in each virtual network because they are isolated routing domains.</p>
<p>Each virtual network maintains its own routing table. Routes added to one virtual network do not appear in another virtual network routing table. However, if traffic does not match a route in the selected virtual network, Cloudflare may fall back to the default virtual network routing table for WAN routes.</p>
<p>You can add entries to a virtual network routing table through static route configuration or routes learned from BGP peering (beta). Static routes are available for all connection types. BGP peering is currently available over CNI and IPsec/GRE tunnels (beta). For more information on how routes are prioritized within a virtual network, refer to <a href="/cloudflare-wan/reference/traffic-steering/">Traffic steering</a>.</p>
<h2 id="virtual-networks-across-cloudflare">Virtual networks across Cloudflare</h2>
<p>Virtual network support varies by product:</p>
<table>
<thead>
<tr>
<th>Product</th>
<th>Virtual network support</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Tunnel</td>
<td>Multiple virtual networks</td>
<td>Assign CIDR routes to a virtual network when configuring your tunnel</td>
</tr>
<tr>
<td>Cloudflare One Client</td>
<td>Multiple virtual networks</td>
<td>Users land in a virtual network based on policy or client selection</td>
</tr>
<tr>
<td>Cloudflare Mesh</td>
<td>Not currently supported</td>
<td>—</td>
</tr>
<tr>
<td>Cloudflare WAN</td>
<td>Default only</td>
<td>All IPsec, GRE, and CNI connections use the default virtual network</td>
</tr>
</tbody>
</table>
<h2 id="the-default-virtual-network">The default virtual network</h2>
<p>Every account has a <code>default</code> virtual network. If you do not specify a virtual network when creating routes or connections, they are assigned to the default.</p>
<p>For most deployments with a single private network, the default virtual network is all you need. Create additional virtual networks only when you need routing isolation.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6766.md")
</aside>
<h2 id="for-network-engineers">For network engineers</h2>
<p>If you are familiar with enterprise networking concepts, a virtual network is analogous to a VRF (Virtual Routing and Forwarding):</p>
<ul>
<li>Each virtual network maintains its own routing table.</li>
<li>Routes are isolated between virtual networks.</li>
<li>The same IP prefix can exist in multiple virtual networks without conflict.</li>
<li>BGP routes learned on a connection populate only that connection virtual network routing table. BGP peering is currently supported for IPsec/GRE tunnels (beta) and CNI (beta).</li>
</ul>
<p>If you are familiar with cloud networking concepts, a virtual network is analogous to a VPC (Virtual Private Cloud).</p>
<h2 id="create-and-manage-virtual-networks">Create and manage virtual networks</h2>
<p>To create and configure virtual networks, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">Virtual networks (Tunnel configuration)</a>.</p>
<p>To configure which routes belong to which virtual network, refer to <a href="/cloudflare-one/networks/routes/add-routes/">Add routes</a>.</p>
<p>To add static routes or configure BGP peering within the Cloudflare Virtual Network routing table, refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/">Configure routes</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">Private networks</a> — Connect your infrastructure to Cloudflare</li>
<li><a href="/cloudflare-one/networks/routes/">Routes</a> — Define IP and hostname routes through your connectors</li>
<li><a href="/cloudflare-wan/reference/traffic-steering/">Traffic steering</a> — Route prioritization, ECMP, and BGP within the Cloudflare Virtual Network</li>
</ul>
