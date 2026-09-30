<h1 id="changelog">Changelog</h1>

<h2 id="dlp-account-level-settings"><a href="/changelog/post/2025-04-14-account-level-dlp-settings/">DLP account-level settings</a></h2>
<p><em>2026-04-14T12:00:00+00:00</em></p>
<p><strong>Account-level DLP settings are now available</strong> in Cloudflare One. You can now configure advanced DLP settings at the account level, including OCR, AI context analysis, and payload masking. This provides consistent enforcement across all DLP profiles and simplifies configuration management.</p>
<p>Key changes:</p>
<ul>
<li><strong>Consistent enforcement</strong>: Settings configured at the account level apply to all DLP profiles</li>
<li><strong>Simplified migration</strong>: Settings enabled on any profile are automatically migrated to account level</li>
<li><strong>Deprecation notice</strong>: Profile-level advanced settings will be deprecated in a future release</li>
</ul>
<p><strong>Migration details:</strong></p>
<p>During the migration period, if a setting is enabled on any profile, it will automatically be enabled at the account level. This means profiles that previously had a setting disabled may now have it enabled if another profile in the account had it enabled.</p>
<p>Settings are evaluated using OR logic - a setting is enabled if it is turned on at either the account level or the profile level. However, profile-level settings cannot be enabled when the account-level setting is off.</p>
<p>For more details, refer to the <a href="/cloudflare-one/data-loss-prevention/dlp-settings/">DLP settings documentation</a>.</p>


<h2 id="introducing-cloudflare-mesh"><a href="/changelog/post/2026-04-14-cloudflare-mesh/">Introducing Cloudflare Mesh</a></h2>
<p><em>2026-04-14</em></p>
<p><a href="/mesh/">Cloudflare Mesh</a> is now available (<a href="https://blog.cloudflare.com/mesh/">blog post</a>). Mesh connects your services and devices with post-quantum encrypted networking, allowing you to route traffic privately between servers, laptops, and phones over TCP, UDP, and ICMP.</p>
<p><img src="/assets/upstream/images/cloudflare-one/connections/mesh-network-map.gif" alt="Cloudflare Mesh network map showing nodes and devices connected through Cloudflare" /></p>
<h4 id="2026-04-14-cloudflare-mesh-what-cloudflare-mesh-does">What Cloudflare Mesh does</h4>
<ul>
<li>Assigns a private <a href="/mesh/concepts/#mesh-ips">Mesh IP</a> to every enrolled device and node.</li>
<li>Enables any participant to reach any other participant by IP — including client-to-client, without deploying any infrastructure.</li>
<li>Supports <a href="/mesh/features/routes/">CIDR routes</a> for subnet routing through Mesh nodes.</li>
<li>Supports <a href="/mesh/features/high-availability/">high availability</a> with active-passive replicas for nodes with routes.</li>
<li>All traffic flows through Cloudflare, so <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a>, <a href="/cloudflare-one/reusable-components/posture-checks/">device posture checks</a>, and access rules apply to every connection.</li>
</ul>
<h4 id="2026-04-14-cloudflare-mesh-what-changed">What changed</h4>
<ul>
<li><strong>WARP Connector</strong> is now <strong>Cloudflare Mesh</strong>. Existing WARP Connectors are now called mesh nodes. All existing deployments continue to work — no migration required.</li>
<li><strong>Peer-to-peer connectivity</strong> is now called <strong>Mesh connectivity</strong> and is part of the Cloudflare Mesh documentation.</li>
<li><strong>Mesh node limit</strong> increased from 10 to <strong>50 per account</strong>.</li>
<li>New <a href="https://dash.cloudflare.com/?to=/:account/mesh">dashboard experience</a> at <strong>Networking</strong> &gt; <strong>Mesh</strong> with an interactive network map, node management, route configuration, diagnostics, and a setup wizard.</li>
</ul>
<h4 id="2026-04-14-cloudflare-mesh-get-started">Get started</h4>
<p>Refer to the <a href="/mesh/">Cloudflare Mesh documentation</a> to set up your first Mesh network.</p>


