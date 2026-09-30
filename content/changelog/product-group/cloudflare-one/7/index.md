---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/cloudflare-one/7/
  description: '2026-03-11'
  full_title: Cloudflare One changelog - page 7 | Cloudflare Docs
  head_html: <title>Cloudflare One changelog - page 7 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-03-11"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/7/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cloudflare One changelog - page 7"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-03-11"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/7/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/7/#page","headline":"Cloudflare One changelog - page 7 | Cloudflare Docs","description":"2026-03-11","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/7/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/cloudflare-one/7/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="warp-client-for-macos-version-2026-3-566-1"><a href="/changelog/post/2026-03-10-warp-macos-beta/">WARP client for macOS (version 2026.3.566.1)</a></h2>
<p><em>2026-03-11</em></p>
<p>A new Beta release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes and introduces a brand new visual style for the client interface. The new Cloudflare One Client interface changes connectivity management from a toggle to a button and brings useful connectivity settings to the home screen. The redesign also introduces a collapsible navigation bar. When expanded, more client information can be accessed including connectivity, settings, and device profile information. If you have any feedback or questions, visit the <a href="https://community.cloudflare.com/t/introducing-the-new-cloudflare-one-client-interface/901362">Cloudflare Community forum</a> and let us know.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.</li>
<li>Fixed an issue in proxy mode where the client could become unresponsive due to upstream connection timeouts.</li>
<li>Fixed emergency disconnect state from a previous organization incorrectly persisting after switching organizations.</li>
<li>Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.</li>
<li>Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.</li>
<li>Added monitoring for tunnel statistics collection timeouts.</li>
<li>Switched tunnel congestion control algorithm to Cubic for improved reliability across platforms.</li>
<li>Fixed initiating managed network detection checks when no network is available, which caused device profile flapping.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>The client may become stuck in a <code>Connecting</code> state. To resolve this issue, reconnect the client by selecting <strong>Disconnect</strong> and then <strong>Connect</strong> in the client user interface. Alternatively, change the client's operation mode.</li>
<li>The client may display an empty white screen upon the device waking from sleep. To resolve this issue, exit and then open the client to re-launch it.</li>
<li>Canceling login during a single MDM configuration setup results in an empty page with no way to resume authentication. To work around this issue, exit and relaunch the client.</li>
</ul>


<h2 id="warp-client-for-windows-version-2026-3-566-1"><a href="/changelog/post/2026-03-10-warp-windows-beta/">WARP client for Windows (version 2026.3.566.1)</a></h2>
<p><em>2026-03-11</em></p>
<p>A new Beta release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes and introduces a brand new visual style for the client interface. The new Cloudflare One Client interface changes connectivity management from a toggle to a button and brings useful connectivity settings to the home screen. The redesign also introduces a collapsible navigation bar. When expanded, more client information can be accessed including connectivity, settings, and device profile information. If you have any feedback or questions, visit the <a href="https://community.cloudflare.com/t/introducing-the-new-cloudflare-one-client-interface/901362">Cloudflare Community forum</a> and let us know.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.</li>
<li>Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.</li>
<li>Added monitoring for tunnel statistics collection timeouts.</li>
<li>Switched tunnel congestion control algorithm to Cubic for improved reliability across platforms.</li>
<li>Fixed packet capture failing on tunnel interface when the tunnel interface is renamed by SCCM VPN boundary support.</li>
<li>Fixed unnecessary registration deletion caused by RDP connections in multi-user mode.</li>
<li>Fixed increased tunnel interface start-up time due to a race between duplicate address detection (DAD) and disabling NetBT.</li>
<li>Fixed tunnel failing to connect when the system DNS search list contains unexpected characters.</li>
<li>Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.</li>
<li>Fixed an issue in proxy mode where the client could become unresponsive due to upstream connection timeouts.</li>
<li>Fixed emergency disconnect state from a previous organization incorrectly persisting after switching organizations.</li>
<li>Fixed initiating managed network detection checks when no network is available, which caused device profile flapping.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>The client may unexpectedly terminate during captive portal login. To work around this issue, use a web browser to authenticate with the captive portal and then re-launch the client.</li>
<li>An error indicating that Microsoft Edge can't read and write to its data directory may be displayed during captive portal login; this error is benign and can be dismissed.</li>
<li>The client may become stuck in a <code>Connecting</code> state. To resolve this issue, reconnect the client by selecting <strong>Disconnect</strong> and then <strong>Connect</strong> in the client user interface. Alternatively, change the client's operation mode.</li>
<li>The client may display an empty white screen upon the device waking from sleep. To resolve this issue, exit and then open the client to re-launch it.</li>
<li>Canceling login during a single MDM configuration setup results in an empty page with no way to resume authentication. To work around this issue, exit and relaunch the client.</li>
<li>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 version KB5062553</a> or higher for resolution.</li>
<li>Devices with KB5055523 installed may receive a warning about <code>Win32/ClickFix.ABA</code> being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to <a href="https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0">version 1.429.19.0</a> or later. This warning will be omitted from future release notes. This Microsoft Security Intelligence update was released in May 2025.</li>
<li>DNS resolution may be broken when the following conditions are all true:
<ul>
<li>The client is in Secure Web Gateway without DNS filtering (tunnel-only) mode.</li>
<li>A custom DNS server address is configured on the primary network adapter.</li>
<li>The custom DNS server address on the primary network adapter is changed while the client is connected.
To work around this issue, reconnect the client by selecting <strong>Disconnect</strong> and then <strong>Connect</strong> in the client user interface.</li>
</ul>
</li>
</ul>


