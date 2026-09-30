<p>Origin Cache Control is a Cloudflare feature. When enabled on an Enterprise customer's website, it indicates that Cloudflare should strictly respect <code>Cache-Control</code> directives received from the origin server. Free, Pro and Business customers have this feature enabled by default.</p>
<p><code>Cache-Control</code> directives in the HTTP response from your origin server provide specific <a href="https://datatracker.ietf.org/doc/html/rfc7234">caching instructions</a> to intermediary services like Cloudflare.</p>
<p>With the Origin Cache Control feature enabled, <code>Cache-Control</code> directives present in the origin server's response will be followed as specified. For example, if the response includes a <code>max-age</code> directive of 3,600 seconds, Cloudflare will cache the resource for that duration before checking the origin server again for updates.</p>
<p>Cloudflare's <a href="/cache/how-to/cache-rules/">Cache Rules</a> allows users to either augment or override an origin server's <code>Cache-Control</code> headers or <a href="/cache/concepts/default-cache-behavior/">default policies</a> set by Cloudflare.</p>
<p>The following sections cover:</p>
<ul>
<li>The most common <code>Cache-Control</code> directives.</li>
<li>How to enable Origin Cache Control.</li>
<li>How Origin Cache Control behaves with <code>Cache-Control</code> directives.</li>
<li>How other Cloudflare products interact with <code>Cache-Control</code> directives.</li>
</ul>
<h2 id="cache-control-directives"><code>Cache-control</code> directives</h2>
<p>A <code>Cache-Control</code> header can include a number of directives, and the directive dictates who can cache a resource along with how long those resources can be cached before they must be updated.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3829.md")
</aside>
<p>If multiple directives are passed together, each directive is separated by a comma. If the directive takes an argument, it follows the directive separated by an equal sign. For example: <code>max-age=86400</code>.</p>
<p>Directives can be broken down into four groups: <a href="/cache/concepts/cache-control/#cacheability">cacheability</a>, <a href="/cache/concepts/cache-control/#expiration">expiration</a>, <a href="/cache/concepts/cache-control/#revalidation">revalidation</a>, and <a href="/cache/concepts/cache-control/#other">other</a>.</p>
<h3 id="cacheability">Cacheability</h3>
<p>Cacheability refers to whether or not a resource should enter a cache, and the directives below indicate a resource's cacheability.</p>
<ul>
<li><code>public</code> — Indicates any cache may store the response, even if the response is normally non-cacheable or cacheable only within a private cache.</li>
<li><code>private</code> — Indicates the response message is intended for a single user, such as a browser cache, and must not be stored by a shared cache like Cloudflare or a corporate proxy.</li>
<li><code>no-store</code> — Indicates any cache, such as a client or proxy cache, must not store any part of either the immediate request or response.</li>
</ul>
<h3 id="expiration">Expiration</h3>
<p>Expiration refers to how long a resource should remain in the cache, and the directives below affect how long a resource stays in the cache.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-1">Note</h3>
@markup("md", "content/.markup/bodies/3828.md")
</aside>
<ul>
<li><code>max-age=seconds</code> — Indicates the response is stale after its age is greater than the specified number of seconds. Age is defined as the time in seconds since the asset was served from the origin server. The <code>seconds</code> argument is an unquoted integer.</li>
<li><code>s-maxage=seconds</code> — Indicates that in shared caches, the maximum age specified by this directive overrides the maximum age specified by either the <code>max-age</code> directive or the <code>Expires</code> header field. The <code>s-maxage</code> directive also implies the semantics of the <code>proxy-revalidate</code> response directive. Browsers ignore <code>s-maxage</code>.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="s-maxage-disables-stale-while-revalidate">`s-maxage` disables `stale-while-revalidate`</h3>
@markup("md", "content/.markup/bodies/3827.md")
</aside>
* `no-cache` — Indicates the response cannot be used to satisfy a subsequent request without successful validation on the origin server. This allows an origin server to prevent a cache from using the origin to satisfy a request without contacting it, even by caches that have been configured to send stale responses.
<p>Ensure the HTTP <code>Expires</code> header is set in your origin server to use Greenwich Mean Time (GMT) as stipulated in <a href="https://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.3" title="3.3.1 Full Date">RFC 2616</a>.</p>
<h3 id="revalidation">Revalidation</h3>
<p>Revalidation determines how the cache should behave when a resource expires, and the directives below affect the revalidation behavior.</p>
<ul>
<li><code>must-revalidate</code> — Indicates that once the resource is stale, a cache (client or proxy) must not use the response to satisfy subsequent requests without successful validation on the origin server.</li>
<li><code>proxy-revalidate</code> — Has the same meaning as the <code>must-revalidate</code> response directive except that it does not apply to private client caches.</li>
<li><code>stale-while-revalidate=&lt;seconds&gt;</code> — When present in an HTTP response, indicates caches may serve the response in which it appears after it becomes stale, up to the indicated number of seconds since the resource expired. If <a href="/cache/how-to/always-online/">Always Online</a> is enabled, then the <code>stale-while-revalidate</code> and <code>stale-if-error</code> directives are ignored. This directive is not supported when using the Cache API methods <code>cache.match</code> or <code>cache.put</code>. For more information, refer to the <a href="/workers/runtime-apis/cache/#methods">Workers documentation for Cache API</a>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3826.md")
</aside>
<ul>
<li><code>stale-if-error=&lt;seconds&gt;</code> — Indicates that when an error is encountered, a cached stale response may be used to satisfy the request, regardless of other freshness information. To avoid this behavior, include <code>stale-if-error=0</code> directive with the object returned from the origin. This directive is not supported when using the Cache API methods <code>cache.match</code> or <code>cache.put</code>. For more information, refer to the <a href="/workers/runtime-apis/cache/#methods">Workers documentation for Cache API</a>.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="error-status-codes">Error status codes</h3>
@markup("md", "content/.markup/bodies/3825.md")
</aside>
<p>The <code>stale-if-error</code> directive is ignored if <a href="/cache/how-to/always-online/">Always Online</a> is enabled or if an explicit in-protocol directive is passed. Examples of explicit in-protocol directives include a <code>no-store</code> or <code>no-cache cache</code> directive, a <code>must-revalidate</code> cache-response-directive, or an applicable <code>s-maxage</code> or <code>proxy-revalidate</code> cache-response-directive.</p>
<h3 id="other">Other</h3>
<p>Additional directives that influence cache behavior are listed below.</p>
<ul>
<li><code>no-transform</code> — Indicates that an intermediary — regardless of whether it implements a cache — must not transform the payload.</li>
<li><code>vary</code> — By default, Cloudflare does not consider vary values in caching decisions. Vary values are respected when you configure the <a href="/cache/concepts/vary/">Cache Rules Vary setting</a>, when <a href="/cache/advanced-configuration/vary-for-images/">Vary for images</a> is configured, and when the vary header is <a href="/speed/optimization/content/compression/"><code>vary: accept-encoding</code></a>.</li>
<li><code>immutable</code> — Indicates to clients the response body does not change over time. The resource, if unexpired, is unchanged on the server. The user should not send a conditional revalidation request, such as <code>If-None-Match</code> or <code>If-Modified-Since</code>, to check for updates, even when the user explicitly refreshes the page. This directive has no effect on public caches like Cloudflare, but does change browser behavior.</li>
</ul>
<h3 id="understand-no-store-and-no-cache-directives">Understand <code>no-store</code> and <code>no-cache</code> directives</h3>
<p>There is often confusion between the directives <code>Cache-Control: no-store</code> and <code>Cache-Control: no-cache</code>, particularly regarding how they impact browser caching and features like the <a href="https://developer.mozilla.org/en-US/docs/Glossary/bfcache">Back-Forward Cache</a> (BFCache).</p>
<h4 id="no-store"><code>no-store</code></h4>
<ul>
<li>Tells both browsers and intermediaries (like CDNs) not to store a copy of the response under any circumstance.</li>
<li>The response is never written to disk or memory, which means the browser must fetch it again every time.</li>
<li>In many browsers, <code>no-store</code> disables BFCache, because restoring a page from BFCache requires the browser to keep a copy of the page's memory state, which contradicts the “do not store” directive.</li>
<li>This directive is used for highly sensitive or dynamic data (for example, banking apps, personal information, secure dashboards).</li>
</ul>
<h4 id="no-cache"><code>no-cache</code></h4>
<ul>
<li>Allows storing of the response (in both browser and intermediate caches), but requires revalidation with the origin server before using it.</li>
<li>This ensures the content is always up-to-date, while still potentially allowing BFCache or other forms of performance optimization.</li>
<li>This directive is used for data that changes frequently but is not sensitive, and can be served faster if validated rather than re-downloaded.</li>
</ul>
<p>For more information about how these directives behave when Origin Cache Control is enabled or disabled refer to the <a href="/cache/concepts/cache-control/#directives">Directives</a> section.</p>
<h2 id="enable-origin-cache-control">Enable Origin Cache Control</h2>
<p>If you enable Origin Cache Control, Cloudflare will aim to strictly adhere to <a href="https://datatracker.ietf.org/doc/html/rfc7234">RFC 7234</a>. Enterprise customers have the ability to select if Cloudflare will adhere to this behavior, enabling or disabling Origin Cache Control for their websites through cache rules in the <a href="/cache/how-to/cache-rules/settings/#origin-cache-control-enterprise-only">dashboard</a> or via <a href="/cache/how-to/cache-rules/settings/#origin-cache-control-enterprise-only">API</a>. Free, Pro, and Business customers have this option enabled by default and cannot disable it.</p>
<h2 id="origin-cache-control-behavior">Origin Cache Control behavior</h2>
<p>The following section covers the directives and behavioral conditions associated with enabling or disabling Origin Cache Control.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="integer-values-required">Integer values required</h3>
@markup("md", "content/.markup/bodies/3824.md")
</aside>
<h3 id="directives">Directives</h3>
<p>The table below lists directives and their behaviors when Origin Cache Control is disabled and when it is enabled.</p>
<table>
<thead>
<tr>
<th>Directive</th>
<th>Origin Cache Control Disabled Behavior</th>
<th>Origin Cache Control Enabled Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>s-maxage=0</code></td>
<td>Will not cache.</td>
<td>Caches and always revalidates</td>
</tr>
<tr>
<td><code>max-age=0</code></td>
<td>Will not cache.</td>
<td>Caches and always revalidates.</td>
</tr>
<tr>
<td><code>no-cache</code></td>
<td>Will not cache.</td>
<td>Caches and always revalidates. Does not serve stale.</td>
</tr>
<tr>
<td><code>no-cache=&lt;headers&gt;</code></td>
<td>Will not cache.</td>
<td>Caches if headers mentioned in <code>no-cache=&lt;headers&gt;</code> do not exist. Always revalidates if any header mentioned in <code>no-cache=&lt;headers&gt;</code> is present.</td>
</tr>
<tr>
<td><code>Private=&lt;headers&gt;</code></td>
<td>Will not cache.</td>
<td>Does not cache <code>&lt;headers&gt;</code> values mentioned in <code>Private=&lt;headers&gt;</code> directive.</td>
</tr>
<tr>
<td><code>must-revalidate</code></td>
<td>Cache directive is ignored and stale is served.</td>
<td>Does not serve stale. Must revalidate for CDN and for browser.</td>
</tr>
<tr>
<td><code>proxy-revalidate</code></td>
<td>Cache directive is ignored and stale is served.</td>
<td>Does not serve stale. Must revalidate for CDN but not for browser.</td>
</tr>
<tr>
<td><code>no-transform</code></td>
<td>May (un)Gzip, Polish, email filter, etc.</td>
<td>Does not transform body.</td>
</tr>
<tr>
<td><code>s-maxage=delta, delta&gt;1</code></td>
<td>Same as <code>max-age</code>.</td>
<td><code>Max-age</code> and <code>proxy-revalidate</code>.</td>
</tr>
<tr>
<td><code>immutable</code></td>
<td>Not proxied downstream.</td>
<td>Proxied downstream. Browser facing, does not impact caching proxies.</td>
</tr>
<tr>
<td><code>no-store</code></td>
<td>Will not cache.</td>
<td>Will not cache.</td>
</tr>
</tbody>
</table>
<h3 id="conditions">Conditions</h3>
<p>Certain scenarios also affect Origin Cache Control behavior when it is enabled or disabled.</p>
<table>
<tbody>
<th colspan="5" rowspan="1">
      Condition