<h2 id="detect-cloudflare-api-tokens-with-dlp"><a href="/changelog/post/2026-04-14-cloudflare-api-token-detections/">Detect Cloudflare API tokens with DLP</a></h2>
<p><em>2026-04-14</em></p>
<p>The <strong>Credentials and Secrets</strong> DLP profile now includes three new predefined entries for detecting Cloudflare API credentials:</p>
<table>
<thead>
<tr>
<th>Entry name</th>
<th>Token prefix</th>
<th>Detects</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare User API Key</td>
<td><code>cfk_</code></td>
<td>User-scoped API keys</td>
</tr>
<tr>
<td>Cloudflare User API Token</td>
<td><code>cfut_</code></td>
<td>User-scoped API tokens</td>
</tr>
<tr>
<td>Cloudflare Account Owned API Token</td>
<td><code>cfat_</code></td>
<td>Account-scoped API tokens</td>
</tr>
</tbody>
</table>
<p>These detections target the new <a href="/fundamentals/api/get-started/token-formats/">Cloudflare API credential format</a>, which uses a structured prefix and a CRC32 checksum suffix. The identifiable prefix makes it possible to detect leaked credentials with high confidence and low false positive rates — no surrounding context such as <code>Authorization: Bearer</code> headers is required.</p>
<p>Credentials generated before this format change will not be matched by these entries.</p>
<h4 id="2026-04-14-cloudflare-api-token-detections-how-to-enable-cloudflare-api-token-detections">How to enable Cloudflare API token detections</h4>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>DLP</strong> &gt; <strong>DLP Profiles</strong>.</li>
<li>Select the <strong>Credentials and Secrets</strong> profile.</li>
<li>Turn on one or more of the new Cloudflare API token entries.</li>
<li>Use the profile in a Gateway HTTP policy to log or block traffic containing these credentials.</li>
</ol>
<p>Example policy:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>DLP Profile</td>
<td>in</td>
<td><em>Credentials and Secrets</em></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>You can also enable individual entries to scope detection to specific credential types — for example, enabling <strong>Account Owned API Token</strong> detection without enabling <strong>User API Key</strong> detection.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">predefined DLP profiles</a>.</p>


<h2 id="configure-how-sensitive-data-appears-in-dlp-payload-logs"><a href="/changelog/post/2026-04-14-configurable-payload-log-masking/">Configure how sensitive data appears in DLP payload logs</a></h2>
<p><em>2026-04-14</em></p>
<p>You can now configure how sensitive data matches are displayed in your DLP payload match logs — giving your incident response team the context they need to validate alerts without compromising your security posture.</p>
<p>To get started, go to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, select <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>DLP settings</strong> and find the <strong>Payload log masking</strong> card.</p>
<p>Previously, all DLP payload logs used a single masking mode that obscured matched data entirely and hid the original character count, making it difficult to distinguish true positives from false positives. This update introduces three options:</p>
<ul>
<li><strong>Full Mask (default):</strong> Masks the match while preserving character count and visual formatting (for example, <code>***-**-****</code> for a Social Security Number). This is an improvement over the previous default, which did not preserve character count.</li>
<li><strong>Partial Mask:</strong> Reveals 25% of the matched content while masking the remainder (for example, <code>***-**-6789</code>).</li>
<li><strong>Clear Text:</strong> Stores the full, unmasked violation for deep investigation (for example, <code>123-45-6789</code>).</li>
</ul>
<p><strong>Important:</strong> The masking level you select is applied at detection time, before the payload is encrypted. This means the chosen format is what your team will see after decrypting the log with your private key — the existing encryption workflow is unchanged.</p>
<p><strong>Applies to all enabled detections:</strong> When a masking level other than Full Mask is selected, it applies to all sensitive data matches found within a payload window — not just the match that triggered the policy. Any data matched by your enabled DLP detection entries will be masked at the selected level.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-the-payload-of-matched-rules">DLP logging options</a>.</p>


