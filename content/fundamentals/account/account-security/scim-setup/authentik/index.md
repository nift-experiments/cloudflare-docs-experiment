<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8964.md")
</aside>
<p>Once you have <a href="/fundamentals/account/account-security/scim-setup/#gather-the-required-data">gathered the required data</a>, the following steps will be required to finish the provisioning with Authentik.</p>
<h2 id="set-up-your-authentik-scim-provider">Set up your Authentik SCIM provider</h2>
<ol>
<li>In the Authentik Admin interface, go to <strong>Applications</strong> &gt; <strong>Providers</strong>.</li>
<li>Select <strong>Create</strong> and choose <strong>SCIM Provider</strong>.</li>
<li>Name your provider (for example, <code>Cloudflare SCIM</code>).</li>
<li>In <strong>URL</strong>, enter: <code>https://api.cloudflare.com/client/v4/accounts/&lt;accountID&gt;/scim/v2</code>, substituting <code>&lt;accountID&gt;</code> for your <a href="/fundamentals/account/account-security/scim-setup/#get-the-account-id">Cloudflare Account ID</a>.</li>
<li>In <strong>Token</strong>, Paste the SCIM provisioning API token.</li>
<li>(Optional) Adjust the <strong>User filtering</strong> and <strong>Group filtering</strong> settings to control which users and groups are synchronized.</li>
<li>Select <strong>Finish</strong> to create the provider.</li>
</ol>
<h2 id="create-an-authentik-application">Create an Authentik application</h2>
<ol>
<li>In the Authentik Admin interface, go to <strong>Applications</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create</strong>.</li>
<li>Name your application (for example, <code>Cloudflare Dashboard</code>).</li>
<li>In <strong>Provider</strong>, select the SCIM provider you created in the previous step.</li>
<li>Select <strong>Create</strong> to save the application.</li>
</ol>
<h2 id="configure-user-and-group-sync-in-authentik">Configure user and group sync in Authentik</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8963.md")
</aside>
<ol>
<li>In the Authentik Admin interface, go to <strong>Directory</strong> &gt; <strong>Groups</strong>.</li>
<li>Create or select the groups you want to synchronize with Cloudflare. Ensure the users you want to provision are members of these groups.</li>
<li>Return to <strong>Applications</strong> &gt; <strong>Providers</strong> and select your SCIM provider.</li>
<li>Under <strong>Backchannel Providers</strong>, verify that your SCIM provider is correctly linked to the application.</li>
<li>To trigger a manual sync, select <strong>Sync</strong> from the provider page. Authentik will also perform automatic periodic syncs based on your configured schedule.</li>
</ol>
<h2 id="verify-the-integration">Verify the integration</h2>
<p>To verify the integration:</p>
<ol>
<li>In Authentik, go to <strong>Applications</strong> &gt; <strong>Providers</strong>, select your SCIM provider, and review the <strong>Sync status</strong> section for any errors.</li>
<li>In the Cloudflare dashboard, go to <strong>Manage Account</strong> &gt; <strong>Members</strong> &gt; <strong>User Groups</strong> to view the synchronized groups.</li>
<li>Check the Audit Logs in the Cloudflare dashboard by going to <strong>Manage Account</strong> &gt; <strong>Audit Log</strong>.</li>
</ol>
<h2 id="assign-policies-to-user-groups">Assign policies to user groups</h2>
<p>After users and groups are synchronized, you can assign <a href="/fundamentals/manage-members/policies/">policies</a> to user groups:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Manage Account</strong> &gt; <strong>Members</strong> &gt; <strong>User Groups</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the group you want to configure.</li>
<li>Assign the appropriate policies to define the <a href="/fundamentals/manage-members/roles/">roles</a> for group members.</li>
</ol>
