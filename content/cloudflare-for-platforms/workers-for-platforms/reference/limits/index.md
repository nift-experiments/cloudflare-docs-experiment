<h2 id="script-limits">Script limits</h2>
<p>Cloudflare provides an unlimited number of scripts for Workers for Platforms customers.</p>
<h2 id="cf-object"><code>cf</code> object</h2>
<p>The <a href="/workers/runtime-apis/request/#the-cf-property-requestinitcfproperties"><code>cf</code> object</a> contains Cloudflare-specific properties of a request. This field is not accessible in <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#user-workers">user Workers</a> by default because some fields in this object are sensitive and can be used to manipulate Cloudflare features (for example, <code>cacheKey</code>, <code>resolveOverride</code>, <code>scrapeShield</code>.)</p>
<p>To access the <code>cf</code> object, you need to enable <a href="/cloudflare-for-platforms/workers-for-platforms/reference/worker-isolation/#trusted-mode">trusted mode</a> for your namespace. Only enable this if you control all Worker code in the namespace.</p>
<h2 id="durable-object-namespace-limits">Durable Object namespace limits</h2>
<p>Workers for Platforms do not have a limit for the number of Durable Object namespaces.</p>
<h2 id="cache-api">Cache API</h2>
<p>For isolation, <code>caches.default</code> is disabled for namespaced scripts. To learn more about the cache, refer to <a href="/workers/reference/how-the-cache-works/">How the cache Works</a>.</p>
<h2 id="tags">​Tags</h2>
<p>You can set a maximum of eight tags per script. Avoid special characters like <code>,</code> and <code>&amp;</code> when naming your tag.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/4211.md")
</aside>
<h2 id="gradual-deployments">Gradual Deployments</h2>
<p><a href="/workers/versions-and-deployments/gradual-deployments/">Gradual Deployments</a> is not supported yet for user Workers. Changes made to user Workers create a new version that deployed all-at-once to 100% of traffic.</p>
<h2 id="api-rate-limits">API Rate Limits</h2>
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
@markup("md", "content/.markup/bodies/4210.md")
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
