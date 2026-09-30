<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/1046.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="access-to-area-1">Access to Area 1</h3>
@markup("md", "content/.markup/bodies/1045.md")
</aside>
<p>Email security Channel and Alliance partners have the option to set up accounts for themselves and their customers.</p>
<h2 id="create-accounts">Create accounts</h2>
<p>Start by creating parent and child accounts.</p>
<h3 id="create-a-parent-account">Create a parent account</h3>
<p>Parent accounts are treated as containers with no services provisioned. User accounts created at the parent level will allow them to access any child account.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1044.md")
</aside>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>In <strong>Delegated Accounts</strong> &gt; <strong>Accounts</strong>, select <strong>Create new customer</strong>.</li>
<li>Enter their information, and make sure you select <em>Parent</em> in <strong>Account Type</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Your newly created account should show up in the list. If not, refresh the page.</p>
<h3 id="create-a-child-account">Create a child account</h3>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>In <strong>Delegated Accounts</strong> &gt; <strong>Accounts</strong>, select the parent account where you want to create a child account.</li>
<li>Select <strong>Create New customer</strong>.</li>
<li>Enter their information, and make sure you select <em>Advantage</em> in <strong>Account Type</strong>.</li>
<li>Scroll down to the <strong>Email Traffic Related Information</strong> section, and enter the information related to your email provider. The number to enter in <strong>Loopback Hops</strong> will depend on your email configuration and where Email security is in the chain of events. Refer to <a href="/email-security/deployment/inline/">Inline deployment</a> and <a href="/email-security/deployment/api/">API deployment</a> for more information.</li>
<li>For <strong>Daily Email Volume</strong> and <strong>Number of Email Users</strong> make sure you enter the appropriate values for your organization.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="create-users-and-assign-permissions">Create users and assign permissions</h2>
<p>You can create users at both the parent and child account level. Users created at parent level will have access to all its child accounts. Users created at child level will only have access to the assigned child account.</p>
<p>Child accounts can <a href="/email-security/account-setup/manage-parent-permissions/">limit or disable</a> the level of access allowed from their parent account.</p>
<p>If you modify the Delegated Access controls, make sure you create an administrator account in the child first.</p>
<p>To create an account at parent level or child level:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email Security (formerly Area 1) dashboard</a> with a parent account or child account depending on what you are trying to create.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>Go to <strong>Users and Actions</strong>.</li>
<li>Select <strong>Add User</strong>.</li>
<li>Enter their information, as well as their <a href="/email-security/account-setup/permissions/"><strong>Permission</strong> level</a>.</li>
<li>Select <strong>Send Invitation</strong>.</li>
</ol>
<h2 id="escalation-contacts">Escalation contacts</h2>
<p>You should add escalation contacts so Email security can send notifications regarding detection events and critical service related issues. Email security highly recommends that these contacts have both phone and email contacts.</p>
<p>Refer to <a href="/email-security/account-setup/escalation-contacts/">Escalation contacts</a> for more information.</p>
<h2 id="status-alerts">Status alerts</h2>
<p>Subscribe to incident status alerts <a href="https://status.area1security.com/">from Email security</a>.</p>
<h2 id="domains-setup-inline-api">Domains setup (inline/API)</h2>
<p>Refer to the <a href="/email-security/deployment/">setup options</a> for Email security to learn about the best way of deploying Email security in your organization. You can choose between two main setup architectures:</p>
<ul>
<li>Inline deployment</li>
<li>API deployment</li>
</ul>
<p>With an <a href="/email-security/deployment/inline/">inline deployment</a>, Email security evaluates email messages before they reach a user’s inbox. When you choose an <a href="/email-security/deployment/api/">API deployment</a>, email messages only reach Email security after they have already reached a user’s inbox.</p>
<h2 id="classification-actions">Classification actions</h2>
<p>Email security recommends that you quarantine <code>MALICIOUS</code> and <code>SPAM</code> <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/1047.md")
</div>. You can configure this directly in [Office 365](/email-security/deployment/inline/setup/office-365-area1-mx/) and [Gsuite](/email-security/deployment/inline/setup/gsuite-area1-mx/), as well as [Email security](/email-security/email-configuration/domains-and-routing/domains/).
<h2 id="message-retraction">Message retraction</h2>
<p>You can configure message retraction to take post-delivery actions against suspicious email messages. You can retract messages manually or automatically. Refer to <a href="/email-security/email-configuration/retract-settings/">Retract settings</a> for more information.</p>
<h2 id="tls-enforcement-for-domains">TLS enforcement for domains</h2>
<p>To add additional TLS requirements for emails coming from certain domains, you can enforce higher levels of SSL/TLS inspection. Refer to <a href="/email-security/email-configuration/domains-and-routing/partner-domains-tls/">Partner Domains TLS</a> for more information.</p>
<h2 id="reports">Reports</h2>
<p>You can subscribe to <a href="https://horizon.area1security.com/settings/subscriptions/email-subscriptions">daily and weekly email reports</a>, as well as <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/1048.md")
</div>. For SIEM events, you will need to [configure your SIEM tool](/email-security/reporting/siem-integration/) into Email security first.
<h2 id="whitelisting-and-blocklisting-senders">Whitelisting and blocklisting senders</h2>
<p>If you need to whitelist of blocklist senders, refer to <a href="/email-security/email-configuration/lists/">Allow and block lists</a>.</p>
<h2 id="submitting-false-positives-and-false-negatives">Submitting false positives and false negatives</h2>
<p>There are several ways of dealing with missed <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/1049.md")
</div> or messages flagged as such that are not. Refer to [Phish submissions](/email-security/email-configuration/phish-submissions/) to learn more.
<h2 id="best-practices">Best practices</h2>
<p>Refer to the following pages to learn more:</p>
<ol>
<li><a href="/email-security/email-configuration/enhanced-detections/business-email-compromise/">Business Email compromise (BEC)</a></li>
<li><a href="/email-security/email-configuration/email-policies/text-addons/">Text add-ons</a></li>
<li><a href="/email-security/reporting/">Search and reports</a></li>
</ol>
