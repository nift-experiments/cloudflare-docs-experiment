<p>Cloudflare One provides multiple connectivity options for your users, devices, and network infrastructure. Each option serves different use cases, from protecting individual devices to connecting entire data centers.</p>
<p>This page helps you understand which connectivity options to use based on your requirements, and how to combine multiple options in a single deployment.</p>
<h2 id="cloudflare-one-on-ramps-and-off-ramps">Cloudflare One on-ramps and off-ramps</h2>
<p>Cloudflare One connectivity options use the concept of on-ramps and off-ramps:</p>
<ul>
<li><strong>On-ramps</strong> send traffic into Cloudflare's network. For example, a user's device with the Cloudflare One Client installed on-ramps their traffic to Cloudflare for inspection and policy enforcement.</li>
<li><strong>Off-ramps</strong> send traffic from Cloudflare's network to your infrastructure. For example, Cloudflare Tunnel off-ramps traffic to your private applications without exposing them to the public Internet.</li>
</ul>
<p>Some connectivity options support both directions (bidirectional), while others only support one direction.</p>
<h2 id="connectivity-options-comparison">Connectivity options comparison</h2>
<p>The following table provides a high-level comparison of all connectivity options available to Cloudflare One customers.</p>
<p><strong>Table 1: All Cloudflare One connectivity options</strong></p>
<table>
<thead>
<tr>
<th>Connectivity option</th>
<th>Protocol</th>
<th>Direction</th>
<th>Typical deployment model</th>
<th>Use when</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#cloudflare-tunnel">Cloudflare Tunnel</a></td>
<td>HTTP/2, QUIC</td>
<td>Off-ramp only</td>
<td>Software daemon (<code>cloudflared</code>) on server</td>
<td>Exposing private applications without a public IP</td>
</tr>
<tr>
<td><a href="#cloudflare-one-client">Cloudflare One Client</a></td>
<td>MASQUE (default), WireGuard</td>
<td>Bidirectional</td>
<td>Client software on end-user devices</td>
<td>Securing remote workforce devices</td>
</tr>
<tr>
<td><a href="#cloudflare-mesh">Cloudflare Mesh</a></td>
<td>MASQUE</td>
<td>Bidirectional</td>
<td>Software client on Linux host</td>
<td>Connecting sites with IoT or VoIP devices</td>
</tr>
<tr>
<td><a href="#dns-locations">DNS locations</a></td>
<td>DNS (DoH, DoT, IPv4/IPv6)</td>
<td>On-ramp only</td>
<td>DNS resolver configuration</td>
<td>Filtering DNS traffic without device agents</td>
</tr>
<tr>
<td><a href="#proxy-endpoints">Proxy endpoints</a></td>
<td>HTTP/HTTPS</td>
<td>On-ramp only</td>
<td>Browser PAC file configuration</td>
<td>Filtering web traffic without device agents</td>
</tr>
<tr>
<td><a href="#clientless-web-isolation">Clientless Web Isolation</a></td>
<td>HTTP/HTTPS</td>
<td>On-ramp only</td>
<td>Prefixed URL with Access authentication</td>
<td>Secure web access for unmanaged devices</td>
</tr>
<tr>
<td><a href="#gre-tunnels">GRE tunnels</a></td>
<td>GRE</td>
<td>Bidirectional</td>
<td>Network tunnel from router or firewall</td>
<td>Connecting sites with existing network hardware</td>
</tr>
<tr>
<td><a href="#ipsec-tunnels">IPsec tunnels</a></td>
<td>IPsec</td>
<td>Bidirectional</td>
<td>Network tunnel from router or firewall</td>
<td>Encrypted site connectivity over the Internet</td>
</tr>
<tr>
<td><a href="#cloudflare-one-appliance">Cloudflare One Appliance</a></td>
<td>IPsec</td>
<td>Bidirectional</td>
<td>Hardware or virtual appliance</td>
<td>Zero-touch branch office deployments</td>
</tr>
<tr>
<td><a href="#cloudflare-network-interconnect-cni">Cloudflare Network Interconnect</a></td>
<td>Direct, Partner, Cloud</td>
<td>Bidirectional</td>
<td>Physical or virtual cross-connect</td>
<td>Bypassing the public Internet entirely</td>
</tr>
<tr>
<td><a href="#multi-cloud-networking">Multi-Cloud Networking</a></td>
<td>IPsec (automated)</td>
<td>Bidirectional</td>
<td>Cloud provider VPN integration</td>
<td>Connecting cloud VPCs with automated tunnel setup</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="cloudflare-tunnel">Cloudflare Tunnel</h2>
<p>Cloudflare Tunnel provides a secure way to connect your resources to Cloudflare without a publicly routable IP address. The <code>cloudflared</code> daemon creates outbound-only connections to Cloudflare's global network over port <code>7844</code> (TCP/UDP) using HTTP/2 or QUIC. This allows you to expose web servers, SSH servers, remote desktops, and other services without opening inbound ports on your firewall.</p>
<p>Use Cloudflare Tunnel when you need to expose private web applications, protect origin servers by hiding their IP addresses, or deploy cloud-native ingress for Kubernetes services.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="important-to-know">Important to know</h3>
@markup("md", "content/.markup/bodies/4486.md")
</aside>
<p>For detailed configuration, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel documentation</a>.</p>
<hr />
<h2 id="cloudflare-one-client">Cloudflare One Client</h2>
<p>The Cloudflare One Client is a device agent that securely connects end-user devices to Cloudflare's global network. The Cloudflare One Client encrypts traffic from the device using MASQUE (with post-quantum cryptography) or WireGuard and routes it through Cloudflare, where Gateway policies filter and inspect the traffic.</p>
<p>Use Cloudflare One Client to secure remote workforce devices, replace traditional VPN solutions, enforce DNS filtering and web security policies, implement device posture checks, and enable <a href="/mesh/">Mesh connectivity</a> between enrolled devices.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="important-to-know-1">Important to know</h3>
@markup("md", "content/.markup/bodies/4485.md")
</aside>
<p>For detailed configuration, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client documentation</a>.</p>
<hr />
<h2 id="cloudflare-mesh-beta">Cloudflare Mesh (beta)</h2>
<p>Cloudflare Mesh connects your services and devices with post-quantum encrypted networking. Every enrolled device and mesh node receives a private <a href="/mesh/concepts/#mesh-ips">Mesh IP</a> and can communicate with any other participant over TCP, UDP, or ICMP — including device-to-device without any infrastructure.</p>
<p>Mesh nodes run the Cloudflare One Client (<code>warp-cli</code>) in headless mode on Linux servers. They can advertise <a href="/mesh/features/routes/">CIDR routes</a> to make subnets behind them reachable, enabling connectivity to devices that cannot run the client (IoT, printers, legacy servers). All traffic preserves source IP addresses end-to-end.</p>
<p>Use Cloudflare Mesh for bidirectional connectivity (VoIP, SIP, AD updates, SCCM, DevOps), site-to-site networking, device-to-device connectivity, or any scenario where source IP preservation is important. For outbound-only access to private services, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> (<code>cloudflared</code>) is simpler to deploy and runs on all platforms.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="cloudflare-wan-compatibility">Cloudflare WAN compatibility</h3>
@markup("md", "content/.markup/bodies/4484.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4483.md")
</aside>
<p>For detailed configuration, refer to the <a href="/mesh/">Cloudflare Mesh documentation</a>.</p>
<hr />
<h2 id="dns-locations">DNS locations</h2>
<p>DNS locations allow you to filter DNS traffic from networks without deploying the Cloudflare One Client. By configuring your network's DNS resolver to point to Cloudflare Gateway, Gateway applies DNS policies to all queries from that location.</p>
<p>DNS locations support multiple endpoint types:</p>
<ul>
<li><strong>IPv4/IPv6</strong>: Standard DNS resolution using Cloudflare's resolver IPs</li>
<li><strong>DNS over HTTPS (DoH)</strong>: Encrypted DNS queries over HTTPS</li>
<li><strong>DNS over TLS (DoT)</strong>: Encrypted DNS queries over TLS</li>
</ul>
<p>Use DNS locations when you need to filter DNS traffic for an entire office or network, per device without installing agents on devices, or integrate with existing network infrastructure.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="important-to-know-2">Important to know</h3>
@markup("md", "content/.markup/bodies/4482.md")
</aside>
<p>For detailed configuration, refer to the <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">DNS locations documentation</a>.</p>
<hr />
<h2 id="proxy-endpoints">Proxy endpoints</h2>
<p>Proxy endpoints allow you to apply Cloudflare Gateway HTTP policies without installing a client on devices. By configuring a Proxy Auto-Configuration (PAC) file at the browser level, you route web traffic through Gateway for filtering and policy enforcement.</p>
<p>Cloudflare One supports two types of proxy endpoints:</p>
<ul>
<li><strong>Authorization endpoints</strong>: Use Cloudflare Access for identity-based authentication</li>
<li><strong>Source IP endpoints</strong>: Authorize traffic based on originating IP address (Enterprise only)</li>
</ul>
<p>Use proxy endpoints when you need to filter web traffic without device agents, integrate with existing proxy infrastructure, or deploy Gateway alongside other security tools.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="important-to-know-3">Important to know</h3>
@markup("md", "content/.markup/bodies/4481.md")
</aside>
<p>For detailed configuration, refer to the <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">Proxy endpoints documentation</a>.</p>
<hr />
<h2 id="clientless-web-isolation">Clientless Web Isolation</h2>
<p>Clientless Web Isolation allows users to securely access web applications through a remote browser without installing the Cloudflare One Client. Users navigate to a prefixed URL (<code>https://&lt;team-name&gt;.cloudflareaccess.com/browser/&lt;URL&gt;</code>), authenticate through Cloudflare Access, and Cloudflare renders the web content in an isolated browser, streaming only <a href="https://blog.cloudflare.com/cloudflare-and-remote-browser-isolation/">safe draw commands</a> to the user's device while enforcing isolation policies.</p>
<p>Use Clientless Web Isolation when you need to provide secure web access for unmanaged devices (contractors, BYOD), enable access to sensitive applications without requiring endpoint software, or on-ramp users who cannot install the Cloudflare One Client.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="important-to-know-4">Important to know</h3>
@markup("md", "content/.markup/bodies/4480.md")
</aside>
<p>For detailed configuration, refer to the <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">Clientless Web Isolation documentation</a>.</p>
<hr />
<h2 id="gre-tunnels">GRE tunnels</h2>
<p>Generic Routing Encapsulation (GRE) tunnels provide lightweight, stateless network connectivity between your infrastructure and Cloudflare. GRE tunnels are used with Cloudflare WAN (formerly Magic WAN) and Magic Transit to connect sites, data centers, and cloud environments using existing routers and firewalls.</p>
<p>Use GRE tunnels when you need to connect branch offices or data centers with minimal configuration overhead, integrate with Magic Transit for DDoS protection, or deploy redundant tunnels alongside IPsec.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="important-to-know-5">Important to know</h3>
@markup("md", "content/.markup/bodies/4479.md")
</aside>
<p>For detailed configuration, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/gre-ipsec-tunnels/">GRE and IPsec tunnels documentation</a>.</p>
<hr />
<h2 id="ipsec-tunnels">IPsec tunnels</h2>
<p>IPsec tunnels provide encrypted, stateful network connectivity between your infrastructure and Cloudflare. IPsec tunnels are used with Cloudflare WAN and Magic Transit for secure site-to-site connectivity, using IKEv2 for tunnel negotiation and AES-GCM or AES-CBC for encryption.</p>
<p>Use IPsec tunnels when you need to encrypt traffic over the public Internet or meet compliance requirements for encrypted connections. IPsec tunnels are supported on generic router and firewall appliances, and on cloud environment gateways (AWS, Azure, GCP).</p>
<p>For detailed configuration, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/gre-ipsec-tunnels/">GRE and IPsec tunnels documentation</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="key-consideration">Key consideration</h3>
@markup("md", "content/.markup/bodies/4478.md")
</aside>
<hr />
<h2 id="cloudflare-one-appliance">Cloudflare One Appliance</h2>
<p>Cloudflare One Appliance (formerly Magic WAN Connector) is a plug-and-play SD-WAN appliance that automates connectivity to Cloudflare's network. It establishes IPsec tunnels automatically and provides traffic steering. You can deploy it as a hardware appliance (Dell VEP1460) or virtual appliance (VMware ESXi, Proxmox).</p>
<p>Use Cloudflare One Appliance for zero-touch branch office deployments, to replace edge routers, achieve high throughput (1 Gbps or higher), or manage multiple sites through a centralized dashboard.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="key-consideration-1">Key consideration</h3>
@markup("md", "content/.markup/bodies/4477.md")
</aside>
<p>For detailed configuration, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliances/">Cloudflare One Appliance documentation</a>.</p>
<hr />
<h2 id="cloudflare-network-interconnect-cni">Cloudflare Network Interconnect (CNI)</h2>
<p>Cloudflare Network Interconnect (CNI) allows you to connect your network infrastructure directly to Cloudflare through private, dedicated connections that bypass the public Internet. CNI provides predictable latency, consistent throughput, and reduced exposure to attacks.</p>
<p>Use CNI when you need to meet security requirements that prohibit public Internet traffic, reduce cloud egress costs, or deploy in highly regulated industries (financial services, healthcare).</p>
<h3 id="cni-connection-types">CNI connection types</h3>
<p>The following table describes the Cloudflare Network Interconnect (CNI) connection types.</p>
<p><strong>Table 2: Cloudflare One CNI connection types</strong></p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Description</th>
<th>Ideal for</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Direct Interconnect</strong></td>
<td>Physical fiber cross-connect in a shared data center</td>
<td>Customers colocated with Cloudflare who require maximum control and performance</td>
</tr>
<tr>
<td><strong>Partner Interconnect</strong></td>
<td>Virtual connection through connectivity partners (Megaport, Equinix Fabric, PacketFabric)</td>
<td>Customers not colocated with Cloudflare or who prefer managed connectivity</td>
</tr>
<tr>
<td><strong>Cloud Interconnect</strong></td>
<td>Private connection from cloud providers (AWS, GCP, Azure)</td>
<td>Customers with workloads in public clouds requiring private connectivity</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="key-consideration-2">Key consideration</h3>
@markup("md", "content/.markup/bodies/4476.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="important-to-know-6">Important to know</h3>
@markup("md", "content/.markup/bodies/4475.md")
</aside>
<p>For detailed configuration, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/network-interconnect/">Cloudflare Network Interconnect documentation</a>.</p>
<hr />
<h2 id="multi-cloud-networking">Multi-Cloud Networking</h2>
<p>Multi-Cloud Networking (formerly Magic Cloud Networking) is an automation layer that simplifies connecting cloud environments to Cloudflare WAN. Rather than manually configuring IPsec tunnels, Multi-Cloud Networking automatically discovers your cloud resources and creates the necessary VPN tunnels and routes on both sides (cloud provider and Cloudflare WAN).</p>
<p>Multi-Cloud Networking is not a separate tunnel type — it orchestrates your cloud provider's native VPN functionality (AWS VPN Gateway, Azure VPN, GCP Cloud VPN) to establish IPsec connectivity to Cloudflare WAN.</p>
<h3 id="use-cases">Use cases</h3>
<ul>
<li>Connect AWS, Azure, or GCP VPCs to Cloudflare WAN with minimal configuration</li>
<li>Automate tunnel and route creation instead of manual IPsec setup</li>
<li>Connect multiple VPCs through a hub architecture (AWS Transit Gateway)</li>
<li>Simplify multi-cloud networking across different providers</li>
</ul>
<h3 id="cloudflare-one-multi-cloud-on-ramp-types">Cloudflare One Multi-Cloud on-ramp types</h3>
<p>The following table describes the Multi-Cloud Networking on-ramp types.</p>
<p><strong>Table 3: Cloudflare One Multi-Cloud Networking on-ramp types</strong></p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Description</th>
<th>Use when</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Single VPC</strong></td>
<td>Connects one VPC directly to Cloudflare WAN via VPN tunnel</td>
<td>You have a single VPC to connect</td>
</tr>
<tr>
<td><strong>Hub</strong></td>
<td>Connects multiple VPCs through a cloud hub (for example, AWS Transit Gateway)</td>
<td>You need to connect multiple VPCs with inter-VPC communication</td>
</tr>
</tbody>
</table>
<h3 id="supported-cloud-providers">Supported cloud providers</h3>
<ul>
<li>AWS (single VPC and hubs)</li>
<li>Azure (single VPC)</li>
<li>GCP (single VPC)</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="key-consideration-3">Key consideration</h3>
@markup("md", "content/.markup/bodies/4474.md")
</aside>
<h3 id="deployment-notes">Deployment notes</h3>
<ul>
<li><strong>Azure VNet sizing</strong>: Multi-Cloud Networking creates a GatewaySubnet (<code>/27</code>) within your VNet for the Azure VPN Gateway. Ensure your VNet has sufficient address space. A <code>/20</code> or larger VNet is recommended to avoid address exhaustion.</li>
<li><strong>Cloud provider costs</strong>: Multi-Cloud Networking uses your cloud provider's native VPN services. Standard VPN gateway and data transfer costs from your cloud provider apply in addition to Cloudflare WAN costs.</li>
<li><strong>Tunnel creation time</strong>: Cloud provider VPN gateways can take 15-45 minutes to provision. Plan for this delay when onboarding new VPCs.</li>
</ul>
<p>For detailed configuration, refer to the <a href="/multi-cloud-networking/">Multi-Cloud Networking documentation</a>.</p>
<hr />
<h2 id="choose-the-right-cloudflare-one-connectivity-option">Choose the right Cloudflare One connectivity option</h2>
<p>The following table maps common requirements to recommended Cloudflare One connectivity options. These are not exhaustive recommendations.</p>
<p><strong>Table 4. Recommend Cloudflare One connectivity options for common requirements</strong></p>
<table>
<thead>
<tr>
<th>Requirement</th>
<th>Recommended option</th>
</tr>
</thead>
<tbody>
<tr>
<td>Expose a private web application without a public IP</td>
<td><a href="#cloudflare-tunnel">Cloudflare Tunnel</a></td>
</tr>
<tr>
<td>Secure end-user devices</td>
<td><a href="#cloudflare-one-client">Cloudflare One Client</a></td>
</tr>
<tr>
<td>Replace traditional VPN for remote access</td>
<td><a href="#cloudflare-tunnel">Cloudflare Tunnel</a> (primary) + <a href="#cloudflare-mesh">Cloudflare Mesh</a> (for bidirectional needs)</td>
</tr>
<tr>
<td>Connect a site with IoT devices or VoIP systems</td>
<td><a href="#gre-tunnels">GRE</a> or <a href="#ipsec-tunnels">IPsec tunnels</a> (from existing router/firewall), <a href="#cloudflare-one-appliance">Cloudflare One Appliance</a> (zero-touch deployment), or <a href="#cloudflare-mesh">Cloudflare Mesh</a> (requires a Linux host)</td>
</tr>
<tr>
<td>Connect a branch office using existing routers</td>
<td><a href="#gre-tunnels">GRE</a> or <a href="#ipsec-tunnels">IPsec tunnels</a></td>
</tr>
<tr>
<td>Encrypt traffic over the public Internet</td>
<td><a href="#ipsec-tunnels">IPsec tunnels</a></td>
</tr>
<tr>
<td>Zero-touch branch office deployment</td>
<td><a href="#cloudflare-one-appliance">Cloudflare One Appliance</a></td>
</tr>
<tr>
<td>Connect cloud VPCs (AWS, Azure, GCP) with minimal configuration</td>
<td><a href="#multi-cloud-networking">Multi-Cloud Networking</a></td>
</tr>
<tr>
<td>Bypass the public Internet entirely</td>
<td><a href="#cloudflare-network-interconnect-cni">Cloudflare Network Interconnect</a></td>
</tr>
<tr>
<td>High-throughput enterprise connectivity</td>
<td><a href="#cloudflare-one-appliance">Cloudflare One Appliance</a> or <a href="#cloudflare-network-interconnect-cni">CNI</a></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4473.md")
</aside>
<h3 id="cloudflare-one-recommendations-by-team">Cloudflare One recommendations by team</h3>
<p>The team driving your Cloudflare One connectivity project influences which option provides the smoothest adoption path. The following table provides examples.</p>
<p><strong>Table 5. Cloudflare One connectivity recommendations for teams</strong></p>
<table>
<thead>
<tr>
<th>Primary team</th>
<th>Recommended starting point</th>
<th>Rationale</th>
</tr>
</thead>
<tbody>
<tr>
<td>Security / InfoSec</td>
<td><a href="#cloudflare-tunnel">Cloudflare Tunnel</a> + <a href="#cloudflare-one-client">Cloudflare One Client</a></td>
<td>Minimal network infrastructure changes required. Security controls are managed within the Cloudflare One dashboard.</td>
</tr>
<tr>
<td>Network Operations</td>
<td><a href="#ipsec-tunnels">Cloudflare WAN</a> (IPsec/GRE) or <a href="#cloudflare-one-appliance">Cloudflare One Appliance</a></td>
<td>Familiar routing and tunnel configuration. Integrates with existing network equipment and workflows.</td>
</tr>
<tr>
<td>DevOps / Platform Engineering</td>
<td><a href="#cloudflare-mesh">Cloudflare Mesh</a> or <a href="#cloudflare-tunnel">Cloudflare Tunnel</a></td>
<td>Software-defined deployment. Scriptable via API. No hardware dependencies.</td>
</tr>
<tr>
<td>Facilities / Branch IT</td>
<td><a href="#cloudflare-one-appliance">Cloudflare One Appliance</a></td>
<td>Zero-touch deployment with centralized management. No on-site networking expertise required.</td>
</tr>
</tbody>
</table>
<h3 id="cloudflare-mesh-and-cloudflare-one-appliance-comparison">Cloudflare Mesh and Cloudflare One Appliance comparison</h3>
<p>Cloudflare Mesh and Cloudflare One Appliance both provide site-level connectivity, but serve different deployment scenarios.</p>
<table>
<thead>
<tr>
<th>Aspect</th>
<th>Cloudflare Mesh</th>
<th>Cloudflare One Appliance</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Protocol</strong></td>
<td>MASQUE</td>
<td>IPsec</td>
</tr>
<tr>
<td><strong>Deployment model</strong></td>
<td>Software on Linux host (can run alongside other workloads)</td>
<td>Dedicated hardware appliance or virtual machine</td>
</tr>
<tr>
<td><strong>Best for</strong></td>
<td>Cloud VPCs, development environments, smaller deployments with an available Linux host</td>
<td>Enterprise branch offices, data centers, sites requiring high throughput (1 Gbps+)</td>
</tr>
<tr>
<td><strong>Platform support</strong></td>
<td>Linux only (x86_64, ARM64). Currently in beta.</td>
<td>Hardware appliance (Dell VEP1460) or virtual (VMware ESXi, Proxmox)</td>
</tr>
<tr>
<td><strong>High availability</strong></td>
<td><a href="/mesh/features/high-availability/">Active-passive replicas</a> for nodes with routes</td>
<td>Supported through multiple connectors per site</td>
</tr>
<tr>
<td><strong>Management</strong></td>
<td>Configured as a device in the Cloudflare One Client settings</td>
<td>Centralized through the Cloudflare WAN dashboard with zero-touch provisioning</td>
</tr>
</tbody>
</table>
<p>Use Cloudflare Mesh when you need lightweight, software-only connectivity for cloud workloads or sites where a Linux host is available. Use Cloudflare One Appliance when you need enterprise-grade throughput, high availability, or integration with existing network infrastructure.</p>
<hr />
<h2 id="combine-cloudflare-one-connectivity-options">Combine Cloudflare One connectivity options</h2>
<p>Most enterprise Cloudflare One deployments use multiple connectivity options together. This section covers compatibility considerations and common deployment patterns.</p>
<h3 id="cloudflare-one-connectivity-compatibility-matrix">Cloudflare One connectivity compatibility matrix</h3>
<p>Not all Cloudflare One connectivity options work together in the same account. Review the following compatibility information before designing your deployment.</p>
<p><strong>Table 7. Cloudflare One connectivity compatibility</strong></p>
<table>
<thead>
<tr>
<th>Combination</th>
<th>Compatible</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Mesh + Cloudflare WAN</td>
<td>Conditional</td>
<td>Requires <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Cloudflare One Unified Routing</a>. Accounts on Legacy routing mode cannot use both.</td>
</tr>
<tr>
<td>Cloudflare One Client + Cloudflare WAN</td>
<td>Yes</td>
<td>Cloudflare One Client users can access Cloudflare WAN-connected sites. Cloudflare WAN sites can also initiate connections to Cloudflare One Client devices using their virtual IP addresses.</td>
</tr>
<tr>
<td>Cloudflare Tunnel + Cloudflare WAN</td>
<td>Yes</td>
<td>Avoid overlapping IP routes. Cloudflare Tunnel takes priority if the same CIDR is configured for both.</td>
</tr>
<tr>
<td>GRE + IPsec</td>
<td>Yes</td>
<td>Use for redundancy or migration scenarios.</td>
</tr>
<tr>
<td>CNI + GRE or IPsec</td>
<td>Yes</td>
<td>Use Internet-based GRE or IPsec tunnels as backup connectivity alongside CNI.</td>
</tr>
<tr>
<td>Cloudflare One Client + Cloudflare Tunnel + Cloudflare Mesh</td>
<td>Yes</td>
<td>Common pattern for remote access to private applications. All three work together.</td>
</tr>
<tr>
<td>CNI + Cloudflare Tunnel</td>
<td>Conditional</td>
<td><code>cloudflared</code> connects to multiple Cloudflare regions for redundancy. If CNI only advertises one region, the tunnel operates with reduced redundancy. Evaluate whether Cloudflare Tunnel is necessary if CNI already provides private connectivity.</td>
</tr>
</tbody>
</table>
<h3 id="cloudflare-one-routing-considerations">Cloudflare One routing considerations</h3>
<p>When using multiple Cloudflare One connectivity options, follow these guidelines to avoid routing conflicts:</p>
<ul>
<li><strong>Avoid overlapping CIDR ranges</strong>: Do not configure the same IP range for multiple tunnel types. If an overlap exists, Cloudflare Tunnel takes priority over Cloudflare WAN routes.</li>
<li><strong>No automatic failover</strong>: Cloudflare does not automatically fail over traffic between different connectivity options. Plan your routing to handle failures within each tunnel type.</li>
<li><strong>Virtual Networks</strong>: Use <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">Virtual Networks</a> to handle overlapping private IP ranges from different environments (for example, multiple cloud VPCs using <code>10.0.0.0/8</code>).</li>
</ul>
<h3 id="cloudflare-one-mtu-planning">Cloudflare One MTU planning</h3>
<p>When layering Cloudflare One tunnels or using multiple encapsulation methods, account for overhead to prevent fragmentation.</p>
<p><strong>Table 8. Effective MTU values for Cloudflare One tunnel types</strong></p>
<table>
<thead>
<tr>
<th>Scenario</th>
<th>Effective MTU</th>
<th>MSS clamping</th>
</tr>
</thead>
<tbody>
<tr>
<td>GRE tunnel</td>
<td>1,476 bytes</td>
<td>1,436 bytes or lower</td>
</tr>
<tr>
<td>IPsec tunnel</td>
<td>1,400-1,436 bytes (varies by encryption)</td>
<td>1,360-1,396 bytes</td>
</tr>
<tr>
<td>Cloudflare One Client behind Cloudflare WAN (double encapsulation)</td>
<td>~1,300 bytes</td>
<td>Configure based on testing</td>
</tr>
<tr>
<td>Cloudflare Mesh to Cloudflare One Client</td>
<td>~1,280 bytes</td>
<td>Configure based on testing. Traffic is encapsulated twice: by Cloudflare Mesh and again by Cloudflare before delivery to the Cloudflare One Client.</td>
</tr>
</tbody>
</table>
<p>Configure MSS clamping on your edge devices to ensure TCP traffic does not require fragmentation.</p>
<h3 id="cloudflare-one-source-ip-preservation">Cloudflare One source IP preservation</h3>
<p>Cloudflare One connectivity options handle source IP addresses differently. The following table shows how each Cloudflare One connectivity option handles source IP addresses.</p>
<p><strong>Table 9. Cloudflare One source IP behavior</strong></p>
<table>
<thead>
<tr>
<th>Connectivity option</th>
<th>Source IP behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Tunnel</td>
<td>Origin sees the <code>cloudflared</code> process IP. Use <code>CF-Connecting-IP</code> header for HTTP traffic.</td>
</tr>
<tr>
<td>Cloudflare Mesh</td>
<td>Preserves original source IP end-to-end.</td>
</tr>
<tr>
<td>GRE and IPsec tunnels</td>
<td>Preserves original source IP within the tunnel.</td>
</tr>
<tr>
<td>Cloudflare One Appliance</td>
<td>Preserves original source IP within the tunnel.</td>
</tr>
</tbody>
</table>
<p>Source IP preservation is required for:</p>
<ul>
<li>VoIP and SIP protocols that embed IP addresses in signaling</li>
<li>Audit logging that requires client IP visibility</li>
<li>Applications that make authorization decisions based on source IP</li>
</ul>
<h3 id="cloudflare-one-traffic-direction-capabilities">Cloudflare One Traffic direction capabilities</h3>
<p>The following table shows traffic direction support for each Cloudflare One connectivity option.</p>
<p><strong>Table 10. Cloudflare One connectivity traffic direction support</strong></p>
<table>
<thead>
<tr>
<th>Connectivity option</th>
<th>Client-initiated traffic</th>
<th>Server-initiated traffic</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Tunnel</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>Cloudflare One Client</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Cloudflare Mesh</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>GRE and IPsec tunnels</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Cloudflare One Appliance</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>CNI</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<p>If your application requires server-initiated connections (for example, VoIP callbacks, database replication), use a bidirectional connectivity option such as Cloudflare One Client, Cloudflare Mesh, Cloudflare WAN (IPsec/GRE), or CNI. Cloudflare Tunnel does not support server-initiated traffic.</p>
<hr />
<h2 id="common-cloudflare-one-deployment-patterns">Common Cloudflare One deployment patterns</h2>
<p>The following patterns illustrate how organizations combine Cloudflare One connectivity options for different scenarios.</p>
<h3 id="enterprise-with-remote-workers-and-branch-offices">Enterprise with remote workers and branch offices</h3>
<p>This pattern serves organizations with a distributed workforce and multiple physical locations.</p>
<p><strong>Components:</strong></p>
<ul>
<li><strong>Cloudflare One Client</strong> for remote employees, providing secure access from any location</li>
<li><strong>IPsec tunnels</strong> (via Cloudflare WAN) for branch offices with existing network infrastructure</li>
<li><strong>Cloudflare Tunnel</strong> for specific internal applications that need clientless browser access</li>
</ul>
<p><strong>Traffic flow:</strong></p>
<ol>
<li>Remote employees connect through the Cloudflare One Client, which on-ramps their traffic to Cloudflare.</li>
<li>Gateway policies inspect and filter traffic based on user identity and device posture.</li>
<li>Traffic destined for branch office resources routes through IPsec tunnels to Cloudflare WAN-connected sites.</li>
<li>Traffic destined for specific applications routes through Cloudflare Tunnel to origin servers.</li>
</ol>
<h3 id="cloud-first-organization">Cloud-first organization</h3>
<p>This pattern serves organizations with primarily cloud-based infrastructure and minimal on-premises equipment.</p>
<p><strong>Components:</strong></p>
<ul>
<li><strong>Multi-Cloud Networking</strong> for cloud VPCs (AWS, GCP, Azure), automating IPsec tunnel creation to Cloudflare WAN</li>
<li><strong>Cloudflare Tunnel</strong> for Kubernetes services and containerized applications</li>
<li><strong>Cloudflare One Client</strong> for employee devices</li>
</ul>
<p><strong>Traffic flow:</strong></p>
<ol>
<li>Multi-Cloud Networking automatically creates IPsec tunnels between cloud VPCs and Cloudflare WAN.</li>
<li>Cloudflare Tunnel provides ingress for external-facing applications.</li>
<li>Employees access cloud resources through the Cloudflare One Client.</li>
</ol>
<p><strong>Alternative:</strong> For organizations not using Cloudflare WAN, Cloudflare Mesh can provide bidirectional connectivity for cloud VPCs. Note that accounts on Legacy routing mode cannot use Cloudflare Mesh and Cloudflare WAN together.</p>
<h3 id="highly-regulated-enterprise">Highly regulated enterprise</h3>
<p>This pattern serves organizations with strict compliance requirements that prohibit traffic from traversing the public Internet.</p>
<p><strong>Components:</strong></p>
<ul>
<li><strong>Cloudflare Network Interconnect (CNI)</strong> for primary connectivity from data centers</li>
<li><strong>IPsec tunnels</strong> as backup connectivity in case of CNI issues</li>
<li><strong>Cloudflare One Client</strong> for remote employees</li>
</ul>
<p><strong>Traffic flow:</strong></p>
<ol>
<li>Data center traffic routes through CNI, never touching the public Internet.</li>
<li>IPsec tunnels provide backup connectivity if CNI experiences issues.</li>
<li>Remote employees connect through the Cloudflare One Client over the public Internet (encrypted).</li>
<li>Gateway policies enforce compliance rules on all traffic regardless of connectivity method.</li>
</ol>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/reference-architecture/architectures/sase/">SASE reference architecture</a> - Guide to deploying Cloudflare One</li>
<li><a href="/cloudflare-wan/wan-transformation/">WAN transformation</a> - Plan your migration from legacy WAN to Cloudflare One</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a></li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a></li>
<li><a href="/mesh/">Cloudflare Mesh</a></li>
<li><a href="/cloudflare-wan/">Cloudflare WAN</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/on-ramps/">WAN Connectors on-ramps</a> - Full list of supported on-ramps</li>
<li><a href="/multi-cloud-networking/">Multi-Cloud Networking</a> - Automate cloud VPC connectivity</li>
<li><a href="/magic-transit/">Magic Transit</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliances/">Cloudflare One Appliance</a></li>
<li><a href="/network-interconnect/">Cloudflare Network Interconnect</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">Virtual Networks</a></li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">DNS locations</a> - Filter DNS traffic without device agents</li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">Proxy endpoints</a> - Filter web traffic using PAC files</li>
<li><a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">Clientless Web Isolation</a> - Secure web access without device agents</li>
</ul>
<p>For implementation guidance on combining Cloudflare One connectivity options, refer to the <a href="/reference-architecture/architectures/sase/">SASE reference architecture</a>.</p>
