<p>This guide covers how to configure <a href="https://support.google.com/cloudidentity/topic/7558767">Google Cloud</a> as a SAML application in Cloudflare One.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4855.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Google Workspace account</li>
<li><a href="https://support.google.com/cloudidentity/answer/7389973">Cloud Identity Free or Premium</a> set up in your organization's Google Cloud account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, select <em>Google Cloud</em>.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>google.com</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://www.google.com/a/&lt;your_domain.com&gt;/acs</code></li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>SSO endpoint</strong>, <strong>Access Entity ID or Issuer</strong>, and <strong>Public key</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-create-a-x-509-certificate"><ol start="2">
<li>Create a x.509 certificate</li>
</ol></h2>
<ol>
<li>Paste the Public key from application configuration in Cloudflare One into a text editor.</li>
<li>Wrap the certificate in <code>-----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>.</li>
<li>Set the file extension as <code>.crt</code> and save.</li>
</ol>
<h2 id="3-create-an-sso-provider-in-google-cloud"><ol start="3">
<li>Create an SSO provider in Google Cloud</li>
</ol></h2>
<ol>
<li>In your <a href="https://admin.google.com/">Google Admin console</a>, go to <strong>Security</strong> &gt; <strong>Authentication</strong> &gt; <strong>SSO with third party IdP</strong>.</li>
<li>Select <strong>Third-party SSO profile for your organization</strong> &gt; <strong>Add SSO Profile</strong>.</li>
<li>Turn on <strong>Set up SSO with third-party identity provider</strong>.</li>
<li>Fill in the following information:
<ul>
<li><strong>Sign-in page URL</strong>: SSO endpoint from application configuration in Cloudflare One.</li>
<li><strong>Sign-out page URL</strong>: <code>https://&lt;team-name&gt;.cloudflareaccess.com/cdn-cgi/access/logout</code>, where <code>&lt;team-name&gt;</code> is your Cloudflare One <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
</li>
</ol>
@markup("md", "content/.markup/bodies/4856.md")
</div>.
   - **Verification certificate**: Upload the `.crt` certificate file from step [2. Create a x.509 certificate](#2-create-a-x509-certificate).
5. (Optional) Turn on **Use a domain specific issuer**. If you select this option, Google will send an issuer specific to your Google Cloud domain (`google.com/a/<your_domain.com>` instead of the standard `google.com`).
<h2 id="4-test-the-integration"><ol start="4">
<li>Test the integration</li>
</ol></h2>
<p>Open an incognito browser window and go to your Google Cloud URL (<code>https://console.cloud.google.com/a/&lt;your_domain.com&gt;</code>). Sign in using credentials that do not belong to a super admin account.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p><code>Error: &quot;G Suite - This account cannot be accessed because the login credentials could not be verified.&quot;</code></p>
<p>If you see this error, it is likely that the public key and private key do not match. Confirm that your certificate file includes the correct public key.</p>
