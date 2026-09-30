<p>For production deployments, you can run multiple replicas of a Mesh node in active-passive mode. All replicas share the same node identity and advertise the same <a href="/mesh/features/routes/">routes</a>. If the active replica goes down, Cloudflare automatically promotes a standby replica.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="masque-required">MASQUE required</h3>
@markup("md", "content/.markup/bodies/5229.md")
</aside>
<h2 id="when-to-use-high-availability">When to use high availability</h2>
<p>High availability provides resilience for CIDR route prefixes advertised by a Mesh node. When the active replica disconnects, Cloudflare promotes a standby so that traffic to the advertised subnets continues to flow.</p>
<p>This means HA is useful for nodes that have routes configured — nodes acting as subnet gateways for private networks behind them. If a node is only used for direct Mesh IP connectivity (no routes), HA has limited benefit because the node's Mesh IP is tied to the individual replica.</p>
<h2 id="how-it-works">How it works</h2>
<p>When you create a Mesh node with high availability enabled, Cloudflare generates a single token for that node. You install the Cloudflare One Client on multiple Linux hosts using this token. Each host registers as a replica of the same node.</p>
<ul>
<li>All replicas advertise the same CIDR routes.</li>
<li>One replica is active at a time. The others are passive standby.</li>
<li>If the active replica disconnects, Cloudflare automatically promotes a passive replica.</li>
<li>Failover is handled by Cloudflare's network.</li>
</ul>
<pre><code class="language-mermaid">flowchart LR&#10;  subgraph replicas[&quot;Mesh node: web-server&quot;]&#10;    R1[&quot;Replica 1 &lt;br&gt; (active)&quot;]&#10;    R2[&quot;Replica 2 &lt;br&gt; (standby)&quot;]&#10;    R3[&quot;Replica 3 &lt;br&gt; (standby)&quot;]&#10;  end&#10;  CF((Cloudflare)) &lt;--&gt; R1&#10;  CF -. failover .-&gt; R2&#10;  CF -. failover .-&gt; R3&#10;  client[&quot;Client device&quot;] &lt;--&gt; CF&#10;</code></pre>
<h2 id="create-a-node-with-high-availability">Create a node with high availability</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5232.md")
</div></div>
<h2 id="add-replicas">Add replicas</h2>
<p>To add a replica to an existing high-availability node, install the Cloudflare One Client on a new Linux host and register it using the same node token.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5242.md")
</div></div>
<p>The new replica will be in standby mode until the active replica disconnects.</p>
<h2 id="view-replicas">View replicas</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5245.md")
</div></div>
<h2 id="manual-failover">Manual failover</h2>
<p>In addition to automatic failover when the active replica disconnects, you can manually promote a passive replica to active.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5248.md")
</div></div>
<h2 id="considerations">Considerations</h2>
<h3 id="setup-requirements">Setup requirements</h3>
<ul>
<li>High availability is set at node creation time and cannot be changed afterward.</li>
<li>You must install the client on at least two hosts for failover to work. A single replica means no redundancy.</li>
<li>High availability requires that the Mesh node's <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> is configured to use <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">MASQUE</a>, the default protocol for the Cloudflare One Client. It does not work if the device profile uses WireGuard instead.</li>
</ul>
<h3 id="network-configuration">Network configuration</h3>
<ul>
<li>All replicas must be on the same subnet and have the same network routing configuration (Split Tunnels, static routes).</li>
<li>HA provides resilience for CIDR route prefixes. Nodes without routes do not benefit from HA failover.</li>
</ul>
<h3 id="failover-behavior">Failover behavior</h3>
<ul>
<li>Failover time depends on how quickly Cloudflare detects the active replica has disconnected (typically seconds).</li>
<li>Inbound traffic (from Mesh clients to the subnet) fails over automatically on Cloudflare's network. Cloudflare routes traffic to the newly promoted active replica.</li>
<li>Outbound traffic (from devices on the subnet through the Mesh node) does not fail over automatically. Your environment must detect that a different replica has been promoted to active and update routing tables to send traffic through the now-active host. There is no client-side failover for on-ramp traffic at this time.</li>
</ul>
