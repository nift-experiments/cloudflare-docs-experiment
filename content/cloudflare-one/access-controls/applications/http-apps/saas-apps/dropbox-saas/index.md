<p>This guide covers how to configure <a href="https://help.dropbox.com/security/sso-admin">Dropbox</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Dropbox Advanced, Business Plus, or Enterprise account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, select <code>Dropbox</code>.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>Dropbox</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://www.dropbox.com/saml_login</code></li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>SSO endpoint</strong> and <strong>Public key</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-create-a-certificate-file"><ol start="2">
<li>Create a certificate file</li>
</ol></h2>
<ol>
<li>Paste the <strong>Public key</strong> in a text editor.</li>
<li>Wrap the certificate in <code>-----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>.</li>
<li>Set the file extension as <code>.pem</code> and save.</li>
</ol>
<h2 id="3-add-a-saml-sso-provider-to-dropbox"><ol start="3">
<li>Add a SAML SSO provider to Dropbox</li>
</ol></h2>
<ol>
<li>In Dropbox, go to your profile picture &gt; <strong>Settings</strong> &gt; <strong>Admin Console</strong> &gt; <strong>Security</strong> &gt; <strong>Single sign-on</strong>.</li>
<li>For <strong>Single sign-on</strong>, select <em>Optional</em>.</li>
<li>Select <strong>Add Identity provider sign-in URL</strong>.</li>
<li>Paste the SSO endpoint from application configuration in Cloudflare One and select <strong>Done</strong>.</li>
<li>Select <strong>Add X.509 certificate</strong> and upload the <code>.pem</code> file from step <a href="#2-create-a-certificate-file">2. Create a certificate file</a>.</li>
<li>Copy <strong>SSO sign-in URL</strong>. This is your custom Dropbox SSO URL.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="3-test-the-integration-and-require-sso"><ol start="3">
<li>Test the integration and require SSO</li>
</ol></h2>
<ol>
<li>
<p>Open an incognito browser window and go to your custom Dropbox SSO URL. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</p>
</li>
<li>
<p>After this is successful, you may want to require users to log in via SSO. Go to your profile picture &gt; <strong>Settings</strong> &gt; <strong>Admin Console</strong> &gt; <strong>Security</strong> &gt; <strong>Single sign-on</strong>. For <strong>Single sign-on</strong>, select <em>Required</em>. Dropbox will send an email to your users notifying them of the change.</p>
</li>
</ol>
