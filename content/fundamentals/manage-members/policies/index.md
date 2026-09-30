<p>Policies define what access a given user has to your account or domains, and are constructed out of three parts:</p>
<ol>
<li>An actor (your user).</li>
<li>A <code>ResourceGroup</code> (a scope).</li>
<li>A <code>PermissionGroup</code> (roles).</li>
</ol>
<p>An account member can have one or several of these policies to represent the most appropriate access. A member’s effective permissions are the union of all policies assigned to them—whether directly, or through group membership.</p>
<p>To increase the usability and flexibility of Cloudflare's role system, changes to the API have been made to expose these underlying data principles and allow users to interact with them.</p>
<p>For example, you may want to assign multiple policies and use scopes to control access to an account where you have a single account with both Production and Staging domains, and a user that should be able see the whole account, purge the production domains, but have the ability to configure the staging domains.</p>
<h2 id="manage-policies">Manage policies</h2>
<p>A set of standard API endpoints is present on every account that allow access to your members, which has recently been enhanced by a list of <code>resourceGroups</code> and <code>PermissionGroups</code>.</p>
<ul>
<li>A <code>resourceGroup</code> is a unique identifier for the scope for which a policy applies.</li>
<li>A <code>permissionGroup</code> is a unique identifier for the set of roles that are assigned to a given policy.</li>
</ul>
<p>Refer to the <a href="/api/">API documentation</a> for more information.</p>
<h2 id="viewing-effective-permissions">Viewing Effective Permissions</h2>
<p>Cloudflare supports assigning permissions to members both directly and through <a href="/fundamentals/manage-members/user-groups/">User Groups</a>. A member’s effective permissions are additive; they represent the union of all permissions granted directly to a member and those inherited through a member's group membership.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8863.md")
</aside>
