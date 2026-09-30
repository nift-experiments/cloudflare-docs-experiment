<p>Cloudflare supports bulk provisioning of users into the Cloudflare dashboard by using the System for Cross-domain Identity Management (SCIM) protocol. This allows you to connect an external identity provider (IdP) to Cloudflare, quickly onboard and manage user permissions. Currently, SCIM provisioning has been integrated with Okta, Microsoft Entra, and Authentik.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8959.md")
</aside>
<h2 id="objectives">Objectives</h2>
<p>Once the SCIM provisioning is enabled:</p>
<ul>
<li>A Cloudflare account can receive user group provisioning from the identity provider.</li>
<li>Members of each user group can be assigned one or more <a href="/fundamentals/manage-members/policies/">policies</a>. Each policy defines one or more <a href="https://developers.cloudflare.com/fundamentals/manage-members/roles/">roles</a> applied to all group members thereof.</li>
<li>Members can belong to multiple user groups, and each group can also be configured with different policies.</li>
<li>Policies provisioned via SCIM can coexist with policies configured via the <a href="/fundamentals/manage-members/manage/#edit-member-permissions">traditional setup</a>.</li>
</ul>
<h2 id="expected-behaviors">Expected behaviors</h2>
<p>Expectations for user lifecycle management with SCIM:</p>
<table>
<thead>
<tr>
<th>Expected Cloudflare dash behavior</th>
<th>Identity provider action</th>
</tr>
</thead>
<tbody>
<tr>
<td>User is added to account as member</td>
<td>Assign the user to a SCIM application. They will be assigned the Minimal Account Access role so that their dash experience is not broken.</td>
</tr>
<tr>
<td>User is removed from account as member</td>
<td>Unassign the user from the SCIM application.</td>
</tr>
<tr>
<td>Add role to user</td>
<td>Add the user to a group in the IdP which is pushed via SCIM. They must also be assigned to the SCIM application and exist as an account member.</td>
</tr>
<tr>
<td>Remove role from user</td>
<td>Remove the user from the corresponding group in the IdP.</td>
</tr>
<tr>
<td>Retain user in account but with no permissions</td>
<td>Remove the user from all role groups but leave them assigned to the SCIM application. They will be an account member with only the role Minimal Account Access.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8958.md")
</aside>
<h2 id="limitations">Limitations</h2>
<ul>
<li>If a user is the only Super Administrator on an Enterprise account, they will not be deprovisioned.</li>
<li>It is possible to unintentionally remove all account Super Administrators by misconfiguring SCIM groups. Refer to <a href="/fundamentals/account/account-security/scim-setup/troubleshooting/">SCIM troubleshooting</a> for more information.</li>
<li>SCIM group names cannot begin with the reserved prefix <code>CF</code>.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Cloudflare dashboard SCIM provisioning is only available to Enterprise customers using Okta, Microsoft Entra, or Authentik.</li>
<li>You must be a Super Administrator for the initial setup.</li>
<li>In the identity provider, you must have the ability to create applications and groups.</li>
</ul>
<hr />
<h2 id="gather-the-required-data">Gather the required data</h2>
<p>To start, you will need to collect a couple of pieces of data from Cloudflare and set these aside for later use.</p>
<h3 id="get-the-account-id">Get the Account ID</h3>
<p>The account ID can be found via dashboard or API. For more information, refer to <a href="/fundamentals/account/find-account-and-zone-ids/">Find account and zone IDs</a>.</p>
<h3 id="create-an-api-token">Create an API token</h3>
<ol>
<li><a href="/fundamentals/api/get-started/create-token/">Create an API token</a> with the following permissions:</li>
</ol>
<table>
<thead>
<tr>
<th>Type</th>
<th>Item</th>
<th>Permission</th>
</tr>
</thead>
<tbody>
<tr>
<td>Account</td>
<td>SCIM Provisioning</td>
<td>Edit</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8957.md")
</aside>
<ol start="2">
<li>Under <strong>Account Resources</strong>, select the specific account to include or exclude from the dropdown menu, if applicable.</li>
<li>Select <strong>Continue to summary</strong>.</li>
<li>Validate the permissions and select <strong>Create Token</strong>.</li>
<li>Copy the token value.</li>
</ol>
