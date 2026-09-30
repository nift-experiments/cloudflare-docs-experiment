<p>The <a href="https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API">Fetch API</a> provides an interface for asynchronously fetching resources via HTTP requests inside of a Worker.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16146.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="worker-to-worker">Worker to Worker</h3>
@markup("md", "content/.markup/bodies/16145.md")
</aside>
<h2 id="syntax">Syntax</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16150.md")
</div></div>
<ul>
<li><code>fetch(resource, options optional)</code> : Promise<code>&lt;Response&gt;</code></li>
<li>Fetch returns a promise to a Response.</li>
</ul>
<h3 id="parameters">Parameters</h3>
<ul>
<li>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/API/fetch#resource"><code>resource</code></a> Request | string | URL</p>
</li>
<li>
<p><code>options</code> options</p>
<ul>
<li><code>cache</code> <code>undefined | 'no-store' | 'no-cache'</code> optional
<ul>
<li>Standard HTTP <code>cache</code> header. Only <code>cache: 'no-store'</code> and <code>cache: 'no-cache'</code> are supported.
Any other <code>cache</code> header will result in a <code>TypeError</code> with the message <code>Unsupported cache mode: &lt;attempted-cache-mode&gt;</code>.
_ For all requests this forwards the <code>Pragma: no-cache</code> and <code>Cache-Control: no-cache</code> headers to the origin.
_ For <code>no-store</code>, requests to origins not hosted by Cloudflare bypass the use of Cloudflare's caches.
_ For <code>no-cache</code>, requests to origins not hosted by Cloudflare are forced to revalidate with
the origin before responding.</li>
</ul>
</li>
<li>An object that defines the content and behavior of the request.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="how-the-accept-encoding-header-is-handled">How the <code>Accept-Encoding</code> header is handled</h2>
<p>When making a subrequest with the <code>fetch()</code> API, you can specify which forms of compression to prefer that the server will respond with (if the server supports it) by including the <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept-Encoding"><code>Accept-Encoding</code></a> header.</p>
<p>Workers supports both the gzip and brotli compression algorithms. Usually it is not necessary to specify <code>Accept-Encoding</code> or <code>Content-Encoding</code> headers in the Workers Runtime production environment – brotli or gzip compression is automatically requested when fetching from an origin and applied to the response when returning data to the client, depending on the capabilities of the client and origin server.</p>
<p>To support requesting brotli from the origin, you must enable the <a href="/workers/configuration/compatibility-flags/#brotli-content-encoding-support"><code>brotli_content_encoding</code></a> compatibility flag in your Worker. Soon, this compatibility flag will be enabled by default for all Workers past an upcoming compatibility date.</p>
<h3 id="passthrough-behavior">Passthrough behavior</h3>
<p>One scenario where the Accept-Encoding header is useful is for passing through compressed data from a server to the client, where the Accept-Encoding allows the worker to directly receive the compressed data stream from the server without it being decompressed beforehand. As long as you do not read the body of the compressed response prior to returning it to the client and keep the <code>Content-Encoding</code> header intact, it will &quot;pass through&quot; without being decompressed and then recompressed again. This can be helpful when using Workers in front of origin servers or when fetching compressed media assets, to ensure that the same compression used by the origin server is used in the response that your Worker returns.</p>
<p>In addition to a change in the content encoding, recompression is also needed when a response uses an encoding not supported by the client. As an example, when a Worker requests either brotli or gzip as the encoding but the client only supports gzip, recompression will still be needed if the server returns brotli-encoded data to the server (and will be applied automatically). Note that this behavior may also vary based on the <a href="/rules/compression-rules/">compression rules</a>, which can be used to configure what compression should be applied for different types of data on the server side.</p>
<pre><code class="language-typescript">export default {&#10;	async fetch(request) {&#10;		// Accept brotli or gzip compression&#10;		const headers = new Headers({&#10;			&quot;Accept-Encoding&quot;: &quot;br, gzip&quot;,&#10;		});&#10;		let response = await fetch(&quot;https://developers.cloudflare.com&quot;, {&#10;			method: &quot;GET&quot;,&#10;			headers,&#10;		});&#10;&#10;		// As long as the original response body is returned and the Content-Encoding header is&#10;		// preserved, the same encoded data will be returned without needing to be compressed again.&#10;		return new Response(response.body, {&#10;			status: response.status,&#10;			statusText: response.statusText,&#10;			headers: response.headers,&#10;		});&#10;	},&#10;};&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/examples/respond-with-another-site/">Example: use <code>fetch</code> to respond with another site</a></li>
<li><a href="/workers/examples/fetch-html/">Example: Fetch HTML</a></li>
<li><a href="/workers/examples/fetch-json/">Example: Fetch JSON</a></li>
<li><a href="/workers/examples/cache-using-fetch/">Example: cache using Fetch</a></li>
<li>Write your Worker code in <a href="/workers/reference/migrate-to-module-workers/">ES modules syntax</a> for an optimized experience.</li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/#error-526-in-the-workers-context">Error 526</a></li>
<li><a href="/workers/platform/known-issues/#fetch-api-in-cname-setup">Fetch API in a partial setup</a></li>
</ul>