<h2 id="canvas-remoting-optimizes-performance-for-productivity-applications"><a href="/changelog/post/2026-04-10-canvas-remoting-performance/">Canvas Remoting optimizes performance for productivity applications</a></h2>
<p><em>2026-04-10</em></p>
<p>Remote Browser Isolation now supports <strong>Canvas Remoting</strong>, improving performance for HTML5 Canvas applications by sending vector draw commands instead of rasterized bitmaps.</p>
<h4 id="2026-04-10-canvas-remoting-performance-key-improvements">Key improvements</h4>
<ul>
<li><strong>10x bandwidth reduction:</strong> Microsoft Word and other Office apps use 90% less bandwidth</li>
<li><strong>Smooth performance:</strong> Google Sheets maintains consistent 30fps rendering</li>
<li><strong>Responsive terminals:</strong> Web-based development environments and AI notebooks work in real-time</li>
<li><strong>Zero configuration:</strong> Enabled by default for all Browser Isolation customers</li>
</ul>
<h4 id="2026-04-10-canvas-remoting-performance-how-it-works">How it works</h4>
<p>Instead of sending rasterized bitmaps for every Canvas update, Browser Isolation now:</p>
<ol>
<li>Captures Canvas draw commands at the source</li>
<li>Converts them to lightweight vector instructions</li>
<li>Renders Canvas content on the client</li>
</ol>
<p>This reduces bandwidth from hundreds of kilobytes per second to tens of kilobytes per second.</p>
<h4 id="2026-04-10-canvas-remoting-performance-managing-canvas-remoting">Managing Canvas Remoting</h4>
<p>To temporarily disable for troubleshooting:</p>
<ul>
<li>Right-click the isolated webpage background</li>
<li>Select <strong>Disable Canvas Remoting</strong></li>
<li>Re-enable the same way by selecting <strong>Enable Canvas Remoting</strong></li>
</ul>
<h4 id="2026-04-10-canvas-remoting-performance-limitations">Limitations</h4>
<p>Currently supports 2D Canvas contexts only. WebGL and 3D graphics applications continue using bitmap rendering. For more information, refer to <a href="/cloudflare-one/remote-browser-isolation/canvas-remoting/">Canvas Remoting</a>.</p>


<h2 id="send-casb-posture-finding-instances-with-webhooks"><a href="/changelog/post/2026-04-09-casb-webhooks/">Send CASB posture finding instances with webhooks</a></h2>
<p><em>2026-04-09</em></p>
<p>You can now use <strong>CASB webhooks</strong> in Cloudflare One to send posture finding instances to external systems such as chat platforms, ticketing systems, SIEMs, SOAR tools, and custom automation services.</p>
<p>This gives security teams a simple way to route CASB posture findings into the tools and workflows they already use for triage and response.</p>
<p>To get started, go to <strong>Integrations</strong> &gt; <strong>Webhooks</strong> in the Cloudflare One dashboard to create a webhook destination. After you configure a webhook, open a posture finding instance and select <strong>Send webhook</strong> to send it.</p>
<h4 id="2026-04-09-casb-webhooks-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Flexible authentication</strong> — Configure destinations using <strong>None</strong>, <strong>Basic Auth</strong>, <strong>Bearer Auth</strong>, <strong>Static Headers</strong>, or <strong>HMAC-Signing</strong>.</li>
<li><strong>Built-in testing</strong> — Use <strong>Test delivery</strong> to send a test request before sending a live finding instance.</li>
<li><strong>Posture finding workflows</strong> — Send posture finding instances directly from the finding details workflow in <strong>Cloud &amp; SaaS findings</strong>.</li>
<li><strong>HTTPS destinations</strong> — Configure webhook destinations with public <code>https://</code> URLs.</li>
</ul>
<h4 id="2026-04-09-casb-webhooks-learn-more">Learn more</h4>
<ul>
<li>Configure <a href="/cloudflare-one/integrations/cloud-and-saas/webhooks/">CASB webhooks</a> in Cloudflare.</li>
<li>Learn how to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/">manage findings</a> in Cloudflare.</li>
</ul>
<p>CASB webhooks are now available in Cloudflare One.</p>


<h2 id="user-risk-scoring-for-high-risk-browsing-activity"><a href="/changelog/post/2026-04-08-high-risk-browsing/">User risk scoring for high risk browsing activity</a></h2>
<p><em>2026-04-08</em></p>
<p>Cloudflare One's <strong>User Risk Scoring</strong> now incorporates direct signals from <strong>Gateway DNS traffic patterns</strong>. This update allows security teams to automatically elevate a user's risk score when they visit high-risk or malicious domains, providing a more holistic view of internal threats.</p>
<h4 id="2026-04-08-high-risk-browsing-why-this-matters">Why this matters</h4>
<p>Browsing activity is a primary indicator of potential compromise. By tying Gateway DNS logs to specific users, administrators can now flag individuals interacting with:</p>
<ul>
<li><strong>Security threats</strong>: Domains associated with malware, phishing, or command-and-control (C2) centers.</li>
<li><strong>High-risk content</strong>: Categories such as questionable content or violence that may violate corporate compliance.</li>
</ul>
<p>Even if a Gateway policy is set to <strong>Block</strong> the traffic, the interaction is still captured as a &quot;hit&quot; to ensure the user's risk profile reflects the attempted activity.</p>
<h4 id="2026-04-08-high-risk-browsing-new-risk-behaviors">New risk behaviors</h4>
<p>Two new behaviors are now available in the dashboard:</p>
<ul>
<li><strong>Suspicious Security Domain Visited</strong>: Triggers when a user visits a domain in the security threats or security risk categories.</li>
<li><strong>High risk domain visited</strong>: Triggers when a user visits domains categorized as questionable content, violence, or CIPA.</li>
</ul>
<p>To learn more and get started, refer to the <a href="/cloudflare-one/team-and-resources/users/risk-score/">User Risk Scoring documentation</a>.</p>


