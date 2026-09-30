<p>Instead of managing static IP lists and routes, you can connect users to private HTTP and non-HTTP applications using their hostnames (for example, <code>wiki.internal.local</code>). Private hostname routes are especially useful when the application has an unknown or ephemeral IP, which often occurs when infrastructure is provisioned by a third-party cloud provider.</p>
<div class="nb-interactive-component" data-cf-component="TunnelHostnameRoutingDiagram"></div>
<p>When a user requests a private hostname, Cloudflare Gateway assigns an <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5405.md")
</div> to route the traffic through your tunnel to the correct private IP address. By default, this IP is drawn from a Cloudflare-owned public IPv4 range (`172.64.128.0/20`) rather than Carrier-Grade NAT (CGNAT) space, so it does not trigger [Google Chrome's Local Network Access restrictions](#google-chrome-restricts-access-to-private-hostnames). You can also [configure a custom range](/cloudflare-one/networks/routes/configure-initial-resolved-ips/) if it conflicts with your existing network. For a deep dive into the architecture and packet flow, refer to our [announcement blog post](https://blog.cloudflare.com/tunnel-hostname-routing/).
<h2 id="supported-on-ramps-off-ramps">Supported on-ramps/off-ramps</h2>
<p>The table below summarizes the Cloudflare One products that are compatible with private hostname routing. Refer to the table legend for guidance on interpreting the table.</p>
<p>✅ Product works with no caveats <br/>
🚧 Product can be used with some caveats <br/>
❌ Product cannot be used <br/></p>
<h3 id="device-connectivity">Device connectivity</h3>
<p>End users can connect to private hostnames using the following traffic on-ramps:</p>
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
@markup("md", "content/.markup/bodies/5406.md")
</div></details>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-cloudflare-one-gateway-egress-selector-onramps-mdx-1">Not compatible with [ECMP routing](/cloudflare-wan/reference/traffic-steering/#equal-cost-multi-path-routing). For hostname-based routing to work, DNS queries and the resulting network traffic must reach Cloudflare over the same IPsec/GRE tunnel. <br/></li></ol></section>
<h3 id="private-network-connectivity">Private network connectivity</h3>
<p>Private hostname routing works with the off-ramps below. Other traffic off-ramps require IP-based routes.</p>
<table>
<thead>
<tr>
<th>Connector</th>
<th>Compatibility</th>
<th>Minimum version</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/">cloudflared</a></td>
<td>✅</td>
<td>2025.7.0</td>
</tr>
<tr>
<td><a href="/mesh/features/routes/#hostname-routes">Cloudflare Mesh</a></td>
<td>✅</td>
<td>2026.6.822.0 (Linux)</td>
</tr>
<tr>
<td><a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">Cloudflare WAN</a></td>
<td>❌</td>
<td></td>
</tr>
</tbody>
</table>
<h2 id="connect-a-private-hostname">Connect a private hostname</h2>
<p>This section covers how to enable remote access to a private hostname application using <code>cloudflared</code>.</p>
<h3 id="prerequisites">Prerequisites</h3>
<p>Before you can connect to private hostnames, you must enable the Gateway proxy.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5409.md")
</div></div>
<p>Cloudflare will now proxy traffic from enrolled devices, except for the traffic excluded in your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/#3-route-private-network-ips-through-the-cloudflare-one-client">split tunnel settings</a>. For more information on how Gateway forwards traffic, refer to <a href="/cloudflare-one/traffic-policies/proxy/">Gateway proxy</a>.</p>
<p>Your devices must also forward the following traffic to Cloudflare:</p>
<ul>
<li>
<p>Initial resolved IPs:</p>
</li>
<li>
<p><strong>IPv4</strong>: <code>172.64.128.0/20</code></p>
</li>
<li>
<p><strong>IPv6</strong>: <code>2606:4700:0cf1:4000::/64</code></p>
</li>
</ul>
<p>This is the default range. You can <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">configure a custom initial resolved IP range</a> for IPv4 if it conflicts with your existing network.</p>
<ul>
<li>DNS queries for your private hostname</li>
</ul>
<p>Configuration steps vary depending on your <a href="#device-connectivity">device on-ramp</a>:</p>
<details class="nb-details"><summary>Cloudflare One Clients</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5411.md")
</div></details>
<details class="nb-details"><summary>Cloudflare Mesh</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5413.md")
</div></details>
<details class="nb-details"><summary>Cloudflare WAN</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5415.md")
</div></details>
<h3 id="1-connect-the-application-to-cloudflare"><ol>
<li>Connect the application to Cloudflare</li>
</ol></h3>
<ol>
<li>Log in to the Cloudflare dashboard and go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create a tunnel</strong>.</p>
</li>
<li>
<p>Enter a name for your tunnel. We suggest choosing a name that reflects the type of resources you want to connect through this tunnel (for example, <code>enterprise-VPC-01</code>).</p>
</li>
<li>
<p>Select <strong>Create Tunnel</strong>.</p>
</li>
<li>
<p>Choose your operating system, then copy the installation command and run it in a terminal on your origin server.</p>
</li>
<li>
<p>Wait for the tunnel to connect. Once the connection is established, select <strong>Continue</strong>.</p>
</li>
<li>
<p>After the tunnel is connected, go to the tunnel's <strong>Routes</strong> tab and select <strong>Add route</strong>, then select <strong>Private hostname</strong>.</p>
</li>
<li>
<p>Enter the fully qualified domain name (FQDN) that represents your application (for example, <code>wiki.internal.local</code>).</p>
</li>
</ol>
<details class="nb-details"><summary>Hostname format restrictions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5416.md")
</div></details>
<ol start="10">
<li>Select <strong>Save</strong>.</li>
</ol>
<h3 id="2-configure-dns-resolution"><ol start="2">
<li>Configure DNS resolution</li>
</ol></h3>
<p>When Gateway receives a request for your private hostname, it must resolve the hostname to a private IP address. There are two ways to configure this, depending on your network topology.</p>
<h4 id="scenario-a-use-the-system-resolver-default">Scenario A: Use the system resolver (Default)</h4>
<p>By default, <code>cloudflared</code> uses the private DNS resolver configured on its host machine (for example, in <code>/etc/resolv.conf</code> on Linux).</p>
<p>If the machine running <code>cloudflared</code> can already resolve <code>wiki.internal.local</code> to its private IP using the local system resolver, no further configuration is required. You can skip to <a href="#3-recommended-filter-network-traffic-with-gateway">Step 3</a>.</p>
<h4 id="scenario-b-use-a-specific-private-dns-server-advanced">Scenario B: Use a specific private DNS server (Advanced)</h4>
<p>If you need <code>cloudflared</code> to use a specific internal DNS server that is different from the host's default resolver, you must explicitly connect that DNS server to Cloudflare via an <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">IP/CIDR route</a>. You will also need to configure a <a href="/cloudflare-one/traffic-policies/resolver-policies/">Gateway resolver policy</a> to route queries to this specific private DNS server.</p>
<ol>
<li>To create an IP/CIDR route for the DNS server:
<ol>
<li>Go to <strong>Networking</strong> &gt; <strong>Routes</strong>.</li>
</ol>
</li>
</ol>
<div class="nb-dash-button"></div>
<pre><code>2. Select **Add CIDR route**.&#10;3. Enter the private IP address of your internal DNS resolver.&#10;4. Select the Cloudflare Tunnel that connects to the network where this DNS server resides.&#10;5. Select **Create**.&#10;</code></pre>
<ol start="2">
<li>To create a resolver policy:
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Resolver policies</strong>.</li>
<li>Select <strong>Create a policy</strong>.</li>
<li>Create an expression that matches the private hostname:</li>
</ol>
</li>
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
<td>in</td>
<td><code>wiki.internal.local</code></td>
</tr>
</tbody>
</table>
    4. Under **Configure custom DNS resolvers**, enter the private IP address of your internal DNS server.
    5. From the dropdown menu, select the `- Private` routing option and the [virtual network](/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/) assigned to the tunnel you selected in the previous step.
    6. Select **Create policy**.
<h3 id="3-recommended-filter-network-traffic-with-gateway"><ol start="3">
<li>(Recommended) Filter network traffic with Gateway</li>
</ol></h3>
<p>By default, all devices enrolled in your Zero Trust organization can connect to your private network through Cloudflare Tunnel. You can configure Gateway to inspect your network traffic and either block or allow access based on user identity and device posture. To learn more about policy design, refer to <a href="/learning-paths/replace-vpn/build-policies/create-policy/">Secure your first application</a>.</p>
<p>To prevent Cloudflare One Client users from accessing your entire private network, we recommend creating a <a href="/learning-paths/replace-vpn/build-policies/create-policy/#catch-all-policy">catch-all Gateway block policy</a> for your private IP space. You can then layer on higher priority Allow policies (in either Access or Gateway) which grant users access to specific applications or IPs.</p>
<h4 id="option-1-access-application-recommended">Option 1: Access application (recommended)</h4>
<p>You can create an <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Access self-hosted application</a> for your private hostname and configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> within that application. This option allows you to manage user access alongside your SaaS and other web apps.</p>
<h4 id="option-2-gateway-firewall-policies">Option 2: Gateway firewall policies</h4>
<p>If you prefer to secure the application using a traditional firewall model, you can build Gateway network policies using the <a href="/cloudflare-one/traffic-policies/network-policies/#sni">SNI</a> or <a href="/cloudflare-one/traffic-policies/network-policies/#sni-domain">SNI Domain</a> selector. For an additional layer of protection, add a Gateway DNS policy to allow or block the <a href="/cloudflare-one/traffic-policies/dns-policies/#host">Host</a> or <a href="/cloudflare-one/traffic-policies/dns-policies/#domain">Domain</a> from resolving.</p>
<pre><code>&lt;details class=&quot;nb-details&quot;&gt;&lt;summary&gt;Example network policies&lt;/summary&gt;&lt;div class=&quot;nb-details-body&quot;&gt;&#10;</code></pre>
@markup("md", "content/.markup/bodies/5417.md")
</div></details>
<pre><code>&lt;details class=&quot;nb-details&quot;&gt;&lt;summary&gt;Example DNS policy&lt;/summary&gt;&lt;div class=&quot;nb-details-body&quot;&gt;&#10;</code></pre>
@input("content/.markup/bodies/5418.md")
</div></details>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="sni-selector-limitations">SNI selector limitations</h3>
@markup("md", "content/.markup/bodies/5404.md")
</aside>
<h3 id="4-test-the-connection"><ol start="4">
<li>Test the connection</li>
</ol></h3>
<p>End users can now reach the application by going to its private hostname. For example, to connect to a private web application, open a browser and go to <code>wiki.internal.local</code>.</p>
<h4 id="troubleshooting">Troubleshooting</h4>
<p>If you cannot connect, verify the following:</p>
<ol>
<li><strong>Confirm DNS resolution</strong> - From the device, confirm that you can successfully resolve the private hostname:</li>
</ol>
<pre><code class="language-sh">nslookup wiki.internal.local&#10;</code></pre>
<pre><code class="language-sh">Server:		127.0.2.2&#10;Address:	127.0.2.2#53&#10;&#10;Non-authoritative answer:&#10;Name:	wiki.internal.local&#10;Address: 172.64.128.48&#10;</code></pre>
<p>The query should resolve using <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#dns-traffic">WARP's DNS proxy</a> and return a Gateway <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5419.md")
</div>. If the query fails to resolve or returns a different IP, check your [Local Domain Fallback](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/) configuration and [Gateway resolver policies](/cloudflare-one/traffic-policies/resolver-policies/).
<ol start="2">
<li>
<p><strong>Check Gateway logs</strong> - Review your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway network logs</a> to see if the connection is being blocked by a policy.</p>
</li>
<li>
<p><strong>Verify tunnel status</strong> - Confirm that your tunnel is healthy and connected by checking <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/">tunnel status</a>.</p>
</li>
<li>
<p><strong>Test connectivity to initial resolved IP</strong> - When you connect to the application using its private hostname, the device should make a connection to the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
</li>
</ol>
@markup("md", "content/.markup/bodies/5420.md")
</div>:
<pre><code class="language-sh">curl -v4 http://wiki.internal.local&#10;</code></pre>
<pre><code class="language-sh">&#42; Trying 172.64.128.48:80...&#10;&#42; Connected to wiki.internal.local (172.64.128.48) port 80&#10;...&#10;</code></pre>
<p>If the request fails, confirm that the initial resolved IP <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">routes through the WARP tunnel</a>. You can also check your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">tunnel logs</a> to confirm that requests are routing to the application's private IP.</p>
<h2 id="limitations">Limitations</h2>
<h3 id="google-chrome-restricts-access-to-private-hostnames">Google Chrome restricts access to private hostnames</h3>
<p>Starting with <a href="https://developer.chrome.com/release-notes/142">Chrome 142</a>, Local Network Access (LNA) restricts requests from websites to local IP addresses. LNA is implemented at the Chromium engine level, so this affects all Chromium-based browsers (for example, Microsoft Edge, Brave, and Opera), not only Google Chrome. This can affect accounts whose Gateway <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5421.md")
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
