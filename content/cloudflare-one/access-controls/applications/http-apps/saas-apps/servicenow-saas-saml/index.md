<p>This guide covers how to configure <a href="https://docs.servicenow.com/bundle/washingtondc-platform-security/page/integrate/single-sign-on/task/t_CreateASAML2Upd1SSOConfigMultiSSO.html">ServiceNow</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a ServiceNow account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>ServiceNow</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>https://&lt;INSTANCE-NAME&gt;.service-now.com</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://&lt;INSTANCE-NAME&gt;.service-now.com/navpage.do</code></li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>SAML Metadata endpoint</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-add-the-multiple-provider-single-sign-on-installer-plugin-to-servicenow"><ol start="2">
<li>Add the Multiple Provider Single Sign-On Installer Plugin to ServiceNow</li>
</ol></h2>
<ol>
<li>In ServiceNow, select <strong>All</strong>.</li>
<li>In the search bar, enter <code>System Applications</code>, and under <strong>All Available Applications</strong>, select <strong>All</strong>.</li>
<li>In the search bar, enter <code>Integration - Multiple Provider Single Sign-On Installer</code>.</li>
<li>Select <strong>Install</strong>.</li>
<li>Ensure that <strong>Install now</strong> is selected, and select <strong>Install</strong>.</li>
</ol>
<h2 id="3-add-and-test-a-saml-sso-provider-in-servicenow"><ol start="3">
<li>Add and Test a SAML SSO provider in ServiceNow</li>
</ol></h2>
<ol>
<li>Select <strong>All</strong>.</li>
<li>In the search bar enter <code>Multi-Provider SSO</code>, and select <strong>Identity Providers</strong>.</li>
<li>Select <strong>New</strong> &gt; <strong>SAML</strong>.</li>
<li>In the pop-up, ensure that <strong>URL</strong> is selected.</li>
<li>Paste the <strong>SAML Metadata endpoint</strong> from application configuration in Cloudflare One in the empty field.</li>
<li>Select <strong>Import</strong>.</li>
<li>(Optional) Change the <strong>Name</strong> field to a more recognizable name.</li>
<li>Turn off <strong>Sign AuthnRequest</strong>.</li>
<li>Select <strong>Update</strong>.</li>
<li>In the pop-up, select <strong>Cancel</strong> and then <strong>&gt;</strong>.</li>
<li>Select the <strong>Name</strong> of the configuration you just completed.</li>
<li>Select <strong>Test Connection</strong>.</li>
<li>If the test succeeds, select <strong>Activate</strong>.</li>
</ol>
