<h1 id="changelog">Changelog</h1>

<h2 id="warp-client-for-windows-version-2025-8-779-0"><a href="/changelog/post/2025-10-07-warp-windows-ga/">WARP client for Windows (version 2025.8.779.0)</a></h2>
<p><em>2025-10-08</em></p>
<p>A new GA release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains significant fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> has been enhanced for even faster resolution. Proxy mode now supports SOCKS4, SOCK5, and HTTP CONNECT over an L4 tunnel with custom congestion control optimizations instead of the previous L3 tunnel to Cloudflare's network. This has more than doubled Proxy mode throughput in lab speed testing, by an order of magnitude in some cases.</p>
</li>
<li>
<p>The MASQUE protocol is now the only protocol that can use <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a>. If you previously configured a device profile to use Proxy mode with Wireguard, you will need to select a new WARP mode or switch to the MASQUE protocol. Otherwise, all devices matching the profile will lose connectivity.</p>
</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 KB5062553</a> or higher for resolution.</p>
</li>
<li>
<p>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</p>
</li>
<li>
<p>Devices with KB5055523 installed may receive a warning about <code>Win32/ClickFix.ABA</code> being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to <a href="https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0">version 1.429.19.0</a> or later.</p>
</li>
<li>
<p>DNS resolution may be broken when the following conditions are all true:</p>
<ul>
<li>WARP is in Secure Web Gateway without DNS filtering (tunnel-only) mode.</li>
<li>A custom DNS server address is configured on the primary network adapter.</li>
<li>The custom DNS server address on the primary network adapter is changed while WARP is connected.</li>
</ul>
<p>To work around this issue, reconnect the WARP client by toggling off and back on.</p>
</li>
</ul>


<h2 id="warp-client-for-linux-version-2025-7-176-0"><a href="/changelog/post/2025-09-30-warp-linux-ga/">WARP client for Linux (version 2025.7.176.0)</a></h2>
<p><em>2025-10-01</em></p>
<p>A new GA release for the Linux WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements including an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at <a href="https://pkg.cloudflareclient.com/">pkg.cloudflareclient.com</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>MASQUE is now the default <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">tunnel protocol</a> for all new WARP device profiles.</li>
<li>Improvement to limit idle connections in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#dns-only-mode">Gateway with DoH mode</a> to avoid unnecessary resource usage that can lead to DoH requests not resolving.</li>
<li>Improvements to maintain <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-warp-on-all-devices">Global WARP override</a> settings when <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/#switch-organizations-in-the-cloudflare-one-client">switching between organizations</a>.</li>
<li>Improvements to maintain client connectivity during network changes.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</li>
</ul>


<h2 id="warp-client-for-macos-version-2025-7-176-0"><a href="/changelog/post/2025-09-30-warp-macos-ga/">WARP client for macOS (version 2025.7.176.0)</a></h2>
<p><em>2025-10-01</em></p>
<p>A new GA release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Fixed a bug preventing the <code>warp-diag captive-portal</code> command from running successfully due to the client not parsing SSID on macOS.</li>
<li>Improvements to maintain <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-warp-on-all-devices">Global WARP override</a> settings when <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/#switch-organizations-in-the-cloudflare-one-client">switching between organizations</a>.</li>
<li>MASQUE is now the default <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">tunnel protocol</a> for all new WARP device profiles.</li>
<li>Improvement to limit idle connections in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#dns-only-mode">Gateway with DoH mode</a> to avoid unnecessary resource usage that can lead to DoH requests not resolving.</li>
<li>Improvements to maintain client connectivity during network changes.</li>
<li>The WARP client now supports macOS Tahoe (version 26.0).</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>macOS Sequoia: Due to changes Apple introduced in macOS 15.0.x, the WARP client may not behave as expected. Cloudflare recommends the use of macOS 15.4 or later.</p>
</li>
<li>
<p>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</p>
</li>
</ul>


