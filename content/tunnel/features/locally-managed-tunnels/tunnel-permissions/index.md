<p>Tunnel permissions determine who can run and manage a Cloudflare Tunnel. Two files control permissions for a locally-managed tunnel:</p>
<ul>
<li><strong>An account certificate</strong> (<code>cert.pem</code>) is issued for a Cloudflare account when you login to <code>cloudflared</code>. Make sure you are intentional about the locations and machines you store this certificate on, as this certificate allows users to create, delete, and manage all tunnels for the account.</li>
<li><strong>A tunnel credentials file</strong> (<code>&lt;TUNNEL-UUID&gt;.json</code>) is issued for a tunnel when you create the tunnel. The credentials file only allows the user to run that specific tunnel, and do nothing else. Hence, as an admin, you can share tunnel credentials with users who will run the tunnel.</li>
</ul>
<p>Refer to the table below for a comparison between the two files and the purposes for which they are intended.</p>
<table>
<thead>
<tr>
<th></th>
<th>Account certificate</th>
<th>Tunnel credential</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>File name</strong></td>
<td><code>cert.pem</code></td>
<td><code>&lt;TUNNEL-UUID&gt;.json</code></td>
</tr>
<tr>
<td><strong>Purpose</strong></td>
<td>Authenticates your instance of <code>cloudflared</code> against your Cloudflare account</td>
<td>Authenticates the tunnel it is associated with</td>
</tr>
<tr>
<td><strong>Scope</strong></td>
<td>Account-wide</td>
<td>Tunnel-specific</td>
</tr>
<tr>
<td><strong>File type</strong></td>
<td><code>.pem</code></td>
<td><code>.json</code></td>
</tr>
<tr>
<td><strong>Stored in</strong></td>
<td><a href="/tunnel/features/locally-managed-tunnels/local-tunnel-terms/#default-cloudflared-directory">Default directory</a></td>
<td><a href="/tunnel/features/locally-managed-tunnels/local-tunnel-terms/#default-cloudflared-directory">Default directory</a></td>
</tr>
<tr>
<td><strong>Issued when running</strong></td>
<td><code>cloudflared tunnel login</code></td>
<td><code>cloudflared tunnel create &lt;NAME&gt;</code></td>
</tr>
<tr>
<td><strong>Valid for</strong></td>
<td>At least 10 years, and the service token it contains is valid until <a href="#revoke-account-certificate">revoked</a></td>
<td>Does not expire</td>
</tr>
<tr>
<td><strong>Needed to</strong></td>
<td>Manage tunnels (for example, create, route, delete and list tunnels)</td>
<td>Run a tunnel. Create a config file.</td>
</tr>
</tbody>
</table>
<h2 id="tunnel-ownership">Tunnel ownership</h2>
<p>Tunnel ownership is bound to the Cloudflare account for which the <code>cert.pem</code> file was issued upon authenticating <code>cloudflared</code>. If a user in a Cloudflare account creates a tunnel, any other user in the same account who has access to the <code>cert.pem</code> file for the account can delete, list, or otherwise manage tunnels within it.</p>
<h2 id="revoke-account-certificate">Revoke account certificate</h2>
<p>Your account certificate (<code>cert.pem</code>) contains an API token which authorizes <code>cloudflared</code> to manage tunnels in your Cloudflare account. To revoke the account certificate, delete the API token associated with your tunnel:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong>.</li>
<li>Find the <strong>Cloudflare Tunnel API Token</strong> or <strong>Argo Tunnel API Token</strong> for your zone and account.</li>
<li>Select the three dots &gt; <strong>Delete</strong>.</li>
</ol>
<p>Once this token is deleted, <code>cloudflared</code> can no longer use the old <code>cert.pem</code> file to read or edit tunnels in your account. To generate a new token and <code>cert.pem</code> file, run <code>cloudflared tunnel login</code>.</p>
<h2 id="account-scoped-roles">Account-scoped roles</h2>
<p>Minimum permissions needed to create, delete, and configure tunnels for an account:</p>
<ul>
<li><a href="/cloudflare-one/roles-permissions/">Cloudflare Access</a></li>
</ul>
<p>Additional permissions needed to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">route traffic to a public hostname</a> and to be able to perform <code>cloudflared login</code>:</p>
<ul>
<li><a href="/fundamentals/manage-members/roles/">DNS</a></li>
<li><a href="/fundamentals/manage-members/roles/">Load Balancer</a></li>
</ul>
