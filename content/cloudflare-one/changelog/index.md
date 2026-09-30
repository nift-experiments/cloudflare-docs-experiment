---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/changelog/
  description: Review recent changes to Cloudflare One.
  full_title: Changelog · Cloudflare One docs
  head_html: <title>Changelog · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Review recent changes to Cloudflare One."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/changelog/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/changelog/index.md"><link rel="alternate" type="application/rss+xml" href="https://developers.cloudflare.com/cloudflare-one/changelog/index.xml"><meta property="og:title" content="Changelog · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review recent changes to Cloudflare One."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/changelog/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Changelog"><meta name="algolia_content_type" content="Changelog"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/cloudflare-one/changelog/#page","headline":"Changelog \u00b7 Cloudflare One docs","description":"Review recent changes to Cloudflare One.","url":"https://developers.cloudflare.com/cloudflare-one/changelog/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/changelog/
  schema: 1
---
<h2 id="2026-09-15">2026-09-15</h2>

<strong>Access for Infrastructure now supports tagged targets and tag-based target criteria</strong>

<p><a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure</a> now integrates with <a href="/resource-tagging/">Resource Tagging</a>. You can attach key-value tags to <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target">infrastructure targets</a> and use them in access policies.</p>
<p>You can manage tags on targets inline when you create or edit a target or through the central <a href="/resource-tagging/how-to/manage-tags/">Resource Tagging API</a>. Cloudflare keeps tags in sync across both methods.</p>
<p>Infrastructure applications also support a target criteria model with <code>include</code>, <code>require</code>, and <code>exclude</code> operators. Each operator can match targets by hostname, tag, or both.</p>
<ul>
<li><strong>Include</strong> matches targets that have any of the specified values.</li>
<li><strong>Require</strong> matches targets that have all of the specified values.</li>
<li><strong>Exclude</strong> rejects targets that have any of the specified values.</li>
</ul>
<p><img src="/assets/upstream/images/cloudflare-one/access/tags-in-infra-app.png" alt="Infrastructure application builder showing target criteria with an included tag, port 22, and SSH as the selected protocol" /></p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Add an infrastructure application</a>.</p>


<h2 id="2026-09-14">2026-09-14</h2>

<strong>Require fresh authentication for SAML identity providers</strong>

<p>Cloudflare Access can now request fresh authentication from a SAML identity provider for every login. Turn on <strong>Require reauthentication</strong> in the Cloudflare dashboard, or set <code>force_authn</code> to <code>true</code> through the API. Access will then set <code>ForceAuthn</code> to <code>true</code> in signed and unsigned SAML authentication requests.</p>
<p>This option is useful when an application requires users to reauthenticate at the identity provider instead of relying on an existing identity provider session. The default value is <code>false</code>.</p>
<p>For configuration details, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#require-fresh-authentication-at-the-identity-provider">Require fresh authentication at the identity provider</a>.</p>


<h2 id="2026-09-14-1">2026-09-14</h2>

<strong>Discover where sensitive data goes before you create a Data Loss Prevention policy</strong>

<p><strong>Passive Detection</strong> for <a href="/cloudflare-one/data-loss-prevention/">Cloudflare Data Loss Prevention (DLP)</a> lets you learn from your Gateway traffic before deciding what to log or block. Discover the sensitive data types in sampled traffic, explore their destinations, and use the findings to build policies around your organization's needs.</p>
<p>The dashboard brings together detections from sampled HTTP request and response bodies. Select an entry to follow its detections over time, review destinations, and check policy coverage. You do not need a Gateway DLP policy to get these insights, and existing Gateway policies continue to apply.</p>
<p><img src="/assets/upstream/images/changelog/dlp/passive-detection.gif" alt="Passive Detection dashboard showing detection totals, data type distribution, policy coverage, and detection entries" /></p>
<p>Passive Detection is generally available. The detection entries available to your account depend on your <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">Zero Trust plan</a>.</p>
<p>To get started, refer to the <a href="/cloudflare-one/data-loss-prevention/passive-detection/">Passive Detection documentation</a>.</p>


<h2 id="2026-09-10">2026-09-10</h2>

<strong>Cloudflare One Client for macOS (version 2026.8.1290.1)</strong>

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


<h2 id="2026-09-10-1">2026-09-10</h2>

<strong>Cloudflare One Client for Windows (version 2026.8.1290.1)</strong>

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


<h2 id="2026-09-09">2026-09-09</h2>

<strong>Improved iOS tap-to-type experience for Browser Isolation</strong>

<p><a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> has improved the tap-to-type experience for users on iOS devices.</p>
<p>Previously, Browser Isolation displayed a full-screen overlay with the message <code>tap to type</code> when users focused a text field. The prompt now appears inline over the focused text field, reducing disruption when users enter text in isolated sessions.</p>
<p>If the focused text field is too small to display the full prompt, Browser Isolation displays a keyboard icon in the center of the text field instead.</p>
<p><img src="/assets/upstream/images/cloudflare-one/rbi/tap-to-type.jpg" alt="Inline tap-to-type prompt over a focused text field in Browser Isolation" /></p>
<p>iOS users should tap twice to begin entering text. This update applies automatically to Browser Isolation sessions on iOS.</p>
<p>For more information on why this interaction is required, refer to <a href="/cloudflare-one/remote-browser-isolation/known-limitations/#ios">iOS limitations</a>.</p>


<h2 id="2026-09-09-1">2026-09-09</h2>

<strong>New CASB integration for Zoom</strong>

<p><a href="/cloudflare-one/integrations/cloud-and-saas/">Cloudflare CASB</a> now integrates with <a href="/cloudflare-one/integrations/cloud-and-saas/zoom/">Zoom</a>. The integration connects through Cloudflare's pre-built OAuth application — no manual app setup in Zoom is required. After an initial scan, CASB continuously scans your Zoom account to surface new findings as your environment changes.</p>
<p>Zoom is widely used for meetings, webinars, and collaboration. Misconfigurations in account settings, meeting security controls, and recording access can expose organizations to data leakage, unauthorized access, and compliance risk. Cloudflare CASB ingests Zoom account data via API to surface security findings across these areas.</p>
<h4 id="2026-09-09-casb-zoom-integration-key-capabilities">Key capabilities</h4>
<p>Starting today, security teams can scan for security findings across the following assets:</p>
<ul>
<li><strong>Account settings</strong> — Detect weak password policies, unlocked security controls, and two-factor authentication gaps across your Zoom account</li>
<li><strong>User accounts</strong> — Identify users not enforcing SSO, accounts with insecure host keys, unverified or inactive users, and unsafe overrides of account-level security settings</li>
<li><strong>Meetings</strong> — Surface meetings without passwords or waiting rooms, meetings using Personal Meeting IDs (PMIs), and meetings with external domain hosts</li>
<li><strong>Recordings</strong> — Detect publicly accessible cloud recordings, recordings without passcodes, and weak recording password configurations</li>
<li><strong>Content</strong> — Identify sensitive information in meeting and recording content via DLP Profile matching</li>
</ul>
<h4 id="2026-09-09-casb-zoom-integration-learn-more">Learn more</h4>
<p>This <a href="/cloudflare-one/integrations/cloud-and-saas/zoom/">integration</a> is available to all Cloudflare Zero Trust customers today. New customers can sign up and start with their first two integrations for free. Existing customers can enable the integration directly in the Cloudflare One dashboard under <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>. The integration begins scanning immediately and surfaces findings in the dashboard within minutes.</p>


<h2 id="2026-09-02">2026-09-02</h2>

<strong>Define custom applications for breakout and prioritized traffic from the Cloudflare One Appliance dashboard</strong>

<p>You can now define <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#create-edit-or-delete-a-custom-application">custom applications</a> for <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/">breakout</a> and <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/">prioritized</a> traffic on the <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> directly from the dashboard, without calling the API.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-09-01-appliance-custom-application-traffic-steering.gif" alt="Adding a custom application by hostname, IP subnet, and source subnet from the Traffic Steering tab of an appliance profile" /></p>
<ul>
<li>In <strong>Traffic Steering</strong> &gt; <strong>Breakout traffic</strong> or <strong>Prioritized traffic</strong>, select <strong>Assign application traffic</strong> &gt; <strong>Add</strong> to create a custom application matched by <strong>Hostnames</strong>, <strong>IP subnets</strong>, and/or the new <strong>Source subnets</strong> field, alongside Cloudflare-managed applications.</li>
<li>Edit or delete an existing custom application from the same panel, no API round-trip required.</li>
<li><strong>Source subnets</strong> lets you match traffic by its source IP range, complementing the existing <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source">source LAN interface breakout criteria</a>.</li>
</ul>
<p>This complements the existing API and Terraform workflow for managing applications.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/">Breakout traffic</a> and <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/">Prioritized traffic</a>.</p>


<h2 id="2026-09-02-1">2026-09-02</h2>

<strong>Configure DHCP options from the dashboard on Cloudflare One Appliance</strong>

<p>You can now configure <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">custom DHCP options</a> directly from the dashboard when the <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> is acting as the DHCP server for a LAN.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-09-01-appliance-dhcp-options-ui.gif" alt="Adding a custom DHCP option to a LAN's DHCP server from the Network Configuration tab of an appliance profile" /></p>
<ul>
<li>In <strong>LAN configuration</strong>, under <strong>DHCP server options</strong>, select <strong>Add DHCP option</strong> to choose from common options for PXE / iPXE boot, VoIP phone provisioning, and vendor-specific configuration, or select <strong>Add custom option</strong> to enter your own option code, type, and value.</li>
<li>This complements the existing <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/#configure-dhcp-options">API and Terraform workflow</a> for configuring DHCP options.</li>
</ul>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">DHCP server options</a>.</p>


<h2 id="2026-09-02-2">2026-09-02</h2>

<strong>Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once</strong>

<p>You can now create multiple <a href="/tunnel/">Cloudflare Tunnel</a> and <a href="/mesh/">Cloudflare Mesh</a> routes from the Routes page in a single action, instead of submitting one route at a time.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/2026-09-01-tunnel-mesh-bulk.gif" alt="Creating multiple Cloudflare Tunnel and Cloudflare Mesh routes at once from the Routes page" /></p>
<p>When creating a route, you can now:</p>
<ul>
<li><strong>Add multiple destinations at once</strong> — Enter a comma-separated list of CIDR ranges or hostnames to create several routes of the same type and connector together.</li>
<li><strong>Queue up multiple routes</strong> — Select <strong>Add another</strong> to stage additional routes, including different types or connectors, before creating them all in one action.</li>
<li><strong>Retry only what failed</strong> — If some routes in a batch fail (for example, an invalid CIDR), the routes that were created successfully are removed from the form automatically, so you only need to fix and resubmit the ones that failed.</li>
</ul>
<p>The same Routes UI already supports bulk creation for <a href="/cloudflare-wan/">Cloudflare WAN</a> static routes, so you can add multiple WAN destinations or queue up several WAN routes before creating them together as well.</p>
<div class="nb-dash-button"></div>
<p>For setup steps, refer to <a href="/cloudflare-one/networks/routes/add-routes/">Add routes</a>.</p>


<h2 id="2026-08-31">2026-08-31</h2>

<strong>Load Balancing now supports pool sets</strong>

<p>Cloudflare Load Balancing now supports pool sets through the API. Pool sets combine geographic matching with location-specific traffic steering. One load balancer can now use different routing behavior for different locations.</p>
<p>Each pool set can match a Cloudflare data center, country, or region. It then supplies the candidate pools and can apply its own steering policy, pool weights, and fallback pool. Cloudflare evaluates pool sets in array order and applies the first matching pool set.</p>
<p>For example, this pool set uses Dynamic Latency steering for traffic from Germany:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;pool_sets&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;germany-lowest-latency&quot;,&#10;			&quot;match&quot;: { &quot;topology&quot;: { &quot;countries&quot;: [&quot;DE&quot;] } },&#10;			&quot;overrides&quot;: {&#10;				&quot;pools&quot;: [&#10;					&quot;0930eec54a4c7ae6616985b79f678210&quot;,&#10;					&quot;c8b4f5a6d7e84910a2b3c4d5e6f70819&quot;&#10;				],&#10;				&quot;steering_policy&quot;: &quot;dynamic_latency&quot;&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Use pool sets for active-active traffic distribution, location-specific failover, and regional routing policies. For proxied traffic, a pool set can also return a fixed HTTP response instead of selecting a pool.</p>
<p>For configuration details and more examples, refer to <a href="/load-balancing/understand-basics/traffic-steering/pool-sets/">Pool sets</a>.</p>


<h2 id="2026-08-29">2026-08-29</h2>

<strong>Cloudflare One Client for Linux (version 2026.7.1377.0)</strong>

<p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.</p>


<h2 id="2026-08-29-1">2026-08-29</h2>

<strong>Cloudflare One Client for macOS (version 2026.7.1376.0)</strong>

<p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.</p>


<h2 id="2026-08-29-2">2026-08-29</h2>

<strong>Cloudflare One Client for Windows (version 2026.7.1376.0)</strong>

<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>Fixed a rare but critical issue where the client could fail to connect or switch organizations due to an invalid registration after switching installed client versions. Additionally, this hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.</p>


<h2 id="2026-08-26">2026-08-26</h2>

<strong>Access service token secrets use a scannable format</strong>

<p>Cloudflare Access service token Client Secrets created on or after August 26, 2026, use the format <code>cfast_[40 alphanumeric characters][8-character checksum]</code>. The prefix and checksum make these credentials easier for secret scanning tools to identify with fewer false positives.</p>
<p>Existing service token secrets continue to work and do not require rotation. Both formats use the same Client ID and the same <code>CF-Access-Client-Id</code> and <code>CF-Access-Client-Secret</code> authentication headers.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Service tokens</a>.</p>


<h2 id="2026-08-25">2026-08-25</h2>

<strong>Grace periods for service token rotation</strong>

<p>Cloudflare Access administrators can now choose a grace period when rotating a service token secret. Both secrets remain valid during the grace period, giving administrators time to update services without interrupting authentication.</p>
<p>The dashboard offers grace periods from one hour to 30 days. Administrators can also revoke the previous secret immediately. The API accepts an RFC 3339 expiration time for custom rotation schedules.</p>
<p>For configuration instructions, refer to <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/#rotate-service-token-secrets">Rotate service token secrets</a>.</p>


<h2 id="2026-08-25-1">2026-08-25</h2>

<strong>Temporarily turn off Access service tokens</strong>

<p>Cloudflare Access administrators can now temporarily turn off service tokens without deleting them. A disabled token cannot authenticate, but its configuration remains available so administrators can turn it on again later.</p>
<p>Turning off a token also stops any previous secret in an active rotation grace period. Use this control to contain suspected credential exposure or pause an automated service.</p>
<p>For configuration instructions, refer to <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/#turn-a-service-token-on-or-off">Turn a service token on or off</a>.</p>


<h2 id="2026-08-25-2">2026-08-25</h2>

<strong>MCP server portals support MCP 2026-07-28 specification</strong>

<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support the stateless MCP <code>2026-07-28</code> specification for client and upstream server connections.</p>
<p>The portal's <code>/mcp</code> endpoint automatically accepts stateless MCP <code>2026-07-28</code> requests and earlier 2025 Streamable HTTP clients. When the portal connects to an upstream Streamable HTTP server, it checks for MCP <code>2026-07-28</code> support and falls back to the 2025 handshake when needed. Client and upstream protocol selection are independent, so clients and servers can upgrade separately without portal configuration changes.</p>
<p>SSE connections continue to use the legacy protocol. For details, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#transport">MCP server portal transport and protocol compatibility</a>.</p>


<h2 id="2026-08-24">2026-08-24</h2>

<strong>Download the Cloudflare One Virtual Appliance for your hypervisor from the dashboard</strong>

<p>When you register a <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Virtual Appliance</a>, you can now select your hypervisor and download the appliance directly from the dashboard — no need to look up asset URLs.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-08-24-virtual-appliance-self-serve-download.png" alt="Selecting a hypervisor and downloading the Cloudflare One Virtual Appliance from the Connectors page" /></p>
<ul>
<li>On the <strong>Connectors</strong> page, select <strong>Add an appliance</strong>, choose <strong>Virtual appliance</strong>, then select your hypervisor: <strong>VMware ESXi</strong>, <strong>Proxmox</strong>, or <strong>libvirt/KVM</strong>.</li>
<li>Download the OVA image (VMware ESXi) or the install script (Proxmox and libvirt/KVM) for the selected hypervisor.</li>
<li>Use <strong>View setup guide</strong> to open deployment instructions for your platform.</li>
</ul>
<p>This complements the existing self-serve <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key">registration and license key generation</a> in the dashboard.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#configure-a-virtual-machine">Configure a Cloudflare One Virtual Appliance</a>.</p>


<h2 id="2026-08-21">2026-08-21</h2>

<strong>Automatically remediate Microsoft 365 and Google Workspace findings with API-based CASB remediation policies</strong>

<p><a href="/cloudflare-one/integrations/cloud-and-saas/">Cloudflare CASB</a> is an API-based (agentless) tool that continuously scans your SaaS and cloud applications for security misconfigurations and data exposure. You can now use <strong>CASB remediation policies</strong> to automatically fix a finding or send a webhook the moment CASB detects it, without manual triage.</p>
<h4 id="2026-08-21-casb-policies-remediate-microsoft-365-and-google-workspace-findings">Remediate Microsoft 365 and Google Workspace findings</h4>
<p>A policy can perform a first-party remediation action directly against the SaaS integration API. When a policy triggers, Cloudflare revokes the external sharing configuration without human intervention.</p>
<p>Remediation is currently supported for file-sharing findings in Microsoft 365 and Google Workspace. Support for additional finding types and integrations is coming soon. For the full list of supported finding types, refer to <a href="/cloudflare-one/cloud-and-saas-findings/policies/#run-remediations">Run remediations</a> in the CASB remediation policies documentation.</p>
<h4 id="2026-08-21-casb-policies-send-webhooks">Send webhooks</h4>
<p>A policy can send posture finding data to Slack, ServiceNow, or any other webhook destination. Webhook actions are supported for all posture finding types across CASB integrations.</p>
<p>A single policy can perform both actions: remediate a finding and send a webhook.</p>
<h4 id="2026-08-21-casb-policies-get-started">Get started</h4>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Policies</strong>.</li>
<li>Select <strong>Create a policy</strong>.</li>
<li>Under <strong>Basic information</strong>, enter a <strong>Policy name</strong> and, optionally, a <strong>Description</strong>.</li>
<li>Under <strong>Choose how you want to trigger the policy</strong>, select a <strong>Vendor</strong>, <strong>Integration</strong>, and <strong>Finding type</strong>.</li>
<li>Under <strong>Define what to do with findings that match your trigger</strong>, choose <strong>Run Remediation</strong>, <strong>Send webhooks</strong>, or both.</li>
<li>Under <strong>Status</strong>, turn on <strong>Enable policy</strong>.</li>
<li>Select <strong>Create policy</strong>.</li>
</ol>
<h4 id="2026-08-21-casb-policies-learn-more">Learn more</h4>
<ul>
<li>Learn how to <a href="/cloudflare-one/cloud-and-saas-findings/policies/">create and manage CASB remediation policies</a> in Cloudflare One.</li>
<li>Configure <a href="/cloudflare-one/integrations/cloud-and-saas/webhooks/">CASB webhooks</a> as a policy destination.</li>
<li>Learn how to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/">manage findings</a> in Cloudflare One.</li>
</ul>
<p>CASB remediation policies are now available in Cloudflare One.</p>


<h2 id="2026-08-21-1">2026-08-21</h2>

<strong>Test Data Loss Prevention profiles without sending traffic through Gateway</strong>

<p><strong>Test scan</strong> lets you check how <a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention (DLP)</a> evaluates sample content before you apply a profile to production traffic. Paste text, upload a file, or upload a HAR file, then select the profiles you want to test.</p>
<p><img src="/assets/upstream/images/changelog/dlp/dlp-test-scan.gif" alt="Test scan results showing matched profiles, detection entries, and match context" /></p>
<p>Test scan sends content directly to the DLP scanner. Gateway policies are not evaluated, no traffic passes through Gateway, and no Gateway activity logs are created. Results include matched profiles, detection entries, confidence levels, match context, proximity keywords, file metadata, antivirus status, and OCR output.</p>
<p>Test scan is available to all Cloudflare Zero Trust customers. Profile availability depends on your <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">Zero Trust plan</a>.</p>
<p>For more details, refer to the <a href="/cloudflare-one/data-loss-prevention/test-scan/">Test scan documentation</a>.</p>


<h2 id="2026-08-20">2026-08-20</h2>

<strong>Cloudflare One Client for macOS (version 2026.7.1343.0)</strong>

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


<h2 id="2026-08-20-1">2026-08-20</h2>

<strong>Cloudflare One Client for Windows (version 2026.7.1343.0)</strong>

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


<h2 id="2026-08-19">2026-08-19</h2>

<strong>Access resource lists now support resource-scoped roles</strong>

<p>Members with only resource-scoped Access roles can now open Access resource list pages in the Cloudflare dashboard and call list endpoints in the API. They no longer need an additional account-scoped read-only role to list resources.</p>
<p>The dashboard and API return only resources included in the member's permission policy scopes. Filtering applies to Access applications, policies, service tokens, and identity providers. This allows administrators to delegate specific Access resources without granting account-wide visibility. Previously, the dashboard blocked these list pages and API list requests returned <code>403</code> responses.</p>
<p>For members with the Cloudflare Access App Admin role, policy lists include policies attached directly to the selected application. Reusable policies appear only when the member has the Cloudflare Access Policy Admin role for those policies.</p>
<p>For role definitions and assignment details, refer to <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">Resource-scoped roles</a> and <a href="/fundamentals/manage-members/scope/">Role scopes</a>.</p>


<h2 id="2026-08-19-1">2026-08-19</h2>

<strong>Threat Intel Lists supported in Unified Routing</strong>

<p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> Threat Intel Lists are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. This feature requires a Cloudflare Advanced Network Firewall subscription.</p>
<p>Support for additional features - Rate Limiting and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<h2 id="2026-08-19-2">2026-08-19</h2>

<strong>Cloudflare One Client for Linux (version 2026.7.1343.0)</strong>

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


<h2 id="2026-08-18">2026-08-18</h2>

<strong>Configure origin application settings for Cloudflare Tunnel in the dashboard</strong>

<p>You can now configure origin application settings directly in the Cloudflare dashboard when adding or editing a published application route for a <a href="/tunnel/">Cloudflare Tunnel</a>. These settings control how <code>cloudflared</code> connects to your origin server and were previously only available in the Cloudflare One dashboard or via local configuration files.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-origin-settings-dashboard.gif" alt="Configure origin application settings in the Cloudflare dashboard" /></p>
<p>When editing a published application, expand <strong>Additional application settings</strong> to configure parameters organized into three categories:</p>
<ul>
<li><strong>HTTP</strong> — Set a custom HTTP Host header or disable chunked encoding.</li>
<li><strong>TLS</strong> — Configure origin server name, CA pool, TLS timeout, disable TLS verification, match SNI to host, or enable HTTP/2 to origin.</li>
<li><strong>Connection</strong> — Tune connect timeout, keep-alive timeout, keep-alive connections, TCP keep-alive interval, proxy type, or disable Happy Eyeballs.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For the full list of origin parameters, refer to <a href="/tunnel/reference/origin-parameters/">Origin parameters</a>.</p>


<h2 id="2026-08-17">2026-08-17</h2>

<strong>Post-quantum key exchange for MX deployments</strong>

<p>Cloudflare Email Security now supports post-quantum hybrid key exchange with X25519MLKEM768 on the SMTP connections we make to receive and deliver mail. Deploying Email Security in front of a provider that supports post-quantum hybrid key agreement (like Google Workspace) will create a TLS 1.3 connection using post-quantum key agreement.</p>
<p>Inbound MX connections and outbound delivery connections now negotiate the <a href="/ssl/post-quantum-cryptography/#hybrid-key-agreement">X25519MLKEM768</a> hybrid key agreement when the peer supports it, protecting SMTP traffic against <a href="https://blog.cloudflare.com/pq-2024/">harvest-now, decrypt-later</a> attacks.</p>
<p>Support is backwards compatible and enabled automatically for all customers. Senders and receivers that do not yet advertise post-quantum key agreement continue to connect with classical key exchange.</p>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2026-08-17-1">2026-08-17</h2>

<strong>Load balancing analytics now filters by pool name</strong>

<p>Load balancing analytics now filters traffic data by pool name instead of pool ID, aligning the query behavior with the pool names displayed in the filter dropdown.</p>
<p>Previously, the analytics pool filter queried by internal pool ID while displaying pool names in the UI dropdown. This mismatch caused filtering issues when pools shared similar names or when you expected results based on the visible pool name. Because the underlying query used a different identifier than what appeared on screen, the displayed data could be confusing or incorrect.</p>
<p>The pool filter now queries by the same pool name shown in the dropdown. When you select a pool from the filter, the analytics graphs and tables display data for that specific pool as you would expect. This change affects:</p>
<ul>
<li><strong>Requests over time</strong>, filtering the chart series to the selected pool.</li>
<li><strong>Pool distribution</strong>, showing only the selected pool segment.</li>
<li><strong>Top endpoints</strong>, displaying cards for origins in the selected pool.</li>
<li><strong>Latency</strong>, showing latency data for the selected pool.</li>
</ul>
<p>The <strong>Logs</strong> view and health event filtering are unchanged.</p>
<p>To use this, go to <strong>Traffic</strong> &gt; <strong>Load Balancing Analytics</strong> for a zone. The same pool filter appears in the analytics view for an individual load balancer under <strong>Load Balancing</strong> at the account level.</p>
<p>For more information about analytics filters and metrics, refer to <a href="/load-balancing/reference/load-balancing-analytics/">Load Balancing Analytics</a>.</p>


<h2 id="2026-08-14">2026-08-14</h2>

<strong>You can now enable Access on a Worker or all Workers at once</strong>

