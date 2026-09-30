<p>This guide helps you diagnose and resolve common issues with the Cloudflare One Client (formerly WARP). It covers how to troubleshoot the Cloudflare One Client on desktop operating systems, including Windows, macOS, and Linux.</p>
<ol>
<li><strong>Before you start</strong>: <a href="#prerequisites">Prerequisites</a>, permissions, <a href="#check-your-client-version">version control</a>, and client basics.</li>
<li><strong>Collect logs</strong>: Through the <a href="#option-a-collect-logs-via-the-cloudflare-dashboard">Cloudflare dashboard</a> (with DEX remote capture) or the <a href="#option-b-collect-logs-via-the-cli">command-line interface</a> (CLI) (<code>warp-diag</code>).</li>
<li><strong>Review logs</strong>: <a href="#check-client-status">Status</a>, <a href="#check-client-settings">settings</a>, <a href="#profile-id">profile ID</a>, <a href="#exclude-mode-with-hostsips">split tunnel</a> configuration, and other settings.</li>
<li><strong>Fix common misconfigurations</strong>: <a href="#wrong-profile-id">Profile mismatch</a>, <a href="#wrong-split-tunnel-configuration">split tunnel issues</a>, <a href="#review-your-managed-network-settings">managed network issues</a>, <a href="#check-a-users-group-membership">user group mismatch</a>.</li>
<li><strong>File a support ticket</strong>: <a href="#5-file-a-support-ticket">How to file a ticket</a> after you have exhausted your troubleshooting options.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="ai-assisted-troubleshooting">AI-assisted troubleshooting</h3>
@markup("md", "content/.markup/bodies/6071.md")
</aside>
<h2 id="1-before-you-start"><ol>
<li>Before you start</li>
</ol></h2>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li>You must have completed the <a href="/cloudflare-one/setup/">Zero Trust onboarding flow</a> with a Zero Trust organization created.</li>
<li>You must have the Cloudflare One Client installed on an end user device.</li>
<li>You must have a <a href="/cloudflare-one/roles-permissions/">role</a> that gives admin permission to access logs on the Cloudflare dashboard.</li>
</ul>
<h3 id="check-your-client-version">Check your client version</h3>
<p>Many troubleshooting issues are caused by outdated client versions. For the best performance and compatibility, administrators should check for new releases and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">update the Cloudflare One Client</a> before attempting to troubleshoot other issues.</p>
<p>After updating the Cloudflare One Client, monitor the issue to see if it recurs. If the issue persists, continue with the troubleshooting guide.</p>
<h4 id="via-the-device">Via the device</h4>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6074.md")
</div></div>
<h4 id="via-the-cloudflare-dashboard">Via the Cloudflare dashboard</h4>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Your devices</strong>.</li>
<li>Select the device you want to investigate.</li>
<li>Find the device's client version under <strong>Client version</strong> in the side menu.</li>
<li>Compare your device's version with the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">latest version of the Cloudflare One Client</a>.</li>
</ol>
<h3 id="client-basics">Client basics</h3>
<p>Understand the Cloudflare One Client's architecture, installation paths, and modes to help you diagnose issues with greater accuracy.</p>
<div class="video-frame"><img class="video-poster" src="https://imagedelivery.net/xDOJvHcv1KwTQn6S-BGFIw/4fdd3005-7995-4876-8faa-4375f9236500/public" alt="Understand Cloudflare WARP basics"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/31178cc41d0ec56d42ef892160589635/iframe?preload=true&amp;letterboxColor=transparent" title="Understand Cloudflare WARP basics" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h4 id="client-architecture">Client architecture</h4>
<p>The Cloudflare One Client consists of:</p>
<ul>
<li><strong>Graphical User Interface (GUI)</strong>: Control panel that allows end users to view the client's <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">status</a> and perform actions such as turning the Cloudflare One Client on or off.</li>
<li><strong>WARP daemon (or service)</strong>: Core background component responsible for establishing secure tunnels (using WireGuard or MASQUE) and handling all client functionality on your device.</li>
</ul>
<p>Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/">client architecture</a> for more information on how the Cloudflare One Client interacts with a device's operating system to route traffic.</p>
<h4 id="client-installation-details">Client installation details</h4>
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
<h4 id="client-modes">Client modes</h4>
<p>The Cloudflare One Client operates in several modes, each with different traffic handling capabilities:</p>
<p>Each client mode offers a different set of Zero Trust features.</p>
<table>
<thead>
<tr>
<th>Client mode</th>
<th>DNS Filtering</th>
<th>Network Filtering</th>
<th>HTTP Filtering</th>
<th>Service mode (displayed in <code>warp-cli settings</code>)</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#traffic-and-dns-mode-default"><strong>Traffic and DNS mode (default)</strong></a></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td><code>WarpWithDnsOverHttps</code></td>
</tr>
<tr>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#dns-only-mode"><strong>DNS only mode</strong></a></td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td><code>DnsOverHttps</code></td>
</tr>
<tr>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#traffic-only-mode"><strong>Traffic only mode</strong></a></td>
<td>❌</td>
<td>✅</td>
<td>✅</td>
<td><code>TunnelOnly</code></td>
</tr>
<tr>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode"><strong>Local proxy mode</strong></a></td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td><code>WarpProxy</code></td>
</tr>
<tr>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#posture-only-mode"><strong>Posture only mode</strong></a></td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td><code>PostureOnly</code></td>
</tr>
</tbody>
</table>
<h2 id="2-collect-diagnostic-logs"><ol start="2">
<li>Collect diagnostic logs</li>
</ol></h2>
<p>You can collect diagnostic logs in two ways: the <a href="#option-a-collect-logs-via-the-cloudflare-dashboard">Cloudflare dashboard</a> or the <a href="#option-b-collect-logs-via-the-cli"><code>warp-diag</code></a> command-line interface (CLI).</p>
<h3 id="option-a-collect-logs-via-the-cloudflare-dashboard">Option A: Collect logs via the Cloudflare dashboard</h3>
<p>Collect client diagnostic logs remotely from the Cloudflare dashboard by using Digital Experience Monitoring's (DEX) remote captures.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="best-practice">Best practice</h3>
@markup("md", "content/.markup/bodies/6070.md")
</aside>
<h4 id="start-a-remote-capture">Start a remote capture</h4>
<p>Devices must be actively connected to the Internet for remote captures to run.</p>
<p>To capture data from a remote device:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>DEX</strong> &gt; <strong>Remote captures</strong>.</li>
<li>Select up to 10 devices that you want to run a capture on. Devices must be <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">registered</a> in your Zero Trust organization.</li>
<li>Configure the types of captures to run.
<ul>
<li><strong>Packet captures (PCAP)</strong>: Performs packet captures for traffic outside of the WARP tunnel (default network interface) and traffic inside of the WARP tunnel (<a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#ip-traffic">virtual interface</a>).</li>
<li><strong>Device diagnostic logs</strong>: Generates a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#warp-diag-logs">Cloudflare One Client diagnostic log</a> of the past 96 hours. To include a routing test for all IPs and domains in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel configuration</a>, select <strong>Test all routes</strong>.</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6069.md")
</aside>
		 You must select Device Diagnostic Logs. You can also choose to run a PCAP and reproduce the issue in the window the PCAP is running to gain further network insight. The scope of this troubleshooting covers only client diagnostic logs. If not choosing PCAPs, reproduce the issue right before running diagnostics.
4. Select **Run diagnostics**.
<p>DEX will now send capture requests to the configured devices. If the Cloudflare One Client is disconnected, the capture will time out after 10 minutes.</p>
<h4 id="check-remote-capture-status">Check remote capture status</h4>
<p>To view a list of captures, go to <strong>Insights</strong> &gt; <strong>Digital experience</strong> &gt; <strong>Diagnostics</strong>. The <strong>Status</strong> column displays one of the following options:</p>
<ul>
<li><strong>Success</strong>: The capture is complete and ready for download. Any partially successful captures will still upload to Cloudflare. For example, there could be a scenario where the PCAP succeeds on the primary network interface but fails on the WARP tunnel interface. You can <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#download-remote-captures">review PCAP results</a> to determine which PCAPs succeeded or failed.</li>
<li><strong>Running</strong>: The capture is in progress on the device.</li>
<li><strong>Pending Upload</strong>: The capture is complete but not yet ready for download.</li>
<li><strong>Failed</strong>: The capture has either timed out or encountered an error. To retry the capture, check the Cloudflare One Client version and <a href="/cloudflare-one/insights/dex/monitoring/#fleet-status">connectivity status</a>, then start a <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#start-a-remote-capture">new capture</a>.</li>
</ul>
<h4 id="download-remote-captures">Download remote captures</h4>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>DEX</strong> &gt; <strong>Remote captures</strong>.</li>
<li>Find a successful capture.</li>
<li>Select the three-dot menu and select <strong>Download</strong>.</li>
</ol>
<p>This will download a ZIP file to your local machine called <code>&lt;capture-id&gt;.zip</code>. DEX will store capture data according to our <a href="/cloudflare-one/insights/logs/#log-retention">log retention policy</a>.</p>
<p>After you have your diagnostic files, go to <a href="#option-b-collect-logs-via-the-cli">Review key files</a> to continue troubleshooting.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="ai-assisted-troubleshooting-1">AI-assisted troubleshooting</h3>
@markup("md", "content/.markup/bodies/6068.md")
</aside>
<h3 id="option-b-collect-logs-via-the-cli">Option B: Collect logs via the CLI</h3>
<p>Collect client diagnostic logs on your desktop using the <code>warp-diag</code> CLI.</p>
<p>To view client logs on desktop devices:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6078.md")
</div></div>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="best-practice-1">Best practice</h3>
@markup("md", "content/.markup/bodies/6067.md")
</aside>
<p>After you have your diagnostic files, go to <a href="#option-b-collect-logs-via-the-cli">Review key files</a> to continue troubleshooting.</p>
<h2 id="3-review-key-files"><ol start="3">
<li>Review key files</li>
</ol></h2>
<p>Client diagnostic logs capture the final Cloudflare One Client configuration and status on a device after all MDM policies and other software settings have been applied. Reviewing these logs can help you identify misconfigurations or unexpected behavior.</p>
<div class="video-frame"><img class="video-poster" src="https://pub-d9bf66e086fb4b639107aa52105b49dd.r2.dev/Warp-diagnostics%20thumbnail.png" alt="WARP diagnostic logs"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/c29964ab3dcf7c3432ebb2b4e93c3aca/iframe?preload=true&amp;letterboxColor=transparent" title="WARP diagnostic logs" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h3 id="check-client-status">Check client status</h3>
<p>Open the <code>warp-status.txt</code> file to review the status of the Cloudflare One Client connection when the <code>warp-diag</code> was collected. A connected Cloudflare One Client will appear as:</p>
<pre><code>Ok(Connected)&#10;</code></pre>
<p>If the Cloudflare One Client is experiencing issues, the error will display in the Cloudflare One Client GUI on the device. Use the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/client-errors/">Client errors</a> documentation to identify your error, its cause, and the solution.</p>
<h3 id="check-client-settings">Check client settings</h3>
<p>After you have checked client status, review the Cloudflare One Client's settings on the device to check if the expected configuration has been applied. Open the <code>warp-settings.txt</code> file to review the Cloudflare One Client settings. You will check the device's applied device profile and split tunnel configuration.</p>
<h4 id="example-warp-settings-txt-file">Example <code>warp-settings.txt</code> file</h4>
<p>Find the client diagnostic logs on your desktop, and open the <code>warp-settings.txt</code> file. Review the following example <code>warp-settings.txt</code> file and the descriptions of its content below.</p>
<pre><code class="language-txt">Merged configuration:&#10;(derived)   Always On: true&#10;(network policy)    Switch Locked: false # If false, does not allow the user to turn off the WARP toggle and disconnect the WARP client&#10;(network policy)    Mode: WarpWithDnsOverHttps # The device&#x27;s WARP mode, this mode is WARP with Gateway mode&#10;(network policy)    WARP tunnel protocol: WireGuard&#10;(default)   Disabled for Wifi: false&#10;(default)   Disabled for Ethernet: false&#10;(reg defaults)  Resolve via: 1xx0x1011xx000000000f0x00000x11.cloudflare-gateway.com @ [1xx.1xx.1x.1, 1x01:1x00:1x00::1xx1] # The SNI Cloudflare will use and the IP address for DNS-over-HTTPS (DoH) requests&#10;(user set)  qlog logging: Enabled&#10;(default)   Onboarding: true # If true, the user sees an onboarding prompt when they first install the WARP client&#10;(network policy)    Exclude mode, with hosts/ips: # Split tunnel configuration&#10;  1xx.1xx.1xx.1xx/25 (zoom)&#10;...&#10;  cname.user.net&#10;&#10;(network policy)    Fallback domains: # Local domain fallback configuration&#10;  intranet&#10;...&#10;  test&#10;(not set)   Daemon Teams Auth: false&#10;(network policy)    Disable Auto Fallback: false&#10;(network policy)    Captive Portal: 180&#10;(network policy)    Support URL: my-organizations-support-portal.com # Your organization&#x27;s support portal or IT help desk&#10;(user set)  Organization: Organization-Name&#10;(network policy)    Allow Mode Switch: true  # The user is allowed to switch between WARP modes&#10;(network policy)    Allow Updates: false # WARP client will not perform update checks&#10;(network policy)    Allowed to Leave Org: true&#10;(api defaults)  Known apple connectivity check IPs: xx.xxx.0.0/16;&#10;(network policy)    LAN Access Settings: Allowed until reconnect on a /24 subnet # The maximum size of network that will be allowed when Access Lan is clicked.&#10;(network policy)    Profile ID: 000000x1-00x1-1xx0-1xx1-11101x1axx11&#10;</code></pre>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="quick-debugging">Quick debugging</h3>
@markup("md", "content/.markup/bodies/6066.md")
</aside>
<h4 id="contents-of-warp-settings-txt-file">Contents of <code>warp-settings.txt</code> file</h4>
<p>Review the meanings of the fields in <code>warp-settings.txt</code> that are relevant to troubleshooting.</p>
<h5 id="always-on">Always On</h5>
<p>Refers to the current state of the connection toggle in the GUI. In the example file, the toggle is switched on.</p>
<pre><code class="language-txt">Always On: true&#10;</code></pre>
<h5 id="switch-locked">Switch Locked</h5>
<p>Refers to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#lock-device-client-switch">Lock device client switch</a> which allows the user to use the client's connection toggle and disconnect the client. In the example file, the value is <code>false</code> meaning the user is able to connect or disconnect at their discretion.</p>
<pre><code class="language-txt">Switch Locked: false&#10;</code></pre>
<p>When <strong>Lock device client switch</strong> is enabled (<code>true</code>), users will need an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-admin-override-codes">admin override code</a> to temporarily disconnect the Cloudflare One Client on their device.</p>
<h5 id="mode">Mode</h5>
<p>Refers to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/">client mode</a> the device is using. In the example file, the client mode is <code>WarpWithDnsOverHttps</code> which is Traffic and DNS mode. Refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/">client modes comparison matrix</a> to match your <code>warp-settings.txt</code> file's value with the mode name.</p>
<pre><code class="language-txt">Mode: WarpWithDnsOverHttps&#10;</code></pre>
<h5 id="exclude-mode-with-hosts-ips">Exclude mode, with hosts/ips</h5>
<p>Refers to your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">split tunnel</a> settings. In the example file, the Cloudflare One Client is running in Exclude mode, meaning all traffic except for the traffic destined for these hosts and IPs will be sent through the WARP tunnel. The host <code>cname.user.net</code> and the IP <code>1xx.1xx.1xx.1xx/25 </code> are both excluded from the WARP tunnel.</p>
<pre><code class="language-txt">Exclude mode, with hosts/ips:&#10;  1xx.1xx.1xx.1xx/25 (zoom)&#10;...&#10;  cname.user.net&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="exclude-mode-versus-include-mode">Exclude mode versus Include mode</h3>
@markup("md", "content/.markup/bodies/6065.md")
</aside>
<h5 id="fallback-domains">Fallback domains</h5>
<p>Refers to your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> settings. In the example file, the Cloudflare One Client lists <code>intranet</code> as a domain that will not be sent to Gateway for processing and will instead be sent directly to the configured fallback servers.</p>
<pre><code class="language-txt">(network policy)    Fallback domains:&#10;  intranet&#10;...&#10;</code></pre>
<h5 id="allow-mode-switch">Allow Mode Switch</h5>
<p>Refers to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#mode-switch">Mode switch</a> setting. In the example file, the mode switch is enabled (<code>true</code>) which means the user has the option to switch between <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#traffic-and-dns-mode-default">Traffic and DNS mode</a> mode and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#dns-only-mode">Gateway with DNS-over-HTTPS (DoH)</a> mode.</p>
<pre><code class="language-txt">Allow Mode Switch: true&#10;</code></pre>
<h5 id="allow-updates">Allow Updates</h5>
<p>Refers to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-updates">Allow updates</a> setting. In the example file, the allow updates setting is set to <code>false</code> meaning that the user will not receive update notifications when a new version of the Cloudflare One Client is available and cannot update the client without administrator approval.</p>
<pre><code class="language-txt">Allow Updates: false&#10;</code></pre>
<p><strong>Allowed to Leave Org</strong></p>
<p>Refers to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-device-to-leave-organization">Allow device to leave organization</a> setting. In the example file, the value is set to <code>true</code> meaning the user can log out from your Zero Trust organization.</p>
<pre><code class="language-txt">Allowed to Leave Org: true&#10;</code></pre>
<p><strong>LAN Access Settings</strong></p>
<p>Refers to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion">Allow users to enable local network exclusion</a> setting. When enabled, it allows users to temporarily access local devices (like printers) by excluding the detected local subnet from the WARP tunnel. This example indicates access is allowed until the next client reconnection, and only for subnets up to <code>/24</code>.</p>
<pre><code class="language-txt">LAN Access Settings: Allowed until reconnect on a /24 subnet&#10;</code></pre>
<p><strong>Profile ID</strong></p>
<p>Refers to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">Device profile</a> a device is using. In this example, the ID is <code>000000x1-00x1-1xx0-1xx1-11101x1axx11</code>.</p>
<pre><code class="language-txt">Profile ID: 000000x1-00x1-1xx0-1xx1-11101x1axx11&#10;</code></pre>
<h2 id="4-fix-common-misconfigurations"><ol start="4">
<li>Fix common misconfigurations</li>
</ol></h2>
<p>To verify that the Cloudflare One Client is configured and working properly, review the following:</p>
<ol>
<li>Is the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/troubleshooting-guide/#edit-your-device-profile-match-rules">wrong profile ID</a> applied to the device?</li>
<li>Is the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/troubleshooting-guide/#wrong-split-tunnel-configuration">wrong split tunnel configuration</a> active on the device?</li>
</ol>
<h3 id="wrong-profile-id">Wrong profile ID</h3>
<p>A profile ID is a unique identifier assigned to each <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> in the Cloudflare dashboard, used to determine which configuration settings apply to a device.</p>
<h4 id="check-the-applied-device-profile">Check the applied device profile</h4>
<p>To check that the applied device profile is the intended device profile:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong> &gt; <strong>General profiles</strong>.</li>
<li>Find and select the device profile intended for the device.</li>
<li>Under <strong>Profile details</strong>, compare the displayed <strong>Profile ID</strong> with the <code>Profile ID</code> in the <code>warp-settings.txt</code> file.</li>
</ol>
<p>If your organization has multiple device profiles defined in the Cloudflare dashboard, a device may be matched to an unexpected profile because:</p>
<ul>
<li>How <a href="#review-profile-precedence">profile precedence</a> is configured.</li>
<li><a href="#review-your-managed-network-settings">Managed network</a> issues (if you are using a managed network.)</li>
<li>User group <a href="#check-a-users-group-membership">mismatch</a>.</li>
<li>Lack of <a href="#edit-your-device-profile-match-rules">precise match rules</a>.</li>
</ul>
<h4 id="review-profile-precedence">Review profile precedence</h4>
<p>The Cloudflare One Client evaluates device profiles dynamically based on a hierarchy. When a device connects, the client checks the profiles from top to bottom as they appear in the dashboard. The client follows the first match principle — once a device matches a profile, the client stops evaluating and no subsequent profiles can override the decision.</p>
<p>The <strong>Default</strong> profile is always at the bottom of the list. It will only be applied if the device does not meet the criteria of any profile listed above it. If you make another custom profile the default, all settings will be copied over into the <strong>Default</strong> profile.</p>
<p>Administrators can create multiple profiles to apply different settings based on specific criteria such as user identity, location, or operating system. Understanding this top-to-bottom evaluation order is crucial for ensuring that the correct policies are applied to devices.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6064.md")
</aside>
<h4 id="review-your-managed-network-settings">Review your managed network settings</h4>
<p>A <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/managed-networks/">managed network</a> is a network location that you define with a TLS endpoint, like a physical office. The Cloudflare One Client checks for this TLS endpoint to determine its location and apply the corresponding device profile.</p>
<p>If the managed network is misconfigured or the TLS endpoint is unreachable, the device may fall back to an unintended profile.</p>
<p>When troubleshooting the Cloudflare One Client for managed network issues:</p>
<ol>
<li>
<p>Verify the endpoint is reachable.</p>
<p>The Cloudflare One Client connects to the TLS endpoint to identify the network. If the endpoint is down or unreachable, the Cloudflare One Client will fail to detect the network and apply the wrong profile.</p>
</li>
</ol>
<p>To test connectivity and obtain the SHA-256 fingerprint of a remote server:</p>
<pre><code class="language-sh">openssl s_client -connect &lt;private-server-IP&gt;:443 &lt; /dev/null 2&gt; /dev/null | openssl x509 -noout -fingerprint -sha256 | tr -d :&#10;</code></pre>
<p>The output will look something like:</p>
<pre><code class="language-txt">SHA256 Fingerprint=DD4F4806C57A5BBAF1AA5B080F0541DA75DB468D0A1FE731310149500CCD8662&#10;</code></pre>
<p>If the endpoint is down, you will receive a <code>Could not find certificate from &lt;stdin&gt;</code> response.</p>
<p>If you received a returned SHA-256 fingerprint:</p>
<ol>
<li>
<p>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong>.</p>
</li>
<li>
<p>Go to <strong>Managed networks</strong> &gt; <strong>Edit</strong>.</p>
</li>
<li>
<p>Compare the TLS Cert SHA-256 in the dashboard with the returned fingerprint in your terminal to ensure they match.</p>
</li>
<li>
<p>Use a single profile for a single location.</p>
<p>To simplify management and prevent errors, avoid creating multiple managed network profiles for the same location. For example, if you have multiple TLS endpoints in one office, link them all to a single device profile. This reduces the risk of a device matching an unintended profile due to a configuration error.</p>
</li>
</ol>
<h4 id="check-a-user-s-group-membership">Check a user's group membership</h4>
<p>If a user is having issues with a device profile, it may be because they are not part of the correct user group. This can happen when an organization is not using SCIM for automatic identity provider (IdP) updates.</p>
<p>To check that the user belongs to the intended group:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Your devices</strong>.</li>
<li>Select the user.</li>
<li>Under <strong>User Registry Identity</strong>, select the user's name.</li>
<li>The <strong>Get-identity endpoint</strong> lists all the groups the user belongs to.</li>
</ol>
<p>If the user was recently added to a group, they will need to update their group membership with Cloudflare Zero Trust. This can be accomplished by logging into the reauthenticate endpoint.</p>
<p>To manually refresh your Cloudflare Access session and update your group information from your identity provider (IdP), go to the following URL in your browser and fill in your <a href="/cloudflare-one/faq/getting-started-faq/#what-is-a-team-domainteam-name">team name</a>:</p>
<p><code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/refresh-identity</code></p>
<p>Reauthenticating resets your <a href="/cloudflare-one/access-controls/access-settings/session-management/">session duration</a> and fetches the latest group information from the organization's IdP.</p>
<h4 id="edit-your-device-profile-match-rules">Edit your device profile match rules</h4>
<p>To modify the match rules of a device profile, you will need to edit the device profile. To edit the device profile:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong> &gt; <strong>General profiles</strong>.</li>
<li>Locate the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> you would like to update and select <strong>Configure</strong>.</li>
<li>Use <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/#selectors">selectors</a> to add or adjust match rules, and modify <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-settings">device client settings</a> for this profile as needed.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6063.md")
</aside>
<ol start="4">
<li>Select <strong>Save profile</strong>.</li>
</ol>
<p>It may take up to 10 minutes for newly updated settings to propagate to devices.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6062.md")
</aside>
<h3 id="wrong-split-tunnel-configuration">Wrong split tunnel configuration</h3>
<p>Split Tunnels can be configured to exclude or include IP addresses or domains from going through the Cloudflare One Client (formerly WARP). This feature is commonly used to run the Cloudflare One Client alongside a VPN (in Exclude mode) or to provide access to a specific private network (in Include mode).</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6061.md")
</aside>
<p>Because Split Tunnels controls what Gateway has visibility on at the network level, we recommend testing all changes before rolling out updates to end users.</p>
<p>A misconfigured <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">split tunnel</a> can cause connectivity issues.</p>
<p>For example, if you set your mode to Exclude IPs and domains and accidentally exclude an IP address needed by an application, that application may not work correctly. Similarly, in Include IPs and domains mode, forgetting to include a necessary IP or domain will cause traffic to bypass the Cloudflare One Client, and you will lose access to your Zero Trust security features.</p>
<h4 id="1-check-the-applied-split-tunnel-configuration"><ol>
<li>Check the applied split tunnel configuration</li>
</ol></h4>
<p>After downloading the client diagnostic logs, review that your configuration is working as intended:</p>
<ol>
<li>Open the <code>warp-settings.txt</code> file and find <code>Exclude mode, with hosts/ips:</code> or <code>Include mode, with hosts/ips:</code>.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="exclude-mode-versus-include-mode-1">Exclude mode versus Include mode</h3>
@markup("md", "content/.markup/bodies/6060.md")
</aside>
<ol start="2">
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong> &gt; <strong>General profiles</strong>.</li>
<li>Find and select the device profile intended for the device.</li>
<li>Select <strong>Edit</strong>.</li>
<li>Find <strong>Split Tunnels</strong> and note the mode you have selected &gt; select <strong>Manage</strong>.</li>
<li>Cross-reference the IPs/hosts you have configured in the Cloudflare dashboard with the IPs/hosts listed in <code>warp-settings.txt</code>.</li>
</ol>
<p>If your dashboard split tunnel configuration does not match your <code>warp-settings.txt</code> file configuration, you may need to force the Cloudflare One Client to <a href="#update-the-cloudflare-one-clients-settings">update its settings</a>.</p>
<h4 id="2-update-the-cloudflare-one-client-s-settings"><ol start="2">
<li>Update the Cloudflare One Client's settings</li>
</ol></h4>
<p>If the split tunnel configuration in <code>warp-settings.txt</code> does not match the dashboard, you can force the Cloudflare One Client to fetch the latest settings.</p>
<p>This can be done by instructing the end user to <a href="#option-a-disconnect-and-reconnect-the-client">disconnect and reconnect the client</a>, or <a href="#option-b-reset-the-encryption-keys">reset their encryption keys</a>.</p>
<p>Both methods update the client with the latest configuration.</p>
<p><strong>Option A: Disconnect and reconnect the client</strong></p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6081.md")
</div></div>
<p>The client will fetch new settings when it reconnects.</p>
<p><strong>Option B: Reset the encryption keys</strong></p>
<p>To reset the encryption keys on an end user's desktop:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6084.md")
</div></div>
<p>Resetting the encryption keys forces the client to reestablish its tunnel and retrieve the latest configuration.</p>
<h2 id="5-get-help"><ol start="5">
<li>Get help</li>
</ol></h2>
<p>For the fastest possible troubleshooting, ensure your support ticket includes comprehensive details. The more context you provide, the faster your issue can be identified and resolved.</p>
<p>To ensure efficient resolution when <a href="/support/contacting-cloudflare-support/">contacting support</a>, include as much relevant detail as possible in your ticket:</p>
<ul>
<pre><code>&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Context: Briefly describe the scenario or use&#10;		case (for example, where the user was, what they were trying to do).&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Reproduction steps: Describe the steps you took&#10;		to reproduce the issue during troubleshhooting.&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Timestamps: Be specific and include the exact&#10;		time and time zone when the issue occurred.&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Troubleshooting attempts: Outline any&#10;		troubleshooting steps or changes already attempted to resolve the issue.&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;label&gt;&#10;		&lt;input type=&quot;checkbox&quot; /&gt; Client diagnostics logs: Include the client&#10;		diagnostics you downloaded from the dashboard or through the CLI.&#10;	&lt;/label&gt;&#10;&lt;/li&gt;&#10;</code></pre>
</ul>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="write-a-detailed-ticket-to-resolve-your-issue-faster">Write a detailed ticket to resolve your issue faster</h3>
@markup("md", "content/.markup/bodies/6057.md")
</aside>
