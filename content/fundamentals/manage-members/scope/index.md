<p>Scopes are one of three constituent parts of a policy that allows granting of access to users.</p>
<p>To allow for flexible combinations of access to users, Cloudflare currently has account-level scopes, domain scopes, and resource-specific scopes. Each scope is associated with a different set of <a href="/fundamentals/manage-members/roles/">roles</a>.</p>
<ul>
<li><strong>Account scope:</strong> Use when the member needs access across the entire account, for example, billing or account-level settings.</li>
<li><strong>Specific domains:</strong> Use when the member should only manage certain domains, for example, a developer who works on staging domains but should not modify production.</li>
<li><strong>Domain groups:</strong> Use when you have related domains that share the same access needs, for example, all production domains.</li>
<li><strong>Specific resources:</strong> Use when access should be limited to individual resources.</li>
</ul>
<hr />
<h2 id="choose-the-scope-of-roles">Choose the scope of roles</h2>
<p>Each policy has a limitation of a single scope, but you can assign multiple policies to a given user.</p>
<p>You can choose the scope of a policy when you <a href="/fundamentals/manage-members/manage/">add a member</a>.</p>
<h3 id="account-scope">Account scope</h3>
<p>If you want the member to have a policy that applies across your account, use the following combination of fields.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Operator</td>
<td><em>Include</em></td>
</tr>
<tr>
<td>Type</td>
<td><em>All domains</em></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8861.md")
</aside>
<h3 id="specific-domains">Specific domains</h3>
<p>If you want the member to have a policy that applies to a specific domain, use the following combination of fields. When applying these roles to this policy, only domain-scoped roles can be used.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Operator</td>
<td><em>Include</em></td>
</tr>
<tr>
<td>Type</td>
<td><em>A specific domain</em></td>
</tr>
<tr>
<td>Name</td>
<td><em>A specific domain</em></td>
</tr>
</tbody>
</table>
<h3 id="domain-groups">Domain groups</h3>
<p>If you have a set of domains that are all categorized similarly (e.g. all of your sensitive/production domains, all domains around a given project or geography), you can pre-assign them into a domain group and then create policies that provide access to all domains within this group.</p>
<h4 id="create-group">Create group</h4>
<p>To create a domain group:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Settings</strong> &gt; <strong>Lists</strong> page. (You must be logged in as a <strong>Super Administrator</strong> and have a <a href="/fundamentals/user-profiles/verify-email-address/">verified email address</a>).</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>For <strong>Domain Group Manager</strong>, select <strong>Create</strong>.</p>
</li>
<li>
<p>Create your domain group:</p>
<ol>
<li>Select the domains to include.</li>
<li>Add a <strong>Name</strong>.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
</li>
</ol>
<p>You can also edit and delete these groups as needed.</p>
<h4 id="use-group">Use group</h4>
<p>To assign a member permissions to a domain group, use the following combination of fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Operator</td>
<td><em>Include</em></td>
</tr>
<tr>
<td>Type</td>
<td><em>Domain Group</em></td>
</tr>
<tr>
<td>Name</td>
<td><em>Example Group</em></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8860.md")
</aside>
<h3 id="specific-resources">Specific resources</h3>
<p>If you want the member to have a policy that applies to a specific resource, use the following combination of fields.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Operator</td>
<td><em>Include</em></td>
</tr>
<tr>
<td>Type</td>
<td><em>Granular</em></td>
</tr>
<tr>
<td>Product</td>
<td><em>Product Name</em></td>
</tr>
<tr>
<td>Resource</td>
<td><em>Specific Resource</em></td>
</tr>
</tbody>
</table>
<h4 id="available-scopes">Available scopes</h4>
<p>You can assign the following resource-specific scopes to members:</p>
<table>
<thead>
<tr>
<th>Scope</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Individual Access applications</td>
<td>Grant access to manage a specific <a href="/cloudflare-one/access-controls/applications/">Access application</a>.</td>
</tr>
<tr>
<td>Individual Access identity providers (IdPs)</td>
<td>Grant access to manage a specific <a href="/cloudflare-one/integrations/identity-providers/">Cloudflare One identity provider (IdP)</a>.</td>
</tr>
<tr>
<td>Individual Access policies</td>
<td>Grant access to manage a specific <a href="/cloudflare-one/access-controls/policies/">Access policy</a>.</td>
</tr>
<tr>
<td>Individual Access service tokens</td>
<td>Grant access to manage a specific <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Access service token</a>.</td>
</tr>
<tr>
<td>Individual Access infrastructure targets</td>
<td>Grant access to manage a specific <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure target</a>.</td>
</tr>
<tr>
<td>Individual Cloudflare Tunnel instances</td>
<td>Grant access to manage a specific <a href="/tunnel/">Cloudflare Tunnel</a> instance.</td>
</tr>
<tr>
<td>Individual Cloudflare Mesh nodes</td>
<td>Grant access to manage a specific <a href="/mesh/">Cloudflare Mesh</a> node.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8859.md")
</aside>
