---
cp9:
  canonical: https://developers.cloudflare.com/agents/harnesses/think/lifecycle-hooks/
  description: Hooks at each stage of a Think chat turn — beforeTurn, beforeStep, beforeToolCall, afterToolCall, onStepFinish, onChunk, onChatResponse, and onChatError.
  full_title: Lifecycle hooks · Cloudflare Agents docs
  head_html: <title>Lifecycle hooks · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Hooks at each stage of a Think chat turn — beforeTurn, beforeStep, beforeToolCall, afterToolCall, onStepFinish, onChunk, onChatResponse, and onChatError."><link rel="canonical" href="https://developers.cloudflare.com/agents/harnesses/think/lifecycle-hooks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/harnesses/think/lifecycle-hooks/index.md"><meta property="og:title" content="Lifecycle hooks · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Hooks at each stage of a Think chat turn — beforeTurn, beforeStep, beforeToolCall, afterToolCall, onStepFinish, onChunk, onChatResponse, and onChatError."><meta property="og:url" content="https://developers.cloudflare.com/agents/harnesses/think/lifecycle-hooks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/harnesses/think/lifecycle-hooks/#page","headline":"Lifecycle hooks \u00b7 Cloudflare Agents docs","description":"Hooks at each stage of a Think chat turn \u2014 beforeTurn, beforeStep, beforeToolCall, afterToolCall, onStepFinish, onChunk, onChatResponse, and onChatError.","url":"https://developers.cloudflare.com/agents/harnesses/think/lifecycle-hooks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/harnesses/think/lifecycle-hooks/
  schema: 1
