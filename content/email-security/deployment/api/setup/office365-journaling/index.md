<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8512.md")
</aside>
<p>For customers using Microsoft Office 365, setting up Email security via journaling is quick and easy. The following email flow shows how this works:</p>
<p><img src="/assets/upstream/images/email-security/deployment/api-setup/journaling/office365-journaling-flow.png" alt="Email flow when setting up a phishing assessment risk for Office 365 with Email security." /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8511.md")
</aside>
<h2 id="journaling">Journaling</h2>
<h3 id="1-configure-connector-for-delivery-to-email-security-formerly-area-1-if-required"><ol>
<li>Configure connector for delivery to Email security (formerly Area 1) (if required)</li>
</ol></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8510.md")
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
