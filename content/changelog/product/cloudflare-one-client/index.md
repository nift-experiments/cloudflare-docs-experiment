---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/cloudflare-one-client/
  description: '2026-09-10'
  full_title: cloudflare-one-client changelog | Cloudflare Docs
  head_html: <title>cloudflare-one-client changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-10"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/cloudflare-one-client/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cloudflare-one-client changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-10"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/cloudflare-one-client/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/cloudflare-one-client/#page","headline":"cloudflare-one-client changelog | Cloudflare Docs","description":"2026-09-10","url":"https://developers.cloudflare.com/changelog/product/cloudflare-one-client/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/cloudflare-one-client/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="cloudflare-one-client-for-macos-version-2026-8-1290-1"><a href="/changelog/post/2026-09-09-warp-macos-beta/">Cloudflare One Client for macOS (version 2026.8.1290.1)</a></h2>
<p><em>2026-09-10</em></p>
<p>A new Beta release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This beta release includes the following changes and improvements:</p>
<ul>
<li>Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.</li>
<li>Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.</li>
<li>Improved API reliability by retrying requests dropped when reusing pooled connections.</li>
<li>Fixed Extra Logging failing to capture packets across all interfaces.</li>
<li>Fixed an issue that could prevent remote diagnostics from completing.</li>
<li>Fixed DNS connectivity checks failing on IPv6-only networks.</li>
<li>Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.</li>
<li>Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.</li>
<li>Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.</li>
<li>Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.</li>
<li>Fixed the client continuing to report 'No network' after a successful manual disconnect.</li>
<li>Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.</li>
<li>Fixed a startup crash when date formatting data for the system locale had not yet loaded.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>None</li>
</ul>
<p>For Zero Trust documentation, see: <a href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/</a><br />
For Consumer documentation, see: <a href="https://developers.cloudflare.com/warp-client/">https://developers.cloudflare.com/warp-client/</a></p>


<h2 id="cloudflare-one-client-for-windows-version-2026-8-1290-1"><a href="/changelog/post/2026-09-09-warp-windows-beta/">Cloudflare One Client for Windows (version 2026.8.1290.1)</a></h2>
<p><em>2026-09-10</em></p>
<p>A new Beta release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This beta release includes the following changes and improvements:</p>
<ul>
<li>Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.</li>
<li>Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.</li>
<li>Improved API reliability by retrying requests dropped when reusing pooled connections.</li>
<li>The client no longer requires the Windows WLAN AutoConfig service to be running.</li>
<li>Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.</li>
<li>Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.</li>
<li>Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.</li>
<li>Fixed the client continuing to report 'No network' after a successful manual disconnect.</li>
<li>Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.</li>
<li>Fixed the client UI crashing at startup when it could not write to the Windows registry.</li>
<li>Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.</li>
<li>Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.</li>
<li>Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.</li>
<li>Fixed a startup crash when date formatting data for the system locale had not yet loaded.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>None</li>
</ul>
<p>For Zero Trust documentation, see: <a href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/</a><br />
For Consumer documentation, see: <a href="https://developers.cloudflare.com/warp-client/">https://developers.cloudflare.com/warp-client/</a></p>


<h2 id="cloudflare-one-client-for-linux-version-2026-7-1377-0"><a href="/changelog/post/2026-08-28-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.7.1377.0)</a></h2>
<p><em>2026-08-29</em></p>
<p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.</p>


<h2 id="cloudflare-one-client-for-macos-version-2026-7-1376-0"><a href="/changelog/post/2026-08-28-warp-macos-ga/">Cloudflare One Client for macOS (version 2026.7.1376.0)</a></h2>
<p><em>2026-08-29</em></p>
<p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.</p>


<h2 id="cloudflare-one-client-for-windows-version-2026-7-1376-0"><a href="/changelog/post/2026-08-28-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.7.1376.0)</a></h2>
<p><em>2026-08-29</em></p>
<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>Fixed a rare but critical issue where the client could fail to connect or switch organizations due to an invalid registration after switching installed client versions. Additionally, this hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.</p>


<h2 id="cloudflare-one-client-for-macos-version-2026-7-1343-0"><a href="/changelog/post/2026-08-19-warp-macos-ga/">Cloudflare One Client for macOS (version 2026.7.1343.0)</a></h2>
<p><em>2026-08-20</em></p>
<p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces multiple features from our previous beta release into stable release, including:</p>
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