---
<p>Think owns the <code>streamText</code> call and provides hooks at each stage of the chat turn. Hooks fire on every turn regardless of entry path — WebSocket chat, sub-agent <code>chat()</code>, <code>saveMessages()</code>, durable <code>submitMessages()</code> execution, <code>continueLastTurn()</code>, and auto-continuation after tool results.</p>
<h2 id="hook-summary">Hook summary</h2>
<table>
<thead>
<tr>
<th>Hook</th>
<th>When it fires</th>
<th>Return</th>
<th>Async</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>configureSession(session)</code></td>
<td>Once during <code>onStart</code></td>
<td><code>Session</code></td>
<td>yes</td>
</tr>
<tr>
<td><code>beforeTurn(ctx)</code></td>
<td>Before <code>streamText</code></td>
<td><code>TurnConfig</code> or void</td>
<td>yes</td>
</tr>
<tr>
<td><code>beforeStep(ctx)</code></td>
<td>Before each model step</td>
<td><code>StepConfig</code> or void</td>
<td>yes</td>
</tr>
<tr>
<td><code>beforeToolCall(ctx)</code></td>
<td>Before a server-side tool executes</td>
<td><code>ToolCallDecision</code> or void</td>
<td>yes</td>
</tr>
<tr>
<td><code>afterToolCall(ctx)</code></td>
<td>After a tool outcome is known</td>
<td>void</td>
<td>yes</td>
</tr>
<tr>
<td><code>onStepFinish(ctx)</code></td>
<td>After each step completes</td>
<td>void</td>
<td>yes</td>
</tr>
<tr>
<td><code>onChunk(ctx)</code></td>
<td>Per streaming chunk</td>
<td>void</td>
<td>yes</td>
</tr>
<tr>
<td><code>onChatResponse(result)</code></td>
<td>After turn completes and message is persisted</td>
<td>void</td>
<td>yes</td>
</tr>
<tr>
<td><code>onChatError(error, ctx?)</code></td>
<td>On error during a turn</td>
<td>error to propagate</td>
<td>no</td>
</tr>
<tr>
<td><code>classifyChatError(error, ctx?)</code></td>
<td>On a turn error, when <code>contextOverflow.reactive</code> is enabled</td>
<td><code>ChatErrorClassification</code> or void</td>
<td>no</td>
</tr>
</tbody>
</table>
<h2 id="execution-order">Execution order</h2>
<p>For a turn with two tool calls:</p>
<pre tabindex="0"><code class="language-mermaid">flowchart TD&#10;    cfg[&quot;configureSession() — once at startup, not per-turn&quot;] --&gt; bt[&quot;beforeTurn() — inspect context, override model/tools/prompt&quot;]&#10;    bt --&gt; bs&#10;&#10;    subgraph loop [&quot;streamText (repeats per step)&quot;]&#10;        bs[&quot;beforeStep()&quot;] --&gt; chunk[&quot;onChunk() — per streaming chunk&quot;]&#10;        chunk --&gt; btc[&quot;beforeToolCall()&quot;]&#10;        btc --&gt; exec[&quot;tool executes&quot;]&#10;        exec --&gt; atc[&quot;afterToolCall()&quot;]&#10;        atc --&gt; sf[&quot;onStepFinish()&quot;]&#10;        sf --&gt;|&quot;more steps&quot;| bs&#10;    end&#10;&#10;    sf --&gt;|&quot;turn complete&quot;| ocr[&quot;onChatResponse() — message persisted, turn lock released&quot;]&#10;</code></pre>
<h2 id="beforeturn">beforeTurn</h2>
<p>Called before <code>streamText</code>. Receives the fully assembled context — system prompt, converted messages, merged tools, and model. Return a <code>TurnConfig</code> to override any part, or void to accept defaults.</p>
<pre tabindex="0"><code class="language-ts">beforeTurn(ctx: TurnContext): TurnConfig | void | Promise&lt;TurnConfig | void&gt;&#10;</code></pre>
<h3 id="turncontext">TurnContext</h3>
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
<td><code>system</code></td>
<td><code>string</code></td>
<td>Assembled system prompt (from context blocks or <code>getSystemPrompt()</code>)</td>
</tr>
<tr>
<td><code>messages</code></td>
<td><code>ModelMessage[]</code></td>
<td>Assembled model messages (truncated, pruned)</td>
</tr>
<tr>
<td><code>tools</code></td>
<td><code>ToolSet</code></td>
<td>Merged tool set (workspace + getTools + session + extensions + MCP + client)</td>
</tr>
<tr>
<td><code>model</code></td>
<td><code>LanguageModel</code></td>
<td>The model from <code>getModel()</code></td>
</tr>
<tr>
<td><code>continuation</code></td>
<td><code>boolean</code></td>
<td>Whether this is a continuation turn (auto-continue after tool result)</td>
</tr>
<tr>
<td><code>body</code></td>
<td><code>Record&lt;string, unknown&gt;</code></td>
<td>Custom body fields from the client request</td>
</tr>
</tbody>
</table>
<h3 id="turnconfig">TurnConfig</h3>
<p>All fields are optional. Return only what you want to change.</p>
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
<td><code>model</code></td>
<td><code>LanguageModel</code></td>
<td>Override the model for this turn</td>
</tr>
<tr>
<td><code>system</code></td>
<td><code>string</code></td>
<td>Override the system prompt</td>
</tr>
<tr>
<td><code>messages</code></td>
<td><code>ModelMessage[]</code></td>
<td>Override the assembled messages</td>
</tr>
<tr>
<td><code>tools</code></td>
<td><code>ToolSet</code></td>
<td>Extra tools to merge (additive)</td>
</tr>
<tr>
<td><code>activeTools</code></td>
<td><code>string[]</code></td>
<td>Limit which tools the model can call</td>
</tr>
<tr>
<td><code>toolChoice</code></td>
<td><code>ToolChoice</code></td>
<td>Force a specific tool call</td>
</tr>
<tr>
<td><code>maxSteps</code></td>
<td><code>number</code></td>
<td>Override <code>maxSteps</code> for this turn</td>
</tr>
<tr>
<td><code>sendReasoning</code></td>
<td><code>boolean</code></td>
<td>Send reasoning chunks for this turn</td>
</tr>
<tr>
<td><code>chatStreamStallTimeoutMs</code></td>
<td><code>number</code></td>
<td>Override the stream-stall watchdog for this turn (<code>0</code> disables it); auto-resets after the turn. Useful for a turn with a known-slow tool — refer to <a href="/agents/harnesses/think/recovery/">Durable recovery</a></td>
</tr>
<tr>
<td><code>output</code></td>
<td><code>Output</code></td>
<td>Request structured output for this turn</td>
</tr>
<tr>
<td><code>providerOptions</code></td>
<td><code>Record&lt;string, unknown&gt;</code></td>
<td>Provider-specific options</td>
</tr>
<tr>
<td><code>experimental_telemetry</code></td>
<td><code>object</code></td>
<td>AI SDK telemetry settings for this turn</td>
</tr>
<tr>
<td><code>experimental_transform</code></td>
<td><code>StreamTextTransform | StreamTextTransform[]</code></td>
<td>AI SDK stream transform(s) for this turn — inspect or rewrite stream parts (for example, emit <code>source</code> parts derived from tool results). Applied in order.</td>
</tr>
</tbody>
</table>
<h3 id="examples">Examples</h3>
<p>Switch to a cheaper model for continuation turns:</p>
<pre tabindex="0"><code class="language-ts">beforeTurn(ctx: TurnContext) {&#10;	if (ctx.continuation) {&#10;		return { model: this.cheapModel };&#10;	}&#10;}&#10;</code></pre>
<p>Restrict which tools the model can call:</p>
<pre tabindex="0"><code class="language-ts">beforeTurn(ctx: TurnContext) {&#10;	return { activeTools: [&quot;read&quot;, &quot;write&quot;, &quot;getWeather&quot;] };&#10;}&#10;</code></pre>
<p>Add per-turn context from the client body:</p>
<pre tabindex="0"><code class="language-ts">beforeTurn(ctx: TurnContext) {&#10;	if (ctx.body?.selectedFile) {&#10;		return {&#10;			system: ctx.system + `\n\nUser is editing: ${ctx.body.selectedFile}`,&#10;		};&#10;	}&#10;}&#10;</code></pre>
<p>Hide reasoning for internal continuation turns:</p>
<pre tabindex="0"><code class="language-ts">beforeTurn(ctx: TurnContext) {&#10;	if (ctx.continuation) {&#10;		return { sendReasoning: false };&#10;	}&#10;}&#10;</code></pre>
<p>Force structured output for a turn:</p>
<pre tabindex="0"><code class="language-ts">import { Output } from &quot;ai&quot;;&#10;import { z } from &quot;zod&quot;;&#10;&#10;const ResultSchema = z.object({ severity: z.enum([&quot;low&quot;, &quot;high&quot;]) });&#10;&#10;beforeTurn(ctx: TurnContext) {&#10;	if (ctx.body?.mode === &quot;structured-answer&quot;) {&#10;		return {&#10;			output: Output.object({ schema: ResultSchema }),&#10;			activeTools: [],&#10;		};&#10;	}&#10;}&#10;</code></pre>
<p><code>output</code> is a turn-level setting only. The AI SDK's <code>prepareStep</code> does not accept an <code>output</code> override, so <code>beforeStep</code> cannot toggle structured output on a single step.</p>
<h2 id="beforestep">beforeStep</h2>
<p>Called before each AI SDK step in the agentic loop. Think forwards this hook to <code>streamText</code> as <code>prepareStep</code>, so it receives the AI SDK's full prepare-step context and can return per-step overrides. Use <code>beforeTurn</code> for turn-wide assembly and <code>beforeStep</code> when the decision depends on the step number or previous step results.</p>
<pre tabindex="0"><code class="language-ts">beforeStep(ctx: PrepareStepContext): StepConfig | void {&#10;	if (ctx.stepNumber &gt; 0) {&#10;		return { activeTools: [] };&#10;	}&#10;}&#10;</code></pre>
<h2 id="beforetoolcall">beforeToolCall</h2>
<p>Called before a server-side tool's <code>execute</code> function runs. Think wraps each server-side tool so the hook can allow, modify, block, or substitute the call before the model receives the tool result.</p>
<pre tabindex="0"><code class="language-ts">beforeToolCall(ctx: ToolCallContext): ToolCallDecision | void {&#10;	if (ctx.toolName === &quot;delete&quot; &amp;&amp; this.isReadOnlyMode) {&#10;		return { action: &quot;block&quot;, reason: &quot;delete is disabled in read-only mode&quot; };&#10;	}&#10;&#10;	if (ctx.toolName === &quot;weather&quot;) {&#10;		const cached = this.weatherCache.get(JSON.stringify(ctx.input));&#10;		if (cached) return { action: &quot;substitute&quot;, output: cached };&#10;	}&#10;}&#10;</code></pre>
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
<td><code>toolName</code></td>
<td><code>string</code></td>
<td>Name of the tool being called</td>
</tr>
<tr>
<td><code>input</code></td>
<td><code>unknown</code></td>
<td>Input the model provided</td>
</tr>
<tr>
<td><code>toolCallId</code></td>
<td><code>string</code></td>
<td>ID for this tool call</td>
</tr>
<tr>
<td><code>messages</code></td>
<td><code>ModelMessage[]</code></td>
<td>Messages visible at tool execution time</td>
</tr>
<tr>
<td><code>abortSignal</code></td>
<td><code>AbortSignal | undefined</code></td>
<td>Signal that aborts if the turn is canceled</td>
</tr>
</tbody>
</table>
<p>Return a <code>ToolCallDecision</code> to control execution:</p>
<table>
<thead>
<tr>
<th>Decision</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>void</code> or <code>{ action: &quot;allow&quot; }</code></td>
<td>Run the original tool with the original input</td>
</tr>
<tr>
<td><code>{ action: &quot;allow&quot;, input }</code></td>
<td>Run the original tool with modified input</td>
</tr>
<tr>
<td><code>{ action: &quot;block&quot;, reason }</code></td>
<td>Skip the original tool and return <code>reason</code> as the tool result</td>
</tr>
<tr>
<td><code>{ action: &quot;substitute&quot;, output }</code></td>
<td>Skip the original tool and return <code>output</code> as the tool result</td>
</tr>
</tbody>
</table>
<p>If a wrapped tool returns an <code>AsyncIterable</code> for preliminary tool results, Think collapses the iterable to its final yielded value after <code>beforeToolCall</code> runs. If you need true preliminary streaming from that tool, avoid intercepting it with <code>beforeToolCall</code>.</p>
<h2 id="aftertoolcall">afterToolCall</h2>
<p>Called after a tool outcome is known. This includes real executions, blocked calls, substituted calls, and thrown tool errors.</p>
<pre tabindex="0"><code class="language-ts">afterToolCall(ctx: ToolCallResultContext) {&#10;	if (!ctx.success) return;&#10;&#10;	this.env.ANALYTICS.writeDataPoint({&#10;		blobs: [ctx.toolName],&#10;		doubles: [JSON.stringify(ctx.output).length],&#10;	});&#10;}&#10;</code></pre>
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
<td><code>toolName</code></td>
<td><code>string</code></td>
<td>Name of the tool that was called</td>
</tr>
<tr>
<td><code>input</code></td>
<td><code>unknown</code></td>
<td>Input the model provided</td>
</tr>
<tr>
<td><code>toolCallId</code></td>
<td><code>string</code></td>
<td>ID for this tool call</td>
</tr>
<tr>
<td><code>messages</code></td>
<td><code>ModelMessage[]</code></td>
<td>Messages visible at tool execution time</td>
</tr>
<tr>
<td><code>durationMs</code></td>
<td><code>number</code></td>
<td>Tool execution duration in milliseconds</td>
</tr>
<tr>
<td><code>success</code></td>
<td><code>boolean</code></td>
<td>Whether the model received a successful tool outcome</td>
</tr>
<tr>
<td><code>output</code></td>
<td><code>unknown</code></td>
<td>Present when <code>success</code> is <code>true</code></td>
</tr>
<tr>
<td><code>error</code></td>
<td><code>unknown</code></td>
<td>Present when <code>success</code> is <code>false</code></td>
</tr>
</tbody>
</table>
<p>For blocked and substituted tool calls, <code>success</code> is <code>true</code> because the model receives a valid tool result. Only thrown errors from the original tool execution surface as <code>success: false</code>.</p>
<h2 id="onstepfinish">onStepFinish</h2>
<p>Called after each step completes in the agentic loop. <code>StepContext</code> is the AI SDK's step-finish event, so it includes the full step record: generated text, reasoning, files, sources, typed tool calls and results, usage, warnings, request and response metadata, and provider metadata.</p>
<pre tabindex="0"><code class="language-ts">onStepFinish(ctx: StepContext) {&#10;	console.log(&#10;		`Step ${ctx.stepNumber} (${ctx.finishReason}): ` +&#10;			`${ctx.usage.inputTokens}in/${ctx.usage.outputTokens}out`,&#10;	);&#10;}&#10;</code></pre>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>stepNumber</code></td>
<td>Zero-based index of the step</td>
</tr>
<tr>
<td><code>text</code></td>
<td>Text generated in this step</td>
</tr>
<tr>
<td><code>reasoning</code></td>
<td>Reasoning parts emitted by the model</td>
</tr>
<tr>
<td><code>files</code></td>
<td>Files generated during the step</td>
</tr>
<tr>
<td><code>sources</code></td>
<td>Citations or sources used by the model</td>
</tr>
<tr>
<td><code>toolCalls</code></td>
<td>Typed tool calls made in this step</td>
</tr>
<tr>
<td><code>toolResults</code></td>
<td>Typed tool results received in this step</td>
</tr>
<tr>
<td><code>finishReason</code></td>
<td>Why the step ended</td>
</tr>
<tr>
<td><code>usage</code></td>
<td>Token usage, including cache and reasoning tokens</td>
</tr>
<tr>
<td><code>providerMetadata</code></td>
<td>Provider-specific metadata</td>
</tr>
</tbody>
</table>
<h2 id="onchunk">onChunk</h2>
<p>Called for each streaming chunk. High-frequency — fires per token. Use for streaming analytics, progress indicators, or token counting. Observational only.</p>
<h2 id="onchatresponse">onChatResponse</h2>
<p>Called after a chat turn produces and persists an assistant message. The turn lock is released before this hook runs, so it is safe to call <code>saveMessages</code> or other methods from inside.</p>
<p>Fires for all turn paths that persist an assistant message: WebSocket, sub-agent RPC, <code>saveMessages</code>, and auto-continuation. If a turn fails before producing any assistant parts, <code>onChatError</code> handles the error instead.</p>
<pre tabindex="0"><code class="language-ts">onChatResponse(result: ChatResponseResult) {&#10;	if (result.status === &quot;completed&quot;) {&#10;		console.log(`Turn ${result.requestId}: ${result.message.parts.length} parts`);&#10;	}&#10;}&#10;</code></pre>
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
<td>The persisted assistant message</td>
</tr>
<tr>
<td><code>requestId</code></td>
<td><code>string</code></td>
<td>Unique ID for this turn</td>
</tr>
<tr>
<td><code>continuation</code></td>
<td><code>boolean</code></td>
<td>Whether this was a continuation turn</td>
</tr>
<tr>
<td><code>status</code></td>
<td><code>&quot;completed&quot; | &quot;error&quot; | &quot;aborted&quot;</code></td>
<td>How the turn ended</td>
</tr>
<tr>
<td><code>error</code></td>
<td><code>string?</code></td>
<td>Error message (when <code>status</code> is <code>&quot;error&quot;</code>)</td>
</tr>
</tbody>
</table>
<h2 id="onchaterror">onChatError</h2>
<p>Called when an error occurs during a chat turn. Return the error to propagate it, or return a different error. The optional context describes where the failure happened and whether user messages were already persisted. The partial assistant message (if any) is persisted before this hook fires.</p>
<pre tabindex="0"><code class="language-ts">onChatError(error: unknown, ctx?: ChatErrorContext): unknown&#10;</code></pre>
<p><code>ChatErrorContext</code> includes:</p>
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
<td><code>requestId</code></td>
<td><code>string | undefined</code></td>
<td>Chat request ID, when available</td>
</tr>
<tr>
<td><code>stage</code></td>
<td><code>&quot;parse&quot; | &quot;persist&quot; | &quot;turn&quot; | &quot;stream&quot; | &quot;recovery&quot; | &quot;transcript&quot;</code></td>
<td>Failure stage</td>
</tr>
<tr>
<td><code>messagesPersisted</code></td>
<td><code>boolean</code></td>
<td>Whether incoming user messages were already stored</td>
</tr>
<tr>
<td><code>classification</code></td>
<td><code>ChatErrorClassification | undefined</code></td>
<td>Set to <code>&quot;context_overflow&quot;</code> on the terminal <code>onChatError</code> when a context overflow could not be recovered (refer to <a href="#classifychaterror"><code>classifyChatError</code></a>); <code>undefined</code> otherwise</td>
</tr>
</tbody>
</table>
<p>Think also emits <code>chat:request:failed</code> on the <code>agents:chat</code> observability channel with the same stage and persistence information.</p>
<pre tabindex="0"><code class="language-ts">onChatError(error: unknown, ctx?: ChatErrorContext) {&#10;	console.error(&quot;Chat turn failed:&quot;, ctx?.stage, error);&#10;	if (ctx?.classification === &quot;context_overflow&quot;) {&#10;		return new Error(&quot;This conversation is too long to continue. Please start a new one.&quot;);&#10;	}&#10;	return new Error(&quot;Something went wrong. Please try again.&quot;);&#10;}&#10;</code></pre>
<h2 id="classifychaterror">classifyChatError</h2>
<p>Called when an error occurs during a turn, <strong>before</strong> <code>onChatError</code>. Maps a raw provider error into a provider-agnostic category so Think can react without baking provider-specific strings into the framework — the same split as the <code>tokenCounter</code> you pass to <code>compactAfter()</code>. The app owns the mapping because it knows which provider and model it talks to.</p>
<pre tabindex="0"><code class="language-ts">classifyChatError(error: unknown, ctx?: ChatErrorContext): ChatErrorClassification | void&#10;</code></pre>
<p><code>ChatErrorClassification</code> is <code>&quot;context_overflow&quot; | &quot;rate_limit&quot; | &quot;transient&quot; | &quot;fatal&quot; | &quot;unknown&quot;</code>. Today this hook drives only context-overflow recovery. Think calls it when a turn errors and <code>contextOverflow.reactive</code> is enabled. If reactive is off, it is not called.</p>
<p>Returning <code>&quot;context_overflow&quot;</code> runs the compact-and-retry backstop (refer to <a href="/agents/harnesses/think/recovery/#context-window-overflow-recovery">Context-window overflow recovery</a>). If recovery cannot save the turn, that classification is surfaced on the terminal <code>onChatError</code> call through <code>ChatErrorContext.classification</code>.</p>
<p>The other categories are reserved for future use. Returning one today is a no-op and is not forwarded to <code>onChatError</code>. Returning <code>void</code> (the default) keeps the existing terminal behavior.</p>
<p>The argument may be an <code>Error</code>, an AI SDK <code>APICallError</code> (with <code>statusCode</code>/<code>responseBody</code>), or — for in-stream provider errors that surface as a stream error part rather than a throw — the error message string. Narrow accordingly. Provider context-overflow errors arrive as in-stream error parts, so this hook receives them in string form, not as a thrown exception.</p>
<p>The second argument is a <a href="#onchaterror"><code>ChatErrorContext</code></a>. During overflow recovery it is <code>{ stage: &quot;stream&quot;, requestId }</code>, so a classifier can correlate the error with the in-flight turn — for example, to call <code>cancelChat(requestId)</code> and bail out of recovery.</p>
<h3 id="example">Example</h3>
<p>For the common case, assign the bundled <code>defaultContextOverflowClassifier</code>, which matches the context-overflow errors of Anthropic, OpenAI, Google, Bedrock, and others:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2150.md")
</div>
<p>Or write your own, optionally delegating to the bundled classifier:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2151.md")
</div>
