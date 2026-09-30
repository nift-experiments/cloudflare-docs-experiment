---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/features/routes/
  description: Configure CIDR and hostname routes to send private network traffic through Cloudflare Mesh nodes.
  full_title: Configure routes for Cloudflare Mesh · Cloudflare One docs
  head_html: <title>Configure routes for Cloudflare Mesh · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure CIDR and hostname routes to send private network traffic through Cloudflare Mesh nodes."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/features/routes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/features/routes/index.md"><meta property="og:title" content="Configure routes for Cloudflare Mesh · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure CIDR and hostname routes to send private network traffic through Cloudflare Mesh nodes."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/features/routes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Mesh"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/features/routes/#page","headline":"Configure routes for Cloudflare Mesh \u00b7 Cloudflare One docs","description":"Configure CIDR and hostname routes to send private network traffic through Cloudflare Mesh nodes.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/features/routes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-mesh/features/routes/
  schema: 1
---
<p>By default, a Mesh node is reachable only by its own <a href="/mesh/concepts/#mesh-ips">Mesh IP</a>. To make other devices on the subnet behind the node reachable — servers, databases, printers, IoT devices that cannot run the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> — add a route to the node. A Mesh node supports two types of routes:</p>
<ul>
<li><strong>CIDR routes</strong> — forward traffic for an IP range — private (for example, <code>10.0.0.0/24</code>) or public — through the node.</li>
<li><strong>Hostname routes</strong> — attract traffic for a hostname to the node instead of an IP. This works for a <strong>private</strong> hostname (for example, <code>wiki.internal.local</code>), which is useful when the application has an unknown or ephemeral IP, as well as a <strong>public</strong> hostname (for example, <code>www.example.com</code>), which routes that hostname's traffic through the node and egresses via the node's public IP.</li>
</ul>
<p>When you add a route, the Mesh node acts as a gateway: traffic destined for the advertised CIDR or hostname is forwarded to the node, which delivers it to the appropriate host on the local network (or egresses it to the public Internet).</p>
<p>Both IPv4 and IPv6 CIDR routes are supported. IPv6 routes require that the Mesh node's <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> is configured to use <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">MASQUE</a>; they will not work if the device profile uses WireGuard instead.</p>
<h2 id="when-to-use-routes">When to use routes</h2>
<ul>
<li><strong>Without routes</strong> — Devices on your Mesh can only reach the node itself by its Mesh IP. Services running directly on the node are reachable this way.</li>
<li><strong>With routes</strong> — Devices on your Mesh can reach any host on the subnet behind the node. Use this when you have infrastructure that cannot run the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>.</li>
</ul>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;  subgraph subnet[&quot;Subnet 10.0.0.0/24&quot;]&#10;    node[&quot;Mesh node &lt;br&gt; 10.0.0.1&quot;]&#10;    db[&quot;Database &lt;br&gt; 10.0.0.50&quot;]&#10;    printer[&quot;Printer &lt;br&gt; 10.0.0.100&quot;]&#10;  end&#10;  client[&quot;Client device &lt;br&gt; 100.96.0.10&quot;] --&gt; CF((Cloudflare)) --&gt; node&#10;  node --&gt; db&#10;  node --&gt; printer&#10;</code></pre>
<h2 id="manage-cidr-routes">Manage CIDR routes</h2>
<p>Use CIDR routes to forward traffic from your mesh node to devices on your local network.</p>
<h3 id="add-a-route">Add a route</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5213.md")
</div></div>
<h3 id="edit-a-route">Edit a route</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5216.md")
</div></div>
<h3 id="delete-a-route">Delete a route</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5219.md")
</div></div>
<h2 id="configure-split-tunnels">Configure Split Tunnels</h2>
<p>For traffic to reach your advertised CIDR, the range must route through Cloudflare on both the Mesh node and client devices.</p>
<h3 id="on-the-mesh-node">On the Mesh node</h3>
<p>In your Mesh node's device profile, ensure the advertised CIDR routes through Cloudflare:</p>
<ul>
<li><strong>Include mode</strong> (recommended for Mesh nodes): Add the CIDR to your include list.</li>
<li><strong>Exclude mode</strong>: Remove the CIDR (or its parent range) from your exclude list.</li>
</ul>
<p>For example, if you are advertising <code>10.0.0.0/24</code> and your Split Tunnels exclude list contains <code>10.0.0.0/8</code>, you need to remove <code>10.0.0.0/8</code> and re-add the portions of the <code>10.0.0.0/8</code> range that you do not want to route through Cloudflare.</p>
<h3 id="on-client-devices">On client devices</h3>
<p>Repeat the same Split Tunnel configuration on the device profiles used by your client devices, ensuring the advertised CIDR routes through Cloudflare.</p>
<h2 id="return-traffic-routing">Return traffic routing</h2>
<p>The Mesh node forwards inbound traffic from Cloudflare to devices on the subnet. However, for <strong>return traffic</strong> (responses from subnet devices back to Mesh clients), the subnet devices need a route back to the Mesh node.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;  client[&quot;Client device &lt;br&gt; 100.96.0.10&quot;] -- request --&gt; CF((Cloudflare)) -- request --&gt; node[&quot;Mesh node &lt;br&gt; 10.0.0.1&quot;]&#10;  node --&gt; db[&quot;Database &lt;br&gt; 10.0.0.50&quot;]&#10;  db -. &quot;response: &lt;br&gt; needs route to node&quot; .-&gt; node -. response .-&gt; CF -. response .-&gt; client&#10;</code></pre>
<p>How you configure this depends on where the Mesh node is installed:</p>
<h3 id="option-1-mesh-node-is-the-default-gateway">Option 1: Mesh node is the default gateway</h3>
<p>If the Mesh node is the subnet's default gateway (or is installed on the router), no additional configuration is needed. All traffic from subnet devices naturally routes through the node.</p>
<h3 id="option-2-mesh-node-is-not-the-default-gateway">Option 2: Mesh node is not the default gateway</h3>
<p>If the Mesh node is a regular host on the subnet, configure the subnet's router to send Mesh traffic through the node. Add a static route:</p>
<ul>
<li><strong>Destination</strong>: <code>100.96.0.0/12</code> (Mesh IP range)</li>
<li><strong>Next hop</strong>: The Mesh node's local subnet IP (for example, <code>10.0.0.1</code>)</li>
</ul>
<p>This ensures that responses to Mesh clients are forwarded to the Mesh node for delivery through Cloudflare.</p>
<h2 id="site-to-site-routing">Site-to-site routing</h2>
<p>When you have Mesh nodes at multiple sites, devices on one subnet can reach devices on another subnet through Cloudflare.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart TD&#10;  subgraph siteA[&quot;Site A — 10.0.0.0/24&quot;]&#10;    serverA[&quot;Server &lt;br&gt; 10.0.0.50&quot;] --- nodeA[&quot;Mesh node &lt;br&gt; 10.0.0.1&quot;]&#10;  end&#10;  subgraph siteB[&quot;Site B — 192.168.1.0/24&quot;]&#10;    serverB[&quot;Server &lt;br&gt; 192.168.1.50&quot;] --- nodeB[&quot;Mesh node &lt;br&gt; 192.168.1.1&quot;]&#10;  end&#10;  nodeA &lt;--&gt; CF((Cloudflare))&#10;  nodeB &lt;--&gt; CF&#10;</code></pre>
<p>For this to work:</p>
<ol>
<li>Each Mesh node must advertise the local subnet as a <a href="#add-a-route">CIDR route</a> so Cloudflare knows which node to forward traffic to.</li>
<li>The remote subnet CIDRs must route through Cloudflare on each node. In your Mesh node's <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel</a> configuration, add the remote site's CIDR to the include list (or remove it from the exclude list).</li>
<li>Each site's router needs static routes pointing remote subnets to the local Mesh node:</li>
</ol>
<p><strong>Site A router:</strong></p>
<ul>
<li><strong>Destination</strong>: <code>192.168.1.0/24</code> → <strong>Next hop</strong>: <code>10.0.0.1</code> (local Mesh node)</li>
<li><strong>Destination</strong>: <code>100.96.0.0/12</code> → <strong>Next hop</strong>: <code>10.0.0.1</code></li>
</ul>
<p><strong>Site B router:</strong></p>
<ul>
<li><strong>Destination</strong>: <code>10.0.0.0/24</code> → <strong>Next hop</strong>: <code>192.168.1.1</code> (local Mesh node)</li>
<li><strong>Destination</strong>: <code>100.96.0.0/12</code> → <strong>Next hop</strong>: <code>192.168.1.1</code></li>
</ul>
<p>For production site-to-site deployments, consider enabling <a href="/mesh/features/high-availability/">high availability</a> on each node. HA provides failover for the CIDR routes advertised by a node — if the active replica goes down, Cloudflare promotes a standby so traffic to the subnet continues to flow.</p>
<h2 id="dns-filtering">DNS filtering</h2>
<p>To filter DNS queries from the subnet using <a href="/cloudflare-one/traffic-policies/dns-policies/">Cloudflare Gateway</a>:</p>
<ol>
<li>
<p><strong>Configure DNS on your router</strong>: Point your router's DNS to the Gateway resolver IPs:</p>
<ul>
<li><code>172.64.36.1</code></li>
<li><code>172.64.36.2</code></li>
</ul>
</li>
<li>
<p><strong>Add IP routes to your router</strong>: On your router, add static routes pointing the Gateway resolver IPs to your Mesh node's local IP. This allows DNS traffic to reach Cloudflare through the node.</p>
<ul>
<li><strong>Destination</strong>: <code>172.64.36.1</code> → <strong>Next hop</strong>: <code>10.0.0.1</code> (local Mesh node)</li>
<li><strong>Destination</strong>: <code>172.64.36.2</code> → <strong>Next hop</strong>: <code>10.0.0.1</code></li>
</ul>
</li>
<li>
<p><strong>Configure Split Tunnels</strong>: Ensure the following IPs route through the Mesh node in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a> configuration:</p>
<ul>
<li>The subnet's internal DNS resolver IP</li>
<li>Gateway initial resolved IP range: <code>172.64.128.0/20</code> (IPv4) and <code>2606:4700:0cf1:4000::/64</code> (IPv6)</li>
</ul>
</li>
</ol>
<p>Gateway logs DNS queries with the private source IP of the originating device. You can use this to create <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a> for internal DNS records.</p>
<h2 id="hostname-routes">Hostname routes</h2>
<p>Instead of advertising an IP range, you can attract traffic for a specific hostname to a Mesh node. When a user requests the hostname, Cloudflare Gateway assigns an <span class="nb-glossary-tooltip" title="initial resolved IP">initial resolved IP</span> and routes the traffic through the node.</p>
<ul>
<li><strong>Private hostname</strong> (for example, <code>wiki.internal.local</code>) — the node delivers the traffic to the application's private IP on the local network. Useful when the application has an unknown or ephemeral IP.</li>
<li><strong>Public hostname</strong> (for example, <code>www.example.com</code>) — the node egresses the traffic to the public Internet using its own public IP. This lets you use a Mesh node as a dedicated egress for that hostname.</li>
</ul>
<p>Hostname routes replace <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">virtual networks</a> as the way to reach resources: because a hostname is globally unique, <strong>overlapping hostnames are not supported</strong> and a hostname can only be routed to one node or tunnel at a time.</p>
<div class="nb-interactive-component" data-cf-component="MeshHostnameRoutingDiagram"></div>
<p>For a deeper look at the packet flow behind hostname routing, refer to the <a href="https://blog.cloudflare.com/tunnel-hostname-routing/">announcement blog post</a>.</p>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li><strong>Run a supported Mesh node version.</strong> Hostname routing requires the Mesh node to run Linux Cloudflare One Client version <code>2026.6.822.0</code> or newer.</li>
<li><strong>Configure the Mesh node's <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> to use <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">MASQUE</a>.</strong> Hostname routing does not work if the device profile uses WireGuard instead.</li>
<li><strong>Enable the Gateway proxy</strong> with TCP, UDP, and ICMP:</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5223.md")
</div></div>
<p>Cloudflare will now proxy traffic from enrolled devices, except for the traffic excluded in your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/#3-route-private-network-ips-through-the-cloudflare-one-client">split tunnel settings</a>. For more information on how Gateway forwards traffic, refer to <a href="/cloudflare-one/traffic-policies/proxy/">Gateway proxy</a>.</p>
<ul>
<li><strong>Route the following IPv4 ranges through Cloudflare</strong> in the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel</a> configuration of <strong>both</strong> the Mesh node's device profile <strong>and</strong> your client device profiles. In Include mode, add each range. In Exclude mode, ensure none of them (or their parent ranges) are excluded.</li>
</ul>
<table>
<thead>
<tr>
<th>Purpose</th>
<th>IPv4</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mesh device IP range</td>
<td><code>100.96.0.0/12</code></td>
</tr>
<tr>
<td>Cloudflare source IP range</td>
<td><code>100.64.0.0/12</code></td>
</tr>
</tbody>
</table>
<p>The hostname routing (token IP) range (<code>172.64.128.0/20</code>) and all Cloudflare One IPv6 ranges are <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges">automatically routed through Cloudflare</a> and do not need to be added manually.</p>
<ul>
<li><strong>Remove the hostname's top-level domain from <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a></strong> on client devices, so the DNS query is sent to Cloudflare Gateway for resolution.</li>
</ul>
<h3 id="add-a-hostname-route">Add a hostname route</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5227.md")
</div></div>
<h3 id="configure-dns-resolution">Configure DNS resolution</h3>
<p>For a <strong>private</strong> hostname, Gateway must be able to resolve the hostname to its private IP. How you configure this depends on whether DNS resolution and application traffic use the <strong>same</strong> connector or <strong>different</strong> connectors.</p>
<h4 id="the-node-resolves-the-hostname-default">The node resolves the hostname (default)</h4>
<p>By default, the Mesh node resolves the hostname using the DNS resolver configured on its host machine (for example, in <code>/etc/resolv.conf</code> on Linux) — the same way <code>cloudflared</code> does. If the node can already resolve the hostname to its private IP through that resolver, no further configuration is required.</p>
<p>If the node cannot resolve the hostname on its own, the simplest option is to add an entry to the node's hosts file (for example, <code>/etc/hosts</code> on Linux) mapping the hostname to its private IP. Unlike a Cloudflare Tunnel, a Mesh node does <strong>not</strong> require you to run a dedicated DNS server:</p>
<pre tabindex="0"><code class="language-txt">10.0.0.50 wiki.internal.local&#10;</code></pre>
<h4 id="split-dns-dns-and-application-traffic-use-different-connectors">Split DNS: DNS and application traffic use different connectors</h4>
<p>You only need a Gateway <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policy</a> when the DNS query must be sent to a <strong>different</strong> connector than the application traffic — for example, the internal DNS server sits behind one Mesh node or Cloudflare Tunnel, while the application is reached through another. In that case:</p>
<ol>
<li>Add a <a href="#add-a-route">CIDR route</a> for the DNS server's IP so Gateway can reach it through the connector where the DNS server lives (a Mesh node or a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>).</li>
<li>Create a <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policy</a> that sends DNS queries for the hostname (or its domain) to that internal DNS server.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="where-to-run-the-dns-server">Where to run the DNS server</h3>
@markup("md", "content/.markup/bodies/5210.md")
</aside>
<p>For a <strong>public</strong> hostname, the Mesh node handles resolution: Gateway sends the DNS query to the node, the node resolves it through its upstream DNS provider, and then routes the packet to the destination and egresses using its own public IP. No internal DNS server or resolver policy is required.</p>
<h3 id="secure-hostname-traffic">Secure hostname traffic</h3>
<p>After adding a hostname route, secure it with either an <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Access self-hosted application</a> or <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a>. For details and examples, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/#3-recommended-filter-network-traffic-with-gateway">Connect a private hostname</a>.</p>
<h3 id="limitations">Limitations</h3>
<p>Starting with <a href="https://developer.chrome.com/release-notes/142">Chrome 142</a>, Local Network Access (LNA) restricts requests from websites to local IP addresses. LNA is implemented at the Chromium engine level, so this affects all Chromium-based browsers (for example, Microsoft Edge, Brave, and Opera), not only Google Chrome. This can affect accounts whose Gateway <span class="nb-glossary-tooltip" title="initial resolved IP">initial resolved IP</span> range is still drawn from Carrier-Grade NAT (CGNAT) address space (<code>100.64.0.0/10</code>) — for example, the legacy default range <code>100.80.0.0/16</code>, or a custom range configured within CGNAT space. These browsers categorize such addresses as belonging to a local network. When a website loaded from a public IP makes subrequests to a domain resolved through an initial resolved IP in this space, the browser treats this as a public-to-local network request and displays a prompt asking the user to allow access to devices on the local network. The browser blocks requests to these domains until the user accepts this prompt.</p>
<p>This commonly occurs when an Egress policy matches broadly used domains (such as <code>cloudfront.net</code> or <code>github.com</code>), causing subrequests from public pages to resolve into CGNAT space.</p>
<p>Accounts using the current default initial resolved IP range (<code>172.64.128.0/20</code>) are not affected, because this range is public Cloudflare address space rather than CGNAT. If your account was created before this default changed, or if you configured a custom CGNAT-space range, refer to <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">Configure initial resolved IPs</a> to move to a non-CGNAT range instead of relying on the following browser workarounds.</p>
<p>The workarounds below use Google Chrome Enterprise policies. If your organization manages a different Chromium-based browser, consult that browser's enterprise policy documentation for an equivalent control.</p>
<h4 id="iframes">Iframes</h4>
<p>If the affected request originates from within an iframe (for example, an application embedded in a third-party portal), the iframe must declare the <code>local-network-access</code> permission for the browser prompt to appear in the parent frame:</p>
<ul>
<li><strong>Chrome 142-144</strong>: Use the <code>allow=&quot;local-network-access&quot;</code> attribute on the iframe element.</li>
<li><strong>Chrome 145+</strong>: The permission was split into <code>allow=&quot;local-network&quot;</code> and <code>allow=&quot;loopback-network&quot;</code>.</li>
</ul>
<p>If iframes are nested, every iframe in the chain must include the appropriate attribute. Since third-party applications control their own iframe attributes, this may not be configurable by the end user.</p>
<h4 id="workarounds">Workarounds</h4>
<p>To avoid this issue, choose one of the following options:</p>
<ul>
<li><strong>Override IP address space classification (Chrome 146+)</strong>: Use the <a href="https://chromeenterprise.google/policies/#LocalNetworkAccessIpAddressSpaceOverrides"><code>LocalNetworkAccessIpAddressSpaceOverrides</code></a> Chrome Enterprise policy to reclassify your CGNAT-space initial resolved IP range (for example, <code>100.80.0.0/16</code>) as public. This is the most targeted fix because it only changes the classification for the initial resolved IP range rather than disabling security checks entirely.</li>
<li><strong>Allow specific URLs (Chrome 140+)</strong>: Use the <a href="https://chromeenterprise.google/policies/#LocalNetworkAccessAllowedForUrls"><code>LocalNetworkAccessAllowedForUrls</code></a> Chrome Enterprise policy to exempt specific websites from Local Network Access checks. Note that <code>https://*</code> is a valid entry to disable checks for all URLs.</li>
<li><strong>Allow specific URLs (Chrome 146+)</strong>: Use the <a href="https://chromeenterprise.google/policies/#LocalNetworkAllowedForUrls"><code>LocalNetworkAllowedForUrls</code></a> Chrome Enterprise policy, which replaces <code>LocalNetworkAccessAllowedForUrls</code> starting in Chrome 146.</li>
<li><strong>Opt out of Local Network Access restrictions (Chrome 142-152)</strong>: Use the <a href="https://chromeenterprise.google/policies/#LocalNetworkAccessRestrictionsTemporaryOptOut"><code>LocalNetworkAccessRestrictionsTemporaryOptOut</code></a> Chrome Enterprise policy to completely opt out of Local Network Access restrictions. This is a temporary policy and will be removed after Chrome 152.</li>
<li><strong>Disable the Chrome feature flag</strong>: Go to <code>chrome://flags</code> and set the <strong>Local Network Access Checks</strong> flag to <em>Disabled</em>. This approach is suitable for individual users but not for enterprise-wide deployment.</li>
</ul>
