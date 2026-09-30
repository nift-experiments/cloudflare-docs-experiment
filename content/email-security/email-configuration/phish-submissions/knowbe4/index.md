<p>If you have KnowBe4 Phish Alert Button (PAB) for Microsoft Outlook, Microsoft Exchange, Microsoft 365, and Google Workspace follow the steps below to set it up with Email security and report suspicious emails.</p>
<ol>
<li>Log in to your KnowBe4 console.</li>
<li>Select the <strong>cog symbol</strong> to go to your <strong>Account Settings</strong> screen.</li>
<li>Go to <strong>Account Integrations</strong> &gt; <strong>Phish Alert</strong>.</li>
<li>In <strong>Setting Name</strong>, give your PAB a descriptive name.</li>
<li>(Optional) If you do not want to differentiate between spam and malicious emails, enter <code>&lt;ACCOUNT_NAME&gt;+user+malicious@submission.area1reports.com</code> in <strong>Send Non-Simulated Emails to</strong> to receive spam reports.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8553.md")
</aside>
<ol start="6">
<li>If you do want to differentiate between spam and malicious emails, go to <strong>Comments and Disposition Settings</strong>.</li>
<li>Select <strong>Allow users to leave comments and disposition</strong>.</li>
<li>Select <strong>Disable Unknown Email Disposition</strong>.</li>
<li>In <strong>Send Dispositioned Emails to</strong>, you need to enter the email addresses to forward spam and malicious emails. You can find these addresses in your <strong>Email security dashboard</strong> &gt; <strong>Support</strong> &gt; <a href="https://horizon.area1security.com/support/service-addresses"><strong>Service Addresses</strong></a>:
<ol>
<li><strong>Phishing/Suspicious</strong>: Enter your malicious email address. For example, <code>&lt;ACCOUNT_NAME&gt;+user+malicious@submission.area1reports.com</code>.</li>
<li><strong>Spam/Junk</strong>: Enter your spam email address. For example, <code>&lt;ACCOUNT_NAME&gt;+user+spam@submission.area1reports.com</code>.</li>
</ol>
</li>
<li>Select <strong>Save changes</strong>.</li>
</ol>
