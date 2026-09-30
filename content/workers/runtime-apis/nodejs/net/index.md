<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17141.md")
</aside>
<p>You can use <a href="https://nodejs.org/api/net.html"><code>node:net</code></a> to create a direct connection to servers via a TCP sockets
with <a href="https://nodejs.org/api/net.html#class-netsocket"><code>net.Socket</code></a>.</p>
<p>These functions use <a href="/workers/runtime-apis/tcp-sockets/#connect"><code>connect</code></a> functionality from the built-in <code>cloudflare:sockets</code> module.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17142.md")
</div>
<p>Additionally, other APIs such as <a href="https://nodejs.org/api/net.html#class-netblocklist"><code>net.BlockList</code></a>
and <a href="https://nodejs.org/api/net.html#class-netsocketaddress"><code>net.SocketAddress</code></a> are available.</p>
<p>Note that the <a href="https://nodejs.org/api/net.html#class-netserver"><code>net.Server</code></a> class is not supported by Workers.</p>
<p>The full <code>node:net</code> API is documented in the <a href="https://nodejs.org/api/net.html">Node.js documentation for <code>node:net</code></a>.</p>
<pre><code>&#10;</code></pre>
