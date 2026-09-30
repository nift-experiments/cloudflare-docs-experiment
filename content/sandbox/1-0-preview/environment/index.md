<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13753.md")
</aside>
<p>Each <code>exec()</code> and <code>createTerminal()</code> starts an independent process. Shell <code>export</code> in one process does not apply to the next launch. Configure process environment with the container image, <code>setEnvVars</code>, and per-launch <code>env</code>.</p>
<p>Use environment variables for <strong>non-secret</strong> configuration (paths, feature flags, <code>NODE_ENV</code>, and similar). Do not put live API keys or other long-lived credentials into the sandbox. To call external services that need credentials, use <a href="/sandbox/guides/outbound-traffic/">outbound traffic handlers</a> so secrets stay in the Worker.</p>
<h2 id="how-a-process-gets-its-environment">How a process gets its environment</h2>
<p>When a process starts, the runtime builds its environment from:</p>
<ol>
<li>The <strong>container</strong> environment (image <code>ENV</code> and defaults).</li>
<li>Names from <strong><code>setEnvVars</code></strong>, when you use <code>exec()</code> (described in the next section).</li>
<li>The <strong><code>env</code> option</strong> on that launch, if you pass one.</li>
</ol>
<p>Later launches do not keep overlays from earlier launches. A command that runs <code>export FOO=bar</code> inside one process does not change the next <code>exec()</code>.</p>
<p>Worker bindings in your <code>fetch</code> handler are not process environment variables. Only values you pass through <code>setEnvVars</code> or launch <code>env</code> appear inside the process (and those should not be long-lived secrets).</p>
<h2 id="setenvvars"><code>setEnvVars()</code></h2>
<pre><code class="language-ts">setEnvVars(envVars: Record&lt;string, string | undefined&gt;): Promise&lt;void&gt;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Value</th>
<th>Effect</th>
</tr>
</thead>
<tbody>
<tr>
<td>string</td>
<td>Set this environment variable for later <code>exec()</code> launches</td>
</tr>
<tr>
<td><code>undefined</code></td>
<td>Remove a previously stored variable</td>
</tr>
</tbody>
</table>
<p>On each <code>exec()</code>, the SDK merges stored names into that process’s environment at launch.</p>
<p>Stored names live in the sandbox Durable Object’s memory. They are not written to the container filesystem and are not part of a backup. After the Durable Object is evicted or replaced, call <code>setEnvVars</code> again if you still need those names, or pass <code>env</code> on each <code>exec()</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13754.md")
</div>
<h2 id="env-on-exec"><code>env</code> on <code>exec()</code></h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13755.md")
</div>
<table>
<thead>
<tr>
<th>Behavior</th>
<th>Detail</th>
</tr>
</thead>
<tbody>
<tr>
<td>Scope</td>
<td>This launch only</td>
</tr>
<tr>
<td>Merge order</td>
<td>Container environment, then <code>setEnvVars</code>, then this <code>env</code></td>
</tr>
<tr>
<td>Side effects</td>
<td>Does not update <code>setEnvVars</code> storage</td>
</tr>
</tbody>
</table>
<p>Omit <code>env</code> when sandbox-wide names (and the container environment) are enough.</p>
<h2 id="env-on-createterminal"><code>env</code> on <code>createTerminal()</code></h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13756.md")
</div>
<p>The terminal’s launch <code>env</code> overlays the container environment for that terminal only. Pass the names the terminal needs on <code>createTerminal</code>.</p>
<p>Inside an interactive shell, <code>export</code> applies for the life of that terminal. It does not apply to later <code>exec()</code> calls. Refer to <a href="/sandbox/1-0-preview/terminals/">Terminals</a>.</p>
<h2 id="external-apis-and-credentials">External APIs and credentials</h2>
<p>Code inside the sandbox should not hold live provider credentials. Keep secrets in the Worker and intercept outbound HTTP(S) with <code>outboundByHost</code> (and related policy such as <code>enableInternet</code> / <code>allowedHosts</code>). The sandbox can send ordinary requests—or placeholders client libraries require—while the Worker attaches real credentials before the request leaves your account.</p>
<p>Refer to <a href="/sandbox/guides/outbound-traffic/">Handle outbound traffic</a>, including securely injecting credentials. For Workers bindings (KV, R2, and similar) reached by hostname from the sandbox, refer to <a href="/sandbox/guides/workers-connections/">Connect to Workers bindings</a>.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/guides/outbound-traffic/">Handle outbound traffic</a></li>
<li><a href="/sandbox/guides/workers-connections/">Connect to Workers bindings</a></li>
<li><a href="/sandbox/1-0-preview/processes/">Process execution</a></li>
<li><a href="/sandbox/1-0-preview/api/processes/">Processes API</a></li>
<li><a href="/sandbox/1-0-preview/terminals/">Terminals</a></li>
<li><a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a></li>
</ul>
