<p>When you use both <a href="/cache/how-to/cache-rules/">Cache Rules</a> and <a href="/workers/">Workers</a> on the same request, the Worker's cache settings take priority — but only when the required <a href="#compatibility-flags">compatibility flags</a> are enabled.</p>
<p>Your Workers script can override Cache Rules behavior, whether the request is for a domain proxied through Cloudflare or a domain that is not. For example, if a Cache Rule is configured to bypass cache for <code>example.com/foo</code>, but your Workers script sets <code>cacheEverything: true</code> in the <a href="/workers/runtime-apis/request/#the-cf-property-requestinitcfproperties"><code>cf</code> object</a> of a <code>fetch()</code> request, the Worker's setting takes precedence and the response is cached.</p>
<h2 id="precedence-order">Precedence order</h2>
<p>Cache behavior is determined by the following order of precedence:</p>
<ol>
<li><a href="/workers/">Workers</a> script settings</li>
<li><a href="/cache/how-to/cache-rules/">Cache rules</a></li>
<li><a href="/rules/page-rules/">Page rules</a></li>
</ol>
<p>Workers override Cache Rules, and Cache Rules override Page Rules. When multiple rules at the same level match the same request, the <a href="/cache/how-to/cache-rules/order/">last matching rule wins</a> for any conflicting settings.</p>
<h2 id="compatibility-flags">Compatibility flags</h2>
<p>The override behavior is controlled by <a href="/workers/configuration/compatibility-flags/">compatibility flags</a> — configuration settings that opt your Worker into specific runtime behaviors. There are two flags because Workers have two ways to interact with the cache:</p>
<ul>
<li>For the <a href="/workers/runtime-apis/fetch/">Fetch API</a> (<code>fetch()</code> with <code>cf</code> properties): <code>request_cf_overrides_cache_rules</code></li>
<li>For the <a href="/workers/runtime-apis/cache/">Cache API</a> (<code>caches.default.put()</code> / <code>caches.default.match()</code>): <code>cache_api_request_cf_overrides_cache_rules</code></li>
</ul>
<p>These flags must be enabled to allow Workers scripts to override Cache Rules. If the correct flag is not enabled for the API you are using, your Worker's cache settings are silently ignored and Cache Rules apply instead.</p>
<h3 id="compatibility-date-behavior">Compatibility date behavior</h3>
<p>A Worker's <a href="/workers/configuration/compatibility-dates/">compatibility date</a> determines which flags are active by default. When you set a compatibility date, all flags with an enable date on or before that date are automatically turned on.</p>
<table>
<thead>
<tr>
<th>Flag</th>
<th>Enabled by default</th>
<th>Prerequisite</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>request_cf_overrides_cache_rules</code> (Fetch API)</td>
<td>Compatibility dates on or after <code>2025-04-02</code></td>
<td>None</td>
</tr>
<tr>
<td><code>cache_api_compat_flags</code></td>
<td>Compatibility dates on or after <code>2025-04-19</code></td>
<td>None</td>
</tr>
<tr>
<td><code>cache_api_request_cf_overrides_cache_rules</code> (Cache API)</td>
<td>Compatibility dates on or after <code>2025-05-19</code></td>
<td>Requires <code>cache_api_compat_flags</code></td>
</tr>
</tbody>
</table>
<p>The Cache API has an extra requirement: <code>cache_api_compat_flags</code> must be enabled for any compatibility flags to take effect on the Cache API. Without it, the Cache API ignores all compatibility flags, even ones you explicitly list in your configuration.</p>
<p>If your Worker uses a compatibility date before the dates listed above, you must manually add the flags to your configuration. Otherwise, cache behavior follows Cache Rules instead of the Worker's settings.</p>
<h3 id="example-older-compatibility-date">Example (Older compatibility date)</h3>
<p>A Cache Rule bypasses cache for <code>example.com/foo</code>. A Worker with a compatibility date before <code>2025-04-02</code> sets <code>cacheEverything: true</code> via <code>fetch()</code>. Because the compatibility date is too old for <code>request_cf_overrides_cache_rules</code> to be active by default, the Cache Rule wins and the response is not cached.</p>
<p>Similarly, if you use the Cache API and your compatibility date is before <code>2025-04-19</code>, <code>cache_api_compat_flags</code> is not active. Even if you manually add <code>cache_api_request_cf_overrides_cache_rules</code> to your configuration, it has no effect because the Cache API does not recognize compatibility flags without <code>cache_api_compat_flags</code>.</p>
