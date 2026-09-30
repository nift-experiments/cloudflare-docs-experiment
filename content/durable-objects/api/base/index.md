<p>The <code>DurableObject</code> base class is an abstract class which all Durable Objects inherit from. This base class provides a set of optional methods, frequently referred to as handler methods, which can respond to events, for example a <code>webSocketMessage</code> when using the <a href="/durable-objects/best-practices/websockets/#durable-objects-hibernation-websocket-api">WebSocket Hibernation API</a>. To provide a concrete example, here is a Durable Object <code>MyDurableObject</code> which extends <code>DurableObject</code> and implements the fetch handler to return &quot;Hello, World!&quot; to the calling Worker.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8407.md")
</div></div>
<h2 id="methods">Methods</h2>
<h3 id="fetch"><code>fetch</code></h3>
<ul>
<li><code>fetch(request <span class="nb-type">Request</span>)</code>
: <span class="nb-type">Response</span> | <span class="nb-type">Promise&lt;Response&gt;</span>- Takes an HTTP
<a href="https://developers.cloudflare.com/workers/runtime-apis/request/">Request</a> and
returns an HTTP
<a href="https://developers.cloudflare.com/workers/runtime-apis/response/">Response</a>.
This method allows the Durable Object to emulate an HTTP server where a Worker
with a binding to that object is the client. - This method can be <code>async</code>.
<ul>
<li>Durable Objects support <a href="/durable-objects/best-practices/create-durable-object-stubs-and-send-requests/">RPC calls</a> as of compatibility date <a href="/workers/configuration/compatibility-flags/#durable-object-stubs-and-service-bindings-support-rpc">2024-04-03</a>. RPC methods are preferred over <code>fetch()</code> when your application does not follow HTTP request/response flow.</li>
</ul>
</li>
</ul>
<h4 id="parameters">Parameters</h4>
<ul>
<li><code>request</code> <span class="nb-type">Request</span> - the incoming HTTP request object.</li>
</ul>
<h4 id="return-values">Return values</h4>
<ul>
<li>A <span class="nb-type">Response</span> or <span class="nb-type">Promise&lt;Response&gt;</span>.</li>
</ul>
<h4 id="example">Example</h4>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8410.md")
</div></div>
<h3 id="alarm"><code>alarm</code></h3>
<ul>
<li><code>alarm(alarmInfo? <span class="nb-type">AlarmInvocationInfo</span>)</code>
: <span class="nb-type">void</span> | <span class="nb-type">Promise&lt;void&gt;</span>
<ul>
<li>Called by the system when a scheduled alarm time is reached.</li>
<li>The <code>alarm()</code> handler has guaranteed at-least-once execution and will be retried upon failure using exponential backoff, starting at two second delays for up to six retries. Retries will be performed if the method fails with an uncaught exception.</li>
<li>This method can be <code>async</code>.</li>
<li>Refer to <a href="/durable-objects/api/alarms/">Alarms</a> for more information.</li>
</ul>
</li>
</ul>
<h4 id="parameters-1">Parameters</h4>
<ul>
<li><code>alarmInfo</code> <span class="nb-type">AlarmInvocationInfo</span> (optional) - an object containing retry information:
<ul>
<li><code>retryCount</code> <span class="nb-type">number</span> - the number of times this alarm event has been retried.</li>
<li><code>isRetry</code> <span class="nb-type">boolean</span> - <code>true</code> if this alarm event is a retry, <code>false</code> otherwise.</li>
</ul>
</li>
</ul>
<h4 id="return-values-1">Return values</h4>
<ul>
<li>None.</li>
</ul>
<h4 id="example-1">Example</h4>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8413.md")
</div></div>
<h3 id="websocketmessage"><code>webSocketMessage</code></h3>
<ul>
<li><code>webSocketMessage(ws <span class="nb-type">WebSocket</span>, message <span class="nb-type">string | ArrayBuffer</span>)</code>
: <span class="nb-type">void</span> | <span class="nb-type">Promise&lt;void&gt;</span>- Called by the system
when an accepted WebSocket receives a message. - This method is not called for
WebSocket control frames. The system will respond to an incoming <a href="https://www.rfc-editor.org/rfc/rfc6455#section-5.5.2">WebSocket
protocol ping</a>
automatically without interrupting hibernation.
<ul>
<li>This method can be <code>async</code>.</li>
</ul>
</li>
</ul>
<h4 id="parameters-2">Parameters</h4>
<ul>
<li><code>ws</code> <span class="nb-type">WebSocket</span> - the <a href="https://developer.mozilla.org/en-US/docs/Web/API/WebSocket">WebSocket</a> that received the message. Use this reference to send responses or access serialized attachments.</li>
<li><code>message</code> <span class="nb-type">string | ArrayBuffer</span> - the message data. Text messages arrive as <code>string</code>, binary messages as <code>ArrayBuffer</code>.</li>
</ul>
<h4 id="return-values-2">Return values</h4>
<ul>
<li>None.</li>
</ul>
<h4 id="example-2">Example</h4>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8416.md")
</div></div>
<h3 id="websocketclose"><code>webSocketClose</code></h3>
<ul>
<li><code>webSocketClose(ws <span class="nb-type">WebSocket</span>, code <span class="nb-type">number</span>, reason <span class="nb-type">string</span>, wasClean <span class="nb-type">boolean</span>)</code>
: <span class="nb-type">void</span> | <span class="nb-type">Promise&lt;void&gt;</span>- Called by the system
when a WebSocket connection is closed.
<ul>
<li>With the <a href="/workers/configuration/compatibility-flags/#websocket-auto-reply-to-close"><code>web_socket_auto_reply_to_close</code></a> compatibility flag (enabled by default on compatibility dates on or after <code>2026-04-07</code>), the runtime automatically sends a reciprocal Close frame and transitions <code>readyState</code> to <code>CLOSED</code> before this handler is called. You do not need to call <code>ws.close()</code> — but doing so is safe (the call is silently ignored).</li>
<li>On older compatibility dates (before <code>2026-04-07</code>), you <strong>must</strong> call <code>ws.close(code, reason)</code> inside this handler to complete the WebSocket close handshake. Failing to reciprocate the close will result in <code>1006</code> errors on the client, representing an abnormal closure per the WebSocket specification.</li>
<li>This method can be <code>async</code>.</li>
</ul>
</li>
</ul>
<h4 id="parameters-3">Parameters</h4>
<ul>
<li><code>ws</code> <span class="nb-type">WebSocket</span> - the <a href="https://developer.mozilla.org/en-US/docs/Web/API/WebSocket">WebSocket</a> that was closed.</li>
<li><code>code</code> <span class="nb-type">number</span> - the <a href="https://developer.mozilla.org/en-US/docs/Web/API/CloseEvent/code">WebSocket close code</a> sent by the peer (e.g., <code>1000</code> for normal closure, <code>1001</code> for going away).</li>
<li><code>reason</code> <span class="nb-type">string</span> - a string indicating why the connection was closed. May be empty.</li>
<li><code>wasClean</code> <span class="nb-type">boolean</span> - <code>true</code> if the connection closed cleanly with a proper closing handshake, <code>false</code> otherwise.</li>
</ul>
<h4 id="return-values-3">Return values</h4>
<ul>
<li>None.</li>
</ul>
<h4 id="example-3">Example</h4>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8419.md")
</div></div>
<h3 id="websocketerror"><code>webSocketError</code></h3>
<ul>
<li><code>webSocketError(ws <span class="nb-type">WebSocket</span>, error <span class="nb-type">unknown</span>)</code>
: <span class="nb-type">void</span> | <span class="nb-type">Promise&lt;void&gt;</span>- Called by the system
when a non-disconnection error occurs on a WebSocket connection. - This method
can be <code>async</code>.</li>
</ul>
<h4 id="parameters-4">Parameters</h4>
<ul>
<li><code>ws</code> <span class="nb-type">WebSocket</span> - the <a href="https://developer.mozilla.org/en-US/docs/Web/API/WebSocket">WebSocket</a> that encountered an error.</li>
<li><code>error</code> <span class="nb-type">unknown</span> - the error that occurred. May be an <code>Error</code> object or another type depending on the error source.</li>
</ul>
<h4 id="return-values-4">Return values</h4>
<ul>
<li>None.</li>
</ul>
<h4 id="example-4">Example</h4>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8422.md")
</div></div>
<h2 id="properties">Properties</h2>
<h3 id="ctx"><code>ctx</code></h3>
<p><code>ctx</code> is a readonly property of type <a href="/durable-objects/api/state/"><code>DurableObjectState</code></a> providing access to storage, WebSocket management, and other instance-specific functionality.</p>
<h3 id="env"><code>env</code></h3>
<p><code>env</code> contains the environment bindings available to this Durable Object, as defined in your Wrangler configuration.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/durable-objects/best-practices/websockets/">Use WebSockets</a> for WebSocket handler best practices.</li>
<li><a href="/durable-objects/api/alarms/">Alarms API</a> for scheduling future work.</li>
<li><a href="/durable-objects/best-practices/create-durable-object-stubs-and-send-requests/">RPC methods</a> for type-safe method calls.</li>
</ul>
