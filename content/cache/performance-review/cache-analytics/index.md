<p>Cache Analytics shows how much of your site's traffic is served from Cloudflare's cache versus your origin server. When content is served from cache, visitors get faster page loads and your origin web server handles less traffic. Use Cache Analytics to identify resources that are <a href="/cache/concepts/cache-responses/#miss">missing from cache</a>, <a href="/cache/concepts/cache-responses/#expired">expired</a> (cached copy is outdated), or <a href="/cache/concepts/cache-responses/#noneunknown">ineligible for caching</a> (not eligible for caching). You can filter by hostname, review the top URLs that miss cache, and query up to three days of data.</p>
<h2 id="availability">Availability</h2>
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
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Retention period</td>
<td>N/A</td>
<td>7 days</td>
<td>30 days</td>
<td>30 days</td>
</tr>
</tbody>
</table>
<h2 id="access-cache-analytics">Access Cache Analytics</h2>
<p>In the Cloudflare dashboard, go to the <strong>Caching</strong> page.</p>
<div class="nb-dash-button"></div>
<h2 id="requests-vs-data-transfer">Requests vs Data Transfer</h2>
<p>You can decide whether to focus on <strong>Requests</strong> or <strong>Data Transfer</strong>:</p>
<ul>
<li><strong>Requests</strong> (default view) helps assess performance. Each cache <a href="/cache/concepts/cache-responses/#miss">MISS</a> means the request must go to your origin server instead of being served from Cloudflare's cache, which adds latency.</li>
<li><strong>Data Transfer</strong> is useful for cost analysis, since most hosting providers charge for data sent from their servers (egress bandwidth).</li>
</ul>
<p>You can switch between these views while keeping other analytics filters applied.</p>
<p>For best practices related to Cache Analytics, refer to <a href="/cache/performance-review/cache-performance/">Cache performance</a>.</p>
<h2 id="add-filters">Add filters</h2>
<p>Create filters to narrow the data to specific traffic segments. Example filters include <strong>Cache status</strong>, <strong>Host</strong>, <strong>Path</strong>, or <strong>Content type</strong>.</p>
<p>To add filters, under <strong>Cache Performance</strong>, select <strong>Add filter</strong>. Select <strong>Apply</strong> when you are done.</p>
<h2 id="review-cache-status">Review cache status</h2>
<p>The <strong>Requests summary</strong> graph shows how your traffic changes over time, such as in response to a high-traffic event or a recent configuration change. The Requests summary is based on a sample of requests, not the full dataset. Totals are extrapolated from the sample to represent overall traffic. For more information on how sampling works, refer to <a href="/analytics/sampling/">Understanding sampling in Cloudflare Analytics</a>.</p>
<p><strong>Served by Cloudflare</strong> indicates content served by Cloudflare that did not require contacting your origin web server. <strong>Served by Origin</strong> indicates traffic served from the origin web server.</p>
<p>Revalidated requests — where Cloudflare checks with your origin to confirm cached content is still current — are counted differently depending on the view. In the <strong>Data Transfer</strong> view, revalidated requests count as <strong>Served by Cloudflare</strong> because the response body is served from cache, not re-downloaded from the origin. In the <strong>Requests</strong> view, revalidated requests count as <strong>Served by Origin</strong> because Cloudflare still contacts the origin server to verify the content.</p>
<p><strong>Cache status</strong> graphs break down why traffic is served from Cloudflare versus the origin web server, organized by content type.</p>
<p>For a breakdown of cache statuses and their descriptions, refer to <a href="/cache/concepts/cache-responses/">Cloudflare cache responses</a>.</p>
<h2 id="review-requests-by-source">Review requests by source</h2>
<p>Cache Analytics shows the most frequent values (top N) for several request attributes. Apply filters before reviewing these metrics to focus on specific traffic. For example, filtering to only view traffic with an Expired or Revalidated cache status shows which URLs were primarily responsible for those statuses.</p>
<h3 id="empty-content-types">Empty content types</h3>
<p>Finding an <strong>empty</strong> content type in your analytics is common. Responses to redirect status codes (<code>301</code>/<code>302</code>) typically do not include content, so they have no content type. Similarly, many HTTP error responses, such as <code>403</code>, do not return <code>text/html</code> and are also reported as empty.</p>
