<p>This page provides generic instructions for setting up a SaaS application in Cloudflare Access using the OpenID Connect (OIDC) authentication protocol.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to the account of the SaaS application</li>
</ul>
<h2 id="1-get-saas-application-url"><ol>
<li>Get SaaS application URL</li>
</ol></h2>
<p>In your SaaS application account, obtain the <strong>Redirect URL</strong> (also known as the callback URL). This is the SaaS endpoint where users are redirected to after they authenticate with Cloudflare Access.</p>
<p>Some SaaS applications provide the Redirect URL after you <a href="#3-configure-sso-in-your-saas-application">configure the SSO provider</a>.</p>
<h2 id="2-add-your-application-to-access"><ol start="2">
<li>Add your application to Access</li>
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
<p>Select your <strong>Application</strong> from the drop-down menu. If your application is not listed, enter a custom name in the <strong>Application</strong> field and select the textbox that appears below.</p>
</li>
<li>
<p>Select <strong>OIDC</strong>.</p>
</li>
<li>
<p>Select <strong>Add application</strong>.</p>
</li>
<li>
<p>In <strong>Scopes</strong>, select the user attributes that you want Access to send in the ID token. For more information about configuring OIDC scopes and claims, refer to <a href="#oidc-claims">OIDC claims</a>.</p>
</li>
<li>
<p>In <strong>Redirect URLs</strong>, enter the callback URL obtained from the SaaS application.</p>
</li>
<li>
<p>(Optional) Enable <a href="https://www.oauth.com/oauth2-servers/pkce/">Proof of Key Exchange (PKCE)</a> if the protocol is supported by your IdP. PKCE will be performed on all login attempts.</p>
</li>
<li>
<p>Copy the following values to input into your SaaS application. Different SaaS applications may require different sets of input values.</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client secret</td>
<td>Credential used to authorize Access as an SSO provider</td>
</tr>
<tr>
<td>Client ID</td>
<td>Unique identifier for this Access application</td>
</tr>
<tr>
<td>Configuration endpoint</td>
<td>If supported by your SaaS application, you can configure OIDC using this endpoint instead of manually entering the URLs listed below. <br/> <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/sso/oidc/&lt;client-id&gt;/.well-known/openid-configuration</code></td>
</tr>
<tr>
<td>Issuer</td>
<td>Base URL for this OIDC integration <br/> <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/sso/oidc/&lt;client-id&gt;</code></td>
</tr>
<tr>
<td>Token endpoint</td>
<td>Returns the user's ID token <br/> <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/sso/oidc/&lt;client-id&gt;/token</code></td>
</tr>
<tr>
<td>Authorization endpoint</td>
<td>URL where users authenticate with Access <br/> <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/sso/oidc/&lt;client-id&gt;/authorization</code></td>
</tr>
<tr>
<td>Key endpoint</td>
<td>Returns the current public keys used to <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/">verify the Access JWT</a> <br/> <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/sso/oidc/&lt;client-id&gt;/jwks</code></td>
</tr>
<tr>
<td>User info endpoint</td>
<td>Returns all user claims in JSON format <br/> <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/sso/oidc/&lt;client-id&gt;/userinfo</code></td>
</tr>
</tbody>
</table>
<ol start="11">
<li></li>
</ol>
<p>Under <strong>Access policies</strong>, add an existing policy or <a href="/cloudflare-one/access-controls/policies/policy-management/">create a new policy</a> to control who can connect to your application. All Access applications are deny by default -- a user must match an Allow policy before they are granted access.</p>
<ol start="12">
<li></li>
</ol>
<p>Configure how users will authenticate:</p>
<ol>
<li>
Select the [identity providers](/cloudflare-one/integrations/identity-providers/) you want to enable for your application.
</li>
<li>
(Recommended) If you plan to only allow access via a single IdP, turn on **Apply instant authentication**. End users will not be shown the [Cloudflare Access login page](/cloudflare-one/reusable-components/custom-pages/access-login-page/). Instead, Cloudflare will redirect users directly to your SSO login event.
</li>
<li> (Optional) Turn on  <b>Authenticate with Cloudflare One Client</b> to allow users to authenticate to the application using their <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/"> Cloudflare One Client session identity</a>. </li>
</ol>
<ol start="13">
<li>
<p>(Optional) Go to <strong>Additional settings</strong> to customize the application experience:</p>
<ul>
<li><strong>App Launcher customization</strong>: Configure how this application appears to users in the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a>. If <strong>Show application in App Launcher</strong> is enabled, then you must enter an <strong>App Launcher URL</strong>. The App Launcher URL is provided by the SaaS application. It may match the base URL portion of <strong>Redirect URL</strong> (<code>https://&lt;INSTANCE-NAME&gt;.example-app.com</code>) but could be a different value.</li>
<li></li>
</ul>
</li>
</ol>
<p><strong>Custom block pages</strong>: Choose what users will see when they are denied access to the application.</p>
<ul>
<li><strong>Cloudflare default</strong>: Reload the <a href="/cloudflare-one/reusable-components/custom-pages/access-login-page/">login page</a> and display a block message below the Cloudflare Access logo. The default message is <code>That account does not have access</code>, or you can enter a custom message.</li>
<li><strong>Redirect URL</strong>: Redirect to the specified website.</li>
<li><strong>Custom page template</strong>: Display a <a href="/cloudflare-one/reusable-components/custom-pages/access-block-page/">custom block page</a> hosted in Cloudflare One.</li>
</ul>
<ol start="14">
<li>Select <strong>Create</strong>.</li>
</ol>
<h2 id="3-configure-sso-in-your-saas-application"><ol start="3">
<li>Configure SSO in your SaaS application</li>
</ol></h2>
<p>Next, configure your SaaS application to require users to log in through Cloudflare Access. Refer to your SaaS application documentation for instructions on how to configure a third-party OIDC SSO provider.</p>
<h2 id="4-test-the-integration"><ol start="4">
<li>Test the integration</li>
</ol></h2>
<p>Open an incognito browser window and go to the SaaS application's login URL. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</p>
<h2 id="oidc-claims">OIDC claims</h2>
<p>OIDC claims refer to the user identity characteristics that Cloudflare Access shares with your OIDC SaaS application upon successful authentication. An OIDC scope defines a set of OIDC claims. By default, Cloudflare Access passes all <a href="https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims">standard claims</a> that are included in the <code>openid</code>, <code>email</code>, <code>profile</code>, and <code>groups</code> scopes (if available).</p>
<table>
<thead>
<tr>
<th>Scope</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>openid</code></td>
<td>Includes a unique identifier for the user (required).</td>
</tr>
<tr>
<td><code>email</code></td>
<td>Includes the user's email address.</td>
</tr>
<tr>
<td><code>profile</code></td>
<td>Includes the user's name and all custom OIDC claims from the IdP.</td>
</tr>
<tr>
<td><code>groups</code></td>
<td>Include the user's IdP group membership.</td>
</tr>
</tbody>
</table>
<p>In your Access application, you can configure the OIDC scopes and claims that Access sends to the SaaS provider. For example, you can remove the <code>groups</code> scope if your SaaS application does not need to receive user group information.</p>
<h3 id="filter-groups">Filter groups</h3>
<p>In <strong>Group filter regex</strong>, you can enter a regular expression to define the identity provider groups that you want to include in the <code>groups</code> scope. For example, if you enter the expression <code>(^TEAM-Engineering-.$)|(^TEAM-Product-.$)</code>, only groups with names like TEAM-Engineering-A or TEAM-Product-B would get passed to the SaaS application.</p>
<h3 id="add-claims">Add claims</h3>
<p>To add additional OIDC claims onto the ID token sent to your SaaS application, configure the following fields for each claim:</p>
<pre><code>- **Name**: OIDC claim name&#10;- **Scope**: Select the OIDC scope where this claim should be included. In most cases, we recommend selecting `profile` since it already includes other custom claims from the IdP.&#10;- **IdP claim**: The identity provider value that should map to this OIDC claim. You can select any [SAML attribute](/cloudflare-one/integrations/identity-providers/generic-saml/#saml-headers-and-attributes) or [OIDC claim](/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims) that was configured in a Zero Trust IdP integration.&#10;- **Required**: If a claim is marked as required but is not provided by an IdP, Cloudflare will fail the authentication request and show an error page.&#10;- **Add per IdP claim**: (Optional) If you turned on multiple identity providers for the SaaS application, you can choose different attribute mappings for each IdP. These values will override the parent **IdP claim**.&#10;</code></pre>
<h2 id="advanced-settings">Advanced settings</h2>
<h3 id="access-token-lifetime">Access token lifetime</h3>
<p>The OIDC Access token authorizes users to connect to the SaaS application through Cloudflare Access. You can set an <strong>Access token lifetime</strong> to determine the window in which the token can be used to establish authentication with the SaaS application — if it expires, the user must re-authenticate through Cloudflare Access. To balance security and user convenience, Cloudflare recommends configuring a short Access token lifetime in conjunction with a longer <strong>Refresh token lifetime</strong> (if supported by your application). When the access token expires, Cloudflare will use the refresh token to obtain a new access token after checking the user's identity against your Access policies. When the refresh token expires, the user will need to log back in to the identity provider. The refresh token lifetime should be less than your <a href="/cloudflare-one/access-controls/access-settings/session-management/">global session duration</a>, otherwise the global session would take precedence.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4866.md")
</aside>
<h3 id="oidc-flows">OIDC flows</h3>
<p>Some SaaS applications require SSO providers to provide tokens to the browser without backend authentication. Access for SaaS supports the following OIDC flows:</p>
<ul>
<li><strong>No additional OIDC flows</strong>: (Default) Recommended unless your application requires additional flows.</li>
<li><strong>Hybrid flows</strong>: Used by applications that require information from the ID token before authenticating the user.</li>
<li><strong>Implicit flows</strong>: (Not recommended) Typically used by frontend applications that cannot store secrets and which do not support <strong>PKCE without client secret</strong>.</li>
</ul>
<p>Cloudflare allows various <code>response_type</code> values in the authorization request depending on the selected flow. For example, the implicit flow allows Cloudflare to return the ID token, Access token, or both the ID token and Access token from the Authorization endpoint.</p>
<table>
<thead>
<tr>
<th><code>response_type</code> values</th>
<th>Default flow</th>
<th>Hybrid flow</th>
<th>Implicit flow</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>code</code></td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td><code>id_token</code></td>
<td>❌</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><code>token</code></td>
<td>❌</td>
<td>✅</td>
<td>✅</td>
</tr>
</tbody>
</table>
<p>To include <code>id_token</code> in the authorization request, turn on <strong>Return ID Token from Authorization Endpoint</strong>. To include <code>token</code>, turn on <strong>Return Access Token from Authorization Endpoint</strong></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4865.md")
</aside>
