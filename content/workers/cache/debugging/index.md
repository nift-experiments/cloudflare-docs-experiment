<p>If caching is not behaving the way you expect, the <code>Cf-Cache-Status</code> response header is the first place to look. Every response carries it, and its value tells you exactly what happened for that request.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16714.md")
</aside>
<h2 id="inspect-cf-cache-status">Inspect <code>Cf-Cache-Status</code></h2>
<p>Send two requests to the same URL and compare the headers:</p>
<pre><code class="language-sh">curl -I https://my-worker.example.workers.dev/api/users/42&#10;curl -I https://my-worker.example.workers.dev/api/users/42&#10;</code></pre>
<p>Match the status value against the scenarios below.</p>
<h2 id="my-worker-runs-on-every-request">My Worker runs on every request</h2>
<p><code>Cf-Cache-Status</code> is not present. Check that your wrangler version is 4.69.0 or above, and that
wrangler.toml or wrangler.jsonc has <code>cache.enabled = true</code> for that worker.</p>
<p><code>Cf-Cache-Status</code> is <code>MISS</code> on every request, or <code>DYNAMIC</code>, or <code>BYPASS</code>. Caching is not storing anything, or a bypass rule is firing.</p>
<p><strong>Check your <code>Cache-Control</code> header.</strong> The response must carry directives that make it cacheable:</p>
<ul>
<li><code>public, max-age=N</code> — cached in Cloudflare and browsers for <code>N</code> seconds.</li>
</ul>
<p>A response with <code>Cache-Control: private</code> or <code>no-store</code> is not stored, and <code>Cf-Cache-Status</code> is <code>BYPASS</code>.</p>
<p>A response with <code>Cache-Control: no-cache</code> <em>is</em> stored, but Cloudflare treats every subsequent request as stale and consults your Worker before serving. The exact <code>Cf-Cache-Status</code> depends on whether <code>stale-while-revalidate</code> is also set:</p>
<ul>
<li>With just <code>Cache-Control: no-cache</code>, every subsequent request triggers an inline revalidation. <code>Cf-Cache-Status</code> is <code>REVALIDATED</code> if your Worker returns <code>304 Not Modified</code> (body served from cache), or <code>EXPIRED</code> if your Worker returns a fresh <code>200</code> (body replaced).</li>
<li>With <code>Cache-Control: no-cache, stale-while-revalidate=N</code>, the cached body is served immediately and the Worker runs in the background. <code>Cf-Cache-Status</code> is <code>UPDATING</code> for the SWR window.</li>
</ul>
<p>If you wanted long-lived cache hits, use <code>max-age</code> instead. Refer to <a href="/workers/cache/configuration/#automatic-bypass-conditions"><code>no-cache</code> is not a bypass</a>.</p>
<p>If the response carries <strong>no</strong> <code>Cache-Control</code> header at all, behavior depends on the status code: Workers Caching applies <a href="https://www.rfc-editor.org/rfc/rfc9111#name-calculating-heuristic-fresh">RFC 9111 heuristic freshness</a> and caches default-cacheable status codes for a heuristic TTL — for example, <code>200</code> is cached for 2 hours and <code>404</code> for 3 minutes. For the full table of default TTLs, refer to <a href="/workers/cache/configuration/#cache-control-semantics">Responses with no <code>Cache-Control</code> header are still cached</a> in the configuration reference. If you do not want any of these defaults to apply, set <code>Cache-Control</code> explicitly on the response.</p>
<p><strong>Check the request method.</strong> Only <code>GET</code> and <code>HEAD</code> requests are cached. Everything else is <code>BYPASS</code>. <code>GET</code> and <code>HEAD</code> requests for the same URL share the same cache entry — refer to <a href="/workers/cache/cache-keys/#what-goes-into-the-cache-key">Cache keys</a> for how Cloudflare handles populating the cache from either method.</p>
<p><strong>Check for automatic bypass conditions.</strong> Cloudflare bypasses the cache when:</p>
<ul>
<li>The response includes a <code>Set-Cookie</code> header.</li>
<li>The request includes an <code>Authorization</code> header, unless the response explicitly sets <code>Cache-Control: public</code>, <code>must-revalidate</code>, or <code>s-maxage</code>.</li>
</ul>
<p>If your Worker unconditionally sets <code>Set-Cookie</code> (for example, a session cookie on every response), the response is never cached. Either remove the cookie from cacheable responses, or separate cookie-setting and cacheable responses into different routes.</p>
<p><strong>Check the status code.</strong> Workers Caching follows <a href="https://www.rfc-editor.org/rfc/rfc9111">RFC 9111</a>. Responses with status codes that are not cacheable by default (for example, <code>401</code>, <code>403</code>, <code>500</code>) are not stored unless you explicitly mark them with cacheable directives.</p>
<p>A few status codes are never cached, even with explicit <code>Cache-Control</code>:</p>
<ul>
<li><strong><code>520</code>–<code>526</code></strong> are treated as Cloudflare failsafe responses and are never stored.</li>
<li><strong><code>206 Partial Content</code></strong> returned by your Worker is not stored. Workers Caching handles <code>Range</code> requests itself by fetching the full body from your Worker and slicing from the cached entry — if your Worker returns its own <code>206</code>, that response is treated as uncacheable. Return a full <code>200</code> instead. Refer to <a href="/workers/cache/configuration/#range-requests"><code>Range</code> requests</a>.</li>
</ul>
<h2 id="my-worker-runs-even-after-the-first-request">My Worker runs even after the first request</h2>
<p><code>Cf-Cache-Status</code> is <code>MISS</code> on the first request but still <code>MISS</code> on subsequent requests.</p>
<p><strong>The cache is likely partitioned.</strong> The cache key includes the request path, the target entrypoint, and the invocation's <code>ctx.props</code>. Two requests that look the same to you may produce different cache keys if any of these differ.</p>
<p>Common causes:</p>
<ul>
<li>The URL path or query string differs between requests (even trailing slashes matter).</li>
<li>The calling Worker passes different <code>ctx.props</code> for each request — for example, a different user ID.</li>
<li>Requests are hitting different <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#named-entrypoints">named entrypoints</a> of the same Worker.</li>
</ul>
<p>Cloudflare does not currently expose the cache key composition, so you cannot see the computed key directly. Instead, walk through the components listed in <a href="/workers/cache/cache-keys/#what-goes-into-the-cache-key">Cache keys</a> and verify each one is the same for both requests.</p>
<h2 id="my-cache-hit-rate-dropped-after-a-deployment">My cache hit rate dropped after a deployment</h2>
<p>This is expected with the default configuration. By default, the <a href="/workers/cache/cache-keys/#invalidating-cache-across-deployments">Worker version is part of the cache key</a>, so each new version starts from a cold cache and cannot reuse the previous version's cached responses. The first requests after a deploy are misses while the new version's cache fills, then the hit rate recovers.</p>
<p>If you deploy frequently and your responses rarely change between deployments, enable <a href="/workers/cache/configuration/#cross-version-caching"><code>cache.cross_version_cache</code></a> to share cached responses across versions and avoid resetting the cache on every deploy. The trade-off is that cache-affecting changes no longer apply immediately — see below.</p>
<h2 id="my-cache-still-serves-old-content-after-a-deployment">My cache still serves old content after a deployment</h2>
<p>By default a deployment takes effect immediately, because the Worker version is part of the cache key and the new version starts from a cold cache. If you are still seeing responses from a previous version, you have <a href="/workers/cache/configuration/#cross-version-caching"><code>cache.cross_version_cache</code></a> enabled, which shares cached entries across versions. To force a deployment to take effect while keeping <code>cross_version_cache</code> on:</p>
<ul>
<li><strong>Call <a href="/workers/cache/purge/#purge-everything"><code>ctx.cache.purge({ purgeEverything: true })</code></a></strong> after deploying. This is the simplest approach.</li>
<li><strong>Tag each cached response with the producing version</strong> using the <a href="/workers/runtime-apis/bindings/version-metadata/">version metadata binding</a>, then purge that tag on rollback. Refer to <a href="/workers/cache/purge/#version-specific-purging">Version-specific purging</a>.</li>
</ul>
<h2 id="my-cache-never-updates-after-content-changes">My cache never updates after content changes</h2>
<p>If your origin data changed but requests still return stale content:</p>
<ul>
<li><strong>Check the TTL.</strong> The response stays cached for <code>max-age</code> seconds. You may be looking at a response that is still within its freshness window.</li>
<li><strong>Purge the affected responses.</strong> Use <code>ctx.cache.purge()</code> with tags or a path prefix to invalidate specific entries. Refer to <a href="/workers/cache/purge/">Purging the cache</a>.</li>
<li><strong>Add tags at write time.</strong> If you did not set <code>Cache-Tag</code> headers, you cannot purge by tag. Add tags to your cached responses, deploy, and once new entries are written they become purgeable.</li>
</ul>
<h2 id="two-callers-receive-each-other-s-cached-responses">Two callers receive each other's cached responses</h2>
<p>This should not happen if you use <code>ctx.props</code> for per-caller authorization context. If it does, one of the following is true:</p>
<ul>
<li>You are authenticating callers with a header or query parameter that is not part of the cache key. Move the authorization input into <code>ctx.props</code>. Refer to <a href="/workers/cache/cache-keys/#multi-tenant-safety-with-ctxprops">Multi-tenant safety with <code>ctx.props</code></a>.</li>
<li>You are calling a service binding with a user-specific query parameter that is not present. The query string is part of the cache key; make sure each caller's request path actually differs.</li>
</ul>
<h2 id="cf-cache-status-updating-appears-constantly"><code>Cf-Cache-Status: UPDATING</code> appears constantly</h2>
<p><code>UPDATING</code> means the response was served from cache while stale and your Worker is running in the background to refresh it. This is expected behavior when using <code>stale-while-revalidate</code>.</p>
<p>If you see <code>UPDATING</code> more often than you expect:</p>
<ul>
<li>Your <code>max-age</code> is shorter than your request arrival rate. Every request that arrives after <code>max-age</code> elapses triggers a revalidation.</li>
<li>With <code>max-age=0, stale-while-revalidate=&lt;large&gt;</code>, <strong>every</strong> request triggers a revalidation. This is &quot;always serve from cache&quot; behavior, not &quot;don't run the Worker.&quot; Refer to <a href="/workers/cache/configuration/#choose-ttl-and-stale-while-revalidate-values">Choose TTL and stale-while-revalidate values</a>.</li>
</ul>
<h2 id="cf-cache-status-updating-never-appears"><code>Cf-Cache-Status: UPDATING</code> never appears</h2>
<p><code>UPDATING</code> is emitted only when <strong>all</strong> of the following are true:</p>
<ul>
<li>A cached entry exists and is past its freshness window (stale).</li>
<li>The response carries <code>stale-while-revalidate=N</code>, and the request arrives within <code>N</code> seconds of the entry going stale.</li>
<li>The response does <strong>not</strong> also carry <code>s-maxage</code>, <code>must-revalidate</code>, or <code>proxy-revalidate</code>.</li>
</ul>
<p>If any of those is false, requests for stale entries fall through to inline revalidation instead, producing <code>EXPIRED</code> (Worker returned a fresh body) or <code>REVALIDATED</code> (Worker returned <code>304 Not Modified</code>).</p>
<p>Common reasons <code>UPDATING</code> does not appear:</p>
<ul>
<li><strong>No <code>stale-while-revalidate</code> directive on the response.</strong> The default SWR window is <code>0</code>, so without an explicit directive every stale request is foreground-revalidated.</li>
<li><strong><code>s-maxage</code>, <code>must-revalidate</code>, or <code>proxy-revalidate</code> is present.</strong> Per <a href="https://www.rfc-editor.org/rfc/rfc9111#section-4.2.4">RFC 9111 §4.2.4</a>, these directives forbid serving stale content, so Cloudflare disables <code>stale-while-revalidate</code> (and <code>stale-if-error</code>) when any of them is present. Use <code>max-age</code> for the edge freshness window if you want stale-serving to work.</li>
<li><strong>The SWR window has elapsed.</strong> If your response uses <code>max-age=60, stale-while-revalidate=120</code>, you will see <code>UPDATING</code> for requests arriving in the 120 seconds after the entry goes stale. Requests arriving after that revert to inline revalidation.</li>
</ul>
<h2 id="cf-cache-status-stale-appears-unexpectedly"><code>Cf-Cache-Status: STALE</code> appears unexpectedly</h2>
<p><code>STALE</code> means Cloudflare served a previously cached response because your Worker errored on the request that would have refreshed it — for example, the Worker threw, timed out, or returned a <code>5xx</code> response. This is <code>stale-if-error</code> behavior. Refer to <a href="/workers/cache/configuration/#serve-stale-on-error-with-stale-if-error">Serve stale on error with <code>stale-if-error</code></a>.</p>
<p>If you see <code>STALE</code> and did not expect it:</p>
<ul>
<li><strong>Your Worker is failing on cache fills or revalidations.</strong> Check the <a href="/workers/observability/">Workers observability dashboard</a> for errors on the requests that should have produced a fresh response. The fact that clients see a stale response instead of a <code>5xx</code> is masking a real failure.</li>
<li><strong>You did not set <code>stale-if-error</code> explicitly, and your response does not include <code>s-maxage</code>/<code>must-revalidate</code>/<code>proxy-revalidate</code>.</strong> In that case, Cloudflare's default behavior is to serve stale responses on Worker error indefinitely, as long as the cached entry has not been purged. If you want errors to surface to clients quickly, set <code>stale-if-error=0</code> in <code>Cache-Control</code>. For details, refer to <a href="/workers/cache/configuration/#serve-stale-on-error-with-stale-if-error">Serve stale on error with <code>stale-if-error</code></a>.</li>
<li><strong>A previously deployed version is being served.</strong> If you deployed a fix but <code>STALE</code> keeps appearing, the cached entry from the broken version is still being served on every error. <a href="/workers/cache/purge/">Purge</a> the affected entries to force a fresh fill from the current version.</li>
</ul>
<p>To distinguish a <code>STALE</code> from a normal <code>HIT</code> in client-side observability, log <code>Cf-Cache-Status</code> alongside the response — <code>STALE</code> is the only signal that the Worker is failing and clients are not seeing it.</p>
<h2 id="my-response-is-larger-than-the-size-limit">My response is larger than the size limit</h2>
<p>If a response is too large to cache, Cloudflare does not store it. You will see <code>Cf-Cache-Status: MISS</code> on every request even though the response otherwise looks cacheable.</p>
<p>For per-plan response size limits, refer to <a href="/cache/concepts/default-cache-behavior/#cacheable-size-limits">Cacheable size limits</a>. Note that at launch all Workers Caching responses are subject to the Free plan size limit — refer to <a href="/workers/cache/limitations/#response-size">Response size</a> for details.</p>
<h2 id="i-need-more-visibility">I need more visibility</h2>
<p>At launch, the primary debugging surfaces are the <code>Cf-Cache-Status</code> response header and per-invocation cache-hit information in the <a href="/workers/observability/">Workers observability dashboard</a>.</p>
