---
cp9:
  canonical: https://developers.cloudflare.com/workers/cache/purge/
  description: Invalidate cached responses using ctx.cache.purge() — purge by tag, by path prefix, or purge everything.
  full_title: Purging the cache · Cloudflare Workers docs
  head_html: <title>Purging the cache · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Invalidate cached responses using ctx.cache.purge() — purge by tag, by path prefix, or purge everything."><link rel="canonical" href="https://developers.cloudflare.com/workers/cache/purge/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/cache/purge/index.md"><meta property="og:title" content="Purging the cache · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Invalidate cached responses using ctx.cache.purge() — purge by tag, by path prefix, or purge everything."><meta property="og:url" content="https://developers.cloudflare.com/workers/cache/purge/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/cache/purge/#page","headline":"Purging the cache \u00b7 Cloudflare Workers docs","description":"Invalidate cached responses using ctx.cache.purge() \u2014 purge by tag, by path prefix, or purge everything.","url":"https://developers.cloudflare.com/workers/cache/purge/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/cache/purge/
  schema: 1
---
<p>Your Worker can invalidate its own cached responses at any time using the purge API. Purging is useful when data changes and the new value is more important than the performance benefit of continuing to serve the cached response — for example, after a content update, a user action, or a webhook from an upstream system.</p>
<p>Because Workers Caching is <strong>your Worker's cache</strong>, purging is scoped to the Worker that owns the cache. Within a Worker, purges are further scoped to the <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#named-entrypoints">entrypoint</a> that called <code>purge()</code>. A Worker cannot reach into another Worker's cache, an entrypoint cannot reach into another entrypoint's cache, and no zone-level purge (via the dashboard, <a href="/cache/how-to/purge-cache/">API</a>, or Terraform) affects Workers Caching content.</p>
<h2 id="two-ways-to-call-purge">Two ways to call purge</h2>
<p>There are two equivalent ways to trigger a purge from inside your Worker:</p>
<ul>
<li><strong><code>ctx.cache.purge(...)</code></strong> — available on the execution context passed to every handler. Use this when you already have <code>ctx</code> in scope.</li>
<li><strong><code>cache.purge(...)</code></strong> — imported from <code>cloudflare:workers</code>. Use this when you want to call purge from code that does not receive <code>ctx</code> — for example, a utility module shared across multiple handlers, or a framework adapter that does not thread the execution context through its internals.</li>
</ul>
<p>Both forms call into the same API and behave identically. Pick whichever reads more cleanly for your code.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16679.md")
</div>
<p>The rest of this page uses <code>ctx.cache.purge(...)</code> in most examples because those examples already have <code>ctx</code> in scope. If you prefer the import form, substitute <code>cache.purge(...)</code> — nothing else changes.</p>
<h2 id="purge-modes">Purge modes</h2>
<p><code>purge()</code> accepts either <code>purgeEverything: true</code> on its own, or one or both of <code>tags</code> and <code>pathPrefixes</code>:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Purges</th>
<th>Scope</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>tags</code></td>
<td>Every cached response tagged with one of the given values via <code>Cache-Tag</code>.</td>
<td>Per entrypoint</td>
</tr>
<tr>
<td><code>pathPrefixes</code></td>
<td>Every cached response whose request path starts with one of the given prefixes.</td>
<td>Per entrypoint</td>
</tr>
<tr>
<td><code>purgeEverything</code></td>
<td>Every cached response for the entrypoint that called <code>purge()</code>.</td>
<td>Per entrypoint</td>
</tr>
</tbody>
</table>
<p><code>purgeEverything</code> is exclusive — combine <code>tags</code> and <code>pathPrefixes</code> in a single call if you want, but do not pass either alongside <code>purgeEverything</code>.</p>
<p>All three modes are scoped to the <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#named-entrypoints">entrypoint</a> that called <code>purge()</code>. A purge from <code>PublicAPI</code> does not affect cached responses stored by <code>AdminAPI</code>, even if they share tag names or path prefixes. To invalidate across every entrypoint of a Worker, call <code>purge()</code> from each entrypoint.</p>
<p>The returned promise resolves to a result object you can inspect to confirm success or handle failures — see <a href="#return-value">Return value</a>.</p>
<p>Purge after a write by calling <code>ctx.cache.purge()</code> at the end of any handler that mutates data:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16680.md")
</div>
<p>You can combine fields in a single call. For example, <code>purge({ tags: [&quot;blog-posts&quot;], pathPrefixes: [&quot;/blog/&quot;] })</code> purges everything that matches <strong>either</strong> tag or path-prefix — the fields are unioned, not intersected. Use this when one logical invalidation affects responses tagged by multiple schemes.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16681.md")
</div>
<h2 id="purge-by-tag">Purge by tag</h2>
<p>Tags are attached to responses via the <code>Cache-Tag</code> response header, and purged later by name. This is the most flexible and commonly used purge method.</p>
<h3 id="attach-tags-on-write">Attach tags on write</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16682.md")
</div>
<p>The <code>Cache-Tag</code> header value is a comma-separated list of tags. Cloudflare strips this header before returning the response to clients.</p>
<p>Tag values must be <strong>printable ASCII</strong> (no spaces, no Unicode), each tag is at most <strong>1024 characters</strong> long, and a response can carry up to <strong>1000 tags</strong>. Tag matching at purge time is <strong>case-insensitive</strong>, so <code>Foo</code> and <code>foo</code> purge the same set of responses. Invalid tags are silently dropped at storage time — the response is still cached with the remaining valid tags. Refer to <a href="/cache/how-to/purge-cache/purge-by-tags/#a-few-things-to-remember">Cache tag limits</a> for the full list.</p>
<h3 id="trigger-the-purge">Trigger the purge</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16683.md")
</div>
<h3 id="tag-scope-across-entrypoints">Tag scope across entrypoints</h3>
<p>Tags are scoped to the entrypoint that called <code>purge()</code>. A tag named <code>user-42</code> applied to responses in two different entrypoints is <strong>not</strong> invalidated by a single <code>purge({ tags: [&quot;user-42&quot;] })</code> call — it only affects the entrypoint the call originated from. If you need to invalidate the same tag across several entrypoints, call <code>purge()</code> from each entrypoint, or centralize purge calls in a shared entrypoint that caches every response you later need to invalidate.</p>
<h3 id="use-hierarchical-tags">Use hierarchical tags</h3>
<p>To invalidate groups of related responses in one call, tag each response with multiple tags representing every level of hierarchy it belongs to — sometimes called &quot;soft tags&quot;:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16684.md")
</div>
<p>Purging the tag <code>_path:/blog/2025/</code> then invalidates every cached response whose URL starts with <code>/blog/2025/</code>.</p>
<p>For limits on the number, length, and character set of tags, refer to <a href="/cache/how-to/purge-cache/purge-by-tags/#a-few-things-to-remember">Cache tag limits</a>.</p>
<h3 id="version-specific-purging">Version-specific purging</h3>
<p>By default, Workers Caching <a href="/workers/cache/cache-keys/#invalidating-cache-across-deployments">partitions the cache by Worker version</a>, so each deployment already starts from a cold cache and version-specific purging is unnecessary. This section applies only when you have enabled <a href="/workers/cache/configuration/#cross-version-caching"><code>cache.cross_version_cache</code></a> to share cached responses across versions. In that case, a response written by version A may still be served after version B is deployed, and you may want to purge the entries a specific version wrote — for example, after a rollback. To do that, tag each response with the version that produced it and purge that tag later.</p>
<p>Add the <a href="/workers/runtime-apis/bindings/version-metadata/">version metadata binding</a> to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16685.md")
</div>
<p>Then prepend the version ID to your tags:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16686.md")
</div>
<p>When you want to invalidate everything a specific version wrote — for example, after a rollback — purge the version tag:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16687.md")
</div>
<h2 id="purge-by-path-prefix">Purge by path prefix</h2>
<p><code>pathPrefixes</code> invalidates every cached response whose <strong>request path</strong> begins with one of the given prefixes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16688.md")
</div>
<p>Entries in <code>pathPrefixes</code> are <strong>paths</strong>, not full URLs. A prefix must not include a scheme, host, query string, or fragment — passing something like <code>https://example.com/blog/</code> is invalid input, not a prefix that simply fails to match. A leading slash is optional (<code>/images</code> and <code>images</code> are treated the same) but recommended for clarity.</p>
<p><code>pathPrefixes</code> is scoped to the entrypoint that makes the purge call. A <code>purge({ pathPrefixes: [&quot;/blog/&quot;] })</code> from <code>PublicAPI</code> will not affect cached responses stored by <code>AdminAPI</code>, even when their paths also start with <code>/blog/</code>.</p>
<h3 id="purge-a-single-url">Purge a single URL</h3>
<p>There is no dedicated &quot;purge by URL&quot; mode. To invalidate a single cached URL, pass its path as a single-element <code>pathPrefixes</code> array:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16689.md")
</div>
<p>Because <code>pathPrefixes</code> matches on the start of the request path, passing the full path matches only that path — plus any paths that happen to extend it (for example, <code>/blog/2026/hello-world-2</code>). If you need exact-match semantics with no risk of over-purge, use a <a href="#purge-by-tag">tag</a> instead.</p>
<h2 id="purge-everything">Purge everything</h2>
<p>Invalidate every cached response stored by the calling entrypoint:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16690.md")
</div>
<p>Use this sparingly. Purging everything causes all subsequent requests to miss the cache until they can be re-filled, which temporarily increases load on your Worker and any upstream services it calls.</p>
<h2 id="purge-propagation">Purge propagation</h2>
<p>Purges triggered by <code>ctx.cache.purge()</code> use Cloudflare's <a href="/cache/how-to/purge-cache/">Instant Purge</a> infrastructure and propagate globally with the same guarantees as zone-level purges.</p>
<h2 id="return-value">Return value</h2>
<p><code>purge()</code> resolves to a result object. Check <code>success</code> to confirm the purge was accepted, and inspect <code>errors</code> if it was not:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16691.md")
</div>
<p>On failure, each error in <code>errors</code> carries a numeric <code>code</code> and a human-readable <code>message</code> you can log or surface to the caller.</p>
<h2 id="rate-limits">Rate limits</h2>
<p><code>purge()</code> uses the same rate-limiting system as Cloudflare's zone purge API. However, because Workers Caching is associated with the Worker rather than the zone, Workers Cache always uses the <strong>Free tier limits</strong> described in <a href="/cache/how-to/purge-cache/#availability-and-limits">Availability and limits</a>, regardless of your account or zone plan. When the purge is rate-limited, <code>success</code> is <code>false</code> and <code>errors</code> contains an entry describing the rejection.</p>
