<p>Use <code>exec()</code> to start another process inside a running <a href="/containers/reference/container-class/">Container</a>. The examples call <code>this.ctx.container.exec()</code> inside a class extending <code>Container</code> from <code>@cloudflare/containers</code>.</p>
<p><code>exec()</code> does not start a stopped Container. In remote procedure call (RPC) methods, check <code>this.ctx.container.running</code> and call <code>await this.start()</code> when needed. You can also use the <code>onStart()</code> hook to run any series of commands whenever the Container starts.</p>
<h2 id="run-a-process-after-startup">Run a process after startup</h2>
<p>The following hook runs a preparation command whenever the Container starts. You can execute any series of startup commands from this hook. <code>output()</code> buffers standard output and standard error as separate <code>ArrayBuffer</code> values.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7116.md")
</div>
<p>In an RPC method, ensure the Container is running before calling <code>exec()</code>. Standard output uses a readable stream by default.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7117.md")
</div>
<p>The returned <code>pid</code> identifies the new process. The <code>exitCode</code> promise resolves when that process exits.</p>
<h2 id="pass-arguments-directly">Pass arguments directly</h2>
<p>The <code>exec()</code> operation starts the executable directly with the provided argument array. It does not start a shell first.</p>
<p>Each array item becomes one argument. Shell features such as pipes, redirects, globbing, and variable expansion do not run implicitly.</p>
<p>Invoke a shell when your command needs those features. Use <code>[&quot;bash&quot;, &quot;-lc&quot;, &quot;&lt;COMMAND&gt;&quot;]</code> if Bash exists in your image. Use <code>[&quot;sh&quot;, &quot;-c&quot;, &quot;&lt;COMMAND&gt;&quot;]</code> if the image only provides a Portable Operating System Interface (POSIX) shell. Pass untrusted values as separate arguments instead of interpolating them into a shell command string.</p>
<h2 id="send-standard-input">Send standard input</h2>
<p>Pass a <code>ReadableStream</code> to send existing data. Setting <code>stdout</code> to <code>&quot;ignore&quot;</code> discards standard output.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7118.md")
</div>
<p>Ignored standard output produces an empty buffer from <code>output()</code>. Set <code>stdin</code> to <code>&quot;pipe&quot;</code> to write data over time.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7119.md")
</div>
<p>Close the writer to send end-of-file (EOF). If you omit <code>stdin</code>, <code>exec()</code> closes standard input and sends EOF immediately.</p>
<h3 id="pass-an-rpc-stream-to-standard-input">Pass an RPC stream to standard input</h3>
<p>RPC methods can accept byte-oriented <code>ReadableStream</code> values whose underlying source uses <code>type: &quot;bytes&quot;</code>. A <code>Request</code> body meets this requirement. You can pass the received stream directly to <code>exec()</code> without buffering the entire stream in the Durable Object. For more information, refer to <a href="/workers/runtime-apis/rpc/#readablestream-writeablestream-request-and-response">Streams over RPC</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7120.md")
</div>
<p>RPC transfers ownership of the stream to the Durable Object. The calling Worker cannot read it after passing it to <code>writeFile()</code>.</p>
<p>The following <code>cat</code> process exits because standard input is omitted:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7121.md")
</div>
<h2 id="set-the-process-context">Set the process context</h2>
<p>Use <code>cwd</code>, <code>env</code>, and <code>user</code> to set the process context. The process inherits the Container environment set by <code>envVars</code>. Per-execution <code>env</code> values add variables or override matching keys.</p>
<p>This example uses <code>sh</code> because it needs expansion and redirection. It also captures standard output and standard error separately.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7122.md")
</div>
<p>The <code>user</code> option sets the user name or numeric user ID (UID) for the process. The Container runtime resolves user names from the container image.</p>
<h2 id="combine-standard-error">Combine standard error</h2>
<p>Set <code>stderr</code> to <code>&quot;combined&quot;</code> to merge standard error into standard output. Combined output requires <code>stdout: &quot;pipe&quot;</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7123.md")
</div>
<p>The merged stream does not guarantee ordering between source streams. In this mode, <code>process.stderr</code> is <code>null</code>, and <code>output.stderr</code> is an empty <code>ArrayBuffer</code>. This example assumes Bash exists in the image.</p>
<h2 id="handle-nonzero-exits">Handle nonzero exits</h2>
<p>A nonzero exit code resolves <code>exitCode</code> normally. It does not reject the promise.</p>
<p>This example preserves standard error while ignoring standard output:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7124.md")
</div>
<p>The result contains exit code <code>7</code> and the standard error text. Its ignored standard output buffer has zero bytes.</p>
<h2 id="stream-large-output">Stream large output</h2>
<p><code>output()</code> buffers both streams in memory. For large output, drain <code>stdout</code> and <code>stderr</code> concurrently instead.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7125.md")
</div>
<p>Streaming and <code>output()</code> are alternative consumption methods. <code>output()</code> throws a <code>TypeError</code> if either stream has started being consumed. A second call to <code>output()</code> also throws a <code>TypeError</code>.</p>
<h3 id="return-standard-output-over-rpc">Return standard output over RPC</h3>
<p>Return a <code>ReadableStream</code> from an RPC method to stream output to the calling Worker. Combining standard error provides one stream for both output channels.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7126.md")
</div>
<p>RPC transfers ownership of the stream to the caller and preserves flow control. The caller must consume or cancel the stream. If the caller stops reading, backpressure can pause a process that continues writing.</p>
<p>This method transfers output, not the <code>ExecProcess</code> handle. Define a separate application protocol when the caller needs completion metadata or process control.</p>
<h2 id="stop-a-process">Stop a process</h2>
<p><code>exec()</code> has no built-in timeout. You can request termination after a delay with <code>kill()</code> and then await <code>exitCode</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7127.md")
</div>
<p>Calling <code>kill()</code> without an argument queues a <code>SIGTERM</code>, signal <code>15</code>. You can pass another signal when the process requires it. A process can handle or ignore a signal, so this is not a hard execution deadline. Observe completion through <code>exitCode</code>, and do not infer a specific exit code from a signal.</p>
<h2 id="coordinate-operations">Coordinate operations</h2>
<p>Place <code>exec()</code> calls in the Durable Object that controls the Container. The Durable Object can coordinate process state and Container lifecycle.</p>
<p>One application RPC method can perform multiple <code>exec()</code> operations. Each command remains a separate exec operation, but the caller makes one Durable Object RPC call. This reduces caller-to-Durable Object round trips while keeping lifecycle decisions together.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7128.md")
</div>
<p>For all fields and return types, refer to the <a href="/durable-objects/api/container/#exec"><code>exec()</code> API contract</a>.</p>
