<p>This guide covers how to configure <a href="https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/generic-oauth/">Grafana</a> as an OIDC application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Grafana account</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4851.md")
</aside>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong>.</li>
<li>Select <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, select <em>Grafana</em>.</li>
<li>For the authentication protocol, select <strong>OIDC</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>In <strong>Scopes</strong>, select the attributes that you want Access to send in the ID token.</li>
<li>In <strong>Redirect URLs</strong>, enter <code>https://&lt;your-grafana-domain&gt;/login/generic_oauth</code>.</li>
<li>(Optional) Enable <a href="https://www.oauth.com/oauth2-servers/pkce/">Proof of Key Exchange (PKCE)</a> if the protocol is supported by your IdP. PKCE will be performed on all login attempts.</li>
<li>Copy the <strong>Client secret</strong>, <strong>Client ID</strong>, <strong>Token endpoint</strong>, and <strong>Authorization endpoint</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>(Optional) In <strong>Experience settings</strong>, configure <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher settings</a> by turning on <strong>Enable App in App Launcher</strong> and, in <strong>App Launcher URL</strong>, entering <code>https://&lt;your-grafana-domain&gt;/login</code>.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-add-a-sso-provider-to-grafana"><ol start="2">
<li>Add a SSO provider to Grafana</li>
</ol></h2>
<ol>
<li>In Grafana, select the <strong>menu</strong> icon &gt; <strong>Administration</strong> &gt; <strong>Authentication</strong> &gt; <strong>Generic OAuth</strong>.</li>
<li>(Optional) For <strong>Display name</strong>, enter a new display name (for example, <code>Cloudflare Access</code>). Users will select <strong>Sign in with (display name)</strong> when signing in via SSO.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Client Id</strong>: Client ID from application configuration in Cloudflare One</li>
<li><strong>Client secret</strong>: Client secret from application configuration in Cloudflare One</li>
<li><strong>Scopes</strong>: Delete <code>user:email</code> and enter the scopes configured in Cloudflare One</li>
<li><strong>Auth URL</strong>: Authorization endpoint from application configuration in Cloudflare One</li>
<li><strong>Token URL</strong>: Token endpoint from application configuration in Cloudflare One</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="3-test-the-integration"><ol start="3">
<li>Test the integration</li>
</ol></h2>
<p>Log out, then select <strong>Sign in with (display name)</strong>. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</p>