<h2 id="cloudflare-one-client-for-windows-version-2026-3-851-0"><a href="/changelog/post/2026-04-07-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.3.851.0)</a></h2>
<p><em>2026-04-08</em></p>
<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
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


<h2 id="user-submission-triage-status-tracking"><a href="/changelog/post/2026-04-07-triage-status-tracking/">User Submission Triage Status Tracking</a></h2>
<p><em>2026-04-07 09:00:00 UTC</em></p>
<p>Cloudflare Email security now supports <strong>Triage Status Tracking for User Submissions</strong>. This enhancement gives SOC teams a streamlined way to track, manage, and prioritize user-submitted emails directly within the Cloudflare One dashboard.</p>
<ul>
<li>The User Submissions table now includes a <strong>Status</strong> column with three states: <strong>Unreviewed</strong> (new submissions awaiting triage), <strong>Reviewed</strong> (submissions assessed by the SOC team), and <strong>Escalated</strong> (submissions escalated to team submissions for further investigation). Analysts can quickly update statuses and filter the table to focus on what needs attention.</li>
<li>SOC teams can now organize their triage workflows, avoid duplicate reviews, and make sure critical threats get escalated for deeper investigation—bringing order to the chaos of high-volume submission management.</li>
</ul>
<p>Triage Status Tracking is <strong>automatically available</strong> for all Email security customers using the user submissions feature. No additional configuration is required; customers just need to make sure user submissions are being sent to their user submission aliases.</p>
<p>This applies to all Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="link-aggregation-lacp-support-for-cloudflare-one-appliance"><a href="/changelog/post/2026-04-07-link-aggregation-lacp-appliance/">Link aggregation (LACP) support for Cloudflare One Appliance</a></h2>
<p><em>2026-04-07</em></p>
<p>Cloudflare One Appliance now supports Link Aggregation Control Protocol (LACP), allowing you to bundle up to six physical LAN ports into a single logical interface. Link aggregation increases available bandwidth and eliminates single points of failure on the LAN side of the appliance.</p>
<p>This feature is available in beta on physical appliance hardware with the latest OS. No entitlement is required.</p>
<p>To configure a Link Aggregation Group, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/link-aggregation/">Configure link aggregation groups</a>.</p>


<h2 id="dane-support-for-mx-deployments"><a href="/changelog/post/2026-04-06-dane-support-mx-deployments/">DANE Support for MX Deployments</a></h2>
<p><em>2026-04-06T09:00:00+00:00</em></p>
<p>Cloudflare Email Security now supports DANE (DNS-based Authentication of Named Entities) for MX deployments. This enhancement strengthens email transport security by enabling DNSSEC-backed certificate verification for our regional MX records.</p>
<ul>
<li>Regional MX hostnames now publish DANE TLSA records backed by DNSSEC, enabling DANE-capable SMTP senders to cryptographically validate certificate identities before establishing TLS connections—moving beyond opportunistic encryption to verified encrypted delivery.</li>
<li>DANE support is automatically available for all customers using regional MX deployments. No additional configuration is required; DANE-capable mail infrastructure will automatically validate MX certificates using the published records.</li>
</ul>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="organizations-is-now-in-public-beta-for-enterprises"><a href="/changelog/post/2026-04-06-organizations-public-beta/">Organizations is now in public beta for enterprises</a></h2>
<p><em>2026-04-06</em></p>
<p>We're announcing the public beta of <strong>Organizations</strong> for enterprise customers, a new top-level Cloudflare container that lets Cloudflare customers manage multiple accounts, members, analytics, and shared policies from one centralized location.</p>
<p><strong>What's New</strong></p>
<p><strong>Organizations [BETA]</strong>: <a href="/fundamentals/organizations/">Organizations</a> are a new top-level container for centrally managing multiple accounts. Each Organization supports up to 500 accounts and 5000 zones, giving larger teams a single place to administer resources at scale.</p>
<p><strong>Self-serve onboarding</strong>: Enterprise customers can <a href="/fundamentals/organizations/setup/">create an Organization</a> in the dashboard and assign accounts where they are already Super Administrators.</p>
<p><strong>Centralized Account Management</strong>: At launch, every Organization member has the Organization Super Admin role. Organization Super Admins can invite other users and manage any child account under the Organization implicitly.
<strong>Shared policies</strong>: Share <a href="/waf/custom-rules/">WAF</a> or <a href="/cloudflare-one/traffic-policies/tiered-policies/organizations/">Gateway</a> policies across multiple accounts within your Organization to simplify centralized policy management.
<strong>Implicit access</strong>: Members of an Organization automatically receive Super Administrator permissions across child accounts, removing the need for explicit membership on each account. Additional Org-level roles will be available over the course of the year.</p>
<p><strong>Unified analytics</strong>: View, filter, and download aggregate HTTP analytics across all Organization child accounts from a single dashboard for centralized visibility into traffic patterns and security events.</p>
<p><strong>Terraform provider support</strong>: Manage Organizations with infrastructure as code from day one. Provision organizations, assign accounts, and configure settings programmatically with the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/organization">Cloudflare Terraform provider</a>.</p>
<p><strong>Shared policies</strong>: Share <a href="/waf/custom-rules/">WAF</a> or <a href="/cloudflare-one/traffic-policies/">Gateway</a> policies across multiple accounts within your Organization to simplify centralized policy management.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17731.md")</aside>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/organizations/">Get started with Organizations</a></li>
<li><a href="/fundamentals/organizations/setup/">Set up your Organization</a></li>
<li><a href="/fundamentals/organizations/limitations/">Review limitations</a></li>
</ul>


