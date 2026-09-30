---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/best-practices/
  description: Recommended practices for reliable Cloudflare Mesh deployments.
  full_title: Best practices · Cloudflare One docs
  head_html: <title>Best practices · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Recommended practices for reliable Cloudflare Mesh deployments."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/best-practices/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/best-practices/index.md"><meta property="og:title" content="Best practices · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Recommended practices for reliable Cloudflare Mesh deployments."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/best-practices/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Mesh"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/best-practices/#page","headline":"Best practices \u00b7 Cloudflare One docs","description":"Recommended practices for reliable Cloudflare Mesh deployments.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/best-practices/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-mesh/best-practices/
  schema: 1
---
<p>Operational guidance for managing Cloudflare Mesh deployments — updating the client, configuring cloud providers, running alongside Cloudflare Tunnel, and common troubleshooting.</p>
<h2 id="update-a-mesh-node">Update a Mesh node</h2>
<p>Updating a Mesh node means updating the <code>cloudflare-warp</code> package on the Linux host. The node briefly disconnects during the update, which interrupts traffic routed through it. If you have <a href="/mesh/features/high-availability/">high availability</a> enabled, traffic fails over to a standby replica automatically.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5254.md")
</div></div>
<ol start="3">
<li>Verify the node has reconnected:</li>
</ol>
<pre tabindex="0"><code class="language-sh">warp-cli status&#10;</code></pre>
<p>You should see <code>Status update: Connected</code> in the output.</p>
<h2 id="make-ip-forwarding-persistent">Make IP forwarding persistent</h2>
<p>IP forwarding allows a Mesh node to act as a gateway, forwarding packets between its network interface and the Cloudflare network. This is only required if the node advertises <a href="/mesh/features/routes/">CIDR routes</a> — if you are only reaching the node by its Mesh IP, forwarding is not needed.</p>
<p>Older installations may have used <code>sysctl -w</code> for IP forwarding, which does not persist across reboots. If your node loses route connectivity after a server restart, run the following to make forwarding permanent:</p>
<pre tabindex="0"><code class="language-sh">printf &#x27;net.ipv4.ip_forward = 1\nnet.ipv6.conf.all.forwarding = 1\nnet.ipv6.conf.all.accept_ra = 2\n&#x27; | sudo tee /etc/sysctl.d/99-zzz-cloudflare-warp-connector.conf &amp;&amp; sudo sysctl --system&#10;</code></pre>
<p>You can verify the settings are active with:</p>
<pre tabindex="0"><code class="language-sh">sysctl net.ipv4.ip_forward net.ipv6.conf.all.forwarding net.ipv6.conf.all.accept_ra&#10;</code></pre>
<p>New installations include this step automatically.</p>
<h2 id="cloud-vpc-deployments">Cloud VPC deployments</h2>
<p>When deploying Mesh nodes in a cloud VPC, you may need to configure additional provider settings so the node can forward traffic for other devices on the subnet.</p>
<h3 id="google-cloud-platform-gcp">Google Cloud Platform (GCP)</h3>
<p><a href="https://cloud.google.com/vpc/docs/using-routes#canipforward">Enable IP forwarding</a> on the VM instance where you installed the Mesh node.</p>
<h3 id="amazon-web-services-aws">Amazon Web Services (AWS)</h3>
<ul>
<li>Disable <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html">source/destination checking</a> on the EC2 instance.</li>
<li>In your <a href="https://docs.aws.amazon.com/vpc/latest/userguide/subnet-route-tables.html">subnet route table</a>, add a route for Mesh traffic (for example, <code>100.96.0.0/12</code>) pointing to the EC2 instance.</li>
</ul>
<h3 id="microsoft-azure">Microsoft Azure</h3>
<ul>
<li><a href="https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-network-interface?tabs=azure-portal#enable-or-disable-ip-forwarding">Enable IP forwarding</a> on the network interface of the VM.</li>
<li>Add a <a href="https://learn.microsoft.com/en-us/azure/virtual-network/manage-route-table">user-defined route</a> for Mesh traffic pointing to the VM's private IP.</li>
</ul>
<h2 id="running-mesh-on-a-dns-server">Running Mesh on a DNS server</h2>
<p>Mesh nodes run in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/">Traffic and DNS mode</a>, which redirects DNS queries on the host to Cloudflare Gateway. This will conflict with DNS services running on the same machine (for example, Active Directory DNS, Pi-hole, Unbound, BIND, or dnsmasq).</p>
<p>If your server runs a DNS service, do not install the Mesh node on that host. Instead, install the node on a separate machine on the same subnet and use <a href="/mesh/features/routes/">CIDR routes</a> to make the DNS server reachable.</p>
<h2 id="running-mesh-alongside-other-vpn-or-mesh-software">Running Mesh alongside other VPN or mesh software</h2>
<p>The Cloudflare One Client creates a virtual network interface and manages the system routing table. Other software that does the same — Tailscale, WireGuard, OpenVPN, Cisco AnyConnect, GlobalProtect, ZScaler, Netskope, or any traditional VPN client — will compete for control of routing. Running them simultaneously causes unpredictable behavior: traffic may flow through the wrong tunnel or fail entirely.</p>
<p>If you are migrating to Cloudflare Mesh from another solution:</p>
<ol>
<li>Uninstall or disable the other client (for example, <code>sudo systemctl stop tailscaled &amp;&amp; sudo systemctl disable tailscaled</code> on Linux, or quit the application from the system tray on macOS/Windows).</li>
<li>Restart the machine so the Cloudflare One Client's virtual network interface takes priority in the routing table.</li>
<li>Verify connectivity by running <code>warp-cli status</code> and pinging a Mesh IP.</li>
</ol>
<p>This applies to both Mesh nodes and client devices.</p>
<h2 id="running-mesh-with-cloudflare-tunnel">Running Mesh with Cloudflare Tunnel</h2>
<p>A Mesh node (<code>warp-cli</code>) and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> (<code>cloudflared</code>) can run on the same Linux host. This is useful when you want to use the Mesh node as a gateway for your private network while also using Cloudflare Tunnel to publish specific applications.</p>
<p>The Mesh node captures outbound traffic and routes it through Cloudflare, which can prevent <code>cloudflared</code> from making its required outbound connections. To resolve this, use <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a> to exclude the hostnames and IPs listed in <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/#required-for-tunnel-operation">Tunnel with firewall</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5251.md")
</aside>
<h2 id="routing-between-mesh-and-cloudflare-wan">Routing between Mesh and Cloudflare WAN</h2>
<p>To route traffic between Cloudflare Mesh and <a href="/cloudflare-wan/">Cloudflare WAN</a> (for example, reaching a Mesh node from a WAN-connected site or vice versa), your account must be on <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing mode (beta)</a>. Unified Routing uses a single routing fabric for all connection types (Cloudflare One Client, Cloudflare Tunnel, IPsec, GRE, CNI). Without it, Mesh and WAN connections cannot exchange traffic.</p>
<h2 id="connect-workers-to-mesh">Connect Workers to Mesh</h2>
<p>Cloudflare Workers can connect to your Mesh network using <a href="/workers-vpc/configuration/vpc-networks/">VPC Network bindings</a>. Bind to <code>cf1:network</code> to reach any Mesh node, client device, or subnet route in your account — without specifying a particular tunnel UUID.</p>
<p>The same binding also handles outbound traffic to public Internet destinations: requests egress through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>, so your existing Zero Trust traffic policies are enforced and Worker traffic appears in Gateway DNS, HTTP, and Network logs alongside the rest of your traffic.</p>
<p>For setup instructions and examples, refer to <a href="/workers-vpc/examples/connect-to-cloudflare-mesh/">Connect Workers to Cloudflare Mesh</a>.</p>
<h2 id="source-ips-for-cloudflare-services">Source IPs for Cloudflare services</h2>
<p>When Cloudflare services (such as <a href="/load-balancing/">Load Balancing</a> health checks or <a href="/workers/">Workers</a>) send traffic to your private network through a Mesh node, the traffic originates from the Cloudflare source IP range (default <code>100.64.0.0/12</code>). You may need to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/">configure Cloudflare source IPs</a> to avoid IP conflicts.</p>
<h2 id="mtu-and-packet-fragmentation">MTU and packet fragmentation</h2>
<p>Mesh nodes use encapsulation to route traffic, which adds overhead to each packet. This is especially relevant for traffic between two Mesh participants, where the packet may be encapsulated twice (once by the sending node, and again by Cloudflare before delivery to the receiving side).</p>
<p>If source devices send packets near the maximum size (1,460 bytes or more), the double encapsulation can push packets over 1,500 bytes, causing them to be dropped.</p>
<h3 id="recommendations">Recommendations</h3>
<ul>
<li>Set the MTU on source devices (servers, cameras, IoT devices) to <strong>1,280 bytes</strong> to ensure packets fit after encapsulation.</li>
<li>For TCP-only traffic, apply MSS clamping on your router with a value of <strong>1,240 bytes</strong> (1,280 MTU - 20 byte IP header - 20 byte TCP header).</li>
<li>Modern applications using <a href="https://www.cloudflare.com/learning/network-layer/what-is-mtu/">Path MTU Discovery (PMTUD)</a> typically handle this automatically.</li>
</ul>