<h2 id="cloudflare-one-client-for-windows-version-2026-7-1343-0"><a href="/changelog/post/2026-08-19-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.7.1343.0)</a></h2>
<p><em>2026-08-20</em></p>
<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces multiple features from our previous beta release into stable release, including:</p>
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


<h2 id="cloudflare-one-client-for-linux-version-2026-7-1343-0"><a href="/changelog/post/2026-08-19-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.7.1343.0)</a></h2>
<p><em>2026-08-19</em></p>
<p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces multiple features from our previous beta release into stable release, including:</p>
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


<h2 id="cloudflare-one-client-for-windows-version-2026-6-905-0"><a href="/changelog/post/2026-08-10-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.6.905.0)</a></h2>
<p><em>2026-08-11</em></p>
<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix addresses an uncommon and intermittent case on Windows devices where the device is unable to reconnect after the device is woken from sleep.</p>


<h2 id="cloudflare-one-client-for-macos-version-2026-7-1210-1"><a href="/changelog/post/2026-07-31-warp-macos-beta/">Cloudflare One Client for macOS (version 2026.7.1210.1)</a></h2>
<p><em>2026-07-31</em></p>
<p>A new Beta release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This beta release includes the following changes and improvements:</p>
<ul>
<li>Improved connection reliability: the client now swaps protocol order after repeated connectivity-check failures, which helps when HTTP/3 is blocked after the QUIC handshake.</li>
<li>Fixed issue where a certificate error could be incorrectly displayed right after the connection is established.</li>
<li>A <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search domain</a> parsing failure no longer prevents connection.</li>
<li>Fixed a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">MASQUE</a> issue where the tunnel could stall while uploading at a high rate.</li>
<li>Fixed being unable to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/">switch organizations</a> when the client was stuck in the &quot;Device not in organization&quot; state.</li>
<li>Fixed the Home Screen dropdown popup not anchoring correctly.</li>
<li>Fixed a crash during dialog dismissal.</li>
<li>Increased tolerance for configurations with a large number of <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">local domain fallback</a> resolver IPs, so DNS resolution behaves correctly even when more fallback resolvers are configured than recommended.</li>
<li>Fixed the WARP client stealing window focus (for example, during reauth).</li>
<li>Fixed a client crash when connecting to a captive portal over Wi-Fi.</li>
<li>Fixed the system tray icon showing &quot;disconnected&quot; while the UI showed &quot;connected&quot;.</li>
<li>A successful re-authentication will cause the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> to be re-evaluated.</li>
<li>Improved <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">dashboard-managed client updates</a> by running the updater only when needed.</li>
</ul>


<h2 id="cloudflare-one-client-for-windows-version-2026-7-1210-1"><a href="/changelog/post/2026-07-31-warp-windows-beta/">Cloudflare One Client for Windows (version 2026.7.1210.1)</a></h2>
<p><em>2026-07-31</em></p>
<p>A new Beta release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This beta release includes the following changes and improvements:</p>
<ul>
<li>Improved connection reliability: the client now swaps protocol order after repeated connectivity-check failures, which helps when HTTP/3 is blocked after the QUIC handshake.</li>
<li>Fixed issue where a certificate error could be incorrectly displayed right after the connection is established.</li>
<li>A <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search domain</a> parsing failure no longer prevents connection.</li>
<li>Fixed a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">MASQUE</a> issue where the tunnel could stall while uploading at a high rate.</li>
<li>Fixed being unable to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/">switch organizations</a> when the client was stuck in the &quot;Device not in organization&quot; state.</li>
<li>Fixed the Home Screen dropdown popup not anchoring correctly.</li>
<li>Fixed a crash during dialog dismissal.</li>
<li>Increased tolerance for configurations with a large number of <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">local domain fallback</a> resolver IPs, so DNS resolution behaves correctly even when more fallback resolvers are configured than recommended.</li>
<li>Fixed a networking issue where IPv6 multicast routes were being assigned to the WARP tunnel interface.</li>
<li>Fixed fatal errors on UI load on Windows 10.</li>
<li>Fixed a crash during Windows notification initialization.</li>
<li>Made the Windows <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/domain-joined/">domain-joined posture check</a> more reliable.</li>
<li>Fixed orphaned credentials left behind on multi-user uninstall.</li>
<li>A successful re-authentication will cause the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> to be re-evaluated.</li>
<li>Improved <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">dashboard-managed client updates</a> by running the updater only when needed.</li>
</ul>


<h2 id="cloudflare-one-client-for-linux-version-2026-6-880-0"><a href="/changelog/post/2026-07-21-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.6.880.0)</a></h2>
<p><em>2026-07-22</em></p>
<p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.</p>