<h2 id="user-risk-score-selector-in-access-policies"><a href="/changelog/post/2026-03-04-user-risk-score-access-policies/">User risk score selector in Access policies</a></h2>
<p><em>2026-03-04</em></p>
<p>You can now use <a href="/cloudflare-one/team-and-resources/users/risk-score/">user risk scores</a> in your <a href="/cloudflare-one/access-controls/policies/">Access policies</a>. The new <strong>User Risk Score</strong> selector allows you to create Access policies that respond to user behavior patterns detected by Cloudflare's risk scoring system, including impossible travel, high DLP policy matches, and more.</p>
<p>For more information, refer to <a href="/cloudflare-one/team-and-resources/users/risk-score/#use-risk-scores-in-access-policies">Use risk scores in Access policies</a>.</p>


<h2 id="gateway-authorization-proxy-and-hosted-pac-files-open-beta"><a href="/changelog/post/2026-03-04-gateway-authorization-proxy-open-beta/">Gateway Authorization Proxy and hosted PAC files (open beta)</a></h2>
<p><em>2026-03-04</em></p>
<p>The <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">Gateway Authorization Proxy</a> and <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file">PAC file hosting</a> are now in open beta for all plan types.</p>
<p>Previously, <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint">proxy endpoints</a> relied on static source IP addresses to authorize traffic, providing no user-level identity in logs or policies. The new authorization proxy replaces IP-based authorization with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> authentication, verifying who a user is before applying Gateway filtering without installing the WARP client.</p>
<p>This is ideal for environments where you cannot deploy a device client, such as virtual desktops (VDI), mergers and acquisitions, or compliance-restricted endpoints.</p>
<h4 id="2026-03-04-gateway-authorization-proxy-open-beta-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Identity-aware proxy traffic</strong> — Users authenticate through your identity provider (Okta, Microsoft Entra ID, Google Workspace, and others) via Cloudflare Access. Logs now show exactly which user accessed which site, and you can write <a href="/cloudflare-one/traffic-policies/identity-selectors/">identity-based policies</a> like &quot;only the Finance team can access this accounting tool.&quot;</li>
<li><strong>Multiple identity providers</strong> — Display one or multiple login methods simultaneously, giving flexibility for organizations managing users across different identity systems.</li>
<li><strong>Cloudflare-hosted PAC files</strong> — Create and host <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file">PAC files</a> directly in Cloudflare One with pre-configured templates for Okta and Azure, hosted at <code>https://pac.cloudflare-gateway.com/&lt;account-id&gt;/&lt;slug&gt;</code> on Cloudflare's global network.</li>
<li><strong>Simplified billing</strong> — Each user occupies a seat, exactly like they do with the Cloudflare One Client. No new metrics to track.</li>
</ul>
<h4 id="2026-03-04-gateway-authorization-proxy-open-beta-get-started">Get started</h4>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Networks</strong> &gt; <strong>Resolvers &amp; Proxies</strong> &gt; <strong>Proxy endpoints</strong>.</li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">Create an authorization proxy endpoint</a> and configure Access policies.</li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file">Create a hosted PAC file</a> or write your own.</li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#3b-configure-browser-to-use-pac-file">Configure browsers</a> to use the PAC file URL.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">Install the Cloudflare certificate</a> for HTTPS inspection.</li>
</ol>
<p>For more details, refer to the <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints documentation</a> and the <a href="https://blog.cloudflare.com/gateway-authorization-proxy-identity-aware-policies/">announcement blog post</a>.</p>


