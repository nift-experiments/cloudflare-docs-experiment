<p>This guide shows you how to work with WebSocket servers running in your sandboxes.</p>
<h2 id="choose-your-approach">Choose your approach</h2>
<p><strong>Expose via preview URL</strong> - Get a public URL for external clients to connect to. Best for public chat rooms, multiplayer games, or real-time dashboards.</p>
<p><strong>Connect with wsConnect()</strong> - Your Worker establishes the WebSocket connection. Best for custom routing logic, authentication gates, or when your Worker needs real-time data from sandbox services.</p>
<h2 id="connect-to-websocket-echo-server">Connect to WebSocket echo server</h2>
<p><strong>Create the echo server:</strong></p>
<pre><code class="language-typescript">Bun.serve({&#10;	port: 8080,&#10;	hostname: &quot;0.0.0.0&quot;,&#10;	fetch(req, server) {&#10;		if (server.upgrade(req)) {&#10;			return;&#10;		}&#10;		return new Response(&quot;WebSocket echo server&quot;);&#10;	},&#10;	websocket: {&#10;		message(ws, message) {&#10;			ws.send(`Echo: ${message}`);&#10;		},&#10;		open(ws) {&#10;			console.log(&quot;Client connected&quot;);&#10;		},&#10;		close(ws) {&#10;			console.log(&quot;Client disconnected&quot;);&#10;		},&#10;	},&#10;});&#10;&#10;console.log(&quot;WebSocket server listening on port 8080&quot;);&#10;</code></pre>
<p><strong>Extend the Dockerfile:</strong></p>
<pre><code class="language-dockerfile">FROM docker.io/cloudflare/sandbox:0.3.3&#10;&#10;&#35; Copy echo server into the container&#10;COPY echo-server.ts /workspace/echo-server.ts&#10;&#10;&#35; Create custom startup script&#10;COPY startup.sh /container-server/startup.sh&#10;RUN chmod +x /container-server/startup.sh&#10;</code></pre>
<p><strong>Create startup script:</strong></p>
<pre><code class="language-bash">&#35;!/bin/bash&#10;&#35; Start your WebSocket server in the background&#10;bun /workspace/echo-server.ts &amp;&#10;&#35; Start SDK&#x27;s control plane (needed for the SDK to work)&#10;exec bun dist/index.js&#10;</code></pre>
<p><strong>Connect from your Worker:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13348.md")
</div>
<p><strong>Client connects:</strong></p>
<pre><code class="language-javascript">const ws = new WebSocket(&#x27;wss://your-worker.com&#x27;);&#10;ws.onmessage = (event) =&gt; console.log(event.data);&#10;ws.send(&#x27;Hello!&#x27;); // Receives: &quot;Echo: Hello!&quot;&#10;</code></pre>
<h2 id="expose-websocket-service-via-preview-url">Expose WebSocket service via preview URL</h2>
<p>Get a public URL for your WebSocket server:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13349.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="alternative-quick-tunnels">Alternative: quick tunnels</h3>
@markup("md", "content/.markup/bodies/13347.md")
</aside>
<p><strong>Client connects to preview URL:</strong></p>
<pre><code class="language-javascript">// Get the preview URL&#10;const response = await fetch(&#x27;https://your-worker.com/ws-url&#x27;);&#10;const { url } = await response.json();&#10;&#10;// Connect&#10;const ws = new WebSocket(url);&#10;ws.onmessage = (event) =&gt; console.log(event.data);&#10;ws.send(&#x27;Hello!&#x27;); // Receives: &quot;Echo: Hello!&quot;&#10;</code></pre>
<h2 id="connect-from-worker-to-get-real-time-data">Connect from Worker to get real-time data</h2>
<p>Your Worker can connect to a WebSocket service to get real-time data, even when the incoming request isn't a WebSocket:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13350.md")
</div>
<p>This pattern is useful when you need streaming data from sandbox services but want to return HTTP responses to clients.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="upgrade-failed">Upgrade failed</h3>
<p>Verify request has WebSocket headers:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13351.md")
</div>
<h3 id="local-development">Local development</h3>
<p>Expose ports in Dockerfile for <code>wrangler dev</code>:</p>
<pre><code class="language-dockerfile">FROM docker.io/cloudflare/sandbox:0.3.3&#10;&#10;COPY echo-server.ts /workspace/echo-server.ts&#10;COPY startup.sh /container-server/startup.sh&#10;RUN chmod +x /container-server/startup.sh&#10;&#10;&#35; Required for local development&#10;EXPOSE 8080&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13346.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/api/ports/">Ports API reference</a> - Complete API documentation</li>
<li><a href="/sandbox/concepts/preview-urls/">Preview URLs concept</a> - How preview URLs work</li>
<li><a href="/sandbox/api/tunnels/">Tunnels API</a> - Zero-config <code>*.trycloudflare.com</code> URLs for WebSocket services in development</li>
<li><a href="/sandbox/guides/background-processes/">Background processes guide</a> - Managing long-running services</li>
</ul>
