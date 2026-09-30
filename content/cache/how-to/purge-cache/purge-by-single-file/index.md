<p>With purge by single-file, cached resources are instantly removed from the stored assets in your Content Delivery Network (CDN) across all data centers. New requests for the purged asset receive the latest version from your origin web server and add it back to your CDN cache within the specific Cloudflare data center that served the request.</p>
<p>For information on single-file purge rate limits, refer to the <a href="/cache/how-to/purge-cache/#single-file-purge-limits">limits</a> section.</p>
<h2 id="how-to-purge-a-single-file">How to purge a single file</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Configuration</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Under <strong>Purge Cache</strong>, select <strong>Custom Purge</strong>. The <strong>Custom Purge</strong> window appears.</li>
<li>Under <strong>Purge by</strong>, select <strong>URL</strong>.</li>
<li>Enter the appropriate value(s) in the text field using the format shown in the example. Be aware that the host part of the URL is not case-sensitive, meaning it will always be converted to lowercase according to RFC standards. However, the path portion is case-sensitive. For example, <code>https://EXAMPLE.com/helloHI</code> would be treated as <code>https://example.com/helloHI</code>.</li>
<li>Perform any additional instructions to complete the form.</li>
<li>Review your entries.</li>
<li>Select <strong>Purge</strong>.</li>
</ol>
<h2 id="limitations-and-alternatives">Limitations and alternatives</h2>
<p>Single-file purge works for most resources, but there are situations where it cannot clear cached content. This section explains when single-file purge does not work and what to use instead.</p>
<h3 id="custom-cache-keys">Custom cache keys</h3>
<p>If you use <a href="/cache/how-to/cache-rules/">Cache Rules</a> to set a <a href="/cache/how-to/cache-keys/">custom cache key</a> that includes headers, cookies, or other request properties, single-file purge via the dashboard will not invalidate the cached resource. This is because the dashboard cannot send those values in a purge request. Custom cache keys that only change how the query string is handled (for example, ignoring the query string) generally work with dashboard single-file purge.</p>
<p><strong>What to do instead:</strong></p>
<ul>
<li><strong>Use the API</strong> to <a href="/api/resources/cache/methods/purge/#purge-cached-content-by-url">purge files by URL</a>, including all headers and cookies that are part of your custom cache key. If any header or cookie is missing from the purge request, Cloudflare treats it as an empty value in the cache key.</li>
<li><strong>Use purge by prefix</strong> (<a href="/cache/how-to/purge-cache/purge_by_prefix/">purge by prefix</a>) to clear all resources under a URL path.</li>
<li><strong>Use purge by tag</strong> (<a href="/cache/how-to/purge-cache/purge-by-tags/">purge by tag</a>) if your resources are tagged.</li>
<li><strong>Use purge everything</strong> (<a href="/cache/how-to/purge-cache/purge-everything/">purge everything</a>) to clear all cached resources for the zone.</li>
</ul>
<h3 id="cache-rules-that-match-on-request-properties">Cache Rules that match on request properties</h3>
<p>Single-file purge may also not work as expected if your Cache Rules match only on <code>GET</code> requests, or match on properties that are not present during a purge. For example, a Cache Rule with the expression <code>(http.host eq &quot;example.com&quot; and http.request.method eq &quot;GET&quot;)</code> will not match during a single-file purge.</p>
<p><strong>What to do instead:</strong></p>
<p>Update your Cache Rule expression to also match on the <code>PURGE</code> method, for example <code>(http.host eq &quot;example.com&quot; and (http.request.method eq &quot;GET&quot; or http.request.method eq &quot;PURGE&quot;))</code>. This allows the rule to apply to both client requests and purge requests.</p>
<p>For rules that match on fields which cannot be evaluated during purge (such as <code>cf.bot_management.score</code>), use <a href="/cache/how-to/purge-cache/purge_by_prefix/">purge by prefix</a>, <a href="/cache/how-to/purge-cache/purge-by-tags/">purge by tag</a>, or <a href="/cache/how-to/purge-cache/purge-everything/">purge everything</a>.</p>
<h3 id="redirect-responses">Redirect responses</h3>
<p>If the URL you want to purge returns a redirect (<code>301</code> or <code>302</code>), single-file purge removes the cached redirect response — not the content at the redirect destination. The resource at the destination URL remains cached.</p>
<p>To clear the destination content, purge the final destination URL directly. You can find it by following the redirect chain to its end:</p>
<pre><code class="language-bash">curl -Ls -o /dev/null -w &quot;%{url_effective}&#10;&quot; https://example.com/redirecting-path&#10;</code></pre>
<p>This outputs the final URL after following all redirects. Use that URL for your purge request.</p>
<h3 id="resources-with-special-headers">Resources with special headers</h3>
<p>A single-file purge performed through your Cloudflare dashboard does not clear objects that contain any of the following:</p>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Origin">Origin header</a></li>
<li>Any of these request headers:
<ul>
<li><code>X-Forwarded-Host</code></li>
<li><code>X-Host</code></li>
<li><code>X-Forwarded-Scheme</code></li>
<li><code>X-Original-URL</code></li>
<li><code>X-Rewrite-URL</code></li>
<li><code>Forwarded</code></li>
</ul>
</li>
</ul>
<p>You can purge objects with these characteristics using an API call to <a href="/api/resources/cache/methods/purge/">purge files by URL</a>. In the <code>headers</code> object of the request body, include the header values that match those used in the cached resource's cache key.</p>
<h2 id="additional-notes">Additional notes</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3871.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3870.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3869.md")
</aside>
<h2 id="resulting-cache-status">Resulting cache status</h2>
<p>Purging by single-file deletes the resource, resulting in the <code>CF-Cache-Status</code> header being set to <a href="/cache/concepts/cache-responses/#miss"><code>MISS</code></a> for subsequent requests.</p>
