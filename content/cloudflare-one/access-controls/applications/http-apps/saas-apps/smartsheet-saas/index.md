<p>This guide covers how to configure <a href="https://help.smartsheet.com/articles/2483123-domain-level-saml-configuration">Smartsheet</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Smartsheet Enterprise account</li>
<li>A <a href="https://help.smartsheet.com/articles/2483051-domain-management">domain</a> verified in Smartsheet</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4840.md")
</aside>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>Smartsheet</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>urn:amazon:cognito:sp:us-east-1_xww1cbP43</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://saml.authn.smartsheet.com/saml2/idpresponse</code></li>
<li><strong>Name ID format</strong>: <em>Unique ID</em></li>
</ul>
</li>
<li>Copy the <strong>SAML Metadata endpoint</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-create-and-test-a-saml-sso-provider-in-smartsheet"><ol start="2">
<li>Create and test a SAML SSO provider in Smartsheet</li>
</ol></h2>
<ol>
<li>In your Smartsheet Admin Center, go to <strong>Settings</strong> &gt; <strong>Authentication</strong> &gt; <strong>Add a SAML IdP</strong>.</li>
<li>In <strong>Other IdP (Customize)</strong>, select <strong>Configure</strong>.</li>
<li>Select <strong>Next</strong>.</li>
<li>Under <strong>XML URL</strong>, paste the SAML Metadata endpoint from application configuration in Cloudflare One.</li>
<li>Under <strong>Name SAML IdP</strong>, enter a name (for example, <code>Cloudflare Access</code>).</li>
<li>Select <strong>Save &amp; Next</strong>.</li>
<li>Select <strong>Verify connection</strong> and sign in via Access. If validation is successful, you will see a <strong>SAML IdP Successfully Connected!</strong> message. Close the configuration verification page.</li>
<li>Turn on <strong>I have successfully verified the connection</strong>.</li>
<li>Select <strong>Save &amp; Next</strong>.</li>
<li>Under <strong>Assign domains to SAML IdP</strong>, select your desired domain.</li>
<li>Select <strong>Save and Next</strong> and then <strong>Finish</strong>.</li>
</ol>
