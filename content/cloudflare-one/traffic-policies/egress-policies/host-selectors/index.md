<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6617.md")
</div></details>
<p>Egress policies are evaluated at Layer 4 (<a href="https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/">https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/</a>) of the OSI model, where only IP addresses are available — not hostnames. The <a href="/cloudflare-one/traffic-policies/egress-policies/#application">Application</a>, <a href="/cloudflare-one/traffic-policies/egress-policies/#content-categories">Content Categories</a>, <a href="/cloudflare-one/traffic-policies/egress-policies/#domain">Domain</a>, and <a href="/cloudflare-one/traffic-policies/egress-policies/#host">Host</a> selectors need to match traffic by hostname, so Gateway uses a two-step process:</p>
<ol>
<li>When Gateway receives a DNS query for a hostname that matches one of these selectors, it initially resolves the query to a temporary <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ol>
@markup("md", "content/.markup/bodies/6618.md")
</div>. By default, this IP is drawn from a Cloudflare-owned public range (`172.64.128.0/20` for IPv4, or `2606:4700:0cf1:4000::/64` for IPv6). You can [configure a custom IPv4 range](/cloudflare-one/networks/routes/configure-initial-resolved-ips/) if it conflicts with your existing network.
2. When traffic arrives with this temporary destination IP, Gateway can identify which hostname the connection belongs to, apply the correct egress policy, then replace the temporary IP with the real destination IP before forwarding the traffic.
<div class="nb-interactive-component" data-cf-component="HostSelectorEgressDiagram"></div>
<p>These selectors require additional configuration before they work.</p>
<h2 id="turn-on-host-selectors">Turn on Host selectors</h2>
<p>To turn on the selectors for your account:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6621.md")
</div></div>
<h2 id="prerequisites">Prerequisites</h2>
<p>Traffic must be on-ramped to Gateway with the following methods:</p>
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
<td>❌</td>
</tr>
<tr>
<td><a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">Cloudflare WAN</a></td>
<td>✅</td>
</tr>
</tbody>
</table>
<p>Traffic from unsupported on-ramp methods resolves using your default Gateway settings. If you use DNS locations to send DNS queries to Gateway (over IPv4, IPv6, DNS over TLS, or DNS over HTTPS), Gateway does not return the initial resolved IP and the host selectors do not apply.</p>
<h3 id="configuration-changes">Configuration changes</h3>
<p>To configure your Zero Trust organization to use Host selectors with Egress policies:</p>
<ol>
<li>
<p>Make sure you deploy the following version of the Cloudflare One Client on your users' devices:</p>
<ul>
<li><strong>Desktop</strong>: <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">Cloudflare One Client version 2025.4.929.0</a> or later</li>
<li><strong>iOS</strong>: <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/#ios">Cloudflare One Client version 1.11</a> or later</li>
<li><strong>Android and Chrome OS</strong>: <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/#android">Cloudflare One Client version 2.4.2</a> or later.</li>
</ul>
<p>If you need to support devices running prior versions of WARP, add and deploy the following key-value pair to your devices' <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/">WARP configuration file</a> (<code>mdm.xml</code> on Windows and Linux or <code>com.cloudflare.warp.plist</code> on macOS):</p>
</li>
</ol>
<pre><code class="language-diff">&lt;array&gt;&#10;	&lt;dict&gt;&#10;&#43;		&lt;key&gt;doh_in_tunnel&lt;/key&gt;&#10;&#43;		&lt;true/&gt;&#10;	&lt;/dict&gt;&#10;&lt;/array&gt;&#10;</code></pre>
<ol start="2">
<li></li>
</ol>
<p>In your WARP <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a>, configure <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a> such that the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/6622.md")
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
<p>The Cloudflare One Client must be set to <em>Traffic and DNS mode</em> for traffic affected by these selectors to route correctly.</p>
<h2 id="known-issues">Known issues</h2>
<h3 id="dns-resolution-location">DNS resolution location</h3>
<p>For the <a href="/cloudflare-one/traffic-policies/egress-policies/#application">Application</a>, <a href="/cloudflare-one/traffic-policies/egress-policies/#content-categories">Content Categories</a>, <a href="/cloudflare-one/traffic-policies/egress-policies/#domain">Domain</a>, and <a href="/cloudflare-one/traffic-policies/egress-policies/#host">Host</a> selectors, Gateway captures the destination IP address during the initial DNS resolution step described above. The egress policy does not change this IP address, so the destination Gateway connects to is independent of the location of the egress data center or dedicated egress IP you select.</p>
<p>If the resolved destination IP and the egress IP are located in different regions, connections to destinations that enforce geo-restriction or IP-allowlisting based on the connection source may be rejected.</p>
<p>This can affect you if you use Domain or Host egress selectors, your users are located outside the region associated with your egress IP, and the destination applies geo-restriction or IP-based access controls.</p>
<h3 id="google-chrome-restricts-local-network-access">Google Chrome restricts local network access</h3>
<p>Starting with <a href="https://developer.chrome.com/release-notes/142">Chrome 142</a>, Local Network Access (LNA) restricts requests from websites to local IP addresses. LNA is implemented at the Chromium engine level, so this affects all Chromium-based browsers (for example, Microsoft Edge, Brave, and Opera), not only Google Chrome. This can affect accounts whose Gateway <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/6623.md")
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
<h3 id="dns-override-policies-bypass-host-selectors">DNS Override policies bypass host selectors</h3>
<p>If a domain matches a <a href="/cloudflare-one/traffic-policies/dns-policies/#override">DNS Override policy</a>, Gateway will not apply the initial resolved IP mapping for that domain. This means host-based egress selectors (Application, Content Categories, Domain, and Host) will not evaluate against traffic to the overridden domain. Traffic to these domains will use the default Cloudflare egress method.</p>
<h3 id="https-dns-records-not-supported">HTTPS DNS records not supported</h3>
<p>Host selectors do not support HTTPS DNS record types. When a domain uses HTTPS records for connection establishment, Gateway cannot map the DNS query to a hostname for egress policy evaluation. Traffic to these domains will use the default Cloudflare egress method instead of matching a host-based egress policy.</p>
<p>If you need to apply egress policies to a domain that uses HTTPS records, use an IP-based selector (such as <a href="/cloudflare-one/traffic-policies/egress-policies/#destination-ip">Destination IP</a>) instead.</p>