<p>You now have two new ways to protect your <a href="/workers/">Workers</a> with <a href="/workers/configuration/cloudflare-access/">Cloudflare Access</a>.</p>
<p><strong>Protect an application across all its domains at once</strong></p>
<p>Until now, if a Worker was reachable on a route, a Custom Domain, and a <code>workers.dev</code> URL, you had to manually add each one to an Access application and keep the list in sync whenever routes or domains changed.</p>
<p>Now, Access attaches the policy to the Worker itself, so every associated domain and preview URL stays protected even when its routes or domains change.</p>
<p><img src="/assets/upstream/images/changelog/workers/protect-one-worker.png" alt="Access setting for protecting a single Worker" /></p>
<p><strong>Protect all new and existing Workers by default</strong></p>
<p>Make all Workers private by default, so every existing and newly created Worker requires sign-in before anyone can reach it.</p>
<p><img src="/assets/upstream/images/changelog/workers/protect-all-workers.png" alt="Account-wide Access setting that protects all Workers" /></p>
<p>If a specific Worker should remain publicly accessible, add a Worker-level bypass to exempt it.</p>
<p><img src="/assets/upstream/images/changelog/workers/make-worker-public.png" alt="Make a Worker public when all Workers are protected" /></p>
<p>Whether you protect a single application or all Workers at once, you can choose whether to protect preview deployments only or both previews and production, and control who can sign in by Cloudflare account membership, email address, or email domain.</p>
<p>For more advanced policy options, edit the policy in <a href="https://dash.cloudflare.com/?to=/:account/one/access/apps">Zero Trust</a>.</p>
<p><img src="/assets/upstream/images/changelog/workers/choose-who-can-sign-in.png" alt="Access policy configuration for controlling who can sign in" /></p>
<p><strong>View all of your Worker Access policies</strong></p>
<p>You can view and manage all of your Access policies in the <strong>Access</strong> tab of the Workers &amp; Pages section in the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers/access-policies.png" alt="Access tab showing all configured Access policies" /></p>
<p><strong>See who is accessing your Worker</strong></p>
<p>When Access is enabled on your Worker, every authenticated request includes <code>ctx.access</code>. Call <a href="/workers/runtime-apis/context/#access"><code>ctx.access.getIdentity()</code></a> to get the user's email, name, and groups — no manual JWT validation required.</p>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;    if (!ctx.access) {&#10;      return new Response(&quot;Access did not run&quot;, { status: 401 });&#10;    }&#10;&#10;    const identity = await ctx.access.getIdentity();&#10;    return Response.json({ aud: ctx.access.aud, email: identity?.email });&#10;  },&#10;};&#10;</code></pre>
<p><strong>Test Access locally</strong></p>
<p>You can now test Cloudflare Access locally with <code>wrangler dev</code>. Add a <code>dev</code> block to your <code>wrangler.jsonc</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;access&quot;: {&#10;    &quot;dev&quot;: {&#10;      &quot;aud&quot;: &quot;my-app&quot;,&#10;      &quot;identity&quot;: { &quot;email&quot;: &quot;admin@example.com&quot; }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Your Worker will receive this identity through <code>ctx.access</code> and <code>ctx.access.getIdentity()</code>, letting you test authenticated and unauthenticated flows without deploying. Remove the <code>dev</code> block to simulate unauthenticated requests.</p>
<p><strong>API and programmatic access</strong></p>
<p>You can also set up these policies through the <a href="/workers/configuration/cloudflare-access/">Workers API</a> instead of the dashboard.</p>


<h2 id="2026-08-13">2026-08-13</h2>

<strong>Detect and control software package downloads with package registry security</strong>

<p>Cloudflare Gateway can now detect software package downloads and give you policy control over supply chain traffic. When a developer or CI/CD pipeline downloads a package through Gateway, the proxy identifies the registry protocol from the request URL and extracts the package ecosystem, name, version, and namespace. You can then write <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a> using <code>pkg.*</code> selectors to allow or block package downloads.</p>
<h4 id="2026-08-13-package-protection-supported-ecosystems">Supported ecosystems</h4>
<p>Gateway detects package downloads for the following ecosystems:</p>
<table>
<thead>
<tr>
<th>Ecosystem</th>
<th>Namespace</th>
</tr>
</thead>
<tbody>
<tr>
<td>npm</td>
<td>Scope (for example, <code>@babel</code>)</td>
</tr>
<tr>
<td>PyPI</td>
<td>--</td>
</tr>
<tr>
<td>RubyGems</td>
<td>--</td>
</tr>
<tr>
<td>Cargo</td>
<td>--</td>
</tr>
<tr>
<td>Go</td>
<td>Module path</td>
</tr>
<tr>
<td>Maven</td>
<td>Group ID</td>
</tr>
<tr>
<td>NuGet</td>
<td>--</td>
</tr>
</tbody>
</table>
<h4 id="2026-08-13-package-protection-selectors">Selectors</h4>
<p>In the dashboard, select <strong>Package Ecosystem</strong> to access the package registry selectors. After selecting a single ecosystem, nested fields for package name, version, and namespace become available. Five <code>pkg.*</code> selectors are available for HTTP policies with the Allow and Block actions:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pkg.ecosystem</code></td>
<td>The package ecosystem detected from the request URL.</td>
</tr>
<tr>
<td><code>pkg.name</code></td>
<td>The package name extracted from the download URL.</td>
</tr>
<tr>
<td><code>pkg.version</code></td>
<td>The package version, with support for ecosystem-aware comparison operators.</td>
</tr>
<tr>
<td><code>pkg.namespace</code></td>
<td>The package namespace, when the ecosystem supports one.</td>
</tr>
<tr>
<td><code>pkg.purl</code></td>
<td>The <a href="https://github.com/package-url/purl-spec">Package URL (PURL)</a> derived from the detected coordinates. Available in the API only.</td>
</tr>
</tbody>
</table>
<p>Detection is based on the registry protocol rather than the hostname, so it works the same way whether traffic goes to a public registry, a corporate proxy such as Artifactory or Nexus, or a self-hosted mirror.</p>
<p>Package registry security requires <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a> to be turned on.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/package-registry-security/">Package registry security</a>.</p>


<h2 id="2026-08-12">2026-08-12</h2>

<strong>Block emails by content with blocked content rules</strong>

<p>Cloudflare Email security now lets administrators write their own content-based blocking rules. A new <strong>Blocked content</strong> area under <strong>Policies &amp; rules</strong> lets you define a plaintext string or a regular expression, choose whether to scan the message subject, body, or both, and automatically block any message that matches.</p>
<ul>
<li>Create rules using either <strong>plaintext</strong> matches or <strong>regular expressions</strong> — useful for blocking targeted phishing campaigns, known-bad phrases, or content patterns unique to your organization.</li>
<li>Choose the <strong>search location</strong> for each rule: <strong>subject</strong>, <strong>body</strong>, or <strong>subject and body</strong>.</li>
<li>Use the built-in <strong>regular expression checker</strong> to validate your pattern against sample text before saving, so you can confirm the rule matches what you expect and avoid false positives.</li>
<li>Matching messages are marked with a malicious <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/">disposition</a> and prevented from reaching users' inboxes.</li>
</ul>
<p>Blocked content rules currently only support the block action.</p>
<p>This feature is available for the following Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/email-security/settings/detection-settings/blocked-content/">Blocked content</a>.</p>


<h2 id="2026-08-12-1">2026-08-12</h2>

<strong>Independent MFA supports FIDO2 for infrastructure applications</strong>

<p><a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Infrastructure</a> applications support independent multi-factor authentication (MFA) with FIDO2 keys. You can allow <code>ssh_fido2_key</code>, <code>piv_key</code>, or both in application-level and policy-level MFA settings.</p>
<p>Users enroll FIDO2 keys through the App Launcher and connect with the generated SSH identity. FIDO2 keys for SSH are separate from browser-based WebAuthn security keys and Personal Identity Verification (PIV) keys.</p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-fido2-key-for-infrastructure-apps">Enroll a FIDO2 key for infrastructure apps</a> and <a href="/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications">Configure MFA for infrastructure applications</a>.</p>


<h2 id="2026-08-12-2">2026-08-12</h2>

<strong>MCP protocol detection and AI Security dashboard</strong>

<p>Cloudflare Gateway now automatically detects <a href="https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/">Model Context Protocol (MCP)</a> traffic flowing through your network. MCP is the standard protocol used by AI agents to connect to external tools and data sources. Gateway identifies MCP requests by inspecting protocol-specific headers and payload characteristics.</p>
<h4 id="2026-08-12-mcp-detection-and-dashboard-mcp-policy-selector">MCP policy selector</h4>
<p>A new <strong>Is MCP</strong> selector (<code>experimental.is_mcp</code>) is available in <a href="/cloudflare-one/traffic-policies/http-policies/#is-mcp">HTTP policies</a>. Use this selector to build Gateway rules that allow, block, or isolate MCP traffic.</p>
<p>This selector is currently in beta and may change before general availability.</p>
<p>For example, the following policy blocks MCP traffic that does not arrive through an approved <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP portal</a>:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Is MCP</td>
<td>is</td>
<td><em>True</em></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>Traffic Source</td>
<td>is not</td>
<td><em>MCP portal</em></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p><img src="/assets/upstream/images/changelog/gateway/gateway-block-unknown-mcp.png" alt="Example Gateway policy that blocks MCP traffic not arriving through an MCP portal" /></p>
<h4 id="2026-08-12-mcp-detection-and-dashboard-ai-security-report">AI security report</h4>
<p>A new <strong>AI security report</strong> dashboard under <strong>Insights &amp; Logs &gt; Dashboards</strong> provides visibility into MCP usage across your organization. The dashboard includes:</p>
<ul>
<li>Total MCP request volume, unique users, and unique MCP servers</li>
<li>A timeseries chart of unique MCP servers observed over time</li>
<li>A summary of Gateway policies that target MCP traffic</li>
</ul>
<p><img src="/assets/upstream/images/changelog/gateway/gateway-mcp-dashboard.png" alt="AI security report dashboard showing MCP detection data including total MCP requests, users, servers, and Gateway policies for MCP" /></p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a>.</p>


<h2 id="2026-08-12-3">2026-08-12</h2>

<strong>Traffic Source selector in Gateway policies</strong>

<p>Gateway <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a> and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> policies now include a <strong>Traffic Source</strong> selector that identifies how traffic reaches Cloudflare. This allows administrators to write policies that target specific on-ramp methods - for example, applying different rules to traffic arriving via the Cloudflare One Client compared to traffic routed through an MCP portal or a proxy endpoint.</p>
<h4 id="2026-08-12-traffic-source-selector-available-traffic-source-values">Available traffic source values</h4>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Device client</td>
<td><code>device_client</code></td>
<td>Traffic from the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client (WARP)</a></td>
</tr>
<tr>
<td>Mesh</td>
<td><code>mesh</code></td>
<td>Traffic from a <a href="/mesh/">Cloudflare Mesh</a> connector</td>
</tr>
<tr>
<td>Cloudflare WAN</td>
<td><code>cloudflare_wan</code></td>
<td>Traffic from <a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">Cloudflare WAN</a> (Magic WAN)</td>
</tr>
<tr>
<td>Clientless RDP</td>
<td><code>clientless_rdp</code></td>
<td>Traffic from a clientless RDP session</td>
</tr>
<tr>
<td>Proxy endpoint</td>
<td><code>proxy_endpoint</code></td>
<td>Traffic from a <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoint</a> (PAC file)</td>
</tr>
<tr>
<td>Clientless Browser Isolation</td>
<td><code>agentless_biso</code></td>
<td>Traffic from <a href="/cloudflare-one/remote-browser-isolation/">clientless Browser Isolation</a></td>
</tr>
<tr>
<td>MCP portal</td>
<td><code>mcp_portal</code></td>
<td>Traffic from an <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP portal</a></td>
</tr>
</tbody>
</table>
<p>The selector uses the <code>net.onramp.type</code> API field in both HTTP and Network policies.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Traffic Source</td>
<td><code>net.onramp.type == &quot;device_client&quot;</code></td>
</tr>
</tbody>
</table>
<h4 id="2026-08-12-traffic-source-selector-browser-isolation-selector">Browser Isolation selector</h4>
<p>A <strong>Browser Isolation</strong> selector is also available in Network and HTTP policies. This selector identifies whether the current session is running inside <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation</a>, allowing administrators to apply different policy behavior to isolated traffic.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Browser Isolation</td>
<td><code>net.is_isolated == true</code></td>
</tr>
</tbody>
</table>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a> and <a href="/cloudflare-one/traffic-policies/network-policies/">Network policies</a>.</p>


<h2 id="2026-08-11">2026-08-11</h2>

<strong>Hostname routing is now generally available, with a new public IP range for initial resolved IPs</strong>

<p><a href="https://blog.cloudflare.com/tunnel-hostname-routing/">Hostname routing</a> is now generally available. Instead of managing static IP lists and routes, you can route traffic by hostname across multiple Cloudflare One connectors:</p>
<ul>
<li><strong>Cloudflare Tunnel</strong>: route a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostname</a> (for example, <code>wiki.internal.local</code>) to a private application behind your tunnel, or a <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public hostname</a> (for example, <code>bank.example.com</code>) to egress through a specific tunnel and anchor traffic to a dedicated exit node.</li>
<li><strong>Cloudflare Mesh</strong>: attract a <a href="/mesh/features/routes/#hostname-routes">private or public hostname's traffic</a> to a Mesh node.</li>
</ul>
<p>Alongside GA, the default IPv4 range used for <span class="nb-glossary-tooltip" title="initial resolved IP">initial resolved IPs</span> (also called token IPs) is changing from a Carrier-Grade NAT (CGNAT) range to a public Cloudflare-owned range:</p>
<ul>
<li><strong>IPv4</strong>: <code>172.64.128.0/20</code></li>
<li><strong>IPv6</strong>: <code>2606:4700:0cf1:4000::/64</code></li>
</ul>
<p>This is the default range. You can <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">configure a custom initial resolved IP range</a> for IPv4 if it conflicts with your existing network.</p>
<p><strong>Why this is changing:</strong> Starting with <a href="https://developer.chrome.com/release-notes/142">Chrome 142</a>, Local Network Access (LNA) restrictions block background requests to CGNAT addresses (<code>100.64.0.0/10</code>), which included the previous initial resolved IP default (<code>100.80.0.0/16</code>). LNA is implemented at the Chromium engine level, so it affects all Chromium-based browsers (for example, Microsoft Edge, Brave, and Opera), not only Google Chrome. This could silently break hostname-based Gateway features for users of these browsers, and required Chrome Enterprise policy workarounds. The new default range is public Cloudflare address space, so it is not affected by this restriction.</p>
<p><strong>What is affected:</strong> Initial resolved IPs are used by several features that associate a DNS query with the network connection that follows it:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">Private</a> and <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public</a> hostname routing for Cloudflare Tunnel</li>
<li><a href="/mesh/features/routes/#hostname-routes">Hostname routes</a> for Cloudflare Mesh</li>
<li><a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Access private applications</a> on non-HTTPS ports</li>
<li><a href="/cloudflare-one/traffic-policies/egress-policies/host-selectors/">Egress policy host selectors</a> (Domain, Host, Application, and Content Categories)</li>
</ul>
<p>You can check your account's current range, or configure a custom range, at any time from <strong>Networking</strong> &gt; <strong>IP addresses</strong> &gt; <strong>Address space</strong> &gt; <strong>Custom IPs</strong>, or using the <a href="/api/resources/zero_trust/subresources/networks/subresources/subnets/#(resource)%20zero_trust.networks.subnets.initial_resolved_ip">Initial Resolved IP Subnet API</a>.</p>
<div class="nb-dash-button"></div>
<p>For full instructions, refer to <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">Configure initial resolved IPs</a>. The IPv6 range (<code>2606:4700:0cf1:4000::/64</code>) is unchanged and is not affected by this restriction.</p>
<p>The default IPv4 range, and all Cloudflare One IPv6 ranges, are automatically routed through the Cloudflare One Client and do not require any Split Tunnel configuration. Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges">Automatically managed ranges</a> for details.</p>
<p>If you were relying on a Chrome Enterprise policy workaround (such as <code>LocalNetworkAccessRestrictionsTemporaryOptOut</code>) while your account was still on the legacy CGNAT-based range, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/#google-chrome-restricts-access-to-private-hostnames">Google Chrome restricts access to private hostnames</a> for next steps.</p>


<h2 id="2026-08-11-1">2026-08-11</h2>

<strong>Cloudflare One Client for Windows (version 2026.6.905.0)</strong>

<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix addresses an uncommon and intermittent case on Windows devices where the device is unable to reconnect after the device is woken from sleep.</p>


<h2 id="2026-08-10">2026-08-10</h2>

<strong>Stream live logs from Cloudflare Tunnel in the dashboard</strong>

<p>Real-time Tunnel log streaming is now available in the Cloudflare dashboard under <strong>Networking</strong> &gt; <strong>Tunnels</strong>. This brings the same live debugging capability previously only available in the Cloudflare One dashboard, including multi-connector aggregated streaming for high-availability deployments.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-live-logs-core-dashboard.gif" alt="Stream live logs from a tunnel in the Cloudflare dashboard" /></p>
<p>In the tunnel detail view, a new <strong>Live logs</strong> tab lets you:</p>
<ul>
<li><strong>Stream logs from single or multiple connectors</strong> — In <a href="/tunnel/configuration/#replicas-and-high-availability">highly available</a> deployments with multiple <code>cloudflared</code> replicas, logs from all connectors are merged into a single stream grouped by hostname, making it easy to identify which host machine produced each log entry.</li>
<li><strong>Filter by log level, event type, and HTTP method</strong> — Narrow the stream to only the events you care about (HTTP, TCP, UDP, or <code>cloudflared</code> internal), at any log level.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For more information, refer to <a href="/tunnel/observability/#remote-log-streaming">Tunnel observability</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel log streams</a>.</p>


<h2 id="2026-08-07">2026-08-07</h2>

<strong>Load Balancing health notifications now resolve automatically</strong>

<p><a href="/load-balancing/">Load Balancing</a> health notifications are now stateful. When a pool or endpoint becomes unhealthy, the notification opens an incident in your alerting tool as before. When that same pool or endpoint recovers, the follow-up notification is matched to the original alert and resolves that incident automatically, so you no longer have to close it by hand.</p>
<p>As part of this change, Load Balancing also sends a notification when a pool or endpoint returns to a healthy state, not only when it becomes unhealthy. Expect to see recovery notifications alongside the failure notifications you already receive.</p>
<p>This applies to your existing Load Balancing health alerts with no configuration change, and it matches the behavior already used by <a href="/health-checks/">Health Checks</a> notifications.</p>
<p>Two things to keep in mind:</p>
<ul>
<li>A recovery notification is matched to the earlier unhealthy notification for the <strong>same pool or endpoint</strong>. Renaming an endpoint while an incident is open prevents the match, so that incident stays open until you close it.</li>
<li>If a health change cannot be classified as either healthy or unhealthy, the notification is still delivered, but without the state needed to open or resolve an incident.</li>
</ul>
<p>Refer to <a href="/load-balancing/additional-options/pagerduty-integration/">Integrate with PagerDuty</a> to learn more about routing Load Balancing health notifications to an incident management tool.</p>


<h2 id="2026-08-07-1">2026-08-07</h2>

<strong>Container image for Cloudflare Mesh</strong>

<p><a href="/mesh/">Cloudflare Mesh</a> nodes can now run as Docker containers. The <a href="https://hub.docker.com/r/cloudflare/mesh"><code>cloudflare/mesh</code></a> image is available on Docker Hub for Docker Compose, Kubernetes, and any OCI-compatible runtime — no host-level package installation required.</p>
<p>The image supports <code>amd64</code> and <code>arm64</code> architectures and includes built-in <a href="/mesh/guides/run-mesh-in-containers/#source-nat">source NAT</a> so return traffic routes correctly without VPC route table changes.</p>
<h4 id="2026-08-07-mesh-container-image-deployment-patterns">Deployment patterns</h4>
<ul>
<li><strong>Docker Compose</strong> — add a <code>cloudflare-mesh</code> service to your <code>compose.yaml</code> and connect your entire stack to a private network.</li>
<li><strong>Kubernetes StatefulSet</strong> — deploy a standalone Mesh node with persistent registration state.</li>
<li><strong>Kubernetes sidecar</strong> — add the Mesh image as a sidecar container in a Pod to connect an application to Cloudflare without application changes.</li>
<li><strong>CI/CD</strong> — pull the image in a pipeline step, join the Mesh, run integration tests against private infrastructure, and tear down. The node disappears when the container exits.</li>
</ul>
<p>For <a href="/mesh/features/high-availability/">high availability</a>, run multiple replicas with the same Mesh node token. Cloudflare operates replicas in active-passive mode with automatic failover.</p>
<div class="nb-dash-button"></div>
<p>For setup steps, runtime configuration, and deployment examples, refer to <a href="/mesh/guides/run-mesh-in-containers/">Run Mesh in Docker / Kubernetes</a>.</p>


<h2 id="2026-08-05">2026-08-05</h2>

<strong>Identity-aware controls are now available in AI Gateway</strong>

<p>AI Gateway now integrates with Cloudflare Access, giving you two new capabilities:</p>
<ul>
<li><strong>Protect your gateway endpoint.</strong> Put your AI Gateway behind Access so you can set policies that control who is allowed to call a specific gateway's endpoint.</li>
<li><strong>Identity-aware controls.</strong> When traffic reaches AI Gateway through an Access-protected custom domain, AI Gateway can use the authenticated user's Access identity in logs, analytics, routing, and spend controls.</li>
</ul>
<p>With identity-aware controls, you can set spend limits by authenticated user, control which gateways different users can access, filter logs by user, and build policies without passing user IDs from the client application. AI Gateway adds the verified Access user ID to request metadata as <code>cf.user_id</code>.</p>
<p>For setup instructions, refer to <a href="/ai-gateway/configuration/cloudflare-access/">Cloudflare Access</a>.</p>


<h2 id="2026-08-03">2026-08-03</h2>

<strong>Control authorization cookies for multi-domain Access applications</strong>

<p>Cloudflare Access administrators can now control whether a self-hosted application preemptively sets authorization cookies across its public hostnames.</p>
<p>Previously, Access automatically used eager redirects for applications with five or fewer hostnames. Applications with more than five hostnames received cookies as users visited each hostname. Administrators can now choose either behavior, regardless of the number of hostnames.</p>
<p>The new <strong>Eager redirect cookie</strong> setting is turned on by default for new applications. After a user signs in, Access redirects the browser through each hostname and sets a <code>CF_Authorization</code> cookie. This supports applications that need to make requests across hostnames before the user visits each one.</p>
<p>For applications with many hostnames, the redirect chain can cause sign-in loops in some browsers. Turn off the setting to issue the cookie only when a user visits each hostname.</p>
<p>To configure the setting, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#eager-redirect-cookie">Authorization cookie</a>.</p>


<h2 id="2026-08-03-1">2026-08-03</h2>

<strong>See fallback pool traffic separately in load balancing analytics</strong>

<p>Load balancing analytics now shows traffic served by your <a href="/load-balancing/understand-basics/health-details/#fallback-pools">fallback pool</a> separately from traffic routed to the same pool by normal steering.</p>
<p>Previously, requests were grouped by pool name alone. If the pool acting as your fallback also received traffic through your steering policy, both appeared as a single series, so it was not obvious from the graph whether Cloudflare was still making health-based routing decisions or had fallen back to the pool of last resort. Because the fallback pool ignores health, that distinction matters when you are diagnosing an outage or reviewing how much traffic was shed.</p>
<p>Fallback traffic is now labeled with the pool name followed by <code>(Fallback)</code>. A pool named <code>eu-west</code>, for example, is shown as <code>eu-west (Fallback)</code>. This label appears as its own entry in:</p>
<ul>
<li><strong>Requests over time</strong>, as a separate series in the chart.</li>
<li><strong>Pool distribution</strong>, as a separate segment.</li>
<li><strong>Top endpoints</strong>, as a separate card for the pool.</li>
</ul>
<p>The <strong>Latency</strong> view and the health event <strong>Logs</strong> are unchanged.</p>
<p>To see this, go to <strong>Traffic</strong> &gt; <strong>Load Balancing Analytics</strong> for a zone. The same breakdown appears in the analytics view for an individual load balancer under <strong>Load Balancing</strong> at the account level.</p>
<p>Refer to <a href="/load-balancing/reference/load-balancing-analytics/">load balancing analytics</a> to learn more.</p>


<h2 id="2026-07-31">2026-07-31</h2>

<strong>Static OAuth client credentials for MCP server portals</strong>

<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> can now connect to upstream MCP servers that require a pre-registered OAuth client. This supports OAuth providers that do not offer Dynamic Client Registration or have disabled it. This unlocks portal connections to major SaaS providers such as Slack and GitHub, whose MCP servers do not yet support DCR.</p>
<p>When adding an MCP server, administrators can enter the client ID and client secret from an OAuth application registered with the upstream provider. The configuration also supports custom OAuth endpoints, scopes, and the <code>client_secret_post</code> and <code>client_secret_basic</code> token endpoint authentication methods.</p>
<p>Cloudflare stores the client secret encrypted. Users still authenticate to the upstream server with their own accounts when they connect through a portal.</p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#configure-manual-oauth-credentials">Configure manual OAuth credentials</a>.</p>


<h2 id="2026-07-31-1">2026-07-31</h2>

<strong>Cloudflare One Client for macOS (version 2026.7.1210.1)</strong>

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


<h2 id="2026-07-31-2">2026-07-31</h2>

<strong>Cloudflare One Client for Windows (version 2026.7.1210.1)</strong>

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


<h2 id="2026-07-30">2026-07-30</h2>

<strong>Admins can turn on Code Mode by default for MCP portal users</strong>

<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> now support four Code Mode policies: <em>Off</em>, <em>Opt-in</em>, <em>On by default</em>, and <em>Enforced</em>. Admins can choose whether Code Mode is unavailable, optional, enabled by default, or required for every session.</p>
<p>Existing portals retain their current behavior. Portals that previously allowed Code Mode use <em>Opt-in</em>, while portals that did not allow Code Mode use <em>Off</em>. New portals also use <em>Opt-in</em> by default.</p>
<p>Clients turn on Code Mode for an <em>Opt-in</em> portal with <code>?codemode=search_and_execute</code>. The <em>On by default</em> policy lets clients opt out with <code>?codemode=off</code>, which avoids nested code execution when a client runs its own Code Mode implementation. The <em>Off</em> and <em>Enforced</em> policies ignore client overrides.</p>
<p>The Cloudflare API exposes these policies through the <code>code_mode</code> field:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;code_mode&quot;: &quot;default_on&quot;&#10;}&#10;</code></pre>
<p>The supported values are <code>off</code>, <code>opt_in</code>, <code>default_on</code>, and <code>enforced</code>. The previous <code>allow_code_mode</code> boolean is deprecated.</p>
<p>For configuration details and client behavior, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode-policies">Code Mode policies</a>.</p>


<h2 id="2026-07-28">2026-07-28</h2>

<strong>Control Cloudflare Gateway DNS caching with a maximum TTL setting</strong>

<p>You can now set a maximum time-to-live (TTL) for DNS responses returned by Gateway. When an upstream DNS record has a TTL that exceeds the configured maximum, Gateway caps it to your specified value. This ensures that DNS policy changes - such as blocking a newly identified malicious domain - take effect faster across all clients.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/gateway-max-ttl-traffic-settings.png" alt="The maximum DNS TTL setting in Traffic policies &gt; Traffic settings, showing a numeric input field that accepts values between 60 and 36,000 seconds" /></p>
<p>The setting is available at two levels:</p>
<ul>
<li><strong>Account level</strong> - In <strong>Traffic Policies</strong> &gt; <strong>Traffic Settings</strong>, under <strong>Proxy and inspection</strong>. This sets the default cap for all DNS locations.</li>
<li><strong>Per-location</strong> - Each <a href="/cloudflare-one/networks/resolvers-proxies/">DNS location</a> can inherit the account setting, disable the cap, or override it with a custom value.</li>
</ul>
<p>Two new fields are also available in DNS logs: <code>upstream_record_ttls</code> (the original TTL from the upstream response) and <code>applied_max_ttl</code> (the cap Gateway applied). These appear in the DNS logs column picker and in Logpush datasets.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/">Maximum DNS TTL</a>.</p>


<h2 id="2026-07-22">2026-07-22</h2>

<strong>Cloudflare One Client for Linux (version 2026.6.880.0)</strong>

<p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.</p>


<h2 id="2026-07-22-1">2026-07-22</h2>

<strong>Cloudflare One Client for macOS (version 2026.6.880.0)</strong>

<p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.</p>


<h2 id="2026-07-22-2">2026-07-22</h2>

<strong>Cloudflare One Client for Windows (version 2026.6.880.0)</strong>

<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.</p>


<h2 id="2026-07-20">2026-07-20</h2>

<strong>Browser-based login for plaintext HTTP private applications</strong>

<p>Cloudflare Access now uses the standard browser-based login flow for <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private applications</a> served over plaintext HTTP on port <code>80</code>.</p>
<p>Previously, plaintext HTTP private apps fell back to the same session flow used for SSH, RDP, and other non-HTTP protocols: users got an <code>Authentication required</code> pop-up from the Cloudflare One Client, then had to select the notification to open a browser and log in. Now, users hitting an HTTP private app see the Access login page directly in the browser and receive a standard Access <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/">application token</a> on success.</p>
<p>This brings the HTTP experience in line with HTTPS apps (with <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">Gateway TLS decryption</a> turned on). No configuration change is required. The Cloudflare One Client is still required to route traffic to the private network, but it no longer manages the Access session for HTTP apps.</p>
<p>Other non-HTTP protocols (SSH, RDP, arbitrary TCP/UDP) continue to use the Cloudflare One Client notification flow.</p>


<h2 id="2026-07-17">2026-07-17</h2>

<strong>Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard</strong>

<p>You can now restart, reboot, or shut down a <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> directly from the dashboard or via API.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-07-17-appliance-restart-reboot-shutdown.gif" alt="Restarting a Cloudflare One Appliance from the Operations section of the Edit Appliance page" /></p>
<ul>
<li><strong>Restart</strong> — Restart managed services. Purges temporary and (optionally) persistent state.</li>
<li><strong>Reboot</strong> — Power cycle the appliance. Optionally, purge persistent state. Re-applies configuration starting from scratch.</li>
<li><strong>Shutdown</strong> — Power off the appliance. Optionally, purge persistent state. The machine will be offline until manually powered on again.</li>
</ul>
<p>In the dashboard, go to <strong>Networking</strong> &gt; <strong>Connectors</strong> &gt; <strong>Appliances</strong>, select an appliance, then <strong>Edit</strong> &gt; <strong>Operations</strong> to send an operation. Via API, <code>POST</code> to the <code>/accounts/{account_id}/magic/connectors/{connector_id}/interrupts</code> endpoint.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/">Appliance operations</a>.</p>


<h2 id="2026-07-17-1">2026-07-17</h2>

<strong>New header control options for Gateway HTTP policies</strong>

<p>Cloudflare Gateway now supports advanced header control on <a href="/cloudflare-one/traffic-policies/http-policies/#allow">Allow policies</a>. Administrators can add, overwrite, or delete headers on matching requests using static values or dynamic variables.</p>
<h4 id="2026-07-17-http-request-header-manipulation-header-operations">Header operations</h4>
<p>Gateway HTTP policies using the Allow action support three operations in <code>rule_settings</code>:</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>API field</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Add</td>
<td><code>add_headers</code></td>
<td>Appends a value to the header. Existing values are preserved.</td>
</tr>
<tr>
<td>Overwrite</td>
<td><code>set_headers</code></td>
<td>Replaces the header value. Creates the header if it does not exist.</td>
</tr>
<tr>
<td>Delete</td>
<td><code>delete_headers</code></td>
<td>Removes the header from the request.</td>
</tr>
</tbody>
</table>
<p>Gateway applies operations in order: delete, then overwrite, then add.</p>
<h4 id="2026-07-17-http-request-header-manipulation-dynamic-variables">Dynamic variables</h4>
<p>Header values can include dynamic variables using the <code>@{...}</code> syntax. Gateway resolves variables at request time from identity, device, and network context.</p>
<table>
<thead>
<tr>
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@{identity.email}</code></td>
<td>User email from the identity provider</td>
</tr>
<tr>
<td><code>@{identity.name}</code></td>
<td>User display name from the identity provider</td>
</tr>
<tr>
<td><code>@{identity.id}</code></td>
<td>Cloudflare identity UUID</td>
</tr>
<tr>
<td><code>@{identity.groups}</code></td>
<td>Identity provider group memberships</td>
</tr>
<tr>
<td><code>@{identity.SAML}</code></td>
<td>SAML attributes (if configured)</td>
</tr>
<tr>
<td><code>@{identity.OIDC}</code></td>
<td>OIDC claims (if configured)</td>
</tr>
<tr>
<td><code>@{source.ip}</code></td>
<td>Source IP of the connection</td>
</tr>
<tr>
<td><code>@{destination.ip}</code></td>
<td>Destination IP of the request</td>
</tr>
<tr>
<td><code>@{device.id}</code></td>
<td>Cloudflare One Client device UUID</td>
</tr>
<tr>
<td><code>@{device.posture}</code></td>
<td>Device posture check results (JSON string)</td>
</tr>
</tbody>
</table>
<p>You can mix static text and dynamic variables in a single header value. For example, <code>user-@{identity.email}</code> resolves to <code>user-jdoe@example.com</code>.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/tenant-control/">Custom headers</a>.</p>


<h2 id="2026-07-16">2026-07-16</h2>

<strong>Bulk print PDFs for browser-based RDP</strong>

<p>Users in browser-based RDP sessions can now print multiple PDF files as a single print job. Copy the files to your clipboard on the remote machine, then select <strong>Print all PDFs</strong> in the clipboard panel. The files are combined into one PDF and sent to your local printer.</p>
<p><img src="/assets/upstream/images/changelog/access/rdp-bulk-print.png" alt="The clipboard panel showing the Print all PDFs option for multiple selected PDF files." /></p>
<p>Bulk print is available in Chromium-based browsers and Firefox. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#print-pdfs">Print PDFs for browser-based RDP</a>.</p>


<h2 id="2026-07-15">2026-07-15</h2>

<strong>Internal DNS is now generally available</strong>

<p><a href="/dns/internal-dns/">Internal DNS</a> is now generally available. Internal DNS provides authoritative and recursive DNS for private networks on the same global network and control plane you already use for public DNS, Zero Trust, and application services.</p>
<h4 id="2026-07-15-internal-dns-ga-why-it-matters">Why it matters</h4>
<ul>
<li><strong>Consolidate DNS operations.</strong> Public and private DNS run on one platform, with one API, one audit trail, and one place to set policy.</li>
<li><strong>Simplify split-horizon DNS.</strong> Internal and external resolution are defined as separate <a href="/dns/internal-dns/dns-views/">views</a> over shared zones, managed from a single control plane — so there is no drift to chase down.</li>
<li><strong>Extend Zero Trust to DNS.</strong> Resolver policies decide which users and devices resolve against which view, enforced by the same <a href="/cloudflare-one/traffic-policies/">Gateway</a> that already governs the rest of your traffic.</li>
</ul>
<p>Setting up Internal DNS takes three steps: create a zone, create a view, and define a resolver policy.</p>
<pre tabindex="0"><code class="language-json">POST /zones&#10;{&#10;  &quot;account&quot;: {&#10;    &quot;id&quot;: &quot;&lt;ACCOUNT_ID&gt;&quot;&#10;  },&#10;  &quot;name&quot;: &quot;corp.internal&quot;,&#10;  &quot;type&quot;: &quot;internal&quot;&#10;}&#10;</code></pre>
<p>Internal DNS is included with <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> for Enterprise customers. To get started, refer to the <a href="/dns/internal-dns/">Internal DNS documentation</a>.</p>


<h2 id="2026-07-10">2026-07-10</h2>

<strong>Source code detection improvements</strong>

<p>Data Loss Prevention (DLP) source code detection now focuses on identifying whole source code file uploads and downloads. Previously, source code detection performed partial scans resulting in a higher rate of false positives. Since only whole source code files are evaluated, code embedded in other content — such as chat messages, documentation, or code samples — is no longer flagged as source code, removing a common source of false positives.</p>
<p>Source code detection requires a minimum of 500 characters to evaluate a file. Files below this threshold are not flagged to reduce noise. This threshold filters out small fragments that lack enough context for reliable classification.</p>
<p>Enable and set <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/#confidence-thresholds">confidence levels</a> to tune match sensitivity. A higher confidence level reduces false positives by requiring stronger signals that the content is truly source code. A lower confidence level catches more files at the cost of additional noise.</p>
<p>Source code detection applies to standalone source code files in <a href="/cloudflare-one/traffic-policies/http-policies/">Gateway HTTP policies</a>. It does not detect source code embedded within other file types or payloads, such as <code>.docx</code> files or chat messages.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#source-code">Source Code predefined profiles</a>.</p>


<h2 id="2026-07-09">2026-07-09</h2>

<strong>Wi-Fi signal and network performance analytics for Cloudflare One Client devices</strong>

<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into device, network, and application performance across your Cloudflare SASE deployment.</p>
<p>The <strong>Device Monitoring</strong> page now analyzes hardware and network data between a Cloudflare One Client device and Cloudflare's edge, so you can diagnose connectivity and performance issues. Previously, this data was only available in raw DEX Device State Event logs, which required you to build your own analytics to interpret it.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex-device-monitoring-summary.png" alt="Device Monitoring summary with connection status, connection mode, Wi-Fi signal strength, traffic performance, and device health" /></p>
<p>A summary at the top of the page shows the health of each category at a glance, using <strong>Good</strong>, <strong>Fair</strong>, and <strong>Poor</strong> labels:</p>
<ul>
<li><strong>Connection</strong> — connection status, Cloudflare One Client mode, and tunnel type over time</li>
<li><strong>Wi-Fi signal strength</strong> — signal measured in dBm over time, with thresholds that flag a weak signal</li>
<li><strong>Traffic performance</strong> — upstream and downstream performance, including network throughput on the active interface</li>
<li><strong>Device health</strong> — hardware metrics such as CPU, memory, and disk</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dex/dex-device-monitoring-wifi-network.png" alt="Wi-Fi signal strength and network throughput charts on the Device Monitoring page" /></p>
<p>You can filter by category and adjust the time range to correlate a device's metrics with a user's reported issue.</p>
<p>These analytics are available to all Cloudflare One customers at no additional cost.</p>
<p>To learn more, refer to the <a href="/cloudflare-one/insights/dex/monitoring/">DEX monitoring documentation</a>.</p>


<h2 id="2026-07-09-1">2026-07-09</h2>

<strong>Zero Trust Networks route endpoints and Cloudflare Tunnel connections field retiring on October 5, 2026</strong>

<p>On <strong>October 5, 2026</strong>, two changes take effect across the <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> and <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a>: the CIDR-encoded route endpoints are removed, and tunnel list and get responses no longer include the <code>connections</code> field. If you manage private network routes or read tunnel connection details through the API, <code>cloudflared</code>, Terraform, or another integration, review the changes in the following sections and migrate before the removal date.</p>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-route-endpoints">Route endpoints</h4>
<p>The CIDR-encoded route endpoints are deprecated in favor of the standard, <code>route_id</code>-based endpoints that already exist today. Both sets of endpoints route a private network through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> or <a href="/mesh/">Cloudflare Mesh</a> (the API still refers to Mesh nodes as <code>warp_connector</code>) — only the request shape changes.</p>
<p><strong>Deprecated endpoints (removed October 5, 2026):</strong></p>
<ul>
<li>Create a tunnel route (CIDR Endpoint): <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/create/"><code>POST /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}</code></a></li>
<li>Update a tunnel route (CIDR Endpoint): <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/edit/"><code>PATCH /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}</code></a></li>
<li>Delete a tunnel route (CIDR Endpoint): <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/delete/"><code>DELETE /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}</code></a></li>
</ul>
<p><strong>Replacement endpoints:</strong></p>
<ul>
<li>Create a tunnel route: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/create/"><code>POST /accounts/{account_id}/teamnet/routes</code></a></li>
<li>Update a tunnel route: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/edit/"><code>PATCH /accounts/{account_id}/teamnet/routes/{route_id}</code></a></li>
<li>Delete a tunnel route: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/delete/"><code>DELETE /accounts/{account_id}/teamnet/routes/{route_id}</code></a></li>
</ul>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-what-is-changing">What is changing</h4>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Deprecated (CIDR-encoded path)</th>
<th align="left">Replacement</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Route identifier</td>
<td align="left">URL-encoded CIDR in the path (<code>/network/{ip_network_encoded}</code>)</td>
<td align="left"><code>route_id</code> in the path (<code>network</code> moves to the request body on create)</td>
</tr>
<tr>
<td align="left">Create</td>
<td align="left"><code>POST .../teamnet/routes/network/{ip_network_encoded}</code></td>
<td align="left"><code>POST .../teamnet/routes</code> with <code>network</code> and <code>tunnel_id</code> in the body</td>
</tr>
<tr>
<td align="left">Update</td>
<td align="left"><code>PATCH .../teamnet/routes/network/{ip_network_encoded}</code></td>
<td align="left"><code>PATCH .../teamnet/routes/{route_id}</code></td>
</tr>
<tr>
<td align="left">Delete</td>
<td align="left"><code>DELETE .../teamnet/routes/network/{ip_network_encoded}</code></td>
<td align="left"><code>DELETE .../teamnet/routes/{route_id}</code></td>
</tr>
</tbody>
</table>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-action-required">Action required</h4>
<ol>
<li>Capture each route's <code>route_id</code> by calling <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/">List tunnel routes</a>, or read it from the response the first time you create a route with the replacement endpoint.</li>
<li>Update any scripts, backend services, or CI/CD pipelines that call the CIDR-encoded endpoints directly.</li>
<li>If you manage routes with the <code>cloudflared tunnel route ip add | delete</code> commands, upgrade <code>cloudflared</code> to the <a href="https://github.com/cloudflare/cloudflared/releases">latest version</a>.</li>
<li>If you manage routes with Terraform, make sure you are on a current version of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_tunnel_cloudflared_route"><code>cloudflare_zero_trust_tunnel_cloudflared_route</code></a> resource and the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider</a>.</li>
</ol>
<pre tabindex="0"><code class="language-bash">&#35; Before: create a route by URL-encoding the CIDR into the path&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/network/172.16.0.0%2F16 \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;tunnel_id&quot;: &quot;&#x27;$TUNNEL_ID&#x27;&quot;, &quot;comment&quot;: &quot;Example comment for this route.&quot;}&#x27;&#10;&#10;&#35; After: create a route with the network in the request body&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;network&quot;: &quot;172.16.0.0/16&quot;, &quot;tunnel_id&quot;: &quot;&#x27;$TUNNEL_ID&#x27;&quot;, &quot;comment&quot;: &quot;Example comment for this route.&quot;}&#x27;&#10;&#10;&#35; After: update or delete a route using its route_id&#10;curl -X PATCH https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;comment&quot;: &quot;Updated comment for this route.&quot;}&#x27;&#10;&#10;curl -X DELETE https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-cloudflare-tunnel-and-cloudflare-mesh-connections">Cloudflare Tunnel and Cloudflare Mesh connections</h4>
<p>Starting the same day, the <code>connections</code> array is removed from list and get responses for <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> and <a href="/mesh/">Cloudflare Mesh</a> nodes (the <code>cfd_tunnel</code> and <code>warp_connector</code> API resources). Query the dedicated connections endpoint instead of reading the field off the tunnel or node object.</p>
<p>This affects:</p>
<ul>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/"><code>GET /accounts/{account_id}/cfd_tunnel</code></a> — <code>connections</code> removed from each item in <code>result</code></li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/get/"><code>GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}</code></a> — <code>connections</code> removed from <code>result</code></li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/"><code>GET /accounts/{account_id}/warp_connector</code></a> — <code>connections</code> removed from each item in <code>result</code></li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/get/"><code>GET /accounts/{account_id}/warp_connector/{tunnel_id}</code></a> — <code>connections</code> removed from <code>result</code></li>
</ul>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-action-required-1">Action required</h4>
<p>Fetch connection details from the tunnel-specific connections endpoint instead of parsing it off the list or get response. For Cloudflare Tunnel, call <a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connections/methods/get/"><code>GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections</code></a>. For Cloudflare Mesh, call <a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/connections/methods/get/"><code>GET /accounts/{account_id}/warp_connector/{tunnel_id}/connections</code></a>.</p>
<pre tabindex="0"><code class="language-bash">&#35; Before: read connections off the tunnel object&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;&#10;&#35; After: query connections directly&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID/connections \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Update any dashboards, monitoring scripts, or automation that parses <code>connections</code> from the tunnel list or get response. <code>cloudflared</code> and the Cloudflare Terraform provider do not read this field, so no changes are required on their side for this part of the update.</p>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-why-we-are-making-these-changes">Why we are making these changes</h4>
<ul>
<li><strong>Smaller, faster responses.</strong> Cloudflare Tunnel and Cloudflare Mesh nodes with many connections no longer inflate every list and get call — connection detail is only fetched when you need it.</li>
<li><strong>A single way to identify a route.</strong> Consolidating on <code>route_id</code> removes the need to URL-encode CIDR ranges into the path and matches how every other resource in the Zero Trust Networks API is addressed.</li>
<li><strong>Consistency across the API.</strong> Both changes align these endpoints with Cloudflare's standard REST conventions for resource identifiers and nested detail endpoints.</li>
</ul>
<p>To learn more, refer to the <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a>, the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a>, and <a href="/cloudflare-one/networks/routes/">Routes</a> documentation.</p>


<h2 id="2026-07-08">2026-07-08</h2>

<strong>IPsec downgrade protection (beta)</strong>

<p>Cloudflare IPsec now supports the <a href="https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-downgrade-prevention/"><code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code></a> IKEv2 extension to protect against downgrade attacks on IPsec tunnels.</p>
<p>IKEv2's original authentication design has each endpoint sign only its own outbound messages, not the full handshake transcript. A quantum-capable <a href="https://www.cloudflare.com/learning/security/threats/on-path-attack/">on-path attacker</a> can exploit this to bypass post-quantum key exchange by downgrading the connection to classical cryptography. The <code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code> extension addresses this by having both peers sign the entire handshake transcript during the authentication exchange, preventing an attacker from manipulating the negotiation without detection.</p>
<p>Key details:</p>
<ul>
<li>Available in beta for Cloudflare WAN and Magic Transit IPsec tunnels.</li>
<li>Cloudflare sends the <code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code> notification unconditionally as a responder when the feature flag is enabled.</li>
<li>Both the initiator (your device) and responder (Cloudflare) must support the extension for downgrade protection to be effective.</li>
<li>This feature is currently gated by a per-account feature flag. Contact your account team to turn it on.</li>
</ul>
<p>Refer to <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/#improved-downgrade-protection-beta">Downgrade protection</a> for more details.</p>


<h2 id="2026-07-08-1">2026-07-08</h2>

<strong>IP lists, IDS, and SIP rules supported in Unified Routing</strong>

<p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> IP lists, IDS, and SIP rules are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. These features require a Cloudflare Advanced Network Firewall subscription.</p>
<p>Support for additional features - Threat Intel Lists, Rate Limiting, and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<h2 id="2026-07-08-2">2026-07-08</h2>

<strong>Cloudflare One Client for Windows (version 2026.6.850.0)</strong>

<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix addresses a Windows authentication issue in the embedded WebView2 browser. Single sign-on could fail to use the Windows primary account, causing users to be prompted for an interactive sign-in. The embedded authentication browser now allows SSO providers to use the OS primary account when available.</p>


<h2 id="2026-07-07">2026-07-07</h2>

<strong>File transfer controls for browser-based RDP (beta)</strong>

<p>You can now configure file transfer controls for browser-based RDP with Cloudflare Access, allowing you to restrict whether users can upload or download files between their local machine and the remote Windows server.</p>
<p><img src="/assets/upstream/images/changelog/access/file-transfer-policy-control.png" alt="File transfer connection settings in the Access policy configuration." /></p>
<p>This feature is useful for organizations that support bring-your-own-device (BYOD) policies or third-party contractors using unmanaged devices. By restricting file transfers, you can prevent sensitive data from being moved out of the remote session to a user's personal device.</p>
<h4 id="2026-07-07-rdp-file-transfer-beta-configuration-options">Configuration options</h4>
<p>File transfer controls are configured per policy within your Access application, alongside existing <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#connection-settings">text clipboard controls</a>. For each policy, you can select one of the following options:</p>
<ul>
<li><strong>Client to remote RDP session allowed</strong> — Users can upload files from their local machine into the browser-based RDP session.</li>
<li><strong>Remote RDP session to client allowed</strong> — Users can download files from the browser-based RDP session to their local machine.</li>
<li><strong>Both directions allowed</strong> — Users can upload and download files between their local machine and the browser-based RDP session.</li>
<li><strong>Disable copying/pasting</strong> — Users are not allowed to transfer files between their local machine and the browser-based RDP session.</li>
</ul>
<p>By default, file transfer is denied for new policies. For existing Access applications created before this feature was available, file transfer remains denied.</p>
<h4 id="2026-07-07-rdp-file-transfer-beta-how-it-works">How it works</h4>
<p>To upload, drag files into the browser window or select the settings gear icon on the left side of the RDP session. To download, copy a file in the remote session and select the settings gear to download it, download multiple files as a zip, or print PDFs to a local printer.</p>
<p><img src="/assets/upstream/images/changelog/access/clipboard-side-panel.png" alt="The clipboard side panel showing files available for transfer." /></p>
<p><img src="/assets/upstream/images/changelog/access/remote-doc-ready-for-download-or-print-local.png" alt="A remote document ready for download or local printing." /></p>
<p>This feature is in beta and available on all Zero Trust plans. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#transfer-files">File transfer for browser-based RDP</a>.</p>


<h2 id="2026-07-07-1">2026-07-07</h2>

<strong>Browser Isolation support for authorization proxy endpoints</strong>

<p><a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> now supports Gateway <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">authorization proxy endpoints</a>. You can apply <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">HTTP Isolate policies</a> to traffic routed through authorization proxy endpoints, the same way you can for traffic from the Cloudflare One Client.</p>
<p>Previously, only <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint">source IP proxy endpoints</a> supported Browser Isolation, and only with non-identity policies. Because authorization proxy endpoints authenticate users through an identity provider, you can now apply identity-based Isolate policies to PAC file-proxied traffic without requiring the Cloudflare One Client.</p>
<p>To get started, <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">create an authorization proxy endpoint</a> and <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">build an Isolate policy</a>.</p>


<h2 id="2026-07-06">2026-07-06</h2>

<strong>Self-serve registration of Cloudflare One Virtual Appliance in the dashboard</strong>

<p>You can now register a <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Virtual Appliance</a> and generate its license key directly from the dashboard, without contacting your account team.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-07-06-virtual-appliance-self-serve-ui.gif" alt="Registering a Cloudflare One Virtual Appliance and generating its authentication key from the Connectors page" /></p>
<ul>
<li>On the <strong>Connectors</strong> page, select <strong>Add an appliance</strong> and choose <strong>Virtual appliance</strong> to register a virtual appliance and generate its authentication key.</li>
<li>Use <strong>Regenerate authentication key</strong> from a virtual appliance connector's menu to rotate its key. The previous key is immediately and irrevocably revoked.</li>
<li>The authentication key is shown only once — copy and store it securely.</li>
</ul>
<p>This complements the existing <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key">API and Terraform self-serve workflow</a> for provisioning virtual appliances. Hardware appliances continue to use the existing account-team fulfillment workflow.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a Cloudflare One Virtual Appliance</a>.</p>


<h2 id="2026-07-02">2026-07-02</h2>

<strong>Hostname routing for Cloudflare Mesh</strong>

<p>You can now add <a href="/mesh/features/routes/#hostname-routes">hostname routes</a> to a Cloudflare Mesh node, in addition to CIDR routes.</p>
<div class="nb-interactive-component" data-cf-component="MeshHostnameRoutingDiagram"></div>
<p>Instead of managing IP ranges, you can attract traffic for a hostname to a Mesh node:</p>
<ul>
<li><strong>Private hostname</strong> (for example, <code>wiki.internal.local</code>) — reach an internal application by name, which is useful when it has an unknown or ephemeral IP. On Mesh you do not need to run a DNS server; a local hosts-file entry on the node is enough, or you can use a Gateway resolver policy for split DNS.</li>
<li><strong>Public hostname</strong> (for example, <code>www.example.com</code>) — route that hostname's traffic through the node and egress via the node's public IP.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For setup steps, prerequisites, and DNS options, refer to <a href="/mesh/features/routes/#hostname-routes">Hostname routes</a>.</p>


<h2 id="2026-07-02-1">2026-07-02</h2>

<strong>Cloudflare One Client for Linux (version 2026.6.836.0)</strong>

<p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This package is the same release as 2026.6.822.0, with a fix for our RPM package. Previously the repository served a single build to every OS version, so an install could pull a dependency that isn't available on that release. The repository now serves the correct build for each operating system version, so installs automatically pull the dependencies that version requires. Debian and Ubuntu were not affected.</p>
<p>If you installed version 2026.6.822.0 on an RPM-based distribution, we recommend refreshing your repository configuration:</p>
<pre tabindex="0"><code class="language-bash">sudo curl -fsSL https://pkg.cloudflareclient.com/cloudflare-warp-ascii.repo | sudo tee /etc/yum.repos.d/cloudflare-warp.repo&#10;sudo dnf clean all&#10;sudo dnf install cloudflare-warp&#10;</code></pre>


<h2 id="2026-07-01">2026-07-01</h2>

<strong>Fix redirect URL fragment encoding for single-page applications</strong>

<p>Access now correctly preserves URL fragment characters (<code>/</code>, <code>?</code>, <code>=</code>, <code>&amp;</code>, <code>;</code>) when redirecting users back to an application after login. Previously, these characters were encoded with <code>encodeURIComponent</code>, which mangled fragment-based routes used by single-page applications (SPAs).</p>
<p>For example, an SPA URL like <code>https://app.example.com/#/dashboard?tab=settings&amp;view=advanced</code> would previously redirect to a broken URL after login. This is now handled correctly.</p>
<p>If your SPA users were experiencing broken navigation after authenticating through Access, this fix resolves the issue without any configuration changes.</p>


<h2 id="2026-07-01-1">2026-07-01</h2>

<strong>Independent MFA for infrastructure applications</strong>

<p><a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure</a> now supports independent multi-factor authentication (MFA) for SSH connections using YubiKey PIV keys. This adds a hardware-backed second factor to SSH access, ensuring that a compromised device session alone is not sufficient to reach your servers.</p>
<p>With per-application and per-policy configuration, you can enforce PIV key authentication for sensitive usernames (for example, <code>root</code>) while applying different requirements for other usernames. You can also set an MFA session duration to control how often users must re-authenticate.</p>
<h4 id="2026-07-01-ssh-mfa-piv-keys-enrollment">Enrollment</h4>
<p>Users enroll their YubiKey PIV key through the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a>. For enrollment instructions and SSH client setup, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-piv-key-for-infrastructure-apps">Enroll a PIV key for infrastructure apps</a>.</p>
<h4 id="2026-07-01-ssh-mfa-piv-keys-configuration">Configuration</h4>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications">Enforce MFA for infrastructure applications</a>.</p>


<h2 id="2026-06-30">2026-06-30</h2>

<strong>New permissions and roles for Gateway policies and lists</strong>

<p>You can now assign granular, resource-scoped roles for <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> firewall policies and <a href="/cloudflare-one/reusable-components/lists/">Zero Trust lists</a>. Administrators can delegate access to specific policy types or list management without granting account-wide or product-wide control.</p>
<h4 id="2026-06-30-gateway-granular-permissions-what-is-new">What is new</h4>
<p>When you <a href="/fundamentals/manage-members/manage/">add a member</a> or create a <a href="/fundamentals/manage-members/policies/">permission policy</a>, the following resource-scoped roles are now available:</p>
<table>
<thead>
<tr>
<th>Role</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Zero Trust Gateway Firewall Policies Admin</td>
<td>Can view and edit all Gateway firewall policies, including DNS, HTTP, and Network policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway DNS Policies Admin</td>
<td>Can view and edit Gateway DNS policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway HTTP Policies Admin</td>
<td>Can view and edit Gateway HTTP policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Network Policies Admin</td>
<td>Can view and edit Gateway Network policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Egress Policies Admin</td>
<td>Can view and edit Gateway Egress policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Resolver Policies Admin</td>
<td>Can view and edit Gateway Resolver policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Policies Admin</td>
<td>Can view and edit all Gateway policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Policies Read</td>
<td>Can view all Gateway policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Read Only</td>
<td>Can view all Gateway resources.</td>
</tr>
<tr>
<td>Zero Trust DNS Locations Admin</td>
<td>Can view and edit DNS locations.</td>
</tr>
<tr>
<td>Zero Trust Proxy Endpoints Admin</td>
<td>Can view and edit Gateway Proxy Endpoints.</td>
</tr>
<tr>
<td>Zero Trust Account Lists Admin</td>
<td>Can view and edit all Gateway and Access lists.</td>
</tr>
<tr>
<td>Zero Trust Account Lists Read</td>
<td>Can view all Gateway and Access lists.</td>
</tr>
</tbody>
</table>
<p>These roles allow you to:</p>
<ul>
<li>Grant a network engineer write access to Network policies only, without exposing DNS or HTTP policy configuration.</li>
<li>Allow a security analyst to view all Gateway policies in read-only mode for auditing purposes.</li>
<li>Delegate list management to a team that maintains block and allow lists without giving them access to policy configuration.</li>
</ul>
<p>You can also now assign <em>Resource-scoped roles</em>. These roles are complementary to existing account-level roles, and allow you to grant access to a specific resource, like an individual Gateway policy or Cloudflare One list. <strong>Existing account-level roles continue to work.</strong> A member with the <code>Cloudflare Gateway</code> or <code>Cloudflare Zero Trust</code> role retains full access to all Gateway resources. This ensures backward compatibility for existing automation and API tokens.</p>
<h4 id="2026-06-30-gateway-granular-permissions-get-started">Get started</h4>
<ul>
<li>Review the <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">resource-scoped roles</a> on the Cloudflare role reference.</li>
<li>Learn how to <a href="/fundamentals/manage-members/policies/">create permission policies</a> that use these roles.</li>
</ul>


<h2 id="2026-06-30-1">2026-06-30</h2>

<strong>Cloudflare One Client for Linux (version 2026.6.822.0)</strong>

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


<h2 id="2026-06-30-2">2026-06-30</h2>

<strong>Cloudflare One Client for macOS (version 2026.6.822.0)</strong>

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


<h2 id="2026-06-30-3">2026-06-30</h2>

<strong>Cloudflare One Client for Windows (version 2026.6.822.0)</strong>

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


<h2 id="2026-06-26">2026-06-26</h2>

<strong>Service token support for MCP server portals</strong>

<p>You can now connect autonomous agents and bots to an <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portal</a> using an <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Access service token</a>. Service token sessions can reach upstream MCP servers through the portal without a browser-based OAuth flow.</p>
<p>To set this up:</p>
<ul>
<li>Add a <a href="/cloudflare-one/access-controls/policies/#service-auth">Service Auth policy</a> that matches your service token to the portal's Access application.</li>
<li>Add a Service Auth policy that matches the same token to each linked MCP server's Access application.</li>
<li>Turn <strong>Require user auth</strong> off (<code>on_behalf: false</code>) for each linked server so the portal uses the admin credential instead of a per-user OAuth grant.</li>
</ul>
<p>The bot connects with <code>CF-Access-Client-Id</code> and <code>CF-Access-Client-Secret</code> headers and sees the tools from every linked server it is authorized for. Servers that still require per-user OAuth are excluded from service token sessions because a service token cannot complete a per-user OAuth grant.</p>
<p>For step-by-step setup, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-with-a-service-token">Connect with a service token</a>.</p>


<h2 id="2026-06-25">2026-06-25</h2>

<strong>Cloudflare One Client for macOS (version 2026.6.782.1)</strong>

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


<h2 id="2026-06-23">2026-06-23</h2>

<strong>Regionalized IP Bindings for Regional Services</strong>

<p>Regional Services now supports <strong>Regionalized IP Bindings</strong>, letting you regionalize traffic at the IP layer for prefixes you bring to Cloudflare through <a href="/byoip/">Bring Your Own IP (BYOIP)</a>.</p>
<p>Where <a href="/data-localization/regional-services/regional-hostnames/">Regional Hostnames</a> regionalize traffic by hostname, Regionalized IP Bindings let you bind a CIDR from one of your prefixes to a region — ideal for address-map deployments and any service you address by IP rather than hostname. Cloudflare then terminates TLS and processes traffic to those addresses only within the data centers in that region.</p>
<p>Regionalized IP Bindings requires the Regional Services and Regional Services for BYOIP entitlements. Contact your account team to enable them.</p>
<p>To get started, refer to <a href="/data-localization/regional-services/ip-bindings/">Regionalized IP Bindings</a>.</p>


<h2 id="2026-06-19">2026-06-19</h2>

<strong>Manage all your routes from one page in the dashboard</strong>

<p>The <strong>Routes</strong> page in the Cloudflare dashboard now shows the routes across all of your connectors — <a href="/mesh/">Cloudflare Mesh</a> and <a href="/tunnel/">Cloudflare Tunnel</a> routes alongside <a href="/cloudflare-wan/">Cloudflare WAN</a> and <a href="/magic-transit/">Magic Transit</a> static routes — in a single table, instead of a separate routes view per product.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/2026-06-19-unified-routes.gif" alt="The unified Routes page in the Cloudflare dashboard, showing routes across connectors in a single table" /></p>
<p>From the unified Routes page you can:</p>
<ul>
<li><strong>Visualize your network with an interactive map</strong> that shows how your destinations flow through to your connectors — including equal-cost multi-path (ECMP) routes where the same prefix is served by several connectors. Select a node to filter the table down to the routes behind it.</li>
<li><strong>See every route in one table</strong>, with its destination, type, connector, priority, and source, and filter or sort to find what you need.</li>
<li><strong>Create, edit, and delete routes</strong> of any supported type without leaving the page. When adding a Cloudflare WAN or Magic Transit static route, you now pick the next hop by <strong>connector name</strong> instead of typing its IP.</li>
<li><strong>Manage <a href="/cloudflare-one/networks/virtual-networks/">virtual networks</a></strong> from a dedicated tab.</li>
<li><strong>Test a route</strong> to see which connector and next hop a destination resolves to before you commit a change.</li>
</ul>
<p>To find it, go to <strong>Networking</strong> &gt; <strong>Routes</strong> in the dashboard sidebar.</p>
<div class="nb-dash-button"></div>
<p>Your existing routes, APIs, and configurations are unchanged — this is a dashboard experience that brings them together in one place. Learn how to <a href="/cloudflare-one/networks/routes/add-routes/">add routes</a> and <a href="/cloudflare-one/networks/virtual-networks/">manage virtual networks</a>.</p>


<h2 id="2026-06-18">2026-06-18</h2>

<strong>Cloudflare identity provider is now the default for new accounts</strong>

<p>When you create a new Zero Trust organization, Cloudflare now adds the <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">Cloudflare identity provider</a> as your default login method. Previously, new organizations started with <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time PIN (OTP)</a>.</p>
<p>With the Cloudflare identity provider, your users authenticate using their existing Cloudflare account credentials, and authentication is restricted to members of your account. You can still add OTP or connect any <a href="/cloudflare-one/integrations/identity-providers/">third-party identity provider</a> whenever you need to.</p>
<p>This change only applies to newly created accounts. Existing organizations keep the login methods they already have configured. If you would like to use the Cloudflare Identity Provider in an existing account, you must enable it.</p>


<h2 id="2026-06-11">2026-06-11</h2>

<strong>Define custom topics for AI prompt protection</strong>

<p>You can now define custom topics for AI prompt protection. Predefined <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topics</a> cover common content and intent categories such as PII, source code, and jailbreak attempts. Custom topics let you detect unique or proprietary concepts that are not included in predefined categories.</p>
<p>You describe a custom topic in natural language, and Cloudflare DLP detects whether a prompt matches that topic based on context rather than specific keywords. For example, a topic that describes confidential merger discussions matches a prompt that paraphrases the deal, even when the prompt never uses the word merger or names the companies involved. To detect literal values such as internal codenames or product identifiers, use a <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#custom-wordlist-datasets">custom wordlist or pattern entry</a> instead.</p>
<p>Custom topics run through the same <a href="/cloudflare-one/traffic-policies/http-policies/#granular-controls">application granular controls</a> path as predefined AI prompt topics. Custom topics are available for ChatGPT, Google Gemini, Perplexity, and Claude.</p>
<h4 id="2026-06-11-custom-ai-prompt-topics-create-a-custom-ai-prompt-topic">Create a custom AI prompt topic</h4>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Detection entries</strong>.</li>
<li>Select <strong>AI prompt topics</strong>, then select <strong>Custom Prompt Topic</strong>.</li>
<li>Describe the topic in natural language. Be specific about the concept you want to detect. For example, describe unreleased product roadmap details or confidential customer contract terms.</li>
<li>Add this detection entry to an existing DLP profile, or <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile">create a new DLP profile</a>.</li>
<li>Use the profile in a Gateway HTTP policy to log or block prompts that match the topic.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17715.md")</aside>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topics</a>.</p>


<h2 id="2026-06-05">2026-06-05</h2>

<strong>Filter Workers' public Internet traffic using Gateway policies</strong>

<p>Workers using a <a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> binding with <code>network_id: &quot;cf1:network&quot;</code> now egress to public Internet destinations through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>. This means your existing Zero Trust traffic policies — DNS, HTTP, Network, and egress — extend to traffic that originates from your Workers, the same way they do for WARP users today.</p>
<div class="nb-interactive-component" data-cf-component="WorkersVPCEgressDiagram"></div>
<p>What you get by default:</p>
<ul>
<li><strong>Visibility.</strong> Worker egress shows up in Gateway <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS</a>, <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a>, and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> logs alongside your other traffic, so you can audit what your Workers are calling and when.</li>
<li><strong>Enforcement.</strong> Any existing Gateway policy whose selectors match a Worker request will apply — including allow / block lists, DNS category filtering, and HTTP destination rules. If you have already blocked a category for your workforce, your Workers inherit that block.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17825.md")</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17826.md")</div>
<p>For configuration options, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a>. For policy authoring, refer to <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway traffic policies</a>.</p>


