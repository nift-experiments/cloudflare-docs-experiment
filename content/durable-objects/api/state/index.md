<h2 id="description">Description</h2>
<p>The <code>DurableObjectState</code> interface is accessible as an instance property on the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8329.md")
</div>. This interface encapsulates methods that modify the state of a Durable Object, for example which WebSockets are attached to a Durable Object or how the runtime should handle concurrent Durable Object requests.
<p>The <code>DurableObjectState</code> interface is different from the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8330.md")
</div> in that it does not have top-level methods which manipulate persistent application data. These methods are instead encapsulated in the [`DurableObjectStorage`](/durable-objects/api/sqlite-storage-api/) interface and accessed by [`DurableObjectState::storage`](/durable-objects/api/state/#storage).
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8334.md")
</div></div>
<h2 id="methods-and-properties">Methods and Properties</h2>
<h3 id="exports"><code>exports</code></h3>
<p>Contains loopback bindings to the Worker's own top-level exports. This has exactly the same meaning as <a href="/workers/runtime-apis/context/#exports"><code>ExecutionContext</code>'s <code>ctx.exports</code></a>.</p>
<h3 id="waituntil"><code>waitUntil</code></h3>
<p><code>waitUntil</code> is available on <code>DurableObjectState</code> for API compatibility with <a href="/workers/runtime-apis/context/#waituntil">Workers Runtime APIs</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="waituntil-has-no-effect-in-durable-objects">`waitUntil` has no effect in Durable Objects</h3>
@markup("md", "content/.markup/bodies/8328.md")
</aside>
<h4 id="parameters">Parameters</h4>
<ul>
<li>A required promise of any type.</li>
</ul>
<h4 id="return-values">Return values</h4>
<ul>
<li>None.</li>
</ul>
<h3 id="blockconcurrencywhile"><code>blockConcurrencyWhile</code></h3>
<p><code>blockConcurrencyWhile</code> executes an async callback while blocking any other events from being delivered to the Durable Object until the callback completes. This method guarantees ordering and prevents concurrent requests. All events that were not explicitly initiated as part of the callback itself will be blocked. Once the callback completes, all other events will be delivered.</p>
<ul>
<li><code>blockConcurrencyWhile</code> is commonly used within the constructor of the Durable Object class to enforce initialization to occur before any requests are delivered.</li>
<li>Another use case is executing <code>async</code> operations based on the current state of the Durable Object and using <code>blockConcurrencyWhile</code> to prevent that state from changing while yielding the event loop.</li>
<li>If the callback throws an exception, the object will be terminated and reset. This ensures that the object cannot be left stuck in an uninitialized state if something fails unexpectedly.</li>
<li>To avoid this behavior, enclose the body of your callback in a <code>try...catch</code> block to ensure it cannot throw an exception.</li>
</ul>
<p>To help mitigate deadlocks there is a 30 second timeout applied when executing the callback. If this timeout is exceeded, the Durable Object will be reset. It is best practice to have the callback do as little work as possible to improve overall request throughput to the Durable Object.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="when-to-use-blockconcurrencywhile">When to use `blockConcurrencyWhile`</h3>
@markup("md", "content/.markup/bodies/8327.md")
</aside>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8337.md")
</div></div>
<h4 id="parameters-1">Parameters</h4>
<ul>
<li>A required callback which returns a <code>Promise&lt;T&gt;</code>.</li>
</ul>
<h4 id="return-values-1">Return values</h4>
<ul>
<li>A <code>Promise&lt;T&gt;</code> returned by the callback.</li>
</ul>
<h3 id="acceptwebsocket"><code>acceptWebSocket</code></h3>
<p><code>acceptWebSocket</code> is part of the <a href="/durable-objects/best-practices/websockets/#durable-objects-hibernation-websocket-api">WebSocket Hibernation API</a>, which allows a Durable Object to be removed from memory to save costs while keeping its WebSockets connected.</p>
<p><code>acceptWebSocket</code> adds a WebSocket to the set of WebSockets attached to the Durable Object. Once called, any incoming messages will be delivered by calling the Durable Object's <code>webSocketMessage</code> handler, and <code>webSocketClose</code> will be invoked upon disconnect. After calling <code>acceptWebSocket</code>, the WebSocket is accepted and its <code>send</code> and <code>close</code> methods can be used.</p>
<p>The <a href="/durable-objects/best-practices/websockets/#durable-objects-hibernation-websocket-api">WebSocket Hibernation API</a> takes the place of the standard <a href="/workers/runtime-apis/websockets/">WebSockets API</a>. Therefore, <code>ws.accept</code> must not have been called separately and <code>ws.addEventListener</code> method will not receive events as they will instead be delivered to the Durable Object.</p>
<p>The WebSocket Hibernation API permits a maximum of 32,768 WebSocket connections per Durable Object, but the CPU and memory usage of a given workload may further limit the practical number of simultaneous connections.</p>
<h4 id="parameters-2">Parameters</h4>
<ul>
<li>A required <code>WebSocket</code> with name <code>ws</code>.</li>
<li>An optional <code>Array&lt;string&gt;</code> of associated tags. Tags can be used to retrieve WebSockets via <a href="/durable-objects/api/state/#getwebsockets"><code>DurableObjectState::getWebSockets</code></a>. Each tag is a maximum of 256 characters and there can be at most 10 tags associated with a WebSocket.</li>
</ul>
<h4 id="return-values-2">Return values</h4>
<ul>
<li>None.</li>
</ul>
<h3 id="getwebsockets"><code>getWebSockets</code></h3>
<p><code>getWebSockets</code> is part of the <a href="/durable-objects/best-practices/websockets/#durable-objects-hibernation-websocket-api">WebSocket Hibernation API</a>, which allows a Durable Object to be removed from memory to save costs while keeping its WebSockets connected.</p>
<p><code>getWebSockets</code> returns an <code>Array&lt;WebSocket&gt;</code> which is the set of WebSockets attached to the Durable Object. An optional tag argument can be used to filter the list according to tags supplied when calling <a href="/durable-objects/api/state/#acceptwebsocket"><code>DurableObjectState::acceptWebSocket</code></a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="waituntil-is-not-necessary">`waitUntil` is not necessary</h3>
@markup("md", "content/.markup/bodies/8326.md")
</aside>
<h4 id="parameters-3">Parameters</h4>
<ul>
<li>An optional tag of type <code>string</code>.</li>
</ul>
<h4 id="return-values-3">Return values</h4>
<ul>
<li>An <code>Array&lt;WebSocket&gt;</code>.</li>
</ul>
<h3 id="setwebsocketautoresponse"><code>setWebSocketAutoResponse</code></h3>
<p><code>setWebSocketAutoResponse</code> is part of the <a href="/durable-objects/best-practices/websockets/#durable-objects-hibernation-websocket-api">WebSocket Hibernation API</a>, which allows a Durable Object to be removed from memory to save costs while keeping its WebSockets connected.</p>
<p><code>setWebSocketAutoResponse</code> sets an automatic response, auto-response, for the request provided for all WebSockets attached to the Durable Object. If a request is received matching the provided request then the auto-response will be returned without waking WebSockets in hibernation and incurring billable duration charges.</p>
<p><code>setWebSocketAutoResponse</code> is a common alternative to setting up a server for static ping/pong messages because this can be handled without waking hibernating WebSockets.</p>
<h4 id="parameters-4">Parameters</h4>
<ul>
<li>An optional <code>WebSocketRequestResponsePair(request string, response string)</code> enabling any WebSocket accepted via <a href="/durable-objects/api/state/#acceptwebsocket"><code>DurableObjectState::acceptWebSocket</code></a> to automatically reply to the provided response when it receives the provided request. Both request and response are limited to 2,048 characters each. If the parameter is omitted, any previously set auto-response configuration will be removed. <a href="/durable-objects/api/state/#getwebsocketautoresponsetimestamp"><code>DurableObjectState::getWebSocketAutoResponseTimestamp</code></a> will still reflect the last timestamp that an auto-response was sent.</li>
</ul>
<h4 id="return-values-4">Return values</h4>
<ul>
<li>None.</li>
</ul>
<h3 id="getwebsocketautoresponse"><code>getWebSocketAutoResponse</code></h3>
<p><code>getWebSocketAutoResponse</code> returns the <code>WebSocketRequestResponsePair</code> object last set by <a href="/durable-objects/api/state/#setwebsocketautoresponse"><code>DurableObjectState::setWebSocketAutoResponse</code></a>, or null if not auto-response has been set.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="inspect-websocketrequestresponsepair">inspect `WebSocketRequestResponsePair`</h3>
@markup("md", "content/.markup/bodies/8325.md")
</aside>
<h4 id="parameters-5">Parameters</h4>
<ul>
<li>None.</li>
</ul>
<h4 id="return-values-5">Return values</h4>
<ul>
<li>A <code>WebSocketRequestResponsePair</code> or null.</li>
</ul>
<h3 id="getwebsocketautoresponsetimestamp"><code>getWebSocketAutoResponseTimestamp</code></h3>
<p><code>getWebSocketAutoResponseTimestamp</code> is part of the <a href="/durable-objects/best-practices/websockets/#durable-objects-hibernation-websocket-api">WebSocket Hibernation API</a>, which allows a Durable Object to be removed from memory to save costs while keeping its WebSockets connected.</p>
<p><code>getWebSocketAutoResponseTimestamp</code> gets the most recent <code>Date</code> on which the given WebSocket sent an auto-response, or null if the given WebSocket never sent an auto-response.</p>
<h4 id="parameters-6">Parameters</h4>
<ul>
<li>A required <code>WebSocket</code>.</li>
</ul>
<h4 id="return-values-6">Return values</h4>
<ul>
<li>A <code>Date</code> or null.</li>
</ul>
<h3 id="sethibernatablewebsocketeventtimeout"><code>setHibernatableWebSocketEventTimeout</code></h3>
<p><code>setHibernatableWebSocketEventTimeout</code> is part of the <a href="/durable-objects/best-practices/websockets/#durable-objects-hibernation-websocket-api">WebSocket Hibernation API</a>, which allows a Durable Object to be removed from memory to save costs while keeping its WebSockets connected.</p>
<p><code>setHibernatableWebSocketEventTimeout</code> sets the maximum amount of time in milliseconds that a WebSocket event can run for.</p>
<p>If no parameter or a parameter of <code>0</code> is provided and a timeout has been previously set, then the timeout will be unset. The maximum value of timeout is 604,800,000 ms (7 days).</p>
<h4 id="parameters-7">Parameters</h4>
<ul>
<li>An optional <code>number</code>.</li>
</ul>
<h4 id="return-values-7">Return values</h4>
<ul>
<li>None.</li>
</ul>
<h3 id="gethibernatablewebsocketeventtimeout"><code>getHibernatableWebSocketEventTimeout</code></h3>
<p><code>getHibernatableWebSocketEventTimeout</code> is part of the <a href="/durable-objects/best-practices/websockets/#durable-objects-hibernation-websocket-api">WebSocket Hibernation API</a>, which allows a Durable Object to be removed from memory to save costs while keeping its WebSockets connected.</p>
<p><code>getHibernatableWebSocketEventTimeout</code> gets the currently set hibernatable WebSocket event timeout if one has been set via <a href="/durable-objects/api/state/#sethibernatablewebsocketeventtimeout"><code>DurableObjectState::setHibernatableWebSocketEventTimeout</code></a>.</p>
<h4 id="parameters-8">Parameters</h4>
<ul>
<li>None.</li>
</ul>
<h4 id="return-values-8">Return values</h4>
<ul>
<li>A number, or null if the timeout has not been set.</li>
</ul>
<h3 id="gettags"><code>getTags</code></h3>
<p><code>getTags</code> is part of the <a href="/durable-objects/best-practices/websockets/#durable-objects-hibernation-websocket-api">WebSocket Hibernation API</a>, which allows a Durable Object to be removed from memory to save costs while keeping its WebSockets connected.</p>
<p><code>getTags</code> returns tags associated with a given WebSocket. This method throws an exception if the WebSocket has not been associated with the Durable Object via <a href="/durable-objects/api/state/#acceptwebsocket"><code>DurableObjectState::acceptWebSocket</code></a>.</p>
<h4 id="parameters-9">Parameters</h4>
<ul>
<li>A required <code>WebSocket</code>.</li>
</ul>
<h4 id="return-values-9">Return values</h4>
<ul>
<li>An <code>Array&lt;string&gt;</code> of tags.</li>
</ul>
<h3 id="abort"><code>abort</code></h3>
<p>Calling <code>abort</code> immediately resets a Durable Object. The runtime logs a JavaScript <code>Error</code> with the message passed to <code>abort</code>. Application code cannot catch this error.</p>
<p>By default, an alarm interrupted by <code>abort</code> retries after the Durable Object resets. A Durable Object can run an alarm concurrently with another request, and that request can call <code>abort</code> while the alarm is still running.</p>
<p>The default retry prevents an unrelated request from permanently canceling the alarm. Pass <code>{ retryAlarm: false }</code> on any abort call that should prevent an interrupted alarm from retrying, including abort calls outside the alarm handler.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8340.md")
</div></div>
<h4 id="parameters-10">Parameters</h4>
<ul>
<li>An optional <code>string</code> containing the error message to log.</li>
<li>An optional <code>DurableObjectAbortOptions</code> object:
<ul>
<li><code>retryAlarm</code> <span class="nb-type">boolean</span>: Controls whether an alarm interrupted by this abort retries. It defaults to <code>true</code>.</li>
</ul>
</li>
</ul>
<h4 id="return-values-10">Return values</h4>
<ul>
<li>None.</li>
</ul>
<h2 id="properties">Properties</h2>
<h3 id="id"><code>id</code></h3>
<p><code>id</code> is a readonly property of type <code>DurableObjectId</code> corresponding to the <a href="/durable-objects/api/id"><code>DurableObjectId</code></a> of the Durable Object.</p>
<h3 id="storage"><code>storage</code></h3>
<p><code>storage</code> is a readonly property of type <code>DurableObjectStorage</code> encapsulating the <a href="/durable-objects/api/sqlite-storage-api/">Storage API</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://blog.cloudflare.com/durable-objects-easy-fast-correct-choose-three/">Durable Objects: Easy, Fast, Correct - Choose Three</a>.</li>
</ul>
