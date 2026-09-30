<h2 id="about-the-cloudflare-one-client">About the Cloudflare One Client</h2>
<p>The Cloudflare One Client (formerly WARP) securely and privately sends traffic from your devices to Cloudflare's global network, where <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> can apply advanced web filtering. The client also reports device health information — such as OS version, disk encryption status, and the presence of specific applications — so that you can enforce <a href="/cloudflare-one/reusable-components/posture-checks/">device posture checks</a> in your Access and Gateway policies.</p>
<h2 id="how-the-cloudflare-one-client-works">How the Cloudflare One Client works</h2>
<p>The Cloudflare One Client creates encrypted connections between your device and Cloudflare's network. It does this in two ways:</p>
<ul>
<li><strong>Proxy tunnel</strong> — Encrypts and routes your device's internet and private network traffic through Cloudflare, using the <a href="https://www.wireguard.com/">WireGuard</a> or <a href="https://blog.cloudflare.com/zero-trust-warp-with-a-masque">MASQUE</a> protocol.</li>
<li><strong>DNS proxy</strong> — Sends your device's DNS queries to Cloudflare over an encrypted channel (<a href="https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/">DNS-over-HTTPS</a>), where <a href="/cloudflare-one/traffic-policies/dns-policies/">Gateway DNS policies</a> can filter them.</li>
</ul>
<p>The client runs on all major operating systems and can be deployed through common endpoint management tools (such as Intune, JAMF, or JumpCloud).</p>
<p>The Cloudflare One Client consists of:</p>
<ul>
<li><strong>Graphical User Interface (GUI):</strong> A control panel that allows end users to view the client's <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">status</a> and perform actions such as connecting or disconnecting.</li>
<li><strong>WARP daemon (or service):</strong> The core background process responsible for establishing the encrypted connections described above and handling all client functionality on your device.</li>
</ul>
<p>For more information on how the Cloudflare One Client routes traffic, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/">client architecture page</a> and watch the video below.</p>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/31178cc41d0ec56d42ef892160589635/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2F4fdd3005-7995-4876-8faa-4375f9236500%2Fpublic" title="Understand Cloudflare WARP basics" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div><details class="nb-details video-chapters"><summary>Chapters</summary><ul><li><button type="button" data-video-time="0"><img src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/31178cc41d0ec56d42ef892160589635/thumbnails/thumbnail.jpg?fit=crop&amp;time=0s" alt="Introduction and WARP GUI Basics"><strong>Introduction and WARP GUI Basics</strong><span>0s</span></button></li><li><button type="button" data-video-time="57"><img src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/31178cc41d0ec56d42ef892160589635/thumbnails/thumbnail.jpg?fit=crop&amp;time=57s" alt="Consumer vs. Corporate WARP"><strong>Consumer vs. Corporate WARP</strong><span>57s</span></button></li><li><button type="button" data-video-time="95"><img src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/31178cc41d0ec56d42ef892160589635/thumbnails/thumbnail.jpg?fit=crop&amp;time=95s" alt="Device Profiles Explained"><strong>Device Profiles Explained</strong><span>1m35s</span></button></li><li><button type="button" data-video-time="132"><img src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/31178cc41d0ec56d42ef892160589635/thumbnails/thumbnail.jpg?fit=crop&amp;time=132s" alt="WARP Operating Modes"><strong>WARP Operating Modes</strong><span>2m12s</span></button></li><li><button type="button" data-video-time="224"><img src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/31178cc41d0ec56d42ef892160589635/thumbnails/thumbnail.jpg?fit=crop&amp;time=224s" alt="Split Tunneling"><strong>Split Tunneling</strong><span>3m44s</span></button></li><li><button type="button" data-video-time="296"><img src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/31178cc41d0ec56d42ef892160589635/thumbnails/thumbnail.jpg?fit=crop&amp;time=296s" alt="Conclusion"><strong>Conclusion</strong><span>4m56s</span></button></li></ul></details>
<h2 id="installation-details">Installation details</h2>
<p>The GUI and daemon (or service) have different names and are stored in the following locations:</p>
<details>
<summary>Windows</summary>
<table>
<thead>
<tr>
<th></th>
<th>Windows</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Service / Daemon</strong></td>
<td><code>C:\Program Files\Cloudflare\Cloudflare WARP\warp-svc.exe</code></td>
</tr>
<tr>
<td><strong>GUI application</strong></td>
<td><code>C:\Program Files\Cloudflare\Cloudflare WARP\Cloudflare WARP.exe</code></td>
</tr>
<tr>
<td><strong>Logs Location</strong></td>
<td><details><summary>Daemon</summary><code>C:\ProgramData\Cloudflare\</code></details><br/><details><summary>GUI Logs</summary><code>C:\Users\&lt;USER&gt;.WARP\AppData\Local</code><br/>or<br/><code>%LOCALAPPDATA%\Cloudflare</code></details></td>
</tr>
</tbody>
</table>
</details>
<details>
<summary>macOS</summary>
<table>
<thead>
<tr>
<th></th>
<th>macOS</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Service / Daemon</strong></td>
<td><code>/Applications/Cloudflare WARP.app/Contents/Resources/CloudflareWARP</code></td>
</tr>
<tr>
<td><strong>GUI application</strong></td>
<td><code>/Applications/Cloudflare WARP.app/Contents/MacOS/Cloudflare WARP</code></td>
</tr>
<tr>
<td><strong>Logs Location</strong></td>
<td><details><summary>Daemon</summary><code>/Library/Application Support/Cloudflare/</code></details><details><summary>GUI Logs</summary><code>~/Library/Logs/Cloudflare/</code></details></td>
</tr>
</tbody>
</table>
</details>
<details>
<summary>Linux</summary>
<table>
<thead>
<tr>
<th></th>
<th>Linux</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Service / Daemon</strong></td>
<td><code>/bin/warp-svc</code></td>
</tr>
<tr>
<td><strong>GUI application</strong></td>
<td><code>/bin/warp-taskbar</code></td>
</tr>
<tr>
<td><strong>Logs Location</strong></td>
<td><code>/var/log/cloudflare-warp/</code><br/><code>/var/lib/cloudflare-warp</code></td>
</tr>
</tbody>
</table>
</details>
<p>Along with the Cloudflare One Client GUI and daemon, <code>warp-cli</code> and <code>warp-diag</code> are also <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">installed</a> on the machine and added to the system path for use from any terminal session.</p>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/"><code>warp-diag</code></a> is a command-line diagnostics tool that collects logs, configuration details, and connectivity data from the Cloudflare One Client to help troubleshoot issues.</p>
<p><code>warp-cli</code> is the command-line interface (CLI) for managing and configuring the Cloudflare One Client, allowing users to connect, disconnect, and adjust settings programmatically.</p>
<h2 id="key-benefits-of-using-the-cloudflare-one-client">Key benefits of using the Cloudflare One Client</h2>
<p>Deploying the Cloudflare One Client significantly enhances your organization's security and visibility within Cloudflare Zero Trust:</p>
<ul>
<li>
<p><strong>Unified security policies everywhere</strong>: With the Cloudflare One Client deployed in the Traffic and DNS mode, <a href="/cloudflare-one/traffic-policies/">Gateway policies</a> are not location-dependent — they can be enforced anywhere.</p>
</li>
<li>
<p><strong>Advanced web filtering and threat protection</strong>: Activate Gateway features for your device traffic, including:</p>
<pre><code>- [Anti-Virus scanning](/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/)&#10;- [HTTP filtering](/cloudflare-one/traffic-policies/http-policies/)&#10;- [Browser Isolation](/cloudflare-one/traffic-policies/http-policies/#isolate)&#10;- [Identity-based policies](/cloudflare-one/traffic-policies/network-policies/)&#10;</code></pre>
</li>
<li>
<p><strong>Application and device-specific insights</strong>: View which SaaS applications your users are accessing and review their approval status on the <a href="/cloudflare-one/insights/analytics/shadow-it-discovery/">Shadow IT Discovery</a> page. Monitor device and network performance with <a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> to detect connectivity or performance issues before users report them.</p>
</li>
<li>
<p><strong>Device posture checks</strong>: The Cloudflare One Client provides advanced Zero Trust protection by making it possible to check for <a href="/cloudflare-one/reusable-components/posture-checks/">device posture</a>. By setting up device posture checks, you can build Access or Gateway policies that check for a device's location, disk encryption status, OS version, and more.</p>
</li>
<li>
<p><strong>Secure private and infrastructure access</strong>: Connect devices to internal networks and applications through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/">Cloudflare Tunnel</a> without exposing them to the public internet. The client is also required for <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">Access for Infrastructure</a>, which provides SSH access using short-lived certificates and detailed audit logging.</p>
</li>
</ul>
<h2 id="client-modes">Client modes</h2>
<p>The Cloudflare One Client offers flexible <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/">operating modes</a> to suit your specific needs:</p>
<ul>
<li><strong>Traffic and DNS mode</strong> (default) — Routes device traffic (by default, all ports and protocols) and DNS queries through Cloudflare for filtering, inspection, and policy enforcement. Traffic exclusions can be configured with <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a>.</li>
<li><strong>DNS-only mode</strong> — Routes only DNS queries through Cloudflare. Use this mode if you only need DNS-level filtering without inspecting web or application traffic.</li>
</ul>
<p>Other modes (Traffic only, Local proxy, Posture only) are also available. For details, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/">operating modes</a> page.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Review the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/set-up/">first-time setup</a> guide to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">install</a> and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deploy</a> the Cloudflare One Client on your corporate devices.</li>
<li>Review possible <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/">client modes</a> and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/">settings</a> to best suit your organization's needs.</li>
<li>Explore <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> to enforce advanced DNS, network, HTTP, and egress policies with the Cloudflare One Client.</li>
</ul>
