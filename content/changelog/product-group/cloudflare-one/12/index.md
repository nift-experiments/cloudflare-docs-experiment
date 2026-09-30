---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/cloudflare-one/12/
  description: '2025-05-01'
  full_title: Cloudflare One changelog - page 12 | Cloudflare Docs
  head_html: <title>Cloudflare One changelog - page 12 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-05-01"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/12/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cloudflare One changelog - page 12"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-05-01"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/12/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/12/#page","headline":"Cloudflare One changelog - page 12 | Cloudflare Docs","description":"2025-05-01","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/12/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/cloudflare-one/12/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="browser-isolation-overview-page-for-zero-trust"><a href="/changelog/post/2025-05-01-browser-isolation-overview-page/">Browser Isolation Overview page for Zero Trust</a></h2>
<p><em>2025-05-01</em></p>
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


<h2 id="dark-mode-for-zero-trust-dashboard"><a href="/changelog/post/2025-04-30-zero-trust-dashboard-dark-mode/">Dark Mode for Zero Trust Dashboard</a></h2>
<p><em>2025-04-30</em></p>
<p>The <a href="https://one.dash.cloudflare.com/">Cloudflare Zero Trust dashboard</a> now supports Cloudflare's native dark mode for all accounts and plan types.</p>
<p>Zero Trust Dashboard will automatically accept your user-level preferences for system settings, so if your Dashboard appearance is set to 'system' or 'dark', the Zero Trust dashboard will enter dark mode whenever the rest of your Cloudflare account does.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/dark-mode.png" alt="Zero Trust dashboard supports dark mode" /></p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17706.md")
</div></div>


<h2 id="cloudflare-one-appliance-supports-multiple-dns-server-ips"><a href="/changelog/post/2025-04-30-appliance-multiple-dns-servers/">Cloudflare One Appliance supports multiple DNS server IPs</a></h2>
<p><em>2025-04-30</em></p>
<p>Cloudflare One Appliance DHCP server settings now support specifying multiple DNS server IP addresses in the DHCP pool.</p>
<p>Previously, customers could only configure a single DNS server per DHCP pool. With this update, you can specify multiple DNS servers to provide redundancy for clients at branch locations.</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/">DHCP server</a>.</p>


<h2 id="fqdn-filtering-for-gateway-egress-policies"><a href="/changelog/post/2025-04-28-FDQN-Filtering-Egress-Policies/">FQDN Filtering For Gateway Egress Policies</a></h2>
<p><em>2025-04-28</em></p>
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


<h2 id="access-bulk-policy-tester"><a href="/changelog/post/2025-04-21-Access-Bulk-Policy-Tester/">Access bulk policy tester</a></h2>
<p><em>2025-04-21</em></p>
<p>The <a href="/cloudflare-one/access-controls/policies/policy-management/#test-all-policies-in-an-application">Access bulk policy tester</a> is now available in the Cloudflare Zero Trust dashboard. The bulk policy tester allows you to simulate Access policies against your entire user base before and after deploying any changes. The policy tester will simulate the configured policy against each user's last seen identity and device posture (if applicable).</p>
<p><img src="/assets/upstream/images/changelog/access/example-policy-tester.png" alt="Example policy tester" /></p>


<h2 id="new-predefined-detection-entry-for-icd-11"><a href="/changelog/post/2025-04-14-icd11-support/">New predefined detection entry for ICD-11</a></h2>
<p><em>2025-04-14</em></p>
<p>You now have access to the World Health Organization (WHO) 2025 edition of the <a href="https://www.who.int/news/item/14-02-2025-who-releases-2025-update-to-the-international-classification-of-diseases-%28icd-11%29">International Classification of Diseases 11th Revision (ICD-11)</a> as a predefined detection entry. The new dataset can be found in the <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#health-information">Health Information</a> predefined profile.</p>
<p>ICD-10 dataset remains available for use.</p>


<h2 id="http-redirect-and-custom-block-page-redirect"><a href="/changelog/post/2025-04-11-http-redirect-custom-block-page-redirect/">HTTP redirect and custom block page redirect</a></h2>
<p><em>2025-04-11</em></p>
<p>You can now use more flexible redirect capabilities in Cloudflare One with Gateway.</p>
<ul>
<li>A new <strong>Redirect</strong> action is available in the HTTP policy builder, allowing admins to redirect users to any URL when their request matches a policy. You can choose to preserve the original URL and query string, and optionally include policy context via query parameters.</li>
<li>For <strong>Block</strong> actions, admins can now configure a custom URL to display when access is denied. This block page redirect is set at the account level and can be overridden in DNS or HTTP policies. Policy context can also be passed along in the URL.</li>
</ul>
<p>Learn more in our documentation for <a href="/cloudflare-one/traffic-policies/http-policies/#redirect">HTTP Redirect</a> and <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#redirect-to-a-block-page">Block page redirect</a>.</p>


