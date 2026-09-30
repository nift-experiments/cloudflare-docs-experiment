<p>In this tutorial, you will learn how to deliver emails to the Microsoft 365 junk email folder and the Admin Quarantine in Email security.</p>
<h2 id="create-quarantine-policies">Create quarantine policies</h2>
<p>To create <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/4966.md")
</div>:
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
<p>Under <strong>Rules</strong>, select <strong>Quarantine policies</strong>.</p>
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
<li>In <strong>Select release action preference</strong>, choose <em>Allow recipients to request a message to be released from quarantine</em>.</li>
<li>In <strong>Select additional actions recipients can take on quarantined messages</strong>, select the <strong>Delete</strong> and <strong>Preview</strong> checkboxes.</li>
</ul>
</li>
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
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<h2 id="configure-anti-spam-policies">Configure anti-spam policies</h2>
<p>To configure anti-spam policies:</p>
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
<p>Under <strong>Policies</strong>, select <strong>Anti-spam</strong>.</p>
</li>
<li>
<p>Select the <strong>Anti-spam inbound policy (Default)</strong> text (not the checkbox).</p>
</li>
<li>
<p>In <strong>Actions</strong>, scroll down and select <strong>Edit actions</strong>.</p>
</li>
<li>
<p>Set the following conditions and actions (you might need to scroll up or down to find them):</p>
</li>
</ol>
<ul>
<li><strong>Spam</strong>: <em>Move messages to Junk Email folder</em>.</li>
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
<li><strong>Retain spam in quarantine for this many days</strong>: Default is 15 days. Email security recommends 15-30 days.
<ul>
<li>Select the spam actions in the above step.</li>
</ul>
</li>
</ul>
<ol start="8">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="create-transport-rules">Create transport rules</h2>
<p>To create the transport rules that will send emails with certain dispositions to Email security:</p>
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
<li><strong>Name</strong>: <code>Email security Deliver to Junk Email folder</code>.</li>
<li><strong>Apply this rule if</strong>: <em>The message headers</em> &gt; <em>includes any of these words</em>.
<ul>
<li><strong>Enter text</strong>: <code>X-CFEmailSecurity-Disposition</code> &gt; <strong>Save</strong>.</li>
<li><strong>Enter words</strong>: <code>BULK</code> &gt; <strong>Add</strong> &gt; <strong>Save</strong>.</li>
</ul>
</li>
<li><strong>Apply this rule if</strong>: Select <strong>+</strong> to add a second condition.</li>
<li><strong>And</strong>: <em>The sender</em> &gt; <em>IP address is in any of these ranges or exactly matches</em> &gt; enter the egress IPs in the <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/">Egress IPs</a> page.</li>
<li><strong>Do the following</strong> - <em>Modify the message properties</em> &gt; <em>Set the Spam Confidence Level (SCL)</em> &gt; <em>5</em>.</li>
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
<p>Select the rule <code>Email security Deliver to Junk Email folder</code> you have just created, and select <strong>Enable</strong>.</p>
</li>
</ol>
