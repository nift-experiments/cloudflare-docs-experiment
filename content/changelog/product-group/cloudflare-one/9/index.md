---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/cloudflare-one/9/
  description: '2025-11-06'
  full_title: Cloudflare One changelog - page 9 | Cloudflare Docs
  head_html: <title>Cloudflare One changelog - page 9 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-11-06"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/9/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cloudflare One changelog - page 9"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-11-06"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/9/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/9/#page","headline":"Cloudflare One changelog - page 9 | Cloudflare Docs","description":"2025-11-06","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/9/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/cloudflare-one/9/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="automatic-return-routing-beta"><a href="/changelog/post/2025-11-06-automatic-return-routing-beta/">Automatic Return Routing (Beta)</a></h2>
<p><em>2025-11-06</em></p>
<p>Magic WAN now supports Automatic Return Routing (ARR), allowing customers to configure Magic on-ramps (IPsec/GRE/CNI) to learn the return path for traffic flows without requiring static routes.</p>
<p>Key benefits:</p>
<ul>
<li><strong>Route-less mode</strong>: Static or dynamic routes are optional when using ARR.</li>
<li><strong>Overlapping IP space support</strong>: Traffic originating from customer sites can use overlapping private IP ranges.</li>
<li><strong>Symmetric routing</strong>: Return traffic is guaranteed to use the same connection as the original on-ramp.</li>
</ul>
<p>This feature is currently in beta and requires the new Unified Routing mode (beta).</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/#configure-automatic-return-routing-beta">Configure Automatic Return Routing</a>.</p>


<h2 id="designate-wan-link-for-breakout-traffic"><a href="/changelog/post/2025-11-06-connector-designate-wan-link-breakout/">Designate WAN link for breakout traffic</a></h2>
<p><em>2025-11-06</em></p>
<p>Magic WAN Connector now allows you to designate a specific WAN port for breakout traffic, giving you deterministic control over the egress path for latency-sensitive applications.</p>
<p>With this feature, you can:</p>
<ul>
<li>Pin breakout traffic for specific applications to a preferred WAN port.</li>
<li>Ensure critical traffic (such as Zoom or Teams) always uses your fastest or most reliable connection.</li>
<li>Benefit from automatic failover to standard WAN port priority if the preferred port goes down.</li>
</ul>
<p>This is useful for organizations with multiple ISP uplinks who need predictable egress behavior for performance-sensitive traffic.</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#designate-wan-ports-for-breakout-apps">Designate WAN ports for breakout apps</a>.</p>


<h2 id="applications-to-be-remapped-to-the-new-categories"><a href="/changelog/post/2025-11-06-Applications-recategorised-plan/">Applications to be remapped to the new categories</a></h2>
<p><em>2025-11-06</em></p>
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


<h2 id="access-private-hostname-applications-support-all-ports-protocols"><a href="/changelog/post/2025-10-28-Access-Application-Support-For-All-Ports-And-Protocols/">Access private hostname applications support all ports/protocols</a></h2>
<p><em>2025-10-28</em></p>
<p><a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Cloudflare Access for private hostname applications</a> can now secure traffic on all ports and protocols.</p>
<p>Previously, applying Zero Trust policies to private applications required the application to use HTTPS on port <code>443</code> and support Server Name Indicator (SNI).</p>
<p>This update removes that limitation. As long as the application is reachable via a Cloudflare off-ramp, you can now enforce your critical security controls — like single sign-on (SSO), MFA, device posture, and variable session lengths — to any private application. This allows you to extend Zero Trust security to services like SSH, RDP, internal databases, and other non-HTTPS applications.</p>
<p><img src="/assets/upstream/images/changelog/access/internal_private_app_any_port.png" alt="Example private application on non-443 port" /></p>
<p>For example, you can now create a self-hosted application in Access for <code>ssh.testapp.local</code> running on port <code>22</code>. You can then build a policy that only allows engineers in your organization to connect after they pass an SSO/MFA check and are using a corporate device.</p>
<p>This feature is generally available across all plans.</p>


