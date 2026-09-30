---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/access/3/
  description: '2025-08-14'
  full_title: access changelog - page 3 | Cloudflare Docs
  head_html: <title>access changelog - page 3 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-08-14"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/access/3/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="access changelog - page 3"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-08-14"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/access/3/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/access/3/#page","headline":"access changelog - page 3 | Cloudflare Docs","description":"2025-08-14","url":"https://developers.cloudflare.com/changelog/product/access/3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/access/3/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="cloudflare-access-logging-supports-the-customer-metadata-boundary-cmb"><a href="/changelog/post/2025-07-01-Access-Supports-Customer-Metadata-Boundary/">Cloudflare Access Logging supports the Customer Metadata Boundary (CMB)</a></h2>
<p><em>2025-08-14</em></p>
<p>Cloudflare Access logs now support the <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary (CMB)</a>. If you have configured the CMB for your account, all Access logging will respect that configuration.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17615.md")</aside>


<h2 id="access-rdp-securely-from-your-browser-now-in-open-beta"><a href="/changelog/post/2025-07-01-browser-based-rdp-open-beta/">Access RDP securely from your browser — now in open beta</a></h2>
<p><em>2025-07-01</em></p>
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


<h2 id="cloudflare-one-analytics-dashboards-and-exportable-access-report"><a href="/changelog/post/dashboards-access-report/">Cloudflare One Analytics Dashboards and Exportable Access Report</a></h2>
<p><em>2025-06-05</em></p>
<p>Cloudflare One now offers powerful new analytics dashboards to help customers easily discover available insights into their application access and network activity. These dashboards provide a centralized, intuitive view for understanding user behavior, application usage, and security posture.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/Analytics Dashboards.png" alt="Cloudflare One Analytics Dashboards"></p>
<p>Additionally, a new exportable access report is available, allowing customers to quickly view high-level metrics and trends in their application access. A <strong>preview</strong> of the report is shown below, with more to be found in the report:</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-report.png" alt="Cloudflare One Analytics Dashboards" /></p>
<p>Both features are accessible in the Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, empowering organizations with better visibility and control.</p>


<h2 id="new-access-analytics-in-the-cloudflare-one-dashboard"><a href="/changelog/post/access-analytics-v2/">New Access Analytics in the Cloudflare One Dashboard</a></h2>
<p><em>2025-05-16</em></p>
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


<h2 id="access-bulk-policy-tester"><a href="/changelog/post/2025-04-21-Access-Bulk-Policy-Tester/">Access bulk policy tester</a></h2>
<p><em>2025-04-21</em></p>
<p>The <a href="/cloudflare-one/access-controls/policies/policy-management/#test-all-policies-in-an-application">Access bulk policy tester</a> is now available in the Cloudflare Zero Trust dashboard. The bulk policy tester allows you to simulate Access policies against your entire user base before and after deploying any changes. The policy tester will simulate the configured policy against each user's last seen identity and device posture (if applicable).</p>
<p><img src="/assets/upstream/images/changelog/access/example-policy-tester.png" alt="Example policy tester" /></p>


<h2 id="cloudflare-zero-trust-scim-user-and-group-provisioning-logs"><a href="/changelog/post/2025-04-09-SCIM-provisioning-logs/">Cloudflare Zero Trust SCIM User and Group Provisioning Logs</a></h2>
<p><em>2025-04-09</em></p>
<p><a href="/cloudflare-one/team-and-resources/users/scim">Cloudflare Zero Trust SCIM provisioning</a> now has a full audit log of all create, update and delete event from any SCIM Enabled IdP. The <a href="/cloudflare-one/insights/logs/dashboard-logs/scim-logs/">SCIM logs</a> support filtering by IdP, Event type, Result and many more fields. This will help with debugging user and group update issues and questions.</p>
<p>SCIM logs can be found on the Zero Trust Dashboard under <strong>Logs</strong> -&gt; <strong>SCIM provisioning</strong>.</p>
<p><img src="/assets/upstream/images/changelog/access/example-scim-log.png" alt="Example SCIM Logs" /></p>


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


<h2 id="export-ssh-command-logs-with-access-for-infrastructure-using-logpush"><a href="/changelog/post/2025-01-15-ssh-logs-and-logpush/">Export SSH command logs with Access for Infrastructure using Logpush</a></h2>
<p><em>2025-01-15</em></p>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2025-01-15-ssh-logs-and-logpush-availability">Availability</h4>
@markup("md", "content/.markup/bodies/17614.md")</aside>
<p>Cloudflare now allows you to send SSH command logs to storage destinations configured in <a href="/logs/logpush/">Logpush</a>, including third-party destinations. Once exported, analyze and audit the data as best fits your organization! For a list of available data fields, refer to the <a href="/logs/logpush/logpush-job/datasets/account/ssh_logs/">SSH logs dataset</a>.</p>
<p>To set up a Logpush job, refer to <a href="/cloudflare-one/insights/logs/logpush/">Logpush integration</a>.</p>


<h2 id="eliminate-long-lived-credentials-and-enhance-ssh-security-with-cloudflare-access-for-infrastructure"><a href="/changelog/post/2024-10-01-ssh-with-access-for-infrastructure/">Eliminate long-lived credentials and enhance SSH security with Cloudflare Access for Infrastructure</a></h2>
<p><em>2024-10-01</em></p>
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


<h2 id="explore-product-updates-for-cloudflare-one"><a href="/changelog/post/2024-06-16-cloudflare-one/">Explore product updates for Cloudflare One</a></h2>
<p><em>2024-06-16</em></p>
<p>Welcome to your new home for product updates on <a href="/cloudflare-one/">Cloudflare One</a>.</p>
<p>Our <a href="/changelog/">new changelog</a> lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.</p>
<p>If you are looking for older product updates, refer to the following locations.</p>
<details class="nb-details" open><summary>Older product updates</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17707.md")</div></details>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/access/2/">Previous</a><span>Page 3 of 3</span></nav>
