<ul>
<li><a href="/workers/runtime-apis/websockets">WebSockets Reference</a></li>
<li><a href="/workers/examples/websockets/">Using WebSockets</a></li>
</ul>
<h2 id="server">Server</h2>
<p>Miniflare will always upgrade Web Socket connections. The Worker must respond
with a status <code>101 Switching Protocols</code> response including a <code>webSocket</code>. For
example, the Worker below implements an echo WebSocket server:</p>
<pre><code class="language-js">export default {&#10;	fetch(request) {&#10;		const [client, server] = Object.values(new WebSocketPair());&#10;&#10;		server.accept();&#10;		server.addEventListener(&quot;message&quot;, (event) =&gt; {&#10;			server.send(event.data);&#10;		});&#10;&#10;		return new Response(null, {&#10;			status: 101,&#10;			webSocket: client,&#10;		});&#10;	},&#10;};&#10;</code></pre>
<p>When using <code>dispatchFetch</code>, you are responsible for handling WebSockets by using
the <code>webSocket</code> property on <code>Response</code>. As an example, if the above worker
script was stored in <code>echo.mjs</code>:</p>
<pre><code class="language-js">import { Miniflare } from &quot;miniflare&quot;;&#10;&#10;const mf = new Miniflare({&#10;	modules: true,&#10;	scriptPath: &quot;echo.mjs&quot;,&#10;});&#10;&#10;const res = await mf.dispatchFetch(&quot;https://example.com&quot;, {&#10;	headers: {&#10;		Upgrade: &quot;websocket&quot;,&#10;	},&#10;});&#10;const webSocket = res.webSocket;&#10;webSocket.accept();&#10;webSocket.addEventListener(&quot;message&quot;, (event) =&gt; {&#10;	console.log(event.data);&#10;});&#10;&#10;webSocket.send(&quot;Hello!&quot;); // Above listener logs &quot;Hello!&quot;&#10;</code></pre>
