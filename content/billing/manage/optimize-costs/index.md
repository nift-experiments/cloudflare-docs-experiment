<p>Reducing usage-based charges starts with understanding where your consumption comes from. Use the <a href="/billing/manage/billable-usage/">billable usage dashboard</a> to identify which products are driving costs, then apply the strategies below.</p>
<h2 id="general-strategies">General strategies</h2>
<table>
<thead>
<tr>
<th>Strategy</th>
<th>Impact</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set up <a href="/billing/manage/budget-alerts/">budget alerts</a> to catch unexpected spikes early</td>
<td>Prevents surprise invoices across all products</td>
</tr>
<tr>
<td>Review the <a href="/billing/manage/billable-usage/">billable usage dashboard</a> weekly to identify cost trends</td>
<td>Catches runaway costs before the invoice arrives</td>
</tr>
<tr>
<td>Understand <a href="/billing/understand/how-charges-accrue/">how charges accrue</a> across the request lifecycle</td>
<td>Identifies which stage of a request generates the most cost</td>
</tr>
</tbody>
</table>
<h2 id="per-product-optimization">Per-product optimization</h2>
<h3 id="cache-and-cdn">Cache and CDN</h3>
<p>Cached responses are the cheapest path through Cloudflare. Every cache hit avoids origin fetch costs, Argo routing charges, and Workers execution.</p>
<table>
<thead>
<tr>
<th>Strategy</th>
<th>What it reduces</th>
</tr>
</thead>
<tbody>
<tr>
<td>Increase cache hit ratio with longer TTLs and appropriate <code>Cache-Control</code> headers</td>
<td>Argo data transfer, Workers invocations, origin load</td>
</tr>
<tr>
<td>Use <a href="/cache/advanced-configuration/cache-reserve/">Cache Reserve</a> for long-tail content that is accessed infrequently</td>
<td>Origin fetches — keeps content cached even when it would normally be evicted</td>
</tr>
<tr>
<td>Use <a href="/cache/how-to/tiered-cache/">tiered caching</a> to reduce origin pulls</td>
<td>Origin bandwidth and Argo transfer between Cloudflare data centers</td>
</tr>
<tr>
<td>Configure <a href="/cache/how-to/cache-rules/">cache rules</a> to cache more static content by default</td>
<td>Overall cache hit ratio</td>
</tr>
</tbody>
</table>
<h3 id="workers-durable-objects">Workers &amp; Durable Objects</h3>
<table>
<thead>
<tr>
<th>Strategy</th>
<th>What it reduces</th>
</tr>
</thead>
<tbody>
<tr>
<td>Use <a href="/workers/observability/logs/workers-logs/">Workers Logs</a> for log retention instead of Logpush</td>
<td>Logpush-enabled Workers requests and Logpush data transfer</td>
</tr>
<tr>
<td>Use the <a href="/durable-objects/best-practices/websockets/#durable-objects-hibernation-websocket-api">WebSocket Hibernation API</a> for Durable Objects with idle WebSocket connections</td>
<td>Duration (GB-s) charges — billing pauses while the Durable Object is hibernated</td>
</tr>
</tbody>
</table>
<h3 id="r2">R2</h3>
<table>
<thead>
<tr>
<th>Strategy</th>
<th>What it reduces</th>
</tr>
</thead>
<tbody>
<tr>
<td>Use <a href="/r2/buckets/object-lifecycles/">R2 lifecycle rules</a> to transition cold data to the Infrequent Access storage class</td>
<td>Storage costs for archival data</td>
</tr>
<tr>
<td>Batch R2 operations where possible instead of per-object reads</td>
<td>Class B operation count</td>
</tr>
<tr>
<td>Use <a href="/r2/api/s3/presigned-urls/">presigned URLs</a> for direct client access instead of proxying through Workers</td>
<td>Workers invocations and CPU time</td>
</tr>
<tr>
<td>Enable <a href="/r2/buckets/public-buckets/">Cache-Control headers on R2 objects</a> to leverage Cloudflare's CDN cache</td>
<td>Class B reads — cached objects do not hit R2</td>
</tr>
</tbody>
</table>
<h3 id="stream-and-images">Stream and Images</h3>
<table>
<thead>
<tr>
<th>Strategy</th>
<th>What it reduces</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set appropriate cache headers on Stream embed pages</td>
<td>Repeated Stream delivery minutes</td>
</tr>
<tr>
<td>Use <a href="/images/optimization/features/">Image Resizing URL format</a> with width/height parameters to serve appropriately sized variants</td>
<td>Transformation count — sized variants are cached</td>
</tr>
</tbody>
</table>
<h3 id="load-balancing">Load Balancing</h3>
<table>
<thead>
<tr>
<th>Strategy</th>
<th>What it reduces</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set health check intervals to the longest acceptable value for your availability requirements</td>
<td>DNS queries to load-balanced hostnames</td>
</tr>
<tr>
<td>Use fewer health check regions where regional redundancy is not critical</td>
<td>Health check frequency multiplier</td>
</tr>
</tbody>
</table>
<h2 id="monitor-and-alert">Monitor and alert</h2>
<p>Visibility is the foundation of cost optimization. Cloudflare provides two complementary tools:</p>
<ol>
<li><strong><a href="/billing/manage/billable-usage/">Billable usage dashboard</a></strong> — shows daily usage-based costs per product with a chart and sortable table. Available to Pay-as-you-go accounts.</li>
<li><strong><a href="/billing/manage/budget-alerts/">Budget alerts</a></strong> — sends an email notification when your total spend crosses a dollar threshold you define.</li>
</ol>
<p>For per-product usage notifications (bytes, requests, minutes), configure <a href="/billing/understand/usage-based-billing/#set-up-usage-notifications">usage-based billing notifications</a> in the Cloudflare dashboard.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/billing/understand/how-charges-accrue/">How charges accrue</a> — Follow a request and see which products generate charges</li>
<li><a href="/billing/understand/usage-based-billing/">Usage-based billing</a> — Products table with free tiers and overage rates</li>
<li><a href="/billing/manage/billable-usage/">Monitor billable usage</a> — Track daily usage-based costs</li>
<li><a href="/billing/manage/budget-alerts/">Budget alerts</a> — Get notified when spend crosses a threshold</li>
</ul>
