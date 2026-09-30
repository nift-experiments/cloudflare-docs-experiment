<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 5, 2025</time><h2 id="post-title">Cloudflare Sandbox SDK adds streaming, code interpreter, Git support, process control and more</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>We’ve shipped a major release for the <a href="https://github.com/cloudflare/sandbox-sdk">@cloudflare/sandbox</a> SDK, turning it into a full-featured, container-based execution platform that runs securely on Cloudflare Workers.</p>
<p>This update adds live streaming of output, persistent Python and JavaScript code interpreters with rich output support (charts, tables, HTML, JSON), file system access, Git operations, full background process control, and the ability to expose running services via public URLs.</p>
<p>This makes it ideal for building AI agents, CI runners, cloud REPLs, data analysis pipelines, or full developer tools — all without managing infrastructure.</p>
<h4 id="code-interpreter-python-js-ts">Code interpreter (Python, JS, TS)</h4>
<p>Create persistent code contexts with support for rich visual + structured outputs.</p>
<h4 id="createcodecontext-options">createCodeContext(options)</h4>
<p>Creates a new code execution context with persistent state.</p>
<pre><code class="language-ts">// Create a Python context&#10;const pythonCtx = await sandbox.createCodeContext({ language: &quot;python&quot; });&#10;&#10;// Create a JavaScript context&#10;const jsCtx = await sandbox.createCodeContext({ language: &quot;javascript&quot; });&#10;</code></pre>
<p>Options:</p>
<ul>
<li>language: Programming language ('python' | 'javascript' | 'typescript')</li>
<li>cwd: Working directory (default: /workspace)</li>
<li>envVars: Environment variables for the context</li>
</ul>
<h4 id="runcode-code-options">runCode(code, options)</h4>
<p>Executes code with optional streaming callbacks.</p>
<pre><code class="language-ts">// Simple execution&#10;const execution = await sandbox.runCode(&#x27;print(&quot;Hello World&quot;)&#x27;, {&#10;	context: pythonCtx,&#10;});&#10;&#10;// With streaming callbacks&#10;await sandbox.runCode(&#10;	`&#10;for i in range(5):&#10;    print(f&quot;Step {i}&quot;)&#10;    time.sleep(1)&#10;`,&#10;	{&#10;		context: pythonCtx,&#10;		onStdout: (output) =&gt; console.log(&quot;Real-time:&quot;, output.text),&#10;		onResult: (result) =&gt; console.log(&quot;Result:&quot;, result),&#10;	},&#10;);&#10;</code></pre>
<p>Options:</p>
<ul>
<li>language: Programming language ('python' | 'javascript' | 'typescript')</li>
<li>cwd: Working directory (default: /workspace)</li>
<li>envVars: Environment variables for the context</li>
</ul>
<h4 id="real-time-streaming-output">Real-time streaming output</h4>
<p>Returns a streaming response for real-time processing.</p>
<pre><code class="language-ts">const stream = await sandbox.runCodeStream(&#10;	&quot;import time; [print(i) for i in range(10)]&quot;,&#10;);&#10;// Process the stream as needed&#10;</code></pre>
<h4 id="rich-output-handling">Rich output handling</h4>
<p>Interpreter outputs are auto-formatted and returned in multiple formats:</p>
<ul>
<li>text</li>
<li>html (e.g., Pandas tables)</li>
<li>png, svg (e.g., Matplotlib charts)</li>
<li>json (structured data)</li>
<li>chart (parsed visualizations)</li>
</ul>
<pre><code class="language-ts">const result = await sandbox.runCode(&#10;	`&#10;import seaborn as sns&#10;import matplotlib.pyplot as plt&#10;&#10;data = sns.load_dataset(&quot;flights&quot;)&#10;pivot = data.pivot(&quot;month&quot;, &quot;year&quot;, &quot;passengers&quot;)&#10;sns.heatmap(pivot, annot=True, fmt=&quot;d&quot;)&#10;plt.title(&quot;Flight Passengers&quot;)&#10;plt.show()&#10;&#10;pivot.to_dict()&#10;`,&#10;	{ context: pythonCtx },&#10;);&#10;&#10;if (result.png) {&#10;	console.log(&quot;Chart output:&quot;, result.png);&#10;}&#10;</code></pre>
<h4 id="preview-urls-from-exposed-ports">Preview URLs from Exposed Ports</h4>
<p>Start background processes and expose them with live URLs.</p>
<pre><code class="language-ts">await sandbox.startProcess(&quot;python -m http.server 8000&quot;);&#10;const preview = await sandbox.exposePort(8000);&#10;&#10;console.log(&quot;Live preview at:&quot;, preview.url);&#10;</code></pre>
<h4 id="full-process-lifecycle-control">Full process lifecycle control</h4>
<p>Start, inspect, and terminate long-running background processes.</p>
<pre><code class="language-ts">const process = await sandbox.startProcess(&quot;node server.js&quot;);&#10;console.log(`Started process ${process.id} with PID ${process.pid}`);&#10;&#10;// Monitor the process&#10;const logStream = await sandbox.streamProcessLogs(process.id);&#10;for await (const log of parseSSEStream&lt;LogEvent&gt;(logStream)) {&#10;	console.log(`Server: ${log.data}`);&#10;}&#10;</code></pre>
<ul>
<li>listProcesses() - List all running processes</li>
<li>getProcess(id) - Get detailed process status</li>
<li>killProcess(id, signal) - Terminate specific processes</li>
<li>killAllProcesses() - Kill all processes</li>
<li>streamProcessLogs(id, options) - Stream logs from running processes</li>
<li>getProcessLogs(id) - Get accumulated process output</li>
</ul>
<h4 id="git-integration">Git integration</h4>
<p>Clone Git repositories directly into the sandbox.</p>
<pre><code class="language-ts">await sandbox.gitCheckout(&quot;https://github.com/user/repo&quot;, {&#10;	branch: &quot;main&quot;,&#10;	targetDir: &quot;my-project&quot;,&#10;});&#10;</code></pre>
<p>Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.</p>
</div></article></div>