<h2 id="warp-client-for-windows-version-2025-7-176-0"><a href="/changelog/post/2025-09-30-warp-windows-ga/">WARP client for Windows (version 2025.7.176.0)</a></h2>
<p><em>2025-10-01</em></p>
<p>A new GA release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>MASQUE is now the default <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">tunnel protocol</a> for all new WARP device profiles.</li>
<li>Improvement to limit idle connections in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#dns-only-mode">Gateway with DoH mode</a> to avoid unnecessary resource usage that can lead to DoH requests not resolving.</li>
<li>Improvement to maintain TCP connections to reduce interruptions in long-lived connections such as RDP or SSH.</li>
<li>Improvements to maintain <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-warp-on-all-devices">Global WARP override</a> settings when <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/#switch-organizations-in-the-cloudflare-one-client">switching between organizations</a>.</li>
<li>Improvements to maintain client connectivity during network changes.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 KB5062553</a> or higher for resolution.</p>
</li>
<li>
<p>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</p>
</li>
<li>
<p>Devices with KB5055523 installed may receive a warning about <code>Win32/ClickFix.ABA</code> being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to <a href="https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0">version 1.429.19.0</a> or later.</p>
</li>
<li>
<p>DNS resolution may be broken when the following conditions are all true:</p>
<ul>
<li>WARP is in Secure Web Gateway without DNS filtering (tunnel-only) mode.</li>
<li>A custom DNS server address is configured on the primary network adapter.</li>
<li>The custom DNS server address on the primary network adapter is changed while WARP is connected.</li>
</ul>
<p>To work around this issue, reconnect the WARP client by toggling off and back on.</p>
</li>
</ul>


<h2 id="cloudflare-one-warp-diagnostic-ai-analyzer"><a href="/changelog/post/2025-08-29-warp-AI-diag-analyzer/">Cloudflare One WARP Diagnostic AI Analyzer</a></h2>
<p><em>2025-08-29</em></p>
<p>We're excited to share a new AI feature, the <a href="https://blog.cloudflare.com/ai-troubleshoot-warp-and-network-connectivity-issues/">WARP diagnostic analyzer</a>, to help you troubleshoot and resolve WARP connectivity issues faster. This beta feature is now available in the <a href="https://dash.cloudflare.com/one/">Cloudflare One dashboard</a> to all users. The AI analyzer makes it easier for you to identify the root cause of client connectivity issues by parsing <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#start-a-remote-capture">remote captures</a> of <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#warp-diag-logs">WARP diagnostic logs</a>. The WARP diagnostic analyzer provides a summary of impact that may be experienced on the device, lists notable events that may contribute to performance issues, and recommended troubleshooting steps and articles to help you resolve these issues. Refer to <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#diagnostics-analyzer-beta">WARP diagnostics analyzer (beta)</a> to learn more about how to maximize using the WARP diagnostic analyzer to troubleshoot the WARP client.</p>


<h2 id="cloudflare-one-agent-for-android-version-2-4-2"><a href="/changelog/post/2025-06-30-warp-ga-android/">Cloudflare One Agent for Android (version 2.4.2)</a></h2>
<p><em>2025-06-30</em></p>
<p>A new GA release for the Android Cloudflare One Agent is now available in the <a href="https://play.google.com/store/apps/details?id=com.cloudflare.cloudflareoneagent">Google Play Store</a>. This release
contains improvements and new exciting features, including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum">post-quantum cryptography</a>.
By tunneling your corporate network traffic over Cloudflare, you can now gain the immediate <a href="https://blog.cloudflare.com/pq-2024/">protection of post-quantum cryptography</a> without needing to upgrade any of your individual corporate applications or systems.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>QLogs are now disabled by default and can be enabled in the app by turning on <strong>Enable qlogs</strong> under <strong>Settings</strong> &gt; <strong>Advanced</strong> &gt; <strong>Diagnostics</strong> &gt; <strong>Debug Logs</strong>. The QLog setting from previous releases will no longer be respected.</li>
<li>DNS over HTTPS traffic is now included in the WARP tunnel by default.</li>
<li>The WARP client now applies <a href="https://blog.cloudflare.com/pq-2024/">post-quantum cryptography</a> end-to-end on enabled devices accessing resources behind a Cloudflare Tunnel. This feature can be enabled by <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum">MDM</a>.</li>
<li>Fixed an issue that caused WARP connection failures on ChromeOS devices.</li>
</ul>


