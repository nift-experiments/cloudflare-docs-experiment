<p>The Workers runtime provides the <code>connect()</code> API for creating outbound <a href="https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/">TCP connections</a> from Workers.</p>
<p>Many application-layer protocols are built on top of the Transmission Control Protocol (TCP). These application-layer protocols, including SSH, MQTT, SMTP, FTP, IRC, and most database wire protocols including MySQL, PostgreSQL, MongoDB, require an underlying TCP socket API in order to work.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16129.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16128.md")
</aside>
<h2 id="connect"><code>connect()</code></h2>
<p>The <code>connect()</code> function returns a TCP socket, with both a <a href="/workers/runtime-apis/streams/readablestream/">readable</a> and <a href="/workers/runtime-apis/streams/writablestream/">writable</a> stream of data. This allows you to read and write data on an ongoing basis, as long as the connection remains open.</p>
<p><code>connect()</code> is provided as a <a href="/workers/runtime-apis/">Runtime API</a>, and is accessed by importing the <code>connect</code> function from <code>cloudflare:sockets</code>. This process is similar to how one imports built-in modules in Node.js. Refer to the following codeblock for an example of creating a TCP socket, writing to it, and returning the readable side of the socket as a response:</p>
<pre><code class="language-typescript">import { connect } from &#x27;cloudflare:sockets&#x27;;&#10;&#10;export default {&#10;  async fetch(req): Promise&lt;Response&gt; {&#10;    const gopherAddr = { hostname: &quot;gopher.floodgap.com&quot;, port: 70 };&#10;    const url = new URL(req.url);&#10;&#10;    try {&#10;      const socket = connect(gopherAddr);&#10;&#10;      const writer = socket.writable.getWriter()&#10;      const encoder = new TextEncoder();&#10;      const encoded = encoder.encode(url.pathname + &quot;\r\n&quot;);&#10;      await writer.write(encoded);&#10;      await writer.close();&#10;&#10;      return new Response(socket.readable, { headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; } });&#10;    } catch (error) {&#10;      return new Response(&quot;Socket connection failed: &quot; + error, { status: 500 });&#10;    }&#10;  }&#10;} satisfies ExportedHandler;&#10;</code></pre>
<ul>
<li><code>connect(address: SocketAddress | string, options?: optional SocketOptions)</code> : <code>Socket</code>
<ul>
<li><code>connect()</code> accepts either a URL string or <a href="/workers/runtime-apis/tcp-sockets/#socketaddress"><code>SocketAddress</code></a> to define the hostname and port number to connect to, and an optional configuration object, <a href="/workers/runtime-apis/tcp-sockets/#socketoptions"><code>SocketOptions</code></a>. It returns an instance of a <a href="/workers/runtime-apis/tcp-sockets/#socket"><code>Socket</code></a>.</li>
</ul>
</li>
</ul>
<h3 id="socketaddress"><code>SocketAddress</code></h3>
<ul>
<li>
<p><code>hostname</code> string</p>
<ul>
<li>The hostname to connect to. Example: <code>cloudflare.com</code>.</li>
</ul>
</li>
<li>
<p><code>port</code> number</p>
<ul>
<li>The port number to connect to. Example: <code>5432</code>.</li>
</ul>
</li>
</ul>
<h3 id="socketoptions"><code>SocketOptions</code></h3>
<ul>
<li>
<p><code>secureTransport</code> &quot;off&quot; | &quot;on&quot; | &quot;starttls&quot; — Defaults to <code>off</code></p>
<ul>
<li>Specifies whether or not to use <a href="https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/">TLS</a> when creating the TCP socket.</li>
<li><code>off</code> — Do not use TLS.</li>
<li><code>on</code> — Use TLS.</li>
<li><code>starttls</code> — Do not use TLS initially, but allow the socket to be upgraded to use TLS by calling <a href="/workers/runtime-apis/tcp-sockets/#opportunistic-tls-starttls"><code>startTls()</code></a>.</li>
</ul>
</li>
<li>
<p><code>allowHalfOpen</code> boolean — Defaults to <code>false</code></p>
<ul>
<li>Defines whether the writable side of the TCP socket will automatically close on end-of-file (EOF). When set to <code>false</code>, the writable side of the TCP socket will automatically close on EOF. When set to <code>true</code>, the writable side of the TCP socket will remain open on EOF.</li>
<li>This option is similar to that offered by the Node.js <a href="https://nodejs.org/api/net.html"><code>net</code> module</a> and allows interoperability with code which utilizes it.</li>
</ul>
</li>
</ul>
<h3 id="socketinfo"><code>SocketInfo</code></h3>
<ul>
<li>
<p><code>remoteAddress</code> string | null</p>
<ul>
<li>The address of the remote peer the socket is connected to. May not always be set.</li>
</ul>
</li>
<li>
<p><code>localAddress</code> string | null</p>
<ul>
<li>The address of the local network endpoint for this socket. May not always be set.</li>
</ul>
</li>
</ul>
<h3 id="socket"><code>Socket</code></h3>
<ul>
<li>
<p><code>readable</code> : ReadableStream</p>
<ul>
<li>Returns the readable side of the TCP socket.</li>
</ul>
</li>
<li>
<p><code>writable</code> : WritableStream</p>
<ul>
<li>Returns the writable side of the TCP socket.</li>
<li>The <code>WritableStream</code> returned only accepts chunks of <code>Uint8Array</code> or its views.</li>
</ul>
</li>
<li>
<p><code>opened</code> <code>Promise&lt;SocketInfo&gt;</code></p>
<ul>
<li>This promise is resolved when the socket connection is established and is rejected if the socket encounters an error.</li>
</ul>
</li>
<li>
<p><code>closed</code> <code>Promise&lt;void&gt;</code></p>
<ul>
<li>This promise is resolved when the socket is closed and is rejected if the socket encounters an error.</li>
</ul>
</li>
<li>
<p><code>close()</code> <code>Promise&lt;void&gt;</code></p>
<ul>
<li>Closes the TCP socket. Both the readable and writable streams are forcibly closed.</li>
</ul>
</li>
<li>
<p><code>startTls()</code> : Socket</p>
<ul>
<li>Upgrades an insecure socket to a secure one that uses TLS, returning a new <a href="/workers/runtime-apis/tcp-sockets#socket">Socket</a>. Note that in order to call <code>startTls()</code>, you must set <a href="/workers/runtime-apis/tcp-sockets/#socketoptions"><code>secureTransport</code></a> to <code>starttls</code> when initially calling <code>connect()</code> to create the socket.</li>
</ul>
</li>
</ul>
<h2 id="opportunistic-tls-starttls">Opportunistic TLS (StartTLS)</h2>
<p>Many TCP-based systems, including databases and email servers, require that clients use opportunistic TLS (otherwise known as <a href="https://en.wikipedia.org/wiki/Opportunistic_TLS">StartTLS</a>) when connecting. In this pattern, the client first creates an insecure TCP socket, without TLS, and then upgrades it to a secure TCP socket, that uses TLS. The <code>connect()</code> API simplifies this by providing a method, <code>startTls()</code>, which returns a new <code>Socket</code> instance that uses TLS:</p>
<pre><code class="language-typescript">import { connect } from &quot;cloudflare:sockets&quot;&#10;&#10;const address = {&#10;  hostname: &quot;example-postgres-db.com&quot;,&#10;  port: 5432&#10;};&#10;const socket = connect(address, { secureTransport: &quot;starttls&quot; });&#10;const secureSocket = socket.startTls();&#10;</code></pre>
<ul>
<li><code>startTls()</code> can only be called if <code>secureTransport</code> is set to <code>starttls</code> when creating the initial TCP socket.</li>
<li>Once <code>startTls()</code> is called, the initial socket is closed and can no longer be read from or written to. In the example above, anytime after <code>startTls()</code> is called, you would use the newly created <code>secureSocket</code>. Any existing readers and writers based off the original socket will no longer work. You must create new readers and writers from the newly created <code>secureSocket</code>.</li>
<li><code>startTls()</code> should only be called once on an existing socket.</li>
</ul>
<h2 id="handle-errors">Handle errors</h2>
<p>To handle errors when creating a new TCP socket, reading from a socket, or writing to a socket, wrap these calls inside <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch"><code>try...catch</code></a> statement blocks. The following example opens a connection to Google.com, initiates a HTTP request, and returns the response. If this fails and throws an exception, it returns a <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-500/"><code>500</code></a> response:</p>
<pre><code class="language-typescript">import { connect } from &#x27;cloudflare:sockets&#x27;;&#10;const connectionUrl = { hostname: &quot;google.com&quot;, port: 80 };&#10;export interface Env { }&#10;export default {&#10;  async fetch(req, env, ctx): Promise&lt;Response&gt; {&#10;    try {&#10;      const socket = connect(connectionUrl);&#10;      const writer = socket.writable.getWriter();&#10;      const encoder = new TextEncoder();&#10;      const encoded = encoder.encode(&quot;GET / HTTP/1.0\r\n\r\n&quot;);&#10;      await writer.write(encoded);&#10;      await writer.close();&#10;&#10;      return new Response(socket.readable, { headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; } });&#10;    } catch (error) {&#10;      return new Response(`Socket connection failed: ${error}`, { status: 500 });&#10;    }&#10;  }&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h2 id="close-tcp-connections">Close TCP connections</h2>
<p>You can close a TCP connection by calling <code>close()</code> on the socket. This will close both the readable and writable sides of the socket.</p>
<pre><code class="language-typescript">import { connect } from &quot;cloudflare:sockets&quot;&#10;&#10;const socket = connect({ hostname: &quot;my-url.com&quot;, port: 70 });&#10;const reader = socket.readable.getReader();&#10;socket.close();&#10;&#10;// After close() is called, you can no longer read from the readable side of the socket&#10;const reader = socket.readable.getReader(); // This fails&#10;</code></pre>
<h2 id="considerations">Considerations</h2>
<ul>
<li>Outbound TCP sockets to <a href="https://www.cloudflare.com/ips/">Cloudflare IP ranges</a> are blocked.</li>
<li>TCP sockets cannot be created in global scope and shared across requests. You should always create TCP sockets within a handler (ex: <a href="/workers/get-started/guide/#3-write-code"><code>fetch()</code></a>, <a href="/workers/runtime-apis/handlers/scheduled/"><code>scheduled()</code></a>, <a href="/queues/configuration/javascript-apis/#consumer"><code>queue()</code></a>) or <a href="/durable-objects/api/alarms/"><code>alarm()</code></a>.</li>
<li>Each open TCP socket counts towards the maximum number of <a href="/workers/platform/limits/#simultaneous-open-connections">open connections</a> that can be simultaneously open.</li>
<li>When created from within a Durable Object, an open TCP socket keeps the Durable Object in memory and causes it to incur duration charges for up to 15 minutes per connection. After 15 minutes, the socket stops keeping the Durable Object alive (the socket itself continues operating) and the <a href="/durable-objects/concepts/durable-object-lifecycle/">standard eviction rules</a> resume.</li>
<li>By default, Workers cannot create outbound TCP connections on port <code>25</code> to send email to SMTP mail servers. <a href="/email-service/api/route-emails/">Cloudflare Email Workers</a> provides APIs to process and forward email.</li>
<li>Support for handling inbound TCP connections is <a href="https://blog.cloudflare.com/workers-tcp-socket-api-connect-databases/">coming soon</a>. Currently, it is not possible to make an inbound TCP connection to your Worker, for example, by using the <code>CONNECT</code> HTTP method.</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>Review descriptions of common error messages you may see when working with TCP Sockets, what the error messages mean, and how to solve them.</p>
<h3 id="proxy-request-failed-cannot-connect-to-the-specified-address"><code>proxy request failed, cannot connect to the specified address</code></h3>
<p>Your socket is connecting to an address that was disallowed. Examples of a disallowed address include Cloudflare IPs, <code>localhost</code>, and private network IPs.</p>
<p>If you need to connect to addresses on port <code>80</code> or <code>443</code> to make HTTP requests, use <a href="/workers/runtime-apis/fetch/"><code>fetch</code></a>.</p>
<h3 id="tcp-loop-detected"><code>TCP Loop detected</code></h3>
<p>Your socket is connecting back to the Worker that initiated the outbound connection. In other words, the Worker is connecting back to itself. This is currently not supported.</p>
<h3 id="connections-to-port-25-are-prohibited"><code>Connections to port 25 are prohibited</code></h3>
<p>Your socket is connecting to an address on port <code>25</code>. This is usually the port used for SMTP mail servers. Workers cannot create outbound connections on port <code>25</code>. Consider using <a href="/email-service/api/route-emails/email-handler/">Cloudflare Email Workers</a> instead.</p>
