---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/cloudflare-one/
  description: '2026-09-15'
  full_title: Cloudflare One changelog | Cloudflare Docs
  head_html: <title>Cloudflare One changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-15"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cloudflare One changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-15"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/#page","headline":"Cloudflare One changelog | Cloudflare Docs","description":"2026-09-15","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/cloudflare-one/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="access-for-infrastructure-now-supports-tagged-targets-and-tag-based-target-criteria"><a href="/changelog/post/2026-09-15-infrastructure-target-tags/">Access for Infrastructure now supports tagged targets and tag-based target criteria</a></h2>
<p><em>2026-09-15</em></p>
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


<h2 id="require-fresh-authentication-for-saml-identity-providers"><a href="/changelog/post/2026-09-14-saml-force-authentication/">Require fresh authentication for SAML identity providers</a></h2>
<p><em>2026-09-14</em></p>
<p>Cloudflare Access can now request fresh authentication from a SAML identity provider for every login. Turn on <strong>Require reauthentication</strong> in the Cloudflare dashboard, or set <code>force_authn</code> to <code>true</code> through the API. Access will then set <code>ForceAuthn</code> to <code>true</code> in signed and unsigned SAML authentication requests.</p>
<p>This option is useful when an application requires users to reauthenticate at the identity provider instead of relying on an existing identity provider session. The default value is <code>false</code>.</p>
<p>For configuration details, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#require-fresh-authentication-at-the-identity-provider">Require fresh authentication at the identity provider</a>.</p>


<h2 id="discover-where-sensitive-data-goes-before-you-create-a-data-loss-prevention-policy"><a href="/changelog/post/2026-09-14-passive-detection/">Discover where sensitive data goes before you create a Data Loss Prevention policy</a></h2>
<p><em>2026-09-14</em></p>
<p><strong>Passive Detection</strong> for <a href="/cloudflare-one/data-loss-prevention/">Cloudflare Data Loss Prevention (DLP)</a> lets you learn from your Gateway traffic before deciding what to log or block. Discover the sensitive data types in sampled traffic, explore their destinations, and use the findings to build policies around your organization's needs.</p>
<p>The dashboard brings together detections from sampled HTTP request and response bodies. Select an entry to follow its detections over time, review destinations, and check policy coverage. You do not need a Gateway DLP policy to get these insights, and existing Gateway policies continue to apply.</p>
<p><img src="/assets/upstream/images/changelog/dlp/passive-detection.gif" alt="Passive Detection dashboard showing detection totals, data type distribution, policy coverage, and detection entries" /></p>
<p>Passive Detection is generally available. The detection entries available to your account depend on your <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">Zero Trust plan</a>.</p>
<p>To get started, refer to the <a href="/cloudflare-one/data-loss-prevention/passive-detection/">Passive Detection documentation</a>.</p>


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


<h2 id="improved-ios-tap-to-type-experience-for-browser-isolation"><a href="/changelog/post/2026-09-09-ios-tap-to-type/">Improved iOS tap-to-type experience for Browser Isolation</a></h2>
<p><em>2026-09-09</em></p>
<p><a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> has improved the tap-to-type experience for users on iOS devices.</p>
<p>Previously, Browser Isolation displayed a full-screen overlay with the message <code>tap to type</code> when users focused a text field. The prompt now appears inline over the focused text field, reducing disruption when users enter text in isolated sessions.</p>
<p>If the focused text field is too small to display the full prompt, Browser Isolation displays a keyboard icon in the center of the text field instead.</p>
<p><img src="/assets/upstream/images/cloudflare-one/rbi/tap-to-type.jpg" alt="Inline tap-to-type prompt over a focused text field in Browser Isolation" /></p>
<p>iOS users should tap twice to begin entering text. This update applies automatically to Browser Isolation sessions on iOS.</p>
<p>For more information on why this interaction is required, refer to <a href="/cloudflare-one/remote-browser-isolation/known-limitations/#ios">iOS limitations</a>.</p>


