<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13757.md")
</aside>
<p>Create and control interactive PTY terminals in the current container for a sandbox.</p>
<p>For the mental model and browser connect walkthrough, refer to <a href="/sandbox/1-0-preview/terminals/">Terminals</a>.</p>
<h2 id="createterminal"><code>createTerminal()</code></h2>
<p>Start a terminal from <strong>argv</strong> (usually a shell). Resolves when the terminal resource is created. Same rules as process <code>exec</code>: no implicit shell wrapping, and argv entries are not shell-escaped.</p>
<pre><code class="language-ts">createTerminal(options: CreateTerminalOptions): Promise&lt;Terminal&gt;&#10;</code></pre>
<h3 id="createterminaloptions"><code>CreateTerminalOptions</code></h3>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>command</code></td>
<td><code>SandboxCommand</code></td>
<td>Argv to run under the PTY. Required. Example: <code>['bash']</code> or <code>['/bin/bash']</code>.</td>
</tr>
<tr>
<td><code>cwd</code></td>
<td><code>string</code></td>
<td>Working directory for the terminal process.</td>
</tr>
<tr>
<td><code>env</code></td>
<td><code>Record&lt;string, string&gt;</code></td>
<td>Environment overlay for this terminal. Does not mutate later launches.</td>
</tr>
<tr>
<td><code>cols</code></td>
<td><code>number</code></td>
<td>Initial width in columns.</td>
</tr>
<tr>
<td><code>rows</code></td>
<td><code>number</code></td>
<td>Initial height in rows.</td>
</tr>
<tr>
<td><code>bufferSize</code></td>
<td><code>number</code></td>
<td>Output buffer sizing for replay (when supported by the runtime).</td>
</tr>
</tbody>
</table>
<p><code>SandboxCommand</code> is the same argv type as process <code>exec</code>: <code>readonly [executable: string, ...args: string[]]</code>.</p>
<h3 id="returns">Returns</h3>
<p><code>Promise&lt;Terminal&gt;</code> — a handle for the terminal in the <strong>current container</strong>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13758.md")
</div>
<h2 id="getterminal"><code>getTerminal()</code></h2>
<p>Return a handle for a terminal in the <strong>current container</strong>, or <code>null</code>.</p>
<p>Does not start a container if none is running. Returns <code>null</code> when no container is up, when the terminal ID is unknown in the current container, or when that terminal belonged to a previous container for the same sandbox ID.</p>
<pre><code class="language-ts">getTerminal(id: string): Promise&lt;Terminal | null&gt;&#10;</code></pre>
<h2 id="listterminals"><code>listTerminals()</code></h2>
<p>List terminals in the current container for this sandbox. Does not start a container if none is running. Returns an empty list when no container is up.</p>
<pre><code class="language-ts">listTerminals(): Promise&lt;Terminal[]&gt;&#10;</code></pre>
<h2 id="terminal"><code>Terminal</code></h2>
<table>
<thead>
<tr>
<th>Member</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>id</code></td>
<td>Terminal ID in the current container.</td>
</tr>
<tr>
<td><code>getSnapshot()</code></td>
<td>Current snapshot (<code>running</code> / <code>exited</code> / <code>error</code>).</td>
</tr>
<tr>
<td><code>write(data)</code></td>
<td>Write bytes to the PTY (stdin).</td>
</tr>
<tr>
<td><code>resize(cols, rows)</code></td>
<td>Resize the PTY.</td>
</tr>
<tr>
<td><code>output(options?)</code></td>
<td>Cursor-based output event stream.</td>
</tr>
<tr>
<td><code>waitForExit(options?)</code></td>
<td>Wait until the terminal completes.</td>
</tr>
<tr>
<td><code>interrupt()</code></td>
<td>Send an interrupt to the terminal session (for example Ctrl-C semantics).</td>
</tr>
<tr>
<td><code>terminate()</code></td>
<td>End the terminal resource.</td>
</tr>
<tr>
<td><code>connect(request, opts?)</code></td>
<td>Accept a browser WebSocket upgrade and attach it to this terminal.</td>
</tr>
</tbody>
</table>
<h3 id="getsnapshot"><code>getSnapshot()</code></h3>
<pre><code class="language-ts">interface TerminalSnapshot {&#10;	id: string;&#10;	pid?: number;&#10;	command: SandboxCommand;&#10;	cwd?: string;&#10;	status: &quot;running&quot; | &quot;exited&quot; | &quot;error&quot;;&#10;	exit?: ProcessExit;&#10;	error?: ProcessFailure;&#10;}&#10;</code></pre>
<h3 id="write"><code>write()</code></h3>
<pre><code class="language-ts">write(data: Uint8Array): Promise&lt;void&gt;&#10;</code></pre>
<p>Write bytes to the PTY. Browser keystrokes normally arrive through <code>connect()</code> instead.</p>
<h3 id="resize"><code>resize()</code></h3>
<pre><code class="language-ts">resize(cols: number, rows: number): Promise&lt;void&gt;&#10;</code></pre>
<h3 id="output"><code>output()</code></h3>
<pre><code class="language-ts">output(options?: TerminalOutputOptions): Promise&lt;ReadableStream&lt;TerminalOutputEvent&gt;&gt;&#10;</code></pre>
<h4 id="terminaloutputoptions"><code>TerminalOutputOptions</code></h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>since</code></td>
<td><code>string</code></td>
<td>Opaque cursor; resume after a previous event.</td>
</tr>
<tr>
<td><code>replay</code></td>
<td><code>boolean</code></td>
<td>Include buffered history when resuming.</td>
</tr>
<tr>
<td><code>follow</code></td>
<td><code>boolean</code></td>
<td>Keep the stream open for live output.</td>
</tr>
<tr>
<td><code>signal</code></td>
<td><code>AbortSignal</code></td>
<td>Cancel this subscription only. The terminal keeps running.</td>
</tr>
</tbody>
</table>
<h4 id="terminaloutputevent"><code>TerminalOutputEvent</code></h4>
<pre><code class="language-ts">type TerminalOutputEvent =&#10;	| {&#10;			type: &quot;data&quot;;&#10;			terminalId: string;&#10;			cursor: string;&#10;			timestamp: string;&#10;			data: Uint8Array;&#10;	  }&#10;	| {&#10;			type: &quot;terminal&quot;;&#10;			terminalId: string;&#10;			cursor: string;&#10;			timestamp: string;&#10;			state: &quot;exited&quot;;&#10;			exit: ProcessExit;&#10;	  }&#10;	| {&#10;			type: &quot;terminal&quot;;&#10;			terminalId: string;&#10;			cursor: string;&#10;			timestamp: string;&#10;			state: &quot;error&quot;;&#10;			error: ProcessFailure;&#10;	  }&#10;	| {&#10;			type: &quot;truncated&quot;;&#10;			terminalId: string;&#10;			cursor?: string;&#10;			timestamp: string;&#10;	  };&#10;</code></pre>
<p>Retain the latest <code>cursor</code> from delivered events if you reconnect or call <code>output({ since, replay: true })</code> later on the <strong>same</strong> terminal in the <strong>same</strong> container.</p>
<h3 id="waitforexit"><code>waitForExit()</code></h3>
<pre><code class="language-ts">waitForExit(options?: {&#10;	timeout?: number;&#10;	signal?: AbortSignal;&#10;}): Promise&lt;ProcessExit&gt;&#10;</code></pre>
<p>Local <code>timeout</code> / <code>signal</code> cancel only the wait. They do not terminate the terminal. Call <code>terminate()</code> or <code>interrupt()</code> when you intend to stop it.</p>
<h3 id="interrupt-and-terminate"><code>interrupt()</code> and <code>terminate()</code></h3>
<pre><code class="language-ts">interrupt(): Promise&lt;void&gt;&#10;terminate(): Promise&lt;void&gt;&#10;</code></pre>
<p>These are terminal control operations. They are not the same as process <code>kill(signal)</code> on an <code>exec</code> handle.</p>
<h3 id="connect"><code>connect()</code></h3>
<p>Attach a browser (or other) WebSocket upgrade request to this terminal.</p>
<pre><code class="language-ts">connect(&#10;	request: Request,&#10;	options?: {&#10;		cursor?: string;&#10;		cols?: number;&#10;		rows?: number;&#10;	},&#10;): Promise&lt;Response&gt;&#10;</code></pre>
<ul>
<li><code>request</code> must be a WebSocket upgrade request.</li>
<li><code>cursor</code> resumes output replay after a previous disconnect when the client has one.</li>
<li><code>cols</code> / <code>rows</code> set the PTY size for this attachment when provided.</li>
</ul>
<p>Returns the WebSocket upgrade <code>Response</code> your Worker should return to the client.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13759.md")
</div>
<p>For the full Worker + xterm.js path, refer to <a href="/sandbox/1-0-preview/terminals/#browser-connect">Terminals</a>.</p>
<h2 id="client-helper-cloudflare-sandbox-xterm">Client helper: <code>@cloudflare/sandbox/xterm</code></h2>
<p><code>SandboxAddon</code> integrates <a href="https://xtermjs.org/">xterm.js</a> with preview terminals.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13760.md")
</div>
<table>
<thead>
<tr>
<th>Item</th>
<th>Preview detail</th>
</tr>
</thead>
<tbody>
<tr>
<td>Connection target</td>
<td><code>{ sandboxId, terminalId? }</code></td>
</tr>
<tr>
<td><code>getWebSocketUrl</code> params</td>
<td><code>sandboxId</code>, <code>terminalId?</code>, <code>cursor?</code>, <code>origin</code></td>
</tr>
<tr>
<td>Properties</td>
<td><code>state</code>, <code>sandboxId</code>, <code>terminalId</code></td>
</tr>
</tbody>
</table>
<p><code>@xterm/xterm</code> is an optional peer dependency of the preview package.</p>
<h2 id="common-errors">Common errors</h2>
<table>
<thead>
<tr>
<th>Situation</th>
<th>Class / outcome</th>
</tr>
</thead>
<tbody>
<tr>
<td>Unknown terminal ID in the current container</td>
<td><code>TerminalNotFoundError</code></td>
</tr>
<tr>
<td><code>getTerminal</code> / <code>listTerminals</code> while no container is running</td>
<td><code>null</code> / <code>[]</code> (not an error; does not start a container)</td>
</tr>
<tr>
<td>Handle or terminal ID from a previous container</td>
<td><code>StaleTerminalHandleError</code></td>
</tr>
<tr>
<td>Invalid working directory at create</td>
<td><code>InvalidTerminalCwdError</code></td>
</tr>
<tr>
<td>Invalid output cursor</td>
<td><code>InvalidTerminalCursorError</code></td>
</tr>
<tr>
<td>Control operation failed</td>
<td><code>TerminalControlError</code></td>
</tr>
</tbody>
</table>
<p>Recovery guidance: <a href="/sandbox/1-0-preview/errors/">Errors and recovery</a>. Full catalog: <a href="/sandbox/1-0-preview/api/errors/">Errors API</a>. Lifetime: <a href="/sandbox/1-0-preview/processes/#how-long-a-process-lives">How long a process lives</a>.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/1-0-preview/terminals/">Terminals</a></li>
<li><a href="/sandbox/1-0-preview/errors/">Errors and recovery</a></li>
<li><a href="/sandbox/1-0-preview/api/errors/">Errors API</a></li>
<li><a href="/sandbox/1-0-preview/api/processes/">Processes API</a></li>
<li><a href="/sandbox/1-0-preview/api/">API reference</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a></li>
<li>Stable: <a href="/sandbox/api/terminal/">Terminal</a></li>
</ul>
