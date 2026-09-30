<p>This guide covers how to configure <a href="https://support.google.com/a/topic/7579248?ref_topic=7556686&amp;sjid=14539485562330725560-NA">Google Workspace</a> as a SAML application in Cloudflare One.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4853.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Google Workspace account</li>
</ul>
<h2 id="1-create-an-application-in-cloudflare-one"><ol>
<li>Create an application in Cloudflare One</li>
</ol></h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Create new application</strong>.</p>
</li>
<li>
<p>Select <strong>SaaS application</strong>.</p>
</li>
<li>
<p>Fill in the following information:</p>
<ul>
<li><strong>Application</strong>: <em>Google</em>.</li>
<li><strong>Entity ID</strong>: Use the value provided to you by Google when <a href="https://saml-doc.okta.com/SAML_Docs/How-to-Enable-SAML-2.0-in-Google-Apps.html">configuring your SAML SSO provider</a>.</li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://www.google.com/a/&lt;your_domain.com&gt;/acs</code>, where <code>&lt;your_domain.com&gt;</code> is your Google Workspace domain.</li>
<li><strong>Name ID Format</strong>: <em>Email</em>.</li>
</ul>
</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4852.md")
</aside>
<ol start="5">
<li>
<p><a href="/cloudflare-one/access-controls/policies/">Create an Access policy</a> for your application. For example, you could allow users with an <code>@your_domain.com</code> email address.</p>
</li>
<li>
<p>Copy the <strong>SSO endpoint</strong>, <strong>Access Entity ID or Issuer</strong>, and <strong>Public key</strong>. These values will be used to configure Google Workspace.</p>
</li>
<li>
<p>Save the application.</p>
</li>
</ol>
<h2 id="2-create-a-certificate-from-your-public-key"><ol start="2">
<li>Create a certificate from your public key</li>
</ol></h2>
<ol>
<li>
<p>Copy and then paste your <strong>Public key</strong> into a text editor.</p>
</li>
<li>
<p>Wrap the certificate in <code>-----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>. For example,</p>
</li>
</ol>
<pre><code class="language-txt">&#45;----BEGIN CERTIFICATE-----&#10;&lt;PUBLIC_KEY&gt;&#10;&#45;----END CERTIFICATE-----&#10;</code></pre>
<ol start="3">
<li>Set the file extension as <code>.crt</code> and save.</li>
</ol>
<h2 id="3-create-an-sso-provider-in-google-workspace"><ol start="3">
<li>Create an SSO provider in Google Workspace</li>
</ol></h2>
<ol>
<li>Log in to your <a href="https://admin.google.com/">Google Admin console</a>.</li>
<li>Go to <strong>Security</strong> &gt; <strong>Authentication</strong> &gt; <strong>SSO with third party IdP</strong>.</li>
<li>Select <strong>Third-party SSO profile for your organization</strong>.</li>
<li>Enable <strong>Set up SSO with third-party identity provider</strong>.</li>
<li>Fill in the following information:
<ul>
<li><strong>Sign-in page URL</strong>: Copy and then paste your <strong>SSO endpoint</strong> from Cloudflare One.</li>
<li><strong>Sign-out page URL</strong>: <code>https://&lt;team-name&gt;.cloudflareaccess.com/cdn-cgi/access/logout</code>, where <code>&lt;team-name&gt;</code> is your Cloudflare One <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
</li>
</ol>
@markup("md", "content/.markup/bodies/4854.md")
</div>.
   - **Verification certificate**: Upload the certificate file containing your public key.
6. (Optional) Enable **Use a domain specific issuer**. If you select this option, Google will send an issuer specific to your Google Workspace domain (`google.com/a/<your_domain.com>` instead of the standard `google.com`).
<h2 id="4-test-the-integration"><ol start="4">
<li>Test the integration</li>
</ol></h2>
<ol>
<li>In your <a href="https://admin.google.com/">Google Admin console</a>, go to <strong>Apps</strong> &gt; <strong>Google Workspace</strong> &gt; <strong>Gmail</strong> &gt; <strong>Setup</strong>.</li>
<li>Copy your Gmail <strong>Web address</strong>.</li>
<li>Open an incognito browser window and go to your Gmail web address (for example, <code>https://mail.google.com/a/&lt;your_domain.com&gt;</code>).</li>
</ol>
<p>An Access login screen should appear.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p><code>Error: &quot;G Suite - This account cannot be accessed because the login credentials could not be verified.&quot;</code></p>
<p>If you see this error, it is likely that the public key and private key do not match. Confirm that your certificate file includes the correct public key.</p>
