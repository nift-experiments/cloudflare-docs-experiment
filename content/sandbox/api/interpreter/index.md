<p>Execute Python, JavaScript, and TypeScript code with support for data visualizations, tables, and rich output formats. Contexts maintain state (variables, imports, functions) across executions.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13635.md")
</aside>
<h2 id="methods">Methods</h2>
<h3 id="createcodecontext"><code>createCodeContext()</code></h3>
<p>Create a persistent execution context for running code.</p>
<pre><code class="language-ts">const context = await sandbox.createCodeContext(options?: CreateContextOptions): Promise&lt;CodeContext&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>options</code> (optional):
<ul>
<li><code>language</code> - <code>&quot;python&quot; | &quot;javascript&quot; | &quot;typescript&quot;</code> (default: <code>&quot;python&quot;</code>)</li>
<li><code>cwd</code> - Working directory (default: <code>&quot;/workspace&quot;</code>)</li>
<li><code>envVars</code> - Environment variables</li>
<li><code>timeout</code> - Request timeout in milliseconds (default: 30000)</li>
</ul>
</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;CodeContext&gt;</code> with <code>id</code>, <code>language</code>, <code>cwd</code>, <code>createdAt</code>, <code>lastUsed</code></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13636.md")
</div>
<h3 id="runcode"><code>runCode()</code></h3>
<p>Execute code in a context and return the complete result.</p>
<pre><code class="language-ts">const result = await sandbox.runCode(code: string, options?: RunCodeOptions): Promise&lt;ExecutionResult&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>code</code> - The code to execute (required)</li>
<li><code>options</code> (optional):
<ul>
<li><code>context</code> - Context to run in (recommended - see below)</li>
<li><code>language</code> - <code>&quot;python&quot; | &quot;javascript&quot; | &quot;typescript&quot;</code> (default: <code>&quot;python&quot;</code>)</li>
<li><code>timeout</code> - Execution timeout in milliseconds (default: 60000)</li>
<li><code>onStdout</code>, <code>onStderr</code>, <code>onResult</code>, <code>onError</code> - Streaming callbacks</li>
</ul>
</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;ExecutionResult&gt;</code> with:</p>
<ul>
<li><code>code</code> - The executed code</li>
<li><code>logs</code> - <code>stdout</code> and <code>stderr</code> arrays</li>
<li><code>results</code> - Array of rich outputs (see <a href="#rich-output-formats">Rich Output Formats</a>)</li>
<li><code>error</code> - Execution error if any</li>
<li><code>executionCount</code> - Execution counter</li>
</ul>
<p><strong>Recommended usage - create explicit context</strong>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13637.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="default-context-behavior">Default context behavior</h3>
@markup("md", "content/.markup/bodies/13634.md")
</aside>
<p><strong>Error handling</strong>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13638.md")
</div>
<p><strong>JavaScript and TypeScript features</strong>:</p>
<p>JavaScript and TypeScript code execution supports top-level <code>await</code> and persistent variables across executions within the same context.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13639.md")
</div>
<p>Variables declared with <code>const</code>, <code>let</code>, or <code>var</code> persist across executions, enabling multi-step workflows:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13640.md")
</div>
<h3 id="listcodecontexts"><code>listCodeContexts()</code></h3>
<p>List all active code execution contexts.</p>
<pre><code class="language-ts">const contexts = await sandbox.listCodeContexts(): Promise&lt;CodeContext[]&gt;&#10;</code></pre>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13641.md")
</div>
<h3 id="deletecodecontext"><code>deleteCodeContext()</code></h3>
<p>Delete a code execution context and free its resources.</p>
<pre><code class="language-ts">await sandbox.deleteCodeContext(contextId: string): Promise&lt;void&gt;&#10;</code></pre>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13642.md")
</div>
<h2 id="rich-output-formats">Rich Output Formats</h2>
<p>Results include: <code>text</code>, <code>html</code>, <code>png</code>, <code>jpeg</code>, <code>svg</code>, <code>latex</code>, <code>markdown</code>, <code>json</code>, <code>chart</code>, <code>data</code></p>
<p><strong>Charts (matplotlib)</strong>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13643.md")
</div>
<p><strong>Tables (pandas)</strong>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13644.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/tutorials/ai-code-executor/">Build an AI Code Executor</a> - Complete tutorial</li>
<li><a href="/sandbox/api/commands/">Commands API</a> - Lower-level command execution</li>
<li><a href="/sandbox/api/files/">Files API</a> - File operations</li>
</ul>
