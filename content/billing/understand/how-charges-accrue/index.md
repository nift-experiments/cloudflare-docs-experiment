<p>Every request to a Cloudflare-proxied domain can touch multiple products, each with its own billing dimension. This page walks through a realistic request lifecycle and shows which products generate charges at each stage.</p>
<p>Understanding this flow helps you predict costs, identify optimization opportunities, and make sense of your invoice.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3362.md")
</aside>
<h2 id="a-request-through-a-pro-zone">A request through a Pro zone</h2>
<p>Consider a visitor loading a page on a Pro domain that uses Workers, R2, Argo Smart Routing, and Cache Reserve. Here is what happens at each stage and which billable resources are involved.</p>
<h3 id="1-dns-resolution"><ol>
<li>DNS resolution</li>
</ol></h3>
<p>The visitor's browser resolves the domain. This DNS query is handled by Cloudflare's authoritative DNS.</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Billing impact</th>
</tr>
</thead>
<tbody>
<tr>
<td>DNS queries</td>
<td>Included in all plans at no extra charge. If you use Load Balancing, DNS queries to load-balanced hostnames are metered (first 500K included).</td>
</tr>
</tbody>
</table>
<h3 id="2-edge-request-and-tls"><ol start="2">
<li>Edge request and TLS</li>
</ol></h3>
<p>The request arrives at the nearest Cloudflare data center. Cloudflare terminates TLS and processes the request.</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Billing impact</th>
</tr>
</thead>
<tbody>
<tr>
<td>TLS/SSL</td>
<td>Included in all plans. Advanced Certificate Manager and SSL for SaaS have separate pricing.</td>
</tr>
</tbody>
</table>
<h3 id="3-cache-lookup"><ol start="3">
<li>Cache lookup</li>
</ol></h3>
<p>Cloudflare checks whether a cached response exists for this request.</p>
<p><strong>Cache hit</strong> — the response is served directly from the edge. No origin fetch occurs. This is the cheapest path.</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Billing impact</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bandwidth</td>
<td>Included in all plans. Cloudflare does not charge for bandwidth.</td>
</tr>
<tr>
<td>Cache Reserve reads</td>
<td>If Cache Reserve is enabled and the asset is served from tiered cache storage, reads are metered. Refer to <a href="/cache/advanced-configuration/cache-reserve/">Cache Reserve pricing</a> for current rates.</td>
</tr>
</tbody>
</table>
<p><strong>Cache miss</strong> — the request must be forwarded to the origin. Continue to step 4.</p>
<h3 id="4-argo-smart-routing-if-enabled"><ol start="4">
<li>Argo Smart Routing (if enabled)</li>
</ol></h3>
<p>If Argo is enabled, Cloudflare routes the request through the fastest path across its network to your origin.</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Billing impact</th>
</tr>
</thead>
<tbody>
<tr>
<td>Argo data transfer</td>
<td>Metered per GB transferred between Cloudflare and your origin. First 1 GB included. Refer to <a href="/argo-smart-routing/">Argo Smart Routing</a> for current rates.</td>
</tr>
</tbody>
</table>
<h3 id="5-workers-execution-if-configured"><ol start="5">
<li>Workers execution (if configured)</li>
</ol></h3>
<p>If a Worker is bound to the route, it executes before or instead of fetching from the origin.</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Billing impact</th>
</tr>
</thead>
<tbody>
<tr>
<td>Worker requests</td>
<td>Metered per invocation. Workers Paid plan includes 10 million requests. Refer to <a href="/workers/platform/pricing/">Workers pricing</a> for current rates.</td>
</tr>
<tr>
<td>Worker CPU time</td>
<td>Metered per millisecond of CPU time. 30 million CPU-ms included. Refer to <a href="/workers/platform/pricing/">Workers pricing</a> for current rates.</td>
</tr>
<tr>
<td>Workers KV reads/writes</td>
<td>If the Worker reads from or writes to KV, each operation is metered separately. Refer to <a href="/kv/platform/pricing/">KV pricing</a> for current rates.</td>
</tr>
</tbody>
</table>
<h3 id="6-origin-fetch-and-response"><ol start="6">
<li>Origin fetch and response</li>
</ol></h3>
<p>If the Worker or cache miss triggers an origin fetch, Cloudflare retrieves the response from your origin server.</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Billing impact</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bandwidth</td>
<td>No charge for data transfer between Cloudflare and your origin (no egress fees).</td>
</tr>
</tbody>
</table>
<h3 id="7-r2-storage-operations-if-used"><ol start="7">
<li>R2 storage operations (if used)</li>
</ol></h3>
<p>If the Worker or origin logic reads from or writes to R2, each operation is metered.</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Billing impact</th>
</tr>
</thead>
<tbody>
<tr>
<td>R2 Class A operations (writes)</td>
<td>First 1 million included. Refer to <a href="/r2/pricing/">R2 pricing</a> for current rates.</td>
</tr>
<tr>
<td>R2 Class B operations (reads)</td>
<td>First 10 million included. Refer to <a href="/r2/pricing/">R2 pricing</a> for current rates.</td>
</tr>
<tr>
<td>R2 storage</td>
<td>First 10 GB-month included. Refer to <a href="/r2/pricing/">R2 pricing</a> for current rates.</td>
</tr>
<tr>
<td>R2 data egress</td>
<td>Free. Cloudflare does not charge for R2 egress.</td>
</tr>
</tbody>
</table>
<h3 id="8-cache-write-miss-path"><ol start="8">
<li>Cache write (miss path)</li>
</ol></h3>
<p>After fetching from the origin, Cloudflare caches the response at the edge for future requests.</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Billing impact</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cache Reserve writes</td>
<td>If Cache Reserve is enabled, writes are metered. Refer to <a href="/cache/advanced-configuration/cache-reserve/">Cache Reserve pricing</a> for current rates.</td>
</tr>
</tbody>
</table>
<h3 id="9-image-resizing-if-configured"><ol start="9">
<li>Image Resizing (if configured)</li>
</ol></h3>
<p>If the request triggers Image Resizing (via URL parameters or a Worker), the transformation is metered.</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Billing impact</th>
</tr>
</thead>
<tbody>
<tr>
<td>Image transformations</td>
<td>First 50,000 included on the Business plan, then metered per request. Refer to <a href="/images/pricing/">Images pricing</a> for current rates.</td>
</tr>
</tbody>
</table>
<h3 id="10-response-delivered"><ol start="10">
<li>Response delivered</li>
</ol></h3>
<p>The final response is sent to the visitor. No additional charges apply at this stage.</p>
<h2 id="what-this-means-for-your-invoice">What this means for your invoice</h2>
<p>A single page load can generate dozens of requests. Each request may touch a different combination of the products above. Your monthly invoice aggregates all of these individual operations across all requests, all domains, and the full billing period.</p>
<p>The key takeaway: <strong>cached responses are the cheapest path</strong>. Every cache hit avoids origin fetch costs, Argo routing charges, Workers execution, and R2 operations. Optimizing your cache hit ratio is the single most effective way to reduce usage-based charges.</p>
<h2 id="cost-optimization-strategies">Cost optimization strategies</h2>
<table>
<thead>
<tr>
<th>Strategy</th>
<th>Products affected</th>
<th>Impact</th>
</tr>
</thead>
<tbody>
<tr>
<td>Maximize cache hit ratio with appropriate Cache-Control headers</td>
<td>Argo, Workers, origin bandwidth</td>
<td>High — every cache hit eliminates origin-side costs</td>
</tr>
<tr>
<td>Use Cache Reserve for long-tail content</td>
<td>Cache, origin</td>
<td>Medium — reduces origin fetches for infrequently accessed content</td>
</tr>
<tr>
<td>Set appropriate TTLs to avoid unnecessary revalidation</td>
<td>Cache, Argo</td>
<td>Medium — reduces origin round-trips</td>
</tr>
<tr>
<td>Use Workers Smart Placement to run Workers closer to your data</td>
<td>Workers CPU time</td>
<td>Medium — reduces execution time for data-dependent Workers</td>
</tr>
<tr>
<td>Use R2 lifecycle rules to move infrequently accessed data to Infrequent Access tier</td>
<td>R2 storage</td>
<td>Medium — reduces storage costs for archival data</td>
</tr>
<tr>
<td>Monitor usage with the <a href="/billing/manage/billable-usage/">billable usage dashboard</a></td>
<td>All usage-based products</td>
<td>High — visibility is the first step to optimization</td>
</tr>
<tr>
<td>Set up <a href="/billing/manage/budget-alerts/">budget alerts</a> to catch unexpected spikes</td>
<td>All usage-based products</td>
<td>High — prevents surprise invoices</td>
</tr>
</tbody>
</table>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/billing/understand/how-billing-works/">How Cloudflare billing works</a> — Billing lifecycle, charge types, and invoice structure</li>
<li><a href="/billing/understand/usage-based-billing/">Usage-based billing</a> — Which products use metered billing</li>
<li><a href="/billing/manage/billable-usage/">Monitor billable usage</a> — Track daily usage-based costs</li>
<li><a href="/billing/manage/budget-alerts/">Budget alerts</a> — Get notified when spend crosses a threshold</li>
</ul>
