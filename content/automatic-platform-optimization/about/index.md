<p>With Automatic Platform Optimization (APO), Cloudflare serves your entire site from our edge network, ensuring customers see improved performance when visiting your site. Cloudflare typically only caches static content, but with APO, we can also cache dynamic content — like HTML — to serve the entire site from the cache. This process removes round trips from the origin to drastically improve time to first byte (TTFB) along with other site performance metrics. In addition to caching dynamic content, APO caches third-party scripts to further reduce the number of requests that leave Cloudflare's edge network.</p>
<p>With APO, you can manage your WordPress site as normal. Whenever you update content in WordPress, Cloudflare updates content on our edge to prevent serving stale content when you use Cloudflare's WordPress plugin. Additionally, for logged-in or administrator users, we bypass the cache to ensure that private content is not cached and served to other visitors. Find more about <a href="https://www.youtube.com/watch?v=DWANhxoDxFI?feature=youtu.be">what APO can do for you.</a></p>
<h2 id="how-apo-decides-what-to-cache">How APO decides what to cache</h2>
<p>APO only caches a response as HTML when the request and the origin response meet all of the following criteria. When any criterion is not met, the request bypasses the cache and is served from the origin (<code>cf-cache-status: DYNAMIC</code>), and the <code>cf-apo-via</code> response header indicates the reason.</p>
<ul>
<li><strong>Request method</strong> is <code>GET</code> or <code>HEAD</code>.</li>
<li><strong>HTML eligibility</strong> is met, based on the request's <code>Accept</code> header and URL path:
<ul>
<li><code>Accept: text/html</code> (with a quality value greater than zero) is treated as an HTML request.</li>
<li><code>Accept: text/html; q=0</code> explicitly refuses HTML and is not cached as HTML.</li>
<li>When the <code>Accept</code> header does not mention <code>text/html</code> — including <code>Accept: */*</code> or a missing <code>Accept</code> header — the URL path is used instead: non-static paths (such as a page or post) remain eligible, while static file extensions do not.</li>
</ul>
</li>
<li><strong>Origin response</strong> returns HTTP <code>200</code> with a <code>Content-Type</code> of <code>text/html</code>.</li>
<li><strong>The <code>cf-edge-cache</code> response header</strong> from the WordPress plugin permits caching (for example, <code>cache,platform=wordpress</code>, and not <code>no-cache</code>).</li>
<li><strong>No bypass cookies</strong> are present (for example, logged-in, session, or WooCommerce cookies).</li>
<li><strong>No cache-bypassing request headers</strong> (such as <code>Cache-Control: no-cache</code>) or risky headers (<code>x-host</code>, <code>x-forwarded-host</code>, <code>x-original-url</code>, <code>x-rewrite-url</code>) are present.</li>
<li><strong>The URL path</strong> is not an excluded path (such as checkout, <code>wp-cron.php</code>, or feeds).</li>
<li><strong>Query strings</strong> are either absent or limited to the supported marketing parameters. For more information, refer to <a href="/automatic-platform-optimization/reference/query-parameters/">Query parameters and cached responses</a>.</li>
<li><strong>No Page Rule</strong> with <code>Cache Level: Bypass</code> matches the request. For more information, refer to <a href="/automatic-platform-optimization/reference/page-rule-integration/">Page Rule integration with APO</a>.</li>
</ul>
<h2 id="limitations">Limitations</h2>
<p>Automatic Platform Optimization is not compatible with Enterprise <a href="/dns/zone-setups/subdomain-setup/">subdomain setup</a> when a subdomain, for example, <code>www</code> is in a different zone to the apex domain.</p>
