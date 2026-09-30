<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13704.md")
</aside>
<p>A <strong>terminal</strong> is an interactive PTY in the current container for a sandbox. Use it for full-duplex terminal I/O: a browser shell, resize, interrupt, and reconnect.</p>
<p>Command execution uses <a href="/sandbox/1-0-preview/processes/"><code>exec</code></a> and process handles. Terminals are a separate resource type. API reference: <a href="/sandbox/1-0-preview/api/terminals/">Terminals API</a>.</p>
<h2 id="processes-and-terminals">Processes and terminals</h2>
<table>
<thead>
<tr>
<th></th>
<th>Process (<code>exec</code>)</th>
<th>Terminal</th>
</tr>
</thead>
<tbody>
<tr>
<td>Role</td>
<td>Supervised argv process</td>
<td>Interactive PTY</td>
</tr>
<tr>
<td>Input</td>
<td>Launch-time argv (and whatever the program reads on its own)</td>
<td>PTY input via <code>write()</code> or browser <code>connect()</code></td>
</tr>
<tr>
<td>Output</td>
<td><code>logs()</code>, <code>output()</code>, waits</td>
<td><code>output()</code>, snapshot, <code>waitForExit()</code></td>
</tr>
<tr>
<td>Stop</td>
<td><code>kill(signal?)</code></td>
<td><code>interrupt()</code> / <code>terminate()</code></td>
</tr>
<tr>
<td>Lookup</td>
<td><code>getProcess</code> / <code>listProcesses</code></td>
<td><code>getTerminal</code> / <code>listTerminals</code></td>
</tr>
</tbody>
</table>
<p>Both kinds of resource live only in the current container for a sandbox ID. Lookup methods do not start a container. Refer to <a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a> and <a href="/sandbox/1-0-preview/processes/#how-long-a-process-lives">How long a process lives</a>.</p>
<h2 id="create-a-terminal">Create a terminal</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13705.md")
</div>
<p>You can write to the PTY from the Worker, resize it, stream output, or end it:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13706.md")
</div>
<h2 id="lifetime">Lifetime</h2>
<ul>
<li>A terminal exists only in the <strong>current container</strong> for that sandbox ID.</li>
<li><code>getTerminal</code> / <code>listTerminals</code> return <code>null</code> / <code>[]</code> when no container is running. They do not start one.</li>
<li>After the container stops or is replaced, old terminal IDs are invalid. Create a new terminal if you need one again.</li>
<li>An active terminal can keep the container alive across Worker requests, as an active process can.</li>
</ul>
<p>Store <code>terminal.id</code> to resume the same PTY while that container is still up.</p>
<h2 id="browser-connect">Browser connect</h2>
<ol>
<li>Create a terminal and keep <code>terminal.id</code> with the sandbox id.</li>
<li>On each WebSocket upgrade, resolve the terminal with <code>getTerminal</code>, then return <code>terminal.connect(request)</code>.</li>
<li>In the browser, use <code>@cloudflare/sandbox/xterm</code> with <strong><code>terminalId</code></strong>.</li>
</ol>
<h3 id="worker">Worker</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13707.md")
</div>
<p>Create the terminal from an application route when the UI needs one:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13708.md")
</div>
<h3 id="browser-xterm-js">Browser (xterm.js)</h3>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div></div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13709.md")
</div>
<table>
<thead>
<tr>
<th>Stable package</th>
<th>Preview</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sandbox.terminal(request)</code></td>
<td><code>createTerminal</code> + <code>getTerminal</code> + <code>connect</code></td>
</tr>
<tr>
<td>xterm / URL <code>sessionId</code></td>
<td><code>terminalId</code> (and optional <code>cursor</code>)</td>
</tr>
</tbody>
</table>
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/1-0-preview/api/terminals/">Terminals API</a></li>
<li><a href="/sandbox/1-0-preview/errors/">Errors and recovery</a></li>
<li><a href="/sandbox/1-0-preview/api/errors/">Errors API</a></li>
<li><a href="/sandbox/1-0-preview/processes/">Process execution</a></li>
<li><a href="/sandbox/1-0-preview/api/processes/">Processes API</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a></li>
</ul>
