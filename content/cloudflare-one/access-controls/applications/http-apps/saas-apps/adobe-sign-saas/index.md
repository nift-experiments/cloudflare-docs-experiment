<p>This guide covers how to configure <a href="https://helpx.adobe.com/sign/using/enable-saml-single-sign-on.html">Adobe Acrobat Sign</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Adobe Acrobat Sign account</li>
<li>A <a href="https://helpx.adobe.com/sign/using/claim-domain-names.html">claimed domain</a> in Adobe Acrobat Sign</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>Adobe Sign</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Copy the <strong>Access Entity ID or Issuer</strong>, <strong>Public key</strong>, and <strong>SSO endpoint</strong>.</li>
<li>Keep this window open without selecting <strong>Select configuration</strong>. You will finish this configuration in step <a href="#3-finish-adding-a-saas-application-to-cloudflare-one">3. Finish adding a SaaS application to Cloudflare One</a>.</li>
</ol>
<h2 id="2-add-a-saml-sso-provider-to-adobe-sign"><ol start="2">
<li>Add a SAML SSO provider to Adobe Sign</li>
</ol></h2>
<ol>
<li>In Adobe Acrobat Sign, select your profile picture &gt; your name &gt; <strong>Account Settings</strong> &gt; <strong>SAML Settings</strong>.</li>
<li>Turn <strong>SAML Allowed</strong> on.</li>
<li>Enter a hostname (for example, <code>yourcompanyname</code>). Users can use this URL or <code>https://secure.adobesign.com/public/login</code> to sign in via SSO.</li>
<li>(Optional) For <strong>Single Sign On Login Message</strong>, enter a custom message (for example, <code>Log in via SSO</code>). The default message is <strong>Sign in using your corporate credentials</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID/Issuer URL</strong>: Access Entity ID or Issuer from application configuration in Cloudflare One.</li>
<li><strong>Login URL/SSO Endpoint</strong>: SSO endpoint from application configuration in Cloudflare One.</li>
<li><strong>IdP Certificate</strong>: Public key from application configuration in Cloudflare One. Wrap the certificate in <code>-----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>.</li>
</ul>
</li>
<li>Copy the <strong>Entity ID/SAML Audience</strong> and <strong>Assertion Consumer URL</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="3-finish-adding-a-saas-application-to-cloudflare-one"><ol start="3">
<li>Finish adding a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In your open Cloudflare One window, fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: Entity ID/SAML Audience from Adobe Acrobat Sign SAML SSO configuration.</li>
<li><strong>Assertion Consumer Service URL</strong>: Assertion Consumer URL from Adobe Acrobat Sign SAML SSO configuration.</li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="4-test-the-integration-and-finalize-configuration"><ol start="4">
<li>Test the integration and finalize configuration</li>
</ol></h2>
<ol>
<li>Open an incognito browser window and go to your Adobe Sign hostname URL or <code>https://secure.adobesign.com/public/login</code>. Select the option to sign in via SSO (<strong>Sign in using your corporate credentials</strong> if you have not configured a custom message). You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4872.md")
</aside>
<ol start="2">
<li>Once this is successful, you can make sign in via SSO mandatory. Select your profile picture &gt; your name &gt; <strong>Account Settings</strong> &gt; <strong>SAML Settings</strong>, and then turn on <strong>SAML Mandatory</strong>. Keeping <strong>Allow Acrobat Sign Account Administrators to log in using their Acrobat Sign Credentials</strong> turned on will allow administrators to log in even if your account experiences SSO issues.</li>
</ol>
