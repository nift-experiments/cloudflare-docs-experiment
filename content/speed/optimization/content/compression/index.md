<p>Cloudflare compresses content in two ways: between Cloudflare and your website visitors and between Cloudflare and your origin server.</p>
<h2 id="compression-between-cloudflare-and-website-visitors">Compression between Cloudflare and website visitors</h2>
<p>In addition to Cloudflare's <a href="/cache/concepts/default-cache-behavior/">default caching behavior</a>, Cloudflare supports Gzip, Brotli, and Zstandard compression when delivering content to website visitors.</p>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/9103750883217fcb9274666fd57ebac1/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2F386f9df0-25fc-4d2a-07fa-6dd3497d2e00%2Fpublic" title="Content compression" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13943.md")
</aside>
<p>If supported by visitors' web browsers, Cloudflare will return Gzip, Brotli, or Zstandard-encoded responses for the following content types:</p>
<pre><code>text/html&#10;text/richtext&#10;text/plain&#10;text/css&#10;text/x-script&#10;text/x-component&#10;text/x-java-source&#10;text/x-markdown&#10;application/javascript&#10;application/x-javascript&#10;text/javascript&#10;text/js&#10;image/x-icon&#10;image/vnd.microsoft.icon&#10;application/x-perl&#10;application/x-httpd-cgi&#10;text/xml&#10;application/xml&#10;application/rss+xml&#10;application/vnd.api+json&#10;application/x-protobuf&#10;application/json&#10;multipart/bag&#10;multipart/mixed&#10;application/xhtml+xml&#10;font/ttf&#10;font/otf&#10;font/x-woff&#10;image/svg+xml&#10;application/vnd.ms-fontobject&#10;application/ttf&#10;application/x-ttf&#10;application/otf&#10;application/x-otf&#10;application/truetype&#10;application/opentype&#10;application/x-opentype&#10;application/font-woff&#10;application/eot&#10;application/font&#10;application/font-sfnt&#10;application/wasm&#10;application/javascript-binast&#10;application/manifest+json&#10;application/ld+json&#10;application/graphql+json&#10;application/geo+json&#10;</code></pre>
<p>Cloudflare's global network can deliver content to website visitors using Gzip compression, Brotli compression, Zstandard compression, or no compression, depending on:</p>
<ul>
<li>The values visitors provide in the <code>accept-encoding</code> request header.</li>
<li>Your <a href="#between-visitors-and-cloudflare">Cloudflare plan</a>.</li>
<li>Any configured <a href="/rules/compression-rules/">compression rule</a> that matches incoming requests.</li>
</ul>
<p>For responses with error status codes, Cloudflare will only compress responses if their error status code is <code>403</code> or <code>404</code>. For successful response status codes, Cloudflare will only compress responses if their status code is <code>200</code>. Responses with other status codes will not be compressed.</p>
<p>You can override Cloudflare's default compression behavior using <a href="/rules/compression-rules/">Compression Rules</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="minimum-response-size-for-compression">Minimum response size for compression</h3>
@markup("md", "content/.markup/bodies/13942.md")
</aside>
<h3 id="content-length-header-handling">Content-Length header handling</h3>
<p>When Cloudflare compresses a response sent to the website visitor, it may omit the <code>Content-Length</code> HTTP header to avoid delivering incorrect length information caused by dynamic transformations. To preserve the <code>Content-Length</code> header set by the origin server, add <code>cache-control: no-transform</code> to the origin server's response. This directive prevents Cloudflare from altering compression on responses, allowing the <code>Content-Length</code> header to pass through as-is. The <code>cache-control: no-transform</code> header must be set by the origin — it cannot be added in client requests.</p>
<hr />
<h2 id="content-compression-from-origin-servers-to-the-cloudflare-network">Content compression from origin servers to the Cloudflare network</h2>
<p>When requesting content from your origin server, Cloudflare supports Brotli compression, Gzip compression, or no compression.</p>
<pre><code class="language-mermaid">flowchart LR&#10;accTitle: Compressed responses sent from the origin server&#10;accDescr: Cloudflare accepts responses from origin server using Brotli compression, Gzip compression, or no compression.&#10;&#10;A[Visitor browser]&#10;B((Cloudflare))&#10;C[(Origin server)]&#10;&#10;A -.-&gt; B == &quot;Request&lt;br&gt;Accept-Encoding: br, gzip&quot; ==&gt; C&#10;C == &quot;Response&lt;br&gt;(Brotli / Gzip / No compression)&quot; ==&gt; B -.-&gt; A&#10;&#10;style A stroke-dasharray: 5 5&#10;style B stroke: orange,fill: orange,color: black&#10;style C stroke-width: 2px&#10;linkStyle 1,2 stroke-width: 2px&#10;linkStyle 0,3 stroke-width: 1px&#10;</code></pre>
<p>If your origin server responds to a Cloudflare request using Brotli/Gzip compression, we will keep the same compression in the response sent to the website visitor if:</p>
<ul>
<li>You include a <code>content-encoding</code> header in your server response mentioning the compression being used (<code>br</code> or <code>gzip</code>).</li>
<li>The visitor browser (or client) supports the compression algorithm.</li>
<li>You do not enable Cloudflare features that change the response content (refer to <a href="#notes-about-end-to-end-compression">Notes about end-to-end compression</a> for details).</li>
</ul>
<p>Cloudflare's reverse proxy can also convert between compressed formats and uncompressed formats. Cloudflare can receive content from your origin server with Brotli or Gzip compression and serve it to visitors uncompressed (or vice versa), independently of caching.</p>
<p>If you do not want a particular response from your origin to be encoded with Brotli/Gzip when delivered to website visitors, you can disable this by including a <code>cache-control: no-transform</code> HTTP header in the response from your origin web server.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13941.md")
</aside>
<hr />
<h2 id="notes-about-end-to-end-compression">Notes about end-to-end compression</h2>
<h3 id="content-recompression-due-to-dynamic-transformations">Content recompression due to dynamic transformations</h3>
<p>Even when using the same compression algorithm end to end (between your origin server and Cloudflare, and between the Cloudflare global network and your website visitor), Cloudflare will need to decompress the response and compress it again if you enable any of the following settings for the request:</p>
<ul>
<li><a href="/ssl/edge-certificates/additional-options/automatic-https-rewrites/">Automatic HTTPS Rewrites</a></li>
<li><a href="/speed/optimization/content/fonts/">Cloudflare Fonts</a></li>
<li><a href="/waf/tools/scrape-shield/email-address-obfuscation/">Email Address Obfuscation</a></li>
<li><a href="/images/polish/">Polish</a></li>
<li><a href="/speed/optimization/content/rocket-loader/">Rocket Loader</a></li>
<li><a href="/bots/additional-configurations/javascript-detections/">JavaScript detections</a></li>
<li><a href="/speed/observatory/run-speed-test/#enable-real-user-monitoring-rum">RUM</a></li>
</ul>
<p>To disable these settings for specific URI paths, create a <a href="/rules/configuration-rules/">configuration rule</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13940.md")
</aside>
<h3 id="content-length-header">Content-Length header</h3>
<p>Cloudflare may remove the <code>Content-Length</code> HTTP header of responses delivered to website visitors. To ensure that the header is preserved, add a <code>cache-control: no-transform</code> HTTP header to the response at the origin server.</p>
<h2 id="compression-methods-by-plan">Compression methods by plan</h2>
<h3 id="between-visitors-and-cloudflare">Between visitors and Cloudflare</h3>
<p>By default, Cloudflare uses the following compression methods for content delivery, depending on the zone plan. However, the actual compression applied may also depend on what the visitor's browser requests via the <code>accept-encoding</code> header.</p>
<ul>
<li>Free Plan: Content is compressed by default using Zstandard.</li>
<li>Pro and Business Plans: Content is compressed by default using Brotli.</li>
<li>Enterprise Plan: Content is compressed by default using Gzip.</li>
</ul>
<h3 id="between-cloudflare-and-the-origin-server">Between Cloudflare and the origin server</h3>
<p>On all plans, Cloudflare requests content from the origin server using the <code>accept-encoding: br, gzip</code> header. This means that Cloudflare asks the origin to send the content compressed using Brotli or Gzip, depending on which method the origin server supports.</p>