<h2 id="2026-06-04">2026-06-04</h2>

<strong>Share identity providers across accounts with IdP federation</strong>

<p>Cloudflare Access now supports <a href="/cloudflare-one/integrations/identity-providers/idp-federation/">IdP federation</a>, which allows organizations to share a single identity provider across multiple Cloudflare accounts.</p>
<p>Instead of configuring the same IdP (for example, Okta or Entra ID) separately in every account, you configure it once in a source account and share it with the other accounts in your organization. Each recipient account gets a read-only IdP connection that routes authentication back to the source account through a bridge — a hidden application in the source account that brokers the cross-account login. End users sign in with their existing IdP credentials, and each account's Access policies evaluate the resulting identity just like any other IdP login.</p>
<p>Key capabilities:</p>
<ul>
<li><strong>One IdP, many accounts</strong> — Configure your IdP once and share it with all accounts in your organization.</li>
<li><strong>Lifecycle management</strong> — As accounts join or leave your Cloudflare organization, their IdP connections are provisioned and removed automatically — no manual cleanup required.</li>
<li><strong>Immutable recipient connections</strong> — IdP connections in recipient accounts cannot be accidentally modified or deleted.</li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/integrations/identity-providers/idp-federation/">IdP federation</a>.</p>


<h2 id="2026-06-03">2026-06-03</h2>

<strong>SAML assertion encryption for identity providers</strong>

<p>Cloudflare Access now supports SAML assertion encryption for identity provider integrations. When turned on, your identity provider encrypts SAML assertions using a Cloudflare-managed certificate before sending them through the user's browser. Only Access can decrypt these assertions, protecting sensitive identity data even after TLS termination.</p>
<p>Without encryption, SAML assertions are transmitted in plaintext and could be visible to browser extensions or client-side malware.</p>
<p><img src="/assets/upstream/images/changelog/access/saml-encryption.png" alt="SAML encryption toggle in the identity provider configuration" /></p>
<p>SAML encryption includes built-in certificate lifecycle management:</p>
<ul>
<li><strong>Automatic certificate generation</strong>: Access generates an encryption certificate when you turn on SAML encryption for an identity provider.</li>
<li><strong>Certificate rotation</strong>: Rotate certificates without downtime. The previous certificate remains valid until expiration, giving you time to update your IdP.</li>
<li><strong>PEM export</strong>: Copy the certificate in PEM format for manual upload to your IdP, or point your IdP to the SAML metadata endpoint for automatic retrieval.</li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#encrypt-saml-assertions">Encrypt SAML assertions</a>.</p>


<h2 id="2026-06-02">2026-06-02</h2>

<strong>Cisco IOS XE</strong>

<p>The Cisco IOS XE third-party integration guide for Cloudflare WAN has been updated to include:</p>
<ul>
<li>Post Quantum Cryptography (PQC)</li>
<li>Policy-Based Routing (PBR)</li>
<li>IP Service Level Agreement (IP SLA)</li>
</ul>
<p>This link will take you directly to the updated <a href="/cloudflare-wan/configuration/third-party/cisco-ios-xe/">Cisco IOS XE</a> guide.</p>


<h2 id="2026-05-29">2026-05-29</h2>

<strong>Cloudflare One Client for macOS (version 2026.5.1155.1)</strong>

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


<h2 id="2026-05-29-1">2026-05-29</h2>

<strong>Cloudflare One Client for Windows (version 2026.5.1155.1)</strong>

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


<h2 id="2026-05-28">2026-05-28</h2>

<strong>Tool and prompt aliases for MCP server portals</strong>

<p>When you connect third-party MCP servers through <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a>, you have no control over how the server author named tools or wrote descriptions. Unclear names make it harder for AI agents to select the right tool and harder for users to understand what is available.</p>
<p>You can now <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#rename-tools-and-prompts-with-aliases">rename tools and prompts</a> and rewrite their descriptions directly on the portal, without modifying the upstream server. For example, a tool named <code>super_cool_tool</code> can become <code>search_customer_records</code> with a description tailored to your organization.</p>
<p><img src="/assets/upstream/images/changelog/access/portal-edit-tool-modal.png" alt="Edit tool modal showing name and description fields for an MCP server tool" /></p>
<p>Modified tools display a <strong>Modified</strong> label in the tools list so administrators can see which tools have been customized at a glance.</p>
<p><img src="/assets/upstream/images/changelog/access/portal-tools-authorized-modified.png" alt="Tools authorized list showing a modified label on a renamed tool" /></p>
<p>Aliases override the metadata that MCP clients receive. You can set them at two levels:</p>
<ul>
<li><strong>Per portal</strong>: Applies only within a specific portal. Takes precedence over server-level aliases.</li>
<li><strong>Per server</strong>: Applies across all portals that use the server.</li>
</ul>
<p>You can reset an alias at any time to restore the original upstream name.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#rename-tools-and-prompts-with-aliases">Tool and prompt aliases</a>.</p>


<h2 id="2026-05-28-1">2026-05-28</h2>

<strong>High availability replica management for Cloudflare Mesh</strong>

<p>The <a href="/mesh/">Cloudflare Mesh</a> dashboard now shows per-replica details for <a href="/mesh/features/high-availability/">high availability</a> nodes. You can see which replica is active, view each replica's Mesh IP and connection details, and manually trigger failover — all from the node detail page.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/mesh-ha-replicas.gif" alt="Mesh HA replica tabs showing active and passive replicas with per-replica Mesh IPs and a manual failover option" /></p>
<h4 id="2026-05-28-mesh-ha-replica-ui-what-s-new">What's new</h4>
<ul>
<li><strong>Replica tabs</strong> on the node detail page — switch between replicas to see each one's Mesh IP, edge data center, origin IP, platform, version, and uptime.</li>
<li><strong>Active/passive badges</strong> identify which replica is currently routing traffic.</li>
<li><strong>Manual failover</strong> — promote a passive replica to active with a single click. The previous active replica switches to standby.</li>
<li><strong>HA badge</strong> in the overview table identifies nodes running multiple replicas.</li>
<li><strong>Active replica IP</strong> shown in the overview table — the dashboard now resolves which replica is active and displays the correct Mesh IP.</li>
</ul>
<h4 id="2026-05-28-mesh-ha-replica-ui-manual-failover">Manual failover</h4>
<p>To manually promote a passive replica:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/?to=/:account/mesh">Cloudflare dashboard</a>, go to <strong>Networking</strong> &gt; <strong>Mesh</strong>.</li>
<li>Select an HA-enabled node.</li>
<li>Select the passive replica tab.</li>
<li>Select <strong>Promote to active</strong> and confirm.</li>
</ol>
<p>Traffic reroutes to the promoted replica immediately. Refer to <a href="/mesh/features/high-availability/">High availability</a> for details on failover behavior.</p>


<h2 id="2026-05-27">2026-05-27</h2>

<strong>Write regex using natural language in Cloudflare One</strong>

<p><a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> policy selectors which support regular expressions can now be authored in the dashboard using natural language. When building a <a href="/cloudflare-one/traffic-policies/expression-syntax/">policy</a> with a regex-based selector (like <code>matches regex</code>), you can describe what you want to match in plain English and the Cloudflare Agent will generate and validate a corresponding regular expression.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/gateway-regex-ai-generation.png" alt="Write policy regex using natural language" /></p>
<p>To get started, select a regex-compatible selector in the <a href="/cloudflare-one/traffic-policies/">Gateway policy builder</a> and select the icon. You'll see an input field for natural language, such as &quot;any URL starting with /api/v1&quot; or &quot;.com, .net, and .app hosts which contain <code>gooogle</code> in the host.&quot;</p>
<p>You can also use the tool to explain existing regular expressions. If a policy already contains a regex pattern, you can instantly generate a plain-language description.</p>
<p>A built-in feedback mechanism allows you to rate each interaction to help improve output quality over time.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/">Cloudflare One firewall policies</a> and expect to see the same functionality supported soon in <a href="/cloudflare-one/data-loss-prevention/">Data loss prevention profiles</a>.</p>


<h2 id="2026-05-27-1">2026-05-27</h2>

<strong>Cloudflare Tunnel now runs connectivity pre-checks at startup</strong>

<p>Starting with <a href="https://github.com/cloudflare/cloudflared/releases"><code>cloudflared</code> version 2026.5.2</a>, <a href="/tunnel/">Cloudflare Tunnel</a> automates the entire <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/">connectivity pre-checks workflow</a> directly inside the binary. Previously, customers had to install <code>dig</code> and <code>netcat</code> and run those commands by hand to verify their environment. Now <code>cloudflared</code> does it natively at startup — and surfaces actionable remediation when something is blocked.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/cloudflared-connectivity-prechecks.gif" alt="cloudflared connectivity pre-checks output" /></p>
<p>On every <code>cloudflared tunnel run</code> (and <code>cloudflared tunnel diag</code>), the binary now natively checks:</p>
<ul>
<li><strong>DNS resolution</strong> — <code>region1.v2.argotunnel.com</code> and <code>region2.v2.argotunnel.com</code> resolve to valid Cloudflare IPs.</li>
<li><strong>Transport connectivity</strong> — outbound <code>UDP (QUIC)</code> and <code>TCP (HTTP/2)</code> on port <code>7844</code>.</li>
<li><strong>Management API</strong> — outbound <code>TCP/443</code> to <code>api.cloudflare.com</code> for software updates.</li>
</ul>
<p>Results are printed in a scannable CLI table with three states:</p>
<ul>
<li>✅ <strong>Pass</strong> — the check succeeded.</li>
<li>⚠️ <strong>Warn</strong> — a non-blocking issue, for example the Management API is unreachable so automatic updates will not work, but the tunnel will still come up.</li>
<li>❌ <strong>Fail</strong> — a blocking issue, with a specific remediation hint (for example, <code>Allow outbound UDP on port 7844</code>).</li>
</ul>
<p>If DNS is unresolvable, or <strong>both</strong> UDP and TCP fail on port 7844, <code>cloudflared</code> exits early with the failure rather than looping on opaque <code>failed to dial</code> errors.</p>
<p>Pre-checks now run automatically on every start, which also catches regressions like overnight firewall policy changes — no need to remember to rerun the troubleshooting guide.</p>
<p>To get the new behavior, upgrade <code>cloudflared</code> to version <code>2026.5.2</code> or later. For more details, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/">Connectivity pre-checks documentation</a>.</p>


<h2 id="2026-05-27-2">2026-05-27</h2>

<strong>Cloudflare One Client for Linux (version 2026.4.1390.0)</strong>

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


<h2 id="2026-05-27-3">2026-05-27</h2>

<strong>Cloudflare One Client for macOS (version 2026.4.1390.0)</strong>

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


<h2 id="2026-05-27-4">2026-05-27</h2>

<strong>Cloudflare One Client for Windows (version 2026.4.1390.0)</strong>

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


<h2 id="2026-05-21">2026-05-21</h2>

<strong>Granular permissions for Cloudflare Tunnel and Cloudflare Mesh</strong>

<p>You can now scope Cloudflare permissions to individual <a href="/tunnel/">Cloudflare Tunnel</a> instances and <a href="/mesh/">Cloudflare Mesh</a> nodes. Administrators can delegate access to specific Tunnels or Mesh nodes without granting account-wide control over private networking.</p>
<h4 id="2026-05-21-tunnel-mesh-granular-permissions-what-is-new">What is new</h4>
<p>When you <a href="/fundamentals/manage-members/manage/">add a member</a> or create a <a href="/fundamentals/manage-members/policies/">permission policy</a>, the resource picker now lists <a href="/tunnel/">Cloudflare Tunnel</a> instances and <a href="/mesh/">Cloudflare Mesh</a> nodes as scopable resource types. You can:</p>
<ul>
<li>Grant a read-only role on a single Cloudflare Tunnel instance to a support operator for log streaming and diagnostics — without exposing other Tunnels or destructive actions.</li>
<li>Grant a write role on a specific Cloudflare Mesh node to an application team — without giving them access to the rest of your private network.</li>
<li>Scope a single policy to one or many Tunnels and Mesh nodes at once.</li>
</ul>
<h4 id="2026-05-21-tunnel-mesh-granular-permissions-how-it-works">How it works</h4>
<p>Granular permissions are a parallel layer to existing account-level roles — they do not replace them.</p>
<ul>
<li><strong>Existing account-level roles continue to work.</strong> A member with <code>Cloudflare Access</code> or <code>Cloudflare Zero Trust</code> retains write access to every Tunnel and Mesh node in the account. This ensures backward compatibility for existing automation and tokens.</li>
<li><strong>Granular permissions are additive.</strong> For any API request on a specific Tunnel or Mesh node, access is granted if the principal has <strong>either</strong> the account-level role <strong>or</strong> a granular permission for that resource.</li>
<li><strong>Resource enumeration is authorization-aware.</strong> Listing endpoints (<code>GET /accounts/{id}/cfd_tunnel</code>, <code>GET /accounts/{id}/warp_connector</code>) return only the resources the principal has at least read access to.</li>
</ul>
<h4 id="2026-05-21-tunnel-mesh-granular-permissions-get-started">Get started</h4>
<ul>
<li>Configure <a href="/tunnel/guides/granular-permissions/">granular permissions for Cloudflare Tunnel</a>.</li>
<li>Configure <a href="/cloudflare-one/networks/connectors/granular-permissions/">granular permissions for Cloudflare Tunnel and Cloudflare Mesh in Cloudflare One</a>.</li>
<li>Review the <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">resource-scoped roles</a> on the Cloudflare role reference.</li>
</ul>


<h2 id="2026-05-19">2026-05-19</h2>

<strong>Cloudflare as identity provider and account membership selector</strong>

<p>Cloudflare Access now supports using Cloudflare itself as an <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">identity provider</a>. If you publish an Access application and select Cloudflare as the login method, users can sign in with their existing Cloudflare account — no one-time PINs, no third-party IdP configuration, and no shared email inboxes. Authentication is backed by Cloudflare's own account security (including multi-factor authentication), making it both simpler to set up and more secure than OTP-based login for most use cases.</p>
<p>Cloudflare is now the <strong>default identity provider for all newly created Zero Trust accounts</strong>, replacing One-time PIN.</p>
<p>This also enables two new capabilities:</p>
<ul>
<li><strong>Cloudflare Account Member selector</strong> — A new <a href="/cloudflare-one/access-controls/policies/#cloudflare-access-selectors">policy selector</a> that matches users based on their membership in a Cloudflare account. You can target the current account or specify a different account ID for cross-account access scenarios.</li>
<li><strong>Restrict to account members</strong> — An identity provider configuration option that limits authentication to users who are members of your Cloudflare account.</li>
</ul>
<p>To get started, add Cloudflare as an <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">identity provider</a> in your Zero Trust settings.</p>


<h2 id="2026-05-19-1">2026-05-19</h2>

<strong>CASB adds support for Claude Compliance API</strong>

