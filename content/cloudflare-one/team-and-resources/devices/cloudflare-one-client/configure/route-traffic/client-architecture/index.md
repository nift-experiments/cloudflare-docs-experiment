<p>This guide explains how the Cloudflare One Client (formerly WARP) interacts with a device's operating system to route traffic in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#traffic-and-dns-mode-default">Traffic and DNS mode</a> mode.</p>
<p>In <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#dns-only-mode">DNS only mode</a> mode, the IP traffic information does not apply. In <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#traffic-only-mode">Traffic only mode</a> mode, the DNS traffic information does not apply.</p>
<h2 id="client-traffic-flow">Client traffic flow</h2>
<p>The Cloudflare One Client allows organizations to have granular control over the applications an end user device can access. The client forwards DNS and network traffic from the device to Cloudflare's global network, where Zero Trust policies are applied in the cloud. On all operating systems, the WARP daemon maintains three connections between the device and Cloudflare:</p>
<table>
<thead>
<tr>
<th>Connection</th>
<th>Protocol</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>WARP tunnel (<a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">via WireGuard or MASQUE</a>)</td>
<td>UDP</td>
<td>Send IP packets to Gateway for network policy enforcement, HTTP policy enforcement, and private network access.</td>
</tr>
<tr>
<td><a href="https://www.cloudflare.com/learning/dns/dns-over-tls/">DoH</a></td>
<td>HTTPS</td>
<td>Send DNS requests to Gateway for DNS policy enforcement. The DoH connection is maintained inside of the WARP tunnel.</td>
</tr>
<tr>
<td>Device orchestration</td>
<td>HTTPS</td>
<td>Perform user registration, check device posture, apply device client profile settings.</td>
</tr>
</tbody>
</table>
<pre><code class="language-mermaid">flowchart LR&#10;subgraph Device&#10;W[Cloudflare One Client] -.-&gt; D&#10;D[DNS proxy]&#10;W -.-&gt; V[Virtual interface]&#10;end&#10;subgraph Cloudflare&#10;A[Zero Trust account]&#10;subgraph Gateway&#10;N[L3/L4 firewall]&#10;G[DNS resolver]&#10;end&#10;end&#10;W&lt;--&quot;Device&#10;orchestration&quot;--&gt;A&#10;subgraph tunnel[&quot;WARP tunnel&quot;]&#10; ip@{ shape: text, label: &quot;Network traffic&quot; }&#10;  dns@{ shape: text, label: &quot;DNS traffic&quot; }&#10;end&#10;V --- ip--&gt;N&#10;D --- dns--&gt;G&#10;N --&gt; O[(Application)]&#10;</code></pre>
<p>Your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel</a> configuration determines what IP traffic is sent down the WARP tunnel. Your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> configuration determines which DNS requests are sent to Gateway via DoH. Traffic to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/#client-orchestration-api">device orchestration API</a> endpoint does not obey Split Tunnel rules since the connection always operates outside of the WARP tunnel.</p>
<p>Next, you will learn how the Cloudflare One Client configures your operating system to apply your Local Domain Fallback and Split Tunnel routing rules. Implementation details differ between desktop and mobile clients.</p>
<h2 id="windows-macos-and-linux">Windows, macOS, and Linux</h2>
<p>The desktop client consists of two components: a service/daemon that handles all client functionality on your device, and a GUI wrapper that makes it easier for a user to interact with the daemon.</p>
<h3 id="dns-traffic">DNS traffic</h3>
<p>When you connect the Cloudflare One Client, the client creates a local DNS proxy on the device and binds it to these IP addresses on port 53 (the port designated for DNS traffic):</p>
<ul>
<li><strong>IPv4</strong>: <code>127.0.2.2</code> and <code>127.0.2.3</code></li>
<li><strong>IPv6</strong>:
<ul>
<li>macOS and Linux: <code>fd01:db8:1111::2</code> and <code>fd01:db8:1111::3</code></li>
<li>Windows: <code>::ffff:127.0.2.2</code></li>
</ul>
</li>
</ul>
<p>The Cloudflare One Client then configures the operating system to send all DNS requests to these IP addresses. All network interfaces on the device will now use this local DNS proxy for DNS resolution. In other words, all DNS traffic will now be handled by the Cloudflare One Client.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6298.md")
</aside>
<p>Based on your Local Domain Fallback configuration, the Cloudflare One Client will either forward the request to Gateway for DNS policy enforcement or forward the request to your private DNS resolver.</p>
<ul>
<li>Requests to Gateway are sent over our <a href="#overview">DoH connection</a> inside the WARP tunnel.</li>
<li>Requests to your private DNS resolver are sent either inside or outside of the tunnel depending on your Split Tunnel configuration. For more information, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/#how-the-cloudflare-one-client-handles-dns-requests">How the Cloudflare One Client handles DNS requests</a>.</li>
</ul>
<pre><code class="language-mermaid">flowchart LR&#10;D{{DNS request}}--&gt;L[&quot;Local DNS proxy &lt;br&gt; (127.0.2.2 and 127.0.2.3)&quot;]--&gt;R{In local domain fallback?}&#10;R -- Yes --&gt; F[Private DNS resolver]&#10;R -- No --&gt; G[Cloudflare Gateway]&#10;</code></pre>
<p>You can verify that the operating system is using the Cloudflare One Client's local DNS proxy:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6302.md")
</div></div>
<h3 id="ip-traffic">IP traffic</h3>
<p>When you connect the Cloudflare One Client, it makes three changes on the device to control if traffic is sent inside or outside of the WARP tunnel:</p>
<ul>
<li>Creates a <a href="#virtual-interface">virtual network interface</a>.</li>
<li>Modifies the operating system <a href="#routing-table">routing table</a> according to your Split Tunnel rules.</li>
<li>Modifies the operating system <a href="#system-firewall">firewall</a> according to your Split Tunnel rules.</li>
</ul>
<pre><code class="language-mermaid">flowchart LR&#10;P{{IP packet}}--&gt;R[&quot;OS routing table&quot;]--&gt;F[&quot;OS firewall&quot;] --&gt; S{Excluded from Split Tunnels?}&#10;S -- Yes --&gt; A[(Application)]&#10;S -- No --&gt; U[&quot;Virtual interface&lt;br&gt; (172.16.0.2)&quot;] --&gt; G[Cloudflare Gateway]&#10;</code></pre>
<h4 id="virtual-interface">Virtual interface</h4>
<p>Virtual interfaces allow the operating system to logically subdivide a physical interface, such as a network interface controller (NIC), into separate interfaces for the purposes of routing IP traffic. The Cloudflare One Client's virtual interface is what maintains the WireGuard/MASQUE connection between the device and Cloudflare. By default, its IPv4 address is hardcoded as <code>172.16.0.2</code> for devices using WireGuard, whereas devices using MASQUE are <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#assign-a-unique-ip-address-to-each-device">assigned a unique IP</a> from the CGNAT IP space (<code>100.96.0.0/12</code>). You can override the default virtual interface IP with a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-ips/">custom device IP</a>.</p>
<p>To view a list of all network interfaces on the operating system:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6306.md")
</div></div>
<p>In the example above, the device IPv4 address is <code>172.16.0.2</code>.</p>
<h4 id="routing-table">Routing table</h4>
<p>The Cloudflare One Client edits the system routing table to control what IP traffic goes to Gateway. The routing table indicates which network interface should handle packets to a particular IP address. By default, all traffic routes through the Cloudflare One Client's virtual interface except for the IPs and domains on your Split Tunnel exclude list (which use the default interface on your device).</p>
<p>You can verify that the routing table matches your Split Tunnel rules:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6310.md")
</div></div>
<h4 id="system-firewall">System firewall</h4>
<p>The Cloudflare One Client modifies the operating system firewall to enforce your Split Tunnel rules. This adds a layer of protection in case a service bypasses the routing table and tries to send traffic directly through another interface. For example, if traffic to <code>203.0.113.0</code> is supposed to be inspected by Gateway, we create a firewall rule that blocks <code>203.0.113.0</code> on all interfaces except for <code>utun</code>.</p>
<h2 id="ios-android-and-chromeos">iOS, Android, and ChromeOS</h2>
<p>On iOS and Android/ChromeOS, the Cloudflare One Agent installs itself as a VPN client to capture and route all traffic. The app is built on the official VPN framework for iOS and Android. For more information, refer to Apple's <a href="https://developer.apple.com/documentation/networkextension">NetworkExtension documentation</a> and Google's <a href="https://developer.android.com/guide/topics/connectivity/vpn">Android developer documentation</a>.</p>
<p>Note that ChromeOS runs the Android app in a virtual machine, rather than running a native Chrome app.</p>
