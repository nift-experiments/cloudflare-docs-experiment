---
cp9:
  canonical: https://developers.cloudflare.com/workers/cache/limitations/
  description: Current limitations, unsupported scenarios, and how Workers Caching relates to other Cloudflare caches.
  full_title: Limitations · Cloudflare Workers docs
  head_html: <title>Limitations · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Current limitations, unsupported scenarios, and how Workers Caching relates to other Cloudflare caches."><link rel="canonical" href="https://developers.cloudflare.com/workers/cache/limitations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/cache/limitations/index.md"><meta property="og:title" content="Limitations · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Current limitations, unsupported scenarios, and how Workers Caching relates to other Cloudflare caches."><meta property="og:url" content="https://developers.cloudflare.com/workers/cache/limitations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/cache/limitations/#page","headline":"Limitations \u00b7 Cloudflare Workers docs","description":"Current limitations, unsupported scenarios, and how Workers Caching relates to other Cloudflare caches.","url":"https://developers.cloudflare.com/workers/cache/limitations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/cache/limitations/
  schema: 1
---
<p>This page lists the scenarios where Workers Caching does not apply, followed by notes on how it relates to other caches you may already be using.</p>
<h2 id="unsupported-scenarios">Unsupported scenarios</h2>
<h3 id="http-methods">HTTP methods</h3>
<p>Only <code>GET</code> and <code>HEAD</code> requests are cached. <code>POST</code>, <code>PUT</code>, <code>PATCH</code>, <code>DELETE</code>, and other methods always invoke your Worker.</p>
<p><code>GET</code> and <code>HEAD</code> for the same URL share a single cache entry. A <code>HEAD</code> request that arrives on a cold cache is converted to a <code>GET</code> internally so the cache is populated with the full asset. Refer to <a href="/workers/cache/cache-keys/#what-goes-into-the-cache-key">Cache keys</a>.</p>
<p>If you need to cache responses to non-idempotent requests, do so explicitly in your Worker — for example, by hashing the request body into a synthetic URL and making an internal <code>GET</code> subrequest.</p>
<h3 id="websocket-upgrades">WebSocket upgrades</h3>
<p>WebSocket upgrade requests (<code>GET</code> with <code>Upgrade: websocket</code>) bypass the cache and always invoke your Worker. WebSocket sessions are stateful by definition and are not a meaningful unit of caching.</p>
<h3 id="custom-rpc-methods">Custom RPC methods</h3>
<p>Only <code>fetch()</code> invocations on a <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#named-entrypoints"><code>WorkerEntrypoint</code></a> go through Workers Caching. Custom RPC methods like <code>ctx.exports.Backend.getUser(id)</code> bypass the cache and always run the callee, regardless of the entrypoint's <code>cache.enabled</code> setting.</p>
<p>To cache a piece of work that is currently exposed as an RPC method, refactor it to a <code>fetch</code> handler on its own entrypoint and call it with <code>fetch()</code>.</p>
<h3 id="status-codes-that-are-never-cached">Status codes that are never cached</h3>
<p>Workers Caching never stores the following responses, even with explicit <code>Cache-Control</code> directives:</p>
<ul>
<li><strong><code>520</code>–<code>526</code></strong> (Cloudflare failsafe responses) are treated as transient errors and always re-run the Worker.</li>
<li><strong><code>206 Partial Content</code></strong> returned by your Worker is not stored — Workers Caching expects your Worker to return the full <code>200</code> response and does the range slicing itself. Refer to <a href="/workers/cache/configuration/#range-requests"><code>Range</code> requests</a> for the supported pattern.</li>
</ul>
<h3 id="other-invocation-types">Other invocation types</h3>
<p>Workers Caching only applies to HTTP requests handled by a <code>fetch</code> handler on a <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#named-entrypoints">Worker entrypoint</a>. The following invocation types always run without cache involvement:</p>
<ul>
<li><a href="/workers/configuration/cron-triggers/">Cron Triggers</a> — scheduled invocations via the <code>scheduled</code> handler.</li>
<li><a href="/queues/configuration/javascript-apis/#consumer">Queue consumers</a> — messages delivered via the <code>queue</code> handler.</li>
<li><a href="/workflows/">Workflows</a> — workflow step execution.</li>
<li><a href="/workers/observability/logs/tail-workers/">Tail Workers</a> — trace event handlers.</li>
<li><a href="/durable-objects/">Durable Objects</a> — Durable Object invocations are never cached, regardless of handler or method. To cache a Durable Object's HTTP responses, wrap it behind a Worker entrypoint with caching enabled. See <a href="/workers/cache/#cache-durable-object-responses">Cache Durable Object responses</a>.</li>
</ul>
<h3 id="purge-by-host">Purge by host</h3>
<p>There is no &quot;purge by host&quot; mode. The cache <a href="/workers/cache/cache-keys/#the-cache-belongs-to-the-worker-not-to-a-domain">belongs to the Worker, not to a domain</a> — the host is not part of the cache key, so purging by host would not map onto anything the cache stores. Use <a href="/workers/cache/purge/#purge-by-tag">purge by tag</a>, <a href="/workers/cache/purge/#purge-by-path-prefix">purge by path prefix</a>, or <a href="/workers/cache/purge/#purge-everything"><code>purgeEverything</code></a> instead.</p>
<h3 id="cache-pre-warming">Cache pre-warming</h3>
<p>There is no API to pre-populate the cache with responses generated at build time. A response is only cached once it has been served at least once. If you need pre-rendered content available to the first requester, use <a href="/workers/static-assets/">Static Assets</a>.</p>
<h2 id="limits">Limits</h2>
<h3 id="response-size">Response size</h3>
<p>Response size limits are the same as Cloudflare's zone cache. For per-plan limits, refer to <a href="/cache/concepts/default-cache-behavior/#cacheable-size-limits">Cacheable size limits</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16692.md")
</aside>
<h3 id="cache-tag-limits"><code>Cache-Tag</code> limits</h3>
<p>Limits on the number, length, and character set of <code>Cache-Tag</code> values are the same as Cloudflare's zone cache. Refer to <a href="/cache/how-to/purge-cache/purge-by-tags/#a-few-things-to-remember">Cache tag limits</a> for the full list.</p>
<h3 id="purge-rate-limits">Purge rate limits</h3>
<p><code>ctx.cache.purge()</code> uses the same rate-limiting system as the zone purge API. However, because Workers Caching is associated with the Worker rather than the zone, Workers Caching always uses the <strong>Free tier limits</strong> described in <a href="/cache/how-to/purge-cache/#availability-and-limits">Availability and limits</a>, regardless of your account or zone plan.</p>
<h2 id="relationship-to-other-caches">Relationship to other caches</h2>
<h3 id="zone-level-cache-configuration">Zone-level cache configuration</h3>
<p>Workers Caching is <strong>your Worker's cache</strong>, not your zone's cache. It uses your Worker itself as the configuration surface, so there is no separate layer of rules or settings to configure alongside it. None of the following applies to Workers Caching:</p>
<table>
<thead>
<tr>
<th>Zone-level feature</th>
<th>Equivalent in Workers Caching</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cache/how-to/cache-rules/">Cache Rules</a> and <a href="/cache/how-to/cache-response-rules/">Cache Response Rules</a></td>
<td>Set <code>Cache-Control</code> headers in your Worker, or branch on the request and return different headers per path.</td>
</tr>
<tr>
<td><a href="/cache/how-to/cache-rules/settings/#cache-key">Cache key customization in Cache Rules</a></td>
<td>Workers Caching has its own key composition; see <a href="/workers/cache/cache-keys/">Cache keys</a>. Shape the key by shaping the request (for example, by rewriting the URL or setting <code>ctx.props</code> in a gateway Worker).</td>
</tr>
<tr>
<td>Zone-level cache level settings (bypass / standard / aggressive / ignore query string)</td>
<td><code>Cache-Control</code> headers on the response express the same intent at a per-request level.</td>
</tr>
<tr>
<td>The zone's default cached-file-extensions list</td>
<td>Workers Caching caches any response whose headers say it is cacheable, regardless of file extension.</td>
</tr>
<tr>
<td>Custom tiered cache topologies</td>
<td>Workers Caching uses a generic tiered cache topology by default. Because a Worker can execute anywhere, a fixed custom topology does not apply — future integrations with <a href="/workers/configuration/placement/">Smart Placement</a> may tailor tiering further.</td>
</tr>
<tr>
<td><a href="/ruleset-engine/">Rulesets</a> that modify request or response before cache</td>
<td>Transform the request or response in your Worker's code before returning it.</td>
</tr>
</tbody>
</table>
<p>To influence your Worker's cache, change your Worker. <code>Cache-Control</code> headers, <code>ctx.props</code>, service binding composition, and <a href="/workers/cache/purge/"><code>ctx.cache.purge()</code></a> cover the configuration surface.</p>
<h3 id="cache-api-caches-default">Cache API (<code>caches.default</code>)</h3>
<p>The <a href="/workers/runtime-apis/cache/">Cache API</a> is a separate programmatic cache store. It is independent of Workers Caching — operations on one do not affect the other, and <code>ctx.cache.purge()</code> is what invalidates Workers-Caching entries.</p>
<p>For new Workers, prefer Workers Caching. The Cache API, by design, is a lower-level primitive:</p>
<ul>
<li>It does not read through — responses are only cached when your Worker explicitly calls <code>put()</code>, and every request still executes your Worker on the way in.</li>
<li>It does not <a href="/workers/cache/#request-collapsing">collapse concurrent requests</a> for the same resource. A burst of traffic to a fresh URL invokes your Worker once per request.</li>
<li>It does not participate in <a href="/cache/how-to/tiered-cache/">tiered caching</a>.</li>
</ul>
<p>Workers Caching provides all three automatically. The Cache API remains useful when you need fine-grained programmatic control.</p>
<h3 id="fetch-subrequest-caching"><code>fetch()</code> subrequest caching</h3>
<p>Workers Caching is a server-side cache <strong>in front of</strong> your Worker. It is a separate cache from the one that sits in front of outgoing <a href="/workers/runtime-apis/fetch/"><code>fetch()</code></a> subrequests your Worker makes to its own origins. The two operate independently: a <code>fetch()</code> subrequest hit saves a trip to your origin, while a Workers Caching hit saves your Worker from running at all.</p>
<p>The <code>cf</code> properties on a <code>Request</code> behave differently across the two:</p>
<table>
<thead>
<tr>
<th><code>cf</code> property</th>
<th>On outgoing <code>fetch()</code> to your origin</th>
<th>On <code>ctx.exports.&lt;Entrypoint&gt;.fetch()</code></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.cacheKey</code></td>
<td>Supported</td>
<td>Supported — see <a href="/workers/cache/cache-keys/#custom-cache-keys">Custom cache keys</a></td>
</tr>
<tr>
<td><code>cf.cacheControl</code></td>
<td>Supported</td>
<td>Supported — see <a href="/workers/cache/configuration/#override-cache-control-from-the-calling-worker">Override <code>Cache-Control</code> from the calling Worker</a></td>
</tr>
<tr>
<td><code>cf.cacheTtl</code></td>
<td>Supported</td>
<td>Not supported — set the TTL by returning <code>Cache-Control: max-age=N</code> (or <code>s-maxage=N</code>) from the callee, or by overriding it with <code>cf.cacheControl</code> from the caller</td>
</tr>
<tr>
<td><code>cf.cacheEverything</code></td>
<td>Supported</td>
<td>Not supported — Workers Caching decides cacheability from the response's <code>Cache-Control</code>; there is no override to force-cache an otherwise uncacheable response</td>
</tr>
</tbody>
</table>
<h2 id="coming-soon">Coming soon</h2>
<p>The following surfaces are in development:</p>
<ul>
<li><strong>Dashboard UI</strong> for enabling caching without Wrangler.</li>
<li><strong>Cache Analytics in Workers Observability</strong>.</li>
</ul>
