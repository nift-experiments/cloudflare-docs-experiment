<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 2, 2026</time><h2 id="post-title">Cache multiple versions of a URL with Vary</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>Your origin can serve different responses for the same URL — different languages based on <code>Accept-Language</code>, or different formats based on <code>Accept</code> — by returning a <a href="https://www.rfc-editor.org/rfc/rfc9110.html#name-vary"><code>Vary</code></a> response header. Cloudflare's cache now honors that header directly in <a href="/cache/how-to/cache-rules/">Cache Rules</a>, so the same URL can hold multiple cached versions and each request is matched to the right one. Content that previously had to bypass cache to stay correct can now be cached, following standard <a href="https://www.rfc-editor.org/rfc/rfc9111.html#name-calculating-cache-keys-with">HTTP caching behavior</a>.</p>
<h4 id="what-changed">What changed</h4>
<p>Your origin now decides which request headers matter by listing them in its <code>Vary</code> response, and you control how Cloudflare treats each one. When you have enabled Vary using a cache rule and a response includes a <code>Vary</code> header, the request headers listed become part of the cache key.</p>
<p>For each header your origin varies on, choose one of three actions:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Behavior</th>
<th>Best for</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>normalize</code></td>
<td>Converts equivalent header values to the same cache key value before matching, collapsing redundant versions.</td>
<td>Most <code>Accept</code>, <code>Accept-Language</code>, and <code>Accept-Encoding</code> use cases.</td>
</tr>
<tr>
<td><code>passthrough</code></td>
<td>Uses the raw header value to select the cached version and forwards it to the origin unchanged.</td>
<td>When byte-for-byte differences in the header value should create versions.</td>
</tr>
<tr>
<td><code>bypass</code></td>
<td>Bypasses cache whenever this header name appears in the origin's <code>Vary</code> response.</td>
<td>Per-user values, or headers with too many possible values to cache safely.</td>
</tr>
</tbody>
</table>
<h4 id="benefits">Benefits</h4>
<ul>
<li><strong>Higher cache hit ratios</strong>: <code>normalize</code> treats semantically equivalent headers as one version. For example, <code>Accept-Language: en-US, fr;q=0.8</code> and <code>Accept-Language: fr;q=0.8, en-GB</code> both resolve to the same cache key, so you serve more requests from cache instead of the origin.</li>
<li><strong>Correct content negotiation</strong>: Requests always receive the cached version that matches their headers, so language and format variants stay accurate.</li>
<li><strong>No origin or Worker changes required</strong>: If your origin already sends <code>Vary</code>, you configure the behavior entirely in Cache Rules.</li>
<li><strong>Standards-aligned</strong>: Cache key calculation follows RFC 9111, and <code>Vary: *</code> continues to bypass cache as required by RFC 9110.</li>
</ul>
<h4 id="availability">Availability</h4>
<p>Vary in Cache Rules is available on all plans (Free, Pro, Business, and Enterprise). For per-request control in Workers subrequests, use the <a href="/workers/runtime-apis/request/#the-cfvary-property"><code>cf.vary</code></a> property.</p>
<h4 id="get-started">Get started</h4>
<p>Configure Vary in the <a href="https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules">Cloudflare dashboard</a> under <strong>Caching</strong> &gt; <strong>Cache Rules</strong>, or through the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a>. To learn how Vary affects cache keys and how each action works, refer to <a href="/cache/concepts/vary/">Vary</a> and the <a href="/cache/how-to/cache-rules/settings/#vary">Cache Rules Vary setting</a>.</p>
</div></article></div>
