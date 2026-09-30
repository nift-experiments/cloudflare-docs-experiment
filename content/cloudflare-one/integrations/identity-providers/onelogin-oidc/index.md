<p>OneLogin provides SSO identity management. Cloudflare Access supports OneLogin as an OIDC identity provider.</p>
<h2 id="set-up-onelogin-as-an-oidc-provider">Set up OneLogin as an OIDC provider</h2>
<h3 id="1-create-an-application-in-onelogin"><ol>
<li>Create an application in OneLogin</li>
</ol></h3>
<ol>
<li>
<p>Log in to your OneLogin admin portal.</p>
</li>
<li>
<p>Go to <strong>Applications</strong> &gt; <strong>Applications</strong> and select <strong>Add App</strong>.</p>
</li>
<li>
<p>Search for <code>OIDC</code> and select <strong>OpenId Connect (OIDC)</strong> by OneLogin, Inc.</p>
</li>
<li>
<p>In <strong>Display Name</strong>, enter any name for your application. Select <strong>Save</strong>.</p>
</li>
<li>
<p>Next, go to <strong>Configuration</strong>. In the <strong>Redirect URI</strong> field, enter the following URL:</p>
</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="6">
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p>Go to <strong>Access</strong> and choose the <strong>Roles</strong> that can access this application. Select <strong>Save</strong>.</p>
</li>
<li>
<p>Go to <strong>SSO</strong> and select <strong>Show client secret</strong>.</p>
</li>
<li>
<p>Copy the <strong>Client ID</strong> and <strong>Client Secret</strong>.</p>
</li>
</ol>
<h3 id="2-add-onelogin-to-cloudflare-one"><ol start="2">
<li>Add OneLogin to Cloudflare One</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</p>
</li>
<li>
<p>Select <strong>OneLogin</strong>.</p>
</li>
<li>
<p>Fill in the following information:</p>
<ul>
<li><strong>Name</strong>: Name your identity provider.</li>
<li><strong>App ID</strong>: Enter your OneLogin client ID.</li>
<li><strong>Client secret</strong>: Enter your OneLogin client secret.</li>
<li><strong>OneLogin account URL</strong>: Enter your OneLogin domain, for example <code>https://&lt;your-domain&gt;.onelogin.com</code>.</li>
</ul>
</li>
<li>
<p>(Optional) To enable SCIM, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#synchronize-users-and-groups">Synchronize users and groups</a>.</p>
</li>
<li>
<p>(Optional) Under <strong>Optional configurations</strong>, enter <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims">custom OIDC claims</a> that you wish to add to your user's identity.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>To test that your connection is working, go to <strong>Integrations</strong> &gt; <strong>Identity providers</strong> and select <strong>Test</strong> next to OneLogin.</p>
<h2 id="example-api-config">Example API Config</h2>
<pre><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;client_id&quot;: &quot;&lt;your client id&gt;&quot;,&#10;		&quot;client_secret&quot;: &quot;&lt;your client secret&gt;&quot;,&#10;		&quot;onelogin_account&quot;: &quot;https://mycompany.onelogin.com&quot;&#10;	},&#10;	&quot;type&quot;: &quot;onelogin&quot;,&#10;	&quot;name&quot;: &quot;my example idp&quot;&#10;}&#10;</code></pre>
