<p>This guide covers how to configure <a href="https://support.pingboard.com/hc/en-us/articles/360046585994-Set-Up-a-Custom-SSO-Solution">Pingboard</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Pingboard account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>Pingboard</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>http://app.pingboard.com/sp</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://sso-demo.pingboard.com/auth/saml/consume</code></li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>SAML Metadata endpoint</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-add-a-saml-sso-provider-to-pingboard"><ol start="2">
<li>Add a SAML SSO provider to Pingboard</li>
</ol></h2>
<ol>
<li>In Pingboard, go to <strong>Account</strong> &gt; <strong>Add-Ons</strong>.</li>
<li>Under <strong>Third-Party Integrations</strong>, select <strong>Custom SSO</strong>.</li>
<li>In a web browser, paste the SAML Metadata endpoint you copied from the application configuration in Cloudflare One. Next, copy the contents of the displayed page.</li>
<li>In Pingboard, under <strong>IdP Metadata</strong>, paste the contents from the SAML Metadata endpoint.</li>
<li>(Optional) Under <strong>Sign in with</strong>, enter a name (for example, <code>Cloudflare Access</code>). Your users will select this name when signing in.</li>
</ol>
<h2 id="3-test-the-integration"><ol start="3">
<li>Test the integration</li>
</ol></h2>
<p>Open an incognito browser window and go to your Pingboard URL. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</p>
