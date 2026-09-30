<p>The <code>Response</code> interface represents an HTTP response and is part of the Fetch API.</p>
<hr />
<h2 id="constructor">Constructor</h2>
<pre><code class="language-js">let response = new Response(body, init);&#10;</code></pre>
<h3 id="parameters">Parameters</h3>
<ul>
<li>
<p><code>body</code> optional</p>
<ul>
<li>
<p>An object that defines the body text for the response. Can be <code>null</code> or any one of the following types:</p>
<ul>
<li>BufferSource</li>
<li>FormData</li>
<li>ReadableStream</li>
<li>URLSearchParams</li>
<li>USVString</li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>init</code> optional</p>
<ul>
<li>An <code>options</code> object that contains custom settings to apply to the response.</li>
</ul>
</li>
</ul>
<p>Valid options for the <code>options</code> object include:</p>
<ul>
<li><code>cf</code> any | null
<ul>
<li>An object that contains Cloudflare-specific information. This object is not part of the Fetch API standard and is only available in Cloudflare Workers. This field is only used by consumers of the Response for informational purposes and does not have any impact on Workers behavior.</li>
</ul>
</li>
<li><code>encodeBody</code> string
<ul>
<li>Workers have to compress data according to the <code>content-encoding</code> header when transmitting, to serve data that is already compressed, this property has to be set to <code>&quot;manual&quot;</code>, otherwise the default is <code>&quot;automatic&quot;</code>.</li>
</ul>
</li>
<li><code>headers</code> Headers | ByteString
<ul>
<li>Any headers to add to your response that are contained within a <a href="/workers/runtime-apis/request/#parameters"><code>Headers</code></a> object or object literal of <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String"><code>ByteString</code></a> key-value pairs.</li>
</ul>
</li>
<li><code>status</code> int
<ul>
<li>The status code for the response, such as <code>200</code>.</li>
</ul>
</li>
<li><code>statusText</code> string
<ul>
<li>The status message associated with the status code, such as, <code>OK</code>.</li>
</ul>
</li>
<li><code>webSocket</code> WebSocket | null
<ul>
<li>This is present in successful WebSocket handshake responses. For example, if a client sends a WebSocket upgrade request to an origin and a Worker intercepts the request and then forwards it to the origin and the origin replies with a successful WebSocket upgrade response, the Worker sees <code>response.webSocket</code>. This establishes a WebSocket connection proxied through a Worker. Note that you cannot intercept data flowing over a WebSocket connection.</li>
</ul>
</li>
</ul>
<h2 id="properties">Properties</h2>
<ul>
<li><code>response.body</code> Readable Stream
<ul>
<li>A getter to get the body contents.</li>
</ul>
</li>
<li><code>response.bodyUsed</code> boolean
<ul>
<li>A boolean indicating if the body was used in the response.</li>
</ul>
</li>
<li><code>response.headers</code> Headers
<ul>
<li>The headers for the response.</li>
</ul>
</li>
<li><code>response.ok</code> boolean
<ul>
<li>A boolean indicating if the response was successful (status in the range <code>200</code>-<code>299</code>).</li>
</ul>
</li>
<li><code>response.redirected</code> boolean
<ul>
<li>A boolean indicating if the response is the result of a redirect. If so, its URL list has more than one entry.</li>
</ul>
</li>
<li><code>response.status</code> int
<ul>
<li>The status code of the response (for example, <code>200</code> to indicate success).</li>
</ul>
</li>
<li><code>response.statusText</code> string
<ul>
<li>The status message corresponding to the status code (for example, <code>OK</code> for <code>200</code>).</li>
</ul>
</li>
<li><code>response.url</code> string
<ul>
<li>The URL of the response. The value is the final URL obtained after any redirects.</li>
</ul>
</li>
<li><code>response.webSocket</code> WebSocket?
<ul>
<li>This is present in successful WebSocket handshake responses. For example, if a client sends a WebSocket upgrade request to an origin and a Worker intercepts the request and then forwards it to the origin and the origin replies with a successful WebSocket upgrade response, the Worker sees <code>response.webSocket</code>. This establishes a WebSocket connection proxied through a Worker. Note that you cannot intercept data flowing over a WebSocket connection.</li>
</ul>
</li>
</ul>
<h2 id="methods">Methods</h2>
<h3 id="instance-methods">Instance methods</h3>
<ul>
<li>
<p><code>clone()</code> : Response</p>
<ul>
<li>Creates a clone of a <a href="#response"><code>Response</code></a> object.</li>
</ul>
</li>
<li>
<p><code>json()</code> : Response</p>
<ul>
<li>Creates a new response with a JSON-serialized payload.</li>
</ul>
</li>
<li>
<p><code>redirect()</code> : Response</p>
<ul>
<li>Creates a new response with a different URL.</li>
</ul>
</li>
</ul>
<h3 id="additional-instance-methods">Additional instance methods</h3>
<p><code>Response</code> implements the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#body"><code>Body</code></a> mixin of the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API">Fetch API</a>, and therefore <code>Response</code> instances additionally have the following methods available:</p>
<ul>
<li>
<p><code>arrayBuffer()</code> : Promise&lt;ArrayBuffer&gt;</p>
<ul>
<li>Takes a <a href="#response"><code>Response</code></a> stream, reads it to completion, and returns a promise that resolves with an <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer"><code>ArrayBuffer</code></a>.</li>
</ul>
</li>
<li>
<p><code>formData()</code> : Promise&lt;FormData&gt;</p>
<ul>
<li>Takes a <a href="#response"><code>Response</code></a> stream, reads it to completion, and returns a promise that resolves with a <a href="https://developer.mozilla.org/en-US/docs/Web/API/FormData"><code>FormData</code></a> object.</li>
</ul>
</li>
<li>
<p><code>json()</code> : Promise&lt;JSON&gt;</p>
<ul>
<li>Takes a <a href="#response"><code>Response</code></a> stream, reads it to completion, and returns a promise that resolves with the result of parsing the body text as <a href="https://developer.mozilla.org/en-US/docs/Web/"><code>JSON</code></a>.</li>
</ul>
</li>
<li>
<p><code>text()</code> : Promise&lt;USVString&gt;</p>
<ul>
<li>Takes a <a href="#response"><code>Response</code></a> stream, reads it to completion, and returns a promise that resolves with a <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String"><code>USVString</code></a> (text).</li>
</ul>
</li>
</ul>
<h3 id="set-the-content-length-header">Set the <code>Content-Length</code> header</h3>
<p>The <code>Content-Length</code> header will be automatically set by the runtime based on whatever the data source for the <code>Response</code> is. Any value manually set by user code in the <code>Headers</code> will be ignored. To have a <code>Content-Length</code> header with a specific value specified, the <code>body</code> of the <code>Response</code> must be either a <code>FixedLengthStream</code> or a fixed-length value just as a string or <code>TypedArray</code>.</p>
<p>A <code>FixedLengthStream</code> is an identity <code>TransformStream</code> that permits only a fixed number of bytes to be written to it.</p>
<pre><code class="language-js">  const { writable, readable } = new FixedLengthStream(11);&#10;&#10;  const enc = new TextEncoder();&#10;  const writer = writable.getWriter();&#10;  writer.write(enc.encode(&quot;hello world&quot;));&#10;  writer.end();&#10;&#10;  return new Response(readable);&#10;</code></pre>
<p>Using any other type of <code>ReadableStream</code> as the body of a response will result in chunked encoding being used.</p>
<hr />
<h2 id="differences">Differences</h2>
<p>The Workers implementation of the <code>Response</code> interface includes several extensions to the web standard <code>Response</code> API. These differences are intentional and provide additional functionality specific to the Workers runtime.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="typescript-users">TypeScript users</h3>
@markup("md", "content/.markup/bodies/16133.md")
</aside>
<h3 id="the-cf-property">The <code>cf</code> property</h3>
<p>Workers adds an optional <code>cf</code> property to the <code>Response</code> object. This property can be set in the <code>ResponseInit</code> options and is used for informational purposes by consumers of the Response. It does not affect Workers behavior.</p>
<h3 id="the-websocket-property">The <code>webSocket</code> property</h3>
<p>Workers adds a <code>webSocket</code> property to the <code>Response</code> object to support WebSocket connections. This property is present in successful WebSocket handshake responses. Refer to <a href="/workers/runtime-apis/websockets/">WebSockets</a> for more information.</p>
<h3 id="the-encodebody-option">The <code>encodeBody</code> option</h3>
<p>Workers adds an <code>encodeBody</code> option in <code>ResponseInit</code> that controls how the response body is compressed. Set this to <code>&quot;manual&quot;</code> when serving pre-compressed data to prevent automatic compression.</p>
<h3 id="the-headers-property">The <code>headers</code> property</h3>
<p>The <code>headers</code> property returns a Workers-specific <a href="/workers/runtime-apis/headers/"><code>Headers</code></a> object that includes additional methods like <code>getAll()</code> for <code>Set-Cookie</code> headers. Refer to the <a href="/workers/runtime-apis/headers/#differences">Headers documentation</a> for details on how the Workers <code>Headers</code> implementation differs from the web standard.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/examples/modify-response/">Examples: Modify response</a></li>
<li><a href="/workers/examples/conditional-response/">Examples: Conditional response</a></li>
<li><a href="/workers/runtime-apis/request/">Reference: <code>Request</code></a></li>
<li>Write your Worker code in <a href="/workers/reference/migrate-to-module-workers/">ES modules syntax</a> for an optimized experience.</li>
</ul>
