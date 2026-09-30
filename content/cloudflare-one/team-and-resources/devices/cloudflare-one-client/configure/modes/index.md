<p>You can deploy the Cloudflare One Client (formerly WARP) in different modes to control the types of traffic sent to Cloudflare Gateway. The client mode determines which Zero Trust features are available on the device.</p>
<h2 id="traffic-and-dns-mode-default">Traffic and DNS mode (default)</h2>
<p>The Cloudflare One Client routes device traffic for all ports and protocols, and forwards DNS resolution to the <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/">client DNS resolver</a>.</p>
<p>Use when you want full security coverage, including DNS filtering, HTTP inspection, network firewall policies, and device posture checks.</p>
<table>
<thead>
<tr>
<th>DNS filtering</th>
<th>Network filtering</th>
<th>HTTP filtering</th>
<th>Features enabled</th>
</tr>
</thead>
<tbody>
<tr>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>DNS policies, network policies, HTTP policies, Browser Isolation, identity-based policies, device posture checks, AV scanning, and Data Loss Prevention</td>
</tr>
</tbody>
</table>
<h2 id="dns-only-mode">DNS only mode</h2>
<p>The Cloudflare One Client forwards DNS resolution to the Cloudflare account resolver, but does not route device traffic. Network and HTTP traffic is handled by the default mechanisms on your devices.</p>
<p>Use when you only want to apply DNS filtering to outbound traffic from your company devices.</p>
<table>
<thead>
<tr>
<th>DNS filtering</th>
<th>Network filtering</th>
<th>HTTP filtering</th>
<th>Features enabled</th>
</tr>
</thead>
<tbody>
<tr>
<td>Yes</td>
<td>No</td>
<td>No</td>
<td>DNS policies</td>
</tr>
</tbody>
</table>
<h2 id="traffic-only-mode">Traffic only mode</h2>
<p>The Cloudflare One Client routes device traffic for all ports and protocols. DNS resolution remains managed by the device operating system.</p>
<p>Use when you want to proxy network and HTTP traffic but keep your existing DNS filtering software.</p>
<table>
<thead>
<tr>
<th>DNS filtering</th>
<th>Network filtering</th>
<th>HTTP filtering</th>
<th>Features enabled</th>
</tr>
</thead>
<tbody>
<tr>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Network policies, HTTP policies, Browser Isolation, identity-based policies, device posture checks, AV scanning, and Data Loss Prevention</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6312.md")
</aside>
<h2 id="local-proxy-mode">Local proxy mode</h2>
<p>The Cloudflare One Client only forwards explicitly-directed local HTTP traffic.</p>
<p>Use when you want to filter traffic directed to specific applications.</p>
<table>
<thead>
<tr>
<th>DNS filtering</th>
<th>Network filtering</th>
<th>HTTP filtering</th>
<th>Features enabled</th>
</tr>
</thead>
<tbody>
<tr>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>HTTP policies, Browser Isolation, identity-based policies, AV scanning, and Data Loss Prevention for traffic sent through localhost proxy</td>
</tr>
</tbody>
</table>
<h3 id="set-up-local-proxy-mode">Set up Local proxy mode</h3>
<p>When you create a Cloudflare One account, a default <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> is created in Traffic and DNS mode. To set up Local proxy mode, you will need to edit the default device profile or create a new device profile and set the client mode to Local proxy mode.</p>
<p>The default profile is used for all devices that are not assigned to a specific profile. If you want to apply Local proxy mode to a specific group of devices, you will need to create a new device profile and assign it to those devices.</p>
<p>To set up Local proxy mode:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Teams &amp; Resources</strong> &gt; <strong>Device profiles</strong>.</li>
<li>Decide whether you would like to edit the default profile or create a new device profile.</li>
<li>Select the device profile you want to configure &gt; <strong>Edit</strong> (If you only see <strong>View</strong>, you lack the permissions required to modify profiles).</li>
<li>Ensure the <strong>Device tunnel protocol</strong> is set to <code>MASQUE</code>.</li>
<li>Under <strong>Service mode</strong>, select <strong>Local proxy mode</strong>.</li>
<li>Select <strong>Save profile</strong>.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="mdm-deployment">MDM deployment</h3>
@markup("md", "content/.markup/bodies/6311.md")
</aside>
<p>For devices using Local proxy mode, the Cloudflare One Client listens on the configured port at the address <code>127.0.0.1</code> (<code>localhost</code>). Cloudflare uses <code>40000</code> as the default port for the Cloudflare One Client in Local proxy mode, but you can modify this to any available port. You must explicitly configure individual applications or your system proxy settings to use this proxy.</p>
<p>Once configured, traffic to and from these applications will securely tunnel through the Cloudflare One Client.</p>
<p>To make more complex routing decisions (such as, routing traffic directly to the Internet or other proxies), you can use a <a href="/learning-paths/secure-internet-traffic/configure-device-agent/pac-files/">PAC file</a>.</p>
<h3 id="limitations">Limitations</h3>
<ul>
<li>Local proxy mode can only be used by applications/operating systems that support SOCKS5/HTTP proxy communication.</li>
<li>Requires the MASQUE <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">device tunnel protocol</a>. Wireguard is not supported.</li>
<li>Only available on Windows, Linux, and macOS.</li>
<li>Local proxy mode has a timeout limit of 10 seconds for requests. If a request goes above the 10 second limit, Cloudflare will drop the connection.</li>
</ul>
<h2 id="posture-only-mode">Posture only mode</h2>
<p>The Cloudflare One Client collects device health and posture data, which you can reference in your security policies. The client does not route traffic or forward DNS queries in this mode.</p>
<p>Use when you only want to enforce <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client device posture checks</a> for zones in your account. To set up Posture only mode, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/device-information-only/">dedicated page</a>.</p>
<table>
<thead>
<tr>
<th>DNS filtering</th>
<th>Network filtering</th>
<th>HTTP filtering</th>
<th>Features enabled</th>
</tr>
</thead>
<tbody>
<tr>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Device posture rules in <a href="/cloudflare-one/access-controls/policies/">Access policies</a></td>
</tr>
</tbody>
</table>
<h2 id="modes-comparison">Modes comparison</h2>
<p>Each client mode offers a different set of Zero Trust features.</p>
<table>
<thead>
<tr>
<th>Client mode</th>
<th>Best for</th>
<th>DNS Filtering</th>
<th>Network Filtering</th>
<th>HTTP Filtering</th>
<th>Service mode (displayed in <code>warp-cli settings</code>)</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#traffic-and-dns-mode-default"><strong>Traffic and DNS mode (default)</strong></a></td>
<td>Full security with all filtering capabilities</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td><code>WarpWithDnsOverHttps</code></td>
</tr>
<tr>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#dns-only-mode"><strong>DNS only mode</strong></a></td>
<td>DNS filtering without routing device traffic</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td><code>DnsOverHttps</code></td>
</tr>
<tr>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#traffic-only-mode"><strong>Traffic only mode</strong></a></td>
<td>Traffic routing with existing DNS infrastructure</td>
<td>❌</td>
<td>✅</td>
<td>✅</td>
<td><code>TunnelOnly</code></td>
</tr>
<tr>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode"><strong>Local proxy mode</strong></a></td>
<td>Filtering traffic to specific applications</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td><code>WarpProxy on port 40000</code></td>
</tr>
<tr>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#posture-only-mode"><strong>Posture only mode</strong></a></td>
<td>Device posture checks without traffic routing</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td><code>PostureOnly</code></td>
</tr>
</tbody>
</table>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a> - Learn about the status messages displayed by the Cloudflare One Client during its connection process, and understand each stage as the client establishes a secure tunnel to Cloudflare.</li>
</ul>
