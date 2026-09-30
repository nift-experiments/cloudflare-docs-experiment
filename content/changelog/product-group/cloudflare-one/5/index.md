---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/cloudflare-one/5/
  description: '2026-05-12'
  full_title: Cloudflare One changelog - page 5 | Cloudflare Docs
  head_html: <title>Cloudflare One changelog - page 5 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-05-12"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/5/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cloudflare One changelog - page 5"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-05-12"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/5/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/5/#page","headline":"Cloudflare One changelog - page 5 | Cloudflare Docs","description":"2026-05-12","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/5/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/cloudflare-one/5/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="cloudflare-one-client-for-macos-version-2026-4-1350-0"><a href="/changelog/post/2026-05-11-warp-macos-ga/">Cloudflare One Client for macOS (version 2026.4.1350.0)</a></h2>
<p><em>2026-05-12</em></p>
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


<h2 id="cloudflare-one-client-for-windows-version-2026-4-1350-0"><a href="/changelog/post/2026-05-11-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.4.1350.0)</a></h2>
<p><em>2026-05-12</em></p>
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


<h2 id="nat-t-support-for-ike-on-udp-port-500"><a href="/changelog/post/2026-05-11-nat-t-port-500/">NAT-T support for IKE on UDP port 500</a></h2>
<p><em>2026-05-11</em></p>
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


<h2 id="custom-dhcp-options-on-cloudflare-one-appliance"><a href="/changelog/post/2026-05-07-appliance-dhcp-options/">Custom DHCP options on Cloudflare One Appliance</a></h2>
<p><em>2026-05-07</em></p>
<p>When the Cloudflare One Appliance is acting as the DHCP server for a LAN, you can now configure custom DHCP options on the leases it issues. This unlocks workflows such as PXE / iPXE boot, VoIP phone provisioning, and vendor-specific client configuration.</p>
<p>Each option is defined by <code>option_number</code>, <code>value</code>, and one of four value types: <code>text</code>, <code>integer</code>, <code>hex</code>, or <code>ip</code>. Configurations are validated on the appliance before being applied — invalid configurations are rejected and the underlying error is returned to the API caller, so a bad option will not disrupt the live DHCP service.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">DHCP server options</a>.</p>


<h2 id="source-based-breakout-and-prioritization-on-cloudflare-one-appliance"><a href="/changelog/post/2026-05-07-appliance-source-based-breakout/">Source-based breakout and prioritization on Cloudflare One Appliance</a></h2>
<p><em>2026-05-07</em></p>
<p>Breakout and traffic prioritization rules on the Cloudflare One Appliance can now match by <strong>source</strong> in addition to destination application. You can pin breakout or priority behavior to:</p>
<ul>
<li>A source LAN interface — VLANs attached to that LAN are included automatically.</li>
<li>A source IP address, range, or CIDR block.</li>
</ul>
<p>This is the natural way to break out a guest VLAN to the local Internet, or to prioritize traffic from a specific subnet, without enumerating destination applications.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source">Breakout traffic</a>.</p>


<h2 id="self-serve-provisioning-of-cloudflare-one-virtual-appliance-via-api"><a href="/changelog/post/2026-05-07-virtual-appliance-self-serve-api/">Self-serve provisioning of Cloudflare One Virtual Appliance via API</a></h2>
<p><em>2026-05-07</em></p>
<p>You can now create, rotate, and delete Cloudflare One Virtual Appliance instances and their license keys directly via the API and Terraform.</p>
<ul>
<li>Create a virtual appliance and receive a license key: <code>POST /accounts/{account_id}/magic/connectors</code> with <code>device.provision_license: true</code>.</li>
<li>Rotate the license key for an existing virtual appliance: <code>PATCH /accounts/{account_id}/magic/connectors/{connector_id}</code> with <code>provision_license: true</code>. The previous key is immediately and irrevocably revoked.</li>
<li>Delete a virtual appliance to release the associated licensed device.</li>
</ul>
<p>The license key is returned in the response only once, at create or rotate time. Copy and store it securely.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a Cloudflare One Virtual Appliance</a>.</p>


