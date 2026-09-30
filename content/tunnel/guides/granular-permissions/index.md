<p>You can scope Cloudflare member permissions to individual <a href="/tunnel/">Cloudflare Tunnel</a> instances instead of granting account-wide access. This lets you delegate management of specific Tunnels — for example, letting an application team manage one Tunnel for its service without exposing every Tunnel in the account.</p>
<p>Granular permissions are a parallel layer to account-level roles — they do not replace them. Members who already hold an account-level role like <code>Cloudflare Access</code> retain write access to every Tunnel in the account.</p>
<h2 id="how-it-works">How it works</h2>
<p>For any API request on a specific Cloudflare Tunnel, access is granted if the principal has <strong>either</strong>:</p>
<ul>
<li>An account-level role that covers Tunnels (for example, <code>Cloudflare Access</code>), <strong>or</strong></li>
<li>A <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">resource-scoped role</a> bound to that specific Tunnel.</li>
</ul>
<p><a href="#resource-enumeration">Listing endpoints</a> (<code>GET /accounts/{id}/cfd_tunnel</code>, <code>GET /accounts/{id}/teamnet/routes</code>) return only the Tunnels and routes the principal has at least read access to.</p>
<h2 id="grant-a-granular-permission">Grant a granular permission</h2>
<p>Granular permissions are assigned through the standard <a href="/fundamentals/manage-members/manage/">member management</a> flow.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Manage Account</strong> &gt; <strong>Members</strong> and select <strong>Invite Members</strong>, or open an existing member to edit their permissions.</li>
<li>Add a permission policy and choose a <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">resource-scoped role</a> that targets Cloudflare Tunnel instances.</li>
<li>In the <strong>Scope</strong> section, choose <strong>Specific resources</strong>.</li>
<li>Set <strong>Resource type</strong> to <strong>Cloudflare Tunnel instances</strong>.</li>
<li>Select one or more specific Tunnels from the resource picker.</li>
<li>Save the policy.</li>
</ol>
<p>You can attach multiple granular policies to the same member to cover different Tunnels with different roles.</p>
<h2 id="resource-enumeration">Resource enumeration</h2>
<p>Listing endpoints are authorization-aware. When a principal calls a listing endpoint, the response is filtered to the Tunnels and routes they have at least read access to.</p>
<table>
<thead>
<tr>
<th>Endpoint</th>
<th>Method</th>
<th>Returns</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/accounts/{account_id}/cfd_tunnel</code></td>
<td><code>GET</code></td>
<td>Cloudflare Tunnel instances the principal can read or manage.</td>
</tr>
<tr>
<td><code>/accounts/{account_id}/teamnet/routes</code></td>
<td><code>GET</code></td>
<td>Routes attached to Tunnels the principal can read or manage.</td>
</tr>
</tbody>
</table>
<p>Members with an account-level role that covers Tunnels continue to see all Tunnels in the account.</p>
<h2 id="backward-compatibility">Backward compatibility</h2>
<ul>
<li>Existing account-level roles and API tokens continue to function as before.</li>
<li>Existing automation that authenticates with an account-level token (for example, Terraform pipelines using a <code>Cloudflare Access</code> token) is unaffected.</li>
<li>Granular permissions are opt-in. Granting one to a member adds capability; it never removes capability that the member already has from an account-level role.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/fundamentals/manage-members/roles/">Roles reference</a> — the full list of Cloudflare roles, including resource-scoped roles for Cloudflare Tunnel instances.</li>
<li><a href="/fundamentals/manage-members/manage/">Manage account members</a> — the member invite and edit flow.</li>
<li><a href="/cloudflare-one/networks/connectors/granular-permissions/">Granular permissions for Cloudflare Tunnel and Cloudflare Mesh in Cloudflare One</a> — the same RBAC capability applied to Cloudflare Mesh nodes alongside Tunnels.</li>
</ul>
