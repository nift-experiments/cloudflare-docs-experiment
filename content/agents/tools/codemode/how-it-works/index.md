<p>Code Mode is a pattern where a model writes code to compose tools. The <code>@cloudflare/codemode</code> package implements that pattern with an isolated executor, service connectors, and a durable runtime.</p>
<p>These parts have separate responsibilities. The executor runs code but stores no state. Connectors provide capabilities but do not manage replay. The runtime records execution and controls approvals, replay, rollback, and reuse.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2675.md")
</aside>
<h2 id="what-the-model-sees">What the model sees</h2>
<p>In the standard setup, the model receives one outer tool named <code>codemode</code>. That tool accepts one field and returns a durable execution outcome:</p>
<pre><code class="language-ts">type CodeModeInput = {&#10;	code: string;&#10;};&#10;&#10;type PendingAction = {&#10;	executionId: string;&#10;	seq: number;&#10;	connector: string;&#10;	method: string;&#10;	args: unknown;&#10;};&#10;&#10;type CodeModeOutput =&#10;	| { status: &quot;completed&quot;; executionId: string; result: unknown; logs?: string[] }&#10;	| { status: &quot;paused&quot;; executionId: string; pending: PendingAction[] }&#10;	| { status: &quot;error&quot;; executionId: string; error: string; logs?: string[] };&#10;</code></pre>
<p>Its description tells the model to write a JavaScript async arrow function. The description lists the configured connector namespace names, such as <code>github</code> or <code>stripe</code>, but it does not include every connector method and schema.</p>
<p>The model can use one Code Mode execution to discover relevant methods, then use the returned paths and types in its next execution. This keeps the complete tool catalog out of the initial model context.</p>
<h3 id="platform-sdk">Platform SDK</h3>
<p>Inside the sandbox, the <code>codemode</code> global provides the platform-level SDK:</p>
<pre><code class="language-ts">declare const codemode: {&#10;	search(query: string): Promise&lt;SearchOutput&gt;;&#10;	describe(target: string): Promise&lt;DescribeOutput&gt;;&#10;	step&lt;T&gt;(name: string, fn: () =&gt; T | Promise&lt;T&gt;): Promise&lt;T&gt;;&#10;	run(name: string, input?: unknown): Promise&lt;unknown&gt;;&#10;};&#10;&#10;type SearchOutput = {&#10;	results: Array&lt;{&#10;		path: string;&#10;		connector: string;&#10;		method: string;&#10;		description?: string;&#10;		kind: &quot;method&quot; | &quot;snippet&quot;;&#10;		score: number;&#10;	}&gt;;&#10;	total: number;&#10;	truncated: boolean;&#10;};&#10;&#10;type DescribeOutput = {&#10;	path: string;&#10;	description?: string;&#10;	types: string;&#10;	kind: &quot;connector&quot; | &quot;method&quot; | &quot;snippet&quot;;&#10;};&#10;</code></pre>
<p><code>codemode.search()</code> searches connector methods and saved snippets. It returns ranked paths, not complete schemas. The model can then pass one path to <code>codemode.describe()</code> to request focused TypeScript documentation.</p>
<p><code>codemode.step()</code> records nondeterministic or side-effectful sandbox work for replay. <code>codemode.run()</code> invokes a saved snippet.</p>
<h3 id="connector-sdks">Connector SDKs</h3>
<p>Each configured connector becomes another sandbox global. A connector named <code>github</code> is available as <code>github</code>, and its methods appear under paths such as <code>github.list_pull_requests</code>.</p>
<p>A connector-level description returns declarations similar to:</p>
<pre><code class="language-ts">type ListPullRequestsInput = {&#10;	owner: string;&#10;	repo: string;&#10;	state?: &quot;open&quot; | &quot;closed&quot;;&#10;};&#10;&#10;type ListPullRequestsOutput = unknown;&#10;&#10;declare const github: {&#10;	list_pull_requests(&#10;		input: ListPullRequestsInput,&#10;	): Promise&lt;ListPullRequestsOutput&gt;;&#10;};&#10;</code></pre>
<p>These declarations are generated from connector schemas. They are illustrative; the actual method names, input fields, and output types depend on the connector.</p>
<p>The sandbox also includes standard JavaScript globals. It does not expose Node.js APIs, host credentials, <code>process</code>, <code>require</code>, or unrestricted network access. All external operations go through connector globals unless the executor explicitly provides another capability.</p>
<h2 id="executor-connectors-and-runtime">Executor, connectors, and runtime</h2>
<h3 id="executor">Executor</h3>
<p>An executor runs one block of model-generated code once. It receives callable namespaces and returns a result, an error, and captured console output. It does not retain execution history.</p>
<p><code>DynamicWorkerExecutor</code> uses a <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker Loader</a> to create an isolated Worker for each execution pass. A resumed execution runs the code again in another pass. Durable state therefore cannot live inside the sandbox.</p>
<p>External <code>fetch()</code> and <code>connect()</code> calls are blocked by default. <code>DynamicWorkerExecutor</code> configures <code>globalOutbound: null</code> unless you provide another value. You can provide a <code>Fetcher</code> to route outbound requests through a controlled service.</p>
<h3 id="connectors">Connectors</h3>
<p>Connectors bridge host-side services into the sandbox. A connector can wrap a Model Context Protocol (MCP) server, an OpenAPI document, an AI SDK toolset, or custom code.</p>
<p>Each connector becomes a global namespace. For example, a connector named <code>github</code> exposes calls such as <code>github.list_pull_requests()</code>. The generated code never receives the connector credentials or client objects.</p>
<p>Connector calls cross the sandbox boundary through <a href="/workers/runtime-apis/rpc/">Workers remote procedure calls (RPC)</a>. The runtime intercepts each call before the connector executes it. This interception applies approval, logging, replay, and rollback policy.</p>
<p>The <code>codemode</code> global provides discovery and runtime operations. <code>codemode.search()</code> finds connector methods and saved snippets. <code>codemode.describe()</code> returns focused TypeScript documentation without placing every connector schema in the model context.</p>
<h3 id="durable-runtime">Durable runtime</h3>
<p>The runtime connects the executor and connectors. It stores execution records, connector-call logs, pending approvals, and snippets in isolated SQLite storage. This state survives request completion and Durable Object hibernation.</p>
<p>The executor and connector instances remain transient. Your application provides them again when it handles a later approval or request.</p>
<p>A typical Agent creates all three parts together:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2676.md")
</div>
<p>Code Mode stores this state in a Durable Object facet. A facet is a durable child of the Agent with its own SQLite storage. <code>createCodemodeRuntime()</code> and the Vite plugin manage this implementation detail. You do not create or address the facet directly.</p>
<h2 id="use-multiple-runtimes">Use multiple runtimes</h2>
<p>Most Agents need only one Code Mode runtime. If you omit <code>name</code>, the runtime uses the name <code>default</code>.</p>
<p>Set <code>name</code> when one Agent needs separate Code Mode histories. For example, a runtime named <code>research</code> and another named <code>operations</code> keep separate execution records and snippet collections:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2677.md")
</div>
<p>A runtime name identifies its durable storage. It does not name the model, connector, tool, or individual execution.</p>
<p>Changing the connector set does not create another runtime. Each execution records every connector configured when it starts, and a saved snippet inherits that list. Approval replay and snippet execution require all recorded connectors to remain available, even if the original code did not call each one.</p>
<h2 id="durable-execution-log">Durable execution log</h2>
<p>The runtime assigns each execution a stable ID. Each connector call and <code>codemode.step()</code> entry receives a sequence number. The log records its arguments, state, replay policy, and result when applicable.</p>
<p>The runtime marks a call as <code>executing</code> before invoking its connector. It marks the call as <code>applied</code> after recording the result. If the host stops before completing the pass, the execution can remain in <code>running</code>. A later <code>expirePaused()</code> maintenance call marks that stale execution as an error and releases its resources. Approval does not resume a stale <code>running</code> execution.</p>
<p>This log is the replay spine. It also supports developer audit views and determines which actions can be rolled back. It is not general conversation memory and does not replace Agent state.</p>
<h2 id="approvals-through-abort-and-replay">Approvals through abort and replay</h2>
<p>A connector method can require user approval. When generated code reaches that method, the runtime records the action as pending and aborts the current pass. The action does not receive a provisional result.</p>
<p>The application can show the pending method and arguments to a user. Approval starts another pass with the same source code and execution ID. Calls already marked as applied return their recorded results instead of executing again. The approved action then executes, and the code continues until completion or another approval.</p>
<pre><code class="language-txt">first pass:   read ── execute ──&gt; result&#10;              write ── pause&#10;&#10;approval&#10;&#10;second pass:  read ── replay ───&gt; recorded result&#10;              write ── execute ─&gt; result&#10;              next call ────────&gt; continue&#10;</code></pre>
<p>This design lets an approval wait beyond a request or hibernation. Generated code remains linear and does not implement pause or resume logic.</p>
<p>Only a paused execution can resume. A stale approval cannot revive a completed, rejected, or rolled-back execution. Rejecting an action ends the execution, but it does not undo earlier actions. Rollback is a separate operation.</p>
<p>Execution failures are returned as data to the agent loop. Sandbox errors and replay divergence therefore do not need to escape as uncaught RPC exceptions.</p>
<h2 id="deterministic-replay">Deterministic replay</h2>
<p>Replay requires connector calls and steps to occur in the same order. On every pass, a given sequence number must use the same connector, method, and arguments. A mismatch ends the execution with a replay-divergence error.</p>
<p>Recorded connector results make normal data-dependent branches stable. However, values from <code>Date.now()</code>, <code>Math.random()</code>, or other nondeterministic sources can change control flow or action arguments.</p>
<p>Use <code>codemode.step()</code> to capture such work once. The runtime records the closure result and returns that value during approval replay:</p>
<pre><code class="language-js">async () =&gt; {&#10;	const createdAt = await codemode.step(&quot;created-at&quot;, () =&gt; Date.now());&#10;&#10;	return github.create_issue({&#10;		owner: &quot;cloudflare&quot;,&#10;		repo: &quot;agents&quot;,&#10;		title: `Review created at ${createdAt}`,&#10;	});&#10;};&#10;</code></pre>
<p>Connector calls already pass through the runtime and do not need a step wrapper. Use steps for nondeterministic or side-effectful work outside connector calls. If you explicitly allow direct network access, this includes direct network operations that must not repeat during approval replay.</p>
<p>Issue connector calls sequentially when an execution might pause. The host assigns sequence numbers when calls arrive. Calls in <code>Promise.all()</code> can arrive in different orders across passes and cause replay divergence.</p>
<h2 id="resource-lifetimes">Resource lifetimes</h2>
<p>Some connectors need resources beyond one method call. Examples include browser sessions, database transactions, and temporary workspaces. Connector methods receive the stable execution ID, which can key durable resource metadata across passes.</p>
<p>Code Mode distinguishes two resource lifetimes:</p>
<ul>
<li><strong>Pass resources</strong> last for one sandbox pass. The runtime invokes <code>onPassEnd()</code> after completed, failed, and paused passes.</li>
<li><strong>Execution resources</strong> last for the whole execution. The runtime invokes <code>disposeExecution()</code> after completion, failure, rejection, or rollback, but not after a pause.</li>
</ul>
<p>A paused execution can resume in another Worker invocation. Connector lifecycle hooks must not depend on instance memory. Cleanup must also be idempotent because a completed execution can later be rolled back and disposed again.</p>
<p>The runtime calls lifecycle hooks for every configured connector. A connector that did not allocate a resource should safely do nothing. Cleanup errors are ignored so they do not turn a finished execution into a failed one.</p>
<h2 id="replay-policy">Replay policy</h2>
<p>By default, the runtime stores a connector result and replays it on later passes. This preserves the exact value that the original code observed.</p>
<p>A connector can mark a call with <code>replay: &quot;reexecute&quot;</code>. The runtime still logs its sequence and arguments, but it does not store the result. A later pass runs the connector method again.</p>
<p>Use this policy only for idempotent reads with large, inexpensive results. The result can change between passes, so generated code must tolerate that change. Approval-required methods cannot use <code>replay: &quot;reexecute&quot;</code> because replay could apply an approved side effect more than once.</p>
<h2 id="rollback">Rollback</h2>
<p>Rollback walks applied connector calls in reverse order. It invokes the <code>revert</code> implementation for every applied method that provides one, regardless of whether that method required approval.</p>
<p>For each applied connector call, the runtime asks the currently configured connector to run its <code>revert</code> implementation. Methods without <code>revert</code> remain applied. Missing connectors are also skipped. A failed revert does not stop later compensation attempts, and the runtime reports failures after trying the remaining calls. The execution moves to <code>rolled_back</code> only if at least one call is reverted.</p>
<p>Rollback is compensation, not database transaction isolation. Connector authors define what reversal means for each action. An external system may also change between the original call and its compensation.</p>
<h2 id="retention-and-stale-executions">Retention and stale executions</h2>
<p>The execution log is an audit trail and grows over time. When a new run begins, the runtime first inserts that run and then prunes older terminal executions. <code>maxExecutions</code> defaults to 50. Because a running execution is not terminal, completion can temporarily leave 51 terminal records until another run begins or you call <code>pruneExecutions()</code>.</p>
<p>Running and paused executions are not pruned automatically. They may still need to finish or resume. Use <code>expirePaused()</code> from recurring maintenance to reclaim stale nonterminal runs. The runtime marks stale paused runs as rejected and stale running runs as errors, then disposes their execution resources.</p>
<p>You can also remove individual execution records or prune terminal history explicitly. Deleting a nonterminal execution disposes its execution-scoped resources.</p>
<h2 id="durable-value-and-result-limits">Durable value and result limits</h2>
<p>Each value stored for durable replay has a serialized character limit of 1,000,000. The implementation checks the JavaScript string length after serialization. This limit applies to connector arguments, recorded connector results, step results, and execution source code.</p>
<p>The runtime cannot truncate these values. Truncation would provide different data during replay. An oversized or unserializable replay value therefore fails the execution and suggests storing the data elsewhere, then passing a small reference such as a file path.</p>
<p>A final result has different behavior because replay does not consume it. The execution can complete and return the real result to the model. If the result cannot fit in the audit record, the runtime stores an omission message there instead.</p>
<p><code>transformResult</code> can reshape the completed result before the model receives it. The transform runs after the runtime attempts to record the raw result. The audit trail retains the original value when it fits, while the model can receive a smaller representation.</p>
<h2 id="snippets">Snippets</h2>
<p>A snippet is saved source from an execution. Snippets turn model-written programs into reusable recipes. They remain available across requests and hibernation.</p>
<p>The model does not promote its own code. Your application reviews an execution and calls <code>runtime.saveSnippet()</code> with its execution ID. The API accepts any execution status, so verify that the execution completed successfully before saving it. The model can then find the snippet with <code>codemode.search()</code>, inspect it with <code>codemode.describe()</code>, and invoke it with <code>codemode.run()</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2678.md")
</div>
<p>A snippet can accept an input value. Its connector calls join the current execution log when the model runs it. The snippet also retains the connector list from its source execution. If a recorded connector is unavailable, <code>codemode.run()</code> resolves to an object with an <code>error</code> property. It does not throw automatically.</p>
