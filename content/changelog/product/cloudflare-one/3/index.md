<h1 id="changelog">Changelog</h1>

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


<h2 id="new-ai-enabled-search-for-zero-trust-dashboard"><a href="/changelog/post/2025-09-16-new-ai-enabled-search-for-zero-trust-dashboard/">New AI-Enabled Search for Zero Trust Dashboard</a></h2>
<p><em>2025-09-16</em></p>
<p>Zero Trust Dashboard has a brand new, AI-powered search functionality. You can search your account by resources (applications, policies, device profiles, settings, etc.), pages, products, and more.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/searchexample.png" alt="Example search results in the Zero Trust dashboard" /></p>
<p><strong>Ask Cloudy</strong> — You can also ask Cloudy, our AI agent, questions about Cloudflare Zero Trust. Cloudy is trained on our developer documentation and implementation guides, so it can tell you how to configure functionality, best practices, and can make recommendations.</p>
<p>Cloudy can then stay open with you as you move between pages to build configuration or answer more questions.</p>
<p><strong>Find Recents</strong> — Recent searches and Cloudy questions also have a new tab under Zero Trust Overview.</p>


<h2 id="shadow-it-saas-analytics-dashboard"><a href="/changelog/post/2025-08-27-shadow-it-analytics/">Shadow IT - SaaS analytics dashboard</a></h2>
<p><em>2025-08-27</em></p>
<p>Zero Trust has significantly upgraded its <strong>Shadow IT analytics</strong>, providing you with unprecedented visibility into your organizations use of SaaS tools. With this dashboard, you can review who is using an application and volumes of data transfer to the application.</p>
<p>You can review these metrics against application type, such as Artificial Intelligence or Social Media. You can also mark applications with an approval status, including <strong>Unreviewed</strong>, <strong>In Review</strong>, <strong>Approved</strong>, and <strong>Unapproved</strong> designating how they can be used in your organization.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/shadow-it-analytics.png" alt="Cloudflare One Analytics Dashboards" /></p>
<p>These application statuses can also be used in Gateway HTTP policies, so you can block, isolate, limit uploads and downloads, and more based on the application status.</p>
<p>Both the analytics and policies are accessible in the Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, empowering organizations with better visibility and control.</p>


<h2 id="virtual-cloudflare-one-appliance-with-kvm-support-open-beta"><a href="/changelog/post/2025-07-21-virtual-appliance-kvm-proxmox/">Virtual Cloudflare One Appliance with KVM support (open beta)</a></h2>
<p><em>2025-07-21</em></p>
<p>The KVM-based virtual Cloudflare One Appliance is now in open beta with official support for Proxmox VE.</p>
<p>Customers can deploy the virtual appliance on KVM hypervisors to connect branch or data center networks to Cloudflare WAN without dedicated hardware.</p>
<p>For setup instructions, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a virtual Cloudflare One Appliance</a>.</p>


<h2 id="new-onboarding-guides-for-zero-trust"><a href="/changelog/post/2025-07-09-onboarding-resources/">New onboarding guides for Zero Trust</a></h2>
<p><em>2025-07-10</em></p>
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


<h2 id="cloudy-summaries-for-access-and-gateway-logs"><a href="/changelog/post/2025-07-07-cloudy-summaries-access-gateway/">Cloudy summaries for Access and Gateway Logs</a></h2>
<p><em>2025-07-07</em></p>
<p>Cloudy, Cloudflare's AI Agent, will now automatically summarize your <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/">Access</a> and <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway</a> block logs.</p>
<p>In the log itself, Cloudy will summarize what occurred and why. This will be helpful for quick troubleshooting and issue correlation.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/cloudy-explanation.png" alt="Cloudy AI summarizes a log" /></p>
<p>If you have feedback about the Cloudy summary - good or bad - you can provide that right from the summary itself.</p>


<h2 id="new-app-library-for-zero-trust-dashboard"><a href="/changelog/post/2025-07-07-dashboard-app-library/">New App Library for Zero Trust Dashboard</a></h2>
<p><em>2025-07-07</em></p>
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


<h2 id="data-security-analytics-in-the-zero-trust-dashboard"><a href="/changelog/post/cf1-data-security-analytics-v1/">Data Security Analytics in the Zero Trust dashboard</a></h2>
<p><em>2025-06-23T09:00:00+00:00</em></p>
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


<h2 id="cloudflare-one-analytics-dashboards-and-exportable-access-report"><a href="/changelog/post/dashboards-access-report/">Cloudflare One Analytics Dashboards and Exportable Access Report</a></h2>
<p><em>2025-06-05</em></p>
<p>Cloudflare One now offers powerful new analytics dashboards to help customers easily discover available insights into their application access and network activity. These dashboards provide a centralized, intuitive view for understanding user behavior, application usage, and security posture.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/Analytics Dashboards.png" alt="Cloudflare One Analytics Dashboards"></p>
<p>Additionally, a new exportable access report is available, allowing customers to quickly view high-level metrics and trends in their application access. A <strong>preview</strong> of the report is shown below, with more to be found in the report:</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-report.png" alt="Cloudflare One Analytics Dashboards" /></p>
<p>Both features are accessible in the Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, empowering organizations with better visibility and control.</p>


<h2 id="new-gateway-analytics-in-the-cloudflare-one-dashboard"><a href="/changelog/post/gateway-analytics-v2/">New Gateway Analytics in the Cloudflare One Dashboard</a></h2>
<p><em>2025-05-29</em></p>
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


<h2 id="new-applications-added-to-zero-trust"><a href="/changelog/post/new-applications-71825/">New Applications Added to Zero Trust</a></h2>
<p><em>2025-05-18</em></p>
<p>42 new applications have been added for Zero Trust support within the Application Library and Gateway policy enforcement, giving you the ability to investigate or apply inline policies to these applications.</p>
<p>33 of the 42 applications are Artificial Intelligence applications. The others are Human Resources (2 applications), Development (2 applications), Productivity (2 applications), Sales &amp; Marketing, Public Cloud, and Security.</p>
<p>To view all available applications, log in to your Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, navigate to the <strong>App Library</strong> under <strong>My Team</strong>.</p>
<p>For more information on creating Gateway policies, see our <a href="/cloudflare-one/traffic-policies/">Gateway policy documentation</a>.</p>


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


<h2 id="configure-your-magic-wan-connector-to-connect-via-static-ip-assignment"><a href="/changelog/post/2025-02-14-local-console-access/">Configure your Magic WAN Connector to connect via static IP assignment</a></h2>
<p><em>2025-02-14</em></p>
<p>You can now locally configure your <a href="/cloudflare-wan/configuration/appliance/">Magic WAN Connector</a> to work in a static IP configuration.</p>
<p>This local method does not require having access to a DHCP Internet connection. However, it does require being comfortable with using tools to access the serial port on Magic WAN Connector as well as using a serial terminal client to access the Connector's environment.</p>
<p>For more details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#bootstrap-via-serial-console">WAN with a static IP address</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/cloudflare-one/2/">Previous</a><span>Page 3 of 3</span></nav>
