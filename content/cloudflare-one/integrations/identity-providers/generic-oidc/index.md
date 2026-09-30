<p>Cloudflare Access has a generic OpenID Connect (OIDC) connector to help you integrate IdPs not already set in Access.</p>
<h2 id="1-create-an-application-in-your-identity-provider"><ol>
<li>Create an application in your identity provider</li>
</ol></h2>
<ol>
<li>
<p>Visit your identity provider and create a client/app.</p>
</li>
<li>
<p>When creating a client/app, your IdP may request an <strong>authorized redirect URI</strong>. Enter the following URL:</p>
</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="3">
<li>
<p>Copy the content of these fields:</p>
<ul>
<li>Client ID</li>
<li>Client secret</li>
<li>Auth URL: The <code>authorization_endpoint</code> URL of your IdP</li>
<li>Token URL: The <code>token_endpoint</code> URL of your IdP</li>
<li>Certificate URL: The <code>jwks_uri</code> endpoint of your IdP to allow the IdP keys to sign the tokens</li>
</ul>
<p>You can find these values on your identity provider's <strong>OIDC discovery endpoint</strong>. Some providers call this the &quot;well-known URL&quot;.</p>
</li>
</ol>
<h2 id="2-add-an-oidc-provider-to-cloudflare-one"><ol start="2">
<li>Add an OIDC provider to Cloudflare One</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5072.md")
</div></div>
<h2 id="3-test-the-connection"><ol start="3">
<li>Test the connection</li>
</ol></h2>
<p>To test that your connection is working, go to <strong>Authentication</strong> &gt; <strong>Login methods</strong> and select <strong>Test</strong> next to the login method you want to test. On success, a confirmation screen displays.</p>
<h2 id="synchronize-users-and-groups">Synchronize users and groups</h2>
<p>The generic OIDC integration allows you to synchronize user groups and automatically deprovision users using <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM</a>.</p>
<p>SCIM affects Access and Gateway policy evaluation differently.</p>
<p>Access evaluates a user's identity and group membership from the SAML assertion or OIDC token returned by the identity provider during authentication. SCIM provides readable group names in the Access policy builder, but Access does not use SCIM group membership to evaluate a login. If you turn on <strong>Enable user deprovisioning</strong>, removing a user from the SCIM application revokes their active Access sessions. You can also configure SCIM to revoke sessions after group membership changes. Access evaluates the updated identity provider data when the user authenticates again.</p>
<p>Gateway evaluates identity-based policies against the <a href="/cloudflare-one/team-and-resources/users/users/">User Registry identity</a>. SCIM updates this identity when users or group memberships change, without waiting for the user to authenticate again. Cloudflare One Client device profiles use the same synchronized identity.</p>
<h3 id="prerequisites">Prerequisites</h3>
<p>Your identity provider must support SCIM version 2.0.</p>
<h3 id="1-enable-scim-in-cloudflare-one"><ol>
<li>Enable SCIM in Cloudflare One</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Find the IdP integration and select <strong>Edit</strong>.</p>
</li>
<li>
<p>Turn on <strong>Enable SCIM</strong>.</p>
</li>
<li>
<p>(Optional) Configure the following settings:</p>
</li>
</ol>
<ul>
<li><strong>Enable user deprovisioning</strong>: <a href="/cloudflare-one/access-controls/access-settings/session-management/#per-user">Revoke a user's active session</a> when they are removed from the SCIM application in IdP. This will invalidate all active Access sessions and prompt for reauthentication for any <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">Cloudflare One Client session policies</a>.</li>
<li><strong>Remove user seat on deprovision</strong>: <a href="/cloudflare-one/team-and-resources/users/seat-management/">Remove a user's seat</a> from your Cloudflare One account when they are removed from the SCIM application in IdP.</li>
<li><strong>SCIM identity update behavior</strong>: Choose what happens in Cloudflare One when the user's identity updates in IdP.
<ul>
<li><em>Automatic identity updates</em>: Automatically update the <a href="/cloudflare-one/team-and-resources/users/users/">User Registry identity</a> when IdP sends an updated identity or group membership through SCIM. This identity is used for Gateway policies and Cloudflare One Client <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profiles</a>; Access will read the user's updated identity when they reauthenticate.</li>
<li><em>Group membership change reauthentication</em>: <a href="/cloudflare-one/access-controls/access-settings/session-management/#per-user">Revoke a user's active session</a> when their group membership changes in IdP. This will invalidate all active Access sessions and prompt for reauthentication for any <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">Cloudflare One Client session policies</a>. Access will read the user's updated group membership when they reauthenticate.</li>
<li><em>No action</em>: Update the user's identity the next time they reauthenticate to Access or the Cloudflare One Client.</li>
</ul>
</li>
</ul>
<ol start="5">
<li>
<p>Select <strong>Regenerate Secret</strong>. Copy the <strong>SCIM Endpoint</strong> and <strong>SCIM Secret</strong>. You will need to enter these values into IdP.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>The SCIM secret never expires, but you can manually regenerate the secret at any time.</p>
<h3 id="2-configure-scim-in-the-idp"><ol start="2">
<li>Configure SCIM in the IdP</li>
</ol></h3>
<p>Setup instructions vary depending on the identity provider. In your identity provider, you will either need to edit the <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#1-create-an-application-in-your-identity-provider">original SSO application</a> or create a new SCIM application. Refer to your identity provider's documentation for more details. For example instructions, refer to our <a href="/cloudflare-one/integrations/identity-providers/okta/#synchronize-users-and-groups">Okta</a> or <a href="/cloudflare-one/integrations/identity-providers/jumpcloud-saml/#synchronize-users-and-groups">Jumpcloud</a> guides.</p>
<h4 id="idp-groups">IdP groups</h4>
<p>If you would like to build policies based on IdP groups:</p>
<ul>
<li>Ensure that your IdP sends a <code>groups</code> field. The naming must match exactly (case insensitive). All other values will be sent as a OIDC claim.</li>
<li>If your IdP requires a new SCIM application, ensure that its groups match the groups in the <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#1-create-an-application-in-your-identity-provider">original SSO application</a>. Matching the groups keeps the Gateway identity synchronized with the groups that the IdP returns when the user authenticates to Access.</li>
</ul>
<h3 id="3-verify-scim-provisioning"><ol start="3">
<li>Verify SCIM provisioning</li>
</ol></h3>
<p>To check if user identities were updated in Cloudflare One, view your <a href="/cloudflare-one/insights/logs/dashboard-logs/scim-logs/">SCIM provisioning logs</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5068.md")
</aside>
<h2 id="optional-configurations">Optional configurations</h2>
<h3 id="custom-oidc-claims">Custom OIDC claims</h3>
<p>All OIDC IdP integrations support the use of custom OIDC claims. Once configured, Access will add the claims to the <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/">Access JWT</a> for consumption by your origin services. You can reference the custom OIDC claims in <a href="/cloudflare-one/access-controls/policies/">Access policies</a> and <a href="/cloudflare-one/traffic-policies/identity-selectors/#oidc-claims">Gateway policies</a>, offering a means to control user access to applications based on custom identity attributes.</p>
<p>To add a custom OIDC claim to an IdP integration:</p>
<ol>
<li>In your identity provider, ensure that the custom claim is included in your OIDC ID token.</li>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</li>
<li>Under <strong>Your identity providers</strong>, find your identity provider and select <strong>Edit</strong>.</li>
<li>Under <strong>OIDC Claims</strong>, enter the name of your custom claim (for example, <code>oid</code>).</li>
<li>Select <strong>Save</strong>.</li>
<li>Select <strong>Test</strong> and verify that the custom claim appears in <code>oidc_fields</code>. For example,</li>
</ol>
<pre><code class="language-json">	&quot;oidc_fields&quot;: {&#10;		&quot;oid&quot;: &quot;54eb1ed2-7150-44e6-bbe4-ead24c132fd4&quot;&#10;	},&#10;</code></pre>
<p>You can now build an Access policy for the custom claim using the <strong>OIDC Claim</strong> or <strong>IdP OIDC Claim</strong> selector. You can also use custom OIDC claims as <a href="/cloudflare-one/traffic-policies/identity-selectors/#oidc-claims">identity-based selectors in Gateway policies</a>. The custom claim will be passed to origins behind Access in a <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/#custom-saml-attributes-and-oidc-claims">JWT</a>.</p>
<h4 id="email-claim">Email claim</h4>
<p>You can specify a custom <strong>Email claim</strong> name that Access will use to identify user emails. This is useful if your IdP does not return the standard <code>email</code> claim in the OIDC ID token.</p>
<h4 id="multi-record-oidc-claims">Multi-record OIDC claims</h4>
<p>Cloudflare Access extends support for multi-record OIDC claims. These claims are parsed out and can be individually referenced in policies. This feature enables granular access control and precise user authorization in applications.</p>
<p>Cloudflare Access does not support partial OIDC claim value references or OIDC scopes.</p>
<h2 id="supported-algorithms-for-generic-oidc-tokens">Supported algorithms for generic OIDC tokens</h2>
<p>Cloudflare supports the following algorithms for verifying generic OIDC tokens:</p>
<ul>
<li>RS512</li>
<li>RS256</li>
<li>PS512</li>
<li>ES256</li>
<li>ES384</li>
<li>ES512</li>
</ul>