<h2 id="cloudflare-one-client-for-linux-version-2026-3-846-0"><a href="/changelog/post/2026-04-02-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.3.846.0)</a></h2>
<p><em>2026-04-03</em></p>
<p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
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


<h2 id="cloudflare-one-client-for-macos-version-2026-3-846-0"><a href="/changelog/post/2026-04-02-warp-macos-ga/">Cloudflare One Client for macOS (version 2026.3.846.0)</a></h2>
<p><em>2026-04-03</em></p>
<p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
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


<h2 id="session-management-for-mcp-server-portals"><a href="/changelog/post/2026-04-02-mcp-portal-session-management/">Session management for MCP server portals</a></h2>
<p><em>2026-04-02</em></p>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support in-session management of upstream MCP server connections. Users can return to the server selection page at any time to enable or disable servers, reauthenticate, or change which data a server has access to — all without leaving their MCP client.</p>
<p>To return to the server selection page, ask your AI agent with a prompt like &quot;take me back to the server selection page.&quot; The portal responds with an authorization URL via <a href="https://modelcontextprotocol.io/specification/2025-03-26/server/elicitation">MCP elicitation</a> that you open in your browser:</p>
<pre><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/authorize?elicitationId=&lt;ELICITATION_ID&gt;&#10;</code></pre>
<p>From the server selection page you can:</p>
<ul>
<li><strong>Enable or disable servers</strong> — Toggle individual upstream MCP servers on or off. Disabling a server removes its tools from the active session, which reduces context window usage.</li>
<li><strong>Log out and reauthenticate</strong> — Log out of a server and log back in to change which data the server has access to, or to reauthenticate with different permissions.</li>
</ul>
<p>Users can also enable or disable a server inline by asking their AI agent directly, for example &quot;enable the wiki server&quot; or &quot;disable my Jira server.&quot;</p>
<p>The portal also automatically prompts connected users to authorize new servers when an admin adds them to the portal. This requires the use of <a href="/cloudflare-one/access-controls/applications/http-apps/managed-oauth/#enable-managed-oauth-on-an-mcp-server-portal">managed OAuth</a>.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#manage-portal-sessions">Manage portal sessions</a>.</p>


<h2 id="logs-ui-refresh"><a href="/changelog/post/2026-04-01-logs-ui-refresh/">Logs UI refresh</a></h2>
<p><em>2026-04-01</em></p>
<p>Access authentication logs and Gateway activity logs (DNS, Network, and HTTP) now feature a refreshed user interface that gives you more flexibility when viewing and analyzing your logs.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/cf1-new-logs-ui.png" alt="Screenshot of the new logs UI showing DNS query logs with customizable columns and filtering options" /></p>
<p>The updated UI includes:</p>
<ul>
<li><strong>Filter by field</strong> - Select any field value to add it as a filter and narrow down your results.</li>
<li><strong>Customizable fields</strong> - Choose which fields to display in the log table. Querying for fewer fields improves log loading performance.</li>
<li><strong>View details</strong> - Select a timestamp to view the full details of a log entry.</li>
<li><strong>Switch to classic view</strong> - Return to the previous log viewer interface if needed.</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/">Access authentication logs</a> and <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway activity logs</a>.</p>