<h2 id="new-casb-integration-for-zoom"><a href="/changelog/post/2026-09-09-casb-zoom-integration/">New CASB integration for Zoom</a></h2>
<p><em>2026-09-09</em></p>
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


<h2 id="define-custom-applications-for-breakout-and-prioritized-traffic-from-the-cloudflare-one-appliance-dashboard"><a href="/changelog/post/2026-09-02-appliance-custom-application-traffic-steering/">Define custom applications for breakout and prioritized traffic from the Cloudflare One Appliance dashboard</a></h2>
<p><em>2026-09-02</em></p>
<p>You can now define <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#create-edit-or-delete-a-custom-application">custom applications</a> for <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/">breakout</a> and <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/">prioritized</a> traffic on the <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> directly from the dashboard, without calling the API.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-09-01-appliance-custom-application-traffic-steering.gif" alt="Adding a custom application by hostname, IP subnet, and source subnet from the Traffic Steering tab of an appliance profile" /></p>
<ul>
<li>In <strong>Traffic Steering</strong> &gt; <strong>Breakout traffic</strong> or <strong>Prioritized traffic</strong>, select <strong>Assign application traffic</strong> &gt; <strong>Add</strong> to create a custom application matched by <strong>Hostnames</strong>, <strong>IP subnets</strong>, and/or the new <strong>Source subnets</strong> field, alongside Cloudflare-managed applications.</li>
<li>Edit or delete an existing custom application from the same panel, no API round-trip required.</li>
<li><strong>Source subnets</strong> lets you match traffic by its source IP range, complementing the existing <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source">source LAN interface breakout criteria</a>.</li>
</ul>
<p>This complements the existing API and Terraform workflow for managing applications.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/">Breakout traffic</a> and <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/">Prioritized traffic</a>.</p>


<h2 id="configure-dhcp-options-from-the-dashboard-on-cloudflare-one-appliance"><a href="/changelog/post/2026-09-02-appliance-dhcp-options-ui/">Configure DHCP options from the dashboard on Cloudflare One Appliance</a></h2>
<p><em>2026-09-02</em></p>
<p>You can now configure <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">custom DHCP options</a> directly from the dashboard when the <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> is acting as the DHCP server for a LAN.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-09-01-appliance-dhcp-options-ui.gif" alt="Adding a custom DHCP option to a LAN's DHCP server from the Network Configuration tab of an appliance profile" /></p>
<ul>
<li>In <strong>LAN configuration</strong>, under <strong>DHCP server options</strong>, select <strong>Add DHCP option</strong> to choose from common options for PXE / iPXE boot, VoIP phone provisioning, and vendor-specific configuration, or select <strong>Add custom option</strong> to enter your own option code, type, and value.</li>
<li>This complements the existing <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/#configure-dhcp-options">API and Terraform workflow</a> for configuring DHCP options.</li>
</ul>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">DHCP server options</a>.</p>


<h2 id="create-multiple-cloudflare-tunnel-and-cloudflare-mesh-routes-at-once"><a href="/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/">Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once</a></h2>
<p><em>2026-09-02</em></p>
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


<h2 id="load-balancing-now-supports-pool-sets"><a href="/changelog/post/2026-08-31-pool-sets/">Load Balancing now supports pool sets</a></h2>
<p><em>2026-08-31</em></p>
<p>Cloudflare Load Balancing now supports pool sets through the API. Pool sets combine geographic matching with location-specific traffic steering. One load balancer can now use different routing behavior for different locations.</p>
<p>Each pool set can match a Cloudflare data center, country, or region. It then supplies the candidate pools and can apply its own steering policy, pool weights, and fallback pool. Cloudflare evaluates pool sets in array order and applies the first matching pool set.</p>
<p>For example, this pool set uses Dynamic Latency steering for traffic from Germany:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;pool_sets&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;germany-lowest-latency&quot;,&#10;			&quot;match&quot;: { &quot;topology&quot;: { &quot;countries&quot;: [&quot;DE&quot;] } },&#10;			&quot;overrides&quot;: {&#10;				&quot;pools&quot;: [&#10;					&quot;0930eec54a4c7ae6616985b79f678210&quot;,&#10;					&quot;c8b4f5a6d7e84910a2b3c4d5e6f70819&quot;&#10;				],&#10;				&quot;steering_policy&quot;: &quot;dynamic_latency&quot;&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Use pool sets for active-active traffic distribution, location-specific failover, and regional routing policies. For proxied traffic, a pool set can also return a fixed HTTP response instead of selecting a pool.</p>
<p>For configuration details and more examples, refer to <a href="/load-balancing/understand-basics/traffic-steering/pool-sets/">Pool sets</a>.</p>


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


