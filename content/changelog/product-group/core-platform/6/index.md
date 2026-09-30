<h1 id="changelog">Changelog</h1>

<h2 id="log-explorer-now-shows-query-result-distribution"><a href="/changelog/post/2025-11-13-query-result-distribution/">Log Explorer now shows query result distribution</a></h2>
<p><em>2025-11-04</em></p>
<p>We're excited to announce a new feature in Log Explorer that significantly enhances how you analyze query results: the Query results distribution chart.</p>
<p>This new chart provides a graphical distribution of your results over the time window of the query. Immediately after running a query, you will see the distribution chart above your result table. This visualization allows Log Explorer users to quickly spot trends, identify anomalies, and understand the temporal concentration of log events that match their criteria. For example, you can visually confirm if a spike in traffic or errors occurred at a specific time, allowing you to focus your investigation efforts more effectively. This feature makes it faster and easier to extract meaningful insights from your vast log data.</p>
<p>The chart will dynamically update to reflect the logs matching your current query.</p>


<h2 id="introducing-email-two-factor-authentication"><a href="/changelog/post/2025-10-30-email-2FA/">Introducing email two-factor authentication</a></h2>
<p><em>2025-10-30</em></p>
<p>Two-factor authentication (2FA) is one of the best ways to protect your account from the risk of account takeover. Cloudflare has offered phishing resistant 2FA options including hardware based keys (for example, a Yubikey) and app based TOTP (time-based one-time password) options which use apps like Google or Microsoft's Authenticator app. Unfortunately, while these solutions are very secure, they can be lost if you misplace the hardware based key, or lose the phone which includes that app. The result is that users sometimes get locked out of their accounts and need to contact support.</p>
<p>Today, we are announcing the addition of email as a 2FA factor for all Cloudflare accounts. Email 2FA is in wide use across the industry as a least common denominator for 2FA because it is low friction, loss resistant, and still improves security over username/password login only. We also know that most commercial email providers already require 2FA, so your email address is usually well protected already.</p>
<p>You can now enable email 2FA on the Cloudflare dashboard:</p>
<ol>
<li>Go to <strong>Profile</strong> at the top right corner.</li>
<li>Select <strong>Authentication</strong>.</li>
<li>Under <strong>Two-Factor Authentication</strong>, select <strong>Set up</strong>.</li>
</ol>
<h4 id="2025-10-30-email-2FA-sign-in-security-best-practices">Sign-in security best practices</h4>
<p>Cloudflare is critical infrastructure, and you should protect it as such. Review the following best practices and make sure you are doing your part to secure your account:</p>
<ul>
<li>Use a unique password for every website, including Cloudflare, and store it in a password manager like 1Password or Keeper. These services are cross-platform and simplify the process of managing secure passwords.</li>
<li>Use 2FA to make it harder for an attacker to get into your account in the event your password is leaked.</li>
<li>Store your backup codes securely. A password manager is the best place since it keeps the backup codes encrypted, but you can also print them and put them somewhere safe in your home.</li>
<li>If you use an app to manage your 2FA keys, enable cloud backup, so that you don't lose your keys in the event you lose your phone.</li>
<li>If you use a custom email domain to sign in, <a href="/fundamentals/manage-members/dashboard-sso/">configure SSO</a>.</li>
<li>If you use a public email domain like Gmail or Hotmail, you can also use social login with Apple, GitHub, or Google to sign in.</li>
<li>If you manage a Cloudflare account for work:
<ul>
<li>Have at least two administrators in case one of them unexpectedly leaves your company.</li>
<li>Use SCIM to automate permissions management for members in your Cloudflare account.</li>
</ul>
</li>
</ul>


