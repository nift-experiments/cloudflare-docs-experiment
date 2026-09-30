<h2 id="overview">Overview</h2>
<p>When you authorize a third-party OAuth application, you grant it permission to access specific Cloudflare resources on your behalf. Cloudflare provides tools to view, manage, and revoke these authorizations at any time.</p>
<h2 id="authorize-a-third-party-application">Authorize a third-party application</h2>
<p>When a third-party application requests access to your Cloudflare account, you will see a consent screen that displays:</p>
<ul>
<li><strong>Application name and logo</strong>: The name and branding of the requesting application</li>
<li><strong>Publisher domain</strong>: The domain and verification status of the application publisher</li>
<li><strong>Account selection</strong>: Choose which Cloudflare account(s) the application can access</li>
<li><strong>Requested permissions</strong>: After selecting the account(s) the application may access, the specific scopes the application is requesting will be displayed before consent is complete. You can also decline optional permissions. To finish the authorization process, review the permissions the application is requesting and select “<strong>Authorize</strong>”</li>
</ul>
<p>Each shield icon indicates who owns the application and whether its domain ownership is verified:</p>
<ul>
<li><strong>Green filled shield</strong>: Cloudflare owns and manages the application.</li>
<li><strong>Blue outlined shield</strong>: A third-party application with verified ownership of its domain.</li>
<li><strong>Amber filled shield</strong>: A third-party application without verified ownership of a domain.</li>
</ul>
<p>Domain verification only confirms that the application owner controls the displayed domain.</p>
<h3 id="edit-optional-permissions">Edit optional permissions</h3>
<p>All requested permissions are selected by default. You can turn off optional permissions, but required permissions remain selected. Select <strong>Read only</strong> to include only optional scopes with read access, or <strong>Full access</strong> to include all optional scopes. If the client has no permissions configured as optional, editing controls do not appear.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8848.md")
</div>
<h2 id="view-and-revoke-authorized-applications">View and revoke authorized applications</h2>
<p>Application authorizations may be viewed and revoked at any time from the profile page on the Cloudflare dashboard.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8849.md")
</div>
<h2 id="account-administrator-controls">Account administrator controls</h2>
<p>If an account is not available for selection during the consent flow, it may be due to an administrator of that account disabling access to account resources via OAuth.</p>
<p>Account administrators can restrict OAuth applications from accessing account resources via <strong>Manage Account</strong> &gt; <strong>Members &gt; Settings &gt; Public OAuth App access</strong>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8847.md")
</aside>
