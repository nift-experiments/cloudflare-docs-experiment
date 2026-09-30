<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5057.md")
</aside>
<p>You can integrate a Google Workspace (formerly G Suite) account with Cloudflare Access. Unlike the instructions for <a href="/cloudflare-one/integrations/identity-providers/google/">generic Google authentication</a>, the steps below will allow you to pull group membership information from your Google Workspace account.</p>
<p>Once integrated, users will log in with their Google Workspace credentials to reach resources protected by Cloudflare Access or to enroll their device into Cloudflare Gateway.</p>
<p>You do not need to be a Google Cloud Platform user to integrate Google Workspace as an identity provider with Cloudflare One. You will only need to open the Google Cloud Platform to configure IdP integration settings.</p>
<h2 id="set-up-google-workspace-as-an-identity-provider">Set up Google Workspace as an identity provider</h2>
<h3 id="1-configure-google-workspace"><ol>
<li>Configure Google Workspace</li>
</ol></h3>
<ol>
<li>
<p>Log in to the Google Cloud Platform <a href="https://console.cloud.google.com/">console</a>. This is separate from your Google Workspace console.</p>
</li>
<li>
<p>A Google Cloud project is required to enable Google Workspace APIs. If you do not already have a Google Cloud project, go to <strong>IAM &amp; Admin</strong> &gt; <strong>Create Project</strong>. Name the project and select <strong>Create</strong>.</p>
</li>
<li>
<p>Go to <strong>APIs &amp; Services</strong> and select <strong>Enable APIs and Services</strong>. The API Library will load.</p>
</li>
<li>
<p>In the API Library, search for <code>admin</code> and select <strong>Admin SDK API</strong>.</p>
</li>
<li>
<p><strong>Enable</strong> the Admin SDK API.</p>
</li>
<li>
<p>Return to the <strong>APIs &amp; Services</strong> page and go to <strong>Credentials</strong>.</p>
</li>
<li>
<p>Select <strong>Configure Consent Screen</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/google/configure-consent-screen.png" alt="Location to configure a Consent Screen in the Google Cloud Platform console." /></p>
<ol start="8">
<li>
<p>To configure the consent screen:</p>
<ol>
<li>Select <strong>Get Started</strong>.</li>
<li>Enter an <strong>App name</strong> and a <strong>User support email</strong>.</li>
<li>Choose <strong>Internal</strong> as the Audience Type. This Audience Type limits authorization requests to users in your Google Workspace and blocks users who have regular Gmail addresses.</li>
<li>Enter your <strong>Contact Information</strong>. Google Cloud Platform requires an email in your account.</li>
<li>Agree to Google's user data policy and select <strong>Continue</strong>.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
</li>
<li>
<p>The OAuth overview page will load. Select <strong>Create OAuth Client</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/google/create-oauth-client.png" alt="Location to create an OAuth client in the Google Cloud Platform console." /></p>
<ol start="10">
<li>
<p>Choose <em>Web application</em> as the <strong>Application type</strong> and give your OAuth Client ID a name.</p>
</li>
<li>
<p>Under <strong>Authorized JavaScript origins</strong>, in the <strong>URIs</strong> field, enter your team domain:</p>
</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com&#10;</code></pre>
<pre><code>You can find your team name in the [Cloudflare dashboard](https://dash.cloudflare.com) under **Settings** &gt; **Team name and domain** &gt; **Team name**.&#10;</code></pre>
<ol start="12">
<li>Under <strong>Authorized redirect URIs</strong>, in the <strong>URIs</strong> field, enter the following URL:</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<ol start="13">
<li>
<p>After creating the OAuth client, select the OAuth client that you just created. Google will present the <strong>OAuth Client ID</strong> value and <strong>Client secret</strong> value. The client secret field functions like a password and should not be shared. Copy both the <strong>OAuth Client ID</strong> value and <strong>Client secret</strong> value.</p>
</li>
<li>
<p>On your <a href="https://admin.google.com">Google Admin console</a>, go to <strong>Security</strong> &gt; <strong>Access and data control</strong> &gt; <strong>API controls</strong>.</p>
</li>
<li>
<p>In <strong>API Controls</strong>, select <strong>Settings</strong>.</p>
</li>
<li>
<p>Select <strong>Internal apps</strong> and check the box next to <strong>Trust internal apps</strong> to enable this option. The <strong>Trust internal apps</strong> setting is disabled by default and must be enabled for Cloudflare Access to work correctly.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/gsuite/trust-internal-apps.png" alt="Location to trust internal apps in the Google Cloud Platform console." /></p>
<h3 id="2-add-google-workspace-to-cloudflare-one"><ol start="2">
<li>Add Google Workspace to Cloudflare One</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Select <strong>Add new identity provider</strong> and select <strong>Google Workspace</strong>.</p>
</li>
<li>
<p>Input the Client ID (<strong>App ID</strong> in the Cloudflare dashboard) and Client Secret fields generated previously. Additionally, enter the domain of your Google Workspace account.</p>
</li>
<li>
<p>(Optional) Enable <a href="https://www.oauth.com/oauth2-servers/pkce/">Proof of Key Exchange (PKCE)</a>. PKCE will be performed on all login attempts.</p>
</li>
<li>
<p>(Optional) Under <strong>Optional configurations</strong>, enter <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims">custom OIDC claims</a> that you wish to add to your user's identity.</p>
</li>
<li>
<p>Select <strong>Save</strong>. To complete setup, you must visit the generated link. If you are not the Google Workspace administrator, share the link with the administrator.</p>
</li>
<li>
<p>The generated link will prompt you to log in to your Google admin account and to authorize Cloudflare Access to view group information. After allowing permissions, you will see a success page from Cloudflare Access.</p>
</li>
</ol>
<p>To test that your connection is working, go to <strong>Integrations</strong> &gt; <strong>Identity providers</strong> and select <strong>Test</strong> next to Google Workspace. Your user identity and group membership should return.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="scim-provisioning-beta">SCIM Provisioning (Beta)</h3>
@markup("md", "content/.markup/bodies/5056.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="failed-to-fetch-group-information-from-the-identity-provider-error">`Failed to fetch group information from the identity provider` error</h3>
@markup("md", "content/.markup/bodies/5055.md")
</aside>
<h2 id="example-api-configuration">Example API Configuration</h2>
<pre><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;client_id&quot;: &quot;&lt;your client id&gt;&quot;,&#10;		&quot;client_secret&quot;: &quot;&lt;your client secret&gt;&quot;,&#10;		&quot;apps_domain&quot;: &quot;mycompany.com&quot;&#10;	},&#10;	&quot;type&quot;: &quot;google-apps&quot;,&#10;	&quot;name&quot;: &quot;my example idp&quot;&#10;}&#10;</code></pre>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="error-401-deleted-client"><code>Error 401: deleted_client</code></h3>
<p>If you deleted the OAuth client (or the OAuth client expired) in Google, you will receive a <code>Error 401: deleted_client</code> authorization error.</p>
<p>To fix this issue, complete steps 6 through 12 in the <a href="/cloudflare-one/integrations/identity-providers/google/#set-up-google-as-an-identity-provider">Google</a> guide and steps 9 through 15 in the <a href="/cloudflare-one/integrations/identity-providers/google/#set-up-google-as-an-identity-provider">Google Workspace</a> guide.</p>
