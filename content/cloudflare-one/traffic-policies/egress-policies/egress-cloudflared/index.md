<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6625.md")
</div></details>
<p>Some third-party services only accept connections from specific source IPs listed in an Access Control List (ACL). If a non-Cloudflare IP (for example, an IP from your ISP or a cloud provider like AWS) is already on their allowlist, you can route traffic through a Cloudflare Tunnel so that it exits using that same IP. This is called source IP anchoring — it allows you to keep your existing egress IPs without purchasing <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">Cloudflare dedicated egress IPs</a>.</p>
<p>For example, assume your banking service at <code>app.bank.com</code> expects traffic from an AWS IP. You install <code>cloudflared</code> in your AWS environment and add a public hostname route for <code>app.bank.com</code>. When users connect to <code>app.bank.com</code> through the Cloudflare One Client, Gateway applies your network policies and routes the filtered traffic through the Cloudflare Tunnel to AWS. The traffic then exits to the public Internet using your AWS egress IP.</p>
<pre><code class="language-mermaid">    flowchart LR&#10;      subgraph aws[&quot;AWS VPC&quot;]&#10;				cloudflared[&quot;cloudflared&quot;]&#10;      end&#10;			subgraph cloudflare[Cloudflare]&#10;			  gateway[&quot;Gateway&quot;]&#10;			end&#10;			subgraph internet[Internet]&#10;				resolver[1.1.1.1]&#10;				app[Application]&#10;			end&#10;      warp[&quot;Cloudflare One&#10;				Client&quot;]--&quot;app.bank.com&quot;--&gt;gateway--&quot;Network traffic&quot;--&gt;cloudflared&#10;			gateway&lt;-.DNS lookup.-&gt;resolver&#10;			aws--AWS egress IP --&gt;app&#10;</code></pre>
<p>To learn more about how Gateway applies hostname-based egress policies, refer to the <a href="https://blog.cloudflare.com/egress-policies-by-hostname/">Cloudflare blog</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>User traffic must be on-ramped to Gateway using one of the following methods:</p>
<table>
<thead>
<tr>
<th>On-ramp method</th>
<th>Compatibility</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a></td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">PAC files</a></td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a></td>
<td>✅</td>
</tr>
<tr>
<td><a href="/mesh/">Cloudflare Mesh</a></td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">Cloudflare WAN</a></td>
<td>🚧<sup><a href="#footnote-cloudflare-one-gateway-egress-selector-onramps-mdx-1">1</a></sup></td>
</tr>
</tbody>
</table>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6626.md")
</div></details>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-cloudflare-one-gateway-egress-selector-onramps-mdx-1">Not compatible with [ECMP routing](/cloudflare-wan/reference/traffic-steering/#equal-cost-multi-path-routing). For hostname-based routing to work, DNS queries and the resulting network traffic must reach Cloudflare over the same IPsec/GRE tunnel. <br/></li></ol></section>
<h2 id="1-connect-your-private-network"><ol>
<li>Connect your private network</li>
</ol></h2>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">Connect your private network</a> to Cloudflare using <code>cloudflared</code>. For example, if you want traffic to egress from AWS, connect the private CIDR block of your AWS VPC.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6624.md")
</aside>
<h2 id="2-add-a-public-hostname-route"><ol start="2">
<li>Add a public hostname route</li>
</ol></h2>
<p>To route a public hostname through Cloudflare Tunnel:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Routes</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create hostname route</strong>.</p>
</li>
<li>
<p>In <strong>Hostname</strong>, enter the public hostname that represents the application (for example, <code>app.bank.com</code>). The hostname should be accessible from the public Internet.</p>
</li>
<li>
<p>For <strong>Tunnel</strong>, select the Cloudflare Tunnel that is being used to connect the private network to Cloudflare.</p>
</li>
<li>
<p>Select <strong>Create route</strong>.</p>
</li>
</ol>
<h2 id="3-route-network-traffic-through-the-cloudflare-one-client"><ol start="3">
<li>Route network traffic through the Cloudflare One Client</li>
</ol></h2>
<p>In your WARP <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a> configuration, route the following IP addresses through the WARP tunnel to Gateway.</p>
<h3 id="initial-resolved-ips">Initial resolved IPs</h3>
<p>When users connect to a public hostname route, Gateway will assign an <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/6627.md")
</div> to the DNS query from the following range:
<ul>
<li><strong>IPv4</strong>: <code>172.64.128.0/20</code></li>
<li><strong>IPv6</strong>: <code>2606:4700:0cf1:4000::/64</code></li>
</ul>
<p>This is the default range. You can <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">configure a custom initial resolved IP range</a> for IPv4 if it conflicts with your existing network.</p>
<p>Gateway's network engine operates at Layer 3/Layer 4 of the <a href="https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/">OSI model</a>, where only IP addresses are available — not hostnames. The initial resolved IP acts as a signal: when a packet's destination IP falls within this range, Gateway recognizes that the IP maps to a public hostname route and sends the traffic through the corresponding Cloudflare Tunnel.</p>
<p>To route initial resolved IPs through the Cloudflare One Client:</p>
<p>In your WARP <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a>, configure <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a> such that the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/6628.md")
</div> route through the WARP tunnel.  Configuration depends on your [Split Tunnels mode](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#change-split-tunnels-mode):
<ul>
<li>
<p><strong>Exclude mode</strong>: Delete <code>100.64.0.0/10</code> from your Split Tunnels list. We recommend <a href="/cloudflare-one/networks/routes/reserved-ips/#split-tunnel-configuration">adding back the IP ranges</a> that are not explicitly used for Cloudflare One services. This reduces the risk of conflicts with existing private network configurations that may use the CGNAT address space.</p>
</li>
<li>
<p><strong>Include mode</strong>: Add Split Tunnel entries for the following IP addresses:</p>
</li>
<li>
<p><strong>IPv4</strong>: <code>172.64.128.0/20</code></p>
</li>
<li>
<p><strong>IPv6</strong>: <code>2606:4700:0cf1:4000::/64</code></p>
</li>
</ul>
<p>This is the default range. You can <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">configure a custom initial resolved IP range</a> for IPv4 if it conflicts with your existing network.</p>
<h3 id="private-network-ips">Private network IPs</h3>
<p>Your private network's CIDR block should also route through the WARP tunnel. For a detailed configuration example, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/#3-route-private-network-ips-through-the-cloudflare-one-client">Connect a private network</a>.</p>
<h2 id="4-optional-configure-network-policies"><ol start="4">
<li>(Optional) Configure network policies</li>
</ol></h2>
<p>You can build <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a> to filter HTTPS traffic to your public hostname on port <code>443</code>. For example, to restrict <code>app.bank.com</code> so that only certain users or groups can access it through your AWS egress IP, create two policies: one to allow authorized users, and one to block everyone else.</p>
<ol>
<li>Allow company employees:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>SNI</td>
<td>in</td>
<td><code>app.bank.com</code></td>
<td>And</td>
<td>Allow</td>
</tr>
<tr>
<td>User Email</td>
<td>matches regex</td>
<td><code>.*@example.com</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<ol start="2">
<li>Block everyone else on port <code>443</code>:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>SNI</td>
<td>in</td>
<td><code>app.bank.com</code></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>Gateway does not support hostname-based filtering for traffic on non-<code>443</code> ports. To block traffic to <code>app.bank.com</code> on all ports, use the <a href="/cloudflare-one/traffic-policies/network-policies/#destination-ip">Destination IP</a> selector and specify the public IP range of <code>app.bank.com</code>.</p>
<h2 id="5-test-the-connection"><ol start="5">
<li>Test the connection</li>
</ol></h2>
<p>From a device, open a browser and go to <code>app.bank.com</code>.</p>
<p>You can search for <code>app.bank.com</code> in your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway DNS logs</a>; the <strong>DNS response details</strong> section should show the public resolved IPs as well as an <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/6629.md")
</div>. You can also check your [Cloudflare Tunnel logs](/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/) to confirm that requests are routing through the tunnel to the public resolved IPs.
<h2 id="limitations">Limitations</h2>
<h3 id="google-chrome-restricts-local-network-access">Google Chrome restricts local network access</h3>
<p>Starting with <a href="https://developer.chrome.com/release-notes/142">Chrome 142</a>, Local Network Access (LNA) restricts requests from websites to local IP addresses. LNA is implemented at the Chromium engine level, so this affects all Chromium-based browsers (for example, Microsoft Edge, Brave, and Opera), not only Google Chrome. This can affect accounts whose Gateway <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/6630.md")
</div> range is still drawn from Carrier-Grade NAT (CGNAT) address space (`100.64.0.0/10`) — for example, the legacy default range `100.80.0.0/16`, or a custom range configured within CGNAT space. These browsers categorize such addresses as belonging to a local network. When a website loaded from a public IP makes subrequests to a domain resolved through an initial resolved IP in this space, the browser treats this as a public-to-local network request and displays a prompt asking the user to allow access to devices on the local network. The browser blocks requests to these domains until the user accepts this prompt.
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
