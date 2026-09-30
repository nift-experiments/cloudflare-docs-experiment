---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/cloudflare-one/4/
  description: '2026-06-23'
  full_title: Cloudflare One changelog - page 4 | Cloudflare Docs
  head_html: <title>Cloudflare One changelog - page 4 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-06-23"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/4/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cloudflare One changelog - page 4"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-06-23"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/4/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/4/#page","headline":"Cloudflare One changelog - page 4 | Cloudflare Docs","description":"2026-06-23","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/4/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/cloudflare-one/4/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="regionalized-ip-bindings-for-regional-services"><a href="/changelog/post/2026-06-23-regionalized-ip-bindings/">Regionalized IP Bindings for Regional Services</a></h2>
<p><em>2026-06-23</em></p>
<p>Regional Services now supports <strong>Regionalized IP Bindings</strong>, letting you regionalize traffic at the IP layer for prefixes you bring to Cloudflare through <a href="/byoip/">Bring Your Own IP (BYOIP)</a>.</p>
<p>Where <a href="/data-localization/regional-services/regional-hostnames/">Regional Hostnames</a> regionalize traffic by hostname, Regionalized IP Bindings let you bind a CIDR from one of your prefixes to a region — ideal for address-map deployments and any service you address by IP rather than hostname. Cloudflare then terminates TLS and processes traffic to those addresses only within the data centers in that region.</p>
<p>Regionalized IP Bindings requires the Regional Services and Regional Services for BYOIP entitlements. Contact your account team to enable them.</p>
<p>To get started, refer to <a href="/data-localization/regional-services/ip-bindings/">Regionalized IP Bindings</a>.</p>


<h2 id="manage-all-your-routes-from-one-page-in-the-dashboard"><a href="/changelog/post/2026-06-19-unified-routes-page/">Manage all your routes from one page in the dashboard</a></h2>
<p><em>2026-06-19</em></p>
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


<h2 id="cloudflare-identity-provider-is-now-the-default-for-new-accounts"><a href="/changelog/post/2026-06-18-cloudflare-idp-default/">Cloudflare identity provider is now the default for new accounts</a></h2>
<p><em>2026-06-18</em></p>
<p>When you create a new Zero Trust organization, Cloudflare now adds the <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">Cloudflare identity provider</a> as your default login method. Previously, new organizations started with <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time PIN (OTP)</a>.</p>
<p>With the Cloudflare identity provider, your users authenticate using their existing Cloudflare account credentials, and authentication is restricted to members of your account. You can still add OTP or connect any <a href="/cloudflare-one/integrations/identity-providers/">third-party identity provider</a> whenever you need to.</p>
<p>This change only applies to newly created accounts. Existing organizations keep the login methods they already have configured. If you would like to use the Cloudflare Identity Provider in an existing account, you must enable it.</p>


<h2 id="define-custom-topics-for-ai-prompt-protection"><a href="/changelog/post/2026-06-11-custom-ai-prompt-topics/">Define custom topics for AI prompt protection</a></h2>
<p><em>2026-06-11</em></p>
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


<h2 id="filter-workers-public-internet-traffic-using-gateway-policies"><a href="/changelog/post/2026-06-05-gateway-egress/">Filter Workers' public Internet traffic using Gateway policies</a></h2>
<p><em>2026-06-05</em></p>
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


<h2 id="share-identity-providers-across-accounts-with-idp-federation"><a href="/changelog/post/2026-06-04-idp-federation/">Share identity providers across accounts with IdP federation</a></h2>
<p><em>2026-06-04</em></p>
<p>Cloudflare Access now supports <a href="/cloudflare-one/integrations/identity-providers/idp-federation/">IdP federation</a>, which allows organizations to share a single identity provider across multiple Cloudflare accounts.</p>
<p>Instead of configuring the same IdP (for example, Okta or Entra ID) separately in every account, you configure it once in a source account and share it with the other accounts in your organization. Each recipient account gets a read-only IdP connection that routes authentication back to the source account through a bridge — a hidden application in the source account that brokers the cross-account login. End users sign in with their existing IdP credentials, and each account's Access policies evaluate the resulting identity just like any other IdP login.</p>
<p>Key capabilities:</p>
<ul>
<li><strong>One IdP, many accounts</strong> — Configure your IdP once and share it with all accounts in your organization.</li>
<li><strong>Lifecycle management</strong> — As accounts join or leave your Cloudflare organization, their IdP connections are provisioned and removed automatically — no manual cleanup required.</li>
<li><strong>Immutable recipient connections</strong> — IdP connections in recipient accounts cannot be accidentally modified or deleted.</li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/integrations/identity-providers/idp-federation/">IdP federation</a>.</p>


