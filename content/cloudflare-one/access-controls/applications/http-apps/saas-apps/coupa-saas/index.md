<p>This guide covers how to configure <a href="https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-user-authentication/coupa-saml-sso-setup">Coupa</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Coupa Stage or Production account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>Coupa</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>:
<code>sso-stg1.coupahost.com</code> for a stage account or <code>sso-prd1.coupahost.com</code> for a production account</li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://sso-stg1.coupahost.com/sp/ACS.saml2</code> for a stage account or <code>https://sso-prd1.coupahost.com/sp/ACS.saml2</code> for a production account</li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>Access Entity ID or Issuer</strong> and <strong>SAML Metadata Endpoint</strong>.</li>
<li>In <strong>Default relay state</strong>, enter <code>https://&lt;your-subdomain&gt;.coupahost.com/sessions/saml_post</code>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-download-the-metadata-file"><ol start="2">
<li>Download the metadata file</li>
</ol></h2>
<ol>
<li>Paste the SAML metadata endpoint from application configuration in Cloudflare One in a web browser.</li>
<li>Follow your browser-specific steps to download the URL's contents as an <code>.xml</code> file.</li>
</ol>
<h2 id="3-add-a-saml-sso-provider-in-coupa"><ol start="3">
<li>Add a SAML SSO provider in Coupa</li>
</ol></h2>
<ol>
<li>In Coupa, go to <strong>Setup</strong> &gt; <strong>Company Setup</strong> &gt; <strong>Security Controls</strong>.</li>
<li>Under <strong>Sign in using SAML</strong>, turn on <strong>Sign in using SAML</strong>.</li>
<li>In <strong>Upload IdP metadata</strong>, select <strong>Choose File</strong>, and upload the <code>.xml</code> file you downloaded in step <a href="#2-download-the-metadata-file">2. Download the metadata file</a>.</li>
<li>Turn on <strong>Advanced Options</strong>.</li>
<li>For <strong>Sign in page URL</strong> and <strong>Timeout URL</strong>, enter <code>https://sso-stg1.coupahost.com/sp/startSSO.ping?PartnerIdpId=&lt;access-entity-id-or-issuer&gt;&amp;TARGET=https://&lt;your-subdomain&gt;.coupahost.com/sessions/saml_post</code> using the Access Entity ID or Issuer from application configuration in Cloudflare One.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="3-create-a-test-user-and-test-the-integration"><ol start="3">
<li>Create a test user and test the integration</li>
</ol></h2>
<ol>
<li>In Coupa, go to <strong>Setup</strong> &gt; <strong>Company Setup</strong> &gt; <strong>Users</strong>.</li>
<li>Select <strong>Create</strong>, then enter the user details for your test user. For <strong>Login</strong> and <strong>Single Sign-On ID</strong>, enter the user's email address.</li>
<li>Select <strong>Save</strong>.</li>
<li>Open an incognito browser window and go to your Coupa URL. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</li>
<li>Once the login is successful, you can configure other users for SSO by adding their email to the <strong>Single Sign-On ID</strong> field in <strong>Setup</strong> &gt; <strong>Company Setup</strong> &gt; <strong>Users</strong> &gt; user's name.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4868.md")
</aside>
