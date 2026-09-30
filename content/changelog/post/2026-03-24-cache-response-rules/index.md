<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 24, 2026</time><h2 id="post-title">Cache Response Rules</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now control how Cloudflare handles origin responses without changing your origin. Cache Response Rules let you modify <code>Cache-Control</code> directives, manage cache tags, and strip headers like <code>Set-Cookie</code> from origin responses <em>before</em> they reach Cloudflare's cache. Whether traffic is cached or passed through dynamically, these rules give you control over origin response behavior that was previously out of reach.</p>
<h4 id="what-changed">What changed</h4>
<p>Cache Rules previously only operated on request attributes. Cache Response Rules introduce a new response phase that evaluates origin responses and lets you act on them before caching. You can now:</p>
<ul>
<li><strong>Modify <code>Cache-Control</code> directives</strong>: Set or remove individual directives like <code>no-store</code>, <code>no-cache</code>, <code>max-age</code>, <code>s-maxage</code>, <code>stale-while-revalidate</code>, <code>immutable</code>, and more. For example, remove a <code>no-cache</code> directive your origin sends so Cloudflare can cache the asset, or set an <code>s-maxage</code> to control how long Cloudflare stores it.</li>
<li><strong>Set a different browser <code>Cache-Control</code></strong>: Send a different <code>Cache-Control</code> header downstream to browsers and other clients than what Cloudflare uses internally, giving you independent control over edge and browser caching strategies.</li>
<li><strong>Manage cache tags</strong>: Add, set, or remove cache tags on responses, including converting tags from another CDN's header format into Cloudflare's <code>Cache-Tag</code> header. This is especially useful if you are migrating from a CDN that uses a different tag header or delimiter.</li>
<li><strong>Strip headers that block caching</strong>: Remove <code>Set-Cookie</code>, <code>ETag</code>, or <code>Last-Modified</code> headers from origin responses before caching, so responses that would otherwise be treated as uncacheable can be stored and served from cache.</li>
</ul>
<h4 id="benefits">Benefits</h4>
<ul>
<li><strong>No origin changes required</strong>: Fix caching behavior entirely from Cloudflare, even when your origin configuration is locked down or managed by a different team.</li>
<li><strong>Simpler CDN migration</strong>: Match caching behavior from other CDN providers without rewriting your origin. Translate cache tag formats and override directives that do not align with Cloudflare's defaults.</li>
<li><strong>Native support, fewer workarounds</strong>: Functionality that previously required workarounds is now built into Cache Rules with full Tiered Cache compatibility.</li>
<li><strong>Fine-grained control</strong>: Use expressions to match on request and response attributes, then apply precise cache settings per rule. Rules are stackable and composable with existing Cache Rules.</li>
</ul>
<h4 id="get-started">Get started</h4>
<p>Configure Cache Response Rules in the <a href="https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules">Cloudflare dashboard</a> under <strong>Caching</strong> &gt; <strong>Cache Rules</strong>, or via the <a href="https://developers.cloudflare.com/ruleset-engine/rulesets-api/">Rulesets API</a>. For more details, refer to the <a href="https://developers.cloudflare.com/cache/how-to/cache-response-rules/">Cache Rules documentation</a>.</p>
</div></article></div>