<h2 id="saml-assertion-encryption-for-identity-providers"><a href="/changelog/post/2026-06-03-saml-assertion-encryption/">SAML assertion encryption for identity providers</a></h2>
<p><em>2026-06-03</em></p>
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


<h2 id="cisco-ios-xe"><a href="/changelog/post/2026-06-02-cisco-ios-xe/">Cisco IOS XE</a></h2>
<p><em>2026-06-02</em></p>
<p>The Cisco IOS XE third-party integration guide for Cloudflare WAN has been updated to include:</p>
<ul>
<li>Post Quantum Cryptography (PQC)</li>
<li>Policy-Based Routing (PBR)</li>
<li>IP Service Level Agreement (IP SLA)</li>
</ul>
<p>This link will take you directly to the updated <a href="/cloudflare-wan/configuration/third-party/cisco-ios-xe/">Cisco IOS XE</a> guide.</p>


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


<h2 id="tool-and-prompt-aliases-for-mcp-server-portals"><a href="/changelog/post/2026-05-28-mcp-portal-tool-prompt-aliases/">Tool and prompt aliases for MCP server portals</a></h2>
<p><em>2026-05-28</em></p>
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


<h2 id="high-availability-replica-management-for-cloudflare-mesh"><a href="/changelog/post/2026-05-28-mesh-ha-replica-ui/">High availability replica management for Cloudflare Mesh</a></h2>
<p><em>2026-05-28</em></p>
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


<h2 id="write-regex-using-natural-language-in-cloudflare-one"><a href="/changelog/post/2026-05-27-cloudy-regex-assistance/">Write regex using natural language in Cloudflare One</a></h2>
<p><em>2026-05-27</em></p>
<p><a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> policy selectors which support regular expressions can now be authored in the dashboard using natural language. When building a <a href="/cloudflare-one/traffic-policies/expression-syntax/">policy</a> with a regex-based selector (like <code>matches regex</code>), you can describe what you want to match in plain English and the Cloudflare Agent will generate and validate a corresponding regular expression.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/gateway-regex-ai-generation.png" alt="Write policy regex using natural language" /></p>
<p>To get started, select a regex-compatible selector in the <a href="/cloudflare-one/traffic-policies/">Gateway policy builder</a> and select the icon. You'll see an input field for natural language, such as &quot;any URL starting with /api/v1&quot; or &quot;.com, .net, and .app hosts which contain <code>gooogle</code> in the host.&quot;</p>
<p>You can also use the tool to explain existing regular expressions. If a policy already contains a regex pattern, you can instantly generate a plain-language description.</p>
<p>A built-in feedback mechanism allows you to rate each interaction to help improve output quality over time.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/">Cloudflare One firewall policies</a> and expect to see the same functionality supported soon in <a href="/cloudflare-one/data-loss-prevention/">Data loss prevention profiles</a>.</p>


<h2 id="cloudflare-tunnel-now-runs-connectivity-pre-checks-at-startup"><a href="/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/">Cloudflare Tunnel now runs connectivity pre-checks at startup</a></h2>
<p><em>2026-05-27</em></p>
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


<h2 id="granular-permissions-for-cloudflare-tunnel-and-cloudflare-mesh"><a href="/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/">Granular permissions for Cloudflare Tunnel and Cloudflare Mesh</a></h2>
<p><em>2026-05-21</em></p>
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


