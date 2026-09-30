<pre><code>&quot;If your account includes zones with different Cloudflare plans, the above limits are shared between all the zones with the same plan. For example, all the zones in your account with a Pro plan will share the limits for the Pro plan, and all the zones in your account with a Business plan will share the limits for the Business plan.&quot;;&#10;</code></pre>
<p>Cloudflare's Instant Purge ensures that updates to your content are reflected immediately. Multiple options are available for purging content, with single-file cache purging (purge by URL) being the recommended method. However, the following additional options are also available:</p>
<ul class="directory-listing"><li><a href="/cache/how-to/purge-cache/purge-by-single-file/">Purge by single-file</a></li><li><a href="/cache/how-to/purge-cache/purge-everything/">​Purge everything</a></li><li><a href="/cache/how-to/purge-cache/purge-by-tags/">Purge cache by cache-tags</a></li><li><a href="/cache/how-to/purge-cache/purge-by-hostname/">​Purge cache by hostname</a></li><li><a href="/cache/how-to/purge-cache/purge_by_prefix/">​Purge cache by prefix (URL)</a></li><li><a href="/cache/how-to/purge-cache/purge-cache-key/">Purge cache key resources</a></li><li><a href="/cache/how-to/purge-cache/purge-varied-images/">P​urge varied images</a></li><li><a href="/cache/how-to/purge-cache/purge-zone-versions/">Purge zone versions via API</a></li></ul>
<p>To purge cached content using the Cloudflare API, refer to <a href="/api/resources/cache/methods/purge/">Purge Cached Content</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3873.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3872.md")
</aside>
<h2 id="availability-and-limits">Availability and limits</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Purge options</td>
<td>URL, Hostname, Tag, Prefix, and Purge Everything</td>
<td>URL, Hostname, Tag, Prefix, and Purge Everything</td>
<td>URL, Hostname, Tag, Prefix, and Purge Everything</td>
<td>URL, Hostname, Tag, Prefix, and Purge Everything</td>
</tr>
</tbody>
</table>
<h3 id="hostname-tag-prefix-url-and-purge-everything-limits">Hostname, tag, prefix URL, and purge everything limits</h3>
<p>The current purge limits are applied per <strong>account</strong>:</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Requests</td>
<td>5 requests per minute</td>
<td>5 requests per second</td>
<td>10 requests per second</td>
<td>50 requests per second</td>
</tr>
<tr>
<td>Bucket size</td>
<td>25</td>
<td>25</td>
<td>50</td>
<td>500</td>
</tr>
<tr>
<td>Max operations per request</td>
<td>100</td>
<td>100</td>
<td>100</td>
<td>100</td>
</tr>
</tbody>
</table>
<p>{limitsDetails}</p>
<h3 id="single-file-purge-limits">Single-file purge limits</h3>
<p>The current purge limits are applied per <strong>account</strong>:</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>URLs</td>
<td>800 URLs per second</td>
<td>1500 URLs per second</td>
<td>1500 URLs per second</td>
<td>3000 URLs per second</td>
</tr>
<tr>
<td>Max operations per request</td>
<td>100</td>
<td>100</td>
<td>100</td>
<td>500</td>
</tr>
</tbody>
</table>
<p>{limitsDetails}</p>
<p>Note that the thresholds for URLs are calculated using a moving average.</p>
<h3 id="token-bucket-rate-limiting">Token bucket rate limiting</h3>
<p>Cloudflare uses token bucket rate limiting to limit the number of purge requests flowing through the system at any given time, ensuring a steady and manageable flow.</p>
<p>Each account tier has a defined request rate (for example, Free: 5 requests per minute, Business: 10 requests per second), and requests are only allowed if there are available tokens in the bucket. Tokens refill at a consistent rate, but each bucket has a maximum capacity (for example, Free: 25 tokens, Enterprise: 500 tokens), allowing short bursts of requests if tokens have accumulated.</p>
<p>If the bucket is empty, further requests must wait until new tokens are added. This system maintains fair usage while allowing occasional bursts within the bucket's capacity.</p>
<p>If you are an Enterprise customer and you need more operations, reach out to your account team for support.</p>
