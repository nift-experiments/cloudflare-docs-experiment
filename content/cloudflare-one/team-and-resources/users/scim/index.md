<p>System for Cross-domain Identity Management (SCIM) is an open standard protocol that allows identity providers to synchronize user identity information with cloud applications and services. After configuring SCIM, user identities that you create, edit, or delete in the identity provider are automatically updated across all supported applications. This makes it easier for IT admins to onboard new users, update their groups and permissions, and revoke access in the event of an employee termination or security breach.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5954.md")
</aside>
<h2 id="supported-identity-providers">Supported identity providers</h2>
<p>Cloudflare One supports SCIM provisioning for all SAML and OIDC identity providers that use SCIM version <code>2.0</code>.</p>
<h2 id="sync-users-and-groups-in-zero-trust-policies">Sync users and groups in Zero Trust policies</h2>
<p>Cloudflare Access can automatically deprovision users from Zero Trust after they are deactivated in the identity provider and display synchronized group names in the Access and Gateway policy builders. Cloudflare does not provision new users in Zero Trust when they are added to the identity provider -- users must first register a device with the Cloudflare One Client or authenticate to an Access application.</p>
<p>SCIM affects Access and Gateway policy evaluation differently.</p>
<p>Access evaluates a user's identity and group membership from the SAML assertion or OIDC token returned by the identity provider during authentication. SCIM provides readable group names in the Access policy builder, but Access does not use SCIM group membership to evaluate a login. If you turn on <strong>Enable user deprovisioning</strong>, removing a user from the SCIM application revokes their active Access sessions. You can also configure SCIM to revoke sessions after group membership changes. Access evaluates the updated identity provider data when the user authenticates again.</p>
<p>Gateway evaluates identity-based policies against the <a href="/cloudflare-one/team-and-resources/users/users/">User Registry identity</a>. SCIM updates this identity when users or group memberships change, without waiting for the user to authenticate again. Cloudflare One Client device profiles use the same synchronized identity.</p>
<p>To set up SCIM for Zero Trust, refer to our <a href="/cloudflare-one/integrations/identity-providers/">SSO integration</a> guides.</p>
<h2 id="common-provider-specific-issues">Common provider-specific issues</h2>
<p>SCIM behavior depends on the identity provider configuration as well as Cloudflare.</p>
<p>Common issues include:</p>
<ul>
<li><strong>Okta</strong>: User sync and group sync are separate. Make sure <strong>Push Groups</strong> is configured if you expect groups to appear in Zero Trust policies.</li>
<li><strong>Microsoft Entra ID</strong>: Group sync only occurs for groups included in the provisioning scope. The <code>userName</code> attribute should match the user's email address in Cloudflare One.</li>
</ul>
<p>If users appear but groups do not, verify the IdP-side SCIM app first before troubleshooting Cloudflare policy behavior.</p>
