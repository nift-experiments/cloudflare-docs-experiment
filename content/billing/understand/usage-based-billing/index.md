<p>For some Cloudflare subscriptions and services, Cloudflare charges you based on how much you used a feature during your previous billing period. This differs from other services, which are a prepaid flat fee for the upcoming month (for example, plans and page rules).</p>
<p>For example, if your billing date is on the 15th of the month and you turn on Cloudflare Workers in the dashboard on the 1st, your next invoice includes the Workers charges from the 1st through the 15th. The following invoice includes charges for Workers usage during the full billing period.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3349.md")
</aside>
<h2 id="products-with-usage-based-billing">Products with usage-based billing</h2>
<p>The following products bill based on consumption. Many products include a free tier or included usage — you are only charged for usage that exceeds the included amount.</p>
<p>For current overage rates, refer to the <a href="https://www.cloudflare.com/plans/">Cloudflare plans page</a> or each product's pricing page linked below. Rates may change — the links below are always up to date.</p>
<table>
<thead>
<tr>
<th>Product</th>
<th>Billable metric</th>
<th>Free tier or included usage</th>
<th>Pricing details</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/workers/platform/pricing/">Workers</a></td>
<td>Requests and CPU time</td>
<td>10M requests and 30M CPU-ms</td>
<td><a href="/workers/platform/pricing/">Workers pricing</a></td>
</tr>
<tr>
<td><a href="/r2/pricing/">R2</a></td>
<td>Storage and operations</td>
<td>10 GB storage, 1M Class A operations, and 10M Class B operations</td>
<td><a href="/r2/pricing/">R2 pricing</a></td>
</tr>
<tr>
<td><a href="/argo-smart-routing/">Argo Smart Routing</a></td>
<td>Data transfer</td>
<td>First 1 GB</td>
<td><a href="/argo-smart-routing/">Argo Smart Routing</a></td>
</tr>
<tr>
<td><a href="/cache/advanced-configuration/cache-reserve/">Cache Reserve</a></td>
<td>Reads, writes, and storage</td>
<td>None</td>
<td><a href="/cache/advanced-configuration/cache-reserve/">Cache Reserve</a></td>
</tr>
<tr>
<td><a href="/load-balancing/">Load Balancing</a></td>
<td>DNS queries</td>
<td>First 500K queries</td>
<td><a href="/load-balancing/">Load Balancing</a></td>
</tr>
<tr>
<td><a href="/stream/pricing/">Stream</a></td>
<td>Minutes stored and minutes viewed</td>
<td>Varies by plan</td>
<td><a href="/stream/pricing/">Stream pricing</a></td>
</tr>
<tr>
<td><a href="/images/pricing/">Images</a></td>
<td>Transformations and storage</td>
<td>Varies by plan</td>
<td><a href="/images/pricing/">Images pricing</a></td>
</tr>
<tr>
<td><a href="/spectrum/">Spectrum</a></td>
<td>Data transfer</td>
<td>None</td>
<td><a href="/spectrum/">Spectrum</a></td>
</tr>
<tr>
<td><a href="/waf/rate-limiting-rules/">Rate Limiting</a></td>
<td>Rule requests</td>
<td>Varies by plan</td>
<td><a href="/waf/rate-limiting-rules/">Rate Limiting</a></td>
</tr>
<tr>
<td><a href="/log-explorer/pricing/">Log Explorer</a></td>
<td>Log storage and queries</td>
<td>Varies by plan</td>
<td><a href="/log-explorer/pricing/">Log Explorer pricing</a></td>
</tr>
<tr>
<td><a href="/cloudflare-one/">Zero Trust</a></td>
<td>Seats and usage-based services</td>
<td>Varies by plan</td>
<td><a href="/cloudflare-one/">Zero Trust</a></td>
</tr>
<tr>
<td><a href="/vectorize/platform/pricing/">Vectorize</a></td>
<td>Stored dimensions and queried vectors</td>
<td>Varies by plan</td>
<td><a href="/vectorize/platform/pricing/">Vectorize pricing</a></td>
</tr>
<tr>
<td><a href="/analytics/analytics-engine/pricing/">Analytics Engine</a></td>
<td>Data points read and written</td>
<td>Varies by plan</td>
<td><a href="/analytics/analytics-engine/pricing/">Analytics Engine pricing</a></td>
</tr>
</tbody>
</table>
<h2 id="optimize-usage-based-costs">Optimize usage-based costs</h2>
<p>Reducing usage-based charges starts with understanding where your consumption comes from. Use the <a href="/billing/manage/billable-usage/">billable usage dashboard</a> to identify which products are driving costs, then apply the strategies below.</p>
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
<td>Use <a href="/cache/advanced-configuration/cache-reserve/">Cache Reserve</a> for long-tail content</td>
<td>Origin fetches for infrequently accessed assets</td>
</tr>
<tr>
<td>Set up <a href="/r2/buckets/object-lifecycles/">R2 lifecycle rules</a> to transition cold data to Infrequent Access</td>
<td>R2 storage costs</td>
</tr>
<tr>
<td>Use <a href="/workers/configuration/placement/">Workers Smart Placement</a> for data-heavy Workers</td>
<td>Workers CPU time</td>
</tr>
<tr>
<td>Batch R2 operations where possible instead of per-object reads</td>
<td>R2 Class B operation count</td>
</tr>
<tr>
<td>Set up <a href="/billing/manage/budget-alerts/">budget alerts</a> to catch unexpected spikes early</td>
<td>All products — prevents surprise invoices</td>
</tr>
</tbody>
</table>
<p>For a detailed walkthrough of how a single request generates charges across multiple products, refer to <a href="/billing/understand/how-charges-accrue/">How charges accrue</a>.</p>
<h2 id="monitor-your-usage">Monitor your usage</h2>
<p>The <a href="/billing/manage/billable-usage/">billable usage dashboard</a> gives Pay-as-you-go customers daily visibility into usage-based costs. The dashboard shows a daily cost breakdown chart and a per-product usage table with free-tier allowances, so you can see exactly what you are being charged for.</p>
<p>You can also set up <a href="/billing/manage/budget-alerts/">budget alerts</a> to get notified by email when your account-wide spend crosses a dollar threshold you define.</p>
<h2 id="usage-based-billing-notifications">Usage-based billing notifications</h2>
<p>If you are on a Professional plan or higher, you can monitor the usage of individual Cloudflare add-ons by turning on email notifications. Cloudflare sends a notification to the billing email address on file when traffic, queries, requests, or minutes watched exceed your defined threshold.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3348.md")
</aside>
<p>You can choose the product you want to monitor and the threshold that triggers the notification. Thresholds depend on the product.</p>
<p>For example, Argo Smart Routing has <strong>Notify when total bytes of traffic exceeds</strong> as a threshold, and Load Balancing has <strong>Notify when total number of DNS Queries exceeds</strong> as a threshold.</p>
<h3 id="set-up-usage-notifications">Set up usage notifications</h3>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</li>
<li>Select your account.</li>
<li>Go to <strong>Notifications</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="4">
<li>Select <strong>Add</strong> to create a new notification for <strong>Billable Usage</strong>.</li>
</ol>
<p>For more information, refer to <a href="/notifications/get-started/">Cloudflare notifications</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3347.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/billing/understand/how-charges-accrue/">How charges accrue</a> — How a request generates charges across products</li>
<li><a href="/billing/manage/billable-usage/">Monitor billable usage</a> — Track daily usage-based costs</li>
<li><a href="/billing/manage/budget-alerts/">Budget alerts</a> — Get notified when spend crosses a threshold</li>
<li><a href="/billing/understand/how-billing-works/">How Cloudflare billing works</a> — Billing lifecycle and charge types</li>
</ul>