<h2 id="revamped-member-management-ui"><a href="/changelog/post/2025-10-30-member-management-improvements/">Revamped Member Management UI</a></h2>
<p><em>2025-10-30</em></p>
<p>As Cloudflare's platform has grown, so has the need for precise, role-based access control. We’ve redesigned the Member Management experience in the Dashboard to help administrators more easily discover, assign, and refine permissions for specific principals.</p>
<h4 id="2025-10-30-member-management-improvements-what-s-new">What's New</h4>
<p><strong>Refreshed member invite flow</strong></p>
<p>We overhauled the Invite Members UI to simplify inviting users and assigning permissions.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-30-invite-experience.gif" alt="Updated Invite Flow UX" /></p>
<p><strong>Refreshed Members Overview Page</strong></p>
<p>We've updated the Members Overview Page to clearly display:</p>
<ul>
<li>Member 2FA status</li>
<li>Which members hold Super Admin privileges</li>
<li>API access settings per member</li>
<li>Member onboarding state (accepted vs pending invite)</li>
</ul>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-30-member-management-screen.png" alt="Updated Member Management Overview" /></p>
<p><strong>New Member Permission Policies Details View</strong></p>
<p>We've created a new member details screen that shows all permission policies associated with a member; including policies inherited from group associations to make it easier for members to understand the effective permissions they have.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-30-permission-policies-screen.gif" alt="Updated Permission Policies Details Screen" /></p>
<p><strong>Improved Member Permission Workflow</strong></p>
<p>We redesigned the permission management experience to make it faster and easier for administrators to review roles and grant access.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-30-permission-policies-screen.gif" alt="Updated Member Permission Management UX" /></p>
<p><strong>Account-scoped Policies Restrictions Relaxed</strong></p>
<p>Previously, customers could only associate a single account-scoped policy with a member. We've relaxed this restriction, and now Administrators can now assign multiple account-scoped policies to the same member; bringing policy assignment behavior in-line with user-groups and providing greater flexibility in managing member permissions.</p>


<h2 id="new-tcp-based-fields-available-in-rulesets"><a href="/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/">New TCP-based fields available in Rulesets</a></h2>
<p><em>2025-10-30</em></p>
<h4 id="2025-10-30-tcp-rtt-and-tcp-fields-build-rules-based-on-tcp-transport-and-latency">Build rules based on TCP transport and latency</h4>
<p>Cloudflare now provides two new request fields in the Ruleset engine that let you make decisions based on whether a request used TCP and the measured TCP round-trip time between the client and Cloudflare. These fields help you understand protocol usage across your traffic and build policies that respond to network performance. For example, you can distinguish TCP from QUIC traffic or route high latency requests to alternative origins when needed.</p>
<hr />
<h4 id="2025-10-30-tcp-rtt-and-tcp-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.edge.client_tcp</code></td>
<td>Boolean</td>
<td>Indicates whether the request used TCP. A value of true means the client connected using TCP instead of QUIC.</td>
</tr>
<tr>
<td><code>cf.timings.client_tcp_rtt_msec</code></td>
<td>Number</td>
<td>Reports the smoothed TCP round-trip time between the client and Cloudflare in milliseconds. For example, a value of 20 indicates roughly twenty milliseconds of RTT.</td>
</tr>
</tbody>
</table>
<p>Example filter expression:</p>
<pre><code>cf.edge.client_tcp &amp;&amp; cf.timings.client_tcp_rtt_msec &lt; 100&#10;</code></pre>
<p>More information can be found in the Rules language <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>


<h2 id="azure-sentinel-connector"><a href="/changelog/post/2025-10-27-Sentinel-connector/">Azure Sentinel Connector</a></h2>
<p><em>2025-10-27</em></p>
<p>Logpush now supports integration with <a href="https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-sentinel">Microsoft Sentinel</a>.The new Azure Sentinel Connector built on Microsoft’s Codeless Connector Framework (CCF), is now available. This solution replaces the previous Azure Functions-based connector, offering significant improvements in security, data control, and ease of use for customers. Logpush customers can send logs to Azure Blob Storage and configure this new Sentinel Connector to ingest those logs directly into Microsoft Sentinel.</p>
<p>This upgrade significantly streamlines log ingestion, improves security, and provides greater control:</p>
<ul>
<li>Simplified Implementation: Easier for engineering teams to set up and maintain.</li>
<li>Cost Control: New support for Data Collection Rules (DCRs) allows you to filter and transform logs at ingestion time, offering potential cost savings.</li>
<li>Enhanced Security: CCF provides a higher level of security compared to the older Azure Functions connector.</li>
<li>Data Lake Integration: Includes native integration with Data Lake.</li>
</ul>
<p>Find the new solution <a href="https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview">here</a> and refer to the <a href="https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/#supported-logs:~:text=WorkBook%20fields,-Analytic%20rules">Cloudflare's developer documentation</a>for more information on the connector, including setup steps, supported logs and Microsoft's resources.</p>


