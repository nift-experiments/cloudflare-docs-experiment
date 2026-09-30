<p>This guide covers how to configure <a href="https://support.zoom.com/hc/en/article?id=zm_kb&amp;sysparm_article=KB0060673">Zoom</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Zoom Business, Education, or Enterprise account</li>
<li>An <a href="https://support.zoom.com/hc/en/article?id=zm_kb&amp;sysparm_article=KB0066259">associated domain</a> configured in your Zoom account</li>
<li>A <a href="https://support.zoom.com/hc/en/article?id=zm_kb&amp;sysparm_article=KB0061540">vanity URL</a> configured in your Zoom account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, select <em>Zoom</em>.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code> https://&lt;your-vanity-url&gt;.zoom.us</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://&lt;your-vanity-url&gt;.zoom.us/saml/SSO</code></li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>Access Entity ID or Issuer</strong>, <strong>Public key</strong>, and <strong>SSO endpoint</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-add-a-saml-sso-provider-in-zoom"><ol start="2">
<li>Add a SAML SSO provider in Zoom</li>
</ol></h2>
<ol>
<li>In Zoom, go to <strong>Advanced</strong> &gt; <strong>Single Sign-On</strong>.</li>
<li>For <strong>Vanity URL</strong>, select the vanity URL you want to configure SSO for.</li>
<li>Fill out the following fields:
<ul>
<li><strong>Sign in page URL</strong>: SSO endpoint from application configuration in Cloudflare One</li>
<li><strong>Identity Provider Certificate</strong>: Public key from application configuration in Cloudflare One</li>
<li><strong>Service Provider (SP) Entity ID</strong>: <code>yourvanityurl.zoom.us</code> (no <code>https://</code>)</li>
<li><strong>Issuer (DP Entity ID)</strong>: Access Entity ID or Issuer from application configuration in Cloudflare One</li>
</ul>
</li>
<li>For <strong>Binding</strong>, select <em>http-redirect</em>.</li>
<li>For <strong>Signature Hash Algorithm</strong>, ensure <strong>SHA-256</strong> is selected.</li>
<li>Under <strong>Security</strong>, turn off <strong>Sign SAML request</strong> and <strong>Sign SAML logout request</strong>.</li>
<li>Select <strong>Save Changes</strong>.</li>
<li>Go to <strong>Advanced</strong> &gt; <strong>Security</strong>.</li>
<li>Under <strong>Sign-in Methods</strong>, ensure <strong>Allow users to sign in with Single Sign-On (SSO)</strong> is turned on.</li>
</ol>
<h2 id="3-test-the-integration"><ol start="3">
<li>Test the integration</li>
</ol></h2>
<p>Open an incognito browser window, go to your Zoom vanity URL, and select <strong>Sign in</strong>. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</p>
<p>Once this is successful, you can require SSO for users in your associated domain(s) by completing the following steps:</p>
<ol>
<li>In Zoom, go to <strong>Advanced</strong> &gt; <strong>Security</strong>.</li>
<li>Under <strong>Sign-in Methods</strong>, turn on <strong>Require users to sign in with SSO if their e-mail address belongs to one of the domains below</strong>.</li>
<li>Under <strong>Select Domains</strong>, turn on the domains that you want to require SSO for.</li>
<li>(Optional) Under <strong>Specify users who can bypass SSO sign-in</strong>, add your desired users.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