<h2 id="cloudflare-one-client-for-macos-version-2026-6-880-0"><a href="/changelog/post/2026-07-21-warp-macos-ga/">Cloudflare One Client for macOS (version 2026.6.880.0)</a></h2>
<p><em>2026-07-22</em></p>
<p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.</p>


<h2 id="cloudflare-one-client-for-windows-version-2026-6-880-0"><a href="/changelog/post/2026-07-21-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.6.880.0)</a></h2>
<p><em>2026-07-22</em></p>
<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.</p>


<h2 id="cloudflare-one-client-for-windows-version-2026-6-850-0"><a href="/changelog/post/2026-07-07-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.6.850.0)</a></h2>
<p><em>2026-07-08</em></p>
<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix addresses a Windows authentication issue in the embedded WebView2 browser. Single sign-on could fail to use the Windows primary account, causing users to be prompted for an interactive sign-in. The embedded authentication browser now allows SSO providers to use the OS primary account when available.</p>


<h2 id="cloudflare-one-client-for-linux-version-2026-6-836-0"><a href="/changelog/post/2026-07-01-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.6.836.0)</a></h2>
<p><em>2026-07-02</em></p>
<p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This package is the same release as 2026.6.822.0, with a fix for our RPM package. Previously the repository served a single build to every OS version, so an install could pull a dependency that isn't available on that release. The repository now serves the correct build for each operating system version, so installs automatically pull the dependencies that version requires. Debian and Ubuntu were not affected.</p>
<p>If you installed version 2026.6.822.0 on an RPM-based distribution, we recommend refreshing your repository configuration:</p>
<pre tabindex="0"><code class="language-bash">sudo curl -fsSL https://pkg.cloudflareclient.com/cloudflare-warp-ascii.repo | sudo tee /etc/yum.repos.d/cloudflare-warp.repo&#10;sudo dnf clean all&#10;sudo dnf install cloudflare-warp&#10;</code></pre>


<h2 id="cloudflare-one-client-for-linux-version-2026-6-822-0"><a href="/changelog/post/2026-06-29-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.6.822.0)</a></h2>
<p><em>2026-06-30</em></p>
<p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces multiple features from our previous beta release into stable release, including:</p>
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


<h2 id="cloudflare-one-client-for-macos-version-2026-6-822-0"><a href="/changelog/post/2026-06-29-warp-macos-ga/">Cloudflare One Client for macOS (version 2026.6.822.0)</a></h2>
<p><em>2026-06-30</em></p>
<p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces multiple features from our previous beta release into stable release, including:</p>
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


<h2 id="cloudflare-one-client-for-windows-version-2026-6-822-0"><a href="/changelog/post/2026-06-29-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.6.822.0)</a></h2>
<p><em>2026-06-30</em></p>
<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces multiple features from our previous beta release into stable release, including:</p>
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


<h2 id="cloudflare-one-client-for-macos-version-2026-6-782-1"><a href="/changelog/post/2026-06-24-warp-macos-beta/">Cloudflare One Client for macOS (version 2026.6.782.1)</a></h2>
<p><em>2026-06-25</em></p>
<p>A new Beta release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This beta release introduces upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the Secure Enclave whenever available to provide stronger protection against device impersonation.</p>
<p><strong>Additional changes and improvements</strong></p>
<p>This release also introduces multiple fixes and improvements including:</p>
<ul>
<li>Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in the macOS Display settings.</li>
<li>Path MTU Discovery (PMTUD) is now enabled by default.</li>
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
</ul>