<h2 id="new-robots-txt-tab-for-tracking-crawler-compliance"><a href="/changelog/post/2025-10-21-track-robots-txt/">New Robots.txt tab for tracking crawler compliance</a></h2>
<p><em>2025-10-21</em></p>
<p>AI Crawl Control now includes a <strong>Robots.txt</strong> tab that provides insights into how AI crawlers interact with your <code>robots.txt</code> files.</p>
<h4 id="2025-10-21-track-robots-txt-what-s-new">What's new</h4>
<p>The Robots.txt tab allows you to:</p>
<ul>
<li>Monitor the health status of <code>robots.txt</code> files across all your hostnames, including HTTP status codes, and identify hostnames that need a <code>robots.txt</code> file.</li>
<li>Track the total number of requests to each <code>robots.txt</code> file, with breakdowns of successful versus unsuccessful requests.</li>
<li>Check whether your <code>robots.txt</code> files contain <a href="https://contentsignals.org/">Content Signals</a> directives for AI training, search, and AI input.</li>
<li>Identify crawlers that request paths explicitly disallowed by your <code>robots.txt</code> directives, including the crawler name, operator, violated path, specific directive, and violation count.</li>
<li>Filter <code>robots.txt</code> request data by crawler, operator, category, and custom time ranges.</li>
</ul>
<h4 id="2025-10-21-track-robots-txt-take-action">Take action</h4>
<p>When you identify non-compliant crawlers, you can:</p>
<ul>
<li>Block the crawler in the <a href="/ai-crawl-control/features/manage-ai-crawlers/">Crawlers tab</a></li>
<li>Create custom <a href="/waf/">WAF rules</a> for path-specific security</li>
<li>Use <a href="/rules/url-forwarding/">Redirect Rules</a> to guide crawlers to appropriate areas of your site</li>
</ul>
<p>To get started, go to <strong>AI Crawl Control</strong> &gt; <strong>Robots.txt</strong> in the Cloudflare dashboard. Learn more in the <a href="/ai-crawl-control/features/track-robots-txt/">Track robots.txt documentation</a>.</p>


<h2 id="increased-http-header-size-limit-to-128-kb"><a href="/changelog/post/2025-10-16-header-limit-increase/">Increased HTTP header size limit to 128 KB</a></h2>
<p><em>2025-10-16</em></p>
<h4 id="2025-10-16-header-limit-increase-cdn-now-supports-128-kb-request-and-response-headers">CDN now supports 128 KB request and response headers 🚀</h4>
<p>We're excited to announce a significant increase in the maximum header size supported by Cloudflare's Content Delivery Network (CDN). Cloudflare now supports up to <strong>128 KB</strong> for both <strong>request and response headers</strong>.</p>
<p>Previously, customers were limited to a total of 32 KB for request or response headers, with a maximum of 16 KB per individual header. Larger headers could cause requests to fail with <code>HTTP 413</code> (Request Header Fields Too Large) errors.</p>
<hr />
<h4 id="2025-10-16-header-limit-increase-what-s-new">What's new?</h4>
<ul>
<li><strong>Support for large headers:</strong> You can now utilize much larger headers, whether as a single large header up to 128 KB or split over multiple headers.</li>
<li><strong>Reduces <code>413</code> and <code>520</code> HTTP errors:</strong> This change drastically reduces the likelihood of customers encountering <code>HTTP 413</code> errors from large request headers or <code>HTTP 520</code> errors caused by oversized response headers, improving the overall reliability of your web applications.</li>
<li><strong>Enhanced functionality:</strong> This is especially beneficial for applications that rely on:
<ul>
<li>A large number of cookies.</li>
<li>Large Content-Security-Policy (CSP) response headers.</li>
<li>Advanced use cases with Cloudflare Workers that generate large response headers.</li>
</ul>
</li>
</ul>
<p>This enhancement improves compatibility with Cloudflare's CDN, enabling more use cases that previously failed due to header size limits.</p>
<hr />
<p>To learn more and get started, refer to the <a href="/fundamentals/reference/connection-limits/#request-limits">Cloudflare Fundamentals documentation</a>.</p>


