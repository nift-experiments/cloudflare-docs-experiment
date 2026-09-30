<p>This guide covers how to configure <a href="https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise">GitHub Enterprise Cloud</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>A GitHub Enterprise Cloud subscription</li>
<li>Access to a GitHub account as an organization owner</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, select <em>GitHub</em>.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>https://github.com/orgs/&lt;your-organization&gt;</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://github.com/orgs/&lt;your-organization&gt;/saml/consume</code></li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>SSO endpoint</strong>, <strong>Access Entity ID or Issuer</strong>, and <strong>Public key</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-create-an-x-509-certificate"><ol start="2">
<li>Create an X.509 certificate</li>
</ol></h2>
<ol>
<li>Paste the <strong>Public key</strong> in a text editor.</li>
<li>Wrap the certificate in <code>-----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>.</li>
</ol>
<h2 id="3-configure-an-identity-provider-and-saml-sso-in-github-enterprise-cloud"><ol start="3">
<li>Configure an identity provider and SAML SSO in GitHub Enterprise Cloud</li>
</ol></h2>
<ol>
<li>In your GitHub organization page, go to <strong>Settings</strong> &gt; <strong>Authentication security</strong>.</li>
<li>Under <strong>SAML single sign-on</strong>, turn on <strong>Enable SAML authentication</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Sign on URL</strong>: SSO endpoint from application configuration in Cloudflare One.</li>
<li><strong>Issuer</strong>: Access Entity ID or Issuer from application configuration in Cloudflare One.</li>
<li><strong>Public certificate</strong>: Paste the entire x.509 certificate from step <a href="#2-create-a-x509-certificate">2. Create a x.509 certificate</a>.</li>
</ul>
</li>
</ol>
<h2 id="4-test-the-integration"><ol start="4">
<li>Test the integration</li>
</ol></h2>
<p>Select <strong>Test SAML configuration</strong>. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.
When this is successful, select <strong>Save</strong>.</p>
<p>You can also turn on <strong>Require SAML SSO authentication for all members of your organization</strong> if you want to enforce SSO login with Cloudflare Access.</p>
