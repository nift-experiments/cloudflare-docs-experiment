<p>This guide covers how to configure <a href="https://support.sparkpost.com/docs/my-account-and-profile/sso">SparkPost or SparkPost EU</a> as a SAML application in Cloudflare Zero Trust.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a SparkPost or SparkPost EU account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>SparkPost</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>:
<ul>
<li><code>https://api.sparkpost.com</code> for SparkPost accounts</li>
<li><code>https://api.eu.sparkpost.com</code> for SparkPost EU accounts</li>
<li><code>https://&lt;api-host&gt;</code> for SparkPost accounts with dedicated tenants</li>
</ul>
</li>
<li><strong>Assertion Consumer Service URL</strong>:
<ul>
<li><code>https://api.sparkpost.com/api/v1/users/saml/consume</code> for SparkPost accounts</li>
<li><code>https://api.eu.sparkpost.com/api/v1/users/saml/consume</code> for SparkPost EU accounts</li>
<li><code>https://&lt;api-host&gt;/api/v1/users/saml/consume</code> for SparkPost accounts with dedicated tenants</li>
</ul>
</li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>SAML Metadata endpoint</strong>.</li>
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
<h2 id="3-add-a-saml-sso-provider-to-sparkpost"><ol start="3">
<li>Add a SAML SSO provider to SparkPost</li>
</ol></h2>
<ol>
<li>In SparkPost, select your profile picture &gt; <strong>Account Settings</strong>.</li>
<li>Under <strong>Single Sign-On</strong>, select <strong>Provision SSO</strong>.</li>
<li>Under <strong>Upload your Security Assertion Markup Language (SAML)</strong>, select <strong>select a file</strong> and upload the <code>.xml</code> file you created in step <a href="#2-download-the-metadata-file">2. Download the metadata file</a>.</li>
<li>Select <strong>Provision SSO</strong>.</li>
<li>Select <strong>Enable SSO</strong>.</li>
</ol>
<h2 id="4-add-a-test-user-and-test-the-integration"><ol start="4">
<li>Add a test user and test the integration</li>
</ol></h2>
<ol>
<li>In SparkPost, current users must be deleted and re-invited to use SSO. To create a test user, select your profile picture &gt; <strong>Users</strong> &gt; name of the user &gt; <strong>Delete User</strong>. Then, select <strong>Invite User</strong> and fill in the necessary information. Alternatively, invite a new user. An invitation email will be sent.</li>
<li>Go to the link sent in the invitation email. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</li>
<li>Once SSO is successful, you can turn on SSO for the rest of your current users by deleting and then re-inviting them.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4839.md")
</aside>
