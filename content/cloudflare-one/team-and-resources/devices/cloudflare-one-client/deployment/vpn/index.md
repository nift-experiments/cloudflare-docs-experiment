<p>The Cloudflare One Client (formerly WARP) can run alongside most legacy third-party VPNs. However, both the Cloudflare One Client and your VPN try to control the same things on the device: which traffic goes where (routing), which DNS server answers queries, and which firewall rules apply. To prevent conflicts, you must split these responsibilities between the two products:</p>
<ul>
<li>IP traffic is split tunneled between the Cloudflare One Client and the VPN. All VPN traffic must bypass the Cloudflare One Client and vice versa.</li>
<li>The VPN bypasses/allows/excludes all domains, IPs, and ports listed in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">Cloudflare One Client with firewall</a>.</li>
<li>DNS resolution is handled by either the Cloudflare One Client or the VPN. You must disable DNS filtering in one of the two products.</li>
</ul>
<p>For the most stable and consistent connection, we recommend connecting your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">private network or individual applications</a> to Cloudflare instead of using a legacy VPN. However, until you can migrate, the following guidelines will help get your Zero Trust deployment up and running.</p>
<h2 id="traffic-and-dns-mode">Traffic and DNS mode</h2>
<p>In <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#traffic-and-dns-mode-default">Traffic and DNS mode</a>, the Cloudflare One Client must be allowed to capture and route all DNS traffic on the device. You can use <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> to send DNS requests to a server behind your third-party VPN or firewall, but the request must first go through the client's local DNS proxy. Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/">client architecture</a> for more information about this requirement.</p>
<p>If you cannot disable DNS on your VPN, switch to <a href="#secure-web-gateway-without-dns-filtering">Traffic only mode</a> mode to disable DNS in the Cloudflare One Client.</p>
<h3 id="1-configure-the-vpn"><ol>
<li>Configure the VPN</li>
</ol></h3>
<p>Perform these steps in your third-party VPN software. Refer to your VPN's documentation for specific instructions on how to configure these settings.</p>
<ol>
<li>
<p>Enable split tunneling in the third-party VPN.</p>
</li>
<li>
<p>Disable DNS configuration in the third-party VPN.</p>
</li>
</ol>
<h3 id="2-configure-warp"><ol start="2">
<li>Configure WARP</li>
</ol></h3>
<p>Perform these steps in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> under <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong> &gt; <strong>General profiles</strong>.</p>
<ol>
<li>
<p>Set your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#change-split-tunnels-mode">Split Tunnels mode</a> to <strong>Exclude IPs and domains</strong>.</p>
</li>
<li>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#add-a-route">Add the following entries</a> to your Split Tunnel Exclude list:</p>
<ul>
<li>Private IP address range exposed by your third-party VPN client. For example,</li>
</ul>
</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>IP Address</td>
<td><code>172.16.0.0/12</code></td>
</tr>
</tbody>
</table>
<p>|</p>
   * Server that your third-party VPN client connects to. For example,
<table>
<thead>
<tr>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Domain</td>
<td><code>*.cvpn-endpoint-xxxxx.prod.clientvpn.us-west-2.amazonaws.com</code></td>
</tr>
</tbody>
</table>
<ol start="3">
<li>(Optional) In <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a>, add the domains that you want to resolve using your VPN's private DNS servers. For example,</li>
</ol>
<table>
<thead>
<tr>
<th>Domain</th>
<th>DNS Servers</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>internal.wiki.intranet</code></td>
<td><code>172.31.26.130</code>, <code>172.31.23.120</code></td>
</tr>
</tbody>
</table>
<p>You can now <a href="#test-the-configuration">test</a> if WARP runs alongside the VPN.</p>
<h2 id="traffic-only-mode">Traffic only mode</h2>
<p>In <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#traffic-only-mode">Traffic only mode</a>, the Cloudflare One Client only controls IP routing — it does not manage DNS. This is the simpler option when your VPN must retain DNS control, because you only need to split tunnel IP traffic.</p>
<h3 id="1-configure-the-vpn-1"><ol>
<li>Configure the VPN</li>
</ol></h3>
<p>Enable split tunneling in your third-party VPN software. Refer to your VPN's documentation for specific instructions on how to configure this setting.</p>
<h3 id="2-configure-warp-1"><ol start="2">
<li>Configure WARP</li>
</ol></h3>
<p>Perform these steps in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> under <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong> &gt; <strong>General profiles</strong>.</p>
<ol>
<li>
<p>Set your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#change-split-tunnels-mode">Split Tunnels mode</a> to <strong>Exclude IPs and domains</strong>.</p>
</li>
<li>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#add-a-route">Add the following entries</a> to your Split Tunnel Exclude list:</p>
<ul>
<li>Private IP address range exposed by your third-party VPN client. For example,</li>
</ul>
</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>IP Address</td>
<td><code>172.16.0.0/12</code></td>
</tr>
</tbody>
</table>
<p>|</p>
   * Server that your third-party VPN client connects to. For example,
<table>
<thead>
<tr>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Domain</td>
<td><code>*.cvpn-endpoint-xxxxx.prod.clientvpn.us-west-2.amazonaws.com</code></td>
</tr>
</tbody>
</table>
<ol start="3">
<li>In your device profile, verify that <strong>Service mode</strong> is set to <strong>Traffic only mode</strong>.</li>
</ol>
<h2 id="test-the-configuration">Test the configuration</h2>
<p>We recommend enabling the Cloudflare One Client before enabling your third-party VPN. Some third-party VPNs must be the last to edit a network's configuration or they will fail.</p>
<ol>
<li>Connect the Cloudflare One Client.</li>
<li>Connect the third-party VPN client.</li>
<li>To test your Split Tunnel configuration, connect to a private IP address that is behind the VPN. For example, you can open a terminal and run <code>ping &lt;SERVER-IP&gt;</code>.</li>
<li>To test your DNS configuration, connect to an internal domain that is behind the VPN. For example, you can open a browser and go to <code>internal.wiki.intranet</code>.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="test-before-updates">Test before updates</h3>
@markup("md", "content/.markup/bodies/6123.md")
</aside>