</th>
<th colspan="5" rowspan="1">
      Origin Cache Control disabled behavior
</th>
<th colspan="5" rowspan="1">
      Origin Cache Control enabled behavior
</th>
<tr>
<td colspan="5" rowspan="1">
        Presence of <code>Authorization</code> header.
</td>
<td colspan="5" rowspan="1">
        Content may be cached.
</td>
<td colspan="5" rowspan="1">
        Content is cached only if <code>must-revalidate</code>, <code>public</code>, or <code>s-maxage</code> is also present.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
        Use of <code>no-cache</code> header.
</td>
<td colspan="5" rowspan="1">
        In logs, <code>cacheStatus=miss</code>.
</td>
<td colspan="5" rowspan="1">
        In logs, <code>cacheStatus=bypass</code>.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
        Origin response has <code>Set-Cookie</code> header and default cache level is used.
</td>
<td colspan="5" rowspan="1">
        Content may be cached with stripped <code>set-cookie</code> header.
</td>
<td colspan="5" rowspan="1">
        Content is not cached.
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
        Browser Cache TTL is set.
</td>
<td colspan="5" rowspan="1">
        `Cache-Control` returned to eyeball does not include <code>private</code>.
</td>
<td colspan="5" rowspan="1">
        If origin returns <code>private</code> in `Cache-Control` then preserve it.
