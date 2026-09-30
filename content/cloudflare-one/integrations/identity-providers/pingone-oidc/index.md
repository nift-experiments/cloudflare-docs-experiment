<p>The PingOne cloud platform from PingIdentity provides SSO identity management. Cloudflare Access supports PingOne as an OIDC identity provider.</p>
<h2 id="set-up-pingone-as-an-oidc-provider">Set up PingOne as an OIDC provider</h2>
<h3 id="1-create-an-application-in-pingone"><ol>
<li>Create an application in PingOne</li>
</ol></h3>
<ol>
<li>In your PingIdentity environment, go to <strong>Connections</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Add Application</strong>.</li>
<li>Enter an <strong>Application Name</strong>.</li>
<li>Select <strong>OIDC Web App</strong> and then <strong>Save</strong>.</li>
<li>Select <strong>Resource Access</strong> and add the <strong>email</strong> and <strong>profile</strong> scopes.</li>
<li>In the <strong>Configuration</strong> tab, select <strong>General</strong>.</li>
<li>Copy the <strong>Client ID</strong>, <strong>Client Secret</strong>, and <strong>Environment ID</strong> to a safe place. These IDs will be used in a later step to add PingOne to Cloudflare One.</li>
<li>In the <strong>Configuration</strong> tab, select the pencil icon.</li>
<li>In the <strong>Redirect URIs</strong> field, enter the following URL:</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="10">
<li>Select <strong>Save</strong>.</li>
</ol>
<h3 id="2-add-pingone-to-cloudflare-one"><ol start="2">
<li>Add PingOne to Cloudflare One</li>
</ol></h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</li>
<li>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</li>
<li>Select <strong>PingOne</strong>.</li>
<li>Input the <strong>Client ID</strong>, <strong>Client Secret</strong>, and <strong>Environment ID</strong> generated previously.</li>
<li>(Optional) Enable <a href="https://www.oauth.com/oauth2-servers/pkce/">Proof of Key Exchange (PKCE)</a>. PKCE will be performed on all login attempts.</li>
<li>(Optional) To enable SCIM, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#synchronize-users-and-groups">Synchronize users and groups</a>.</li>
<li>(Optional) Under <strong>Optional configurations</strong>, enter <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims">custom OIDC claims</a> that you wish to add to your users' identity.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>You can now <a href="/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one">test your connection</a> and create <a href="/cloudflare-one/access-controls/policies/">Access policies</a> based on the configured login method.</p>
<h2 id="example-api-configuration">Example API configuration</h2>
<pre><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;client_id&quot;: &quot;&lt;your client id&gt;&quot;,&#10;		&quot;client_secret&quot;: &quot;&lt;your client secret&gt;&quot;,&#10;		&quot;ping_env_id&quot;: &quot;&lt;your ping environment id&gt;&quot;&#10;	},&#10;	&quot;type&quot;: &quot;ping&quot;,&#10;	&quot;name&quot;: &quot;my example idp&quot;&#10;}&#10;</code></pre>
