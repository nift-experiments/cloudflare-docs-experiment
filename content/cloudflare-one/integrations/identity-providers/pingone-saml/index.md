<p>The PingOne cloud platform from PingIdentity provides SSO identity management. Cloudflare Access supports PingOne as a SAML identity provider.</p>
<h2 id="set-up-pingone-as-a-saml-provider">Set up PingOne as a SAML provider</h2>
<h2 id="1-create-an-application-in-pingone"><ol>
<li>Create an application in PingOne</li>
</ol></h2>
<ol>
<li>
<p>In your PingIdentity environment, go to <strong>Connections</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Add Application</strong>.</p>
</li>
<li>
<p>Enter an <strong>Application Name</strong>.</p>
</li>
<li>
<p>Select <strong>SAML Application</strong>.</p>
</li>
<li>
<p>Select <strong>Configure</strong>.</p>
</li>
<li>
<p>To fill in your Cloudflare Access metadata:</p>
<ol>
<li>Select <strong>Import from URL</strong>.</li>
<li>Set the <strong>Import URL</strong> to:</li>
</ol>
</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/saml-metadata&#10;</code></pre>
<p>where <code>&lt;your-team-name&gt;</code> is your Cloudflare One <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5027.md")
</div>. 3. Select **Import**. 4. **Save** the configuration.
<ol start="7">
<li>
<p>In the <strong>Configuration</strong> tab, select <strong>Download metadata</strong> and save the XML metadata file. This file will be used in a later step to add PingOne to Cloudflare One.</p>
</li>
<li>
<p>In the <strong>Attribute Mappings</strong> tab, add the following required attributes (case sensitive) and select <strong>Save</strong>.</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Application attribute</th>
<th>Outgoing value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>email</code></td>
<td>Email Address</td>
</tr>
<tr>
<td><code>givenName</code></td>
<td>Given Name</td>
</tr>
<tr>
<td><code>surName</code></td>
<td>Family Name</td>
</tr>
</tbody>
</table>
<p>These <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#saml-attributes">SAML attributes</a> tell Cloudflare Access who the user is.</p>
<ol start="9">
<li>Set the application to <strong>Active</strong>.</li>
</ol>
<h3 id="2-add-pingone-to-cloudflare-one"><ol start="2">
<li>Add PingOne to Cloudflare One</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</p>
</li>
<li>
<p>Select <strong>SAML</strong>.</p>
</li>
<li>
<p>Upload your PingOne XML metadata file.</p>
</li>
<li>
<p>(Optional) To enable SCIM, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#synchronize-users-and-groups">Synchronize users and groups</a>.</p>
</li>
<li>
<p>(Optional) Under <strong>Optional configurations</strong>, configure <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#optional-configurations">additional SAML options</a>.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>You can now <a href="/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one">test your connection</a> and create <a href="/cloudflare-one/access-controls/policies/">Access policies</a> based on the configured login method and SAML attributes.</p>