<h2 id="copy-cloudflare-one-resources-as-json-or-post-requests"><a href="/changelog/post/2026-03-copy-resources-as-json-or-post-requests/">Copy Cloudflare One resources as JSON or POST requests</a></h2>
<p><em>2026-03-02</em></p>
<p>You can now copy Cloudflare One resources as JSON or as a ready-to-use API POST request directly from the dashboard. This makes it simple to transition workflows into API calls, automation scripts, or infrastructure-as-code pipelines.</p>
<p>To use this feature, click the overflow menu (⋮) on any supported resource and select <strong>Copy as JSON</strong> or <strong>Copy as POST request</strong>. The copied output includes only the fields present on your resource, giving you a clean and minimal starting point for your own API calls.</p>
<p>Initially supported resources:</p>
<ul>
<li>Access applications</li>
<li>Access policies</li>
<li>Gateway policies</li>
<li>Resolver policies</li>
<li>Service tokens</li>
<li>Identity providers</li>
</ul>
<p>We will continue to add support for more resources throughout 2026.</p>


<h2 id="clipboard-controls-for-browser-based-rdp"><a href="/changelog/post/2026-03-01-rdp-clipboard-controls/">Clipboard controls for browser-based RDP</a></h2>
<p><em>2026-03-01</em></p>
<p>You can now configure clipboard controls for browser-based RDP with Cloudflare Access. Clipboard controls allow administrators to restrict whether users can copy or paste text between their local machine and the remote Windows server.</p>
<p><img src="/assets/upstream/images/changelog/access/rdp-clipboard-controls.png" alt="Enable users to copy and paste content from their local machine to remote RDP sessions in the Cloudflare One dashboard" /></p>
<p>This feature is useful for organizations that support bring-your-own-device (BYOD) policies or third-party contractors using unmanaged devices. By restricting clipboard access, you can prevent sensitive data from being transferred out of the remote session to a user's personal device.</p>
<h4 id="2026-03-01-rdp-clipboard-controls-configuration-options">Configuration options</h4>
<p>Clipboard controls are configured per policy within your Access application. For each policy, you can independently allow or deny:</p>
<ul>
<li><strong>Copy from local client to remote RDP session</strong> — Users can copy/paste text from their local machine into the browser-based RDP session.</li>
<li><strong>Copy from remote RDP session to local client</strong> — Users can copy/paste text from the browser-based RDP session to their local machine.</li>
</ul>
<p>By default, both directions are denied for new policies. For existing Access applications created before this feature was available, clipboard access remains enabled to preserve backwards compatibility.</p>
<p>When a user attempts a restricted clipboard action, the clipboard content is replaced with an error message informing them that the action is not allowed.</p>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#clipboard-controls">Clipboard controls for browser-based RDP</a>.</p>


<h2 id="export-mcp-server-portal-logs-with-logpush"><a href="/changelog/post/2026-02-27-mcp-portal-logpush/">Export MCP server portal logs with Logpush</a></h2>
<p><em>2026-02-27</em></p>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2026-02-27-mcp-portal-logpush-availability">Availability</h4>
@markup("md", "content/.markup/bodies/17617.md")</aside>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> now supports <a href="/logs/logpush/">Logpush</a> integration. You can automatically export MCP server portal activity logs to third-party storage destinations or security information and event management (SIEM) tools for analysis and auditing.</p>
<h4 id="2026-02-27-mcp-portal-logpush-available-log-fields">Available log fields</h4>
<p>The MCP server portal logs dataset includes fields such as:</p>
<ul>
<li><code>Datetime</code> — Timestamp of the request</li>
<li><code>PortalID</code> / <code>PortalAUD</code> — Portal identifiers</li>
<li><code>ServerID</code> / <code>ServerURL</code> — Upstream MCP server details</li>
<li><code>Method</code> — JSON-RPC method (for example, <code>tools/call</code>, <code>prompts/get</code>, <code>resources/read</code>)</li>
<li><code>ToolCallName</code> / <code>PromptGetName</code> / <code>ResourceReadURI</code> — Method-specific identifiers</li>
<li><code>UserID</code> / <code>UserEmail</code> — Authenticated user information</li>
<li><code>Success</code> / <code>Error</code> — Request outcome</li>
<li><code>ServerResponseDurationMs</code> — Response time from upstream server</li>
</ul>
<p>For the complete field reference, refer to <a href="/logs/logpush/logpush-job/datasets/account/mcp_portal_logs/">MCP portal logs</a>.</p>
<h4 id="2026-02-27-mcp-portal-logpush-set-up-logpush">Set up Logpush</h4>
<p>To configure Logpush for MCP server portal logs, refer to <a href="/cloudflare-one/insights/logs/logpush/">Logpush integration</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17616.md")</aside>


