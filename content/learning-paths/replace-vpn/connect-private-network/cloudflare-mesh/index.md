<p><a href="/mesh/">Cloudflare Mesh</a> (formerly WARP Connector) connects your private networks to Cloudflare using the Cloudflare One Client (<code>warp-cli</code>) running in headless mode on a Linux server. Every enrolled device and node receives a private Mesh IP and can communicate with any other participant over TCP, UDP, or ICMP.</p>
<p>Mesh supports bidirectional traffic — devices can reach servers, servers can reach devices, and networks can reach other networks. This makes it the recommended approach for replacing a VPN, as it covers both user-to-network and network-to-network connectivity.</p>
<h2 id="set-up-cloudflare-mesh">Set up Cloudflare Mesh</h2>
<p>To connect your private network using Cloudflare Mesh, refer to <a href="/mesh/get-started/">Get started with Cloudflare Mesh</a>.</p>
<p>The setup wizard in the dashboard configures enrollment, device profiles, and connectivity settings automatically. Once a node is online, add <a href="/mesh/features/routes/">CIDR routes</a> to make the subnet behind it reachable from any enrolled device.</p>
<h2 id="when-to-use-mesh">When to use Mesh</h2>
<ul>
<li>Replacing a VPN for remote access to private networks</li>
<li>Bidirectional connectivity (VoIP, SIP, Active Directory, SCCM, DevOps pipelines)</li>
<li>Long-lived TCP connections sensitive to interruptions (SAP, database replication, ERP systems, RDP sessions)</li>
<li>Site-to-site networking between offices, data centers, or cloud VPCs</li>
<li>Client-to-client connectivity (two laptops reaching each other by private IP)</li>
<li>Any L3/L4 workload where source IP preservation matters</li>
</ul>
<h2 id="best-practices">Best practices</h2>
<ul>
<li>Enable <a href="/mesh/features/high-availability/">high availability</a> for production nodes with CIDR routes.</li>
<li>Use <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a> to control which users and devices can reach specific resources.</li>
<li>Refer to <a href="/mesh/best-practices/">Tips and best practices</a> for cloud VPC configuration and running alongside Cloudflare Tunnel.</li>
</ul>
