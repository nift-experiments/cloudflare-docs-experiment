<p>The <code>CF-Cache-Status</code> header output indicates whether a resource is cached or not. To investigate cache responses returned by this header, use services like <a href="https://redbot.org/">Redbot</a>, <a href="http://www.webpagetest.org/">webpagetest.org</a>, or a visual tool like <a href="https://chromewebstore.google.com/detail/cloudflare-optics/mdjgbjnbdnhneejmmaabmccfehigbjbe">Cloudflare Optics plugin</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="age-response-header">Age response header</h3>
@markup("md", "content/.markup/bodies/3821.md")
</aside>
<p>Below you can find a comprehensive breakdown of Cloudflare's cache response statuses.</p>
<h2 id="hit">HIT</h2>
<p>The resource was found in Cloudflare's cache.</p>
<h2 id="miss">MISS</h2>
<p>The response is eligible for cache but was not present in Cloudflare's cache at request time, so it was served from the origin web server. Responses that Cloudflare chooses not to cache return <a href="#bypass"><code>BYPASS</code></a> instead of <code>MISS</code>.</p>
<h2 id="none-unknown">NONE/UNKNOWN</h2>
<p>Cloudflare generated a response that denotes the asset is not eligible for caching. This may have happened because:</p>
<ul>
<li>
<p>A Worker generated a response without sending any subrequests. In this case, the response did not come from cache, so the cache status will be <code>none/unknown</code>.</p>
</li>
<li>
<p>A Worker request made a subrequest (<code>fetch</code>). In this case, the subrequest will be logged with a cache status, while the main request will be logged with <code>none/unknown</code> status (the main request did not hit cache, since Workers sits in front of cache).</p>
</li>
<li>
<p>A WAF custom rule was triggered to block a request. The response will come from the Cloudflare global network before it hits cache. Since there is no cache status, Cloudflare will log as <code>none/unknown</code>.</p>
</li>
<li>
<p>A <a href="/rules/url-forwarding/">redirect rule</a> or <a href="/ssl/edge-certificates/additional-options/always-use-https/">Always Use HTTPS</a> caused the global network to respond with a redirect to another asset/URL. This redirect response happens before the request reaches cache, so the cache status is <code>none/unknown</code>.</p>
</li>
</ul>
<h2 id="expired">EXPIRED</h2>
<p>The resource was found in Cloudflare's cache but was expired and served from the origin web server.</p>
<h2 id="stale">STALE</h2>
<p>The resource was served from Cloudflare's cache but was expired. Cloudflare could not contact the origin web server to retrieve an updated resource.</p>
<h2 id="bypass">BYPASS</h2>
<p>Cloudflare considered the asset eligible for cache at request time — either because it matches the <a href="/cache/concepts/default-cache-behavior/#default-cached-file-extensions">default cached file extensions</a>, or because a <a href="/cache/how-to/cache-rules/">Cache Rule</a> enabled caching for it — but the origin response was ultimately not cacheable.</p>
<p>Common reasons the origin response is treated as not cacheable include:</p>
<ul>
<li>The response exceeds the <a href="/cache/concepts/default-cache-behavior/#cacheable-size-limits">maximum cacheable file size</a> for your plan.</li>
<li>The origin returned <code>no-store</code> or bare <code>private</code> in a <code>Cloudflare-CDN-Cache-Control</code> or <code>CDN-Cache-Control</code> header. Cloudflare evaluates these headers ahead of <code>Cache-Control</code>, in the precedence <code>Cloudflare-CDN-Cache-Control</code> &gt; <code>CDN-Cache-Control</code> &gt; <code>Cache-Control</code> — so an origin returning <code>Cache-Control: public, max-age=3600</code> together with <code>CDN-Cache-Control: no-store</code> produces <code>BYPASS</code>. A <a href="/cache/how-to/cache-rules/">Cache Rule</a> with an <a href="/cache/how-to/cache-rules/settings/#edge-ttl">Edge Cache TTL</a> setting that ignores origin cache-control overrides these directives, same as it does for <code>Cache-Control: no-store</code>. <code>no-cache</code>, <code>max-age=0</code>, or <code>s-maxage=0</code> in these headers do not produce <code>BYPASS</code>. They produce <code>MISS</code> on the first request, then <a href="#revalidated"><code>REVALIDATED</code></a> or <a href="#expired"><code>EXPIRED</code></a>. Refer to <a href="/cache/concepts/cdn-cache-control/">CDN-Cache-Control</a> for the precedence rules.</li>
<li>The origin returned <code>Cache-Control: no-store</code> or <code>private</code>. These directives prevent caching in either <a href="/cache/concepts/cache-control/">Origin Cache Control</a> mode.</li>
<li>The origin returned <code>Cache-Control: no-cache</code>, <code>max-age=0</code>, or <code>s-maxage=0</code>, and <a href="/cache/concepts/cache-control/">Origin Cache Control</a> is disabled (the default on Enterprise plans). With Origin Cache Control enabled (the default on Free, Pro, and Business plans), these directives cause Cloudflare to cache and revalidate the response instead, producing <a href="#revalidated"><code>REVALIDATED</code></a> or <a href="#expired"><code>EXPIRED</code></a>. Refer to <a href="/cache/concepts/cache-control/#understand-no-store-and-no-cache-directives">Understand <code>no-store</code> and <code>no-cache</code> directives</a> and the <a href="/cache/concepts/cache-control/#conditions">Conditions</a> table.</li>
<li>The origin returned a <code>Set-Cookie</code> header. Refer to <a href="/cache/concepts/cache-behavior/#interaction-of-set-cookie-response-header-with-cache">Interaction of <code>Set-Cookie</code> response header with Cache</a> for the specific configurations that produce <code>BYPASS</code>.</li>
<li>The origin returned a <code>Vary: *</code> response header, which always bypasses cache.</li>
<li>The request included an <code>Authorization</code> header and <a href="/cache/concepts/cache-control/">Origin Cache Control</a> is enabled (the default on Free, Pro, and Business plans). In that mode, the response is cacheable only if <code>Cache-Control</code> also includes <code>public</code>, <code>s-maxage</code>, or <code>must-revalidate</code>. On Enterprise plans with Origin Cache Control disabled, <code>Authorization</code> does not by itself prevent caching.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3820.md")
</aside>
<p>BYPASS means the decision not to cache was made at <strong>response time</strong> — the request was initially eligible for caching, but the origin response or response headers instructed Cloudflare not to cache. For example, a Cache Rule that sets <code>&quot;cache&quot;: true</code> enables caching at request time, but if the origin returns <code>Cache-Control: no-store</code>, the response will be BYPASS.</p>
<p>If you expected a URL to be cached but see <code>BYPASS</code>, refer to <a href="/cache/troubleshooting/investigating-uncached-responses/#bypass--origin-response-is-not-cacheable">Investigate uncached responses</a> for a step-by-step diagnostic.</p>
<h2 id="revalidated">REVALIDATED</h2>
<p>The origin confirmed the cached resource was unchanged via a conditional request (<code>If-Modified-Since</code> or <code>If-None-Match</code>), and the response is served from Cloudflare's cache. This status reflects the synchronous validation path — the request waits for the origin to respond before being served.</p>
<p>With <a href="/cache/concepts/revalidation/#asynchronous-revalidation">asynchronous <code>stale-while-revalidate</code></a>, most revalidations now return <code>UPDATING</code> or <code>HIT</code> instead. <code>REVALIDATED</code> is seen in the following situations: <code>stale-while-revalidate</code> is not set; or directives like <code>must-revalidate</code> or <code>no-cache</code> (with <a href="/cache/concepts/cache-control/">Origin Cache Control</a> enabled) prevent stale content from being served.</p>
<h2 id="updating">UPDATING</h2>
<p>The resource was expired but served from Cloudflare's cache while the origin updates it in the background. <code>UPDATING</code> is the expected status during <a href="/cache/concepts/revalidation/#asynchronous-revalidation">asynchronous <code>stale-while-revalidate</code></a> revalidation — all requests during the revalidation window receive <code>UPDATING</code> or <code>HIT</code> rather than waiting for the origin.</p>
<h2 id="dynamic">DYNAMIC</h2>
<p>Cloudflare determined at request time that the asset is not eligible for cache, so the request went to the origin web server without a cache lookup.</p>
<p>This typically happens when:</p>
<ul>
<li>The requested asset is not one of the <a href="/cache/concepts/default-cache-behavior/#default-cached-file-extensions">default cached file extensions</a> (for example, HTML or JSON) and no rule instructs Cloudflare to cache it.</li>
<li>A <a href="/cache/how-to/cache-rules/">Cache Rule</a> with the <strong>Bypass cache</strong> setting matches the request. The legacy <code>Cache Level: Bypass</code> option in <a href="/rules/configuration-rules/">Configuration Rules</a> or <a href="/rules/page-rules/">Page Rules</a> behaves the same way.</li>
<li><a href="/cache/reference/development-mode/">Development Mode</a> is enabled on the zone, which suspends cache for three hours.</li>
</ul>
<p>Use <a href="/cache/how-to/cache-rules/">Cache Rules</a> to change what content Cloudflare caches. Once the request is treated as eligible for cache, the <code>CF-Cache-Status</code> header will reflect the response-time cache decision (<code>HIT</code>, <code>MISS</code>, <code>EXPIRED</code>, <code>REVALIDATED</code>, <code>BYPASS</code>, and so on) — refer to <a href="#bypass">BYPASS</a> for the case where the origin response is ultimately not cacheable.</p>
<p>If you expected the request to be eligible for cache but see <code>DYNAMIC</code>, refer to <a href="/cache/troubleshooting/investigating-uncached-responses/#dynamic--request-not-eligible-for-cache">Investigate uncached responses</a>.</p>