</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3823.md")
</aside>
<h2 id="examples">Examples</h2>
<p>Review the examples below to learn which directives to use with the <code>Cache-Control</code> header to control specific caching behavior.</p>
<details class="nb-details"><summary>Cache a static asset.</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3830.md")
</div></details>
<details class="nb-details"><summary>Ensure a secret asset is never cached.</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3831.md")
</div></details>
<details class="nb-details"><summary>Cache assets on browsers but not on proxy cache.</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3832.md")
</div></details>
<details class="nb-details"><summary>Cache assets in client and proxy caches, but prefer revalidation when serve.</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3833.md")
</div></details>
<details class="nb-details"><summary>Cache assets in proxy caches but REQUIRE revalidation by the proxy when serve.</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3834.md")
</div></details>
<details class="nb-details"><summary>Cache assets in proxy caches, but REQUIRE revalidation by any cache when serve.</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3835.md")
</div></details>
<details class="nb-details"><summary>Cache assets, but ensure the proxy does not modify it.</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3836.md")
</div></details>
<details class="nb-details"><summary>Cache assets with revalidation, but allow stale responses if origin server is unreachable.</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3837.md")
</div></details>
<details class="nb-details"><summary>Cache assets for different amounts of time on Cloudflare and in visitor browsers.</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3838.md")
</div></details>
<details class="nb-details"><summary>Cache an asset and serve while asset is being revalidated.</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3839.md")
</div></details>
<h2 id="interaction-with-other-cloudflare-features">Interaction with other Cloudflare features</h2>
<p>This section covers how other Cloudflare features interact with <code>Cache-Control</code> directives.</p>
<h3 id="edge-cache-ttl">Edge Cache TTL</h3>
<p><a href="/cache/how-to/edge-browser-cache-ttl/#edge-cache-ttl">Edge Cache TTL</a> Cache Rules override <code>s-maxage</code> and disable revalidation directives if present. When Origin Cache Control is enabled at Cloudflare, the original <code>Cache-Control</code> header passes downstream from our edge even if Edge Cache TTL overrides are present. Otherwise, when Origin Cache Control is disabled at Cloudflare, Cloudflare overrides the Origin Cache Control.</p>
<h3 id="browser-cache-ttl">Browser Cache TTL</h3>
<p><a href="/cache/how-to/edge-browser-cache-ttl/#browser-cache-ttl">Browser Cache TTL</a> Cache Rules override <code>max-age</code> settings passed downstream from our edge, typically to your visitor's browsers.</p>
<h3 id="polish">Polish</h3>
<p><a href="/images/polish/">Polish</a> is disabled when the <code>no-transform</code> directive is present.</p>
<h3 id="gzip-and-other-compression">Gzip and Other Compression</h3>
<p>Compression is disabled when the <code>no-transform</code> directive is present. If the original asset fetched from the origin is compressed, it is served compressed to the visitor. If the original asset is uncompressed, compression is not applied.</p>
<h3 id="javascript-detections">JavaScript Detections</h3>
<p><a href="/cloudflare-challenges/challenge-types/javascript-detections/">JavaScript Detections</a> injection is disabled when the <code>no-transform</code> directive is present. The <code>cf.bot_management.js_detection.passed</code> field will show as <code>missing</code> for affected requests.</p>
