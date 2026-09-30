<h2 id="quick-deployment">Quick deployment</h2>
<p>For quick preview deployments we recommend using <a href="https://developers.cloudflare.com/tunnel/">Cloudflare Tunnel</a> to generate preview URLs to your web services. These work across local development, workers.dev and production usage.</p>
<pre><code class="language-ts">await sandbox.startProcess(&quot;python -m http.server 8000&quot;);&#10;const tunnel = await sandbox.tunnels.get(8000);&#10;console.log(tunnel.url);&#10;// https://acute-llama-dancing-roundly.trycloudflare.app&#10;&#10;// Request will be routed directly to the webserver running on the sandbox.&#10;const req = await fetch(`${tunnel.url}/api/users`); // =&gt; GET http://localhost:8000/api/users&#10;</code></pre>
<p>Cloudflare Tunnel support currently has the following limitations:</p>
<ul>
<li>No control over generated URL.</li>
<li>No authentication mechanism beyond randomly generated URL.</li>
<li>Each URL uses an additional <code>cloudflared</code> process on the sandbox.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="production-requires-custom-domain">Production requires custom domain</h3>
@markup("md", "content/.markup/bodies/13573.md")
</aside>
<p>See the <a href="/sandbox/api/tunnels/">tunnels API reference</a> for the full API and feature set.</p>
<h2 id="production-usage-stable-urls-custom-domains">Production usage, stable URLs &amp; custom domains</h2>
<p>For production use we recommend using the <code>exposePort()</code> API and routing traffic through your worker.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="custom-domain-for-exposeport-production-urls">Custom domain for exposePort production URLs</h3>
@markup("md", "content/.markup/bodies/13572.md")
</aside>
<p>Preview URLs provide public HTTPS access to services running inside sandboxes. When you expose a port, you get a unique URL that proxies requests to your service.</p>
<pre><code class="language-typescript">// Extract hostname from request&#10;const { hostname } = new URL(request.url);&#10;&#10;await sandbox.startProcess(&quot;python -m http.server 8000&quot;);&#10;const exposed = await sandbox.exposePort(8000, { hostname });&#10;&#10;console.log(exposed.url);&#10;// Production: https://8000-sandbox-id-abc123random4567.yourdomain.com&#10;// Local dev: http://8000-sandbox-id-abc123random4567.localhost:{port}/&#10;</code></pre>
<h2 id="url-format">URL Format</h2>
<p><strong>Production</strong>: <code>https://{port}-{sandbox-id}-{token}.yourdomain.com</code></p>
<ul>
<li>With auto-generated token: <code>https://8080-abc123-random16chars12.yourdomain.com</code></li>
<li>With custom token: <code>https://8080-abc123-my_api_v1.yourdomain.com</code></li>
</ul>
<p><strong>Local development</strong>: <code>http://{port}-{sandbox-id}-{token}.localhost:{dev-server-port}</code></p>
<h2 id="token-types">Token Types</h2>
<h3 id="auto-generated-tokens-default">Auto-generated tokens (default)</h3>
<p>When no custom token is specified, a random 16-character token is generated:</p>
<pre><code class="language-typescript">const exposed = await sandbox.exposePort(8000, { hostname });&#10;// https://8000-sandbox-id-abc123random4567.yourdomain.com&#10;</code></pre>
<p>URLs with auto-generated tokens change when you unexpose and re-expose a port.</p>
<h3 id="custom-tokens-for-stable-urls">Custom tokens for stable URLs</h3>
<p>For production deployments or shared URLs, specify a custom token to maintain consistency across container restarts:</p>
<pre><code class="language-typescript">const stable = await sandbox.exposePort(8000, {&#10;	hostname,&#10;	token: &quot;api_v1&quot;,&#10;});&#10;// https://8000-sandbox-id-api_v1.yourdomain.com&#10;// Same URL every time ✓&#10;</code></pre>
<p><strong>Token requirements:</strong></p>
<ul>
<li>1-16 characters long</li>
<li>Lowercase letters (a-z), numbers (0-9), and underscores (_) only</li>
<li>Must be unique within each sandbox</li>
</ul>
<p><strong>Use cases for custom tokens:</strong></p>
<ul>
<li>Production APIs with stable endpoints</li>
<li>Sharing demo URLs with external users</li>
<li>Documentation with consistent examples</li>
<li>Integration testing with predictable URLs</li>
</ul>
<h2 id="id-case-sensitivity">ID Case Sensitivity</h2>
<p>Preview URLs extract the sandbox ID from the hostname to route requests. Since hostnames are case-insensitive (per RFC 3986), they're always lowercased: <code>8080-MyProject-123.yourdomain.com</code> becomes <code>8080-myproject-123.yourdomain.com</code>.</p>
<p><strong>The problem</strong>: If you create a sandbox with <code>&quot;MyProject-123&quot;</code>, it exists as a Durable Object with that exact ID. But the preview URL routes to <code>&quot;myproject-123&quot;</code> (lowercased from the hostname). These are different Durable Objects, so your sandbox is unreachable via preview URL.</p>
<pre><code class="language-typescript">// Problem scenario&#10;const sandbox = getSandbox(env.Sandbox, &quot;MyProject-123&quot;);&#10;// Durable Object ID: &quot;MyProject-123&quot;&#10;await sandbox.exposePort(8080, { hostname });&#10;// Preview URL: 8080-myproject-123-token123.yourdomain.com&#10;// Routes to: &quot;myproject-123&quot; (different DO - doesn&#x27;t exist!)&#10;</code></pre>
<p><strong>The solution</strong>: Use <code>normalizeId: true</code> to lowercase IDs when creating sandboxes:</p>
<pre><code class="language-typescript">const sandbox = getSandbox(env.Sandbox, &quot;MyProject-123&quot;, {&#10;	normalizeId: true,&#10;});&#10;// Durable Object ID: &quot;myproject-123&quot; (lowercased)&#10;// Preview URL: 8080-myproject-123-token123.yourdomain.com&#10;// Routes to: &quot;myproject-123&quot; (same DO - works!)&#10;</code></pre>
<p>Without <code>normalizeId: true</code>, <code>exposePort()</code> throws an error when the ID contains uppercase letters.</p>
<p><strong>Best practice</strong>: Use lowercase IDs from the start (<code>'my-project-123'</code>). See <a href="/sandbox/configuration/sandbox-options/#normalizeid">Sandbox options - normalizeId</a> for details.</p>
<h2 id="request-routing">Request Routing</h2>
<p>You must call <code>proxyToSandbox()</code> first in your Worker's fetch handler to route preview URL requests:</p>
<pre><code class="language-typescript">import { proxyToSandbox, getSandbox } from &quot;@cloudflare/sandbox&quot;;&#10;&#10;export { Sandbox } from &quot;@cloudflare/sandbox&quot;;&#10;&#10;export default {&#10;	async fetch(request, env) {&#10;		// Handle preview URL routing first&#10;		const proxyResponse = await proxyToSandbox(request, env);&#10;		if (proxyResponse) return proxyResponse;&#10;&#10;		// Your application routes&#10;		// ...&#10;	},&#10;};&#10;</code></pre>
<p>Requests flow: Browser → Your Worker → Durable Object (sandbox) → Your Service.</p>
<h2 id="multiple-ports">Multiple Ports</h2>
<p>Expose multiple services simultaneously:</p>
<pre><code class="language-typescript">// Extract hostname from request&#10;const { hostname } = new URL(request.url);&#10;&#10;await sandbox.startProcess(&quot;node api.js&quot;); // Port 3000&#10;await sandbox.startProcess(&quot;node admin.js&quot;); // Port 3001&#10;&#10;const api = await sandbox.exposePort(3000, { hostname, name: &quot;api&quot; });&#10;const admin = await sandbox.exposePort(3001, { hostname, name: &quot;admin&quot; });&#10;&#10;// Each gets its own URL with unique tokens:&#10;// https://3000-abc123-random16chars01.yourdomain.com&#10;// https://3001-abc123-random16chars02.yourdomain.com&#10;</code></pre>
<h2 id="what-works">What Works</h2>
<ul>
<li>HTTP/HTTPS requests</li>
<li>WebSocket connections</li>
<li>Server-Sent Events</li>
<li>All HTTP methods (GET, POST, PUT, DELETE, etc.)</li>
<li>Request and response headers</li>
</ul>
<h2 id="what-does-not-work">What Does Not Work</h2>
<ul>
<li>Raw TCP/UDP connections</li>
<li>Custom protocols (must wrap in HTTP)</li>
<li>Ports outside range 1024-65535</li>
<li>Port 3000 (used internally by the SDK)</li>
</ul>
<h2 id="websocket-support">WebSocket Support</h2>
<p>Preview URLs support WebSocket connections. When a WebSocket upgrade request hits an exposed port, the routing layer automatically handles the connection handshake.</p>
<pre><code class="language-typescript">// Extract hostname from request&#10;const { hostname } = new URL(request.url);&#10;&#10;// Start a WebSocket server&#10;await sandbox.startProcess(&quot;bun run ws-server.ts 8080&quot;);&#10;const { url } = await sandbox.exposePort(8080, { hostname });&#10;&#10;// Clients connect using WebSocket protocol&#10;// Browser: new WebSocket(&#x27;wss://8080-abc123-token123.yourdomain.com&#x27;)&#10;&#10;// Your Worker routes automatically&#10;export default {&#10;	async fetch(request, env) {&#10;		const proxyResponse = await proxyToSandbox(request, env);&#10;		if (proxyResponse) return proxyResponse;&#10;	},&#10;};&#10;</code></pre>
<p>For custom routing scenarios where your Worker needs to control which sandbox or port to connect to based on request properties, see <code>wsConnect()</code> in the <a href="/sandbox/api/ports/#wsconnect">Ports API</a>.</p>
<h2 id="security">Security</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13571.md")
</aside>
<p><strong>Built-in security</strong>:</p>
<ul>
<li><strong>Token-based access</strong> - Each exposed port gets a unique token in the URL (for example, <code>https://8080-sandbox-abc123token456.yourdomain.com</code>)</li>
<li><strong>HTTPS in production</strong> - All traffic is encrypted with TLS. Certificates are provisioned automatically for first-level wildcards (<code>*.yourdomain.com</code>). If your Worker runs on a subdomain, refer to the <a href="/sandbox/guides/preview-urls-custom-domain/#subdomain-depth-matters-for-tls">TLS note for custom domains</a>.</li>
<li><strong>Unpredictable URLs</strong> - Auto-generated tokens are randomly generated and difficult to guess</li>
<li><strong>Token collision prevention</strong> - Custom tokens are validated to ensure uniqueness within each sandbox</li>
</ul>
<p><strong>Add application-level authentication</strong>:</p>
<p>For additional security, implement authentication within your application:</p>
<pre><code class="language-python">from flask import Flask, request, abort&#10;&#10;app = Flask(__name__)&#10;&#10;@app.route(&#x27;/data&#x27;)&#10;def get_data():&#10;    &#35; Check for your own authentication token&#10;    auth_token = request.headers.get(&#x27;Authorization&#x27;)&#10;    if auth_token != &#x27;Bearer your-secret-token&#x27;:&#10;        abort(401)&#10;    return {&#x27;data&#x27;: &#x27;protected&#x27;}&#10;</code></pre>
<p>This adds a second layer of security on top of the URL token.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="url-not-accessible">URL Not Accessible</h3>
<p>Check if service is running and listening:</p>
<pre><code class="language-typescript">// 1. Is service running?&#10;const processes = await sandbox.listProcesses();&#10;&#10;// 2. Is port exposed?&#10;const ports = await sandbox.getExposedPorts();&#10;&#10;// 3. Is service binding to 0.0.0.0 (not 127.0.0.1)?&#10;// Good:&#10;app.run((host = &quot;0.0.0.0&quot;), (port = 3000));&#10;&#10;// Bad (localhost only):&#10;app.run((host = &quot;127.0.0.1&quot;), (port = 3000));&#10;</code></pre>
<h3 id="production-errors">Production Errors</h3>
<p>For custom domain issues, refer to <a href="/sandbox/guides/preview-urls-custom-domain/#troubleshooting">preview URL custom domain troubleshooting</a>.</p>
<h3 id="local-development">Local Development</h3>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="local-development-limitation">Local development limitation</h3>
@markup("md", "content/.markup/bodies/13570.md")
</aside>
<h2 id="related-resources">Related Resources</h2>
<ul>
<li><a href="/sandbox/guides/preview-urls-custom-domain/">Configure preview URLs on a custom domain</a> - Wildcard DNS and TLS for <code>exposePort()</code></li>
<li><a href="/sandbox/guides/deploy/">Deploy a Sandbox application</a> - Worker and container image deploys</li>
<li><a href="/sandbox/guides/expose-services/">Expose Services</a> - Practical patterns for exposing ports</li>
<li><a href="/sandbox/api/ports/">Ports API</a> - Complete API reference</li>
<li><a href="/sandbox/api/tunnels/">Tunnels API</a> - Zero-config <code>*.trycloudflare.com</code> URLs as an alternative for development</li>
<li><a href="/sandbox/concepts/security/">Security Model</a> - Security best practices</li>
</ul>
