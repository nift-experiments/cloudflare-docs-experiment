<p>This guide covers how to configure <a href="https://help.asana.com/hc/en-us/articles/14075208738587-Authentication-and-access-management-options-for-paid-plans#gl-saml">Asana</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Super admin access to an Asana Enterprise, Enterprise+, or Legacy Enterprise account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, select <em>Asana</em>.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>https://app.asana.com/</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://app.asana.com/-/saml/consume</code></li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>SSO endpoint</strong> and <strong>Public key</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-add-a-saml-sso-provider-to-asana"><ol start="2">
<li>Add a SAML SSO provider to Asana</li>
</ol></h2>
<ol>
<li>In Asana, select your profile picture &gt; <strong>Admin console</strong> &gt; <strong>Security</strong> &gt; <strong>SAML authentication</strong>.</li>
<li>Under <strong>SAML options</strong>, select <em>Optional</em>.</li>
<li>Fill in the following fields:
<ul>
<li>Sign-in page URL: SSO endpoint from application configuration in Cloudflare One.</li>
<li>X.509 certificate: Public key from application configuration in Cloudflare One. Wrap the public key in <code>-----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>.</li>
</ul>
</li>
<li>Select <strong>Save changes</strong>.</li>
</ol>
<h2 id="3-test-the-integration-and-require-sso"><ol start="3">
<li>Test the integration and require SSO</li>
</ol></h2>
<ol>
<li>
<p>Open an incognito browser window and go to your Asana URL. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</p>
</li>
<li>
<p>After this is successful, you may want to require users to log in via SSO. In Asana, select your profile picture &gt; <strong>Admin console</strong> &gt; <strong>Security</strong> &gt; <strong>SAML authentication</strong>. Under <strong>SAML options</strong>, select <strong>Required for all members, except guest accounts</strong>.</p>
</li>
</ol>
