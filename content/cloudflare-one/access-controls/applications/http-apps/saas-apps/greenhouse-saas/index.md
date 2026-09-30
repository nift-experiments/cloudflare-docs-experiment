<p>This guide covers how to configure <a href="https://support.greenhouse.io/hc/en-us/articles/360040753811-Configure-single-sign-on-SSO-for-Greenhouse-Recruiting">Greenhouse Recruiting</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to an Advanced or Expert Greenhouse Recruiting site</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>Greenhouse</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Copy the <strong>SAML Metadata endpoint</strong>.</li>
<li>Keep this window open. You will finish this configuration in step <a href="#4-finish-adding-a-saas-application-to-cloudflare-one">4. Finish adding a SaaS application to Cloudflare One</a>.</li>
</ol>
<h2 id="2-download-the-metadata-file"><ol start="2">
<li>Download the metadata file</li>
</ol></h2>
<ol>
<li>Paste the SAML Metadata endpoint from application configuration in Cloudflare One in a web browser.</li>
<li>Follow your browser-specific steps to download the URL's contents as an <code>.xml</code> file.</li>
</ol>
<h2 id="3-add-a-saml-sso-provider-to-greenhouse"><ol start="3">
<li>Add a SAML SSO provider to Greenhouse</li>
</ol></h2>
<ol>
<li>In Greenhouse Recruiting, go to the <strong>Configure</strong> icon &gt; <strong>Dev Center</strong> &gt; <strong>Single sign-on</strong>.</li>
<li>Copy the <strong>SSO Assertion Consumer URL</strong>.</li>
<li>Under <strong>Upload XML file</strong>, select <strong>Choose a file</strong>, and upload the <code>.xml</code> file created in step <a href="#2-download-the-metadata-file">2. Download the metadata file</a>.</li>
<li>Change the <strong>Entity ID</strong> to <code>greenhouse.io</code>.</li>
<li>Keep this window open without selecting <strong>Begin testing</strong>. You will finish this configuration in step <a href="#5-test-the-integration-and-finalize-configuration">5. Test the integration and finalize configuration</a>.</li>
</ol>
<h2 id="4-finish-adding-a-saas-application-to-cloudflare-one"><ol start="4">
<li>Finish adding a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In your open Cloudflare One window, fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>greenhouse.io</code></li>
<li><strong>Assertion Consumer Service URL</strong>: SSO Assertion Consumer URL from SSO configuration in Greenhouse Recruiting.</li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="5-test-the-integration-and-finalize-configuration"><ol start="5">
<li>Test the integration and finalize configuration</li>
</ol></h2>
<ol>
<li>In your open Greenhouse Recruiting window, select <strong>Begin Testing</strong> &gt; <strong>Proceed</strong>.</li>
<li>Open an incognito browser window and go to your Greenhouse Recruiting URL. Choose the SSO login option. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</li>
<li>Once SSO sign in is successful, go to the <strong>Configure</strong> icon &gt; <strong>Dev Center</strong> &gt; <strong>Single sign-on</strong>.</li>
<li>Select <strong>Finalize Configuration</strong>.</li>
<li>In the text field, enter <code>CONFIGURE</code>.</li>
<li>Select <strong>Finalize</strong>. Now, users will only be able to sign in with SSO.</li>
</ol>