<h2 id="enhanced-ai-crawl-control-metrics-with-new-drilldowns-and-filters"><a href="/changelog/post/2025-10-14-enhanced-metrics-drilldowns/">Enhanced AI Crawl Control metrics with new drilldowns and filters</a></h2>
<p><em>2025-10-14</em></p>
<p>AI Crawl Control now provides enhanced metrics and CSV data exports to help you better understand AI crawler activity across your sites.</p>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-what-s-new">What's new</h4>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-track-crawler-requests-over-time">Track crawler requests over time</h4>
<p>Visualize crawler activity patterns over time, and group data by different dimensions:</p>
<ul>
<li><strong>By Crawler</strong> — Track activity from individual AI crawlers (GPTBot, ClaudeBot, Bytespider)</li>
<li><strong>By Category</strong> — Analyze crawler purpose or type</li>
<li><strong>By Operator</strong> — Discover which companies (OpenAI, Anthropic, ByteDance) are crawling your site</li>
<li><strong>By Host</strong> — Break down activity across multiple subdomains</li>
<li><strong>By Status Code</strong> — Monitor HTTP response codes to crawlers (200s, 300s, 400s, 500s)</li>
</ul>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-requests-over-time.png" alt="AI Crawl Control requests over time chart with grouping tabs" title="Interactive chart showing crawler requests over time with filterable dimensions" /></p>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-analyze-referrer-data-paid-plans">Analyze referrer data (Paid plans)</h4>
<p>Identify traffic sources with referrer analytics:</p>
<ul>
<li>View top referrers driving traffic to your site</li>
<li>Understand discovery patterns and content popularity from AI operators</li>
</ul>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-top-referrers.png" alt="AI Crawl Control top referrers breakdown" title="Bar chart showing top referrers and their respective traffic volumes" /></p>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-export-data">Export data</h4>
<p>Download your filtered view as a CSV:</p>
<ul>
<li>Includes all applied filters and groupings</li>
<li>Useful for custom reporting and deeper analysis</li>
</ul>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-get-started">Get started</h4>
<ol>
<li>Log in to the Cloudflare dashboard, and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong> &gt; <strong>Metrics</strong>.</li>
<li>Use the grouping tabs to explore different views of your data.</li>
<li>Apply filters to focus on specific crawlers, time ranges, or response codes.</li>
<li>Select <strong>Download CSV</strong> to export your filtered data for further analysis.</li>
</ol>
<p>Learn more about <a href="/ai-crawl-control">AI Crawl Control</a>.</p>


<h2 id="single-sign-on-now-manageable-in-the-user-experience"><a href="/changelog/post/2025-10-14-sso-self-service-ux/">Single sign-on now manageable in the user experience</a></h2>
<p><em>2025-10-14</em></p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-14-sso-configuration-ux.png" alt="Screenshot of new user experience for managing SSO" /></p>
<p>During Birthday Week, we announced that <a href="https://blog.cloudflare.com/enterprise-grade-features-for-all/">single sign-on (SSO) is available for free</a> to everyone who signs in with a custom email domain and maintains a compatible <a href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/">identity provider</a>. SSO minimizes user friction around login and provides the strongest security posture available. At the time, this could only be configured using the API.</p>
<p>Today, we are launching a new user experience which allows users to manage their SSO configuration from within the Cloudflare dashboard. You can access this by going to <strong>Manage account</strong> &gt; <strong>Members</strong> &gt; <strong>Settings</strong>.</p>
<h4 id="2025-10-14-sso-self-service-ux-for-more-information">For more information</h4>
<ul>
<li><a href="/fundamentals/manage-members/dashboard-sso/">Cloudflare dashboard SSO</a></li>
</ul>


<h2 id="automated-reminders-for-backup-codes"><a href="/changelog/post/2025-10-07-recovery-codes/">Automated reminders for backup codes</a></h2>
<p><em>2025-10-07</em></p>
<p>The most common reason users contact Cloudflare support is lost two-factor authentication (2FA) credentials. Cloudflare supports both app-based and hardware keys for 2FA, but you could lose access to your account if you lose these. Over the past few weeks, we have been rolling out email and in-product reminders that remind you to also download backup codes (sometimes called recovery keys) that can get you back into your account in the event you lose your 2FA credentials. Download your backup codes now by logging into Cloudflare, then navigating to <strong>Profile</strong> &gt; <strong>Security &amp; Authentication</strong> &gt; <strong>Backup codes</strong>.</p>
<h4 id="2025-10-07-recovery-codes-sign-in-security-best-practices">Sign-in security best practices</h4>
<p>Cloudflare is critical infrastructure, and you should protect it as such. Please review the following best practices and make sure you are doing your part to secure your account.</p>
<ul>
<li>Use a unique password for every website, including Cloudflare, and store it in a password manager like 1Password or Keeper. These services are cross-platform and simplify the process of managing secure passwords.</li>
<li>Use 2FA to make it harder for an attacker to get into your account in the event your password is leaked</li>
<li>Store your backup codes securely. A password manager is the best place since it keeps the backup codes encrypted, but you can also print them and put them somewhere safe in your home.</li>
<li>If you use an app to manage your 2FA keys, enable cloud backup, so that you don't lose your keys in the event you lose your phone.</li>
<li>If you use a custom email domain to sign in, <a href="https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/">configure SSO</a>.</li>
<li>If you use a public email domain like Gmail or Hotmail, you can also use social login with Apple, GitHub, or Google to sign in.</li>
<li>If you manage a Cloudflare account for work:
<ul>
<li>Have at least two administrators in case one of them unexpectedly leaves your company</li>
<li>Use SCIM to automate permissions management for members in your Cloudflare account</li>
</ul>
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