<h2 id="access-service-token-secrets-use-a-scannable-format"><a href="/changelog/post/2026-08-26-service-token-secret-format/">Access service token secrets use a scannable format</a></h2>
<p><em>2026-08-26</em></p>
<p>Cloudflare Access service token Client Secrets created on or after August 26, 2026, use the format <code>cfast_[40 alphanumeric characters][8-character checksum]</code>. The prefix and checksum make these credentials easier for secret scanning tools to identify with fewer false positives.</p>
<p>Existing service token secrets continue to work and do not require rotation. Both formats use the same Client ID and the same <code>CF-Access-Client-Id</code> and <code>CF-Access-Client-Secret</code> authentication headers.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Service tokens</a>.</p>


<h2 id="grace-periods-for-service-token-rotation"><a href="/changelog/post/2026-08-25-service-token-rotation-grace-periods/">Grace periods for service token rotation</a></h2>
<p><em>2026-08-25</em></p>
<p>Cloudflare Access administrators can now choose a grace period when rotating a service token secret. Both secrets remain valid during the grace period, giving administrators time to update services without interrupting authentication.</p>
<p>The dashboard offers grace periods from one hour to 30 days. Administrators can also revoke the previous secret immediately. The API accepts an RFC 3339 expiration time for custom rotation schedules.</p>
<p>For configuration instructions, refer to <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/#rotate-service-token-secrets">Rotate service token secrets</a>.</p>


<h2 id="temporarily-turn-off-access-service-tokens"><a href="/changelog/post/2026-08-25-service-token-status-controls/">Temporarily turn off Access service tokens</a></h2>
<p><em>2026-08-25</em></p>
<p>Cloudflare Access administrators can now temporarily turn off service tokens without deleting them. A disabled token cannot authenticate, but its configuration remains available so administrators can turn it on again later.</p>
<p>Turning off a token also stops any previous secret in an active rotation grace period. Use this control to contain suspected credential exposure or pause an automated service.</p>
<p>For configuration instructions, refer to <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/#turn-a-service-token-on-or-off">Turn a service token on or off</a>.</p>


<h2 id="mcp-server-portals-support-mcp-2026-07-28-specification"><a href="/changelog/post/2026-08-25-mcp-portals-mcp-2026-07-28/">MCP server portals support MCP 2026-07-28 specification</a></h2>
<p><em>2026-08-25</em></p>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support the stateless MCP <code>2026-07-28</code> specification for client and upstream server connections.</p>
<p>The portal's <code>/mcp</code> endpoint automatically accepts stateless MCP <code>2026-07-28</code> requests and earlier 2025 Streamable HTTP clients. When the portal connects to an upstream Streamable HTTP server, it checks for MCP <code>2026-07-28</code> support and falls back to the 2025 handshake when needed. Client and upstream protocol selection are independent, so clients and servers can upgrade separately without portal configuration changes.</p>
<p>SSE connections continue to use the legacy protocol. For details, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#transport">MCP server portal transport and protocol compatibility</a>.</p>


