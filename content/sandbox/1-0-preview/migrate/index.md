---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/1-0-preview/migrate/
  description: Update an existing Sandbox SDK application from the stable package to @cloudflare/sandbox@next.
  full_title: Migrate · Cloudflare Sandbox SDK docs
  head_html: <title>Migrate · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Update an existing Sandbox SDK application from the stable package to @cloudflare/sandbox@next."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/1-0-preview/migrate/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/1-0-preview/migrate/index.md"><meta property="og:title" content="Migrate · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Update an existing Sandbox SDK application from the stable package to @cloudflare/sandbox@next."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/1-0-preview/migrate/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/1-0-preview/migrate/#page","headline":"Migrate \u00b7 Cloudflare Sandbox SDK docs","description":"Update an existing Sandbox SDK application from the stable package to @cloudflare/sandbox@next.","url":"https://developers.cloudflare.com/sandbox/1-0-preview/migrate/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/1-0-preview/migrate/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13719.md")
</aside>
<h2 id="before-you-start">Before you start</h2>
<ol>
<li>Work on a branch or staging deployment. Finish the code migration steps in this guide, then cut production over in one deploy.</li>
<li>Expect a short cutover window. Live processes, terminals, and other container work stop when the new image replaces the old one.</li>
<li>Inventory call sites in the Worker:
<ul>
<li>Commands: <code>exec</code>, <code>execStream</code>, <code>startProcess</code>, string kill signals, process stdin</li>
<li>Sessions and transport: <code>createSession</code>, <code>enableDefaultSession</code>, <code>SANDBOX_TRANSPORT</code>, <code>setTransport</code></li>
<li>Terminals: <code>sandbox.terminal</code>, session <code>terminal()</code>, xterm <code>sessionId</code></li>
<li>Interpreter: <code>createCodeContext</code> / <code>runCode</code> on bare <code>Sandbox</code></li>
<li>Git: <code>gitCheckout</code></li>
</ul>
</li>
</ol>
<p>If you still need stable-line cleanup first (RPC transport, <code>exposePort</code>, stream helpers), complete the <a href="/sandbox/guides/2026-deprecation/">2026 deprecation migration</a>, then return here.</p>
<h2 id="what-you-will-change">What you will change</h2>
<table>
<thead>
<tr>
<th>Stable surface</th>
<th>Preview action</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>SANDBOX_TRANSPORT</code>, <code>transport</code> on <code>getSandbox()</code>, <code>setTransport()</code></td>
<td>Remove. The preview uses RPC automatically; no transport setting.</td>
</tr>
<tr>
<td><code>await sandbox.exec(string)</code> → buffered result</td>
<td><code>await sandbox.exec(argv)</code> then <code>await process.output(...)</code>.</td>
</tr>
<tr>
<td><code>execStream</code>, <code>startProcess</code>, process log helpers</td>
<td>Process handle: <code>logs</code>, <code>kill</code>, <code>waitFor*</code>.</td>
</tr>
<tr>
<td>Default session / <code>enableDefaultSession</code></td>
<td>Gone. Each <code>exec</code> is independent.</td>
</tr>
<tr>
<td><code>createSession</code> / <code>ExecutionSession</code></td>
<td>Gone from the core public surface. Pass <code>cwd</code>/<code>env</code> per <code>exec</code>, or one shell argv script.</td>
</tr>
<tr>
<td>Interpreter methods on <code>Sandbox</code></td>
<td>Same method names on <code>sandbox.interpreter</code> after <code>withInterpreter</code>. <code>runCode</code> returns plain <code>ExecutionResult</code>. Refer to <a href="/sandbox/1-0-preview/interpreter/">Code interpreter</a>.</td>
</tr>
<tr>
<td>String kill signals</td>
<td>Numeric signals on <code>process.kill</code>.</td>
</tr>
<tr>
<td><code>waitForPort</code> default mode</td>
<td>Preview default is <strong><code>tcp</code></strong>. Pass <code>mode: &quot;http&quot;</code> for HTTP checks.</td>
</tr>
<tr>
<td>Process / stream <strong>stdin</strong></td>
<td>No process stdin on the handle. Non-interactive: argv/<code>cwd</code>/<code>env</code>. Interactive PTY: <a href="/sandbox/1-0-preview/terminals/">terminals</a>.</td>
</tr>
<tr>
<td><code>sandbox.terminal(request)</code> / session <code>terminal()</code></td>
<td><code>createTerminal</code>, then <code>terminal.connect(request)</code>.</td>
</tr>
<tr>
<td>xterm <code>sessionId</code></td>
<td><code>terminalId</code> (and optional <code>cursor</code>).</td>
</tr>
<tr>
<td><code>sandbox.gitCheckout(...)</code></td>
<td>Removed. Run <code>git</code> with argv <code>exec</code>, for example <code>['git', 'clone', '--', url, dir]</code>, then <code>output()</code> / waits as needed.</td>
</tr>
</tbody>
</table>
<p>Files, mounts, backups, ports, tunnels, <code>proxyToSandbox</code>, and most lifecycle options stay available. Use the main Sandbox docs for those signatures. Where a stable page still describes sessions, transport selection, string <code>exec</code> helpers, or <code>sandbox.terminal</code>, follow this preview section instead.</p>
<h2 id="install-the-preview-package-and-image">Install the preview package and image</h2>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Confirm the lockfile resolves <code>@cloudflare/sandbox</code> to a preview build. Point your Dockerfile at the matching preview image, for example <code>cloudflare/sandbox:next</code> (or the <code>-python</code> / other variant you use).</p>
<p>Do not mix a preview Worker package with a stable container image, or the reverse. Both sides must come from the same <code>@next</code> line.</p>
<h2 id="remove-transport-selection">Remove transport selection</h2>
<p>Delete <code>SANDBOX_TRANSPORT</code>, the <code>transport</code> option on <code>getSandbox()</code>, <code>SandboxTransport</code> types, and <code>sandbox.setTransport()</code>. No replacement setting is required.</p>
<h2 id="migrate-command-execution">Migrate command execution</h2>
<h3 id="buffered-commands">Buffered commands</h3>
<p>Stable:</p>
<pre tabindex="0"><code class="language-txt">const result = await sandbox.exec(&quot;npm test&quot;);&#10;console.log(result.stdout, result.exitCode);&#10;</code></pre>
<p>Preview:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13720.md")
</div>
<p>Rules:</p>
<ul>
<li><code>await sandbox.exec(...)</code> means <strong>launch succeeded</strong>, not <strong>command finished</strong>.</li>
<li>Prefer argv without a shell when you run a single binary: <code>['npm', 'test']</code> with <code>cwd</code> set.</li>
<li><code>output()</code> defaults to <strong>byte</strong> streams (<code>Uint8Array</code>). Pass <code>{ encoding: &quot;utf8&quot; }</code> for strings.</li>
<li>There is no <code>sandbox.run()</code> compatibility helper on the current preview tip.</li>
</ul>
<h3 id="background-processes-and-streaming">Background processes and streaming</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13721.md")
</div>
<p>Process handle details (waits, log events, <code>kill</code>, no stdin): <a href="/sandbox/1-0-preview/api/processes/">Processes API</a>.</p>
<p>Across Worker requests, keep <code>server.id</code> and resume with <code>getProcess(id)</code> only while that process may still be running in the current container. If the container stopped, <code>getProcess</code> may return <code>null</code>. If you still hold a handle from a previous container, expect a stale-handle error. In both cases, start a new <code>exec</code> from the work you still need to run. Refer to <a href="/sandbox/1-0-preview/processes/#how-long-a-process-lives">How long a process lives</a>.</p>
<h3 id="working-directory-and-environment">Working directory and environment</h3>
<table>
<thead>
<tr>
<th>Stable</th>
<th>Preview</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>exec(&quot;cd /app&quot;); exec(&quot;npm test&quot;);</code></td>
<td><code>exec(['/bin/bash', '-lc', 'cd /app &amp;&amp; npm test'])</code> or <code>exec(['npm', 'test'], { cwd: '/app' })</code></td>
</tr>
<tr>
<td>Exported vars in the default session</td>
<td><code>setEnvVars</code> and/or <code>env</code> on each <code>exec</code></td>
</tr>
<tr>
<td><code>createSession({ env })</code></td>
<td><code>setEnvVars</code> and/or <code>env</code> on each <code>exec</code> / <code>createTerminal</code></td>
</tr>
</tbody>
</table>
<p>Details: <a href="/sandbox/1-0-preview/environment/">Environment variables</a>.</p>
<p>Do not put live API keys or long-lived provider credentials into <code>setEnvVars</code> or launch <code>env</code>. Keep secrets in the Worker and inject them with <a href="/sandbox/guides/outbound-traffic/">outbound traffic</a> handlers when the process must call an external API.</p>
<h3 id="timeouts-and-cancellation">Timeouts and cancellation</h3>
<table>
<thead>
<tr>
<th>Goal</th>
<th>API</th>
</tr>
</thead>
<tbody>
<tr>
<td>Limit process lifetime</td>
<td><code>exec(argv, { timeout })</code> — may finish with <code>timedOut: true</code></td>
</tr>
<tr>
<td>Limit how long you wait</td>
<td>Options or <code>AbortSignal</code> on <code>output</code> / waits / <code>logs</code> — does <strong>not</strong> kill the process</td>
</tr>
</tbody>
</table>
<h2 id="drop-session-apis">Drop session APIs</h2>
<p>Remove <code>createSession</code>, <code>getSession</code>, <code>deleteSession</code>, and <code>sessionId</code> options on core calls.</p>
<p>User isolation remains <strong>one sandbox per user</strong> (or per trust boundary), not sessions inside one sandbox.</p>
<h2 id="attach-the-interpreter">Attach the interpreter</h2>
<p>Refer to <a href="/sandbox/1-0-preview/interpreter/">Code interpreter</a>. Minimum:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13722.md")
</div>
<p>Use the <strong><code>-python</code></strong> image variant when you run Python. Keep the Worker package and container image on the same <code>@next</code> line.</p>
<h2 id="git">Git</h2>
<p><code>sandbox.gitCheckout</code> is removed. Clone or fetch with argv <code>exec</code>, for example:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13723.md")
</div>
<h2 id="terminals">Terminals</h2>
<p>Replace stable <code>sandbox.terminal(request)</code> (and session-scoped <code>terminal()</code>) with the preview terminal resource API:</p>
<ol>
<li><code>const terminal = await sandbox.createTerminal({ command: ['bash'], ... })</code></li>
<li>Store <code>terminal.id</code> with the sandbox id.</li>
<li>On WebSocket upgrade: <code>getTerminal(id)</code> then <code>terminal.connect(request, { cursor?, cols?, rows? })</code>.</li>
<li>In the browser, <code>@cloudflare/sandbox/xterm</code> uses <code>terminalId</code>.</li>
</ol>
<p>Details: <a href="/sandbox/1-0-preview/terminals/">Terminals</a>, <a href="/sandbox/1-0-preview/api/terminals/">Terminals API</a>.</p>
<h2 id="self-deployed-bridge">Self-deployed bridge</h2>
<p>This guide covers Worker SDK applications on <code>@next</code>.</p>
<p>The self-deployed <a href="/sandbox/bridge/">Sandbox bridge</a> stays on the stable release line. Keep its Worker package, container image, and HTTP clients on matching stable versions. Do not pair a bridge deployment with <code>@cloudflare/sandbox@next</code>.</p>
<h2 id="handle-lifecycle-the-preview-way">Handle lifecycle the preview way</h2>
<p>On <code>@next</code>, a <strong>sandbox ID</strong> stays stable, but the <strong>container</strong> behind it can be replaced. Processes and terminals live only in the current container. After replacement, old handles fail and you start the work again.</p>
<p>That is normal after idle time, restarts, and this migration cutover. Full model: <a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a> and <a href="/sandbox/1-0-preview/processes/#how-long-a-process-lives">How long a process lives</a>. Recovery patterns: <a href="/sandbox/1-0-preview/errors/">Errors and recovery</a>. Catalog: <a href="/sandbox/1-0-preview/api/errors/">Errors API</a>.</p>
<p>When you migrate long-running work:</p>
<ol>
<li>Do not treat a stored <code>process.id</code> or <code>terminal.id</code> as enough to resume after an arbitrary delay or after deploy.</li>
<li>Persist the command, <code>cwd</code>, <code>env</code>, and any app checkpoint you need to relaunch.</li>
<li>On a later request, call <code>getProcess(id)</code> / <code>getTerminal(id)</code> only if that resource might still be running in the current container. If you get <code>null</code> or a stale-handle error, start again from the stored work.</li>
</ol>
<p>Handle at least these errors as follows:</p>
<table>
<thead>
<tr>
<th>Error</th>
<th>What to do</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ContainerUnavailableError</code></td>
<td>Container did not start the work — back off (<code>retryAfterMs</code> when set), then try the work again</td>
</tr>
<tr>
<td><code>StaleProcessHandleError</code> / <code>StaleTerminalHandleError</code></td>
<td>Previous container — start again from stored work state</td>
</tr>
<tr>
<td><code>OperationInterruptedError</code></td>
<td>Work may have started — read <code>reason</code> / <code>retryable</code>; check state before repeating</td>
</tr>
<tr>
<td><code>RPCTransportError</code></td>
<td>Lost contact during the call — a later call may work; this call may already have run</td>
</tr>
<tr>
<td><code>ProcessWaitTimeoutError</code> / <code>ProcessAbortedError</code></td>
<td>Wait ended only — process may still be running</td>
</tr>
<tr>
<td><code>RuntimeControlProtocolError</code> or unusable image after deploy</td>
<td>Worker package and container image must match on the same <code>@next</code> line; do not treat as a slow start</td>
</tr>
</tbody>
</table>
<p><code>getProcess</code> / <code>getTerminal</code> / <code>list*</code> do not start a container. They return <code>null</code> or <code>[]</code> when none is running (not an exception).</p>
<h2 id="deploy-the-cutover">Deploy the cutover</h2>
<p>Finish the code migration steps in this guide on a branch first. Production cutover is one deploy of the preview Worker package and the matching container image.</p>
<p>Stable Sandbox and <code>@next</code> use different control protocols. A mixed pair does not work in either direction: new Worker code against an old container image fails, and old Worker code against a new container image fails.</p>
<p>On a normal <code>wrangler deploy</code>, Worker code becomes active immediately while container instances can still update gradually. That leaves a window where new Worker code can reach old containers. For this migration, roll containers out in one step:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy --containers-rollout=immediate&#10;</code></pre>
<p><code>--containers-rollout=immediate</code> does not override <a href="/workers/wrangler/configuration/#containers"><code>rollout_active_grace_period</code></a>. Leave that setting at its default of <code>0</code> for the cutover (or set it to <code>0</code> if you raised it earlier). A nonzero grace period keeps active old containers eligible longer while the new Worker is already live.</p>
<p>Before production:</p>
<ol>
<li>Finish or stop work you need to keep through the cutover.</li>
<li>Deploy with the immediate container rollout command from the previous section.</li>
<li>Wait until the new container image is serving traffic.</li>
<li>Treat process and terminal IDs from before the deploy as invalid. Start that work again and keep the new IDs.</li>
<li>Run the checks in <a href="#verify">Verify</a>.</li>
</ol>
<p>For routine deploys after migration, refer to <a href="/sandbox/guides/deploy/">Deploy a Sandbox application</a>. For rollout options, refer to <a href="/containers/configuration/rollouts/">Rollouts</a>.</p>
<h2 id="verify">Verify</h2>
<ol>
<li>Confirm the lockfile and Dockerfile are both on the same <code>@next</code> line, then deploy with <code>--containers-rollout=immediate</code>.</li>
<li>Run one argv <code>exec</code> and <code>output({ encoding: &quot;utf8&quot; })</code>.</li>
<li>Run one long-lived process with <code>waitForPort</code> or <code>logs</code>.</li>
<li>If the app uses a browser terminal: create, connect, and resume with <code>getTerminal</code> while the container still has it.</li>
<li>Exercise the interpreter only if your app uses that extension (Python needs <code>-python</code>).</li>
<li>Confirm error handling distinguishes unavailable, interrupted/RPC, stale handle, and local wait timeouts — <a href="/sandbox/1-0-preview/errors/">Errors and recovery</a>.</li>
<li>Confirm secrets are not stored in sandbox env. Use outbound handlers where needed.</li>
<li>Grep again for removed APIs (transport, sessions, <code>execStream</code>, <code>startProcess</code>, <code>sandbox.terminal</code>, <code>gitCheckout</code>, xterm <code>sessionId</code>).</li>
</ol>
<h2 id="coding-agents">Coding agents</h2>
<p>Install <a href="https://github.com/cloudflare/skills">Cloudflare Skills</a> for your agent (<a href="/agent-setup/">Agent setup</a>). The <strong><code>sandbox-migrate-to-next</code></strong> skill performs this migration. For new apps on <code>@next</code>, use <strong><code>sandbox-next</code></strong>. For day-to-day work on the current stable package, use <strong><code>sandbox-stable</code></strong>. Deprecated-API cleanup while staying on stable is in the <a href="/sandbox/guides/2026-deprecation/">2026 deprecation guide</a> (and <strong><code>sandbox-stable</code></strong>) before or instead of this guide.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/1-0-preview/">1.0 preview overview</a></li>
<li><a href="/sandbox/1-0-preview/get-started/">Get started</a></li>
<li><a href="/sandbox/1-0-preview/environment/">Environment variables</a></li>
<li><a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a></li>
<li><a href="/sandbox/1-0-preview/processes/">Process execution</a> (including <a href="/sandbox/1-0-preview/processes/#how-long-a-process-lives">how long a process lives</a>)</li>
<li><a href="/sandbox/1-0-preview/api/processes/">Processes API</a></li>
<li><a href="/sandbox/1-0-preview/errors/">Errors and recovery</a></li>
<li><a href="/sandbox/1-0-preview/api/errors/">Errors API</a></li>
<li><a href="/sandbox/1-0-preview/api/">API reference</a></li>
<li><a href="/sandbox/1-0-preview/terminals/">Terminals</a></li>
<li><a href="/sandbox/1-0-preview/api/terminals/">Terminals API</a></li>
<li><a href="/sandbox/1-0-preview/interpreter/">Code interpreter</a></li>
<li><a href="/sandbox/1-0-preview/extensions/">Extensions</a></li>
<li><a href="/sandbox/1-0-preview/troubleshooting/">Troubleshooting</a></li>
<li><a href="/sandbox/guides/deploy/">Deploy a Sandbox application</a></li>
<li><a href="/containers/guides/deploy/">Deploy Containers</a></li>
<li><a href="/containers/configuration/rollouts/">Rollouts</a></li>
</ul>
