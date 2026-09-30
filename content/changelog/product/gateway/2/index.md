<h1 id="changelog">Changelog</h1>

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


<h2 id="dns-filtering-for-private-network-onramps"><a href="/changelog/post/2025-09-11-dns-filtering-for-private-network-onramps/">DNS filtering for private network onramps</a></h2>
<p><em>2025-09-11</em></p>
<p><a href="/cloudflare-wan/zero-trust/cloudflare-gateway/#dns-filtering">Magic WAN</a> and <a href="/mesh/features/routes/#dns-filtering">WARP Connector</a> users can now securely route their DNS traffic to the Gateway resolver without exposing traffic to the public Internet.</p>
<p>Routing DNS traffic to the Gateway resolver allows DNS resolution and filtering for traffic coming from private networks while preserving source internal IP visibility. This ensures Magic WAN users have full integration with our Cloudflare One features, including <a href="/cloudflare-one/traffic-policies/resolver-policies/#internal-dns">Internal DNS</a> and <a href="/cloudflare-one/traffic-policies/egress-policies/#selector-prerequisites">hostname-based policies</a>.</p>
<p>To configure DNS filtering, change your Magic WAN or WARP Connector DNS settings to use Cloudflare's shared resolver IPs, <code>172.64.36.1</code> and <code>172.64.36.2</code>. Once you configure DNS resolution and filtering, you can use <em>Source Internal IP</em> as a traffic selector in your <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a> for routing private DNS traffic to your <a href="/dns/internal-dns/">Internal DNS</a>.</p>


<h2 id="shadow-it-saas-analytics-dashboard"><a href="/changelog/post/2025-08-27-shadow-it-analytics/">Shadow IT - SaaS analytics dashboard</a></h2>
<p><em>2025-08-27</em></p>
<p>Zero Trust has significantly upgraded its <strong>Shadow IT analytics</strong>, providing you with unprecedented visibility into your organizations use of SaaS tools. With this dashboard, you can review who is using an application and volumes of data transfer to the application.</p>
<p>You can review these metrics against application type, such as Artificial Intelligence or Social Media. You can also mark applications with an approval status, including <strong>Unreviewed</strong>, <strong>In Review</strong>, <strong>Approved</strong>, and <strong>Unapproved</strong> designating how they can be used in your organization.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/shadow-it-analytics.png" alt="Cloudflare One Analytics Dashboards" /></p>
<p>These application statuses can also be used in Gateway HTTP policies, so you can block, isolate, limit uploads and downloads, and more based on the application status.</p>
<p>Both the analytics and policies are accessible in the Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, empowering organizations with better visibility and control.</p>


<h2 id="gateway-byoip-dedicated-egress-ips-now-available"><a href="/changelog/post/2025-08-21-byoip-dedicated-egress-ip/">Gateway BYOIP Dedicated Egress IPs now available.</a></h2>
<p><em>2025-08-21</em></p>
<p>Enterprise Gateway users can now use Bring Your Own IP (BYOIP) for dedicated egress IPs.</p>
<p>Admins can now onboard and use their own IPv4 or IPv6 prefixes to egress traffic from Cloudflare, delivering greater control, flexibility, and compliance for network traffic.</p>
<p>Get started by following the <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip">BYOIP onboarding process</a>. Once your IPs are onboarded, go to <strong>Gateway</strong> &gt; <strong>Egress policies</strong> and select or create an egress policy. In <strong>Select an egress IP</strong>, choose <em>Use dedicated egress IPs (Cloudflare or BYOIP)</em>, then select your BYOIP address from the dropdown menu.</p>
<p><img src="/assets/upstream/images/gateway/Gateway-byoip-dedicated-egress-ips.png" alt="Screenshot of a dropdown menu adding a BYOIP IPv4 address as a dedicated egress IP in a Gateway egress policy" /></p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip">BYOIP for dedicated egress IPs</a>.</p>


