<p>Build AI-powered chat interfaces with <code>AIChatAgent</code> and <code>useAgentChat</code>. Messages are automatically persisted to SQLite, streams resume on disconnect, and tool calls work across server and client.</p>
<h2 id="overview">Overview</h2>
<p>The <code>@cloudflare/ai-chat</code> package provides two primary APIs:</p>
<table>
<thead>
<tr>
<th>Export</th>
<th>Import</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>AIChatAgent</code></td>
<td><code>@cloudflare/ai-chat</code></td>
<td>Server-side agent class with message persistence and streaming</td>
</tr>
<tr>
<td><code>useAgentChat</code></td>
<td><code>@cloudflare/ai-chat/react</code></td>
<td>React hook for building chat UIs</td>
</tr>
</tbody>
</table>
<p>Advanced helpers are also available from <code>@cloudflare/ai-chat/react</code>, <code>@cloudflare/ai-chat/types</code>, and <code>agents/chat</code>; see <a href="#exports">Exports</a> for the full package surface.</p>
<p>Built on the <a href="https://ai-sdk.dev">AI SDK</a> and Cloudflare Durable Objects, you get:</p>
<ul>
<li><strong>Automatic message persistence</strong> — conversations stored in SQLite, survive restarts</li>
<li><strong>Resumable streaming</strong> — disconnected clients resume mid-stream without data loss</li>
<li><strong>Real-time sync</strong> — messages broadcast to all connected clients via WebSocket</li>
<li><strong>Tool support</strong> — server-side, client-side, and human-in-the-loop tool patterns</li>
<li><strong>Data parts</strong> — attach typed JSON (citations, progress, usage) to messages alongside text</li>
<li><strong>Row size protection</strong> — automatic compaction when messages approach SQLite limits</li>
</ul>
<h2 id="quick-start">Quick start</h2>
<h3 id="install">Install</h3>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/ai-chat agents ai @ai-sdk/react workers-ai-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/ai-chat agents ai @ai-sdk/react workers-ai-provider" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/ai-chat agents ai @ai-sdk/react workers-ai-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/ai-chat agents ai @ai-sdk/react workers-ai-provider" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/ai-chat agents ai @ai-sdk/react workers-ai-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/ai-chat agents ai @ai-sdk/react workers-ai-provider" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/ai-chat agents ai @ai-sdk/react workers-ai-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/ai-chat agents ai @ai-sdk/react workers-ai-provider" aria-label="Copy to clipboard">Copy</button></div></div>
<h3 id="server">Server</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2034.md")
</div>
<h3 id="client">Client</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2035.md")
</div>
<h3 id="wrangler-configuration">Wrangler configuration</h3>
<pre><code class="language-jsonc">// wrangler.jsonc&#10;{&#10;	&quot;ai&quot;: { &quot;binding&quot;: &quot;AI&quot; },&#10;	&quot;durable_objects&quot;: {&#10;		&quot;bindings&quot;: [{ &quot;name&quot;: &quot;ChatAgent&quot;, &quot;class_name&quot;: &quot;ChatAgent&quot; }],&#10;	},&#10;	&quot;migrations&quot;: [{ &quot;tag&quot;: &quot;v1&quot;, &quot;new_sqlite_classes&quot;: [&quot;ChatAgent&quot;] }],&#10;}&#10;</code></pre>
<p>The <code>new_sqlite_classes</code> migration is required — <code>AIChatAgent</code> uses SQLite for message persistence and stream chunk buffering.</p>
<h2 id="how-it-works">How it works</h2>
<pre><code class="language-mermaid">sequenceDiagram&#10;    participant Client as Client (useAgentChat)&#10;    participant Agent as AIChatAgent&#10;    participant DB as SQLite&#10;&#10;    Client-&gt;&gt;Agent: CF_AGENT_USE_CHAT_REQUEST (WebSocket)&#10;    Agent-&gt;&gt;DB: Persist messages&#10;    Agent-&gt;&gt;Agent: onChatMessage()&#10;    loop Streaming response&#10;        Agent--&gt;&gt;Client: CF_AGENT_USE_CHAT_RESPONSE (chunks)&#10;        Agent-&gt;&gt;DB: Buffer chunks&#10;    end&#10;    Agent-&gt;&gt;DB: Persist final message&#10;    Agent--&gt;&gt;Client: CF_AGENT_CHAT_MESSAGES (broadcast to all clients)&#10;</code></pre>
<ol>
<li>The client sends a message via WebSocket</li>
<li><code>AIChatAgent</code> persists messages to SQLite and calls your <code>onChatMessage</code> method</li>
<li>Your method returns a streaming <code>Response</code> (typically from <code>streamText</code>)</li>
<li>Chunks stream back over WebSocket in real-time</li>
<li>When the stream completes, the final message is persisted and broadcast to all connections</li>
</ol>
<h2 id="server-api">Server API</h2>
<h3 id="aichatagent"><code>AIChatAgent</code></h3>
<p>Extends <code>Agent</code> from the <code>agents</code> package. Manages conversation state, persistence, and streaming.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2036.md")
</div>
<h3 id="onchatmessage"><code>onChatMessage</code></h3>
<p>This is the main method you override. It receives the conversation context and should return a <code>Response</code>.</p>
<p><strong>Streaming response</strong> (most common):</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2037.md")
</div>
<p><strong>Plain text response</strong>:</p>
<pre><code class="language-ts">export class ChatAgent extends AIChatAgent {&#10;	async onChatMessage() {&#10;		return new Response(&quot;Hello! I am a simple agent.&quot;, {&#10;			headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p><strong>Accessing custom body data and request ID</strong>:</p>
<pre><code class="language-ts">export class ChatAgent extends AIChatAgent {&#10;	async onChatMessage(_onFinish, options) {&#10;		const { timezone, userId } = options?.body ?? {};&#10;		// Use these values in your LLM call or business logic&#10;&#10;		// options.requestId — unique identifier for this chat request,&#10;		// useful for logging and correlating events&#10;		console.log(&quot;Request ID:&quot;, options?.requestId);&#10;&#10;		if (options?.continuation) {&#10;			// This turn continues a previous assistant message after a tool result,&#10;			// continueLastTurn(), or recovery.&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p><code>options.continuation</code> is <code>true</code> for automatic continuations after tool results or approvals, calls to <code>continueLastTurn()</code>, and recovered turns. Use it to choose a different model, adjust your system prompt, or skip expensive context assembly for continuation turns.</p>
<h3 id="this-messages"><code>this.messages</code></h3>
<p>The current conversation history, loaded from SQLite. This is an array of <code>UIMessage</code> objects from the AI SDK. Messages are automatically persisted after each interaction.</p>
<h3 id="maxpersistedmessages"><code>maxPersistedMessages</code></h3>
<p>Cap the number of messages stored in SQLite. When the limit is exceeded, the oldest messages are deleted. This controls storage only — it does not affect what is sent to the LLM.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2038.md")
</div>
<p>To control what is sent to the model, use the AI SDK's <code>pruneMessages()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2039.md")
</div>
<h3 id="waitformcpconnections"><code>waitForMcpConnections</code></h3>
<p>Controls whether <code>AIChatAgent</code> waits for MCP server connections to settle before calling <code>onChatMessage</code>. This ensures <code>this.mcp.getAITools()</code> returns the full set of tools, especially after Durable Object hibernation when connections are being restored in the background.</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>{ timeout: 10_000 }</code></td>
<td>Wait up to 10 seconds (default)</td>
</tr>
<tr>
<td><code>{ timeout: N }</code></td>
<td>Wait up to <code>N</code> milliseconds</td>
</tr>
<tr>
<td><code>true</code></td>
<td>Wait indefinitely until all connections ready</td>
</tr>
<tr>
<td><code>false</code></td>
<td>Do not wait (old behavior before 0.2.0)</td>
</tr>
</tbody>
</table>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2040.md")
</div>
<p>For lower-level control, call <code>this.mcp.waitForConnections()</code> directly inside your <code>onChatMessage</code> instead.</p>
<h3 id="messageconcurrency"><code>messageConcurrency</code></h3>
<p>Controls how overlapping user submissions behave when a chat turn is already active or queued.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2041.md")
</div>
<table>
<thead>
<tr>
<th>Strategy</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;queue&quot;</code> (default)</td>
<td>Queue every submission and process in order</td>
</tr>
<tr>
<td><code>&quot;latest&quot;</code></td>
<td>Keep only the latest overlapping submission; superseded submissions still persist their user messages but do not start a model turn</td>
</tr>
<tr>
<td><code>&quot;merge&quot;</code></td>
<td>Queue overlapping submissions, then collapse their trailing user messages into one combined turn before the latest queued turn runs</td>
</tr>
<tr>
<td><code>&quot;drop&quot;</code></td>
<td>Ignore overlapping submissions entirely. Messages are not persisted.</td>
</tr>
<tr>
<td><code>{ strategy: &quot;debounce&quot;, debounceMs?: number }</code></td>
<td>Trailing-edge latest with a quiet window (default 750ms)</td>
</tr>
</tbody>
</table>
<p>This setting only applies to <code>sendMessage()</code> submissions. Regenerations, tool continuations, approvals, clears, and programmatic <code>saveMessages()</code> calls keep their existing serialized behavior.</p>
<h3 id="persistmessages-and-savemessages"><code>persistMessages</code> and <code>saveMessages</code></h3>
<p><code>persistMessages</code> stores messages in SQLite and broadcasts the update to all connected clients, but does <strong>not</strong> trigger a model turn. Use it when you want to inject messages into the conversation without starting a new response.</p>
<p><code>saveMessages</code> persists messages <strong>and</strong> triggers <code>onChatMessage()</code> for a new response. It waits for any active chat turn to finish before starting, so scheduled or programmatic messages never overlap an in-flight stream.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2042.md")
</div>
<p><code>saveMessages</code> accepts either an array of messages or a function that derives the next message list from the latest persisted <code>this.messages</code>. Use the function form to avoid stale baselines when multiple calls queue up:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2043.md")
</div>
<p><code>saveMessages</code> returns <code>{ requestId, status, error? }</code> where <code>status</code> is <code>&quot;completed&quot;</code> if the turn ran, <code>&quot;error&quot;</code> if the stream reported an error, <code>&quot;skipped&quot;</code> if the chat was cleared before it started, or <code>&quot;aborted&quot;</code> if an external <code>AbortSignal</code> cancelled it before completion. When <code>status</code> is <code>&quot;error&quot;</code>, <code>error</code> contains the stream error message when available.</p>
<p>Pass <code>options.signal</code> to cancel a programmatic turn from outside the chat agent. This is useful when a parent tool call needs to cancel a child agent turn without knowing the internally generated request ID:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2044.md")
</div>
<p><code>continueLastTurn()</code> accepts the same <code>options.signal</code> argument. <code>AbortSignal</code> objects cannot cross Durable Object RPC boundaries, so construct the controller inside the Durable Object that calls <code>saveMessages()</code> or <code>continueLastTurn()</code>. The signal is in memory only. If the Durable Object hibernates mid-turn, the recovered turn runs without the original signal. Persist cancellation intent when cancellation must survive a restart.</p>
<h3 id="onchatresponse"><code>onChatResponse</code></h3>
<p>Called after a chat turn produces and persists an assistant message. The turn lock is released before this hook runs, so it is safe to call <code>saveMessages</code> from inside. Fires for turn paths that persist an assistant message: WebSocket chat requests, <code>saveMessages</code>, and auto-continuation. If a turn fails before producing any assistant parts, the error is surfaced through the original request instead.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2045.md")
</div>
<p>The <code>ChatResponseResult</code> contains:</p>
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
<td><code>message</code></td>
<td><code>UIMessage</code></td>
<td>The finalized assistant message from this turn</td>
</tr>
<tr>
<td><code>requestId</code></td>
<td><code>string</code></td>
<td>The request ID associated with this turn</td>
</tr>
<tr>
<td><code>continuation</code></td>
<td><code>boolean</code></td>
<td>Whether this turn was a continuation of a previous assistant turn</td>
</tr>
<tr>
<td><code>status</code></td>
<td><code>&quot;completed&quot; | &quot;error&quot; | &quot;aborted&quot;</code></td>
<td>How the turn ended</td>
</tr>
<tr>
<td><code>error</code></td>
<td><code>string | undefined</code></td>
<td>Error message when <code>status</code> is <code>&quot;error&quot;</code></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2033.md")
</aside>
<h3 id="sanitizemessageforpersistence"><code>sanitizeMessageForPersistence</code></h3>
<p>Override this method to apply custom transformations to messages before they are persisted to storage. This hook runs <strong>after</strong> the built-in sanitization (OpenAI metadata stripping, Anthropic provider-executed tool payload truncation, empty reasoning part filtering).</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2046.md")
</div>
<h3 id="turn-lifecycle-helpers">Turn lifecycle helpers</h3>
<p>These methods help you coordinate programmatic turns and wait for pending interactions.</p>
<h4 id="haspendinginteraction"><code>hasPendingInteraction()</code></h4>
<p>Returns <code>true</code> when an assistant message is waiting on a client tool result or approval.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2047.md")
</div>
<h4 id="waituntilstable"><code>waitUntilStable()</code></h4>
<p>Waits until the conversation is fully stable — no active stream, no pending client-tool interactions, and no queued continuation turns. Returns <code>true</code> when stable, or <code>false</code> if the timeout expires before a pending interaction resolves.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2048.md")
</div>
<p>This is especially useful with <code>saveMessages</code> for server-driven flows:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2049.md")
</div>
<h4 id="resetturnstate"><code>resetTurnState()</code></h4>
<p>Aborts the active turn and invalidates queued continuations. The built-in <code>CF_AGENT_CHAT_CLEAR</code> handler calls this automatically, but you can call it manually if needed.</p>
<h3 id="lifecycle-hooks">Lifecycle hooks</h3>
<p>Override <code>onConnect</code> and <code>onClose</code> to add custom logic. Stream resumption and message sync are handled for you:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2050.md")
</div>
<p>The <code>destroy()</code> method cancels any pending chat requests and cleans up stream state. It is called automatically when the Durable Object is evicted, but you can call it manually if needed.</p>
<h3 id="request-cancellation">Request cancellation</h3>
<p>When a user clicks &quot;stop&quot; in the chat UI, the client sends a <code>CF_AGENT_CHAT_REQUEST_CANCEL</code> message. The server propagates this to the <code>abortSignal</code> in <code>options</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2051.md")
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2032.md")
</aside>
<p>Subclasses can also cancel turns from inside the Durable Object:</p>
<pre><code class="language-ts">protected abortRequest(requestId: string, reason?: unknown): void&#10;protected abortAllRequests(): void&#10;</code></pre>
<p>Use <code>abortRequest()</code> when you know the request ID. Use <code>abortAllRequests()</code> for single-purpose helpers that should cancel whatever turn is currently running. Prefer <code>SaveMessagesOptions.signal</code> for programmatic turns when you can pass a signal at the call site.</p>
<h3 id="stream-recovery">Stream recovery</h3>
<p>Automatic stream resumption (the <code>resume</code> option on <code>useAgentChat</code>) is <strong>client reconnect recovery</strong> — it resumes an active stream when a client disconnects and reconnects. It does not cover Durable Object eviction. If the Worker process or Durable Object is evicted while the model call is in flight, the stream itself is gone. Durable chat recovery handles that case.</p>
<p>A mid-stream Durable Object eviction permanently severs the LLM connection. Durable recovery wraps every <code>AIChatAgent</code> and <a href="/agents/harnesses/think/"><code>Think</code></a> chat turn in a <a href="/agents/runtime/execution/durable-execution/"><code>runFiber()</code></a>. The fiber provides automatic <code>keepAlive</code> during streaming and a recovery hook on restart.</p>
<p>The fiber row survives in SQLite after an eviction. On the next activation, the framework detects the interrupted fiber. It reconstructs the partial response from buffered stream chunks and calls <code>onChatRecovery</code>.</p>
<p>Durable recovery is always on. Use <code>chatRecovery</code> only to tune recovery budgets and terminal behavior:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2052.md")
</div>
<p>The <code>chatRecovery</code> object accepts the following configuration options:</p>
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
<td><code>maxAttempts</code></td>
<td><code>10</code></td>
<td>Attempt cap before terminal exhaustion. Resets on forward progress, so it catches a tight no-progress alarm loop, not a healthy long turn.</td>
</tr>
<tr>
<td><code>stableTimeoutMs</code></td>
<td><code>10_000</code></td>
<td>How long a recovery attempt waits for the isolate to reach stable state before rescheduling.</td>
</tr>
<tr>
<td><code>terminalMessage</code></td>
<td>generic message</td>
<td>The message shown to the user when recovery is given up on.</td>
</tr>
<tr>
<td><code>noProgressTimeoutMs</code></td>
<td><code>300_000</code> (5 min)</td>
<td>Primary stuck-turn bound: how long an incident may go without forward progress before it is sealed (<code>no_progress_timeout</code>). <strong>Resets on every progress-bearing attempt</strong>, so a turn that keeps producing content survives unbounded interruption.</td>
</tr>
<tr>
<td><code>maxRecoveryWork</code></td>
<td><code>1,000</code></td>
<td>Runaway-loop guard. Maximum produced content/tool units since the incident began before a still-progressing turn is sealed. Set a higher value or <code>Infinity</code> for a long agentic turn.</td>
</tr>
<tr>
<td><code>maxOomRetries</code></td>
<td><code>3</code></td>
<td>Retry budget for Durable Object memory-limit resets. Set <code>0</code> to stop after the first memory-limit reset.</td>
</tr>
<tr>
<td><code>shouldKeepRecovering</code></td>
<td>—</td>
<td>Caller policy consulted from the second recovery attempt onward. Return <code>false</code> to stop recovery. Use it to enforce a token or cost budget. <code>ctx.work</code> is a coarse segment count, not tokens, so track real spend yourself.</td>
</tr>
<tr>
<td><code>onExhausted</code></td>
<td>—</td>
<td>Called once when recovery is given up on, before the terminal message is delivered. Inspect <code>ctx.reason</code> for why.</td>
</tr>
</tbody>
</table>
<p><code>ChatRecoveryProgressContext</code> (the <code>ctx</code> passed to <code>shouldKeepRecovering</code>) contains the following fields:</p>
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
<td><code>incidentId</code></td>
<td><code>string</code></td>
<td>Stable ID for this recovery incident.</td>
</tr>
<tr>
<td><code>requestId</code></td>
<td><code>string</code></td>
<td>Request ID for the current continuation (changes per chained continuation).</td>
</tr>
<tr>
<td><code>recoveryRootRequestId</code></td>
<td><code>string</code></td>
<td>Stable ID for the whole continuation chain — the right key for per-incident budget tracking.</td>
</tr>
<tr>
<td><code>attempt</code></td>
<td><code>number</code></td>
<td>Attempt number for this incident (2 or greater when this hook runs).</td>
</tr>
<tr>
<td><code>maxAttempts</code></td>
<td><code>number</code></td>
<td>Configured attempt cap.</td>
</tr>
<tr>
<td><code>recoveryKind</code></td>
<td><code>&quot;retry&quot; | &quot;continue&quot;</code></td>
<td>Whether recovery retries an unanswered user turn or continues a partial assistant turn.</td>
</tr>
<tr>
<td><code>work</code></td>
<td><code>number</code></td>
<td>Coarse, monotonic count of content/tool segments produced since the incident opened (not tokens).</td>
</tr>
<tr>
<td><code>ageMs</code></td>
<td><code>number</code></td>
<td>Wall-clock ms since the incident's first interruption.</td>
</tr>
</tbody>
</table>
<p>A progressing turn survives repeated interruptions as long as it stays within the <code>maxRecoveryWork</code> limit. Recovery is sealed by one of these <code>ctx.reason</code> values:</p>
<ul>
<li><code>no_progress_timeout</code> — no forward progress within the no-progress window (a stuck turn).</li>
<li><code>max_attempts_exceeded</code> — the attempt cap was spent on a tight no-progress alarm loop.</li>
<li><code>work_budget_exceeded</code> — the turn kept producing content but exceeded <code>maxRecoveryWork</code> (a runaway loop).</li>
<li><code>recovery_aborted</code> — your <code>shouldKeepRecovering</code> hook returned <code>false</code>.</li>
<li><code>out_of_memory</code> — recovery exceeded the memory-limit retry budget.</li>
<li><code>stable_timeout</code> — recovery attempts kept timing out waiting for stable state until the budget drained (extreme churn).</li>
</ul>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/2031.md")
</aside>
<h4 id="turns-waiting-on-a-human-are-not-sealed">Turns waiting on a human are not sealed</h4>
<p>A turn can pause on a client interaction it cannot resolve on its own: a client-side tool call (a tool with no server <code>execute</code>, whose result the client replays), or an <code>approval-requested</code> part. Such a turn is waiting on the human, not stuck.</p>
<p>While the interaction is pending, the turn is exempt from every recovery budget. The no-progress window, attempt cap, <code>maxRecoveryWork</code>, and <code>shouldKeepRecovering</code> are all suspended. A user who takes minutes to answer a prompt that was interrupted by a deploy never trips a seal. Recovery parks the turn instead of failing it, and the user's eventual approval or tool result resumes it through the normal continuation path.</p>
<p>This exemption is client-only. A server tool whose <code>execute()</code> was killed mid-flight is a genuine orphan, so it is not exempt and recovers through transcript repair instead.</p>
<p>Monitor terminal exhaustion through observability:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2053.md")
</div>
<h4 id="onchatrecovery"><code>onChatRecovery</code></h4>
<p>Override to implement provider-specific recovery. The default behavior persists the partial response and schedules a continuation via <code>continueLastTurn()</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2054.md")
</div>
<p><strong><code>ChatRecoveryContext</code>:</strong></p>
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
<td><code>incidentId</code></td>
<td><code>string</code></td>
<td>Stable ID for this recovery incident</td>
</tr>
<tr>
<td><code>attempt</code></td>
<td><code>number</code></td>
<td>Current attempt number for this incident, starting at 1</td>
</tr>
<tr>
<td><code>maxAttempts</code></td>
<td><code>number</code></td>
<td>Configured attempt cap before terminal exhaustion</td>
</tr>
<tr>
<td><code>recoveryKind</code></td>
<td><code>&quot;retry&quot; | &quot;continue&quot;</code></td>
<td>Whether recovery will retry an unanswered user turn or continue a partial assistant turn</td>
</tr>
<tr>
<td><code>streamId</code></td>
<td><code>string</code></td>
<td>ID of the interrupted stream</td>
</tr>
<tr>
<td><code>requestId</code></td>
<td><code>string</code></td>
<td>ID of the original chat request</td>
</tr>
<tr>
<td><code>partialText</code></td>
<td><code>string</code></td>
<td>Text generated before eviction</td>
</tr>
<tr>
<td><code>partialParts</code></td>
<td><code>MessagePart[]</code></td>
<td>Message parts (text, reasoning, tool calls) generated before eviction</td>
</tr>
<tr>
<td><code>recoveryData</code></td>
<td><code>unknown | null</code></td>
<td>Data from <code>this.stash()</code> — entirely user-controlled</td>
</tr>
<tr>
<td><code>messages</code></td>
<td><code>ChatMessage[]</code></td>
<td>Full conversation history</td>
</tr>
<tr>
<td><code>lastBody</code></td>
<td><code>Record&lt;string, unknown&gt; | undefined</code></td>
<td>The original request body</td>
</tr>
<tr>
<td><code>lastClientTools</code></td>
<td><code>ClientToolSchema[] | undefined</code></td>
<td>Client tool schemas from the original request</td>
</tr>
<tr>
<td><code>createdAt</code></td>
<td><code>number</code></td>
<td>Epoch milliseconds when the interrupted turn started</td>
</tr>
</tbody>
</table>
<p><strong><code>ChatRecoveryOptions</code>:</strong></p>
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
<td><code>persist</code></td>
<td><code>true</code></td>
<td>Save the partial response as an assistant message</td>
</tr>
<tr>
<td><code>continue</code></td>
<td><code>true</code></td>
<td>Schedule a continuation via <code>continueLastTurn()</code></td>
</tr>
</tbody>
</table>
<p>Common return values:</p>
<ul>
<li><code>{}</code> — persist partial + auto-continue (default, works with providers that support assistant prefill)</li>
<li><code>{ continue: false }</code> — persist partial but do not auto-continue (handle continuation yourself)</li>
<li><code>{ persist: false, continue: false }</code> — do not persist the unsettled remainder and handle everything yourself (for example, retrieve a completed response from the provider)</li>
</ul>
<p>Settled work is never dropped: <code>persist: false</code> only suppresses persistence of a partial that has nothing settled to lose. A partial that already carries settled tool results (completed, often non-idempotent work) is persisted regardless, so an app cannot accidentally discard completed tool calls — and never needs <code>{ persist: true }</code> just to stay safe.</p>
<p>When recovery happens before any stream chunks were written, there is no partial assistant message to continue. If the latest persisted message is still the unanswered user message from the interrupted turn, the framework retries that turn automatically unless <code>continue</code> is <code>false</code>.</p>
<p>Use <code>ctx.createdAt</code> to skip stale recoveries:</p>
<pre><code class="language-ts">override async onChatRecovery(&#10;	ctx: ChatRecoveryContext,&#10;): Promise&lt;ChatRecoveryOptions&gt; {&#10;	if (Date.now() - ctx.createdAt &gt; 2 * 60 * 1000) {&#10;		return { continue: false };&#10;	}&#10;	return {};&#10;}&#10;</code></pre>
<h4 id="control-automatic-continuation">Control automatic continuation</h4>
<p>Durable bookkeeping remains active when automatic continuation is not appropriate.</p>
<ul>
<li>Return <code>{ continue: false }</code> when another model call is unsafe.</li>
<li>Persist cancellation intent and read it in <code>onChatRecovery()</code>.</li>
<li>Record idempotency keys before external side effects.</li>
<li>Use recovery budgets with durable spend data to limit cost.</li>
</ul>
<h4 id="continuelastturn"><code>continueLastTurn</code></h4>
<p>Appends to the last assistant message by re-calling <code>onChatMessage</code> with the saved request body. The response is streamed as a continuation — appended to the existing assistant message, not a new one. No synthetic user message is created.</p>
<pre><code class="language-ts">protected continueLastTurn(&#10;	body?: Record&lt;string, unknown&gt;,&#10;	options?: SaveMessagesOptions,&#10;): Promise&lt;SaveMessagesResult&gt;;&#10;</code></pre>
<p>Called automatically by the default recovery path. Can also be called manually from scheduled callbacks or other entry points. The optional <code>body</code> parameter overrides the saved request body for this continuation. Pass <code>options.signal</code> to cancel the continuation while it is running.</p>
<h4 id="stashing-recovery-data">Stashing recovery data</h4>
<p>Use <code>this.stash()</code> inside <code>onChatMessage</code> to persist provider-specific data for recovery. The stash is stored in the fiber's SQLite row, separate from agent state, and available as <code>ctx.recoveryData</code> in <code>onChatRecovery</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2055.md")
</div>
<h4 id="recovery-strategies-by-provider">Recovery strategies by provider</h4>
<p>The right strategy depends on whether the provider supports assistant prefill and whether the response continues server-side after disconnection:</p>
<table>
<thead>
<tr>
<th>Provider</th>
<th>Strategy</th>
<th>Token cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>Workers AI</td>
<td><code>continueLastTurn()</code> — model continues via assistant prefill</td>
<td>Low</td>
</tr>
<tr>
<td>OpenAI (Responses API)</td>
<td>Retrieve completed response by ID — zero wasted tokens</td>
<td>Zero</td>
</tr>
<tr>
<td>Anthropic</td>
<td>Persist partial, send a synthetic user message to continue</td>
<td>Medium</td>
</tr>
</tbody>
</table>
<h4 id="recovering-status-on-the-client">Recovering status on the client</h4>
<p>While a turn is being recovered, the agent broadcasts a <code>cf_agent_chat_recovering</code> status frame so clients can show a &quot;recovering…&quot; indicator instead of looking frozen. It is set when a recovery continuation is scheduled and cleared on every terminal outcome, so the indicator never spins forever. Consume it through <code>useAgentChat</code>'s <code>isRecovering</code> flag (see <a href="#return-values">Return values</a>). The signal is advisory and backward-compatible — clients that do not understand it ignore it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2030.md")
</aside>
<p>Transcript repairs — healing orphaned tool calls (preserved as errored results rather than deleted, so the record survives and the model does not silently re-run the tool) and normalizing malformed or missing tool inputs before a provider call — are emitted on the <code>transcript</code> observability channel.</p>
<p>For how chat recovery fits into the broader long-running agents story, refer to <a href="/agents/concepts/agentic-patterns/long-running-agents/#recovering-interrupted-llm-streams">Long-running agents: Recovering interrupted LLM streams</a>. For the underlying fiber API, refer to <a href="/agents/runtime/execution/durable-execution/">Durable Execution</a>.</p>
<h2 id="client-api">Client API</h2>
<h3 id="useagentchat"><code>useAgentChat</code></h3>
<p>React hook that connects to an <code>AIChatAgent</code> over WebSocket. Wraps the AI SDK's <code>useChat</code> with a native WebSocket transport.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2056.md")
</div>
<h3 id="options">Options</h3>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>agent</code></td>
<td><code>ReturnType&lt;typeof useAgent&gt;</code></td>
<td>Required</td>
<td>Agent connection from <code>useAgent</code></td>
</tr>
<tr>
<td><code>onToolCall</code></td>
<td><code>({ toolCall, addToolOutput }) =&gt; void</code></td>
<td>—</td>
<td>Handle client-side tool execution</td>
</tr>
<tr>
<td><code>tools</code></td>
<td><code>Record&lt;string, AITool&gt;</code></td>
<td>—</td>
<td>Advanced: dynamically register client-executed tools from the browser</td>
</tr>
<tr>
<td><code>autoContinueAfterToolResult</code></td>
<td><code>boolean</code></td>
<td><code>true</code></td>
<td>Auto-continue conversation after client tool results and approvals</td>
</tr>
<tr>
<td><code>resume</code></td>
<td><code>boolean</code></td>
<td><code>true</code></td>
<td>Enable automatic stream resumption on reconnect</td>
</tr>
<tr>
<td><code>cancelOnClientAbort</code></td>
<td><code>boolean</code></td>
<td><code>false</code></td>
<td>Cancel the server turn when generic client stream abort or cleanup occurs</td>
</tr>
<tr>
<td><code>body</code></td>
<td><code>object | () =&gt; object</code></td>
<td>—</td>
<td>Custom data sent with every request</td>
</tr>
<tr>
<td><code>prepareSendMessagesRequest</code></td>
<td><code>(options) =&gt; { body?, headers? }</code></td>
<td>—</td>
<td>Advanced per-request customization</td>
</tr>
<tr>
<td><code>getInitialMessages</code></td>
<td><code>(options) =&gt; Promise&lt;UIMessage[]&gt;</code> or <code>null</code></td>
<td>—</td>
<td>Custom initial message loader. Set to <code>null</code> to skip the HTTP fetch entirely (useful when providing <code>messages</code> directly)</td>
</tr>
<tr>
<td><code>syncMessagesToServer</code></td>
<td><code>boolean</code></td>
<td><code>true</code></td>
<td>When <code>true</code>, <code>setMessages</code> pushes the transcript to the server. Set to <code>false</code> for hosts with server-authoritative transcript storage so <code>setMessages</code> updates the local view only</td>
</tr>
</tbody>
</table>
<h3 id="return-values">Return values</h3>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>messages</code></td>
<td><code>UIMessage[]</code></td>
<td>Current conversation messages</td>
</tr>
<tr>
<td><code>sendMessage</code></td>
<td><code>(message) =&gt; void</code></td>
<td>Send a message</td>
</tr>
<tr>
<td><code>clearHistory</code></td>
<td><code>() =&gt; void</code></td>
<td>Clear conversation (client and server)</td>
</tr>
<tr>
<td><code>addToolOutput</code></td>
<td><code>({ toolCallId, output }) =&gt; void</code></td>
<td>Provide output for a client-side tool</td>
</tr>
<tr>
<td><code>addToolApprovalResponse</code></td>
<td><code>({ id, approved }) =&gt; void</code></td>
<td>Approve or reject a tool requiring approval</td>
</tr>
<tr>
<td><code>setMessages</code></td>
<td><code>(messages | updater) =&gt; void</code></td>
<td>Set messages directly (syncs to server)</td>
</tr>
<tr>
<td><code>status</code></td>
<td><code>string</code></td>
<td><code>&quot;ready&quot;</code>, <code>&quot;submitted&quot;</code>, <code>&quot;streaming&quot;</code>, or <code>&quot;error&quot;</code></td>
</tr>
<tr>
<td><code>isStreaming</code></td>
<td><code>boolean</code></td>
<td><code>true</code> while the agent is streaming or waiting on an active client tool</td>
</tr>
<tr>
<td><code>isServerStreaming</code></td>
<td><code>boolean</code></td>
<td><code>true</code> while a server-initiated stream or active client-tool phase is in progress</td>
</tr>
<tr>
<td><code>isToolContinuation</code></td>
<td><code>boolean</code></td>
<td><code>true</code> while an automatic continuation after a tool result or approval is running</td>
</tr>
<tr>
<td><code>isRecovering</code></td>
<td><code>boolean</code></td>
<td><code>true</code> while a durable turn is being recovered (interrupted and resuming). Distinct from <code>isStreaming</code> — a recovering turn is not producing tokens yet. Render a &quot;recovering…&quot; hint; most UIs treat <code>isStreaming || isRecovering</code> as &quot;busy&quot;</td>
</tr>
</tbody>
</table>
<p>Use <code>isToolContinuation</code> when your UI should distinguish a fresh user submit from a continuation after a tool result. For example, show a typing indicator only for <code>status === &quot;submitted&quot; &amp;&amp; !isToolContinuation</code>, while keeping loading controls disabled whenever <code>isStreaming</code> is true.</p>
<h3 id="non-react-clients">Non-React clients</h3>
<p><code>useAgentChat</code> is React-specific. For Vue, Svelte, or vanilla JavaScript, <code>agents/chat/transport</code> exports <code>WebSocketChatTransport</code>, which adapts an <code>AgentClient</code> WebSocket connection to the AI SDK transport interface. This entry point requires no React peer dependency.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2057.md")
</div>
<p>The transport covers new turns, regenerated turns, and stream cancellation. It is a lower-level primitive than <code>useAgentChat</code>: loading persisted history, automatic stream resume after a reconnect, cross-tab transcript synchronization, and client-side tool continuations remain the React hook's responsibility. Implement whichever of those your client needs on top of the transport.</p>
<p>The <a href="https://github.com/cloudflare/agents/tree/main/examples/vue-chat"><code>vue-chat</code> example</a> shows a minimal Vue client, and <a href="https://github.com/cloudflare/agents/tree/main/examples/ai-chat"><code>ai-chat</code></a> shows the full React integration for comparison.</p>
<h2 id="tools">Tools</h2>
<p><code>AIChatAgent</code> supports three tool patterns, all using the AI SDK's <code>tool()</code> function:</p>
<table>
<thead>
<tr>
<th>Pattern</th>
<th>Where it runs</th>
<th>When to use</th>
</tr>
</thead>
<tbody>
<tr>
<td>Server-side</td>
<td>Server (automatic)</td>
<td>API calls, database queries, computations</td>
</tr>
<tr>
<td>Client-side</td>
<td>Browser (via <code>onToolCall</code>)</td>
<td>Geolocation, clipboard, camera, local storage</td>
</tr>
<tr>
<td>Approval</td>
<td>Server (after user approval)</td>
<td>Payments, deletions, external actions</td>
</tr>
</tbody>
</table>
<h3 id="server-side-tools">Server-side tools</h3>
<p>Tools with an <code>execute</code> function run automatically on the server:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2058.md")
</div>
<h3 id="client-side-tools">Client-side tools</h3>
<p>Define a tool on the server without <code>execute</code>, then handle it on the client with <code>onToolCall</code>. Use this for tools that need browser APIs.</p>
<p><strong>Server:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2059.md")
</div>
<p><strong>Client:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2060.md")
</div>
<p>When the LLM invokes <code>getLocation</code>, the stream pauses. The <code>onToolCall</code> callback fires, your code provides the output, and the conversation continues.</p>
<p>For SDKs or platforms where the browser decides the available tools at runtime, pass a <code>tools</code> object to <code>useAgentChat</code>. Tools with client-side <code>execute</code> functions are serialized and sent to the server automatically. On the server, <code>options.clientTools</code> and <code>createToolsFromClientSchemas()</code> remain supported for this dynamic tool pattern.</p>
<h3 id="tool-approval-human-in-the-loop">Tool approval (human-in-the-loop)</h3>
<p>Use <code>needsApproval</code> for tools that require user confirmation before executing.</p>
<p><strong>Server:</strong></p>
<pre><code class="language-ts">tools: {&#10;	processPayment: tool({&#10;		description: &quot;Process a payment&quot;,&#10;		inputSchema: z.object({&#10;			amount: z.coerce.number(),&#10;			recipient: z.string(),&#10;		}),&#10;		needsApproval: async ({ amount }) =&gt; amount &gt; 100,&#10;		execute: async ({ amount, recipient }) =&gt; charge(amount, recipient),&#10;	});&#10;}&#10;</code></pre>
<p><strong>Client:</strong></p>
<pre><code class="language-ts">import { getToolName, isToolUIPart } from &quot;ai&quot;;&#10;import {&#10;	getToolApproval,&#10;	getToolCallId,&#10;	getToolPartState,&#10;} from &quot;@cloudflare/ai-chat/react&quot;;&#10;&#10;const { messages, addToolApprovalResponse } = useAgentChat({ agent });&#10;&#10;// Render pending approvals from message parts&#10;{&#10;	messages.map((msg) =&gt;&#10;		msg.parts&#10;			.filter(&#10;				(part) =&gt;&#10;					isToolUIPart(part) &amp;&amp; getToolPartState(part) === &quot;waiting-approval&quot;,&#10;			)&#10;			.map((part) =&gt; (&#10;				&lt;div key={getToolCallId(part)}&gt;&#10;					&lt;p&gt;Approve {getToolName(part)}?&lt;/p&gt;&#10;					&lt;button&#10;						onClick={() =&gt; {&#10;							const approval = getToolApproval(part);&#10;							if (!approval) return;&#10;							addToolApprovalResponse({&#10;								id: approval.id,&#10;								approved: true,&#10;							});&#10;						}}&#10;					&gt;&#10;						Approve&#10;					&lt;/button&gt;&#10;					&lt;button&#10;						onClick={() =&gt; {&#10;							const approval = getToolApproval(part);&#10;							if (!approval) return;&#10;							addToolApprovalResponse({&#10;								id: approval.id,&#10;								approved: false,&#10;							});&#10;						}}&#10;					&gt;&#10;						Reject&#10;					&lt;/button&gt;&#10;				&lt;/div&gt;&#10;			)),&#10;	);&#10;}&#10;</code></pre>
<h4 id="custom-denial-messages-with-addtooloutput">Custom denial messages with <code>addToolOutput</code></h4>
<p>When a user rejects a tool, <code>addToolApprovalResponse({ id, approved: false })</code> sets the tool state to <code>output-denied</code> with a generic message. To give the LLM a more specific reason for the denial, use <code>addToolOutput</code> with <code>state: &quot;output-error&quot;</code> instead:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2061.md")
</div>
<p>This sends a <code>tool_result</code> to the LLM with your custom error text, so it can respond appropriately (for example, suggest an alternative or ask clarifying questions).</p>
<p><code>addToolApprovalResponse</code> (with <code>approved: false</code>) auto-continues the conversation when <code>autoContinueAfterToolResult</code> is enabled (the default). <code>addToolOutput</code> with <code>state: &quot;output-error&quot;</code> does <strong>not</strong> auto-continue — call <code>sendMessage()</code> afterward if you want the LLM to respond to the error.</p>
<p>For more patterns, refer to <a href="/agents/concepts/agentic-patterns/human-in-the-loop/">Human-in-the-loop</a>.</p>
<h2 id="custom-request-data">Custom request data</h2>
<p>Include custom data with every chat request using the <code>body</code> option:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2062.md")
</div>
<p>For dynamic values, use a function:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2063.md")
</div>
<p>Access these fields on the server:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2064.md")
</div>
<p>For advanced per-request customization (custom headers, different body per request), use <code>prepareSendMessagesRequest</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2065.md")
</div>
<h2 id="data-parts">Data parts</h2>
<p>Data parts let you attach typed JSON to messages alongside text — progress indicators, source citations, token usage, or any structured data your UI needs.</p>
<h3 id="writing-data-parts-server">Writing data parts (server)</h3>
<p>Use <code>createUIMessageStream</code> with <code>writer.write()</code> to send data parts from the server:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2066.md")
</div>
<h3 id="three-patterns">Three patterns</h3>
<table>
<thead>
<tr>
<th>Pattern</th>
<th>How</th>
<th>Persisted?</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Reconciliation</strong></td>
<td>Same <code>type</code> + <code>id</code> → updates in-place</td>
<td>Yes</td>
<td>Progressive state (searching → found)</td>
</tr>
<tr>
<td><strong>Append</strong></td>
<td>No <code>id</code>, or different <code>id</code> → appends</td>
<td>Yes</td>
<td>Log entries, multiple citations</td>
</tr>
<tr>
<td><strong>Transient</strong></td>
<td><code>transient: true</code> → not added to <code>message.parts</code></td>
<td>No</td>
<td>Ephemeral status (thinking indicator)</td>
</tr>
</tbody>
</table>
<p>Transient parts are broadcast to connected clients in real time but excluded from SQLite persistence and <code>message.parts</code>. Use the <code>onData</code> callback to consume them.</p>
<h3 id="reading-data-parts-client">Reading data parts (client)</h3>
<p>Non-transient data parts appear in <code>message.parts</code>. Use the <code>UIMessage</code> generic to type them:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2067.md")
</div>
<h3 id="transient-parts-with-ondata">Transient parts with <code>onData</code></h3>
<p>Transient data parts are not in <code>message.parts</code>. Use the <code>onData</code> callback instead:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2068.md")
</div>
<p>On the server, write transient parts with <code>transient: true</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2069.md")
</div>
<p><code>onData</code> fires on all code paths — new messages, stream resumption, and cross-tab broadcasts.</p>
<h2 id="resumable-streaming">Resumable streaming</h2>
<p>Streams automatically resume when a client disconnects and reconnects. No configuration is needed — it works out of the box.</p>
<p>When streaming is active:</p>
<ol>
<li>All chunks are buffered in SQLite as they are generated</li>
<li>If the client disconnects, the server continues streaming and buffering</li>
<li>When the client reconnects, it receives all buffered chunks and resumes live streaming</li>
</ol>
<p>Generic client stream abort or cleanup stays local to the browser by default, so the server turn keeps running and can be resumed later. Calling <code>stop()</code> explicitly still cancels the server turn:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2070.md")
</div>
<p>Set <code>cancelOnClientAbort: true</code> when your app intentionally wants the browser lifecycle to own the server lifecycle, such as request-lifetime or token-saving flows. Explicit <code>stop()</code> always cancels server work regardless of this option.</p>
<p>Disable with <code>resume: false</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2071.md")
</div>
<h2 id="storage-management">Storage management</h2>
<h3 id="row-size-protection">Row size protection</h3>
<p>Workers SQLite rows have a hard maximum size of 2 MB. To stay below that limit, <code>AIChatAgent</code> starts compacting a serialized message at roughly 1.8 MB, for example when a tool returns a very large output:</p>
<ol>
<li><strong>Tool output compaction</strong> — Large tool outputs are replaced with an LLM-friendly summary that instructs the model to suggest re-running the tool</li>
<li><strong>Text truncation</strong> — If the message is still too large after tool compaction, text parts are truncated with a note</li>
</ol>
<p>Compacted messages include <code>metadata.compactedToolOutputs</code> so clients can detect and display this gracefully.</p>
<h3 id="controlling-llm-context-vs-storage">Controlling LLM context vs storage</h3>
<p>Storage (<code>maxPersistedMessages</code>) and LLM context are independent:</p>
<table>
<thead>
<tr>
<th>Concern</th>
<th>Control</th>
<th>Scope</th>
</tr>
</thead>
<tbody>
<tr>
<td>How many messages SQLite stores</td>
<td><code>maxPersistedMessages</code></td>
<td>Persistence</td>
</tr>
<tr>
<td>What the model sees</td>
<td><code>pruneMessages()</code></td>
<td>LLM context</td>
</tr>
<tr>
<td>Row size limits</td>
<td>Automatic compaction</td>
<td>Per-message</td>
</tr>
</tbody>
</table>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2072.md")
</div>
<h2 id="using-different-ai-providers">Using different AI providers</h2>
<p><code>AIChatAgent</code> works with any AI SDK-compatible provider. The server code determines which model to use — the client does not need to change it manually.</p>
<h3 id="workers-ai-cloudflare">Workers AI (Cloudflare)</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2073.md")
</div>
<h3 id="openai">OpenAI</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2074.md")
</div>
<h3 id="anthropic">Anthropic</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2075.md")
</div>
<h2 id="advanced-patterns">Advanced patterns</h2>
<p>Since <code>onChatMessage</code> gives you full control over the <code>streamText</code> call, you can use any AI SDK feature directly. The patterns below all work out of the box — no special <code>AIChatAgent</code> configuration is needed.</p>
<h3 id="dynamic-model-and-tool-control">Dynamic model and tool control</h3>
<p>Use <a href="https://ai-sdk.dev/docs/agents/loop-control"><code>prepareStep</code></a> to change the model, available tools, or system prompt between steps in a multi-step agent loop:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2076.md")
</div>
<p><code>prepareStep</code> runs before each step and can return overrides for <code>model</code>, <code>activeTools</code>, <code>toolChoice</code>, <code>system</code>, and <code>messages</code>. Use it to:</p>
<ul>
<li><strong>Switch models</strong> — use a cheap model for simple steps, escalate for reasoning</li>
<li><strong>Phase tools</strong> — restrict which tools are available at each step</li>
<li><strong>Manage context</strong> — prune or transform messages to stay within token limits</li>
<li><strong>Force tool calls</strong> — use <code>toolChoice: { type: &quot;tool&quot;, toolName: &quot;search&quot; }</code> to require a specific tool</li>
</ul>
<h3 id="language-model-middleware">Language model middleware</h3>
<p>Use <a href="https://ai-sdk.dev/docs/ai-sdk-core/middleware"><code>wrapLanguageModel</code></a> to add guardrails, RAG, caching, or logging without modifying your chat logic:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2077.md")
</div>
<p>The AI SDK includes built-in middlewares:</p>
<ul>
<li><code>extractReasoningMiddleware</code> — surface chain-of-thought from models like DeepSeek R1</li>
<li><code>defaultSettingsMiddleware</code> — apply default temperature, max tokens, etc.</li>
<li><code>simulateStreamingMiddleware</code> — add streaming to non-streaming models</li>
</ul>
<p>Multiple middlewares compose in order: <code>middleware: [first, second]</code> applies as <code>first(second(model))</code>.</p>
<h3 id="structured-output">Structured output</h3>
<p>Use <a href="https://ai-sdk.dev/docs/ai-sdk-core/generating-structured-data"><code>generateObject</code></a> inside tools for structured data extraction:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2078.md")
</div>
<h3 id="in-process-subagent-delegation">In-process subagent delegation</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2029.md")
</aside>
<p>Tools can delegate work to focused sub-calls with their own context. Use <a href="https://ai-sdk.dev/docs/reference/ai-sdk-core/tool-loop-agent"><code>ToolLoopAgent</code></a> to define a reusable agent, then call it from a tool's <code>execute</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2079.md")
</div>
<p>The research agent runs in its own context — its token budget is separate from the orchestrator's. Only the summary goes back to the parent model.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2028.md")
</aside>
<h4 id="streaming-progress-with-preliminary-results">Streaming progress with preliminary results</h4>
<p>By default, a tool part appears as loading until <code>execute</code> returns. Use an async generator (<code>async function*</code>) to stream progress updates to the client while the tool is still working:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2080.md")
</div>
<p>Each <code>yield</code> updates the tool part on the client in real-time (with <code>preliminary: true</code>). The last yielded value becomes the final output that the model sees.</p>
<p>This pattern is useful when:</p>
<ul>
<li>A task requires exploring large amounts of information that would bloat the main context</li>
<li>You want to show real-time progress for long-running tools</li>
<li>You want to parallelize independent research (multiple tool calls run concurrently)</li>
<li>You need different models or system prompts for different subtasks</li>
</ul>
<p>For more, refer to the <a href="https://ai-sdk.dev/docs/agents/overview">AI SDK Agents docs</a>, <a href="https://ai-sdk.dev/docs/agents/subagents">Subagents</a>, and <a href="https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling#preliminary-tool-results">Preliminary Tool Results</a>.</p>
<h2 id="multi-client-sync">Multi-client sync</h2>
<p>When multiple clients connect to the same agent instance, messages are automatically broadcast to all connections. If one client sends a message, all other connected clients receive the updated message list.</p>
<pre><code>Client A ──── sendMessage(&quot;Hello&quot;) ────▶ AIChatAgent&#10;                                              │&#10;                                        persist + stream&#10;                                              │&#10;Client A ◀── CF_AGENT_USE_CHAT_RESPONSE ──────┤&#10;Client B ◀── CF_AGENT_CHAT_MESSAGES ──────────┘&#10;</code></pre>
<p>The originating client receives the streaming response. All other clients receive the final messages via a <code>CF_AGENT_CHAT_MESSAGES</code> broadcast.</p>
<h2 id="api-reference">API reference</h2>
<h3 id="exports">Exports</h3>
<table>
<thead>
<tr>
<th>Import path</th>
<th>Exports</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cloudflare/ai-chat</code></td>
<td><code>AIChatAgent</code>, <code>createToolsFromClientSchemas</code>, <code>ClientToolSchema</code>, <code>ChatRecoveryContext</code>, <code>ChatRecoveryOptions</code>, <code>ChatRecoveryConfig</code>, <code>ChatRecoveryExhaustedContext</code>, <code>ResolvedChatRecoveryConfig</code>, lifecycle types</td>
</tr>
<tr>
<td><code>@cloudflare/ai-chat/react</code></td>
<td><code>useAgentChat</code>, <code>extractClientToolSchemas</code>, <code>getToolPartState</code>, <code>getToolCallId</code>, <code>getToolInput</code>, <code>getToolOutput</code>, <code>getToolApproval</code></td>
</tr>
<tr>
<td><code>@cloudflare/ai-chat/types</code></td>
<td><code>MessageType</code>, <code>OutgoingMessage</code>, <code>IncomingMessage</code></td>
</tr>
<tr>
<td><code>agents/chat</code></td>
<td>Shared advanced chat primitives such as <code>SaveMessagesResult</code>, <code>SaveMessagesOptions</code>, <code>CHAT_MESSAGE_TYPES</code>, <code>ROW_MAX_BYTES</code>, and <code>isReplayChunk()</code></td>
</tr>
<tr>
<td><code>agents/chat/transport</code></td>
<td><code>WebSocketChatTransport</code> and its <code>AgentConnection</code> connection types, for non-React clients</td>
</tr>
</tbody>
</table>
<h3 id="websocket-protocol">WebSocket protocol</h3>
<p>The chat protocol uses typed JSON messages over WebSocket:</p>
<table>
<thead>
<tr>
<th>Message</th>
<th>Direction</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CF_AGENT_USE_CHAT_REQUEST</code></td>
<td>Client → Server</td>
<td>Send a chat message</td>
</tr>
<tr>
<td><code>CF_AGENT_USE_CHAT_RESPONSE</code></td>
<td>Server → Client</td>
<td>Stream response chunks</td>
</tr>
<tr>
<td><code>CF_AGENT_CHAT_MESSAGES</code></td>
<td>Server → Client</td>
<td>Broadcast updated messages</td>
</tr>
<tr>
<td><code>CF_AGENT_CHAT_CLEAR</code></td>
<td>Bidirectional</td>
<td>Clear conversation</td>
</tr>
<tr>
<td><code>CF_AGENT_CHAT_REQUEST_CANCEL</code></td>
<td>Client → Server</td>
<td>Cancel active stream</td>
</tr>
<tr>
<td><code>CF_AGENT_TOOL_RESULT</code></td>
<td>Client → Server</td>
<td>Provide tool output</td>
</tr>
<tr>
<td><code>CF_AGENT_TOOL_APPROVAL</code></td>
<td>Client → Server</td>
<td>Approve or reject a tool</td>
</tr>
<tr>
<td><code>CF_AGENT_MESSAGE_UPDATED</code></td>
<td>Server → Client</td>
<td>Notify of message update</td>
</tr>
<tr>
<td><code>CF_AGENT_STREAM_RESUMING</code></td>
<td>Server → Client</td>
<td>Notify of stream resumption</td>
</tr>
<tr>
<td><code>CF_AGENT_STREAM_RESUME_REQUEST</code></td>
<td>Client → Server</td>
<td>Request stream resume check</td>
</tr>
<tr>
<td><code>CF_AGENT_STREAM_RESUME_ACK</code></td>
<td>Server → Client</td>
<td>Resume stream from a cursor</td>
</tr>
<tr>
<td><code>CF_AGENT_STREAM_RESUME_NONE</code></td>
<td>Server → Client</td>
<td>No resumable stream exists</td>
</tr>
</tbody>
</table>
<h2 id="deprecated-apis">Deprecated APIs</h2>
<p>The following APIs are deprecated and will emit a console warning when used. They will be removed in a future release.</p>
<table>
<thead>
<tr>
<th>Deprecated</th>
<th>Replacement</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>addToolResult({ toolCallId, result })</code></td>
<td><code>addToolOutput({ toolCallId, output })</code></td>
<td>Renamed for consistency with AI SDK terminology</td>
</tr>
<tr>
<td><code>detectToolsRequiringConfirmation()</code></td>
<td>Use <code>needsApproval</code> on the tool definition</td>
<td>Approval is now per-tool, not a global filter</td>
</tr>
<tr>
<td><code>toolsRequiringConfirmation</code> option</td>
<td>Use <code>needsApproval</code> on individual tools</td>
<td>Per-tool approval replaces global list</td>
</tr>
</tbody>
</table>
<p>If you are upgrading from an earlier version, replace deprecated calls with their replacements. The deprecated APIs still work but will be removed in a future major version.</p>
<p><code>createToolsFromClientSchemas()</code>, <code>extractClientToolSchemas()</code>, and the <code>tools</code> option on <code>useAgentChat</code> are still supported for dynamic client-side tools. They are advanced APIs, not deprecated APIs.</p>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/communication-channels/chat/client-sdk/"><h3 id="card-client-sdk-agents-communication-channels-chat-client-sdk">Client SDK</h3><p>useAgent hook and AgentClient class.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/concepts/agentic-patterns/human-in-the-loop/"><h3 id="card-human-in-the-loop-agents-concepts-agentic-patterns-human-in-the-loop">Human-in-the-loop</h3><p>Approval flows and manual intervention patterns.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/examples/chat-agent/"><h3 id="card-build-a-chat-agent-agents-examples-chat-agent">Build a chat agent</h3><p>Step-by-step tutorial for building your first chat agent.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/execution/durable-execution/"><h3 id="card-durable-execution-agents-runtime-execution-durable-execution">Durable execution</h3><p>runFiber(), stash(), and crash recovery for long-running work.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/concepts/agentic-patterns/long-running-agents/"><h3 id="card-long-running-agents-agents-concepts-agentic-patterns-long-running-agents">Long-running agents</h3><p>Lifecycle, recovery patterns, and provider-specific strategies.</p></a></p>