<h2 id="cloudflare-as-identity-provider-and-account-membership-selector"><a href="/changelog/post/2026-05-19-cloudflare-as-identity-provider/">Cloudflare as identity provider and account membership selector</a></h2>
<p><em>2026-05-19</em></p>
<p>Cloudflare Access now supports using Cloudflare itself as an <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">identity provider</a>. If you publish an Access application and select Cloudflare as the login method, users can sign in with their existing Cloudflare account — no one-time PINs, no third-party IdP configuration, and no shared email inboxes. Authentication is backed by Cloudflare's own account security (including multi-factor authentication), making it both simpler to set up and more secure than OTP-based login for most use cases.</p>
<p>Cloudflare is now the <strong>default identity provider for all newly created Zero Trust accounts</strong>, replacing One-time PIN.</p>
<p>This also enables two new capabilities:</p>
<ul>
<li><strong>Cloudflare Account Member selector</strong> — A new <a href="/cloudflare-one/access-controls/policies/#cloudflare-access-selectors">policy selector</a> that matches users based on their membership in a Cloudflare account. You can target the current account or specify a different account ID for cross-account access scenarios.</li>
<li><strong>Restrict to account members</strong> — An identity provider configuration option that limits authentication to users who are members of your Cloudflare account.</li>
</ul>
<p>To get started, add Cloudflare as an <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">identity provider</a> in your Zero Trust settings.</p>


<h2 id="casb-adds-support-for-claude-compliance-api"><a href="/changelog/post/2026-05-19-casb-claude-compliance-api/">CASB adds support for Claude Compliance API</a></h2>
<p><em>2026-05-19</em></p>
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


<h2 id="network-analytics-support-for-unified-routing"><a href="/changelog/post/2026-05-18-unified-routing-network-analytics/">Network Analytics support for Unified Routing</a></h2>
<p><em>2026-05-18</em></p>
<p><a href="/analytics/network-analytics/">Network Analytics</a> is now fully supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. Traffic that traverses Unified Routing onramps and offramps is now visible in Network Analytics with the same dimensions and filters as traffic on the standard data plane.</p>
<p>This closes a parity gap for customers who had moved tunnels onto Unified Routing and lost visibility into their dataplane traffic in the Network Analytics dashboard. No configuration change is required — analytics data is collected automatically for all accounts with Unified Routing enabled.</p>
<p>For the remaining beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<h2 id="refreshed-access-login-page"><a href="/changelog/post/2026-05-12-access-login-page-refresh/">Refreshed Access login page</a></h2>
<p><em>2026-05-12</em></p>
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


<h2 id="new-accounts-assigned-a-single-ipv4-anycast-address"><a href="/changelog/post/2026-05-12-single-anycast-ip-default/">New accounts assigned a single IPv4 anycast address</a></h2>
<p><em>2026-05-12</em></p>
<p>New Magic Transit and Cloudflare WAN accounts are now assigned a single IPv4 anycast address by default.</p>
<p>Cloudflare handles failures on its network automatically by advertising your endpoint IP from multiple nodes across many globally distributed data centers. To handle failures on your network, configure two tunnels from separate routers.</p>
<p>To request additional anycast IP addresses for your account, contact your account team.</p>
<p>For tunnel configuration guidance, refer to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a> for Cloudflare WAN or <a href="/magic-transit/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a> for Magic Transit.</p>


<h2 id="create-gateway-firewall-policies-with-natural-language"><a href="/changelog/post/2026-05-12-natural-language-policy-creation/">Create Gateway firewall policies with natural language</a></h2>
<p><em>2026-05-12</em></p>
<p>Cloudflare Gateway now supports natural language policy creation for <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS</a>, <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a>, and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> firewall policies. Administrators can describe the outcome they want in plain language, and Cloudflare will generate a complete policy rule that populates the policy builder form.</p>
<p><img src="/assets/upstream/images/changelog/gateway/gateway-create-with-ai.png" alt="Create with AI button on the Gateway firewall policies page" /></p>
<p>To create a policy with natural language, select <strong>Create with AI</strong> on any Gateway firewall policy tab. Choose a policy type, describe what the policy should do, and a fully configured rule will appear in the policy builder for review. You can edit any field before saving, or re-generate with a different prompt.</p>
<p>The generated policy incorporates your account context - including lists, DLP profiles, applications, and device posture checks - so that references to your existing resources resolve automatically.</p>
<p>A built-in feedback mechanism allows you to rate each generated policy and provide optional comments, which Cloudflare uses to improve output quality over time.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/">Gateway firewall policies</a>.</p>


<h2 id="cloudflare-one-client-for-linux-version-2026-4-1350-0"><a href="/changelog/post/2026-05-11-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.4.1350.0)</a></h2>
<p><em>2026-05-12</em></p>
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


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/cloudflare-one/3/">Previous</a><span>Page 4 of 13</span><a class="pagination-next" rel="next" href="/changelog/product-group/cloudflare-one/5/">Next</a></nav>
