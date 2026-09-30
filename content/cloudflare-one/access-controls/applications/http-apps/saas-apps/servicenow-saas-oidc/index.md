<p>This guide covers how to configure <a href="https://docs.servicenow.com/bundle/washingtondc-platform-security/page/integrate/single-sign-on/task/create-OIDC-configuration-SSO.html">ServiceNow</a> as an OIDC application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a ServiceNow account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>ServiceNow</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>OIDC</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>In <strong>Scopes</strong>, select the attributes that you want Access to send in the ID token.</li>
<li>In <strong>Redirect URLs</strong>, enter <code>https://&lt;INSTANCE-NAME&gt;.service-now.com/navpage.do</code>.</li>
<li>(Optional) Enable <a href="https://www.oauth.com/oauth2-servers/pkce/">Proof of Key Exchange (PKCE)</a> if the protocol is supported by your IdP. PKCE will be performed on all login attempts.</li>
<li>Copy the <strong>Client secret</strong> and <strong>Client ID</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>(Optional) In <strong>Experience settings</strong>, configure <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher settings</a> by turning on <strong>Enable App in App Launcher</strong> and, in <strong>App Launcher URL</strong>, entering <code>https://&lt;INSTANCE-NAME&gt;.service-now.com</code>.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-add-the-multiple-provider-single-sign-on-installer-plugin-to-servicenow"><ol start="2">
<li>Add the Multiple Provider Single Sign-On Installer Plugin to ServiceNow</li>
</ol></h2>
<ol>
<li>In ServiceNow, select <strong>All</strong>.</li>
<li>In the search bar, enter <code>System Applications</code>, and under <strong>All Available Applications</strong>, select <strong>All</strong>.</li>
<li>In the search bar, enter <code>Integration - Multiple Provider Single Sign-On Installer</code>.</li>
<li>Select <strong>Install</strong>.</li>
<li>Ensure that <strong>Install now</strong> is selected, and select <strong>Install</strong>.</li>
</ol>
<h2 id="3-add-and-test-an-oidc-sso-provider-in-servicenow"><ol start="3">
<li>Add and Test an OIDC SSO provider in ServiceNow</li>
</ol></h2>
<ol>
<li>Select <strong>All</strong>.</li>
<li>In the search bar enter <code>Multi-Provider SSO</code>, and select <strong>Identity Providers</strong>.</li>
<li>Select <strong>New</strong> &gt; <strong>OpenID Connect</strong>.</li>
<li>In the pop-up, fill in the following fields:
<ul>
<li><strong>Name</strong>: Name of the SSO (for example, <code>Cloudflare Access</code>). Unless otherwise configured, users will select this name when signing in to ServiceNow.</li>
<li><strong>Client ID</strong>: <strong>Client ID</strong> from application configuration in Cloudflare One.</li>
<li><strong>Client Secret</strong>: <strong>Client Secret</strong> from application configuration in Cloudflare One.</li>
<li><strong>Well Known Configuration URL</strong>: <code>https://&lt;TEAM-DOMAIN&gt;.cloudflareaccess.com/cdn-cgi/access/sso/oidc/&lt;CLIENT-ID&gt;/.well-known/openid-configuration</code>.</li>
</ul>
</li>
<li>Select <strong>Import</strong>.</li>
<li>Ensure <strong>Active</strong> is turned on</li>
<li>Turn on <strong>Show as Login option</strong>, and for <strong>SSO label</strong> enter a label for the user login screen, if desired.</li>
<li>Select <strong>Update</strong>.</li>
</ol>
<h2 id="4-test-the-integration"><ol start="4">
<li>Test the integration</li>
</ol></h2>
<p>For SSO to appear on the login screen, you must have <a href="https://docs.servicenow.com/bundle/washingtondc-platform-security/page/integrate/single-sign-on/concept/sso-acct-recovery.html">account recovery</a> enabled and configured for at least one admin account. After account recovery is configured, log out of ServiceNow and open an incognito browser window. Go to your ServiceNow URL. Select the SSO name you just configured, which will prompt you to sign in with your identity provider. When the integration is successful, you can go back to the OIDC configuration screen to turn on <strong>Default</strong> and/or <strong>Auto Redirect IDP</strong>.</p>
