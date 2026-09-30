<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="access-to-area-1">Access to Area 1</h3>
@markup("md", "content/.markup/bodies/4871.md")
</aside>
<p><a href="https://www.cloudflare.com/products/zero-trust/email-security/">Cloudflare Area 1</a> is an email security platform that protects your organization's inbox from phishing, spam, and other malicious messages. This guide covers how to configure Area 1 as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to your Area 1 account</li>
<li>Your user's email in Area 1 matches their email in Cloudflare One</li>
</ul>
<h2 id="1-add-area-1-to-cloudflare-one"><ol>
<li>Add Area 1 to Cloudflare One</li>
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
<p>In the <strong>Application</strong> field, enter <code>Area 1</code> and select <strong>Area 1</strong>. (Area 1 is not currently listed in the default drop-down menu.)</p>
</li>
<li>
<p>Enter the following values for your application configuration:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Entity ID</strong></td>
<td><code>https://horizon.area1security.com</code></td>
</tr>
<tr>
<td><strong>Assertion Consumer Service URL</strong></td>
<td><code>https://horizon.area1security.com/api/users/saml</code></td>
</tr>
<tr>
<td><strong>Name ID Format</strong></td>
<td><em>Email</em></td>
</tr>
</tbody>
</table>
<ol start="6">
<li>
<p>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</p>
</li>
<li>
<p>Save the application.</p>
</li>
</ol>
<h2 id="2-configure-sso-for-area-1"><ol start="2">
<li>Configure SSO for Area 1</li>
</ol></h2>
<p>Finally, you will need to configure Area 1 to allow users to log in through Cloudflare Access.</p>
<ol>
<li>
<p>In your <a href="https://horizon.area1security.com/">Area 1 portal</a>, go to <strong>Settings</strong> &gt; <strong>SSO</strong>.</p>
</li>
<li>
<p>Turn on <strong>Single Sign On</strong>.</p>
</li>
<li>
<p>(Optional) To require users to sign in through Access, set <strong>SSO Enforcement</strong> to <em>All</em>. When SSO is enforced, users will no longer be able to sign in with their Area 1 credentials.</p>
</li>
<li>
<p>In <strong>SAML SSO Domain</strong>, enter <code>&lt;your-team-name&gt;.cloudflareaccess.com</code>.</p>
</li>
<li>
<p>Get your Metadata XML file:</p>
<ol>
<li>In Cloudflare One, copy the <strong>SSO Endpoint</strong> for your application.</li>
</ol>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/applications/saas-sso-endpoint.png" alt="Copy SSO settings for a SaaS application from Cloudflare One" /></p>
<ol start="2">
<li>
<p>In a new browser tab, paste the <strong>SSO Endpoint</strong> and append <code>/saml-metadata</code> to the end of the URL. For example, <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/sso/saml/&lt;app-id&gt;/saml-metadata</code>.</p>
</li>
<li>
<p>Copy the resulting metadata.</p>
</li>
<li>
<p>Return to the Area 1 portal and paste the metadata into <strong>Metadata XML</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/applications/area1-sso-config.png" alt="Configure SSO in the Area 1 portal" /></p>
<ol start="7">
<li>Select <strong>Update Settings</strong>.</li>
</ol>
<p>If you added the application to your App Launcher, you can test the integration by going to <code>&lt;your-team-name&gt;.cloudflareaccess.com</code>.</p>
