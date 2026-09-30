<p>Create and manage sandbox containers. Get sandbox instances, configure options, and clean up resources.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13629.md")
</aside>
<h2 id="methods">Methods</h2>
<h3 id="getsandbox"><code>getSandbox()</code></h3>
<p>Get or create a sandbox instance by ID.</p>
<pre><code class="language-ts">const sandbox = getSandbox(&#10;  binding: DurableObjectNamespace&lt;Sandbox&gt;,&#10;  sandboxId: string,&#10;  options?: SandboxOptions&#10;): Sandbox&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>binding</code> - The Durable Object namespace binding from your Worker environment</li>
<li><code>sandboxId</code> - Unique identifier for this sandbox. The same ID always returns the same sandbox instance. In user-facing apps, scope IDs to a single user.</li>
<li><code>options</code> (optional) - See <a href="/sandbox/configuration/sandbox-options/">SandboxOptions</a> for all available options:
<ul>
<li><code>enableDefaultSession</code> - Use the default session for operations without an explicit <code>sessionId</code>. Set to <code>false</code> to evaluate each call in isolation (default: <code>true</code>)</li>
<li><code>sleepAfter</code> - Duration of inactivity before automatic sleep (default: <code>&quot;10m&quot;</code>)</li>
<li><code>keepAlive</code> - Prevent automatic sleep entirely. Persists across hibernation (default: <code>false</code>)</li>
<li><code>containerTimeouts</code> - Configure container startup timeouts</li>
<li><code>normalizeId</code> - Lowercase sandbox IDs for preview URL compatibility (default: <code>false</code>)</li>
</ul>
</li>
</ul>
<p><strong>Returns</strong>: <code>Sandbox</code> instance</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13628.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="implicit-execution-mode">Implicit execution mode</h3>
@markup("md", "content/.markup/bodies/13627.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13630.md")
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13626.md")
</aside>
<hr />
<h3 id="setkeepalive"><code>setKeepAlive()</code></h3>
<p>Enable or disable keepAlive mode dynamically after sandbox creation.</p>
<pre><code class="language-ts">await sandbox.setKeepAlive(keepAlive: boolean): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>keepAlive</code> - <code>true</code> to prevent automatic sleep, <code>false</code> to allow normal sleep behavior</li>
</ul>
<p>When enabled, the sandbox automatically sends heartbeat pings every 30 seconds to prevent container eviction. When disabled, the sandbox returns to normal sleep behavior based on the <code>sleepAfter</code> configuration.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13631.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="heartbeat-mechanism">Heartbeat mechanism</h3>
@markup("md", "content/.markup/bodies/13625.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="resource-management">Resource management</h3>
@markup("md", "content/.markup/bodies/13624.md")
</aside>
<hr />
<h3 id="destroy"><code>destroy()</code></h3>
<p>Destroy the sandbox container and free up resources.</p>
<pre><code class="language-ts">await sandbox.destroy(): Promise&lt;void&gt;&#10;</code></pre>
<p>Immediately terminates the container and permanently deletes all state:</p>
<ul>
<li>All files in <code>/workspace</code>, <code>/tmp</code>, and <code>/home</code></li>
<li>All running processes</li>
<li>All sessions (including the default session)</li>
<li>Network connections and exposed ports</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13632.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13623.md")
</aside>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/concepts/sandboxes/">Sandbox lifecycle concept</a> - Understanding container lifecycle and state</li>
<li><a href="/sandbox/configuration/sandbox-options/">Sandbox options configuration</a> - Configure <code>keepAlive</code> and other options</li>
<li><a href="/sandbox/api/sessions/">Sessions API</a> - Create execution contexts within a sandbox</li>
</ul>
