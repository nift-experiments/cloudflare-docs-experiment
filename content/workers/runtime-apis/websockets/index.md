---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/websockets/
  description: Communicate in real time with your Cloudflare Workers.
  full_title: WebSockets · Cloudflare Workers docs
  head_html: <title>WebSockets · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Communicate in real time with your Cloudflare Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/websockets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/websockets/index.md"><meta property="og:title" content="WebSockets · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Communicate in real time with your Cloudflare Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/websockets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/websockets/#page","headline":"WebSockets \u00b7 Cloudflare Workers docs","description":"Communicate in real time with your Cloudflare Workers.","url":"https://developers.cloudflare.com/workers/runtime-apis/websockets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/websockets/
  schema: 1
---
<h2 id="background">Background</h2>
<p>WebSockets allow you to communicate in real time with your Cloudflare Workers serverless functions. For a complete example, refer to <a href="/workers/examples/websockets/">Using the WebSockets API</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16120.md")
</aside>
<h2 id="constructor">Constructor</h2>
<pre tabindex="0"><code class="language-js">// { 0: &lt;WebSocket&gt;, 1: &lt;WebSocket&gt; }&#10;let websocketPair = new WebSocketPair();&#10;</code></pre>
<p>The WebSocketPair returned from this constructor is an Object, with two WebSockets at keys <code>0</code> and <code>1</code>.</p>
<p>These WebSockets are commonly referred to as <code>client</code> and <code>server</code>. The below example combines <code>Object.values</code> and ES6 destructuring to retrieve the WebSockets as <code>client</code> and <code>server</code>:</p>
<pre tabindex="0"><code class="language-js">let [client, server] = Object.values(new WebSocketPair());&#10;</code></pre>
<h2 id="methods">Methods</h2>
<h3 id="accept">accept</h3>
<ul>
<li>
<p><code>accept(options?)</code></p>
<ul>
<li>Accepts the WebSocket connection and begins terminating requests for the WebSocket on Cloudflare's global network. This effectively enables the Workers runtime to begin responding to and handling WebSocket requests.</li>
</ul>
</li>
</ul>
<h4 id="parameters">Parameters</h4>
<ul>
<li>
<p><code>options</code> object optional</p>
<ul>
<li>
<p>An optional configuration object with the following properties:</p>
<ul>
<li><code>allowHalfOpen</code> boolean optional — When <code>true</code>, the runtime will not automatically send a reciprocal Close frame when a Close frame is received from the peer. Instead, <code>readyState</code> remains <code>CLOSING</code> until you explicitly call <code>close()</code>. This is useful for <a href="#close-behavior">WebSocket proxying</a> where you need to coordinate the close across both sides of the proxy. Defaults to <code>false</code>.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="addeventlistener">addEventListener</h3>
<ul>
<li>
<p><code>addEventListener(eventWebSocketEvent, callbackFunctionFunction)</code></p>
<ul>
<li>Add callback functions to be executed when an event has occurred on the WebSocket.</li>
</ul>
</li>
</ul>
<h4 id="parameters-1">Parameters</h4>
<ul>
<li>
<p><code>event</code> WebSocketEvent</p>
<ul>
<li>The WebSocket event (refer to <a href="/workers/runtime-apis/websockets/#events">Events</a>) to listen to.</li>
</ul>
</li>
<li>
<p><code>callbackFunction(messageMessage)</code> Function</p>
<ul>
<li>A function to be called when the WebSocket responds to a specific event.</li>
</ul>
</li>
</ul>
<h3 id="close">close</h3>
<ul>
<li>
<p><code>close(codenumber, reasonstring)</code></p>
<ul>
<li>Close the WebSocket connection.</li>
</ul>
</li>
</ul>
<h4 id="parameters-2">Parameters</h4>
<ul>
<li>
<p><code>codeinteger</code> optional</p>
<ul>
<li>An integer indicating the close code sent by the server. This should match an option from the <a href="https://developer.mozilla.org/en-US/docs/Web/API/CloseEvent#status_codes">list of status codes</a> provided by the WebSocket spec.</li>
</ul>
</li>
<li>
<p><code>reasonstring</code> optional</p>
<ul>
<li>A human-readable string indicating why the WebSocket connection was closed.</li>
</ul>
</li>
</ul>
<h3 id="send">send</h3>
<ul>
<li>
<p><code>send(messagestring | ArrayBuffer | ArrayBufferView)</code></p>
<ul>
<li>Send a message to the other WebSocket in this WebSocket pair.</li>
</ul>
</li>
</ul>
<h4 id="parameters-3">Parameters</h4>
<ul>
<li>
<p><code>messagestring</code></p>
<ul>
<li>The message to send down the WebSocket connection to the corresponding client. This should be a string or something coercible into a string; for example, strings and numbers will be simply cast into strings, but objects and arrays should be cast to JSON strings using <code>JSON.stringify</code>, and parsed in the client.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="properties">Properties</h2>
<h3 id="readystate">readyState</h3>
<ul>
<li>
<p><code>readyState</code> number</p>
<ul>
<li>Returns the current state of the WebSocket connection. Possible values:</li>
</ul>
</li>
</ul>
<table>
<thead>
<tr>
<th>Constant</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>WebSocket.CONNECTING</code></td>
<td><code>0</code></td>
<td>The connection is not yet open.</td>
</tr>
<tr>
<td><code>WebSocket.OPEN</code></td>
<td><code>1</code></td>
<td>The connection is open and ready to communicate.</td>
</tr>
<tr>
<td><code>WebSocket.CLOSING</code></td>
<td><code>2</code></td>
<td>The connection is in the process of closing.</td>
</tr>
<tr>
<td><code>WebSocket.CLOSED</code></td>
<td><code>3</code></td>
<td>The connection is closed.</td>
</tr>
</tbody>
</table>
<h3 id="binarytype">binaryType</h3>
<ul>
<li>
<p><code>binaryType</code> string</p>
<ul>
<li>Controls how binary frames received on this WebSocket are surfaced to the <code>message</code> event. Valid values are <code>&quot;blob&quot;</code> and <code>&quot;arraybuffer&quot;</code>. The value is consulted when each incoming binary frame is dispatched, so assigning a new value affects subsequent messages only. The default is controlled by the <a href="/workers/configuration/compatibility-flags/#websocket-standard-binary-type"><code>websocket_standard_binary_type</code></a> compatibility flag. Refer to <a href="#binary-messages">Binary messages</a> for details.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="events">Events</h2>
<ul>
<li>
<p><code>close</code></p>
<ul>
<li>An event indicating the WebSocket has closed. The <code>CloseEvent</code> includes <code>code</code> (number), <code>reason</code> (string), and <code>wasClean</code> (boolean) properties.</li>
</ul>
</li>
<li>
<p><code>error</code></p>
<ul>
<li>An event indicating there was an error with the WebSocket.</li>
</ul>
</li>
<li>
<p><code>message</code></p>
<ul>
<li>An event indicating a new message received from the client, including the data passed by the client.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16119.md")
</aside>
<h2 id="types">Types</h2>
<h3 id="message">Message</h3>
<ul>
<li><code>data</code> any - The data passed back from the other WebSocket in your pair.</li>
<li><code>type</code> string - Defaults to <code>message</code>.</li>
</ul>
<hr />
<h2 id="close-behavior">Close behavior</h2>
<p>With the <a href="/workers/configuration/compatibility-flags/#websocket-auto-reply-to-close"><code>web_socket_auto_reply_to_close</code></a> compatibility flag (enabled by default on compatibility dates on or after <code>2026-04-07</code>), the Workers runtime automatically sends a reciprocal Close frame when it receives a Close frame from the peer. The <code>readyState</code> transitions to <code>CLOSED</code> before the <code>close</code> event fires. This matches the <a href="https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close_event">WebSocket specification</a> and standard browser behavior.</p>
<p>If you still call <code>close()</code> inside the <code>close</code> event handler, the call is silently ignored. Existing code that manually replies to Close frames will continue to work without changes.</p>
<pre tabindex="0"><code class="language-js">server.addEventListener(&quot;close&quot;, (event) =&gt; {&#10;  // readyState is already CLOSED — no need to call server.close().&#10;  console.log(server.readyState); // WebSocket.CLOSED&#10;  console.log(event.code);        // 1000&#10;  console.log(event.wasClean);    // true&#10;});&#10;</code></pre>
<h3 id="half-open-mode-for-proxying">Half-open mode for proxying</h3>
<p>The automatic close behavior can interfere with WebSocket proxying, where a Worker sits between a client and a backend and needs to coordinate the close on both sides independently. To support this, pass <code>{ allowHalfOpen: true }</code> to <code>accept()</code>:</p>
<pre tabindex="0"><code class="language-js">server.accept({ allowHalfOpen: true });&#10;&#10;server.addEventListener(&quot;close&quot;, (event) =&gt; {&#10;  // readyState is still CLOSING here, giving you time&#10;  // to coordinate the close on the other side.&#10;  console.log(server.readyState); // WebSocket.CLOSING&#10;&#10;  // Manually close when ready.&#10;  server.close(event.code, &quot;done&quot;);&#10;});&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16118.md")
</aside>
<h3 id="prior-behavior">Prior behavior</h3>
<p>On compatibility dates before <code>2026-04-07</code> (or with the <code>web_socket_manual_reply_to_close</code> flag), receiving a Close frame leaves the WebSocket in <code>CLOSING</code> state, and your code must call <code>close()</code> to complete the handshake. Failing to do so can result in <code>1006</code> abnormal closure errors on the client.</p>
<hr />
<h2 id="binary-messages">Binary messages</h2>
<p>WebSocket frames carry either text or binary payloads, and the choice between the two is made by the sender at the time the frame is sent. Text frames are always delivered to the <code>message</code> event as JavaScript strings. Binary frames are delivered either as <a href="https://developer.mozilla.org/en-US/docs/Web/API/Blob"><code>Blob</code></a> or as <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer"><code>ArrayBuffer</code></a>, depending on the WebSocket's <code>binaryType</code>.</p>
<p>With the <a href="/workers/configuration/compatibility-flags/#websocket-standard-binary-type"><code>websocket_standard_binary_type</code></a> compatibility flag (enabled by default on compatibility dates on or after <code>2026-03-17</code>), <code>binaryType</code> defaults to <code>&quot;blob&quot;</code> and binary frames are delivered as <code>Blob</code> objects. This matches the <a href="https://websockets.spec.whatwg.org/">WebSocket specification</a> and standard browser behavior. Without the flag, <code>binaryType</code> defaults to <code>&quot;arraybuffer&quot;</code> and binary frames are delivered as <code>ArrayBuffer</code>, matching the runtime's historical behavior.</p>
<p>The <code>binaryType</code> property itself is always available. To opt back into <code>ArrayBuffer</code> delivery for a single WebSocket, assign <code>binaryType</code> before calling <code>accept()</code>:</p>
<pre tabindex="0"><code class="language-js">const resp = await fetch(&quot;https://example.com&quot;, {&#10;  headers: { Upgrade: &quot;websocket&quot; },&#10;});&#10;const ws = resp.webSocket;&#10;&#10;// Opt back into ArrayBuffer delivery for this WebSocket.&#10;ws.binaryType = &quot;arraybuffer&quot;;&#10;ws.accept();&#10;&#10;ws.addEventListener(&quot;message&quot;, (event) =&gt; {&#10;  if (typeof event.data === &quot;string&quot;) {&#10;    // Text frame.&#10;  } else {&#10;    // event.data is an ArrayBuffer because we set binaryType above.&#10;  }&#10;});&#10;</code></pre>
<h3 id="reading-binary-payloads">Reading binary payloads</h3>
<p>An incoming binary frame is fully buffered before the <code>message</code> event fires, regardless of <code>binaryType</code>. The choice between <code>Blob</code> and <code>ArrayBuffer</code> does not change when or whether the frame is received — only how you access its bytes:</p>
<ul>
<li>With <code>&quot;arraybuffer&quot;</code>, <code>event.data</code> is an <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer"><code>ArrayBuffer</code></a>. You can inspect its size and read bytes synchronously (for example, <code>new Uint8Array(event.data)</code>).</li>
<li>With <code>&quot;blob&quot;</code>, <code>event.data</code> is a <a href="https://developer.mozilla.org/en-US/docs/Web/API/Blob"><code>Blob</code></a>. Reading the bytes is asynchronous — for example, <code>await event.data.arrayBuffer()</code> or <code>await event.data.bytes()</code>.</li>
</ul>
<p>Under the new default, a binary message handler must be <code>async</code> in order to read the payload. If you want to keep an existing synchronous handler, set <code>binaryType</code> to <code>&quot;arraybuffer&quot;</code> on the WebSocket.</p>
<h3 id="when-the-value-takes-effect">When the value takes effect</h3>
<p>Per the <a href="https://websockets.spec.whatwg.org/#feedback-from-the-protocol">WebSocket specification</a>, <code>binaryType</code> is mutable: the value is consulted at the moment each binary frame is dispatched to the <code>message</code> event, so assigning a new value affects only subsequent messages. If you want every binary message on a WebSocket to be delivered as the same type, assign <code>binaryType</code> before calling <code>accept()</code>. That guarantees the setting is in place before the runtime starts dispatching any incoming frames.</p>
<h3 id="worker-wide-opt-out">Worker-wide opt-out</h3>
<p>If you are not ready to migrate and want to keep <code>ArrayBuffer</code> as the default for every WebSocket in your Worker, add the <code>no_websocket_standard_binary_type</code> flag to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>. Individual WebSockets can still override the default by assigning <code>binaryType</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16117.md")
</aside>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/WebSocket">Mozilla Developer Network's (MDN) documentation on the WebSocket class</a></li>
<li><a href="https://github.com/cloudflare/websocket-template">Our WebSocket template for building applications on Workers using WebSockets</a></li>
</ul>
