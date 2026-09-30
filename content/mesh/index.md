<div class="nb-description">
@markup("md", "content/.markup/bodies/749.md")
</div>
<p>Cloudflare Mesh gives every enrolled server, laptop, and phone a private Mesh IP. Participants can communicate by IP over TCP, UDP, or ICMP, including device-to-device connections that do not require customer-managed networking infrastructure.</p>
<p>Mesh nodes run the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> in headless mode on Linux. They can also advertise routes to make private subnets and hostnames reachable from other Mesh participants.</p>
<p><img src="/assets/upstream/images/cloudflare-one/connections/mesh-network-map.gif" alt="The Mesh network map in the Cloudflare dashboard showing nodes and devices connected through Cloudflare" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/748.md")
</aside>
<p><span id="how-it-works"></span>
<span id="protocol-requirement"></span>
<span id="mesh-ips"></span></p>
<p>For details about how Mesh works, protocol requirements, and Mesh IP assignment, refer to <a href="/mesh/concepts/">Concepts</a>.</p>
<h2 id="use-cases">Use cases</h2>
<ul>
<li>Connect enrolled devices to each other by private IP.</li>
<li>Provide bidirectional connectivity between servers, cloud networks, and sites.</li>
<li>Route traffic to devices that cannot run the Cloudflare One Client.</li>
<li>Preserve long-lived TCP connections for databases, replication, ERP systems, and remote administration.</li>
</ul>
<h2 id="get-started">Get started</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/754.md")
</div>
<p><span id="mesh-vs-tunnel"></span></p>
<h2 id="mesh-vs-cloudflare-tunnel">Mesh vs. Cloudflare Tunnel</h2>
<p>Use Mesh when participants need bidirectional private IP connectivity or when a workload requires stable, long-lived connections. Use <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> when you want to publish specific applications, hostnames, or IP routes through an outbound-only connector.</p>
<p>For a detailed comparison, refer to <a href="/mesh/concepts/#mesh-vs-tunnel">How Cloudflare Mesh works</a>.</p>
