---
cp9:
  canonical: https://developers.cloudflare.com/agents/harnesses/think/recovery/
  description: Bounded chat recovery, the stream-stall watchdog, repairing interrupted tool calls, and stability detection for Think agents.
  full_title: Durable recovery · Cloudflare Agents docs
  head_html: <title>Durable recovery · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Bounded chat recovery, the stream-stall watchdog, repairing interrupted tool calls, and stability detection for Think agents."><link rel="canonical" href="https://developers.cloudflare.com/agents/harnesses/think/recovery/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/harnesses/think/recovery/index.md"><meta property="og:title" content="Durable recovery · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Bounded chat recovery, the stream-stall watchdog, repairing interrupted tool calls, and stability detection for Think agents."><meta property="og:url" content="https://developers.cloudflare.com/agents/harnesses/think/recovery/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/harnesses/think/recovery/#page","headline":"Durable recovery \u00b7 Cloudflare Agents docs","description":"Bounded chat recovery, the stream-stall watchdog, repairing interrupted tool calls, and stability detection for Think agents.","url":"https://developers.cloudflare.com/agents/harnesses/think/recovery/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/harnesses/think/recovery/
  schema: 1
---
<p>Think always wraps chat turns in recoverable <a href="/agents/runtime/execution/durable-execution/">fibers</a>. If the Durable Object is evicted mid-stream, Think reconstructs any buffered chunks. It persists partial output and schedules a continuation or retry.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2132.md")
</aside>
<p>WebSocket turns, sub-agent <code>chat()</code> turns, durable <code>submitMessages()</code> executions, automatic continuations, <code>saveMessages()</code>, and <code>continueLastTurn()</code> are wrapped in <code>runFiber</code>.</p>
<h2 id="bounded-recovery">Bounded recovery</h2>
<p>A stream-stall watchdog abort (<code>chatStreamStallTimeoutMs</code>) uses the same bounded recovery path. The SDK preserves the settled partial and schedules a continuation. A transient hang recovers automatically. A persistently hanging provider exhausts the budget through the same path as a deployment or eviction. The SDK calls <code>onExhausted</code>, emits <code>chat:recovery:exhausted</code>, and shows the configured <code>terminalMessage</code>.</p>
<p>Configure bounded recovery by setting <code>chatRecovery</code> to an object:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2133.md")
</div>
<p>The same recovery events are available through <code>agents/observability</code> on the <code>chat</code> channel; transcript repairs are emitted on the <code>transcript</code> channel. Refer to <a href="/agents/runtime/operations/observability/diagnostics-channels/#chat-recovery-events">Diagnostics channels</a>.</p>
<h2 id="onchatrecovery">onChatRecovery</h2>
<p>Override <code>onChatRecovery</code> when you need provider-specific recovery, such as retrieving a stored OpenAI Responses result instead of issuing a new model call:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2134.md")
</div>
<h3 id="chatrecoverycontext">ChatRecoveryContext</h3>
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
<td>The stream ID of the interrupted turn</td>
</tr>
<tr>
<td><code>requestId</code></td>
<td><code>string</code></td>
<td>The request ID of the interrupted turn</td>
</tr>
<tr>
<td><code>partialText</code></td>
<td><code>string</code></td>
<td>Text generated before the interruption</td>
</tr>
<tr>
<td><code>partialParts</code></td>
<td><code>MessagePart[]</code></td>
<td>Parts accumulated before the interruption</td>
</tr>
<tr>
<td><code>recoveryData</code></td>
<td><code>unknown | null</code></td>
<td>Data from <code>this.stash()</code> during the turn</td>
</tr>
<tr>
<td><code>messages</code></td>
<td><code>UIMessage[]</code></td>
<td>Current conversation history</td>
</tr>
<tr>
<td><code>lastBody</code></td>
<td><code>Record&lt;string, unknown&gt;?</code></td>
<td>Body from the interrupted turn</td>
</tr>
<tr>
<td><code>lastClientTools</code></td>
<td><code>ClientToolSchema[]?</code></td>
<td>Client tools from the interrupted turn</td>
</tr>
<tr>
<td><code>createdAt</code></td>
<td><code>number</code></td>
<td>Epoch milliseconds when the turn started</td>
</tr>
</tbody>
</table>
<h3 id="chatrecoveryoptions">ChatRecoveryOptions</h3>
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
<td><code>persist</code></td>
<td><code>boolean?</code></td>
<td>Whether to persist the partial assistant message</td>
</tr>
<tr>
<td><code>continue</code></td>
<td><code>boolean?</code></td>
<td>Whether to auto-continue with a new turn via <code>continueLastTurn()</code></td>
</tr>
</tbody>
</table>
<p>With <code>persist: true</code>, the partial message is saved. With <code>continue: true</code>, Think calls <code>continueLastTurn()</code> after the agent reaches a stable state.</p>
<p>For pre-stream interruptions, where <code>ctx.streamId === &quot;&quot;</code> and <code>ctx.partialText === &quot;&quot;</code> but the latest persisted message is still the unanswered user message, Think retries that turn automatically unless <code>continue</code> is <code>false</code>.</p>
<pre tabindex="0"><code class="language-ts">onChatRecovery(ctx: ChatRecoveryContext): ChatRecoveryOptions {&#10;	if (!ctx.streamId &amp;&amp; !ctx.partialText) {&#10;		console.log(&quot;Recovering a pre-stream interruption&quot;);&#10;	}&#10;	return {};&#10;}&#10;</code></pre>
<p>Use <code>ctx.createdAt</code> to skip stale recoveries. For example, if the interrupted turn is older than a few minutes, return <code>{ continue: false }</code> so the partial response is preserved without starting an old continuation.</p>
<p>Durable bookkeeping remains active when automatic continuation is not appropriate. Return <code>{ continue: false }</code> to prevent another model call. For cancellation, side-effect, and cost controls, refer to <a href="/agents/communication-channels/chat/chat-agents/#control-automatic-continuation">Control automatic continuation</a>.</p>
<h3 id="recovery-budgets-and-limits">Recovery budgets and limits</h3>
<p>Assign a <code>chatRecovery</code> object to tune recovery limits and terminal behavior. A progressing turn survives repeated interruptions while it stays within the <code>maxRecoveryWork</code> limit. The following options control when recovery stops:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2135.md")
</div>
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
<td>Attempt cap. Resets on forward progress, so it catches a tight no-progress alarm loop, not a healthy long turn.</td>
</tr>
<tr>
<td><code>stableTimeoutMs</code></td>
<td><code>10_000</code></td>
<td>How long an attempt waits for the isolate to reach stable state before rescheduling.</td>
</tr>
<tr>
<td><code>noProgressTimeoutMs</code></td>
<td><code>300_000</code> (5 min)</td>
<td>Primary stuck-turn bound: max time without forward progress before sealing. <strong>Resets on every progress-bearing attempt.</strong></td>
</tr>
<tr>
<td><code>maxRecoveryWork</code></td>
<td><code>1,000</code></td>
<td>Runaway-loop guard: maximum produced content/tool units before a still-progressing turn is sealed. Set a higher value or <code>Infinity</code> for a long agentic turn.</td>
</tr>
<tr>
<td><code>maxOomRetries</code></td>
<td><code>3</code></td>
<td>Retry budget for Durable Object memory-limit resets. Set <code>0</code> to stop after the first memory-limit reset.</td>
</tr>
<tr>
<td><code>shouldKeepRecovering</code></td>
<td>—</td>
<td>Caller policy consulted from the second attempt onward. Return <code>false</code> to stop recovery. The hook point for a token/cost budget (<code>ctx.work</code> is a coarse segment count, not tokens).</td>
</tr>
<tr>
<td><code>terminalMessage</code></td>
<td>generic message</td>
<td>Message shown to the user when recovery is given up on.</td>
</tr>
<tr>
<td><code>onExhausted</code></td>
<td>—</td>
<td>Called once when recovery is given up on. Inspect <code>ctx.reason</code>.</td>
</tr>
</tbody>
</table>
<p><code>ctx.reason</code> on the exhausted hook is one of: <code>no_progress_timeout</code> (stuck), <code>max_attempts_exceeded</code> (no-progress alarm loop), <code>work_budget_exceeded</code> (runaway), <code>recovery_aborted</code> (your <code>shouldKeepRecovering</code> returned <code>false</code>), <code>out_of_memory</code> (memory-limit retry budget), or <code>stable_timeout</code> (extreme churn). Refer to <a href="/agents/communication-channels/chat/chat-agents/#stream-recovery">Stream recovery</a> for the full shared reference. Think and <code>@cloudflare/ai-chat</code> use the same recovery configuration.</p>
<h2 id="repairing-interrupted-tool-calls">Repairing interrupted tool calls</h2>
<p>When a turn is interrupted mid-flight, the transcript can contain a tool call with no settled result. Before the next provider call, Think repairs each such call so the model does not silently re-run it and the provider does not reject the transcript with <code>AI_MissingToolResultsError</code>. The default flips the interrupted call to an errored tool result, so the record survives and conversion still has a tool result for it.</p>
<p>Override <code>repairInterruptedToolPart</code> to customize the repaired shape. The common case is a client-resolved tool — for example an <code>ask_user</code> question that has no server <code>execute</code> and is normally answered by the user's next message. Converting it to a plain text part lets the model treat it as ordinary conversation rather than a tool error, and keeps the question verbatim through compaction:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2136.md")
</div>
<p>This runs during transcript repair — before the repaired transcript is persisted and sent to the model — so the conversion shapes the current turn, not just the next one. The <code>input</code> is already normalized to a valid object. A returned tool part must carry a settled result (<code>output-available</code>, <code>output-error</code>, or <code>output-denied</code>); returning a non-tool part such as text is also fine.</p>
<h2 id="context-window-overflow-recovery">Context-window overflow recovery</h2>
<p><a href="/agents/runtime/lifecycle/sessions/#compaction">Compaction</a> is checked <strong>between turns</strong> — <code>compactAfter()</code> runs after each <code>appendMessage()</code>. But a single long, tool-heavy turn grows the prompt step by step inside one <code>streamText</code> loop and can exceed the model context window <strong>mid-turn</strong>, before the next pre-turn check. The provider then rejects the request (<code>&quot;prompt is too long&quot;</code>, <code>context_length_exceeded</code>), and the turn would otherwise die terminally.</p>
<p>Think recovers from this with two opt-in, provider-agnostic layers, both configured through the <code>contextOverflow</code> property. Both are off by default, so existing behavior is unchanged. Both reuse your session's compaction function, so they require a <code>configureSession()</code> with <code>onCompaction()</code> configured. Both require <a href="/agents/harnesses/think/lifecycle-hooks/#classifychaterror"><code>classifyChatError</code></a> to tell Think which errors are overflows — Think ships no provider-specific matching in core.</p>
<p><strong>1. Reactive backstop — <code>contextOverflow.reactive</code>.</strong> When a turn fails with an error you classify as <code>&quot;context_overflow&quot;</code>, Think discards the truncated partial, runs <code>session.compact()</code>, and re-runs the turn from the compacted history. The partial is not persisted: the turn restarts from scratch, so keeping the cut-off assistant message would orphan it beside the recovered answer. It is bounded by <code>contextOverflow.maxRetries</code> (default <code>1</code>); if compaction cannot shorten history or the budget is spent, the overflow surfaces terminally through <code>onChatError</code> with <code>classification: &quot;context_overflow&quot;</code> — it never loops or ends silently.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2137.md")
</div>
<p><strong>2. Proactive guard — <code>contextOverflow.proactive</code>.</strong> Heads off the provider error before it happens. Before each step, Think reads the previous step's model-reported <code>usage.inputTokens</code> (provider-agnostic) and, if it crosses <code>maxInputTokens * (headroom ?? 0.9)</code>, compacts in place and feeds the recompacted history into the upcoming step. If a provider omits <code>inputTokens</code>, it falls back to <code>usage.totalTokens</code> (a safe over-approximation — it compacts slightly early rather than missing the threshold). It compacts at most <code>proactive.maxCompactions</code> times per turn (default <code>1</code>) — independent of the reactive <code>maxRetries</code> budget — so a history that cannot shorten does not compact on every step.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2138.md")
</div>
<p>Use either layer alone, or both together: the proactive guard avoids most overflows, and the reactive backstop catches any that still slip through (for example, a turn that starts already over budget, or a single tool result so large that compaction cannot help — in which case it terminalizes cleanly). Both apply to every turn entry path (WebSocket, sub-agent <code>chat()</code>, and programmatic <code>saveMessages()</code> / <code>submitMessages()</code>), and both emit a <code>chat:context:compacted</code> <a href="/agents/runtime/operations/observability/diagnostics-channels/#chat-context-events">diagnostics channel event</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2131.md")
</aside>
<p>For a runnable demo against a real Workers AI model, refer to the <a href="https://github.com/cloudflare/agents/tree/main/examples/context-overflow-recovery"><code>context-overflow-recovery</code> example</a>.</p>
<h2 id="stability-detection">Stability detection</h2>
<p>Think provides methods to check if the agent is in a stable state — no pending tool results, no pending approvals, no active turns.</p>
<h3 id="haspendinginteraction">hasPendingInteraction</h3>
<p>Returns <code>true</code> if any assistant message has pending tool calls (tools without results or pending approvals).</p>
<pre tabindex="0"><code class="language-ts">protected hasPendingInteraction(): boolean&#10;</code></pre>
<h3 id="waituntilstable">waitUntilStable</h3>
<p>Returns a promise that resolves to <code>true</code> when the agent reaches a stable state, or <code>false</code> if the timeout is exceeded.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2139.md")
</div>
