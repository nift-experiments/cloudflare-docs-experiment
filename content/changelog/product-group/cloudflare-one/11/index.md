---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/cloudflare-one/11/
  description: '2025-07-21'
  full_title: Cloudflare One changelog - page 11 | Cloudflare Docs
  head_html: <title>Cloudflare One changelog - page 11 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-07-21"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/11/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cloudflare One changelog - page 11"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-07-21"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/cloudflare-one/11/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/11/#page","headline":"Cloudflare One changelog - page 11 | Cloudflare Docs","description":"2025-07-21","url":"https://developers.cloudflare.com/changelog/product-group/cloudflare-one/11/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/cloudflare-one/11/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="virtual-cloudflare-one-appliance-with-kvm-support-open-beta"><a href="/changelog/post/2025-07-21-virtual-appliance-kvm-proxmox/">Virtual Cloudflare One Appliance with KVM support (open beta)</a></h2>
<p><em>2025-07-21</em></p>
<p>The KVM-based virtual Cloudflare One Appliance is now in open beta with official support for Proxmox VE.</p>
<p>Customers can deploy the virtual appliance on KVM hypervisors to connect branch or data center networks to Cloudflare WAN without dedicated hardware.</p>
<p>For setup instructions, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a virtual Cloudflare One Appliance</a>.</p>


<h2 id="new-detection-entry-type-document-matching-for-dlp"><a href="/changelog/post/2025-07-17-document-matching/">New detection entry type: Document Matching for DLP</a></h2>
<p><em>2025-07-17</em></p>
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


<h2 id="faster-more-reliable-udp-traffic-for-cloudflare-tunnel"><a href="/changelog/post/2025-07-15-udp-improvements/">Faster, more reliable UDP traffic for Cloudflare Tunnel</a></h2>
<p><em>2025-07-15</em></p>
<p>Your real-time applications running over <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> are now faster and more reliable. We've completely re-architected the way <code>cloudflared</code> proxies UDP traffic in order to isolate it from other traffic, ensuring latency-sensitive applications like private DNS are no longer slowed down by heavy TCP traffic (like file transfers) on the same Tunnel.</p>
<p>This is a foundational improvement to Cloudflare Tunnel, delivered automatically to all customers. There are no settings to configure — your UDP traffic is already flowing faster and more reliably.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li><strong>Faster UDP performance</strong>: We've significantly reduced the latency for establishing new UDP sessions, making applications like private DNS much more responsive.</li>
<li><strong>Greater reliability for mixed traffic</strong>: UDP packets are no longer affected by heavy TCP traffic, preventing timeouts and connection drops for your real-time services.</li>
</ul>
<p>Learn more about running <a href="/reference-architecture/architectures/sase/#connecting-applications">TCP or UDP applications</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">private networks</a> through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>.</p>


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


<h2 id="cloudflare-one-agent-for-android-version-2-4-2"><a href="/changelog/post/2025-06-30-warp-ga-android/">Cloudflare One Agent for Android (version 2.4.2)</a></h2>
<p><em>2025-06-30</em></p>
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


<h2 id="cloudflare-one-agent-for-ios-version-1-11"><a href="/changelog/post/2025-06-30-warp-ga-ios/">Cloudflare One Agent for iOS (version 1.11)</a></h2>
<p><em>2025-06-30</em></p>
<p>A new GA release for the iOS Cloudflare One Agent is now available in the <a href="https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492">iOS App Store</a>. This release
contains improvements and new exciting features, including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum">post-quantum cryptography</a>.
By tunneling your corporate network traffic over Cloudflare, you can now gain the immediate <a href="https://blog.cloudflare.com/pq-2024/">protection of post-quantum cryptography</a> without needing to upgrade any of your individual corporate applications or systems.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>QLogs are now disabled by default and can be enabled in the app by turning on <strong>Enable qlogs</strong> under <strong>Settings</strong> &gt; <strong>Advanced</strong> &gt; <strong>Diagnostics</strong> &gt; <strong>Debug Logs</strong>. The QLog setting from previous releases will no longer be respected.</li>
<li>DNS over HTTPS traffic is now included in the WARP tunnel by default.</li>
<li>The WARP client now applies <a href="https://blog.cloudflare.com/pq-2024/">post-quantum cryptography</a> end-to-end on enabled devices accessing resources behind a Cloudflare Tunnel. This feature can be enabled by <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum">MDM</a>.</li>
</ul>


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