<h2 id="new-confidence-intervals-in-graphql-analytics-api"><a href="/changelog/post/2025-10-01-confidence-intervals/">New Confidence Intervals in GraphQL Analytics API</a></h2>
<p><em>2025-10-01</em></p>
<p>The GraphQL Analytics API now supports confidence intervals for <code>sum</code> and <code>count</code> fields on adaptive (sampled) datasets. Confidence intervals provide a statistical range around sampled results, helping verify accuracy and quantify uncertainty.</p>
<ul>
<li><strong>Supported datasets</strong>: Adaptive (sampled) datasets only.</li>
<li><strong>Supported fields</strong>: All <code>sum</code> and <code>count</code> fields.</li>
<li><strong>Usage</strong>: The confidence <code>level</code> must be provided as a decimal between 0 and 1 (e.g. <code>0.90</code>, <code>0.95</code>, <code>0.99</code>).</li>
<li><strong>Default</strong>: If no confidence level is specified, no intervals are returned.</li>
</ul>
<p>For examples and more details, see the <a href="/analytics/graphql-api/features/confidence-intervals/">GraphQL Analytics API documentation</a>.</p>


<h2 id="return-markdown"><a href="/changelog/post/2025-10-01-md-returned/">Return markdown</a></h2>
<p><em>2025-10-01</em></p>
<p>Users can now specify that they want to retrieve Cloudflare documentation as markdown rather than the previous HTML default. This can significantly reduce token consumption when used alongside Large Language Model (LLM) tools.</p>
<pre><code class="language-sh">curl https://developers.cloudflare.com/workers/ -H &#x27;Accept: text/markdown&#x27;  -v&#10;</code></pre>
<p>If you maintain your own site and want to adopt this practice using Cloudflare Workers for your own users you can follow the example <a href="https://github.com/cloudflare/cloudflare-docs/pull/25493">here</a>.</p>


<h2 id="sign-in-with-github"><a href="/changelog/post/2025-09-25-sign-in-with-github/">Sign in with GitHub</a></h2>
<p><em>2025-09-25</em></p>
<p>Cloudflare has launched sign in with GitHub as a log in option. This feature is available to all users with a verified email address who are not using SSO. To use it, simply click on the <code>Sign in with GitHub</code> button on the dashboard login page. You will be logged in with your primary GitHub email address.</p>
<h4 id="2025-09-25-sign-in-with-github-for-more-information">For more information</h4>
- [Log in to Cloudflare](/fundamentals/user-profiles/login/)


<h2 id="sso-for-all"><a href="/changelog/post/2025-09-25-sso-for-all/">SSO for all</a></h2>
<p><em>2025-09-25</em></p>
<p>Single sign-on (SSO) streamlines the process of logging into Cloudflare for Enterprise customers who manage a custom email domain and manage their own identity provider. Instead of managing a password and two-factor authentication credentials directly for Cloudflare, SSO lets you reuse your existing login infrastructure to seamlessly log in. SSO also provides additional security opportunities such as device health checks which are not available natively within Cloudflare.</p>
<p>Historically, SSO was only available for Enterprise accounts. Today, we are announcing that we are making SSO available to all users for free. We have also added the ability to directly manage SSO configurations using the API. This removes the previous requirement to contact support to configure SSO.</p>
<h4 id="2025-09-25-sso-for-all-for-more-information">For more information</h4>
<ul>
<li><a href="https://blog.cloudflare.com/enterprise-grade-features-for-all/">Every Cloudflare feature, available to all</a></li>
<li><a href="/fundamentals/manage-members/dashboard-sso/">Configure Dashboard SSO</a></li>
</ul>


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


