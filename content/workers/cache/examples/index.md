<p>Workers Caching is <strong>a cache that is itself a Worker primitive</strong>. It sits in front of every Worker entrypoint — the default export and every named <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#named-entrypoints"><code>WorkerEntrypoint</code></a> — and it also sits in front of <code>fetch()</code> calls between entrypoints in the same Worker via <a href="/workers/runtime-apis/bindings/service-bindings/rpc/"><code>ctx.exports</code></a>. That second fact is the one that makes the rest of this page possible.</p>
<p>When one entrypoint invokes another's <code>fetch()</code> via <code>ctx.exports</code>, the cache evaluates that call the same way it would evaluate a request from a browser. A hit returns the cached response without the callee running. A miss runs the callee and stores the response under its own cache key, keyed by the callee's entrypoint, path, query string, and <a href="/workers/cache/cache-keys/#multi-tenant-safety-with-ctxprops"><code>ctx.props</code></a>. The caller still runs on every request — but anything the caller hands off to the callee is cacheable independently.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16703.md")
</aside>
<p>That gives you a primitive you can compose. You can author a Worker as a chain of small entrypoints — auth, normalization, routing, the expensive read, the data layer — and let Workers Caching slot in wherever you want it. Each cached entrypoint is a unit of memoization with its own key, its own TTL, and its own tag namespace for purging. Anything you would want to configure about caching — when it runs, what it keys on, when it invalidates — is expressed as ordinary Worker code: which entrypoint you call, what request you forward, what <code>ctx.props</code> you pass, what <code>Cache-Control</code> you set.</p>
<p>The examples on this page all use the same shape: an outer (gateway) entrypoint that runs every request, plus one or more inner entrypoints that are cached. The outer entrypoint does something cheap (authenticate, rewrite a header, pick a route); the inner entrypoint does something expensive (look up data, transform it, run a Durable Object). They are written as classes in one source file, deployed as one Worker, billed as one Worker — connected by a cache stage that sits in front of the inner entrypoint.</p>
<h3 id="two-rules-to-keep-in-mind">Two rules to keep in mind</h3>
<p>Two facts shape every pattern below. They follow directly from &quot;the cache is in front of every entrypoint&quot;:</p>
<p><strong>Disable caching on the gateway entrypoint.</strong> Because the cache sits in front of every entrypoint by default, the outer entrypoint would itself be cached — and the next request would be served from that outer cache without ever entering your gateway logic. Turn caching off for the gateway entrypoint in your Wrangler configuration, and leave it on for the inner entrypoint the gateway forwards to. Using <code>&quot;default&quot;</code> for the default export:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16704.md")
</div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="do-not-use-cache-control-no-store-to-keep-the-gateway-running">Do not use `Cache-Control: no-store` to keep the gateway running</h3>
@markup("md", "content/.markup/bodies/16702.md")
</aside>
<p><strong>Strip request headers that would force a bypass.</strong> Cloudflare's standard <a href="/cache/concepts/cache-responses/#bypass">bypass rules</a> apply to the inner entrypoint's cache too — an <code>Authorization</code> header on the forwarded request will turn every inner call into a <code>BYPASS</code>, and nothing will ever be stored. When the outer entrypoint authenticates the request and decides it is safe to cache, it must strip <code>Authorization</code> (and anything else that triggers automatic bypass) before invoking the inner entrypoint.</p>
<p>Both rules apply to every example below.</p>
<h2 id="cache-authenticated-responses">Cache authenticated responses</h2>
<p>Caching authenticated APIs has historically been awkward. The standard <a href="/cache/concepts/cache-responses/#bypass">bypass rules</a> treat any request with an <code>Authorization</code> header as private and refuse to cache it — which is the safe default, but means a token-authenticated endpoint that returns identical responses to thousands of users runs your Worker every single time.</p>
<p>The pattern below lets you authenticate every request and still serve cache hits without running the cacheable handler:</p>
<ol>
<li>The outer (default) entrypoint receives the request and authenticates it.</li>
<li>On success, it strips the <code>Authorization</code> header and forwards the request to a named entrypoint via <code>ctx.exports</code>.</li>
<li>Workers Caching sits in front of the named entrypoint. On a hit, the cached response is returned to the outer entrypoint, which returns it to the client — without the named entrypoint ever running.</li>
</ol>
<p>Disable caching on the default entrypoint so it runs on every request to authenticate, and keep it on for <code>CachedAPI</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16705.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16706.md")
</div>
<p>A few things to notice:</p>
<ul>
<li><strong>The cache is in the right place.</strong> It sits between the outer entrypoint and the cached entrypoint, so cache hits skip the expensive work entirely. Only the auth check runs.</li>
<li><strong><code>Authorization</code> is stripped before forwarding.</strong> This is what makes the response cacheable — Cloudflare's bypass rule fires on the inbound request, not on the response, so removing the header before the request reaches the cached entrypoint is what lets the cached entrypoint's <code>Cache-Control: public</code> take effect. It also prevents tokens from contributing to any future cache key.</li>
<li><strong>The cached response is shared across users.</strong> Every caller who passes the auth check sees the same cached body.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16701.md")
</aside>
<h3 id="per-user-authenticated-responses">Per-user authenticated responses</h3>
<p>If your endpoint returns user-specific data, pass the user identifier via <code>ctx.props</code>. Workers Caching includes <code>ctx.props</code> in the cache key, so each user gets their own cache entry and one user can never receive another user's cached response. This uses the same Wrangler configuration as the previous example — caching disabled on <code>default</code>, enabled on <code>CachedAPI</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16707.md")
</div>
<p>For more on cache isolation between callers, refer to <a href="/workers/cache/cache-keys/#multi-tenant-safety-with-ctxprops">Multi-tenant safety with <code>ctx.props</code></a>.</p>
<p>The shape of this example — the outer entrypoint shapes a value (the user's identity) into the cache key by passing it through <code>ctx.props</code> — is the same shape the next example uses to influence a different part of the key.</p>
<h2 id="normalize-accept-encoding-for-vary">Normalize <code>Accept-Encoding</code> for <code>Vary</code></h2>
<p><a href="/workers/cache/#content-negotiation-with-vary"><code>Vary</code></a> lets a single URL cache multiple representations — for example, a Brotli-encoded and gzip-encoded variant of the same asset. Cloudflare keys variants on the <strong>verbatim value</strong> of each <code>Vary</code>-listed request header, so two requests with semantically equivalent but textually different <code>Accept-Encoding</code> headers produce two separate variants.</p>
<p>For requests routed through Cloudflare's front line, this matters even more: the <code>Accept-Encoding</code> request header your Worker sees has typically been rewritten by Cloudflare to a canonical value (such as <code>gzip, br</code>) for cache efficiency. The original value is preserved at <a href="/workers/runtime-apis/request/#incomingrequestcfproperties"><code>request.cf.clientAcceptEncoding</code></a>, but if your Worker varies on <code>Accept-Encoding</code> without restoring the eyeball's value first, every cached variant ends up keyed on the rewritten string — so the cache returns a Brotli variant to clients that only accept gzip, or the other way around.</p>
<p>The fix is a gateway entrypoint that restores <code>Accept-Encoding</code> from <code>request.cf.clientAcceptEncoding</code> before forwarding to the cached entrypoint. Disable caching on the gateway and enable it on <code>CachedAssets</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16708.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16709.md")
</div>
<p>Things to notice:</p>
<ul>
<li><strong>The gateway runs on every request, but it is small.</strong> It only restores one header and calls <code>ctx.exports</code>. The expensive work — picking the encoding, loading the asset — runs only on cache misses.</li>
<li><strong>Variants share a single purge identity.</strong> Purging by tag or path prefix invalidates every variant of a URL together, so all variants must use the same <a href="/workers/cache/configuration/#cache-tag"><code>Cache-Tag</code></a> values. Refer to the notes in <a href="/workers/cache/#content-negotiation-with-vary">Content negotiation with <code>Vary</code></a>.</li>
<li><strong>The same pattern applies to other normalizable headers.</strong> If you want to vary on <code>Accept-Language</code> and you receive a long, complex value from browsers, normalize it in the gateway (for example, fold it down to the primary language tag) before forwarding. This keeps the cache fan-out bounded.</li>
</ul>
<p>If you do not need per-encoding variants — for example, if your Worker always returns Brotli when the client accepts it and otherwise falls back to gzip — you do not need <code>Vary</code> at all. Pick a canonical encoding inside the cached entrypoint based on the restored <code>Accept-Encoding</code>, and let the cache store a single variant. Refer to <a href="/workers/cache/configuration/#accept-encoding-and-content-encoding"><code>Accept-Encoding</code> and <code>Content-Encoding</code></a> for that variant of the pattern.</p>
<p>So far the inner entrypoint has been a function of the request. The next example puts a stateful component — a Durable Object — behind the same cache stage, with the same shape.</p>
<h2 id="cache-durable-object-responses">Cache Durable Object responses</h2>
<p><a href="/durable-objects/">Durable Objects</a> are never cached directly by Workers Caching — they are stateful, and caching their responses would defeat the point. But many Durable Object endpoints serve read-heavy traffic where a short cache TTL is perfectly acceptable: leaderboards, counters, aggregated stats, configuration that changes a few times an hour.</p>
<p>You can cache those responses by wrapping the Durable Object behind a named entrypoint and letting Workers Caching sit in front of the entrypoint. On a cache hit, the wrapper never runs and the Durable Object is never touched. Disable caching on the default (router) entrypoint and enable it on the <code>CachedLeaderboard</code> wrapper — the Durable Object itself is never cached and needs no cache configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16710.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16711.md")
</div>
<p>Why this works:</p>
<ul>
<li><strong>Reads pay nothing on a cache hit.</strong> Workers Caching sits in front of <code>CachedLeaderboard</code>, so a hit returns the cached body without invoking the wrapper, without invoking the Durable Object, and without doing the expensive aggregation. The default entrypoint still runs to dispatch the request, but it is a thin router.</li>
<li><strong>Writes invalidate the cache immediately.</strong> The POST handler updates the Durable Object and then calls <code>ctx.exports.CachedLeaderboard.invalidate()</code>, which runs <a href="/workers/cache/purge/#purge-by-tag"><code>purge({ tags: [&quot;leaderboard&quot;] })</code></a> <em>inside</em> <code>CachedLeaderboard</code>. This matters because <a href="/workers/cache/purge/#purge-modes">purges are scoped to the entrypoint that calls them</a> — the gateway's cache is disabled, so a purge issued from the gateway would not touch the entries <code>CachedLeaderboard</code> stored. The very next GET misses the cache, reruns the wrapper, and stores a fresh response.</li>
<li><strong>The cached entrypoint owns the cache contract.</strong> All cache-control headers are set in <code>CachedLeaderboard</code>, including the <code>Cache-Tag</code>, and <code>CachedLeaderboard</code> also exposes the <code>invalidate()</code> method that purges them. The Durable Object stays unaware of caching.</li>
</ul>
<p>If you have many independent Durable Object instances — for example, one per tenant — pass the tenant identifier via <code>ctx.props</code> when invoking the cached entrypoint, the same way <a href="#per-user-authenticated-responses">Per-user authenticated responses</a> does. Each tenant gets its own cache entry, and a purge on one tenant does not invalidate any other.</p>
<h2 id="cache-an-origin-you-do-not-control">Cache an origin you do not control</h2>
<p>Sometimes the origin you depend on is not yours. A third-party API, a SaaS endpoint, a public dataset, a vendor service behind a slow CDN — its caching headers are whatever the owner decided to ship, and you cannot change them. Maybe it sends <code>Cache-Control: no-store</code> to be safe. Maybe it sends nothing at all. Maybe it caches aggressively in a way that does not match your application's read patterns. Either way, you pay the latency and the request cost on every call.</p>
<p>Workers Caching lets you put your own cache layer in front of that origin without changing anything on the origin side. The pattern is the same outer-plus-inner shape as the rest of this page: a thin entrypoint that forwards to the origin, with Workers Caching sitting in front of it and applying the <code>Cache-Control</code> directives you choose. The origin keeps its own caching contract with the rest of the world; your Worker just adds a second, user-controlled layer between your application and that origin. As with the other patterns, disable caching on the gateway and enable it on <code>CachedOrigin</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16712.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16713.md")
</div>
<p>What is happening here:</p>
<ul>
<li><strong>The cache layer is yours.</strong> The origin's <code>Cache-Control</code> is replaced before the response reaches Workers Caching, so the TTL, freshness directives, and <code>Cache-Tag</code> namespace are all controlled by your code. You decide when the cache holds onto a response, and you decide when to purge it via <a href="/workers/cache/purge/"><code>ctx.cache.purge()</code></a>.</li>
<li><strong>The origin's own caching model is untouched.</strong> Your Worker is the only thing that sees the rewritten <code>Cache-Control</code>. The origin still serves its other clients with whatever caching contract it published — you have not changed its behaviour or its security model, you have only added a layer in front of it for your application.</li>
<li><strong>Cache hits never touch the origin.</strong> Workers Caching sits in front of <code>CachedOrigin</code>, so a hit returns the stored response without invoking <code>fetch</code> against the upstream. This is what cuts the origin request volume and the latency of every cached call.</li>
</ul>
<p>A few common extensions to this pattern:</p>
<ul>
<li><strong>Per-resource TTLs.</strong> If different paths on the upstream should have different freshness, branch on <code>url.pathname</code> inside <code>CachedOrigin</code> and set a different <code>max-age</code> (and a different <code>Cache-Tag</code>) for each. The cache key already includes the path and query string, so each resource gets its own entry.</li>
<li><strong>Per-user caching.</strong> If your application authenticates the caller and the upstream returns user-specific data, authenticate in the outer entrypoint and pass the user identifier via <code>ctx.props</code> to <code>CachedOrigin</code> — the same shape as <a href="#per-user-authenticated-responses">Per-user authenticated responses</a>. Each user gets their own cache entry, and one user can never receive another user's cached response.</li>
<li><strong>Stale-while-revalidate.</strong> If the origin is slow or flaky, set <code>Cache-Control: public, max-age=60, stale-while-revalidate=600</code> on the cached response. Most requests return the cached body immediately, and Workers Caching refreshes the origin in the background. Refer to <a href="/workers/cache/configuration/#use-stale-while-revalidate-for-low-latency-refreshes">Use <code>stale-while-revalidate</code> for low-latency refreshes</a>.</li>
<li><strong>Targeted invalidation.</strong> Tag responses with <code>Cache-Tag</code> values that reflect your application's data model (for example, <code>Cache-Tag: origin:example, product:42</code>). When you know the upstream has changed — a webhook fires, an admin action runs — call <code>ctx.cache.purge({ tags: [&quot;product:42&quot;] })</code> and the next request repopulates the cache.</li>
</ul>
<p>This is the same building block as every other example on this page. The only difference is that the &quot;expensive work&quot; the cached entrypoint does on a miss is a <code>fetch</code> to somebody else's server. The control over how long that response lives, how it is keyed, and when it is invalidated stays entirely in your Worker.</p>
<h2 id="composing-the-patterns">Composing the patterns</h2>
<p>All four examples are the same architecture seen through four lenses:</p>
<table>
<thead>
<tr>
<th>Outer entrypoint</th>
<th>What the cache stage is doing</th>
<th>Inner entrypoint</th>
</tr>
</thead>
<tbody>
<tr>
<td>Authenticate the request</td>
<td>Caching an expensive computation per user</td>
<td>Loads or computes the user's data</td>
</tr>
<tr>
<td>Restore <code>Accept-Encoding</code></td>
<td>Caching one variant per real encoding</td>
<td>Loads the correctly-encoded asset</td>
</tr>
<tr>
<td>Route reads vs. writes</td>
<td>Caching reads, invalidating them on writes</td>
<td>Wraps a Durable Object behind a <code>Cache-Tag</code></td>
</tr>
<tr>
<td>Forward the request as-is</td>
<td>Caching a third-party origin under your terms</td>
<td>Fetches the upstream and overlays <code>Cache-Control</code></td>
</tr>
</tbody>
</table>
<p>The only thing that changes between rows is what the outer entrypoint does before the call and what the inner entrypoint does on a miss. The cache stage in the middle is the same primitive every time — keyed by the inner entrypoint, the request path and query string, and <code>ctx.props</code>; configured by the inner entrypoint's <code>Cache-Control</code> and <code>Cache-Tag</code>; invalidated by <code>ctx.cache.purge()</code> from whichever entrypoint owns the data.</p>
<p>That uniformity is what makes the patterns compose. Nothing stops you from stacking them in a single Worker:</p>
<ul>
<li>An outer entrypoint that authenticates and routes.</li>
<li>A normalization entrypoint that strips tracking query parameters, restores <code>Accept-Encoding</code>, and shapes the request into a canonical form.</li>
<li>A cached entrypoint that fronts a Durable Object, tagged for purging.</li>
<li>A separate cached entrypoint for an unauthenticated public endpoint, also reachable through the same outer entrypoint, with its own cache key and <code>Cache-Tag</code> namespace.</li>
</ul>
<p>Each call between these entrypoints goes through its own cache stage. The chain is built out of the same three building blocks — <code>WorkerEntrypoint</code>, <code>ctx.exports</code>, and a <code>Cache-Control</code> header — and the cache is a stage of the chain rather than a separate system bolted on. Whatever you would have configured in a cache rules engine, you now write as code: which entrypoint runs, what request gets forwarded, what props get passed, what <code>Cache-Control</code> gets returned, what gets purged.</p>
<p>There is no fixed list of patterns. Workers Caching gives you a cache between every Worker entrypoint — what you build with that is up to you.</p>
