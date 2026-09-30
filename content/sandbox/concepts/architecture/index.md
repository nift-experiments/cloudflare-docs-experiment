<p>Sandbox SDK lets you execute untrusted code safely from your Workers. It combines three Cloudflare technologies to provide secure, stateful, and isolated execution:</p>
<ul>
<li><strong>Workers</strong> - Your application logic that calls the Sandbox SDK</li>
<li><strong>Durable Objects</strong> - Persistent sandbox instances with unique identities</li>
<li><strong>Containers</strong> - Isolated Linux environments where code actually runs</li>
</ul>
<h2 id="architecture-overview">Architecture overview</h2>
<pre><code class="language-mermaid">flowchart TB&#10;    accTitle: Sandbox SDK Architecture&#10;    accDescr: Three-layer architecture showing how Cloudflare Sandbox SDK combines Workers, Durable Objects, and Containers for secure code execution&#10;&#10;    subgraph UserSpace[&quot;&lt;b&gt;Your Worker&lt;/b&gt;&quot;]&#10;        Worker[&quot;Application code using the methods exposed by the Sandbox SDK&quot;]&#10;    end&#10;&#10;    subgraph SDKSpace[&quot;&lt;b&gt;Sandbox SDK Implementation&lt;/b&gt;&quot;]&#10;        DO[&quot;Sandbox Durable Object routes requests &amp; maintains state&quot;]&#10;        Container[&quot;Isolated Ubuntu container executes untrusted code safely&quot;]&#10;&#10;        DO --&gt;|HTTP API| Container&#10;    end&#10;&#10;    Worker --&gt;|RPC call via the Durable Object stub returned by `getSandbox`| DO&#10;&#10;    style UserSpace fill:#fff8f0,stroke:#f6821f,stroke-width:2px&#10;    style SDKSpace fill:#f5f5f5,stroke:#666,stroke-width:2px,stroke-dasharray: 5 5&#10;    style Worker fill:#ffe8d1,stroke:#f6821f,stroke-width:2px&#10;    style DO fill:#dce9f7,stroke:#1d8cf8,stroke-width:2px&#10;    style Container fill:#d4f4e2,stroke:#17b26a,stroke-width:2px&#10;</code></pre>
<h3 id="layer-1-client-sdk">Layer 1: Client SDK</h3>
<p>The developer-facing API you use in your Workers:</p>
<pre><code class="language-typescript">import { getSandbox } from &quot;@cloudflare/sandbox&quot;;&#10;&#10;const sandbox = getSandbox(env.Sandbox, &quot;my-sandbox&quot;);&#10;const result = await sandbox.exec(&quot;python script.py&quot;);&#10;</code></pre>
<p><strong>Purpose</strong>: Provide a clean, type-safe TypeScript interface for all sandbox operations.</p>
<h3 id="layer-2-durable-object">Layer 2: Durable Object</h3>
<p>Manages sandbox lifecycle and routing:</p>
<pre><code class="language-typescript">export class Sandbox extends DurableObject&lt;Env&gt; {&#10;	// Extends Cloudflare Container for isolation&#10;	// Routes requests between client and container&#10;	// Manages preview URLs and state&#10;}&#10;</code></pre>
<p><strong>Purpose</strong>: Provide persistent, stateful sandbox instances with unique identities.</p>
<p><strong>Why Durable Objects</strong>:</p>
<ul>
<li><strong>Persistent identity</strong> - Same sandbox ID always routes to same instance</li>
<li><strong>Container management</strong> - Durable Object owns and manages the container lifecycle</li>
<li><strong>Geographic distribution</strong> - Sandboxes run close to users</li>
<li><strong>Automatic scaling</strong> - Cloudflare manages provisioning</li>
</ul>
<h3 id="layer-3-container-runtime">Layer 3: Container Runtime</h3>
<p>Executes code in isolation with full Linux capabilities.</p>
<p><strong>Purpose</strong>: Safely execute untrusted code.</p>
<p><strong>Why containers</strong>:</p>
<ul>
<li><strong>VM-based isolation</strong> - Each sandbox runs in its own VM</li>
<li><strong>Full environment</strong> - Ubuntu Linux with Python, Node.js, Git, etc.</li>
</ul>
<h2 id="communication-transports">Communication transports</h2>
<p>The SDK supports three transport protocols for communication between the Durable Object and container:</p>
<h3 id="http-transport-default">HTTP transport (default)</h3>
<p>Each SDK method makes a separate HTTP request to the container API. Simple, reliable, and works for most use cases.</p>
<pre><code class="language-typescript">// Default behavior - uses HTTP&#10;const sandbox = getSandbox(env.Sandbox, &quot;my-sandbox&quot;);&#10;await sandbox.exec(&quot;python script.py&quot;);&#10;</code></pre>
<h3 id="rpc-transport">RPC transport</h3>
<p>Multiplexes all SDK calls over a single persistent connection. It avoids <a href="/workers/platform/limits/#subrequests">subrequest limits</a> when making many concurrent operations.</p>
<p>Enable RPC transport by setting the <code>SANDBOX_TRANSPORT</code> variable in your Worker's configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13576.md")
</div>
<h3 id="websocket-transport">WebSocket transport</h3>
<p>WebSocket transport is deprecated. Use RPC transport for new applications.</p>
<p>The transport layer is transparent to your application code — all SDK methods work identically regardless of transport. For details on when to use each transport and configuration examples, refer to <a href="/sandbox/configuration/transport/">Transport modes</a>.</p>
<h2 id="request-flow">Request flow</h2>
<p>When you execute a command:</p>
<pre><code class="language-typescript">await sandbox.exec(&quot;python script.py&quot;);&#10;</code></pre>
<p><strong>HTTP transport flow</strong>:</p>
<ol>
<li><strong>Client SDK</strong> validates parameters and sends HTTP request to Durable Object</li>
<li><strong>Durable Object</strong> authenticates and forwards HTTP request to container</li>
<li><strong>Container Runtime</strong> validates inputs, executes command, captures output</li>
<li><strong>Response flows back</strong> through all layers with proper error transformation</li>
</ol>
<p><strong>RPC transport flow</strong>:</p>
<ol>
<li><strong>Client SDK</strong> validates parameters and sends the request to the Durable Object</li>
<li><strong>Durable Object</strong> maintains the persistent connection to the container and multiplexes concurrent requests</li>
<li><strong>Container Runtime</strong> adapts RPC messages to HTTP-style request and response handling</li>
<li><strong>Response flows back</strong> over the same connection with proper error transformation</li>
</ol>
<p>The Durable Object establishes the persistent connection to the container on first SDK call and reuses it for all subsequent operations, reducing overhead for high-frequency operations.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/concepts/sandboxes/">Sandbox lifecycle</a> - How sandboxes are created and managed</li>
<li><a href="/sandbox/concepts/containers/">Container runtime</a> - Inside the execution environment</li>
<li><a href="/sandbox/concepts/security/">Security model</a> - How isolation and validation work</li>
<li><a href="/sandbox/concepts/sessions/">Session management</a> - Advanced state management</li>
</ul>
