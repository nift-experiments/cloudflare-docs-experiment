---
cp9:
  canonical: https://developers.cloudflare.com/agents/runtime/execution/durable-execution/
  description: Run work that survives Durable Object eviction with runFiber(), startFiber(), keepAlive(), and crash recovery.
  full_title: Durable execution with fibers · Cloudflare Agents docs
  head_html: <title>Durable execution with fibers · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Run work that survives Durable Object eviction with runFiber(), startFiber(), keepAlive(), and crash recovery."><link rel="canonical" href="https://developers.cloudflare.com/agents/runtime/execution/durable-execution/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/runtime/execution/durable-execution/index.md"><meta property="og:title" content="Durable execution with fibers · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Run work that survives Durable Object eviction with runFiber(), startFiber(), keepAlive(), and crash recovery."><meta property="og:url" content="https://developers.cloudflare.com/agents/runtime/execution/durable-execution/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/runtime/execution/durable-execution/#page","headline":"Durable execution with fibers \u00b7 Cloudflare Agents docs","description":"Run work that survives Durable Object eviction with runFiber(), startFiber(), keepAlive(), and crash recovery.","url":"https://developers.cloudflare.com/agents/runtime/execution/durable-execution/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /agents/runtime/execution/durable-execution/
  schema: 1
