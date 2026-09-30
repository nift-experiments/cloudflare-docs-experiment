<p>This guide covers how to configure <a href="https://support.atlassian.com/security-and-access-policies/docs/configure-saml-single-sign-on-with-an-identity-provider/">Atlassian Cloud</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to an Atlassian Cloud account</li>
<li>Atlassian Guard Standard subscription</li>
<li>A <a href="https://support.atlassian.com/user-management/docs/verify-a-domain-to-manage-accounts/">domain</a> verified in Atlassian Cloud</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, select <em>Atlassian</em>.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Copy the <strong>Access Entity ID or Issuer</strong>, <strong>Public key</strong>, and <strong>SSO endpoint</strong>.</li>
<li>Keep this window open. You will finish this configuration in step <a href="#4-finish-adding-a-saas-application-to-cloudflare-one">4. Finish adding a SaaS application to Cloudflare One</a>.</li>
</ol>
<h2 id="2-create-a-x-509-certificate"><ol start="2">
<li>Create a x.509 certificate</li>
</ol></h2>
<ol>
<li>Paste the <strong>Public key</strong> in a text editor.</li>
<li>Wrap the certificate in <code>-----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>.</li>
</ol>
<h2 id="3-configure-an-identity-provider-and-saml-sso-in-atlassian-cloud"><ol start="3">
<li>Configure an identity provider and SAML SSO in Atlassian Cloud</li>
</ol></h2>
<ol>
<li>In Atlassian Cloud, go to <strong>Security</strong> &gt; <strong>Identity providers</strong>.</li>
<li>Select <strong>Other provider</strong> &gt; <strong>Choose</strong>.</li>
<li>For <strong>Directory name</strong>, enter your desired name. For example, you could enter <code>Cloudflare Access</code>.</li>
<li>Select <strong>Add</strong> &gt; <strong>Set up SAML single sign-on</strong> &gt; <strong>Next</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4870.md")
</aside>
<ol start="5">
<li>Fill in the following fields:
<ul>
<li><strong>Identity provider Entity ID</strong>: Access Entity ID or Issuer from application configuration in Cloudflare One.</li>
<li><strong>Identity provider SSO URL</strong>: SSO endpoint from application configuration in Cloudflare One.</li>
<li><strong>Public x509 certificate</strong>: Paste the entire x.509 certificate from step <a href="#2-create-a-x509-certificate">2. Create a x.509 certificate</a>.</li>
</ul>
</li>
<li>Select <strong>Next</strong>.</li>
<li>Copy the <strong>Service provider entity URL</strong> and <strong>Service provider assertion consumer service URL</strong>.</li>
<li>Select <strong>Next</strong>.</li>
<li>Under <strong>Link domain</strong>, select the domain you want to use with SAML SSO.</li>
<li>Select <strong>Next</strong> &gt; <strong>Stop and save SAML</strong>.</li>
</ol>
<h2 id="4-finish-adding-a-saas-application-to-cloudflare-one"><ol start="4">
<li>Finish adding a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In your open Cloudflare One window, fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: Service provider entity URL from Atlassian Cloud SAML SSO set-up.</li>
<li><strong>Assertion Consumer Service URL</strong>: Service provider assertion consumer service URL from Atlassian Cloud SAML SSO set-up.</li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="5-create-an-authentication-policy-to-test-integration"><ol start="5">
<li>Create an authentication policy to test integration</li>
</ol></h2>
<p>To enable SSO for users in Atlassian Cloud, create an <a href="https://support.atlassian.com/security-and-access-policies/docs/configure-authentication-policies-for-your-organization/">Atlassian authentication policy</a>:</p>
<ol>
<li>In Atlassian Cloud, go to <strong>Security</strong> &gt; <strong>Authentication policies</strong>.</li>
<li>Select <strong>Add policy</strong>.</li>
<li>Under <strong>Directory</strong>, select the identity provider you used to configure SAML SSO.</li>
<li>For <strong>Policy name</strong>, enter your desired name.</li>
<li>Select <strong>Add</strong>.</li>
<li>In <strong>Settings</strong>, turn on <strong>Enforce single sign-on</strong>.</li>
<li>In <strong>Members</strong>, select <strong>Add members</strong>.</li>
<li>In <strong>Individual Users</strong>, select your desired test user(s) in the dropdown, and select <strong>Add members</strong>.</li>
<li>In <strong>Settings</strong>, select <strong>Update</strong> &gt; <strong>Update</strong>.</li>
</ol>
<h2 id="6-test-the-integration"><ol start="6">
<li>Test the integration</li>
</ol></h2>
<p>Open an incognito browser window and log in with the credentials of the test user you added to the test authentication policy. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider. When this is successful, turn on <strong>Enforce single sign-on</strong> in your desired authentication policy, or add the desired users to the application policy created in step <a href="#5-create-an-authentication-policy-to-test-integration">5. Create an Application Policy to test Integration</a>.</p>
