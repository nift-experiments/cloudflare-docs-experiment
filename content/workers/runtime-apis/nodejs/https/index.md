<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17146.md")
</aside>
<h2 id="compatibility-flags">Compatibility flags</h2>
<h3 id="client-side-methods">Client-side methods</h3>
<p>To use the HTTPS client-side methods (<code>https.get</code>, <code>https.request</code>, etc.), you must enable the <a href="/workers/configuration/compatibility-flags/"><code>enable_nodejs_http_modules</code></a> compatibility flag in addition to the <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code></a> flag.</p>
<p>This flag is automatically enabled for Workers using a <a href="/workers/configuration/compatibility-dates/">compatibility date</a> of <code>2025-08-15</code> or later when <code>nodejs_compat</code> is enabled. For Workers using an earlier compatibility date, you can manually enable it by adding the flag to your <code>wrangler.toml</code>:</p>
<pre><code class="language-toml">compatibility_flags = [&quot;nodejs_compat&quot;, &quot;enable_nodejs_http_modules&quot;]&#10;</code></pre>
<h3 id="server-side-methods">Server-side methods</h3>
<p>To use the HTTPS server-side methods (<code>https.createServer</code>, <code>https.Server</code>, <code>https.ServerResponse</code>), you must enable the <code>enable_nodejs_http_server_modules</code> compatibility flag in addition to the <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code></a> flag.</p>
<p>This flag is automatically enabled for Workers using a <a href="/workers/configuration/compatibility-dates/">compatibility date</a> of <code>2025-09-01</code> or later when <code>nodejs_compat</code> is enabled. For Workers using an earlier compatibility date, you can manually enable it by adding the flag to your <code>wrangler.toml</code>:</p>
<pre><code class="language-toml">compatibility_flags = [&quot;nodejs_compat&quot;, &quot;enable_nodejs_http_server_modules&quot;]&#10;</code></pre>
<p>To use both client-side and server-side methods, enable both flags:</p>
<pre><code class="language-toml">compatibility_flags = [&quot;nodejs_compat&quot;, &quot;enable_nodejs_http_modules&quot;, &quot;enable_nodejs_http_server_modules&quot;]&#10;</code></pre>
<h2 id="get">get</h2>
<p>An implementation of the Node.js <a href="https://nodejs.org/docs/latest/api/https.html#httpsgetoptions-callback">`https.get'</a> method.</p>
<p>The <code>get</code> method performs a GET request to the specified URL and invokes the callback with the response. This is a convenience method that simplifies making HTTPS GET requests without manually configuring request options.</p>
<p>Because <code>get</code> is a wrapper around <code>fetch(...)</code>, it may be used only within an exported fetch or similar handler. Outside of such a handler, attempts to use <code>get</code> will throw an error.</p>
<pre><code class="language-js">import { get } from &quot;node:https&quot;;&#10;&#10;export default {&#10;	async fetch() {&#10;		const { promise, resolve, reject } = Promise.withResolvers();&#10;		get(&quot;https://example.com&quot;, (res) =&gt; {&#10;			let data = &quot;&quot;;&#10;			res.setEncoding(&quot;utf8&quot;);&#10;			res.on(&quot;data&quot;, (chunk) =&gt; {&#10;				data += chunk;&#10;			});&#10;			res.on(&quot;end&quot;, () =&gt; {&#10;				resolve(new Response(data));&#10;			});&#10;			res.on(&quot;error&quot;, reject);&#10;		}).on(&quot;error&quot;, reject);&#10;		return promise;&#10;	},&#10;};&#10;</code></pre>
<p>The implementation of <code>get</code> in Workers is a wrapper around the global
<a href="https://developers.cloudflare.com/workers/runtime-apis/fetch/"><code>fetch</code> API</a>
and is therefore subject to the same <a href="https://developers.cloudflare.com/workers/platform/limits/">limits</a>.</p>
<p>As shown in the example above, it is necessary to arrange for requests to be correctly
awaited in the <code>fetch</code> handler using a promise or the fetch may be canceled prematurely
when the handler returns.</p>
<h2 id="request">request</h2>
<p>An implementation of the Node.js <a href="https://nodejs.org/docs/latest/api/https.html#httpsrequestoptions-callback">`https.request'</a> method.</p>
<p>The <code>request</code> method creates an HTTPS request with customizable options like method, headers, and body. It provides full control over the request configuration and returns a Node.js <a href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/streams/">stream.Writable</a> for sending request data.</p>
<p>Because <code>get</code> is a wrapper around <code>fetch(...)</code>, it may be used only within an exported fetch or similar handler. Outside of such a handler, attempts to use <code>get</code> will throw an error.</p>
<p>The request method accepts all options from <a href="/workers/runtime-apis/nodejs/http#request"><code>http.request</code></a> with some differences in default values:</p>
<ul>
<li><code>protocol</code>: default <code>https:</code></li>
<li><code>port</code>: default <code>443</code></li>
<li><code>agent</code>: default <code>https.globalAgent</code></li>
</ul>
<pre><code class="language-js">import { request } from &quot;node:https&quot;;&#10;import { strictEqual, ok } from &quot;node:assert&quot;;&#10;&#10;export default {&#10;	async fetch() {&#10;		const { promise, resolve, reject } = Promise.withResolvers();&#10;		const req = request(&#10;			&quot;https://developers.cloudflare.com/robots.txt&quot;,&#10;			{&#10;				method: &quot;GET&quot;,&#10;			},&#10;			(res) =&gt; {&#10;				strictEqual(res.statusCode, 200);&#10;				let data = &quot;&quot;;&#10;				res.setEncoding(&quot;utf8&quot;);&#10;				res.on(&quot;data&quot;, (chunk) =&gt; {&#10;					data += chunk;&#10;				});&#10;				res.once(&quot;error&quot;, reject);&#10;				res.on(&quot;end&quot;, () =&gt; {&#10;					ok(data.includes(&quot;User-agent&quot;));&#10;					resolve(new Response(data));&#10;				});&#10;			},&#10;		);&#10;		req.end();&#10;		return promise;&#10;	},&#10;};&#10;</code></pre>
<p>The following additional options are not supported: <code>ca</code>, <code>cert</code>, <code>ciphers</code>, <code>clientCertEngine</code> (deprecated), <code>crl</code>, <code>dhparam</code>, <code>ecdhCurve</code>, <code>honorCipherOrder</code>, <code>key</code>, <code>passphrase</code>, <code>pfx</code>, <code>rejectUnauthorized</code>, <code>secureOptions</code>, <code>secureProtocol</code>, <code>servername</code>, <code>sessionIdContext</code>, <code>highWaterMark</code>.</p>
<h2 id="createserver">createServer</h2>
<p>An implementation of the Node.js <a href="https://nodejs.org/docs/latest/api/https.html#httpscreateserveroptions-requestlistener"><code>https.createServer</code></a> method.</p>
<p>The <code>createServer</code> method creates an HTTPS server instance that can handle incoming secure requests. It's a convenience function that creates a new <code>Server</code> instance and optionally sets up a request listener callback.</p>
<pre><code class="language-js">import { createServer } from &quot;node:https&quot;;&#10;import { httpServerHandler } from &quot;cloudflare:node&quot;;&#10;&#10;const server = createServer((req, res) =&gt; {&#10;	res.writeHead(200, { &quot;Content-Type&quot;: &quot;text/plain&quot; });&#10;	res.end(&quot;Hello from Node.js HTTPS server!&quot;);&#10;});&#10;&#10;server.listen(8080);&#10;export default httpServerHandler({ port: 8080 });&#10;</code></pre>
<p>The <code>httpServerHandler</code> function integrates Node.js HTTPS servers with the Cloudflare Workers request model. When a request arrives at your Worker, the handler automatically routes it to your Node.js server running on the specified port. This bridge allows you to use familiar Node.js server patterns while benefiting from the Workers runtime environment, including automatic scaling, edge deployment, and integration with other Cloudflare services.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17145.md")
</aside>
<h2 id="agent">Agent</h2>
<p>An implementation of the Node.js <a href="https://nodejs.org/docs/latest/api/https.html#class-httpsagent"><code>https.Agent</code></a> class.</p>
<p>An <a href="https://nodejs.org/docs/latest/api/https.html#class-httpsagent">Agent</a> manages HTTPS connection reuse by maintaining request queues per host/port. In the Workers environment, however, such low-level management of the network connection, ports, etc, is not relevant because it is handled by the Cloudflare infrastructure instead. Accordingly, the implementation of <code>Agent</code> in Workers is a stub implementation that does not support connection pooling or keep-alive.</p>
<h2 id="server">Server</h2>
<p>An implementation of the Node.js <a href="https://nodejs.org/docs/latest/api/https.html#class-httpsserver"><code>https.Server</code></a> class.</p>
<p>In Node.js, the <code>https.Server</code> class represents an HTTPS server and provides methods for handling incoming secure requests. In Workers, handling of secure requests is provided by the Cloudflare infrastructure so there really is not much difference between using <code>https.Server</code> or <code>http.Server</code>. The workers runtime provides an implementation for completeness but most workers should probably just use <a href="/workers/runtime-apis/nodejs/http#server"><code>http.Server</code></a>.</p>
<pre><code class="language-js">import { Server } from &quot;node:https&quot;;&#10;import { httpServerHandler } from &quot;cloudflare:node&quot;;&#10;&#10;const server = new Server((req, res) =&gt; {&#10;	res.writeHead(200, { &quot;Content-Type&quot;: &quot;application/json&quot; });&#10;	res.end(JSON.stringify({ message: &quot;Hello from HTTPS Server!&quot; }));&#10;});&#10;server.listen(8080);&#10;export default httpServerHandler({ port: 8080 });&#10;</code></pre>
<p>The following differences exist between the Workers implementation and Node.js:</p>
<ul>
<li>Connection management methods such as <code>closeAllConnections()</code> and <code>closeIdleConnections()</code> are not implemented due to the nature of the Workers environment.</li>
<li>Only <code>listen()</code> variants with a port number or no parameters are supported: <code>listen()</code>, <code>listen(0, callback)</code>, <code>listen(callback)</code>, etc.</li>
<li>The following server options are not supported: <code>maxHeaderSize</code>, <code>insecureHTTPParser</code>, <code>keepAliveTimeout</code>, <code>connectionsCheckingInterval</code></li>
<li>TLS/SSL-specific options such as <code>ca</code>, <code>cert</code>, <code>key</code>, <code>pfx</code>, <code>rejectUnauthorized</code>, <code>secureProtocol</code> are not supported in the Workers environment. If you need to use mTLS, use the <a href="/workers/runtime-apis/bindings/mtls/">mTLS binding</a>.</li>
</ul>
<h2 id="other-differences-between-node-js-and-workers-implementation-of-node-https">Other differences between Node.js and Workers implementation of <code>node:https</code></h2>
<p>Because the Workers implementation of <code>node:https</code> is a wrapper around the global <code>fetch</code> API, there are some differences in behavior compared to Node.js:</p>
<ul>
<li><code>Connection</code> headers are not used. Workers will manage connections automatically.</li>
<li><code>Content-Length</code> headers will be handled the same way as in the <code>fetch</code> API. If a body is provided, the header will be set automatically and manually set values will be ignored.</li>
<li><code>Expect: 100-continue</code> headers are not supported.</li>
<li>Trailing headers are not supported.</li>
<li>The <code>'continue'</code> event is not supported.</li>
<li>The <code>'information'</code> event is not supported.</li>
<li>The <code>'socket'</code> event is not supported.</li>
<li>The <code>'upgrade'</code> event is not supported.</li>
<li>Gaining direct access to the underlying <code>socket</code> is not supported.</li>
<li>Configuring TLS-specific options like <code>ca</code>, <code>cert</code>, <code>key</code>, <code>rejectUnauthorized</code>, etc, is not supported.</li>
</ul>
