<p>This guide covers how to configure <a href="https://help.miro.com/hc/articles/360017571414-Single-sign-on-SSO">Miro</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Miro Business or Enterprise plan account</li>
<li>A <a href="https://help.miro.com/hc/articles/360034831793-Domain-control">verified domain</a> added to your Miro account (Enterprise plan), or be prepared to do so during SSO configuration (Business or Enterprise plan)</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>Miro</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>https://miro.com/</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://miro.com/sso/saml</code></li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>SSO endpoint</strong> and <strong>Public key</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-add-a-saml-sso-provider-to-miro"><ol start="2">
<li>Add a SAML SSO provider to Miro</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4849.md")
</div></div>
<h2 id="3-test-the-integration"><ol start="3">
<li>Test the integration</li>
</ol></h2>
<p>In the Miro SAML/SSO configuration page, select <strong>Test SSO Configuration</strong>. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider. If the login is successful, you will receive a <strong>SSO configuration test was successful</strong> message.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4846.md")
</aside>
