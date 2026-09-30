<p>Before deploying Email security to production, you will have to consider reporting any phishing attacks, evaluating which disposition to assign a specific message, and using different screen criteria to search through your inbox.</p>
<p>PhishNet is an add-in button that helps users to submit phish samples missed by Email security detection.</p>
<h3 id="phishnet-for-microsoft-365">PhishNet for Microsoft 365</h3>
<p>To set up PhishNet Microsoft 365:</p>
<ol>
<li>Log in to the Microsoft admin panel. Go to <strong>Microsoft 365 admin center</strong> &gt; <strong>Settings</strong> &gt; <strong>Integrated Apps</strong>.</li>
<li>Select <strong>Upload custom apps</strong>.</li>
<li>Choose <strong>Provide link to manifest file</strong> and paste the following URL:</li>
</ol>
<pre><code class="language-txt">https://phishnet-o365.area1cloudflare-webapps.workers.dev?clientId=ODcxNDA0MjMyNDM3NTA4NjQwNDk1Mzc3MDIxNzE0OTcxNTg0Njk5NDEyOTE2NDU5ODQyNjU5NzYzNjYyNDQ3NjEwMzIxODEyMDk1NQ&#10;</code></pre>
<ol start="4">
<li>Verify and complete the wizard.</li>
</ol>
<h3 id="phishnet-for-google-workspace">PhishNet for Google Workspace</h3>
<p>To set up PhishNet for Google Workspace:</p>
<ol>
<li>Log in to the Google Workspace Marketplace using an administrator account.</li>
<li>Select <strong>Admin install</strong> to install Cloudflare PhishNet.</li>
</ol>
<p>Refer to <a href="/cloudflare-one/email-security/settings/phish-submissions/phishnet-google-workspace/#set-up-phishnet-for-google-workspace">Set up PhishNet for Google Workspace</a> for more information.</p>
