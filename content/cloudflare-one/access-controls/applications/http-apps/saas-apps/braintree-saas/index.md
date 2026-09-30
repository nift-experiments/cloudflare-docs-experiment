<p>This guide covers how to configure <a href="https://developer.paypal.com/braintree/articles/guides/single-sign-on-sso">Braintree</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Braintree production or sandbox account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>Braintree</code> and select the textbox that appears below.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields with temporary values:
<ul>
<li><strong>Entity ID</strong>: <code>placeholder</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://www.placeholder.com</code></li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>SSO endpoint</strong> and <strong>Public key</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-enable-sso-configuration-in-braintree"><ol start="2">
<li>Enable SSO Configuration in Braintree</li>
</ol></h2>
<ol>
<li>In Braintree, create a <a href="https://developer.paypal.com/braintree/help">support ticket</a>.</li>
<li>In <strong>Search Issues</strong>, enter <code>Login and password issues</code> and select the corresponding value.</li>
<li>In <strong>Issue Details</strong>, fill in the following:
<ul>
<li><strong>Merchant ID</strong>: Your Braintree Merchant ID. This is the 16-digit value that follows <code>/merchants/</code>in your Braintree Control Panel URL.</li>
<li><strong>Email domain(s) to be used in user IDs</strong>: The email domain(s) that should be allowed to sign in to your account via SSO.</li>
<li><strong>Single Sign-on HTTP POST Binding URL</strong>: SSO endpoint from application configuration in Cloudflare One</li>
<li><strong>Certificate for validation</strong>: Public key from application configuration in Cloudflare One.</li>
</ul>
</li>
<li>Select whether you are using a <strong>Production</strong> or <strong>Sandbox</strong> account.</li>
<li>Fill out the <strong>Your contact information</strong> fields and select <strong>Submit a help request</strong>.</li>
<li>When you receive an email stating SSO has been successfully configured for your account, you can proceed to the next step.</li>
</ol>
<h2 id="3-finish-adding-a-saas-application-to-cloudflare-one"><ol start="3">
<li>Finish adding a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Braintree</strong> &gt; <strong>Edit</strong> &gt; <strong>Overview</strong>.</li>
<li>Replace the temporary values for <strong>Entity ID</strong> and <strong>Assertion Consumer Service URL</strong> with the link provided in the successful SSO configuration email from Braintree support. You will use the same link for both values.</li>
<li>Select <strong>Save Application</strong>.</li>
</ol>
<h2 id="4-test-the-integration-and-add-sso-users"><ol start="4">
<li>Test the integration and add SSO users</li>
</ol></h2>
<ol>
<li>In your Braintree Control Panel, select the <strong>settings</strong> icon &gt; <strong>Team</strong>.</li>
<li>Select your desired test user.</li>
<li>Under <strong>Single Sign-On</strong>, select <strong>Enable</strong>.</li>
<li>Open an incognito browser window. In the address bar, paste <code>https://id.sandbox.braintreegateway.com</code> for a sandbox account or
<code>https://id.braintreegateway.com</code> for a production account.</li>
<li>In <strong>Your corporate email address</strong> field, type your test user's email. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</li>
<li>Upon successful sign-in, you can enable SSO for other users using steps 4.1 - 4.3.</li>
</ol>
