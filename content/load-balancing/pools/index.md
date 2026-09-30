<div class="nb-glossary-definition"><p>Within Cloudflare, pools represent your endpoints and how they are organized. As such, a pool can be a group of several endpoints, or you could also have only one endpoint (an origin server, for example) per pool.</p>
<p>If you are familiar with DNS terminology, think of a pool as a “record set,” except Cloudflare only returns addresses that are considered healthy. You can attach health monitors to individual pools for customized monitoring. A pool can have either a single monitor or a monitor group attached — but not both.</p></div>
<p>For more details about how endpoints and pools become unhealthy, refer to <a href="/load-balancing/understand-basics/health-details/">Endpoint and pool health</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10354.md")
</aside>
<hr />
<h2 id="properties">Properties</h2>
<p>For an up-to-date list of pool properties, refer to <a href="/api/resources/load_balancers/subresources/pools/methods/list/">Pool properties</a> in our API documentation.</p>
<hr />
<h2 id="create-pools">Create pools</h2>
<p>For step-by-step guidance, refer to <a href="/load-balancing/pools/create-pool/">Create pools</a>.</p>
<hr />
<h2 id="per-endpoint-host-header-override">Per-endpoint Host header override</h2>
<p>When your application needs specialized routing (<code>CNAME</code> setup or custom hosts like Heroku), change the <code>Host</code> header used in health monitor requests. For more details, refer to <a href="/load-balancing/additional-options/override-http-host-headers/">Override HTTP Host headers</a>.</p>
<hr />
<h2 id="api-commands">API commands</h2>
<p>The Cloudflare API supports the following commands for pools. Examples are given for user-level endpoint but apply to the account-level endpoint as well.</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Method</th>
<th>Endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/methods/create/">Create Pool</a></td>
<td><code>POST</code></td>
<td><code>accounts/:account_id/load_balancers/pools</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/methods/delete/">Delete Pool</a></td>
<td><code>DELETE</code></td>
<td><code>accounts/:account_id/load_balancers/pools/:id</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/methods/list/">List Pools</a></td>
<td><code>GET</code></td>
<td><code>accounts/:account_id/load_balancers/pools</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/methods/get/">Pool Details</a></td>
<td><code>GET</code></td>
<td><code>accounts/:account_id/load_balancers/pools/:id</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/subresources/health/methods/get/">Pool Health Details</a></td>
<td><code>GET</code></td>
<td><code>account/:account_id/load_balancers/pools/:id/health</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/methods/edit/">Overwrite specific properties</a></td>
<td><code>PATCH</code></td>
<td><code>accounts/:account_id/load_balancers/pools/:id</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/methods/update/">Overwrite existing pool</a></td>
<td><code>PUT</code></td>
<td><code>accounts/:account_id/load_balancers/pools/:id</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/subresources/health/methods/create/">Preview Pool</a></td>
<td><code>POST</code></td>
<td><code>account/:account_id/load_balancers/pools/:id/preview</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/pools/subresources/references/methods/get/">List Pool References</a></td>
<td><code>GET</code></td>
<td><code>accounts/:account_id/load_balancers/pools/:id/references</code></td>
</tr>
</tbody>
</table>
