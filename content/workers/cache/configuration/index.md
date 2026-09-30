<p>Workers Caching is configured per Worker, in your Wrangler configuration file. When enabled, caching applies to every <code>fetch()</code> invocation — eyeball requests, service binding <code>fetch()</code> calls, and loopback <code>fetch()</code> calls between entrypoints via <a href="/workers/runtime-apis/bindings/service-bindings/rpc/"><code>ctx.exports</code></a> — unless you <a href="#per-entrypoint-caching">disable it for a specific entrypoint</a>. Custom <a href="/workers/runtime-apis/rpc/">RPC methods</a> bypass the cache.</p>
<p>This is <strong>your Worker's cache</strong> — configured through your Worker's code and Wrangler file. Your Worker controls its cache entirely through:</p>
<ul>
<li>The <code>cache.enabled</code> flag in your Wrangler configuration, which turns caching on or off. You can override it <a href="#per-entrypoint-caching">per entrypoint</a> and control <a href="#cross-version-caching">cross-version behavior</a>.</li>
<li>The <code>Cache-Control</code> (and <code>cdn-cache-control</code>, <code>cloudflare-cdn-cache-control</code>) headers your Worker sets on its responses, per <a href="https://www.rfc-editor.org/rfc/rfc9111">RFC 9111</a>.</li>
<li>The optional <code>Cache-Tag</code> response header for bulk purging, and <a href="/workers/cache/purge/"><code>ctx.cache.purge()</code></a> for programmatic invalidation.</li>
</ul>
<p>That is the entire configuration surface.</p>
<h2 id="enable-caching">Enable caching</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16723.md")
</aside>
<p>Add a <code>cache</code> block to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16724.md")
</div>
<p>Setting <code>cache.enabled</code> to <code>true</code> causes Cloudflare to check the cache before invoking your Worker on every HTTP request. This is the default for every entrypoint; you can override it per entrypoint with <a href="#per-entrypoint-caching"><code>exports</code></a>.</p>
<p>The <code>cache</code> block accepts two fields: <code>enabled</code> (required) and <a href="#cross-version-caching"><code>cross_version_cache</code></a> (optional). Any other fields are reserved for future use and may cause validation errors in future versions of Wrangler.</p>
<h2 id="disable-caching">Disable caching</h2>
<p>To turn caching off, set <code>cache.enabled</code> to <code>false</code> (or remove the <code>cache</code> block) and redeploy:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16725.md")
</div>
<p>Disabling caching does not purge previously cached responses — it only stops Cloudflare from consulting or populating the cache on subsequent requests. If you re-enable caching later, any entries that are still within their TTL become usable again. If you need cached responses to stop being served immediately, <a href="/workers/cache/purge/">purge the cache</a> after disabling.</p>
<h2 id="per-entrypoint-caching">Per-entrypoint caching</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16722.md")
</aside>
<p><code>cache.enabled</code> sets the default for the whole Worker, but a Worker can expose several <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#named-entrypoints">entrypoints</a> — the default export and any number of named <code>WorkerEntrypoint</code> classes — and you can turn caching on or off for each one independently. Use the <code>exports</code> map, keyed by entrypoint name, with <code>&quot;default&quot;</code> referring to the default export:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16726.md")
</div>
<p>Each entry is <code>{ &quot;type&quot;: &quot;worker&quot;, &quot;cache&quot;: { &quot;enabled&quot;: &lt;boolean&gt; } }</code>. A per-entrypoint <code>cache.enabled</code> overrides the top-level <code>cache.enabled</code> for that entrypoint; entrypoints you do not list inherit the top-level value. You can also enable caching for a single entrypoint without a top-level <code>cache</code> block by listing only that entrypoint.</p>
<p>This lets you <strong>opt specific entrypoints in and out</strong> without changing your Worker code:</p>
<ul>
<li><strong>Opt an entrypoint out</strong> to keep it running on every request — the natural fit for a gateway or router entrypoint that authenticates, normalizes, or dispatches, and should never itself be served from cache. This is the recommended way to build the <a href="/workers/cache/examples/">gateway pattern</a>: disable caching on the gateway entrypoint and enable it on the inner entrypoint the gateway calls through <code>ctx.exports</code>.</li>
<li><strong>Opt an entrypoint in</strong> to cache only the specific entrypoints that return reusable responses, leaving the rest of the Worker uncached.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="for-lowest-latency-disable-cache-for-an-entrypoint-instead-of-returning-cache-control-no-store-for-all-responses">For lowest latency, disable cache for an entrypoint instead of returning `Cache-Control: no-store` for all responses</h3>
@markup("md", "content/.markup/bodies/16721.md")
</aside>
<h2 id="versioned-deployments">Versioned deployments</h2>
<p>The <code>cache</code> configuration is part of your Worker version:</p>
<ul>
<li>Each version uploaded with <a href="/workers/wrangler/commands/#deploy"><code>wrangler deploy</code></a> or <a href="/workers/wrangler/commands/#versions-upload"><code>wrangler versions upload</code></a> captures whatever <code>cache.enabled</code> value is in its Wrangler configuration.</li>
<li>Rolling back to a previous version also rolls back the <code>cache</code> setting attached to that version.</li>
<li>You can use <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployments</a> to turn caching on for a percentage of traffic before applying it to 100%. During a gradual rollout from a version with caching disabled to a version with caching enabled, traffic routed to the old version runs uncached as it did before, and traffic routed to the new version consults and populates the cache. By default, the Worker version is part of the cache key, so the two versions populate independent cache entries and do not serve each other's responses — see <a href="#cross-version-caching">Cross-version caching</a>.</li>
</ul>
<h2 id="cross-version-caching">Cross-version caching</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16720.md")
</aside>
<p>By default, the <strong>Worker version is part of the cache key</strong>. Each deployed version has its own isolated cache, so a new deployment starts from an empty cache and never serves responses written by a previous version. This is the default because it is the simplest behavior to reason about: a new deployment applies immediately, and you never serve a response that a superseded version produced.</p>
<p>The trade-off is that <strong>cache hit rate resets on every deployment</strong>. Because a new version cannot reuse the previous version's cached responses, the first requests after a deploy are misses while the new version's cache fills. This is the most common reason a Worker's cache hit rate drops right after a deployment.</p>
<p>If you want to maximize cache hit rate and are willing to accept slower rollouts of cache-affecting changes, set <code>cross_version_cache</code> to <code>true</code>. Cached responses are then shared across versions — a response written by one version can be served by a later version as long as its TTL has not expired:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16727.md")
</div>
<p>Advanced users who deploy frequently and whose responses do not change between most deployments should consider enabling <code>cross_version_cache</code> — it avoids throwing away a warm cache on every deploy. The cost is that a deployment no longer invalidates the cache: after a change that alters response content, older cached responses continue to be served until they expire or you <a href="/workers/cache/purge/">purge</a> them, and during a <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployment</a> both versions share one cache. When you need a deployment to take effect immediately with <code>cross_version_cache</code> enabled, purge the cache after deploying, or tag responses by version — see <a href="/workers/cache/cache-keys/#invalidating-cache-across-deployments">Invalidating cache across deployments</a>.</p>
<p><code>cross_version_cache</code> only has an effect when caching is enabled. It applies to every entrypoint whose cache is on.</p>
<h2 id="environment-specific-configuration">Environment-specific configuration</h2>
<p>The <code>cache</code> block can be set at the top level and overridden per <a href="/workers/wrangler/environments/">environment</a>. The typical pattern is to turn caching on in production once you are confident it is safe, while keeping staging uncached for easier debugging:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16728.md")
</div>
<h2 id="cache-control-semantics">Cache-Control semantics</h2>
<p>With caching enabled, your Worker is the origin for Cloudflare's cache. Standard HTTP <code>Cache-Control</code> directives on the response your Worker returns determine whether and for how long Cloudflare caches it. For the full list of directives and how they interact, refer to <a href="/cache/concepts/cache-control/">Cache-Control</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="responses-with-no-cache-control-header-are-still-cached">Responses with no `Cache-Control` header are still cached</h3>
@markup("md", "content/.markup/bodies/16719.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="cache-deception-armor">Cache Deception Armor</h3>
@markup("md", "content/.markup/bodies/16718.md")
</aside>
<h3 id="set-the-freshness-window-with-max-age">Set the freshness window with <code>max-age</code></h3>
<p>Use <code>max-age</code> to control how long the response is treated as fresh:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16729.md")
</div>
<p>If you need browsers and the edge to cache for different durations, use <code>cdn-cache-control</code> (or <code>cloudflare-cdn-cache-control</code>) for the edge-only directive and keep <code>Cache-Control</code> for what browsers see. Refer to <a href="#header-precedence">Header precedence</a> below.</p>
<h3 id="use-stale-while-revalidate-for-low-latency-refreshes">Use <code>stale-while-revalidate</code> for low-latency refreshes</h3>
<p>When a cached response becomes stale, <code>stale-while-revalidate</code> lets Cloudflare return the stale response immediately and refresh it in the background:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16730.md")
</div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="s-maxage-must-revalidate-and-proxy-revalidate-disable-stale-while-revalidate">`s-maxage`, `must-revalidate`, and `proxy-revalidate` disable `stale-while-revalidate`</h3>
@markup("md", "content/.markup/bodies/16717.md")
</aside>
<h3 id="choose-ttl-and-stale-while-revalidate-values">Choose TTL and stale-while-revalidate values</h3>
<p>High cache hit rate and high freshness are in tension. Background revalidation hides the latency of refreshing the cache, but your Worker still runs once per revalidation — it is not free.</p>
<p>Two common patterns:</p>
<ul>
<li><strong>Mostly static content with a small tolerance for staleness.</strong> Use a short <code>max-age</code> (for example, 60 seconds) and a longer <code>stale-while-revalidate</code> window (for example, 3600 seconds). Most requests are <code>HIT</code>s; occasional requests trigger a background refresh.</li>
<li><strong>&quot;Always serve from cache&quot; for high-traffic endpoints.</strong> Use <code>max-age=0, stale-while-revalidate=&lt;large&gt;</code>. Every request returns the previously cached response immediately and triggers a background refresh. Your Worker runs once per request to revalidate, so CPU costs are close to running the Worker every time. Freshness drops as request volume drops — if no request arrives for a long time, the next request will see stale content.</li>
</ul>
<h3 id="serve-stale-on-error-with-stale-if-error">Serve stale on error with <code>stale-if-error</code></h3>
<p><code>stale-if-error</code> lets Cloudflare return a previously cached response when the Worker fails while refreshing an expired cache entry — for example, when it throws, times out, or returns a <code>5xx</code> response. This insulates clients from transient Worker failures.</p>
<pre><code class="language-ts">&quot;Cache-Control&quot;: &quot;public, max-age=600, stale-if-error=86400&quot;,&#10;</code></pre>
<p>When the Worker is producing a fresh response, <code>stale-if-error</code> has no effect. When the Worker fails while refreshing an expired entry, Cloudflare serves the last successful cached response (with <code>Cf-Cache-Status: STALE</code>) for up to the <code>stale-if-error</code> window. A true cache miss (no prior entry) cannot benefit from <code>stale-if-error</code> because there is nothing stale to serve — Worker errors flow through to clients in that case.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16716.md")
</aside>
<h3 id="header-precedence">Header precedence</h3>
<p>When multiple cache headers are present, the most specific wins:</p>
<ol>
<li><code>cloudflare-cdn-cache-control</code> — Cloudflare-specific, highest precedence. Consumed by Cloudflare and stripped from the response returned to clients.</li>
<li><code>cdn-cache-control</code> — standard header for CDN-only directives. Respected by Cloudflare and passed through to downstream CDNs.</li>
<li><code>Cache-Control</code> — standard HTTP header. Respected by Cloudflare and passed through to clients.</li>
</ol>
<p>Use <code>cloudflare-cdn-cache-control</code> when you want a longer edge TTL than you expose to browsers without leaking the directive downstream.</p>
<h3 id="override-cache-control-from-the-calling-worker">Override <code>Cache-Control</code> from the calling Worker</h3>
<p>Normally the callee decides how its responses are cached by setting <code>Cache-Control</code> on them. When one entrypoint invokes another cached entrypoint through a <a href="/workers/runtime-apis/bindings/service-bindings/rpc/"><code>ctx.exports</code></a> loopback, the <strong>calling</strong> entrypoint can instead supply the <code>Cache-Control</code> directive for that call by setting <code>cf.cacheControl</code> on the request.</p>
<p>Here the <code>Backend</code> entrypoint returns no <code>Cache-Control</code> of its own; the default entrypoint decides the caching policy when it calls <code>Backend</code> through <code>ctx.exports</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16731.md")
</div>
<p>Cloudflare treats <code>cf.cacheControl</code> as a trusted <code>Cache-Control</code> directive for caching the callee's response on that call. The value is a standard <code>Cache-Control</code> string and follows the <a href="/cache/concepts/cache-control/">same directive semantics</a> described throughout this page — <code>max-age</code>, <code>stale-while-revalidate</code>, <code>no-store</code>, and so on. This lets a calling entrypoint decide how a cached entrypoint's responses are cached without modifying that entrypoint's code.</p>
<p>Like <a href="/workers/cache/cache-keys/#custom-cache-keys">custom cache keys</a>, <code>cf.cacheControl</code> is honored only for calls that stay within your account. Cloudflare drops the <code>cf</code> object whenever a request crosses an account boundary, so a caller in one account cannot change how a Worker in another account caches its responses. The directive also has no effect on eyeball requests, because the <code>cf</code> object on an inbound request is populated by Cloudflare rather than by the client.</p>
<h2 id="response-headers">Response headers</h2>
<h3 id="cf-cache-status"><code>Cf-Cache-Status</code></h3>
<p>Every response carries a <code>Cf-Cache-Status</code> header indicating what happened for that request. The values you will see most often are <code>HIT</code>, <code>MISS</code>, <code>EXPIRED</code>, <code>REVALIDATED</code>, <code>UPDATING</code>, <code>STALE</code>, and <code>BYPASS</code>. For the full set of values and their meanings, refer to <a href="/cache/concepts/cache-responses/">Cloudflare cache responses</a>.</p>
<h3 id="cache-tag"><code>Cache-Tag</code></h3>
<p>The <a href="/cache/how-to/purge-cache/purge-by-tags/"><code>Cache-Tag</code></a> response header attaches tags to a cached response so you can purge it later in bulk. Cloudflare consumes this header and strips it before the response reaches the client.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16732.md")
</div>
<p>The <code>Cache-Tag</code> header value is a comma-separated list of tags. The same limits as the zone cache apply — refer to <a href="/cache/how-to/purge-cache/purge-by-tags/#a-few-things-to-remember">Cache tag limits</a> for the full list. The most common constraints to keep in mind:</p>
<ul>
<li>Tag values must be <strong>printable ASCII</strong> (<code>0x21</code>–<code>0x7E</code>) — no spaces, no Unicode, no control characters.</li>
<li>Each tag is at most <strong>1024 characters</strong> long.</li>
<li>A response can carry up to <strong>1000 tags</strong> for purge purposes.</li>
<li>Tag matching at purge time is <strong>case-insensitive</strong>. <code>Foo</code> and <code>foo</code> purge the same set of responses.</li>
</ul>
<p>Invalid tags (over-length, containing spaces, or containing non-ASCII characters) are silently dropped during cache storage — the response is still cached with the remaining valid tags, but you have no way to detect which tags were dropped. Validate tags in your Worker before returning them if this matters.</p>
<h3 id="automatic-bypass-conditions">Automatic bypass conditions</h3>
<p>Workers Caching inherits Cloudflare's standard <a href="/cache/concepts/cache-responses/#bypass">cache bypass rules</a>. The most common triggers:</p>
<ul>
<li>The response includes a <code>Set-Cookie</code> header (unless <code>Cache-Control</code> includes <code>private=&quot;set-cookie&quot;</code> or <code>no-cache=&quot;set-cookie&quot;</code>, in which case the <code>Set-Cookie</code> is stripped from the cached copy).</li>
<li>The request includes an <code>Authorization</code> header. The response is only stored if <code>Cache-Control</code> includes <code>public</code>, <code>must-revalidate</code>, or <code>s-maxage</code>, per <a href="https://www.rfc-editor.org/rfc/rfc9111#name-storing-responses-to-authen">RFC 9111 §3.5</a>.</li>
<li>The response <code>Cache-Control</code> header includes <code>private</code> or <code>no-store</code>.</li>
</ul>
<p>When any of these apply, <code>Cf-Cache-Status</code> is <code>BYPASS</code> and your Worker runs on every request.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="no-cache-is-not-a-bypass">`no-cache` is not a bypass</h3>
@markup("md", "content/.markup/bodies/16715.md")
</aside>
<h3 id="status-codes-that-are-never-cached">Status codes that are never cached</h3>
<p>A few status codes are never stored, even with explicit <code>Cache-Control</code> directives:</p>
<ul>
<li><strong><code>520</code>–<code>526</code></strong> (Cloudflare failsafe responses) are treated as transient errors and never cached.</li>
</ul>
<h3 id="range-requests"><code>Range</code> requests</h3>
<p>Workers Caching serves <code>Range</code> requests from a cached full response — your Worker does not have to implement byte-range slicing.</p>
<p>When a client sends a <code>Range</code> request, Cloudflare <strong>strips the <code>Range</code> header before invoking your Worker</strong> and asks your Worker for the full body. Your Worker returns a normal <code>200</code> response with a <code>Cache-Control</code> header (as it would for any other request), Cloudflare stores that full response, and then slices out the requested byte range and returns it to the client as a <code>206 Partial Content</code> response (or <code>416 Range Not Satisfiable</code> if the range is invalid). Subsequent <code>Range</code> requests to the same URL are satisfied entirely from the cached entry — your Worker is not invoked, and <code>Cf-Cache-Status</code> is <code>HIT</code>.</p>
<p>For example, a <code>GET</code> with <code>Range: bytes=0-9</code> against a cold cache produces a <code>MISS</code> on the way in (your Worker runs and returns the full body), then returns <code>206</code> with the first 10 bytes. A follow-up <code>GET Range: bytes=10-19</code> for the same URL is a <code>HIT</code> and returns those 10 bytes from cache without invoking your Worker.</p>
<p>If your Worker returns a <code>206</code> response of its own — for example, because you implemented <code>Range</code> handling inside the Worker — Cloudflare treats it as an uncacheable response and it is not stored. Return a full <code>200</code> and let Workers Caching handle range slicing.</p>
<h3 id="vary"><code>Vary</code></h3>
<p>When your Worker returns a <code>Vary</code> response header, Cloudflare stores a separate cached variant per distinct combination of the listed request header values, and only returns a variant whose stored values match the incoming request. This implements <a href="https://www.rfc-editor.org/rfc/rfc9110.html#name-vary">RFC 9110</a> and the cache-key calculation in <a href="https://www.rfc-editor.org/rfc/rfc9111.html#name-calculating-cache-keys-with">RFC 9111</a>. For an introduction with example code, refer to <a href="/workers/cache/#content-negotiation-with-vary">Content negotiation with <code>Vary</code></a>.</p>
<p>How <code>Vary</code> is processed for Workers Caching:</p>
<ul>
<li><strong>All header names are honored.</strong> Any header name your Worker lists in <code>Vary</code> participates in the variant key. There is no allowlist.</li>
<li><strong>Values are compared verbatim.</strong> Cloudflare does not normalize the listed request headers before keying. <code>Accept-Encoding: gzip, br</code> and <code>Accept-Encoding: br, gzip</code> produce two separate variants even though they are semantically identical. If you need to fold equivalent values onto the same variant, normalize the headers your Worker sees in a gateway Worker before passing the request on, or canonicalize them inside the Worker that sets <code>Vary</code>.</li>
<li><strong><code>Vary: *</code> disables caching.</strong> A wildcard variance cannot be satisfied deterministically from request headers, so the response is treated as uncacheable and <code>Cf-Cache-Status</code> is <code>BYPASS</code>.</li>
<li><strong>Variants share a single purge identity.</strong> <a href="/workers/cache/purge/">Purging</a> by tag or path prefix invalidates every variant of a URL together. All variants must therefore use the same <code>Cache-Tag</code> values — assigning different tags to different variants results in inconsistent purges.</li>
<li><strong>Image transformation features take precedence.</strong> Responses produced by Polish or Image Resizing already generate their own variants, and <code>Vary</code> on those responses is ignored.</li>
</ul>
<h3 id="accept-encoding-and-content-encoding"><code>Accept-Encoding</code> and <code>Content-Encoding</code></h3>
<p>Your Worker controls its own content negotiation. Whatever <code>Content-Encoding</code> your Worker sets on the response is what Cloudflare stores and serves to subsequent requests.</p>
<p>If your Worker needs to return different encodings to different clients, you have two options:</p>
<ul>
<li><strong>Pick one canonical encoding inside your Worker.</strong> Decide based on the <code>Accept-Encoding</code> request header, encode the body once, and return a single representation. Subsequent requests for that URL hit the same cached entry regardless of what they accept. This produces the highest cache hit rate but requires you to decide which clients you serve which encoding to.</li>
<li><strong>Vary on <code>Accept-Encoding</code>.</strong> Return a different <code>Content-Encoding</code> per request and set <code>Vary: Accept-Encoding</code>. Cloudflare stores one variant per distinct <code>Accept-Encoding</code> value the Worker has seen. Because comparison is verbatim, clients that send semantically equivalent values in different orders or with different quality factors produce separate variants — keep cache fan-out under control by normalizing <code>Accept-Encoding</code> (for example, in a gateway Worker) before the response is generated.</li>
</ul>
