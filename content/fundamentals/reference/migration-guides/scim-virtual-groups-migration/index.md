<p>Cloudflare's first iteration of SCIM integration introduced a concept called <em>Virtual Groups</em>, typically identified by the pattern <code>CF-&lt;accountID&gt;-&lt;Role Name&gt;</code> in your IdP. Virtual Groups were an early implementation of group-based access control: they acted as placeholders created automatically by SCIM to map IdP groups to account memberships.</p>
<p>While customers could add or remove members from these groups within their IdP, Virtual Groups had important limitations:</p>
<ul>
<li>They could not be renamed or deleted in the IdP.</li>
<li>They could not be managed within Cloudflare.</li>
<li>Functionally, managing a Virtual Group was equivalent to syncing users and editing each member’s policies individually.</li>
</ul>
<p>With the GA of <a href="/changelog/2025-06-23-user-groups-ga/">User Groups</a>, Virtual Groups are now deprecated. Customers should migrate to <a href="/fundamentals/manage-members/user-groups/">User Groups</a>, which provide a more flexible and scalable way to assign and manage policies. To maintain SCIM synchronization with the Cloudflare Dashboard, we strongly recommend migrating to <strong>SCIM User Groups</strong>.</p>
<p>If you have never synced a group linked to a <code>CF-&lt;accountID&gt;-&lt;Role Name&gt;</code> Virtual Group from your IdP to Cloudflare, no action is needed.</p>
<h2 id="migration-steps">Migration steps</h2>
<ol>
<li><strong>Create a new SCIM integration</strong> in your IdP using an <a href="/fundamentals/account/account-security/scim-setup/">Account Owned Token</a> provisioned in Cloudflare.</li>
<li><strong>Assign users &amp; groups to your new Application</strong> in your IdP, following a naming convention that aligns with your internal processes.</li>
<li><strong>Sync groups to Cloudflare</strong> and verify they appear in the <strong>User Groups</strong> pane of the Cloudflare Dashboard.</li>
<li><strong>Attach permission policies</strong> to the new User Groups so members inherit the correct access upon assignment to the group.</li>
<li><strong>Migrate users</strong> into the new groups incrementally, testing synchronization of users &amp; groups into the Cloudflare Dashboard.</li>
<li><strong>Clean up legacy resources</strong> by removing SCIM v1 Virtual Groups and IdP mappings that follow the <code>CF-&lt;accountID&gt;-&lt;Role Name&gt;</code> pattern.</li>
</ol>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="/changelog/2025-06-02-user-groups-beta/">User Groups changelog</a></li>
<li><a href="/fundamentals/manage-members/user-groups/">User Groups documentation</a></li>
<li><a href="/fundamentals/api/get-started/account-owned-tokens/#create-an-account-owned-token">Create an Account Owned Token</a></li>
<li><a href="/fundamentals/account/account-security/scim-setup/">SCIM provisioning setup guide</a></li>
</ul>
