<p>Below, you will find information on devices, software, and configurations that are incompatible with the Cloudflare One Client (formerly WARP).</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="troubleshoot-the-cloudflare-one-client">Troubleshoot the Cloudflare One Client</h3>
@markup("md", "content/.markup/bodies/6086.md")
</aside>
<h2 id="windows-server">Windows Server</h2>
<p>The Cloudflare One Client does not run on Windows Server. Refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">downloads page</a> for a list of supported operating systems.</p>
<h2 id="cloudflare-one-client-disconnected-on-windows-arm">Cloudflare One Client disconnected on Windows ARM</h2>
<p>On Windows devices with ARM-based processors, the Cloudflare One Client can sometimes get <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/common-issues/#unable-to-connect-warp">stuck in a disconnected state</a> when you connect (such as when installing the Cloudflare One Client for the first time).</p>
<p>To work around this issue, you can temporarily remove the WARP network adapter:</p>
<ol>
<li>Open the Cloudflare One Client GUI and disconnect.</li>
<li>In Windows, open Device Manager.</li>
<li>Select <strong>View</strong> &gt; <strong>Show hidden devices</strong>.</li>
<li>Under <strong>Network adapters</strong>, find <strong>Cloudflare WARP Interface Tunnel</strong> and select <strong>Uninstall device</strong>.</li>
<li>Select <strong>Attempt to remove the drive for this device</strong>, then select <strong>Uninstall</strong>.</li>
<li>Reconnect the Cloudflare One Client.</li>
</ol>
<p>The Cloudflare One Client will now reinstall its network adapter, and the Cloudflare One Client GUI should now show <strong>Connected</strong>.</p>
<h2 id="managed-network-on-legacy-windows-server">Managed network on legacy Windows Server</h2>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/managed-networks/">Managed network detection</a> will not work when the TLS certificate is served from IIS 8.5 on Windows Server 2012 R2. To work around the limitation, move the certificate to a different host.</p>
<h2 id="nslookup-on-windows-in-doh-mode">nslookup on Windows in DoH mode</h2>
<p>On Windows devices in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#dns-only-mode">DNS only mode</a>, <code>nslookup</code> by default sends DNS requests to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#dns-traffic">WARP local DNS proxy</a> over IPv6. However, because the Cloudflare One Client uses an IPv4-mapped IPv6 address (instead of a real IPv6 address), <code>nslookup</code> will not recognize this address type and the query will fail:</p>
<pre><code class="language-txt">C:\Users\JohnDoe&gt;nslookup google.com&#10;Server:  UnKnown&#10;Address:  ::ffff:127.0.2.2&#10;&#10;&#42;** UnKnown can&#x27;t find google.com: No response from server&#10;</code></pre>
<p>To work around the issue, specify the IPv4 address of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#dns-traffic">WARP local DNS proxy</a> in your query:</p>
<pre><code class="language-bash">C:\Users\JohnDoe&gt;nslookup google.com 127.0.2.2&#10;</code></pre>
<p>Alternatively, use PowerShell:</p>
<pre><code class="language-powershell">Resolve-DnsName -Name google.com&#10;</code></pre>
<h2 id="comcast-dns-servers">Comcast DNS servers</h2>
<p>Comcast DNS traffic (to the IPs below) cannot be proxied through the Cloudflare One Client. This is because Comcast rejects DNS traffic that is not sent directly from the user's device.</p>
<ul>
<li>IPv4 Addresses: <code>75.75.75.75</code> and <code>75.75.76.76</code></li>
<li>IPv6 Addresses: <code>2001:558:feed::1</code> and <code>2001:558:feed::2</code></li>
</ul>
<p>To work around the issue, you can either:</p>
<ul>
<li>Create a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel rule</a> that excludes the above IPs from the Cloudflare One Client.</li>
<li>Configure your device or router to use a public DNS server such as <a href="https://1.1.1.1/dns/"><code>1.1.1.1</code></a>.</li>
</ul>
<h2 id="cox-dns-servers">Cox DNS servers</h2>
<p>Similar to the <a href="#comcast-dns-servers">Comcast DNS servers</a> limitation listed above, Cox DNS servers will not respond to traffic from the WARP egress IPs (or any IP that is not a Cox IP). The workaround is nearly identical, except that Cox DNS servers may be specific to the individual end user. You can either:</p>
<ul>
<li>Create a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel rule</a> that excludes all Cox DNS servers. For business customers, refer to the <a href="https://www.cox.com/business/support/cox-business-dns-and-mail-exchange-hosting-services.html">COX documentation</a> for the DNS server IPs. For residential customers, check your local DNS servers. The residential DNS servers typically fall under <code>68.105.28.0/24</code> and <code>68.105.29.0/24</code>.</li>
<li>Configure your device or router to use a public DNS server such as <a href="https://1.1.1.1/dns/"><code>1.1.1.1</code></a>.</li>
</ul>
<h2 id="hp-velocity">HP Velocity</h2>
<p>The HP Velocity driver has a bug which will cause a blue screen error on devices running the Cloudflare One Client. HP recommends <a href="https://support.hp.com/gb-en/document/c06266198">uninstalling this driver</a>.</p>
<h2 id="dell-firmware-version-1-35-0">Dell firmware version 1.35.0</h2>
<p>For Dell devices running firmware version <code>1.35.0</code> (released 2025-07-07), regardless of operating system, Cloudflare has confirmed a bug that prevents the WARP service from starting. Cloudflare recommends users experiencing these issues upgrade their Dell device firmware to version <code>1.36.0</code> or later.</p>
<h2 id="cisco-meraki">Cisco Meraki</h2>
<p>Cisco Meraki devices have a bug where client traffic can sometimes be identified as <a href="https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/qos_nbar/prot_lib/config_library/pp4600/nbar-prot-pack4600/s.html#wp1488575851"><code>Statistical-P2P</code></a> and de-prioritised or dropped entirely. To resolve the issue, disable <code>Statistical-P2P</code> on the Cisco Meraki device.</p>
<h2 id="windows-teredo">Windows Teredo</h2>
<p>The <a href="https://learn.microsoft.com/en-us/windows/win32/teredo/about-teredo">Windows Teredo</a> interface conflicts with the Cloudflare One Client. Since Teredo and the Cloudflare One Client will fight for control over IPv6 traffic routing, you must disable Teredo on your Windows device. This allows the Cloudflare One Client to provide IPv6 connectivity on the device.</p>
<h2 id="docker-on-linux-with-bridged-networking">Docker on Linux with bridged networking</h2>
<p><a href="https://www.docker.com/products/container-runtime/">Docker</a> on Linux does not perform the underlying network tunnel MTU changes required by the Cloudflare One Client. This can cause connectivity issues inside of a Docker container when the Cloudflare One Client is enabled on the host machine. For example, <code>curl -v https://cloudflare.com &gt; /dev/null</code> will fail if run from a Docker container that is using the default bridge network driver.</p>
<p>To work around this issue, users of the Cloudflare One Client with Docker on Linux can manually reconfigure the MTU on Docker's network interface. You can either modify <code>/etc/docker/daemon.json</code> to include:</p>
<pre><code class="language-json">{&#10;	&quot;mtu&quot;: 1420&#10;}&#10;</code></pre>
<p>or create a Docker network with a working MTU value:</p>
<pre><code class="language-sh">docker network create -o &quot;com.docker.network.driver.mtu=1420&quot; my-docker-network&#10;</code></pre>
<p>The MTU value should be set to the MTU of your host's default interface minus 80 bytes for the WARP protocol overhead. Most MTUs are 1500, so 1420 should work for most users.</p>
<h2 id="access-cloudflare-one-client-dns-from-docker">Access Cloudflare One Client DNS from Docker</h2>
<p>The Cloudflare One Client runs a local DNS proxy on <code>127.0.2.2</code> and <code>127.0.2.3</code>. You may need access to these addresses from within Docker containers to resolve internal-only or fallback domains. The default Docker <a href="https://docs.docker.com/engine/network/drivers/bridge/">bridge network</a> copies the DNS settings from the host, but filters out loopback DNS addresses like <code>127.0.2.2</code> and <code>127.0.2.3</code>, so containers cannot use them.</p>
<p>To enable Cloudflare One Client DNS resolution with containers:</p>
<ul>
<li>Use a <a href="https://docs.docker.com/engine/network/#user-defined-networks">custom Docker network</a> (recommended): Allows the Docker container to still use the bridge network driver that maintains network isolation from the host. If you are creating your own bridge network, you should also <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/known-limitations/#docker-on-linux-with-bridged-networking">adjust the MTU accordingly</a>.</li>
<li>Use <a href="https://docs.docker.com/engine/network/drivers/host/">host networking</a> (not recommended): Removes the security benefits of network isolation and may lead to port conflicts.</li>
</ul>
<p>The following example uses a special host (<code>connectivity-check.warp-svc</code>) that is only resolvable by the local DNS proxy to show the supported Docker networking modes.</p>
<pre><code>&#35; This host is not resolvable by default&#10;❯ docker run --rm alpine nslookup connectivity-check.warp-svc.&#10;Server:         8.8.8.8&#10;Address:        8.8.8.8:53&#10;&#10;&#42;* server can&#x27;t find connectivity-check.warp-svc.: NXDOMAIN&#10;&#42;* server can&#x27;t find connectivity-check.warp-svc.: NXDOMAIN&#10;&#10;&#35; Create a bridge network called demo&#10;❯ docker network create demo&#10;e1e1943a6995a7e8c115a1c60357fe64f87a3ae90074ce6e4c3f0d2bba3fa892&#10;&#10;&#35; The host is resolvable by running a container under this custom network&#10;❯ docker run --rm --net demo alpine nslookup connectivity-check.warp-svc.&#10;Server:         127.0.0.11&#10;Address:        127.0.0.11:53Non-authoritative answer:&#10;Name:   connectivity-check.warp-svc&#10;Address: ::ffff:127.0.2.2&#10;Name:   connectivity-check.warp-svc&#10;Address: ::ffff:127.0.2.3Non-authoritative answer:&#10;Name:   connectivity-check.warp-svc&#10;Address: 127.0.2.2&#10;Name:   connectivity-check.warp-svc&#10;Address: 127.0.2.3&#10;&#10;&#35; The host is also resolvable by running a container using a host network&#10;❯ docker run --rm --net host alpine nslookup connectivity-check.warp-svc.&#10;Server:         127.0.0.11&#10;Address:        127.0.0.11:53Non-authoritative answer:&#10;Name:   connectivity-check.warp-svc&#10;Address: ::ffff:127.0.2.2&#10;Name:   connectivity-check.warp-svc&#10;Address: ::ffff:127.0.2.3Non-authoritative answer:&#10;Name:   connectivity-check.warp-svc&#10;Address: 127.0.2.2&#10;Name:   connectivity-check.warp-svc&#10;Address: 127.0.2.3&#10;</code></pre>
<h2 id="linux-dns-domains-with-systemd-resolved-versions-earlier-than-252-3">Linux DNS domains with systemd-resolved versions earlier than 252.3</h2>
<p>On some Linux systems with <code>systemd-resolved</code> versions earlier than <code>252.3</code>, DNS domains configured on non-WARP interfaces may not resolve as expected while the Cloudflare One Client is connected. This can affect hostnames that rely on DHCP-provided search domains or interface-specific DNS routing domains.</p>
<p>For example, commands that resolve the device hostname may take several seconds to start, or may print an error similar to:</p>
<pre><code class="language-txt">sudo: unable to resolve host &lt;HOSTNAME&gt;: Temporary failure in name resolution&#10;</code></pre>
<p>This happens because <code>systemd-resolved</code> versions earlier than <code>252.3</code> do not support the link-specific DNS configuration that the Cloudflare One Client uses on newer Linux distributions. On these systems, the Cloudflare One Client falls back to a global DNS configuration. As a result, DNS domains configured on other interfaces, such as cloud-provider or corporate network search domains, may not be routed or resolved consistently while WARP is connected.</p>
<p>To work around this issue, upgrade to a Linux distribution with <code>systemd-resolved</code> version <code>252.3</code> or later when possible. If the issue affects local hostname resolution, add the local hostname to <code>/etc/hosts</code> so that Linux resolves it before using DNS:</p>
<pre><code class="language-sh">echo &quot;127.0.1.1 $(hostname)&quot; | sudo tee -a /etc/hosts&#10;</code></pre>
<p>Before adding the entry, check whether <code>/etc/hosts</code> already contains a mapping for the hostname. If your organization manages <code>/etc/hosts</code>, contact your administrator before changing it.</p>
<h2 id="windows-app-connection-issue">Windows App connection issue</h2>
<p>When the Cloudflare One Client is active on a local machine, users may be unable to connect to a Windows 365 PC using the <a href="https://aka.ms/WindowsApp">Windows App</a>. This issue does not affect browser-based connections to Windows 365.</p>
<p>To resolve this, exclude the networks specified below from any relevant Cloudflare One Client <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profiles</a>. The required networks are listed under the <code>WindowsVirtualDesktop</code> service tag in the <a href="https://www.microsoft.com/en-us/download/details.aspx?id=56519">Azure IP Ranges and Service Tags - Public Cloud</a> resource (search for <code>&quot;name&quot;: &quot;WindowsVirtualDesktop&quot;</code>).</p>
<p>Microsoft previously provided a <a href="https://github.com/microsoft/Windows365-PSScripts/tree/main/Windows%20365%20Gateway%20IP%20Lookup">PowerShell script</a> to retrieve these networks, but it has since been deprecated. The relevant networks are now consolidated to the following subnets and should be excluded from any relevant Cloudflare One Client device profiles:</p>
<pre><code>40.64.144.0/20&#10;51.5.0.0/16&#10;57.156.5.248/29&#10;57.156.73.192/28&#10;172.183.252.22/32&#10;2603:1061:2010::/48&#10;2603:1061:2011::/48&#10;</code></pre>
<h2 id="windows-10-in-microsoft-365-cloud-pc-is-not-supported">Windows 10 in Microsoft 365 Cloud PC is not supported</h2>
<p>Use of the Cloudflare One Client in a Microsoft 365 Windows 10 Cloud PC is not supported. To work around this limitation, use Windows 11.</p>
<h2 id="ipv6-dns-resolution-in-traffic-only-mode">IPv6 DNS resolution in Traffic only mode</h2>
<p>In <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#traffic-only-mode">Traffic only mode</a>, devices using IPv6 DNS servers may experience connectivity issues if these servers are not manually excluded from the WARP tunnel.</p>
<p>Unlike common IPv4 DHCP configurations where DNS servers often fall within automatically excluded private address ranges, IPv6 environments typically require manual exclusion of DNS server addresses via split tunnel settings for proper operation.</p>
<p>If your DNS server uses an IPv6 address, you must manually exclude it using <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">split tunnel settings</a> for Traffic only mode to work properly.</p>
<h2 id="ivanti-secure-access-formerly-pulse-secure">Ivanti Secure Access (formerly Pulse Secure)</h2>
<p>The Ivanti Secure Access VPN client can conflict with the Cloudflare One Client by installing Windows Filtering Platform (WFP) rules that block outgoing traffic to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#dns-traffic">WARP local DNS proxy</a> on port <code>53</code>. This results in <code>Host not found</code> errors or a total loss of Internet connectivity even when Ivanti is disabled or disconnected.</p>
<p>To resolve this, contact Ivanti support or your administrator to modify or remove the specific firewall rules blocking traffic to <code>127.0.2.2</code>.</p>
<h2 id="always-on-vpn-with-lockdown-mode-in-microsoft-intune">Always-On VPN with Lockdown Mode in Microsoft Intune</h2>
<p>If you are using Microsoft Intune to deploy the Cloudflare One Client on Android with <a href="https://learn.microsoft.com/en-us/intune/intune-service/configuration/device-restrictions-android-for-work?tabs=aecorporate#fully-managed-dedicated-and-corporate-owned-work-profile-devices-5">Always-On VPN and Lockdown mode enabled</a>, the Cloudflare One agent may fail to register. This is because Lockdown mode prevents the Cloudflare One agent from accessing the underlying network to complete the registration process.</p>
<p>This is a known limitation of the Android OS, which has been reported to Google. You can track the status of the feature request on the <a href="https://issuetracker.google.com/issues/238109298?pli=1">Google Issue Tracker</a>.</p>
<p>To work around this issue, you can disable Lockdown mode while keeping Always-On VPN enabled:</p>
<ol>
<li>In your Intune profile, disable <strong>Lockdown mode</strong> while keeping <strong>Always-On VPN</strong> enabled.</li>
<li>Use the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#auto_connect"><code>auto_connect</code></a> and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#switch_locked"><code>switch_locked</code></a> parameters in the managed configuration for seamless connectivity.</li>
<li>Instruct users to launch the Cloudflare One agent app and complete the one-time registration manually.</li>
</ol>
<h2 id="repeated-reinstalls-on-macos-with-microsoft-intune">Repeated reinstalls on macOS with Microsoft Intune</h2>
<p>When you deploy the Cloudflare One Client <code>.pkg</code> to macOS with Microsoft Intune, Intune may repeatedly reinstall the package. Each reinstall restarts the client and briefly drops the WARP connection, and you may see the client reinstalled several times within a single Intune evaluation cycle.</p>
<p>This affects Cloudflare One Client versions from 2026.3.566.1 — the first release with the redesigned client interface (the new client UI). The redesigned client bundles several embedded frameworks inside the application, which is what triggers the reinstall loop. This is an Intune-side detection configuration issue rather than a client defect, so apply the following workaround on any affected version.</p>
<p>This happens because of how Intune detects whether a macOS <code>.pkg</code> app is already installed. When you upload the package, Intune automatically populates the app's <strong>Included apps</strong> detection list with every bundle it finds inside the package — including the roughly two dozen embedded framework bundles that ship inside the client (for example <code>io.flutter.flutter-macos</code>, <code>org.sparkle-project.Sparkle</code>, and several <code>org.cocoapods.*</code> bundles). Intune only considers the app installed when <em>every</em> entry in the <strong>Included apps</strong> list is detected on the device.</p>
<p>These embedded frameworks are not independently installable apps. They live inside the client's application bundle and have no installer receipt or standalone presence, so Intune cannot detect them as installed applications on their own. As a result, Intune never detects them, always concludes the app is not fully installed, and reinstalls the package — cycling through each undetectable framework. Intune detects the client's own bundle identifier (<code>com.cloudflare.1dot1dot1dot1.macos</code>) correctly the entire time. The extra framework entries are what fail detection and drive the reinstall loop. Cloudflare has reported this behavior to Microsoft.</p>
<p>To work around this issue, remove the embedded framework bundles from the <strong>Included apps</strong> list so that only the client's own bundle identifier remains, and turn off version-based detection:</p>
<ol>
<li>In the <a href="https://intune.microsoft.com">Microsoft Intune admin center</a>, go to <strong>Apps</strong> &gt; <strong>macOS</strong> and select the Cloudflare One Client app.</li>
<li>Go to <strong>Properties</strong> and, next to <strong>Detection rules</strong>, select <strong>Edit</strong>.</li>
<li>In the <strong>Included apps</strong> list, remove every entry except <code>com.cloudflare.1dot1dot1dot1.macos</code>.</li>
<li>Set <strong>Ignore app version</strong> to <strong>Yes</strong> so that detection succeeds regardless of the deployed client version.</li>
<li>Select <strong>Review + save</strong> to apply the change.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/connections/intune/intune-included-apps-detection.png" alt="The Included apps detection list in Intune with only the Cloudflare One Client bundle identifier and Ignore app version set to Yes" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6085.md")
</aside>
<h2 id="windows-11-24h2-performance-issues">Windows 11 24H2 performance issues</h2>
<p>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 version KB5062553</a> or higher for resolution.</p>
<h2 id="false-positive-malware-warning-on-windows-with-kb5055523">False positive malware warning on Windows with KB5055523</h2>
<p>Windows devices with KB5055523 installed may receive a warning about <code>Win32/ClickFix.ABA</code> being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to version <a href="https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0">1.429.19.0</a> or later.</p>
