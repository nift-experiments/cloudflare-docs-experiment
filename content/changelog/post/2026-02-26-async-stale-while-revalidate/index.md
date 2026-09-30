<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 26, 2026</time><h2 id="post-title">Asynchronous stale-while-revalidate</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>Cloudflare's <a href="/cache/concepts/cache-control/#revalidation"><code>stale-while-revalidate</code></a> support is now fully asynchronous. Previously, the first request for a stale (expired) asset in cache had to wait for an origin response, after which that visitor received a REVALIDATED or EXPIRED status. Now, the first request after the asset expires triggers revalidation in the background and immediately receives stale content with an UPDATING status. All following requests also receive stale content with an <code>UPDATING</code> status until the origin responds, after which subsequent requests receive fresh content with a <code>HIT</code> status.</p>
<p><code>stale-while-revalidate</code> is a <code>Cache-Control</code> directive set by your origin server that allows Cloudflare to serve an expired cached asset while a fresh copy is fetched from the origin.</p>
<p>Asynchronous revalidation brings:</p>
<ul>
<li><strong>Lower latency</strong>: No visitor is waiting for the origin when the asset is already in cache. Every request is served from cache during revalidation.</li>
<li><strong>Consistent experience</strong>: All visitors receive the same cached response during revalidation.</li>
<li><strong>Reduced error exposure</strong>: The first request is no longer vulnerable to origin timeouts or errors. All visitors receive a cached response while revalidation happens in the background.</li>
</ul>
<h4 id="availability">Availability</h4>
<p>This change is live for all Free, Pro, and Business zones. Approximately 75% of Enterprise zones have been migrated, with the remaining zones rolling out throughout the quarter.</p>
<h4 id="get-started">Get started</h4>
<p>To use this feature, make sure your origin includes the <code>stale-while-revalidate</code> directive in the <code>Cache-Control</code> header. Refer to the <a href="/cache/concepts/cache-control/#revalidation">Cache-Control documentation</a> for details.</p>
</div></article></div>
