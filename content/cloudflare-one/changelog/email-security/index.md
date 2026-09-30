<h2 id="2026-08-17">2026-08-17</h2>

<strong>Post-quantum key exchange for MX deployments</strong>

<p>Cloudflare Email Security now supports post-quantum hybrid key exchange with X25519MLKEM768 on the SMTP connections we make to receive and deliver mail. Deploying Email Security in front of a provider that supports post-quantum hybrid key agreement (like Google Workspace) will create a TLS 1.3 connection using post-quantum key agreement.</p>
<p>Inbound MX connections and outbound delivery connections now negotiate the <a href="/ssl/post-quantum-cryptography/#hybrid-key-agreement">X25519MLKEM768</a> hybrid key agreement when the peer supports it, protecting SMTP traffic against <a href="https://blog.cloudflare.com/pq-2024/">harvest-now, decrypt-later</a> attacks.</p>
<p>Support is backwards compatible and enabled automatically for all customers. Senders and receivers that do not yet advertise post-quantum key agreement continue to connect with classical key exchange.</p>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2026-08-12">2026-08-12</h2>

<strong>Block emails by content with blocked content rules</strong>

<p>Cloudflare Email security now lets administrators write their own content-based blocking rules. A new <strong>Blocked content</strong> area under <strong>Policies &amp; rules</strong> lets you define a plaintext string or a regular expression, choose whether to scan the message subject, body, or both, and automatically block any message that matches.</p>
<ul>
<li>Create rules using either <strong>plaintext</strong> matches or <strong>regular expressions</strong> — useful for blocking targeted phishing campaigns, known-bad phrases, or content patterns unique to your organization.</li>
<li>Choose the <strong>search location</strong> for each rule: <strong>subject</strong>, <strong>body</strong>, or <strong>subject and body</strong>.</li>
<li>Use the built-in <strong>regular expression checker</strong> to validate your pattern against sample text before saving, so you can confirm the rule matches what you expect and avoid false positives.</li>
<li>Matching messages are marked with a malicious <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/">disposition</a> and prevented from reaching users' inboxes.</li>
</ul>
<p>Blocked content rules currently only support the block action.</p>
<p>This feature is available for the following Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/email-security/settings/detection-settings/blocked-content/">Blocked content</a>.</p>


<h2 id="2026-05-07">2026-05-07</h2>

<strong>Cloudy Summaries in PhishNet O365</strong>

<p>PhishNet users can now access <strong>Cloudy summaries</strong> directly within the email investigation experience. When reviewing a message in PhishNet, users will see an AI-generated summary that provides additional context and key details about the email.</p>
<p>These summaries help users quickly understand the nature of a message without needing to manually parse through headers, body content, and detection signals. Cloudy surfaces the most relevant information so users can make faster, more informed decisions about suspicious emails.</p>
<p><strong>These summaries are not trained on customer data.</strong> They are generated using the outputs of our existing detection models and analysis systems.</p>
<p>This feature is available for PhishNet with Office 365. Support for Gmail will be available by the end of the quarter.</p>


<h2 id="2026-04-07">2026-04-07</h2>

<strong>User Submission Triage Status Tracking</strong>

<p>Cloudflare Email security now supports <strong>Triage Status Tracking for User Submissions</strong>. This enhancement gives SOC teams a streamlined way to track, manage, and prioritize user-submitted emails directly within the Cloudflare One dashboard.</p>
<ul>
<li>The User Submissions table now includes a <strong>Status</strong> column with three states: <strong>Unreviewed</strong> (new submissions awaiting triage), <strong>Reviewed</strong> (submissions assessed by the SOC team), and <strong>Escalated</strong> (submissions escalated to team submissions for further investigation). Analysts can quickly update statuses and filter the table to focus on what needs attention.</li>
<li>SOC teams can now organize their triage workflows, avoid duplicate reviews, and make sure critical threats get escalated for deeper investigation—bringing order to the chaos of high-volume submission management.</li>
</ul>
<p>Triage Status Tracking is <strong>automatically available</strong> for all Email security customers using the user submissions feature. No additional configuration is required; customers just need to make sure user submissions are being sent to their user submission aliases.</p>
<p>This applies to all Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2026-04-06">2026-04-06</h2>

<strong>DANE Support for MX Deployments</strong>

