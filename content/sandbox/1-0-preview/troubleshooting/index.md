<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13703.md")
</aside>
<p>Use this symptom-to-fix map. For deeper recovery, refer to <a href="/sandbox/1-0-preview/errors/">Errors and recovery</a>. For lifecycle behavior, refer to <a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a>.</p>
<h2 id="deploy-and-image">Deploy and image</h2>
<table>
<thead>
<tr>
<th>Symptom</th>
<th>What to check</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>RuntimeControlProtocolError</code>, control/protocol failures after deploy</td>
<td>Worker package and container image are on different lines. Use the same <code>@next</code> / <code>cloudflare/sandbox:next</code> (or the same exact prerelease) pair.</td>
</tr>
<tr>
<td>Container never becomes ready, or you see repeated <code>ContainerUnavailableError</code></td>
<td>Cold start or capacity. Back off using <code>retryAfterMs</code> when set, then retry the <strong>work</strong>. Refer to <a href="/sandbox/1-0-preview/errors/">Errors and recovery</a>.</td>
</tr>
<tr>
<td>Works in <code>wrangler dev</code>, fails in production only</td>
<td>Production-only limits and cold start. Still keep package/image matched.</td>
</tr>
</tbody>
</table>
<h2 id="processes">Processes</h2>
<table>
<thead>
<tr>
<th>Symptom</th>
<th>What to check</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>await exec</code> “finished” but the command did not</td>
<td><code>exec</code> resolves on <strong>launch</strong>. Use <code>output()</code>, <code>waitForExit()</code>, or <code>exitCode</code>.</td>
</tr>
<tr>
<td>No stdout as a string</td>
<td><code>output()</code> defaults to bytes. Pass <code>{ encoding: &quot;utf8&quot; }</code>.</td>
</tr>
<tr>
<td><code>getProcess</code> is <code>null</code> / list is <code>[]</code></td>
<td>No container running, or ID unknown in the <strong>current</strong> container. Discovery does not wake a sandbox. Relaunch from stored job state if needed.</td>
</tr>
<tr>
<td><code>StaleProcessHandleError</code></td>
<td>Handle was from a previous container. Start a new <code>exec</code> from checkpointed work.</td>
</tr>
<tr>
<td>Wait timed out / aborted but process still runs</td>
<td>Local wait only. Call <code>kill()</code> if you intend to stop it.</td>
</tr>
<tr>
<td>Port never becomes ready</td>
<td>Default <code>waitForPort</code> mode is <strong>TCP</strong>. Use <code>mode: &quot;http&quot;</code> for HTTP checks. Process may have exited — check status/logs.</td>
</tr>
<tr>
<td>Need interactive stdin</td>
<td>Not on the process handle. Use a <a href="/sandbox/1-0-preview/terminals/">terminal</a> or non-interactive argv/<code>cwd</code>/<code>env</code>.</td>
</tr>
</tbody>
</table>
<h2 id="terminals">Terminals</h2>
<table>
<thead>
<tr>
<th>Symptom</th>
<th>What to check</th>
</tr>
</thead>
<tbody>
<tr>
<td>Browser still uses <code>sessionId</code></td>
<td>Preview xterm helper expects <code>terminalId</code>.</td>
</tr>
<tr>
<td><code>getTerminal</code> is <code>null</code></td>
<td>Same lifetime rules as processes. Create again if the container was replaced.</td>
</tr>
<tr>
<td>Reconnect has no history</td>
<td>Pass the last <code>cursor</code> into <code>connect</code> / output options.</td>
</tr>
</tbody>
</table>
<h2 id="environment-and-secrets">Environment and secrets</h2>
<table>
<thead>
<tr>
<th>Symptom</th>
<th>What to check</th>
</tr>
</thead>
<tbody>
<tr>
<td>Env from an earlier <code>exec</code> “disappeared”</td>
<td>No session shell. Use <code>setEnvVars</code> and/or per-launch <code>env</code>. <a href="/sandbox/1-0-preview/environment/">Environment variables</a>.</td>
</tr>
<tr>
<td>API keys leaked into the container</td>
<td>Do not put live secrets in sandbox env. Use <a href="/sandbox/guides/outbound-traffic/">outbound traffic</a> handlers on the Worker.</td>
</tr>
</tbody>
</table>
<h2 id="interpreter">Interpreter</h2>
<table>
<thead>
<tr>
<th>Symptom</th>
<th>What to check</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sandbox.createCodeContext is not a function</code></td>
<td>Attach <code>withInterpreter</code> and call <code>sandbox.interpreter.*</code>.</td>
</tr>
<tr>
<td>Python not available</td>
<td>Use the <strong><code>-python</code></strong> image variant on the same <code>@next</code> line.</td>
</tr>
</tbody>
</table>
<h2 id="bridge-http">Bridge HTTP</h2>
<table>
<thead>
<tr>
<th>Symptom</th>
<th>What to check</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bridge <code>/exec</code>, sessions, or <code>/pty</code> behavior differs from <code>@next</code> Worker SDK docs</td>
<td>The self-deployed bridge is not part of the 1.0 preview. Use the <a href="/sandbox/bridge/">stable bridge</a> with matching stable package and container image.</td>
</tr>
</tbody>
</table>
<h2 id="agents-and-long-running-jobs">Agents and long-running jobs</h2>
<p>For agents and long-running tools on <code>@next</code>:</p>
<ol>
<li>Launch with <code>exec(argv)</code> (often <code>['/bin/bash', '-lc', script]</code>).</li>
<li>Wait with <code>waitForLog</code>, <code>waitForPort</code>, or <code>logs</code> — not only <code>await exec</code>.</li>
<li>Persist <strong>job state</strong> (command, <code>cwd</code>, <code>env</code>, checkpoint), not only <code>process.id</code>.</li>
<li>On a later request: <code>getProcess(id)</code> while the same container may still hold it; otherwise <code>exec</code> again.</li>
<li>Use a <a href="/sandbox/1-0-preview/terminals/">terminal</a> only when you need a human PTY, not as a session substitute.</li>
</ol>
<p>Refer to <a href="/sandbox/1-0-preview/processes/">Process execution</a>, <a href="/sandbox/1-0-preview/migrate/">Migrate</a>, and examples in the <a href="https://github.com/cloudflare/sandbox-sdk/tree/next/examples">sandbox-sdk</a> repo (<code>claude-code</code>, <code>codex</code>, <code>opencode</code>, and others).</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/1-0-preview/errors/">Errors and recovery</a></li>
<li><a href="/sandbox/1-0-preview/api/errors/">Errors API</a></li>
<li><a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a></li>
<li><a href="/sandbox/1-0-preview/api/processes/">Process API</a></li>
<li><a href="/sandbox/1-0-preview/api/terminals/">Terminal API</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a></li>
</ul>
