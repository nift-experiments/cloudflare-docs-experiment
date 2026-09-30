---
cp9:
  canonical: https://developers.cloudflare.com/workers/cache/
  description: Workers Cache lets you cache Worker responses to reduce latency and Workers usage.
  full_title: Workers Cache · Cloudflare Workers docs
  head_html: <title>Workers Cache · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Workers Cache lets you cache Worker responses to reduce latency and Workers usage."><link rel="canonical" href="https://developers.cloudflare.com/workers/cache/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/cache/index.md"><meta property="og:title" content="Workers Cache · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Workers Cache lets you cache Worker responses to reduce latency and Workers usage."><meta property="og:url" content="https://developers.cloudflare.com/workers/cache/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/cache/#page","headline":"Workers Cache \u00b7 Cloudflare Workers docs","description":"Workers Cache lets you cache Worker responses to reduce latency and Workers usage.","url":"https://developers.cloudflare.com/workers/cache/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/cache/
  schema: 1
---
<p>Workers Cache lets Cloudflare return cached HTTP responses from your Worker without executing your Worker code. When an incoming request matches a cached response, Cloudflare serves the response directly from its edge cache — reducing latency and Workers CPU usage.</p>
<p>Caching works for any <code>fetch()</code> invocation of the Worker — eyeball requests (requests from browsers and API clients), requests sent through <a href="/workers/runtime-apis/bindings/service-bindings/">service bindings</a>, and loopback <code>fetch()</code> calls between entrypoints via <a href="/workers/runtime-apis/bindings/service-bindings/rpc/"><code>ctx.exports</code></a>. You control caching with standard HTTP <code>Cache-Control</code> directives on your responses.</p>
<h2 id="your-worker-s-cache">Your Worker's cache</h2>
<p>Workers Cache is <strong>your Worker's cache</strong>. It is owned by your Worker, operated by your Worker, and private to your Worker.</p>
<p>A Worker is a zoneless entity — a Worker can be bound to any number of <a href="/fundamentals/concepts/accounts-and-zones/#zones">zones</a>, run on <code>workers.dev</code>, or be invoked entirely through service bindings without ever touching a zone. The cache follows the Worker, not a zone, so:</p>
<ul>
<li><strong>No zone configuration for caching applies to Workers Caching.</strong> <a href="/cache/how-to/cache-rules/">Cache Rules</a>, <a href="/cache/how-to/cache-response-rules/">Cache Response Rules</a>, <a href="/rules/page-rules/">Page Rules</a>, cache level settings, the zone's <a href="/cache/concepts/default-cache-behavior/#default-cached-file-extensions">default cached-file-extensions</a> list, and every other zone-level cache control have no effect on a Worker's cache.</li>
<li><strong>Your Worker is in full control.</strong> You set <code>Cache-Control</code> headers on your responses, and Cloudflare honors them per <a href="https://www.rfc-editor.org/rfc/rfc9111">RFC 9111</a>. That is the entire configuration surface.</li>
<li><strong>The cache is shared across every way the Worker can be invoked.</strong> A Worker bound to <code>api.example.com</code>, <code>api.example.net</code>, and invoked over a service binding serves the same cached responses to all three — the cache is keyed by the request path, entrypoint, <code>ctx.props</code>, and (by default) the Worker version, not by hostname. See <a href="/workers/cache/cache-keys/">Cache keys</a>.</li>
</ul>
<h3 id="the-worker-is-the-configuration-surface">The Worker is the configuration surface</h3>
<p>A Worker is <strong>already infinitely customizable</strong>. You can change response bodies, rewrite headers, branch on any request attribute, call out to other Workers via service bindings or <a href="/workers/runtime-apis/bindings/service-bindings/rpc/"><code>ctx.exports</code></a>, and compose logic across an entire system.</p>
<p>Workers Caching leans on that. Instead of introducing a separate configuration layer for caching behavior, it lets your Worker express that intent directly — through the <code>Cache-Control</code> headers it returns, the <code>ctx.props</code> it accepts, and the programmatic purges it issues. Anything you might want to configure about caching, you can configure in code:</p>
<ul>
<li>Want a longer TTL for certain paths? Branch on the path in your Worker and set a different <code>max-age</code>.</li>
<li>Want to strip a tracking query parameter before caching? Rewrite the URL or <code>ctx.props</code> in a gateway Worker before dispatching.</li>
<li>Want per-tenant cache partitioning? Set the tenant identifier in <code>ctx.props</code> — that is in the cache key.</li>
<li>Want to bypass the cache for authenticated users? Return <code>Cache-Control: private</code>, or rely on the <a href="/cache/concepts/cache-responses/#bypass">automatic bypass</a> triggered by <code>Set-Cookie</code> and <code>Authorization</code>.</li>
</ul>
<p>The Worker you already wrote is the configuration mechanism. Workers Caching runs in front of it and honors whatever headers the Worker returns.</p>
<h2 id="when-caching-helps">When caching helps</h2>
<p>Caching is a good fit for Workers that:</p>
<ul>
<li>Perform CPU-intensive work whose result can be reused across requests — content generation, template rendering, data transformation.</li>
<li>Fetch data from a slow origin or third-party API and want to absorb that latency for subsequent requests.</li>
<li>Power a server-rendered or statically generated site where many requests produce identical responses.</li>
</ul>
<p>Caching is not useful for per-user responses that change on every request, non-idempotent operations (<code>POST</code>, <code>PUT</code>, <code>DELETE</code>), or responses that must be computed fresh every time.</p>
<h2 id="how-it-works">How it works</h2>
<p>With caching enabled, Cloudflare checks the cache before running your Worker. On a hit, the cached response is returned directly. On a miss, your Worker runs, and if the response is cacheable per its <code>Cache-Control</code> header, Cloudflare stores it for the next request.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;    accTitle: Cache before a Worker request flow&#10;    accDescr: Request arrives at Cloudflare, cache is consulted before Worker execution.&#10;&#10;    Request[&quot;Request&quot;] --&gt; Cache{&quot;Cache&quot;}&#10;    Cache -- Hit --&gt; Response[&quot;Cached response returned&quot;]&#10;    Cache -- Miss --&gt; Worker[&quot;Worker runs&quot;]&#10;    Worker --&gt; Store[&quot;Response stored in cache&quot;]&#10;    Store --&gt; Response2[&quot;Response returned&quot;]&#10;</code></pre>
<h2 id="tiered-cache">Tiered cache</h2>
<p>Workers Caching is <strong>tiered by default</strong>. Cloudflare operates two layers of cache for your Worker:</p>
<ul>
<li><strong>Lower tier</strong> — a cache in the Cloudflare data center closest to the eyeball. Every data center that receives traffic for your Worker has its own lower-tier cache.</li>
<li><strong>Upper tier</strong> — a smaller set of data centers that every lower tier consults on a miss. The upper tier aggregates cache fills across the whole network.</li>
</ul>
<p>A request is served from the lower tier if it is a hit there. If it is a miss, the lower tier asks the upper tier. If the upper tier also misses, your Worker finally runs to generate the response — and that response is stored in <strong>both</strong> tiers on the way back out, so subsequent requests from any data center benefit.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;    accTitle: Tiered cache for Workers&#10;    accDescr: A request hits the lower-tier cache first, then the upper-tier cache, then the Worker.&#10;&#10;    Request[&quot;Request&quot;] --&gt; Lower{&quot;Lower-tier cache&lt;br/&gt;(near eyeball)&quot;}&#10;    Lower -- Hit --&gt; Response[&quot;Cached response returned&quot;]&#10;    Lower -- Miss --&gt; Upper{&quot;Upper-tier cache&quot;}&#10;    Upper -- Hit --&gt; Lower&#10;    Upper -- Miss --&gt; Worker[&quot;Worker runs&quot;]&#10;    Worker --&gt; Upper&#10;</code></pre>
<p>This is the same topology that powers <a href="/cache/how-to/tiered-cache/">Tiered Cache</a> for zones, applied automatically to your Worker. You do not configure it, and the tiering runs regardless of whether your Worker uses <a href="#smart-placement-and-the-cache">Smart Placement</a>.</p>
<p><strong>Why this matters:</strong> the first request for a given cache key anywhere on Earth populates the upper tier. Every later request, from any Cloudflare data center, can be served from the upper tier without running your Worker — even if the lower tier at that location has never seen the request before. Cache hit ratios are substantially higher than a single flat cache layer.</p>
<h2 id="request-collapsing">Request collapsing</h2>
<p>When many requests for the same cache key arrive simultaneously at a Cloudflare data center and the response is not yet cached, Cloudflare runs your Worker <strong>once</strong> and serves the resulting response to every waiting request. This is the same <a href="/cache/concepts/default-cache-behavior/#request-collapsing">request collapsing</a> mechanism the zone cache uses, applied automatically to Workers Caching. The waiting requests block on a per-cache-key <a href="/cache/concepts/default-cache-behavior/#request-collapsing">cache lock</a> until the first request produces a response.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;    accTitle: Cache request collapsing for Workers&#10;    accDescr: Many simultaneous requests for the same cache key produce one Worker invocation; all requests receive the same response.&#10;&#10;    R1[&quot;Request 1&quot;] --&gt; Lock&#10;    R2[&quot;Request 2&quot;] --&gt; Lock&#10;    R3[&quot;Request 3&quot;] --&gt; Lock&#10;    Rn[&quot;...&quot;] --&gt; Lock&#10;    Lock{&quot;Cache lock&lt;br/&gt;(per cache key, per data center)&quot;}&#10;    Lock -- &quot;first request&quot; --&gt; Worker[&quot;Worker runs once&quot;]&#10;    Worker --&gt; Response[&quot;Response&lt;br/&gt;streamed to all&lt;br/&gt;waiting requests&quot;]&#10;</code></pre>
<p><strong>Why this matters:</strong> without request collapsing, a sudden burst of traffic to a fresh URL would invoke your Worker once per request, multiplying CPU billing and load on any backend the Worker calls. With request collapsing, that burst still produces one Worker invocation.</p>
<p>A few details to keep in mind:</p>
<ul>
<li><strong>Collapsing is per cache key, per data center.</strong> Requests that produce different cache keys do not collapse with each other. Two data centers that both miss simultaneously each run your Worker once (the upper tier consolidates further; refer to <a href="#tiered-cache">Tiered cache</a>).</li>
<li><strong>Streaming responses are collapsed too.</strong> Waiting requests are joined to the in-flight response stream so they receive the body as it is produced — they do not have to wait for the full response before any bytes are returned.</li>
<li><strong>Collapsing does not apply to uncacheable responses.</strong> If the Worker's response is uncacheable (<code>BYPASS</code>, <code>DYNAMIC</code>), each request gets its own invocation. The cache only collapses requests that produce a response the cache is allowed to store.</li>
</ul>
<p>This is one of the most significant differences between Workers Caching and the <a href="/workers/runtime-apis/cache/">Cache API</a> — the Cache API does not collapse concurrent requests, so a burst of traffic to a fresh URL invokes your Worker once per request.</p>
<h2 id="quickstart">Quickstart</h2>
<p>This quickstart walks you through enabling caching, deploying, and observing the cache in action.</p>
<h3 id="1-enable-caching-in-your-wrangler-configuration"><ol>
<li>Enable caching in your Wrangler configuration</li>
</ol></h3>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16695.md")
</div>
<h3 id="2-return-a-cacheable-response-from-your-worker"><ol start="2">
<li>Return a cacheable response from your Worker</li>
</ol></h3>
<p>Use <code>max-age</code> to control how long Cloudflare caches each response:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16696.md")
</div>
<h3 id="3-deploy-and-observe-the-cache"><ol start="3">
<li>Deploy and observe the cache</li>
</ol></h3>
<p>Deploy your Worker:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Then send two requests and look at the <code>Cf-Cache-Status</code> response header:</p>
<pre tabindex="0"><code class="language-sh">curl -I https://my-worker.example.workers.dev/&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">HTTP/2 200&#10;cache-control: public, max-age=3600, stale-while-revalidate=300&#10;cf-cache-status: MISS&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">curl -I https://my-worker.example.workers.dev/&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">HTTP/2 200&#10;cache-control: public, max-age=3600, stale-while-revalidate=300&#10;cf-cache-status: HIT&#10;</code></pre>
<p>The second request receives the cached response. The <code>timestamp</code> and <code>random</code> values in the body are identical between the two requests, even though the Worker generates fresh ones on every run — confirming that the second request did not execute your Worker.</p>
<h2 id="what-gets-cached">What gets cached</h2>
<ul>
<li>HTTP invocations of the Worker's <a href="/workers/runtime-apis/fetch/"><code>fetch</code></a> handler are eligible for caching, including eyeball requests, service binding <code>fetch()</code> calls, and loopback <code>fetch()</code> calls via <code>ctx.exports</code>.</li>
<li>Only <code>GET</code> and <code>HEAD</code> requests are cached. Other methods always invoke your Worker. <code>GET</code> and <code>HEAD</code> for the same URL share a single cache entry — see <a href="/workers/cache/cache-keys/#what-goes-into-the-cache-key">Cache keys</a>.</li>
<li><strong>Only <code>fetch()</code> invocations go through the cache.</strong> Custom <a href="/workers/runtime-apis/rpc/">RPC methods</a> on a <code>WorkerEntrypoint</code> (for example <code>ctx.exports.Backend.getUser(id)</code>) bypass the cache entirely and always run the callee. To cache a piece of work, expose it as a <code>fetch</code> handler on its own entrypoint.</li>
<li><strong>WebSocket upgrade requests bypass the cache.</strong> A <code>GET</code> request carrying <code>Upgrade: websocket</code> always invokes your Worker.</li>
<li>Other invocation types — <a href="/workers/configuration/cron-triggers/"><code>scheduled</code></a> (Cron Triggers), <a href="/queues/configuration/javascript-apis/#consumer"><code>queue</code></a> consumers, <a href="/workflows/">Workflows</a>, <a href="/workers/observability/logs/tail-workers/">Tail Workers</a>, <a href="/durable-objects/">Durable Object</a> invocations, <a href="/email-service/api/route-emails/email-handler/">Email Workers</a> — always run without cache involvement.</li>
<li>Cacheability is determined by the response headers your Worker returns. Workers Caching follows the semantics defined in <a href="https://www.rfc-editor.org/rfc/rfc9111">RFC 9111</a>, including <a href="https://www.rfc-editor.org/rfc/rfc9111#name-calculating-heuristic-fresh">heuristic freshness</a> for responses that do not carry <code>Cache-Control</code>. Refer to <a href="/cache/concepts/cache-control/">Cache-Control</a> for the full list of directives Cloudflare respects.</li>
<li>Cloudflare's standard <a href="/cache/concepts/cache-responses/#bypass">cache bypass conditions</a> apply. In particular, responses with a <code>Set-Cookie</code> header and requests with an <code>Authorization</code> header trigger automatic bypass.</li>
<li><a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a> are supported. Each preview caches independently of your production deployment, so testing a cache-affecting change in a preview never touches production's cached responses.</li>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> is supported. Each user Worker has its own cache, isolated from the dispatcher and from other user Workers in the namespace.</li>
</ul>
<p>The <code>Cf-Cache-Status</code> response header tells you what happened for each request.
The values you will see most often are <code>HIT</code>, <code>MISS</code>, <code>EXPIRED</code>, <code>REVALIDATED</code>,
<code>UPDATING</code>, <code>STALE</code>, and <code>BYPASS</code>. Refer to <a href="/cache/concepts/cache-responses/">Cloudflare cache
responses</a> for the full set of values.</p>
<h2 id="content-negotiation-with-vary">Content negotiation with <code>Vary</code></h2>
<p>Workers Caching honors the <a href="https://www.rfc-editor.org/rfc/rfc9110.html#name-vary"><code>Vary</code></a> response header as defined in <a href="https://www.rfc-editor.org/rfc/rfc9110.html">RFC 9110</a> and <a href="https://www.rfc-editor.org/rfc/rfc9111.html#name-calculating-cache-keys-with">RFC 9111</a>. When your Worker returns a <code>Vary</code> header, Cloudflare stores a separate cached variant per distinct combination of the listed request header values, and only returns a cached variant when the incoming request's headers match the ones the variant was stored under.</p>
<p>This lets a single URL cache multiple representations — for example, different encodings, different content types, or different languages — without your Worker coordinating content negotiation by hand:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16697.md")
</div>
<p>Notes:</p>
<ul>
<li><code>Vary: *</code> disables caching for the response. A wildcard variance cannot be satisfied deterministically from request headers, so Cloudflare does not store the response.</li>
<li>Variants share a single cache entry for purge purposes — <a href="/workers/cache/purge/">purging</a> a tag or path prefix that matches any variant invalidates all variants of that URL. All variants of a URL must therefore use the same <code>Cache-Tag</code> values.</li>
<li><code>Vary</code> is not compatible with image-transformation features that already produce their own variants (Polish, Image Resizing). Responses rewritten by those features ignore <code>Vary</code>.</li>
<li>Variants are stored per exact request-header value. Clients that send semantically equivalent but textually different values — for example <code>Accept-Encoding: gzip, br</code> and <code>Accept-Encoding: br, gzip</code> — produce separate variants. Shape the headers your Worker sees (for example, by normalizing them in a gateway Worker before passing the request on) if you need to reduce variant fan-out.</li>
</ul>
<h2 id="caching-between-workers">Caching between Workers</h2>
<p>When one Worker calls another over a <a href="/workers/runtime-apis/bindings/service-bindings/">service binding</a>, the <strong>callee's</strong> cache is consulted. If the callee has caching enabled and has a matching cached response, the caller receives it without invoking the callee.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;    accTitle: Cache between Workers&#10;    accDescr: Worker A calls Worker B; Worker B&#x27;s cache is consulted before Worker B runs.&#10;&#10;    Request[&quot;Request&quot;] --&gt; WorkerA[&quot;Worker A&quot;]&#10;    WorkerA --&gt; CacheB{&quot;Worker B&#x27;s cache&quot;}&#10;    CacheB -- Hit --&gt; WorkerA&#10;    CacheB -- Miss --&gt; WorkerB[&quot;Worker B&quot;]&#10;    WorkerB --&gt; CacheB&#10;</code></pre>
<p>The cache key for service binding calls includes the caller's <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#ctxprops"><code>ctx.props</code></a>, so different callers with different authorization context are cached separately. For details, refer to <a href="/workers/cache/cache-keys/">Cache keys</a>.</p>
<p>For same-account calls, the calling Worker can also tailor the callee's caching for an individual request by setting <a href="/workers/cache/cache-keys/#custom-cache-keys"><code>cf.cacheKey</code></a> to override the cache key or <a href="/workers/cache/configuration/#override-cache-control-from-the-calling-worker"><code>cf.cacheControl</code></a> to supply a <code>Cache-Control</code> directive.</p>
<h2 id="cache-durable-object-responses">Cache Durable Object responses</h2>
<p><a href="/durable-objects/">Durable Objects</a> are never cached directly by Workers Caching. However, since Workers Caching runs in front of any Worker entrypoint, you can cache a Durable Object's HTTP responses by wrapping the Durable Object behind a <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#named-entrypoints">named Worker entrypoint</a> and caching the entrypoint.</p>
<p>The wrapper entrypoint forwards the request into the Durable Object and sets <code>Cache-Control</code> on the response it returns. Because Workers Caching sits in front of the entrypoint, subsequent requests are served from cache without re-entering the Durable Object.</p>
<p>The default entrypoint here is a gateway that should run on every request, so disable caching on it and enable it on <code>CachedCounter</code> (see <a href="/workers/cache/configuration/#per-entrypoint-caching">Per-entrypoint caching</a>):</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16698.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16699.md")
</div>
<p>For more patterns that combine a gateway entrypoint with cached inner entrypoints, refer to <a href="/workers/cache/examples/">Examples</a>.</p>
<h2 id="smart-placement-and-the-cache">Smart placement and the cache</h2>
<p><a href="/workers/configuration/placement/">Smart Placement</a> moves <strong>where your Worker runs</strong> when it runs — typically closer to a slow origin or database. It does not move the cache. Workers Caching always has a lower tier near the eyeball and an upper tier aggregating the network, exactly as described in <a href="#tiered-cache">Tiered cache</a> above, whether or not Smart Placement is enabled.</p>
<p>The cache is always consulted before Smart Placement is considered. Concretely:</p>
<ul>
<li><strong>Lower-tier hit:</strong> the response is returned from the data center nearest the eyeball. Your Worker does not run. Smart Placement is not consulted.</li>
<li><strong>Lower-tier miss, upper-tier hit:</strong> the response is returned from the upper tier. Your Worker does not run. Smart Placement is not consulted.</li>
<li><strong>Both tiers miss:</strong> Smart Placement routes execution of your Worker to the placement target (for example, near your origin). The resulting response is stored in both cache tiers on the way back to the eyeball.</li>
</ul>
<p>Importantly, the <strong>upper tier and the Smart Placement target are independent locations</strong>. The upper tier is chosen by Cloudflare to aggregate cache fills across the network; the Smart Placement target is chosen to minimize latency between your Worker and its backend. They are generally not in the same data center.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;    accTitle: Tiered cache with Smart Placement across three locations&#10;    accDescr: The eyeball, the upper-tier cache, and the Smart Placement target are three independent locations. Requests traverse them in order on a full cache miss.&#10;&#10;    subgraph EyeballColo[&quot;Data center near eyeball&quot;]&#10;        Request[&quot;Request&quot;] --&gt; Lower{&quot;Lower-tier cache&quot;}&#10;    end&#10;&#10;    subgraph UpperColo[&quot;Upper-tier data center&quot;]&#10;        Upper{&quot;Upper-tier cache&quot;}&#10;    end&#10;&#10;    subgraph PlacedColo[&quot;Smart Placement target&quot;]&#10;        Placed[&quot;Worker runs&quot;]&#10;        Origin[&quot;Origin / backend&quot;]&#10;        Placed &lt;--&gt; Origin&#10;    end&#10;&#10;    Lower -- Hit --&gt; Response[&quot;Response&quot;]&#10;    Lower -- Miss --&gt; Upper&#10;    Upper -- Hit --&gt; Lower&#10;    Upper -- Miss --&gt; Placed&#10;    Placed --&gt; Upper&#10;</code></pre>
<p>On a full cache miss, a request therefore traverses three locations: the lower-tier data center near the eyeball, the upper-tier data center, and the Smart Placement target. The cache tiers absorb this cost so that the slow trip to the placement target is only paid once for the whole network — the upper tier shields the placement target from every lower-tier miss.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="future-optimization">Future optimization</h3>
@markup("md", "content/.markup/bodies/16694.md")
</aside>
<h2 id="purging-the-cache">Purging the cache</h2>
<p>Your Worker can invalidate its own cache at any time using <code>ctx.cache.purge()</code>. Tags are the most flexible mechanism — tag responses with <code>Cache-Tag</code> when returning them, and purge those tags later:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16700.md")
</div>
<p>You can also <a href="/workers/cache/purge/#two-ways-to-call-purge">import <code>cache</code> from <code>cloudflare:workers</code></a> and call <code>cache.purge({...})</code> when you do not have <code>ctx</code> in scope — for example, from a utility module. For all purge modes and patterns, refer to <a href="/workers/cache/purge/">Purging the cache</a>.</p>
<h2 id="pricing">Pricing</h2>
<p>Workers Cache has no separate pricing. When you enable Workers Cache, all requests to your Worker are billed at the standard <a href="/workers/platform/pricing/">Workers request rate</a> — the same per-request rate as any other request to your Worker — whether the response comes from cache or from your Worker. There is no charge beyond the standard request rate. <strong>CPU time is only billed when your Worker runs</strong> — cache hits do not consume CPU time.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="caching-bills-requests-that-are-normally-free">Caching bills requests that are normally free</h3>
@markup("md", "content/.markup/bodies/16693.md")
</aside>
<table>
<thead>
<tr>
<th>Request type</th>
<th>Request charge</th>
<th>CPU time charge</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cache <code>HIT</code> (Worker does not run)</td>
<td>Standard rate</td>
<td>Not billed</td>
</tr>
<tr>
<td>Cache <code>MISS</code> (Worker runs)</td>
<td>Standard rate</td>
<td>Billed</td>
</tr>
<tr>
<td>Cache <code>BYPASS</code> (Worker runs)</td>
<td>Standard rate</td>
<td>Billed</td>
</tr>
<tr>
<td><a href="/workers/static-assets/billing-and-limitations/">Static asset request</a></td>
<td>Standard rate</td>
<td>Not billed</td>
</tr>
<tr>
<td><a href="/workers/platform/pricing/#service-bindings">Worker-to-worker invocation</a></td>
<td>Standard rate</td>
<td>Billed if Worker runs</td>
</tr>
</tbody>
</table>
<p>For an example, refer to <a href="/workers/platform/pricing/#example-5-worker-with-caching">Pricing example: Worker with caching</a>.</p>
<h2 id="next-steps">Next steps</h2>
<ul class="directory-listing"><li><a href="/workers/cache/configuration/">Configuration</a></li><li><a href="/workers/cache/cache-keys/">Cache keys</a></li><li><a href="/workers/cache/purge/">Purging the cache</a></li><li><a href="/workers/cache/examples/">Examples</a></li><li><a href="/workers/cache/debugging/">Debugging</a></li><li><a href="/workers/cache/limitations/">Limitations</a></li></ul>
