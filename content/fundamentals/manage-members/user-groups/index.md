<p>User Groups are a collection of <a href="/fundamentals/manage-members/">account members</a> that are treated equally from an access control perspective. User Groups can be assigned permission policies, with individual members in the group receiving all permissions of the roles assigned to the User Group. If users also have individually assigned permissions, then their effective permissions are the union of all of their individual permissions, plus the permissions for all of the User Groups they are a member of.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8852.md")
</aside>
<h2 id="create-a-user-group-manually">Create a User Group manually</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Members</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Groups</strong> tab.</li>
<li>Select <strong>Create a Group</strong> and enter a name and description for your new group.</li>
<li>Select <strong>Create group</strong> to confirm your changes. The <strong>Group members</strong> tab displays.</li>
<li>Select <strong>Add members</strong>.</li>
<li>Select the relevant members you want to include in the group and select <strong>Add to Group</strong>.</li>
</ol>
<h3 id="assign-a-permission-policy">Assign a Permission Policy</h3>
<p>With your Group created, you can now add a <a href="/fundamentals/manage-members/policies/">Permission Policy</a> to your Group.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8855.md")
</div></div>
<h2 id="create-a-user-group-with-scim">Create a User Group with SCIM</h2>
<p>Customers with the SCIM integration configured can sync User Groups from an upstream identity provider to Cloudflare. Cloudflare's SCIM integration requires one external application per account.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8851.md")
</aside>
<p>To set up a user group with SCIM, refer to the <a href="/fundamentals/account/account-security/scim-setup/">Provisioning with SCIM guide</a>.</p>
<h3 id="set-up-permissions-for-user-groups">Set up permissions for User Groups</h3>
<p>After a user group is created either manually in Cloudflare dashboard or through SCIM integration the final step is to attach permissions to it.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8858.md")
</div></div>
<h2 id="inspect-group-members">Inspect Group Members</h2>
<p>To verify the IdP synchronized the group and user members pushed in the SCIM operation, query the Group Members API.</p>
<pre><code class="language-curl">$ curl -XGET -H &quot;Authorization: Bearer $DEMO_AOT&quot; https://api.cloudflare.com/client/v4/accounts/$ACCT/iam/user_groups/$PUSHED_GROUP/members | jq .&#10;</code></pre>
<pre><code class="language-curl">{&#10;  &quot;result&quot;: [&#10;    {&#10;      &quot;id&quot;: &quot;a4366a09c43a0b0c4606dc5528472bb6&quot;,&#10;      &quot;email&quot;: &quot;luke.skywalker@rebelalliance.net&quot;&#10;    },&#10;    {&#10;      &quot;id&quot;: &quot;0329c17f6c13f5202dc38d2036efb1a9&quot;,&#10;      &quot;email&quot;: &quot;arya.stark@winterfell.place&quot;&#10;    }&#10;  ],&#10;  &quot;result_info&quot;: {&#10;    &quot;page&quot;: 1,&#10;    &quot;per_page&quot;: 100,&#10;    &quot;total_pages&quot;: 1,&#10;    &quot;count&quot;: 2,&#10;    &quot;total_count&quot;: 2&#10;  },&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