<p><a href="/cloudflare-one/integrations/cloud-and-saas/anthropic/">Cloudflare CASB</a> now integrates with the <a href="https://support.claude.com/en/articles/13015708-access-the-compliance-api">Claude Compliance API</a>. This enhancement gives security teams visibility into Claude usage patterns, admin activity, and compliance-relevant events across their organization.</p>
<p>The Claude Compliance API provides structured access to audit logs and administrative actions within Claude Enterprise and Claude Platform. Cloudflare CASB ingests this data to surface security findings that help organizations enhance their security posture and enforce AI governance.</p>
<h4 id="2026-05-19-casb-claude-compliance-api-key-capabilities">Key capabilities</h4>
<p>Starting today, security teams can scan for security findings across the following assets:</p>
<ul>
<li><strong>Public projects</strong> — Projects set to public visibility</li>
<li><strong>Project attachment</strong> — Files and documents added to projects that violate DLP policies</li>
<li><strong>Chat files</strong> — User-uploaded and provider-generated files that violate DLP policies</li>
<li><strong>Chat messages</strong> — User prompts and provider responses that violate DLP policies</li>
<li><strong>Artifacts</strong> — Provider-generated documents and files that violate DLP policies</li>
</ul>
<h4 id="2026-05-19-casb-claude-compliance-api-learn-more">Learn more</h4>
<p>This <a href="/cloudflare-one/integrations/cloud-and-saas/anthropic/">integration</a> is available to all Cloudflare One customers. New Cloudflare customers can sign up and start with their first two integrations for free. Existing customers can enable the integration directly in the dashboard. The integration begins scanning immediately and surfaces findings in the dashboard within minutes.</p>


<h2 id="2026-05-18">2026-05-18</h2>

<strong>Network Analytics support for Unified Routing</strong>

<p><a href="/analytics/network-analytics/">Network Analytics</a> is now fully supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. Traffic that traverses Unified Routing onramps and offramps is now visible in Network Analytics with the same dimensions and filters as traffic on the standard data plane.</p>
<p>This closes a parity gap for customers who had moved tunnels onto Unified Routing and lost visibility into their dataplane traffic in the Network Analytics dashboard. No configuration change is required — analytics data is collected automatically for all accounts with Unified Routing enabled.</p>
<p>For the remaining beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<h2 id="2026-05-12">2026-05-12</h2>

<strong>Refreshed Access login page</strong>

<p>The <a href="/cloudflare-one/reusable-components/custom-pages/access-login-page/">Access login page</a> and <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time password (OTP)</a> page now feature a refreshed design that improves visual consistency, user trust, and mobile responsiveness.</p>
<p><strong>Before:</strong></p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-login-old.png" alt="Screenshot of the previous Access login page" /></p>
<p><strong>After:</strong></p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-login-new.png" alt="Screenshot of the updated Access login page" /></p>
<p>The updated login experience includes:</p>
<ul>
<li><strong>Unified authentication card</strong> - All sign-in options (identity provider buttons, email input, OTP) now appear in a single card with consistent styling, replacing the previous multi-section layout.</li>
<li><strong>Consistent button styling</strong> - Identity provider buttons use a uniform size and layout for easier scanning and selection.</li>
<li><strong>Better mobile experience</strong> - Responsive layout improvements ensure the login page renders correctly on phones and tablets.</li>
<li><strong>Dark mode support</strong> - The login page now supports dark mode.</li>
</ul>


<h2 id="2026-05-12-1">2026-05-12</h2>

<strong>New accounts assigned a single IPv4 anycast address</strong>

<p>New Magic Transit and Cloudflare WAN accounts are now assigned a single IPv4 anycast address by default.</p>
<p>Cloudflare handles failures on its network automatically by advertising your endpoint IP from multiple nodes across many globally distributed data centers. To handle failures on your network, configure two tunnels from separate routers.</p>
<p>To request additional anycast IP addresses for your account, contact your account team.</p>
<p>For tunnel configuration guidance, refer to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a> for Cloudflare WAN or <a href="/magic-transit/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a> for Magic Transit.</p>


<h2 id="2026-05-12-2">2026-05-12</h2>

<strong>Create Gateway firewall policies with natural language</strong>

<p>Cloudflare Gateway now supports natural language policy creation for <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS</a>, <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a>, and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> firewall policies. Administrators can describe the outcome they want in plain language, and Cloudflare will generate a complete policy rule that populates the policy builder form.</p>
<p><img src="/assets/upstream/images/changelog/gateway/gateway-create-with-ai.png" alt="Create with AI button on the Gateway firewall policies page" /></p>
<p>To create a policy with natural language, select <strong>Create with AI</strong> on any Gateway firewall policy tab. Choose a policy type, describe what the policy should do, and a fully configured rule will appear in the policy builder for review. You can edit any field before saving, or re-generate with a different prompt.</p>
<p>The generated policy incorporates your account context - including lists, DLP profiles, applications, and device posture checks - so that references to your existing resources resolve automatically.</p>
<p>A built-in feedback mechanism allows you to rate each generated policy and provide optional comments, which Cloudflare uses to improve output quality over time.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/">Gateway firewall policies</a>.</p>


<h2 id="2026-05-12-3">2026-05-12</h2>

<strong>Cloudflare One Client for Linux (version 2026.4.1350.0)</strong>

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
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Split tunnel list configuration is not available in the new UI. Management of split tunnel entries is currently only possible via <code>warp-cli tunnel ip</code> and <code>warp-cli tunnel host</code>. UI support will be added in a future release.</li>
</ul>


<h2 id="2026-05-12-4">2026-05-12</h2>

<strong>Cloudflare One Client for macOS (version 2026.4.1350.0)</strong>

<p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces the new Cloudflare One Client UI for macOS! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
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


<h2 id="2026-05-12-5">2026-05-12</h2>

<strong>Cloudflare One Client for Windows (version 2026.4.1350.0)</strong>

<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces the new Cloudflare One Client UI for Windows! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
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


<h2 id="2026-05-11">2026-05-11</h2>

<strong>NAT-T support for IKE on UDP port 500</strong>

<p>Cloudflare IPsec now supports the standard NAT traversal (NAT-T) flow, where IKE begins on UDP port <code>500</code> and switches to UDP port <code>4500</code> after NAT is detected.</p>
<p>Previously, devices behind NAT had to be configured to initiate IKE on UDP port <code>4500</code> directly. Devices that started on UDP port <code>500</code> could not complete the IKE handshake when NAT was in the path. This required custom configuration on devices such as VeloCloud SD-WAN edges, Cisco IOS-XE routers, and Juniper SRX firewalls, and was not possible on every platform.</p>
<p>What changed:</p>
<ul>
<li>Devices behind NAT can now initiate IKE on either UDP port <code>500</code> or UDP port <code>4500</code>.</li>
<li>Devices that start IKE on UDP port <code>500</code> and switch to UDP port <code>4500</code> after NAT detection now complete the handshake successfully.</li>
<li>No configuration change is required on Cloudflare. The change is available for all IPsec tunnels on Cloudflare WAN and Magic Transit.</li>
</ul>
<p>This change does not affect existing tunnels:</p>
<ul>
<li>Tunnels using UDP port <code>500</code> with no NAT detected continue to operate as before.</li>
<li>Tunnels configured to start IKE on UDP port <code>4500</code> continue to operate as before.</li>
<li>NAT detection logic is unchanged.</li>
</ul>
<p>For configuration details, refer to <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/">GRE and IPsec tunnels</a>.</p>


<h2 id="2026-05-07">2026-05-07</h2>

<strong>Custom DHCP options on Cloudflare One Appliance</strong>

<p>When the Cloudflare One Appliance is acting as the DHCP server for a LAN, you can now configure custom DHCP options on the leases it issues. This unlocks workflows such as PXE / iPXE boot, VoIP phone provisioning, and vendor-specific client configuration.</p>
<p>Each option is defined by <code>option_number</code>, <code>value</code>, and one of four value types: <code>text</code>, <code>integer</code>, <code>hex</code>, or <code>ip</code>. Configurations are validated on the appliance before being applied — invalid configurations are rejected and the underlying error is returned to the API caller, so a bad option will not disrupt the live DHCP service.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">DHCP server options</a>.</p>


<h2 id="2026-05-07-1">2026-05-07</h2>

<strong>Source-based breakout and prioritization on Cloudflare One Appliance</strong>

<p>Breakout and traffic prioritization rules on the Cloudflare One Appliance can now match by <strong>source</strong> in addition to destination application. You can pin breakout or priority behavior to:</p>
<ul>
<li>A source LAN interface — VLANs attached to that LAN are included automatically.</li>
<li>A source IP address, range, or CIDR block.</li>
</ul>
<p>This is the natural way to break out a guest VLAN to the local Internet, or to prioritize traffic from a specific subnet, without enumerating destination applications.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source">Breakout traffic</a>.</p>


<h2 id="2026-05-07-2">2026-05-07</h2>

<strong>Self-serve provisioning of Cloudflare One Virtual Appliance via API</strong>

<p>You can now create, rotate, and delete Cloudflare One Virtual Appliance instances and their license keys directly via the API and Terraform.</p>
<ul>
<li>Create a virtual appliance and receive a license key: <code>POST /accounts/{account_id}/magic/connectors</code> with <code>device.provision_license: true</code>.</li>
<li>Rotate the license key for an existing virtual appliance: <code>PATCH /accounts/{account_id}/magic/connectors/{connector_id}</code> with <code>provision_license: true</code>. The previous key is immediately and irrevocably revoked.</li>
<li>Delete a virtual appliance to release the associated licensed device.</li>
</ul>
<p>The license key is returned in the response only once, at create or rotate time. Copy and store it securely.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a Cloudflare One Virtual Appliance</a>.</p>


<h2 id="2026-05-07-3">2026-05-07</h2>

<strong>Cloudy Summaries in PhishNet O365</strong>

<p>PhishNet users can now access <strong>Cloudy summaries</strong> directly within the email investigation experience. When reviewing a message in PhishNet, users will see an AI-generated summary that provides additional context and key details about the email.</p>
<p>These summaries help users quickly understand the nature of a message without needing to manually parse through headers, body content, and detection signals. Cloudy surfaces the most relevant information so users can make faster, more informed decisions about suspicious emails.</p>
<p><strong>These summaries are not trained on customer data.</strong> They are generated using the outputs of our existing detection models and analysis systems.</p>
<p>This feature is available for PhishNet with Office 365. Support for Gmail will be available by the end of the quarter.</p>


<h2 id="2026-05-06">2026-05-06</h2>

<strong>IPv6 CIDR routes for Cloudflare Mesh</strong>

<p><a href="/mesh/">Cloudflare Mesh</a> nodes now support IPv6 CIDR routes. You can advertise both IPv4 and IPv6 subnets through your Mesh nodes, making IPv6-only or dual-stack private networks reachable from any enrolled device.</p>
<p><img src="/assets/upstream/images/cloudflare-one/connections/mesh-ipv6-routes.png" alt="IPv6 CIDR routes on a Mesh node in the Cloudflare dashboard" /></p>
<p>To add an IPv6 route, follow the same steps as <a href="/mesh/features/routes/#add-a-route">adding an IPv4 route</a> — enter the IPv6 CIDR (for example, <code>fd00::/64</code>) when configuring the route in the <a href="https://dash.cloudflare.com/?to=/:account/mesh">dashboard</a> or via the API.</p>


<h2 id="2026-04-30">2026-04-30</h2>

<strong>Post-quantum IPsec interoperability with third-party devices</strong>

<p>Cloudflare IPsec now supports post-quantum key agreement with compatible third-party devices. <a href="https://www.cisco.com/">Cisco</a> and <a href="https://www.fortinet.com/">Fortinet</a> are the first third-party vendors validated to interoperate with Cloudflare IPsec using ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).</p>
<p>Post-quantum IPsec uses <a href="https://datatracker.ietf.org/doc/rfc9370/">RFC 9370</a> and <a href="https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/">draft-ietf-ipsecme-ikev2-mlkem</a> to negotiate hybrid key agreement during the IKEv2 <code>IKE_INTERMEDIATE</code> phase. This combines classical Diffie-Hellman (Group 20) with ML-KEM-768 or ML-KEM-1024 to protect against <a href="https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later">harvest-now, decrypt-later</a> attacks.</p>
<p>Key details:</p>
<ul>
<li>Compatible with Cisco 8000 Series Secure Routers with IOS XR Release 26.1.1 and Fortinet FortiOS 7.6.6 and later.</li>
<li>Uses ML-KEM-768 or ML-KEM-1024 as an additional Key Exchange to DH Group 20.</li>
<li>Follows RFC 9370 and draft-ietf-ipsecme-ikev2-mlkem standards.</li>
<li>No additional licensing required.</li>
</ul>
<p>Post-quantum IPsec with third-party devices is now generally available with confirmed interoperability for the platforms listed above. Cloudflare intends to support interoperability with more vendors as they build out support for draft-ietf-ipsecme-ikev2-mlkem. Contact your account team to discuss support for additional vendors.</p>
<p>For supported key exchange methods and the list of validated platforms, refer to <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/#tested-third-party-vendor-interoperability">GRE and IPsec tunnels</a>.</p>


<h2 id="2026-04-30-1">2026-04-30</h2>

<strong>Classify sensitive content with Data Classification</strong>

<p>Cloudflare DLP now includes <strong>Data Classification</strong>, which lets administrators organize and label sensitive content using labels, templates, and reusable data classes.</p>
<p>With Data Classification, administrators can define labels such as sensitivity schemas and levels, and data tag groups and tags. Administrators can also build from Cloudflare-managed templates and create reusable data classes that combine detection entries, other data classes, sensitivity levels, and data tags.</p>
<p>You can then use those classifications in custom DLP profiles to identify the severity of sensitive content, understand where it exists, and apply that logic consistently across DLP profiles.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/data-classification/">Data Classification</a>.</p>


<h2 id="2026-04-30-2">2026-04-30</h2>

<strong>New predefined detection entries are available</strong>

<p>Cloudflare DLP now includes new predefined detection entries.</p>
<p>The expanded catalog includes detections for specific credential types, webhooks, addresses, tax identifiers, national IDs, financial data, and crypto wallets.</p>
<p>Examples include <code>GitHub PAT</code>, <code>OpenAI API Key</code>, <code>Slack Webhook</code>, <code>Discord Webhook</code>, <code>US Physical Address</code>, and <code>Bitcoin Wallet</code>.</p>
<p>For the full list, refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/predefined-detection-entries/">Predefined detection entries</a>.</p>


<h2 id="2026-04-29">2026-04-29</h2>

<strong>Digital experience tests to authenticated resources and enhanced configuration</strong>

<p><a href="/cloudflare-one/insights/dex/tests/">Digital experience tests</a> now support testing applications protected by Cloudflare Access or third-party authentication. All authentication secrets are managed via <a href="/secrets-store/">Cloudflare Secret Store</a>.</p>
<p>Digital experience tests also have enhanced configuration options including:</p>
<ul>
<li>New HTTP methods (DELETE, PATCH, POST, PUT)</li>
<li>Secret Store headers, custom plain text headers, and custom request bodies</li>
<li>Advanced settings: follow redirects, response bodies, response headers, and allow untrusted certificates</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dex/dex_test_auth_config.png" alt="Digital experience test configuration for Cloudflare Access applications" />
<img src="/assets/upstream/images/changelog/dex/dex_test_enhanced_config.png" alt="Digital experience enhanced test configuration" /></p>


<h2 id="2026-04-29-1">2026-04-29</h2>

<strong>Gateway Authorization Proxy and hosted PAC files are now generally available</strong>

<p>The <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">Gateway Authorization Proxy</a> and <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file">hosted PAC files</a> are now generally available for all plan types.</p>
<p>Authorization proxy endpoints add an identity-aware option alongside the existing <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint">source IP proxy endpoints</a>, using <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> authentication to verify who a user is before applying Gateway filtering — without installing the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>. Cloudflare-hosted PAC files let you create and distribute PAC files directly from Cloudflare One on Cloudflare's global network.</p>
<p>These features are ideal for environments where deploying a device client is not an option, such as virtual desktops (VDI) or compliance-restricted endpoints.</p>
<p>To get started, refer to the <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints documentation</a>.</p>


<h2 id="2026-04-28">2026-04-28</h2>

<strong>Internet outage notifications for devices</strong>

<p><a href="/cloudflare-one/insights/dex/">Digital Experience</a> will display a dashboard notification when an Internet outage or traffic anomaly may impact a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> device based on its geographic location or network connection.</p>
<p>This Internet outage and traffic anomaly data is pulled from <a href="https://radar.cloudflare.com/">Cloudflare Radar</a>. All Internet outage and traffic anomaly observations can be viewed in the <a href="https://radar.cloudflare.com/outage-center">Radar Outage Center</a>.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_radar_ux_notification.png" alt="Digital Experience Monitoring dashboard notification for Internet outage impacting Cloudflare One Client devices" />
<img src="/assets/upstream/images/changelog/dex/dex_radar_analytics.png" alt="Digital Experience Monitoring dashboard analytics for Internet outage impacting Cloudflare One Client devices" /></p>


<h2 id="2026-04-28-1">2026-04-28</h2>

<strong>Cloudflare One Client speed tests</strong>

<p>IT teams can now remotely run speed tests from the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> to Cloudflare's network edge.</p>
<p>Each speed test includes the following metrics:</p>
<ul>
<li>Internet speed: download and upload throughput</li>
<li>Latency: download, upload, unloaded latency, and jitter</li>
<li>Network quality score: video streaming, webchat/real-time communication (RTC)</li>
</ul>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Digital experience</strong> &gt; <strong>Diagnostics</strong> and select <strong>Run diagnostics</strong> to use the feature today.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_speed_test.png" alt="Cloudflare One client speed test result" /></p>


<h2 id="2026-04-28-2">2026-04-28</h2>

<strong>Create and manage DLP detection entries outside of profiles</strong>

<p>You can now create, view, and manage DLP detection entries outside of profiles.</p>
<p>Detection entries are no longer hidden inside individual profiles. Administrators can manage detection entries directly from the <strong>Detection entries</strong> section and use them in custom DLP profiles.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/">Configure detection entries</a>.</p>


<h2 id="2026-04-28-3">2026-04-28</h2>

<strong>Detect PII records with a new predefined DLP profile</strong>

<p>Cloudflare DLP now includes a new predefined profile designed to detect PII records that contain multiple types of personal data: <strong>Personally Identifiable Information (PII) Record</strong>.</p>
<p>Most predefined and custom DLP profiles match when any enabled detection entry matches. The <strong>Personally Identifiable Information (PII) Record</strong> profile is different. It only matches when at least three unique detection entries are found in close proximity, which reduces false positives from standalone values that may not represent a real PII record.</p>
<p>Detection entries included in the profile:</p>
<ul>
<li>AU Passport Number</li>
<li>American Express Card Number</li>
<li>Diners Club Card Number</li>
<li>US Driver's License Number</li>
<li>Email Address</li>
<li>Full Name</li>
<li>US Mailing Address</li>
<li>Mastercard Card Number</li>
<li>US Individual Tax Identification Number (ITIN)</li>
<li>US Passport Number</li>
<li>US Phone Number</li>
<li>Union Pay Card Number</li>
<li>United States SSN Numeric Detection</li>
<li>Visa Card Number</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">predefined DLP profiles</a>.</p>


<h2 id="2026-04-24">2026-04-24</h2>

<strong>Network Session Logs now available for all on-ramps</strong>

<p><a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a> are now generated for all traffic proxied through Cloudflare Gateway, regardless of on-ramp type. This includes traffic from <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints (PAC files)</a> and <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> egress — on-ramps that previously did not generate session logs.</p>
<p>Customers who already consume the <code>zero_trust_network_sessions</code> dataset via <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a> or <a href="/log-explorer/">Log Explorer</a> may see increased log volume if they use these on-ramps.</p>
<p>For field definitions, refer to <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a>. For traffic analysis, refer to <a href="/cloudflare-one/insights/analytics/network-sessions/">Network session analytics</a>.</p>


<h2 id="2026-04-23">2026-04-23</h2>

<strong>AAGUID restrictions and AMR matching for Access independent MFA</strong>

<p><a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">Independent MFA</a> in Cloudflare Access now supports two additional organization-level controls:</p>
<ul>
<li><strong><a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#restrict-authenticators-by-aaguid">Restrict authenticators by AAGUID</a></strong> — Limit enrollment to a specific set of WebAuthn authenticators using their <a href="https://fidoalliance.org/specs/fido-v2.0-id-20180227/fido-registry-v2.0-id-20180227.html#authenticator-attestation-guid">AAGUID</a>. This is useful for organizations that require FIPS-validated security keys or company-issued hardware. AAGUIDs are managed through a new <a href="/cloudflare-one/reusable-components/lists/">List</a> type.</li>
<li><strong><a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#use-identity-provider-mfa">AMR matching</a></strong> — Skip the independent MFA prompt when the identity provider has already performed an equivalent MFA. Access reads the <code>amr</code> claim defined in <a href="https://datatracker.ietf.org/doc/html/rfc8176">RFC 8176</a> and matches supported values such as <code>hwk</code>, <code>otp</code>, and <code>fpt</code> to the authenticator types allowed on the application or policy. This prevents users from having to complete MFA twice when their identity provider already enforces it.</li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">Independent MFA</a>.</p>


<h2 id="2026-04-21">2026-04-21</h2>

<strong>Country rules supported in Unified Routing</strong>

<p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> Country rules are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. This feature requires a Cloudflare Advanced Network Firewall subscription.</p>
<p>You can create firewall rules that match traffic based on source or destination country to enforce geographic access policies across your network.</p>
<p>This is the first of the Cloudflare Advanced Network Firewall features to become available in Unified Routing. Support for additional features - IP Lists, ASN Lists, Threat Intel Lists, IDS, Rate Limiting, SIP, and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<h2 id="2026-04-20">2026-04-20</h2>

<strong>Network session analytics dashboard</strong>

<p>The new <a href="/cloudflare-one/insights/analytics/network-sessions/">Network session analytics</a> dashboard is now available in Cloudflare One. This dashboard provides visibility into your network traffic patterns, helping you understand how traffic flows through your Cloudflare One infrastructure.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/cf1-network-session-analytics.png" alt="Cloudflare One Network Session Analytics" /></p>
<h4 id="2026-04-20-network-session-analytics-what-you-can-do-with-network-session-analytics">What you can do with Network session analytics</h4>
<ul>
<li><strong>Analyze geographic distribution</strong>: View a world map showing where your network traffic originates, with a list of top locations by session count.</li>
<li><strong>Monitor key metrics</strong>: Track session count, total bytes transferred, and unique users.</li>
<li><strong>Identify connection issues</strong>: Analyze connection close reasons to troubleshoot network problems.</li>
<li><strong>Review protocol usage</strong>: See which network protocols (TCP, UDP, ICMP) are most used.</li>
</ul>
<h4 id="2026-04-20-network-session-analytics-dashboard-features">Dashboard features</h4>
<ul>
<li><strong>Summary metrics</strong>: Session count, bytes total, and unique users</li>
<li><strong>Traffic by location</strong>: World map visualization and location list with top traffic sources</li>
<li><strong>Top protocols</strong>: Breakdown of TCP, UDP, ICMP, and ICMPv6 traffic</li>
<li><strong>Connection close reasons</strong>: Insights into why sessions terminated (client closed, origin closed, timeouts, errors)</li>
</ul>
<h4 id="2026-04-20-network-session-analytics-how-to-access">How to access</h4>
<ol>
<li>Log in to <a href="https://dash.cloudflare.com">Cloudflare One</a>.</li>
<li>Go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Dashboards</strong>.</li>
<li>Select <strong>Network session analytics</strong>.</li>
</ol>
<p>For more information, refer to the <a href="/cloudflare-one/insights/analytics/network-sessions/">Network session analytics documentation</a>.</p>


<h2 id="2026-04-17">2026-04-17</h2>

<strong>Homepage and sign-out for MCP server portals</strong>

<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> display a homepage when users visit the portal domain in a browser.</p>
<p><img src="/assets/upstream/images/changelog/access/portals-homepage-disconnected.png" alt="MCP server portal homepage showing connection status and setup instructions" /></p>
<p>The homepage shows:</p>
<ul>
<li>The portal name and organization branding</li>
<li>The MCP endpoint URL with a copy button</li>
<li>Per-client connection instructions for Claude Desktop, Workers AI Playground, OpenCode, Windsurf, and other MCP clients</li>
</ul>
<p>Authenticated users see their email address and a <strong>Sign out</strong> button. Selecting <strong>Sign out</strong> revokes all portal-level OAuth grants, deletes upstream server OAuth states, and redirects through Cloudflare Access logout. A confirmation page shows a summary of the revoked sessions.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#portal-homepage">MCP server portals</a>.</p>


<h2 id="2026-04-15">2026-04-15</h2>

<strong>Independent MFA for Access applications</strong>

<p>Cloudflare Access now supports independent multi-factor authentication (MFA), allowing you to enforce MFA requirements without relying on your identity provider (IdP). With per-application and per-policy configuration, you can enforce stricter authentication methods like hardware security keys on sensitive applications without requiring them across your entire organization. This reduces the risk of MFA fatigue for your broader user population while adding additional security where it matters most.</p>
<p>This feature also addresses common gaps in IdP-based MFA, such as inconsistent MFA policies across different identity providers or the need for additional security layers beyond what the IdP provides.</p>
<p>Independent MFA supports the following authenticator types:</p>
<ul>
<li><strong>Authenticator application</strong> — Time-based one-time passwords (TOTP) using apps like Google Authenticator, Microsoft Authenticator, or Authy.</li>
<li><strong>Security key</strong> — Hardware security keys such as YubiKeys.</li>
<li><strong>Biometrics</strong> — Built-in device authenticators including Apple Touch ID, Apple Face ID, and Windows Hello.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17620.md")</aside>
<h4 id="2026-04-15-independent-mfa-configuration-levels">Configuration levels</h4>
<p>You can configure MFA requirements at three levels:</p>
<table>
<thead>
<tr>
<th>Level</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Organization</strong></td>
<td>Enforce MFA by default for all applications in your account.</td>
</tr>
<tr>
<td><strong>Application</strong></td>
<td>Require or turn off MFA for a specific application.</td>
</tr>
<tr>
<td><strong>Policy</strong></td>
<td>Require or turn off MFA for users who match a specific policy.</td>
</tr>
</tbody>
</table>
<p>Settings at lower levels (policy) override settings at higher levels (organization), giving you granular control over MFA enforcement.</p>
<h4 id="2026-04-15-independent-mfa-user-enrollment">User enrollment</h4>
<p>Users enroll their authenticators through the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a>. To help with onboarding, administrators can share a direct enrollment link: <code>&lt;your-team-name&gt;.cloudflareaccess.com/AddMfaDevice</code>.</p>
<p>To get started with Independent MFA, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">Independent MFA</a>.</p>


<h2 id="2026-04-15-1">2026-04-15</h2>

<strong>New, streamlined creation experience for Access Applications and Gateway Policies</strong>

<p>The Cloudflare One dashboard now features redesigned builders for two core workflows: creating Gateway policies and configuring self-hosted Access applications.</p>
<h4 id="2026-04-15-new-rule-and-application-builders-gateway-rule-builder">Gateway rule builder</h4>
<p>The Gateway rule builder now features a redesigned user experience, bringing it in line with the Access policy builder experience. Improvements include:</p>
<ul>
<li><strong>Streamlined UX</strong> with clearer states and improved user interactions</li>
<li><strong>Wirefilter editing</strong> for viewing and editing Gateway rules directly from wirefilter expressions</li>
<li><strong>Preview state</strong> to review the impact of your policy in a simple graphic</li>
</ul>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/gateway-rule-builder.png" alt="New Gateway rule builder" /></p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/">Traffic policies</a>.</p>
<h4 id="2026-04-15-new-rule-and-application-builders-access-application-builder-for-self-hosted-apps">Access application builder for self-hosted apps</h4>
<p>The self-hosted Access application builder now offers a simplified creation workflow with fewer steps from setup to save. Improvements include:</p>
<ul>
<li><strong>New application selection experience</strong> that makes choosing the right application type before you begin easier.</li>
<li><strong>Streamlined creation flow</strong> with fewer clicks to build and save an application</li>
<li><strong>Inline policy creation</strong> for building Access policies directly within the application creation flow</li>
<li><strong>Preview state</strong> to understand how your policies enforce user access before saving</li>
</ul>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-application-builder.png" alt="New Access application builder" /></p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/">self-hosted applications</a>.</p>


<h2 id="2026-04-15-2">2026-04-15</h2>

<strong>Last seen timestamp for Cloudflare One Client devices is more consistent</strong>

<p>The last seen timestamp for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> devices is now more consistent across the dashboard. IT teams will see more consistent information about the most recent client event between a device and Cloudflare's network.</p>


<h2 id="2026-04-14">2026-04-14</h2>

<strong>DLP account-level settings</strong>

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


<h2 id="2026-04-14-1">2026-04-14</h2>

<strong>Introducing Cloudflare Mesh</strong>

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


<h2 id="2026-04-14-2">2026-04-14</h2>

<strong>Detect Cloudflare API tokens with DLP</strong>

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


<h2 id="2026-04-14-3">2026-04-14</h2>

<strong>Configure how sensitive data appears in DLP payload logs</strong>

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


<h2 id="2026-04-10">2026-04-10</h2>

<strong>Canvas Remoting optimizes performance for productivity applications</strong>

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


<h2 id="2026-04-09">2026-04-09</h2>

<strong>Send CASB posture finding instances with webhooks</strong>

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


<h2 id="2026-04-08">2026-04-08</h2>

<strong>User risk scoring for high risk browsing activity</strong>

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


<h2 id="2026-04-08-1">2026-04-08</h2>

<strong>Cloudflare One Client for Windows (version 2026.3.851.0)</strong>

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


<h2 id="2026-04-07">2026-04-07</h2>

<strong>User Submission Triage Status Tracking</strong>

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


<h2 id="2026-04-07-1">2026-04-07</h2>

<strong>Link aggregation (LACP) support for Cloudflare One Appliance</strong>

<p>Cloudflare One Appliance now supports Link Aggregation Control Protocol (LACP), allowing you to bundle up to six physical LAN ports into a single logical interface. Link aggregation increases available bandwidth and eliminates single points of failure on the LAN side of the appliance.</p>
<p>This feature is available in beta on physical appliance hardware with the latest OS. No entitlement is required.</p>
<p>To configure a Link Aggregation Group, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/link-aggregation/">Configure link aggregation groups</a>.</p>


<h2 id="2026-04-06">2026-04-06</h2>

<strong>DANE Support for MX Deployments</strong>

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


<h2 id="2026-04-06-1">2026-04-06</h2>

<strong>Organizations is now in public beta for enterprises</strong>

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


<h2 id="2026-04-03">2026-04-03</h2>

<strong>Cloudflare One Client for Linux (version 2026.3.846.0)</strong>

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


<h2 id="2026-04-03-1">2026-04-03</h2>

<strong>Cloudflare One Client for macOS (version 2026.3.846.0)</strong>

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


<h2 id="2026-04-02">2026-04-02</h2>

<strong>Session management for MCP server portals</strong>

<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support in-session management of upstream MCP server connections. Users can return to the server selection page at any time to enable or disable servers, reauthenticate, or change which data a server has access to — all without leaving their MCP client.</p>
<p>To return to the server selection page, ask your AI agent with a prompt like &quot;take me back to the server selection page.&quot; The portal responds with an authorization URL via <a href="https://modelcontextprotocol.io/specification/2025-03-26/server/elicitation">MCP elicitation</a> that you open in your browser:</p>
<pre tabindex="0"><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/authorize?elicitationId=&lt;ELICITATION_ID&gt;&#10;</code></pre>
<p>From the server selection page you can:</p>
<ul>
<li><strong>Enable or disable servers</strong> — Toggle individual upstream MCP servers on or off. Disabling a server removes its tools from the active session, which reduces context window usage.</li>
<li><strong>Log out and reauthenticate</strong> — Log out of a server and log back in to change which data the server has access to, or to reauthenticate with different permissions.</li>
</ul>
<p>Users can also enable or disable a server inline by asking their AI agent directly, for example &quot;enable the wiki server&quot; or &quot;disable my Jira server.&quot;</p>
<p>The portal also automatically prompts connected users to authorize new servers when an admin adds them to the portal. This requires the use of <a href="/cloudflare-one/access-controls/applications/http-apps/managed-oauth/#enable-managed-oauth-on-an-mcp-server-portal">managed OAuth</a>.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#manage-portal-sessions">Manage portal sessions</a>.</p>


<h2 id="2026-04-01">2026-04-01</h2>

<strong>Logs UI refresh</strong>

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


<h2 id="2026-03-26">2026-03-26</h2>

<strong>Code Mode for MCP server portals</strong>

<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support <a href="/agents/model-context-protocol/codemode/">Code Mode MCP server patterns</a>, a technique that reduces context window usage by replacing individual tool definitions with a single code execution tool. Code Mode is turned on by default on all portals.</p>
<p>To turn it off, edit the portal in <strong>Access controls</strong> &gt; <strong>AI controls</strong> and turn off <strong>Code Mode</strong> under <strong>Basic information</strong>.</p>
<p>When Code Mode is active, the portal exposes a single <code>code</code> tool instead of listing every tool from every upstream MCP server. The connected AI agent writes JavaScript that calls typed <code>codemode.*</code> methods for each upstream tool. The generated code runs in an isolated <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a> environment, keeping authentication credentials and environment variables out of the model context.</p>
<p>To use Code Mode, append <code>?codemode=search_and_execute</code> to your portal URL when connecting from an MCP client:</p>
<pre tabindex="0"><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?codemode=search_and_execute&#10;</code></pre>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode">Code Mode</a>.</p>


<h2 id="2026-03-26-1">2026-03-26</h2>

<strong>Context optimization for MCP server portals</strong>

<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support two context optimization options that reduce how many tokens tool definitions consume in the model's context window. Both options are activated by appending the <code>optimize_context</code> query parameter to the portal URL.</p>
<h4 id="2026-03-26-mcp-portal-context-optimization-minimize-tools"><code>minimize_tools</code></h4>
<p>Strips tool descriptions and input schemas from all upstream tools, leaving only their names. The portal exposes a special <code>query</code> tool that agents use to retrieve full definitions on demand. This provides up to 5x savings in token usage.</p>
<pre tabindex="0"><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?optimize_context=minimize_tools&#10;</code></pre>
<h4 id="2026-03-26-mcp-portal-context-optimization-search-and-execute"><code>search_and_execute</code></h4>
<p>Hides all upstream tools and exposes only two tools: <code>query</code> and <code>execute</code>. The <code>query</code> tool searches and retrieves tool definitions. The <code>execute</code> tool runs the upstream tools in an isolated <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a> environment. This reduces the initial token cost to a small constant, regardless of how many tools are available through the portal.</p>
<pre tabindex="0"><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?optimize_context=search_and_execute&#10;</code></pre>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#optimize-context">Optimize context</a>.</p>


<h2 id="2026-03-26-2">2026-03-26</h2>

<strong>Streaming ZIP file scanning removes per-file size limits</strong>

<p>DLP now processes ZIP files using a streaming handler that scans archive contents element-by-element as data arrives. This removes previous file size limitations and improves memory efficiency when scanning large archives.</p>
<p>Microsoft Office documents (DOCX, XLSX, PPTX) also benefit from this improvement, as they use ZIP as a container format.</p>
<p>This improvement is automatic — no configuration changes are required.</p>


<h2 id="2026-03-25">2026-03-25</h2>

<strong>Detect and sanitize HAR files</strong>

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


<h2 id="2026-03-24">2026-03-24</h2>

<strong>OIDC Claims filtering now available in Gateway Firewall, Resolver, and Egress policies</strong>

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


<h2 id="2026-03-20">2026-03-20</h2>

<strong>Managed OAuth for Cloudflare Access</strong>

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


<h2 id="2026-03-20-1">2026-03-20</h2>

<strong>Route MCP server portal traffic through Cloudflare Gateway</strong>

<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> can now route traffic through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> for richer HTTP request logging and data loss prevention (DLP) scanning.</p>
<p>When Gateway routing is turned on, portal traffic appears in your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway HTTP logs</a>. You can create <a href="/cloudflare-one/traffic-policies/">Gateway HTTP policies</a> with <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a> to detect and block sensitive data sent to upstream MCP servers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17619.md")</aside>
<p>To enable Gateway routing, go to <strong>Access controls</strong> &gt; <strong>AI controls</strong>, edit the portal, and turn on <strong>Route traffic through Cloudflare Gateway</strong> under <strong>Basic information</strong>.</p>
<p><img src="/assets/upstream/images/changelog/access/portal-route-through-gateway.png" alt="Route MCP server portal traffic through Cloudflare Gateway" /></p>
<p>For more details, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#route-portal-traffic-through-gateway">Route traffic through Gateway</a>.</p>


