<p><img src="/assets/upstream/images/email-security/email-retraction/o365/opening_img-o365-retraction.png" alt="Email workflow for retracting emails with Microsoft Office 365" /></p>
<p>In this tutorial you will learn how to set up email retraction for Microsoft Office 365.</p>
<h2 id="1-authorize-email-security-with-office-365-for-retraction"><ol>
<li>Authorize Email security with Office 365 for retraction</li>
</ol></h2>
<p>For message retraction to successfully execute, Email security needs to be authorized to make API calls into the Office 365 Graph API architecture. The account used to authorize Email security requires the <strong>Privileged role admin</strong> role.</p>
<p>When assigning user roles in the Office 365 console, you will find these roles in <strong>User permissions</strong> &gt; <strong>Roles configuration</strong> &gt; <strong>Identity admin roles</strong>.</p>
<h3 id="how-does-the-authorization-work">How does the authorization work?</h3>
<p>The authorization process grants Email security access to the Azure environment with the least applicable privileges required to function. The Enterprise Application that Email security registers (the Email security Synchronator) is not tied to any administrator account. Inside of the Azure Active Directory admin center you can review the permissions granted to the application in the Enterprise Application section.</p>
<p><img src="/assets/upstream/images/email-security/email-retraction/o365/area1-synchronator.png" alt="Permissions required for Email security to access Office 365" /></p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>, and select <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>Go to <strong>Email Configuration</strong> &gt; <strong>RETRACT SETTINGS</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/email-retraction/o365/step2-retract-settings.png" alt="Access the retract settings in Email security" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8544.md")
</aside>
<ol>
<li>You need to authorize Email security to execute retractions through the Graph API of Office 365. Make sure that the account that you will be using to authenticate has the appropriate administrative roles assigned. Select <strong>Authorize</strong> to start the process.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/email-retraction/o365/step3-authorize-o365.png" alt="Select Authorize to start the process of authorizing Email security to access Office 365" /></p>
<ol start="2">
<li>The Email security dashboard will redirect you to a Microsoft login page. Select or enter the appropriate account to initiate the authentication process.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/email-retraction/o365/step4-authorize-login.png" alt="Select an account or enter a new account to authorize Email security" /></p>
<ol start="3">
<li>Once authenticated, the system will show a dialog box with a list of the requested permissions. Select <strong>Accept</strong> to authorize the change.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/email-retraction/o365/step5-authorize.png" alt="Select Accept to authorize Email security in Office 365" /></p>
<ol start="4">
<li>Upon authorization, you will be automatically redirected to the Email security dashboard, with a notification that the authorization completed successfully. Select <strong>Dismiss</strong> to clear the notification.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/email-retraction/o365/step6-dismiss.png" alt="Select Dismiss to dismiss the success notification" /></p>
<h2 id="2-configure-auto-retraction-actions"><ol start="2">
<li>Configure auto-retraction actions</li>
</ol></h2>
<p>You can set up auto-retraction to automatically move messages matching certain <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8545.md")
</div> to specific folders within a user's mailbox.
<p>To set up automatic retraction:</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email Security (formerly Area 1) dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>On <strong>Email Configuration</strong>, go to <strong>Retract Settings</strong> &gt; <strong>Auto-Retract</strong>.</p>
</li>
<li>
<p>Select <strong>Edit</strong>.</p>
</li>
<li>
<p>For each disposition, choose which folder the message should be sent to:</p>
<ul>
<li><strong>No Action</strong>: Do not move the message.</li>
<li><strong>Junk Email</strong>: Sends the message to the junk or spam email folder.</li>
<li><strong>Trash</strong>: Sends the message to the trash or deleted items email folder.</li>
<li><strong>Soft Delete — user recoverable</strong> (Microsoft only): Sends the message to the user's <strong>Deleted Items</strong> folder. Messages can be recovered by the user.</li>
<li><strong>Hard Delete — admin recoverable</strong>: Completely deletes messages from a user's inbox. Office 365 messages cannot be recovered without using the eDiscovery feature or the Exchange admin center. Refer to <a href="#recover-hard-deleted-messages">Recover hard deleted messages</a> for more information.</li>
</ul>
</li>
<li>
<p>Select <strong>Update Auto-retract Settings</strong>.</p>
</li>
</ol>
<h3 id="post-delivery-retractions-for-new-threats">Post delivery retractions for new threats</h3>
<p>Email Security (formerly Area 1) is continuously gathering new information about <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8546.md")
</div> campaigns. Users might have email messages in their inboxes that were scanned by Email Security (formerly Area 1) but not retracted initially because, at the time of scan, these email messages had not been identified as a threat. To mitigate risk, Email Security (formerly Area 1) offers you tools to re-evaluate email messages at a fixed time interval based on knowledge Cloudflare may have acquired since initial delivery. Any email messages that fit this new threat knowledge will be retracted.
<p>You can enable two options:</p>
<ul>
<li><strong>Post Delivery Response</strong>:  Email Security (formerly Area 1) will continue to re-evaluate emails already delivered to your users' inboxes at a fixed time interval in search for phishing sites or campaigns not previously known to Cloudflare. If any email messages fitting these new criteria are found, Email Security (formerly Area 1) retracts them. Rescans occur at a five minute, 12 hour, and 24 hour intervals.</li>
<li><strong>Phish Submission Response</strong>: Email Security (formerly Area 1) will retract emails already delivered that are reported by your users as phishing, and are found to be malicious by Email Security (formerly Area 1). Retraction will occur according to your configuration.</li>
</ul>
<h2 id="3-configure-journaling"><ol start="3">
<li>Configure journaling</li>
</ol></h2>
<h3 id="1-configure-connector-for-delivery-to-email-security-formerly-area-1-if-required"><ol>
<li>Configure connector for delivery to Email security (formerly Area 1) (if required)</li>
</ol></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8543.md")
</aside>
<p>If your email architecture does not include an outbound gateway, you can skip this step and <a href="#2-configure-journal-rule">proceed to the next one</a>.</p>
<p>On the other hand, if your email architecture requires outbound messages to traverse your email gateway, you may want to consider configuring a connector to send the journal messages directly to Email security.</p>
<ol>
<li>Log in to the <a href="https://admin.exchange.microsoft.com">Exchange admin center</a>, and go to <strong>Mail flow</strong> &gt; <strong>Connectors</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/step1-connector.png" alt="Go to the connectors area" /></p>
<ol start="2">
<li>
<p>Select <strong>Add a connector</strong>.</p>
</li>
<li>
<p>Configure the new connector as follows:</p>
<ul>
<li><strong>Connection From</strong>: Office 365</li>
<li><strong>Connection to</strong>: Partner Organization</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/step3-configure-connector.png" alt="Configure the connector" /></p>
<ol start="4">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Configure the connector as follows:</p>
<ul>
<li><strong>Name</strong>: <code>Deliver journal directly to Area 1</code></li>
<li><strong>Description</strong>: <code>Deliver journal directly to Area 1</code></li>
<li><strong>Turn it on</strong>: Enabled.</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/step5-name-connector.png" alt="Name the connector and give it a description" /></p>
<ol start="6">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Configure the <strong>Use of connector</strong> setting as follows:</p>
<ul>
<li>Select <strong>Only when email messages are sent to these domains</strong>.</li>
<li>In the text field, enter <code>journaling.mxrecord.io</code> as the host address, and select <strong>+</strong> to add the domain.</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/step7-use-of-connector.png" alt="Configure use of connector" /></p>
<ol start="8">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Configure the <strong>Routing</strong> setting as follows:</p>
<ul>
<li>Select <strong>Route email through these smart hosts</strong>.</li>
<li>In the text field, enter <code>journaling.mxrecord.io</code> as the <a href="https://en.wikipedia.org/wiki/Smart_host">smart host</a> address, and select <strong>+</strong> to add the domain.</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/step9-routing.png" alt="Configure the routing setting" /></p>
<ol start="10">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>In <strong>Security restrictions</strong>, you need to keep the default TLS configuration. Review the following settings:</p>
<ul>
<li>Make sure the <strong>Always use Transport Layer Security (TLS) to secure the connection (recommended)</strong> checkbox is selected.</li>
<li>In <strong>Connect only if the recipients email server certificate matches this criteria</strong> select <strong>Issued by a trusted certificate authority (CA)</strong>.</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/step11-security.png" alt="Configure security restrictions" /></p>
<ol start="12">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>You need to validate the connector by using your tenant’s specific journaling address. To find this address, go to the <a href="https://horizon.area1security.com/support/service-addresses">Email security dashboard</a> &gt; <strong>Support</strong> &gt; <strong>Service Addresses page</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/step13-validate-email.png" alt="Validate the connector" /></p>
<ol start="14">
<li>
<p>Add the address and select <strong>Validate</strong>.</p>
</li>
<li>
<p>Once the validation completes, you should receive a <strong>Succeed</strong> status for all the tasks. Select <strong>Next</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/step15-validation-success.png" alt="Validation success if all goes well" /></p>
<ol start="16">
<li>Review the configuration and select <strong>Create connector</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/step16-review-connector.png" alt="Review your connector" /></p>
<p>Your connector is now active. You can find it in <strong>Exchange admin center</strong> &gt; <strong>Mail flow</strong> &gt; <strong>Connectors</strong>.</p>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/connector-active.png" alt="Connector active" /></p>
<h3 id="2-configure-journal-rule"><ol start="2">
<li>Configure journal rule</li>
</ol></h3>
<ol>
<li>
<p>Log in to the <a href="https://compliance.microsoft.com/homepage">Microsoft Purview compliance portal</a>.</p>
</li>
<li>
<p>Go to <strong>Data lifecycle management</strong> &gt; <strong>Exchange (legacy)</strong>.</p>
</li>
<li>
<p>Select <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>In <strong>Send undeliverable journal reports to</strong> enter the email address of a valid user account. Note that you cannot use a team or group address.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/step4-undeliverable.png" alt="Configure undeliverable emails" /></p>
<ol start="5">
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p>Still in the Exchange (legacy) screen, select <strong>Journal Rules</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/step6-journal-rules.png" alt="Select journal rules" /></p>
<ol start="7">
<li>
<p>Select <strong>New rule</strong> to configure a journaling rule, and configure it as follows:</p>
<ul>
<li><strong>Send journal reports to</strong>: This address is specific to each customer tenant, and can be found in your <a href="https://horizon.area1security.com/support/service-addresses">Email security dashboard</a>. For example, <code>&lt;customer_name&gt;@journaling.mxrecord.io</code>.</li>
<li><strong>Journal Rule Name</strong>: <code>Journal Messages to CloudflareArea 1</code></li>
<li><strong>Journal messages sent or received from</strong>: <em>Everyone</em></li>
<li><strong>Type of message to journal</strong>: <em>External messages only</em></li>
</ul>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Verify the information is correct, and select <strong>Submit</strong> &gt; <strong>Done</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/step9-verify-journal-rules.png" alt="Verify the journal rule information" /></p>
<p>Once saved, the rule is automatically active. However, it may take a few minutes for the configuration to propagate and start pushing messages to Cloudflare Email security. After it propagates, you can access the Cloudflare Email security dashboard to check the number of messages processed. This number will grow as journaled messages are sent to Cloudflare Email security from your Exchange server.</p>
<h3 id="3-compliance"><ol start="3">
<li>Compliance</li>
</ol></h3>
<h4 id="create-office-365-distribution-lists">Create Office 365 distribution lists</h4>
<p>For compliance purposes, you might be required to process emails in certain geographic regions such as India or the EU. If that is your case, you should <a href="https://learn.microsoft.com/en-us/microsoft-365/admin/setup/create-distribution-lists?view=o365-worldwide#create-a-distribution-group-list">create Office 365 distribution lists</a> for each geographic region where you need to process your emails, before configuring your journal rule.</p>
<h4 id="configure-journal-rule">Configure journal rule</h4>
<p>After creating the distribution lists based on regions for your users, configure your journal rule:</p>
<ol>
<li>
<p>Log in to the <a href="https://compliance.microsoft.com/homepage">Microsoft Purview compliance portal</a>.</p>
</li>
<li>
<p>Go to <strong>Data lifecycle management</strong> &gt; <strong>Exchange (legacy)</strong>.</p>
</li>
<li>
<p>Select <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>In <strong>Send undeliverable journal reports to</strong> enter the email address of a valid user account. Note that you cannot use a team or group address.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/step4-undeliverable.png" alt="Configure undeliverable emails" /></p>
<ol start="5">
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p>Still in the Exchange (legacy) screen, select <strong>Journal Rules</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/step6-journal-rules.png" alt="Select journal rules" /></p>
<ol start="7">
<li>
<p>Select <strong>New rule</strong> to configure a journaling rule, and configure it as follows:</p>
<ul>
<li><strong>Send journal reports to</strong>: This address is specific to each customer tenant, and can be found in your <a href="https://horizon.area1security.com/support/service-addresses">Email security dashboard</a>. If you need to process emails in certain geographic regions, refer to the <a href="#geographic-locations">Geographic locations</a> table for more information on what address you should use.</li>
<li><strong>Journal Rule Name</strong>: <code>Journal Messages to CloudflareArea 1</code></li>
<li><strong>Journal messages sent or received from</strong>: <em>A specific user or group</em> and select the user group you <a href="#3-compliance">created above</a>.</li>
<li><strong>Type of message to journal</strong>: <em>External messages only</em></li>
</ul>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Verify the information is correct, and select <strong>Submit</strong> &gt; <strong>Done</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/step9-verify-journal-rules.png" alt="Verify the journal rule information" /></p>
<p>Once saved, the rule is automatically active. However, it may take a few minutes for the configuration to propagate and start pushing messages to Cloudflare Email security. After it propagates, you can access the Cloudflare Email security dashboard to check the number of messages processed. This number will grow as journaled messages are sent to Cloudflare Email security from your Exchange server.</p>
<h2 id="4-manual-message-retraction"><ol start="4">
<li>Manual message retraction</li>
</ol></h2>
<p>When retraction is enabled, you can manually retract messages that were not automatically retracted.</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email Security (formerly Area 1) dashboard</a>.</p>
</li>
<li>
<p>Select the search bar and enter the search parameters to find the emails you are looking for.</p>
</li>
<li>
<p>To retract a single message, select <strong>Retract</strong>. To retract multiple messages, first select the checkboxes on the messages you want to retract. Then, select <strong>Retract</strong>.</p>
</li>
<li>
<p>Choose where you want to retract the message to, and select <strong>Retract message</strong>.</p>
</li>
</ol>
<div class="medium-img">
<p><img src="/assets/upstream/images/email-security/email-retraction/gmail/step5-retract-destination.png" alt="Choose your retraction destination" /></p>
</div>
<ol start="5">
<li>If the retraction was successful, there will be positive confirmation on Email Security (formerly Area 1) dashboard.</li>
</ol>
<h2 id="recover-hard-deleted-messages">Recover hard deleted messages</h2>
<p>Office 365 has two ways for recovering hard deleted email messages:</p>
<ul>
<li><strong><a href="https://learn.microsoft.com/en-us/purview/ediscovery?view=o365-worldwide">eDiscovery</a></strong></li>
<li><strong><a href="https://learn.microsoft.com/en-us/exchange/recipients-in-exchange-online/manage-user-mailboxes/recover-deleted-messages">Exchange admin center</a></strong></li>
</ul>
<p>Refer to Microsoft's documentation to learn more about how to use these tools to recover deleted email messages.</p>
<h2 id="geographic-locations">Geographic locations</h2>
<p>Select from the following BCC addresses to process email in the correct geographic location.</p>
<table>
<thead>
<tr>
<th>Host</th>
<th>Location</th>
<th>Note</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mxrecord.io</code></td>
<td>US</td>
<td>Best option to ensure all email traffic processing happens US data centers.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-eu-primary.mxrecord.io</code></td>
<td>EU</td>
<td>Best option to ensure all email traffic processing happens in Germany, with backup to US data centers.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-eu1.mxrecord.io</code></td>
<td>EU</td>
<td>Best option to ensure all email traffic processing happens within the EU without backup to US data centers.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-bom.mxrecord.mx</code></td>
<td>India</td>
<td>Best option to ensure all email traffic processing happens within India.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-india-primary.mxrecord.mx</code></td>
<td>India</td>
<td>Same as <code>mailstream-bom.mxrecord.mx</code>, with backup to US data centers.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-asia.mxrecord.mx</code></td>
<td>India</td>
<td>Best option to ensure all email traffic processing happens in India, with Australia data centers as backup.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-syd.area1.cloudflare.net</code></td>
<td>Australia / New Zealand</td>
<td>Best option to ensure all email traffic processing happens within Australia.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-australia.area1.cloudflare.net</code></td>
<td>Australia / New Zealand</td>
<td>Best option to ensure all email traffic processing happens in Australia, with India and US data centers as backup.</td>
</tr>
</tbody>
</table>