<h2 id="casb-introduces-new-granular-roles"><a href="/changelog/post/2025-10-28-casb-roles/">CASB introduces new granular roles</a></h2>
<p><em>2025-10-28</em></p>
<p>Cloudflare CASB (Cloud Access Security Broker) now supports two new granular roles to provide more precise access control for your security teams:</p>
<ul>
<li><strong>Cloudflare CASB Read:</strong> Provides read-only access to view CASB findings and dashboards. This role is ideal for security analysts, compliance auditors, or team members who need visibility without modification rights.</li>
<li><strong>Cloudflare CASB:</strong> Provides full administrative access to configure and manage all aspects of the CASB product.</li>
</ul>
<p>These new roles help you better enforce the principle of least privilege. You can now grant specific members access to CASB security findings without assigning them broader permissions, such as the <strong>Super Administrator</strong> or <strong>Administrator</strong> roles.</p>
<p>To enable <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">Data Loss Prevention (DLP)</a>, scans in CASB, account members will need the <strong>Cloudflare Zero Trust</strong> role.</p>
<p>You can find these new roles when inviting members or creating API tokens in the Cloudflare dashboard under <strong>Manage Account</strong> &gt; <strong>Members</strong>.</p>
<p>To learn more about managing roles and permissions, refer to the <a href="/fundamentals/manage-members/roles/">Manage account members and roles documentation</a>.</p>


<h2 id="new-application-categories-added-for-http-traffic-management"><a href="/changelog/post/Gateway-application-categories-added/">New Application Categories added for HTTP Traffic Management</a></h2>
<p><em>2025-10-28</em></p>
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


<h2 id="schedule-dns-policies-from-the-ui"><a href="/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/">Schedule DNS policies from the UI</a></h2>
<p><em>2025-10-20</em></p>
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


<h2 id="on-demand-security-report"><a href="/changelog/post/2025-10-16-on-demand-security-report/">On-Demand Security Report</a></h2>
<p><em>2025-10-17T22:14:43+00:00</em></p>
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


<h2 id="warp-client-for-macos-version-2025-9-173-1"><a href="/changelog/post/2025-10-16-warp-macos-beta/">WARP client for macOS (version 2025.9.173.1)</a></h2>
<p><em>2025-10-17</em></p>
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


<h2 id="warp-client-for-windows-version-2025-9-173-1"><a href="/changelog/post/2025-10-16-warp-windows-beta/">WARP client for Windows (version 2025.9.173.1)</a></h2>
<p><em>2025-10-17</em></p>
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


<h2 id="monitor-groups-for-advanced-health-checking-with-load-balancing"><a href="/changelog/post/2025-08-15-monitor-groups-for-load-balancing/">Monitor Groups for Advanced Health Checking With Load Balancing</a></h2>
<p><em>2025-10-16</em></p>
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


<h2 id="new-domain-categories-added"><a href="/changelog/post/2025-10-10-new-domain-categories/">New domain categories added</a></h2>
<p><em>2025-10-10</em></p>
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


<h2 id="warp-client-for-linux-version-2025-8-779-0"><a href="/changelog/post/2025-10-07-warp-linux-ga/">WARP client for Linux (version 2025.8.779.0)</a></h2>
<p><em>2025-10-08</em></p>
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


<h2 id="warp-client-for-macos-version-2025-8-779-0"><a href="/changelog/post/2025-10-07-warp-macos-ga/">WARP client for macOS (version 2025.8.779.0)</a></h2>
<p><em>2025-10-08</em></p>
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


<h2 id="fine-grained-permissioning-for-access-for-apps-idps-targets-now-in-public-beta"><a href="/changelog/post/2025-10-01-fine-grained-permissioning-beta/">Fine-grained Permissioning for Access for Apps, IdPs, & Targets now in Public Beta</a></h2>
<p><em>2025-10-02</em></p>
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