<h2 id="contextual-pivots"><a href="/changelog/post/2025-09-11-contextual-pivots/">Contextual pivots</a></h2>
<p><em>2025-09-11</em></p>
<p>Directly from <a href="/log-explorer/log-search/">Log Search</a> results, customers can pivot to other parts of the Cloudflare dashboard to immediately take action as a result of their investigation.</p>
<p>From the <code>http_requests</code> or <code>fw_events</code> dataset results, right click on an IP Address or JA3 Fingerprint to pivot to the Investigate portal to lookup the reputation of an IP address or JA3 fingerprint.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/investigate-ip-address.png" alt="Investigate IP address" /></p>
<p>Easily learn about error codes by linking directly to our documentation from the <strong>EdgeResponseStatus</strong> or <strong>OriginResponseStatus</strong> fields.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/view-documentation.png" alt="View documentation" /></p>
<p>From the <code>gateway_http</code> dataset, click on a <strong>policyid</strong> to link directly to the Zero Trust dashboard to review or make changes to a specific Gateway policy.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/policyid.png" alt="View policy" /></p>


<h2 id="new-results-table-view"><a href="/changelog/post/2025-09-11-new-results-table-view/">New results table view</a></h2>
<p><em>2025-09-11</em></p>
<p>The results table view of <strong>Log Search</strong> has been updated with additional functionality and a more streamlined user experience. Users can now easily:</p>
<ul>
<li>Remove/add columns.</li>
<li>Resize columns.</li>
<li>Sort columns.</li>
<li>Copy values from any field.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/log-explorer/new-table.png" alt="New results table view" /></p>


<h2 id="reminders-about-two-factor-authentication-backup-codes"><a href="/changelog/post/2025-09-08-reminders-about-two-factor-authentication-backup-codes/">Reminders about two-factor authentication backup codes</a></h2>
<p><em>2025-09-08</em></p>
<p>Two-factor authentication is the best way to help protect your account from account takeovers, but if you lose your second factor, you could be locked out of your account. Lock outs are one of the top reasons customers contact Cloudflare support, and our policies often don't allow us to bypass two-factor authentication for customers that are locked out. Today we are releasing an improvement where Cloudflare will periodically remind you to securely save your backup codes so you don't get locked out in the future.</p>
<h4 id="2025-09-08-reminders-about-two-factor-authentication-backup-codes-for-more-information">For more information</h4>
- [Two-factor authentication](/fundamentals/user-profiles/2fa/)


