---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/
  description: Reference information for Download Cloudflare One Client stable releases in Zero Trust.
  full_title: Download Cloudflare One Client stable releases · Cloudflare One docs
  head_html: <title>Download Cloudflare One Client stable releases · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Download Cloudflare One Client stable releases in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/index.md"><meta property="og:title" content="Download Cloudflare One Client stable releases · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Download Cloudflare One Client stable releases in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/#page","headline":"Download Cloudflare One Client stable releases \u00b7 Cloudflare One docs","description":"Reference information for Download Cloudflare One Client stable releases in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/
  schema: 1
---
<p>This page contains the stable Cloudflare One Client (formerly WARP) releases from the past year. We recommend using stable releases for production environments. You can download stable releases from the links below after checking requirements.</p>
<p>Cloudflare also offers an unstable <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta release track</a> with the latest features and improvements, and an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/lts-releases/">LTS release track</a> with extended support durations.</p>
<p>For more details on Cloudflare One Client support timelines and end-of-life (EOL) policies, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/support-lifecycle/">Support lifecycle</a> page.</p>
<h2 id="windows">Windows</h2>
<p><a class="nb-link-button" href="https://downloads.cloudflareclient.com/v1/download/windows/ga">Download latest stable release</a></p>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>OS version</strong></td>
<td>Windows 10 LTSC, Windows 11, Windows 365 Cloud PC running Windows 11</td>
</tr>
<tr>
<td><strong>Processor</strong></td>
<td>AMD64 / x86-64 or ARM64 / AArch64</td>
</tr>
<tr>
<td><strong>.NET Framework version</strong></td>
<td>4.7.2 or later</td>
</tr>
<tr>
<td><strong>HD space</strong></td>
<td>184 MB</td>
</tr>
<tr>
<td><strong>Memory</strong></td>
<td>3 MB</td>
</tr>
<tr>
<td><strong>Network interface type</strong></td>
<td>Wi-Fi or LAN</td>
</tr>
<tr>
<td><strong>MTU</strong></td>
<td>1381 bytes recommended <sup><a href="#footnote-cloudflare-one-warp-system-requirements-windows-mdx-1">1</a></sup></td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-cloudflare-one-warp-system-requirements-windows-mdx-1">Minimum 1281 bytes with [Path MTU Discovery](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/)</li></ol></section>
<h2 id="footnotes-1">Footnotes</h2><details class="nb-details" open><summary>Latest release</summary><p><strong>Release date:</strong> 2026-08-28</p><p><a href="https://downloads.cloudflareclient.com/v1/download/windows/version/2026.7.1376.0">Download Windows 2026.7.1376.0</a></p><h4 id="release-notes">Release notes</h4><p>Fixed a rare but critical issue where the client could fail to connect or switch organizations due to an invalid registration after switching installed client versions. Additionally, this hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.</p>
</details><details class="nb-details"><summary>Windows 2026.7.1343.0</summary><p><strong>Release date:</strong> 2026-08-19</p><p><a href="https://downloads.cloudflareclient.com/v1/download/windows/version/2026.7.1343.0">Download Windows 2026.7.1343.0</a></p><h4 id="release-notes-1">Release notes</h4><p>This release introduces multiple features from our previous beta release into stable release, including:</p>
<ul>
<li>When reauthentication is needed for any reason, the notifications are clearer and reduce the actions needed to get you back to work by redirecting to the browser for authentication instead of the app window when necessary.</li>
<li>When a network is blocking or otherwise not supportive of HTTP/3, the client will learn and adapt by switching the order of fallback for that network by starting with HTTP/2 first and then trying HTTP/3 if needed. This reduces delays in time to connectivity when joining older or heavily filtered networks.</li>
</ul>
<p><strong>Additional changes and improvements</strong></p>
<ul>
<li>Fixed a process leak in the Windows GUI that could exhaust system resources during IPC client-creation failures.</li>
<li>Fixed being unable to switch organizations when the client was stuck in the &quot;Device not in organization&quot; state.</li>
<li>Fixed an issue where Microsoft Defender would falsely flag the Cloudflare One Client installation as malicious when installing with Intune.</li>
<li>Made the Windows domain-joined posture check more reliable.</li>
<li>A DNS search domain parsing failure no longer prevents connection.</li>
<li>Cloud icon now correctly reflects actual connection status instead of showing disconnected while fully connected.</li>
<li>Fixed missing certificate error display due to a race condition.</li>
<li>Fixed empty black window after transitioning from docked dual displays to undocked/internal display.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>If a user upgrades to version 2026.7.1343.0, downgrades to an earlier version, re-registers, and then upgrades back to 2026.7.1343.0, the client might fail to connect or switch organizations. To resolve this issue, run <code>warp-cli registration delete</code> or <code>warp-cli registration delete-all</code>.</li>
</ul>
<p>For Zero Trust documentation please see: <a href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/</a><br />
For Consumer documentation please see: <a href="https://developers.cloudflare.com/warp-client/">https://developers.cloudflare.com/warp-client/</a></p>
</details><details class="nb-details"><summary>Windows 2026.6.905.0</summary><p><strong>Release date:</strong> 2026-08-10</p><p><a href="https://downloads.cloudflareclient.com/v1/download/windows/version/2026.6.905.0">Download Windows 2026.6.905.0</a></p><h4 id="release-notes-2">Release notes</h4><p>This hotfix addresses an uncommon and intermittent case on Windows devices where the device is unable to reconnect after the device is woken from sleep.</p>
</details><details class="nb-details"><summary>Windows 2026.6.880.0</summary><p><strong>Release date:</strong> 2026-07-21</p><p><a href="https://downloads.cloudflareclient.com/v1/download/windows/version/2026.6.880.0">Download Windows 2026.6.880.0</a></p><h4 id="release-notes-3">Release notes</h4><p>This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.</p>
</details><details class="nb-details"><summary>Windows 2026.6.850.0</summary><p><strong>Release date:</strong> 2026-07-07</p><p><a href="https://downloads.cloudflareclient.com/v1/download/windows/version/2026.6.850.0">Download Windows 2026.6.850.0</a></p><h4 id="release-notes-4">Release notes</h4><p>This hotfix addresses a Windows authentication issue in the embedded WebView2 browser. Single sign-on could fail to use the Windows primary account, causing users to be prompted for an interactive sign-in. The embedded authentication browser now allows SSO providers to use the OS primary account when available.</p>
</details><details class="nb-details"><summary>Windows 2026.6.822.0</summary><p><strong>Release date:</strong> 2026-06-29</p><p><a href="https://downloads.cloudflareclient.com/v1/download/windows/version/2026.6.822.0">Download Windows 2026.6.822.0</a></p><h4 id="release-notes-5">Release notes</h4><p>This release introduces multiple features from our previous beta release into stable release, including:</p>
<ul>
<li>The client now applies DNS search suffixes configured in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles">device profile</a> / <a href="/cloudflare-one/traffic-policies/network-policies">network policy</a>. Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search suffixes</a> for details.</li>
<li>Added mandatory authentication. When enabled via MDM, the Cloudflare One Client blocks all Internet traffic from the moment the machine boots until the user authenticates, closing the visibility gap on newly deployed devices and during re-authentication. See the <a href="https://blog.cloudflare.com/mandatory-authentication-mfa/">announcement blog</a> and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-no-auth-no-internet/">documentation</a> for details.</li>
<li>Upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the TPM (with TPM 2.0+) whenever it is available to provide stronger protection against device impersonation. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/">Hardware-backed registration</a> for details.</li>
<li>Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.</li>
<li>Added new warp-cli debug commands for interactive connection diagnosis. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging">Extra debug logging</a> for details.</li>
<li>The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.</li>
<li>Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs">Cloudflare One MDM documentation</a> for details.</li>
<li>Added support for dashboard-managed client version deployments. Administrators can now upgrade or downgrade the client version on enrolled devices directly from the Zero Trust dashboard. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">Client version assignments</a> for details.</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>Starting with 2026.6.822.0, the client unifies all API requests under the <code>api.devices.cloudflare.com</code> SNI, where previously both <code>zero-trust-client.cloudflareclient.com</code> and <code>notifications.cloudflareclient.com</code> were used. Review <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">Cloudflare One Client with firewall</a> to ensure systems that rely on SNI inspection do not block the API traffic. The behavior of previous client versions is unaffected.</li>
<li>Client Certificate device-posture checks now support template variables (e.g. <code>${serial_number}</code>, <code>${device_uuid}</code>) in the Subject Alternative Name field. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.</li>
<li>Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in Windows Accessibility settings.</li>
<li>Path MTU Discovery (PMTUD) is now enabled by default.</li>
<li>The UseWebView2 registry value (HKLM\SOFTWARE\Cloudflare\CloudflareWARP\UseWebView2 = y) is once again honored by the new GUI for authentication, so administrators who prefer the embedded WebView2 browser for sign-in can opt back in. This setting was effectively ignored in the previous release; the default browser was always used. This key is now also honored for re-authentications.</li>
<li>Fixed a crash in the authentication browser when navigating to a site that prompts for browser permissions (microphone, camera, notifications, etc.). The same fix had previously landed for the captive-portal browser; this extends it to the auth browser.</li>
<li>Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.</li>
<li>Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.</li>
<li>Fixed a high CPU issue when the device wakes from sleep.</li>
<li>Users can now register with team names in any case format without errors.</li>
<li>New UI fixes
<ul>
<li>Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.</li>
<li>Added a re-auth button and banner to the home screen so users don't miss it when their session expires.</li>
<li>Added clear error messaging when the Cloudflare certificate needs to be installed.</li>
<li>Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.</li>
<li>New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.</li>
<li>Added ability to configure proxy mode for consumer users.</li>
<li>Added back the option to quit for consumer users.</li>
</ul>
</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Single sign-on in the embedded WebView2 authentication browser may fail to use the Windows primary account, prompting for an interactive sign-in.</li>
<li>An error indicating that Microsoft Edge can't read and write to its data directory may be displayed during captive portal login; this error is benign and can be dismissed.</li>
<li>In rare cases, a registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Windows ARM may prompt the user to close running applications while trying to install this version. Simply click &quot;Ok&quot; with the default highlighted option.</li>
</ul>
</details><details class="nb-details"><summary>Windows 2026.4.1390.0</summary><p><strong>Release date:</strong> 2026-05-26</p><p><a href="https://downloads.cloudflareclient.com/v1/download/windows/version/2026.4.1390.0">Download Windows 2026.4.1390.0</a></p><h4 id="release-notes-6">Release notes</h4><p>This release introduces the new Cloudflare One Client UI for Windows! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
<ul>
<li>Right click context menu to access the most common client actions quickly</li>
<li>Built-in captive portal login experience</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.</li>
<li>Fixed a proxy mode connection stall issue.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration authentication for devices via the integrated WebView2 browser is unavailable in this version as a temporary measure. As a result, the client will utilize the default browser on the device to complete the authentication process.</li>
<li>An error indicating that Microsoft Edge can't read and write to its data directory may be displayed during captive portal login; this error is benign and can be dismissed.</li>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Split tunnel list configuration is not available in the new UI. Management of Split Tunnel entries is currently only possible via <code>warp-cli tunnel ip</code> and <code>warp-cli tunnel host</code>. UI support will be added in a future release.</li>
<li>Windows ARM may prompt the user to close running applications while trying to install this version. Simply click “Ok” with the default highlighted option.</li>
<li>DNS resolution may be broken when the following conditions are all true:
<ul>
<li>The client is in Secure Web Gateway without DNS filtering (tunnel-only) mode.</li>
<li>A custom DNS server address is configured on the primary network adapter.</li>
<li>The custom DNS server address on the primary network adapter is changed while the client is connected.<br />
To work around this issue, please reconnect the client by selecting &quot;disconnect&quot; and then &quot;connect&quot; in the client user interface.</li>
</ul>
</li>
</ul>
</details><details class="nb-details"><summary>Windows 2026.4.1350.0</summary><p><strong>Release date:</strong> 2026-05-11</p><p><a href="https://downloads.cloudflareclient.com/v1/download/windows/version/2026.4.1350.0">Download Windows 2026.4.1350.0</a></p><h4 id="release-notes-7">Release notes</h4><p>This release introduces the new Cloudflare One Client UI for Windows! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
<ul>
<li>Right click context menu to access the most common client actions quickly</li>
<li>Built-in captive portal login experience</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration authentication for devices via the integrated WebView2 browser is unavailable in this version as a temporary measure. As a result, the client will utilize the default browser on the device to complete the authentication process.</li>
<li>An error indicating that Microsoft Edge can't read and write to its data directory may be displayed during captive portal login; this error is benign and can be dismissed.</li>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Split tunnel list configuration is not available in the new UI. Management of Split Tunnel entries is currently only possible via <code>warp-cli tunnel ip</code> and <code>warp-cli tunnel host</code>. UI support will be added in a future release.</li>
<li>Windows ARM may prompt the user to close running applications while trying to install this version. Simply click “Ok” with the default highlighted option.</li>
<li>DNS resolution may be broken when the following conditions are all true:
<ul>
<li>The client is in Secure Web Gateway without DNS filtering (tunnel-only) mode.</li>
<li>A custom DNS server address is configured on the primary network adapter.</li>
<li>The custom DNS server address on the primary network adapter is changed while the client is connected.<br />
To work around this issue, please reconnect the client by selecting &quot;disconnect&quot; and then &quot;connect&quot; in the client user interface.</li>
</ul>
</li>
</ul>
</details><details class="nb-details"><summary>Windows 2026.3.851.0</summary><p><strong>Release date:</strong> 2026-04-07</p><p><a href="https://downloads.cloudflareclient.com/v1/download/windows/version/2026.3.851.0">Download Windows 2026.3.851.0</a></p><h4 id="release-notes-8">Release notes</h4><p>This release contains minor fixes and improvements.</p>
<p>The next stable release for Windows will introduce the new Cloudflare One Client UI, providing a cleaner and more intuitive design as well as easier access to common actions and information.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Fixed an issue causing Windows client tunnel interface initialization failure which prevented clients from establishing a tunnel for connection.</li>
<li>Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.</li>
<li>Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.</li>
<li>Added monitoring for tunnel statistics collection timeouts.</li>
<li>Switched tunnel congestion control algorithm for local proxy mode to Cubic for improved reliability across platforms.</li>
<li>Fixed packet capture failing on tunnel interface when the tunnel interface is renamed by SCCM VPN boundary support.</li>
<li>Fixed unnecessary registration deletion caused by RDP connections in multi-user mode.</li>
<li>Fixed increased tunnel interface start-up time due to a race between duplicate address detection (DAD) and disabling NetBT.</li>
<li>Fixed tunnel failing to connect when the system DNS search list contains unexpected characters.</li>
<li>Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.</li>
<li>Fixed an issue in local proxy mode where the client could become unresponsive due to upstream connection timeouts.</li>
<li>Fixed an issue where the emergency disconnect status of a prior organization persisted after a switch to a different organization.</li>
<li>Fixed initiating managed network detections checks when no network is available, which caused device profile flapping.</li>
<li>Fixed an issue where degraded Windows Management Instrumentation (WMI) state could put the client in a failed connection state loop during initialization.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 version KB5062553</a> or higher for resolution. This warning will be omitted from future release notes. This Windows update was released in July 2025.</p>
</li>
<li>
<p>Devices with KB5055523 installed may receive a warning about <code>Win32/ClickFix.ABA</code> being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to <a href="https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0">version 1.429.19.0</a> or later. This warning will be omitted from future release notes. This Microsoft Security Intelligence update was released in May 2025.</p>
</li>
<li>
<p>DNS resolution may be broken when the following conditions are all true:</p>
<ul>
<li>The client is in Secure Web Gateway without DNS filtering (tunnel-only) mode.</li>
<li>A custom DNS server address is configured on the primary network adapter.</li>
<li>The custom DNS server address on the primary network adapter is changed while the client is connected.</li>
</ul>
<p>To work around this issue, reconnect the client by selecting <strong>Disconnect</strong> and then <strong>Connect</strong> in the client user interface.</p>
</li>
</ul>
</details><details class="nb-details"><summary>Windows 2026.1.150.0</summary><p><strong>Release date:</strong> 2026-02-24</p><p><a href="https://downloads.cloudflareclient.com/v1/download/windows/version/2026.1.150.0">Download Windows 2026.1.150.0</a></p><h4 id="release-notes-9">Release notes</h4><p>This release contains minor fixes, improvements, and new features.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Improvements to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-multiuser/">multi-user mode</a>. Fixed an issue where when switching from a pre-login registration to a user registration, Mobile Device Management (MDM) configuration association could be lost.</li>
<li>Added a new feature to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#netbios-over-tcpip">manage NetBIOS over TCP/IP</a> functionality on the Windows client. NetBIOS over TCP/IP on the Windows client is now disabled by default and can be enabled in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile settings</a>.</li>
<li>Fixed an issue causing failure of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion">local network exclusion</a> feature when configured with a timeout of <code>0</code>.</li>
<li>Improvement for the Windows <a href="/cloudflare-one/reusable-components/posture-checks/warp-client-checks/client-certificate/">client certificate posture check</a> to ensure logged results are from checks that run once users log in.</li>
<li>Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.</li>
<li>Fixed an issue where misconfigured DEX HTTP tests prevented new registrations.</li>
<li>Fixed an issue causing DNS requests to fail with clients in Traffic and DNS mode.</li>
<li>Improved service shutdown behavior in cases where the daemon is unresponsive.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 KB5062553</a> or higher for resolution.</p>
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
</details><details class="nb-details"><summary>Windows 2025.10.186.0</summary><p><strong>Release date:</strong> 2026-01-13</p><p><a href="https://downloads.cloudflareclient.com/v1/download/windows/version/2025.10.186.0">Download Windows 2025.10.186.0</a></p><h4 id="release-notes-10">Release notes</h4><p>This release contains minor fixes, improvements, and new features. New features include the ability to manage WARP client connectivity for all devices in your fleet using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>, and a new WARP client device posture check for <a href="/cloudflare-one/reusable-components/posture-checks/warp-client-checks/antivirus/">Antivirus</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Added a new feature to manage WARP client connectivity for all devices using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>. This feature allows administrators to send a global signal from an on-premises HTTPS endpoint that force disconnects or reconnects all WARP clients in an account based on configuration set on the endpoint.</li>
<li>Fixed an issue that caused occasional audio degradation and increased CPU usage on Windows by optimizing route configurations for large <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#domain-based-split-tunnels">domain-based split tunnel rules</a>.</li>
<li>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> now supports transparent HTTP proxying in addition to CONNECT-based proxying.</li>
<li>Fixed an issue where sending large messages to the daemon by Inter-Process Communication (IPC) could cause the daemon to fail and result in service interruptions.</li>
<li>Added support for a new WARP client device posture check for <a href="/cloudflare-one/reusable-components/posture-checks/warp-client-checks/antivirus/">Antivirus</a>. The check confirms the presence of an antivirus program on a Windows device with the option to check if the antivirus is up to date.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 KB5062553</a> or higher for resolution.</p>
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
</details><details class="nb-details"><summary>Windows 2025.9.558.0</summary><p><strong>Release date:</strong> 2025-11-11</p><p><a href="https://downloads.cloudflareclient.com/v1/download/windows/version/2025.9.558.0">Download Windows 2025.9.558.0</a></p><h4 id="release-notes-11">Release notes</h4><p>This release contains minor fixes, improvements, and new features including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">Path Maximum Transmission Unit Discovery (PMTUD)</a>. When PMTUD is enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to diagnose connectivity issues.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Fixed an inconsistency with <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-warp-on-all-devices">Global WARP override</a> settings in multi-user environments when switching between users.</li>
<li>The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to diagnose connectivity issues.</li>
<li>Fixed an issue where deleting a registration was erroneously reported as having failed.</li>
<li>Path Maximum Transmission Unit Discovery (PMTUD) may now be used to discover the effective MTU of the connection. This allows the WARP client to improve connectivity optimized for each network. PMTUD is disabled by default. To enable it, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">PMTUD documentation</a>.</li>
<li>Improvements for the <a href="/cloudflare-one/reusable-components/posture-checks/warp-client-checks/os-version/">OS version</a> WARP client check. Windows Updated Build Revision (UBR) numbers can now be checked by the client to ensure devices have required security patches and features installed.</li>
<li>The WARP client now supports Windows 11 ARM-based machines. For information on known limitations, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/known-limitations/#cloudflare-one-client-disconnected-on-windows-arm">Known limitations page</a>.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 KB5062553</a> or higher for resolution.</p>
</li>
<li>
<p>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</p>
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
</details><details class="nb-details"><summary>Windows 2025.8.779.0</summary><p><strong>Release date:</strong> 2025-10-07</p><p><a href="https://downloads.cloudflareclient.com/v1/download/windows/version/2025.8.779.0">Download Windows 2025.8.779.0</a></p><h4 id="release-notes-12">Release notes</h4><p>This release contains significant fixes and improvements.</p>
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
</details><details class="nb-details"><summary>Windows 2025.7.176.0</summary><p><strong>Release date:</strong> 2025-09-30</p><p><a href="https://downloads.cloudflareclient.com/v1/download/windows/version/2025.7.176.0">Download Windows 2025.7.176.0</a></p><h4 id="release-notes-13">Release notes</h4><p>This release contains minor fixes and improvements.</p>
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
</details>
<h2 id="macos">macOS</h2>
<p><a class="nb-link-button" href="https://downloads.cloudflareclient.com/v1/download/macos/ga">Download latest stable release</a></p>
<div class="nb-data-component" data-cf-component="Render"></div>
<h2 id="footnotes-2">Footnotes</h2><details class="nb-details" open><summary>Latest release</summary><p><strong>Release date:</strong> 2026-08-28</p><p><a href="https://downloads.cloudflareclient.com/v1/download/macos/version/2026.7.1376.0">Download macOS 2026.7.1376.0</a></p><h4 id="release-notes-14">Release notes</h4><p>This hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.</p>
</details><details class="nb-details"><summary>macOS 2026.7.1343.0</summary><p><strong>Release date:</strong> 2026-08-19</p><p><a href="https://downloads.cloudflareclient.com/v1/download/macos/version/2026.7.1343.0">Download macOS 2026.7.1343.0</a></p><h4 id="release-notes-15">Release notes</h4><p>This release introduces multiple features from our previous beta release into stable release, including:</p>
<ul>
<li>When reauthentication is needed for any reason, the notifications are clearer and reduce the actions needed to get you back to work by redirecting to the browser for authentication instead of the app window when necessary.</li>
<li>When a network is blocking or otherwise not supportive of HTTP/3, the client will learn and adapt by switching the order of fallback for that network by starting with HTTP/2 first and then trying HTTP/3 if needed. This reduces delays in time to connectivity when joining older or heavily filtered networks.</li>
</ul>
<p><strong>Additional changes and improvements</strong></p>
<ul>
<li>Fixed the client not allowing login to another organization when currently showing &quot;Device not in organization.&quot;</li>
<li>A DNS search domain parsing failure no longer prevents connection.</li>
<li>Cloud icon now correctly reflects actual connection status instead of showing disconnected while fully connected.</li>
<li>Fixed missing certificate error display due to a race condition.</li>
<li>Fixed crash when trying to connect to captive portal on Wi-Fi.</li>
<li>Fixed empty black window after transitioning from docked dual displays to undocked/internal display.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>None</li>
</ul>
<p>For Zero Trust documentation please see: <a href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/</a><br />
For Consumer documentation please see: <a href="https://developers.cloudflare.com/warp-client/">https://developers.cloudflare.com/warp-client/</a></p>
</details><details class="nb-details"><summary>macOS 2026.6.880.0</summary><p><strong>Release date:</strong> 2026-07-21</p><p><a href="https://downloads.cloudflareclient.com/v1/download/macos/version/2026.6.880.0">Download macOS 2026.6.880.0</a></p><h4 id="release-notes-16">Release notes</h4><p>This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.</p>
</details><details class="nb-details"><summary>macOS 2026.6.822.0</summary><p><strong>Release date:</strong> 2026-06-29</p><p><a href="https://downloads.cloudflareclient.com/v1/download/macos/version/2026.6.822.0">Download macOS 2026.6.822.0</a></p><h4 id="release-notes-17">Release notes</h4><p>This release introduces multiple features from our previous beta release into stable release, including:</p>
<ul>
<li>The client now applies DNS search suffixes configured in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles">device profile</a> / <a href="/cloudflare-one/traffic-policies/network-policies">network policy</a>. Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search suffixes</a> for details.</li>
<li>Upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the Secure Enclave whenever available to provide stronger protection against device impersonation. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/">Hardware-backed registration</a> for details.</li>
<li>Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.</li>
<li>Added new warp-cli debug commands for interactive connection diagnosis. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging">Extra debug logging</a> for details.</li>
<li>The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.</li>
<li>Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs">Cloudflare One MDM documentation</a> for details.</li>
<li>Added support for dashboard-managed client version deployments. Administrators can now upgrade or downgrade the client version on enrolled devices directly from the Zero Trust dashboard. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">Client version assignments</a> for details.</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>Starting with 2026.6.822.0, the client unifies all API requests under the <code>api.devices.cloudflare.com</code> SNI, where previously both <code>zero-trust-client.cloudflareclient.com</code> and <code>notifications.cloudflareclient.com</code> were used. Review <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">Cloudflare One Client with firewall</a> to ensure systems that rely on SNI inspection do not block the API traffic. The behavior of previous client versions is unaffected.</li>
<li>Client Certificate device-posture checks now support template variables (e.g. <code>${serial_number}</code>, <code>${device_uuid}</code>) in the Subject Alternative Name field. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.</li>
<li>Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in the macOS Display settings.</li>
<li>Path MTU Discovery (PMTUD) is now enabled by default.</li>
<li>Fixed the in-client captive-portal browser rendering a blank &quot;Success&quot; page on some airline Wi-Fi networks. The browser now more consistently loads the airline's real portal page so users can complete sign-in from inside the client instead of having to open a separate browser.</li>
<li>Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.</li>
<li>Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.</li>
<li>Users can now register with team names in any case format without errors.</li>
<li>New UI fixes
<ul>
<li>Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.</li>
<li>Added a re-auth button and banner to the home screen so users don't miss it when their session expires.</li>
<li>Added clear error messaging when the Cloudflare certificate needs to be installed.</li>
<li>Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.</li>
<li>New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.</li>
<li>Added ability to configure proxy mode for consumer users.</li>
<li>Added back the option to quit for consumer users.</li>
</ul>
</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>When deploying with Microsoft Intune, the client may be repeatedly reinstalled because Intune adds the client's embedded framework bundles to its install-detection list, and those frameworks cannot be detected as installed on their own. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/known-limitations/#repeated-reinstalls-on-macos-with-microsoft-intune">Repeated reinstalls on macOS with Microsoft Intune</a> for the workaround.</li>
</ul>
</details><details class="nb-details"><summary>macOS 2026.4.1390.0</summary><p><strong>Release date:</strong> 2026-05-26</p><p><a href="https://downloads.cloudflareclient.com/v1/download/macos/version/2026.4.1390.0">Download macOS 2026.4.1390.0</a></p><h4 id="release-notes-18">Release notes</h4><p>This release introduces the new Cloudflare One Client UI for macOS! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
<ul>
<li>Right click context menu to access the most common client actions quickly</li>
<li>Built-in captive portal login experience</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.</li>
<li>Fixed a proxy mode connection stall issue.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Split tunnel list configuration is not available in the new UI. Management of split tunnel entries is currently only possible via <code>warp-cli tunnel ip</code> and <code>warp-cli tunnel host</code>. UI support will be added in a future release.</li>
</ul>
</details><details class="nb-details"><summary>macOS 2026.4.1350.0</summary><p><strong>Release date:</strong> 2026-05-11</p><p><a href="https://downloads.cloudflareclient.com/v1/download/macos/version/2026.4.1350.0">Download macOS 2026.4.1350.0</a></p><h4 id="release-notes-19">Release notes</h4><p>This release introduces the new Cloudflare One Client UI for macOS! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
<ul>
<li>Right click context menu to access the most common client actions quickly</li>
<li>Built-in captive portal login experience</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Split tunnel list configuration is not available in the new UI. Management of split tunnel entries is currently only possible via <code>warp-cli tunnel ip</code> and <code>warp-cli tunnel host</code>. UI support will be added in a future release.</li>
</ul>
</details><details class="nb-details"><summary>macOS 2026.3.846.0</summary><p><strong>Release date:</strong> 2026-04-02</p><p><a href="https://downloads.cloudflareclient.com/v1/download/macos/version/2026.3.846.0">Download macOS 2026.3.846.0</a></p><h4 id="release-notes-20">Release notes</h4><p>This release contains minor fixes and improvements.</p>
<p>The next stable release for macOS will introduce the new Cloudflare One Client UI, providing a cleaner and more intuitive design as well as easier access to common actions and information.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.</li>
<li>Fixed an issue in local proxy mode where the client could become unresponsive due to upstream connection timeouts.</li>
<li>Fixed an issue where the emergency disconnect status of a prior organization persisted after a switch to a different organization.</li>
<li>Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.</li>
<li>Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.</li>
<li>Added monitoring for tunnel statistics collection timeouts.</li>
<li>Switched tunnel congestion control algorithm for local proxy mode to Cubic for improved reliability across platforms.</li>
<li>Fixed initiating managed network detections checks when no network is available, which caused device profile flapping.</li>
</ul>
</details><details class="nb-details"><summary>macOS 2026.1.150.0</summary><p><strong>Release date:</strong> 2026-02-24</p><p><a href="https://downloads.cloudflareclient.com/v1/download/macos/version/2026.1.150.0">Download macOS 2026.1.150.0</a></p><h4 id="release-notes-21">Release notes</h4><p>This release contains minor fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Fixed an issue causing failure of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion">local network exclusion</a> feature when configured with a timeout of <code>0</code>.</li>
<li>Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.</li>
<li>Fixed an issue with DNS server configuration failures that caused tunnel connection delays.</li>
<li>Fixed an issue where misconfigured DEX HTTP tests prevented new registrations.</li>
<li>Fixed an issue causing DNS requests to fail with clients in Traffic and DNS mode.</li>
</ul>
</details><details class="nb-details"><summary>macOS 2025.10.186.0</summary><p><strong>Release date:</strong> 2026-01-13</p><p><a href="https://downloads.cloudflareclient.com/v1/download/macos/version/2025.10.186.0">Download macOS 2025.10.186.0</a></p><h4 id="release-notes-22">Release notes</h4><p>This release contains minor fixes, improvements, and new features, including the ability to manage WARP client connectivity for all devices in your fleet using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> now supports transparent HTTP proxying in addition to CONNECT-based proxying.</li>
<li>Added a new feature to manage WARP client connectivity for all devices using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>. This feature allows administrators to send a global signal from an on-premises HTTPS endpoint that force disconnects or reconnects all WARP clients in an account based on configuration set on the endpoint.</li>
</ul>
</details><details class="nb-details"><summary>macOS 2025.9.558.0</summary><p><strong>Release date:</strong> 2025-11-11</p><p><a href="https://downloads.cloudflareclient.com/v1/download/macos/version/2025.9.558.0">Download macOS 2025.9.558.0</a></p><h4 id="release-notes-23">Release notes</h4><p>This release contains minor fixes, improvements, and new features including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">Path Maximum Transmission Unit Discovery (PMTUD)</a>. When PMTUD is enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to diagnose connectivity issues.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to diagnose connectivity issues.</li>
<li>Fixed an issue where deleting a registration was erroneously reported as having failed.</li>
<li>Path Maximum Transmission Unit Discovery (PMTUD) may now be used to discover the effective MTU of the connection. This allows the WARP client to improve connectivity optimized for each network. PMTUD is disabled by default. To enable it, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">PMTUD documentation</a>.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</li>
</ul>
</details><details class="nb-details"><summary>macOS 2025.8.779.0</summary><p><strong>Release date:</strong> 2025-10-07</p><p><a href="https://downloads.cloudflareclient.com/v1/download/macos/version/2025.8.779.0">Download macOS 2025.8.779.0</a></p><h4 id="release-notes-24">Release notes</h4><p>This release contains significant fixes and improvements.</p>
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
<p>macOS Sequoia: Due to changes Apple introduced in macOS 15.0.x, the WARP client may not behave as expected. Cloudflare recommends the use of macOS 15.4 or later.</p>
</li>
<li>
<p>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</p>
</li>
</ul>
</details><details class="nb-details"><summary>macOS 2025.7.176.0</summary><p><strong>Release date:</strong> 2025-09-30</p><p><a href="https://downloads.cloudflareclient.com/v1/download/macos/version/2025.7.176.0">Download macOS 2025.7.176.0</a></p><h4 id="release-notes-25">Release notes</h4><p>This release contains minor fixes and improvements.</p>
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
</details>
<h2 id="linux">Linux</h2>
<p><a class="nb-link-button" href="https://pkg.cloudflareclient.com/">Package repository</a></p>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>OS version</strong></td>
<td>RHEL 9 <sup><a href="#footnote-cloudflare-one-warp-system-requirements-linux-mdx-1">1</a></sup>, RHEL 10, Debian 12, Debian 13, Fedora 43, Fedora 44, Ubuntu 22.04 LTS, Ubuntu 24.04 LTS, Ubuntu 26.04 LTS</td>
</tr>
<tr>
<td><strong>Processor</strong></td>
<td>AMD64 / x86-64 or ARM64 / AArch64</td>
</tr>
<tr>
<td><strong>HD space</strong></td>
<td>75 MB</td>
</tr>
<tr>
<td><strong>Memory</strong></td>
<td>35 MB</td>
</tr>
<tr>
<td><strong>Network interface type</strong></td>
<td>Wi-Fi or LAN</td>
</tr>
<tr>
<td><strong>MTU</strong></td>
<td>1381 bytes recommended <sup><a href="#footnote-cloudflare-one-warp-system-requirements-linux-mdx-2">2</a></sup></td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes-3">Footnotes</h2><ol><li id="footnote-cloudflare-one-warp-system-requirements-linux-mdx-1">On RHEL 9 and later, enable the [Extra Packages for Enterprise Linux (EPEL)](https://docs.fedoraproject.org/en-US/epel/) repository (`sudo dnf install epel-release`) before installing `cloudflare-warp`. EPEL provides dependencies required by the client UI.</li>
<li id="footnote-cloudflare-one-warp-system-requirements-linux-mdx-2">Minimum 1281 bytes with [Path MTU Discovery](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/)</li></ol></section>
<h2 id="footnotes-4">Footnotes</h2><details class="nb-details" open><summary>Latest release</summary><p><strong>Release date:</strong> 2026-08-28</p><p><a href="https://downloads.cloudflareclient.com/v1/download/fedora43-intel/version/2026.7.1377.0">Download Linux 2026.7.1377.0</a></p><h4 id="release-notes-26">Release notes</h4><p>This hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.</p>
</details><details class="nb-details"><summary>Linux 2026.7.1343.0</summary><p><strong>Release date:</strong> 2026-08-19</p><p><a href="https://downloads.cloudflareclient.com/v1/download/almalinux9-intel/version/2026.7.1343.0">Download Linux 2026.7.1343.0</a></p><h4 id="release-notes-27">Release notes</h4><p>This release introduces multiple features from our previous beta release into stable release, including:</p>
<ul>
<li>When reauthentication is needed for any reason, the notifications are clearer and reduce the actions needed to get you back to work by redirecting to the browser for authentication instead of the app window when necessary.</li>
<li>When a network is blocking or otherwise not supportive of HTTP/3, the client will learn and adapt by switching the order of fallback for that network by starting with HTTP/2 first and then trying HTTP/3 if needed. This reduces delays in time to connectivity when joining older or heavily filtered networks.</li>
</ul>
<p><strong>Additional changes and improvements</strong></p>
<ul>
<li>Fixed the client not allowing login to another organization when currently showing &quot;Device not in organization.&quot;</li>
<li>A DNS search domain parsing failure no longer prevents connection.</li>
<li>Cloud icon now correctly reflects actual connection status instead of showing disconnected while fully connected.</li>
<li>Fixed missing certificate error display due to a race condition.</li>
<li>Fixed empty black window after transitioning from docked dual displays to undocked/internal display.</li>
<li>Fixed hostname routes not working for Cloudflare Mesh when the IP addresses of the hostnames are local addresses.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>When in DNS Only mode, the client may send DNS queries for names that are configured for Local Domain Fallback to the encrypted DNS server instead of falling back to the system configuration. Local Domain Fallback works as expected in other client modes.</li>
</ul>
<p>For Zero Trust documentation please see: <a href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/</a><br />
For Consumer documentation please see: <a href="https://developers.cloudflare.com/warp-client/">https://developers.cloudflare.com/warp-client/</a></p>
</details><details class="nb-details"><summary>Linux 2026.6.880.0</summary><p><strong>Release date:</strong> 2026-07-21</p><p><a href="https://downloads.cloudflareclient.com/v1/download/trixie-intel/version/2026.6.880.0">Download Linux 2026.6.880.0</a></p><h4 id="release-notes-28">Release notes</h4><p>This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.</p>
</details><details class="nb-details"><summary>Linux 2026.6.836.0</summary><p><strong>Release date:</strong> 2026-07-01</p><p><a href="https://downloads.cloudflareclient.com/v1/download/resolute-intel/version/2026.6.836.0">Download Linux 2026.6.836.0</a></p><h4 id="release-notes-29">Release notes</h4><p>This package is the same release as 2026.6.822.0, with a fix for our RPM package. Previously the repository served a single build to every OS version, so an install could pull a dependency that isn't available on that release. The repository now serves the correct build for each operating system version, so installs automatically pull the dependencies that version requires. Debian and Ubuntu were not affected.</p>
<p>If you installed version 2026.6.822.0 on an RPM-based distribution, we recommend refreshing your repository configuration:</p>
<pre tabindex="0"><code class="language-bash">sudo curl -fsSL https://pkg.cloudflareclient.com/cloudflare-warp-ascii.repo | sudo tee /etc/yum.repos.d/cloudflare-warp.repo&#10;sudo dnf clean all&#10;sudo dnf install cloudflare-warp&#10;</code></pre>
</details><details class="nb-details"><summary>Linux 2026.6.822.0</summary><p><strong>Release date:</strong> 2026-06-29</p><p><a href="https://downloads.cloudflareclient.com/v1/download/fedora43-arm/version/2026.6.822.0">Download Linux 2026.6.822.0</a></p><h4 id="release-notes-30">Release notes</h4><p>This release introduces multiple features from our previous beta release into stable release, including:</p>
<ul>
<li>The client now applies DNS search suffixes configured in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles">device profile</a> / <a href="/cloudflare-one/traffic-policies/network-policies">network policy</a>. Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search suffixes</a> for details.</li>
<li>Upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the TPM (with TPM 2.0+) whenever it is available to provide stronger protection against device impersonation. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/">Hardware-backed registration</a> for details.</li>
<li>Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.</li>
<li>Added new warp-cli debug commands for interactive connection diagnosis. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging">Extra debug logging</a> for details.</li>
<li>The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.</li>
<li>Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs">Cloudflare One MDM documentation</a> for details.</li>
</ul>
<p><strong>Additional changes and improvements</strong></p>
<ul>
<li>Starting with 2026.6.822.0, the client unifies all API requests under the <code>api.devices.cloudflare.com</code> SNI, where previously both <code>zero-trust-client.cloudflareclient.com</code> and <code>notifications.cloudflareclient.com</code> were used. Review <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">Cloudflare One Client with firewall</a> to ensure systems that rely on SNI inspection do not block the API traffic. The behavior of previous client versions is unaffected.</li>
<li><a href="/mesh/">Cloudflare Mesh</a> functionality using the Cloudflare One Client is now supported on RHEL 9 and 10.</li>
<li>Cloudflare Mesh now supports <a href="/mesh/features/routes/#hostname-routes">hostname-based routing</a>.</li>
<li>Client Certificate device-posture checks now support template variables (e.g. <code>${serial_number}</code>, <code>${device_uuid}</code>) in the Subject Alternative Name field. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.</li>
<li>Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in the system display settings.</li>
<li>Path MTU Discovery (PMTUD) is now enabled by default.</li>
<li>Fixed the in-client captive-portal browser rendering a blank &quot;Success&quot; page on some airline Wi-Fi networks. The browser now more consistently loads the airline's real portal page so users can complete sign-in from inside the client instead of having to open a separate browser.</li>
<li>Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.</li>
<li>Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.</li>
<li>Fixed an issue where some Debian releases experienced inaccurate version reporting for posture checks.</li>
<li>Users can now register with team names in any case format without errors.</li>
<li>New UI fixes
<ul>
<li>Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.</li>
<li>Added a re-auth button and banner to the home screen so users don't miss it when their session expires.</li>
<li>Added clear error messaging when the Cloudflare certificate needs to be installed.</li>
<li>Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.</li>
<li>New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.</li>
<li>Added ability to configure proxy mode for consumer users.</li>
<li>Added back the option to quit for consumer users.</li>
</ul>
</li>
</ul>
<p>For RHEL deployments, this release introduces a dependency on the <a href="https://docs.fedoraproject.org/en-US/epel/">Extra Packages for Enterprise Linux</a> repository (EPEL). The EPEL repository provides packages that support the captive portal detection’s in-app browser authentication and system tray icon. See <a href="https://docs.fedoraproject.org/en-US/epel/getting-started/">Getting started with EPEL</a> for instructions on enabling EPEL.</p>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
</ul>
</details><details class="nb-details"><summary>Linux 2026.4.1390.0</summary><p><strong>Release date:</strong> 2026-05-26</p><p><a href="https://downloads.cloudflareclient.com/v1/download/fedora35-intel/version/2026.4.1390.0">Download Linux 2026.4.1390.0</a></p><h4 id="release-notes-31">Release notes</h4><p>This release introduces the new Cloudflare One Client UI for Linux! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
<ul>
<li>Right click context menu to access the most common client actions quickly</li>
<li>Built-in captive portal login experience</li>
</ul>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.</li>
<li>Official support for RHEL 9 has been added for Cloudflare Mesh nodes. To install the RHEL 9 package, the Extra Packages for Enterprise Linux (EPEL) repository must be active, as it contains dependencies required for the tray icon and captive portal webview.</li>
<li>Fixed a proxy mode connection stall issue.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Split tunnel list configuration is not available in the new UI. Management of split tunnel entries is currently only possible via <code>warp-cli tunnel ip</code> and <code>warp-cli tunnel host</code>. UI support will be added in a future release.</li>
</ul>
</details><details class="nb-details"><summary>Linux 2026.4.1350.0</summary><p><strong>Release date:</strong> 2026-05-11</p><p><a href="https://downloads.cloudflareclient.com/v1/download/fedora35-intel/version/2026.4.1350.0">Download Linux 2026.4.1350.0</a></p><h4 id="release-notes-32">Release notes</h4><p>This release introduces the new Cloudflare One Client UI for Linux! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
<ul>
<li>Right click context menu to access the most common client actions quickly</li>
<li>Built-in captive portal login experience</li>
</ul>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.</li>
<li>Official support for RHEL 9 has been added for Cloudflare Mesh nodes. To install the RHEL 9 package, the Extra Packages for Enterprise Linux (EPEL) repository must be active, as it contains dependencies required for the tray icon and captive portal webview.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Split tunnel list configuration is not available in the new UI. Management of split tunnel entries is currently only possible via <code>warp-cli tunnel ip</code> and <code>warp-cli tunnel host</code>. UI support will be added in a future release.</li>
</ul>
</details><details class="nb-details"><summary>Linux 2026.3.846.0</summary><p><strong>Release date:</strong> 2026-04-02</p><p><a href="https://downloads.cloudflareclient.com/v1/download/fedora35-intel/version/2026.3.846.0">Download Linux 2026.3.846.0</a></p><h4 id="release-notes-33">Release notes</h4><p>This release contains minor fixes and improvements.</p>
<p>The next stable release for Linux will introduce the new Cloudflare One Client UI, providing a cleaner and more intuitive design as well as easier access to common actions and information.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.</li>
<li>Fixed an issue in local proxy mode where the client could become unresponsive due to upstream connection timeouts.</li>
<li>Fixed an issue where the emergency disconnect status of a prior organization persisted after a switch to a different organization.</li>
<li>Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.</li>
<li>Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.</li>
<li>Added monitoring for tunnel statistics collection timeouts.</li>
<li>Switched tunnel congestion control algorithm for local proxy mode to Cubic for improved reliability across platforms.</li>
<li>Fixed initiating managed network detections checks when no network is available, which caused device profile flapping.</li>
</ul>
</details><details class="nb-details"><summary>Linux 2026.1.150.0</summary><p><strong>Release date:</strong> 2026-02-24</p><p><a href="https://downloads.cloudflareclient.com/v1/download/bullseye-intel/version/2026.1.150.0">Download Linux 2026.1.150.0</a></p><h4 id="release-notes-34">Release notes</h4><p>This release contains minor fixes and improvements.</p>
<p>WARP client version 2025.8.779.0 introduced an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at <a href="https://pkg.cloudflareclient.com">pkg.cloudflareclient.com</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Fixed an issue causing failure of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion">local network exclusion</a> feature when configured with a timeout of <code>0</code>.</li>
<li>Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.</li>
<li>Fixed an issue where misconfigured DEX HTTP tests prevented new registrations.</li>
<li>Fixed issues causing DNS requests to fail with clients in Traffic and DNS mode or DNS only mode.</li>
</ul>
</details><details class="nb-details"><summary>Linux 2025.10.186.0</summary><p><strong>Release date:</strong> 2026-01-13</p><p><a href="https://downloads.cloudflareclient.com/v1/download/noble-arm/version/2025.10.186.0">Download Linux 2025.10.186.0</a></p><h4 id="release-notes-35">Release notes</h4><p>This release contains minor fixes, improvements, and new features, including the ability to manage WARP client connectivity for all devices in your fleet using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>.</p>
<p>WARP client version 2025.8.779.0 introduced an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at <a href="https://pkg.cloudflareclient.com">pkg.cloudflareclient.com</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.</li>
<li>Linux <a href="/cloudflare-one/reusable-components/posture-checks/warp-client-checks/disk-encryption/">disk encryption posture check</a> now supports non-filesystem encryption types like <code>dm-crypt</code>.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> now supports transparent HTTP proxying in addition to CONNECT-based proxying.</li>
<li>Fixed an issue where the GUI becomes unresponsive when the <strong>Re-Authenticate in browser</strong> button is clicked.</li>
<li>Added a new feature to manage WARP client connectivity for all devices using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>. This feature allows administrators to send a global signal from an on-premises HTTPS endpoint that force disconnects or reconnects all WARP clients in an account based on configuration set on the endpoint.</li>
</ul>
</details><details class="nb-details"><summary>Linux 2025.9.558.0</summary><p><strong>Release date:</strong> 2025-11-11</p><p><a href="https://downloads.cloudflareclient.com/v1/download/centos8-intel/version/2025.9.558.0">Download Linux 2025.9.558.0</a></p><h4 id="release-notes-36">Release notes</h4><p>This release contains minor fixes, improvements, and new features including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">Path Maximum Transmission Unit Discovery (PMTUD)</a>. When PMTUD is enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to diagnose connectivity issues.</p>
<p>WARP client version 2025.8.779.0 introduced an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at <a href="https://pkg.cloudflareclient.com/">pkg.cloudflareclient.com</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to diagnose connectivity issues.</li>
<li>Fixed an issue where deleting a registration was erroneously reported as having failed.</li>
<li>Path Maximum Transmission Unit Discovery (PMTUD) may now be used to discover the effective MTU of the connection. This allows the WARP client to improve connectivity optimized for each network. PMTUD is disabled by default. To enable it, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">PMTUD documentation</a>.</li>
</ul>
</details><details class="nb-details"><summary>Linux 2025.8.779.0</summary><p><strong>Release date:</strong> 2025-10-07</p><p><a href="https://downloads.cloudflareclient.com/v1/download/bullseye-intel/version/2025.8.779.0">Download Linux 2025.8.779.0</a></p><h4 id="release-notes-37">Release notes</h4><p>This release contains significant fixes and improvements including an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at <a href="https://pkg.cloudflareclient.com/">pkg.cloudflareclient.com</a>.</p>
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
<li>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</li>
</ul>
</details><details class="nb-details"><summary>Linux 2025.7.176.0</summary><p><strong>Release date:</strong> 2025-09-30</p><p><a href="https://downloads.cloudflareclient.com/v1/download/fedora35-arm/version/2025.7.176.0">Download Linux 2025.7.176.0</a></p><h4 id="release-notes-38">Release notes</h4><p>This release contains minor fixes and improvements including an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at <a href="https://pkg.cloudflareclient.com/">pkg.cloudflareclient.com</a>.</p>
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
</details>
<h2 id="ios">iOS</h2>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>OS version</strong></td>
<td>iOS 11+</td>
</tr>
</tbody>
</table>
<p><a href="https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492">Download from the iOS App Store</a> or search for &quot;Cloudflare One Agent&quot;.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="migrate-from-1-1-1-1">Migrate from 1.1.1.1</h3>
@markup("md", "content/.markup/bodies/6111.md")
</aside>
<h2 id="android">Android</h2>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>OS version</strong></td>
<td>5.0+</td>
</tr>
</tbody>
</table>
<p><a href="https://play.google.com/store/apps/details?id=com.cloudflare.cloudflareoneagent">Download from the Google Play store</a> or search for &quot;Cloudflare One Agent&quot;.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="migrate-from-1-1-1-1-1">Migrate from 1.1.1.1</h3>
@markup("md", "content/.markup/bodies/6110.md")
</aside>
<h2 id="chromeos">ChromeOS</h2>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>OS version</strong></td>
<td>Chromebooks manufactured after 2019</td>
</tr>
</tbody>
</table>
<p>Chromebooks are supported by our <a href="#android">Android app</a>. All Chromebooks made after 2019 should fully support our Android app. If you have a Chromebook made before 2019, <a href="https://www.chromium.org/chromium-os/chrome-os-systems-supporting-android-apps/">refer to this list</a> to verify that your device is supported.</p>
