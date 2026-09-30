<p>Think provides built-in workspace file tools on every turn, plus integration points for custom tools, code execution, and dynamic extensions.</p>
<h2 id="tool-merge-order">Tool merge order</h2>
<p>On every turn, Think merges tools from multiple sources. Later sources override earlier ones if names collide:</p>
<ol>
<li><strong>Workspace tools</strong> — <code>read</code>, <code>write</code>, <code>edit</code>, <code>list</code>, <code>find</code>, <code>grep</code>, <code>delete</code>, <code>bash</code> (built-in)</li>
<li><strong><code>getTools()</code></strong> — your custom server-side tools</li>
<li><strong>Extension tools</strong> — tools from loaded extensions (prefixed by extension name)</li>
<li><strong>Session tools</strong> — <code>set_context</code>, <code>load_context</code>, <code>search_context</code> (from <code>configureSession</code>)</li>
<li><strong>Skill tools</strong> — <code>activate_skill</code>, <code>read_skill_resource</code>, <code>run_skill_script</code> (from <code>getSkills()</code>, refer to <a href="/agents/runtime/execution/agent-skills/">Agent Skills</a>)</li>
<li><strong>MCP tools</strong> — from connected MCP servers when <code>includeMcpTools</code> is <code>true</code></li>
<li><strong>Client tools</strong> — from the browser (refer to <a href="/agents/harnesses/think/client-tools/">Client tools</a>)</li>
</ol>
<p>Tools belong to the agent running the turn. For parent-child orchestration, use <a href="/agents/runtime/execution/agent-tools/">Agents as tools</a> instead of passing one-off tools through <code>chat()</code>.</p>
<h2 id="built-in-workspace-tools">Built-in workspace tools</h2>
<p>Every Think agent gets <code>this.workspace</code> — a virtual filesystem backed by Durable Object SQLite. Workspace tools are automatically available to the model with no configuration.</p>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>read</code></td>
<td>Read text with line numbers; pass images and PDFs to multimodal models</td>
</tr>
<tr>
<td><code>write</code></td>
<td>Write content to a file (creates parent directories)</td>
</tr>
<tr>
<td><code>edit</code></td>
<td>Apply a find-and-replace edit to an existing file (supports fuzzy matching)</td>
</tr>
<tr>
<td><code>list</code></td>
<td>List files and directories in a path</td>
</tr>
<tr>
<td><code>find</code></td>
<td>Find files matching a glob pattern</td>
</tr>
<tr>
<td><code>grep</code></td>
<td>Search file contents by regex or fixed string</td>
</tr>
<tr>
<td><code>delete</code></td>
<td>Delete a file or directory</td>
</tr>
<tr>
<td><code>bash</code></td>
<td>Run a sandboxed Bash script against workspace files</td>
</tr>
</tbody>
</table>
<p>The <code>bash</code> tool is enabled by default. It mounts workspace files into a <code>just-bash</code> virtual filesystem, runs with network access disabled, and writes created, updated, and deleted files and empty directories back to the workspace. Use it for shell-style workflows that combine multiple file operations; use the narrower tools for simple reads, writes, and edits.</p>
<p>To keep tool calls bounded, the Bash tool snapshots up to 1,000 workspace files by default and skips files larger than 1 MB. Skipped files are reported in the tool result and are treated as protected during write-back so the script cannot accidentally overwrite or delete content that was not mounted. You can tune <code>maxWorkspaceFiles</code>, <code>maxWorkspaceFileBytes</code>, <code>maxOutputBytes</code>, <code>timeout</code>, and <code>network</code> through <code>workspaceBash</code>.</p>
<p>Disable the default Bash tool for conservative deployments:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2101.md")
</div>
<h3 id="r2-spillover">R2 spillover</h3>
<p>By default, the workspace stores everything in SQLite. For large files, override <code>workspace</code> to add R2 spillover:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2102.md")
</div>
<p>This requires an R2 bucket binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2103.md")
</div>
<h2 id="custom-tools">Custom tools</h2>
<p>Override <code>getTools()</code> to add your own tools. These are standard AI SDK <code>tool()</code> definitions with schemas from a library like Zod or Valibot:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2104.md")
</div>
<p>Custom tools are merged with workspace tools automatically. If a custom tool has the same name as a workspace tool, the custom tool wins.</p>
<h2 id="tool-approval">Tool approval</h2>
<p>Tools can require user approval before execution using the <code>needsApproval</code> option:</p>
<pre><code class="language-ts">getTools(): ToolSet {&#10;	return {&#10;		deleteFile: tool({&#10;			description: &quot;Delete a file from the system&quot;,&#10;			inputSchema: z.object({ path: z.string() }),&#10;			needsApproval: async ({ path }) =&gt; path.startsWith(&quot;/important/&quot;),&#10;			execute: async ({ path }) =&gt; {&#10;				await this.workspace.rm(path);&#10;				return { deleted: path };&#10;			},&#10;		}),&#10;	};&#10;}&#10;</code></pre>
<p>When <code>needsApproval</code> returns <code>true</code>, the tool call is sent to the client for approval. The conversation pauses until the client responds with <code>CF_AGENT_TOOL_APPROVAL</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2100.md")
</aside>
<h2 id="per-turn-tool-overrides">Per-turn tool overrides</h2>
<p>The <code>beforeTurn</code> hook can restrict or add tools for a specific turn:</p>
<pre><code class="language-ts">beforeTurn(ctx: TurnContext) {&#10;	return {&#10;		activeTools: [&quot;read&quot;, &quot;write&quot;, &quot;getWeather&quot;],&#10;		tools: { emergencyTool: this.createEmergencyTool() },&#10;	};&#10;}&#10;</code></pre>
<p><code>activeTools</code> limits which tools the model can call. <code>tools</code> adds extra tools for this turn only (merged on top of existing tools).</p>
<h2 id="mcp-tools">MCP tools</h2>
<p>Think inherits MCP client support from the <code>Agent</code> base class. By default, Think converts tools from connected MCP servers to AI SDK tools and adds them to every turn.</p>
<p>Set <code>waitForMcpConnections</code> to ensure MCP servers are connected before inference runs:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2105.md")
</div>
<p>If you expose MCP tools through Code Mode or another mechanism outside Think's automatic tool set, turn off direct AI SDK tool exposure:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2106.md")
</div>
<p><code>includeMcpTools</code> controls only the automatic model tool merge. MCP connections still register, restore, discover, and wait. Raw catalog access, direct calls, Code Mode connectors, and explicit <code>this.mcp.getAITools()</code> calls continue to work.</p>
<p>Use this property instead of removing MCP tool names through <code>activeTools</code> in <code>beforeTurn</code>. Think converts MCP schemas before it calls <code>beforeTurn</code>, so <code>activeTools</code> cannot avoid that conversion. To configure a connector runtime, refer to <a href="/agents/tools/codemode/mcp/">Use MCP tools with Code Mode</a>.</p>
<p>Add MCP servers programmatically or via <code>@callable</code> methods:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2107.md")
</div>
<h2 id="code-execution-tool">Code execution tool</h2>
<p>Let the LLM write and run JavaScript in a sandboxed Worker, recorded on a durable Code Mode runtime (abort-and-replay, human approvals, audit trail, reusable snippets). Requires <code>@cloudflare/codemode</code> and a <code>worker_loaders</code> binding.</p>
<pre><code class="language-sh">npm install @cloudflare/codemode&#10;</code></pre>
<p>The one-liner infers everything from the agent — <code>state.*</code> from <code>this.workspace</code>, the executor from <code>env.LOADER</code>, and a live browser (<code>cdp.*</code>) from <code>env.BROWSER</code> if bound:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2108.md")
</div>
<p>Setup checklist:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2109.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2110.md")
</div>
<p>Each missing piece fails with an error naming the step.</p>
<p>Inside the sandbox the model sees typed namespaces plus the platform SDK:</p>
<ul>
<li><code>tools.*</code> — your AI SDK tools (object args, validated against their schemas). Only tools with an <code>execute</code> function are exposed — client-side tools cannot run in the sandbox.</li>
<li><code>state.*</code> — the workspace filesystem (<code>state.readFile({ path })</code>, <code>state.glob({ pattern })</code>, <code>state.planEdits(...)</code>, and so on).</li>
<li><code>cdp.*</code> — the browser, when a Browser Run binding is configured. The execute tool defaults to <code>session: { mode: &quot;dynamic&quot; }</code>: sessions are per-execution unless the model promotes one with <code>cdp.startSession()</code>.</li>
<li><code>codemode.search</code> / <code>codemode.describe</code> / <code>codemode.step</code> / <code>codemode.run</code> — discovery, side-effect boundaries, and saved snippets.</li>
</ul>
<p>Pass overrides for anything beyond the defaults — for example, custom <code>tools.*</code> alongside the agent-derived state:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2111.md")
</div>
<p>Or fully explicit options (no agent inference):</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2112.md")
</div>
<h3 id="approvals-human-in-the-loop">Approvals (human-in-the-loop)</h3>
<p>An AI SDK tool with <code>needsApproval</code> does not run immediately inside the sandbox — calling it <strong>pauses the run durably</strong>. The pause comes back as a normal tool output (<code>{ status: &quot;paused&quot;, executionId, pending }</code>), the model tells the user what it needs, and the turn ends. This differs from the client-side approval flow for plain <code>getTools()</code> tools: inside the sandbox a function-valued <code>needsApproval</code> cannot be evaluated against the call's arguments ahead of time, so it conservatively <strong>always</strong> requires approval. Think ships built-in callables to resolve it:</p>
<ul>
<li><code>approveExecution(executionId)</code> — resumes the run where it stopped. Already-done work is replayed, not re-executed. The outcome replaces the paused output in the transcript and the chat auto-continues.</li>
<li><code>rejectExecution(executionId, reason?)</code> — ends the run with <code>{ status: &quot;rejected&quot;, reason }</code> so the model can adapt.</li>
<li><code>pendingExecutions()</code> — pending actions (with full args) for rendering approval UI.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2099.md")
</aside>
<p>For a working approval card, refer to the <a href="https://github.com/cloudflare/agents/tree/main/examples/assistant"><code>assistant</code> example</a>.</p>
<h3 id="the-runtime-handle">The runtime handle</h3>
<p><code>createExecuteRuntime</code> returns the moving parts when the host needs more than the tool — and the handle is also assigned to <code>this.codemode</code> when created from an agent:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2113.md")
</div>
<h2 id="browser-tools">Browser tools</h2>
<p>Give your agent access to the Chrome DevTools Protocol (CDP) for web page inspection, scraping, screenshots, and debugging. Requires <code>@cloudflare/codemode</code> and a Browser Run binding.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2114.md")
</div>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2115.md")
</div>
<p>This adds the durable CDP tool plus stateless <a href="/agents/tools/browser/#quick-actions">Quick Action</a> tools when a <code>browser</code> binding is present:</p>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>browser_execute</code></td>
<td>Run JavaScript against a live browser over CDP (screenshots, DOM reads, JS evaluation).</td>
</tr>
<tr>
<td><code>browser_markdown</code></td>
<td>Read a page or raw HTML as Markdown.</td>
</tr>
<tr>
<td><code>browser_extract</code></td>
<td>Extract structured data from a page with AI.</td>
</tr>
<tr>
<td><code>browser_links</code></td>
<td>List links on a page.</td>
</tr>
<tr>
<td><code>browser_scrape</code></td>
<td>Scrape specific elements by CSS selector.</td>
</tr>
</tbody>
</table>
<p>Pass <code>quickActions: false</code> to keep only <code>browser_execute</code>, or pass <code>quickActions: { actions, maxChars, options }</code> to configure the stateless tools. The Quick Action tools share the <code>browser</code> binding, need no Worker Loader, and resolve <code>ctx</code> from the current Agent automatically. To use only the stateless tools, import <code>createQuickActionTools</code> from <code>@cloudflare/think/tools/browser</code>.</p>
<p>The tool is backed by a Code Mode runtime with the <code>cdp</code> connector: the model writes async arrow functions that run in a sandboxed Worker isolate, with <code>cdp.send()</code>, <code>cdp.attachToTarget()</code>, <code>cdp.spec()</code> (the live, normalized protocol description), session helpers (<code>cdp.startSession()</code>, <code>cdp.sessionInfo()</code>, <code>cdp.closeSession()</code>), and debug-log helpers. Executions are recorded for abort-and-replay, so browser sessions survive approval pauses.</p>
<p>By default each execution gets a fresh browser session (<code>one-shot</code>), torn down when the run ends. Pass <code>session: { mode: &quot;dynamic&quot; }</code> to let the model promote a session with <code>cdp.startSession()</code> so later executions continue in the same browser, or <code>session: { mode: &quot;reuse&quot;, key }</code> for a named long-lived session. Stale sessions are reclaimed by the connector's <code>sweep()</code> — call it from a scheduled task.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2098.md")
</aside>
<p>For a custom Chrome endpoint, pass <code>cdpUrl</code> instead of <code>browser</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2116.md")
</div>
<p>For the full CDP connector API, refer to <a href="/agents/tools/browser/">Browse the web</a>.</p>
<h2 id="extensions">Extensions</h2>
<p>Extensions are dynamically loaded sandboxed Workers that add tools at runtime. The LLM can write extension source code, load it, and use the new tools on the next turn.</p>
<p>Extensions require a <code>worker_loaders</code> binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2117.md")
</div>
<h3 id="static-extensions">Static extensions</h3>
<p>Define extensions that load at startup:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2118.md")
</div>
<p>Extension tools are namespaced — a <code>math</code> extension with an <code>add</code> tool becomes <code>math_add</code> in the model's tool set.</p>
<h3 id="llm-driven-extensions">LLM-driven extensions</h3>
<p>Give the model <code>createExtensionTools</code> so it can load extensions dynamically:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2119.md")
</div>
<p>This gives the model two tools:</p>
<ul>
<li><code>load_extension</code> — load a new extension from JavaScript source</li>
<li><code>list_extensions</code> — list currently loaded extensions</li>
</ul>
<h3 id="extension-context-blocks">Extension context blocks</h3>
<p>Extensions can declare context blocks in their manifest. These are automatically registered with the Session:</p>
<pre><code class="language-ts">getExtensions() {&#10;	return [{&#10;		manifest: {&#10;			name: &quot;notes&quot;,&#10;			version: &quot;1.0.0&quot;,&#10;			permissions: { network: false },&#10;			context: [&#10;				{ label: &quot;scratchpad&quot;, description: &quot;Extension scratch space&quot;, maxTokens: 500 },&#10;			],&#10;		},&#10;		source: `({ tools: { /* ... */ } })`,&#10;	}];&#10;}&#10;</code></pre>
<p>The context block is registered as <code>notes_scratchpad</code> (namespaced by extension name).</p>
<h2 id="custom-workspace-backends">Custom workspace backends</h2>
<p>The individual tool factories are exported for use with custom storage backends:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2120.md")
</div>
<p>Implement the operations interface for your storage backend:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2121.md")
</div>
<p>Or create the full set from a <code>Workspace</code>, optionally disabling the Bash tool:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2122.md")
</div>