<h2 id="new-protocols-added-for-gateway-protocol-detection-beta"><a href="/changelog/post/2026-02-27-new-protocol-detection-protocols/">New protocols added for Gateway Protocol Detection (Beta)</a></h2>
<p><em>2026-02-27</em></p>
<p>Gateway <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">Protocol Detection</a> now supports seven additional protocols in beta:</p>
<table>
<thead>
<tr>
<th>Protocol</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>IMAP</td>
<td>Internet Message Access Protocol — email retrieval</td>
</tr>
<tr>
<td>POP3</td>
<td>Post Office Protocol v3 — email retrieval</td>
</tr>
<tr>
<td>SMTP</td>
<td>Simple Mail Transfer Protocol — email sending</td>
</tr>
<tr>
<td>MYSQL</td>
<td>MySQL database wire protocol</td>
</tr>
<tr>
<td>RSYNC-DAEMON</td>
<td>rsync daemon protocol</td>
</tr>
<tr>
<td>LDAP</td>
<td>Lightweight Directory Access Protocol</td>
</tr>
<tr>
<td>NTP</td>
<td>Network Time Protocol</td>
</tr>
</tbody>
</table>
<p>These protocols join the existing set of detected protocols (HTTP, HTTP2, SSH, TLS, DCERPC, MQTT, and TPKT) and can be used with the <em>Detected Protocol</em> selector in <a href="/cloudflare-one/traffic-policies/network-policies/">Network policies</a> to identify and filter traffic based on the application-layer protocol, without relying on port-based identification.</p>
<p>If protocol detection is enabled on your account, these protocols will automatically be logged when detected in your Gateway network traffic.</p>
<p>For more information on using Protocol Detection, refer to the <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">Protocol detection documentation</a>.</p>


<h2 id="warp-client-for-linux-version-2026-1-150-0"><a href="/changelog/post/2026-02-24-warp-linux-ga/">WARP client for Linux (version 2026.1.150.0)</a></h2>
<p><em>2026-02-24</em></p>
<p>A new GA release for the Linux WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p>WARP client version 2025.8.779.0 introduced an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at <a href="https://pkg.cloudflareclient.com">pkg.cloudflareclient.com</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Fixed an issue causing failure of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion">local network exclusion</a> feature when configured with a timeout of <code>0</code>.</li>
<li>Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.</li>
<li>Fixed an issue where misconfigured DEX HTTP tests prevented new registrations.</li>
<li>Fixed issues causing DNS requests to fail with clients in Traffic and DNS mode or DNS only mode.</li>
</ul>


<h2 id="warp-client-for-macos-version-2026-1-150-0"><a href="/changelog/post/2026-02-24-warp-macos-ga/">WARP client for macOS (version 2026.1.150.0)</a></h2>
<p><em>2026-02-24</em></p>
<p>A new GA release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Fixed an issue causing failure of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion">local network exclusion</a> feature when configured with a timeout of <code>0</code>.</li>
<li>Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.</li>
<li>Fixed an issue with DNS server configuration failures that caused tunnel connection delays.</li>
<li>Fixed an issue where misconfigured DEX HTTP tests prevented new registrations.</li>
<li>Fixed an issue causing DNS requests to fail with clients in Traffic and DNS mode.</li>
</ul>


<h2 id="warp-client-for-windows-version-2026-1-150-0"><a href="/changelog/post/2026-02-24-warp-windows-ga/">WARP client for Windows (version 2026.1.150.0)</a></h2>
<p><em>2026-02-24</em></p>
<p>A new GA release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features.</p>
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