<h2 id="scam-domain-category-introduced-under-security-threats"><a href="/changelog/post/2025-07-28-Spam-domain-category-introduced/">Scam domain category introduced under Security Threats</a></h2>
<p><em>2025-07-28</em></p>
<p>We have introduced a new Security Threat category called <strong>Scam</strong>. Relevant domains are marked with the Scam category. Scam typically refers to fraudulent websites and schemes designed to trick victims into giving away money or personal information.</p>
<p><strong>New category added</strong></p>
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
<td>21</td>
<td>Security Threats</td>
<td>191</td>
<td>Scam</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">Gateway domain categories</a> to learn more.</p>


<h2 id="gateway-http-filtering-on-all-ports-available-in-open-beta"><a href="/changelog/post/2025-07-24-HTTP-Inspection-on-all-ports/">Gateway HTTP Filtering on all ports available in open BETA</a></h2>
<p><em>2025-07-24</em></p>
<p><a href="/cloudflare-one/traffic-policies/">Gateway</a> can now apply <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP filtering</a> to all proxied HTTP requests, not just traffic on standard HTTP (<code>80</code>) and HTTPS (<code>443</code>) ports. This means all requests can now be filtered by <a href="/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/">A/V scanning</a>, <a href="/cloudflare-one/traffic-policies/http-policies/file-sandboxing/">file sandboxing</a>, <a href="/cloudflare-one/data-loss-prevention/#data-in-transit">Data Loss Prevention (DLP)</a>, and more.</p>
<p>You can turn this <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports">setting</a> on by going to <strong>Settings</strong> &gt; <strong>Network</strong> &gt; <strong>Firewall</strong> and choosing  <em>Inspect on all ports</em>.</p>
<p><img src="/assets/upstream/images/gateway/Gateway-Inspection-all-ports.png" alt="HTTP Inspection on all ports setting" /></p>
<p>To learn more, refer to <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports">Inspect on all ports (Beta)</a>.</p>


<h2 id="google-bard-application-replaced-by-gemini"><a href="/changelog/post/2025-08-15-gemini-application-replaces-bard/">Google Bard Application replaced by Gemini</a></h2>
<p><em>2025-07-22</em></p>
<p>The <strong>Google Bard</strong> application (ID: 1198) has been deprecated and fully removed from the system. It has been replaced by the <strong>Gemini</strong> application (ID: 1340).
Any existing Gateway policies that reference the old Google Bard application will no longer function.
To ensure your policies continue to work as intended, you should update them to use the new Gemini application.
We recommend replacing all instances of the deprecated Bard application with the new Gemini application in your Gateway policies.
For more information about application policies, please see the <a href="/cloudflare-one/traffic-policies/application-app-types/">Cloudflare Gateway documentation</a>.</p>


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


<h2 id="http-redirect-and-custom-block-page-redirect"><a href="/changelog/post/2025-04-11-http-redirect-custom-block-page-redirect/">HTTP redirect and custom block page redirect</a></h2>
<p><em>2025-04-11</em></p>
<p>You can now use more flexible redirect capabilities in Cloudflare One with Gateway.</p>
<ul>
<li>A new <strong>Redirect</strong> action is available in the HTTP policy builder, allowing admins to redirect users to any URL when their request matches a policy. You can choose to preserve the original URL and query string, and optionally include policy context via query parameters.</li>
<li>For <strong>Block</strong> actions, admins can now configure a custom URL to display when access is denied. This block page redirect is set at the account level and can be overridden in DNS or HTTP policies. Policy context can also be passed along in the URL.</li>
</ul>
<p>Learn more in our documentation for <a href="/cloudflare-one/traffic-policies/http-policies/#redirect">HTTP Redirect</a> and <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#redirect-to-a-block-page">Block page redirect</a>.</p>


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


<h2 id="explore-product-updates-for-cloudflare-one"><a href="/changelog/post/2024-06-16-cloudflare-one/">Explore product updates for Cloudflare One</a></h2>
<p><em>2024-06-16</em></p>
<p>Welcome to your new home for product updates on <a href="/cloudflare-one/">Cloudflare One</a>.</p>
<p>Our <a href="/changelog/">new changelog</a> lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.</p>
<p>If you are looking for older product updates, refer to the following locations.</p>
<details class="nb-details" open><summary>Older product updates</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17707.md")</div></details>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/gateway/">Previous</a><span>Page 2 of 2</span></nav>
