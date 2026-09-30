<p>Review detailed logs for your Zero Trust organization.</p>
<ul class="directory-listing"><li><a href="/cloudflare-one/insights/logs/dashboard-logs/">Dashboard logs</a></li><li><a href="/cloudflare-one/insights/logs/logpush/">Logpush integration</a></li></ul>
<h2 id="log-retention">Log retention</h2>
<p>Cloudflare stores Zero Trust logs for different periods of time based on the service and plan type:</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Standard</th>
<th>Access</th>
<th>Gateway</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Admin logs</strong></td>
<td>18 months</td>
<td>18 months</td>
<td>18 months</td>
<td>18 months</td>
<td>18 months</td>
</tr>
<tr>
<td><strong>Access logs</strong></td>
<td>24 hours</td>
<td>30 days</td>
<td>30 days</td>
<td>24 hours</td>
<td>180 days</td>
</tr>
<tr>
<td><strong>DNS logs</strong></td>
<td>24 hours</td>
<td>30 days</td>
<td>24 hours</td>
<td>30 days</td>
<td>180 days<sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td><strong>Network logs</strong></td>
<td>24 hours</td>
<td>30 days</td>
<td>24 hours</td>
<td>30 days</td>
<td>30 days</td>
</tr>
<tr>
<td><strong>HTTP logs</strong></td>
<td>24 hours</td>
<td>30 days</td>
<td>24 hours</td>
<td>30 days</td>
<td>30 days</td>
</tr>
<tr>
<td><strong>DEX logs</strong></td>
<td>7 days</td>
<td>7 days</td>
<td>7 days</td>
<td>7 days</td>
<td>7 days</td>
</tr>
<tr>
<td><strong>Device posture logs</strong></td>
<td>30 days</td>
<td>30 days</td>
<td>30 days</td>
<td>30 days</td>
<td>30 days</td>
</tr>
</tbody>
</table>
<h2 id="log-explorer">Log Explorer <span class="nb-badge">Beta</span></h2>
<p>Log Explorer users can store Zero Trust logs directly within Cloudflare in an <a href="/r2/">R2 bucket</a> and access them with the dashboard or API. Log Explorer supports the following Zero Trust datasets:</p>
<ul>
<li><a href="/logs/logpush/logpush-job/datasets/account/access_requests/">Access requests</a> (<code>FROM access_requests</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/casb_findings/">CASB Findings</a> (<code>FROM casb_findings</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/device_posture_results/">Device posture results</a> (<code>FROM device_posture_results</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/gateway_dns/">Gateway DNS</a> (<code>FROM gateway_dns</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/gateway_http/">Gateway HTTP</a> (<code>FROM gateway_http</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/gateway_network/">Gateway Network</a> (<code>FROM gateway_network</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a> (<code>FROM zero_trust_network_sessions</code>)</li>
</ul>
<p>For more information, refer to <a href="/log-explorer/">Log Explorer</a>.</p>
<h2 id="customer-metadata-boundary">Customer Metadata Boundary</h2>
<p>You can use Cloudflare Zero Trust with the Data Localization Suite to restrict data storage to a specific geographic region. For more information, refer to <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary</a>.</p>
<h2 id="data-privacy">Data privacy</h2>
<p>For more information on how we use this data, refer to our <a href="https://www.cloudflare.com/application/privacypolicy/">Privacy Policy</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Enterprise users on per query plans cannot store DNS logs via Cloudflare. You can still export logs via [Logpush](/cloudflare-one/insights/logs/logpush/). For more information, contact your account team.</li></ol></section>