<h2 id="understand-casb-findings-instantly-with-cloudy-summaries"><a href="/changelog/post/2026-02-20-cloudy-in-casb/">Understand CASB findings instantly with Cloudy Summaries</a></h2>
<p><em>2026-02-20</em></p>
<p>You can now easily understand your SaaS security posture findings and why they were detected with <strong>Cloudy Summaries in CASB</strong>. This feature integrates Cloudflare's Cloudy AI directly into your CASB Posture Findings to automatically generate clear, plain-language summaries of complex security misconfigurations, third-party app risks, and data exposures.</p>
<p>This allows security teams and IT administrators to drastically reduce triage time by immediately understanding the context, potential impact, and necessary remediation steps for any given finding—without needing to be an expert in every connected SaaS application.</p>
<p>To view a summary, simply navigate to your Posture Findings in the Cloudflare One dashboard (under <strong>Cloud and SaaS findings</strong>) and open the finding details of a specific instance of a Finding.</p>
<p>Cloudy Summaries are supported on all available integrations, including Microsoft 365, Google Workspace, Salesforce, GitHub, AWS, Slack, and Dropbox. See the full list of supported integrations <a href="/cloudflare-one/integrations/cloud-and-saas/">here</a>.</p>
<h4 id="2026-02-20-cloudy-in-casb-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Contextual explanations</strong> — Quickly understand the specifics of a finding with plain-language summaries detailing exactly what was detected, from publicly shared sensitive files to risky third-party app scopes.</li>
<li><strong>Clear risk assessment</strong> — Instantly grasp the potential security impact of the finding, such as data breach risks, unauthorized account access, or email spoofing vulnerabilities.</li>
<li><strong>Actionable guidance</strong> — Get clear recommendations and next steps on how to effectively remediate the issue and secure your environment.</li>
<li><strong>Built-in feedback</strong> — Help improve future AI summarization accuracy by submitting feedback directly using the thumbs-up and thumbs-down buttons.</li>
</ul>
<h4 id="2026-02-20-cloudy-in-casb-learn-more">Learn more</h4>
<ul>
<li>Learn more about managing <a href="/cloudflare-one/cloud-and-saas-findings/">CASB Posture Findings</a> in Cloudflare.</li>
</ul>
<p>Cloudy Summaries in CASB are available to all Cloudflare CASB users today.</p>


<h2 id="manage-cloudflare-tunnel-directly-from-the-main-cloudflare-dashboard"><a href="/changelog/post/2026-02-20-tunnel-core-dashboard/">Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard</a></h2>
<p><em>2026-02-20</em></p>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> is now available in the main Cloudflare Dashboard at <a href="https://dash.cloudflare.com/?to=/:account/tunnels">Networking &gt; Tunnels</a>, bringing first-class Tunnel management to developers using Tunnel for securing origin servers.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-core-dashboard.gif" alt="Manage Tunnels in the Core Dashboard" /></p>
<p>This new experience provides everything you need to manage Tunnels for <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a>, including:</p>
<ul>
<li><strong>Full Tunnel lifecycle management</strong>: Create, configure, delete, and monitor all your Tunnels in one place.</li>
<li><strong>Native integrations</strong>: View Tunnels by name when configuring <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS records</a> and <a href="/workers-vpc/">Workers VPC</a> — no more copy-pasting UUIDs.</li>
<li><strong>Real-time visibility</strong>: Monitor <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">replicas</a> and Tunnel <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status">health status</a> directly in the dashboard.</li>
<li><strong>Routing map</strong>: Manage all ingress routes for your Tunnel, including <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a>, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostnames</a>, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">private CIDRs</a>, and <a href="/workers-vpc/">Workers VPC services</a>, from a single interactive interface.</li>
</ul>
<h4 id="2026-02-20-tunnel-core-dashboard-choose-the-right-dashboard-for-your-use-case">Choose the right dashboard for your use case</h4>
<p><strong>Core Dashboard</strong>: Navigate to <a href="https://dash.cloudflare.com/?to=/:account/tunnels">Networking &gt; Tunnels</a> to manage Tunnels for:</p>
<ul>
<li>Securing origin servers and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a> with CDN, WAF, Load Balancing, and DDoS protection</li>
<li>Connecting <a href="/workers-vpc/">Workers to private services</a> via Workers VPC</li>
</ul>
<p><strong>Cloudflare One Dashboard</strong>: Navigate to <a href="https://one.dash.cloudflare.com/?to=/:account/networks/connectors">Zero Trust &gt; Networks &gt; Connectors</a> to manage Tunnels for:</p>
<ul>
<li>Securing your public applications with <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Zero Trust access policies</a></li>
<li>Connecting users to <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private applications</a></li>
<li>Building a <a href="/reference-architecture/architectures/sase/#connecting-networks">private mesh network</a></li>
</ul>
<p>Both dashboards provide complete Tunnel management capabilities — choose based on your primary workflow.</p>
<h4 id="2026-02-20-tunnel-core-dashboard-get-started">Get started</h4>
<p>New to Tunnel? Learn how to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">get started with Cloudflare Tunnel</a> or explore advanced use cases like <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/">securing SSH servers</a> or <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/kubernetes/">running Tunnels in Kubernetes</a>.</p>


