<p class="article-summary">Use the WebSockets API to communicate in real time with your Cloudflare Workers.</p>
<p>WebSockets allow you to communicate in real time with your Cloudflare Workers serverless functions. In this guide, you will learn the basics of WebSockets on Cloudflare Workers, both from the perspective of writing WebSocket servers in your Workers functions, as well as connecting to and working with those WebSocket servers as a client.</p>
<p>WebSockets are open connections sustained between the client and the origin server. Inside a WebSocket connection, the client and the origin can pass data back and forth without having to reestablish sessions. This makes exchanging data within a WebSocket connection fast. WebSockets are often used for real-time applications such as live chat and gaming.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16309.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16308.md")
</aside>
<h2 id="write-a-websocket-server">Write a WebSocket Server</h2>
<p>WebSocket servers in Cloudflare Workers allow you to receive messages from a client in real time. This guide will show you how to set up a WebSocket server in Workers.</p>
<p>A client can make a WebSocket request in the browser by instantiating a new instance of <code>WebSocket</code>, passing in the URL for your Workers function:</p>
<pre><code class="language-js">// In client-side JavaScript, connect to your Workers function using WebSockets:&#10;const websocket = new WebSocket(&#10;	&quot;wss://example-websocket.signalnerve.workers.dev&quot;,&#10;);&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16307.md")
</aside>
<p>When an incoming WebSocket request reaches the Workers function, it will contain an <code>Upgrade</code> header, set to the string value <code>websocket</code>. Check for this header before continuing to instantiate a WebSocket:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16312.md")
</div></div>
After you have appropriately checked for the `Upgrade` header, you can create a new instance of `WebSocketPair`, which contains server and client WebSockets. One of these WebSockets should be handled by the Workers function and the other should be returned as part of a `Response` with the [`101` status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/101), indicating the request is switching protocols:
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16315.md")
</div></div>
<p>The <code>WebSocketPair</code> constructor returns an Object, with the <code>0</code> and <code>1</code> keys each holding a <code>WebSocket</code> instance as its value. It is common to grab the two WebSockets from this pair using <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Object/values"><code>Object.values</code></a> and <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment">ES6 destructuring</a>, as seen in the below example.</p>
<p>In order to begin communicating with the <code>client</code> WebSocket in your Worker, call <code>accept</code> on the <code>server</code> WebSocket. This will tell the Workers runtime that it should listen for WebSocket data and keep the connection open with your <code>client</code> WebSocket:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16318.md")
</div></div>
<p>WebSockets emit a number of <a href="/workers/runtime-apis/websockets/#events">Events</a> that can be connected to using <code>addEventListener</code>. The below example hooks into the <code>message</code> event and emits a <code>console.log</code> with the data from it:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16322.md")
</div></div>
<h3 id="connect-to-the-websocket-server-from-a-client">Connect to the WebSocket server from a client</h3>
<p>Writing WebSocket clients that communicate with your Workers function is a two-step process: first, create the WebSocket instance, and then attach event listeners to it:</p>
<pre><code class="language-js">const websocket = new WebSocket(&#10;	&quot;wss://websocket-example.signalnerve.workers.dev&quot;,&#10;);&#10;websocket.addEventListener(&quot;message&quot;, (event) =&gt; {&#10;	console.log(&quot;Message received from server&quot;);&#10;	console.log(event.data);&#10;});&#10;</code></pre>
<p>WebSocket clients can send messages back to the server using the <a href="/workers/runtime-apis/websockets/#send"><code>send</code></a> function:</p>
<pre><code class="language-js">websocket.send(&quot;MESSAGE&quot;);&#10;</code></pre>
<p>When the WebSocket interaction is complete, the client can close the connection using <a href="/workers/runtime-apis/websockets/#close"><code>close</code></a>:</p>
<pre><code class="language-js">websocket.close();&#10;</code></pre>
<p>For an example of this in practice, refer to the <a href="https://github.com/cloudflare/websocket-template"><code>websocket-template</code></a> to get started with WebSockets.</p>
<h2 id="write-a-websocket-client">Write a WebSocket client</h2>
<p>Cloudflare Workers supports the <code>new WebSocket(url)</code> constructor. A Worker can establish a WebSocket connection to a remote server in the same manner as the client implementation described above.</p>
<p>Additionally, Cloudflare supports establishing WebSocket connections by making a fetch request to a URL with the <code>Upgrade</code> header set.</p>
<pre><code class="language-js">async function websocket(url) {&#10;	// Make a fetch request including `Upgrade: websocket` header.&#10;	// The Workers Runtime will automatically handle other requirements&#10;	// of the WebSocket protocol, like the Sec-WebSocket-Key header.&#10;	let resp = await fetch(url, {&#10;		headers: {&#10;			Upgrade: &quot;websocket&quot;,&#10;		},&#10;	});&#10;&#10;	// If the WebSocket handshake completed successfully, then the&#10;	// response has a `webSocket` property.&#10;	let ws = resp.webSocket;&#10;	if (!ws) {&#10;		throw new Error(&quot;server didn&#x27;t accept WebSocket&quot;);&#10;	}&#10;&#10;	// Call accept() to indicate that you&#x27;ll be handling the socket here&#10;	// in JavaScript, as opposed to returning it on to a client.&#10;	// You can pass { allowHalfOpen: true } if you need to coordinate&#10;	// the close handshake manually (for example, when proxying).&#10;	ws.accept();&#10;&#10;	// Now you can send and receive messages like before.&#10;	ws.send(&quot;hello&quot;);&#10;	ws.addEventListener(&quot;message&quot;, (msg) =&gt; {&#10;		console.log(msg.data);&#10;	});&#10;}&#10;</code></pre>
<h2 id="websocket-close-behavior">WebSocket close behavior</h2>
<p>With the <a href="/workers/configuration/compatibility-flags/#websocket-auto-reply-to-close"><code>web_socket_auto_reply_to_close</code></a> compatibility flag (enabled by default on compatibility dates on or after <code>2026-04-07</code>), the Workers runtime automatically replies to incoming Close frames and transitions <code>readyState</code> to <code>CLOSED</code> before firing the <code>close</code> event. You do not need to call <code>close()</code> in your <code>close</code> event handler, but doing so is safe (the call is silently ignored).</p>
<p>If you need half-open behavior (for example, for WebSocket proxying), pass <code>{ allowHalfOpen: true }</code> to <code>accept()</code>. Note that <code>new WebSocket(url)</code> always auto-replies after this flag takes effect. To get half-open behavior for a client WebSocket, use the <code>fetch()</code>-based pattern shown above and call <code>ws.accept({ allowHalfOpen: true })</code>.</p>
<p>For more details, refer to <a href="/workers/runtime-apis/websockets/#close-behavior">WebSocket close behavior</a>.</p>
<h2 id="websocket-compression">WebSocket compression</h2>
<p>Cloudflare Workers supports WebSocket compression. Refer to <a href="/workers/configuration/compatibility-flags/#websocket-compression">WebSocket Compression</a> for more information.</p>
