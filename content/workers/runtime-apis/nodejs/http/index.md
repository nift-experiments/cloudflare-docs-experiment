---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/nodejs/http/
  description: Use the Node.js http module in Cloudflare Workers for client and server-side HTTP functionality.
  full_title: http · Cloudflare Workers docs
  head_html: <title>http · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the Node.js http module in Cloudflare Workers for client and server-side HTTP functionality."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/http/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/http/index.md"><meta property="og:title" content="http · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the Node.js http module in Cloudflare Workers for client and server-side HTTP functionality."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/nodejs/http/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/http/#page","headline":"http \u00b7 Cloudflare Workers docs","description":"Use the Node.js http module in Cloudflare Workers for client and server-side HTTP functionality.","url":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/http/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/nodejs/http/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17148.md")
</aside>
<h2 id="compatibility-flags">Compatibility flags</h2>
<h3 id="client-side-methods">Client-side methods</h3>
<p>To use the HTTP client-side methods (<code>http.get</code>, <code>http.request</code>, etc.), you must enable the <a href="/workers/configuration/compatibility-flags/"><code>enable_nodejs_http_modules</code></a> compatibility flag in addition to the <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code></a> flag.</p>
<p>This flag is automatically enabled for Workers using a <a href="/workers/configuration/compatibility-dates/">compatibility date</a> of <code>2025-08-15</code> or later when <code>nodejs_compat</code> is enabled. For Workers using an earlier compatibility date, you can manually enable it by adding the flag to your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17149.md")
</div>
<h3 id="server-side-methods">Server-side methods</h3>
<p>To use the HTTP server-side methods (<code>http.createServer</code>, <code>http.Server</code>, <code>http.ServerResponse</code>), you must enable the <code>enable_nodejs_http_server_modules</code> compatibility flag in addition to the <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code></a> flag.</p>
<p>This flag is automatically enabled for Workers using a <a href="/workers/configuration/compatibility-dates/">compatibility date</a> of <code>2025-09-01</code> or later when <code>nodejs_compat</code> is enabled. For Workers using an earlier compatibility date, you can manually enable it by adding the flag to your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17150.md")
</div>
<p>To use both client-side and server-side methods, enable both flags:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17151.md")
</div>
<h2 id="get">get</h2>
<p>An implementation of the Node.js <a href="https://nodejs.org/docs/latest/api/http.html#httpgetoptions-callback"><code>http.get</code></a> method.</p>
<p>The <code>get</code> method performs a GET request to the specified URL and invokes the callback with the response. It's a convenience method that simplifies making HTTP GET requests without manually configuring request options.</p>
<p>Because <code>get</code> is a wrapper around <code>fetch(...)</code>, it may be used only within an exported
fetch or similar handler. Outside of such a handler, attempts to use <code>get</code> will throw
an error.</p>
<pre tabindex="0"><code class="language-js">import { get } from &quot;node:http&quot;;&#10;&#10;export default {&#10;	async fetch() {&#10;		const { promise, resolve, reject } = Promise.withResolvers();&#10;		get(&quot;http://example.org&quot;, (res) =&gt; {&#10;			let data = &quot;&quot;;&#10;			res.setEncoding(&quot;utf8&quot;);&#10;			res.on(&quot;data&quot;, (chunk) =&gt; {&#10;				data += chunk;&#10;			});&#10;			res.on(&quot;end&quot;, () =&gt; {&#10;				resolve(new Response(data));&#10;			});&#10;			res.on(&quot;error&quot;, reject);&#10;		}).on(&quot;error&quot;, reject);&#10;		return promise;&#10;	},&#10;};&#10;</code></pre>
<p>The implementation of <code>get</code> in Workers is a wrapper around the global
<a href="https://developers.cloudflare.com/workers/runtime-apis/fetch/"><code>fetch</code> API</a>
and is therefore subject to the same <a href="https://developers.cloudflare.com/workers/platform/limits/">limits</a>.</p>
<p>As shown in the example above, it is necessary to arrange for requests to be correctly
awaited in the <code>fetch</code> handler using a promise or the fetch may be canceled prematurely
when the handler returns.</p>
<h2 id="request">request</h2>
<p>An implementation of the Node.js <a href="https://nodejs.org/docs/latest/api/http.html#httprequesturl-options-callback">`http.request'</a> method.</p>
<p>The <code>request</code> method creates an HTTP request with customizable options like method, headers, and body. It provides full control over the request configuration and returns a Node.js <a href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/streams/">stream.Writable</a> for sending request data.</p>
<p>Because <code>request</code> is a wrapper around <code>fetch(...)</code>, it may be used only within an exported
fetch or similar handler. Outside of such a handler, attempts to use <code>request</code> will throw
an error.</p>
<pre tabindex="0"><code class="language-js">import { get } from &quot;node:http&quot;;&#10;&#10;export default {&#10;	async fetch() {&#10;		const { promise, resolve, reject } = Promise.withResolvers();&#10;		get(&#10;			{&#10;				method: &quot;GET&quot;,&#10;				protocol: &quot;http:&quot;,&#10;				hostname: &quot;example.org&quot;,&#10;				path: &quot;/&quot;,&#10;			},&#10;			(res) =&gt; {&#10;				let data = &quot;&quot;;&#10;				res.setEncoding(&quot;utf8&quot;);&#10;				res.on(&quot;data&quot;, (chunk) =&gt; {&#10;					data += chunk;&#10;				});&#10;				res.on(&quot;end&quot;, () =&gt; {&#10;					resolve(new Response(data));&#10;				});&#10;				res.on(&quot;error&quot;, reject);&#10;			},&#10;		)&#10;			.on(&quot;error&quot;, reject)&#10;			.end();&#10;		return promise;&#10;	},&#10;};&#10;</code></pre>
<p>The following options passed to the <code>request</code> (and <code>get</code>) method are not supported due to the differences required by Cloudflare Workers implementation of <code>node:http</code> as a wrapper around the global <code>fetch</code> API:</p>
<ul>
<li><code>maxHeaderSize</code></li>
<li><code>insecureHTTPParser</code></li>
<li><code>createConnection</code></li>
<li><code>lookup</code></li>
<li><code>socketPath</code></li>
</ul>
<h2 id="outgoingmessage">OutgoingMessage</h2>
<p>The <a href="https://nodejs.org/docs/latest/api/http.html#class-httpoutgoingmessage"><code>OutgoingMessage</code></a> class represents an HTTP response that is sent to the client. It provides methods for writing response headers and body, as well as for ending the response. <code>OutgoingMessage</code> extends from the Node.js <a href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/streams/"><code>stream.Writable</code> stream class</a>.</p>
<p>The <code>OutgoingMessage</code> class is a base class for outgoing HTTP messages (both requests and responses). It provides methods for writing headers and body data, as well as for ending the message. <code>OutgoingMessage</code> extends from the <a href="https://nodejs.org/docs/latest/api/stream.html#class-streamwritable"><code>Writable</code> stream class</a>.</p>
<p>Both <code>ClientRequest</code> and <code>ServerResponse</code> both extend from and inherit from <code>OutgoingMessage</code>.</p>
<h2 id="incomingmessage">IncomingMessage</h2>
<p>The <code>IncomingMessage</code> class represents an HTTP request that is received from the client. It provides methods for reading request headers and body, as well as for ending the request. <code>IncomingMessage</code> extends from the <code>Readable</code> stream class.</p>
<p>The <code>IncomingMessage</code> class represents an HTTP message (request or response). It provides methods for reading headers and body data. <code>IncomingMessage</code> extends from the <code>Readable</code> stream class.</p>
<pre tabindex="0"><code class="language-js">import { get, IncomingMessage } from &quot;node:http&quot;;&#10;import { ok, strictEqual } from &quot;node:assert&quot;;&#10;&#10;export default {&#10;	async fetch() {&#10;		// ...&#10;		get(&quot;http://example.org&quot;, (res) =&gt; {&#10;			ok(res instanceof IncomingMessage);&#10;		});&#10;		// ...&#10;	},&#10;};&#10;</code></pre>
<p>The Workers implementation includes a <code>cloudflare</code> property on <code>IncomingMessage</code> objects:</p>
<pre tabindex="0"><code class="language-js">import { createServer } from &quot;node:http&quot;;&#10;import { httpServerHandler } from &quot;cloudflare:node&quot;;&#10;&#10;const server = createServer((req, res) =&gt; {&#10;	console.log(req.cloudflare.cf.country);&#10;	console.log(req.cloudflare.cf.ray);&#10;	res.write(&quot;Hello, World!&quot;);&#10;	res.end();&#10;});&#10;&#10;server.listen(8080);&#10;&#10;export default httpServerHandler({ port: 8080 });&#10;</code></pre>
<p>The <code>cloudflare.cf</code> property contains <a href="/workers/runtime-apis/request/#incomingrequestcfproperties">Cloudflare-specific request properties</a>.</p>
<p>The following differences exist between the Workers implementation and Node.js:</p>
<ul>
<li>Trailer headers are not supported</li>
<li>The <code>socket</code> attribute <strong>does not extend from <code>net.Socket</code></strong> and only contains the following properties: <code>encrypted</code>, <code>remoteFamily</code>, <code>remoteAddress</code>, <code>remotePort</code>, <code>localAddress</code>, <code>localPort</code>, and <code>destroy()</code> method.</li>
<li>The following <code>socket</code> attributes behave differently than their Node.js counterparts:
<ul>
<li><code>remoteAddress</code> will return <code>127.0.0.1</code> when ran locally</li>
<li><code>remotePort</code> will return a random port number between 2^15 and 2^16</li>
<li><code>localAddress</code> will return the value of request's <code>host</code> header if exists. Otherwise, it will return <code>127.0.0.1</code></li>
<li><code>localPort</code> will return the port number assigned to the server instance</li>
<li><code>req.socket.destroy()</code> falls through to <code>req.destroy()</code></li>
</ul>
</li>
</ul>
<h2 id="agent">Agent</h2>
<p>A partial implementation of the Node.js <a href="https://nodejs.org/docs/latest/api/http.html#class-httpagent">`http.Agent'</a> class.</p>
<p>An <code>Agent</code> manages HTTP connection reuse by maintaining request queues per host/port. In the workers environment, however, such low-level management of the network connection, ports, etc, is not relevant because it is handled by the Cloudflare infrastructure instead. Accordingly, the implementation of <code>Agent</code> in Workers is a stub implementation that does not support connection pooling or keep-alive.</p>
<pre tabindex="0"><code class="language-js">import { Agent } from &quot;node:http&quot;;&#10;import { strictEqual } from &quot;node:assert&quot;;&#10;&#10;const agent = new Agent();&#10;strictEqual(agent.protocol, &quot;http:&quot;);&#10;</code></pre>
<h2 id="createserver">createServer</h2>
<p>An implementation of the Node.js <a href="https://nodejs.org/docs/latest/api/http.html#httpcreateserveroptions-requestlistener"><code>http.createServer</code></a> method.</p>
<p>The <code>createServer</code> method creates an HTTP server instance that can handle incoming requests.</p>
<pre tabindex="0"><code class="language-js">import { createServer } from &quot;node:http&quot;;&#10;import { httpServerHandler } from &quot;cloudflare:node&quot;;&#10;&#10;const server = createServer((req, res) =&gt; {&#10;	res.writeHead(200, { &quot;Content-Type&quot;: &quot;text/plain&quot; });&#10;	res.end(&quot;Hello from Node.js HTTP server!&quot;);&#10;});&#10;&#10;server.listen(8080);&#10;export default httpServerHandler({ port: 8080 });&#10;</code></pre>
<h2 id="node-js-integration">Node.js integration</h2>
<h3 id="httpserverhandler">httpServerHandler</h3>
<p>The <code>httpServerHandler</code> function integrates Node.js HTTP servers with the Cloudflare Workers request model. It supports two API patterns:</p>
<pre tabindex="0"><code class="language-js">import http from &quot;node:http&quot;;&#10;import { httpServerHandler } from &quot;cloudflare:node&quot;;&#10;&#10;const server = http.createServer((req, res) =&gt; {&#10;	res.end(&quot;hello world&quot;);&#10;});&#10;&#10;// Pass server directly (simplified) - automatically calls listen() if needed&#10;export default httpServerHandler(server);&#10;&#10;// Or use port-based routing for multiple servers&#10;server.listen(8080);&#10;export default httpServerHandler({ port: 8080 });&#10;</code></pre>
<p>The handler automatically routes incoming Worker requests to your Node.js server. When using port-based routing, the port number acts as a routing key to determine which server handles requests, allowing multiple servers to coexist in the same Worker.</p>
<h3 id="handleasnoderequest">handleAsNodeRequest</h3>
<p>For more direct control over request routing, you can use the <code>handleAsNodeRequest</code> function from <code>cloudflare:node</code>. This function directly routes a Worker request to a Node.js server running on a specific port:</p>
<pre tabindex="0"><code class="language-js">import { createServer } from &quot;node:http&quot;;&#10;import { handleAsNodeRequest } from &quot;cloudflare:node&quot;;&#10;&#10;const server = createServer((req, res) =&gt; {&#10;	res.writeHead(200, { &quot;Content-Type&quot;: &quot;text/plain&quot; });&#10;	res.end(&quot;Hello from Node.js HTTP server!&quot;);&#10;});&#10;&#10;server.listen(8080);&#10;&#10;export default {&#10;	fetch(request) {&#10;		return handleAsNodeRequest(8080, request);&#10;	},&#10;};&#10;</code></pre>
<p>This approach gives you full control over the fetch handler while still leveraging Node.js HTTP servers for request processing.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17147.md")
</aside>
<h2 id="server">Server</h2>
<p>An implementation of the Node.js <a href="https://nodejs.org/docs/latest/api/http.html#class-httpserver"><code>http.Server</code></a> class.</p>
<p>The <code>Server</code> class represents an HTTP server and provides methods for handling incoming requests. It extends the Node.js <code>EventEmitter</code> class and can be used to create custom server implementations.</p>
<p>When using <code>httpServerHandler</code>, the port number specified in <code>server.listen()</code> acts as a routing key rather than an actual network port. The handler uses this port to determine which HTTP server instance should handle incoming requests, allowing multiple servers to coexist within the same Worker by using different port numbers for identification. Using a port value of <code>0</code> (or <code>null</code> or <code>undefined</code>) will result in a random port number being assigned.</p>
<pre tabindex="0"><code class="language-js">import { Server } from &quot;node:http&quot;;&#10;import { httpServerHandler } from &quot;cloudflare:node&quot;;&#10;&#10;const server = new Server((req, res) =&gt; {&#10;	res.writeHead(200, { &quot;Content-Type&quot;: &quot;application/json&quot; });&#10;	res.end(JSON.stringify({ message: &quot;Hello from HTTP Server!&quot; }));&#10;});&#10;&#10;server.listen(8080);&#10;export default httpServerHandler({ port: 8080 });&#10;</code></pre>
<p>The following differences exist between the Workers implementation and Node.js:</p>
<ul>
<li>Connection management methods such as <code>closeAllConnections()</code> and <code>closeIdleConnections()</code> are not implemented</li>
<li>Only <code>listen()</code> variants with a port number or no parameters are supported: <code>listen()</code>, <code>listen(0, callback)</code>, <code>listen(callback)</code>, etc. For reference, see the <a href="https://nodejs.org/docs/latest/api/net.html#serverlisten">Node.js documentation</a>.</li>
<li>The following server options are not supported: <code>maxHeaderSize</code>, <code>insecureHTTPParser</code>, <code>keepAliveTimeout</code>, <code>connectionsCheckingInterval</code></li>
</ul>
<h2 id="serverresponse">ServerResponse</h2>
<p>An implementation of the Node.js <a href="https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse"><code>http.ServerResponse</code></a> class.</p>
<p>The <code>ServerResponse</code> class represents the server-side response object that is passed to request handlers. It provides methods for writing response headers and body data, and extends the Node.js <code>Writable</code> stream class.</p>
<pre tabindex="0"><code class="language-js">import { createServer, ServerResponse } from &quot;node:http&quot;;&#10;import { httpServerHandler } from &quot;cloudflare:node&quot;;&#10;import { ok } from &quot;node:assert&quot;;&#10;&#10;const server = createServer((req, res) =&gt; {&#10;	ok(res instanceof ServerResponse);&#10;&#10;	// Set multiple headers at once&#10;	res.writeHead(200, {&#10;		&quot;Content-Type&quot;: &quot;application/json&quot;,&#10;		&quot;X-Custom-Header&quot;: &quot;Workers-HTTP&quot;,&#10;	});&#10;&#10;	// Stream response data&#10;	res.write(&#x27;{&quot;data&quot;: [&#x27;);&#10;	res.write(&#x27;{&quot;id&quot;: 1, &quot;name&quot;: &quot;Item 1&quot;},&#x27;);&#10;	res.write(&#x27;{&quot;id&quot;: 2, &quot;name&quot;: &quot;Item 2&quot;}&#x27;);&#10;	res.write(&quot;]}&quot;);&#10;&#10;	// End the response&#10;	res.end();&#10;});&#10;&#10;export default httpServerHandler(server);&#10;</code></pre>
<p>The following methods and features are not supported in the Workers implementation:</p>
<ul>
<li><code>assignSocket()</code> and <code>detachSocket()</code> methods are not available</li>
<li>Trailer headers are not supported</li>
<li><code>writeContinue()</code> and <code>writeEarlyHints()</code> methods are not available</li>
<li>1xx responses in general are not supported</li>
</ul>
<h2 id="other-differences-between-node-js-and-workers-implementation-of-node-http">Other differences between Node.js and Workers implementation of <code>node:http</code></h2>
<p>Because the Workers implementation of <code>node:http</code> is a wrapper around the global <code>fetch</code> API, there are some differences in behavior and limitations compared to a standard Node.js environment:</p>
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
</ul>
