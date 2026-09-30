<p>The <a href="https://www.rfc-editor.org/rfc/rfc9110.html#name-vary"><code>Vary</code></a> HTTP response header tells Cloudflare that an origin can serve different responses for the same URL depending on request headers. For example, an origin might serve different languages based on <code>Accept-Language</code>, or different content formats based on <code>Accept</code>.</p>
<p>By default, Cloudflare's CDN constructs <a href="/cache/how-to/cache-keys/">cache keys</a> from a request's URL and a handful of specific headers. <a href="/cache/how-to/cache-rules/">Cache Rules</a> can add other request properties to the cache key ahead of time. The <code>Vary</code> response header lets the origin decide which request headers matter when Cloudflare receives the response.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3814.md")
</aside>
<p>This page explains how Vary affects caching. To configure Vary, use <a href="/cache/how-to/cache-rules/settings/#vary">Vary</a> in Cache Rules settings, or <a href="/workers/runtime-apis/request/#the-cfvary-property"><code>cf.vary</code></a> for Workers subrequests.</p>
<p>This feature is distinct from <a href="/cache/advanced-configuration/vary-for-images/">Vary for images</a>, which serves image format variants based on the <code>Accept</code> header through a separate cache variants rule.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="how-vary-affects-cache-keys">How Vary affects cache keys</h2>
<p>When Cloudflare caches a response with a <code>Vary</code> header, the listed request headers become part of the cache key for that response, following the HTTP caching behavior described in <a href="https://www.rfc-editor.org/rfc/rfc9111.html#name-calculating-cache-keys-with">RFC 9111</a>. The same URL can then have multiple cached versions, each selected by the request header values named in the origin's <code>Vary</code> response.</p>
<p>Cloudflare does not vary every cached response just because Vary is configured in a Cache Rule. The origin response must include a <code>Vary</code> header. Cloudflare then uses the configured action for each listed header to decide which request header value is added to the cache key.</p>
<p>For example, assume the origin returns this response:</p>
<pre><code class="language-txt">Vary: Accept-Language&#10;Cache-Control: public, max-age=3600&#10;</code></pre>
<p>This tells Cloudflare that the value of the <code>Accept-Language</code> request header should be part of the cache key.</p>
<p>With <code>accept-language</code> configured to <code>normalize</code>, these two requests can use the same cached version:</p>
<pre><code class="language-txt">Accept-Language: en-US, fr;q=0.8&#10;Accept-Language: fr;q=0.8, en-GB&#10;</code></pre>
<p>Both request headers normalize to the same language preference order, <code>en,fr</code>. A request with a different normalized value, such as <code>Accept-Language: fr, en;q=0.8</code>, creates or selects a different cached version of the same URL.</p>
<p>When a response varies on multiple headers, Cloudflare includes each listed header in the cache key. For example, a response with <code>Vary: Accept, Accept-Language</code> uses both the configured <code>accept</code> value and the configured <code>accept-language</code> value to select the cached response.</p>
<p>If the origin response does not include a <code>Vary</code> header, Cloudflare caches the response normally. If the origin response includes a <code>Vary</code> header name configured to <code>bypass</code> cache, Cloudflare does not store that response.</p>
<h2 id="actions">Actions</h2>
<p>Each configured header uses one of three actions:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Meaning</th>
<th>When to use</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>normalize</code></td>
<td>Normalize the request header value before selecting the cached version. For selected headers, Cloudflare may also forward the normalized value to the origin.</td>
<td>Most <code>Accept</code>, <code>Accept-Language</code>, and <code>Accept-Encoding</code> use cases.</td>
</tr>
<tr>
<td><code>passthrough</code></td>
<td>Use the raw request header value to select the cached version. The header is forwarded to the origin unchanged.</td>
<td>When byte-for-byte differences in the header value should create different versions.</td>
</tr>
<tr>
<td><code>bypass</code></td>
<td>Bypass cache when this header name appears in the origin's <code>Vary</code> response.</td>
<td>Headers with too many possible values, per-user values, or values you do not want cached.</td>
</tr>
</tbody>
</table>
<h3 id="normalize">Normalize</h3>
<p><code>normalize</code> reduces unnecessary cached versions by converting equivalent request header values into the same cache key value.</p>
<p>For example, these two <code>Accept</code> headers can normalize to the same value:</p>
<pre><code class="language-txt">Accept: text/html, application/json;q=0.9&#10;Accept: application/json;q=0.9, text/html&#10;</code></pre>
<h3 id="passthrough">Passthrough</h3>
<p><code>passthrough</code> uses the raw request header value when selecting a cached version. Semantically equivalent values can still create different cached versions if the bytes differ.</p>
<p>For example, under <code>passthrough</code>, these two requests select different cached versions:</p>
<pre><code class="language-txt">Accept: text/html, application/json&#10;Accept: application/json, text/html&#10;</code></pre>
<p>Use <code>passthrough</code> only when the exact header value matters to your origin and should matter to the cache.</p>
<h3 id="bypass">Bypass</h3>
<p><code>bypass</code> tells Cloudflare not to cache a response when the origin's <code>Vary</code> response includes that header name.</p>
<p>For example, if your configuration sets <code>user-agent</code> to <code>bypass</code>, a response with this header is not cached:</p>
<pre><code class="language-txt">Vary: User-Agent&#10;</code></pre>
<h2 id="normalization-behavior">Normalization behavior</h2>
<p>Vary normalization is the normalization performed when the configured action is <code>normalize</code>. It affects how Cloudflare selects a cached version and, for some headers, what Cloudflare forwards to the origin.</p>
<p>Normalization is optional but recommended for most deployments because it reduces the number of cached versions and improves cache hit ratio.</p>
<p>When a header's action is <code>normalize</code>, Cloudflare uses the normalized value to select the cached version. Normalization can be lossy: it may reorder values, drop quality values, lowercase values, or remove entries that are not in a configured allowlist.</p>
<h3 id="origin-request-headers">Origin request headers</h3>
<p>For <code>Accept</code>, <code>Accept-Language</code>, and <code>Accept-Encoding</code> with <a href="/cache/how-to/cache-rules/settings/#respect-strong-etags">Respect Strong ETags</a> enabled, Cloudflare may also forward the normalized header value to the origin. This keeps the response generated by the origin consistent with the cache key value Cloudflare uses for caching.</p>
<p>For example, if <code>accept-language</code> normalizes these two requests to <code>en,fr</code>, Cloudflare forwards <code>Accept-Language: en,fr</code> to the origin on a cache miss or revalidation:</p>
<pre><code class="language-txt">Accept-Language: en-US, fr;q=0.8&#10;Accept-Language: fr;q=0.8, en-GB&#10;</code></pre>
<p>Forwarding the normalized value prevents Cloudflare from storing a response generated for one raw header value under a broader normalized value that another request could later reuse incorrectly.</p>
<p>This origin request rewrite applies to:</p>
<ul>
<li><code>Accept</code></li>
<li><code>Accept-Language</code></li>
<li><code>Accept-Encoding</code>, only when Respect Strong ETags is enabled</li>
</ul>
<p>This rewrite does not apply to:</p>
<ul>
<li>Headers configured as <code>passthrough</code></li>
<li>Headers configured as <code>bypass</code></li>
<li>Other generic headers</li>
</ul>
<p>This rewrite happens before Cloudflare receives the origin response, so it is based on your Cache Rule configuration. If <code>Accept</code>, <code>Accept-Language</code>, or <code>Accept-Encoding</code> is configured with <code>normalize</code>, Cloudflare rewrites that request header when forwarding to the origin even if the origin's eventual response does not list that header in <code>Vary</code>. Cache selection and bypass still depend on the origin response's <code>Vary</code> header.</p>
<p>If normalization reduces a header to an empty value — for example, because none of the request's values match a configured <code>media_types</code> or <code>languages</code> list — Cloudflare removes that header from the origin request.</p>
<h3 id="accept">Accept</h3>
<p>Cloudflare normalizes the <code>Accept</code> request header in the following steps:</p>
<ol>
<li>Convert MIME types to lowercase.</li>
<li>Strip optional whitespace.</li>
<li>Sort MIME types by quality value. Types with the same quality value are sorted alphabetically.</li>
<li>Strip parameters.</li>
</ol>
<p>Quality values are used for sorting and then removed from the normalized value. <code>q=0</code> is preserved because it means &quot;not acceptable&quot; and should remain distinguishable from a low-priority value.</p>
<p>You can provide an optional <code>media_types</code> list. If provided, any MIME type not in the list is removed from the normalized value.</p>
<h3 id="accept-language">Accept-Language</h3>
<p>Cloudflare normalizes the <code>Accept-Language</code> request header in the following steps:</p>
<ol>
<li>Convert languages to lowercase.</li>
<li>Strip optional whitespace.</li>
<li>Sort languages by quality value. Languages with the same quality value are sorted alphabetically.</li>
<li>Strip parameters.</li>
<li>Strip region variants. For example, <code>en-US</code> becomes <code>en</code>. If multiple region variants of the same language are present, they are combined into a single item.</li>
</ol>
<p>Quality values are used for sorting and then removed from the normalized value. <code>q=0</code> is preserved because it means &quot;not acceptable&quot; and should remain distinguishable from a low-priority value.</p>
<p>You can provide an optional <code>languages</code> list. If provided, any language not in the list is removed from the normalized value. If an item in the list specifies a region variant, and there is a matching item in the request header, the region variant is retained in the normalized value.</p>
<h3 id="accept-encoding">Accept-Encoding</h3>
<p>By default, Cloudflare's CDN overrides the <code>Accept-Encoding</code> header based on the enabled compression encodings. If Brotli compression is enabled, the <code>Accept-Encoding</code> forwarded to the origin is <code>gzip, br</code>. If Brotli compression is not enabled, the <code>Accept-Encoding</code> forwarded to the origin is <code>gzip</code>. Cloudflare can then recompress cached assets based on the visitor's <code>Accept-Encoding</code>. For details, refer to <a href="/cache/reference/etag-headers/">ETag headers</a>.</p>
<p>This behavior can be turned off by enabling <a href="/cache/how-to/cache-rules/settings/#respect-strong-etags">Respect Strong ETags</a>. With Respect Strong ETags enabled, the visitor's <code>Accept-Encoding</code> is forwarded to the origin instead of Cloudflare's compression override. If Vary normalization is enabled for <code>Accept-Encoding</code>, the normalized value is used both to select the cached version and as the value forwarded to the origin.</p>
<p>Because Cloudflare controls <code>Accept-Encoding</code> when Respect Strong ETags is turned off, <code>Accept-Encoding</code> normalization only rewrites the origin request when Respect Strong ETags is turned on.</p>
<p>Cloudflare normalizes the <code>Accept-Encoding</code> request header in the following steps:</p>
<ol>
<li>Convert encodings to lowercase.</li>
<li>Strip optional whitespace.</li>
<li>Sort encodings by quality value. Encodings with the same quality value are sorted alphabetically.</li>
<li>Strip parameters.</li>
</ol>
<p>Quality values are used for sorting and then removed from the normalized value. <code>q=0</code> is preserved because it means &quot;not acceptable&quot; and should remain distinguishable from a low-priority value.</p>
<h3 id="other-headers">Other headers</h3>
<p>For any header other than <code>Accept</code>, <code>Accept-Language</code>, and <code>Accept-Encoding</code>, Cloudflare does not know the field's semantics. Normalization is restricted to transformations that are safe for any header:</p>
<ul>
<li>Multiple header field lines for the same header are combined into a single comma-separated value in the order received.</li>
<li>Optional whitespace around each value is trimmed.</li>
</ul>
<p>Values are not reordered, lowercased, deduplicated, or otherwise altered, because the order and contents of an arbitrary header may be significant.</p>
<p>For example, these two header field lines:</p>
<pre><code class="language-txt">X-Custom-Header: Value2&#10;X-Custom-Header: Value1&#10;</code></pre>
<p>When selecting a cached version, Cloudflare combines these values as <code>Value2,Value1</code>. The header forwarded to the origin is not rewritten.</p>
<h2 id="purge-behavior">Purge behavior</h2>
<p>Purging a URL purges all cached versions for that URL. You do not need to send a separate <a href="/cache/how-to/purge-cache/">purge</a> request for each <code>Vary</code> header value. This applies to purge methods that target the cached object, such as purge by URL, tag, hostname, prefix, or purge everything.</p>
<p>Changing Vary configuration does not itself purge cached content. Because a new Vary configuration can change how cached versions are selected, requests may miss and refill under the new cache keys until the old cached entries expire or are purged.</p>
