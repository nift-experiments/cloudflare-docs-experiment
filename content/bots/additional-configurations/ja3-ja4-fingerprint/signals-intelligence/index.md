<p>Bot Management customers can view aggregate intelligence data for each <a href="/bots/additional-configurations/ja3-ja4-fingerprint/">JA4 fingerprint</a> based on traffic across the Cloudflare network. Use this data to understand why a request received a specific bot score or to feed into your own machine learning models running in <a href="/workers/">Cloudflare Workers</a> or at your origin.</p>
<p>Specifically, for each JA4 fingerprint, you will be able to access the following information:</p>
<ul>
<li>The percentage of traffic associated with browsers that Cloudflare sees.</li>
<li>The percentage of traffic associated with known bots that Cloudflare sees.</li>
<li>The number of networks Cloudflare sees actively using this fingerprint.</li>
<li>The number of Cloudflare sites that see traffic from this fingerprint.</li>
<li>The frequency that fingerprint requests caches content and generates errors.</li>
</ul>
<p>You can also use these fields with <a href="/workers-ai/">Workers AI</a> to build custom machine learning models.</p>
<h2 id="signals-intelligence-fields">Signals Intelligence fields</h2>
<p>Signals Intelligence fields show observations about a particular JA4 that Cloudflare has seen globally over the last hour.</p>
<table>
<thead>
<tr>
<th><span style="width:170px">Field name</span></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>h2h3_ratio_1h</code></td>
<td>The ratio of HTTP/2 and HTTP/3 requests combined with the total number of requests for the JA4 fingerprint in the last hour. Higher values indicate a higher proportion of HTTP/2 and HTTP/3 requests compared to other protocol versions.</td>
</tr>
<tr>
<td><code>heuristic_ratio_1h</code></td>
<td>The ratio of requests with a <code>scoreSrc</code> value of &quot;heuristics&quot; for the JA4 fingerprint in the last hour. Higher values suggest a larger proportion of requests being flagged by heuristic-based scoring.</td>
</tr>
<tr>
<td><code>reqs_quantile_1h</code></td>
<td>The quantile position of the JA4 fingerprint based on the number of requests across all fingerprints in the last hour. Higher values indicate a relatively higher number of requests compared to other fingerprints.</td>
</tr>
<tr>
<td><code>uas_rank_1h</code></td>
<td>The rank of the JA4 fingerprint based on the number of distinct user agents across all fingerprints in the last hour. Lower values indicate a higher diversity of user agents associated with the fingerprint.</td>
</tr>
<tr>
<td><code>browser_ratio_1h</code></td>
<td>The ratio of requests originating from browser-based user agents for the JA4 fingerprint in the last hour. Higher values suggest a higher proportion of browser-based requests.</td>
</tr>
<tr>
<td><code>paths_rank_1h</code></td>
<td>The rank of the JA4 fingerprint based on the number of unique request paths across all fingerprints in the last hour. Lower values indicate a higher diversity of request paths associated with the fingerprint.</td>
</tr>
<tr>
<td><code>reqs_rank_1h</code></td>
<td>The rank of the JA4 fingerprint based on the number of requests across all fingerprints in the last hour. Lower values indicate a higher number of requests associated with the fingerprint.</td>
</tr>
<tr>
<td><code>cache_ratio_1h</code></td>
<td>The ratio of cacheable responses for the JA4 fingerprint in the last hour. Higher values suggest a higher proportion of responses that can be cached.</td>
</tr>
<tr>
<td><code>ips_rank_1h</code></td>
<td>The rank of the JA4 fingerprint based on the number of unique client IP addresses across all fingerprints in the last hour. Lower values indicate a higher number of distinct client IPs associated with the fingerprint.</td>
</tr>
<tr>
<td><code>ips_quantile_1h</code></td>
<td>The quantile position of the JA4 fingerprint based on the number of unique client IP addresses across all fingerprints in the last hour. Higher values indicate a relatively higher number of distinct client IPs compared to other fingerprints.</td>
</tr>
</tbody>
</table>
<p>If you want to use JA4 fingerprints and Signals Intelligence, your Workers script should be able to handle missing fields when Bot Management isn't able to calculate or populate JA4 Signals (for example, non-TLS traffic or when Bot Management is skipped). For Orange-to-Orange (O2O) scenarios where Bot Management is in effect, JA4 Signals correspond to the eyeball (end-user) connection and are preserved through the O2O chain, including O2O zone requests and any corresponding subrequests.</p>
<ul>
<li>The possibility that the JA4 fingerprint could be missing.</li>
<li>The possibility that the <code>ja4Signals</code> array could be missing (for example, if JA4 isn't available for the request).</li>
<li>Results with <code>NaN</code> or <code>Infinity</code> values will be excluded from the array.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3542.md")
</aside>
