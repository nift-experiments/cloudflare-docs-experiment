<p>This page describes how Cloudflare's cache system behaves in interaction with:</p>
<ul>
<li><code>HEAD</code> requests</li>
<li><code>Set-Cookie</code> response headers</li>
</ul>
<h2 id="interaction-of-head-requests-with-cache">Interaction of <code>HEAD</code> requests with Cache</h2>
<p>Cloudflare converts <code>HEAD</code> requests to <code>GET</code> requests for <a href="/cache/concepts/default-cache-behavior/#default-cached-file-extensions">cacheable requests</a>.</p>
<p>When you make a <code>HEAD</code> request for a cacheable resource and Cloudflare does not have that resource in the edge cache, a cache miss happens. Cloudflare will send a <code>GET</code> request to your origin, cache the full response and return the response headers only. Make sure the origin server is set up to handle <code>GET</code> requests, even if only <code>HEAD</code> requests are expected, so that compatibility with this behavior is ensured.</p>
<h2 id="interaction-of-set-cookie-response-header-with-cache">Interaction of <code>Set-Cookie</code> response header with Cache</h2>
<p>For non-cacheable requests, <code>Set-Cookie</code> is always preserved. For cacheable requests, there are three possible behaviors:</p>
<ul>
<li>
<p><code>Set-Cookie</code> is returned from origin and the default cache level is used. If <a href="/cache/concepts/cache-control/">origin cache control</a> is not enabled, Cloudflare removes the <code>Set-Cookie</code> and caches the asset. If origin cache control is enabled, Cloudflare does not cache the asset and preserves the <code>Set-Cookie</code>. A cache status of <code>BYPASS</code> is returned.</p>
</li>
<li>
<p><code>Set-Cookie</code> is returned from origin and the cache level is set to <code>Cache Everything</code> in Page Rules, or <code>Eligible for cache</code> in Cache Rules. In this case, Cloudflare preserves the <code>Set-Cookie</code> but does not cache the asset. A cache <code>MISS</code> will be returned every time.</p>
</li>
<li>
<p><code>Set-Cookie</code> is returned from origin, the cache level is set to <code>Cache Everything</code> in Page Rules, or <code>Eligible for cache</code> in Cache Rules, and edge cache TTL is explicitly set using either the &quot;Ignore cache-control header and use this TTL&quot; or &quot;Status code TTL&quot; setting. In this case, Cloudflare removes the <code>Set-Cookie</code> and the asset is cached.</p>
</li>
</ul>