<h2 id="download-the-cloudflare-one-virtual-appliance-for-your-hypervisor-from-the-dashboard"><a href="/changelog/post/2026-08-24-virtual-appliance-self-serve-download/">Download the Cloudflare One Virtual Appliance for your hypervisor from the dashboard</a></h2>
<p><em>2026-08-24</em></p>
<p>When you register a <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Virtual Appliance</a>, you can now select your hypervisor and download the appliance directly from the dashboard — no need to look up asset URLs.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-08-24-virtual-appliance-self-serve-download.png" alt="Selecting a hypervisor and downloading the Cloudflare One Virtual Appliance from the Connectors page" /></p>
<ul>
<li>On the <strong>Connectors</strong> page, select <strong>Add an appliance</strong>, choose <strong>Virtual appliance</strong>, then select your hypervisor: <strong>VMware ESXi</strong>, <strong>Proxmox</strong>, or <strong>libvirt/KVM</strong>.</li>
<li>Download the OVA image (VMware ESXi) or the install script (Proxmox and libvirt/KVM) for the selected hypervisor.</li>
<li>Use <strong>View setup guide</strong> to open deployment instructions for your platform.</li>
</ul>
<p>This complements the existing self-serve <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key">registration and license key generation</a> in the dashboard.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#configure-a-virtual-machine">Configure a Cloudflare One Virtual Appliance</a>.</p>


<h2 id="automatically-remediate-microsoft-365-and-google-workspace-findings-with-api-based-casb-remediation-policies"><a href="/changelog/post/2026-08-21-casb-policies/">Automatically remediate Microsoft 365 and Google Workspace findings with API-based CASB remediation policies</a></h2>
<p><em>2026-08-21</em></p>
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


<h2 id="test-data-loss-prevention-profiles-without-sending-traffic-through-gateway"><a href="/changelog/post/2026-08-21-dlp-test-scan/">Test Data Loss Prevention profiles without sending traffic through Gateway</a></h2>
<p><em>2026-08-21</em></p>
<p><strong>Test scan</strong> lets you check how <a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention (DLP)</a> evaluates sample content before you apply a profile to production traffic. Paste text, upload a file, or upload a HAR file, then select the profiles you want to test.</p>
<p><img src="/assets/upstream/images/changelog/dlp/dlp-test-scan.gif" alt="Test scan results showing matched profiles, detection entries, and match context" /></p>
<p>Test scan sends content directly to the DLP scanner. Gateway policies are not evaluated, no traffic passes through Gateway, and no Gateway activity logs are created. Results include matched profiles, detection entries, confidence levels, match context, proximity keywords, file metadata, antivirus status, and OCR output.</p>
<p>Test scan is available to all Cloudflare Zero Trust customers. Profile availability depends on your <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">Zero Trust plan</a>.</p>
<p>For more details, refer to the <a href="/cloudflare-one/data-loss-prevention/test-scan/">Test scan documentation</a>.</p>


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


<h2 id="access-resource-lists-now-support-resource-scoped-roles"><a href="/changelog/post/2026-08-19-granular-permissions-resource-lists/">Access resource lists now support resource-scoped roles</a></h2>
<p><em>2026-08-19</em></p>
<p>Members with only resource-scoped Access roles can now open Access resource list pages in the Cloudflare dashboard and call list endpoints in the API. They no longer need an additional account-scoped read-only role to list resources.</p>
<p>The dashboard and API return only resources included in the member's permission policy scopes. Filtering applies to Access applications, policies, service tokens, and identity providers. This allows administrators to delegate specific Access resources without granting account-wide visibility. Previously, the dashboard blocked these list pages and API list requests returned <code>403</code> responses.</p>
<p>For members with the Cloudflare Access App Admin role, policy lists include policies attached directly to the selected application. Reusable policies appear only when the member has the Cloudflare Access Policy Admin role for those policies.</p>
<p>For role definitions and assignment details, refer to <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">Resource-scoped roles</a> and <a href="/fundamentals/manage-members/scope/">Role scopes</a>.</p>


<h2 id="threat-intel-lists-supported-in-unified-routing"><a href="/changelog/post/2026-08-19-unified-routing-threat-lists/">Threat Intel Lists supported in Unified Routing</a></h2>
<p><em>2026-08-19</em></p>
<p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> Threat Intel Lists are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. This feature requires a Cloudflare Advanced Network Firewall subscription.</p>
<p>Support for additional features - Rate Limiting and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 13</span><a class="pagination-next" rel="next" href="/changelog/product-group/cloudflare-one/2/">Next</a></nav>