<h2 id="cloudy-summaries-in-phishnet-o365"><a href="/changelog/post/2026-05-06-cloudy-summaries-in-phishnet_o365/">Cloudy Summaries in PhishNet O365</a></h2>
<p><em>2026-05-06T18:15:13+00:00</em></p>
<p>PhishNet users can now access <strong>Cloudy summaries</strong> directly within the email investigation experience. When reviewing a message in PhishNet, users will see an AI-generated summary that provides additional context and key details about the email.</p>
<p>These summaries help users quickly understand the nature of a message without needing to manually parse through headers, body content, and detection signals. Cloudy surfaces the most relevant information so users can make faster, more informed decisions about suspicious emails.</p>
<p><strong>These summaries are not trained on customer data.</strong> They are generated using the outputs of our existing detection models and analysis systems.</p>
<p>This feature is available for PhishNet with Office 365. Support for Gmail will be available by the end of the quarter.</p>


<h2 id="ipv6-cidr-routes-for-cloudflare-mesh"><a href="/changelog/post/2026-05-06-mesh-ipv6-routes/">IPv6 CIDR routes for Cloudflare Mesh</a></h2>
<p><em>2026-05-06</em></p>
<p><a href="/mesh/">Cloudflare Mesh</a> nodes now support IPv6 CIDR routes. You can advertise both IPv4 and IPv6 subnets through your Mesh nodes, making IPv6-only or dual-stack private networks reachable from any enrolled device.</p>
<p><img src="/assets/upstream/images/cloudflare-one/connections/mesh-ipv6-routes.png" alt="IPv6 CIDR routes on a Mesh node in the Cloudflare dashboard" /></p>
<p>To add an IPv6 route, follow the same steps as <a href="/mesh/features/routes/#add-a-route">adding an IPv4 route</a> — enter the IPv6 CIDR (for example, <code>fd00::/64</code>) when configuring the route in the <a href="https://dash.cloudflare.com/?to=/:account/mesh">dashboard</a> or via the API.</p>


<h2 id="post-quantum-ipsec-interoperability-with-third-party-devices"><a href="/changelog/post/2026-04-30-ipsec-post-quantum-third-party/">Post-quantum IPsec interoperability with third-party devices</a></h2>
<p><em>2026-04-30</em></p>
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


<h2 id="classify-sensitive-content-with-data-classification"><a href="/changelog/post/2026-04-30-data-classification/">Classify sensitive content with Data Classification</a></h2>
<p><em>2026-04-30</em></p>
<p>Cloudflare DLP now includes <strong>Data Classification</strong>, which lets administrators organize and label sensitive content using labels, templates, and reusable data classes.</p>
<p>With Data Classification, administrators can define labels such as sensitivity schemas and levels, and data tag groups and tags. Administrators can also build from Cloudflare-managed templates and create reusable data classes that combine detection entries, other data classes, sensitivity levels, and data tags.</p>
<p>You can then use those classifications in custom DLP profiles to identify the severity of sensitive content, understand where it exists, and apply that logic consistently across DLP profiles.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/data-classification/">Data Classification</a>.</p>


<h2 id="new-predefined-detection-entries-are-available"><a href="/changelog/post/2026-04-30-standalone-predefined-detection-entries/">New predefined detection entries are available</a></h2>
<p><em>2026-04-30</em></p>
<p>Cloudflare DLP now includes new predefined detection entries.</p>
<p>The expanded catalog includes detections for specific credential types, webhooks, addresses, tax identifiers, national IDs, financial data, and crypto wallets.</p>
<p>Examples include <code>GitHub PAT</code>, <code>OpenAI API Key</code>, <code>Slack Webhook</code>, <code>Discord Webhook</code>, <code>US Physical Address</code>, and <code>Bitcoin Wallet</code>.</p>
<p>For the full list, refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/predefined-detection-entries/">Predefined detection entries</a>.</p>


<h2 id="digital-experience-tests-to-authenticated-resources-and-enhanced-configuration"><a href="/changelog/post/2026-04-29-dex-tests-to-auth/">Digital experience tests to authenticated resources and enhanced configuration</a></h2>
<p><em>2026-04-29</em></p>
<p><a href="/cloudflare-one/insights/dex/tests/">Digital experience tests</a> now support testing applications protected by Cloudflare Access or third-party authentication. All authentication secrets are managed via <a href="/secrets-store/">Cloudflare Secret Store</a>.</p>
<p>Digital experience tests also have enhanced configuration options including:</p>
<ul>
<li>New HTTP methods (DELETE, PATCH, POST, PUT)</li>
<li>Secret Store headers, custom plain text headers, and custom request bodies</li>
<li>Advanced settings: follow redirects, response bodies, response headers, and allow untrusted certificates</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dex/dex_test_auth_config.png" alt="Digital experience test configuration for Cloudflare Access applications" />
<img src="/assets/upstream/images/changelog/dex/dex_test_enhanced_config.png" alt="Digital experience enhanced test configuration" /></p>


