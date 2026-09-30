<h2 id="default-headers">Default headers</h2>
<p>When serving static assets, Workers will attach some headers to the response by default. These are:</p>
<ul>
<li>
<p><strong><code>Content-Type</code></strong></p>
<p>A <code>Content-Type</code> header is attached to the response if one is provided during <a href="/workers/static-assets/direct-upload/">the asset upload process</a>. <a href="/workers/wrangler/commands/general/#deploy">Wrangler</a> automatically determines the MIME type of the file, based on its extension.</p>
</li>
<li>
<p><strong><code>Cache-Control: public, max-age=0, must-revalidate</code></strong></p>
<p>Sent when the request does not have an <code>Authorization</code> or <code>Range</code> header, this response header tells the browser that the asset can be cached, but that the browser should revalidate the freshness of the content every time before using it. This default behavior ensures good website performance for static pages, while still guaranteeing that stale content will never be served.</p>
</li>
<li>
<p><strong><code>ETag</code></strong></p>
<p>This header complements the default <code>Cache-Control</code> header. Its value is a hash of the static asset file, and browsers can use this in subsequent requests with an <code>If-None-Match</code> header to check for freshness, without needing to re-download the entire file in the case of a match.</p>
</li>
<li>
<p><strong><code>CF-Cache-Status</code></strong></p>
<p>This header indicates whether the asset was served from the cache (<code>HIT</code>) or not (<code>MISS</code>).<sup><a href="#footnote-1">1</a></sup></p>
</li>
</ul>
<p>Cloudflare reserves the right to attach new headers to static asset responses at any time in order to improve performance or harden the security of your Worker application.</p>
<h2 id="custom-headers">Custom headers</h2>
<p>The default response headers served on static asset responses can be overridden, removed, or added to, by creating a plain text file called <code>_headers</code> without a file extension, in the static asset directory of your project. This file will not itself be served as a static asset, but will instead be parsed by Workers and its rules will be applied to static asset responses.</p>
<p>If you are using a framework, you will often have a directory named <code>public/</code> or <code>static/</code>, and this usually contains deploy-ready assets, such as favicons, <code>robots.txt</code> files, and site manifests. These files get copied over to a final output directory during the build, so this is the perfect place to author your <code>_headers</code> file. If you are not using a framework, the <code>_headers</code> file can go directly into your <a href="/workers/static-assets/binding/#directory">static assets directory</a>.</p>
<p>Headers defined in the <code>_headers</code> file override what Cloudflare ordinarily sends.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16096.md")
</aside>
<h3 id="attach-a-header">Attach a header</h3>
<p>Header rules are defined in multi-line blocks. The first line of a block is the URL or URL pattern where the rule's headers should be applied. On the next line, an indented list of header names and header values must be written:</p>
<pre><code class="language-txt">[url]&#10;  [name]: [value]&#10;</code></pre>
<p>Using absolute URLs is supported, though be aware that absolute URLs must begin with <code>https</code> and specifying a port is not supported. <code>_headers</code> rules ignore the incoming request's port and protocol when matching against an incoming request. For example, a rule like <code>https://example.com/path</code> would match against requests to <code>other://example.com:1234/path</code>.</p>
<p>You can define as many <code>[name]: [value]</code> pairs as you require on subsequent lines. For example:</p>
<pre><code class="language-txt">`# This is a comment\n/secure/page\n\tX-Frame-Options: DENY\n\tX-Content-Type-Options: nosniff\n\tReferrer-Policy: no-referrer\n\n/static/*\n\tAccess-Control-Allow-Origin: *\n\tX-Robots-Tag: nosnippet\n\nhttps://myworker.mysubdomain.workers.dev/*\n\tX-Robots-Tag: noindex`</code></pre>
<p>An incoming request which matches multiple rules' URL patterns will inherit all rules' headers. Using the previous <code>_headers</code> file, the following requests will have the following headers applied:</p>
<table>
<thead>
<tr>
<th>Request URL</th>
<th>Headers</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>https://custom.domain/secure/page</code></td>
<td><code>X-Frame-Options: DENY</code> <br /> <code>X-Content-Type-Options: nosniff </code> <br /> <code>Referrer-Policy: no-referrer</code></td>
</tr>
<tr>
<td><code>https://custom.domain/static/image.jpg</code></td>
<td><code>Access-Control-Allow-Origin: *</code> <br /> <code>X-Robots-Tag: nosnippet</code></td>
</tr>
<tr>
<td><code><a href="https://myworker.mysubdomain.workers.dev/home">https://myworker.mysubdomain.workers.dev/home</a></code></td>
<td><code>X-Robots-Tag: noindex</code></td>
</tr>
<tr>
<td><code><a href="https://myworker.mysubdomain.workers.dev/secure/page">https://myworker.mysubdomain.workers.dev/secure/page</a></code></td>
<td><code>X-Frame-Options: DENY</code> <br /> <code>X-Content-Type-Options: nosniff</code> <br /> <code>Referrer-Policy: no-referrer</code> <br /> <code>X-Robots-Tag: noindex</code></td>
</tr>
<tr>
<td><code><a href="https://myworker.mysubdomain.workers.dev/static/styles.css">https://myworker.mysubdomain.workers.dev/static/styles.css</a></code></td>
<td><code>Access-Control-Allow-Origin: *</code> <br /> <code>X-Robots-Tag: nosnippet, noindex</code></td>
</tr>
</tbody>
</table>
<p>You may define up to 100 header rules. Each line in the <code>_headers</code> file has a 2,000 character limit. The entire line, including spacing, header name, and value, counts towards this limit.</p>
<p>If a header is applied twice in the <code>_headers</code> file, the values are joined with a comma separator.</p>
<h3 id="detach-a-header">Detach a header</h3>
<p>You may wish to remove a default header or a header which has been added by a more pervasive rule. This can be done by prepending the header name with an exclamation mark and space (<code>! </code>).</p>
<pre><code class="language-txt">/*&#10;  Content-Security-Policy: default-src &#x27;self&#x27;;&#10;&#10;/*.jpg&#10;  ! Content-Security-Policy&#10;</code></pre>
<h3 id="match-a-path">Match a path</h3>
<p>The same URL matching features that <a href="/workers/static-assets/redirects/"><code>_redirects</code></a> offers is also available to the <code>_headers</code> file. Note, however, that redirects are applied before headers, so when a request matches both a redirect and a header, the redirect takes priority.</p>
<h4 id="splats">Splats</h4>
<p>When matching, a splat pattern — signified by an asterisk (<code>*</code>) — will greedily match all characters. You may only include a single splat in the URL.</p>
<p>The matched value can be referenced within the header value as the <code>:splat</code> placeholder.</p>
<h4 id="placeholders">Placeholders</h4>
<p>A placeholder can be defined with <code>:placeholder_name</code>. A colon (<code>:</code>) followed by a letter indicates the start of a placeholder and the placeholder name that follows must be composed of alphanumeric characters and underscores (<code>:[A-Za-z]\w*</code>). Every named placeholder can only be referenced once. Placeholders match all characters apart from the delimiter, which when part of the host, is a period (<code>.</code>) or a forward-slash (<code>/</code>) and may only be a forward-slash (<code>/</code>) when part of the path.</p>
<p>Similarly, the matched value can be used in the header values with <code>:placeholder_name</code>.</p>
<pre><code class="language-txt">/movies/:title&#10;  x-movie-name: You are watching &quot;:title&quot;&#10;</code></pre>
<h4 id="examples">Examples</h4>
<h5 id="cross-origin-resource-sharing-cors">Cross-Origin Resource Sharing (CORS)</h5>
<p>To enable other domains to fetch every static asset from your Worker, the following can be added to the <code>_headers</code> file:</p>
<pre><code class="language-txt">/*&#10;  Access-Control-Allow-Origin: *&#10;</code></pre>
<p>This applies the <code>Access-Control-Allow-Origin</code> header to any incoming URL. Note that the CORS specification only allows <code>*</code>, <code>null</code>, or an exact origin as valid <code>Access-Control-Allow-Origin</code> values — wildcard patterns within origins are not supported. To allow CORS from specific <a href="/workers/versions-and-deployments/preview-urls/">preview URLs</a>, you will need to handle this dynamically in your Worker code rather than through the <code>_headers</code> file.</p>
<h5 id="prevent-your-workers-dev-urls-showing-in-search-results">Prevent your workers.dev URLs showing in search results</h5>
<p><a href="https://developers.google.com/search/docs/advanced/robots/robots_meta_tag#directives">Google</a> and other search engines often support the <code>X-Robots-Tag</code> header to instruct its crawlers how your website should be indexed.</p>
<p>For example, to prevent your <code>*.*.workers.dev</code> URLs from being indexed, add the following to your <code>_headers</code> file:</p>
<pre><code class="language-txt">`https://:version.:subdomain.workers.dev/*\n\tX-Robots-Tag: noindex`</code></pre>
<h5 id="configure-custom-browser-cache-behavior">Configure custom browser cache behavior</h5>
<p>If you have a folder of fingerprinted assets (assets which have a hash in their filename), you can configure more aggressive caching behavior in the browser to improve performance for repeat visitors:</p>
<pre><code class="language-txt">/static/*&#10;  Cache-Control: public, max-age=31556952, immutable&#10;</code></pre>
<h5 id="harden-security-for-an-application">Harden security for an application</h5>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16095.md")
</aside>
<p>You can prevent click-jacking by informing browsers not to embed your application inside another (for example, with an <code>&lt;iframe&gt;</code>) with a <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options"><code>X-Frame-Options</code></a> header.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options"><code>X-Content-Type-Options: nosniff</code></a> prevents browsers from interpreting a response as any other content-type than what is defined with the <code>Content-Type</code> header.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy"><code>Referrer-Policy</code></a> allows you to customize how much information visitors give about where they are coming from when they navigate away from your page.</p>
<p>Browser features can be disabled to varying degrees with the <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy"><code>Permissions-Policy</code></a> header (recently renamed from <code>Feature-Policy</code>).</p>
<p>If you need fine-grained control over your application's content, the <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy"><code>Content-Security-Policy</code></a> header allows you to configure a number of security settings, including similar controls to the <code>X-Frame-Options</code> header.</p>
<pre><code class="language-txt">/app/*&#10;  X-Frame-Options: DENY&#10;  X-Content-Type-Options: nosniff&#10;  Referrer-Policy: no-referrer&#10;  Permissions-Policy: document-domain=()&#10;  Content-Security-Policy: script-src &#x27;self&#x27;; frame-ancestors &#x27;none&#x27;;&#10;</code></pre>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Due to a technical limitation that we hope to address in the future, the `CF-Cache-Status` header is not always entirely accurate. It is possible for false-positives and false-negatives to occur. This should be rare. In the meantime, this header should be considered as returning a "probabilistic" result.</li></ol></section>