<h2 id="2026-03-20-2">2026-03-20</h2>

<strong>Stream logs from multiple replicas of Cloudflare Tunnel simultaneously</strong>

<p>In the Cloudflare One dashboard, the overview page for a specific Cloudflare Tunnel now shows all <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">replicas</a> of that tunnel and supports streaming logs from multiple replicas at once.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-multiconn.gif" alt="View replicas and stream logs from multiple connectors" /></p>
<p>Previously, you could only stream logs from one replica at a time. With this update:</p>
<ul>
<li><strong>Replicas on the tunnel overview</strong> — All active replicas for the selected tunnel now appear on that tunnel's overview page under <strong>Connectors</strong>. Select any replica to stream its logs.</li>
<li><strong>Multi-connector log streaming</strong> — Stream logs from multiple replicas simultaneously, making it easier to correlate events across your infrastructure during debugging or incident response. To try it out, log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> and go to <strong>Networks</strong> &gt; <strong>Connectors</strong> &gt; <strong>Cloudflare Tunnels</strong>. Select <strong>View logs</strong> next to the tunnel you want to monitor.</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel log streams</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/">Deploy replicas</a>.</p>


<h2 id="2026-03-16">2026-03-16</h2>

<strong>Unlimited result paging in Investigations</strong>

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


<h2 id="2026-03-11">2026-03-11</h2>

<strong>WARP client for macOS (version 2026.3.566.1)</strong>

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


<h2 id="2026-03-11-1">2026-03-11</h2>

<strong>WARP client for Windows (version 2026.3.566.1)</strong>

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


<h2 id="2026-03-04">2026-03-04</h2>

<strong>User risk score selector in Access policies</strong>

<p>You can now use <a href="/cloudflare-one/team-and-resources/users/risk-score/">user risk scores</a> in your <a href="/cloudflare-one/access-controls/policies/">Access policies</a>. The new <strong>User Risk Score</strong> selector allows you to create Access policies that respond to user behavior patterns detected by Cloudflare's risk scoring system, including impossible travel, high DLP policy matches, and more.</p>
<p>For more information, refer to <a href="/cloudflare-one/team-and-resources/users/risk-score/#use-risk-scores-in-access-policies">Use risk scores in Access policies</a>.</p>


<h2 id="2026-03-04-1">2026-03-04</h2>

<strong>Gateway Authorization Proxy and hosted PAC files (open beta)</strong>

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


<h2 id="2026-03-02">2026-03-02</h2>

<strong>Copy Cloudflare One resources as JSON or POST requests</strong>

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


<h2 id="2026-03-01">2026-03-01</h2>

<strong>Clipboard controls for browser-based RDP</strong>

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


<h2 id="2026-02-27">2026-02-27</h2>

<strong>Export MCP server portal logs with Logpush</strong>

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


<h2 id="2026-02-27-1">2026-02-27</h2>

<strong>New protocols added for Gateway Protocol Detection (Beta)</strong>

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


<h2 id="2026-02-24">2026-02-24</h2>

<strong>WARP client for Linux (version 2026.1.150.0)</strong>

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


<h2 id="2026-02-24-1">2026-02-24</h2>

<strong>WARP client for macOS (version 2026.1.150.0)</strong>

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


<h2 id="2026-02-24-2">2026-02-24</h2>

<strong>WARP client for Windows (version 2026.1.150.0)</strong>

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


<h2 id="2026-02-20">2026-02-20</h2>

<strong>Understand CASB findings instantly with Cloudy Summaries</strong>

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


<h2 id="2026-02-20-1">2026-02-20</h2>

<strong>Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard</strong>

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


<h2 id="2026-02-19">2026-02-19</h2>

<strong>DEX Supports EU Customer Metadata Boundary</strong>

<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into <a href="/warp-client/">WARP</a> device connectivity and performance to any internal or external application.</p>
<p>Now, all DEX logs are fully compatible with Cloudflare's <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary</a> (CMB) setting for the 'EU' (European Union), which ensures that DEX logs will not be stored outside the 'EU' when the option is configured.</p>
<p>If a Cloudflare One customer using DEX enables CMB 'EU', they will not see any DEX data in the Cloudflare One dashboard. Customers can ingest DEX data via <a href="/logs/logpush/">LogPush</a>, and build their own analytics and dashboards.</p>
<p>If a customer enables CMB in their account, they will see the following message in the Digital Experience dashboard: &quot;DEX data is unavailable because Customer Metadata Boundary configuration is on. Use Cloudflare LogPush to export DEX datasets.&quot;</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_supports_cmb.png" alt="Digital Experience Monitoring message when Customer Metadata Boundary for the EU is enabled" /></p>


<h2 id="2026-02-17">2026-02-17</h2>

<strong>Streamlined clientless browser isolation for private applications</strong>

<p>A new <strong>Allow clientless access</strong> setting makes it easier to connect users without a device client to internal applications, without using public DNS.</p>
<p><img src="/assets/upstream/images/changelog/access/allow-clientless-access.png" alt="Allow clientless access setting in the Cloudflare One dashboard" /></p>
<p>Previously, to provide clientless access to a private hostname or IP without a <a href="/cloudflare-one/networks/routes/add-routes/#add-a-published-application-route">published application</a>, you had to create a separate <a href="/cloudflare-one/access-controls/applications/bookmarks/">bookmark application</a> pointing to a prefixed <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">Clientless Web Isolation</a> URL (for example, <code>https://&lt;your-teamname&gt;.cloudflareaccess.com/browser/https://10.0.0.1/</code>). This bookmark was visible to all users in the App Launcher, regardless of whether they had access to the underlying application.</p>
<p>Now, you can manage clientless access directly within your <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private self-hosted application</a>. When  <strong>Allow clientless access</strong> is turned on, users who pass your Access application policies will see a tile in their App Launcher pointing to the prefixed URL. Users must have <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">remote browser permissions</a> to open the link.</p>


<h2 id="2026-02-17-1">2026-02-17</h2>

<strong>Policies for bookmark applications</strong>

<p>You can now assign <a href="/cloudflare-one/access-controls/policies/">Access policies</a> to <a href="/cloudflare-one/access-controls/applications/bookmarks/">bookmark applications</a>. This lets you control which users see a bookmark in the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a> based on identity, device posture, and other policy rules.</p>
<p>Previously, bookmark applications were visible to all users in your organization. With policy support, you can now:</p>
<ul>
<li><strong>Tailor the App Launcher to each user</strong> — Users only see the applications they have access to, reducing clutter and preventing accidental clicks on irrelevant resources.</li>
<li><strong>Restrict visibility of sensitive bookmarks</strong> — Limit who can view bookmarks to internal tools or partner resources based on group membership, identity provider, or device posture.</li>
</ul>
<p>Bookmarks support all <a href="/cloudflare-one/access-controls/policies/">Access policy configurations</a> except purpose justification, temporary authentication, and application isolation. If no policy is assigned, the bookmark remains visible to all users (maintaining backwards compatibility).</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/applications/bookmarks/">Add bookmarks</a>.</p>


<h2 id="2026-02-17-2">2026-02-17</h2>

<strong>Cloudflare One Product Name Updates</strong>

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


<h2 id="2026-02-13">2026-02-13</h2>

<strong>Fine-grained permissions for Access policies and service tokens</strong>

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


<h2 id="2026-02-12">2026-02-12</h2>

<strong>Anycast IPs displayed on the dashboard</strong>

<p>Cloudflare WAN now displays your Anycast IP addresses directly in the dashboard when you configure IPsec or GRE tunnels.</p>
<p>Previously, customers received their Anycast IPs during onboarding or had to retrieve them with an API call. The dashboard now pre-loads these addresses, reducing setup friction and preventing configuration errors.</p>
<p>No action is required. All Cloudflare WAN customers can see their Anycast IPs in the tunnel configuration form automatically.</p>
<p>For more information, refer to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a>.</p>


<h2 id="2026-02-11">2026-02-11</h2>

<strong>Post-quantum encryption support for Cloudflare One Appliance</strong>

<p>Cloudflare One Appliance version 2026.2.0 adds <a href="/ssl/post-quantum-cryptography/">post-quantum encryption</a> support using hybrid ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).</p>
<p>The appliance now uses TLS 1.3 with hybrid ML-KEM for its connection to the Cloudflare edge. During the TLS handshake, the appliance and the edge share a symmetric secret over the TLS connection and inject it into the ESP layer of IPsec. This protects IPsec data plane traffic against harvest-now, decrypt-later attacks.</p>
<p>This upgrade deploys automatically to all appliances during their configured interrupt windows with no manual action required.</p>
<p>For more information, refer to <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a>.</p>


<h2 id="2026-02-02">2026-02-02</h2>

<strong>Improved Accessibility and Search for Monitoring</strong>

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


<h2 id="2026-01-30">2026-01-30</h2>

<strong>BGP over GRE and IPsec tunnels</strong>

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


<h2 id="2026-01-28">2026-01-28</h2>

<strong>WARP client for macOS (version 2026.1.89.1)</strong>

<p>A new Beta release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Fixed an issue causing failure of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion">local network exclusion</a> feature when configured with a timeout of <code>0</code>.</li>
<li>Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.</li>
</ul>


<h2 id="2026-01-28-1">2026-01-28</h2>

<strong>WARP client for Windows (version 2026.1.89.1)</strong>

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


<h2 id="2026-01-27">2026-01-27</h2>

<strong>Configure Cloudflare source IPs (beta)</strong>

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


<h2 id="2026-01-22">2026-01-22</h2>

<strong>Require Access protection for zones</strong>

<p>You can now require Cloudflare Access protection for all hostnames in your account. When enabled, traffic to any hostname that does not have a matching Access application is automatically blocked.</p>
<p>This deny-by-default approach prevents accidental exposure of internal resources to the public Internet. If a developer deploys a new application or creates a DNS record without configuring an Access application, the traffic is blocked rather than exposed.</p>
<p><img src="/assets/upstream/images/changelog/access/require-cloudflare-access-protection.png" alt="Require Cloudflare Access protection in the dashboard" /></p>
<h4 id="2026-01-22-deny-by-default-for-zones-how-it-works">How it works</h4>
<ul>
<li><strong>Blocked by default</strong>: Traffic to all hostnames in the account is blocked unless an Access application exists for that hostname.</li>
<li><strong>Explicit access required</strong>: To allow traffic, create an Access application with an Allow or Bypass policy.</li>
<li><strong>Hostname exemptions</strong>: You can exempt specific hostnames from this requirement.</li>
</ul>
<p>To turn on this feature, refer to <a href="/cloudflare-one/access-controls/access-settings/require-access-protection/">Require Access protection</a>.</p>


<h2 id="2026-01-22-1">2026-01-22</h2>

<strong>New granular API token permissions for Cloudflare Access</strong>

<p>Three new API token permissions are available for Cloudflare Access, giving you finer-grained control when building automations and integrations:</p>
<ul>
<li><strong>Access: Organizations Revoke</strong> — Grants the ability to <a href="/cloudflare-one/access-controls/access-settings/session-management/#revoke-user-sessions">revoke user sessions</a> in a Zero Trust organization. Use this permission when you need a token that can terminate active sessions without broader write access to organization settings.</li>
<li><strong>Access: Population Read</strong> — Grants read access to the <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM users and groups</a> synced from an identity provider to Cloudflare Access. Use this permission for tokens that only need to read synced user and group data.</li>
<li><strong>Access: Population Write</strong> — Grants write access to the <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM users and groups</a> synced from an identity provider to Cloudflare Access. Use this permission for tokens that need to create or modify synced user and group data.</li>
</ul>
<p>These permissions are scoped at the account level and can be combined with existing Access permissions.</p>
<p>For a full list of available permissions, refer to <a href="/fundamentals/api/reference/permissions/">API token permissions</a>.</p>


<h2 id="2026-01-15">2026-01-15</h2>

<strong>Network Services navigation update</strong>

<p>The Network Services menu structure in Cloudflare's dashboard has been updated to reflect solutions and capabilities instead of product names. This will make it easier for you to find what you need and better reflects how our services work together.</p>
<p>Your existing configurations will remain the same, and you will have access to all of the same features and functionality.</p>
<p>The changes visible in your dashboard may vary based on the products you use. Overall, changes relate to <a href="https://developers.cloudflare.com/magic-transit/">Magic Transit</a>, <a href="https://developers.cloudflare.com/magic-wan/">Magic WAN</a>, and <a href="https://developers.cloudflare.com/cloudflare-network-firewall/">Magic Firewall</a>.</p>
<p><strong>Summary of changes:</strong></p>
<ul>
<li>A new <strong>Overview</strong> page provides access to the most common tasks across Magic Transit and Magic WAN.</li>
<li>Product names have been removed from top-level navigation.</li>
<li>Magic Transit and Magic WAN configuration is now organized under <strong>Routes</strong> and <strong>Connectors</strong>. For example, you will find IP Prefixes under <strong>Routes</strong>, and your GRE/IPsec Tunnels under <strong>Connectors.</strong></li>
<li>Magic Firewall policies are now called <strong>Firewall Policies.</strong></li>
<li>Magic WAN Connectors and Connector On-Ramps are now referenced in the dashboard as <strong>Appliances</strong> and <strong>Appliance profiles.</strong> They can be found under <strong>Connectors &gt; Appliances.</strong></li>
<li>Network analytics, network health, and real-time analytics are now available under <strong>Insights.</strong></li>
<li>Packet Captures are found under <strong>Insights &gt; Diagnostics.</strong></li>
<li>You can manage your Sites from <strong>Insights &gt; Network health.</strong></li>
<li>You can find Magic Network Monitoring under <strong>Insights &gt; Network flow</strong>.</li>
</ul>
<p>If you would like to provide feedback, complete <a href="https://forms.gle/htWyjRsTjw1usdis5">this form</a>. You can also find these details in the January 7, 2026 email titled <strong>[FYI] Upcoming Network Services Dashboard Navigation Update</strong>.</p>
<p>Preview:
<img src="/assets/upstream/images/changelog/cloudflare-network-firewall/networking-overview-and-navigation.png" alt="Networking Navigation" /></p>


<h2 id="2026-01-15-1">2026-01-15</h2>

<strong>Support for CrowdStrike device scores in User Risk Scoring</strong>