<h2 id="code-mode-for-mcp-server-portals"><a href="/changelog/post/2026-03-26-mcp-portal-code-mode/">Code Mode for MCP server portals</a></h2>
<p><em>2026-03-26</em></p>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support <a href="/agents/model-context-protocol/codemode/">Code Mode MCP server patterns</a>, a technique that reduces context window usage by replacing individual tool definitions with a single code execution tool. Code Mode is turned on by default on all portals.</p>
<p>To turn it off, edit the portal in <strong>Access controls</strong> &gt; <strong>AI controls</strong> and turn off <strong>Code Mode</strong> under <strong>Basic information</strong>.</p>
<p>When Code Mode is active, the portal exposes a single <code>code</code> tool instead of listing every tool from every upstream MCP server. The connected AI agent writes JavaScript that calls typed <code>codemode.*</code> methods for each upstream tool. The generated code runs in an isolated <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a> environment, keeping authentication credentials and environment variables out of the model context.</p>
<p>To use Code Mode, append <code>?codemode=search_and_execute</code> to your portal URL when connecting from an MCP client:</p>
<pre><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?codemode=search_and_execute&#10;</code></pre>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode">Code Mode</a>.</p>


<h2 id="context-optimization-for-mcp-server-portals"><a href="/changelog/post/2026-03-26-mcp-portal-context-optimization/">Context optimization for MCP server portals</a></h2>
<p><em>2026-03-26</em></p>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support two context optimization options that reduce how many tokens tool definitions consume in the model's context window. Both options are activated by appending the <code>optimize_context</code> query parameter to the portal URL.</p>
<h4 id="2026-03-26-mcp-portal-context-optimization-minimize-tools"><code>minimize_tools</code></h4>
<p>Strips tool descriptions and input schemas from all upstream tools, leaving only their names. The portal exposes a special <code>query</code> tool that agents use to retrieve full definitions on demand. This provides up to 5x savings in token usage.</p>
<pre><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?optimize_context=minimize_tools&#10;</code></pre>
<h4 id="2026-03-26-mcp-portal-context-optimization-search-and-execute"><code>search_and_execute</code></h4>
<p>Hides all upstream tools and exposes only two tools: <code>query</code> and <code>execute</code>. The <code>query</code> tool searches and retrieves tool definitions. The <code>execute</code> tool runs the upstream tools in an isolated <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a> environment. This reduces the initial token cost to a small constant, regardless of how many tools are available through the portal.</p>
<pre><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?optimize_context=search_and_execute&#10;</code></pre>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#optimize-context">Optimize context</a>.</p>


<h2 id="streaming-zip-file-scanning-removes-per-file-size-limits"><a href="/changelog/post/2026-03-26-streaming-zip-handler/">Streaming ZIP file scanning removes per-file size limits</a></h2>
<p><em>2026-03-26</em></p>
<p>DLP now processes ZIP files using a streaming handler that scans archive contents element-by-element as data arrives. This removes previous file size limitations and improves memory efficiency when scanning large archives.</p>
<p>Microsoft Office documents (DOCX, XLSX, PPTX) also benefit from this improvement, as they use ZIP as a container format.</p>
<p>This improvement is automatic — no configuration changes are required.</p>


