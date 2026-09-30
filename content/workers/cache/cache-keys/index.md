---
cp9:
  canonical: https://developers.cloudflare.com/workers/cache/cache-keys/
  description: How Workers Caching builds cache keys, with guidance for service bindings, multi-tenant Workers, and gradual deployments.
  full_title: Cache keys · Cloudflare Workers docs
  head_html: <title>Cache keys · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="How Workers Caching builds cache keys, with guidance for service bindings, multi-tenant Workers, and gradual deployments."><link rel="canonical" href="https://developers.cloudflare.com/workers/cache/cache-keys/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/cache/cache-keys/index.md"><meta property="og:title" content="Cache keys · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Workers Caching builds cache keys, with guidance for service bindings, multi-tenant Workers, and gradual deployments."><meta property="og:url" content="https://developers.cloudflare.com/workers/cache/cache-keys/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/cache/cache-keys/#page","headline":"Cache keys \u00b7 Cloudflare Workers docs","description":"How Workers Caching builds cache keys, with guidance for service bindings, multi-tenant Workers, and gradual deployments.","url":"https://developers.cloudflare.com/workers/cache/cache-keys/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/cache/cache-keys/
  schema: 1
---
<p>Every cached response is stored under a <strong>cache key</strong>. When a request arrives, Cloudflare computes a cache key for it and looks it up — on a hit, the stored response is returned; on a miss, your Worker runs and its response is stored under that key for next time.</p>
<p>Two requests that produce the same cache key share the same cached response. Two requests that produce different cache keys get independent cached entries.</p>
<p>This page explains what Workers Caching puts into the cache key, why each component is there, and how to reason about it when designing your Worker.</p>
<h2 id="what-goes-into-the-cache-key">What goes into the cache key</h2>
<p>Workers Caching keys responses by:</p>
<ul>
<li>The <strong>target entrypoint</strong> — which specific <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#named-entrypoints">named entrypoint</a> of the Worker received the request. A <code>default</code> export and an exported class are different entrypoints and do not share a cache even if they produce identical responses.</li>
<li>The <strong>path and query string</strong> of the request URL. Query parameter order matters — <code>?a=1&amp;b=2</code> and <code>?b=2&amp;a=1</code> are different cache keys. Trailing slashes matter too.</li>
<li>The <strong>Worker version</strong>, by default. Each deployed version has its own cache, so a new deployment does not serve responses written by a previous version. You can turn this off with <a href="/workers/cache/configuration/#cross-version-caching"><code>cache.cross_version_cache</code></a> to share cached responses across versions. See <a href="#invalidating-cache-across-deployments">Invalidating cache across deployments</a>.</li>
<li>The invocation's <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#ctxprops"><code>ctx.props</code></a>, when the Worker is invoked through a service binding or RPC. See <a href="#multi-tenant-safety-with-ctxprops">Multi-tenant safety with <code>ctx.props</code></a>.</li>
</ul>
<p>As anti-cache-poisoning measures, the key also includes:</p>
<ul>
<li>The <code>x-http-method-override</code>, <code>x-http-method</code>, and <code>x-method-override</code> request headers.</li>
<li>The <code>x-forwarded-host</code>, <code>x-host</code>, <code>x-forwarded-scheme</code> (unless its value is <code>http</code> or <code>https</code>), <code>x-original-url</code>, <code>x-rewrite-url</code>, and <code>forwarded</code> request headers.</li>
<li>The value of the <code>Cloudflare-Workers-Version-Key</code> request header. This header is not set by Cloudflare automatically — it is only meaningful if a caller (for example, an upstream Worker or proxy) chooses to include it to explicitly partition the cache further. This is independent of the automatic per-version keying described above, which is controlled by <a href="/workers/cache/configuration/#cross-version-caching"><code>cache.cross_version_cache</code></a>.</li>
</ul>
<p>These three bullets are not something you should normally need to reason about. Some frameworks interpret the method-override and URL-rewrite headers as overriding the effective method or URL of a request, which can lead to <a href="https://portswigger.net/research/practical-web-cache-poisoning">cache poisoning</a> if two requests differ only in those headers but produce materially different responses. Including them in the cache key ensures a poisoned entry only affects requests that carry the same poisoned header.</p>
<p>Requests that differ only in request headers that are not part of the cache key (for example, <code>User-Agent</code>, <code>Accept-Language</code>, <code>Cookie</code>, or <code>Authorization</code>) return the same cached response. This is usually what you want — you do not want every user agent string or language preference producing a separate cache entry. If you do need content negotiation, set <a href="/workers/cache/configuration/#vary"><code>Vary</code></a> on the response, or handle it inside your Worker and produce a canonical response per URL.</p>
<p>Notably, the cache key does <strong>not</strong> include:</p>
<ul>
<li><strong>The HTTP method.</strong> <code>GET</code> and <code>HEAD</code> requests for the same URL share a single cache entry. A <code>HEAD</code> request can be served from a <code>GET</code> fill (Cloudflare returns the cached headers without the body). In the other direction, a <code>HEAD</code> request on a cold cache is converted to a <code>GET</code> internally so the full asset is fetched and stored — a subsequent <code>GET</code> then hits the entry that <code>HEAD</code> populated. (<code>POST</code>, <code>PUT</code>, <code>PATCH</code>, and <code>DELETE</code> are never cached at all, so the question does not arise for them.)</li>
<li><strong>The request's host.</strong> The Worker's cache is keyed by path and query string, not the full URL. See <a href="#the-cache-belongs-to-the-worker-not-to-a-domain">The cache belongs to the Worker, not to a domain</a>.</li>
<li><strong>The request body.</strong> Since only <code>GET</code> and <code>HEAD</code> are cacheable, this is rarely relevant — but worth noting if your Worker reads <code>request.body</code> on a cacheable method, the body does not partition the cache.</li>
</ul>
<p>At launch, you cannot inspect the exact cache key Cloudflare computed for a request. The primary signals you have for understanding cache behavior are the <code>Cf-Cache-Status</code> response header and per-invocation cache-hit information in the <a href="/workers/observability/">Workers observability dashboard</a>. See <a href="#inspecting-the-cache-key">Inspecting the cache key</a>.</p>
<h2 id="the-cache-belongs-to-the-worker-not-to-a-domain">The cache belongs to the Worker, not to a domain</h2>
<p>A Worker is a zoneless entity. It can be invoked through several different paths:</p>
<ul>
<li>Directly on a <code>workers.dev</code> subdomain.</li>
<li>Through a <a href="/workers/configuration/routing/routes/">route</a> on any zone you control.</li>
<li>Through a <a href="/workers/configuration/routing/custom-domains/">custom domain</a> — and you can bind the same Worker to many custom domains.</li>
<li>Through a <a href="/workers/runtime-apis/bindings/service-bindings/">service binding</a> from another Worker, with an arbitrary placeholder hostname in the URL.</li>
</ul>
<p>Workers Caching treats all of these as the same Worker and uses a single shared cache across them. The cache key does not include the host, so a request to <code>/api/users/42</code> hits the same cached entry whether it came in through <code>api.example.com</code>, <code>api.example.net</code>, a service binding, or a <code>workers.dev</code> URL.</p>
<p>This is the behavior you almost always want. A Worker's responses are a function of its code and its inputs, not of which domain the request arrived through — so caching them once and serving that response back to every ingress path maximizes the cache hit rate without losing correctness.</p>
<p>If you genuinely need different cached responses for the same path on different hostnames — for example, white-labeled tenants where <code>tenant-a.example.com/index</code> and <code>tenant-b.example.com/index</code> must produce different content — the cache key does not do this for you automatically. Instead, distinguish the tenants at your gateway Worker and pass the tenant identifier via <code>ctx.props</code>, which <em>is</em> part of the cache key.</p>
<h2 id="invalidating-cache-across-deployments">Invalidating cache across deployments</h2>
<p>By default, the currently invoked Worker version <strong>is</strong> part of the cache key. Each deployed version has its own cache, so:</p>
<ul>
<li>A new deployment starts from a cold cache and never serves responses that a previous version wrote.</li>
<li>Cache-affecting changes apply immediately when the new version goes live — you do not have to purge anything to stop serving old content.</li>
<li>During a <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployment</a>, the old and new versions populate independent caches, so a slice of traffic on the new version never receives the old version's responses.</li>
</ul>
<p>This is the default because it is the simplest behavior to reason about. The trade-off is that <strong>cache hit rate resets on every deployment</strong> — the first requests to a new version are misses while its cache fills. This is the most common reason a Worker's cache hit rate drops right after a deploy.</p>
<h3 id="share-the-cache-across-versions">Share the cache across versions</h3>
<p>If you deploy frequently and your responses rarely change between deployments, throwing away a warm cache on every deploy is wasteful. Set <a href="/workers/cache/configuration/#cross-version-caching"><code>cache.cross_version_cache</code></a> to <code>true</code> to drop the version from the cache key and share cached responses across versions. A response written by version A is then still served after version B is deployed, as long as its TTL has not expired.</p>
<p>This maximizes cache hit rate at the expense of slower rollouts: because a deployment no longer invalidates the cache, a change that alters response content will not take effect for already-cached entries until they expire or you purge them. When you have <code>cross_version_cache</code> enabled and need a deployment to take effect immediately, use one of the two tools below.</p>
<h3 id="tag-responses-by-version-purge-the-tag-on-rollback">Tag responses by version, purge the tag on rollback</h3>
<p>If you want fine-grained control, tag each cached response with the Worker version that produced it. Later, purging that version tag removes every entry that version wrote, without affecting cached responses from other versions.</p>
<p>This uses the <a href="/workers/runtime-apis/bindings/version-metadata/">version metadata binding</a> to read the current version ID at request time, and prepends it as a <code>Cache-Tag</code> value. See <a href="/workers/cache/purge/#version-specific-purging">Version-specific purging</a> for the full pattern with code.</p>
<p>This is the best option if you have enabled <code>cross_version_cache</code> and might need to roll back a specific version without blowing away cached content from working versions.</p>
<h3 id="purge-everything-after-deploy">Purge everything after deploy</h3>
<p>The simpler approach: after each deploy, hit a small Worker endpoint from your CI that calls <a href="/workers/cache/purge/#purge-everything"><code>ctx.cache.purge({ purgeEverything: true })</code></a>. The next request after the purge re-populates the cache from whichever Worker version is live at that moment.</p>
<p>This is coarser but requires zero in-Worker logic. Use it if you have enabled <code>cross_version_cache</code> but still want specific deployments to invalidate the cache. With the default per-version cache, deployments already start from a cold cache, so this is unnecessary.</p>
<h2 id="multi-tenant-safety-with-ctx-props">Multi-tenant safety with <code>ctx.props</code></h2>
<p>When your Worker is invoked through a <a href="/workers/runtime-apis/bindings/service-bindings/">service binding</a> or <a href="/workers/runtime-apis/bindings/service-bindings/rpc/">RPC</a>, the caller's <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#ctxprops"><code>ctx.props</code></a> is part of the cache key. Two callers that invoke your Worker with different <code>ctx.props</code> get <strong>separate cached entries</strong> — one caller can never receive another caller's cached response.</p>
<p>This is the mechanism that makes caching safe for multi-tenant Workers invoked over a service binding. If you use <code>ctx.props</code> to carry per-caller authorization context — user ID, tenant ID, organization, role — caching is safe by default. Responses that logically belong to one caller cannot leak to another through the cache.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16734.md")
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16733.md")
</aside>
<h3 id="service-binding-url">Service binding URL</h3>
<p>Service binding calls deserve a specific note because the URL you pass does not mean what you might think it means.</p>
<p>When you call a service binding with <a href="/workers/runtime-apis/bindings/service-bindings/#use-the-fetch-method"><code>fetch()</code></a>, the hostname in the URL is a placeholder. The request is routed via the binding, not by DNS — the hostname is never resolved. And because the host is not part of the cache key (as described in <a href="#the-cache-belongs-to-the-worker-not-to-a-domain">The cache belongs to the Worker, not to a domain</a>), the placeholder has no effect on caching either. Only the <strong>path</strong> (and query string) contribute to the cache key, alongside the target entrypoint and <code>ctx.props</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16735.md")
</div>
<p>If you want cached responses to differ for different callers, vary <code>ctx.props</code>. If you want them to differ by request, vary the path or query string. Varying the hostname does nothing.</p>
<h2 id="inspecting-the-cache-key">Inspecting the cache key</h2>
<p>At launch, two signals give you visibility into cache behavior:</p>
<ol>
<li>
<p><strong>The <code>Cf-Cache-Status</code> response header.</strong> The values you will see most often are <code>HIT</code>, <code>MISS</code>, <code>EXPIRED</code>, <code>REVALIDATED</code>, <code>UPDATING</code>, <code>STALE</code>, and <code>BYPASS</code>. <code>HIT</code> means Cloudflare returned a cached response without running your Worker. <code>MISS</code> means your Worker ran and the response was stored. <code>UPDATING</code> means the cached response was stale and your Worker ran in the background to refresh it. <code>BYPASS</code> means caching was disabled for this request. Refer to <a href="/cache/concepts/cache-responses/">Cloudflare cache responses</a> for the full set of values.</p>
</li>
<li>
<p><strong>Cache hits in the <a href="/workers/observability/">Workers observability dashboard</a>.</strong> Each invocation surfaces whether it was served from cache, so you can filter and aggregate cache-hit behavior across your Worker's traffic.</p>
</li>
</ol>
<p>Cloudflare does not currently expose the cache key composition itself. If two requests you expected to share a cached response do not, you have to reason about what part of the key differed from the components listed in <a href="#what-goes-into-the-cache-key">What goes into the cache key</a>. For a walkthrough of common caching problems and how to diagnose them, refer to <a href="/workers/cache/debugging/">Debugging</a>.</p>
<h2 id="custom-cache-keys">Custom cache keys</h2>
<p>By default, the path and query string of the request URL form the URL component of the cache key. When one entrypoint invokes another cached entrypoint through a <a href="/workers/runtime-apis/bindings/service-bindings/rpc/"><code>ctx.exports</code></a> loopback, the calling entrypoint can override that component by setting <code>cf.cacheKey</code> on the request.</p>
<p>In the example below, the <code>Backend</code> entrypoint is the cached one. The default entrypoint forwards requests to it through <code>ctx.exports</code>, choosing the cache key itself:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16736.md")
</div>
<p>A custom cache key <strong>replaces the path and query string</strong> in the cache key. Everything else described in <a href="#what-goes-into-the-cache-key">What goes into the cache key</a> still applies:</p>
<ul>
<li>The target entrypoint and the caller's <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#ctxprops"><code>ctx.props</code></a> remain part of the key. A custom cache key cannot reach across entrypoints or across <code>ctx.props</code>, so the <a href="#multi-tenant-safety-with-ctxprops">multi-tenant isolation</a> described above still holds even when callers choose their own keys. A custom key only ever addresses entries within the callee's own cache namespace.</li>
<li>Two requests with <strong>different URLs but the same <code>cf.cacheKey</code></strong> resolve to the same cache entry. This is how you collapse several URLs onto a single cached response.</li>
<li>Two requests with the <strong>same URL but different <code>cf.cacheKey</code></strong> resolve to separate cache entries.</li>
</ul>
<p>Set <code>cf.cacheKey</code> to an empty string, or omit it, to fall back to the default URL-derived key.</p>
<p>In this pattern the default entrypoint is a gateway that should run on every request, so disable caching on it and leave it on for <code>Backend</code> (see <a href="/workers/cache/configuration/#per-entrypoint-caching">Per-entrypoint caching</a>):</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16737.md")
</div>
<h3 id="what-you-can-do-with-a-custom-cache-key">What you can do with a custom cache key</h3>
<ul>
<li><strong>Ignore parts of the URL.</strong> Strip tracking parameters (<code>utm_source</code>, <code>gclid</code>), or drop a query string entirely, so that variations that do not change the response share one cache entry.</li>
<li><strong>Key on something other than the URL.</strong> Build the key from a value your gateway Worker trusts — for example, a normalized resource identifier — so that several equivalent URLs map to one entry.</li>
<li><strong>Partition the cache yourself.</strong> Append a discriminating value to the key (for example, a content version) to force separate entries for requests that would otherwise collide.</li>
</ul>
<p>For per-caller isolation, continue to use <a href="#multi-tenant-safety-with-ctxprops"><code>ctx.props</code></a> rather than encoding caller identity into the cache key — <code>ctx.props</code> is part of the key automatically and cannot be bypassed.</p>
<h3 id="custom-keys-apply-to-same-account-calls-only">Custom keys apply to same-account calls only</h3>
<p><code>cf.cacheKey</code> is honored only when the call stays within your account. Cloudflare drops the <code>cf</code> object whenever a request crosses an account boundary — for example, a service binding to a Worker owned by a different account. When that happens, the custom key is disregarded and the cache key falls back to the request URL, so a caller in one account can never influence (or probe) the cache of a Worker in another account.</p>
<p>This also means <code>cf.cacheKey</code> has no effect on eyeball requests. The <code>cf</code> object on an inbound request from a browser or API client is populated by Cloudflare, not by the client, so a client cannot set its own cache key.</p>
