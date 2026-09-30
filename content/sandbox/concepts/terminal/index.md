<p>Terminal connections let browser-based UIs interact directly with sandbox shells. Instead of executing discrete commands with <code>exec()</code>, a terminal connection opens a persistent, bidirectional channel to a bash shell — the same model as SSH or a local terminal emulator.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="sandbox-sdk-1-0-preview">Sandbox SDK 1.0 preview</h3>
@markup("md", "content/.markup/bodies/13567.md")
</aside>
<h2 id="how-terminal-connections-work">How terminal connections work</h2>
<p>Terminal connections use WebSockets to stream raw bytes between a browser terminal (like <a href="https://xtermjs.org/">xterm.js</a>) and a pseudo-terminal (PTY) process running inside the sandbox container.</p>
<pre><code class="language-txt">Browser (xterm.js) &lt;-- WebSocket --&gt; Worker &lt;-- proxy --&gt; Container PTY (bash)&#10;</code></pre>
<ol>
<li>The browser sends a WebSocket upgrade request to your Worker</li>
<li>Your Worker calls <code>sandbox.terminal(request)</code>, which proxies the upgrade to the container</li>
<li>The container spawns a bash shell attached to a PTY</li>
<li>Raw bytes flow bidirectionally — keystrokes in, terminal output out</li>
</ol>
<p>This is fundamentally different from <code>exec()</code>:</p>
<ul>
<li><strong><code>exec()</code></strong> runs a single command to completion and returns the result</li>
<li><strong><code>terminal()</code></strong> opens a persistent shell where users type commands interactively</li>
</ul>
<h2 id="output-buffering">Output buffering</h2>
<p>The container buffers terminal output in a ring buffer. When a client disconnects and reconnects, the server replays buffered output so the terminal appears unchanged. This means:</p>
<ul>
<li>Short network interruptions are invisible to users</li>
<li>Reconnected terminals show previous output without re-running commands</li>
<li>The buffer has a fixed size, so very old output may be lost</li>
</ul>
<p>No client-side code is needed to handle buffering — the container manages it transparently.</p>
<h2 id="automatic-reconnection">Automatic reconnection</h2>
<p>Network interruptions are common in browser-based applications. Terminal connections handle this through a combination of server-side buffering (described above) and client-side reconnection with exponential backoff.</p>
<p>The <code>SandboxAddon</code> for xterm.js implements this automatically. If you are building a custom client, you are responsible for your own reconnection logic — the server-side buffering works regardless of which client connects. Refer to the <a href="/sandbox/api/terminal/#websocket-protocol">WebSocket protocol reference</a> for details on the connection lifecycle.</p>
<h2 id="session-specific-terminals">Session-specific terminals</h2>
<p>Each <a href="/sandbox/concepts/sessions/">session</a> can have its own terminal with independent shell state:</p>
<pre><code class="language-typescript">const devSession = await sandbox.createSession({&#10;	id: &quot;dev&quot;,&#10;	cwd: &quot;/workspace/frontend&quot;,&#10;	env: { NODE_ENV: &quot;development&quot; },&#10;});&#10;&#10;const testSession = await sandbox.createSession({&#10;	id: &quot;test&quot;,&#10;	cwd: &quot;/workspace&quot;,&#10;	env: { NODE_ENV: &quot;test&quot; },&#10;});&#10;&#10;// Each session&#x27;s terminal has its own working directory,&#10;// environment variables, and command history&#10;</code></pre>
<p>Multiple browser clients can connect to the same session's terminal simultaneously. They all see the same shell output and can send input. Use this pattern for intentional collaboration inside one workspace, not to separate independent users.</p>
<h2 id="websocket-protocol">WebSocket protocol</h2>
<p>Terminal connections use binary WebSocket frames for terminal I/O (for performance) and JSON text frames for control and status messages (for structure). This keeps the data path fast while still allowing structured communication for operations like terminal resizing.</p>
<p>For the full protocol specification, including the connection lifecycle and message formats, refer to the <a href="/sandbox/api/terminal/#websocket-protocol">Terminal API reference</a>.</p>
<h2 id="when-to-use-terminals-vs-commands">When to use terminals vs commands</h2>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Approach</th>
</tr>
</thead>
<tbody>
<tr>
<td>Run a command and get the result</td>
<td><code>exec()</code> or <code>execStream()</code></td>
</tr>
<tr>
<td>Interactive shell for end users</td>
<td><code>terminal()</code></td>
</tr>
<tr>
<td>Long-running process with real-time output</td>
<td><code>startProcess()</code> + <code>streamProcessLogs()</code></td>
</tr>
<tr>
<td>Collaborative terminal sharing</td>
<td><code>terminal()</code> with shared session</td>
</tr>
</tbody>
</table>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/api/terminal/">Terminal API reference</a> — Method signatures and types</li>
<li><a href="/sandbox/guides/browser-terminals/">Browser terminals</a> — Step-by-step setup guide</li>
<li><a href="/sandbox/concepts/sessions/">Session management</a> — How sessions work</li>
<li><a href="/sandbox/concepts/architecture/">Architecture</a> — Overall SDK design</li>
</ul>
