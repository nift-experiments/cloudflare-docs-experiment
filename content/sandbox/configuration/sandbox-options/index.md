<p>Configure sandbox behavior by passing options when creating a sandbox instance with <code>getSandbox()</code>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13545.md")
</aside>
<h2 id="available-options">Available options</h2>
<pre><code class="language-ts">import { getSandbox } from &#x27;@cloudflare/sandbox&#x27;;&#10;&#10;const sandbox = getSandbox(binding, sandboxId, options?: SandboxOptions);&#10;</code></pre>
<h3 id="enabledefaultsession">enableDefaultSession</h3>
<p><strong>Type</strong>: <code>boolean</code>
<strong>Default</strong>: <code>true</code></p>
<p>Controls what happens when you call sandbox methods without an explicit <code>sessionId</code>. When <code>true</code>, implicit operations use the sandbox's default session and preserve shell state between calls. When <code>false</code>, implicit operations run in isolation and do not inherit shell state from prior calls unless you explicitly target a session.</p>
<p>Use <code>enableDefaultSession: true</code> for interactive or stateful workflows where commands should share working directory and exported variables. Use <code>enableDefaultSession: false</code> for stateless request handling where one call should not affect the next one. It is recommended to set this to <code>false</code> — default session support will be removed in a future version of the Sandbox SDK, and using <code>createSession()</code> explicitly is the preferred pattern going forward.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13546.md")
</div>
<h3 id="keepalive">keepAlive</h3>
<p><strong>Type</strong>: <code>boolean</code>
<strong>Default</strong>: <code>false</code></p>
<p>Keep the container alive indefinitely by preventing automatic shutdown. When <code>true</code>, the container automatically sends heartbeat pings every 30 seconds to prevent eviction and will never auto-timeout.</p>
<p><strong>How it works</strong>: The sandbox automatically schedules lightweight ping requests to the container every 30 seconds. This prevents the container from being evicted due to inactivity while minimizing resource overhead. You can also enable/disable keepAlive dynamically using <a href="/sandbox/api/lifecycle/#setkeepalive"><code>setKeepAlive()</code></a>.</p>
<p>The <code>keepAlive</code> flag persists across Durable Object hibernation and wakeup cycles. Once enabled, you do not need to re-set it after the sandbox wakes from hibernation.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13547.md")
</div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="resource-management-with-keepalive">Resource management with keepAlive</h3>
@markup("md", "content/.markup/bodies/13544.md")
</aside>
<h3 id="sleepafter">sleepAfter</h3>
<p><strong>Type</strong>: <code>string | number</code>
<strong>Default</strong>: <code>&quot;10m&quot;</code> (10 minutes)</p>
<p>Duration of inactivity before the sandbox automatically sleeps. Accepts duration strings (<code>&quot;30s&quot;</code>, <code>&quot;5m&quot;</code>, <code>&quot;1h&quot;</code>) or numbers (seconds).</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="bug-fix-in-v0-2-17">Bug fix in v0.2.17</h3>
@markup("md", "content/.markup/bodies/13543.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13548.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="ignored-when-keepalive-is-true">Ignored when keepAlive is true</h3>
@markup("md", "content/.markup/bodies/13542.md")
</aside>
<h3 id="containertimeouts">containerTimeouts</h3>
<p><strong>Type</strong>: <code>object</code></p>
<p>Configure timeouts for container startup operations.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13549.md")
</div>
<p><strong>Available timeout options</strong>:</p>
<ul>
<li><code>instanceGetTimeoutMS</code> - How long to wait for Cloudflare to provision a new container instance. Increase during traffic spikes when many containers provision simultaneously. <strong>Default</strong>: <code>30000</code> (30 seconds)</li>
<li><code>portReadyTimeoutMS</code> - How long to wait for the sandbox API to become ready. Increase if you extend the base Dockerfile with custom startup work (installing packages, starting services). <strong>Default</strong>: <code>90000</code> (90 seconds)</li>
</ul>
<p><strong>Environment variable overrides</strong>:</p>
<ul>
<li><code>SANDBOX_INSTANCE_TIMEOUT_MS</code> - Override <code>instanceGetTimeoutMS</code></li>
<li><code>SANDBOX_PORT_TIMEOUT_MS</code> - Override <code>portReadyTimeoutMS</code></li>
</ul>
<p>Precedence: <code>options</code> &gt; <code>env vars</code> &gt; SDK defaults</p>
<h3 id="logging">Logging</h3>
<p><strong>Type</strong>: Environment variables</p>
<p>Control SDK logging for debugging and monitoring. Set these in your Worker's <code>wrangler.jsonc</code> file.</p>
<p><strong>Available options</strong>:</p>
<ul>
<li><code>SANDBOX_LOG_LEVEL</code> - Minimum log level: <code>debug</code>, <code>info</code>, <code>warn</code>, <code>error</code>. <strong>Default</strong>: <code>info</code></li>
<li><code>SANDBOX_LOG_FORMAT</code> - Output format: <code>json</code>, <code>pretty</code>. <strong>Default</strong>: <code>json</code></li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13550.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="read-at-startup">Read at startup</h3>
@markup("md", "content/.markup/bodies/13541.md")
</aside>
<p>Use <code>debug</code> + <code>pretty</code> for local development. Use <code>info</code> or <code>warn</code> + <code>json</code> for production (structured logging).</p>
<h3 id="normalizeid">normalizeId</h3>
<p><strong>Type</strong>: <code>boolean</code>
<strong>Default</strong>: <code>false</code> (will become <code>true</code> in a future version)</p>
<p>Lowercase sandbox IDs when creating sandboxes. When <code>true</code>, the ID you provide is lowercased before creating the Durable Object (e.g., &quot;MyProject-123&quot; → &quot;myproject-123&quot;).</p>
<p><strong>Why this matters</strong>: Preview URLs extract the sandbox ID from the hostname, which is always lowercase due to DNS case-insensitivity. Without normalization, a sandbox created with &quot;MyProject-123&quot; becomes unreachable via preview URL because the URL routing looks for &quot;myproject-123&quot; (different Durable Object).</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13551.md")
</div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="different-normalizeid-values-different-sandboxes">Different normalizeId values = different sandboxes</h3>
@markup("md", "content/.markup/bodies/13540.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="future-default">Future default</h3>
@markup("md", "content/.markup/bodies/13539.md")
</aside>
<h2 id="when-to-use-normalizeid">When to use normalizeId</h2>
<p>Use <code>normalizeId: true</code> when:</p>
<ul>
<li><strong>Using preview URLs</strong> - Required for port exposure if your IDs contain uppercase letters</li>
<li><strong>New projects</strong> - Either enable this option OR use lowercase IDs from the start (both work)</li>
<li><strong>Migrating existing code</strong> - Create new sandboxes with this enabled; old uppercase sandboxes will eventually be destroyed (explicitly or after timeout)</li>
</ul>
<p><strong>Best practice</strong>: Use lowercase IDs from the start (<code>'my-project-123'</code> instead of <code>'MyProject-123'</code>).</p>
<h2 id="when-to-use-sleepafter">When to use sleepAfter</h2>
<p>Use custom <code>sleepAfter</code> values to:</p>
<ul>
<li><strong>Reduce costs</strong> - Shorter timeouts (e.g., <code>&quot;1m&quot;</code>) for infrequent workloads</li>
<li><strong>Extend availability</strong> - Longer timeouts (e.g., <code>&quot;30m&quot;</code>) for interactive workflows</li>
<li><strong>Balance performance</strong> - Fine-tune based on your application's usage patterns</li>
</ul>
<p>The default 10-minute timeout works well for most applications. Adjust based on your needs.</p>
<h2 id="when-to-use-keepalive">When to use keepAlive</h2>
<p>Use <code>keepAlive: true</code> for:</p>
<ul>
<li><strong>Long-running builds</strong> - CI/CD pipelines that may have idle periods between steps</li>
<li><strong>Batch processing</strong> - Jobs that process data in waves with gaps between batches</li>
<li><strong>Monitoring tasks</strong> - Processes that periodically check external services</li>
<li><strong>Interactive sessions</strong> - User-driven workflows where the container should remain available</li>
</ul>
<p>With <code>keepAlive</code>, containers send automatic heartbeat pings every 30 seconds to prevent eviction and never sleep automatically. Use for scenarios where you control the lifecycle explicitly.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/guides/expose-services/">Expose services guide</a> - Using <code>normalizeId</code> with preview URLs</li>
<li><a href="/sandbox/concepts/preview-urls/">Preview URLs concept</a> - Understanding DNS case-insensitivity</li>
<li><a href="/sandbox/guides/background-processes/">Background processes guide</a> - Using <code>keepAlive</code> with long-running processes</li>
<li><a href="/sandbox/api/lifecycle/">Lifecycle API</a> - Create and manage sandboxes with <code>setKeepAlive()</code></li>
<li><a href="/sandbox/concepts/sandboxes/">Sandboxes concept</a> - Understanding sandbox lifecycle</li>
</ul>
