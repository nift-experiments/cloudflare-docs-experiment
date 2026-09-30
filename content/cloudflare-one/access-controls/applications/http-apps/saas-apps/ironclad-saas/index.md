<p>This guide covers how to configure <a href="https://support.ironcladapp.com/hc/articles/12286012625559-Set-Up-Generic-SSO-SAML-Integration">Ironclad</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Ironclad site</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>Ironclad</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Copy the <strong>SSO Endpoint</strong> and <strong>Public key</strong>.</li>
<li>Keep this window open. You will finish this configuration in step <a href="#3-finish-adding-a-saas-application-to-cloudflare-one">3. Finish adding a SaaS application to Cloudflare One</a>.</li>
</ol>
<h2 id="2-add-a-saml-sso-provider-to-ironclad"><ol start="2">
<li>Add a SAML SSO provider to Ironclad</li>
</ol></h2>
<ol>
<li>In Ironclad, select your profile picture &gt; <strong>Company settings</strong> &gt; <strong>Integrations</strong> &gt; <strong>SAML</strong>.</li>
<li>Select <strong>Add SAML Configuration</strong> &gt; <strong>Show Additional IdP Settings</strong>.</li>
<li>Copy the <strong>Callback</strong> value.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entry Point</strong>: SSO endpoint from application configuration in Cloudflare One.</li>
<li><strong>Identity Provider Certificate</strong>: Public key from application configuration in Cloudflare One. The key will automatically be wrapped in <code>-----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="3-finish-adding-a-saas-application-to-cloudflare-one"><ol start="3">
<li>Finish adding a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In your open Cloudflare One window, fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>ironcladapp.com</code></li>
<li><strong>Assertion Consumer Service URL</strong>: Callback from Ironclad SAML SSO set-up.</li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="4-add-a-test-user-to-ironclad-and-test-the-integration"><ol start="4">
<li>Add a test user to Ironclad and test the integration</li>
</ol></h2>
<ol>
<li>In Ironclad, select your profile picture &gt; <strong>Company settings</strong> &gt; <strong>Users &amp; Groups</strong>.</li>
<li>Select <strong>Invite User</strong>.</li>
<li>For <strong>Email addresses</strong>, add your desired email address for your test user.</li>
<li>For <strong>Sign-in Method</strong>, ensure <strong>Sign in with (your-team-domain.cloudflareaccess.com)</strong> is selected</li>
<li>Select <strong>Invite</strong>.</li>
<li>In the invitation email sent to the test user, select <strong>Join now</strong>. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</li>
<li>Once this is successful, you can contact your account team or <code>support@ironcladapp.com</code> to migrate existing users to SSO login.</li>
</ol>
