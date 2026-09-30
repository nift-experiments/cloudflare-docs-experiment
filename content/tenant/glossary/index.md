<p>The following terms are used throughout the Tenant API docs. For more details on how these concepts interact with each other, refer to <a href="/tenant/structure/">Tenant structure</a>.</p>
<h2 id="tenant">Tenant</h2>
<p>A <strong>Tenant</strong> is a special type of Cloudflare account that contains other accounts and resources.</p>
<h2 id="tenant-admin">Tenant admin</h2>
<p>Once you sign a partner agreement with Cloudflare, we create a special Tenant account and then add your user to that account as a <strong>Tenant admin</strong>. Cloudflare can add multiple users as Tenant admins upon request.</p>
<p>Tenant admins then become the default <a href="/fundamentals/manage-members/roles/"><strong>Super administrator(s)</strong></a> for all accounts and zones contained within the Tenant.</p>
<p>This means that each Tenant admin's user API key can be used to provision accounts based on the catalog specified in your partner agreement.</p>
<p>If needed, you can also <a href="/fundamentals/manage-members/manage/">create additional <strong>Super administrators</strong></a>.</p>
<h2 id="account">Account</h2>
<p>An entity that contains various settings, users, and resources (zones, Zero Trust applications, Workers).</p>
<h2 id="user">User</h2>
<p>A member of a Cloudflare account with their own user profile and <a href="/fundamentals/manage-members/roles/">an associated role</a> that specifies their privileges within that account.</p>
<h2 id="resource">Resource</h2>
<p>A resource is an entity owned by an account, which could be a zone/domain, a Workers instance, or a Zero Trust application.</p>
