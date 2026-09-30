<p>This guide covers how to configure <a href="https://docs.digicert.com/en/certcentral/manage-account/saml-admin-single-sign-on-guide/configure-saml-single-sign-on.html">Digicert</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Digicert account</li>
<li><a href="https://docs.digicert.com/en/certcentral/manage-account/saml-admin-single-sign-on-guide/saml-single-sign-on-prerequisites.html">SAML</a> enabled in your Digicert account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>Digicert</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>https://www.digicert.com/account/sso/metadata</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://www.digicert.com/account/sso/</code></li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>SAML Metadata endpoint</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-add-a-saml-sso-provider-in-digicert"><ol start="2">
<li>Add a SAML SSO provider in Digicert</li>
</ol></h2>
<ol>
<li>In Digicert, select <strong>Settings</strong> &gt; <strong>Single Sign-On</strong> &gt; <strong>Set up SAML</strong>.</li>
<li>Under <strong>How will you send data from your IDP?</strong>, turn on <strong>Use a dynamic URL</strong>.</li>
<li>Under <strong>Use a dynamic URL</strong>, paste the SAML Metadata endpoint from application configuration in Cloudflare One.</li>
<li>Under <strong>How will you identify a user?</strong>, turn on <strong>NameID</strong>.</li>
<li>Under <strong>Federation Name</strong>, enter a name (for example, <code>Cloudflare Access</code>). Your users will select this name when signing in.</li>
<li>Select <strong>Save SAML Settings</strong>.</li>
</ol>
<h2 id="3-test-and-enable-sso-in-digicert"><ol start="3">
<li>Test and Enable SSO in Digicert</li>
</ol></h2>
<ol>
<li>In Digicert, select <strong>Settings</strong> &gt; <strong>Single Sign-On</strong>.</li>
<li>Copy the <strong>SP Initiated Custom SSO URL</strong>.</li>
<li>Paste the URL into an incognito browser window and sign in. Upon successful sign in, SAML SSO is fully enabled.</li>
<li>(Optional) By default, users can choose to sign in directly or with SSO. To require SSO sign in, go to <strong>Account</strong> &gt; <strong>Users</strong>. Turn on <strong>Only allow this user to log in through SAML/OIDC SSO</strong> in the user details of the desired user.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4867.md")
</aside>