<h2 id="dex-supports-eu-customer-metadata-boundary"><a href="/changelog/post/2026-02-19-dex-supports-cmb-eu/">DEX Supports EU Customer Metadata Boundary</a></h2>
<p><em>2026-02-19</em></p>
<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into <a href="/warp-client/">WARP</a> device connectivity and performance to any internal or external application.</p>
<p>Now, all DEX logs are fully compatible with Cloudflare's <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary</a> (CMB) setting for the 'EU' (European Union), which ensures that DEX logs will not be stored outside the 'EU' when the option is configured.</p>
<p>If a Cloudflare One customer using DEX enables CMB 'EU', they will not see any DEX data in the Cloudflare One dashboard. Customers can ingest DEX data via <a href="/logs/logpush/">LogPush</a>, and build their own analytics and dashboards.</p>
<p>If a customer enables CMB in their account, they will see the following message in the Digital Experience dashboard: &quot;DEX data is unavailable because Customer Metadata Boundary configuration is on. Use Cloudflare LogPush to export DEX datasets.&quot;</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_supports_cmb.png" alt="Digital Experience Monitoring message when Customer Metadata Boundary for the EU is enabled" /></p>


<h2 id="streamlined-clientless-browser-isolation-for-private-applications"><a href="/changelog/post/2026-02-17-clientless-access-for-private-apps/">Streamlined clientless browser isolation for private applications</a></h2>
<p><em>2026-02-17</em></p>
<p>A new <strong>Allow clientless access</strong> setting makes it easier to connect users without a device client to internal applications, without using public DNS.</p>
<p><img src="/assets/upstream/images/changelog/access/allow-clientless-access.png" alt="Allow clientless access setting in the Cloudflare One dashboard" /></p>
<p>Previously, to provide clientless access to a private hostname or IP without a <a href="/cloudflare-one/networks/routes/add-routes/#add-a-published-application-route">published application</a>, you had to create a separate <a href="/cloudflare-one/access-controls/applications/bookmarks/">bookmark application</a> pointing to a prefixed <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">Clientless Web Isolation</a> URL (for example, <code>https://&lt;your-teamname&gt;.cloudflareaccess.com/browser/https://10.0.0.1/</code>). This bookmark was visible to all users in the App Launcher, regardless of whether they had access to the underlying application.</p>
<p>Now, you can manage clientless access directly within your <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private self-hosted application</a>. When  <strong>Allow clientless access</strong> is turned on, users who pass your Access application policies will see a tile in their App Launcher pointing to the prefixed URL. Users must have <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">remote browser permissions</a> to open the link.</p>


<h2 id="policies-for-bookmark-applications"><a href="/changelog/post/2026-02-17-policies-for-bookmarks/">Policies for bookmark applications</a></h2>
<p><em>2026-02-17</em></p>
<p>You can now assign <a href="/cloudflare-one/access-controls/policies/">Access policies</a> to <a href="/cloudflare-one/access-controls/applications/bookmarks/">bookmark applications</a>. This lets you control which users see a bookmark in the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a> based on identity, device posture, and other policy rules.</p>
<p>Previously, bookmark applications were visible to all users in your organization. With policy support, you can now:</p>
<ul>
<li><strong>Tailor the App Launcher to each user</strong> — Users only see the applications they have access to, reducing clutter and preventing accidental clicks on irrelevant resources.</li>
<li><strong>Restrict visibility of sensitive bookmarks</strong> — Limit who can view bookmarks to internal tools or partner resources based on group membership, identity provider, or device posture.</li>
</ul>
<p>Bookmarks support all <a href="/cloudflare-one/access-controls/policies/">Access policy configurations</a> except purpose justification, temporary authentication, and application isolation. If no policy is assigned, the bookmark remains visible to all users (maintaining backwards compatibility).</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/applications/bookmarks/">Add bookmarks</a>.</p>


<h2 id="cloudflare-one-product-name-updates"><a href="/changelog/post/2026-02-17-product-name-updates/">Cloudflare One Product Name Updates</a></h2>
<p><em>2026-02-17</em></p>
<p>We are updating naming related to some of our Networking products to better clarify their place in the Zero Trust and Secure Access Service Edge (SASE) journey.</p>
<p>We are retiring some older brand names in favor of names that describe exactly what the products do within your network. We are doing this to help customers build better, clearer mental models for comprehensive SASE architecture delivered on Cloudflare.</p>
<h4 id="2026-02-17-product-name-updates-what-s-changing">What's changing</h4>
<ul>
<li><strong>Magic WAN</strong> → <strong>Cloudflare WAN</strong></li>
<li><strong>Magic WAN IPsec</strong> → <strong>Cloudflare IPsec</strong></li>
<li><strong>Magic WAN GRE</strong> → <strong>Cloudflare GRE</strong></li>
<li><strong>Magic WAN Connector</strong> → <strong>Cloudflare One Appliance</strong></li>
<li><strong>Magic Firewall</strong> → <strong>Cloudflare Network Firewall</strong></li>
<li><strong>Magic Network Monitoring</strong> → <strong>Network Flow</strong></li>
<li><strong>Magic Cloud Networking</strong> → <strong>Cloudflare One Multi-cloud Networking</strong></li>
</ul>
<p><strong>No action is required by you</strong> — all functionality, existing configurations, and billing will remain exactly the same.</p>
<p>For more information, visit the <a href="/cloudflare-one/">Cloudflare One documentation</a>.</p>


