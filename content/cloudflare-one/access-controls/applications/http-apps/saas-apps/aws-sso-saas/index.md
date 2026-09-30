<p>This guide covers how to configure <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-idp.html">AWS</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to an AWS account</li>
</ul>
<h2 id="1-get-aws-urls"><ol>
<li>Get AWS URLs</li>
</ol></h2>
<ol>
<li>In the AWS admin panel, search for <code>IAM Identity Center</code>.</li>
<li>Go to <strong>IAM Identity Center</strong> &gt; <strong>Settings</strong>.</li>
<li>In the <strong>Identity source</strong> tab, select the <strong>Actions</strong> dropdown and select <em>Change identity source</em>.</li>
<li>Change the identity source to <strong>External identity provider</strong>.</li>
<li>Copy the values shown in <strong>Service provider metadata</strong>. You will need these values when configuring the SaaS application in Cloudflare One.</li>
</ol>
<p>Next, we will obtain <strong>Identity provider metadata</strong> from Cloudflare One.</p>
<h2 id="2-add-a-saas-application-to-cloudflare-one"><ol start="2">
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In a separate tab or window, open the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, select <em>Amazon AWS</em>.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: IAM Identity Center issuer URL</li>
<li><strong>Assertion Consumer Service URL</strong>: IAM Identity Center Assertion Consumer Service (ACS) URL</li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>(Optional) Additional SAML attribute statements can be passed from your IdP to AWS SSO. To learn more about AWS Attribute mapping, refer to <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/attributemappingsconcept.html#supportedidpattributes">Attribute mappings - AWS Single Sign-On</a>.</li>
<li>AWS supports uploading a metadata XML file. To download your SAML metadata from Access:
<ol>
<li>Copy the <strong>SAML Metadata endpoint</strong>.</li>
<li>In a separate browser window, go to the SAML Metadata endpoint (<code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/sso/saml/xxx/saml-metadata</code>).</li>
<li>Save the page as <code>access_saml_metadata.xml</code>.</li>
</ol>
</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="3-complete-aws-configuration"><ol start="3">
<li>Complete AWS configuration</li>
</ol></h2>
<ol>
<li>
<p>Return to the <strong>IAM Identity Center</strong> &gt; <strong>Settings</strong> &gt; <strong>Change identity source</strong> tab.</p>
</li>
<li>
<p>Under <strong>IdP SAML metadata</strong>, upload your <code>access_saml_metadata.xml</code> file.</p>
</li>
<li>
<p>Select <strong>Next</strong> to review settings, type <strong>ACCEPT</strong> and select <strong>Change identity source</strong> to confirm changes.</p>
</li>
<li>
<p>Confirm that <strong>Provisioning</strong> is set to <em>Manual</em>.</p>
</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/4869.md")
</aside>
<h2 id="4-test-the-integration"><ol start="4">
<li>Test the integration</li>
</ol></h2>
<p>To test the connection, go to your <strong>AWS access portal URL</strong>. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</p>