<h2 id="gateway-will-now-evaluate-network-policies-before-http-policies-from-july-14th-2025"><a href="/changelog/post/2025-06-17-new-order-of-enforcement/">Gateway will now evaluate Network policies before HTTP policies from July 14th, 2025</a></h2>
<p><em>2025-06-18</em></p>
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


<h2 id="cloudflare-one-analytics-dashboards-and-exportable-access-report"><a href="/changelog/post/dashboards-access-report/">Cloudflare One Analytics Dashboards and Exportable Access Report</a></h2>
<p><em>2025-06-05</em></p>
<p>Cloudflare One now offers powerful new analytics dashboards to help customers easily discover available insights into their application access and network activity. These dashboards provide a centralized, intuitive view for understanding user behavior, application usage, and security posture.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/Analytics Dashboards.png" alt="Cloudflare One Analytics Dashboards"></p>
<p>Additionally, a new exportable access report is available, allowing customers to quickly view high-level metrics and trends in their application access. A <strong>preview</strong> of the report is shown below, with more to be found in the report:</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-report.png" alt="Cloudflare One Analytics Dashboards" /></p>
<p>Both features are accessible in the Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, empowering organizations with better visibility and control.</p>


<h2 id="new-account-level-load-balancing-ui-and-private-load-balancers"><a href="/changelog/post/2025-06-04-account-load-balancing-ui/">New Account-Level Load Balancing UI and Private Load Balancers</a></h2>
<p><em>2025-06-04</em></p>
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


<h2 id="gateway-protocol-detection-now-available-for-pay-as-you-go-and-free-plans"><a href="/changelog/post/2025-05-27-Protocol-Detection-availability/">Gateway Protocol Detection Now Available for Pay-as-you-go and Free Plans</a></h2>
<p><em>2025-05-27</em></p>
<p>All Cloudflare One Gateway users can now use Protocol detection logging and filtering, including those on Pay-as-you-go and Free plans.</p>
<p>With Protocol Detection, admins can identify and enforce policies on traffic proxied through Gateway based on the underlying network protocol (for example, HTTP, TLS, or SSH), enabling more granular traffic control and security visibility no matter your plan tier.</p>
<p>This feature is available to enable in your account network settings for all accounts. For more information on using Protocol Detection, refer to the <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">Protocol detection documentation</a>.</p>


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


<h2 id="open-email-attachments-with-browser-isolation"><a href="/changelog/post/2025-05-08-open-attachments-with-browser-isolation/">Open email attachments with Browser Isolation</a></h2>
<p><em>2025-05-15T23:22:49+00:00</em></p>
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


<h2 id="domain-categories-improvements"><a href="/changelog/post/2025-05-14-domain-category-improvements/">Domain Categories improvements</a></h2>
<p><em>2025-05-14</em></p>
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


<h2 id="saml-http-post-bindings-support-for-rbi"><a href="/changelog/post/2025-05-13-rbi-saml-post-support/">SAML HTTP-POST bindings support for RBI</a></h2>
<p><em>2025-05-13</em></p>
<p>Remote Browser Isolation (RBI) now supports SAML HTTP-POST bindings, enabling seamless authentication for SSO-enabled applications that rely on POST-based SAML responses from Identity Providers (IdPs) within a Remote Browser Isolation session. This update resolves a previous limitation that caused <code>405</code> errors during login and improves compatibility with multi-factor authentication (MFA) flows.</p>
<p>With expanded support for major IdPs like Okta and Azure AD, this enhancement delivers a more consistent and user-friendly experience across authentication workflows. Learn how to <a href="/cloudflare-one/remote-browser-isolation/setup/">set up Remote Browser Isolation</a>.</p>


