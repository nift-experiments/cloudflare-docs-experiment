---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/cloudflare-one/8/
  description: '2026-01-22'
  full_title: Cloudflare One changelog - page 8 | Cloudflare Docs
  head_html: <title>Cloudflare One changelog - page 8 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-01-22"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/8/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cloudflare One changelog - page 8"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-01-22"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/8/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/8/#page","headline":"Cloudflare One changelog - page 8 | Cloudflare Docs","description":"2026-01-22","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/8/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/cloudflare-one/8/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="require-access-protection-for-zones"><a href="/changelog/post/2026-01-22-deny-by-default-for-zones/">Require Access protection for zones</a></h2>
<p><em>2026-01-22</em></p>
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


<h2 id="new-granular-api-token-permissions-for-cloudflare-access"><a href="/changelog/post/2026-01-22-granular-api-token-permissions/">New granular API token permissions for Cloudflare Access</a></h2>
<p><em>2026-01-22</em></p>
<p>Three new API token permissions are available for Cloudflare Access, giving you finer-grained control when building automations and integrations:</p>
<ul>
<li><strong>Access: Organizations Revoke</strong> — Grants the ability to <a href="/cloudflare-one/access-controls/access-settings/session-management/#revoke-user-sessions">revoke user sessions</a> in a Zero Trust organization. Use this permission when you need a token that can terminate active sessions without broader write access to organization settings.</li>
<li><strong>Access: Population Read</strong> — Grants read access to the <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM users and groups</a> synced from an identity provider to Cloudflare Access. Use this permission for tokens that only need to read synced user and group data.</li>
<li><strong>Access: Population Write</strong> — Grants write access to the <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM users and groups</a> synced from an identity provider to Cloudflare Access. Use this permission for tokens that need to create or modify synced user and group data.</li>
</ul>
<p>These permissions are scoped at the account level and can be combined with existing Access permissions.</p>
<p>For a full list of available permissions, refer to <a href="/fundamentals/api/reference/permissions/">API token permissions</a>.</p>


<h2 id="network-services-navigation-update"><a href="/changelog/post/2026-01-15-networking-navigation-update/">Network Services navigation update</a></h2>
<p><em>2026-01-15</em></p>
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


