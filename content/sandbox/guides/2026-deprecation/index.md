<aside class="nb-aside note">
<h3 class="nb-aside-title" id="two-different-migration-paths">Two different migration paths</h3>
@markup("md", "content/.markup/bodies/13519.md")
</aside>
<p>This guide walks through migrating away from Sandbox SDK features deprecated in the <a href="/changelog/sandbox/2026-06-09-deprecating-sandbox-sdk-features/">deprecation announcement</a>. Do not build new work on these APIs. Finish this cleanup on the stable package, then move to the <a href="/sandbox/1-0-preview/">1.0 preview</a> when you can.</p>
<p>For the announcement and rationale, refer to the <a href="/changelog/sandbox/2026-06-09-deprecating-sandbox-sdk-features/">deprecation changelog entry</a>.</p>
<h2 id="before-you-migrate">Before you migrate</h2>
<p>Update to the latest Sandbox SDK release before changing transport or session configuration. If your project uses a version earlier than <code>0.9.1</code>, deploy a newer <code>@cloudflare/sandbox</code> package and container image before switching to RPC transport. Session isolation with <code>enableDefaultSession: false</code> requires Sandbox SDK <code>0.10.3</code> or newer — on <code>0.9.1</code>–<code>0.10.2</code>, upgrade first, then set the flag.</p>
<p>Search your codebase for deprecated configuration and APIs:</p>
<pre><code class="language-sh">rg &#x27;SANDBOX_TRANSPORT|transport:|exposePort\(|enableDefaultSession|execStream\(|readFileStream|writeFileStream&#x27;&#10;</code></pre>
<p>Also review any code that uses stream-specific file helpers or depends on shell state carrying across separate <code>exec()</code> calls.</p>
<h2 id="http-and-websocket-transports">HTTP and WebSocket transports</h2>
<p>HTTP and WebSocket transports are deprecated. Switch to the RPC transport.</p>
<p>To configure RPC transport for every sandbox in your Worker, set <code>SANDBOX_TRANSPORT</code> in your Worker's configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13520.md")
</div>
<p>To configure RPC transport for a specific sandbox, pass <code>transport: &quot;rpc&quot;</code> to <code>getSandbox()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13521.md")
</div>
<p>For more information, refer to <a href="/sandbox/configuration/transport/">Transport modes</a>.</p>
<h2 id="desktop">Desktop</h2>
<p>The desktop feature was removed in <code>0.10.2</code>. The feature ran a full Linux desktop inside the sandbox for computer-use style automation. If you still need that shape, rebuild it with <a href="/sandbox/1-0-preview/extensions/">extensions</a> rather than a built-in desktop API. Keep Sandbox SDK for isolated command execution, file operations, and runtime workflows that do not require an in-sandbox desktop.</p>
<h2 id="expose-ports">Expose ports</h2>
<p>Replace <code>exposePort()</code> with the tunnels API for public URLs. The tunnels API requires RPC transport.</p>
<p>Use quick tunnels for development, demos, and short-lived URLs. Use named tunnels for production traffic, webhook receivers, OAuth callbacks, and stable hostnames on a zone you control.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13522.md")
</div>
<p>If your <code>exposePort()</code> flow used <code>proxyToSandbox()</code> to inject authentication or rewrite responses, account for that behavior before moving the public URL to a tunnel.</p>
<p>For more information, refer to <a href="/sandbox/api/tunnels/">Tunnels</a> and <a href="/sandbox/guides/expose-services/">Expose services</a>.</p>
<h2 id="default-sessions">Default sessions</h2>
<p>Set <code>enableDefaultSession: false</code> on <code>getSandbox()</code>. Operations without an explicit session will then run in isolation and will not inherit shell state from earlier calls.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13523.md")
</div>
<p>If your code expects commands like <code>cd /workspace/app</code> to affect later <code>exec()</code> calls, create an explicit session and run related commands through that session:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13524.md")
</div>
<p>For one-off commands, pass <code>cwd</code> or <code>env</code> directly to <code>exec()</code> instead of relying on persisted shell state:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13525.md")
</div>
<p>For more information, refer to <a href="/sandbox/configuration/sandbox-options/#enabledefaultsession">Sandbox options</a> and <a href="/sandbox/api/sessions/">Sessions</a>.</p>
<h2 id="streaming-apis">Streaming APIs</h2>
<p>The Sandbox SDK is consolidating separate streaming APIs into the base <code>exec()</code>, <code>readFile()</code>, and <code>writeFile()</code> methods. Audit code that depends on stream-specific helpers and move to the base APIs where they support streaming behavior.</p>
<p>For command output, use <code>exec()</code> with streaming callbacks:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13526.md")
</div>
<p>For large or binary files, use the base file APIs with RPC transport. Pass a <code>ReadableStream</code> to <code>writeFile()</code>, or read a file as a stream with <code>encoding: &quot;none&quot;</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13527.md")
</div>
<p>For more information, refer to <a href="/sandbox/api/commands/">Commands</a> and <a href="/sandbox/api/files/">Files</a>.</p>
<h2 id="verify-the-migration">Verify the migration</h2>
<p>Use this checklist before you depend on a Sandbox SDK release that has removed the deprecated APIs:</p>
<ul>
<li>RPC transport is configured with <code>SANDBOX_TRANSPORT=rpc</code> or <code>transport: &quot;rpc&quot;</code>.</li>
<li>No <code>websocket</code> or <code>http</code> transport configuration remains.</li>
<li>No <code>exposePort()</code> usage remains in the migrated path.</li>
<li><code>enableDefaultSession</code> is set to <code>false</code>.</li>
<li>Stateful command workflows use <code>sandbox.createSession()</code>.</li>
<li>One-off commands pass <code>cwd</code> and <code>env</code> directly.</li>
<li>Streaming file and command code uses the base APIs.</li>
<li>Your Worker has been deployed and smoke-tested.</li>
</ul>
<h2 id="coding-agents">Coding agents</h2>
<p>Coding agents with <a href="https://github.com/cloudflare/skills">Cloudflare Skills</a> installed (<a href="/agent-setup/">Agent setup</a>) should use <strong><code>sandbox-stable</code></strong> for work on the current stable package and follow <strong>this guide</strong> for deprecated-API cleanup while staying on stable. For a full move to Sandbox SDK 1.0 (<code>@next</code>), use <strong><code>sandbox-migrate-to-next</code></strong> (and the <a href="/sandbox/1-0-preview/migrate/">1.0 migrate guide</a>) instead.</p>
<h2 id="1-0-preview">1.0 preview</h2>
<p>After you finish the stable-line changes in this guide, move on to the <strong>Sandbox SDK 1.0</strong> preview on <code>@cloudflare/sandbox@next</code> when you can. That preview is the path to the next stable major release.</p>
<p>Refer to <a href="/sandbox/1-0-preview/">Sandbox SDK 1.0 preview</a> and <a href="/sandbox/1-0-preview/migrate/">Migrate to the 1.0 preview</a>.</p>
