<p>A remotely-managed tunnel only requires the tunnel token to run. Anyone with access to the token will be able to run the tunnel.</p>
<h2 id="get-the-tunnel-token">Get the tunnel token</h2>
<p>To get the token for a remotely-managed tunnel:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5364.md")
</div></div>
<h2 id="rotate-a-token-without-service-disruption">Rotate a token without service disruption</h2>
<p>Cloudflare recommends rotating the tunnel token at a regular cadence to reduce the risk of token compromise. You can rotate a token with minimal disruption to users as long as the tunnel is served by at least two <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/"><code>cloudflared</code> replicas</a>. To ensure service availability, we recommend performing token rotations outside of working hours or in a maintenance window.</p>
<p>To rotate a tunnel token:</p>
<ol>
<li>Refresh the token on Cloudflare:</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5367.md")
</div></div>
<pre><code>After refreshing the token, `cloudflared` can no longer establish new connections to Cloudflare using the old token. However, existing connectors will remain active and the tunnel will continue serving traffic.&#10;</code></pre>
<ol start="2">
<li>On half of your <code>cloudflared</code> replicas, reinstall the <code>cloudflared</code> service with the new token. For example, on a Linux host:</li>
</ol>
<pre><code class="language-sh">	 sudo cloudflared service uninstall&#10;sudo cloudflared service install &lt;NEW_TOKEN&gt;&#10;</code></pre>
<ol start="3">
<li>Confirm that the service started correctly:</li>
</ol>
<pre><code class="language-sh">sudo systemctl status cloudflared&#10;</code></pre>
<p>While these replicas are connecting to Cloudflare with the new token, traffic will automatically route through the other replicas.</p>
<ol start="5">
<li>
<p>Wait 10 minutes for traffic to route through the new connectors.</p>
</li>
<li>
<p>Repeat steps 2, 3, and 4 for the second half of the replicas.</p>
</li>
</ol>
<p>The tunnel token is now fully rotated. The old token is no longer in use.</p>
<h2 id="rotate-a-compromised-token">Rotate a compromised token</h2>
<p>If your tunnel token is compromised, we recommend taking the following steps:</p>
<ol>
<li>Refresh the token using the dashboard or API. Refer to Step 1 of <a href="#rotate-a-token-without-service-disruption">Rotate a token without service disruption</a>.</li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/connections/methods/delete/">Delete all connections</a> between <code>cloudflared</code> and Cloudflare:</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<p>This will clean up any unauthorized connections and prevent users from connecting to your network.</p>
<ol start="3">
<li>On each <code>cloudflared</code> replica, update <code>cloudflared</code> to use the new token. For example, on a Linux host:</li>
</ol>
<pre><code class="language-sh">	 sudo cloudflared service uninstall&#10;sudo cloudflared service install &lt;NEW_TOKEN&gt;&#10;</code></pre>
<ol start="4">
<li>Confirm that the service started correctly:</li>
</ol>
<pre><code class="language-sh">sudo systemctl status cloudflared&#10;</code></pre>
<p>The tunnel token is now fully rotated. The old token is no longer in use.</p>
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
<h2 id="resource-scoped-permissions">Resource-scoped permissions</h2>
<p>You can also scope permissions to individual <a href="/tunnel/">Cloudflare Tunnel</a> instances instead of granting account-wide access. Refer to <a href="/cloudflare-one/networks/connectors/granular-permissions/">Granular permissions for Tunnels and Mesh nodes</a>.</p>
