<h2 id="do-i-still-need-to-create-edge-cache-ttl-page-rules-with-cache-level-cache-everything">Do I still need to create &quot;Edge Cache TTL&quot; page rules with &quot;Cache Level: Cache Everything&quot;?</h2>
<p>No, you do not need create Edge Cache TTL page rules. When the WordPress plugin is installed, APO automatically caches content for 30 days and invalidates on change within 30 seconds. However, because APO now supports cache-related page rules, make sure existing page rules do not affect the resources served by APO.</p>
<h2 id="does-origin-cache-control-override-apo">Does Origin Cache Control override APO?</h2>
<p>No. APO ignores Origin Cache Control for caching on the Edge, but APO serves original Origin Cache Control to the client.</p>
<h2 id="why-are-my-browser-cache-control-headers-missing-with-apo">Why are my browser cache control headers missing with APO?</h2>
<p>The browser cache control headers may be missing with APO if you set your <strong>Browser Cache TTL</strong> to <strong>Respect Existing Headers</strong>. For example:</p>
<pre><code class="language-sh">curl --silent --verbose --output /dev/null https://example.com/ --header &#x27;Accept: text/html&#x27; 2&gt;&amp;1 | grep cache-control&#10;</code></pre>
<pre><code class="language-sh">&lt; cache-control: max-age=86400, stale-while-revalidate=86400, stale-if-error=86400&#10;</code></pre>
<h2 id="is-the-stale-if-error-directive-still-needed-with-apo">Is the stale-if-error directive still needed with APO?</h2>
<p>No, the <code>stale-if-error</code> directive is not needed because the feature is built into APO.</p>
<h2 id="when-i-check-the-posts-and-homepage-cache-status-the-response-header-shows-cf-cache-status-bypass-is-apo-working">When I check the posts and homepage cache status, the response header shows <code>cf-cache-status: BYPASS</code>. Is APO working?</h2>
<p>When Chrome DevTools is open, Chrome sends <code>Cache-Control: no-cache</code> by default. You can uncheck the <strong>Disable cache (while DevTools is open)</strong> setting and see that <code>cf-cache-status: HIT</code> and <code>cf-apo-via: cache</code> headers will be returned.</p>
<h2 id="when-i-check-cf-cache-status-via-curl-miss-and-dynamic-are-always-returned-in-my-browser-i-see-hit-but-other-tools-return-dynamic-is-this-expected-behavior">When I check <code>cf-cache-status</code> via cURL, <code>MISS</code> and <code>DYNAMIC</code> are always returned. In my browser, I see <code>HIT</code> but other tools return <code>DYNAMIC</code>. Is this expected behavior?</h2>
<p>APO decides whether a request is eligible for HTML caching based on the request's <code>Accept</code> header and its URL path:</p>
<ul>
<li>If the <code>Accept</code> header includes <code>text/html</code> (with a quality value greater than zero), the request is treated as an HTML request and is eligible for caching.</li>
<li>If the <code>Accept</code> header explicitly refuses HTML (<code>Accept: text/html; q=0</code>), the request is not cached as HTML.</li>
<li>If the <code>Accept</code> header does not mention <code>text/html</code> — including <code>Accept: */*</code> or a missing <code>Accept</code> header — APO evaluates the URL path instead. Requests for non-static paths (such as a page or post) remain eligible for HTML caching, while requests for static file extensions do not.</li>
</ul>
<p>Some testing tools send no <code>Accept</code> header. For these requests, APO uses the URL path as described above, so the cache result depends on the requested path and the other eligibility criteria. To reliably reproduce a browser-like HTML request, include <code>-H 'accept: text/html'</code> in your cURL command.</p>
<h2 id="are-google-fonts-optimized-when-apo-is-activated">Are Google Fonts optimized when APO is activated?</h2>
<p>Yes, Google Fonts are also optimized when APO is activated. You can confirm the optimization by checking the font URLs. For example, the URL will change from <code>https://fonts.gstatic.com/s/...</code> to <code>https://example.com/fonts.gstatic.com/s/...</code> when the site loads. For proxied fonts, the <code>cf-apo-via:proxy</code> header is returned.</p>
<h2 id="can-i-customize-query-string-caching-with-apo">Can I customize query string caching with APO?</h2>
<p>For more information on query parameters, see <a href="/automatic-platform-optimization/reference/query-parameters/">Query parameters and cached responses</a>.</p>
<h2 id="why-are-my-font-urls-not-being-transformed">Why are my font URLs not being transformed?</h2>
<p>APO will skip URL font transformation when the <code>content-security-policy</code> response header is present but missing the values described below.</p>
<p>To fix the problem, the <code>content-security-policy</code> header value must allow for <code>unsafe-inline</code> on either the <code>style-src</code> or <code>default-src</code> directive. For example, <code>Content-Security-Policy: style-src unsafe-inline;</code>.</p>
<p>The header must allow for <code>self</code> on either the <code>font-src</code> or <code>default-src</code> directive. For example, <code>Content-Security-Policy: font-src self;</code>.</p>
<h2 id="why-do-i-see-worker-subrequests-in-my-zone-logs-when-using-apo">Why do I see Worker subrequests in my zone logs when using APO?</h2>
<p>APO uses Cloudflare Workers internally to optimize content delivery, which results in Worker subrequests. These subrequests may appear in your zone logs (for example, via Logpush).</p>
<h2 id="for-the-apo-plugin-why-do-i-see-this-plugin-hasn-t-been-tested-with-the-latest-3-major-releases-of-wordpress-it-may-no-longer-be-maintained-or-supported-and-may-have-compatibility-issues-when-used-with-more-recent-versions-of-wordpress">For the APO plugin why do I see: This plugin hasn’t been tested with the latest 3 major releases of WordPress. It may no longer be maintained or supported and may have compatibility issues when used with more recent versions of WordPress.</h2>
<p>It is not uncommon for mature plugins to see no updates for longer periods than it takes to trigger the WordPress not tested warning. The warning is for notification purposes and is not an indication that a plugin no longer works. It is still maintained.</p>
