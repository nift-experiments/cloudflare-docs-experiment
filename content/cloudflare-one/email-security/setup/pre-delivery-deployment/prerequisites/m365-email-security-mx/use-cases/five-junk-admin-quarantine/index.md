<p>In this tutorial, you will learn to deliver <code>BULK</code> messages to the user's junk email folder, and <code>MALICIOUS</code>, <code>SPAM</code>, and <code>SPOOF</code> messages to the Administrative Quarantine (this requires an administrator to release the emails).</p>
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
<li><strong>Select quarantine policy</strong>: <em>AdminOnlyAccessPolicy</em>.</li>
</ul>
</li>
<li><strong>Phishing</strong>: <em>Quarantine message</em>.
<ul>
<li><strong>Select quarantine policy</strong>: <em>AdminOnlyAccessPolicy</em>.</li>
</ul>
</li>
<li><strong>High confidence phishing</strong>: <em>Quarantine message</em>.
<ul>
<li><strong>Select quarantine policy</strong>: <em>AdminOnlyAccessPolicy</em>.</li>
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
<p>To create the transport rules that will send emails with certain <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/#dispositions">disposition</a> to Email security:</p>
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
<li><strong>Name</strong>: <em>Email security Deliver to Junk Email folder`</em>.</li>
<li><strong>Apply this rule if</strong>: <em>The message headers</em> &gt; <em>includes any of these words</em>.
<ul>
<li><strong>Enter text</strong>: <code>X-CFEmailSecurity-Disposition</code> &gt; <strong>Save</strong>.</li>
<li><strong>Enter words</strong>: <code>BULK</code> &gt; <strong>Add</strong> &gt; <strong>Save</strong>.</li>
</ul>
</li>
<li><strong>Apply this rule if</strong>: Select <strong>+</strong> to add a second condition.</li>
<li><strong>And</strong>: <em>The sender</em> &gt; <em>IP address is in any of these ranges or exactly matches</em> &gt; enter the egress IPs in the <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/">Egress IPs</a> page.</li>
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
<p>Select the rule Email security Deliver to Junk Email folder` you have just created, and <strong>Enable</strong>.</p>
</li>
<li>
<p>Select <strong>Add a Rule</strong> &gt; <strong>Create a new rule</strong>.</p>
</li>
<li>
<p>Set the following rule conditions:</p>
<ul>
<li><strong>Name</strong>: <em><code>Email security Admin Managed Host Quarantine</code></em>.</li>
<li><strong>Apply this rule if</strong>: <em>The message headers</em> &gt; <em>includes any of these words</em>.
<ul>
<li><strong>Enter text</strong>: <code>X-CFEmailSecurity-Disposition</code> &gt; <strong>Save</strong>.</li>
<li><strong>Enter words</strong>: _ <code>MALICIOUS</code>, <code>UCE</code>, <code>SPOOF</code>_ &gt; <strong>Add</strong> &gt; <strong>Save</strong>.</li>
</ul>
</li>
<li><strong>Apply this rule if</strong>: Select <strong>+</strong> to add a second condition.</li>
<li><strong>And</strong>: <em>The sender</em> &gt; <em>IP address is in any of these ranges or exactly matches</em> &gt; enter the egress IPs in the <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/">Egress IPs</a> page.</li>
<li><strong>Do the following</strong>: <em><em>Redirect the message to</em> &gt; <em>hosted quarantine</em></em>.</li>
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
<p>Select the rule <em><code>Email security Admin Managed Host Quarantine</code></em> you have just created, and select <strong>Enable</strong>.</p>
</li>
</ol>
