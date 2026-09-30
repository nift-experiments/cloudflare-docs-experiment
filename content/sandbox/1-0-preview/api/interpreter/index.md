<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13769.md")
</aside>
<p>Methods live on <code>sandbox.interpreter</code> after you attach <code>withInterpreter</code> on your <code>Sandbox</code> subclass. Method names match the stable interpreter; <code>runCode</code> returns plain serializable data. Attach and first run: <a href="/sandbox/1-0-preview/interpreter/">Code interpreter</a>.</p>
<h2 id="createcodecontext"><code>createCodeContext()</code></h2>
<pre><code class="language-ts">createCodeContext(options?: CreateContextOptions): Promise&lt;CodeContext&gt;&#10;</code></pre>
<h3 id="createcontextoptions"><code>CreateContextOptions</code></h3>
<p><code>createCodeContext</code> accepts the following options:</p>
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
<td><code>language</code></td>
<td><code>&quot;python&quot; | &quot;javascript&quot; | &quot;typescript&quot;</code></td>
<td>Interpreter language. Default: <code>python</code>.</td>
</tr>
<tr>
<td><code>cwd</code></td>
<td><code>string</code></td>
<td>Working directory. Default: <code>/workspace</code>.</td>
</tr>
</tbody>
</table>
<h3 id="codecontext"><code>CodeContext</code></h3>
<p>A created context has the following fields:</p>
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
<td><code>id</code></td>
<td><code>string</code></td>
<td>Context id in the current container</td>
</tr>
<tr>
<td><code>language</code></td>
<td><code>string</code></td>
<td>Language of the context</td>
</tr>
<tr>
<td><code>cwd</code></td>
<td><code>string</code></td>
<td>Working directory</td>
</tr>
<tr>
<td><code>createdAt</code></td>
<td><code>Date</code></td>
<td>Created time</td>
</tr>
<tr>
<td><code>lastUsed</code></td>
<td><code>Date</code></td>
<td>Last used time</td>
</tr>
</tbody>
</table>
<h2 id="runcode"><code>runCode()</code></h2>
<pre><code class="language-ts">runCode(code: string, options?: RunCodeOptions): Promise&lt;ExecutionResult&gt;&#10;</code></pre>
<h3 id="runcodeoptions"><code>RunCodeOptions</code></h3>
<p><code>runCode</code> accepts the following options. The callback fields apply to <code>runCode</code> only.</p>
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
<td><code>context</code></td>
<td><code>CodeContext</code></td>
<td>Context to use. If omitted, a default context for <code>language</code> is used.</td>
</tr>
<tr>
<td><code>language</code></td>
<td><code>&quot;python&quot; | &quot;javascript&quot; | &quot;typescript&quot;</code></td>
<td>Used when creating or selecting a default context. Default: <code>python</code>.</td>
</tr>
<tr>
<td><code>onStdout</code></td>
<td><code>(output: OutputMessage) =&gt; void | Promise&lt;void&gt;</code></td>
<td>Called for stdout chunks while running</td>
</tr>
<tr>
<td><code>onStderr</code></td>
<td><code>(output: OutputMessage) =&gt; void | Promise&lt;void&gt;</code></td>
<td>Called for stderr chunks while running</td>
</tr>
<tr>
<td><code>onResult</code></td>
<td><code>(result: ResultData) =&gt; void | Promise&lt;void&gt;</code></td>
<td>Called for rich results (plain data)</td>
</tr>
<tr>
<td><code>onError</code></td>
<td><code>(error: ExecutionError) =&gt; void | Promise&lt;void&gt;</code></td>
<td>Called when the run reports an execution error</td>
</tr>
</tbody>
</table>
<h3 id="outputmessage"><code>OutputMessage</code></h3>
<pre><code class="language-ts">interface OutputMessage {&#10;	text: string;&#10;	timestamp: number;&#10;}&#10;</code></pre>
<h3 id="executionresult"><code>ExecutionResult</code></h3>
<pre><code class="language-ts">interface ExecutionResult {&#10;	code: string;&#10;	logs: {&#10;		stdout: string[];&#10;		stderr: string[];&#10;	};&#10;	error?: ExecutionError;&#10;	executionCount?: number;&#10;	results: ResultData[];&#10;}&#10;</code></pre>
<p><code>ResultData</code> may include plain fields such as <code>text</code>, <code>html</code>, <code>png</code>, <code>jpeg</code>, <code>svg</code>, <code>latex</code>, <code>markdown</code>, <code>json</code>, and <code>chart</code> when the runtime produces them.</p>
<h3 id="executionerror"><code>ExecutionError</code></h3>
<pre><code class="language-ts">interface ExecutionError {&#10;	name: string;&#10;	message: string;&#10;	traceback: string[];&#10;	lineNumber?: number;&#10;}&#10;</code></pre>
<h2 id="runcodestream"><code>runCodeStream()</code></h2>
<pre><code class="language-ts">runCodeStream(&#10;	code: string,&#10;	options?: RunCodeOptions,&#10;): Promise&lt;ReadableStream&lt;Uint8Array&gt;&gt;&#10;</code></pre>
<p>Returns an SSE byte stream of execution events. The TypeScript type reuses <code>RunCodeOptions</code> for <code>context</code> and <code>language</code>, but the stream path does <strong>not</strong> invoke <code>onStdout</code>, <code>onStderr</code>, <code>onResult</code>, or <code>onError</code> — consume the SSE body instead. Canceling the stream may interrupt the in-flight run.</p>
<h2 id="listcodecontexts"><code>listCodeContexts()</code></h2>
<pre><code class="language-ts">listCodeContexts(): Promise&lt;CodeContext[]&gt;&#10;</code></pre>
<h2 id="deletecodecontext"><code>deleteCodeContext()</code></h2>
<pre><code class="language-ts">deleteCodeContext(contextId: string): Promise&lt;void&gt;&#10;</code></pre>
<h2 id="errors">Errors</h2>
<p>Interpreter failures may surface as <code>InterpreterNotReadyError</code>, <code>ContextNotFoundError</code>, or <code>CodeExecutionError</code>. Refer to <a href="/sandbox/1-0-preview/api/errors/">Errors API</a> and <a href="/sandbox/1-0-preview/errors/">Errors and recovery</a>.</p>
<p>Python requires the <strong><code>-python</code></strong> container image variant. Deploy the Worker package and container image from the same preview line.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/1-0-preview/interpreter/">Code interpreter</a></li>
<li><a href="/sandbox/1-0-preview/extensions/">Extensions</a></li>
<li><a href="/sandbox/1-0-preview/api/errors/">Errors API</a></li>
<li>Stable: <a href="/sandbox/api/interpreter/">Interpreter API</a></li>
</ul>