<p>Cloudflare One has expanded its [User Risk Scoring] (/cloudflare-one/insights/risk-score/) capabilities by introducing two new behaviors for organizations using the [CrowdStrike integration] (/cloudflare-one/integrations/service-providers/crowdstrike/).</p>
<p>Administrators can now automatically escalate the risk score of a user if their device matches specific CrowdStrike Zero Trust Assessment (ZTA) score ranges. This allows for more granular security policies that respond dynamically to the health of the endpoint.</p>
<p>New risk behaviors
The following risk scoring behaviors are now available:</p>
<ul>
<li>CrowdStrike low device score: Automatically increases a user's risk score when the connected device reports a &quot;Low&quot; score from CrowdStrike.</li>
<li>CrowdStrike medium device score: Automatically increases a user's risk score when the connected device reports a &quot;Medium&quot; score from CrowdStrike.</li>
</ul>
<p>These scores are derived from [CrowdStrike device posture attributes] (/cloudflare-one/integrations/service-providers/crowdstrike/#device-posture-attributes), including OS signals and sensor configurations.</p>


<h2 id="2026-01-15-2">2026-01-15</h2>

<strong>Verify WARP Connector connectivity with a simple ping</strong>

<p>We have made it easier to validate connectivity when deploying <a href="/mesh/">WARP Connector</a> as part of your <a href="/reference-architecture/architectures/sase/#connecting-networks">software-defined private network</a>.</p>
<p>You can now <code>ping</code> the WARP Connector host directly on its LAN IP address immediately after installation. This provides a fast, familiar way to confirm that the Connector is online and reachable within your network before testing access to downstream services.</p>
<p>Starting with <a href="/changelog/2026-01-13-warp-linux-ga/">version 2025.10.186.0</a>, WARP Connector responds to traffic addressed to its own LAN IP, giving you immediate visibility into Connector reachability.</p>
<p>Learn more about deploying <a href="/mesh/">WARP Connector</a> and building private network connectivity with <a href="/cloudflare-one/">Cloudflare One</a>.</p>


<h2 id="2026-01-14">2026-01-14</h2>

<strong>WARP client for macOS (version 2025.10.186.0)</strong>

<p>A new GA release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features, including the ability to manage WARP client connectivity for all devices in your fleet using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> now supports transparent HTTP proxying in addition to CONNECT-based proxying.</li>
<li>Added a new feature to manage WARP client connectivity for all devices using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>. This feature allows administrators to send a global signal from an on-premises HTTPS endpoint that force disconnects or reconnects all WARP clients in an account based on configuration set on the endpoint.</li>
</ul>


<h2 id="2026-01-14-1">2026-01-14</h2>

<strong>WARP client for Windows (version 2025.10.186.0)</strong>

<p>A new GA release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features. New features include the ability to manage WARP client connectivity for all devices in your fleet using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>, and a new WARP client device posture check for <a href="/cloudflare-one/reusable-components/posture-checks/warp-client-checks/antivirus/">Antivirus</a>.</p>
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


<h2 id="2026-01-13">2026-01-13</h2>

<strong>WARP client for Linux (version 2025.10.186.0)</strong>

<p>A new GA release for the Linux WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features, including the ability to manage WARP client connectivity for all devices in your fleet using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>.</p>
<p>WARP client version 2025.8.779.0 introduced an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at <a href="https://pkg.cloudflareclient.com">pkg.cloudflareclient.com</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.</li>
<li>Linux <a href="/cloudflare-one/reusable-components/posture-checks/warp-client-checks/disk-encryption/">disk encryption posture check</a> now supports non-filesystem encryption types like <code>dm-crypt</code>.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> now supports transparent HTTP proxying in addition to CONNECT-based proxying.</li>
<li>Fixed an issue where the GUI becomes unresponsive when the <strong>Re-Authenticate in browser</strong> button is clicked.</li>
<li>Added a new feature to manage WARP client connectivity for all devices using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>. This feature allows administrators to send a global signal from an on-premises HTTPS endpoint that force disconnects or reconnects all WARP clients in an account based on configuration set on the endpoint.</li>
</ul>


<h2 id="2026-01-12">2026-01-12</h2>

<strong>Enhanced visibility for post-delivery actions</strong>

<p>The Action Log now provides enriched data for post-delivery actions to improve troubleshooting. In addition to success confirmations, failed actions now display the targeted Destination folder and a specific failure reason within the Activity field.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17721.md")</aside>
<p><img src="/assets/upstream/images/changelog/email-security/enhanced-visibility-post-delivery-actions.png" alt="failure-log-example" /></p>
<p>This update allows you to see the full lifecycle of a failed action. For instance, if an administrator tries to move an email that has already been deleted or moved manually, the log will now show the multiple retry attempts and the specific destination error.</p>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2026-01-08">2026-01-08</h2>

<strong>Cloudflare admin activity logs capture creation of DNS over HTTP (DoH) users</strong>

<p>Cloudflare <a href="/cloudflare-one/insights/logs/">admin activity logs</a> now capture each time a <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-https/">DNS over HTTP (DoH) user</a> is created.</p>
<p>These logs can be viewed from the <a href="https://one.dash.cloudflare.com/">Cloudflare One dashboard</a>, pulled via the <a href="/api/">Cloudflare API</a>, and exported through <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a>.</p>


<h2 id="2025-12-31">2025-12-31</h2>

<strong>Breakout traffic visibility via NetFlow</strong>

<p>Magic WAN Connector now exports NetFlow data for breakout traffic to Magic Network Monitoring (MNM), providing visibility into traffic that bypasses Cloudflare's security filtering.</p>
<p>This feature allows you to:</p>
<ul>
<li>Monitor breakout traffic statistics in the Cloudflare dashboard.</li>
<li>View traffic patterns for applications configured to bypass Cloudflare.</li>
<li>Maintain visibility across all traffic passing through your Magic WAN Connector.</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-wan/analytics/netflow-analytics/">NetFlow statistics</a>.</p>


<h2 id="2025-12-17">2025-12-17</h2>

<strong>Shadow IT - domain level SaaS analytics</strong>

<p>Zero Trust has again upgraded its <strong>Shadow IT analytics</strong>, providing you with unprecedented visibility into your organizations use of SaaS tools. With this dashboard, you can review who is using an application and volumes of data transfer to the application.</p>
<p>With this update, you can review data transfer metrics at the domain level, rather than just the application level, providing more granular insight into your data transfer patterns.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/shadow-it-domain.png" alt="New Domain Level Metrics" /></p>
<p>These metrics can be filtered by all available filters on the dashboard, including user, application, or content category.</p>
<p>Both the analytics and policies are accessible in the Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, empowering organizations with better visibility and control.</p>


<h2 id="2025-12-16">2025-12-16</h2>

<strong>New duplicate action for supported Cloudflare One resources</strong>

<p>You can now duplicate specific Cloudflare One resources with a single click from the dashboard.</p>
<p>Initially supported resources:</p>
<ul>
<li>Access Applications</li>
<li>Access Policies</li>
<li>Gateway Policies</li>
</ul>
<p>To try this out, simply click on the overflow menu (⋮) from the resource table and click <i>Duplicate</i>. We will continue to add the Duplicate action for resources throughout 2026.</p>


<h2 id="2025-12-10">2025-12-10</h2>

<strong>WARP client for macOS (version 2025.10.118.1)</strong>

<p>A new Beta release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> now supports transparent HTTP proxying in addition to CONNECT-based proxying.</li>
</ul>


<h2 id="2025-12-10-1">2025-12-10</h2>

<strong>WARP client for Windows (version 2025.10.118.1)</strong>

<p>A new Beta release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> now supports transparent HTTP proxying in addition to CONNECT-based proxying.</li>
<li>Fixed an issue where sending large messages to the WARP daemon by Inter-Process Communication (IPC) could cause WARP to crash and result in service interruptions.</li>
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


<h2 id="2025-12-04">2025-12-04</h2>

<strong>Reclassifications to Submissions</strong>

<p>We have updated the terminology “Reclassify” and “Reclassifications” to “Submit” and “Submissions” respectively. This update more accurately reflects the outcome of providing these items to Cloudflare.</p>
<p>Submissions are leveraged to tune future variants of campaigns. To respect data sanctity, providing a submission does not change the original disposition of the emails submitted.</p>
<p><img src="/assets/upstream/images/changelog/email-security/reclassification-submission.png" alt="nav_example" /></p>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2025-11-18">2025-11-18</h2>

<strong>Adjustment to Final Disposition Column</strong>

<h4 id="2025-11-18-temporary-adjustment-to-final-disposition-column-adjustment-to-final-disposition-column">Adjustment to Final Disposition column</h4>
<h4 id="2025-11-18-temporary-adjustment-to-final-disposition-column-the-final-disposition-column-in-submissions-team-submissions-tab-is-changing-for-non-phishguard-customers">The <strong>Final Disposition</strong> column in <strong>Submissions</strong> &gt; <strong>Team Submissions</strong> tab is changing for non-Phishguard customers.</h4>
<h4 id="2025-11-18-temporary-adjustment-to-final-disposition-column-what-s-changing">What's Changing</h4>
<ul>
<li>Column will be called <strong>Status</strong> instead of <strong>Final Disposition</strong></li>
<li>Column status values will now be: <strong>Submitted</strong>, <strong>Accepted</strong> or <strong>Rejected</strong>.</li>
</ul>
<h4 id="2025-11-18-temporary-adjustment-to-final-disposition-column-next-steps">Next Steps</h4>
<p>We will listen carefully to your feedback and continue to find comprehensive ways to communicate updates on your submissions. Your submissions will continue to be addressed at an even greater rate than before, fuelling faster and more accurate email security improvement.</p>


<h2 id="2025-11-17">2025-11-17</h2>

<strong>New Cloudflare One Navigation and Product Experience</strong>

<p>The Zero Trust dashboard and navigation is receiving significant and exciting updates. The dashboard is being restructured to better support common tasks and workflows, and various pages have been moved and consolidated.</p>
<p>There is a new guided experience on login detailing the changes, and you can use the Zero Trust dashboard search to find product pages by both their new and old names, as well as your created resources. To replay the guided experience, you can find it in Overview &gt; Get Started.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/cf1-dash-changes.png" alt="Cloudflare One Dash Changes" /></p>
<p>Notable changes</p>
<ul>
<li>Product names have been removed from many top-level navigation items to help bring clarity to what they help you accomplish. For example, you can find Gateway policies under ‘Traffic policies' and CASB findings under ‘Cloud &amp; SaaS findings.'</li>
<li>You can view all analytics, logs, and real-time monitoring tools from ‘Insights.'</li>
<li>‘Networks' better maps the ways that your corporate network interacts with Cloudflare. Some pages like Tunnels, are now a tab rather than a full page as part of these changes. You can find them at Networks &gt; Connectors.</li>
<li>Settings are now located closer to the tools and resources they impact. For example, this means you'll find your WARP configurations at Team &amp; Resources &gt; Devices.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/new-cf1-navigation.png" alt="New Cloudflare One Navigation" /></p>
<p>No changes to our API endpoint structure or to any backend services have been made as part of this effort.</p>


<h2 id="2025-11-14">2025-11-14</h2>

<strong>Generate Cloudflare Access SSH certificate authority (CA) directly from the Cloudflare dashboard</strong>

<p>SSH with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">Cloudflare Access for Infrastructure</a> allows you to use short-lived SSH certificates to eliminate SSH key management and reduce security risks associated with lost or stolen keys.</p>
<p>Previously, users had to generate this certificate by using the <a href="https://developers.cloudflare.com/api/">Cloudflare API</a> directly. With this update, you can now create and manage this certificate in the <a href="https://one.dash.cloudflare.com">Cloudflare One dashboard</a> from the <strong>Access controls</strong> &gt; <strong>Service credentials</strong> page.</p>
<p><img src="/assets/upstream/images/changelog/access/SSH-CA-generation.png" alt="Navigate to Access controls and then Service credentials to see where you can generate an SSH CA" /></p>
<p>For more details, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#generate-a-cloudflare-ssh-ca">Generate a Cloudflare SSH CA</a>.</p>


<h2 id="2025-11-14-1">2025-11-14</h2>

<strong>New SaaS Security weekly digests with API CASB</strong>

<p>You can now stay on top of your SaaS security posture with the new <strong>CASB Weekly Digest</strong> notification. This opt-in email digest is delivered to your inbox every Monday morning and provides a high-level summary of your organization's Cloudflare API CASB findings from the previous week.</p>
<p>This allows security teams and IT administrators to get proactive, at-a-glance visibility into new risks and integration health without having to log in to the dashboard.</p>
<p>To opt in, navigate to <strong>Manage Account</strong> &gt; <strong>Notifications</strong> in the Cloudflare dashboard to configure the <strong>CASB Weekly Digest</strong> alert type.</p>
<h4 id="2025-11-14-casb-digest-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>At-a-glance summary</strong> — Review new high/critical findings, most frequent finding types, and new content exposures from the past 7 days.</li>
<li><strong>Integration health</strong> — Instantly see the status of all your connected SaaS integrations (Healthy, Unhealthy, or Paused) to spot API connection issues.</li>
<li><strong>Proactive alerting</strong> — The digest is sent automatically to all subscribed users every Monday morning.</li>
<li><strong>Easy to configure</strong> — Users can opt in by enabling the notification in the Cloudflare dashboard under <strong>Manage Account</strong> &gt; <strong>Notifications</strong>.</li>
</ul>
<h4 id="2025-11-14-casb-digest-learn-more">Learn more</h4>
<ul>
<li>Configure <a href="/notifications/">notification preferences</a> in Cloudflare.</li>
</ul>
<p>The CASB Weekly Digest notification is available to all Cloudflare users today.</p>


<h2 id="2025-11-12">2025-11-12</h2>

<strong>DEX Logpush jobs</strong>

<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into WARP device metrics, connectivity, and network performance across your Cloudflare SASE deployment.</p>
<p>We've released four new WARP and DEX device data sets that can be exported via <a href="/cloudflare-one/insights/logs/logpush/">Cloudflare Logpush</a>. These Logpush data sets can be exported to R2, a cloud bucket, or a SIEM to build a customized logging and analytics experience.</p>
<ol>
<li><a href="/logs/logpush/logpush-job/datasets/account/dex_application_tests/">DEX Application Tests</a></li>
<li><a href="/logs/logpush/logpush-job/datasets/account/dex_device_state_events/">DEX Device State Events</a></li>
<li><a href="/logs/logpush/logpush-job/datasets/account/warp_config_changes/">WARP Config Changes</a></li>
<li><a href="/logs/logpush/logpush-job/datasets/account/warp_toggle_changes/">WARP Toggle Changes</a></li>
</ol>
<p>To create a new DEX or WARP Logpush job, customers can go to the account level of the Cloudflare dashboard &gt; Analytics &amp; Logs &gt; Logpush to get started.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_logpush_datasets.png" alt="DEX logpush job creation dashboard" /></p>


<h2 id="2025-11-12-1">2025-11-12</h2>

<strong>WARP client for Linux (version 2025.9.558.0)</strong>

<p>A new GA release for the Linux WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">Path Maximum Transmission Unit Discovery (PMTUD)</a>. When PMTUD is enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to diagnose connectivity issues.</p>
<p>WARP client version 2025.8.779.0 introduced an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at <a href="https://pkg.cloudflareclient.com/">pkg.cloudflareclient.com</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to diagnose connectivity issues.</li>
<li>Fixed an issue where deleting a registration was erroneously reported as having failed.</li>
<li>Path Maximum Transmission Unit Discovery (PMTUD) may now be used to discover the effective MTU of the connection. This allows the WARP client to improve connectivity optimized for each network. PMTUD is disabled by default. To enable it, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">PMTUD documentation</a>.</li>
</ul>


<h2 id="2025-11-12-2">2025-11-12</h2>

<strong>WARP client for macOS (version 2025.9.558.0)</strong>

<p>A new GA release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">Path Maximum Transmission Unit Discovery (PMTUD)</a>. When PMTUD is enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to diagnose connectivity issues.</p>
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


<h2 id="2025-11-12-3">2025-11-12</h2>

<strong>WARP client for Windows (version 2025.9.558.0)</strong>

<p>A new GA release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">Path Maximum Transmission Unit Discovery (PMTUD)</a>. When PMTUD is enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to diagnose connectivity issues.</p>
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


<h2 id="2025-11-11">2025-11-11</h2>

<strong>cloudflared proxy-dns command will be removed starting February 2, 2026</strong>

<p>Starting February 2, 2026, the <code>cloudflared proxy-dns</code> command will be removed from all new <code>cloudflared</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">releases</a>.</p>
<p>This change is being made to enhance security and address a potential vulnerability in an underlying DNS library. This vulnerability is specific to the <code>proxy-dns</code> command and does not affect any other <code>cloudflared</code> features, such as the core <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> service.</p>
<p>The <code>proxy-dns</code> command, which runs a client-side <a href="/1.1.1.1/encryption/dns-over-https/">DNS-over-HTTPS (DoH)</a> proxy, has been an officially undocumented feature for several years. This functionality is fully and securely supported by our actively developed products.</p>
<p>Versions of <code>cloudflared</code> released before this date will not be affected and will continue to operate. However, note that our <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/#deprecated-releases">official support policy</a> for any <code>cloudflared</code> release is one year from its release date.</p>
<h4 id="2025-11-11-cloudflared-proxy-dns-migration-paths">Migration paths</h4>
<p>We strongly advise users of this undocumented feature to migrate to one of the following officially supported solutions before February 2, 2026, to continue benefiting from secure <a href="/1.1.1.1/encryption/dns-over-https/">DNS-over-HTTPS</a>.</p>
<h4 id="2025-11-11-cloudflared-proxy-dns-end-user-devices">End-user devices</h4>
<p>The preferred method for enabling DNS-over-HTTPS on user devices is the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare WARP client</a>. The WARP client automatically secures and proxies all DNS traffic from your device, integrating it with your organization's <a href="/cloudflare-one/traffic-policies/">Zero Trust policies</a> and <a href="/cloudflare-one/reusable-components/posture-checks/">posture checks</a>.</p>
<h4 id="2025-11-11-cloudflared-proxy-dns-servers-routers-and-iot-devices">Servers, routers, and IoT devices</h4>
<p>For scenarios where installing a client on every device is not possible (such as servers, routers, or IoT devices), we recommend using the <a href="/mesh/">WARP Connector</a>.</p>
<p>Instead of running <code>cloudflared proxy-dns</code> on a machine, you can install the WARP Connector on a single Linux host within your private network. This connector will act as a gateway, securely routing all DNS and network traffic from your <a href="/mesh/features/routes/">entire subnet</a> to Cloudflare for <a href="/cloudflare-one/traffic-policies/">filtering and logging</a>.</p>


<h2 id="2025-11-06">2025-11-06</h2>

<strong>Automatic Return Routing (Beta)</strong>

<p>Magic WAN now supports Automatic Return Routing (ARR), allowing customers to configure Magic on-ramps (IPsec/GRE/CNI) to learn the return path for traffic flows without requiring static routes.</p>
<p>Key benefits:</p>
<ul>
<li><strong>Route-less mode</strong>: Static or dynamic routes are optional when using ARR.</li>
<li><strong>Overlapping IP space support</strong>: Traffic originating from customer sites can use overlapping private IP ranges.</li>
<li><strong>Symmetric routing</strong>: Return traffic is guaranteed to use the same connection as the original on-ramp.</li>
</ul>
<p>This feature is currently in beta and requires the new Unified Routing mode (beta).</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/#configure-automatic-return-routing-beta">Configure Automatic Return Routing</a>.</p>


<h2 id="2025-11-06-1">2025-11-06</h2>

<strong>Designate WAN link for breakout traffic</strong>

<p>Magic WAN Connector now allows you to designate a specific WAN port for breakout traffic, giving you deterministic control over the egress path for latency-sensitive applications.</p>
<p>With this feature, you can:</p>
<ul>
<li>Pin breakout traffic for specific applications to a preferred WAN port.</li>
<li>Ensure critical traffic (such as Zoom or Teams) always uses your fastest or most reliable connection.</li>
<li>Benefit from automatic failover to standard WAN port priority if the preferred port goes down.</li>
</ul>
<p>This is useful for organizations with multiple ISP uplinks who need predictable egress behavior for performance-sensitive traffic.</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#designate-wan-ports-for-breakout-apps">Designate WAN ports for breakout apps</a>.</p>


<h2 id="2025-11-06-2">2025-11-06</h2>

<strong>Applications to be remapped to the new categories</strong>

<p>We have previously added new application categories to better reflect their content and improve HTTP traffic management: refer to <a href="/cloudflare-one/changelog/gateway/#2025-10-28">Changelog</a>.
While the new categories are live now, we want to ensure you have ample time to review and adjust any existing rules you have configured against old categories.
The remapping of existing applications into these new categories will be completed by January 30, 2026.
This timeline allows you a dedicated period to:</p>
<ul>
<li>Review the new category structure.</li>
<li>Identify any policies you have that target the older categories.</li>
<li>Adjust your rules to reference the new, more precise categories before the old mappings change.
Once the applications have been fully remapped by January 30, 2026, you might observe some changes in the traffic being mitigated or allowed by your existing policies. We encourage you to use the intervening time to prepare for a smooth transition.</li>
</ul>
<p><strong>Applications being remappedd</strong></p>
<table>
<thead>
<tr>
<th>Application Name</th>
<th>Existing Category</th>
<th>New Category</th>
</tr>
</thead>
<tbody>
<tr>
<td>Google Photos</td>
<td>File Sharing</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>Flickr</td>
<td>File Sharing</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>ADP</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Greenhouse</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>myCigna</td>
<td>Human Resources</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>UnitedHealthcare</td>
<td>Human Resources</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>ZipRecruiter</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Amazon Business</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Jobcenter</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Jobsuche</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Zenjob</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>DocuSign</td>
<td>Legal</td>
<td>Business</td>
</tr>
<tr>
<td>Postident</td>
<td>Legal</td>
<td>Business</td>
</tr>
<tr>
<td>Adobe Creative Cloud</td>
<td>Productivity</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>Airtable</td>
<td>Productivity</td>
<td>Development</td>
</tr>
<tr>
<td>Autodesk Fusion360</td>
<td>Productivity</td>
<td>IT Management</td>
</tr>
<tr>
<td>Coursera</td>
<td>Productivity</td>
<td>Education</td>
</tr>
<tr>
<td>Microsoft Power BI</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Tableau</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Duolingo</td>
<td>Productivity</td>
<td>Education</td>
</tr>
<tr>
<td>Adobe Reader</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>AnpiReport</td>
<td>Productivity</td>
<td>Travel</td>
</tr>
<tr>
<td>ビズリーチ</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>doda (デューダ)</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>求人ボックス</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>マイナビ2026</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Power Apps</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>RECRUIT AGENT</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>シフトボード</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>スタンバイ</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Doctolib</td>
<td>Productivity</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>Miro</td>
<td>Productivity</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>MyFitnessPal</td>
<td>Productivity</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>Sentry Mobile</td>
<td>Productivity</td>
<td>Travel</td>
</tr>
<tr>
<td>Slido</td>
<td>Productivity</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>Arista Networks</td>
<td>Productivity</td>
<td>IT Management</td>
</tr>
<tr>
<td>Atlassian</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>CoderPad</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>eAgreements</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Vmware</td>
<td>Productivity</td>
<td>IT Management</td>
</tr>
<tr>
<td>Vmware Vcenter</td>
<td>Productivity</td>
<td>IT Management</td>
</tr>
<tr>
<td>AWS Skill Builder</td>
<td>Productivity</td>
<td>Education</td>
</tr>
<tr>
<td>Microsoft Office 365 (GCC)</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Microsoft Exchange Online (GCC)</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Canva</td>
<td>Sales &amp; Marketing</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>Instacart</td>
<td>Shopping</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>Wawa</td>
<td>Shopping</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>McDonald's</td>
<td>Shopping</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>Vrbo</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>American Airlines</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>Booking.com</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>Ticketmaster</td>
<td>Shopping</td>
<td>Entertainment &amp; Events</td>
</tr>
<tr>
<td>Airbnb</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>DoorDash</td>
<td>Shopping</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>Expedia</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>EasyPark</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>UEFA Tickets</td>
<td>Shopping</td>
<td>Entertainment &amp; Events</td>
</tr>
<tr>
<td>DHL Express</td>
<td>Shopping</td>
<td>Business</td>
</tr>
<tr>
<td>UPS</td>
<td>Shopping</td>
<td>Business</td>
</tr>
</tbody>
</table>
<p>For more information on creating HTTP policies, refer to <a href="/cloudflare-one/traffic-policies/application-app-types/">Applications and app types</a>.</p>


<h2 id="2025-10-28">2025-10-28</h2>

<strong>Access private hostname applications support all ports/protocols</strong>

<p><a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Cloudflare Access for private hostname applications</a> can now secure traffic on all ports and protocols.</p>
<p>Previously, applying Zero Trust policies to private applications required the application to use HTTPS on port <code>443</code> and support Server Name Indicator (SNI).</p>
<p>This update removes that limitation. As long as the application is reachable via a Cloudflare off-ramp, you can now enforce your critical security controls — like single sign-on (SSO), MFA, device posture, and variable session lengths — to any private application. This allows you to extend Zero Trust security to services like SSH, RDP, internal databases, and other non-HTTPS applications.</p>
<p><img src="/assets/upstream/images/changelog/access/internal_private_app_any_port.png" alt="Example private application on non-443 port" /></p>
<p>For example, you can now create a self-hosted application in Access for <code>ssh.testapp.local</code> running on port <code>22</code>. You can then build a policy that only allows engineers in your organization to connect after they pass an SSO/MFA check and are using a corporate device.</p>
<p>This feature is generally available across all plans.</p>


<h2 id="2025-10-28-1">2025-10-28</h2>

<strong>CASB introduces new granular roles</strong>

<p>Cloudflare CASB (Cloud Access Security Broker) now supports two new granular roles to provide more precise access control for your security teams:</p>
<ul>
<li><strong>Cloudflare CASB Read:</strong> Provides read-only access to view CASB findings and dashboards. This role is ideal for security analysts, compliance auditors, or team members who need visibility without modification rights.</li>
<li><strong>Cloudflare CASB:</strong> Provides full administrative access to configure and manage all aspects of the CASB product.</li>
</ul>
<p>These new roles help you better enforce the principle of least privilege. You can now grant specific members access to CASB security findings without assigning them broader permissions, such as the <strong>Super Administrator</strong> or <strong>Administrator</strong> roles.</p>
<p>To enable <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">Data Loss Prevention (DLP)</a>, scans in CASB, account members will need the <strong>Cloudflare Zero Trust</strong> role.</p>
<p>You can find these new roles when inviting members or creating API tokens in the Cloudflare dashboard under <strong>Manage Account</strong> &gt; <strong>Members</strong>.</p>
<p>To learn more about managing roles and permissions, refer to the <a href="/fundamentals/manage-members/roles/">Manage account members and roles documentation</a>.</p>


<h2 id="2025-10-28-2">2025-10-28</h2>

<strong>New Application Categories added for HTTP Traffic Management</strong>

<p>To give you precision and flexibility while creating policies to block unwanted traffic, we are introducing new, more granular application categories in the Gateway product.</p>
<p>We have added the following categories to provide more precise organization and allow for finer-grained policy creation, designed around how users interact with different types of applications:</p>
<ul>
<li>Business</li>
<li>Education</li>
<li>Entertainment &amp; Events</li>
<li>Food &amp; Drink</li>
<li>Health &amp; Fitness</li>
<li>Lifestyle</li>
<li>Navigation</li>
<li>Photography &amp; Graphic Design</li>
<li>Travel</li>
</ul>
<p>The new categories are live now, but we are providing a transition period for existing applications to be fully remapped to these new categories.</p>
<p>The full remapping will be completed by January 30, 2026.</p>
<p>We encourage you to use this time to:</p>
<ul>
<li>Review the new category structure.</li>
<li>Identify and adjust any existing HTTP policies that reference older categories to ensure a smooth transition.</li>
</ul>
<p>For more information on creating HTTP policies, refer to <a href="/cloudflare-one/traffic-policies/application-app-types/">Applications and app types</a>.</p>


<h2 id="2025-10-20">2025-10-20</h2>

<strong>Schedule DNS policies from the UI</strong>

<p>Admins can now create <a href="/cloudflare-one/traffic-policies/dns-policies/timed-policies/">scheduled DNS policies</a> directly from the Zero Trust dashboard, without using the API. You can configure policies to be active during specific, recurring times, such as blocking social media during business hours or gaming sites on school nights.</p>
<ul>
<li><strong>Preset Schedules</strong>: Use built-in templates for common scenarios like Business Hours, School Days, Weekends, and more.</li>
<li><strong>Custom Schedules</strong>: Define your own schedule with specific days and up to three non-overlapping time ranges per day.</li>
<li><strong>Timezone Control</strong>: Choose to enforce a schedule in a specific timezone (for example, US Eastern) or based on the local time of each user.</li>
<li><strong>Combined with Duration</strong>: Policies can have both a schedule and a duration. If both are set, the duration's expiration takes precedence.</li>
</ul>
<p>You can see the flow in the demo GIF:</p>
<p><img src="/assets/upstream/images/gateway/gateway-dns-scheduled-policies-ui.gif" alt="Schedule DNS policies demo" /></p>
<p>This update makes time-based DNS policies accessible to all Gateway customers, removing the technical barrier of the API.</p>


<h2 id="2025-10-18">2025-10-18</h2>

<strong>On-Demand Security Report</strong>

<p>You can now generate on-demand security reports directly from the Cloudflare dashboard. This new feature provides a comprehensive overview of your email security posture, making it easier than ever to demonstrate the value of Cloudflare’s Email security to executives and other decision makers.</p>
<p>These reports offer several key benefits:</p>
<ul>
<li><strong>Executive Summary:</strong> Quickly view the performance of Email security with a high-level executive summary.</li>
<li><strong>Actionable Insights:</strong> Dive deep into trend data, breakdowns of threat types, and analysis of top targets to identify and address vulnerabilities.</li>
<li><strong>Configuration Transparency:</strong> Gain a clear view of your policy, submission, and domain configurations to ensure optimal setup.</li>
<li><strong>Account Takeover Risks:</strong> Get a snapshot of your M365 risky users (requires a Microsoft Entra ID P2 license and <a href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/">M365 SaaS integration</a>).</li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/email-security/monitoring/download-report/#download-a-security-report">Download a security report</a>.
<img src="/assets/upstream/images/changelog/email-security/report.png" alt="Report" /></p>
<p>This feature is available across the following Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2025-10-17">2025-10-17</h2>

<strong>WARP client for macOS (version 2025.9.173.1)</strong>

<p>A new Beta release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features including Path Maximum Transmission Unit Discovery (PMTUD). With PMTUD enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to debug connectivity issues.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to debug connectivity issues.</li>
<li>Deleting registrations no longer returns an error when succeeding.</li>
<li>Path Maximum Transmission Unit Discovery (PMTUD) is now used to discover the effective MTU of the connection. This allows the client to improve connection performance optimized for the current network.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>macOS Sequoia: Due to changes Apple introduced in macOS 15.0.x, the WARP client may not behave as expected. Cloudflare recommends the use of macOS 15.4 or later.</li>
<li>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</li>
</ul>


<h2 id="2025-10-17-1">2025-10-17</h2>

<strong>WARP client for Windows (version 2025.9.173.1)</strong>

<p>A new Beta release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features including Path Maximum Transmission Unit Discovery (PMTUD). With PMTUD enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to debug connectivity issues.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Improvements for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-multiuser/">Windows multi-user</a> to maintain the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-warp-on-all-devices">Global WARP override</a> state when switching between users.</li>
<li>The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to debug connectivity issues.</li>
<li>Deleting registrations no longer returns an error when succeeding.</li>
<li>Path Maximum Transmission Unit Discovery (PMTUD) is now used to discover the effective MTU of the connection. This allows the client to improve connection performance optimized for the current network.</li>
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


<h2 id="2025-10-16">2025-10-16</h2>

<strong>Monitor Groups for Advanced Health Checking With Load Balancing</strong>

<p>Cloudflare Load Balancing now supports Monitor Groups, a powerful new way to combine multiple health monitors into a single, logical group. This allows you to create sophisticated health checks that more accurately reflect the true availability of your applications by assessing multiple services at once.</p>
<p>With Monitor Groups, you can ensure that all critical components of an application are healthy before sending traffic to an origin pool, enabling smarter failover decisions and greater resilience. This feature is now available via the API for customers with an Enterprise Load Balancing subscription.</p>
<h4 id="2025-08-15-monitor-groups-for-load-balancing-what-you-can-do">What you can do:</h4>
<ul>
<li><strong>Combine Multiple Monitors</strong>: Group different health monitors (for example, HTTP, TCP) that check various application components, like a primary API gateway and a specific <code>/login</code> service.</li>
<li><strong>Isolate Monitors for Observation</strong>: Mark a monitor as &quot;monitoring only&quot; to receive alerts and data without it affecting a pool's health status or traffic steering. This is perfect for testing new checks or observing non-critical dependencies.</li>
<li><strong>Improve Steering Intelligence</strong>: Latency for Dynamic Steering is automatically averaged across all active monitors in a group, providing a more holistic view of an origin's performance.</li>
</ul>
<p>This enhancement is ideal for complex, multi-service applications where the health of one component depends on another. By aggregating health signals, Monitor Groups provide a more accurate and comprehensive assessment of your application's true status.</p>
<p>For detailed information and API configuration guides, please visit our <a href="/load-balancing/monitors/monitor-groups">developer documentation</a> for Monitor Groups.</p>


<h2 id="2025-10-10">2025-10-10</h2>

<strong>New domain categories added</strong>

<p>We have added three new domain categories under the Technology parent category, to better reflect online content and improve DNS filtering.</p>
<p><strong>New categories added</strong></p>
<table>
<thead>
<tr>
<th>Parent ID</th>
<th>Parent Name</th>
<th>Category ID</th>
<th>Category Name</th>
</tr>
</thead>
<tbody>
<tr>
<td>26</td>
<td>Technology</td>
<td>194</td>
<td>Keep Awake Software</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>192</td>
<td>Remote Access</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>193</td>
<td>Shareware/Freeware</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">Gateway domain categories</a> to learn more.</p>


<h2 id="2025-10-08">2025-10-08</h2>

<strong>WARP client for Linux (version 2025.8.779.0)</strong>

<p>A new GA release for the Linux WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains significant fixes and improvements including an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at <a href="https://pkg.cloudflareclient.com/">pkg.cloudflareclient.com</a>.</p>
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


<h2 id="2025-10-08-1">2025-10-08</h2>

<strong>WARP client for macOS (version 2025.8.779.0)</strong>

<p>A new GA release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
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
<p>macOS Sequoia: Due to changes Apple introduced in macOS 15.0.x, the WARP client may not behave as expected. Cloudflare recommends the use of macOS 15.4 or later.</p>
</li>
<li>
<p>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</p>
</li>
</ul>


<h2 id="2025-10-08-2">2025-10-08</h2>

<strong>WARP client for Windows (version 2025.8.779.0)</strong>

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


<h2 id="2025-10-02">2025-10-02</h2>

<strong>Fine-grained Permissioning for Access for Apps, IdPs, &amp; Targets now in Public Beta</strong>

<p>Fine-grained permissions for <strong>Access Applications, Identity Providers (IdPs), and Targets</strong> is now available in Public Beta. This expands our RBAC model beyond account &amp; zone-scoped roles, enabling administrators to grant permissions scoped to individual resources.</p>
<h4 id="2025-10-01-fine-grained-permissioning-beta-what-s-new">What's New</h4>
- **[Access Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)**: Grant admin permissions to specific Access Applications.
- **[Identity Providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)**: Grant admin permissions to individual Identity Providers.
- **[Targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target)**: Grant admin rights to specific Targets
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-01-fine-grained-permissioning-ux.png" alt="Updated Permissions Policy UX" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17728.md")</aside>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/manage-members/roles/">Get started with Cloudflare Permissioning</a></li>
<li><a href="/fundamentals/manage-members/manage">Manage Member Permissioning via the UI &amp; API</a></li>
</ul>


<h2 id="2025-10-01">2025-10-01</h2>

<strong>Expanded File Type Controls for Executables and Disk Images</strong>

<p>You can now enhance your security posture by blocking additional application installer and disk image file types with Cloudflare Gateway. Preventing the download of unauthorized software packages is a critical step in securing endpoints from malware and unwanted applications.</p>
<p>We have expanded Gateway's file type controls to include:</p>
<ul>
<li>Apple Disk Image (dmg)</li>
<li>Microsoft Software Installer (msix, appx)</li>
<li>Apple Software Package (pkg)</li>
</ul>
<p>You can find these new options within the <a href="/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types"><em>Upload File Types</em> and <em>Download File Types</em> selectors</a> when creating or editing an HTTP policy. The file types are categorized as follows:</p>
<ul>
<li><strong>System</strong>: <em>Apple Disk Image (dmg)</em></li>
<li><strong>Executable</strong>: <em>Microsoft Software Installer (msix)</em>, <em>Microsoft Software Installer (appx)</em>, <em>Apple Software Package (pkg)</em></li>
</ul>
<p>To ensure these file types are blocked effectively, please note the following behaviors:</p>
<ul>
<li>DMG: Due to their file structure, DMG files are blocked at the very end of the transfer. A user's download may appear to progress but will fail at the last moment, preventing the browser from saving the file.</li>
<li>MSIX: To comprehensively block Microsoft Software Installers, you should also include the file type <em>Unscannable</em>. MSIX files larger than 100 MB are identified as Unscannable ZIP files during inspection.</li>
</ul>
<p>To get started, go to your HTTP policies in Zero Trust. For a full list of file types, refer to <a href="/cloudflare-one/traffic-policies/http-policies/#supported-file-types">supported file types</a>.</p>


<h2 id="2025-10-01-1">2025-10-01</h2>

<strong>WARP client for Linux (version 2025.7.176.0)</strong>

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


<h2 id="2025-10-01-2">2025-10-01</h2>

<strong>WARP client for macOS (version 2025.7.176.0)</strong>

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


<h2 id="2025-10-01-3">2025-10-01</h2>

<strong>WARP client for Windows (version 2025.7.176.0)</strong>

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


<h2 id="2025-09-30">2025-09-30</h2>

<strong>Application granular controls for operations in SaaS applications</strong>

<p>Gateway users can now apply granular controls to their file sharing and AI chat applications through <a href="/cloudflare-one/traffic-policies/http-policies">HTTP policies</a>.</p>
<p>The new feature offers two methods of controlling SaaS applications:</p>
<ul>
<li><strong>Application Controls</strong> are curated groupings of Operations which provide an easy way for users to achieve a specific outcome. Application Controls may include <em>Upload</em>, <em>Download</em>, <em>Prompt</em>, <em>Voice</em>, and <em>Share</em> depending on the application.</li>
<li><strong>Operations</strong> are controls aligned to the most granular action a user can take. This provides a fine-grained approach to enforcing policy and generally aligns to the SaaS providers API specifications in naming and function.</li>
</ul>
<p>Get started using <a href="/cloudflare-one/traffic-policies/http-policies/granular-controls">Application Granular Controls</a> and refer to the list of <a href="/cloudflare-one/traffic-policies/http-policies/granular-controls/#compatible-applications">supported applications</a>.</p>


<h2 id="2025-09-25">2025-09-25</h2>

<strong>Refine DLP Scans with New Body Phase Selector</strong>

<p>You can now more precisely control your HTTP DLP policies by specifying whether to scan the request or response body, helping to reduce false positives and target specific data flows.</p>
<p>In the Gateway HTTP policy builder, you will find a new selector called <em>Body Phase</em>. This allows you to define the direction of traffic the DLP engine will inspect:</p>
<ul>
<li><em>Request Body</em>: Scans data sent from a user's machine to an upstream service. This is ideal for monitoring data uploads, form submissions, or other user-initiated data exfiltration attempts.</li>
<li><em>Response Body</em>: Scans data sent to a user's machine from an upstream service. Use this to inspect file downloads and website content for sensitive data.</li>
</ul>
<p>For example, consider a policy that blocks Social Security Numbers (SSNs). Previously, this policy might trigger when a user visits a website that contains example SSNs in its content (the response body). Now, by setting the <strong>Body Phase</strong> to <em>Request Body</em>, the policy will only trigger if the user attempts to upload or submit an SSN, ignoring the content of the web page itself.</p>
<p>All policies without this selector will continue to scan both request and response bodies to ensure continued protection.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/#body-phase">Gateway HTTP policy selectors</a>.</p>


<h2 id="2025-09-24">2025-09-24</h2>

<strong>Invalid Submissions Feedback</strong>

<p>Email security relies on your submissions to continuously improve our detection models. However, we often receive submissions in formats that cannot be ingested, such as incomplete EMLs, screenshots, or text files.</p>
<p>To ensure all customer feedback is actionable, we have launched two new features to manage invalid submissions sent to our team and user <a href="/cloudflare-one/email-security/settings/phish-submissions/submission-addresses/">submission aliases</a>:</p>
<ul>
<li><strong>Email Notifications:</strong> We now automatically notify users by email when they provide an invalid submission, educating them on the correct format. To disable notifications, go to <strong><a href="https://one.dash.cloudflare.com/?to=/:account/email-security/settings">Settings</a></strong> &gt; <strong>Invalid submission emails</strong> and turn the feature off.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/email-security/EmailSec-Invalid-Submissions-Toggle.png" alt="EmailSec-Invalid-Submissions-Toggle" /></p>
<ul>
<li><strong>Invalid Submission dashboard:</strong> You can quickly identify which users need education to provide valid submissions so Cloudflare can provide continuous protection.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/email-security/EmailSec-Invalid-Submissions-Dashboard.png" alt="EmailSec-Invalid-Submissions-Dashboard" /></p>
<p>Learn more about this feature on <a href="/cloudflare-one/email-security/submissions/invalid-submissions/">invalid submissions</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2025-09-22">2025-09-22</h2>

<strong>Access Remote Desktop Protocol (RDP) destinations securely from your browser — now generally available!</strong>

<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">Browser-based RDP</a> with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> is now generally available for all Cloudflare customers. It enables secure, remote Windows server access without VPNs or RDP clients.</p>
<p>Since we announced our <a href="/changelog/access/#2025-06-30">open beta</a>, we've made a few improvements:</p>
<ul>
<li>Support for targets with IPv6.</li>
<li>Support for <a href="/cloudflare-wan/">Magic WAN</a> and <a href="/mesh/">WARP Connector</a> as on-ramps.</li>
<li>More robust error messaging on the login page to help you if you encounter an issue.</li>
<li>Worldwide keyboard support. Whether your day-to-day is in Portuguese, Chinese, or something in between, your browser-based RDP experience will look and feel exactly like you are using a desktop RDP client.</li>
<li>Cleaned up some other miscellaneous issues, including but not limited to enhanced support for Entra ID accounts and support for usernames with spaces, quotes, and special characters.</li>
</ul>
<p>As a refresher, here are some benefits browser-based RDP provides:</p>
<ul>
<li><strong>Control how users authenticate to internal RDP resources</strong> with single sign-on (SSO), multi-factor authentication (MFA), and granular access policies.</li>
<li><strong>Record who is accessing which servers and when</strong> to support regulatory compliance requirements and to gain greater visibility in the event of a security event.</li>
<li><strong>Eliminate the need to install and manage software on user devices</strong>. You will only need a web browser.</li>
<li><strong>Reduce your attack surface</strong> by keeping your RDP servers off the public Internet and protecting them from common threats like credential stuffing or brute-force attacks.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/access/browser-based-rdp-access-app.png" alt="Example of a browser-based RDP Access application" /></p>
<p>To get started, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">Connect to RDP in a browser</a>.</p>


<h2 id="2025-09-18">2025-09-18</h2>

<strong>Connect and secure any private or public app by hostname, not IP — with hostname routing for Cloudflare Tunnel</strong>

<p>You can now route private traffic to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> based on a hostname or domain, moving beyond the limitations of IP-based routing. This new capability is <strong>free for all Cloudflare One customers</strong>.</p>
<p>Previously, Tunnel routes could only be defined by IP address or <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">CIDR range</a>. This created a challenge for modern applications with dynamic or ephemeral IP addresses, often forcing administrators to maintain complex and brittle IP lists.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/tunnel-hostname-routing.webp" alt="Hostname-based routing in Cloudflare Tunnel" /></p>
<p><strong>What’s new:</strong></p>
<ul>
<li><strong>Hostname &amp; Domain Routing</strong>: Create routes for individual hostnames (e.g., <code>payroll.acme.local</code>) or entire domains (e.g., <code>*.acme.local</code>) and direct their traffic to a specific Tunnel.</li>
<li><strong>Simplified Zero Trust Policies</strong>: Build resilient policies in Cloudflare Access and Gateway using stable hostnames, making it dramatically easier to apply per-resource authorization for your private applications.</li>
<li><strong>Precise Egress Control</strong>: Route traffic for public hostnames (e.g., <code>bank.example.com</code>) through a specific Tunnel to enforce a dedicated source IP, solving the IP allowlist problem for third-party services.</li>
<li><strong>No More IP Lists</strong>: This feature makes the workaround of maintaining dynamic IP Lists for Tunnel connections obsolete.</li>
</ul>
<p>Get started in the Tunnels section of the Zero Trust dashboard with your first <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostname</a> or <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public hostname</a> route.</p>
<p>Learn more in our <a href="https://blog.cloudflare.com/tunnel-hostname-routing/">blog post</a>.</p>


<h2 id="2025-09-16">2025-09-16</h2>

<strong>New AI-Enabled Search for Zero Trust Dashboard</strong>

<p>Zero Trust Dashboard has a brand new, AI-powered search functionality. You can search your account by resources (applications, policies, device profiles, settings, etc.), pages, products, and more.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/searchexample.png" alt="Example search results in the Zero Trust dashboard" /></p>
<p><strong>Ask Cloudy</strong> — You can also ask Cloudy, our AI agent, questions about Cloudflare Zero Trust. Cloudy is trained on our developer documentation and implementation guides, so it can tell you how to configure functionality, best practices, and can make recommendations.</p>
<p>Cloudy can then stay open with you as you move between pages to build configuration or answer more questions.</p>
<p><strong>Find Recents</strong> — Recent searches and Cloudy questions also have a new tab under Zero Trust Overview.</p>


<h2 id="2025-09-12">2025-09-12</h2>

<strong>Regional Email Processing for Germany, India, or Australia</strong>

<p>We’re excited to announce that Email security customers can now choose their preferred mail processing location directly from the UI when onboarding a domain. This feature is available for the following onboarding methods: <strong>MX</strong>, <strong>BCC</strong>, and <strong>Journaling</strong>.</p>
<h4 id="2025-09-11-regional-email-processing-gia-what-s-new">What’s new</h4>
<p>Customers can now select where their email is processed. The following regions are supported:</p>
<ul>
<li><strong>Germany</strong></li>
<li><strong>India</strong></li>
<li><strong>Australia</strong></li>
</ul>
<p>Global processing remains the default option, providing flexibility to meet both compliance requirements or operational preferences.</p>
<h4 id="2025-09-11-regional-email-processing-gia-how-to-use-it">How to use it</h4>
<p>When onboarding a domain with MX, BCC, or Journaling:</p>
<ol>
<li>Select the desired processing location (Germany, India, or Australia).</li>
<li>The UI will display updated processing addresses specific to that region.</li>
<li>For MX onboarding, if your domain is managed by Cloudflare, you can automatically update MX records directly from the UI.</li>
</ol>
<h4 id="2025-09-11-regional-email-processing-gia-availability">Availability</h4>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
<h4 id="2025-09-11-regional-email-processing-gia-what-s-next">What’s next</h4>
<p>We’re expanding the list of processing locations to match our <a href="/data-localization/">Data Localization Suite (DLS)</a> footprint, giving customers the broadest set of regional options in the market without the complexity of self-hosting.</p>


<h2 id="2025-09-11">2025-09-11</h2>

<strong>DNS filtering for private network onramps</strong>

<p><a href="/cloudflare-wan/zero-trust/cloudflare-gateway/#dns-filtering">Magic WAN</a> and <a href="/mesh/features/routes/#dns-filtering">WARP Connector</a> users can now securely route their DNS traffic to the Gateway resolver without exposing traffic to the public Internet.</p>
<p>Routing DNS traffic to the Gateway resolver allows DNS resolution and filtering for traffic coming from private networks while preserving source internal IP visibility. This ensures Magic WAN users have full integration with our Cloudflare One features, including <a href="/cloudflare-one/traffic-policies/resolver-policies/#internal-dns">Internal DNS</a> and <a href="/cloudflare-one/traffic-policies/egress-policies/#selector-prerequisites">hostname-based policies</a>.</p>
<p>To configure DNS filtering, change your Magic WAN or WARP Connector DNS settings to use Cloudflare's shared resolver IPs, <code>172.64.36.1</code> and <code>172.64.36.2</code>. Once you configure DNS resolution and filtering, you can use <em>Source Internal IP</em> as a traffic selector in your <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a> for routing private DNS traffic to your <a href="/dns/internal-dns/">Internal DNS</a>.</p>


<h2 id="2025-09-08">2025-09-08</h2>

<strong>Custom IKE ID for IPsec Tunnels</strong>

<p>Now, Magic WAN customers can configure a custom IKE ID for their IPsec tunnels. Customers that are using Magic WAN and a VeloCloud SD-WAN device together can utilize this new feature to create a high availability configuration.</p>
<p>This feature is available via API only. Customers can read the Magic WAN documentation to learn more about the <a href="/cloudflare-wan/configuration/common-settings/custom-ike-id-ipsec/">Custom IKE ID feature and the API call to configure it</a>.</p>


<h2 id="2025-09-05">2025-09-05</h2>

<strong>Bidirectional tunnel health checks are compatible with all Magic on-ramps</strong>

<p>All bidirectional tunnel health check return packets are accepted by any Magic on-ramp.</p>
<p>Previously, when a Magic tunnel had a bidirectional health check configured, the bidirectional health check would pass when the return packets came back to Cloudflare over the same tunnel that was traversed by the forward packets.</p>
<p>There are SD-WAN devices, like VeloCloud, that do not offer controls to steer traffic over one tunnel versus another in a high availability tunnel configuration.</p>
<p>Now, when a Magic tunnel has a bidirectional health check configured, the bidirectional health check will pass when the return packet traverses over any tunnel in a high availability configuration.</p>


<h2 id="2025-09-02">2025-09-02</h2>

<strong>Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025</strong>

<p>Starting <strong>December 1, 2025</strong>, list endpoints for the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a> and <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> will no longer return deleted tunnels, routes, subnets and virtual networks by default. This change makes the API behavior more intuitive by only returning active resources unless otherwise specified.</p>
<p>No action is required if you already explicitly set <code>is_deleted=false</code> or if you only need to list active resources.</p>
<p>This change affects the following API endpoints:</p>
<ul>
<li>List all tunnels: <a href="/api/resources/zero_trust/subresources/tunnels/methods/list/"><code>GET /accounts/{account_id}/tunnels</code></a></li>
<li>List <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnels</a>: <a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/"><code>GET /accounts/{account_id}/cfd_tunnel</code></a></li>
<li>List <a href="/mesh/">WARP Connector</a> tunnels: <a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/"><code>GET /accounts/{account_id}/warp_connector</code></a></li>
<li>List tunnel routes: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/"><code>GET /accounts/{account_id}/teamnet/routes</code></a></li>
<li>List subnets: <a href="/api/resources/zero_trust/subresources/networks/subresources/subnets/methods/list/"><code>GET /accounts/{account_id}/zerotrust/subnets</code></a></li>
<li>List virtual networks: <a href="/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/list/"><code>GET /accounts/{account_id}/teamnet/virtual_networks</code></a></li>
</ul>
<h4 id="2025-09-02-tunnel-networks-list-endpoints-new-default-what-is-changing">What is changing?</h4>
<p>The default behavior of the <code>is_deleted</code> query parameter will be updated.</p>
<table>
<thead>
<tr>
<th align="left">Scenario</th>
<th align="left">Previous behavior (before December 1, 2025)</th>
<th align="left">New behavior (from December 1, 2025)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>is_deleted</code> parameter is omitted</td>
<td align="left">Returns <strong>active &amp; deleted</strong> tunnels, routes, subnets and virtual networks</td>
<td align="left">Returns <strong>only active</strong> tunnels, routes, subnets and virtual networks</td>
</tr>
</tbody>
</table>
<h4 id="2025-09-02-tunnel-networks-list-endpoints-new-default-action-required">Action required</h4>
<p>If you need to retrieve deleted (or all) resources, please update your API calls to explicitly include the <code>is_deleted</code> parameter before <strong>December 1, 2025</strong>.</p>
<p>To get a list of only deleted resources, you must now explicitly add the <code>is_deleted=true</code> query parameter to your request:</p>
<pre tabindex="0"><code class="language-bash">&#35; Example: Get ONLY deleted Tunnels&#10;curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tunnels?is_deleted=true&quot; \&#10;     &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;&#10;&#35; Example: Get ONLY deleted Virtual Networks&#10;curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/virtual_networks?is_deleted=true&quot; \&#10;     &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<p>Following this change, retrieving a complete list of both active and deleted resources will require two separate API calls: one to get active items (by omitting the parameter or using <code>is_deleted=false</code>) and one to get deleted items (<code>is_deleted=true</code>).</p>
<h4 id="2025-09-02-tunnel-networks-list-endpoints-new-default-why-we-re-making-this-change">Why we’re making this change</h4>
This update is based on user feedback and aims to:
* **Create a more intuitive default:** Aligning with common API design principles where list operations return only active resources by default.
* **Reduce unexpected results:** Prevents users from accidentally operating on deleted resources that were returned unexpectedly.
* **Improve performance:** For most users, the default query result will now be smaller and more relevant.
<p>To learn more, please visit the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a> and <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> documentation.</p>


<h2 id="2025-09-02-1">2025-09-02</h2>

<strong>Updated Email security roles</strong>

<p>To provide more granular controls, we refined the <a href="/cloudflare-one/roles-permissions/#email-security-roles">existing roles</a> for Email security and launched a new Email security role as well.</p>
<p>All Email security roles no longer have read or write access to any of the other Zero Trust products:</p>
<ul>
<li><strong>Email Configuration Admin</strong></li>
<li><strong>Email Integration Admin</strong></li>
<li><strong>Email security Read Only</strong></li>
<li><strong>Email security Analyst</strong></li>
<li><strong>Email security Policy Admin</strong></li>
<li><strong>Email security Reporting</strong></li>
</ul>
<p>To configure <a href="/cloudflare-one/email-security/outbound-dlp/">Data Loss Prevention (DLP)</a> or <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/#set-up-clientless-web-isolation">Remote Browser Isolation (RBI)</a>, you now need to be an admin for the Zero Trust dashboard with the <strong>Cloudflare Zero Trust</strong> role.</p>
<p>Also through customer feedback, we have created a new additive role to allow <strong>Email security Analyst</strong> to create, edit, and delete Email security policies, without needing to provide access via the <strong>Email Configuration Admin</strong> role. This role is called <strong>Email security Policy Admin</strong>, which can read all settings, but has write access to <a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/">allow policies</a>, <a href="/cloudflare-one/email-security/settings/detection-settings/trusted-domains/">trusted domains</a>, and <a href="/cloudflare-one/email-security/settings/detection-settings/blocked-senders/">blocked senders</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2025-08-29">2025-08-29</h2>

<strong>Cloudflare One WARP Diagnostic AI Analyzer</strong>

<p>We're excited to share a new AI feature, the <a href="https://blog.cloudflare.com/ai-troubleshoot-warp-and-network-connectivity-issues/">WARP diagnostic analyzer</a>, to help you troubleshoot and resolve WARP connectivity issues faster. This beta feature is now available in the <a href="https://dash.cloudflare.com/one/">Cloudflare One dashboard</a> to all users. The AI analyzer makes it easier for you to identify the root cause of client connectivity issues by parsing <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#start-a-remote-capture">remote captures</a> of <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#warp-diag-logs">WARP diagnostic logs</a>. The WARP diagnostic analyzer provides a summary of impact that may be experienced on the device, lists notable events that may contribute to performance issues, and recommended troubleshooting steps and articles to help you resolve these issues. Refer to <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#diagnostics-analyzer-beta">WARP diagnostics analyzer (beta)</a> to learn more about how to maximize using the WARP diagnostic analyzer to troubleshoot the WARP client.</p>


<h2 id="2025-08-29-1">2025-08-29</h2>

<strong>DEX MCP Server</strong>

<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into device connectivity and performance across your Cloudflare SASE deployment.</p>
<p>We've released an MCP server <a href="https://cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/">(Model Context Protocol)</a> for DEX.</p>
<p>The DEX MCP server is an AI tool that allows customers to ask a question like, &quot;Show me the connectivity and performance metrics for the device used by carly‌@acme.com&quot;, and receive an answer that contains data from the DEX API.</p>
<p>Any Cloudflare One customer using a Free, Pay-as-you-go, or Enterprise account can access the DEX MCP Server. This feature is available to everyone.</p>
<p>Customers can test the new DEX MCP server in less than one minute. To learn more, read the <a href="/cloudflare-one/insights/dex/dex-mcp-server/">DEX MCP server documentation</a>.</p>


<h2 id="2025-08-27">2025-08-27</h2>

<strong>Shadow IT - SaaS analytics dashboard</strong>

<p>Zero Trust has significantly upgraded its <strong>Shadow IT analytics</strong>, providing you with unprecedented visibility into your organizations use of SaaS tools. With this dashboard, you can review who is using an application and volumes of data transfer to the application.</p>
<p>You can review these metrics against application type, such as Artificial Intelligence or Social Media. You can also mark applications with an approval status, including <strong>Unreviewed</strong>, <strong>In Review</strong>, <strong>Approved</strong>, and <strong>Unapproved</strong> designating how they can be used in your organization.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/shadow-it-analytics.png" alt="Cloudflare One Analytics Dashboards" /></p>
<p>These application statuses can also be used in Gateway HTTP policies, so you can block, isolate, limit uploads and downloads, and more based on the application status.</p>
<p>Both the analytics and policies are accessible in the Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, empowering organizations with better visibility and control.</p>


<h2 id="2025-08-26">2025-08-26</h2>

<strong>New CASB integrations for ChatGPT, Claude, and Gemini</strong>

<p><a href="https://www.cloudflare.com/zero-trust/products/casb/">Cloudflare CASB</a> now supports three of the most widely used GenAI platforms — <strong>OpenAI ChatGPT</strong>, <strong>Anthropic Claude</strong>, and <strong>Google Gemini</strong>. These API-based integrations give security teams agentless visibility into posture, data, and compliance risks across their organization’s use of generative AI.</p>
<p><img src="/assets/upstream/images/casb/changelog/casb-ai-integrations-preview.png" alt="Cloudflare CASB showing selection of new findings for ChatGPT, Claude, and Gemini integrations." /></p>
<h4 id="2025-08-26-casb-ai-integrations-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Agentless connections</strong> — connect ChatGPT, Claude, and Gemini tenants via API; no endpoint software required</li>
<li><strong>Posture management</strong> — detect insecure settings and misconfigurations that could lead to data exposure</li>
<li><strong>DLP detection</strong> — identify sensitive data in uploaded chat attachments or files</li>
<li><strong>GenAI-specific insights</strong> — surface risks unique to each provider’s capabilities</li>
</ul>
<h4 id="2025-08-26-casb-ai-integrations-learn-more">Learn more</h4>
<ul>
<li><a href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/openai/">ChatGPT integration docs</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/anthropic/">Claude integration docs</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/google-workspace/gemini/">Gemini integration docs</a></li>
</ul>
<p>These integrations are available to all Cloudflare One customers today.</p>


<h2 id="2025-08-26-1">2025-08-26</h2>

<strong>Manage and restrict access to internal MCP servers with Cloudflare Access</strong>

<p>You can now control who within your organization has access to internal MCP servers, by putting internal MCP servers behind <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a>.</p>
<p><a href="/cloudflare-one/access-controls/ai-controls/linked-apps/">Self-hosted applications</a> in Cloudflare Access now support OAuth for MCP server authentication. This allows Cloudflare to delegate access from any self-hosted application to an MCP server via OAuth. The OAuth access token authorizes the MCP server to make requests to your self-hosted applications on behalf of the authorized user, using that user's specific permissions and scopes.</p>
<p>For example, if you have an MCP server designed for internal use within your organization, you can configure Access policies to ensure that only authorized users can access it, regardless of which MCP client they use. Support for internal, self-hosted MCP servers also works with MCP server portals, allowing you to provide a single MCP endpoint for multiple MCP servers. For more on MCP server portals, read the <a href="https://blog.cloudflare.com/zero-trust-mcp-server-portals/">blog post</a> on the Cloudflare Blog.</p>


<h2 id="2025-08-26-2">2025-08-26</h2>

<strong>MCP server portals</strong>

<p><img src="/assets/upstream/images/changelog/access/mcp-server-portal.png" alt="MCP server portal" /></p>
<p>An <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portal</a> centralizes multiple Model Context Protocol (MCP) servers onto a single HTTP endpoint. Key benefits include:</p>
<ul>
<li><strong>Streamlined access to multiple MCP servers</strong>: MCP server portals support both unauthenticated MCP servers as well as MCP servers secured using any third-party or custom OAuth provider. Users log in to the portal URL through Cloudflare Access and are prompted to authenticate separately to each server that requires OAuth.</li>
<li><strong>Customized tools per portal</strong>: Admins can tailor an MCP portal to a particular use case by choosing the specific tools and prompt templates that they want to make available to users through the portal. This allows users to access a curated set of tools and prompts — the less external context exposed to the AI model, the better the AI responses tend to be.</li>
<li><strong>Observability</strong>: Once the user's AI agent is connected to the portal, Cloudflare Access logs the individual requests made using the tools in the portal.</li>
</ul>
<p>This is available in an open beta for all customers across all plans! For more information check out our <a href="https://blog.cloudflare.com/zero-trust-mcp-server-portals/">blog</a> for this release.</p>


<h2 id="2025-08-25">2025-08-25</h2>

<strong>New DLP topic based detection entries for AI prompt protection</strong>

<p>You now have access to a comprehensive suite of capabilities to secure your organization's use of generative AI. AI prompt protection introduces four key features that work together to provide deep visibility and granular control.</p>
<ol>
<li><strong>Prompt Detection for AI Applications</strong></li>
</ol>
<p>DLP can now natively detect and inspect user prompts submitted to popular AI applications, including <strong>Google Gemini</strong>, <strong>ChatGPT</strong>, <strong>Claude</strong>, and <strong>Perplexity</strong>.</p>
<ol start="2">
<li><strong>Prompt Analysis and Topic Classification</strong></li>
</ol>
<p>Our DLP engine performs deep analysis on each prompt, applying <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">topic classification</a>. These topics are grouped into two evaluation categories:</p>
<pre tabindex="0"><code>    - **Content:** PII, Source Code, Credentials and Secrets, Financial Information, and Customer Data.&#10;&#10;    - **Intent:** Jailbreak attempts, requests for malicious code, or attempts to extract PII.&#10;</code></pre>
<p>To help you apply these topics quickly, we have also released five new predefined profiles (for example, AI Prompt: AI Security, AI Prompt: PII) that bundle these new topics.</p>
<p><img src="/assets/upstream/images/changelog/dlp/ai-prompt-detection-entry.png" alt="DLP" /></p>
<ol start="3">
<li>
<p><strong>Granular Guardrails</strong></p>
<p>You can now build guardrails using Gateway HTTP policies with <a href="/cloudflare-one/traffic-policies/http-policies/#granular-controls">application granular controls</a>. Apply a DLP profile containing an <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topic detection</a> to individual AI applications (for example, <code>ChatGPT</code>) and specific user actions (for example, <code>SendPrompt</code>) to block sensitive prompts.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/changelog/dlp/ai-prompt-policy.png" alt="DLP" /></p>
<ol start="4">
<li>
<p><strong>Full Prompt Logging</strong></p>
<p>To aid in incident investigation, an optional setting in your Gateway policy allows you to <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-generative-ai-prompt-content">capture prompt logs</a> to store the full interaction of prompts that trigger a policy match. To make investigations easier, logs can be filtered by <code>conversation_id</code>, allowing you to reconstruct the full context of an interaction that led to a policy violation.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/changelog/dlp/ai-prompt-log.png" alt="DLP" /></p>
<p>AI prompt protection is now available in open beta. To learn more about it, read the <a href="https://blog.cloudflare.com/ai-prompt-protection/#closing-the-loop-logging">blog</a> or refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topics</a>.</p>


<h2 id="2025-08-21">2025-08-21</h2>

<strong>Gateway BYOIP Dedicated Egress IPs now available.</strong>

<p>Enterprise Gateway users can now use Bring Your Own IP (BYOIP) for dedicated egress IPs.</p>
<p>Admins can now onboard and use their own IPv4 or IPv6 prefixes to egress traffic from Cloudflare, delivering greater control, flexibility, and compliance for network traffic.</p>
<p>Get started by following the <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip">BYOIP onboarding process</a>. Once your IPs are onboarded, go to <strong>Gateway</strong> &gt; <strong>Egress policies</strong> and select or create an egress policy. In <strong>Select an egress IP</strong>, choose <em>Use dedicated egress IPs (Cloudflare or BYOIP)</em>, then select your BYOIP address from the dropdown menu.</p>
<p><img src="/assets/upstream/images/gateway/Gateway-byoip-dedicated-egress-ips.png" alt="Screenshot of a dropdown menu adding a BYOIP IPv4 address as a dedicated egress IP in a Gateway egress policy" /></p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip">BYOIP for dedicated egress IPs</a>.</p>


<h2 id="2025-08-15">2025-08-15</h2>

<strong>SFTP support for SSH with Cloudflare Access for Infrastructure</strong>

<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">SSH with Cloudflare Access for Infrastructure</a> now supports SFTP. It is compatible with SFTP clients, such as Cyberduck.</p>


<h2 id="2025-08-15-1">2025-08-15</h2>

<strong>Steer Traffic by AS Number in Load Balancing Custom Rules</strong>

<p>You can now create more granular, network-aware Custom Rules in Cloudflare Load Balancing using the Autonomous System Number (ASN) of an incoming request.</p>
<p>This allows you to steer traffic with greater precision based on the network source of a request. For example, you can route traffic from specific Internet Service Providers (ISPs) or enterprise customers to dedicated infrastructure, optimize performance, or enforce compliance by directing certain networks to preferred data centers.</p>
<p><img src="/assets/upstream/images/changelog/load-balancing/asnum-custom-rule.png" alt="Create a Load Balancing Custom Rule using AS Num" /></p>
<p>To get started, create a <a href="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/">Custom Rule</a> in your Load Balancer and select <strong>AS Num</strong> from the <strong>Field</strong> dropdown.</p>


<h2 id="2025-08-14">2025-08-14</h2>

<strong>Cloudflare Access Logging supports the Customer Metadata Boundary (CMB)</strong>

<p>Cloudflare Access logs now support the <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary (CMB)</a>. If you have configured the CMB for your account, all Access logging will respect that configuration.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17615.md")</aside>


<h2 id="2025-08-08">2025-08-08</h2>

<strong>Expanded Email Link Isolation</strong>

<p>When you deploy MX or Inline, not only can you apply email link isolation to suspicious links in all emails (including benign), you can now also apply email link isolation to all links of a specified disposition. This provides more flexibility in controlling user actions within emails.</p>
<p>For example, you may want to deliver suspicious messages but isolate the links found within them so that users who choose to interact with the links will not accidentally expose your organization to threats. This means your end users are more secure than ever before.</p>
<p><img src="/assets/upstream/images/changelog/email-security/expanded-link-actions.jpg" alt="Expanded Email Link Isolation Configuration" /></p>
<p>To isolate all links within a message based on the disposition, select <strong>Settings</strong> &gt; <strong>Link Actions</strong> &gt; <strong>View</strong> and select <strong>Configure</strong>. As with other other links you isolate, an interstitial will be provided to warn users that this site has been isolated and the link will be recrawled live to evaluate if there are any changes in our threat intel. Learn more about this feature on <a href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/">Configure link actions</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2025-08-06">2025-08-06</h2>

<strong>Improvements to Monitoring Using Zone Settings</strong>

<p>Cloudflare Load Balancing Monitors support loading and applying settings for a specific zone to monitoring requests to origin endpoints. This feature has been migrated to new infrastructure to improve reliability, performance, and accuracy.</p>
<p>All zone monitors have been tested against the new infrastructure. There should be no change to health monitoring results of currently healthy and active pools. Newly created or re-enabled pools may need validation of their monitor zone settings before being introduced to service, especially regarding correct application of mTLS.</p>
<h4 id="2025-08-06-zone-monitoring-improvements-what-you-can-expect">What you can expect:</h4>
<ul>
<li>More reliable application of zone settings to monitoring requests, including
<ul>
<li>Authenticated Origin Pulls</li>
<li>Aegis Egress IP Pools</li>
<li>Argo Smart Routing</li>
<li>HTTP/2 to Origin</li>
</ul>
</li>
<li>Improved support and bug fixes for retries, redirects, and proxied origin resolution</li>
<li>Improved performance and reliability of monitoring requests within the Cloudflare network</li>
<li>Unrelated CDN or WAF configuration changes should have no risk of impact to pool health</li>
</ul>


<h2 id="2025-07-31">2025-07-31</h2>

<strong>Terraform V5 support for tunnels and routes</strong>

<p>The Cloudflare Terraform provider resources for Cloudflare WAN tunnels and routes now support Terraform provider version 5. Customers using infrastructure-as-code workflows can manage their tunnel and route configuration with the latest provider version.</p>
<p>For more information, refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider documentation</a>.</p>


<h2 id="2025-07-30">2025-07-30</h2>

<strong>Magic Transit and Magic WAN health check data is fully compatible with the CMB EU setting.</strong>

<p>Today, we are excited to announce that all Magic Transit and Magic WAN customers with CMB EU (<a href="/data-localization/metadata-boundary/">Customer Metadata Boundary - Europe</a>) enabled in their account will be able to access GRE, IPsec, and CNI health check and traffic volume data in the Cloudflare dashboard and via API.</p>
<p>This ensures that all Magic Transit and Magic WAN customers with CMB EU enabled will be able to access all Magic Transit and Magic WAN features.</p>
<p>Specifically, these two GraphQL endpoints are now compatible with CMB EU:</p>
<ul>
<li><code>magicTransitTunnelHealthChecksAdaptiveGroups</code></li>
<li><code>magicTransitTunnelTrafficAdaptiveGroups</code></li>
</ul>


<h2 id="2025-07-28">2025-07-28</h2>

<strong>Scam domain category introduced under Security Threats</strong>

<p>We have introduced a new Security Threat category called <strong>Scam</strong>. Relevant domains are marked with the Scam category. Scam typically refers to fraudulent websites and schemes designed to trick victims into giving away money or personal information.</p>
<p><strong>New category added</strong></p>
<table>
<thead>
<tr>
<th>Parent ID</th>
<th>Parent Name</th>
<th>Category ID</th>
<th>Category Name</th>
</tr>
</thead>
<tbody>
<tr>
<td>21</td>
<td>Security Threats</td>
<td>191</td>
<td>Scam</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">Gateway domain categories</a> to learn more.</p>


<h2 id="2025-07-24">2025-07-24</h2>

<strong>Gateway HTTP Filtering on all ports available in open BETA</strong>

<p><a href="/cloudflare-one/traffic-policies/">Gateway</a> can now apply <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP filtering</a> to all proxied HTTP requests, not just traffic on standard HTTP (<code>80</code>) and HTTPS (<code>443</code>) ports. This means all requests can now be filtered by <a href="/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/">A/V scanning</a>, <a href="/cloudflare-one/traffic-policies/http-policies/file-sandboxing/">file sandboxing</a>, <a href="/cloudflare-one/data-loss-prevention/#data-in-transit">Data Loss Prevention (DLP)</a>, and more.</p>
<p>You can turn this <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports">setting</a> on by going to <strong>Settings</strong> &gt; <strong>Network</strong> &gt; <strong>Firewall</strong> and choosing  <em>Inspect on all ports</em>.</p>
<p><img src="/assets/upstream/images/gateway/Gateway-Inspection-all-ports.png" alt="HTTP Inspection on all ports setting" /></p>
<p>To learn more, refer to <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports">Inspect on all ports (Beta)</a>.</p>


<h2 id="2025-07-22">2025-07-22</h2>

<strong>Google Bard Application replaced by Gemini</strong>

<p>The <strong>Google Bard</strong> application (ID: 1198) has been deprecated and fully removed from the system. It has been replaced by the <strong>Gemini</strong> application (ID: 1340).
Any existing Gateway policies that reference the old Google Bard application will no longer function.
To ensure your policies continue to work as intended, you should update them to use the new Gemini application.
We recommend replacing all instances of the deprecated Bard application with the new Gemini application in your Gateway policies.
For more information about application policies, please see the <a href="/cloudflare-one/traffic-policies/application-app-types/">Cloudflare Gateway documentation</a>.</p>


<h2 id="2025-07-21">2025-07-21</h2>

<strong>Virtual Cloudflare One Appliance with KVM support (open beta)</strong>

<p>The KVM-based virtual Cloudflare One Appliance is now in open beta with official support for Proxmox VE.</p>
<p>Customers can deploy the virtual appliance on KVM hypervisors to connect branch or data center networks to Cloudflare WAN without dedicated hardware.</p>
<p>For setup instructions, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a virtual Cloudflare One Appliance</a>.</p>


<h2 id="2025-07-17">2025-07-17</h2>

<strong>New detection entry type: Document Matching for DLP</strong>

<p>You can now create <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#document-entries">document-based</a> detection entries in DLP by uploading example documents. Cloudflare will encrypt your documents and create a unique fingerprint of the file. This fingerprint is then used to identify similar documents or snippets within your organization's traffic and stored files.</p>
<p><img src="/assets/upstream/images/changelog/dlp/document-match.png" alt="DLP" /></p>
<p><strong>Key features and benefits:</strong></p>
<ul>
<li>
<p><strong>Upload documents, forms, or templates:</strong> Easily upload .docx and .txt files (up to 10 MB) that contain sensitive information you want to protect.</p>
</li>
<li>
<p><strong>Granular control with similarity percentage:</strong> Define a minimum similarity percentage (0-100%) that a document must meet to trigger a detection, reducing false positives.</p>
</li>
<li>
<p><strong>Comprehensive coverage:</strong> Apply these document-based detection entries in:</p>
<ul>
<li>
<p><strong>Gateway policies:</strong> To inspect network traffic for sensitive documents as they are uploaded or shared.</p>
</li>
<li>
<p><strong>CASB (Cloud Access Security Broker):</strong> To scan files stored in cloud applications for sensitive documents at rest.</p>
</li>
</ul>
</li>
<li>
<p><strong>Identify sensitive data:</strong> This new detection entry type is ideal for identifying sensitive data within completed forms, templates, or even small snippets of a larger document, helping you prevent data exfiltration and ensure compliance.</p>
</li>
</ul>
<p>Once uploaded and processed, you can add this new document entry into a DLP profile and policies to enhance your data protection strategy.</p>


<h2 id="2025-07-15">2025-07-15</h2>

<strong>Faster, more reliable UDP traffic for Cloudflare Tunnel</strong>

<p>Your real-time applications running over <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> are now faster and more reliable. We've completely re-architected the way <code>cloudflared</code> proxies UDP traffic in order to isolate it from other traffic, ensuring latency-sensitive applications like private DNS are no longer slowed down by heavy TCP traffic (like file transfers) on the same Tunnel.</p>
<p>This is a foundational improvement to Cloudflare Tunnel, delivered automatically to all customers. There are no settings to configure — your UDP traffic is already flowing faster and more reliably.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li><strong>Faster UDP performance</strong>: We've significantly reduced the latency for establishing new UDP sessions, making applications like private DNS much more responsive.</li>
<li><strong>Greater reliability for mixed traffic</strong>: UDP packets are no longer affected by heavy TCP traffic, preventing timeouts and connection drops for your real-time services.</li>
</ul>
<p>Learn more about running <a href="/reference-architecture/architectures/sase/#connecting-applications">TCP or UDP applications</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">private networks</a> through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>.</p>


<h2 id="2025-07-10">2025-07-10</h2>

<strong>New onboarding guides for Zero Trust</strong>

<p>Use our brand new onboarding experience for Cloudflare Zero Trust. New and returning users can now engage with a <strong>Get Started</strong> tab with walkthroughs for setting up common use cases end-to-end.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/zt-onboarding-guides.png" alt="Zero Trust onboarding guides" /></p>
<p>There are eight brand new onboarding guides in total:</p>
<ul>
<li>Securely access a private network (sets up device client and Tunnel)</li>
<li>Device-to-device / mesh networking (sets up and connects multiple device clients)</li>
<li>Network to network connectivity (sets up and connects multiple WARP Connectors, makes reference to Magic WAN availability for Enterprise)</li>
<li>Secure web traffic (sets up device client, Gateway, pre-reqs, and initial policies)</li>
<li>Secure DNS for networks (sets up a new DNS location and Gateway policies)</li>
<li>Clientless web access (sets up Access to a web app, Tunnel, and public hostname)</li>
<li>Clientless SSH access (all the same + the web SSH experience)</li>
<li>Clientless RDP access (all the same + RDP-in-browser)</li>
</ul>
<p>Each flow walks the user through the steps to configure the essential elements, and provides a “more details” panel with additional contextual information about what the user will accomplish at the end, along with why the steps they take are important.</p>
<p>Try them out now in the <a href="https://one.dash.cloudflare.com/?to=/:account/home">Zero Trust dashboard</a>!</p>


<h2 id="2025-07-07">2025-07-07</h2>

<strong>Cloudy summaries for Access and Gateway Logs</strong>

<p>Cloudy, Cloudflare's AI Agent, will now automatically summarize your <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/">Access</a> and <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway</a> block logs.</p>
<p>In the log itself, Cloudy will summarize what occurred and why. This will be helpful for quick troubleshooting and issue correlation.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/cloudy-explanation.png" alt="Cloudy AI summarizes a log" /></p>
<p>If you have feedback about the Cloudy summary - good or bad - you can provide that right from the summary itself.</p>


<h2 id="2025-07-07-1">2025-07-07</h2>

<strong>New App Library for Zero Trust Dashboard</strong>

<p>Cloudflare Zero Trust customers can use the App Library to get full visibility over the SaaS applications that they use in their Gateway policies, CASB integrations, and Access for SaaS applications.</p>
<p><strong>App Library</strong>, found under <strong>My Team</strong>, makes information available about all Applications that can be used across the Zero Trust product suite.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/app-library.png" alt="Zero Trust App Library" /></p>
<p>You can use the App Library to see:</p>
<ul>
<li>How Applications are defined</li>
<li>Where they are referenced in policies</li>
<li>Whether they have Access for SaaS configured</li>
<li>Review their CASB findings and integration status.</li>
</ul>
<p>Within individual Applications, you can also track their usage across your organization, and better understand user behavior.</p>


<h2 id="2025-07-01">2025-07-01</h2>

<strong>Access RDP securely from your browser — now in open beta</strong>

<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">Browser-based RDP</a> with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> is now available in open beta for all Cloudflare customers. It enables secure, remote Windows server access without VPNs or RDP clients.</p>
<p>With browser-based RDP, you can:</p>
<ul>
<li><strong>Control how users authenticate to internal RDP resources</strong> with single sign-on (SSO), multi-factor authentication (MFA), and granular access policies.</li>
<li><strong>Record who is accessing which servers and when</strong> to support regulatory compliance requirements and to gain greater visibility in the event of a security event.</li>
<li><strong>Eliminate the need to install and manage software on user devices</strong>. You will only need a web browser.</li>
<li><strong>Reduce your attack surface</strong> by keeping your RDP servers off the public Internet and protecting them from common threats like credential stuffing or brute-force attacks.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/access/browser-based-rdp-access-app.png" alt="Example of a browsed-based RDP Access application" /></p>
<p>To get started, see <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">Connect to RDP in a browser</a>.</p>


<h2 id="2025-06-30">2025-06-30</h2>

<strong>Cloudflare One Agent for Android (version 2.4.2)</strong>

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


<h2 id="2025-06-30-1">2025-06-30</h2>

<strong>Cloudflare One Agent for iOS (version 1.11)</strong>

<p>A new GA release for the iOS Cloudflare One Agent is now available in the <a href="https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492">iOS App Store</a>. This release
contains improvements and new exciting features, including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum">post-quantum cryptography</a>.
By tunneling your corporate network traffic over Cloudflare, you can now gain the immediate <a href="https://blog.cloudflare.com/pq-2024/">protection of post-quantum cryptography</a> without needing to upgrade any of your individual corporate applications or systems.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>QLogs are now disabled by default and can be enabled in the app by turning on <strong>Enable qlogs</strong> under <strong>Settings</strong> &gt; <strong>Advanced</strong> &gt; <strong>Diagnostics</strong> &gt; <strong>Debug Logs</strong>. The QLog setting from previous releases will no longer be respected.</li>
<li>DNS over HTTPS traffic is now included in the WARP tunnel by default.</li>
<li>The WARP client now applies <a href="https://blog.cloudflare.com/pq-2024/">post-quantum cryptography</a> end-to-end on enabled devices accessing resources behind a Cloudflare Tunnel. This feature can be enabled by <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum">MDM</a>.</li>
</ul>


<h2 id="2025-06-23">2025-06-23</h2>

<strong>Data Security Analytics in the Zero Trust dashboard</strong>

<p>Zero Trust now includes <strong>Data security analytics</strong>, providing you with unprecedented visibility into your organization sensitive data.</p>
<p>The new dashboard includes:</p>
<ul>
<li>
<p><strong>Sensitive Data Movement Over Time:</strong></p>
<ul>
<li>See patterns and trends in how sensitive data moves across your environment. This helps understand where data is flowing and identify common paths.</li>
</ul>
</li>
<li>
<p><strong>Sensitive Data at Rest in SaaS &amp; Cloud:</strong></p>
<ul>
<li>View an inventory of sensitive data stored within your corporate SaaS applications (for example, Google Drive, Microsoft 365) and cloud accounts (such as AWS S3).</li>
</ul>
</li>
<li>
<p><strong>DLP Policy Activity:</strong></p>
<ul>
<li>Identify which of your Data Loss Prevention (DLP) policies are being triggered most often.</li>
<li>See which specific users are responsible for triggering DLP policies.</li>
</ul>
</li>
</ul>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/cf1-data-security-analytics-v1.png" alt="Data Security Analytics" /></p>
<p>To access the new dashboard, log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> and go to <strong>Insights</strong> on the sidebar.</p>


<h2 id="2025-06-18">2025-06-18</h2>

<strong>Gateway will now evaluate Network policies before HTTP policies from July 14th, 2025</strong>

<p><a href="/cloudflare-one/traffic-policies/">Gateway</a> will now evaluate <a href="/cloudflare-one/traffic-policies/network-policies/">Network (Layer 4) policies</a> <strong>before</strong> <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP (Layer 7) policies</a>. This change preserves your existing security posture and does not affect which traffic is filtered — but it may impact how notifications are displayed to end users.</p>
<p>This change will roll out progressively between <strong>July 14–18, 2025</strong>. If you use HTTP policies, we recommend reviewing your configuration ahead of rollout to ensure the user experience remains consistent.</p>
<h4 id="2025-06-17-new-order-of-enforcement-updated-order-of-enforcement">Updated order of enforcement</h4>
<p><strong>Previous order:</strong></p>
<ol>
<li>DNS policies</li>
<li>HTTP policies</li>
<li>Network policies</li>
</ol>
<p><strong>New order:</strong></p>
<ol>
<li>DNS policies</li>
<li><strong>Network policies</strong></li>
<li><strong>HTTP policies</strong></li>
</ol>
<h4 id="2025-06-17-new-order-of-enforcement-action-required-review-your-gateway-http-policies">Action required: Review your Gateway HTTP policies</h4>
<p>This change may affect block notifications. For example:</p>
<ul>
<li>You have an <strong>HTTP policy</strong> to block <code>example.com</code> and display a block page.</li>
<li>You also have a <strong>Network policy</strong> to block <code>example.com</code> silently (no client notification).</li>
</ul>
<p>With the new order, the Network policy will trigger first — and the user will no longer see the HTTP block page.</p>
<p>To ensure users still receive a block notification, you can:</p>
<ul>
<li>Add a client notification to your Network policy, or</li>
<li>Use only the HTTP policy for that domain.</li>
</ul>
<hr />
<h4 id="2025-06-17-new-order-of-enforcement-why-we-re-making-this-change">Why we’re making this change</h4>
<p>This update is based on user feedback and aims to:</p>
<ul>
<li>Create a more intuitive model by evaluating network-level policies before application-level policies.</li>
<li>Minimize <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/#error-526-in-the-zero-trust-context">526 connection errors</a> by verifying the network path to an origin before attempting to establish a decrypted TLS connection.</li>
</ul>
<hr />
<p>To learn more, visit the <a href="/cloudflare-one/traffic-policies/order-of-enforcement/">Gateway order of enforcement documentation</a>.</p>


<h2 id="2025-06-05">2025-06-05</h2>

<strong>Cloudflare One Analytics Dashboards and Exportable Access Report</strong>

<p>Cloudflare One now offers powerful new analytics dashboards to help customers easily discover available insights into their application access and network activity. These dashboards provide a centralized, intuitive view for understanding user behavior, application usage, and security posture.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/Analytics Dashboards.png" alt="Cloudflare One Analytics Dashboards"></p>
<p>Additionally, a new exportable access report is available, allowing customers to quickly view high-level metrics and trends in their application access. A <strong>preview</strong> of the report is shown below, with more to be found in the report:</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-report.png" alt="Cloudflare One Analytics Dashboards" /></p>
<p>Both features are accessible in the Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, empowering organizations with better visibility and control.</p>


<h2 id="2025-06-04">2025-06-04</h2>

<strong>New Account-Level Load Balancing UI and Private Load Balancers</strong>

<p>We've made two large changes to load balancing:</p>
<ul>
<li>Redesigned the user interface, now centralized at the <strong>account level</strong>.</li>
<li>Introduced <a href="/load-balancing/private-network/"><strong>Private Load Balancers</strong></a> to the UI, enabling you to manage traffic for all of your external and internal applications in a single spot.</li>
</ul>
<p>This update streamlines how you manage load balancers across multiple zones and extends robust traffic management to your private network infrastructure.</p>
<p><img src="/assets/upstream/images/changelog/load-balancing/account-load-balancing-ui.png" alt="Load Balancing UI" /></p>
<p><strong>Key Enhancements:</strong></p>
<ul>
<li>
<p><strong>Account-Level UI Consolidation:</strong></p>
<ul>
<li>
<p><strong>Unified Management:</strong> Say goodbye to navigating individual zones for load balancing tasks. You can now view, configure, and monitor all your load balancers across every zone in your account from a single, intuitive interface at the account level.</p>
</li>
<li>
<p><strong>Improved Efficiency:</strong> This centralized approach provides a more streamlined workflow, making it faster and easier to manage both your public-facing and internal traffic distribution.</p>
</li>
</ul>
</li>
<li>
<p><strong>Private Network Load Balancing:</strong></p>
<ul>
<li>
<p><strong>Secure Internal Application Access:</strong> Create <a href="/load-balancing/private-network/"><strong>Private Load Balancers</strong></a> to distribute traffic to applications hosted within your private network, ensuring they are not exposed to the public Internet.</p>
</li>
<li>
<p><strong>WARP &amp; Magic WAN Integration:</strong> Effortlessly direct internal traffic from users connected via Cloudflare WARP or through your Magic WAN infrastructure to the appropriate internal endpoint pools.</p>
</li>
<li>
<p><strong>Enhanced Security for Internal Resources:</strong> Combine reliable Load Balancing with Zero Trust access controls to ensure your internal services are both performant and only accessible by verified users.</p>
</li>
</ul>
</li>
</ul>
<p><img src="/assets/upstream/images/changelog/load-balancing/private-load-balancer.png" alt="Private Load Balancers" /></p>


<h2 id="2025-05-29">2025-05-29</h2>

<strong>New Gateway Analytics in the Cloudflare One Dashboard</strong>

<p>Users can now access significant enhancements to Cloudflare Gateway analytics, providing you with unprecedented visibility into your organization's DNS queries, HTTP requests, and Network sessions. These powerful new dashboards enable you to go beyond raw logs and gain actionable insights into how your users are interacting with the Internet and your protected resources.</p>
<p>You can now visualize and explore:</p>
<ul>
<li>Patterns Over Time: Understand trends in traffic volume and blocked requests, helping you identify anomalies and plan for future capacity.</li>
<li>Top Users &amp; Destinations: Quickly pinpoint the most active users, enabling better policy enforcement and resource allocation.</li>
<li>Actions Taken: See a clear breakdown of security actions applied by Gateway policies, such as blocks and allows, offering a comprehensive view of your security posture.</li>
<li>Geographic Regions: Gain insight into the global distribution of your traffic.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/gateway-analytics.png" alt="Gateway Analytics" /></p>
<p>To access the new overview, log in to your Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a> and go to Analytics in the side navigation bar.</p>


<h2 id="2025-05-27">2025-05-27</h2>

<strong>Gateway Protocol Detection Now Available for Pay-as-you-go and Free Plans</strong>

<p>All Cloudflare One Gateway users can now use Protocol detection logging and filtering, including those on Pay-as-you-go and Free plans.</p>
<p>With Protocol Detection, admins can identify and enforce policies on traffic proxied through Gateway based on the underlying network protocol (for example, HTTP, TLS, or SSH), enabling more granular traffic control and security visibility no matter your plan tier.</p>
<p>This feature is available to enable in your account network settings for all accounts. For more information on using Protocol Detection, refer to the <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">Protocol detection documentation</a>.</p>


<h2 id="2025-05-18">2025-05-18</h2>

<strong>New Applications Added to Zero Trust</strong>

<p>42 new applications have been added for Zero Trust support within the Application Library and Gateway policy enforcement, giving you the ability to investigate or apply inline policies to these applications.</p>
<p>33 of the 42 applications are Artificial Intelligence applications. The others are Human Resources (2 applications), Development (2 applications), Productivity (2 applications), Sales &amp; Marketing, Public Cloud, and Security.</p>
<p>To view all available applications, log in to your Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, navigate to the <strong>App Library</strong> under <strong>My Team</strong>.</p>
<p>For more information on creating Gateway policies, see our <a href="/cloudflare-one/traffic-policies/">Gateway policy documentation</a>.</p>


<h2 id="2025-05-16">2025-05-16</h2>

<strong>New Access Analytics in the Cloudflare One Dashboard</strong>

<p>A new Access Analytics dashboard is now available to all Cloudflare One customers. Customers can apply and combine multiple filters to dive into specific slices of their Access metrics. These filters include:</p>
<ul>
<li>Logins granted and denied</li>
<li>Access events by type (SSO, Login, Logout)</li>
<li>Application name (Salesforce, Jira, Slack, etc.)</li>
<li>Identity provider (Okta, Google, Microsoft, onetimepin, etc.)</li>
<li>Users (<code>chris@cloudflare.com</code>, <code>sally@cloudflare.com</code>, <code>rachel@cloudflare.com</code>, etc.)</li>
<li>Countries (US, CA, UK, FR, BR, CN, etc.)</li>
<li>Source IP address</li>
<li>App type (self-hosted, Infrastructure, RDP, etc.)</li>
</ul>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/accessanalytics.png" alt="Access Analytics" /></p>
<p>To access the new overview, log in to your Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a> and find Analytics in the side navigation bar.</p>


<h2 id="2025-05-16-1">2025-05-16</h2>

<strong>Open email attachments with Browser Isolation</strong>

<p>You can now safely open email attachments to view and investigate them.</p>
<p>What this means is that messages now have a <strong>Attachments</strong> section. Here, you can view processed attachments and their classifications (for example, <em>Malicious</em>, <em>Suspicious</em>, <em>Encrypted</em>). Next to each attachment, a <strong>Browser Isolation</strong> icon allows your team to safely open the file in a <strong>clientless, isolated browser</strong> with no risk to the analyst or your environment.</p>
<p><img src="/assets/upstream/images/changelog/email-security/Attachment-RBI.png" alt="Attachment-RBI" /></p>
<p>To use this feature, you must:</p>
<ul>
<li>Turn on <strong>Allow users to open a remote browser without the device client</strong> in your Zero Trust settings.</li>
<li>Have <strong>Browser Isolation (BISO)</strong> seats assigned.</li>
</ul>
<p>For more details, refer to our <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">setup guide</a>.</p>
<p>Some attachment types may not render in Browser Isolation. If there is a file type that you would like to be opened with Browser Isolation, reach out to your Cloudflare contact.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2025-05-14">2025-05-14</h2>

<strong>Domain Categories improvements</strong>

<p><strong>New categories added</strong></p>
<table>
<thead>
<tr>
<th>Parent ID</th>
<th>Parent Name</th>
<th>Category ID</th>
<th>Category Name</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Ads</td>
<td>66</td>
<td>Advertisements</td>
</tr>
<tr>
<td>3</td>
<td>Business &amp; Economy</td>
<td>185</td>
<td>Personal Finance</td>
</tr>
<tr>
<td>3</td>
<td>Business &amp; Economy</td>
<td>186</td>
<td>Brokerage &amp; Investing</td>
</tr>
<tr>
<td>21</td>
<td>Security Threats</td>
<td>187</td>
<td>Compromised Domain</td>
</tr>
<tr>
<td>21</td>
<td>Security Threats</td>
<td>188</td>
<td>Potentially Unwanted Software</td>
</tr>
<tr>
<td>6</td>
<td>Education</td>
<td>189</td>
<td>Reference</td>
</tr>
<tr>
<td>9</td>
<td>Government &amp; Politics</td>
<td>190</td>
<td>Charity and Non-profit</td>
</tr>
</tbody>
</table>
<p><strong>Changes to existing categories</strong></p>
<table>
<thead>
<tr>
<th>Original Name</th>
<th>New Name</th>
</tr>
</thead>
<tbody>
<tr>
<td>Religion</td>
<td>Religion &amp; Spirituality</td>
</tr>
<tr>
<td>Government</td>
<td>Government/Legal</td>
</tr>
<tr>
<td>Redirect</td>
<td>URL Alias/Redirect</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">Gateway domain categories</a> to learn more.</p>


<h2 id="2025-05-13">2025-05-13</h2>

<strong>SAML HTTP-POST bindings support for RBI</strong>

<p>Remote Browser Isolation (RBI) now supports SAML HTTP-POST bindings, enabling seamless authentication for SSO-enabled applications that rely on POST-based SAML responses from Identity Providers (IdPs) within a Remote Browser Isolation session. This update resolves a previous limitation that caused <code>405</code> errors during login and improves compatibility with multi-factor authentication (MFA) flows.</p>
<p>With expanded support for major IdPs like Okta and Azure AD, this enhancement delivers a more consistent and user-friendly experience across authentication workflows. Learn how to <a href="/cloudflare-one/remote-browser-isolation/setup/">set up Remote Browser Isolation</a>.</p>


<h2 id="2025-05-13-1">2025-05-13</h2>

<strong>New Applications Added for DNS Filtering</strong>

<p>You can now create DNS policies to manage outbound traffic for an expanded list of applications.
This update adds support for 273 new applications, giving you more control over your organization's outbound traffic.</p>
<p>With this update, you can:</p>
<ul>
<li>Create DNS policies for a wider range of applications</li>
<li>Manage outbound traffic more effectively</li>
<li>Improve your organization's security and compliance posture</li>
</ul>
<p>For more information on creating DNS policies, see our <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policy documentation</a>.</p>


<h2 id="2025-05-12">2025-05-12</h2>

<strong>Case Sensitive Custom Word Lists</strong>

<p>You can now configure <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#custom-wordlist-datasets">custom word lists</a> to enforce case sensitivity. This setting supports flexibility where needed and aims to reduce false positives where letter casing is critical.</p>
<p><img src="/assets/upstream/images/changelog/dlp/case-sesitive-cwl.png" alt="dlp" /></p>


<h2 id="2025-05-09">2025-05-09</h2>

<strong>Open email links with Browser Isolation</strong>

<p>You can now safely open links in emails to view and investigate them.</p>
<p><img src="/assets/upstream/images/changelog/email-security/investigate-links.jpg" alt="Open links with Browser Isolation" /></p>
<p>From <strong>Investigation</strong>, go to <strong>View details</strong>, and look for the <strong>Links identified</strong> section. Next to each link, the Cloudflare dashboard will display an <strong>Open in Browser Isolation</strong> icon which allows your team to safely open the link in a clientless, isolated browser with no risk to the analyst or your environment. Refer to <a href="/cloudflare-one/email-security/investigation/search-email/#open-links">Open links</a> to learn more about this feature.</p>
<p>To use this feature, you must:</p>
<ul>
<li>Turn on <strong>Allow users to open a remote browser without the device client</strong> in your Zero Trust settings.</li>
<li>Have <strong>Browser Isolation (RBI)</strong> seats assigned.</li>
</ul>
<p>For more details, refer to our <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">setup guide</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2025-05-07">2025-05-07</h2>

<strong>Send forensic copies to storage without DLP profiles</strong>

<p>You can now <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#send-dlp-forensic-copies-to-logpush-destination">send DLP forensic copies</a> to third-party storage for any HTTP policy with an <code>Allow</code> or <code>Block</code> action, without needing to include a DLP profile. This change increases flexibility for data handling and forensic investigation use cases.</p>
<p>By default, Gateway will send all matched HTTP requests to your configured DLP Forensic Copy jobs.</p>
<p><img src="/assets/upstream/images/changelog/dlp/forensic-copies-for-all.png" alt="DLP" /></p>


<h2 id="2025-05-06">2025-05-06</h2>

<strong>UDP and ICMP Monitor Support for Private Load Balancing Endpoints</strong>

<p>Cloudflare Load Balancing now supports <strong>UDP (Layer 4)</strong> and <strong>ICMP (Layer 3)</strong> health monitors for <strong>private endpoints</strong>. This makes it simple to track the health and availability of internal services that don’t respond to HTTP, TCP, or other protocol probes.</p>
<h4 id="2025-05-06-private-health-monitoring-methods-what-you-can-do">What you can do:</h4>
<ul>
<li>Set up <strong>ICMP ping monitors</strong> to check if your private endpoints are reachable.</li>
<li>Use <strong>UDP monitors</strong> for lightweight health checks on non-TCP workloads, such as DNS, VoIP, or custom UDP-based services.</li>
<li>Gain better visibility and uptime guarantees for services running behind <strong>Private Network Load Balancing</strong>, without requiring public IP addresses.</li>
</ul>
<p>This enhancement is ideal for internal applications that rely on low-level protocols, especially when used in conjunction with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/"><strong>Cloudflare Tunnel</strong></a>, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/"><strong>WARP</strong></a>, and <a href="/cloudflare-wan/"><strong>Magic WAN</strong></a> to create a secure and observable private network.</p>
<p>Learn more about <a href="/load-balancing/private-network/">Private Network Load Balancing</a> or view the full list of <a href="/load-balancing/monitors/#supported-protocols">supported health monitor protocols</a>.</p>


<h2 id="2025-05-01">2025-05-01</h2>

<strong>Browser Isolation Overview page for Zero Trust</strong>

<p>A new <strong>Browser Isolation Overview</strong> page is now available in the Cloudflare Zero Trust dashboard. This centralized view simplifies the management of <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation (RBI)</a> deployments, providing:</p>
<ul>
<li><strong>Streamlined Onboarding:</strong> Easily set up and manage isolation policies from one location.</li>
<li><strong>Quick Testing:</strong> Validate <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">clientless web application isolation</a> with ease.</li>
<li><strong>Simplified Configuration:</strong> Configure <a href="/cloudflare-one/access-controls/policies/isolate-application/">isolated access applications</a> and policies efficiently.</li>
<li><strong>Centralized Monitoring:</strong> Track aggregate usage and blocked actions.</li>
</ul>
<p>This update consolidates previously disparate settings, accelerating deployment, improving visibility into isolation activity, and making it easier to ensure your protections are working effectively.</p>
<p><img src="/assets/upstream/images/changelog/browser-isolation/browser-isolation-overview.png" alt="Browser Isolation Overview" /></p>
<p>To access the new overview, log in to your Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a> and find Browser Isolation in the side navigation bar.</p>


<h2 id="2025-04-30">2025-04-30</h2>

<strong>Dark Mode for Zero Trust Dashboard</strong>

<p>The <a href="https://one.dash.cloudflare.com/">Cloudflare Zero Trust dashboard</a> now supports Cloudflare's native dark mode for all accounts and plan types.</p>
<p>Zero Trust Dashboard will automatically accept your user-level preferences for system settings, so if your Dashboard appearance is set to 'system' or 'dark', the Zero Trust dashboard will enter dark mode whenever the rest of your Cloudflare account does.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/dark-mode.png" alt="Zero Trust dashboard supports dark mode" /></p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17706.md")
</div></div>


