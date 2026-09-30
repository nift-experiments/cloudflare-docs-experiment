<p>If your organization uses a firewall or other policies to restrict or intercept Internet traffic, you may need to exempt the following IP addresses and domains to allow the Cloudflare One Client (formerly WARP) to connect.</p>
<h2 id="client-orchestration-api">Client orchestration API</h2>
<p>The Cloudflare One Client connects to Cloudflare via a standard HTTPS connection outside the tunnel for operations like registration or settings changes. To perform these operations, you must allow the following IPs and domains:</p>
<ul>
<li>IPv4 API endpoints: <code>162.159.137.105</code> and <code>162.159.138.105</code></li>
<li>IPv6 API endpoints: <code>2606:4700:7::a29f:8969</code> and <code>2606:4700:7::a29f:8a69</code></li>
<li>SNIs for Cloudflare One Client version 2026.6.0 and later: <code>api.devices.cloudflare.com</code></li>
<li>SNIs for versions earlier than 2026.6.0: <code>zero-trust-client.cloudflareclient.com</code> and <code>notifications.cloudflareclient.com</code></li>
</ul>
<p>Cloudflare One Client version 2026.6.0 and later uses <code>api.devices.cloudflare.com</code>. Versions earlier than 2026.6.0 use <code>zero-trust-client.cloudflareclient.com</code> and <code>notifications.cloudflareclient.com</code>.</p>
<p>These domains may resolve to different IP addresses. The Cloudflare One Client overrides the resolved IPs with the IPs listed above. To avoid connectivity issues, allow those IPs through your firewall.</p>
<details class="nb-details"><summary>FedRAMP High requirements</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6148.md")
</div></details>
<h2 id="doh-ip">DoH IP</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6147.md")
</aside>
<p>In <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#dns-only-mode">DNS only mode</a> mode, the Cloudflare One Client sends DNS requests to Gateway over an HTTPS connection. For DNS to work correctly, you must allow the following IPs and domains:</p>
<ul>
<li>IPv4 DoH addresses: <code>162.159.36.1</code> and <code>162.159.46.1</code></li>
<li>IPv6 DoH addresses: <code>2606:4700:4700::1111</code> and <code>2606:4700:4700::1001</code></li>
<li>SNIs: <code>&lt;ACCOUNT_ID&gt;.cloudflare-gateway.com</code></li>
</ul>
<p>Even though <code>&lt;ACCOUNT_ID&gt;.cloudflare-gateway.com</code> may resolve to different IP addresses, the Cloudflare One Client overrides the resolved IPs with the IPs listed above. To avoid connectivity issues, ensure that the above IPs are permitted through your firewall.</p>
<details class="nb-details"><summary>FedRAMP High requirements</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6149.md")
</div></details>
<h3 id="android-devices">Android devices</h3>
<p>If you are deploying the Cloudflare One Agent on Android/ChromeOS, you must also add <code>cloudflare-dns.com</code> to your firewall exception list. On Android/ChromeOS devices, the Cloudflare One Client uses <code>cloudflare-dns.com</code> to resolve domains on your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#domain-based-split-tunnels">Split Tunnel list</a>.</p>
<h2 id="client-authentication-endpoint">Client authentication endpoint</h2>
<p>When you <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">log in to your Cloudflare One organization</a>, you will have to complete the authentication steps required by your organization in the browser window that opens. To perform these operations, you must allow the following domains:</p>
<ul>
<li>The IdP used to authenticate to Cloudflare One</li>
<li><code>&lt;your-team-name&gt;.cloudflareaccess.com</code></li>
</ul>
<details class="nb-details"><summary>FedRAMP High requirements</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6150.md")
</div></details>
<h2 id="warp-ingress-ip">WARP ingress IP</h2>
<p>The Cloudflare One Client connects to the following IP addresses, depending on which <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">tunnel protocol</a> is configured for your device (WireGuard or MASQUE). All network traffic from your device to Cloudflare goes through these IPs and ports over UDP.</p>
<h3 id="wireguard">WireGuard</h3>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>IPv4 address</td>
<td><code>162.159.193.0/24</code></td>
</tr>
<tr>
<td>IPv6 address</td>
<td><code>2606:4700:100::/48</code></td>
</tr>
<tr>
<td>Default port</td>
<td><code>UDP 2408</code></td>
</tr>
<tr>
<td>Fallback ports</td>
<td><code>UDP 500</code> <br/> <code>UDP 1701</code> <br/> <code>UDP 4500</code></td>
</tr>
</tbody>
</table>
<h3 id="masque">MASQUE</h3>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>IPv4 address</td>
<td><code>162.159.197.0/24</code></td>
</tr>
<tr>
<td>IPv6 address</td>
<td><code>2606:4700:102::/48</code></td>
</tr>
<tr>
<td>Default port</td>
<td><code>UDP 443</code></td>
</tr>
<tr>
<td>Fallback ports</td>
<td><code>UDP 500</code> <br/> <code>UDP 1701</code> <br/> <code>UDP 4500</code> <br/> <code>UDP 4443</code> <br/> <code>UDP 8443</code> <br/> <code>UDP 8095</code> <br/> <code>TCP 443</code> <sup><a href="#footnote-1">1</a></sup></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6146.md")
</aside>
<details class="nb-details"><summary>FedRAMP High requirements</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6151.md")
</div></details>
<h2 id="captive-portal">Captive portal</h2>
<p>The following domains are used as part of our captive portal check:</p>
<ul>
<li><code>cloudflareportal.com</code></li>
<li><code>cloudflareok.com</code></li>
<li><code>cloudflarecp.com</code></li>
<li><code>www.msftconnecttest.com</code></li>
<li><code>captive.apple.com</code></li>
<li><code>connectivitycheck.gstatic.com</code></li>
</ul>
<h2 id="connectivity-checks">Connectivity checks</h2>
<p>As part of establishing the WARP tunnel, the client runs connectivity checks inside and outside of the tunnel.</p>
<h3 id="outside-tunnel">Outside tunnel</h3>
<p>The client connects to the following destinations to verify general Internet connectivity outside of the WARP tunnel. Make sure that these IPs and domains are on your firewall allowlist.</p>
<ul>
<li><code>162.159.197.3</code></li>
<li><code>2606:4700:102::3</code></li>
<li><code>engage.cloudflareclient.com</code>: The client will always send requests directly to an IP in the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/#warp-ingress-ip">WARP ingress IPv4 or IPv6 range</a> (or to your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#override_warp_endpoint"><code>override_warp_endpoint</code></a> if set). Requests will not use a proxy server, even if one is configured for the system.</li>
</ul>
<p>Even though <code>engage.cloudflareclient.com</code> may resolve to different IP addresses, the Cloudflare One Client overrides the resolved IPs with the IPs listed above. To avoid connectivity issues, ensure that the above IPs are permitted through your firewall.</p>
<h3 id="inside-tunnel">Inside tunnel</h3>
<p>The Cloudflare One Client connects to the following destinations to verify connectivity inside of the WARP tunnel:</p>
<ul>
<li><code>162.159.197.4</code></li>
<li><code>2606:4700:102::4</code></li>
<li><code>connectivity.cloudflareclient.com</code></li>
</ul>
<p>Because this check happens inside of the tunnel, you do not need to add these IPs and domains to your firewall allowlist. However, since the requests go through Gateway, ensure that they are not blocked by a Gateway HTTP or Network policy.</p>
<h2 id="nel-reporting-optional">NEL reporting (optional)</h2>
<p>The Cloudflare One Client reports connectivity issues to the Network Error Logging (NEL) endpoint via <code>a.nel.cloudflare.com</code>. This is not technically required to operate but will result in errors in our logs if not excluded properly.</p>
<h2 id="latency-statistics-optional">Latency statistics (optional)</h2>
<p>The Cloudflare One Client generates ICMP traffic to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/#warp-ingress-ip">WARP ingress IPs</a> when running tunnel latency tests. This is not technically required to operate but will result in errors in our logs if not excluded properly.</p>
<h2 id="time-synchronization-optional">Time synchronization (optional)</h2>
<p>The Cloudflare One Client attempts to synchronize the exact time by NTP (<code>UDP 123</code>) to <a href="/time-services/ntp/usage/">Cloudflare's Time Service</a> via <code>time.cloudflare.com</code>. This is not technically required to operate but will result in errors in our logs if not excluded properly.</p>
<h2 id="scope-of-firewall-rules">Scope of firewall rules</h2>
<h3 id="required-scopes">Required scopes</h3>
<p>If your organization does not currently allow inbound/outbound communication over the IP addresses, ports, and domains described above, you must manually add an exception. The rule at a minimum needs to be scoped to the following process based on your platform:</p>
<ul>
<li>Windows: <code>C:\Program Files\Cloudflare\Cloudflare WARP\warp-svc.exe</code>, <code>C:\Program Files\Cloudflare\Cloudflare WARP\warp-updater.exe</code>, and <code>C:\Program Files\Cloudflare\Cloudflare WARP\warp-updater-armed.exe</code></li>
<li>macOS: You must explicitly allow the core networking daemon, updater, and GUI component as shown in the following instructions.
<ol>
<li>
<p>Core networking daemon: <code>/Applications/Cloudflare WARP.app/Contents/Resources/CloudflareWARP</code></p>
<p>This binary does not have a Bundle ID and must be allowed via full path.</p>
</li>
<li>
<p>Updater: <code>/Applications/Cloudflare WARP.app/Contents/Resources/warp-updater</code></p>
</li>
<li>
<p>GUI component, choose one of the following three identifiers depending on your MDM or firewall vendor's preferred format:</p>
<p><code>/Applications/Cloudflare WARP.app</code> (Path)</p>
<p><code>/Applications/Cloudflare WARP.app/Contents/MacOS/Cloudflare WARP</code> (Path)</p>
<p><code>com.cloudflare.1dot1dot1dot1.macos</code> (Bundle ID)</p>
</li>
</ol>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="macos-15-0-through-15-4">macOS 15.0 through 15.4</h3>
@markup("md", "content/.markup/bodies/6145.md")
</aside>
<h3 id="optional-scopes">Optional scopes</h3>
<h4 id="dex-tests">DEX tests</h4>
<p>To run <a href="/cloudflare-one/insights/dex/tests/">Digital Experience Monitoring tests</a>, you will need to allow the <code>warp-dex</code> process to generate network traffic to your target destinations:</p>
<ul>
<li>Windows: <code>C:\Program Files\Cloudflare\Cloudflare WARP\warp-dex.exe</code></li>
<li>macOS: <code>/Applications/Cloudflare WARP.app/Contents/Resources/warp-dex</code></li>
</ul>
<h4 id="network-statistics">Network statistics</h4>
<p>To use the network connectivity tests built into the Cloudflare One Client GUI, you will need to allow the GUI application to generate network traffic:</p>
<ul>
<li>Windows: <code>C:\Program Files\Cloudflare\Cloudflare WARP\Cloudflare WARP.exe</code></li>
<li>macOS: <code>/Applications/Cloudflare WARP.app</code></li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> - Resolve selected domains via local DNS instead of Cloudflare Gateway.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a> - Control which traffic goes through the Cloudflare One Client by including or excluding specific IPs or domains.</li>
</ul>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Required for HTTP/2 fallback</li></ol></section>