<h2 id="gateway-authorization-proxy-and-hosted-pac-files-are-now-generally-available"><a href="/changelog/post/2026-04-29-gateway-authorization-proxy-pac-files-ga/">Gateway Authorization Proxy and hosted PAC files are now generally available</a></h2>
<p><em>2026-04-29</em></p>
<p>The <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">Gateway Authorization Proxy</a> and <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file">hosted PAC files</a> are now generally available for all plan types.</p>
<p>Authorization proxy endpoints add an identity-aware option alongside the existing <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint">source IP proxy endpoints</a>, using <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> authentication to verify who a user is before applying Gateway filtering — without installing the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>. Cloudflare-hosted PAC files let you create and distribute PAC files directly from Cloudflare One on Cloudflare's global network.</p>
<p>These features are ideal for environments where deploying a device client is not an option, such as virtual desktops (VDI) or compliance-restricted endpoints.</p>
<p>To get started, refer to the <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints documentation</a>.</p>


<h2 id="internet-outage-notifications-for-devices"><a href="/changelog/post/2026-04-28-dex-internet-outage-notification/">Internet outage notifications for devices</a></h2>
<p><em>2026-04-28</em></p>
<p><a href="/cloudflare-one/insights/dex/">Digital Experience</a> will display a dashboard notification when an Internet outage or traffic anomaly may impact a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> device based on its geographic location or network connection.</p>
<p>This Internet outage and traffic anomaly data is pulled from <a href="https://radar.cloudflare.com/">Cloudflare Radar</a>. All Internet outage and traffic anomaly observations can be viewed in the <a href="https://radar.cloudflare.com/outage-center">Radar Outage Center</a>.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_radar_ux_notification.png" alt="Digital Experience Monitoring dashboard notification for Internet outage impacting Cloudflare One Client devices" />
<img src="/assets/upstream/images/changelog/dex/dex_radar_analytics.png" alt="Digital Experience Monitoring dashboard analytics for Internet outage impacting Cloudflare One Client devices" /></p>


<h2 id="cloudflare-one-client-speed-tests"><a href="/changelog/post/2026-04-28-dex-speed-test/">Cloudflare One Client speed tests</a></h2>
<p><em>2026-04-28</em></p>
<p>IT teams can now remotely run speed tests from the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> to Cloudflare's network edge.</p>
<p>Each speed test includes the following metrics:</p>
<ul>
<li>Internet speed: download and upload throughput</li>
<li>Latency: download, upload, unloaded latency, and jitter</li>
<li>Network quality score: video streaming, webchat/real-time communication (RTC)</li>
</ul>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Digital experience</strong> &gt; <strong>Diagnostics</strong> and select <strong>Run diagnostics</strong> to use the feature today.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_speed_test.png" alt="Cloudflare One client speed test result" /></p>


<h2 id="create-and-manage-dlp-detection-entries-outside-of-profiles"><a href="/changelog/post/2026-04-28-detection-entries-outside-profiles/">Create and manage DLP detection entries outside of profiles</a></h2>
<p><em>2026-04-28</em></p>
<p>You can now create, view, and manage DLP detection entries outside of profiles.</p>
<p>Detection entries are no longer hidden inside individual profiles. Administrators can manage detection entries directly from the <strong>Detection entries</strong> section and use them in custom DLP profiles.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/">Configure detection entries</a>.</p>


<h2 id="detect-pii-records-with-a-new-predefined-dlp-profile"><a href="/changelog/post/2026-04-28-pii-record-profile/">Detect PII records with a new predefined DLP profile</a></h2>
<p><em>2026-04-28</em></p>
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