<h2 id="support-for-crowdstrike-device-scores-in-user-risk-scoring"><a href="/changelog/post/2026-1-15-crowdstrike-score/">Support for CrowdStrike device scores in User Risk Scoring</a></h2>
<p><em>2026-01-15</em></p>
<p>Cloudflare One has expanded its [User Risk Scoring] (/cloudflare-one/insights/risk-score/) capabilities by introducing two new behaviors for organizations using the [CrowdStrike integration] (/cloudflare-one/integrations/service-providers/crowdstrike/).</p>
<p>Administrators can now automatically escalate the risk score of a user if their device matches specific CrowdStrike Zero Trust Assessment (ZTA) score ranges. This allows for more granular security policies that respond dynamically to the health of the endpoint.</p>
<p>New risk behaviors
The following risk scoring behaviors are now available:</p>
<ul>
<li>CrowdStrike low device score: Automatically increases a user's risk score when the connected device reports a &quot;Low&quot; score from CrowdStrike.</li>
<li>CrowdStrike medium device score: Automatically increases a user's risk score when the connected device reports a &quot;Medium&quot; score from CrowdStrike.</li>
</ul>
<p>These scores are derived from [CrowdStrike device posture attributes] (/cloudflare-one/integrations/service-providers/crowdstrike/#device-posture-attributes), including OS signals and sensor configurations.</p>


<h2 id="verify-warp-connector-connectivity-with-a-simple-ping"><a href="/changelog/post/2026-01-15-warp-connector-ping-support/">Verify WARP Connector connectivity with a simple ping</a></h2>
<p><em>2026-01-15</em></p>
<p>We have made it easier to validate connectivity when deploying <a href="/mesh/">WARP Connector</a> as part of your <a href="/reference-architecture/architectures/sase/#connecting-networks">software-defined private network</a>.</p>
<p>You can now <code>ping</code> the WARP Connector host directly on its LAN IP address immediately after installation. This provides a fast, familiar way to confirm that the Connector is online and reachable within your network before testing access to downstream services.</p>
<p>Starting with <a href="/changelog/2026-01-13-warp-linux-ga/">version 2025.10.186.0</a>, WARP Connector responds to traffic addressed to its own LAN IP, giving you immediate visibility into Connector reachability.</p>
<p>Learn more about deploying <a href="/mesh/">WARP Connector</a> and building private network connectivity with <a href="/cloudflare-one/">Cloudflare One</a>.</p>


<h2 id="warp-client-for-macos-version-2025-10-186-0"><a href="/changelog/post/2026-01-13-warp-macos-ga/">WARP client for macOS (version 2025.10.186.0)</a></h2>
<p><em>2026-01-14</em></p>
<p>A new GA release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features, including the ability to manage WARP client connectivity for all devices in your fleet using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> now supports transparent HTTP proxying in addition to CONNECT-based proxying.</li>
<li>Added a new feature to manage WARP client connectivity for all devices using an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect">external signal</a>. This feature allows administrators to send a global signal from an on-premises HTTPS endpoint that force disconnects or reconnects all WARP clients in an account based on configuration set on the endpoint.</li>
</ul>


<h2 id="warp-client-for-windows-version-2025-10-186-0"><a href="/changelog/post/2026-01-13-warp-windows-ga/">WARP client for Windows (version 2025.10.186.0)</a></h2>
<p><em>2026-01-14</em></p>
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


<h2 id="warp-client-for-linux-version-2025-10-186-0"><a href="/changelog/post/2026-01-13-warp-linux-ga/">WARP client for Linux (version 2025.10.186.0)</a></h2>
<p><em>2026-01-13</em></p>
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


<h2 id="enhanced-visibility-for-post-delivery-actions"><a href="/changelog/post/2026-01-12-enhanced-visibility-post-delivery-actions/">Enhanced visibility for post-delivery actions</a></h2>
<p><em>2026-01-12T11:15:33+00:00</em></p>
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


<h2 id="cloudflare-admin-activity-logs-capture-creation-of-dns-over-http-doh-users"><a href="/changelog/post/2026-01-08-Access-audit-log-for-DoH-users/">Cloudflare admin activity logs capture creation of DNS over HTTP (DoH) users</a></h2>
<p><em>2026-01-08</em></p>
<p>Cloudflare <a href="/cloudflare-one/insights/logs/">admin activity logs</a> now capture each time a <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-https/">DNS over HTTP (DoH) user</a> is created.</p>
<p>These logs can be viewed from the <a href="https://one.dash.cloudflare.com/">Cloudflare One dashboard</a>, pulled via the <a href="/api/">Cloudflare API</a>, and exported through <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a>.</p>


<h2 id="breakout-traffic-visibility-via-netflow"><a href="/changelog/post/2025-12-31-connector-breakout-traffic-netflow/">Breakout traffic visibility via NetFlow</a></h2>
<p><em>2025-12-31</em></p>
<p>Magic WAN Connector now exports NetFlow data for breakout traffic to Magic Network Monitoring (MNM), providing visibility into traffic that bypasses Cloudflare's security filtering.</p>
<p>This feature allows you to:</p>
<ul>
<li>Monitor breakout traffic statistics in the Cloudflare dashboard.</li>
<li>View traffic patterns for applications configured to bypass Cloudflare.</li>
<li>Maintain visibility across all traffic passing through your Magic WAN Connector.</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-wan/analytics/netflow-analytics/">NetFlow statistics</a>.</p>


<h2 id="shadow-it-domain-level-saas-analytics"><a href="/changelog/post/2025-12-17-shadow-it-domain-analytics/">Shadow IT - domain level SaaS analytics</a></h2>
<p><em>2025-12-17</em></p>
<p>Zero Trust has again upgraded its <strong>Shadow IT analytics</strong>, providing you with unprecedented visibility into your organizations use of SaaS tools. With this dashboard, you can review who is using an application and volumes of data transfer to the application.</p>
<p>With this update, you can review data transfer metrics at the domain level, rather than just the application level, providing more granular insight into your data transfer patterns.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/shadow-it-domain.png" alt="New Domain Level Metrics" /></p>
<p>These metrics can be filtered by all available filters on the dashboard, including user, application, or content category.</p>
<p>Both the analytics and policies are accessible in the Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, empowering organizations with better visibility and control.</p>


<h2 id="new-duplicate-action-for-supported-cloudflare-one-resources"><a href="/changelog/post/2025-12-16-new-duplicate-action-for-supported-cloudflare-one-resources/">New duplicate action for supported Cloudflare One resources</a></h2>
<p><em>2025-12-16</em></p>
<p>You can now duplicate specific Cloudflare One resources with a single click from the dashboard.</p>
<p>Initially supported resources:</p>
<ul>
<li>Access Applications</li>
<li>Access Policies</li>
<li>Gateway Policies</li>
</ul>
<p>To try this out, simply click on the overflow menu (⋮) from the resource table and click <i>Duplicate</i>. We will continue to add the Duplicate action for resources throughout 2026.</p>


<h2 id="warp-client-for-macos-version-2025-10-118-1"><a href="/changelog/post/2025-12-09-warp-macos-beta/">WARP client for macOS (version 2025.10.118.1)</a></h2>
<p><em>2025-12-10</em></p>
<p>A new Beta release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> now supports transparent HTTP proxying in addition to CONNECT-based proxying.</li>
</ul>


<h2 id="warp-client-for-windows-version-2025-10-118-1"><a href="/changelog/post/2025-12-09-warp-windows-beta/">WARP client for Windows (version 2025.10.118.1)</a></h2>
<p><em>2025-12-10</em></p>
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


<h2 id="reclassifications-to-submissions"><a href="/changelog/post/2025-12-03-submission-terminology-update/">Reclassifications to Submissions</a></h2>
<p><em>2025-12-03T21:11:33+00:00</em></p>
<p>We have updated the terminology “Reclassify” and “Reclassifications” to “Submit” and “Submissions” respectively. This update more accurately reflects the outcome of providing these items to Cloudflare.</p>
<p>Submissions are leveraged to tune future variants of campaigns. To respect data sanctity, providing a submission does not change the original disposition of the emails submitted.</p>
<p><img src="/assets/upstream/images/changelog/email-security/reclassification-submission.png" alt="nav_example" /></p>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="adjustment-to-final-disposition-column"><a href="/changelog/post/2025-11-18-temporary-adjustment-to-final-disposition-column/">Adjustment to Final Disposition Column</a></h2>
<p><em>2025-11-18</em></p>
<h4 id="2025-11-18-temporary-adjustment-to-final-disposition-column-adjustment-to-final-disposition-column">Adjustment to Final Disposition column</h4>
<h4 id="2025-11-18-temporary-adjustment-to-final-disposition-column-the-final-disposition-column-in-submissions-team-submissions-tab-is-changing-for-non-phishguard-customers">The <strong>Final Disposition</strong> column in <strong>Submissions</strong> &gt; <strong>Team Submissions</strong> tab is changing for non-Phishguard customers.</h4>
<h4 id="2025-11-18-temporary-adjustment-to-final-disposition-column-what-s-changing">What's Changing</h4>
<ul>
<li>Column will be called <strong>Status</strong> instead of <strong>Final Disposition</strong></li>
<li>Column status values will now be: <strong>Submitted</strong>, <strong>Accepted</strong> or <strong>Rejected</strong>.</li>
</ul>
<h4 id="2025-11-18-temporary-adjustment-to-final-disposition-column-next-steps">Next Steps</h4>
<p>We will listen carefully to your feedback and continue to find comprehensive ways to communicate updates on your submissions. Your submissions will continue to be addressed at an even greater rate than before, fuelling faster and more accurate email security improvement.</p>


<h2 id="new-cloudflare-one-navigation-and-product-experience"><a href="/changelog/post/new-cloudflare-one-navigation-and-product-experience/">New Cloudflare One Navigation and Product Experience</a></h2>
<p><em>2025-11-17</em></p>
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


<h2 id="generate-cloudflare-access-ssh-certificate-authority-ca-directly-from-the-cloudflare-dashboard"><a href="/changelog/post/2025-11-14-SSH-CA-enhancements/">Generate Cloudflare Access SSH certificate authority (CA) directly from the Cloudflare dashboard</a></h2>
<p><em>2025-11-14</em></p>
<p>SSH with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">Cloudflare Access for Infrastructure</a> allows you to use short-lived SSH certificates to eliminate SSH key management and reduce security risks associated with lost or stolen keys.</p>
<p>Previously, users had to generate this certificate by using the <a href="https://developers.cloudflare.com/api/">Cloudflare API</a> directly. With this update, you can now create and manage this certificate in the <a href="https://one.dash.cloudflare.com">Cloudflare One dashboard</a> from the <strong>Access controls</strong> &gt; <strong>Service credentials</strong> page.</p>
<p><img src="/assets/upstream/images/changelog/access/SSH-CA-generation.png" alt="Navigate to Access controls and then Service credentials to see where you can generate an SSH CA" /></p>
<p>For more details, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#generate-a-cloudflare-ssh-ca">Generate a Cloudflare SSH CA</a>.</p>


<h2 id="new-saas-security-weekly-digests-with-api-casb"><a href="/changelog/post/2025-11-14-casb-digest/">New SaaS Security weekly digests with API CASB</a></h2>
<p><em>2025-11-14</em></p>
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


<h2 id="dex-logpush-jobs"><a href="/changelog/post/2025-11-12-dex-logpush-jobs/">DEX Logpush jobs</a></h2>
<p><em>2025-11-12</em></p>
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


<h2 id="warp-client-for-linux-version-2025-9-558-0"><a href="/changelog/post/2025-11-11-warp-linux-ga/">WARP client for Linux (version 2025.9.558.0)</a></h2>
<p><em>2025-11-12</em></p>
<p>A new GA release for the Linux WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">Path Maximum Transmission Unit Discovery (PMTUD)</a>. When PMTUD is enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to diagnose connectivity issues.</p>
<p>WARP client version 2025.8.779.0 introduced an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at <a href="https://pkg.cloudflareclient.com/">pkg.cloudflareclient.com</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to diagnose connectivity issues.</li>
<li>Fixed an issue where deleting a registration was erroneously reported as having failed.</li>
<li>Path Maximum Transmission Unit Discovery (PMTUD) may now be used to discover the effective MTU of the connection. This allows the WARP client to improve connectivity optimized for each network. PMTUD is disabled by default. To enable it, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">PMTUD documentation</a>.</li>
</ul>


<h2 id="warp-client-for-macos-version-2025-9-558-0"><a href="/changelog/post/2025-11-11-warp-macos-ga/">WARP client for macOS (version 2025.9.558.0)</a></h2>
<p><em>2025-11-12</em></p>
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


<h2 id="warp-client-for-windows-version-2025-9-558-0"><a href="/changelog/post/2025-11-11-warp-windows-ga/">WARP client for Windows (version 2025.9.558.0)</a></h2>
<p><em>2025-11-12</em></p>
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


<h2 id="cloudflared-proxy-dns-command-will-be-removed-starting-february-2-2026"><a href="/changelog/post/2025-11-11-cloudflared-proxy-dns/">cloudflared proxy-dns command will be removed starting February 2, 2026</a></h2>
<p><em>2025-11-11</em></p>
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


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/cloudflare-one/7/">Previous</a><span>Page 8 of 13</span><a class="pagination-next" rel="next" href="/changelog/product-group/cloudflare-one/9/">Next</a></nav>
