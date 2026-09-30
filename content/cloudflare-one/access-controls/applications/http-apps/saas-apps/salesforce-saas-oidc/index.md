<p>This guide covers how to configure <a href="https://help.salesforce.com/s/articleView?id=sf.sso_provider_openid_connect.htm&amp;type=5">Salesforce</a> as an OpenID Connect (OIDC) application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Salesforce account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, select <em>Salesforce</em>.</li>
<li>For the authentication protocol, select <strong>OIDC</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>In <strong>Scopes</strong>, select the attributes that you want Access to send in the ID token.</li>
<li>In <strong>Redirect URLs</strong>, enter the callback URL obtained from Salesforce (<code>https://&lt;your-domain&gt;.my.salesforce.com/services/authcallback/&lt;URL Suffix&gt;</code>). Refer to <a href="#2-add-a-sso-provider-to-salesforce">Add a SSO provider to Salesforce</a> for instructions on obtaining this value.</li>
<li>(Optional) Enable <a href="https://www.oauth.com/oauth2-servers/pkce/">Proof of Key Exchange (PKCE)</a> if the protocol is supported by your IdP. PKCE will be performed on all login attempts.</li>
<li>Copy the following values:
<ul>
<li><strong>Client ID</strong></li>
<li><strong>Client Secret</strong></li>
<li><strong>Authorization endpoint</strong></li>
<li><strong>Token endpoint</strong></li>
<li><strong>User info endpoint</strong></li>
</ul>
</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>(Optional) In <strong>Experience settings</strong>, configure <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher settings</a> by turning on <strong>Enable App in App Launcher</strong> and, in <strong>App Launcher URL</strong>, entering <code>https://&lt;your-domain&gt;.my.salesforce.com</code>.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-add-a-sso-provider-to-salesforce"><ol start="2">
<li>Add a SSO provider to Salesforce</li>
</ol></h2>
<ol>
<li>In Salesforce, go to <strong>Setup</strong>.</li>
<li>In the <strong>Quick Find</strong> box, enter <code>auth</code> and select <strong>Auth providers</strong>.</li>
<li>Select <strong>New</strong>.</li>
<li>For the provider type, select <strong>OpenID Connect</strong>.</li>
<li>Enter a name for the SSO provider (for example, <code>Cloudflare Access</code>).</li>
<li>Fill in the following fields with values obtained from Cloudflare Access:
<ul>
<li><strong>Consumer Key</strong>: Client ID</li>
<li><strong>Consumer Secret</strong>: Client Secret</li>
<li><strong>Authorize Endpoint URL</strong>: Authorization endpoint</li>
<li><strong>Token endpoint URL</strong>: Token endpoint</li>
<li><strong>User Info Endpoint URL</strong>: User info endpoint</li>
<li><strong>Token Issuer</strong>: Issuer</li>
</ul>
</li>
<li>(Optional) Enable <strong>Use Proof Key for Code Exchange</strong> if you enabled it in Access.</li>
<li>In <strong>Default Scopes</strong>, enter a space-separated list of the scopes you configured in Access (for example, <code>openid email profile groups</code>).</li>
<li>Select <strong>Save</strong>.</li>
<li>Copy the <strong>Callback URL</strong>:</li>
</ol>
<pre><code class="language-txt">https://&lt;your-domain&gt;.my.salesforce.com/services/authcallback/&lt;URL Suffix&gt;&#10;</code></pre>
<ol start="11">
<li>In Cloudflare One, paste the Callback URL into the <strong>Redirect URL</strong> field.</li>
</ol>
<p>To test the integration, open an incognito browser window and go to the <strong>Test-Only Initialization URL</strong> ( <code>https://&lt;your-domain&gt;.my.salesforce.com/services/auth/test/&lt;URL Suffix&gt;</code>)</p>
<h2 id="3-enable-single-sign-on-in-salesforce"><ol start="3">
<li>Enable Single Sign-On in Salesforce</li>
</ol></h2>
<ol>
<li></li>
</ol>
<p>Enable Cloudflare Access as an identity provider on your Salesforce domain:</p>
<ol>
<li>
<p>In the <strong>Quick Find</strong> box, enter <code>domain</code> and select <strong>My Domain</strong>.</p>
</li>
<li>
<p>In <strong>Authentication Configuration</strong>, select <strong>Edit</strong>.</p>
</li>
<li>
<p>In <strong>Authentication Service</strong>, turn on the Cloudflare Access provider.</p>
</li>
<li>
<p>(Optional) To require users to login with Cloudflare Access:</p>
<ol>
<li>In the <strong>Quick Find</strong> box, enter <code>single sign-on</code> and select <strong>Single Sign-On Settings</strong>.</li>
<li>Turn on <strong>Disable login with Salesforce credentials</strong>.</li>
</ol>
</li>
</ol>
<p>To test, open an incognito browser window and go to your Salesforce domain (<code>https://&lt;your-domain&gt;.my.salesforce.com</code>).</p>