<h2 id="fine-grained-permissions-for-access-policies-and-service-tokens"><a href="/changelog/post/2026-02-13-access-policy-service-token-permissions/">Fine-grained permissions for Access policies and service tokens</a></h2>
<p><em>2026-02-13</em></p>
<p>Fine-grained permissions for <strong>Access policies</strong> and <strong>Access service tokens</strong> are available. These new resource-scoped roles expand the existing RBAC model, enabling administrators to grant permissions scoped to individual resources.</p>
<h4 id="2026-02-13-access-policy-service-token-permissions-new-roles">New roles</h4>
<ul>
<li><strong>Cloudflare Access policy admin</strong>: Can edit a specific <a href="/cloudflare-one/access-controls/policies/">Access policy</a> in an account.</li>
<li><strong>Cloudflare Access service token admin</strong>: Can edit a specific <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Access service token</a> in an account.</li>
</ul>
<p>These roles complement the existing resource-scoped roles for Access applications, identity providers, and infrastructure targets.</p>
<p>For more information:</p>
<ul>
<li><a href="/fundamentals/manage-members/roles/#resource-scoped-roles">Resource-scoped roles</a></li>
<li><a href="/fundamentals/manage-members/scope/">Role scopes</a></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17729.md")</aside>


<h2 id="anycast-ips-displayed-on-the-dashboard"><a href="/changelog/post/2026-02-12-anycast-ips-on-dashboard/">Anycast IPs displayed on the dashboard</a></h2>
<p><em>2026-02-12</em></p>
<p>Cloudflare WAN now displays your Anycast IP addresses directly in the dashboard when you configure IPsec or GRE tunnels.</p>
<p>Previously, customers received their Anycast IPs during onboarding or had to retrieve them with an API call. The dashboard now pre-loads these addresses, reducing setup friction and preventing configuration errors.</p>
<p>No action is required. All Cloudflare WAN customers can see their Anycast IPs in the tunnel configuration form automatically.</p>
<p>For more information, refer to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a>.</p>


<h2 id="post-quantum-encryption-support-for-cloudflare-one-appliance"><a href="/changelog/post/2026-02-11-appliance-post-quantum-encryption/">Post-quantum encryption support for Cloudflare One Appliance</a></h2>
<p><em>2026-02-11</em></p>
<p>Cloudflare One Appliance version 2026.2.0 adds <a href="/ssl/post-quantum-cryptography/">post-quantum encryption</a> support using hybrid ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).</p>
<p>The appliance now uses TLS 1.3 with hybrid ML-KEM for its connection to the Cloudflare edge. During the TLS handshake, the appliance and the edge share a symmetric secret over the TLS connection and inject it into the ESP layer of IPsec. This protects IPsec data plane traffic against harvest-now, decrypt-later attacks.</p>
<p>This upgrade deploys automatically to all appliances during their configured interrupt windows with no manual action required.</p>
<p>For more information, refer to <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a>.</p>