<p>Cloudflare Email Security now supports DANE (DNS-based Authentication of Named Entities) for MX deployments. This enhancement strengthens email transport security by enabling DNSSEC-backed certificate verification for our regional MX records.</p>
<ul>
<li>Regional MX hostnames now publish DANE TLSA records backed by DNSSEC, enabling DANE-capable SMTP senders to cryptographically validate certificate identities before establishing TLS connections—moving beyond opportunistic encryption to verified encrypted delivery.</li>
<li>DANE support is automatically available for all customers using regional MX deployments. No additional configuration is required; DANE-capable mail infrastructure will automatically validate MX certificates using the published records.</li>
</ul>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2026-03-16">2026-03-16</h2>

<strong>Unlimited result paging in Investigations</strong>

<p>Investigations now support unlimited result paging in both the dashboard and the API, removing the previous 1,000-record cap. Security teams can page through complete result sets when searching across large mail volumes, giving SOC analysts and automated workflows deeper visibility for forensics and threat hunting.</p>
<p>In the dashboard, infinite paging is now supported in the Investigations view. The 1,000-record ceiling has been removed, so you can navigate through the full result set directly in the UI. The <a href="/api/resources/email_security/subresources/investigate/methods/list">Investigations API</a> now returns up to 10,000 records per page (up from 1,000), with no cap on total result volume across pages.</p>
<p>For high-volume use cases, we recommend:</p>
<ul>
<li><strong><a href="/cloudflare-one/insights/logs/logpush/email-security-logs/">Logpush</a> to a SIEM</strong> for full-fidelity datasets and long-term retention.</li>
<li><strong>SOAR playbooks</strong> against the async bulk action API for large-scale remediation. Bulk actions initiated from the dashboard remain capped at 1,000 messages per action.</li>
<li><strong>The Investigations API</strong> for report exports larger than 1,000 results, which is the dashboard download cap.</li>
</ul>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2026-02-02">2026-02-02</h2>

<strong>Improved Accessibility and Search for Monitoring</strong>

<p>We have updated the Monitoring page to provide a more streamlined and insightful experience for administrators, improving both data visualization and dashboard accessibility.</p>
<ul>
<li><strong>Enhanced Visual Layout</strong>: Optimized contrast and the introduction of stacked bar charts for clearer data visualization and trend analysis.
<img src="/assets/upstream/images/changelog/email-security/monitoring-bar-charts.png" alt="visual-example" /></li>
<li><strong>Improved Accessibility &amp; Usability</strong>:
<ul>
<li><strong>Widget Search</strong>: Added search functionality to multiple widgets, including Policies, Submitters, and Impersonation.</li>
<li><strong>Actionable UI</strong>: All available actions are now accessible via dedicated buttons.</li>
<li><strong>State Indicators</strong>: Improved UI states to clearly communicate loading, empty datasets, and error conditions.
<img src="/assets/upstream/images/changelog/email-security/monitoring-buttons.png" alt="buttons-example" /></li>
</ul>
</li>
<li><strong>Granular Data Breakdowns</strong>: New views for dispositions by month, malicious email details, link actions, and impersonations.
<img src="/assets/upstream/images/changelog/email-security/monitoring-monthly-dispositions.png" alt="monthly-example" /></li>
</ul>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2026-01-12">2026-01-12</h2>

<strong>Enhanced visibility for post-delivery actions</strong>

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


<h2 id="2025-12-04">2025-12-04</h2>

<strong>Reclassifications to Submissions</strong>

<p>We have updated the terminology “Reclassify” and “Reclassifications” to “Submit” and “Submissions” respectively. This update more accurately reflects the outcome of providing these items to Cloudflare.</p>
<p>Submissions are leveraged to tune future variants of campaigns. To respect data sanctity, providing a submission does not change the original disposition of the emails submitted.</p>
<p><img src="/assets/upstream/images/changelog/email-security/reclassification-submission.png" alt="nav_example" /></p>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2025-11-18">2025-11-18</h2>

<strong>Adjustment to Final Disposition Column</strong>

<h4 id="2025-11-18-temporary-adjustment-to-final-disposition-column-adjustment-to-final-disposition-column">Adjustment to Final Disposition column</h4>
<h4 id="2025-11-18-temporary-adjustment-to-final-disposition-column-the-final-disposition-column-in-submissions-team-submissions-tab-is-changing-for-non-phishguard-customers">The <strong>Final Disposition</strong> column in <strong>Submissions</strong> &gt; <strong>Team Submissions</strong> tab is changing for non-Phishguard customers.</h4>
<h4 id="2025-11-18-temporary-adjustment-to-final-disposition-column-what-s-changing">What's Changing</h4>
<ul>
<li>Column will be called <strong>Status</strong> instead of <strong>Final Disposition</strong></li>
<li>Column status values will now be: <strong>Submitted</strong>, <strong>Accepted</strong> or <strong>Rejected</strong>.</li>
</ul>
<h4 id="2025-11-18-temporary-adjustment-to-final-disposition-column-next-steps">Next Steps</h4>
<p>We will listen carefully to your feedback and continue to find comprehensive ways to communicate updates on your submissions. Your submissions will continue to be addressed at an even greater rate than before, fuelling faster and more accurate email security improvement.</p>