<h2 id="2025-04-30-1">2025-04-30</h2>

<strong>Cloudflare One Appliance supports multiple DNS server IPs</strong>

<p>Cloudflare One Appliance DHCP server settings now support specifying multiple DNS server IP addresses in the DHCP pool.</p>
<p>Previously, customers could only configure a single DNS server per DHCP pool. With this update, you can specify multiple DNS servers to provide redundancy for clients at branch locations.</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/">DHCP server</a>.</p>


<h2 id="2025-04-28">2025-04-28</h2>

<strong>FQDN Filtering For Gateway Egress Policies</strong>

<p>Cloudflare One administrators can now control which egress IP is used based on a destination's fully qualified domain name (FDQN) within Gateway Egress policies.</p>
<ul>
<li>Host, Domain, Content Categories, and Application selectors are now available in the Gateway Egress policy builder in beta.</li>
<li>During the beta period, you can use these selectors with traffic on-ramped to Gateway with the WARP client, proxy endpoints (commonly deployed with PAC files), or Cloudflare Browser Isolation.
<ul>
<li>For WARP client support, additional configuration is required. For more information, refer to the <a href="/cloudflare-one/traffic-policies/egress-policies/#limitations">WARP client configuration documentation</a>.</li>
</ul>
</li>
</ul>
<p><img src="/assets/upstream/images/gateway/Gateway-Egress-FQDN-Policy-preview.png" alt="Egress by FQDN and Hostname" /></p>
<p>This will help apply egress IPs to your users' traffic when an upstream application or network requires it, while the rest of their traffic can take the most performant egress path.</p>


