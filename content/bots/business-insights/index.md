<p><strong>Business Insights</strong> helps business decision-makers and content owners analyze bot traffic to their website over the last 24 hours, 7 days, or 30 days.</p>
<h2 id="availability">Availability</h2>
<p>Business Insights is available to all <a href="/bots/get-started/bot-management/">Enterprise Bot Management</a> customers.</p>
<p>Business Insights is an observability surface and does not provide controls. To mitigate bots, use <a href="/security/rules/">Security rules</a> or the <a href="/bots/additional-configurations/block-ai-bots/">AI bot management options</a>.</p>
<h2 id="access">Access</h2>
<div class="nb-dash-button"></div>
<p>You can also reach the dashboard from your zone-level <strong>Analytics</strong> &gt; <strong>Business Insights</strong> in the Cloudflare dashboard.</p>
<h2 id="definitions">Definitions</h2>
<p>The dashboard uses the following definitions:</p>
<ul>
<li><strong>Content pages</strong>: Content is initially defined as HTML pages on your website.</li>
<li><strong>Crawl-to-referral ratio, per bot operator</strong>: The average crawl-to-referral ratio (number of crawls sent by this company, vs. the number of visitors who visit you through a referral link from that company, tracked through UTM parameters) for a given company, in the selected time period.</li>
<li><strong>Crawl-to-referral ratio, site-wide</strong>: The average crawl-to-referral ratio (number of crawls sent by this company, vs. the number of visitors who visit you through a referral link from that company, tracked through UTM parameters) across all activity on your zone, in the selected time period.</li>
<li><strong>Classification</strong>: Each crawler is classified with Cloudflare's updated taxonomy. See <a href="/bots/concepts/bot/verified-bots/">Verified bot classifications</a> for more information. If the company has at least 1 bot with an AI use case, we label the operator with the &quot;AI&quot; label, plus provide this as a filter.</li>
<li><strong>Operator</strong>: An operator row aggregates requests from all bots associated with that operator.</li>
</ul>
<h3 id="outcome">Outcome</h3>
<p><strong>Outcome</strong> summarizes the HTTP responses for requests attributed to an operator.</p>
<table>
<thead>
<tr>
<th>Outcome</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Allowed</strong></td>
<td>All requests received successful HTTP responses (<code>2xx</code> or <code>3xx</code>).</td>
</tr>
<tr>
<td><strong>Blocked</strong></td>
<td>All requests received unsuccessful HTTP responses (status codes other than <code>2xx</code> or <code>3xx</code>).</td>
</tr>
<tr>
<td><strong>Partially blocked</strong></td>
<td>The requests include both successful and unsuccessful HTTP responses.</td>
</tr>
</tbody>
</table>
<p>For a <strong>Partially blocked</strong> row, the Outcome cell shows the successful and unsuccessful request counts.</p>
<p>Outcome is based on HTTP response status and does not identify the mitigation that a website owner configured for a request. Unsuccessful responses can include errors returned by the origin, such as <code>404</code> and <code>5xx</code> responses. To investigate a request, review its mitigation, edge status code, and origin status code in <a href="/waf/analytics/security-analytics/">Security Analytics</a>.</p>
