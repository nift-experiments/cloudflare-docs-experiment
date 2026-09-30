<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 26, 2026</time><h2 id="post-title">BYPASS status now returned for uncacheable responses</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>Cloudflare now returns a <code>BYPASS</code> <a href="/cache/concepts/cache-responses/">cache status</a> whenever a response is not cacheable, instead of the previous mix of <code>BYPASS</code> and <code>MISS</code> that depended on why Cloudflare chose not to cache the response.</p>
<p>There are multiple reasons Cloudflare may refuse to cache a response — for example, the response exceeds the <a href="/cache/concepts/default-cache-behavior/#cacheable-size-limits">maximum cacheable file size</a> for your plan, the origin sends <code>Cache-Control: no-cache</code>, <code>private</code>, or <code>max-age=0</code>, the response includes a <code>Set-Cookie</code> header, or the request includes an <code>Authorization</code> header.</p>
<p>Previously, only some of these conditions returned <code>BYPASS</code>. Others — such as responses exceeding the maximum cacheable file size — returned <code>MISS</code> on every request, regardless of whether <a href="/cache/concepts/cache-control/#origin-cache-control-behavior">Origin Cache Control</a> was on or off. Because the response could never be cached, every subsequent request also returned <code>MISS</code>, which looked indistinguishable from a broken cache and made it hard to tell whether Cloudflare was trying and failing to cache the asset or had deliberately chosen not to cache it.</p>
<p><code>BYPASS</code> now consistently signals that Cloudflare refused to cache the response, regardless of the reason. <code>MISS</code> is reserved for cacheable responses that simply were not in the local cache at request time.</p>
<h4 id="what-to-expect-in-your-analytics">What to expect in your analytics</h4>
<p>After this change rolls out, you should see:</p>
<ul>
<li><strong>MISS rate decreases</strong>: Uncacheable responses no longer count as cache misses.</li>
<li><strong>BYPASS rate increases</strong>: These same responses are now reported as bypasses.</li>
<li><strong>Cache hit ratio increases</strong>: Hit ratio calculations no longer include uncacheable traffic that could never have been cached, giving you a more accurate view of cache effectiveness.</li>
</ul>
<p>Your total request volume and origin traffic are unchanged — only the cache status label is different.</p>
<h4 id="browser-cache-ttl-behavior-is-preserved">Browser cache TTL behavior is preserved</h4>
<p>The cache status label is the only thing changing — browser cache TTL handling for any given response is identical to what it was before:</p>
<ul>
<li>Responses that historically returned <code>MISS</code> because Cloudflare refused to cache them (for example, responses over the maximum cacheable file size) now return <code>BYPASS</code>, but continue to have browser cache TTL applied — exactly as they did when they were labeled <code>MISS</code>.</li>
<li>Responses that historically returned <code>BYPASS</code> and skipped browser cache TTL continue to skip browser cache TTL.</li>
</ul>
<p>In both cases, the decision to apply browser cache TTL depends on the underlying reason Cloudflare did not cache the response, not on the new <code>BYPASS</code> label.</p>
</div></article></div>
