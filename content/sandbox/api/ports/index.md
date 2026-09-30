<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13615.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="production-requires-custom-domain">Production requires custom domain</h3>
@markup("md", "content/.markup/bodies/13614.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prefer-sandbox-tunnels-for-public-urls">Prefer `sandbox.tunnels` for public URLs</h3>
@markup("md", "content/.markup/bodies/13613.md")
</aside>
<p>Expose services running in your sandbox via public preview URLs. See <a href="/sandbox/concepts/preview-urls/">Preview URLs concept</a> for details.</p>
<h2 id="module-functions">Module functions</h2>
<h3 id="proxytosandbox"><code>proxyToSandbox()</code></h3>
<p>Route incoming HTTP and WebSocket requests to the correct sandbox container. Call this at the top of your Worker's <code>fetch</code> handler, before any application logic, so that it intercepts and forwards preview URL requests automatically.</p>
<pre><code class="language-ts">proxyToSandbox(request: Request, env: Env): Promise&lt;Response | null&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>request</code> - The incoming <code>Request</code> object from the <code>fetch</code> handler.</li>
<li><code>env</code> - The <code>Env</code> object containing your Sandbox binding.</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;Response | null&gt;</code> — a <code>Response</code> if the request matched a preview URL and was routed to the sandbox, or <code>null</code> if the request did not match and should be handled by your application logic.</p>
<p>The function inspects the request hostname to determine whether it matches the subdomain pattern of an exposed port (for example, <code>8080-sandbox-id-token.yourdomain.com</code>). If it matches, <code>proxyToSandbox()</code> proxies the request to the correct Durable Object, and the sandbox service handles it. Both HTTP and WebSocket upgrade requests are supported.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13616.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13612.md")
</aside>
<h2 id="methods">Methods</h2>
<h3 id="exposeport"><code>exposePort()</code></h3>
<p>Expose a port and get a preview URL for accessing services running in the sandbox.</p>
<pre><code class="language-ts">const response = await sandbox.exposePort(port: number, options: ExposePortOptions): Promise&lt;ExposePortResponse&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>port</code> - Port number to expose (1024-65535)</li>
<li><code>options</code>:
<ul>
<li><code>hostname</code> - Your Worker's domain name (e.g., <code>'example.com'</code>). Required to construct preview URLs with wildcard subdomains like <code>https://8080-sandbox-abc123token.example.com</code>. Cannot be a <code>.workers.dev</code> domain as it doesn't support wildcard DNS patterns.</li>
<li><code>name</code> - Friendly name for the port (optional)</li>
<li><code>token</code> - Custom token for the preview URL (optional). Must be 1-16 characters containing only lowercase letters (a-z), numbers (0-9), hyphens (-), and underscores (_). If not provided, a random 16-character token is generated automatically.</li>
</ul>
</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;ExposePortResponse&gt;</code> with <code>port</code>, <code>url</code> (preview URL), <code>name</code></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13617.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="local-development">Local development</h3>
@markup("md", "content/.markup/bodies/13611.md")
</aside>
<h2 id="custom-tokens-for-stable-urls">Custom Tokens for Stable URLs</h2>
<p>Custom tokens enable consistent preview URLs across container restarts and deployments. This is useful for:</p>
<ul>
<li><strong>Production environments</strong> - Share stable URLs with users or teams</li>
<li><strong>Development workflows</strong> - Maintain bookmarks and integrations</li>
<li><strong>CI/CD pipelines</strong> - Reference consistent URLs in tests or deployment scripts</li>
</ul>
<p><strong>Token Requirements:</strong></p>
<ul>
<li>1-16 characters in length</li>
<li>Only lowercase letters (a-z), numbers (0-9), hyphens (-), and underscores (_)</li>
<li>Must be unique per sandbox (cannot reuse tokens across different ports)</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13618.md")
</div>
<h3 id="validateporttoken"><code>validatePortToken()</code></h3>
<p>Validate if a token is authorized to access a specific exposed port. Useful for custom authentication or routing logic.</p>
<pre><code class="language-ts">const isValid = await sandbox.validatePortToken(port: number, token: string): Promise&lt;boolean&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>port</code> - Port number to check</li>
<li><code>token</code> - Token to validate</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;boolean&gt;</code> - <code>true</code> if token is valid for the port, <code>false</code> otherwise</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13619.md")
</div>
<h3 id="unexposeport"><code>unexposePort()</code></h3>
<p>Remove an exposed port and close its preview URL.</p>
<pre><code class="language-ts">await sandbox.unexposePort(port: number): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>port</code> - Port number to unexpose</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13620.md")
</div>
<h3 id="getexposedports"><code>getExposedPorts()</code></h3>
<p>Get information about all currently exposed ports.</p>
<pre><code class="language-ts">const response = await sandbox.getExposedPorts(): Promise&lt;GetExposedPortsResponse&gt;&#10;</code></pre>
<p><strong>Returns</strong>: <code>Promise&lt;GetExposedPortsResponse&gt;</code> with <code>ports</code> array (containing <code>port</code>, <code>url</code>, <code>name</code>)</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13621.md")
</div>
<h3 id="wsconnect"><code>wsConnect()</code></h3>
<p>Connect to WebSocket servers running in the sandbox. Use this when your Worker needs to establish WebSocket connections with services in the sandbox.</p>
<p><strong>Common use cases:</strong></p>
<ul>
<li>Route incoming WebSocket upgrade requests with custom authentication or authorization</li>
<li>Connect from your Worker to get real-time data from sandbox services</li>
</ul>
<p>For exposing WebSocket services via public preview URLs, use <code>exposePort()</code> with <code>proxyToSandbox()</code> instead. See <a href="/sandbox/guides/websocket-connections/">WebSocket Connections guide</a> for examples.</p>
<pre><code class="language-ts">const response = await sandbox.wsConnect(request: Request, port: number): Promise&lt;Response&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>request</code> - Incoming WebSocket upgrade request</li>
<li><code>port</code> - Port number (1024-65535, excluding 3000)</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;Response&gt;</code> - WebSocket response establishing the connection</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13622.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/concepts/preview-urls/">Preview URLs concept</a> - How preview URLs work</li>
<li><a href="/sandbox/guides/expose-services/">Expose Services guide</a> - Full workflow for starting services, exposing ports, and routing requests</li>
<li><a href="/sandbox/guides/websocket-connections/">WebSocket Connections guide</a> - WebSocket routing via preview URLs</li>
<li><a href="/sandbox/api/commands/">Commands API</a> - Start background processes</li>
<li><a href="/sandbox/api/tunnels/">Tunnels API</a> - Zero-config <code>*.trycloudflare.com</code> URLs for quick development</li>
</ul>
<pre><code>&#10;</code></pre>
