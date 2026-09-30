<p>Customers can set cache time-to-live (TTL) based on the response status from the origin web server. Cache TTL refers to the duration of a resource in the Cloudflare network before being marked as <code>STALE</code> or discarded from cache. Status codes are returned by a resource's origin.</p>
<p>Setting cache TTL based on response status overrides the <a href="/cache/concepts/default-cache-behavior/">default cache behavior (standard caching)</a> for static files and overrides cache instructions sent by the origin web server. To cache non-static assets, set a <a href="/cache/how-to/cache-rules/create-api/#example-requests">Cache Level of Cache Everything using a Cache Rule</a>. Setting <code>no-store</code> <strong>Cache-Control</strong> or a low TTL (using <code>max-age</code>/<code>s-maxage</code>) increases requests to origin web servers and decreases performance.</p>
<h2 id="caching-limits">Caching limits</h2>
<p>The maximum caching limit for Free, Pro, and Business customers is 512 MB per file, and the maximum caching limit for Enterprise customers is 5 GB per file. If you need to raise the limits, contact your account team.</p>
<h2 id="edge-ttl">Edge TTL</h2>
<p>By default, Cloudflare caches certain HTTP response codes with the following Edge Cache TTL when a <code>cache-control</code> directive or <code>expires</code> response header are not present.</p>
<table>
<thead>
<tr>
<th>HTTP status code</th>
<th>Default TTL</th>
</tr>
</thead>
<tbody>
<tr>
<td>200, 206, 301</td>
<td>120m</td>
</tr>
<tr>
<td>302, 303</td>
<td>20m</td>
</tr>
<tr>
<td>404, 410</td>
<td>3m</td>
</tr>
</tbody>
</table>
<p>All other status codes are not cached by default.</p>
<h2 id="set-cache-ttl-by-response-status-via-the-cloudflare-dashboard">Set cache TTL by response status via the Cloudflare dashboard</h2>
<p>To set cache TTL by response status, <a href="/cache/how-to/cache-rules/">create a Cache Rule</a> for <a href="/cache/how-to/cache-rules/settings/#edge-ttl"><strong>Cache TTL by status code</strong></a>.</p>
<h2 id="set-cache-ttl-by-response-status-via-the-cloudflare-api">Set cache TTL by response status via the Cloudflare API</h2>
<pre><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;expression&quot;: &quot;(http.host eq \&quot;www.example.com\&quot;)&quot;,&#10;      &quot;description&quot;: &quot;set cache TTL by response status&quot;,&#10;      &quot;action&quot;: &quot;set_cache_settings&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;cache&quot;: true,&#10;        &quot;edge_ttl&quot;: {&#10;          &quot;status_code_ttl&quot;: [&#10;            {&#10;              &quot;status_code_range&quot;: {&#10;                &quot;to&quot;: 299&#10;              },&#10;              &quot;value&quot;: 86400&#10;            },&#10;            {&#10;              &quot;status_code_range&quot;: {&#10;                &quot;from&quot;: 300,&#10;                &quot;to&quot;: 499&#10;              },&#10;              &quot;value&quot;: 0  // no-cache&#10;            },&#10;            {&#10;              &quot;status_code_range&quot;: {&#10;                &quot;from&quot;: 500&#10;              },&#10;              &quot;value&quot;: -1  // no-store&#10;            }&#10;          ],&#10;          &quot;mode&quot;: &quot;respect_origin&quot;&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<h3 id="syntax">Syntax</h3>
<p>Provide a JSON object containing status codes and their corresponding TTLs. Each key-value pair in the cache TTL by status cache rule has the following syntax:</p>
<ul>
<li><code>status_code</code>: An integer value such as 200 or 500. <code>status_code</code> matches the exact status code from the origin web server. Valid status codes are between 100-999.</li>
<li><code>status_code_range</code>: Integer values for <code>from</code> and <code>to</code>. <code>status_code_range</code> matches any status code from the origin web server within the specified range.</li>
<li><code>value</code>: An integer value that defines the duration an asset is valid in seconds or one of the following strings: <code>no-store</code> (equivalent to <code>-1</code>), <code>no-cache</code> (equivalent to <code>0</code>).</li>
</ul>
<h2 id="set-cache-ttl-by-response-status-via-a-cloudflare-worker">Set cache TTL by response status via a Cloudflare Worker</h2>
<p>The <strong>cacheTtlByStatus</strong> option is a version of the <strong>cacheTtl</strong> feature that designates a cache TTL for a request’s response status code (for example, <code>{ &quot;200-299&quot;: 86400, 404: 1, &quot;500-599&quot;: 0 }</code>).</p>
<h2 id="ttl-handling-for-304-and-200-status-codes">TTL handling for 304 and 200 status codes</h2>
<ol>
<li>
<p>If a TTL is not explicitly set for status code <code>304</code>, we automatically set it to match the TTL of status code <code>200</code> (if the user has defined one for <code>200</code>).</p>
</li>
<li>
<p>If a user explicitly sets a different TTL for <code>304</code> than for <code>200</code>, the following behavior will occur:</p>
</li>
</ol>
<ul>
<li>When a <code>200</code> response is received, the asset is cached with the TTL specified for status <code>200</code>.</li>
<li>Once the asset expires and we revalidate with the origin, if the origin returns a <code>304</code>, the cache TTL is updated to the value set for <code>304</code>.</li>
</ul>
<p>For example, if a user specifies a TTL of one hour for status <code>200</code> and 0 seconds (cache and always revalidate) for status <code>304</code>, the asset will be cached for 1 hour. After it expires, we revalidate with the origin. If the origin returns a <code>304</code>, each subsequent request will trigger revalidation. If the origin continues to return <code>304</code>, this cycle will persist.</p>
<p>This behavior is likely undesirable unless the user has a specific use case. Therefore, users should ensure that the TTL for <code>304</code> matches the TTL for <code>200</code> unless they intentionally require this behavior.</p>
