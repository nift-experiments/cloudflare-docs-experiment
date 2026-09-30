<h2 id="429-too-many-requests">429 Too Many Requests</h2>
<p>The <code>429 Too Many Requests</code> status code indicates that the client has sent too many requests in a specified amount of time, as determined by the server's rate-limiting rules. The server may include a <code>Retry-After</code> header in the response to specify when the client can try again.</p>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc6585">RFC 6585</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>Servers use this status code to prevent excessive API requests from overloading the system. For example, a client making repeated API calls within a short time frame may trigger a 429 response. Websites or services may impose rate limits to manage traffic spikes or prevent abuse, temporarily blocking excessive requests from users.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<h4 id="cloudflare-api-limits">Cloudflare API limits</h4>
<table>
<thead>
<tr>
<th>Type</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client API per user/account token</td>
<td>1200/5 minutes</td>
</tr>
<tr>
<td>Client API per IP</td>
<td>200/second</td>
</tr>
<tr>
<td>GraphQL</td>
<td>Varies by query cost. Max 320/5 min</td>
</tr>
<tr>
<td>User API token quota</td>
<td>50</td>
</tr>
<tr>
<td>Account API token quota</td>
<td>500</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14744.md")
</aside>
<p>Some specific API calls have their own limits and are documented separately, such as the following:</p>
<ul>
<li><a href="/cache/how-to/purge-cache/#availability-and-limits">Cache Purge APIs</a></li>
<li><a href="/analytics/graphql-api/limits/">GraphQL APIs</a></li>
<li><a href="/ruleset-engine/rulesets-api/#limits">Rulesets APIs</a></li>
<li><a href="/waf/tools/lists/lists-api/#rate-limiting-for-lists-api-requests">Lists API</a></li>
<li><a href="/cloudflare-one/reusable-components/lists/#api-rate-limit">Gateway Lists API</a></li>
</ul>
<p>Enterprise customers can also <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a> to raise the Client API per user, GraphQL, or API token limits to a higher value.</p>
<h4 id="r2-managed-public-buckets">R2 managed public buckets</h4>
<p>Cloudflare applies rate limiting to requests for R2 managed public buckets accessed via <code>r2.dev</code>. This helps protect customers from abuse and overuse of public buckets. For details, refer to <a href="/r2/platform/limits/#rate-limiting-on-managed-public-buckets-through-r2dev">Rate limiting on managed public buckets through <code>r2.dev</code></a>.</p>
<h4 id="website-end-users">Website end users</h4>
<p>Cloudflare will generate a <code>429</code> response when a request is being <a href="https://www.cloudflare.com/rate-limiting/">rate limited</a>. If visitors to your site encounter this error, it will be visible in the <a href="/waf/reference/legacy/old-rate-limiting/#analytics">Rate Limiting Analytics</a> dashboard.</p>
