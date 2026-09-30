<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8484.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="access-to-area-1">Access to Area 1</h3>
@markup("md", "content/.markup/bodies/8483.md")
</aside>
<p>When you <a href="/email-security/account-setup/manage-account-members/#add-user">create a user</a>, the available options for permissions depend on whether your account is a <strong>parent</strong> account or a <strong>child</strong> account.</p>
<h2 id="parent-accounts">Parent accounts</h2>
<p>Parent accounts are treated as containers with no services provisioned. User accounts created at the parent level will allow them to access any child account.</p>
<p>These accounts are only required for administrators who manage multiple accounts, most commonly associated with our <a href="/email-security/partners/">partners</a>.</p>
<p>Parent users can have one of the following roles:</p>
<ul>
<li><strong>Viewer</strong>: Can enter child accounts but is prevented from making any settings changes, regardless of the customer account settings.</li>
<li><strong>SOC Analyst</strong>: Can enter child accounts and make changes on behalf of the customer.</li>
</ul>
<p>If your account has <a href="/email-security/account-setup/manage-parent-permissions/">parent permissions</a> that conflict with a parent user's permissions, the parent permissions set on your account take precedence.</p>
<h2 id="child-accounts">Child accounts</h2>
<p>Child accounts control settings and services associated with an Email security instance.</p>
<h3 id="child-users">Child users</h3>
<p>Users created at child level will only have access to the assigned child account. These users can have one of the following roles:</p>
<ul>
<li><strong>Super Admin</strong>: Has full access to the account and can make any configuration changes. Can access <strong>Settings</strong> (the gear icon).</li>
<li><strong>Configuration Admin</strong>: Can make configuration changes and manage users, except for Super Admin. Has no ability to review messages.</li>
<li><strong>SOC Analyst</strong>: Can search, review and retract messages. Has no admin capabilities or access to <strong>Settings</strong> (the gear icon).</li>
<li><strong>Viewer</strong>: Only has access to metrics within the system. No access to <strong>Settings</strong> (the gear icon).</li>
</ul>
<table-wrap>
<table>
<thead>
<tr>
<th>Account area</th>
<th>Super Admin</th>
<th>Configuration Admin</th>
<th>SOC Analyst</th>
<th>Viewer</th>
</tr>
</thead>
<tbody>
<tr>
<td>All Settings</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
</tr>
<tr>
<td>User Profile</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Global Search</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Detection Search</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Detection Search Actions</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Mail Trace</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Home</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Email</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Web</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Accountability</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Announcements and Support</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Landscape</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Message Preview</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Message Retraction</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Admin Quarantine</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
</tbody>
</table>
</table-wrap>
<h3 id="parent-users">Parent users</h3>
<p>Depending on the <a href="/email-security/account-setup/manage-parent-permissions/">parent permissions</a> of your child account, you can delegate access to parent users of your account. This configuration will allow a parent user to view and change settings associated with your account.</p>
