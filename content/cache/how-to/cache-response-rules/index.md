<p>Cache Response Rules allow you to configure cache settings based on request and response attributes. These rules execute prior to caching in the <code>http_response_cache_settings</code> phase, which runs after Cloudflare receives the origin response.</p>
<p>With Cache Response Rules you can:</p>
<ul>
<li>Modify <code>Cache-Control</code> directives sent by your origin.</li>
<li>Modify cache tags on responses for targeted <a href="/cache/how-to/purge-cache/">cache purging</a>.</li>
<li>Strip headers (<code>ETag</code>, <code>Set-Cookie</code>, <code>Last-Modified</code>) from origin responses before caching.</li>
</ul>
<p>Cache Response Rules apply to both cached and non-cached (dynamic) responses from the origin. For example, you can strip Set-Cookie headers from responses that are not eligible for caching.</p>
<p>Cache Response Rules can be created in the <a href="/cache/how-to/cache-response-rules/create-dashboard/">dashboard</a>, via <a href="/cache/how-to/cache-response-rules/create-api/">API</a>, or <a href="/cache/how-to/cache-response-rules/terraform-example/">Terraform</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3922.md")
</aside>
<h2 id="availability">Availability</h2>
<p>The following table describes Cache Response Rules availability per plan.</p>
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
<td>Number of rules</td>
<td>10</td>
<td>25</td>
<td>50</td>
<td>300</td>
</tr>
</tbody>
</table>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>When troubleshooting Cache Response Rules, use <a href="/rules/trace-request/">Cloudflare Trace</a> to determine if a rule is triggering for a specific URL.</p>
<h2 id="relationship-with-cache-rules">Relationship with Cache Rules</h2>
<p>Cache Response Rules operate on the origin response, while <a href="/cache/how-to/cache-rules/">Cache Rules</a> operate on the incoming request. When settings from both rule types conflict, Cache Response Rules take precedence.</p>
<p>Key differences:</p>
<ul>
<li><strong>Cache eligibility</strong>: Cache Rules remain the only mechanism to decide whether content is eligible for caching. However, Cache Response Rules can make a cacheable asset non-cacheable by setting the <code>no-store</code> directive using the <code>set_cache_control</code> action.</li>
<li><strong>Origin Cache Control (OCC)</strong>: If any rule in the <code>http_response_cache_settings</code> phase matches, Cloudflare defaults to Origin Cache Control behavior (<code>origin_cache_control = true</code>).</li>
<li><strong>CDN-Cache-Control precedence</strong>: <code>Cache-Control</code> directives set by Cache Response Rules take precedence over origin-set <code>Cloudflare-CDN-Cache-Control</code> and <code>CDN-Cache-Control</code> headers. For more information, refer to <a href="/cache/concepts/cdn-cache-control/#header-precedence">CDN-Cache-Control header precedence</a>.</li>
<li><strong>Stacking</strong>: Cache Response Rules stack the same way as Cache Rules. When multiple rules specify the same setting, the last matching rule wins.</li>
</ul>
<h3 id="example-occ-precedence-over-edge-ttl">Example: OCC precedence over Edge TTL</h3>
<p>Consider the following scenario:</p>
<ol>
<li>A Cache Rule sets <strong>Edge TTL</strong> to <code>override_origin</code> with a value of <code>7200</code> seconds (2 hours).</li>
<li>A Cache Response Rule uses <code>set_cache_control</code> to set <code>s-maxage</code> to <code>3600</code> seconds (1 hour) with <code>cloudflare_only</code> enabled.</li>
<li>The origin responds with <code>Cache-Control: s-maxage=600</code>.</li>
</ol>
<p>In this case, the Cache Response Rule takes precedence. Cloudflare caches the asset for <code>3600</code> seconds (1 hour) based on the <code>s-maxage</code> directive set by the Cache Response Rule, while visitors still receive the original <code>s-maxage=600</code> from the origin because <code>cloudflare_only</code> is enabled.</p>
<h2 id="difference-from-workers-and-transform-rules">Difference from Workers and Transform Rules</h2>
<p>Workers and <a href="/rules/transform/response-header-modification/">Response Header Transform Rules</a> execute after the caching decision has been made and cannot influence whether or how a response is cached. Only <a href="/cache/how-to/cache-response-rules/">Cache Response Rules</a> can modify caching behavior based on origin response headers.</p>
<p>If you need to override <code>Cache-Control</code> directives from the origin (for example, remove <code>private</code> or add <code>s-maxage</code>), use a <a href="/cache/how-to/cache-response-rules/">Cache Response Rule</a> — not a Worker or Transform Rule.</p>
<h2 id="notes">Notes</h2>
<ul>
<li>If you strip last modified then Smart Edge Revalidation will be turned off.</li>
<li>Cache Response Rules ignore <a href="/support/troubleshooting/http-status-codes/1xx-informational/"><code>1xx</code> HTTP response status codes</a> as they are treated as informational responses.</li>
<li>Cache Response Rules can be versioned. Refer to the <a href="/version-management/">Version Management</a> documentation for more information.</li>
</ul>
