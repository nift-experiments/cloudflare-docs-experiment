<p>Permissions are segmented into three categories based on resource:</p>
<ul>
<li>Zone permissions</li>
<li>Account permissions</li>
<li>User permissions</li>
</ul>
<p>Each category contains permission groups related to those resources. DNS permissions belong to the Zone category, while Billing permissions belong to the Account category. Below is a list of the available token permissions.</p>
<p>To obtain an updated list of token permissions, including the permission ID and the scope of each permission, use the <a href="/api/resources/user/subresources/tokens/subresources/permission_groups/methods/list/">List permission groups</a> endpoint.</p>
<h2 id="user-permissions">User permissions</h2>
<p>The applicable scope of user permissions is <code>com.cloudflare.api.user</code>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8968.md")
</div></div>
<h2 id="account-permissions">Account permissions</h2>
<p>The applicable scope of account permissions is <code>com.cloudflare.api.account</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8965.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8971.md")
</div></div>
<h2 id="zone-permissions">Zone permissions</h2>
<p>The applicable scope of zone permissions is <code>com.cloudflare.api.account.zone</code>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8974.md")
</div></div>
