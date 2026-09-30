<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17130.md")
</aside>
<p>You can use <a href="https://nodejs.org/api/tls.html"><code>node:tls</code></a> to create secure connections to
external services using <a href="https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security">TLS</a> (Transport Layer Security).</p>
<pre><code class="language-js">import { connect } from &quot;node:tls&quot;;&#10;&#10;// ... in a request handler ...&#10;const connectionOptions = { key: env.KEY, cert: env.CERT };&#10;const socket = connect(url, connectionOptions, () =&gt; {&#10;	if (socket.authorized) {&#10;		console.log(&quot;Connection authorized&quot;);&#10;	}&#10;});&#10;&#10;socket.on(&quot;data&quot;, (data) =&gt; {&#10;	console.log(data);&#10;});&#10;&#10;socket.on(&quot;end&quot;, () =&gt; {&#10;	console.log(&quot;server ends connection&quot;);&#10;});&#10;</code></pre>
<p>The following APIs are available:</p>
<ul>
<li><a href="https://nodejs.org/api/tls.html#tlsconnectoptions-callback"><code>connect</code></a></li>
<li><a href="https://nodejs.org/api/tls.html#class-tlstlssocket"><code>TLSSocket</code></a></li>
<li><a href="https://nodejs.org/api/tls.html#tlscheckserveridentityhostname-cert"><code>checkServerIdentity</code></a></li>
<li><a href="https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions"><code>createSecureContext</code></a></li>
</ul>
<p>All other APIs, including <a href="https://nodejs.org/api/tls.html#class-tlsserver"><code>tls.Server</code></a> and <a href="https://nodejs.org/api/tls.html#tlscreateserveroptions-secureconnectionlistener"><code>tls.createServer</code></a>,
are not supported and will throw a <code>Not implemented</code> error when called.</p>
<p>The full <code>node:tls</code> API is documented in the <a href="https://nodejs.org/api/tls.html">Node.js documentation for <code>node:tls</code></a>.</p>
