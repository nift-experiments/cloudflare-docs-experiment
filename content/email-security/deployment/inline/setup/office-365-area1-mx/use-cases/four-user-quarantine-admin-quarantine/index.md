<p>In this tutorial, you will learn to deliver <code>SPAM</code> and <code>SPOOF</code> messages to the user managed quarantine, and <code>MALICIOUS</code> messages to the administrative quarantine (this requires an administrator to release the emails).</p>
<h2 id="configure-domains">Configure domains</h2>
<p>You first need to configure the domains you are onboarding on the Email Security (formerly Area 1) dashboard. To configure your domains:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email Security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>Go to <strong>Email configuration</strong> &gt; <strong>Domains &amp; Routing</strong> &gt; <strong>Domains</strong>.</li>
<li>Make sure each domain you are onboarding has been added.</li>
<li>For each domain you are configuring, select <strong>...</strong> &gt; <strong>Edit</strong>, and set the following options:
<ul>
<li><strong>Domain</strong> - <code>&lt;YOUR_DOMAIN&gt;</code>.</li>
<li><strong>Configured as</strong> - <code>MX Records</code>.</li>
<li><strong>Forwarding to</strong> - This should match the expected MX record for each domain in your <a href="https://admin.microsoft.com/#/Domains/">Office 365 account</a>.</li>
<li><strong>IP Restrictions</strong> - Leave this field empty.</li>
<li><strong>Outbound TLS</strong> - <code>Forward all messages over TLS</code>.</li>
<li><strong>Quarantine Policy</strong> - Do not check any dispositions.</li>
</ul>
</li>
</ol>
<h2 id="create-quarantine-policies">Create quarantine policies</h2>
<p>To create quarantine policies:</p>
<ol>
<li>
<p>Open the <a href="https://security.microsoft.com/">Microsoft 365 Defender console</a>.</p>
</li>
<li>
<p>Go to <strong>Email &amp; collaboration</strong> &gt; <strong>Policies &amp; rules</strong>.</p>
</li>
<li>
<p>Select <strong>Threat policies</strong>.</p>
</li>
<li>
<p>Under <strong>Rules</strong>, select <strong>Quarantine policies</strong>.</p>
</li>
<li>
<p>Select <strong>Add custom policy</strong>.</p>
</li>
<li>
<p>Set the <strong>Policy name</strong> to <code>UserNotifyUserRelease</code>.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>In <strong>Recipient message access</strong>, select <strong>Set specific access (Advanced)</strong>, and then:</p>
<ul>
<li>In <strong>Select release action preference</strong>, choose <em>Allow recipients to release a message from quarantine</em>.</li>
<li>In <strong>Select additional actions recipients can take on quarantined messages</strong>, select the <strong>Delete</strong> and <strong>Preview</strong> checkboxes.</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/email-security/static/flexible-partial-images/o365-area1-mx/step8-allow-message-release.png" alt="Configure the Recipient message access as stated in the step above" /></p>
<ol start="9">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>In <strong>Quarantine notification</strong>, select <strong>Enable</strong>.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Review your settings and select <strong>Submit</strong>.</p>
</li>
<li>
<p>Select <strong>Done</strong>.</p>
</li>
<li>
<p>Select <strong>Add custom policy</strong>.</p>
</li>
<li>
<p>Set the <strong>Policy name</strong> to <code>UserNotifyAdminRelease</code>.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>In <strong>Recipient message access</strong>, select <strong>Set specific access (Advanced)</strong>, and then:</p>
<ul>
<li>In <strong>Select release action preference</strong>, from the drop-down menu, choose <em>Allow recipients to request a message to be released from quarantine</em>.</li>
<li>In <strong>Select additional actions recipients can take on quarantined messages</strong>, select the <strong>Delete</strong> and <strong>Preview</strong> checkboxes.</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/email-security/static/flexible-partial-images/o365-area1-mx/step8-request-message-release.png" alt="Configure the Recipient message access as stated in the step above" /></p>
<ol start="18">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>In <strong>Quarantine notification</strong>, select <strong>Enable</strong>.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Review your settings and select <strong>Submit</strong>.</p>
</li>
<li>
<p>Select <strong>Done</strong>.</p>
</li>
</ol>
<h2 id="configure-quarantine-notifications">Configure quarantine notifications</h2>
<p>To configure quarantine notifications:</p>
<ol>
<li>
<p>Open the <a href="https://security.microsoft.com/">Microsoft 365 Defender console</a>.</p>
</li>
<li>
<p>Go to <strong>Email &amp; collaboration</strong> &gt; <strong>Policies &amp; rules</strong>.</p>
</li>
<li>
<p>Select <strong>Threat policies</strong>.</p>
</li>
<li>
<p>Under <strong>Rules</strong>, select <strong>Quarantine policies</strong>.</p>
</li>
<li>
<p>Select <strong>Global settings</strong>.</p>
</li>
<li>
<p>Scroll to the bottom and set the desired frequency in <strong>Send end-user spam notifications every (days)</strong>. This value can only be incremented in days.</p>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/email-security/static/flexible-partial-images/o365-area1-mx/step6-spam-notifications.png" alt="Configure the desired spam notification frequency" /></p>
</div>
<ol start="7">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="configure-anti-spam-policies">Configure anti-spam policies</h2>
<p>To configure anti-spam policies:</p>
<ol>
<li>
<p>Open the <a href="https://security.microsoft.com/">Microsoft 365 Defender console</a></p>
</li>
<li>
<p>Go to <strong>Email &amp; collaboration</strong> &gt; <strong>Policies &amp; rules</strong>.</p>
</li>
<li>
<p>Select <strong>Threat policies</strong>.</p>
</li>
<li>
<p>Under <strong>Policies</strong>, select <strong>Anti-spam</strong>.</p>
</li>
<li>
<p>Select the <strong>Anti-spam inbound policy (Default)</strong> text (not the checkbox).</p>
</li>
<li>
<p>In the <strong>Actions</strong> section, scroll down and select <strong>Edit actions</strong>.</p>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/email-security/static/flexible-partial-images/o365-area1-mx/step6-edit-actions.png" alt="Go to Actions and find Edit actions" /></p>
</div>
<ol start="7">
<li>Set the following conditions and actions (you might need to scroll up or down to find them):
<ul>
<li><strong>Spam</strong>: <em>Quarantine message</em>.
<ul>
<li><strong>Select quarantine policy</strong>: <em>UserNotifyUserRelease</em>.</li>
</ul>
</li>
<li><strong>High confidence spam</strong>: <em>Quarantine message</em>.
<ul>
<li><strong>Select quarantine policy</strong>: <em>UserNotifyAdminRelease</em>.</li>
</ul>
</li>
<li><strong>Phishing</strong>: <em>Quarantine message</em>.
<ul>
<li><strong>Select quarantine policy</strong>: <em>UserNotifyAdminRelease</em>.</li>
</ul>
</li>
<li><strong>High confidence phishing</strong>: <em>Quarantine message</em>.
<ul>
<li><strong>Select quarantine policy</strong>: <em>UserNotifyAdminRelease</em>.</li>
</ul>
</li>
<li><strong>Retain spam in quarantine for this many days</strong>: Default is 15 days. Email security recommends 15-30 days.</li>
</ul>
</li>
</ol>
<div class="large-img">
<p><img src="/assets/upstream/email-security/static/flexible-partial-images/o365-area1-mx/step7-quarantine-message-case4.png" alt="Select the spam actions in the above step" /></p>
</div>
<ol start="8">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="create-transport-rules">Create transport rules</h2>
<p>To create the transport rules that will send emails with certain <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8541.md")
</div> to Email Security:
<ol>
<li>
<p>Open the new <a href="https://admin.exchange.microsoft.com/#/homepage">Exchange admin center</a>.</p>
</li>
<li>
<p>Go to <strong>Mail flow</strong> &gt; <strong>Rules</strong>.</p>
</li>
<li>
<p>Select <strong>Add a Rule</strong> &gt; <strong>Create a new rule</strong>.</p>
</li>
<li>
<p>Set the following rule conditions:</p>
<ul>
<li><strong>Name</strong>: <em><code>Email security User Quarantine Message</code></em>.</li>
<li><strong>Apply this rule if</strong>: <em>The message headers</em> &gt; <em>includes any of these words</em>.
<ul>
<li><strong>Enter text</strong>: <code>X-Area1Security-Disposition</code> &gt; <strong>Save</strong>.</li>
<li><strong>Enter words</strong>: <code><code>UCE</code>, <code>SPOOF</code></code> &gt; <strong>Add</strong> &gt; <strong>Save</strong>.</li>
</ul>
</li>
<li><strong>Apply this rule if</strong>: Select <strong>+</strong> to add a second condition.</li>
<li><strong>And</strong>: <em>The sender</em> &gt; <em>IP address is in any of these ranges or exactly matches</em> &gt; enter the egress IPs in the <a href="/email-security/deployment/inline/reference/egress-ips/">Egress IPs page</a>.</li>
<li><strong>Do the following</strong> - <em><em>Modify the message properties</em> &gt; <em>Set the Spam Confidence Level (SCL)</em> &gt; <em>5</em></em>.</li>
</ul>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>You can use the default values on this screen. Select <strong>Next</strong>.</p>
</li>
<li>
<p>Review your settings and select <strong>Finish</strong> &gt; <strong>Done</strong>.</p>
</li>
<li>
<p>Select the rule <code>Email security User Quarantine Message</code> you have just created, and <strong>Enable</strong>.</p>
</li>
<li>
<p>Select <strong>Add a Rule</strong> &gt; <strong>Create a new rule</strong>.</p>
</li>
<li>
<p>Set the following rule conditions:</p>
<ul>
<li><strong>Name</strong>: <em><code>Email security User Quarantine Message Admin Release</code></em>.</li>
<li><strong>Apply this rule if</strong>: <em>The message headers</em> &gt; <em>includes any of these words</em>.
<ul>
<li><strong>Enter text</strong>: <code>X-Area1Security-Disposition</code> &gt; <strong>Save</strong>.</li>
<li><strong>Enter words</strong>: <em><code>MALICIOUS</code></em> &gt; <strong>Add</strong> &gt; <strong>Save</strong>.</li>
</ul>
</li>
<li><strong>Apply this rule if</strong>: Select <strong>+</strong> to add a second condition.</li>
<li><strong>And</strong>: <em>The sender</em> &gt; <em>IP address is in any of these ranges or exactly matches</em> &gt; enter the egress IPs in the <a href="/email-security/deployment/inline/reference/egress-ips/">Egress IPs page</a>.</li>
<li><strong>Do the following</strong>: <em><em>Modify the message properties</em> &gt; <em>Set the Spam Confidence Level (SCL)</em> &gt; <em>9</em></em>.</li>
</ul>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>You can use the default values on this screen. Select <strong>Next</strong>.</p>
</li>
<li>
<p>Review your settings and select <strong>Finish</strong> &gt; <strong>Done</strong>.</p>
</li>
<li>
<p>Select the rule <em><code>Email security User Quarantine Message Admin Release</code></em> you have just created, and select <strong>Enable</strong>.</p>
</li>
</ol>
