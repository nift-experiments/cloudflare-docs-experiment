<p>If you observe suspicious activity within your Cloudflare account, secure your account with these steps.</p>
<h2 id="step-1-change-your-password">Step 1 - Change your password</h2>
<p>For more guidance on changing your password, refer to <a href="/fundamentals/user-profiles/change-password-or-email/">Change email address or password</a>.</p>
<h2 id="step-2-revoke-active-account-sessions">Step 2 - Revoke active account sessions</h2>
<p>When there is more than one active session associated with your email account, you can revoke any session that is not the current session.</p>
<p>To revoke a session:</p>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>My Profile</strong> &gt; <strong>Sessions</strong>.</li>
<li>On a specific section, click <strong>Revoke</strong>.</li>
<li>You will be prompted to enter your password before revoking the session.</li>
</ol>
<h2 id="step-3-enable-two-factor-authentication-2fa">Step 3 - Enable Two-Factor Authentication (2FA)</h2>
<p>To prevent future compromises, make sure that you have <a href="/fundamentals/user-profiles/2fa/">Two-Factor Authentication (2FA)</a> enabled on your account.</p>
<h2 id="step-4-change-api-keys-and-tokens">Step 4 - Change API keys and tokens</h2>
<h3 id="api-keys">API keys</h3>
<p>If your API key might be compromised, change your API key:</p>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong>.</li>
<li>In the <strong>API Keys</strong> section, find your key.</li>
<li>Select <strong>Change</strong>.</li>
</ol>
<h3 id="api-tokens">API tokens</h3>
<p>If your token is lost or compromised, you can either create a new token or roll your token to generate a new secret. Rolling your API token into a new one will invalidate the previous token, but the access and permissions will be the same as the previous API token. The new token uses the <a href="/fundamentals/api/get-started/token-formats/">scannable format</a>, which allows credential scanning tools to detect leaked tokens.</p>
<p>To roll your API token:</p>
<ol>
<li>Go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Next to the API token you want to roll, select the <strong>three dot icon</strong> &gt; <strong>Roll</strong>.</li>
<li>Select <strong>Confirm</strong> to generate a new API token.</li>
</ol>
<h2 id="step-5-review-the-audit-log">Step 5 - Review the audit log</h2>
<p>To access audit logs in the Cloudflare dashboard:</p>
<p>In the Cloudflare dashboard, go to the <strong>Audit Logs</strong> page.</p>
<div class="nb-dash-button"></div>
<p>You can search these audit logs by user email or domain and filter by date range. To download audit logs, click <strong>Download CSV</strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8940.md")
</aside>
<p>If you notice any settings were changed, you should undo those changes.</p>