<h2 id="introducing-new-headers-for-rate-limiting-on-cloudflare-s-api"><a href="/changelog/post/2025-09-03-rate-limiting-improvement/">Introducing new headers for rate limiting on Cloudflare's API</a></h2>
<p><em>2025-09-03</em></p>
<p>Cloudflare's API now supports rate limiting headers using the pattern developed by the <a href="https://ietf-wg-httpapi.github.io/ratelimit-headers/draft-ietf-httpapi-ratelimit-headers.html">IETF draft on rate limiting</a>. This allows API consumers to know how many more calls are left until the rate limit is reached, as well as how long you will need to wait until more capacity is available.</p>
<p>Our SDKs automatically work with these new headers, backing off when rate limits are approached. There is no action required for users of the latest Cloudflare SDKs to take advantage of this.</p>
<p>As always, if you need any help with rate limits, please contact Support.</p>
<h4 id="2025-09-03-rate-limiting-improvement-changes">Changes</h4>
<h4 id="2025-09-03-rate-limiting-improvement-new-headers">New Headers</h4>
<p><strong>Headers that are always returned:</strong></p>
<ul>
<li><code>Ratelimit</code>: List of service limit items, composed of the limit name, the remaining quota (<code>r</code>) and the time next window resets (<code>t</code>). For example: <code>&quot;default&quot;;r=50;t=30</code></li>
<li><code>Ratelimit-Policy</code>: List of quota policy items, composed of the policy name, the total quota (<code>q</code>) and the time window the quota applies to (<code>w</code>). For example: <code>&quot;burst&quot;;q=100;w=60</code></li>
</ul>
<p><strong>Returned only when a rate limit has been reached (error code: 429):</strong></p>
<ul>
<li>Retry-After: Number of Seconds until more capacity is available, rounded up</li>
</ul>
<h4 id="2025-09-03-rate-limiting-improvement-sdk-back-offs">SDK Back offs</h4>
- All of Cloudflare's latest SDKs will automatically respond to the headers, instituting a backoff when limits are approached. 
<h4 id="2025-09-03-rate-limiting-improvement-graphql-and-edge-apis">GraphQL and Edge APIs</h4>
These new headers and back offs are only available for Cloudflare REST APIs, and will not affect GraphQL. 
<h4 id="2025-09-03-rate-limiting-improvement-for-more-information">For more information</h4>
* [Rate limits at Cloudflare](https://developers.cloudflare.com/fundamentals/api/reference/limits/)


<h2 id="logging-headers-and-cookies-using-custom-fields"><a href="/changelog/post/2025-09-03-log-headers-and-cookies/">Logging headers and cookies using custom fields</a></h2>
<p><em>2025-09-03</em></p>
<p><a href="/log-explorer/">Log Explorer</a> now supports logging and filtering on header or cookie fields in the <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/"><code>http_requests</code> dataset</a>.</p>
<p>Create a custom field to log desired header or cookie values into the <code>http_requests</code> dataset and Log Explorer will import these as searchable fields. Once configured, use the custom SQL editor in Log Explorer to view or filter on these requests.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/edit-custom-fields.png" alt="Edit Custom fields" /></p>
<p>For more details, refer to <a href="/log-explorer/log-search/#headers-and-cookies">Headers and cookies</a>.</p>


<h2 id="cloudflare-tunnel-and-networks-api-will-no-longer-return-deleted-resources-by-default-starting-december-1-2025"><a href="/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/">Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025</a></h2>
<p><em>2025-09-02</em></p>
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
<pre><code class="language-bash">&#35; Example: Get ONLY deleted Tunnels&#10;curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tunnels?is_deleted=true&quot; \&#10;     &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;&#10;&#35; Example: Get ONLY deleted Virtual Networks&#10;curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/virtual_networks?is_deleted=true&quot; \&#10;     &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<p>Following this change, retrieving a complete list of both active and deleted resources will require two separate API calls: one to get active items (by omitting the parameter or using <code>is_deleted=false</code>) and one to get deleted items (<code>is_deleted=true</code>).</p>
<h4 id="2025-09-02-tunnel-networks-list-endpoints-new-default-why-we-re-making-this-change">Why we’re making this change</h4>
This update is based on user feedback and aims to:
* **Create a more intuitive default:** Aligning with common API design principles where list operations return only active resources by default.
* **Reduce unexpected results:** Prevents users from accidentally operating on deleted resources that were returned unexpectedly.
* **Improve performance:** For most users, the default query result will now be smaller and more relevant.
<p>To learn more, please visit the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a> and <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> documentation.</p>


<h2 id="terraform-v5-9-now-available"><a href="/changelog/post/2025-08-29-terrform-v5.9-provider/">Terraform v5.9 now available</a></h2>
<p><em>2025-08-29</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadence to ensure its stability and reliability, including the v5.9 release. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release, and closing all associated bugs with that resource before moving onto resolving migration issues.</p>
<p>Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.</p>
<p>This release includes a new resource, <code>cloudflare_snippet</code>, which replaces <code>cloudflare_snippets</code>. <code>cloudflare_snippet</code> is now considered deprecated but can still be used. Please utilize <code>cloudflare_snippet</code> as soon as possible.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-changes">Changes</h4>
- Resources stabilized:
  - `cloudflare_zone_setting`
  - `cloudflare_worker_script`
  - `cloudflare_worker_route`
  - `tiered_cache`
- **NEW** resource `cloudflare_snippet` which should be used in place of `cloudflare_snippets`. `cloudflare_snippets` is now deprecated. This enables the management of Cloudflare's snippet functionality through Terraform.
- DNS Record Improvements: Enhanced handling of DNS record drift detection
- Load Balancer Fixes: Resolved `created_on` field inconsistencies and improved pool configuration handling
- Bot Management: Enhanced auto-update model state consistency and fight mode configurations
- Other bug fixes
<p>For a more detailed look at all of the changes, refer to the
<a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.9.0">changelog</a> in GitHub.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-issues-closed">Issues Closed</h4>
- [#5921: In cloudflare_ruleset removing an existing rule causes recreation of later rules](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5921)
- [#5904: cloudflare_zero_trust_access_application is not idempotent](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5904)
- [#5898: (cloudflare_workers_script) Durable Object migrations not applied](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5898)
- [#5892: cloudflare_workers_script secret_text environment variable gets replaced on every deploy](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5892)
- [#5891: cloudflare_zone suddenly started showing drift](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5891)
- [#5882: cloudflare_zero_trust_list always marked for change due to read only attributes](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5882)
- [#5879: cloudflare_zero_trust_gateway_certificate unable to manage resource (cant mark as active/inactive)](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5879)
- [#5858: cloudflare_dns_records is always updated in-place](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5858)
- [#5839: Recurring change on cloudflare_zero_trust_gateway_policy after upgrade to V5 provider & also setting expiration fails](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5839)
- [#5811: Reusable policies are imported as inline type for cloudflare_zero_trust_access_application](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5811)
- [#5795: cloudflare_zone_setting inconsistent value of "editable" upon apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5795)
- [#5789: Pagination issue fetching all policies in "cloudflare_zero_trust_access_policies" data source](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5789)
- [#5770: cloudflare_zero_trust_access_application type warp diff on every apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5770)
- [#5765: V5 / cloudflare_zone_dnssec fails with HTTP/400 "Malformed request body"](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5765)
- [#5755: Unable to manage Cloudflare managed WAF rules via Terraform](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5755)
- [#5738: v4 to v5 upgrade failing Error: no schema available AND Unable to Read Previously Saved State for UpgradeResourceState](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5738)
- [#5727: cloudflare_ruleset http_request_cache_settings bypass mismatch between dashboard and terraform](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5727)
- [#5700: cloudflare_account_member invalid type 'string' for field 'roles'](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5700)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new issue if one does not already exist for what you are experiencing.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-upgrading">Upgrading</h4>
<p>We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.</p>
<p>If you'd like more information on migrating from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition. These do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test
your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
<li><a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub Repository</a></li>
</ul>


<h2 id="enhanced-crawler-insights-and-custom-402-responses"><a href="/changelog/post/2025-08-27-ai-crawl-control-launch/">Enhanced crawler insights and custom 402 responses</a></h2>
<p><em>2025-08-27</em></p>
<p>We improved AI crawler management with detailed analytics and introduced custom HTTP 402 responses for blocked crawlers. AI Audit has been renamed to AI Crawl Control and is now generally available.</p>
<p><strong>Enhanced Crawlers tab:</strong></p>
<ul>
<li>View total allowed and blocked requests for each AI crawler</li>
<li>Trend charts show crawler activity over your selected time range per crawler</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-table.png" alt="Updated AI Crawl Control table showing request counts and trend charts" /></p>
<p><strong>Custom block responses (paid plans):</strong>
You can now return HTTP 402 &quot;Payment Required&quot; responses when blocking AI crawlers, enabling direct communication with crawler operators about licensing terms.</p>
<p>For users on paid plans, when blocking AI crawlers you can configure:</p>
<ul>
<li><strong>Response code:</strong> Choose between 403 Forbidden or 402 Payment Required</li>
<li><strong>Response body:</strong> Add a custom message with your licensing contact information</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-block-response.png" alt="AI Crawl Control block response configuration interface" /></p>
<p>Example 402 response:</p>
<pre><code class="language-http">HTTP 402 Payment Required&#10;Date: Mon, 24 Aug 2025 12:56:49 GMT&#10;Content-type: application/json&#10;Server: cloudflare&#10;Cf-Ray: 967e8da599d0c3fa-EWR&#10;Cf-Team: 2902f6db750000c3fa1e2ef400000001&#10;&#10;{&#10;  &quot;message&quot;: &quot;Please contact the site owner for access.&quot;&#10;}&#10;</code></pre>


<h2 id="audit-logs-version-2-logpush-beta-release"><a href="/changelog/post/2025-08-22-audit-logs-v2-logpush/">Audit logs (version 2) - Logpush Beta Release</a></h2>
<p><em>2025-08-22</em></p>
<p><a href="/logs/logpush/logpush-job/datasets/account/audit_logs_v2/">Audit Logs v2 dataset</a> is now available via Logpush.</p>
<p>This expands on earlier releases of Audit Logs v2 in the <a href="/changelog/2025-03-27-automatic-audit-logs-beta-release/">API</a> and <a href="/changelog/2025-07-29-audit-logs-v2-ui-beta/">Dashboard UI</a>.</p>
<p>We recommend creating a new Logpush job for the Audit Logs v2 dataset.</p>
<p>Timelines for General Availability (GA) of Audit Logs v2 and the retirement of Audit Logs v1 will be shared in upcoming updates.</p>
<p>For more details on Audit Logs v2, refer to the <a href="https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/">Audit Logs documentation</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/core-platform/5/">Previous</a><span>Page 6 of 8</span><a class="pagination-next" rel="next" href="/changelog/product-group/core-platform/7/">Next</a></nav>