---
<p>Run work that survives Durable Object eviction. <code>runFiber()</code> registers a task in SQLite, keeps the agent alive during execution, lets you checkpoint intermediate state with <code>stash()</code>, and calls <code>onFiberRecovered()</code> on the next activation if the agent was evicted mid-task.</p>
<p>Use <code>startFiber()</code> when a caller needs to durably accept background work, return quickly, safely dedupe retries, inspect status later, or cancel a running job.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2544.md")
</aside>
<h2 id="quick-start">Quick start</h2>
<pre tabindex="0"><code class="language-ts">import { Agent } from &quot;agents&quot;;&#10;import type { FiberRecoveryContext } from &quot;agents&quot;;&#10;&#10;class MyAgent extends Agent {&#10;	async doWork() {&#10;		await this.runFiber(&quot;my-task&quot;, async (ctx) =&gt; {&#10;			const step1 = await expensiveOperation();&#10;			ctx.stash({ step1 });&#10;&#10;			const step2 = await anotherExpensiveOperation(step1);&#10;			this.setState({ ...this.state, result: step2 });&#10;		});&#10;	}&#10;&#10;	async onFiberRecovered(ctx: FiberRecoveryContext) {&#10;		if (ctx.name !== &quot;my-task&quot;) return;&#10;		const snapshot = ctx.snapshot as { step1: unknown } | null;&#10;		if (snapshot) {&#10;			const step2 = await anotherExpensiveOperation(snapshot.step1);&#10;			this.setState({ ...this.state, result: step2 });&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h2 id="why-fibers-exist">Why fibers exist</h2>
<p>Durable Objects get evicted for three reasons:</p>
<ol>
<li><strong>Inactivity timeout</strong> — ~70–140 seconds with no incoming requests or open WebSockets</li>
<li><strong>Code updates / runtime restarts</strong> — non-deterministic, 1–2x per day</li>
<li><strong>Alarm handler timeout</strong> — 15 minutes</li>
</ol>
<p>When eviction happens mid-work, the upstream HTTP connection (to an LLM provider, an API, a database) is severed permanently. In-memory state — streaming buffers, partial responses, loop counters — is lost. Multi-turn agent loops lose their position entirely.</p>
<p><code>keepAlive()</code> reduces the chance of eviction. <code>runFiber()</code> makes eviction survivable.</p>
<p>For work that should run independently of the agent with per-step retries and multi-step orchestration, use <a href="/agents/runtime/execution/run-workflows/">Workflows</a> instead. Fibers are for work that is part of the agent's own execution. Refer to <a href="/agents/concepts/agentic-patterns/long-running-agents/#when-to-use-workflows-vs-agent-internal-patterns">Long-running agents: Workflows vs agent-internal patterns</a> for a comparison.</p>
<h2 id="keepalive">keepAlive</h2>
<p>Prevents idle eviction by creating a 30-second alarm heartbeat that resets the inactivity timer.</p>
<pre tabindex="0"><code class="language-ts">class Agent {&#10;	keepAlive(): Promise&lt;() =&gt; void&gt;;&#10;	keepAliveWhile&lt;T&gt;(fn: () =&gt; Promise&lt;T&gt;): Promise&lt;T&gt;;&#10;}&#10;</code></pre>
<p><code>keepAliveWhile()</code> is the recommended approach — it runs an async function and automatically cleans up the heartbeat when it completes or throws:</p>
<pre tabindex="0"><code class="language-ts">const result = await this.keepAliveWhile(async () =&gt; {&#10;	return await slowAPICall();&#10;});&#10;</code></pre>
<p>For manual control, <code>keepAlive()</code> returns a disposer. Always call it when done — otherwise the heartbeat continues indefinitely:</p>
<pre tabindex="0"><code class="language-ts">const dispose = await this.keepAlive();&#10;try {&#10;	await longWork();&#10;} finally {&#10;	dispose();&#10;}&#10;</code></pre>
<h3 id="how-it-works">How it works</h3>
<p>While any <code>keepAlive</code> ref is held, an alarm fires every 30 seconds that resets the inactivity timer. When all disposers are called, alarms stop and the DO can go idle naturally.</p>
<p>The heartbeat is invisible to <code>listSchedules()</code> — no schedule rows are created. It does not conflict with your own schedules; the alarm system multiplexes all schedules and the keepAlive heartbeat through a single alarm slot.</p>
<h3 id="configurable-interval">Configurable interval</h3>
<p>Default: 30 seconds. The inactivity timeout is ~70–140 seconds, so 30 seconds gives comfortable margin. Override via static options:</p>
<pre tabindex="0"><code class="language-ts">class MyAgent extends Agent {&#10;	static options = { keepAliveIntervalMs: 2_000 };&#10;}&#10;</code></pre>
<h3 id="when-to-use-keepalive-vs-runfiber">When to use keepAlive vs runFiber</h3>
<p><code>keepAlive</code> prevents eviction but does nothing about recovery. If the agent <em>is</em> evicted despite the heartbeat (code update, alarm timeout, resource limit), any in-progress work is lost.</p>
<p><code>runFiber</code> calls <code>keepAlive</code> internally <em>and</em> persists the work in SQLite so it can be recovered. Use <code>keepAlive</code> alone when the work is cheap to redo or does not need checkpointing. Use <code>runFiber</code> when the work is expensive and you need to resume from where you left off.</p>
<table>
<thead>
<tr>
<th>Scenario</th>
<th>Use</th>
</tr>
</thead>
<tbody>
<tr>
<td>Waiting on a slow API call</td>
<td><code>keepAlive()</code></td>
</tr>
<tr>
<td>Streaming an LLM response (via <code>AIChatAgent</code>)</td>
<td>Automatic (built in)</td>
</tr>
<tr>
<td>Multi-step computation with intermediate results</td>
<td><code>runFiber()</code></td>
</tr>
<tr>
<td>Background research loop that takes 10+ minutes</td>
<td><code>runFiber()</code> with <code>stash()</code></td>
</tr>
<tr>
<td>Webhook job that must be accepted exactly once</td>
<td><code>startFiber()</code></td>
</tr>
</tbody>
</table>
<h2 id="runfiber">runFiber</h2>
<p>Durable execution with checkpointing and recovery.</p>
<pre tabindex="0"><code class="language-ts">class Agent {&#10;	runFiber&lt;T&gt;(name: string, fn: (ctx: FiberContext) =&gt; Promise&lt;T&gt;): Promise&lt;T&gt;;&#10;	startFiber(&#10;		name: string,&#10;		fn: (ctx: FiberContext) =&gt; Promise&lt;void&gt;,&#10;		options?: StartFiberOptions,&#10;	): Promise&lt;StartFiberResult&gt;;&#10;	inspectFiber(fiberId: string): Promise&lt;FiberInspection | null&gt;;&#10;	inspectFiberByKey(idempotencyKey: string): Promise&lt;FiberInspection | null&gt;;&#10;	listFibers(options?: ListFibersOptions): Promise&lt;FiberInspection[]&gt;;&#10;	cancelFiber(fiberId: string, reason?: string): Promise&lt;boolean&gt;;&#10;	cancelFiberByKey(idempotencyKey: string, reason?: string): Promise&lt;boolean&gt;;&#10;	deleteFibers(options?: DeleteFibersOptions): Promise&lt;number&gt;;&#10;	resolveFiber(fiberId: string, result: FiberRecoveryResult): Promise&lt;boolean&gt;;&#10;	stash(data: unknown): void;&#10;	onFiberRecovered(&#10;		ctx: FiberRecoveryContext,&#10;	): Promise&lt;void | FiberRecoveryResult&gt;;&#10;}&#10;&#10;type FiberContext = {&#10;	id: string;&#10;	signal: AbortSignal;&#10;	stash(data: unknown): void;&#10;	snapshot: unknown | null;&#10;};&#10;&#10;type FiberStatus =&#10;	| &quot;pending&quot;&#10;	| &quot;running&quot;&#10;	| &quot;completed&quot;&#10;	| &quot;aborted&quot;&#10;	| &quot;interrupted&quot;&#10;	| &quot;error&quot;;&#10;&#10;type FiberRecoveryContext = {&#10;	id: string;&#10;	name: string;&#10;	status?: FiberStatus;&#10;	idempotencyKey?: string;&#10;	metadata?: Record&lt;string, unknown&gt; | null;&#10;	snapshot: unknown | null;&#10;	createdAt: number;&#10;	recoveryReason: &quot;interrupted&quot;;&#10;};&#10;</code></pre>
<h3 id="lifecycle">Lifecycle</h3>
<h4 id="normal-execution">Normal execution</h4>
<pre tabindex="0"><code class="language-txt">runFiber(&quot;work&quot;, fn)&#10;  ├─ Persist recovery metadata&#10;  ├─ keepAlive() — heartbeat starts&#10;  ├─ Execute fn(ctx)&#10;  │    ├─ ctx.stash(data) → persist snapshot&#10;  │    ├─ ctx.stash(data) → persist snapshot&#10;  │    └─ return result&#10;  ├─ Delete recovery metadata&#10;  ├─ keepAlive dispose — heartbeat stops&#10;  └─ Return result to caller&#10;</code></pre>
<h4 id="eviction-and-recovery">Eviction and recovery</h4>
<pre tabindex="0"><code class="language-txt">[DO evicted — all in-memory state lost]&#10;&#10;  On next activation:&#10;  ├─ Request/connection → onStart() → check for orphaned fibers  [primary path]&#10;  │  OR&#10;  ├─ Persisted alarm fires → housekeeping check                   [fallback path]&#10;&#10;  Recovery:&#10;  ├─ Load interrupted fibers from storage&#10;  ├─ For each interrupted fiber:&#10;  │    ├─ Parse snapshot from JSON&#10;  │    ├─ Call onFiberRecovered(ctx)&#10;  │    └─ Delete recovery metadata after successful recovery&#10;  └─ If onFiberRecovered calls runFiber() again → new fiber, normal execution&#10;</code></pre>
<p>Both recovery paths call the same hook. The alarm path is critical for background agents that have no incoming client connections — the persisted alarm wakes the agent on its own.</p>
<h4 id="sub-agents">Sub-agents</h4>
<p>Fibers also work inside sub-agents. The fiber row and snapshots are stored in the sub-agent's own SQLite database, and <code>onFiberRecovered()</code> runs with the sub-agent as <code>this</code>.</p>
<p>Sub-agents do not have independent alarm slots, so the top-level parent owns the physical heartbeat. When a sub-agent starts a fiber, the parent tracks enough metadata to route recovery checks back into the owning sub-agent, even if the child has no client connection or incoming RPC.</p>
<p>This keeps recovery local to the child while preserving the single physical alarm slot owned by the parent. A recovered continuation can use <code>schedule()</code> from inside the facet; the parent owns the physical alarm and routes the callback back to the child.</p>
<h4 id="error-during-execution">Error during execution</h4>
<pre tabindex="0"><code class="language-txt">fn(ctx) throws Error&#10;  ├─ DELETE row from cf_agents_runs&#10;  ├─ keepAlive dispose&#10;  └─ Error propagates to caller (or logged if fire-and-forget)&#10;</code></pre>
<p>No automatic retries. Recovery logic belongs in <code>onFiberRecovered</code>, where you have the snapshot and full context about what went wrong.</p>
<h3 id="inline-vs-fire-and-forget">Inline vs fire-and-forget</h3>
<p><code>runFiber()</code> supports both patterns:</p>
<pre tabindex="0"><code class="language-ts">// Inline — await the result&#10;const result = await this.runFiber(&quot;work&quot;, async (ctx) =&gt; {&#10;	return computeExpensiveThing();&#10;});&#10;&#10;// Fire-and-forget — caller does not wait&#10;void this.runFiber(&quot;background&quot;, async (ctx) =&gt; {&#10;	await longRunningProcess();&#10;});&#10;</code></pre>
<p>If the DO is evicted during an inline <code>await</code>, the caller is gone. On recovery, <code>onFiberRecovered</code> fires — it cannot return a result to the original caller. This is the inherent limitation of durable execution across process boundaries. For long-running work that is likely to outlive a single DO lifetime, use <code>startFiber()</code> when callers need a retained status record, idempotent acceptance, or cancellation.</p>
<h2 id="startfiber">startFiber</h2>
<p>Use <code>startFiber()</code> when a caller needs to durably accept background work, return quickly, and safely dedupe retries. It stores a retained fiber record before the callback runs, then starts the callback in the background using the same keep-alive and recovery machinery as <code>runFiber()</code>.</p>
<pre tabindex="0"><code class="language-ts">const receipt = await this.startFiber(&#10;	&quot;reply-to-webhook&quot;,&#10;	async (ctx) =&gt; {&#10;		ctx.stash({ webhookId, threadId });&#10;		await postReply(threadId);&#10;	},&#10;	{&#10;		idempotencyKey: `webhook:${webhookId}`,&#10;		metadata: { threadId },&#10;	},&#10;);&#10;&#10;if (!receipt.accepted) {&#10;	// This webhook was already accepted by an earlier delivery.&#10;}&#10;</code></pre>
<p>By default, <code>startFiber()</code> returns after the work is durably accepted. Pass <code>waitForCompletion: true</code> when the caller should remain open until the accepted fiber reaches a terminal status. Duplicate calls with the same idempotency key join an active in-memory execution when possible, then return the retained status with <code>accepted: false</code>.</p>
<pre tabindex="0"><code class="language-ts">const result = await this.startFiber(&quot;reply-to-webhook&quot;, reply, {&#10;	idempotencyKey: `webhook:${webhookId}`,&#10;	waitForCompletion: true,&#10;});&#10;&#10;if (result.status === &quot;error&quot;) {&#10;	console.error(result.error);&#10;}&#10;</code></pre>
<p><code>startFiber()</code> is a durable acceptance API, not a value-return API. It returns the managed fiber status, but not the callback's result. Inspect status later with <code>inspectFiber()</code> or <code>inspectFiberByKey()</code>.</p>
<pre tabindex="0"><code class="language-ts">const current = await this.inspectFiberByKey(`webhook:${webhookId}`);&#10;&#10;if (current) {&#10;	await this.cancelFiber(current.fiberId, &quot;No longer needed&quot;);&#10;}&#10;&#10;await this.deleteFibers({&#10;	status: [&quot;completed&quot;, &quot;error&quot;, &quot;aborted&quot;],&#10;	settledBefore: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000),&#10;});&#10;</code></pre>
<p>By default, <code>deleteFibers()</code> deletes settled <code>completed</code>, <code>error</code>, and <code>aborted</code> rows. It does not delete <code>interrupted</code> rows unless you pass that status explicitly, because interrupted rows often need inspection or manual resolution.</p>
<p>Cancellation is cooperative. <code>cancelFiber()</code> records an aborted terminal state and aborts <code>ctx.signal</code> if the fiber is running in the current isolate. Your callback should check <code>ctx.signal.aborted</code> around expensive work and before visible side effects. Callers using <code>waitForCompletion: true</code> return when the ledger reaches <code>aborted</code>, even if a non-cooperative callback keeps running in the current isolate.</p>
<p>If the Durable Object is evicted mid-fiber, the retained record is marked <code>interrupted</code> and <code>onFiberRecovered()</code> receives the last checkpoint. The original closure cannot be replayed automatically; use <code>ctx.name</code>, <code>ctx.snapshot</code>, and metadata to decide whether to resume, compensate, or leave the record for inspection.</p>
<p>Return a <code>FiberRecoveryResult</code> from <code>onFiberRecovered()</code> to record the policy decision:</p>
<pre tabindex="0"><code class="language-ts">async onFiberRecovered(ctx: FiberRecoveryContext) {&#10;	if (ctx.name !== &quot;reply-to-webhook&quot;) return;&#10;&#10;	const snapshot = ctx.snapshot as { webhookId: string; threadId: string };&#10;	await postRecoveryMessage(snapshot.threadId);&#10;&#10;	return {&#10;		status: &quot;completed&quot;,&#10;		snapshot: { ...snapshot, recovered: true },&#10;	};&#10;}&#10;</code></pre>
<p>Returning <code>undefined</code> keeps a managed fiber <code>interrupted</code>. Throwing leaves it <code>interrupted</code> and records the recovery error for inspection. Terminal managed fibers such as <code>aborted</code> are not recovered again if a stale run row remains.</p>
<p>If recovery is triggered by a later duplicate webhook instead of <code>onFiberRecovered()</code>, use <code>resolveFiber()</code> with the same result shape after your application-level recovery succeeds. <code>resolveFiber()</code> only updates managed fibers that are currently <code>interrupted</code>; it returns <code>false</code> for pending, running, or already-terminal rows.</p>
<h2 id="checkpoints-with-stash">Checkpoints with stash</h2>
<p><code>ctx.stash(data)</code> writes to SQLite <strong>synchronously</strong>. There is no async gap between &quot;I decided to save&quot; and &quot;it is saved.&quot; If eviction happens after <code>stash()</code> returns, the data is guaranteed to be in SQLite.</p>
<p>Each call <strong>fully replaces</strong> the previous snapshot — it is not a merge. Write the complete recovery state you need:</p>
<pre tabindex="0"><code class="language-ts">await this.runFiber(&quot;research&quot;, async (ctx) =&gt; {&#10;	const steps = [&quot;search&quot;, &quot;analyze&quot;, &quot;synthesize&quot;];&#10;	const completed: string[] = [];&#10;	const results: Record&lt;string, unknown&gt; = {};&#10;&#10;	for (const step of steps) {&#10;		results[step] = await executeStep(step);&#10;		completed.push(step);&#10;&#10;		ctx.stash({&#10;			completed,&#10;			results,&#10;			pendingSteps: steps.slice(completed.length),&#10;		});&#10;	}&#10;});&#10;</code></pre>
<h3 id="this-stash-vs-ctx-stash">this.stash vs ctx.stash</h3>
<p>Both do the same thing. <code>ctx.stash()</code> uses a direct closure over the fiber ID. <code>this.stash()</code> uses <code>AsyncLocalStorage</code> to find the currently executing fiber — it works correctly even with concurrent fibers, since each fiber's ALS context is independent.</p>
<p><code>this.stash()</code> is convenient when calling from nested functions that do not have access to <code>ctx</code>. It throws if called outside a <code>runFiber</code> callback.</p>
<h2 id="recovery">Recovery</h2>
<p>Override <code>onFiberRecovered</code> to handle interrupted fibers. The default implementation logs a warning and deletes the row.</p>
<pre tabindex="0"><code class="language-ts">class ResearchAgent extends Agent {&#10;	async onFiberRecovered(ctx: FiberRecoveryContext) {&#10;		if (ctx.name !== &quot;research&quot;) return;&#10;&#10;		const snapshot = ctx.snapshot as {&#10;			completed: string[];&#10;			results: Record&lt;string, unknown&gt;;&#10;			pendingSteps: string[];&#10;		} | null;&#10;&#10;		if (snapshot &amp;&amp; snapshot.pendingSteps.length &gt; 0) {&#10;			void this.runFiber(&quot;research&quot;, async (fiberCtx) =&gt; {&#10;				const { completed, results, pendingSteps } = snapshot;&#10;&#10;				for (const step of pendingSteps) {&#10;					results[step] = await this.executeStep(step);&#10;					completed.push(step);&#10;&#10;					fiberCtx.stash({&#10;						completed,&#10;						results,&#10;						pendingSteps: pendingSteps.slice(pendingSteps.indexOf(step) + 1),&#10;					});&#10;				}&#10;			});&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Key points:</p>
<ul>
<li><strong>The original lambda is gone.</strong> On recovery, you only have the <code>name</code> and <code>snapshot</code>. The lambda cannot be serialized — recovery logic must be in the hook.</li>
<li><strong>Unmanaged <code>runFiber()</code> rows are deleted after the hook returns successfully.</strong> If you want to continue unmanaged work, call <code>runFiber()</code> again inside the hook — this creates a new row.</li>
<li><strong>Managed <code>startFiber()</code> rows are retained.</strong> Return a <code>FiberRecoveryResult</code> to mark an interrupted managed fiber as <code>completed</code>, <code>error</code>, <code>aborted</code>, or still <code>interrupted</code>.</li>
<li><strong>You control what recovery means.</strong> Retry from the beginning, resume from a checkpoint, skip and notify the user, or do nothing. The framework does not impose a strategy.</li>
<li><strong>If the hook throws, the row is kept (up to a bound).</strong> A later startup or alarm scan retries recovery, which protects against transient storage or scheduling failures. Catch application-level errors yourself when you want to mark the work terminal instead of retrying. A hook that always throws is retried on a backing-off schedule (the recovery alarm uses an exponential delay capped at 5 minutes, so it is not a busy-loop) until the row exceeds <code>fiberRecoveryMaxAgeMs</code> (default 24 h), after which it is discarded with a <code>fiber:recovery:skipped</code> (<code>reason: &quot;max_age_exceeded&quot;</code>) event. Setting <code>fiberRecoveryMaxAgeMs: 0</code> retains such rows indefinitely — recovery keeps retrying on the capped backoff, and the Durable Object never idle-evicts while an un-recoverable row exists, so prefer a finite age unless you intend to inspect or clear those rows yourself. For managed work, the retained row stays <code>interrupted</code> and records the recovery error for inspection.</li>
</ul>
<h3 id="chat-recovery">Chat recovery</h3>
<p><code>AIChatAgent</code> and <code>Think</code> build on fibers for LLM streaming recovery. Every chat turn is wrapped in a fiber automatically. The framework handles the internal recovery path and exposes <code>onChatRecovery</code> for provider-specific strategies. Refer to <a href="/agents/concepts/agentic-patterns/long-running-agents/#recovering-interrupted-llm-streams">Long-running agents: Recovering interrupted LLM streams</a> for details.</p>
<h2 id="concurrent-fibers">Concurrent fibers</h2>
<p>Multiple fibers can run at the same time. Each has its own row in SQLite with its own snapshot, and each calls <code>keepAlive()</code> independently (ref-counted, so the DO stays alive until all fibers complete).</p>
<pre tabindex="0"><code class="language-ts">void this.runFiber(&quot;fetch-data&quot;, async (ctx) =&gt; {&#10;	/* ... */&#10;});&#10;void this.runFiber(&quot;process-queue&quot;, async (ctx) =&gt; {&#10;	/* ... */&#10;});&#10;</code></pre>
<p>On recovery, all orphaned rows are iterated and <code>onFiberRecovered</code> is called for each. Use <code>ctx.name</code> to distinguish between fiber types in your recovery hook.</p>
<h2 id="testing-locally">Testing locally</h2>
<p>In <code>wrangler dev</code>, fiber recovery works identically to production. SQLite and alarm state persist to disk between restarts.</p>
<ol>
<li>Start your agent and trigger a fiber (<code>runFiber</code>)</li>
<li>Kill the wrangler process (Ctrl-C or SIGKILL)</li>
<li>Restart wrangler</li>
<li>Recovery fires automatically — via <code>onStart()</code> if a request arrives, or via the persisted alarm if no clients connect</li>
</ol>
<h2 id="api-reference">API reference</h2>
<h3 id="runfiber-name-fn">runFiber(name, fn)</h3>
<p>Execute a durable fiber. The fiber is registered in SQLite before <code>fn</code> runs and deleted after it completes (or throws). <code>keepAlive()</code> is held for the duration.</p>
<ul>
<li><strong><code>name</code></strong> — identifier for the fiber, used in <code>onFiberRecovered</code> to distinguish fiber types. Not unique — multiple fibers can share a name.</li>
<li><strong><code>fn</code></strong> — async function receiving a <code>FiberContext</code>. Closures work naturally (<code>this</code> and local variables are captured).</li>
<li><strong>Returns</strong> — the value returned by <code>fn</code>. If the DO is evicted before completion, the return value is lost; recovery happens through the hook.</li>
</ul>
<h3 id="startfiber-name-fn-options">startFiber(name, fn, options)</h3>
<p>Durably accept a retained background fiber. The returned <code>StartFiberResult</code> includes a generated <code>fiberId</code>, current <code>status</code>, optional <code>metadata</code>, and <code>accepted</code>, which is <code>false</code> when an existing fiber matched the same idempotency key.</p>
<ul>
<li><strong><code>name</code></strong> — identifier for the managed fiber, used in inspection and recovery.</li>
<li><strong><code>fn</code></strong> — async function receiving a <code>FiberContext</code>. The function result is not stored.</li>
<li><strong><code>options.idempotencyKey</code></strong> — stable external key used to dedupe retries.</li>
<li><strong><code>options.metadata</code></strong> — JSON-serializable data stored with the retained row.</li>
<li><strong><code>options.waitForCompletion</code></strong> — wait for terminal status before returning.</li>
</ul>
<h3 id="inspectfiber-fiberid-inspectfiberbykey-idempotencykey">inspectFiber(fiberId) / inspectFiberByKey(idempotencyKey)</h3>
<p>Return the retained status row for a managed fiber, or <code>null</code> if no row exists.</p>
<h3 id="listfibers-options">listFibers(options)</h3>
<p>List retained managed fibers. Filter by <code>status</code> or <code>name</code>, and use <code>limit</code> to cap the result set.</p>
<h3 id="cancelfiber-fiberid-reason-cancelfiberbykey-idempotencykey-reason">cancelFiber(fiberId, reason) / cancelFiberByKey(idempotencyKey, reason)</h3>
<p>Mark a managed fiber as <code>aborted</code> and abort its in-memory <code>ctx.signal</code> when it is running in the current isolate. Returns <code>false</code> if the fiber does not exist or is already terminal.</p>
<h3 id="resolvefiber-fiberid-result">resolveFiber(fiberId, result)</h3>
<p>Resolve an <code>interrupted</code> managed fiber after application-level recovery succeeds. Returns <code>false</code> for pending, running, or already-terminal rows.</p>
<h3 id="deletefibers-options">deleteFibers(options)</h3>
<p>Delete retained managed fiber rows. By default, settled <code>completed</code>, <code>error</code>, and <code>aborted</code> rows are eligible. Pass <code>status</code>, <code>settledBefore</code>, or <code>limit</code> to narrow cleanup.</p>
<h3 id="stash-data-ctx-stash-data">stash(data) / ctx.stash(data)</h3>
<p>Checkpoint the current fiber's state. Writes synchronously to SQLite. Each call fully replaces the previous snapshot. <code>data</code> must be JSON-serializable.</p>
<h3 id="onfiberrecovered-ctx">onFiberRecovered(ctx)</h3>
<p>Called once per orphaned fiber row on agent restart. Override to implement recovery. Unmanaged <code>runFiber()</code> rows are deleted after this hook returns successfully; if recovery throws, the row is left for a later scan so transient failures do not lose the recovery handle. Managed <code>startFiber()</code> rows stay retained and can be resolved by returning a <code>FiberRecoveryResult</code>.</p>
<ul>
<li><strong><code>ctx.id</code></strong> — unique fiber ID</li>
<li><strong><code>ctx.name</code></strong> — the name passed to <code>runFiber()</code></li>
<li><strong><code>ctx.status</code></strong> — retained status for managed fibers</li>
<li><strong><code>ctx.idempotencyKey</code></strong> — idempotency key for managed fibers, if supplied</li>
<li><strong><code>ctx.metadata</code></strong> — metadata for managed fibers, if supplied</li>
<li><strong><code>ctx.snapshot</code></strong> — the last <code>stash()</code> data, or <code>null</code> if <code>stash()</code> was never called</li>
<li><strong><code>ctx.createdAt</code></strong> — epoch milliseconds when <code>runFiber()</code> started. Compare against <code>Date.now()</code> to skip recoveries that are too old to replay safely.</li>
<li><strong><code>ctx.recoveryReason</code></strong> — why recovery is running. Currently always <code>&quot;interrupted&quot;</code> for eviction or restart recovery.</li>
</ul>
<h3 id="keepalive-1">keepAlive()</h3>
<p>Create a 30-second alarm heartbeat. Returns a disposer function. Idempotent — calling the disposer multiple times is safe.</p>
<h3 id="keepalivewhile-fn">keepAliveWhile(fn)</h3>
<p>Run an async function while keeping the DO alive. Heartbeat starts before <code>fn</code> and stops when it completes or throws. Returns the value returned by <code>fn</code>.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/agents/concepts/agentic-patterns/long-running-agents/">Long-running agents</a> — how fibers compose with schedules, plans, and async operations</li>
<li><a href="/agents/runtime/execution/schedule-tasks/">Schedule tasks</a> — <code>keepAlive</code> details and the alarm system</li>
<li><a href="/agents/runtime/execution/sub-agents/">Sub-agents</a> — durable execution and schedules inside sub-agents</li>
<li><a href="/agents/runtime/execution/run-workflows/">Workflows</a> — durable multi-step execution outside the agent</li>
<li><a href="/agents/communication-channels/chat/chat-agents/">Chat agents</a> — <code>chatRecovery</code> and <code>onChatRecovery</code></li>
</ul>