<h2 id="detect-and-sanitize-har-files"><a href="/changelog/post/2026-03-25-har-file-detection-and-sanitization/">Detect and sanitize HAR files</a></h2>
<p><em>2026-03-25</em></p>
<p>HTTP Archive (HAR) files are used by engineering and support teams to capture and share web traffic logs for troubleshooting. However, these files routinely contain highly sensitive data — including session cookies, authorization headers, and other credentials — that can pose a significant risk if uploaded to third-party services without being reviewed or cleaned first.</p>
<p>Gateway now includes a predefined DLP profile called <strong>Unsanitized HAR</strong> that detects HAR files in HTTP traffic. You can use this profile in a Gateway HTTP policy to either block HAR file uploads entirely or redirect users to a sanitization tool before allowing the upload to proceed.</p>
<h4 id="2026-03-25-har-file-detection-and-sanitization-how-to-configure-a-har-file-policy">How to configure a HAR file policy</h4>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to  <strong>Zero Trust</strong> &gt;  <strong>Traffic policies</strong> &gt; <strong>Firewall Policies</strong> &gt; <strong>HTTP</strong> and create a new HTTP policy using the <strong>DLP Profile</strong> selector:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>DLP Profile</td>
<td>in</td>
<td><em>Unsanitized HAR</em></td>
<td></td>
</tr>
</tbody>
</table>
<p>Then choose one of the following actions:</p>
<ul>
<li><strong>Block</strong>: Prevents the upload of any HAR file that has not been sanitized by Cloudflare's sanitizer. Use this for strict environments where HAR file sharing must be disallowed entirely.</li>
<li><strong>Block</strong> with <strong>Gateway Redirect</strong>: Intercepts the upload and redirects the user to <code>https://har-sanitizer.pages.dev/</code>, where they can sanitize the file. Once sanitized, the user can re-upload the clean file and proceed with their workflow.</li>
</ul>
<h4 id="2026-03-25-har-file-detection-and-sanitization-sanitized-har-recognition">Sanitized HAR recognition</h4>
<p>HAR files processed by the Cloudflare HAR sanitizer receive a tamper-evident sanitized marker. DLP recognizes this marker and will not re-trigger the policy on a file that has already been sanitized and has not been modified since. If a previously sanitized file is edited, it will be treated as unsanitized and flagged again.</p>
<h4 id="2026-03-25-har-file-detection-and-sanitization-visibility-in-gateway-logs">Visibility in Gateway logs</h4>
<p>Gateway logs will reflect whether a detected HAR file was classified as <strong>Unsanitized</strong> or <strong>Sanitized</strong>, giving your security team full visibility into HAR file activity across your organization.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">predefined DLP profiles</a>.</p>


<h2 id="oidc-claims-filtering-now-available-in-gateway-firewall-resolver-and-egress-policies"><a href="/changelog/post/2026-03-24-oidc-claims-filtering-gateway-policies/">OIDC Claims filtering now available in Gateway Firewall, Resolver, and Egress policies</a></h2>
<p><em>2026-03-24</em></p>
<p>Cloudflare Gateway now supports <a href="/cloudflare-one/traffic-policies/identity-selectors/#oidc-claims">OIDC Claims</a> as a selector in Firewall, Resolver, and Egress policies. Administrators can use custom OIDC claims from their identity provider to build fine-grained, identity-based traffic policies across all Gateway policy types.</p>
<p>With this update, you can:</p>
<ul>
<li>Filter traffic in <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS</a>, <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a>, and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> firewall policies based on OIDC claim values.</li>
<li>Apply custom <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a> to route DNS queries to specific resolvers depending on a user's OIDC claims.</li>
<li>Control <a href="/cloudflare-one/traffic-policies/egress-policies/">egress policies</a> to assign dedicated egress IPs based on OIDC claim attributes.</li>
</ul>
<p>For example, you can create a policy that routes traffic differently for users with <code>department=engineering</code> in their OIDC claims, or restrict access to certain destinations based on a user's role claim.</p>
<p>To get started, configure <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims">custom OIDC claims</a> on your identity provider and use the <strong>OIDC Claims</strong> selector in the Gateway policy builder.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/identity-selectors/">Identity-based policies</a>.</p>


<h2 id="managed-oauth-for-cloudflare-access"><a href="/changelog/post/2026-03-20-managed-oauth/">Managed OAuth for Cloudflare Access</a></h2>
<p><em>2026-03-20</em></p>
<p>Cloudflare Access supports managed OAuth, which allows non-browser clients — such as CLIs, AI agents, SDKs, and scripts — to authenticate with Access-protected applications using a standard OAuth 2.0 authorization code flow.</p>
<p>Previously, non-browser clients that attempted to access a protected application received a <code>302</code> redirect to a login page they could not complete. The established workaround was <code>cloudflared access curl</code>, which required installing additional tooling.</p>
<p>With managed OAuth, clients instead receive a <code>401</code> response with a <code>WWW-Authenticate</code> header that points to Access's OAuth discovery endpoints (<a href="https://datatracker.ietf.org/doc/html/rfc8414">RFC 8414</a> and <a href="https://datatracker.ietf.org/doc/html/rfc9728">RFC 9728</a>). The client opens the end user's browser to the Access login page. The end user authenticates with their identity provider, and the client receives an OAuth access token for subsequent requests.</p>
<p>Access enforces the same policies as a browser login; the OAuth layer is a new transport mechanism, not a separate authentication path.</p>
<p>Managed OAuth can be enabled on any self-hosted Access application or <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portal</a>. It is opt-in for existing applications to avoid interfering with those that run their own OAuth servers and rely on their own <code>WWW-Authenticate</code> headers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17618.md")</aside>
<p>To enable managed OAuth, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>, edit the application, and turn on <strong>Managed OAuth</strong> under <strong>Advanced settings</strong>.</p>
<p>You can also enable it via the API by setting <code>oauth_configuration.enabled</code> to <code>true</code> on the <a href="/api/resources/zero_trust/subresources/access/subresources/applications/methods/update/">Access applications endpoint</a>.</p>
<p><img src="/assets/upstream/images/changelog/access/managed-oauth.png" alt="Managed OAuth settings in the Cloudflare dashboard" /></p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/managed-oauth/">Enable managed OAuth</a>.</p>