<h2 id="new-applications-added-for-dns-filtering"><a href="/changelog/post/2025-05-13-new-applications-added/">New Applications Added for DNS Filtering</a></h2>
<p><em>2025-05-13</em></p>
<p>You can now create DNS policies to manage outbound traffic for an expanded list of applications.
This update adds support for 273 new applications, giving you more control over your organization's outbound traffic.</p>
<p>With this update, you can:</p>
<ul>
<li>Create DNS policies for a wider range of applications</li>
<li>Manage outbound traffic more effectively</li>
<li>Improve your organization's security and compliance posture</li>
</ul>
<p>For more information on creating DNS policies, see our <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policy documentation</a>.</p>


<h2 id="case-sensitive-custom-word-lists"><a href="/changelog/post/2025-05-12-case-sensitive-cwl/">Case Sensitive Custom Word Lists</a></h2>
<p><em>2025-05-12</em></p>
<p>You can now configure <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#custom-wordlist-datasets">custom word lists</a> to enforce case sensitivity. This setting supports flexibility where needed and aims to reduce false positives where letter casing is critical.</p>
<p><img src="/assets/upstream/images/changelog/dlp/case-sesitive-cwl.png" alt="dlp" /></p>


<h2 id="open-email-links-with-browser-isolation"><a href="/changelog/post/2025-05-15-open-links-browser-isolation/">Open email links with Browser Isolation</a></h2>
<p><em>2025-05-08T23:22:49+00:00</em></p>
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


<h2 id="send-forensic-copies-to-storage-without-dlp-profiles"><a href="/changelog/post/2025-05-07-forensic-copy-update/">Send forensic copies to storage without DLP profiles</a></h2>
<p><em>2025-05-07</em></p>
<p>You can now <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#send-dlp-forensic-copies-to-logpush-destination">send DLP forensic copies</a> to third-party storage for any HTTP policy with an <code>Allow</code> or <code>Block</code> action, without needing to include a DLP profile. This change increases flexibility for data handling and forensic investigation use cases.</p>
<p>By default, Gateway will send all matched HTTP requests to your configured DLP Forensic Copy jobs.</p>
<p><img src="/assets/upstream/images/changelog/dlp/forensic-copies-for-all.png" alt="DLP" /></p>


<h2 id="udp-and-icmp-monitor-support-for-private-load-balancing-endpoints"><a href="/changelog/post/2025-05-06-private-health-monitoring-methods/">UDP and ICMP Monitor Support for Private Load Balancing Endpoints</a></h2>
<p><em>2025-05-06</em></p>
<p>Cloudflare Load Balancing now supports <strong>UDP (Layer 4)</strong> and <strong>ICMP (Layer 3)</strong> health monitors for <strong>private endpoints</strong>. This makes it simple to track the health and availability of internal services that don’t respond to HTTP, TCP, or other protocol probes.</p>
<h4 id="2025-05-06-private-health-monitoring-methods-what-you-can-do">What you can do:</h4>
<ul>
<li>Set up <strong>ICMP ping monitors</strong> to check if your private endpoints are reachable.</li>
<li>Use <strong>UDP monitors</strong> for lightweight health checks on non-TCP workloads, such as DNS, VoIP, or custom UDP-based services.</li>
<li>Gain better visibility and uptime guarantees for services running behind <strong>Private Network Load Balancing</strong>, without requiring public IP addresses.</li>
</ul>
<p>This enhancement is ideal for internal applications that rely on low-level protocols, especially when used in conjunction with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/"><strong>Cloudflare Tunnel</strong></a>, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/"><strong>WARP</strong></a>, and <a href="/cloudflare-wan/"><strong>Magic WAN</strong></a> to create a secure and observable private network.</p>
<p>Learn more about <a href="/load-balancing/private-network/">Private Network Load Balancing</a> or view the full list of <a href="/load-balancing/monitors/#supported-protocols">supported health monitor protocols</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/cloudflare-one/10/">Previous</a><span>Page 11 of 13</span><a class="pagination-next" rel="next" href="/changelog/product-group/cloudflare-one/12/">Next</a></nav>
