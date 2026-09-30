<p>Execute commands and manage background processes in the sandbox's isolated container environment.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13679.md")
</aside>
<h2 id="methods">Methods</h2>
<h3 id="exec"><code>exec()</code></h3>
<p>Execute a command and return the complete result.</p>
<pre><code class="language-ts">const result = await sandbox.exec(command: string, options?: ExecOptions): Promise&lt;ExecuteResponse&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>command</code> - The command to execute (can include arguments)</li>
<li><code>options</code> (optional):
<ul>
<li><code>stream</code> - Enable streaming callbacks (default: <code>false</code>)</li>
<li><code>onOutput</code> - Callback for real-time output: <code>(stream: 'stdout' | 'stderr', data: string) =&gt; void</code></li>
<li><code>timeout</code> - Maximum execution time in milliseconds</li>
<li><code>env</code> - Environment variables for this command: <code>Record&lt;string, string | undefined&gt;</code></li>
<li><code>cwd</code> - Working directory for this command</li>
<li><code>stdin</code> - Data to pass to the command's standard input (enables arbitrary input without shell injection risks)</li>
</ul>
</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;ExecuteResponse&gt;</code> with <code>success</code>, <code>stdout</code>, <code>stderr</code>, <code>exitCode</code></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13680.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="timeout-behavior">Timeout behavior</h3>
@markup("md", "content/.markup/bodies/13678.md")
</aside>
<h3 id="execstream"><code>execStream()</code></h3>
<p>Execute a command and return a Server-Sent Events stream for real-time processing.</p>
<pre><code class="language-ts">const stream = await sandbox.execStream(command: string, options?: ExecOptions): Promise&lt;ReadableStream&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>command</code> - The command to execute</li>
<li><code>options</code> - Same as <code>exec()</code> (including <code>stdin</code> support)</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;ReadableStream&gt;</code> emitting <code>ExecEvent</code> objects (<code>start</code>, <code>stdout</code>, <code>stderr</code>, <code>complete</code>, <code>error</code>)</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13681.md")
</div>
<h3 id="startprocess"><code>startProcess()</code></h3>
<p>Start a long-running background process.</p>
<pre><code class="language-ts">const process = await sandbox.startProcess(command: string, options?: ProcessOptions): Promise&lt;Process&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>command</code> - The command to start as a background process</li>
<li><code>options</code> (optional):
<ul>
<li><code>cwd</code> - Working directory</li>
<li><code>env</code> - Environment variables: <code>Record&lt;string, string | undefined&gt;</code></li>
<li><code>stdin</code> - Data to pass to the command's standard input</li>
<li><code>timeout</code> - Maximum execution time in milliseconds</li>
<li><code>processId</code> - Custom process ID</li>
<li><code>encoding</code> - Output encoding (default: <code>'utf8'</code>)</li>
<li><code>autoCleanup</code> - Whether to clean up process on sandbox sleep</li>
</ul>
</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;Process&gt;</code> object with:</p>
<ul>
<li><code>id</code> - Unique process identifier</li>
<li><code>pid</code> - System process ID</li>
<li><code>command</code> - The command being executed</li>
<li><code>status</code> - Current status (<code>'running'</code>, <code>'exited'</code>, etc.)</li>
<li><code>kill()</code> - Stop the process</li>
<li><code>getStatus()</code> - Get current status</li>
<li><code>getLogs()</code> - Get accumulated logs</li>
<li><code>waitForPort()</code> - Wait for process to listen on a port</li>
<li><code>waitForLog()</code> - Wait for pattern in process output</li>
<li><code>waitForExit()</code> - Wait for process to terminate and return exit code</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13682.md")
</div>
<h3 id="listprocesses"><code>listProcesses()</code></h3>
<p>List all running processes.</p>
<pre><code class="language-ts">const processes = await sandbox.listProcesses(): Promise&lt;ProcessInfo[]&gt;&#10;</code></pre>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13683.md")
</div>
<h3 id="killprocess"><code>killProcess()</code></h3>
<p>Terminate a specific process and all of its child processes.</p>
<pre><code class="language-ts">await sandbox.killProcess(processId: string, signal?: string): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>processId</code> - The process ID (from <code>startProcess()</code> or <code>listProcesses()</code>)</li>
<li><code>signal</code> - Signal to send (default: <code>&quot;SIGTERM&quot;</code>)</li>
</ul>
<p>Sends the signal to the entire process group, ensuring that both the main process and any child processes it spawned are terminated. This prevents orphaned processes from continuing to run after the parent is killed.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13684.md")
</div>
<h3 id="killallprocesses"><code>killAllProcesses()</code></h3>
<p>Terminate all running processes.</p>
<pre><code class="language-ts">await sandbox.killAllProcesses(): Promise&lt;void&gt;&#10;</code></pre>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13685.md")
</div>
<h3 id="streamprocesslogs"><code>streamProcessLogs()</code></h3>
<p>Stream logs from a running process in real-time.</p>
<pre><code class="language-ts">const stream = await sandbox.streamProcessLogs(processId: string): Promise&lt;ReadableStream&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>processId</code> - The process ID</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;ReadableStream&gt;</code> emitting <code>LogEvent</code> objects</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13686.md")
</div>
<h3 id="getprocesslogs"><code>getProcessLogs()</code></h3>
<p>Get accumulated logs from a process.</p>
<pre><code class="language-ts">const logs = await sandbox.getProcessLogs(processId: string): Promise&lt;string&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>processId</code> - The process ID</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;string&gt;</code> with all accumulated output</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13687.md")
</div>
<h2 id="standard-input-stdin">Standard input (stdin)</h2>
<p>All command execution methods support passing data to a command's standard input via the <code>stdin</code> option. This enables secure processing of user input without shell injection risks.</p>
<h3 id="how-stdin-works">How stdin works</h3>
<p>When you provide the <code>stdin</code> option:</p>
<ol>
<li>The input data is written to a temporary file inside the container</li>
<li>The command receives this data through its standard input stream</li>
<li>The temporary file is automatically cleaned up after execution</li>
</ol>
<p>This approach prevents shell injection attacks that could occur when embedding user data directly in commands.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13688.md")
</div>
<h3 id="common-patterns">Common patterns</h3>
<p><strong>Processing form data:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13689.md")
</div>
<p><strong>Interactive command-line tools:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13690.md")
</div>
<p><strong>Data transformation:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13691.md")
</div>
<h2 id="process-readiness-methods">Process readiness methods</h2>
<p>The <code>Process</code> object returned by <code>startProcess()</code> includes methods to wait for the process to be ready before proceeding.</p>
<h3 id="process-waitforport"><code>process.waitForPort()</code></h3>
<p>Wait for a process to listen on a port.</p>
<pre><code class="language-ts">await process.waitForPort(port: number, options?: WaitForPortOptions): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>port</code> - The port number to check</li>
<li><code>options</code> (optional):
<ul>
<li><code>mode</code> - Check mode: <code>'http'</code> (default) or <code>'tcp'</code></li>
<li><code>timeout</code> - Maximum wait time in milliseconds</li>
<li><code>interval</code> - Check interval in milliseconds (default: <code>100</code>)</li>
<li><code>path</code> - HTTP path to check (default: <code>'/'</code>, HTTP mode only)</li>
<li><code>status</code> - Expected HTTP status range (default: <code>{ min: 200, max: 399 }</code>, HTTP mode only)</li>
</ul>
</li>
</ul>
<p><strong>HTTP mode</strong> (default) makes an HTTP GET request and checks the response status:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13692.md")
</div>
<p><strong>TCP mode</strong> checks if the port accepts connections:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13693.md")
</div>
<p><strong>Throws</strong>:</p>
<ul>
<li><code>ProcessReadyTimeoutError</code> - If port does not become ready within timeout</li>
<li><code>ProcessExitedBeforeReadyError</code> - If process exits before becoming ready</li>
</ul>
<h3 id="process-waitforlog"><code>process.waitForLog()</code></h3>
<p>Wait for a pattern to appear in process output.</p>
<pre><code class="language-ts">const result = await process.waitForLog(pattern: string | RegExp, timeout?: number): Promise&lt;WaitForLogResult&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>pattern</code> - String or RegExp to match in stdout/stderr</li>
<li><code>timeout</code> - Maximum wait time in milliseconds (optional)</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;WaitForLogResult&gt;</code> with:</p>
<ul>
<li><code>line</code> - The matching line of output</li>
<li><code>matches</code> - Array of capture groups (for RegExp patterns)</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13694.md")
</div>
<p><strong>Throws</strong>:</p>
<ul>
<li><code>ProcessReadyTimeoutError</code> - If pattern is not found within timeout</li>
<li><code>ProcessExitedBeforeReadyError</code> - If process exits before pattern appears</li>
</ul>
<h3 id="process-waitforexit"><code>process.waitForExit()</code></h3>
<p>Wait for a process to terminate and return the exit code.</p>
<pre><code class="language-ts">const result = await process.waitForExit(timeout?: number): Promise&lt;WaitForExitResult&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>timeout</code> - Maximum wait time in milliseconds (optional)</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;WaitForExitResult&gt;</code> with:</p>
<ul>
<li><code>exitCode</code> - The process exit code</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13695.md")
</div>
<p><strong>Throws</strong>:</p>
<ul>
<li><code>ProcessReadyTimeoutError</code> - If process does not exit within timeout</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/guides/background-processes/">Background processes guide</a> - Managing long-running processes</li>
<li><a href="/sandbox/api/files/">Files API</a> - File operations</li>
</ul>