<h2 id="route-mcp-server-portal-traffic-through-cloudflare-gateway"><a href="/changelog/post/2026-03-20-mcp-portal-gateway-routing/">Route MCP server portal traffic through Cloudflare Gateway</a></h2>
<p><em>2026-03-20</em></p>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> can now route traffic through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> for richer HTTP request logging and data loss prevention (DLP) scanning.</p>
<p>When Gateway routing is turned on, portal traffic appears in your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway HTTP logs</a>. You can create <a href="/cloudflare-one/traffic-policies/">Gateway HTTP policies</a> with <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a> to detect and block sensitive data sent to upstream MCP servers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17619.md")</aside>
<p>To enable Gateway routing, go to <strong>Access controls</strong> &gt; <strong>AI controls</strong>, edit the portal, and turn on <strong>Route traffic through Cloudflare Gateway</strong> under <strong>Basic information</strong>.</p>
<p><img src="/assets/upstream/images/changelog/access/portal-route-through-gateway.png" alt="Route MCP server portal traffic through Cloudflare Gateway" /></p>
<p>For more details, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#route-portal-traffic-through-gateway">Route traffic through Gateway</a>.</p>


<h2 id="stream-logs-from-multiple-replicas-of-cloudflare-tunnel-simultaneously"><a href="/changelog/post/2026-03-20-tunnel-replica-overview-and-multi-log-streaming/">Stream logs from multiple replicas of Cloudflare Tunnel simultaneously</a></h2>
<p><em>2026-03-20</em></p>
<p>In the Cloudflare One dashboard, the overview page for a specific Cloudflare Tunnel now shows all <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">replicas</a> of that tunnel and supports streaming logs from multiple replicas at once.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-multiconn.gif" alt="View replicas and stream logs from multiple connectors" /></p>
<p>Previously, you could only stream logs from one replica at a time. With this update:</p>
<ul>
<li><strong>Replicas on the tunnel overview</strong> — All active replicas for the selected tunnel now appear on that tunnel's overview page under <strong>Connectors</strong>. Select any replica to stream its logs.</li>
<li><strong>Multi-connector log streaming</strong> — Stream logs from multiple replicas simultaneously, making it easier to correlate events across your infrastructure during debugging or incident response. To try it out, log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> and go to <strong>Networks</strong> &gt; <strong>Connectors</strong> &gt; <strong>Cloudflare Tunnels</strong>. Select <strong>View logs</strong> next to the tunnel you want to monitor.</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel log streams</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/">Deploy replicas</a>.</p>


<h2 id="unlimited-result-paging-in-investigations"><a href="/changelog/post/2026-03-15-infinite-paging-investigations/">Unlimited result paging in Investigations</a></h2>
<p><em>2026-03-15T16:00:00+00:00</em></p>
<p>Investigations now support unlimited result paging in both the dashboard and the API, removing the previous 1,000-record cap. Security teams can page through complete result sets when searching across large mail volumes, giving SOC analysts and automated workflows deeper visibility for forensics and threat hunting.</p>
<p>In the dashboard, infinite paging is now supported in the Investigations view. The 1,000-record ceiling has been removed, so you can navigate through the full result set directly in the UI. The <a href="/api/resources/email_security/subresources/investigate/methods/list">Investigations API</a> now returns up to 10,000 records per page (up from 1,000), with no cap on total result volume across pages.</p>
<p>For high-volume use cases, we recommend:</p>
<ul>
<li><strong><a href="/cloudflare-one/insights/logs/logpush/email-security-logs/">Logpush</a> to a SIEM</strong> for full-fidelity datasets and long-term retention.</li>
<li><strong>SOAR playbooks</strong> against the async bulk action API for large-scale remediation. Bulk actions initiated from the dashboard remain capped at 1,000 messages per action.</li>
<li><strong>The Investigations API</strong> for report exports larger than 1,000 results, which is the dashboard download cap.</li>
</ul>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/cloudflare-one/5/">Previous</a><span>Page 6 of 13</span><a class="pagination-next" rel="next" href="/changelog/product-group/cloudflare-one/7/">Next</a></nav>