<h2 id="cloudflare-zero-trust-scim-user-and-group-provisioning-logs"><a href="/changelog/post/2025-04-09-SCIM-provisioning-logs/">Cloudflare Zero Trust SCIM User and Group Provisioning Logs</a></h2>
<p><em>2025-04-09</em></p>
<p><a href="/cloudflare-one/team-and-resources/users/scim">Cloudflare Zero Trust SCIM provisioning</a> now has a full audit log of all create, update and delete event from any SCIM Enabled IdP. The <a href="/cloudflare-one/insights/logs/dashboard-logs/scim-logs/">SCIM logs</a> support filtering by IdP, Event type, Result and many more fields. This will help with debugging user and group update issues and questions.</p>
<p>SCIM logs can be found on the Zero Trust Dashboard under <strong>Logs</strong> -&gt; <strong>SCIM provisioning</strong>.</p>
<p><img src="/assets/upstream/images/changelog/access/example-scim-log.png" alt="Example SCIM Logs" /></p>


<h2 id="casb-and-email-security"><a href="/changelog/post/2025-04-01-casb-email-security/">CASB and Email security</a></h2>
<p><em>2025-04-01T23:22:49+00:00</em></p>
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


<h2 id="secure-dns-locations-management-user-role"><a href="/changelog/post/2025-03-21-pdns-user-locations-role/">Secure DNS Locations Management User Role</a></h2>
<p><em>2025-03-21</em></p>
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


<h2 id="cloudflare-one-agent-for-android-version-2-4"><a href="/changelog/post/2025-03-17-warp-ga-android/">Cloudflare One Agent for Android (version 2.4)</a></h2>
<p><em>2025-03-17</em></p>
<p>A new GA release for the Android Cloudflare One Agent is now available in the <a href="https://play.google.com/store/apps/details?id=com.cloudflare.cloudflareoneagent">Google Play Store</a>. This release includes a new feature allowing <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url">team name insertion by URL</a> during enrollment, as well as fixes and minor improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Improved in-app error messages.</li>
<li>Improved mobile client login with support for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url">team name insertion by URL</a>.</li>
<li>Fixed an issue preventing admin split tunnel settings taking priority for traffic from certain applications.</li>
</ul>


<h2 id="cloudflare-one-agent-for-ios-version-1-10"><a href="/changelog/post/2025-03-17-warp-ga-ios/">Cloudflare One Agent for iOS (version 1.10)</a></h2>
<p><em>2025-03-17</em></p>
<p>A new GA release for the iOS Cloudflare One Agent is now available in the <a href="https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492">iOS App Store</a>. This release includes a new feature allowing <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url">team name insertion by URL</a> during enrollment, as well as fixes and minor improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Improved in-app error messages.</li>
<li>Improved mobile client login with support for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/#enroll-using-a-url">team name insertion by URL</a>.</li>
<li>Bug fixes and performance improvements.</li>
</ul>


<h2 id="cloudflare-ip-ranges-list"><a href="/changelog/post/2025-03-13-new-managed-iplist/">Cloudflare IP Ranges List</a></h2>
<p><em>2025-03-13</em></p>
<p>Magic Firewall now supports a new managed list of Cloudflare IP ranges. This list is available as an option when creating a Magic Firewall policy based on IP source/destination addresses. When selecting &quot;is in list&quot; or &quot;is not in list&quot;, the option &quot;<strong>Cloudflare IP Ranges</strong>&quot; will appear in the dropdown menu.</p>
<p>This list is based on the IPs listed in the Cloudflare <a href="https://www.cloudflare.com/en-gb/ips/">IP ranges</a>.
Updates to this managed list are applied automatically.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-network-firewall/cloudflare-ips.png" alt="Cloudflare IPs Managed List" /></p>
<p>Note: IP Lists require a Cloudflare Advanced Network Firewall subscription. For more details about Cloudflare Network Firewall plans, refer to <a href="/cloudflare-network-firewall/plans">Plans</a>.</p>


<h2 id="cloudflare-one-agent-now-supports-endpoint-monitoring"><a href="/changelog/post/2025-03-07-cloudflare-one-device-health-monitoring/">Cloudflare One Agent now supports Endpoint Monitoring</a></h2>
<p><em>2025-03-07</em></p>
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


<h2 id="gain-visibility-into-user-actions-in-zero-trust-browser-isolation-sessions"><a href="/changelog/post/2025-03-03-user-action-logging/">Gain visibility into user actions in Zero Trust Browser Isolation sessions</a></h2>
<p><em>2025-03-04</em></p>
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


