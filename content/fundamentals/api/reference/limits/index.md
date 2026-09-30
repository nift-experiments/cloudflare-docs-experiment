<h2 id="api-token-limits">API token limits</h2>
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
@markup("md", "content/.markup/bodies/8975.md")
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
<h2 id="rate-limiting-headers">Rate limiting headers</h2>
<p>The following headers are returned when calling REST APIs:</p>
<ul>
<li><code>Ratelimit</code>: List of service limit items, composed of the limit name, the remaining quota (<code>r</code>) and the time next window resets (<code>t</code>). For example: <code>&quot;default&quot;;r=50;t=30</code></li>
<li><code>Ratelimit-Policy</code>: List of quota policy items, composed of the policy name, the total quota (<code>q</code>) and the time window the quota applies to (<code>w</code>). For example: <code>&quot;burst&quot;;q=100;w=60</code></li>
<li><code>retry-after</code>: The number of seconds, rounded up, until more capacity is available. Note, this header is only returned when the request has exceeded the rate limit.</li>
</ul>
<p><a href="/fundamentals/api/reference/sdks/">Cloudflare's SDKs</a> will also automatically work with the headers and back off in response to rate limits.</p>