<h2 id="improved-accessibility-and-search-for-monitoring"><a href="/changelog/post/2026-02-02-improved-accessibility-search-for-monitoring/">Improved Accessibility and Search for Monitoring</a></h2>
<p><em>2026-02-02T11:05:33+00:00</em></p>
<p>We have updated the Monitoring page to provide a more streamlined and insightful experience for administrators, improving both data visualization and dashboard accessibility.</p>
<ul>
<li><strong>Enhanced Visual Layout</strong>: Optimized contrast and the introduction of stacked bar charts for clearer data visualization and trend analysis.
<img src="/assets/upstream/images/changelog/email-security/monitoring-bar-charts.png" alt="visual-example" /></li>
<li><strong>Improved Accessibility &amp; Usability</strong>:
<ul>
<li><strong>Widget Search</strong>: Added search functionality to multiple widgets, including Policies, Submitters, and Impersonation.</li>
<li><strong>Actionable UI</strong>: All available actions are now accessible via dedicated buttons.</li>
<li><strong>State Indicators</strong>: Improved UI states to clearly communicate loading, empty datasets, and error conditions.
<img src="/assets/upstream/images/changelog/email-security/monitoring-buttons.png" alt="buttons-example" /></li>
</ul>
</li>
<li><strong>Granular Data Breakdowns</strong>: New views for dispositions by month, malicious email details, link actions, and impersonations.
<img src="/assets/upstream/images/changelog/email-security/monitoring-monthly-dispositions.png" alt="monthly-example" /></li>
</ul>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="bgp-over-gre-and-ipsec-tunnels"><a href="/changelog/post/2026-01-30-bgp-over-tunnels/">BGP over GRE and IPsec tunnels</a></h2>
<p><em>2026-01-30</em></p>
<p>Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using IPsec and GRE tunnel on-ramps (beta).</p>
<p>Using BGP peering allows customers to:</p>
<ul>
<li>Automate the process of adding or removing networks and subnets.</li>
<li>Take advantage of failure detection and session recovery features.</li>
</ul>
<p>With this functionality, customers can:</p>
<ul>
<li>Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via IPsec and GRE tunnel on-ramps.</li>
<li>Secure the session by MD5 authentication to prevent misconfigurations.</li>
<li>Exchange routes dynamically between their devices and their Magic routing table.</li>
</ul>
<p>For configuration details, refer to:</p>
<ul>
<li><a href="/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes">Configure BGP routes for Magic WAN</a></li>
<li><a href="/magic-transit/how-to/configure-routes/#configure-bgp-routes">Configure BGP routes for Magic Transit</a></li>
</ul>


<h2 id="warp-client-for-macos-version-2026-1-89-1"><a href="/changelog/post/2026-01-27-warp-macos-beta/">WARP client for macOS (version 2026.1.89.1)</a></h2>
<p><em>2026-01-28</em></p>
<p>A new Beta release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Fixed an issue causing failure of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion">local network exclusion</a> feature when configured with a timeout of <code>0</code>.</li>
<li>Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.</li>
</ul>


<h2 id="warp-client-for-windows-version-2026-1-89-1"><a href="/changelog/post/2026-01-27-warp-windows-beta/">WARP client for Windows (version 2026.1.89.1)</a></h2>
<p><em>2026-01-28</em></p>
<p>A new Beta release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Improvements to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-multiuser/">multi-user mode</a>. Fixed an issue where when switching from a pre-login registration to a user registration, Mobile Device Management (MDM) configuration association could be lost.</li>
<li>Added a new feature to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#netbios-over-tcpip">manage NetBIOS over TCP/IP</a> functionality on the Windows client. NetBIOS over TCP/IP on the Windows client is now disabled by default and can be enabled in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile settings</a>.</li>
<li>Fixed an issue causing failure of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion">local network exclusion</a> feature when configured with a timeout of <code>0</code>.</li>
<li>Improvement for the Windows <a href="/cloudflare-one/reusable-components/posture-checks/warp-client-checks/client-certificate/">client certificate posture check</a> to ensure logged results are from checks that run once users log in.</li>
<li>Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.</li>
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


<h2 id="configure-cloudflare-source-ips-beta"><a href="/changelog/post/2026-01-27-configure-cloudflare-source-ips/">Configure Cloudflare source IPs (beta)</a></h2>
<p><em>2026-01-27</em></p>
<p>Cloudflare source IPs are the IP addresses used by Cloudflare services (such as Load Balancing, Gateway, and Browser Isolation) when sending traffic to your private networks.</p>
<p>For customers using legacy mode routing, traffic to private networks is sourced from public Cloudflare IPs, which may cause IP conflicts. For customers using Unified Routing mode (beta), traffic to private networks is sourced from dedicated, non-Internet-routable private IPv4 range to ensure:</p>
<ul>
<li>Symmetric routing over private network connections</li>
<li>Proper firewall state preservation</li>
<li>Private traffic stays on secure paths</li>
</ul>
<p>Key details:</p>
<ul>
<li><strong>IPv4</strong>: Sourced from <code>100.64.0.0/12</code> by default, configurable to any <code>/12</code> CIDR</li>
<li><strong>IPv6</strong>: Sourced from <code>2606:4700:cf1:5000::/64</code> (not configurable)</li>
<li><strong>Affected connectors</strong>: GRE, IPsec, CNI, WARP Connector, and WARP Client (Cloudflare Tunnel is not affected)</li>
</ul>
<p>Configuring Cloudflare source IPs requires Unified Routing (beta) and the <code>Cloudflare One Networks Write</code> permission.</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/">Configure Cloudflare source IPs</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/cloudflare-one/6/">Previous</a><span>Page 7 of 13</span><a class="pagination-next" rel="next" href="/changelog/product-group/cloudflare-one/8/">Next</a></nav>