<h2 id="2025-10-18">2025-10-18</h2>

<strong>On-Demand Security Report</strong>

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


<h2 id="2025-09-24">2025-09-24</h2>

<strong>Invalid Submissions Feedback</strong>

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


<h2 id="2025-09-12">2025-09-12</h2>

<strong>Regional Email Processing for Germany, India, or Australia</strong>

<p>We’re excited to announce that Email security customers can now choose their preferred mail processing location directly from the UI when onboarding a domain. This feature is available for the following onboarding methods: <strong>MX</strong>, <strong>BCC</strong>, and <strong>Journaling</strong>.</p>
<h4 id="2025-09-11-regional-email-processing-gia-what-s-new">What’s new</h4>
<p>Customers can now select where their email is processed. The following regions are supported:</p>
<ul>
<li><strong>Germany</strong></li>
<li><strong>India</strong></li>
<li><strong>Australia</strong></li>
</ul>
<p>Global processing remains the default option, providing flexibility to meet both compliance requirements or operational preferences.</p>
<h4 id="2025-09-11-regional-email-processing-gia-how-to-use-it">How to use it</h4>
<p>When onboarding a domain with MX, BCC, or Journaling:</p>
<ol>
<li>Select the desired processing location (Germany, India, or Australia).</li>
<li>The UI will display updated processing addresses specific to that region.</li>
<li>For MX onboarding, if your domain is managed by Cloudflare, you can automatically update MX records directly from the UI.</li>
</ol>
<h4 id="2025-09-11-regional-email-processing-gia-availability">Availability</h4>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
<h4 id="2025-09-11-regional-email-processing-gia-what-s-next">What’s next</h4>
<p>We’re expanding the list of processing locations to match our <a href="/data-localization/">Data Localization Suite (DLS)</a> footprint, giving customers the broadest set of regional options in the market without the complexity of self-hosting.</p>


<h2 id="2025-09-02">2025-09-02</h2>

<strong>Updated Email security roles</strong>

<p>To provide more granular controls, we refined the <a href="/cloudflare-one/roles-permissions/#email-security-roles">existing roles</a> for Email security and launched a new Email security role as well.</p>
<p>All Email security roles no longer have read or write access to any of the other Zero Trust products:</p>
<ul>
<li><strong>Email Configuration Admin</strong></li>
<li><strong>Email Integration Admin</strong></li>
<li><strong>Email security Read Only</strong></li>
<li><strong>Email security Analyst</strong></li>
<li><strong>Email security Policy Admin</strong></li>
<li><strong>Email security Reporting</strong></li>
</ul>
<p>To configure <a href="/cloudflare-one/email-security/outbound-dlp/">Data Loss Prevention (DLP)</a> or <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/#set-up-clientless-web-isolation">Remote Browser Isolation (RBI)</a>, you now need to be an admin for the Zero Trust dashboard with the <strong>Cloudflare Zero Trust</strong> role.</p>
<p>Also through customer feedback, we have created a new additive role to allow <strong>Email security Analyst</strong> to create, edit, and delete Email security policies, without needing to provide access via the <strong>Email Configuration Admin</strong> role. This role is called <strong>Email security Policy Admin</strong>, which can read all settings, but has write access to <a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/">allow policies</a>, <a href="/cloudflare-one/email-security/settings/detection-settings/trusted-domains/">trusted domains</a>, and <a href="/cloudflare-one/email-security/settings/detection-settings/blocked-senders/">blocked senders</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2025-08-08">2025-08-08</h2>

<strong>Expanded Email Link Isolation</strong>