<h2 id="new-saml-and-oidc-fields-and-saml-transforms-for-access-for-saas"><a href="/changelog/post/2025-03-03-saml-oidc-fields-saml-transformations/">New SAML and OIDC Fields and SAML transforms for Access for SaaS</a></h2>
<p><em>2025-03-03</em></p>
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


<h2 id="use-logpush-for-email-security-detections"><a href="/changelog/post/2025-03-01-logpush-detections/">Use Logpush for Email security detections</a></h2>
<p><em>2025-03-01T23:22:49+00:00</em></p>
<p>You can now send detection logs to an endpoint of your choice with Cloudflare Logpush.</p>
<p>Filter logs matching specific criteria you have set and select from over 25 fields you want to send. When creating a new Logpush job, remember to select <strong>Email security alerts</strong> as the dataset.</p>
<p><img src="/assets/upstream/images/changelog/email-security/Logpush-Detections.png" alt="logpush-detections" /></p>
<p>For more information, refer to <a href="/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-detection-logs">Enable detection logs</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="check-status-of-email-security-or-area-1"><a href="/changelog/post/2025-02-07-check-status/">Check status of Email security or Area 1</a></h2>
<p><em>2025-02-27T23:22:49+00:00</em></p>
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


<h2 id="use-dlp-assist-for-m365"><a href="/changelog/post/2025-02-25-dlp-assist-for-m365/">Use DLP Assist for M365</a></h2>
<p><em>2025-02-25T23:22:49+00:00</em></p>
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


<h2 id="configure-your-magic-wan-connector-to-connect-via-static-ip-assignment"><a href="/changelog/post/2025-02-14-local-console-access/">Configure your Magic WAN Connector to connect via static IP assignment</a></h2>
<p><em>2025-02-14</em></p>
<p>You can now locally configure your <a href="/cloudflare-wan/configuration/appliance/">Magic WAN Connector</a> to work in a static IP configuration.</p>
<p>This local method does not require having access to a DHCP Internet connection. However, it does require being comfortable with using tools to access the serial port on Magic WAN Connector as well as using a serial terminal client to access the Connector's environment.</p>
<p>For more details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#bootstrap-via-serial-console">WAN with a static IP address</a>.</p>


<h2 id="open-email-links-with-security-center"><a href="/changelog/post/2025-02-07-open-links-security-center/">Open email links with Security Center</a></h2>
<p><em>2025-02-07T23:22:49+00:00</em></p>
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


<h2 id="block-files-that-are-password-protected-compressed-or-otherwise-unscannable"><a href="/changelog/post/2025-02-13-improvements-unscannable-files/">Block files that are password-protected, compressed, or otherwise unscannable.</a></h2>
<p><em>2025-02-03</em></p>
<p>Gateway HTTP policies can now block files that are password-protected, compressed, or otherwise unscannable.</p>
<p>These unscannable files are now matched with the <a href="/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types">Download and Upload File Types traffic selectors</a> for HTTP policies:</p>
<ul>
<li>Password-protected Microsoft Office document</li>
<li>Password-protected PDF</li>
<li>Password-protected ZIP archive</li>
<li>Unscannable ZIP archive</li>
</ul>
<p>To get started inspecting and modifying behavior based on these and other rules, refer to <a href="/cloudflare-one/traffic-policies/get-started/http/">HTTP filtering</a>.</p>


<h2 id="detect-source-code-leaks-with-data-loss-prevention"><a href="/changelog/post/2025-01-03-source-code-confidence-level/">Detect source code leaks with Data Loss Prevention</a></h2>
<p><em>2025-01-20</em></p>
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


<h2 id="export-ssh-command-logs-with-access-for-infrastructure-using-logpush"><a href="/changelog/post/2025-01-15-ssh-logs-and-logpush/">Export SSH command logs with Access for Infrastructure using Logpush</a></h2>
<p><em>2025-01-15</em></p>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2025-01-15-ssh-logs-and-logpush-availability">Availability</h4>
@markup("md", "content/.markup/bodies/17614.md")</aside>
<p>Cloudflare now allows you to send SSH command logs to storage destinations configured in <a href="/logs/logpush/">Logpush</a>, including third-party destinations. Once exported, analyze and audit the data as best fits your organization! For a list of available data fields, refer to the <a href="/logs/logpush/logpush-job/datasets/account/ssh_logs/">SSH logs dataset</a>.</p>
<p>To set up a Logpush job, refer to <a href="/cloudflare-one/insights/logs/logpush/">Logpush integration</a>.</p>


<h2 id="escalate-user-submissions"><a href="/changelog/post/2024-12-19-escalate-user-submissions/">Escalate user submissions</a></h2>
<p><em>2024-12-19T23:22:49+00:00</em></p>
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


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/cloudflare-one/11/">Previous</a><span>Page 12 of 13</span><a class="pagination-next" rel="next" href="/changelog/product-group/cloudflare-one/13/">Next</a></nav>
