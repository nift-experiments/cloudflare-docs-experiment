<p>Access to billing features in the Cloudflare dashboard depends on the role assigned to each account member. This page maps each billing action to the required role.</p>
<h2 id="roles-and-billing-capabilities">Roles and billing capabilities</h2>
<table>
<thead>
<tr>
<th>Action</th>
<th>Super Administrator</th>
<th>Administrator</th>
<th>Billing</th>
</tr>
</thead>
<tbody>
<tr>
<td>View invoices and billing history</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Download invoice PDFs</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>View billable usage dashboard</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Pay an outstanding balance</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Add or update payment methods</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Change billing address</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Change billing email</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Set up budget alerts</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Change or cancel subscriptions</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>Upgrade or downgrade a domain plan</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>Manage account members and roles</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3382.md")
</aside>
<h2 id="assign-the-billing-role">Assign the Billing role</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</li>
<li>Select your account.</li>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Members</strong>.</li>
<li>Select <strong>Invite</strong> to add a new member, or select an existing member to edit their role.</li>
<li>Assign the <strong>Billing</strong> role.</li>
</ol>
<p>For more detail on account roles, refer to <a href="/fundamentals/manage-members/manage/">Manage account members</a>.</p>
<h2 id="api-access-for-billing">API access for billing</h2>
<p>API tokens used for billing endpoints require the <code>Billing Read</code> or <code>Billing Edit</code> permission. To create an API token with billing access:</p>
<ol>
<li>Go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong>.</li>
<li>Select <strong>Create Token</strong>.</li>
<li>Use the <strong>Custom token</strong> template.</li>
<li>Under <strong>Permissions</strong>, select <strong>Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Read</strong> (or <strong>Edit</strong>).</li>
</ol>
<p>For full API documentation, refer to the <a href="https://developers.cloudflare.com/api/">Cloudflare API reference</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/fundamentals/manage-members/manage/">Manage account members</a> — Add, remove, and change roles for account members</li>
<li><a href="/fundamentals/api/get-started/create-token/">API tokens</a> — Create tokens with specific permissions</li>
<li><a href="/billing/understand/how-billing-works/">How Cloudflare billing works</a> — Billing lifecycle and charge types</li>
</ul>