<h2 id="network-session-logs-now-available-for-all-on-ramps"><a href="/changelog/post/2026-04-24-nsl-all-onramps/">Network Session Logs now available for all on-ramps</a></h2>
<p><em>2026-04-24</em></p>
<p><a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a> are now generated for all traffic proxied through Cloudflare Gateway, regardless of on-ramp type. This includes traffic from <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints (PAC files)</a> and <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> egress — on-ramps that previously did not generate session logs.</p>
<p>Customers who already consume the <code>zero_trust_network_sessions</code> dataset via <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a> or <a href="/log-explorer/">Log Explorer</a> may see increased log volume if they use these on-ramps.</p>
<p>For field definitions, refer to <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a>. For traffic analysis, refer to <a href="/cloudflare-one/insights/analytics/network-sessions/">Network session analytics</a>.</p>


<h2 id="aaguid-restrictions-and-amr-matching-for-access-independent-mfa"><a href="/changelog/post/2026-04-23-independent-mfa-aaguid-amr/">AAGUID restrictions and AMR matching for Access independent MFA</a></h2>
<p><em>2026-04-23</em></p>
<p><a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">Independent MFA</a> in Cloudflare Access now supports two additional organization-level controls:</p>
<ul>
<li><strong><a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#restrict-authenticators-by-aaguid">Restrict authenticators by AAGUID</a></strong> — Limit enrollment to a specific set of WebAuthn authenticators using their <a href="https://fidoalliance.org/specs/fido-v2.0-id-20180227/fido-registry-v2.0-id-20180227.html#authenticator-attestation-guid">AAGUID</a>. This is useful for organizations that require FIPS-validated security keys or company-issued hardware. AAGUIDs are managed through a new <a href="/cloudflare-one/reusable-components/lists/">List</a> type.</li>
<li><strong><a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#use-identity-provider-mfa">AMR matching</a></strong> — Skip the independent MFA prompt when the identity provider has already performed an equivalent MFA. Access reads the <code>amr</code> claim defined in <a href="https://datatracker.ietf.org/doc/html/rfc8176">RFC 8176</a> and matches supported values such as <code>hwk</code>, <code>otp</code>, and <code>fpt</code> to the authenticator types allowed on the application or policy. This prevents users from having to complete MFA twice when their identity provider already enforces it.</li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">Independent MFA</a>.</p>


<h2 id="country-rules-supported-in-unified-routing"><a href="/changelog/post/2026-04-21-unified-routing-geoip-country-rules/">Country rules supported in Unified Routing</a></h2>
<p><em>2026-04-21T12:00:00</em></p>
<p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> Country rules are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. This feature requires a Cloudflare Advanced Network Firewall subscription.</p>
<p>You can create firewall rules that match traffic based on source or destination country to enforce geographic access policies across your network.</p>
<p>This is the first of the Cloudflare Advanced Network Firewall features to become available in Unified Routing. Support for additional features - IP Lists, ASN Lists, Threat Intel Lists, IDS, Rate Limiting, SIP, and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<h2 id="network-session-analytics-dashboard"><a href="/changelog/post/2026-04-20-network-session-analytics/">Network session analytics dashboard</a></h2>
<p><em>2026-04-20</em></p>
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


<h2 id="homepage-and-sign-out-for-mcp-server-portals"><a href="/changelog/post/2026-04-17-mcp-portal-homepage-and-sign-out/">Homepage and sign-out for MCP server portals</a></h2>
<p><em>2026-04-17</em></p>
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


<h2 id="independent-mfa-for-access-applications"><a href="/changelog/post/2026-04-15-independent-mfa/">Independent MFA for Access applications</a></h2>
<p><em>2026-04-15</em></p>
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


<h2 id="new-streamlined-creation-experience-for-access-applications-and-gateway-policies"><a href="/changelog/post/2026-04-15-new-rule-and-application-builders/">New, streamlined creation experience for Access Applications and Gateway Policies</a></h2>
<p><em>2026-04-15</em></p>
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


<h2 id="last-seen-timestamp-for-cloudflare-one-client-devices-is-more-consistent"><a href="/changelog/post/2026-04-15-dex-consistent-last-seen-timestamps/">Last seen timestamp for Cloudflare One Client devices is more consistent</a></h2>
<p><em>2026-04-15</em></p>
<p>The last seen timestamp for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> devices is now more consistent across the dashboard. IT teams will see more consistent information about the most recent client event between a device and Cloudflare's network.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/cloudflare-one/4/">Previous</a><span>Page 5 of 13</span><a class="pagination-next" rel="next" href="/changelog/product-group/cloudflare-one/6/">Next</a></nav>