<h2 id="cloudflare-one-client-for-macos-version-2026-5-1155-1"><a href="/changelog/post/2026-05-29-warp-macos-beta/">Cloudflare One Client for macOS (version 2026.5.1155.1)</a></h2>
<p><em>2026-05-29</em></p>
<p>A new Beta release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release introduces the new Cloudflare One Client UI for macOS! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
<ul>
<li>Right click context menu to access the most common client actions quickly</li>
<li>Built-in captive portal login experience</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>The client now applies DNS search suffixes configured in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles">device profile</a> / <a href="/cloudflare-one/traffic-policies/network-policies">network policy</a>. Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search suffixes</a> for details.</li>
<li>Administrators can now control which virtual networks (VNETs) are available to which users via WARP device profile settings in the Zero Trust dashboard. Previously, every VNET in the organization was visible to every device; you can now scope the VNET picker per profile so users only see the networks relevant to them. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#vnet-availability">VNET availability</a> for details.</li>
<li>Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.</li>
<li>Added new warp-cli debug commands for interactive connection diagnosis. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging">Extra debug logging</a> for details.</li>
<li>The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.</li>
<li>Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs">Cloudflare One MDM documentation</a> for details.</li>
<li>Client Certificate device-posture checks now support template variables (e.g. <code>${serial_number}</code>, <code>${device_uuid}</code>) in the Subject Alternative Name field, matching what the documentation has always claimed. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.</li>
<li>Fixed the in-client captive-portal browser rendering a blank &quot;Success&quot; page on some airline Wi-Fi networks (United inflight Wi-Fi was the reported case). The browser now reliably loads the airline's real portal page so users can complete sign-in from inside the client instead of having to open a separate browser.</li>
<li>Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Split tunnel list configuration is not available in the new UI. Management of split tunnel entries is currently only possible via <code>warp-cli tunnel ip</code> and <code>warp-cli tunnel host</code>. UI support will be added in a future release.</li>
</ul>


<h2 id="cloudflare-one-client-for-windows-version-2026-5-1155-1"><a href="/changelog/post/2026-05-29-warp-windows-beta/">Cloudflare One Client for Windows (version 2026.5.1155.1)</a></h2>
<p><em>2026-05-29</em></p>
<p>A new Beta release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release introduces the new Cloudflare One Client UI for Windows! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
<ul>
<li>Right click context menu to access the most common client actions quickly</li>
<li>Built-in captive portal login experience</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>The client now applies DNS search suffixes configured in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles">device profile</a> / <a href="/cloudflare-one/traffic-policies/network-policies">network policy</a>. Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search suffixes</a> for details.</li>
<li>Administrators can now control which virtual networks (VNETs) are available to which users via WARP device profile settings in the Zero Trust dashboard. Previously, every VNET in the organization was visible to every device; you can now scope the VNET picker per profile so users only see the networks relevant to them. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#vnet-availability">VNET availability</a> for details.</li>
<li>Added mandatory authentication. When enabled via MDM, the Cloudflare One Client blocks all Internet traffic from the moment the machine boots until the user authenticates, closing the visibility gap on newly deployed devices and during re-authentication. See the <a href="https://blog.cloudflare.com/mandatory-authentication-mfa/">announcement blog</a> and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-no-auth-no-internet/">documentation</a> for details.</li>
<li>Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.</li>
<li>Added new warp-cli debug commands for interactive connection diagnosis. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging">Extra debug logging</a> for details.</li>
<li>The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.</li>
<li>Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs">Cloudflare One MDM documentation</a> for details.</li>
<li>Client Certificate device-posture checks now support template variables (e.g. <code>${serial_number}</code>, <code>${device_uuid}</code>) in the Subject Alternative Name field, matching what the documentation has always claimed. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.</li>
<li>The UseWebView2 registry value (HKLM\SOFTWARE\Cloudflare\CloudflareWARP\UseWebView2 = y) is once again honored by the new GUI for authentication, so administrators who prefer the embedded WebView2 browser for sign-in can opt back in. This setting was effectively ignored in the previous release; the default browser was always used. This key is now also honored for re-authentications.</li>
<li>Fixed a crash in the authentication browser when navigating to a site that prompts for browser permissions (microphone, camera, notifications, etc.). The same fix had previously landed for the captive-portal browser; this extends it to the auth browser.</li>
<li>Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
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


<h2 id="cloudflare-one-client-for-linux-version-2026-4-1390-0"><a href="/changelog/post/2026-05-26-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.4.1390.0)</a></h2>
<p><em>2026-05-27</em></p>
<p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces the new Cloudflare One Client UI for Linux! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
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


<h2 id="cloudflare-one-client-for-macos-version-2026-4-1390-0"><a href="/changelog/post/2026-05-26-warp-macos-ga/">Cloudflare One Client for macOS (version 2026.4.1390.0)</a></h2>
<p><em>2026-05-27</em></p>
<p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces the new Cloudflare One Client UI for macOS! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
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


<h2 id="cloudflare-one-client-for-windows-version-2026-4-1390-0"><a href="/changelog/post/2026-05-26-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.4.1390.0)</a></h2>
<p><em>2026-05-27</em></p>
<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces the new Cloudflare One Client UI for Windows! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
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


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 3</span><a class="pagination-next" rel="next" href="/changelog/product/cloudflare-one-client/2/">Next</a></nav>
