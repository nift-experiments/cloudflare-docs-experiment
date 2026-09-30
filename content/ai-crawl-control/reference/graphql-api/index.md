<p>AI Crawl Control analytics are available through Cloudflare's <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. You can query the same data shown in the dashboard to build custom reports, integrate with monitoring systems, or export for analysis. Test queries using the <a href="https://graphql.cloudflare.com/">GraphQL API Explorer</a>, or capture the exact queries the dashboard uses via <a href="/analytics/graphql-api/tutorials/capture-graphql-queries-from-dashboard/">Chrome DevTools</a>.</p>
<h2 id="key-filters">Key filters</h2>
<table>
<thead>
<tr>
<th>Filter</th>
<th>Description</th>
<th>Availability</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>requestSource: &quot;eyeball&quot;</code></td>
<td>Real client requests only. Excludes internal Cloudflare traffic.</td>
<td>All plans</td>
</tr>
<tr>
<td><code>userAgent_like: &quot;%...%&quot;</code></td>
<td>Filter by <a href="/ai-crawl-control/reference/bots/">user agent</a>. Can be spoofed.</td>
<td>All plans</td>
</tr>
<tr>
<td><code>edgeResponseStatus_geq</code> / <code>_lt</code></td>
<td>Filter by HTTP status code range.</td>
<td>All plans</td>
</tr>
<tr>
<td><code>clientRequestPath_like: &quot;%...%&quot;</code></td>
<td>Filter by URL path pattern.</td>
<td>All plans</td>
</tr>
<tr>
<td><code>clientRefererHost_like: &quot;%...%&quot;</code></td>
<td>Filter by <a href="/ai-crawl-control/reference/bots/#referrer-domains-by-operator">referrer domain</a>.</td>
<td>Paid plans only</td>
</tr>
<tr>
<td><code>botDetectionIds_hasany: [...]</code></td>
<td>Filter by <a href="/ai-crawl-control/reference/bots/">detection IDs</a>. Reliably verified by Cloudflare.</td>
<td><a href="/bots/get-started/bot-management/">Bot Management</a></td>
</tr>
</tbody>
</table>
<h2 id="query-examples">Query examples</h2>
<details class="nb-details"><summary>Get AI crawler requests over time using detection IDs</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2719.md")
</div></details>
<details class="nb-details"><summary>Get AI crawler requests over time using user agent</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2720.md")
</div></details>
<details class="nb-details"><summary>Get top crawled paths</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2721.md")
</div></details>
<details class="nb-details"><summary>Get AI referral traffic</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2722.md")
</div></details>
<details class="nb-details"><summary>Get data transfer by crawler</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2723.md")
</div></details>
<h2 id="related">Related</h2>
<ul>
<li><a href="/ai-crawl-control/reference/bots/">Bot reference</a> — Detection IDs and user agents</li>
<li><a href="/analytics/graphql-api/">GraphQL Analytics API</a> — Full API documentation</li>
</ul>