<h2 id="cloudflare-one-agent-for-ios-version-1-11"><a href="/changelog/post/2025-06-30-warp-ga-ios/">Cloudflare One Agent for iOS (version 1.11)</a></h2>
<p><em>2025-06-30</em></p>
<p>A new GA release for the iOS Cloudflare One Agent is now available in the <a href="https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492">iOS App Store</a>. This release
contains improvements and new exciting features, including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum">post-quantum cryptography</a>.
By tunneling your corporate network traffic over Cloudflare, you can now gain the immediate <a href="https://blog.cloudflare.com/pq-2024/">protection of post-quantum cryptography</a> without needing to upgrade any of your individual corporate applications or systems.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>QLogs are now disabled by default and can be enabled in the app by turning on <strong>Enable qlogs</strong> under <strong>Settings</strong> &gt; <strong>Advanced</strong> &gt; <strong>Diagnostics</strong> &gt; <strong>Debug Logs</strong>. The QLog setting from previous releases will no longer be respected.</li>
<li>DNS over HTTPS traffic is now included in the WARP tunnel by default.</li>
<li>The WARP client now applies <a href="https://blog.cloudflare.com/pq-2024/">post-quantum cryptography</a> end-to-end on enabled devices accessing resources behind a Cloudflare Tunnel. This feature can be enabled by <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum">MDM</a>.</li>
</ul>


<h2 id="cloudflare-one-agent-for-android-version-2-4"><a href="/changelog/post/2025-03-17-warp-ga-android/">Cloudflare One Agent for Android (version 2.4)</a></h2>
<p><em>2025-03-17</em></p>
<p>A new GA release for the Android Cloudflare One Agent is now available in the <a href="https://play.google.com/store/apps/details?id=com.cloudflare.cloudflareoneagent">Google Play Store</a>. This release includes a new feature allowing <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url">team name insertion by URL</a> during enrollment, as well as fixes and minor improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Improved in-app error messages.</li>
<li>Improved mobile client login with support for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url">team name insertion by URL</a>.</li>
<li>Fixed an issue preventing admin split tunnel settings taking priority for traffic from certain applications.</li>
</ul>


<h2 id="cloudflare-one-agent-for-ios-version-1-10"><a href="/changelog/post/2025-03-17-warp-ga-ios/">Cloudflare One Agent for iOS (version 1.10)</a></h2>
<p><em>2025-03-17</em></p>
<p>A new GA release for the iOS Cloudflare One Agent is now available in the <a href="https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492">iOS App Store</a>. This release includes a new feature allowing <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url">team name insertion by URL</a> during enrollment, as well as fixes and minor improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Improved in-app error messages.</li>
<li>Improved mobile client login with support for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url">team name insertion by URL</a>.</li>
<li>Bug fixes and performance improvements.</li>
</ul>


<h2 id="explore-product-updates-for-cloudflare-one"><a href="/changelog/post/2024-06-16-cloudflare-one/">Explore product updates for Cloudflare One</a></h2>
<p><em>2024-06-16</em></p>
<p>Welcome to your new home for product updates on <a href="/cloudflare-one/">Cloudflare One</a>.</p>
<p>Our <a href="/changelog/">new changelog</a> lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.</p>
<p>If you are looking for older product updates, refer to the following locations.</p>
<details class="nb-details" open><summary>Older product updates</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17707.md")</div></details>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/cloudflare-one-client/2/">Previous</a><span>Page 3 of 3</span></nav>
