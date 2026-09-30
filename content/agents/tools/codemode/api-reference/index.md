<p>Code Mode publishes six package entry points. Import framework-specific APIs from their matching entry point:</p>
<table>
<thead>
<tr>
<th>Entry point</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cloudflare/codemode</code></td>
<td>Runtime, connectors, Workers executor, and framework-independent utilities</td>
</tr>
<tr>
<td><code>@cloudflare/codemode/ai</code></td>
<td>AI SDK tools and connector adapter</td>
</tr>
<tr>
<td><code>@cloudflare/codemode/mcp</code></td>
<td>Model Context Protocol (MCP) server wrappers</td>
</tr>
<tr>
<td><code>@cloudflare/codemode/tanstack-ai</code></td>
<td>TanStack AI tools and adapter</td>
</tr>
<tr>
<td><code>@cloudflare/codemode/browser</code></td>
<td>Browser tool descriptor and iframe executor</td>
</tr>
<tr>
<td><code>@cloudflare/codemode/vite</code></td>
<td>Vite plugin for connector discovery and Worker exports</td>
</tr>
</tbody>
</table>
<h2 id="cloudflare-codemode"><code>@cloudflare/codemode</code></h2>
<p>The main entry point does not require the optional AI SDK, TanStack AI, or Zod peer dependencies to be installed.</p>
<h3 id="runtime-construction">Runtime construction</h3>
<h4 id="createcodemoderuntime"><code>createCodemodeRuntime()</code></h4>
<pre><code class="language-ts">function createCodemodeRuntime(&#10;	options: CreateCodemodeRuntimeOptions,&#10;): CodemodeRuntimeHandle;&#10;</code></pre>
<p>Creates the host-side control plane for a named Code Mode runtime.</p>
<p><code>CreateCodemodeRuntimeOptions</code> has these fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ctx</code></td>
<td><code>DurableObjectState</code></td>
<td>Yes</td>
<td>Durable Object state that hosts the runtime facet.</td>
</tr>
<tr>
<td><code>connectors</code></td>
<td><code>CodemodeConnector[]</code></td>
<td>Yes</td>
<td>Connectors exposed as sandbox globals. Connector names must be unique, and <code>codemode</code> is reserved.</td>
</tr>
<tr>
<td><code>executor</code></td>
<td><code>Executor</code></td>
<td>Yes</td>
<td>Sandbox that runs generated code.</td>
</tr>
<tr>
<td><code>name</code></td>
<td><code>string</code></td>
<td>No</td>
<td>Durable runtime identity. Defaults to <code>&quot;default&quot;</code>. Valid characters are letters, digits, <code>_</code>, <code>-</code>, and <code>.</code>.</td>
</tr>
<tr>
<td><code>maxExecutions</code></td>
<td><code>number</code></td>
<td>No</td>
<td>Terminal records kept when a new run begins. Defaults to <code>50</code>. Running and paused executions are not pruned.</td>
</tr>
<tr>
<td><code>transformResult</code></td>
<td><code>TransformResult</code></td>
<td>No</td>
<td>Reshapes a completed result returned to the model. The audit trail retains the unmodified result.</td>
</tr>
</tbody>
</table>
<pre><code class="language-ts">interface CodemodeRuntimeHandle {&#10;	tool(&#10;		options?: CodemodeRuntimeToolOptions,&#10;	): Tool&lt;ProxyToolInput, ProxyToolOutput&gt;;&#10;	execute(input: ProxyToolInput): Promise&lt;ProxyToolOutput&gt;;&#10;	search(query: string): Promise&lt;SearchOutput&gt;;&#10;	describe(target: string): Promise&lt;DescribeOutput&gt;;&#10;	approve(options: CodemodeApproveOptions): Promise&lt;ProxyToolOutput&gt;;&#10;	reject(options: CodemodeRejectOptions): Promise&lt;boolean&gt;;&#10;	rollback(options: CodemodeRollbackOptions): Promise&lt;void&gt;;&#10;	pending(executionId?: string): Promise&lt;PendingAction[]&gt;;&#10;	expirePaused(options?: CodemodeExpireOptions): Promise&lt;string[]&gt;;&#10;	executions(limit?: number): Promise&lt;ExecutionState[]&gt;;&#10;	deleteExecution(id: string): Promise&lt;boolean&gt;;&#10;	pruneExecutions(keep?: number): Promise&lt;number&gt;;&#10;	saveSnippet(name: string, options: SaveSnippetOptions): Promise&lt;Snippet&gt;;&#10;	snippets(): Promise&lt;Snippet[]&gt;;&#10;	deleteSnippet(name: string): Promise&lt;boolean&gt;;&#10;}&#10;</code></pre>
<p>The handle methods have these effects:</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>Effect</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>tool(options?)</code></td>
<td>Returns the AI SDK tool given to the model. <code>description</code> replaces the default description. <code>connectorHints</code> adds a one-line hint for each connector when using the default description.</td>
</tr>
<tr>
<td><code>execute({ code })</code></td>
<td>Runs code directly without adapting the runtime to an AI SDK tool. The result can complete, pause for approval, or return an error status.</td>
</tr>
<tr>
<td><code>search(query)</code></td>
<td>Searches connector methods and saved snippets without running sandbox code.</td>
</tr>
<tr>
<td><code>describe(target)</code></td>
<td>Returns on-demand TypeScript documentation for a connector, method, or saved snippet.</td>
</tr>
<tr>
<td><code>approve({ executionId })</code></td>
<td>Resumes a paused execution through replay. The result can complete, pause again, or return an error status. It does not revive a non-paused execution.</td>
</tr>
<tr>
<td><code>reject({ seq, executionId })</code></td>
<td>Rejects one pending action and terminates the execution. Returns <code>false</code> if the action is no longer pending. It does not roll back earlier actions.</td>
</tr>
<tr>
<td><code>rollback({ executionId })</code></td>
<td>Calls available <code>revert</code> functions in reverse call order. Missing connectors and methods without <code>revert</code> remain applied. It attempts later reverts after a failure.</td>
</tr>
<tr>
<td><code>pending(executionId?)</code></td>
<td>Lists pending actions. Without an ID, it combines actions from all paused executions.</td>
</tr>
<tr>
<td><code>expirePaused({ maxAgeMs? })</code></td>
<td>Terminates stale paused or running executions and returns their IDs. The default age is 24 hours.</td>
</tr>
<tr>
<td><code>executions(limit?)</code></td>
<td>Returns audit records, newest first.</td>
</tr>
<tr>
<td><code>deleteExecution(id)</code></td>
<td>Deletes one audit record. It also disposes resources for a non-terminal execution. Returns whether the record existed.</td>
</tr>
<tr>
<td><code>pruneExecutions(keep?)</code></td>
<td>Deletes older terminal records and returns the count deleted. Defaults to keeping <code>50</code>.</td>
</tr>
<tr>
<td><code>saveSnippet(name, options)</code></td>
<td>Saves code from <code>options.executionId</code> as a reusable snippet. It accepts any execution status, so applications should verify successful completion first. Replaces the same name.</td>
</tr>
<tr>
<td><code>snippets()</code></td>
<td>Returns saved snippets, ordered by name.</td>
</tr>
<tr>
<td><code>deleteSnippet(name)</code></td>
<td>Deletes a snippet and returns whether it existed.</td>
</tr>
</tbody>
</table>
<p>The method option types are:</p>
<pre><code class="language-ts">type CodemodeRuntimeToolOptions = {&#10;	description?: string;&#10;	connectorHints?: Record&lt;string, string&gt;;&#10;};&#10;&#10;type CodemodeApproveOptions = { executionId: string };&#10;type CodemodeRejectOptions = { seq: number; executionId: string };&#10;type CodemodeRollbackOptions = { executionId: string };&#10;type CodemodeExpireOptions = { maxAgeMs?: number };&#10;</code></pre>
<h4 id="codemoderuntime"><code>CodemodeRuntime</code></h4>
<pre><code class="language-ts">class CodemodeRuntime extends DurableObject&lt;unknown&gt; {&#10;	constructor(ctx: DurableObjectState, env: unknown);&#10;}&#10;</code></pre>
<p><code>CodemodeRuntime</code> is the durable facet behind the runtime handle. The Vite plugin exports this class from the Worker entry module. Use <code>createCodemodeRuntime()</code> for application code instead of constructing the facet directly.</p>
<p>The main entry point also exports these runtime constants:</p>
<table>
<thead>
<tr>
<th>Constant</th>
<th>Value</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>DEFAULT_MAX_EXECUTIONS</code></td>
<td><code>50</code></td>
<td>Default terminal execution retention count</td>
</tr>
<tr>
<td><code>DEFAULT_PAUSED_TTL_MS</code></td>
<td><code>86400000</code></td>
<td>Default stale execution age in milliseconds (24 hours)</td>
</tr>
<tr>
<td><code>MAX_DURABLE_VALUE_BYTES</code></td>
<td><code>1000000</code></td>
<td>Serialized JavaScript string-length limit for one durable value</td>
</tr>
</tbody>
</table>
<h3 id="runtime-tool-input-and-output">Runtime tool input and output</h3>
<pre><code class="language-ts">type ProxyToolInput = { code: string };&#10;&#10;type ProxyToolOutput =&#10;	| {&#10;			status: &quot;completed&quot;;&#10;			executionId: string;&#10;			result: unknown;&#10;			logs?: string[];&#10;	  }&#10;	| {&#10;			status: &quot;paused&quot;;&#10;			executionId: string;&#10;			pending: PendingAction[];&#10;	  }&#10;	| {&#10;			status: &quot;error&quot;;&#10;			executionId: string;&#10;			error: string;&#10;			logs?: string[];&#10;	  };&#10;&#10;type TransformResult = (result: unknown) =&gt; unknown | Promise&lt;unknown&gt;;&#10;</code></pre>
<p>Sandbox and replay errors use the <code>error</code> output variant. They do not throw through the model tool call.</p>
<h3 id="execution-records">Execution records</h3>
<pre><code class="language-ts">type ExecutionStatus =&#10;	| &quot;running&quot;&#10;	| &quot;paused&quot;&#10;	| &quot;completed&quot;&#10;	| &quot;error&quot;&#10;	| &quot;rejected&quot;&#10;	| &quot;rolled_back&quot;;&#10;&#10;type ExecutionState = {&#10;	id: string;&#10;	code: string;&#10;	status: ExecutionStatus;&#10;	log: ToolLogEntry[];&#10;	result?: unknown;&#10;	error?: string;&#10;	logs?: string[];&#10;	connectors?: string[];&#10;	createdAt: number;&#10;	updatedAt: number;&#10;};&#10;&#10;type ToolLogEntry = {&#10;	seq: number;&#10;	connector: string;&#10;	method: string;&#10;	args: unknown;&#10;	result?: unknown;&#10;	requiresApproval: boolean;&#10;	ephemeral?: boolean;&#10;	state: &quot;executing&quot; | &quot;applied&quot; | &quot;pending&quot; | &quot;reverted&quot; | &quot;error&quot;;&#10;};&#10;&#10;type PendingAction = {&#10;	executionId: string;&#10;	seq: number;&#10;	connector: string;&#10;	method: string;&#10;	args: unknown;&#10;};&#10;</code></pre>
<p><code>createdAt</code> and <code>updatedAt</code> contain epoch milliseconds. An ephemeral log entry comes from a connector tool with <code>replay: &quot;reexecute&quot;</code>. Its result is not stored and the call runs again during replay.</p>
<p>The runtime decision type is:</p>
<pre><code class="language-ts">type ToolDecision =&#10;	| { kind: &quot;replay&quot;; result: unknown }&#10;	| { kind: &quot;execute&quot;; seq: number }&#10;	| { kind: &quot;pause&quot;; seq: number };&#10;</code></pre>
<h3 id="sandbox-codemode-api">Sandbox <code>codemode</code> API</h3>
<p><code>runtime.tool()</code> injects a <code>codemode</code> global into generated sandbox code.</p>
<pre><code class="language-ts">declare const codemode: {&#10;	search(query: string): Promise&lt;SearchOutput&gt;;&#10;	describe(target: string): Promise&lt;DescribeOutput&gt;;&#10;	step&lt;T&gt;(name: string, fn: () =&gt; T | Promise&lt;T&gt;): Promise&lt;T&gt;;&#10;	run(name: string, input?: unknown): Promise&lt;unknown&gt;;&#10;};&#10;</code></pre>
<p>The sandbox methods behave as follows:</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>search(query)</code></td>
<td>Searches connector methods and saved snippets. Results are ranked and limited to <code>50</code>.</td>
</tr>
<tr>
<td><code>describe(target)</code></td>
<td>Returns generated TypeScript for a connector, <code>connector.method</code>, or snippet name.</td>
</tr>
<tr>
<td><code>step(name, fn)</code></td>
<td>Runs a closure once and records its result. Replay returns the recorded result without running the closure again.</td>
</tr>
<tr>
<td><code>run(name, input?)</code></td>
<td>Runs a saved snippet. A missing snippet or recorded connector resolves to an object with an <code>error</code> property.</td>
</tr>
</tbody>
</table>
<p>Use <code>step()</code> around nondeterministic or side-effectful sandbox work that does not use a connector. Issue connector calls sequentially when an execution can pause. Concurrent calls can reach the replay cursor in a different order.</p>
<p>The discovery output types are:</p>
<pre><code class="language-ts">type SearchResult = {&#10;	path: string;&#10;	connector: string;&#10;	method: string;&#10;	description?: string;&#10;	requiresApproval?: boolean;&#10;	kind: &quot;method&quot; | &quot;snippet&quot;;&#10;	score: number;&#10;};&#10;&#10;type SearchOutput = {&#10;	results: SearchResult[];&#10;	total: number;&#10;	truncated: boolean;&#10;};&#10;&#10;type DescribeOutput = {&#10;	path: string;&#10;	description?: string;&#10;	requiresApproval?: boolean;&#10;	types: string;&#10;	kind: &quot;connector&quot; | &quot;method&quot; | &quot;snippet&quot;;&#10;};&#10;</code></pre>
<p><code>requiresApproval</code> is <code>true</code> when a connector method pauses before execution. It is omitted for methods that do not require approval and for snippets.</p>
<h3 id="snippet-types">Snippet types</h3>
<pre><code class="language-ts">interface SaveSnippetOptions {&#10;	description?: string;&#10;	inputSchema?: unknown;&#10;	executionId: string;&#10;}&#10;&#10;interface Snippet {&#10;	name: string;&#10;	description: string;&#10;	code: string;&#10;	savedAt: number;&#10;	inputSchema?: unknown;&#10;	connectors?: string[];&#10;}&#10;</code></pre>
<p><code>connectors</code> records every namespace configured when the source execution started. <code>savedAt</code> contains epoch milliseconds. Before calling <code>saveSnippet()</code>, verify that the source <code>ExecutionState.status</code> is <code>completed</code>.</p>
<h3 id="executor-api">Executor API</h3>
<h4 id="executor"><code>Executor</code></h4>
<pre><code class="language-ts">interface Executor {&#10;	execute(&#10;		code: string,&#10;		providersOrFns:&#10;			| ResolvedProvider[]&#10;			| Record&lt;string, (...args: unknown[]) =&gt; Promise&lt;unknown&gt;&gt;,&#10;		options?: ExecuteOptions,&#10;	): Promise&lt;ExecuteResult&gt;;&#10;}&#10;</code></pre>
<p>Custom executors should report failures in <code>ExecuteResult.error</code> instead of throwing.</p>
<pre><code class="language-ts">interface ExecuteResult {&#10;	result: unknown;&#10;	error?: string;&#10;	logs?: string[];&#10;}&#10;&#10;interface ResolvedProvider {&#10;	name: string;&#10;	fns: Record&lt;string, (...args: unknown[]) =&gt; Promise&lt;unknown&gt;&gt;;&#10;	prelude?: string;&#10;}&#10;&#10;interface ConnectorBinding {&#10;	name: string;&#10;	binding: {&#10;		callTool(method: string, args: unknown): Promise&lt;unknown&gt;;&#10;	};&#10;}&#10;&#10;interface ExecuteOptions {&#10;	connectors?: ConnectorBinding[];&#10;}&#10;</code></pre>
<p>Passing a function record instead of <code>ResolvedProvider[]</code> is deprecated. It creates one provider named <code>codemode</code>.</p>
<h4 id="dynamicworkerexecutor"><code>DynamicWorkerExecutor</code></h4>
<pre><code class="language-ts">class DynamicWorkerExecutor implements Executor {&#10;	constructor(options: DynamicWorkerExecutorOptions);&#10;	execute(&#10;		code: string,&#10;		providersOrFns:&#10;			| ResolvedProvider[]&#10;			| Record&lt;string, (...args: unknown[]) =&gt; Promise&lt;unknown&gt;&gt;,&#10;		options?: ExecuteOptions,&#10;	): Promise&lt;ExecuteResult&gt;;&#10;}&#10;</code></pre>
<p><code>DynamicWorkerExecutorOptions</code> has these fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>loader</code></td>
<td><code>WorkerLoader</code></td>
<td>Yes</td>
<td>—</td>
<td>Worker Loader binding used to create isolated Workers.</td>
</tr>
<tr>
<td><code>timeout</code></td>
<td><code>number</code></td>
<td>No</td>
<td><code>60000</code></td>
<td>Execution timeout in milliseconds.</td>
</tr>
<tr>
<td><code>globalOutbound</code></td>
<td><code>Fetcher | null</code></td>
<td>No</td>
<td><code>null</code></td>
<td>Outbound network policy. <code>null</code> blocks access. A <code>Fetcher</code> receives all outbound requests.</td>
</tr>
<tr>
<td><code>modules</code></td>
<td><code>Record&lt;string, string&gt;</code></td>
<td>No</td>
<td><code>{}</code></td>
<td>Module source keyed by import specifier. The reserved <code>executor.js</code> key is ignored.</td>
</tr>
<tr>
<td><code>bindings</code></td>
<td><code>Record&lt;string, unknown&gt;</code></td>
<td>No</td>
<td><code>{}</code></td>
<td>Additional environment bindings injected into each sandbox Worker.</td>
</tr>
</tbody>
</table>
<p>The executor validates provider and connector namespaces. Names must be valid JavaScript identifiers, unique, and must not shadow executor globals.</p>
<h4 id="tooldispatcher"><code>ToolDispatcher</code></h4>
<pre><code class="language-ts">class ToolDispatcher extends RpcTarget {&#10;	constructor(fns: Record&lt;string, (...args: unknown[]) =&gt; Promise&lt;unknown&gt;&gt;);&#10;	call(name: string, argsJson?: string): Promise&lt;string&gt;;&#10;}&#10;</code></pre>
<p><code>ToolDispatcher</code> is the Workers RPC bridge used by <code>DynamicWorkerExecutor</code>. <code>call()</code> accepts serialized positional arguments and returns a serialized result or error envelope.</p>
<h4 id="runcode"><code>runCode()</code></h4>
<pre><code class="language-ts">function runCode(options: {&#10;	code: string;&#10;	executor: Executor;&#10;	providers: ResolvedProvider[];&#10;	connectors?: ConnectorBinding[];&#10;}): Promise&lt;{ result: unknown; logs?: string[] }&gt;;&#10;</code></pre>
<p>Normalizes and executes code. An <code>ExecuteResult.error</code> causes <code>runCode()</code> to throw an <code>Error</code> that includes captured console output.</p>
<h3 id="tool-providers">Tool providers</h3>
<pre><code class="language-ts">interface ToolProvider {&#10;	name?: string;&#10;	tools: ToolDescriptors | ToolSet | SimpleToolRecord;&#10;	types?: string;&#10;}&#10;</code></pre>
<p>Tool providers have these fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td>Sandbox namespace. Defaults to <code>codemode</code>.</td>
</tr>
<tr>
<td><code>tools</code></td>
<td>Tool descriptors, an AI SDK <code>ToolSet</code>, or records containing <code>execute</code>.</td>
</tr>
<tr>
<td><code>types</code></td>
<td>TypeScript declarations shown to the model. Code Mode generates them when omitted.</td>
</tr>
</tbody>
</table>
<pre><code class="language-ts">function resolveProvider(provider: ToolProvider): ResolvedProvider;&#10;</code></pre>
<p>The main-entry implementation does not validate inputs against schemas. It excludes tools whose <code>needsApproval</code> is <code>true</code> or a function. Use runtime connectors for durable approval flows.</p>
<h3 id="connector-base-classes">Connector base classes</h3>
<h4 id="codemodeconnector"><code>CodemodeConnector</code></h4>
<pre><code class="language-ts">abstract class CodemodeConnector&lt;&#10;	Env = unknown,&#10;	Props = unknown,&#10;&gt; extends WorkerEntrypoint&lt;Env, Props&gt; {&#10;	constructor(ctx: DurableObjectState | ExecutionContext, env: Env);&#10;&#10;	abstract name(): string;&#10;	protected instructions(): string | undefined;&#10;	protected abstract tools(): ConnectorTools | Promise&lt;ConnectorTools&gt;;&#10;	protected tool(name: string, tool: ConnectorTool): ConnectorTool;&#10;&#10;	describe(): Promise&lt;ConnectorDescription&gt;;&#10;	executeTool(&#10;		method: string,&#10;		args: unknown,&#10;		ctx?: ToolExecuteContext,&#10;	): Promise&lt;unknown&gt;;&#10;	revertAction(&#10;		method: string,&#10;		args: unknown,&#10;		result: unknown,&#10;		ctx?: ToolExecuteContext,&#10;	): Promise&lt;boolean&gt;;&#10;	onPassEnd(executionId: string, status: PassEndStatus): Promise&lt;void&gt;;&#10;	disposeExecution(&#10;		executionId: string,&#10;		status: ExecutionEndStatus,&#10;	): Promise&lt;void&gt;;&#10;	getTypeScriptTypes(): Promise&lt;string&gt;;&#10;}&#10;</code></pre>
<p>Connector authors implement or override these hooks:</p>
<table>
<thead>
<tr>
<th>Hook</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>name()</code></td>
<td>Yes</td>
<td>Returns the unique sandbox namespace.</td>
</tr>
<tr>
<td><code>instructions()</code></td>
<td>No</td>
<td>Returns connector guidance included by <code>describe()</code>.</td>
</tr>
<tr>
<td><code>tools()</code></td>
<td>Yes</td>
<td>Returns the connector tool record. Derived connectors implement this hook.</td>
</tr>
<tr>
<td><code>tool(name, tool)</code></td>
<td>No</td>
<td>Decorates a resolved tool. Use it to add approval, replay, or revert behavior to derived tools.</td>
</tr>
<tr>
<td><code>onPassEnd(executionId, status)</code></td>
<td>No</td>
<td>Releases per-pass resources. Runs after every pass, including a paused pass.</td>
</tr>
<tr>
<td><code>disposeExecution(executionId, status)</code></td>
<td>No</td>
<td>Releases per-execution resources after a terminal transition. It does not run on pause.</td>
</tr>
</tbody>
</table>
<p>Lifecycle hooks should be idempotent, should not rely on instance memory, and should not throw. On a terminal pass, <code>onPassEnd()</code> runs before <code>disposeExecution()</code>.</p>
<p>The base class derives <code>describe()</code>, <code>executeTool()</code>, <code>revertAction()</code>, and <code>getTypeScriptTypes()</code> from the tool record. Connector authors do not need to implement these methods.</p>
<h4 id="connector-tool-types">Connector tool types</h4>
<pre><code class="language-ts">type ConnectorTool = {&#10;	description?: string;&#10;	inputSchema?: JSONSchema7;&#10;	outputSchema?: JSONSchema7;&#10;	requiresApproval?: boolean;&#10;	replay?: &quot;log&quot; | &quot;reexecute&quot;;&#10;	execute: (&#10;		args: unknown,&#10;		ctx?: ToolExecuteContext,&#10;	) =&gt; Promise&lt;unknown&gt; | unknown;&#10;	revert?: (&#10;		args: unknown,&#10;		result: unknown,&#10;		ctx?: ToolExecuteContext,&#10;	) =&gt; Promise&lt;void&gt; | void;&#10;};&#10;&#10;type ConnectorTools = Record&lt;string, ConnectorTool&gt;;&#10;type ToolExecuteContext = { executionId: string };&#10;</code></pre>
<p><code>inputSchema</code> defaults to an open object. <code>requiresApproval: true</code> pauses before execution. <code>replay: &quot;reexecute&quot;</code> skips durable result storage and re-executes the call on each resume. These two options cannot be combined.</p>
<p><code>revert</code> provides compensation for <code>runtime.rollback()</code>. It can apply to any tool, whether or not the tool requires approval.</p>
<h4 id="mcpconnector"><code>McpConnector</code></h4>
<pre><code class="language-ts">abstract class McpConnector&lt;&#10;	Env = unknown,&#10;	Props = unknown,&#10;&gt; extends CodemodeConnector&lt;Env, Props&gt; {&#10;	protected abstract createConnection():&#10;		| McpConnectionLike&#10;		| Promise&lt;McpConnectionLike&gt;;&#10;	protected toolName(tool: McpTool): string;&#10;}&#10;</code></pre>
<p><code>McpConnector</code> converts each MCP tool into a connector method. <code>toolName()</code> defaults to <code>sanitizeToolName(tool.name)</code>. Override it to resolve naming collisions.</p>
<pre><code class="language-ts">interface McpConnectionLike {&#10;	name?: string;&#10;	client: Pick&lt;Client, &quot;callTool&quot;&gt;;&#10;	instructions?: string;&#10;	tools?: McpTool[];&#10;	fetchTools?: () =&gt; Promise&lt;McpTool[]&gt;;&#10;}&#10;</code></pre>
<p>The connector uses <code>tools</code> when that array is non-empty. Otherwise, it calls <code>fetchTools()</code> when provided. MCP error results become thrown connector errors. Structured content is returned before text content.</p>
<h4 id="openapiconnector"><code>OpenApiConnector</code></h4>
<pre><code class="language-ts">abstract class OpenApiConnector&lt;&#10;	Env = unknown,&#10;	Props = unknown,&#10;&gt; extends CodemodeConnector&lt;Env, Props&gt; {&#10;	protected abstract spec():&#10;		| Record&lt;string, unknown&gt;&#10;		| Promise&lt;Record&lt;string, unknown&gt;&gt;;&#10;	protected abstract request(options: OpenApiRequestOptions): Promise&lt;unknown&gt;;&#10;	protected exposeSpec(): boolean;&#10;}&#10;</code></pre>
<p><code>OpenApiConnector</code> creates one method per OpenAPI operation. It uses a sanitized <code>operationId</code> when present, then falls back to a name based on the HTTP method and path. Duplicate operations and names reserved for <code>request</code> or <code>spec</code> are skipped.</p>
<p>Every OpenAPI connector exposes a low-level <code>request</code> method. <code>exposeSpec()</code> defaults to <code>false</code>. Return <code>true</code> to also expose <code>spec</code>.</p>
<pre><code class="language-ts">type OpenApiRequestOptions = {&#10;	path: string;&#10;	method?: string;&#10;	params?: Record&lt;string, unknown&gt;;&#10;	body?: unknown;&#10;	headers?: Record&lt;string, string&gt;;&#10;};&#10;</code></pre>
<p>Derived operation tools substitute path parameters. They pass query values as <code>params</code>, header values as <code>headers</code>, and JSON request data as <code>body</code>.</p>
<h4 id="connector-lifecycle-and-description-types">Connector lifecycle and description types</h4>
<pre><code class="language-ts">type ExecutionEndStatus = &quot;completed&quot; | &quot;error&quot; | &quot;rejected&quot; | &quot;rolled_back&quot;;&#10;&#10;type PassEndStatus = ExecutionEndStatus | &quot;paused&quot;;&#10;&#10;type ToolAnnotations = {&#10;	requiresApproval?: boolean;&#10;	replay?: &quot;log&quot; | &quot;reexecute&quot;;&#10;};&#10;&#10;type ConnectorDescription = {&#10;	name: string;&#10;	instructions?: string;&#10;	descriptors: JsonSchemaToolDescriptors;&#10;	annotations?: Record&lt;string, ToolAnnotations&gt;;&#10;};&#10;</code></pre>
<h3 id="json-schema-utilities">JSON Schema utilities</h3>
<pre><code class="language-ts">interface JsonSchemaToolDescriptor {&#10;	description?: string;&#10;	inputSchema: JSONSchema7;&#10;	outputSchema?: JSONSchema7;&#10;}&#10;&#10;type JsonSchemaToolDescriptors = Record&lt;string, JsonSchemaToolDescriptor&gt;;&#10;&#10;function generateTypesFromJsonSchema(tools: JsonSchemaToolDescriptors): string;&#10;&#10;function jsonSchemaToType(schema: JSONSchema7, typeName: string): string;&#10;</code></pre>
<p><code>generateTypesFromJsonSchema()</code> returns declarations for a <code>codemode</code> namespace. Tool names are sanitized before declarations are generated. Unsupported schemas degrade to <code>unknown</code> instead of causing generation to fail.</p>
<h3 id="code-and-output-utilities">Code and output utilities</h3>
<p>The main entry point provides these code and result utilities:</p>
<table>
<thead>
<tr>
<th>Function</th>
<th>Signature</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sanitizeToolName</code></td>
<td><code>(name: string) =&gt; string</code></td>
<td>Replaces common separators, removes invalid characters, prefixes digit-leading names, and suffixes JavaScript reserved words.</td>
</tr>
<tr>
<td><code>normalizeCode</code></td>
<td><code>(code: string) =&gt; string</code></td>
<td>Converts common model output forms into an async arrow function. It also removes supported Markdown fences.</td>
</tr>
<tr>
<td><code>truncateResponse</code></td>
<td><code>(text: string, options?: TruncateOptions) =&gt; string</code></td>
<td>Truncates text to a character budget and appends a size marker.</td>
</tr>
<tr>
<td><code>truncateResult</code></td>
<td><code>(value: unknown, options?: TruncateOptions) =&gt; unknown</code></td>
<td>Preserves small structured values. Oversized serializable values become truncated JSON text.</td>
</tr>
</tbody>
</table>
<pre><code class="language-ts">type TruncateOptions = {&#10;	maxChars?: number;&#10;	maxTokens?: number;&#10;};&#10;</code></pre>
<p>The default budget is <code>6000</code> estimated tokens at four characters per token. <code>maxChars</code> overrides the derived character budget.</p>
<h2 id="cloudflare-codemode-ai"><code>@cloudflare/codemode/ai</code></h2>
<p>This entry point requires the <code>ai</code> and <code>zod</code> peer dependencies.</p>
<h3 id="createcodetool"><code>createCodeTool()</code></h3>
<pre><code class="language-ts">function createCodeTool(&#10;	options: CreateCodeToolOptions,&#10;): Tool&lt;CodeInput, CodeOutput&gt;;&#10;&#10;interface CreateCodeToolOptions {&#10;	tools: ToolProviderTools | ToolProvider[];&#10;	executor: Executor;&#10;	description?: string;&#10;}&#10;&#10;type CodeInput = { code: string };&#10;type CodeOutput = { result: unknown; logs?: string[] };&#10;</code></pre>
<p><code>description</code> can contain <code>{{types}}</code>. Code Mode replaces that token with generated declarations. A raw tool record becomes one provider named <code>codemode</code>. An array accepts multiple provider namespaces.</p>
<p>Tools whose <code>needsApproval</code> is <code>true</code> or a function are excluded. This API does not pause. Use <code>createCodemodeRuntime()</code> and connectors for durable approval handling.</p>
<h3 id="ai-sdk-provider-utilities">AI SDK provider utilities</h3>
<p>The AI SDK entry point provides these tool-provider utilities:</p>
<table>
<thead>
<tr>
<th>Export</th>
<th>Signature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>aiTools</code></td>
<td><code>(tools: ToolDescriptors | ToolSet) =&gt; ToolProvider</code></td>
<td>Wraps AI SDK tools in the default provider.</td>
</tr>
<tr>
<td><code>generateTypes</code></td>
<td><code>(tools: ToolDescriptors | ToolSet, namespace?: string) =&gt; string</code></td>
<td>Generates declarations from AI SDK or Zod schemas. The namespace defaults to <code>codemode</code>.</td>
</tr>
<tr>
<td><code>resolveProvider</code></td>
<td><code>(provider: ToolProvider) =&gt; ResolvedProvider</code></td>
<td>Filters approval-gated tools, validates input with AI SDK <code>asSchema()</code> when available, and extracts executable functions.</td>
</tr>
</tbody>
</table>
<pre><code class="language-ts">interface ToolDescriptor {&#10;	description?: string;&#10;	inputSchema: ZodType;&#10;	outputSchema?: ZodType;&#10;	execute?: (args: unknown) =&gt; Promise&lt;unknown&gt;;&#10;}&#10;&#10;type ToolDescriptors = Record&lt;string, ToolDescriptor&gt;;&#10;</code></pre>
<h3 id="toolsetconnector"><code>ToolSetConnector</code></h3>
<pre><code class="language-ts">class ToolSetConnector extends CodemodeConnector {&#10;	constructor(&#10;		ctx: DurableObjectState | ExecutionContext,&#10;		options: ToolSetConnectorOptions,&#10;	);&#10;}&#10;&#10;function toolSetConnector(&#10;	ctx: DurableObjectState | ExecutionContext,&#10;	options: ToolSetConnectorOptions,&#10;): ToolSetConnector;&#10;&#10;interface ToolSetConnectorOptions {&#10;	name?: string;&#10;	instructions?: string;&#10;	tools: ToolSet;&#10;}&#10;</code></pre>
<p>The namespace defaults to <code>tools</code>. The connector excludes tools without an <code>execute</code> function. <code>needsApproval: true</code> and function-valued <code>needsApproval</code> map to durable connector approval. <code>needsApproval: false</code> executes without approval. AI SDK schemas validate input before execution.</p>
<h2 id="cloudflare-codemode-mcp"><code>@cloudflare/codemode/mcp</code></h2>
<p>This entry point requires the MCP SDK and Zod peer dependencies.</p>
<h3 id="codemcpserver"><code>codeMcpServer()</code></h3>
<pre><code class="language-ts">interface CodeMcpServerOptions {&#10;	server: McpServer;&#10;	executor: Executor;&#10;	description?: string;&#10;}&#10;&#10;function codeMcpServer(options: CodeMcpServerOptions): Promise&lt;McpServer&gt;;&#10;</code></pre>
<p>Wraps an existing MCP server with one <code>code</code> tool. The wrapper connects to the source server through an in-memory transport, discovers its tools, and exposes those tools as methods on <code>codemode</code> inside the executor.</p>
<p>A custom description can contain <code>{{types}}</code>, which the wrapper replaces with generated TypeScript declarations. It can also contain <code>{{example}}</code>, which the wrapper replaces with an example call based on the first upstream MCP tool. Returned MCP values are unwrapped in this order: compatibility <code>toolResult</code>, MCP errors, <code>structuredContent</code>, all-text content, then the original mixed-content result.</p>
<h3 id="openapimcpserver"><code>openApiMcpServer()</code></h3>
<pre><code class="language-ts">interface OpenApiMcpServerOptions {&#10;	spec: Record&lt;string, unknown&gt;;&#10;	executor: Executor;&#10;	request: (options: RequestOptions) =&gt; Promise&lt;unknown&gt;;&#10;	name?: string;&#10;	version?: string;&#10;	description?: string;&#10;}&#10;&#10;interface RequestOptions {&#10;	method: &quot;GET&quot; | &quot;POST&quot; | &quot;PUT&quot; | &quot;PATCH&quot; | &quot;DELETE&quot;;&#10;	path: string;&#10;	query?: Record&lt;string, string | number | boolean | undefined&gt;;&#10;	body?: unknown;&#10;	contentType?: string;&#10;	rawBody?: boolean;&#10;}&#10;&#10;function openApiMcpServer(options: OpenApiMcpServerOptions): McpServer;&#10;</code></pre>
<p>Creates an MCP server with two tools:</p>
<table>
<thead>
<tr>
<th>MCP tool</th>
<th>Sandbox API</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>search</code></td>
<td><code>codemode.spec()</code></td>
<td>Runs code against the OpenAPI document. Local <code>$ref</code> values are resolved before the code receives the document.</td>
</tr>
<tr>
<td><code>execute</code></td>
<td><code>codemode.spec()</code> and <code>codemode.request(options)</code></td>
<td>Runs code that can inspect the document and call the host-provided request function.</td>
</tr>
</tbody>
</table>
<p><code>name</code> defaults to <code>openapi</code>. <code>version</code> defaults to <code>1.0.0</code>. The host request function keeps credentials outside the sandbox. Text responses are limited to approximately 6,000 tokens and include a truncation marker when clipped.</p>
<p>The <code>search</code> and <code>execute</code> tool descriptions use fixed example snippets. Unlike <code>codeMcpServer()</code>, this function does not support <code>{{types}}</code> or <code>{{example}}</code> placeholders. An optional <code>description</code> is appended to the <code>execute</code> tool description.</p>
<h2 id="cloudflare-codemode-tanstack-ai"><code>@cloudflare/codemode/tanstack-ai</code></h2>
<p>This entry point requires the <code>@tanstack/ai</code> and <code>zod</code> peer dependencies.</p>
<h3 id="createcodetool-1"><code>createCodeTool()</code></h3>
<pre><code class="language-ts">function createCodeTool(options: CreateCodeToolOptions): ServerTool;&#10;</code></pre>
<p>The options, <code>CodeInput</code>, and <code>CodeOutput</code> match the <code>/ai</code> entry point. The returned <code>ServerTool</code> can be passed to TanStack AI <code>chat()</code>.</p>
<h3 id="tanstack-ai-provider-utilities">TanStack AI provider utilities</h3>
<p>The TanStack AI entry point provides these tool-provider utilities:</p>
<table>
<thead>
<tr>
<th>Export</th>
<th>Signature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>tanstackTools</code></td>
<td><code>(tools: TanStackTool[], name?: string) =&gt; ToolProvider</code></td>
<td>Wraps TanStack AI tools in a provider. Only tools with an <code>execute</code> function are callable. The namespace defaults to <code>codemode</code>.</td>
</tr>
<tr>
<td><code>generateTypes</code></td>
<td><code>(tools: TanStackTool[], namespace?: string) =&gt; string</code></td>
<td>Converts supported TanStack AI schemas to JSON Schema, then generates declarations.</td>
</tr>
<tr>
<td><code>resolveProvider</code></td>
<td><code>(provider: ToolProvider) =&gt; ResolvedProvider</code></td>
<td>Resolves a framework-independent provider without schema validation.</td>
</tr>
<tr>
<td><code>normalizeProviders</code></td>
<td><code>(tools: ToolProviderTools | ToolProvider[]) =&gt; ToolProvider[]</code></td>
<td>Converts raw tools into a one-element provider array.</td>
</tr>
</tbody>
</table>
<p>This entry point also exports <code>DEFAULT_DESCRIPTION</code>. <code>tanstackTools()</code> excludes tools with <code>needsApproval: true</code> or a function-valued <code>needsApproval</code>. Tools with <code>needsApproval: false</code> remain callable.</p>
<h2 id="cloudflare-codemode-browser"><code>@cloudflare/codemode/browser</code></h2>
<p>The browser entry point uses browser APIs and plain JSON Schema. It does not require the AI SDK or Zod.</p>
<h3 id="createbrowsercodetool"><code>createBrowserCodeTool()</code></h3>
<pre><code class="language-ts">function createBrowserCodeTool(&#10;	options: CreateBrowserCodeToolOptions,&#10;): BrowserCodeToolDescriptor;&#10;&#10;interface CreateBrowserCodeToolOptions {&#10;	tools:&#10;		| JsonSchemaExecutableToolDescriptor[]&#10;		| JsonSchemaExecutableToolDescriptors;&#10;	executor?: Executor;&#10;	description?: string;&#10;}&#10;</code></pre>
<p>Array-form tools must include <code>name</code>. Object-form tools use each record key as the name. The executor defaults to a new <code>IframeSandboxExecutor</code>.</p>
<p>The <code>tools</code> option also accepts descriptors with <code>needsApproval?: boolean | ((...args: unknown[]) =&gt; unknown)</code>. Tools with <code>needsApproval: true</code> or a function-valued <code>needsApproval</code> are excluded. Tools with <code>needsApproval: false</code> remain callable. JSON Schema contributes model-facing declarations but does not perform runtime validation.</p>
<pre><code class="language-ts">interface JsonSchemaExecutableToolDescriptor extends JsonSchemaToolDescriptor {&#10;	name?: string;&#10;	execute: (args: Record&lt;string, unknown&gt;) =&gt; Promise&lt;unknown&gt;;&#10;}&#10;&#10;type JsonSchemaExecutableToolDescriptors = Record&lt;&#10;	string,&#10;	JsonSchemaExecutableToolDescriptor&#10;&gt;;&#10;</code></pre>
<p>The returned descriptor has this shape:</p>
<pre><code class="language-ts">interface BrowserCodeToolDescriptor {&#10;	name: string;&#10;	description: string;&#10;	inputSchema: {&#10;		type: &quot;object&quot;;&#10;		properties: {&#10;			code: { type: &quot;string&quot;; description: string };&#10;		};&#10;		required: [&quot;code&quot;];&#10;	};&#10;	outputSchema: {&#10;		type: &quot;object&quot;;&#10;		properties: {&#10;			result: { description: string };&#10;			logs: {&#10;				type: &quot;array&quot;;&#10;				items: { type: &quot;string&quot; };&#10;				description: string;&#10;			};&#10;		};&#10;		required: [&quot;result&quot;];&#10;	};&#10;	execute(args: CodeInput): Promise&lt;CodeOutput&gt;;&#10;}&#10;</code></pre>
<h3 id="iframesandboxexecutor"><code>IframeSandboxExecutor</code></h3>
<pre><code class="language-ts">class IframeSandboxExecutor implements Executor {&#10;	constructor(options?: IframeSandboxExecutorOptions);&#10;	execute(&#10;		code: string,&#10;		providersOrFns:&#10;			| ResolvedProvider[]&#10;			| Record&lt;string, (...args: unknown[]) =&gt; Promise&lt;unknown&gt;&gt;,&#10;	): Promise&lt;ExecuteResult&gt;;&#10;}&#10;&#10;interface IframeSandboxExecutorOptions {&#10;	timeout?: number;&#10;	csp?: string;&#10;}&#10;</code></pre>
<p>The iframe executor accepts these options:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>timeout</code></td>
<td><code>30000</code></td>
<td>Maximum execution time in milliseconds. It cannot preempt a synchronous loop that blocks the browser event loop.</td>
</tr>
<tr>
<td><code>csp</code></td>
<td><code>default-src 'none'; script-src 'unsafe-inline' 'unsafe-eval';</code></td>
<td>Content Security Policy applied to the sandbox iframe document.</td>
</tr>
</tbody>
</table>
<p>Each execution creates a hidden iframe with <code>sandbox=&quot;allow-scripts&quot;</code>. Tool calls cross the iframe boundary through nonce-scoped <code>postMessage</code> messages. The iframe is removed after success, error, or timeout.</p>
<p>This entry point also exports the framework-independent <code>Executor</code>, <code>ExecuteResult</code>, and <code>ResolvedProvider</code> types. It re-exports <code>JsonSchemaToolDescriptor</code> and <code>JsonSchemaToolDescriptors</code>.</p>
<h2 id="cloudflare-codemode-vite"><code>@cloudflare/codemode/vite</code></h2>
<p>The Vite entry point has one default export:</p>
<pre><code class="language-ts">function codemodeVitePlugin(): Plugin;&#10;</code></pre>
<p>The plugin appends <code>export { CodemodeRuntime } from &quot;@cloudflare/codemode&quot;</code> to the Worker entry module (<code>src/server.ts</code>, <code>src/index.ts</code>, or <code>src/worker.ts</code>). This makes the runtime facet available as <code>ctx.exports.CodemodeRuntime</code>, which <code>createCodemodeRuntime()</code> requires.</p>
<p>The plugin leaves the entry module unchanged if it already exports <code>CodemodeRuntime</code>. Connector classes need no special file name or import syntax — import them normally and pass instances to the runtime.</p>
<p>Without the plugin, add the export manually:</p>
<pre><code class="language-ts">export { CodemodeRuntime } from &quot;@cloudflare/codemode&quot;;&#10;</code></pre>
<p>A connector import can target one connector file or a directory. A directory import re-exports every matching connector file under that directory.</p>
