<p>Cloudflare helps Channel and Alliance partners manage their and their customers' accounts through a Tenant structure.</p>
<p><img src="/assets/upstream/images/tenant/tenant-diagram.png" alt="Partner accounts contain a tenant, which is a container for customer accounts and zones. For more details, keep reading." /></p>
<h2 id="tenants-and-tenant-admins">Tenants and Tenant admins</h2>
<p>A <strong>Tenant</strong> is a special type of Cloudflare account that contains other accounts and resources.</p>
<p>Once you sign a partner agreement with Cloudflare, we create a special Tenant account and then add your user to that account as a <strong>Tenant admin</strong>. Cloudflare can add multiple users as Tenant admins upon request.</p>
<p>Tenant admins then become the default <a href="/fundamentals/manage-members/roles/"><strong>Super administrator(s)</strong></a> for all accounts and zones contained within the Tenant.</p>
<p>This means that each Tenant admin's user API key can be used to provision accounts based on the catalog specified in your partner agreement.</p>
<p>If needed, you can also <a href="/fundamentals/manage-members/manage/">create additional <strong>Super administrators</strong></a>.</p>
<h2 id="accounts-users-and-resources">Accounts, users, and resources</h2>
<p>This Tenant structure gives your account streamlined administrative access to customer:</p>
<ul>
<li>Accounts<sup><a href="#footnote-1">1</a></sup></li>
<li>Users<sup><a href="#footnote-2">2</a></sup></li>
<li>Resources<sup><a href="#footnote-3">3</a></sup></li>
</ul>
<p>At the same time, this structure keeps your customers' data and settings separate from each other.</p>
<p>An entity that contains various settings, users, and resources (zones, Zero Trust applications, Workers).</p>
<p>A member of a Cloudflare account with their own user profile and <a href="/fundamentals/manage-members/roles/">an associated role</a> that specifies their privileges within that account.</p>
<p>A resource is an entity owned by an account, which could be a zone/domain, a Workers instance, or a Zero Trust application.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1"></li>
<li id="footnote-2"></li>
<li id="footnote-3"></li></ol></section>
