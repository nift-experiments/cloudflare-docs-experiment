<p>Split Tunnels can be configured to exclude or include IP addresses or domains from going through the Cloudflare One Client (formerly WARP). This feature is commonly used to run the Cloudflare One Client alongside a VPN (in Exclude mode) or to provide access to a specific private network (in Include mode).</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6278.md")
</aside>
<p>Because Split Tunnels controls what Gateway has visibility on at the network level, we recommend testing all changes before rolling out updates to end users.</p>
<h2 id="change-split-tunnels-mode">Change Split Tunnels mode</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6281.md")
</div></div>
<p>All clients with this device profile will now switch to the new mode and its default route configuration. Next, <a href="#add-a-route">add</a> or <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#remove-a-route">remove</a> routes from your Split Tunnel configuration.</p>
<h2 id="add-a-route">Add a route</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6288.md")
</div></div>
<p>It may take up to 10 minutes for newly updated settings to propagate to devices.</p>
<p>We recommend keeping the Split Tunnels list short, as each entry takes time for the client to parse. In particular, domains are slower to action than IP addresses because they require on-the-fly IP lookups and routing table / local firewall changes. A shorter list will also make it easier to understand and debug your configuration. For information on device profile limits, refer to <a href="/cloudflare-one/account-limits/#warp">Account limits</a>.</p>
<h3 id="when-to-use-split-tunnels">When to use Split Tunnels</h3>
<p>Use Split Tunnels when you need to bypass Gateway entirely for a site or allow traffic through the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#system-firewall">firewall that the Cloudflare One Client creates</a>. Common scenarios include:</p>
<ul>
<li>Connect to a third-party application which requires the actual IP address of the end-user device (for example, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#directly-route-microsoft-365-traffic">Microsoft 365</a>).</li>
<li>Optimize voice and video.</li>
<li>Connect to a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/vpn/">third-party VPN</a> endpoint.</li>
</ul>
<h3 id="when-not-to-use-split-tunnels">When not to use Split Tunnels</h3>
<p>Do not exclude a site from Split Tunnels if you want to see the traffic in your Gateway logs. In particular, we do not recommend using Split Tunnels to:</p>
<ul>
<li>Solve connectivity issues with a specific website. For configuration guidance, refer to our <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/common-issues/#cannot-connect-to-a-specific-app-or-website">troubleshooting guide</a>.</li>
<li>Solve performance issues with a specific website. Since Cloudflare operates within 50 milliseconds of 95% of the Internet-connected population, it is usually faster to send traffic through us. If you are encountering a performance-related issue, it is best to first explore your Gateway policies or reach out to Support.</li>
</ul>
<h2 id="routes-for-split-tunnels-include-mode">Routes for Split Tunnels Include mode</h2>
<p>Many Cloudflare Zero Trust services rely on traffic going through the Cloudflare One Client, such as <a href="/cloudflare-one/reusable-components/posture-checks/">device posture checks</a> and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">device client session durations</a>. If you are using Split Tunnels in Include mode, you will need to manually add Cloudflare Zero Trust domains and IPs in order for these features to function.</p>
<h3 id="cloudflare-zero-trust-domains">Cloudflare Zero Trust domains</h3>
<p>If you are using Split Tunnels in Include mode, you must include the following domains:</p>
<ul>
<li>The IdP used to authenticate to Cloudflare Zero Trust</li>
<li><code>&lt;your-team-name&gt;.cloudflareaccess.com</code></li>
<li>The application protected by the Access or Gateway policy</li>
<li><code>edge.browser.run</code> if using <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a></li>
</ul>
<h3 id="cloudflare-zero-trust-ip-addresses">Cloudflare Zero Trust IP addresses</h3>
<h4 id="block-page">Block page</h4>
<p>If you are using Split Tunnels in Include mode and have <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policies</a> with the <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/">block page</a> enabled, you must include the IPs that blocked domains will resolve to. Unless you are using a <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/#dns-resolver-ip">dedicated or BYOIP resolver IP</a> the block page will resolve to:</p>
<ul>
<li><code>162.159.36.12</code></li>
<li><code>162.159.46.12</code></li>
</ul>
<h4 id="team-domain">Team domain</h4>
<p>In <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#traffic-only-mode">Traffic only mode</a>, you cannot <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#cloudflare-zero-trust-domains">add domains</a> to Split Tunnels. If you are using Split Tunnels in Include mode, you must include the IPs that resolve to <code>&lt;your-team-name&gt;.cloudflareaccess.com</code> instead:</p>
<ul>
<li><code>104.19.194.29</code></li>
<li><code>104.19.195.29</code></li>
</ul>
<h2 id="device-ip-ranges">Device IP ranges</h2>
<p>In Exclude mode, default device profiles exclude the CGNAT range (<code>100.64.0.0/10</code>), which contains the default <a href="/cloudflare-one/networks/routes/reserved-ips/#device-ips">device IP range</a> (<code>100.96.0.0/12</code>). The Mesh setup wizard updates the default profile to route the device IP range through Cloudflare. If you did not use the wizard, or if another profile applies to the device, verify that the profile does not exclude the device IP range or a parent range that contains it.</p>
<h2 id="automatically-managed-ranges">Automatically managed ranges</h2>
<p>The Cloudflare One Client automatically includes the following ranges in Include mode, and automatically removes them from any exclusions configured in Exclude mode. This happens at runtime on the device: the ranges are not stored in your device profile, do not appear in the Split Tunnels list in the dashboard, and do not need to be added manually.</p>
<ul>
<li><strong>IPv4</strong>: <code>172.64.128.0/20</code> — the default <a href="/cloudflare-one/networks/routes/reserved-ips/#gateway-initial-resolved-ips">Gateway initial resolved IP range</a></li>
<li><strong>IPv6</strong>: <code>2606:4700:0cf1::/48</code> — covers <a href="/cloudflare-one/networks/routes/reserved-ips/#device-ips">device IPs</a>, <a href="/cloudflare-one/networks/routes/reserved-ips/#cloudflare-source-ips">Cloudflare source IPs</a>, and <a href="/cloudflare-one/networks/routes/reserved-ips/#gateway-initial-resolved-ips">Gateway initial resolved IPs</a></li>
</ul>
<p>You do not need to add these ranges to your Split Tunnels configuration. If you are troubleshooting a feature that depends on one of these ranges (for example, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">hostname routing</a> or <a href="/mesh/">Cloudflare Mesh</a>), you can still add the range explicitly as a diagnostic step, but this should not be required for normal operation.</p>
<p>If your account uses a <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">custom initial resolved IP range</a> instead of the default <code>172.64.128.0/20</code>, add that custom range to your Split Tunnels configuration.</p>
<h2 id="domain-based-split-tunnels">Domain-based Split Tunnels</h2>
<p>Domain-based split tunneling has a few ramifications you should be aware of before deploying in your organization:.</p>
<ul>
<li>Routes excluded or included from Cloudflare One Client and Gateway visibility may change day to day, and may be different for each user depending on where they are.</li>
<li>You may inadvertently exclude or include additional hostnames that happen to share an IP address. This commonly occurs if you add a domain hosted by a CDN or large Internet provider such as Cloudflare, AWS, or Azure. For example, if you wanted to exclude a VPN hosted on AWS, do not add <code>*.amazonaws.com</code> as that will open up your devices to all traffic on AWS. Instead, add the specific VPN endpoint (<code>*.cvpn-endpoint-&lt;UUID&gt;.prod.clientvpn.us-west-2.amazonaws.com</code>).</li>
<li>Most services are a collection of hostnames. Until Split Tunnels mode supports <a href="/cloudflare-one/traffic-policies/application-app-types/">App Types</a>, you will need to manually add all domains used by a particular app or service.</li>
<li>The Cloudflare One Client must handle the DNS lookup request for the domain. If a DNS result has been previously cached by the operating system or otherwise intercepted (for example, via your browser's secure DNS settings), the IP address will not be dynamically added to your Split Tunnel.</li>
</ul>
<h3 id="valid-domains">Valid domains</h3>
<table>
<thead>
<tr>
<th>Split tunnel domain</th>
<th>Matches</th>
<th>Does not match</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>example.com</code></td>
<td>exact match of <code>example.com</code></td>
<td>subdomains such as <code>www.example.com</code></td>
</tr>
<tr>
<td><code>example.example.com</code></td>
<td>exact match of <code>example.example.com</code></td>
<td><code>example.com</code> or subdomains such as <code>www.example.example.com</code></td>
</tr>
<tr>
<td><code>*.example.com</code></td>
<td>subdomains such as <code>www.example.com</code> and <code>sub2.sub1.example.com</code></td>
<td><code>example.com</code></td>
</tr>
</tbody>
</table>
<h3 id="platform-differences">Platform differences</h3>
<p>Domain-based Split Tunnels work differently on mobile clients than on desktop clients. If both mobile and desktop clients will connect to your organization, it is recommended to use Split Tunnels based on IP addresses or CIDR, which work the same across all platforms.</p>
<h4 id="windows-linux-and-macos">Windows, Linux and macOS</h4>
<p>Clients on these platforms work by dynamically inserting the IP address of the domain immediately after it is resolved into the routing table for split tunneling. This allows the desktop clients to support wildcard domain prefixes (for example, <code>*.example.com</code>), not just a singular domain (like <code>example.com</code> or <code>www.example.com</code>).</p>
<h4 id="ios-android-and-chromeos">iOS, Android and ChromeOS</h4>
<p>Due to platform differences, mobile clients can only apply Split Tunnels rules when the tunnel is initially started. This means:</p>
<ul>
<li>Domain-based Split Tunnels rules are created when the tunnel is established based on the IP address for that domain at that time. The route is refreshed each time the tunnel is established.</li>
<li>Wildcard domain prefixes (for example, <code>*.example.com</code>) are supported only if they have valid wildcard DNS records. Other wildcard domains are not supported because the client is unable to match wildcard domains to hostnames when starting up the tunnel. Unsupported wildcard domain prefixes can still exist in your configuration, but they will be ignored on mobile platforms.</li>
</ul>
<h2 id="remove-a-route">Remove a route</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6276.md")
</aside>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong> &gt; <strong>General profiles</strong>.</li>
<li>Locate the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> you would like to modify and select <strong>Edit</strong>.</li>
<li>Under <strong>Split Tunnels</strong>, select <strong>Manage</strong>.</li>
<li>Find the IP address or hostname in the list and select the <strong>Action</strong> button. From the dropdown, select <em>Delete</em>.</li>
</ol>
<p>It may take up to 10 minutes for newly updated settings to propagate to devices.</p>
<p>If you need to revert to the default Split Tunnel entries recommended by Cloudflare, select <strong>Restore default entries</strong>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> - Resolve selected domains via local DNS instead of Cloudflare Gateway.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">Cloudflare One Client with firewall</a> - Learn which IPs, domains, and ports to allow so users can deploy and connect the Cloudflare One Client successfully behind a firewall.</li>
</ul>
