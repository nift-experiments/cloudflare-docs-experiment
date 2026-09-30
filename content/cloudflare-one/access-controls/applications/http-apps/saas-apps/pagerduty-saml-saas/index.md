<p>This guide covers how to configure <a href="https://support.pagerduty.com/docs/sso">PagerDuty</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a PagerDuty site</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, select <em>PagerDuty</em>.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>https://&lt;your-subdomain&gt;.pagerduty.com</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code> https://&lt;your-subdomain&gt;.pagerduty.com/sso/saml/consume</code></li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>SSO endpoint</strong> and <strong>Public key</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-create-a-x-509-certificate"><ol start="2">
<li>Create a x.509 certificate</li>
</ol></h2>
<ol>
<li>Paste the <strong>Public key</strong> in a text editor.</li>
<li>Amend the public key so each row is a maximum of 64 characters long. Originally, each full row of the public key is 65 characters long.</li>
<li>Wrap the certificate in <code>-----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>.</li>
</ol>
<h2 id="3-add-a-saml-sso-provider-to-pagerduty"><ol start="3">
<li>Add a SAML SSO provider to PagerDuty</li>
</ol></h2>
<ol>
<li>In PagerDuty, select your profile picture and go to <strong>Account Settings</strong> &gt; <strong>Single Sign-on</strong>.</li>
<li>Turn on <strong>SAML</strong>.</li>
<li>In <strong>X.509 Certificate</strong>, paste the entire x.509 certificate from step <a href="#2-create-a-x509-certificate">2. Create a x.509 certificate</a>.</li>
<li>In <strong>Login URL</strong>, paste the SSO endpoint from application configuration in Cloudflare One.</li>
<li>Select <strong>Save Changes</strong>.</li>
</ol>
<h2 id="4-test-the-integration-and-finalize-sso-configuration"><ol start="4">
<li>Test the integration and finalize SSO configuration</li>
</ol></h2>
<ol>
<li>Open an incognito window and paste your PagerDuty URL into the address bar. Select <strong>Sign In With Single Sign-On</strong>. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</li>
<li>In an incognito window, paste your PagerDuty URL and select <strong>Sign In With Single Sign-On</strong>. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</li>
<li>Once SSO sign in is successful, select your profile picture and go to <strong>Account Settings</strong> &gt; <strong>Single Sign-on</strong>.</li>
<li>Turn off <strong>Allow username/password login</strong> and select <strong>Save Changes</strong>. Now, users will only be able to sign in with SSO.</li>
</ol>
