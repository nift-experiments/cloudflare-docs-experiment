<h2 id="background">Background</h2>
<p>The <a href="https://developer.mozilla.org/en-US/docs/Web/API/EventSource"><code>EventSource</code></a> interface is a server-sent event API that allows a server to push events to a client. The <code>EventSource</code> object is used to receive server-sent events. It connects to a server over HTTP and receives events in a text-based format.</p>
<h3 id="constructor">Constructor</h3>
<pre><code class="language-js">let eventSource = new EventSource(url, options);&#10;</code></pre>
<ul>
<li><code>url</code> USVString - The URL to which to connect.</li>
<li><code>options</code> EventSourceInit - An optional dictionary containing any optional settings.</li>
</ul>
<p>By default, the <code>EventSource</code> will use the global <code>fetch()</code> function under the
covers to make requests. If you need to use a different fetch implementation as
provided by a Cloudflare Workers binding, you can pass the <code>fetcher</code> option:</p>
<pre><code class="language-js">export default {&#10;  async fetch(req, env) {&#10;    let eventSource = new EventSource(url, { fetcher: env.MYFETCHER });&#10;    // ...&#10;  }&#10;};&#10;</code></pre>
<p>Note that the <code>fetcher</code> option is a Cloudflare Workers specific extension.</p>
<h3 id="properties">Properties</h3>
<ul>
<li><code>eventSource.url</code> USVString read-only
<ul>
<li>The URL of the event source.</li>
</ul>
</li>
<li><code>eventSource.readyState</code> USVString read-only
<ul>
<li>The state of the connection.</li>
</ul>
</li>
<li><code>eventSource.withCredentials</code> Boolean read-only
<ul>
<li>A Boolean indicating whether the <code>EventSource</code> object was instantiated with cross-origin (CORS) credentials set (<code>true</code>), or not (<code>false</code>).</li>
</ul>
</li>
</ul>
<h3 id="methods">Methods</h3>
<ul>
<li><code>eventSource.close()</code>
<ul>
<li>Closes the connection.</li>
</ul>
</li>
<li><code>eventSource.onopen</code>
<ul>
<li>An event handler called when a connection is opened.</li>
</ul>
</li>
<li><code>eventSource.onmessage</code>
<ul>
<li>An event handler called when a message is received.</li>
</ul>
</li>
<li><code>eventSource.onerror</code>
<ul>
<li>An event handler called when an error occurs.</li>
</ul>
</li>
</ul>
<h3 id="events">Events</h3>
<ul>
<li><code>message</code>
<ul>
<li>Fired when a message is received.</li>
</ul>
</li>
<li><code>open</code>
<ul>
<li>Fired when the connection is opened.</li>
</ul>
</li>
<li><code>error</code>
<ul>
<li>Fired when an error occurs.</li>
</ul>
</li>
</ul>
<h3 id="class-methods">Class Methods</h3>
<ul>
<li><code>EventSource.from(readableStreamReadableStream) : EventSource</code>
<ul>
<li>This is a Cloudflare Workers specific extension that creates a new <code>EventSource</code> object from an existing <code>ReadableStream</code>. Such an instance does not initiate a new connection but instead attaches to the provided stream.</li>
</ul>
</li>
</ul>
