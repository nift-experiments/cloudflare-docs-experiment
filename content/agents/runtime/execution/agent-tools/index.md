---
cp9:
  canonical: https://developers.cloudflare.com/agents/runtime/execution/agent-tools/
  description: Run Think and AIChatAgent sub-agents as retained, streaming tools from a parent agent.
  full_title: Agents as tools · Cloudflare Agents docs
  head_html: <title>Agents as tools · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Run Think and AIChatAgent sub-agents as retained, streaming tools from a parent agent."><link rel="canonical" href="https://developers.cloudflare.com/agents/runtime/execution/agent-tools/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/runtime/execution/agent-tools/index.md"><meta property="og:title" content="Agents as tools · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Run Think and AIChatAgent sub-agents as retained, streaming tools from a parent agent."><meta property="og:url" content="https://developers.cloudflare.com/agents/runtime/execution/agent-tools/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/runtime/execution/agent-tools/#page","headline":"Agents as tools \u00b7 Cloudflare Agents docs","description":"Run Think and AIChatAgent sub-agents as retained, streaming tools from a parent agent.","url":"https://developers.cloudflare.com/agents/runtime/execution/agent-tools/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/runtime/execution/agent-tools/
  schema: 1
---
<p>Agents as tools let one chat agent dispatch another chat-capable sub-agent as part of its work. The child is a real sub-agent with its own Durable Object storage, messages, tools, resumable stream, and drill-in URL. The parent keeps a small run registry so clients can render the child timeline, replay it after refresh, and clean it up later.</p>
<p>Agents as tools support <code>@cloudflare/think</code> agents and <code>AIChatAgent</code> subclasses. <code>AIChatAgent</code> children run headlessly through <code>saveMessages()</code>, so they should use server-side tools. Browser-provided client tools are not available during an agent-tool turn unless you model that interaction as server-side state or a separate parent-mediated workflow.</p>
<h2 id="agents-as-tools-vs-sub-agent-rpc">Agents as tools vs sub-agent RPC</h2>
<p>Use <code>subAgent(...).chat()</code> when parent code needs direct streaming RPC to a specific child and your code owns forwarding, cancellation, and replay policy.</p>
<p>Use <code>agentTool()</code> or <code>runAgentTool()</code> when a parent model or workflow delegates work to a child agent and you want retained child runs, event replay, abort bridging, and UI drill-in. For Think-specific turn choices, refer to <a href="/agents/harnesses/think/#choose-a-turn-api">Choose a turn API</a>.</p>
<h2 id="use-an-agent-as-an-ai-sdk-tool">Use an agent as an AI SDK tool</h2>
<p>Use <code>agentTool()</code> when the parent model should decide when to call the helper.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2545.md")
</div>
<p>The child can also be an <code>AIChatAgent</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2546.md")
</div>
<p>The generated tool calls <code>this.runAgentTool(ChildAgent, ...)</code>, streams <code>agent-tool-event</code> frames on the parent WebSocket, and returns the child summary to the parent model. If the run fails, aborts, or is interrupted, the tool returns a structured <code>AgentToolFailure</code> instead of an empty success value:</p>
<pre tabindex="0"><code class="language-ts">type AgentToolFailure = {&#10;	ok: false;&#10;	status: &quot;error&quot; | &quot;aborted&quot; | &quot;interrupted&quot;;&#10;	error: string; // human-readable, safe to surface&#10;	retryable: boolean;&#10;	// Present only when `status` is &quot;interrupted&quot;:&#10;	reason?: AgentToolInterruptedReason;&#10;	childStillRunning?: boolean;&#10;};&#10;&#10;type AgentToolInterruptedReason =&#10;	| &quot;no-progress&quot;&#10;	| &quot;window-exceeded&quot;&#10;	| &quot;not-tailable&quot;&#10;	| &quot;inspect-timeout&quot;&#10;	| &quot;inspect-failed&quot;&#10;	| &quot;recovery-deadline&quot;&#10;	| &quot;budget-exceeded&quot;;&#10;</code></pre>
<p><code>retryable</code> is <code>true</code> only for an <code>interrupted</code> run — the child was reset or superseded by a deploy or parent recovery and never reached a logical outcome, so re-dispatching the same call can succeed. A genuine <code>error</code> or an intentional <code>aborted</code> is <code>retryable: false</code>. This lets a parent prompt convention or an orchestration harness re-run a transient interruption rather than reporting it to the user as a final failure. <code>AgentToolFailure</code> is exported from <code>agents</code>.</p>
<p>On an <code>interrupted</code> run, <code>reason</code> gives a machine-readable cause and <code>childStillRunning</code> reports whether the child was still working when the parent stopped waiting (<code>true</code>) or has since been torn down (<code>false</code>). Branch on these instead of parsing the <code>error</code> prose — for example, re-dispatch a <code>no-progress</code> interrupt (the child may still self-heal) but reconnect to or surface a <code>window-exceeded</code> one (the child was torn down). Both <code>reason</code> and <code>childStillRunning</code> are also mirrored onto the <code>agent-tool-event</code> wire frame and the <code>useAgentToolEvents()</code> run state.</p>
<p>For Think children that do workflow-style work without user-facing assistant text, override <code>getAgentToolOutput()</code> and, if needed, <code>getAgentToolSummary()</code>. Assistant text remains the default summary when present, but a Think agent-tool run can complete successfully without emitting text chunks.</p>
<p>Persist any structured output before the child turn finishes, because <code>getAgentToolOutput()</code> is read as soon as <code>saveMessages()</code> resolves. Keep <code>getAgentToolSummary()</code> concise for display; the full structured value is stored separately as the tool output.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2547.md")
</div>
<h2 id="run-an-agent-tool-imperatively">Run an agent tool imperatively</h2>
<p>Use <code>runAgentTool()</code> for deterministic workflows, scheduled work, HTTP handlers, or fan-out code.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2548.md")
</div>
<p><code>runAgentTool()</code> is idempotent by <code>runId</code>. Passing the same <code>runId</code> never starts a duplicate child turn. Completed, failed, aborted, and interrupted runs are retained until you explicitly clear them.</p>
<h2 id="detached-background-runs">Detached (background) runs</h2>
<p>By default <code>runAgentTool()</code> <strong>awaits</strong> the child to terminal before returning. For long-running work — large imports, video renders, deep research — that you do not want to block the dispatching turn on, pass <code>detached</code>. The run is dispatched, the current turn continues, and <code>runAgentTool()</code> returns a handle immediately:</p>
<pre tabindex="0"><code class="language-ts">type DetachedRunAgentToolResult = {&#10;	runId: string;&#10;	agentType: string;&#10;	status: &quot;running&quot; | &quot;error&quot;; // &quot;error&quot; only if dispatch itself was rejected&#10;};&#10;</code></pre>
<p><code>detached: true</code> is fire-and-forget — observe the run through <code>agent-tool-event</code> frames (the same ones <code>useAgentToolEvents()</code> consumes) and the global <code>onAgentToolFinish()</code> hook. Pass an object to wire a targeted, durable completion callback:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2549.md")
</div>
<p>Key behaviors:</p>
<ul>
<li><strong>Durable completion.</strong> Delivery survives eviction and deploys: a warm fast path delivers with low latency while the isolate is alive, and a self-scheduling reconcile backbone finalizes anything the fast path missed. Delivery is exactly-once on the happy path; under a crash it is at-least-once, so <code>onFinish</code> handlers must be idempotent.</li>
<li><strong>Give-up vs. finish are independent.</strong> A budget give-up is delivered as <code>status: &quot;interrupted&quot;</code>, <code>reason: &quot;budget-exceeded&quot;</code>. Because <code>interrupted</code> is soft, a child that completes after the give-up still re-fires <code>onFinish</code> with the real result — a premature give-up never hides a late completion.</li>
<li><strong>Bounded.</strong> Every detached run has an absolute <code>maxBudgetMs</code> ceiling (per-run, or the <code>detachedMaxBudgetMs</code> static option; default 24h). On expiry the parent gives up watching and tears the child down so an abandoned run cannot hold a <code>maxConcurrentAgentTools</code> slot forever.</li>
<li><strong>No inherited signal.</strong> A detached run must outlive the spawning turn, so it does <strong>not</strong> inherit <code>options.signal</code>. Cancel it explicitly:</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2550.md")
</div>
<h3 id="notify-the-chat-on-completion-think-aichatagent">Notify the chat on completion (Think / AIChatAgent)</h3>
<p>On a chat agent (<code>@cloudflare/think</code> or <code>AIChatAgent</code>) you usually want the model to <em>react</em> to a finished background run. Instead of wiring <code>onFinish</code> by hand, pass <code>notify: true</code> — when the run finishes the agent injects a message into the chat (idempotent per run + status, so an exactly-once finish never duplicates) and the model takes its next turn with the result in context:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2551.md")
</div>
<p>If your app routes or hides synthetic messages by <code>metadata.source</code>, pass your own source:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2552.md")
</div>
<p>Override <code>formatDetachedCompletion(run, result)</code> to customize the injected text, or return an empty string to suppress the notification for a given outcome. An explicit <code>onFinish</code> takes precedence over <code>notify</code>.</p>
<h3 id="the-inspectagenttoolrun-contract">The <code>inspectAgentToolRun</code> contract</h3>
<p>A child's <code>inspectAgentToolRun(runId)</code> returns the run's current status snapshot, or <code>null</code>. <strong><code>null</code> does not mean &quot;failed&quot;</strong> — it means the child has no record of that run <em>yet</em>. This is normal immediately after dispatch (the child may still be persisting its first row) and is also what a freshly-rehydrated child returns before it has lazily reconciled a stale <code>running</code> row. Callers — and the framework's own reconcile backbone — treat <code>null</code> as &quot;not terminal, keep watching within budget&quot;, never as a terminal failure. Only a non-<code>null</code> inspection with a terminal <code>status</code> (<code>completed</code> / <code>error</code> / <code>aborted</code>) finalizes a run.</p>
<h2 id="report-progress-and-milestones">Report progress and milestones</h2>
<p>A sub-agent running as an agent tool — awaited or detached — can report mid-run progress so a parent can render a live status line, meter the run server-side, or react to a named checkpoint before the run finishes. Call <code>reportProgress()</code> from inside the child (for example, from a tool's <code>execute</code>):</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2553.md")
</div>
<p><code>reportProgress()</code> is available on chat agents (<code>@cloudflare/think</code> and <code>AIChatAgent</code>). It is a no-op with a development warning on the base <code>Agent</code> class and when called outside an active agent-tool run, so the same child code is safe to run standalone. The framework resolves the active run from the current turn — you never thread a run ID.</p>
<pre tabindex="0"><code class="language-ts">reportProgress&lt;T&gt;(&#10;	progress: {&#10;		fraction?: number; // 0..1 — drives a progress bar&#10;		message?: string; // human-readable status line&#10;		phase?: string; // coarse phase label, e.g. &quot;ingesting&quot;&#10;		milestone?: string; // present ⇒ a durable milestone (see below)&#10;		data?: T; // app-specific payload; live-only unless persisted&#10;	},&#10;	options?: { persist?: boolean },&#10;): Promise&lt;void&gt;;&#10;</code></pre>
<p>Ephemeral signals ride the child's own turn stream as a transient <code>data-agent-progress</code> part, so they re-broadcast to the parent's connected clients and surface on <code>AgentToolRunState.progress</code> through <code>useAgentToolEvents()</code> — a background-runs tray can render a live bar, phase, and status line without drilling in. Bursts are coalesced (latest-wins; a <code>fraction &gt;= 1</code> frame always flushes). The <code>data</code> field is live-only unless you pass <code>{ persist: true }</code>.</p>
<h3 id="observe-progress-on-the-parent">Observe progress on the parent</h3>
<p>Override <code>onProgress()</code> to meter, steer, or surface progress server-side. It fires best-effort whenever a child progress signal is forwarded through the parent, for both awaited and detached runs:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2554.md")
</div>
<p><code>onProgress()</code> is not durable: after eviction a detached run's latest snapshot is reconstructed from <code>inspectAgentToolRun().progress</code> on reconcile rather than re-firing the hook. The latest snapshot is also persisted on the child run row, so a rehydrated parent can answer &quot;where is this run&quot; without having tailed the live stream.</p>
<h3 id="durable-milestones">Durable milestones</h3>
<p>Naming a <code>milestone</code> promotes a signal from the ephemeral tier to a <strong>durable</strong> one — there is still only one emit method:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2555.md")
</div>
<p>A milestone is persisted as one row on the child with a monotonic per-run <code>sequence</code>, and rides the stream as a <strong>persisted</strong> <code>data-agent-milestone</code> part (unlike transient progress). It therefore survives eviction, replays on drill-in, and is surfaced — deduped by <code>sequence</code> — on <code>AgentToolRunState.milestones</code> and <code>inspectAgentToolRun().milestones</code>. <code>onProgress()</code> fires for milestones too, with <code>progress.milestone</code> set, so a consumer can branch on milestone versus ephemeral progress.</p>
<h3 id="notify-the-chat-on-a-milestone-think-aichatagent">Notify the chat on a milestone (Think / AIChatAgent)</h3>
<p>For a detached run on a chat agent, <code>detached: { onMilestones }</code> surfaces a chat message when a configured milestone lands, <em>before</em> the run finishes. Each <code>(runId, name)</code> fires at most once — whether observed live or reconciled after eviction — so the deterministic ID collapses warm and cold delivery to at-most-once:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2556.md")
</div>
<p>Override <code>formatDetachedMilestone(run, milestone)</code> to customize the wording, or return an empty string to suppress a given milestone. Synthetic narrate messages carry <code>metadata.source</code>, so clients can render them as an agent event rather than a human turn.</p>
<h3 id="resetting-no-progress-budget-for-detached-runs">Resetting no-progress budget for detached runs</h3>
<p>Once a detached child has reported at least one signal, the reconcile backbone gives up if the run then goes silent for <code>detachedNoProgressBudgetMs</code> (default 1 hour; per-run override via <code>detached: { noProgressBudgetMs }</code>). This surfaces as <code>status: &quot;interrupted&quot;</code>, <code>reason: &quot;no-progress&quot;</code>. A child that never reports is bounded only by the absolute <code>detachedMaxBudgetMs</code> ceiling — a run is never given up on merely for being slow. Set <code>noProgressBudgetMs</code> to <code>0</code> or <code>Infinity</code> to disable the resetting window for a run.</p>
<h2 id="render-child-timelines-in-react">Render child timelines in React</h2>
<p><code>useAgentToolEvents()</code> is a headless hook. It subscribes to the existing parent connection, deduplicates replay/live races, applies child <code>UIMessageChunk</code> bodies to message parts, and groups sibling runs by parent tool call ID. Each run state carries <code>progress</code> and <code>milestones</code>, so a background-runs tray can render a live bar, phase, and milestone chips without drilling in.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2557.md")
</div>
<p>Imperative runs without a parent tool call are available as <code>agentTools.unboundRuns</code>.</p>
<h2 id="drill-in-and-gate-access">Drill in and gate access</h2>
<p>Agents as tools are normal sub-agents. Connect to a retained child through the parent route:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2558.md")
</div>
<p>Gate external access with the parent registry so guessed run IDs cannot spawn fresh child facets:</p>
<pre tabindex="0"><code class="language-ts">override async onBeforeSubAgent(_request, child) {&#10;	if (!this.hasAgentToolRun(child.className, child.name)) {&#10;		return new Response(&quot;Not found&quot;, { status: 404 });&#10;	}&#10;}&#10;</code></pre>
<h2 id="clear-retained-runs">Clear retained runs</h2>
<p>Runs and child facets are retained by default for refresh, drill-in, and later inspection. Delete them explicitly when clearing chat history or applying your own retention policy:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2559.md")
</div>
<p>If a retained run is still <code>starting</code> or <code>running</code>, cleanup cancels the child before deleting its facet.</p>
<h2 id="interrupted-runs-and-recovery">Interrupted runs and recovery</h2>
<p>Agent-tool runs are retained in the parent. If the parent restarts (deploy or eviction) while a child run is still <code>starting</code> or <code>running</code>, it does not abandon the child. Startup recovery re-attaches to the live child and tails its stream to the child's terminal result. Because the child is a sub-agent with its own <code>chatRecovery</code>, it self-heals its own interrupted turn while the parent forwards its output. A completed child is finalized without re-running finished work.</p>
<p>The re-attach wait is <strong>progress-keyed</strong>, not a fixed wall clock. Two static <code>options</code> tune it:</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Default</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>agentToolReattachNoProgressTimeoutMs</code></td>
<td><code>120000</code> (2 min)</td>
<td>How long the parent waits with <strong>no</strong> forward progress before giving up. Resets on every forwarded chunk, so a streaming child is followed through to terminal.</td>
</tr>
<tr>
<td><code>agentToolReattachMaxWindowMs</code></td>
<td><code>Infinity</code></td>
<td>Optional hard wall-clock ceiling on a single re-attach. Uncapped by default (mirrors chat recovery's <code>maxRecoveryWork</code>), so a healthy, long-running child is never cut off. Set a finite value to impose a cap.</td>
</tr>
</tbody>
</table>
<p>Give-up outcomes map to the <code>AgentToolFailure</code> fields:</p>
<ul>
<li>A child that goes silent for a full no-progress window is sealed <code>reason: &quot;no-progress&quot;</code>, <code>childStillRunning: true</code>. This seal is soft: the child is left running, so re-dispatching the same <code>runId</code> can re-attach and collect it if it self-heals.</li>
<li>If you set a finite <code>agentToolReattachMaxWindowMs</code> and it fires, the run is sealed <code>reason: &quot;window-exceeded&quot;</code>, <code>childStillRunning: false</code>, and the child is torn down (it has had its full window and is treated as exhausted).</li>
<li>A child that cannot be tailed or inspected, or that exceeds the overall recovery deadline, is sealed with the matching <code>reason</code> so the parent tool call returns a structured failure instead of hanging indefinitely.</li>
</ul>
<p>A hung child can never block recovery forever. The no-progress budget bounds a silent child. A content runaway is bounded by the child's own <code>chatRecovery</code> (<code>maxRecoveryWork</code> and <code>shouldKeepRecovering</code>), not by a parent-only timer.</p>
<p>Monitor parent reconciliation through the <code>agentTool</code> observability channel:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2560.md")
</div>
<p>Raw <code>diagnostics_channel</code> subscribers should use the channel name <code>agents:agent_tool</code>.</p>
<h2 id="example">Example</h2>
<div class="nb-card nb-link-card"><h3 id="card-agents-as-tools-example-https-github-com-cloudflare-agents-tree-main-examples-agents-as-tools"><a href="https://github.com/cloudflare/agents/tree/main/examples/agents-as-tools">Agents as tools example</a></h3><p>Run chat-capable sub-agents as retained tools, stream their timelines inline, and drill into child agents.</p></div>
<h2 id="related">Related</h2>
<div class="nb-card nb-link-card"><h3 id="card-sub-agents-agents-runtime-execution-sub-agents"><a href="/agents/runtime/execution/sub-agents/">Sub-agents</a></h3><p>Spawn child agents with isolated storage, typed RPC, and nested client routing.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-chat-agents-agents-communication-channels-chat-chat-agents"><a href="/agents/communication-channels/chat/chat-agents/">Chat agents</a></h3><p>Build AI chat interfaces with AIChatAgent and useAgentChat.</p></div>