<h2 id="2025-04-21">2025-04-21</h2>

<strong>Access bulk policy tester</strong>

<p>The <a href="/cloudflare-one/access-controls/policies/policy-management/#test-all-policies-in-an-application">Access bulk policy tester</a> is now available in the Cloudflare Zero Trust dashboard. The bulk policy tester allows you to simulate Access policies against your entire user base before and after deploying any changes. The policy tester will simulate the configured policy against each user's last seen identity and device posture (if applicable).</p>
<p><img src="/assets/upstream/images/changelog/access/example-policy-tester.png" alt="Example policy tester" /></p>


<h2 id="2025-04-14">2025-04-14</h2>

<strong>New predefined detection entry for ICD-11</strong>

<p>You now have access to the World Health Organization (WHO) 2025 edition of the <a href="https://www.who.int/news/item/14-02-2025-who-releases-2025-update-to-the-international-classification-of-diseases-%28icd-11%29">International Classification of Diseases 11th Revision (ICD-11)</a> as a predefined detection entry. The new dataset can be found in the <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#health-information">Health Information</a> predefined profile.</p>
<p>ICD-10 dataset remains available for use.</p>


<h2 id="2025-04-11">2025-04-11</h2>

<strong>HTTP redirect and custom block page redirect</strong>

<p>You can now use more flexible redirect capabilities in Cloudflare One with Gateway.</p>
<ul>
<li>A new <strong>Redirect</strong> action is available in the HTTP policy builder, allowing admins to redirect users to any URL when their request matches a policy. You can choose to preserve the original URL and query string, and optionally include policy context via query parameters.</li>
<li>For <strong>Block</strong> actions, admins can now configure a custom URL to display when access is denied. This block page redirect is set at the account level and can be overridden in DNS or HTTP policies. Policy context can also be passed along in the URL.</li>
</ul>
<p>Learn more in our documentation for <a href="/cloudflare-one/traffic-policies/http-policies/#redirect">HTTP Redirect</a> and <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#redirect-to-a-block-page">Block page redirect</a>.</p>


<h2 id="2025-04-09">2025-04-09</h2>

<strong>Cloudflare Zero Trust SCIM User and Group Provisioning Logs</strong>

<p><a href="/cloudflare-one/team-and-resources/users/scim">Cloudflare Zero Trust SCIM provisioning</a> now has a full audit log of all create, update and delete event from any SCIM Enabled IdP. The <a href="/cloudflare-one/insights/logs/dashboard-logs/scim-logs/">SCIM logs</a> support filtering by IdP, Event type, Result and many more fields. This will help with debugging user and group update issues and questions.</p>
<p>SCIM logs can be found on the Zero Trust Dashboard under <strong>Logs</strong> -&gt; <strong>SCIM provisioning</strong>.</p>
<p><img src="/assets/upstream/images/changelog/access/example-scim-log.png" alt="Example SCIM Logs" /></p>


<h2 id="2025-04-02">2025-04-02</h2>

<strong>CASB and Email security</strong>

<p>With Email security, you get two free CASB integrations.</p>
<p>Use one SaaS integration for Email security to sync with your directory of users, take actions on delivered emails, automatically provide EMLs for reclassification requests for clean emails, discover CASB findings and more.</p>
<p>With the other integration, you can have a separate SaaS integration for CASB findings for another SaaS provider.</p>
<p>Refer to <a href="/cloudflare-one/integrations/cloud-and-saas/">Add an integration</a> to learn more about this feature.</p>
<p><img src="/assets/upstream/images/changelog/email-security/CASB-EmailSecurity.png" alt="CASB-EmailSecurity" /></p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2025-03-21">2025-03-21</h2>

<strong>Secure DNS Locations Management User Role</strong>

<p>We're excited to introduce the <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#secure-dns-locations"><strong>Cloudflare Zero Trust Secure DNS Locations Write role</strong></a>, designed to provide DNS filtering customers with granular control over third-party access when configuring their Protective DNS (PDNS) solutions.</p>
<p>Many DNS filtering customers rely on external service partners to manage their DNS location endpoints. This role allows you to grant access to external parties to administer DNS locations without overprovisioning their permissions.</p>
<p><strong>Secure DNS Location Requirements:</strong></p>
<ul>
<li>
<p>Mandate usage of <a href="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/#bring-your-own-dns-resolver-ip">Bring your own DNS resolver IP addresses</a> if available on the account.</p>
</li>
<li>
<p>Require source network filtering for IPv4/IPv6/DoT endpoints; token authentication or source network filtering for the DoH endpoint.</p>
</li>
</ul>
<p>You can assign the new role via Cloudflare Dashboard (<code>Manage Accounts &gt; Members</code>) or via API. For more information, refer to the <a href="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#secure-dns-locations">Secure DNS Locations documentation</a>.</p>


<h2 id="2025-03-17">2025-03-17</h2>

<strong>Cloudflare One Agent for Android (version 2.4)</strong>

<p>A new GA release for the Android Cloudflare One Agent is now available in the <a href="https://play.google.com/store/apps/details?id=com.cloudflare.cloudflareoneagent">Google Play Store</a>. This release includes a new feature allowing <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url">team name insertion by URL</a> during enrollment, as well as fixes and minor improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Improved in-app error messages.</li>
<li>Improved mobile client login with support for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url">team name insertion by URL</a>.</li>
<li>Fixed an issue preventing admin split tunnel settings taking priority for traffic from certain applications.</li>
</ul>


<h2 id="2025-03-17-1">2025-03-17</h2>

<strong>Cloudflare One Agent for iOS (version 1.10)</strong>

<p>A new GA release for the iOS Cloudflare One Agent is now available in the <a href="https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492">iOS App Store</a>. This release includes a new feature allowing <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url">team name insertion by URL</a> during enrollment, as well as fixes and minor improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Improved in-app error messages.</li>
<li>Improved mobile client login with support for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url">team name insertion by URL</a>.</li>
<li>Bug fixes and performance improvements.</li>
</ul>


<h2 id="2025-03-13">2025-03-13</h2>

<strong>Cloudflare IP Ranges List</strong>

<p>Magic Firewall now supports a new managed list of Cloudflare IP ranges. This list is available as an option when creating a Magic Firewall policy based on IP source/destination addresses. When selecting &quot;is in list&quot; or &quot;is not in list&quot;, the option &quot;<strong>Cloudflare IP Ranges</strong>&quot; will appear in the dropdown menu.</p>
<p>This list is based on the IPs listed in the Cloudflare <a href="https://www.cloudflare.com/en-gb/ips/">IP ranges</a>.
Updates to this managed list are applied automatically.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-network-firewall/cloudflare-ips.png" alt="Cloudflare IPs Managed List" /></p>
<p>Note: IP Lists require a Cloudflare Advanced Network Firewall subscription. For more details about Cloudflare Network Firewall plans, refer to <a href="/cloudflare-network-firewall/plans">Plans</a>.</p>


<h2 id="2025-03-07">2025-03-07</h2>

<strong>Cloudflare One Agent now supports Endpoint Monitoring</strong>

<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into device, network, and application performance across your Cloudflare SASE deployment. The latest release of the Cloudflare One agent (v2025.1.861) now includes device endpoint monitoring capabilities
to provide deeper visibility into end-user device performance which can be analyzed directly from the dashboard.</p>
<p>Device health metrics are now automatically collected, allowing administrators to:</p>
<ul>
<li>View the last network a user was connected to</li>
<li>Monitor CPU and RAM utilization on devices</li>
<li>Identify resource-intensive processes running on endpoints</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dex/cloudflare-one-agent-health-monitoring.gif" alt="Device endpoint monitoring dashboard" /></p>
<p>This feature complements existing DEX features like <a href="/cloudflare-one/insights/dex/tests/">synthetic application monitoring</a> and <a href="/cloudflare-one/insights/dex/tests/traceroute/">network path visualization</a>, creating a comprehensive troubleshooting workflow that connects application performance with device state.</p>
<p>For more details refer to our <a href="/cloudflare-one/insights/dex/">DEX</a> documentation.</p>


<h2 id="2025-03-04">2025-03-04</h2>

<strong>Gain visibility into user actions in Zero Trust Browser Isolation sessions</strong>

<p>We're excited to announce that new logging capabilities for <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation (RBI)</a> through <a href="/logs/logpush/logpush-job/datasets/account/">Logpush</a> are available in Beta starting today!</p>
<p>With these enhanced logs, administrators can gain visibility into end user behavior in the remote browser and track blocked data extraction attempts, along with the websites that triggered them, in an isolated session.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;AccountID&quot;: &quot;$ACCOUNT_ID&quot;,&#10;	&quot;Decision&quot;: &quot;block&quot;,&#10;	&quot;DomainName&quot;: &quot;www.example.com&quot;,&#10;	&quot;Timestamp&quot;: &quot;2025-02-27T23:15:06Z&quot;,&#10;	&quot;Type&quot;: &quot;copy&quot;,&#10;	&quot;UserID&quot;: &quot;$USER_ID&quot;&#10;}&#10;</code></pre>
<p>User Actions available:</p>
<ul>
<li><strong>Copy &amp; Paste</strong></li>
<li><strong>Downloads &amp; Uploads</strong></li>
<li><strong>Printing</strong></li>
</ul>
<p>Learn more about how to get started with Logpush in our <a href="/logs/logpush/">documentation</a>.</p>


<h2 id="2025-03-03">2025-03-03</h2>

<strong>New SAML and OIDC Fields and SAML transforms for Access for SaaS</strong>

<p><a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/">Access for SaaS applications</a> now include more configuration options to support a wider array of SaaS applications.</p>
<p><strong>SAML and OIDC Field Additions</strong></p>
<p>OIDC apps now include:</p>
<ul>
<li>Group Filtering via RegEx</li>
<li>OIDC Claim mapping from an IdP</li>
<li>OIDC token lifetime control</li>
<li>Advanced OIDC auth flows including hybrid and implicit flows</li>
</ul>
<p><img src="/assets/upstream/images/changelog/access/oidc-claims.png" alt="OIDC field additions" /></p>
<p>SAML apps now include improved SAML attribute mapping from an IdP.</p>
<p><img src="/assets/upstream/images/changelog/access/saml-attribute-statements.png" alt="SAML field additions" /></p>
<p><strong>SAML transformations</strong></p>
<p>SAML identities sent to Access applications can be fully customized using JSONata expressions. This allows admins to configure the precise identity SAML statement sent to a SaaS application.</p>
<p><img src="/assets/upstream/images/changelog/access/transformation-box.png" alt="Configured SAML statement sent to application" /></p>


<h2 id="2025-03-02">2025-03-02</h2>

<strong>Use Logpush for Email security detections</strong>

<p>You can now send detection logs to an endpoint of your choice with Cloudflare Logpush.</p>
<p>Filter logs matching specific criteria you have set and select from over 25 fields you want to send. When creating a new Logpush job, remember to select <strong>Email security alerts</strong> as the dataset.</p>
<p><img src="/assets/upstream/images/changelog/email-security/Logpush-Detections.png" alt="logpush-detections" /></p>
<p>For more information, refer to <a href="/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-detection-logs">Enable detection logs</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2025-02-28">2025-02-28</h2>

<strong>Check status of Email security or Area 1</strong>

<p>Concerns about performance for Email security or Area 1? You can now check the operational status of both on the <a href="https://www.cloudflarestatus.com/">Cloudflare Status page</a>.</p>
<p>For Email security, look under <strong>Cloudflare Sites and Services</strong>.</p>
<ul>
<li><strong>Dashboard</strong> is the dashboard for Cloudflare, including Email security</li>
<li><strong>Email security (Zero Trust)</strong> is the processing of email</li>
<li><strong>API</strong> are the Cloudflare endpoints, including the ones for Email security</li>
</ul>
<p>For Area 1, under <strong>Cloudflare Sites and Services</strong>:</p>
<ul>
<li><strong>Area 1 - Dash</strong> is the dashboard for Cloudflare, including Email security</li>
<li><strong>Email security (Area1)</strong> is the processing of email</li>
<li><strong>Area 1 - API</strong> are the Area 1 endpoints</li>
</ul>
<p><img src="/assets/upstream/images/changelog/email-security/Status-Page.png" alt="Status-page" /></p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2025-02-26">2025-02-26</h2>

<strong>Use DLP Assist for M365</strong>

<p>Cloudflare Email security customers who have Microsoft 365 environments can quickly deploy an Email DLP (Data Loss Prevention) solution for free.</p>
<p>Simply deploy our add-in, create a DLP policy in Cloudflare, and configure Outlook to trigger behaviors like displaying a banner, alerting end users before sending, or preventing delivery entirely.</p>
<p>Refer to <a href="/cloudflare-one/email-security/outbound-dlp/">Outbound Data Loss Prevention</a> to learn more about this feature.</p>
<p>In GUI alert:</p>
<p><img src="/assets/upstream/images/changelog/email-security/DLP-Alert.png" alt="DLP-Alert" /></p>
<p>Alert before sending:</p>
<p><img src="/assets/upstream/images/changelog/email-security/DLP-Pop-up.png" alt="DLP-Pop-up" /></p>
<p>Prevent delivery:</p>
<p><img src="/assets/upstream/images/changelog/email-security/DLP-Blocked.png" alt="DLP-Blocked" /></p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2025-02-14">2025-02-14</h2>

<strong>Configure your Magic WAN Connector to connect via static IP assignment</strong>

<p>You can now locally configure your <a href="/cloudflare-wan/configuration/appliance/">Magic WAN Connector</a> to work in a static IP configuration.</p>
<p>This local method does not require having access to a DHCP Internet connection. However, it does require being comfortable with using tools to access the serial port on Magic WAN Connector as well as using a serial terminal client to access the Connector's environment.</p>
<p>For more details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#bootstrap-via-serial-console">WAN with a static IP address</a>.</p>


<h2 id="2025-02-08">2025-02-08</h2>

<strong>Open email links with Security Center</strong>

<p>You can now investigate links in emails with Cloudflare Security Center to generate a report containing a myriad of technical details: a phishing scan, SSL certificate data, HTTP request and response data, page performance data, DNS records, what technologies and libraries the page uses, and more.</p>
<p><img src="/assets/upstream/images/changelog/email-security/Open-Links-Security-Center.png" alt="Open links in Security Center" /></p>
<p>From <strong>Investigation</strong>, go to <strong>View details</strong>, and look for the <strong>Links identified</strong> section. Select <strong>Open in Security Center</strong> next to each link. <strong>Open in Security Center</strong> allows your team to quickly generate a detailed report about the link with no risk to the analyst or your environment.</p>
<p>For more details, refer to <a href="/cloudflare-one/email-security/investigation/search-email/#open-links">Open links</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2025-02-03">2025-02-03</h2>

<strong>Block files that are password-protected, compressed, or otherwise unscannable.</strong>

<p>Gateway HTTP policies can now block files that are password-protected, compressed, or otherwise unscannable.</p>
<p>These unscannable files are now matched with the <a href="/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types">Download and Upload File Types traffic selectors</a> for HTTP policies:</p>
<ul>
<li>Password-protected Microsoft Office document</li>
<li>Password-protected PDF</li>
<li>Password-protected ZIP archive</li>
<li>Unscannable ZIP archive</li>
</ul>
<p>To get started inspecting and modifying behavior based on these and other rules, refer to <a href="/cloudflare-one/traffic-policies/get-started/http/">HTTP filtering</a>.</p>


<h2 id="2025-01-20">2025-01-20</h2>

<strong>Detect source code leaks with Data Loss Prevention</strong>

<p>You can now detect source code leaks with Data Loss Prevention (DLP) with predefined checks against common programming languages.</p>
<p>The following programming languages are validated with natural language processing (NLP).</p>
<ul>
<li>C</li>
<li>C++</li>
<li>C#</li>
<li>Go</li>
<li>Haskell</li>
<li>Java</li>
<li>JavaScript</li>
<li>Lua</li>
<li>Python</li>
<li>R</li>
<li>Rust</li>
<li>Swift</li>
</ul>
<p>DLP also supports confidence level for <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#source-code">source code profiles</a>.</p>
<p>For more details, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a>.</p>


<h2 id="2025-01-15">2025-01-15</h2>

<strong>Export SSH command logs with Access for Infrastructure using Logpush</strong>

<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2025-01-15-ssh-logs-and-logpush-availability">Availability</h4>
@markup("md", "content/.markup/bodies/17614.md")</aside>
<p>Cloudflare now allows you to send SSH command logs to storage destinations configured in <a href="/logs/logpush/">Logpush</a>, including third-party destinations. Once exported, analyze and audit the data as best fits your organization! For a list of available data fields, refer to the <a href="/logs/logpush/logpush-job/datasets/account/ssh_logs/">SSH logs dataset</a>.</p>
<p>To set up a Logpush job, refer to <a href="/cloudflare-one/insights/logs/logpush/">Logpush integration</a>.</p>


<h2 id="2024-12-20">2024-12-20</h2>

<strong>Escalate user submissions</strong>

<p>After you triage your users' submissions (that are machine reviewed), you can now escalate them to our team for reclassification (which are instead human reviewed). User submissions from the submission alias, PhishNet, and our API can all be escalated.</p>
<p><img src="/assets/upstream/images/changelog/email-security/Escalate.png" alt="Escalate" /></p>
<p>From <strong>Reclassifications</strong>, go to <strong>User submissions</strong>. Select the three dots next to any of the user submissions, then select <strong>Escalate</strong> to create a team request for reclassification. The Cloudflare dashboard will then show you the submissions on the <strong>Team Submissions</strong> tab.</p>
<p>Refer to <a href="/cloudflare-one/email-security/submissions/user-submissions/">User submissions</a> to learn more about this feature.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2024-12-19">2024-12-19</h2>

<strong>Increased transparency for phishing email submissions</strong>

<p>You now have more transparency about team and user submissions for phishing emails through a <strong>Reclassification</strong> tab in the Zero Trust dashboard.</p>
<p>Reclassifications happen when users or admins <a href="/cloudflare-one/email-security/settings/phish-submissions/">submit a phish</a> to Email security. Cloudflare reviews and - in some cases - reclassifies these emails based on improvements to our machine learning models.</p>
<p>This new tab increases your visibility into this process, allowing you to view what submissions you have made and what the outcomes of those submissions are.</p>
<p><img src="/assets/upstream/images/changelog/email-security/reclassifications-tab.png" alt="Use the Reclassification area to review submitted phishing emails" /></p>


<h2 id="2024-12-19-1">2024-12-19</h2>

<strong>Troubleshoot tunnels with diagnostic logs</strong>

<p>The latest <code>cloudflared</code> build <a href="https://github.com/cloudflare/cloudflared/releases/tag/2024.12.2">2024.12.2</a> introduces the ability to collect all the diagnostic logs needed to troubleshoot a <code>cloudflared</code> instance.</p>
<p>A diagnostic report collects data from a single instance of <code>cloudflared</code> running on the local machine and outputs it to a <code>cloudflared-diag</code> file.</p>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/">Diagnostic logs</a>.</p>


<h2 id="2024-12-17">2024-12-17</h2>

<strong>Establish BGP peering over Direct CNI circuits</strong>

<p>Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using a Direct CNI on-ramp.</p>
<p>Using BGP peering allows customers to:</p>
<ul>
<li>Automate the process of adding or removing networks and subnets.</li>
<li>Take advantage of failure detection and session recovery features.</li>
</ul>
<p>With this functionality, customers can:</p>
<ul>
<li>Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via CNI.</li>
<li>Secure the session by MD5 authentication to prevent misconfigurations.</li>
<li>Exchange routes dynamically between their devices and their Magic routing table.</li>
</ul>
<p>Refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes">Magic WAN BGP peering</a> or <a href="/magic-transit/how-to/configure-routes/#configure-bgp-routes">Magic Transit BGP peering</a> to learn more about this feature and how to set it up.</p>


<h2 id="2024-12-05">2024-12-05</h2>

<strong>Generate customized terraform files for building cloud network on-ramps</strong>

<p>You can now generate customized terraform files for building cloud network on-ramps to <a href="/cloudflare-wan/">Magic WAN</a>.</p>
<p><a href="/multi-cloud-networking/">Magic Cloud</a> can scan and discover existing network resources and generate the required terraform files to automate cloud resource deployment using their existing infrastructure-as-code workflows for cloud automation.</p>
<p>You might want to do this to:</p>
<ul>
<li>Review the proposed configuration for an on-ramp before deploying it with Cloudflare.</li>
<li>Deploy the on-ramp using your own infrastructure-as-code pipeline instead of deploying it with Cloudflare.</li>
</ul>
<p>For more details, refer to <a href="/multi-cloud-networking/cloud-on-ramps/#set-up-with-terraform">Set up with Terraform</a>.</p>


<h2 id="2024-11-22">2024-11-22</h2>

<strong>Find security misconfigurations in your AWS cloud environment</strong>

<p>You can now use CASB to find security misconfigurations in your AWS cloud environment using <a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention</a>.</p>
<p>You can also <a href="/cloudflare-one/integrations/cloud-and-saas/aws-s3/#compute-account">connect your AWS compute account</a> to extract and scan your S3 buckets for sensitive data while avoiding egress fees. CASB will scan any objects that exist in the bucket at the time of configuration.</p>
<p>To connect a compute account to your AWS integration:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Cloud &amp; SaaS findings</strong> &gt; <strong>Integrations</strong>.</li>
<li>Find and select your AWS integration.</li>
<li>Select <strong>Open connection instructions</strong>.</li>
<li>Follow the instructions provided to connect a new compute account.</li>
<li>Select <strong>Refresh</strong>.</li>
</ol>


<h2 id="2024-11-21">2024-11-21</h2>

<strong>Improved non-English keyboard support</strong>

<p>You can now type in languages that use diacritics (like á or ç) and character-based scripts (such as Chinese, Japanese, and Korean) directly within the remote browser. The isolated browser now properly recognizes non-English keyboard input, eliminating the need to copy and paste content from a local browser or device.</p>


<h2 id="2024-11-08">2024-11-08</h2>

<strong>Use Logpush for Email security user actions</strong>

<p>You can now send user action logs for Email security to an endpoint of your choice with Cloudflare Logpush.</p>
<p>Filter logs matching specific criteria you have set or select from multiple fields you want to send. For all users, we will log the date and time, user ID, IP address, details about the message they accessed, and what actions they took.</p>
<p>When creating a new Logpush job, remember to select <strong>Audit logs</strong> as the dataset and filter by:</p>
<ul>
<li><strong>Field</strong>: <code>&quot;ResourceType&quot;</code></li>
<li><strong>Operator</strong>: <code>&quot;starts with&quot;</code></li>
<li><strong>Value</strong>: <code>&quot;email_security&quot;</code>.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/email-security/Logpush-User-Actions.png" alt="Logpush-user-actions" /></p>
<p>For more information, refer to <a href="/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-user-action-logs">Enable user action logs</a>.</p>
<p>This feature is available across all Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2024-10-02">2024-10-02</h2>

<strong>Search for custom rules using rule name and/or ID</strong>

<p>The Magic Firewall dashboard now allows you to search custom rules using the rule name and/or ID.</p>
<ol>
<li>Log into the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>Analytics &amp; Logs</strong> &gt; <strong>Network Analytics</strong>.</li>
<li>Select <strong>Magic Firewall</strong>.</li>
<li>Add a filter for <strong>Rule ID</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/changelog/cloudflare-network-firewall/search-with-rule-id.png" alt="Search for firewall rules with rule IDs" /></p>
<p>Additionally, the rule ID URL link has been added to Network Analytics.</p>


<h2 id="2024-10-01">2024-10-01</h2>

<strong>Eliminate long-lived credentials and enhance SSH security with Cloudflare Access for Infrastructure</strong>

<p>Organizations can now eliminate long-lived credentials from their SSH setup and enable strong multi-factor authentication for SSH access, similar to other Access applications, all while generating access and command logs.</p>
<p>SSH with <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure</a> uses short-lived SSH certificates from Cloudflare, eliminating SSH key management and reducing the security risks associated with lost or stolen keys. It also leverages a common deployment model for Cloudflare One customers: <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-device-client/">WARP-to-Tunnel</a>.</p>
<p>SSH with Access for Infrastructure enables you to:</p>
<ul>
<li><strong>Author fine-grained policy</strong> to control who may access your SSH servers, including specific ports, protocols, and SSH users.</li>
<li><strong>Monitor infrastructure access</strong> with Access and SSH command logs, supporting regulatory compliance and providing visibility in case of security breach.</li>
<li><strong>Preserve your end users' workflows.</strong> SSH with Access for Infrastructure supports native SSH clients and does not require any modifications to users’ SSH configs.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/access/infrastructure-app.png" alt="Example of an infrastructure Access application" /></p>
<p>To get started, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">SSH with Access for Infrastructure</a>.</p>


<h2 id="2024-06-17">2024-06-17</h2>

<strong>Exchange user risk scores with Okta</strong>

<p>Beyond the controls in <a href="/cloudflare-one/">Zero Trust</a>, you can now <a href="/cloudflare-one/team-and-resources/users/risk-score/#send-risk-score-to-okta">exchange user risk scores</a> with Okta to inform SSO-level policies.</p>
<p>First, configure Cloudflare One to send user risk scores to Okta.</p>
<ol>
<li>Set up the <a href="/cloudflare-one/integrations/identity-providers/okta/">Okta SSO integration</a>.</li>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</li>
<li>In <strong>Your identity providers</strong>, locate your Okta integration and select <strong>Edit</strong>.</li>
<li>Turn on <strong>Send risk score to Okta</strong>.</li>
<li>Select <strong>Save</strong>.</li>
<li>Upon saving, Cloudflare One will display the well-known URL for your organization. Copy the value.</li>
</ol>
<p>Next, configure Okta to receive your risk scores.</p>
<ol>
<li>On your Okta admin dashboard, go to <strong>Security</strong> &gt; <strong>Device Integrations</strong>.</li>
<li>Go to <strong>Receive shared signals</strong>, then select <strong>Create stream</strong>.</li>
<li>Name your integration. In <strong>Set up integration with</strong>, choose <em>Well-known URL</em>.</li>
<li>In <strong>Well-known URL</strong>, enter the well-known URL value provided by Cloudflare One.</li>
<li>Select <strong>Create</strong>.</li>
</ol>


<h2 id="2024-06-16">2024-06-16</h2>

<strong>Explore product updates for Cloudflare One</strong>

<p>Welcome to your new home for product updates on <a href="/cloudflare-one/">Cloudflare One</a>.</p>
<p>Our <a href="/changelog/">new changelog</a> lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.</p>
<p>If you are looking for older product updates, refer to the following locations.</p>
<details class="nb-details" open><summary>Older product updates</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17707.md")</div></details>


