<p>Some method names are reserved or have special semantics.</p>
<h2 id="special-methods">Special Methods</h2>
<p>For backwards compatibility, when extending <code>WorkerEntrypoint</code> or <code>DurableObject</code>, the following method names have special semantics. Note that this does <em>not</em> apply to <code>RpcTarget</code>. On <code>RpcTarget</code>, these methods work like any other RPC method.</p>
<h3 id="fetch"><code>fetch()</code></h3>
<p>The <code>fetch()</code> method is treated specially — it can only be used to handle an HTTP request — equivalent to the <a href="/workers/runtime-apis/handlers/fetch/">fetch handler</a>.</p>
<p>You may implement a <code>fetch()</code> method in your class that extends <code>WorkerEntrypoint</code> — but it must accept only one parameter of type <a href="https://developer.mozilla.org/en-US/docs/Web/API/Request"><code>Request</code></a>, and must return an instance of <a href="https://developer.mozilla.org/en-US/docs/Web/API/Response"><code>Response</code></a>, or a <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise">Promise</a> of one.</p>
<p>On the client side, <code>fetch()</code> called on a service binding or Durable Object stub works like the standard global <code>fetch()</code>. That is, the caller may pass one or two parameters to <code>fetch()</code>. If the caller does not simply pass a single <code>Request</code> object, then a new <code>Request</code> is implicitly constructed, passing the parameters to its constructor, and that request is what is actually sent to the server.</p>
<p>Some properties of <code>Request</code> control the behavior of <code>fetch()</code> on the client side and are not actually sent to the server. For example, the property <code>redirect: &quot;auto&quot;</code> (which is the default) instructs <code>fetch()</code> that if the server returns a redirect response, it should automatically be followed, resulting in an HTTP request to the public internet. Again, this behavior is according to the Fetch API standard. In short, <code>fetch()</code> doesn't have RPC semantics, it has Fetch API semantics.</p>
<h3 id="connect"><code>connect()</code></h3>
<p>The <code>connect()</code> method of the <code>WorkerEntrypoint</code> class is reserved for opening a socket-like connection to your Worker. This is currently not implemented or supported — though you can <a href="/workers/runtime-apis/tcp-sockets/">open a TCP socket from a Worker</a> or connect directly to databases over a TCP socket with <a href="/hyperdrive/get-started/">Hyperdrive</a>.</p>
<h2 id="disallowed-method-names">Disallowed Method Names</h2>
<p>The following method (or property) names may not be used as RPC methods on any RPC type (including <code>WorkerEntrypoint</code>, <code>DurableObject</code>, and <code>RpcTarget</code>):</p>
<ul>
<li><code>dup</code>: This is reserved for duplicating a stub. Refer to the <a href="/workers/runtime-apis/rpc/lifecycle">RPC Lifecycle</a> docs to learn more about <code>dup()</code>.</li>
<li><code>constructor</code>: This name has special meaning for JavaScript classes. It is not intended to be called as a method, so it is not allowed over RPC.</li>
</ul>
<p>The following methods are disallowed only on <code>WorkerEntrypoint</code> and <code>DurableObject</code>, but allowed on <code>RpcTarget</code>. These methods have historically had special meaning to Durable Objects, where they are used to handle certain system-generated events.</p>
<ul>
<li><code>alarm</code></li>
<li><code>webSocketMessage</code></li>
<li><code>webSocketClose</code></li>
<li><code>webSocketError</code></li>
</ul>