<p>When you deploy MX or Inline, not only can you apply email link isolation to suspicious links in all emails (including benign), you can now also apply email link isolation to all links of a specified disposition. This provides more flexibility in controlling user actions within emails.</p>
<p>For example, you may want to deliver suspicious messages but isolate the links found within them so that users who choose to interact with the links will not accidentally expose your organization to threats. This means your end users are more secure than ever before.</p>
<p><img src="/assets/upstream/images/changelog/email-security/expanded-link-actions.jpg" alt="Expanded Email Link Isolation Configuration" /></p>
<p>To isolate all links within a message based on the disposition, select <strong>Settings</strong> &gt; <strong>Link Actions</strong> &gt; <strong>View</strong> and select <strong>Configure</strong>. As with other other links you isolate, an interstitial will be provided to warn users that this site has been isolated and the link will be recrawled live to evaluate if there are any changes in our threat intel. Learn more about this feature on <a href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/">Configure link actions</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2025-05-16">2025-05-16</h2>

<strong>Open email attachments with Browser Isolation</strong>

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


<h2 id="2025-05-09">2025-05-09</h2>

<strong>Open email links with Browser Isolation</strong>

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


<h2 id="2025-04-02">2025-04-02</h2>

<strong>CASB and Email security</strong>

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


<h2 id="2025-03-02">2025-03-02</h2>

<strong>Use Logpush for Email security detections</strong>

<p>You can now send detection logs to an endpoint of your choice with Cloudflare Logpush.</p>
<p>Filter logs matching specific criteria you have set and select from over 25 fields you want to send. When creating a new Logpush job, remember to select <strong>Email security alerts</strong> as the dataset.</p>
<p><img src="/assets/upstream/images/changelog/email-security/Logpush-Detections.png" alt="logpush-detections" /></p>
<p>For more information, refer to <a href="/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-detection-logs">Enable detection logs</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2025-02-28">2025-02-28</h2>

<strong>Check status of Email security or Area 1</strong>

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


<h2 id="2025-02-26">2025-02-26</h2>

<strong>Use DLP Assist for M365</strong>

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


<h2 id="2025-02-08">2025-02-08</h2>

<strong>Open email links with Security Center</strong>

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


<h2 id="2024-12-20">2024-12-20</h2>

<strong>Escalate user submissions</strong>

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


<h2 id="2024-12-19-1">2024-12-19</h2>

<strong>Increased transparency for phishing email submissions</strong>

<p>You now have more transparency about team and user submissions for phishing emails through a <strong>Reclassification</strong> tab in the Zero Trust dashboard.</p>
<p>Reclassifications happen when users or admins <a href="/cloudflare-one/email-security/settings/phish-submissions/">submit a phish</a> to Email security. Cloudflare reviews and - in some cases - reclassifies these emails based on improvements to our machine learning models.</p>
<p>This new tab increases your visibility into this process, allowing you to view what submissions you have made and what the outcomes of those submissions are.</p>
<p><img src="/assets/upstream/images/changelog/email-security/reclassifications-tab.png" alt="Use the Reclassification area to review submitted phishing emails" /></p>


<h2 id="2024-11-08">2024-11-08</h2>

<strong>Use Logpush for Email security user actions</strong>

<p>You can now send user action logs for Email security to an endpoint of your choice with Cloudflare Logpush.</p>
<p>Filter logs matching specific criteria you have set or select from multiple fields you want to send. For all users, we will log the date and time, user ID, IP address, details about the message they accessed, and what actions they took.</p>
<p>When creating a new Logpush job, remember to select <strong>Audit logs</strong> as the dataset and filter by:</p>
<ul>
<li><strong>Field</strong>: <code>&quot;ResourceType&quot;</code></li>
<li><strong>Operator</strong>: <code>&quot;starts with&quot;</code></li>
<li><strong>Value</strong>: <code>&quot;email_security&quot;</code>.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/email-security/Logpush-User-Actions.png" alt="Logpush-user-actions" /></p>
<p>For more information, refer to <a href="/cloudflare-one/insights/logs/logpush/email-security-logs/#enable-user-action-logs">Enable user action logs</a>.</p>
<p>This feature is available across all Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="2024-12-19">2024-12-19</h2>
<p><strong>Email security expanded folder scanning</strong></p>
<p>Microsoft 365 customers can now choose to scan all folders or just the inbox when deploying via the Graph API.</p>
<h2 id="2024-08-06">2024-08-06</h2>
<p><strong>Email security is live</strong></p>
<p>Email security is now live under Zero Trust.</p>
<h2 id="2024-08-06-1">2024-08-06</h2>
<p><strong>Microsoft Graph API deployment.</strong></p>
<p>Customers using Microsoft Office 365 can set up Email security via Microsoft Graph API.</p>