<h2 id="expanded-file-type-controls-for-executables-and-disk-images"><a href="/changelog/post/2025-10-01-new-file-type-support/">Expanded File Type Controls for Executables and Disk Images</a></h2>
<p><em>2025-10-01</em></p>
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


<h2 id="application-granular-controls-for-operations-in-saas-applications"><a href="/changelog/post/2025-09-25-new-granular-controls-for-saas-applications/">Application granular controls for operations in SaaS applications</a></h2>
<p><em>2025-09-30</em></p>
<p>Gateway users can now apply granular controls to their file sharing and AI chat applications through <a href="/cloudflare-one/traffic-policies/http-policies">HTTP policies</a>.</p>
<p>The new feature offers two methods of controlling SaaS applications:</p>
<ul>
<li><strong>Application Controls</strong> are curated groupings of Operations which provide an easy way for users to achieve a specific outcome. Application Controls may include <em>Upload</em>, <em>Download</em>, <em>Prompt</em>, <em>Voice</em>, and <em>Share</em> depending on the application.</li>
<li><strong>Operations</strong> are controls aligned to the most granular action a user can take. This provides a fine-grained approach to enforcing policy and generally aligns to the SaaS providers API specifications in naming and function.</li>
</ul>
<p>Get started using <a href="/cloudflare-one/traffic-policies/http-policies/granular-controls">Application Granular Controls</a> and refer to the list of <a href="/cloudflare-one/traffic-policies/http-policies/granular-controls/#compatible-applications">supported applications</a>.</p>


<h2 id="refine-dlp-scans-with-new-body-phase-selector"><a href="/changelog/post/2025-09-25-body-phase-selector/">Refine DLP Scans with New Body Phase Selector</a></h2>
<p><em>2025-09-25</em></p>
<p>You can now more precisely control your HTTP DLP policies by specifying whether to scan the request or response body, helping to reduce false positives and target specific data flows.</p>
<p>In the Gateway HTTP policy builder, you will find a new selector called <em>Body Phase</em>. This allows you to define the direction of traffic the DLP engine will inspect:</p>
<ul>
<li><em>Request Body</em>: Scans data sent from a user's machine to an upstream service. This is ideal for monitoring data uploads, form submissions, or other user-initiated data exfiltration attempts.</li>
<li><em>Response Body</em>: Scans data sent to a user's machine from an upstream service. Use this to inspect file downloads and website content for sensitive data.</li>
</ul>
<p>For example, consider a policy that blocks Social Security Numbers (SSNs). Previously, this policy might trigger when a user visits a website that contains example SSNs in its content (the response body). Now, by setting the <strong>Body Phase</strong> to <em>Request Body</em>, the policy will only trigger if the user attempts to upload or submit an SSN, ignoring the content of the web page itself.</p>
<p>All policies without this selector will continue to scan both request and response bodies to ensure continued protection.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/#body-phase">Gateway HTTP policy selectors</a>.</p>


<h2 id="invalid-submissions-feedback"><a href="/changelog/post/2025-09-23-invalid-submissions/">Invalid Submissions Feedback</a></h2>
<p><em>2025-09-23T23:11:49+00:00</em></p>
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


<h2 id="access-remote-desktop-protocol-rdp-destinations-securely-from-your-browser-now-generally-available"><a href="/changelog/post/2025-09-22-browser-based-rdp-ga/">Access Remote Desktop Protocol (RDP) destinations securely from your browser — now generally available!</a></h2>
<p><em>2025-09-22</em></p>
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


<h2 id="connect-and-secure-any-private-or-public-app-by-hostname-not-ip-with-hostname-routing-for-cloudflare-tunnel"><a href="/changelog/post/2025-09-18-tunnel-hostname-routing/">Connect and secure any private or public app by hostname, not IP — with hostname routing for Cloudflare Tunnel</a></h2>
<p><em>2025-09-18</em></p>
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


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/cloudflare-one/8/">Previous</a><span>Page 9 of 13</span><a class="pagination-next" rel="next" href="/changelog/product-group/cloudflare-one/10/">Next</a></nav>
