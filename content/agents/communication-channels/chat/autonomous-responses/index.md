---
cp9:
  canonical: https://developers.cloudflare.com/agents/communication-channels/chat/autonomous-responses/
  description: Send server-initiated messages and trigger LLM responses from Cloudflare Agents without user action.
  full_title: Autonomous responses · Cloudflare Agents docs
  head_html: <title>Autonomous responses · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Send server-initiated messages and trigger LLM responses from Cloudflare Agents without user action."><link rel="canonical" href="https://developers.cloudflare.com/agents/communication-channels/chat/autonomous-responses/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/communication-channels/chat/autonomous-responses/index.md"><meta property="og:title" content="Autonomous responses · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send server-initiated messages and trigger LLM responses from Cloudflare Agents without user action."><meta property="og:url" content="https://developers.cloudflare.com/agents/communication-channels/chat/autonomous-responses/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/communication-channels/chat/autonomous-responses/#page","headline":"Autonomous responses \u00b7 Cloudflare Agents docs","description":"Send server-initiated messages and trigger LLM responses from Cloudflare Agents without user action.","url":"https://developers.cloudflare.com/agents/communication-channels/chat/autonomous-responses/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/communication-channels/chat/autonomous-responses/
  schema: 1
---
<p>Send messages and trigger LLM responses from the server without a human action. Use this for scheduled follow-ups, queue processing, email-triggered responses, and autonomous agent workflows.</p>
<h2 id="overview">Overview</h2>
<p>In a typical chat flow, the user sends a message and the agent responds. But agents often need to act on their own — a scheduled reminder fires, a webhook arrives, a workflow completes, or the agent decides to continue after inspecting its own response.</p>
<p>The key primitives:</p>
<table>
<thead>
<tr>
<th>Primitive</th>
<th>Role</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>saveMessages</code></td>
<td>Inject a message and trigger the LLM — the server-side equivalent of <code>sendMessage</code></td>
</tr>
<tr>
<td><code>submitMessages</code></td>
<td>Durably accept a Think turn for async execution and inspect it later</td>
</tr>
<tr>
<td><code>startFiber</code></td>
<td>Durably accept application-owned side effects around a turn</td>
</tr>
<tr>
<td><code>persistMessages</code></td>
<td>Store messages without triggering a response — for injecting context silently</td>
</tr>
<tr>
<td><code>onChatResponse</code></td>
<td>React when any response completes, including ones you did not initiate</td>
</tr>
<tr>
<td><code>isServerStreaming</code></td>
<td>Client-side flag: <code>true</code> when a server-initiated stream is active</td>
</tr>
</tbody>
</table>
<h3 id="savemessages-vs-persistmessages"><code>saveMessages</code> vs <code>persistMessages</code></h3>
<p><code>saveMessages</code> persists messages to SQLite <strong>and</strong> triggers <code>onChatMessage</code> for a new LLM response. It is awaitable — after it returns, the LLM has responded and the message is persisted.</p>
<p><code>persistMessages</code> stores messages and broadcasts them to connected clients, but does <strong>not</strong> trigger a model turn. Use it when you want to inject context (for example, a system message or background data) into the conversation without starting a response.</p>
<h3 id="savemessages-vs-submitmessages"><code>saveMessages</code> vs <code>submitMessages</code></h3>
<p>Use <code>saveMessages()</code> when the caller can wait for the model turn to finish.</p>
<p>Use <code>submitMessages()</code> with Think when the caller needs a fast durable receipt, idempotent retry, and later status inspection. This is useful for webhook handlers, RPC callers, and parent Workers with strict timeout limits:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2081.md")
</div>
<p><code>submitMessages()</code> stores pending work first and appends the messages to the conversation Session only when the submission starts executing. It accepts serializable <code>UIMessage[]</code> values, not the function form supported by <code>saveMessages((messages) =&gt; ...)</code>.</p>
<p>Use <a href="/agents/runtime/execution/durable-execution/#startfiber"><code>startFiber()</code></a> outside Think when the durable unit is a surrounding application job, such as accepting a webhook once, restoring provider state, posting a visible reply, and recording recovery policy. <code>submitMessages()</code> owns Think's conversation admission; managed fibers own external side effects around that turn.</p>
<p>For the full Think API, refer to <a href="/agents/harnesses/think/programmatic-submissions/#submitmessages"><code>submitMessages()</code></a>.</p>
<h3 id="when-to-use-savemessages-vs-onchatresponse">When to use <code>saveMessages</code> vs <code>onChatResponse</code></h3>
<p><strong>Use <code>saveMessages</code> when you control the trigger</strong> — schedule callbacks, webhooks, email handlers, or any method where you decide when to inject a message.</p>
<p><strong>Use <code>onChatResponse</code> when you need to react to responses you did not trigger</strong> — user-initiated messages, auto-continuations after tool approvals, or any turn that the framework ran on your behalf.</p>
<h2 id="waituntilstable"><code>waitUntilStable</code></h2>
<p>Always call <code>waitUntilStable()</code> before reading <code>this.messages</code> or calling <code>saveMessages</code> from schedule callbacks, webhooks, email handlers, or other non-chat entry points.</p>
<p><code>waitUntilStable()</code> waits until the conversation is fully stable:</p>
<ul>
<li>No active LLM stream in progress</li>
<li>No pending client-tool interactions (tool results or approvals the user has not yet provided)</li>
<li>No queued continuation turns</li>
</ul>
<p>It returns <code>true</code> when stable, or <code>false</code> if the timeout expires before a pending interaction resolves. If nothing is pending, it returns immediately.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2082.md")
</div>
<p>Without this guard, you risk reading stale messages or overlapping with an in-flight stream.</p>
<h2 id="trigger-patterns">Trigger patterns</h2>
<h3 id="cron-schedule">Cron schedule</h3>
<p>A daily digest agent that summarizes activity every morning. Cron schedules are idempotent by default, so calling <code>schedule()</code> in <code>onStart</code> is safe — it does not create duplicates across Durable Object restarts.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2083.md")
</div>
<p>The function form of <code>saveMessages</code> — <code>saveMessages((messages) =&gt; [...])</code> — reads the latest persisted messages at execution time. This avoids stale baselines when multiple calls queue up (for example, rapid webhook arrivals). Refer to <a href="/agents/runtime/execution/schedule-tasks/">Schedule tasks</a> for more on <code>schedule()</code> and cron syntax.</p>
<h3 id="processing-a-queue">Processing a queue</h3>
<p>When you control the trigger, a simple loop is the clearest pattern:</p>
<pre tabindex="0"><code class="language-ts">async processQueue() {&#10;	for (const task of this.taskQueue) {&#10;		const stable = await this.waitUntilStable({ timeout: 30_000 });&#10;		if (!stable) {&#10;			console.warn(&quot;Conversation not stable, stopping queue processing&quot;);&#10;			break;&#10;		}&#10;&#10;		await this.saveMessages((messages) =&gt; [&#10;			...messages,&#10;			{&#10;				id: crypto.randomUUID(),&#10;				role: &quot;user&quot;,&#10;				parts: [{ type: &quot;text&quot;, text: task }],&#10;				createdAt: new Date(),&#10;			},&#10;		]);&#10;		// LLM has responded. this.messages is updated. Next iteration.&#10;	}&#10;	this.taskQueue = [];&#10;}&#10;</code></pre>
<p>No special hooks needed — <code>saveMessages</code> returns after the full turn completes.</p>
<h3 id="email-triggered">Email-triggered</h3>
<pre tabindex="0"><code class="language-ts">async onEmail(email: AgentEmail) {&#10;	const stable = await this.waitUntilStable({ timeout: 30_000 });&#10;	if (!stable) {&#10;		console.warn(&quot;Conversation not stable, cannot process email&quot;);&#10;		return;&#10;	}&#10;&#10;	const subject = email.headers.get(&quot;subject&quot;) ?? &quot;(no subject)&quot;;&#10;	const body = await new Response(email.raw).text();&#10;&#10;	await this.saveMessages((messages) =&gt; [&#10;		...messages,&#10;		{&#10;			id: crypto.randomUUID(),&#10;			role: &quot;user&quot;,&#10;			parts: [&#10;				{&#10;					type: &quot;text&quot;,&#10;					text: `Email from ${email.from}: ${subject}\n\n${body}`,&#10;				},&#10;			],&#10;			createdAt: new Date(),&#10;		},&#10;	]);&#10;}&#10;</code></pre>
<h3 id="webhook-triggered">Webhook-triggered</h3>
<pre tabindex="0"><code class="language-ts">async onRequest(request: Request): Promise&lt;Response&gt; {&#10;	const url = new URL(request.url);&#10;&#10;	if (url.pathname.endsWith(&quot;/webhook&quot;) &amp;&amp; request.method === &quot;POST&quot;) {&#10;		const stable = await this.waitUntilStable({ timeout: 30_000 });&#10;		if (!stable) {&#10;			return new Response(&quot;Agent is busy&quot;, { status: 503 });&#10;		}&#10;&#10;		const payload = await request.json();&#10;		try {&#10;			await this.saveMessages((messages) =&gt; [&#10;				...messages,&#10;				{&#10;					id: crypto.randomUUID(),&#10;					role: &quot;user&quot;,&#10;					parts: [&#10;						{&#10;							type: &quot;text&quot;,&#10;							text: `Webhook event: ${JSON.stringify(payload)}`,&#10;						},&#10;					],&#10;					createdAt: new Date(),&#10;				},&#10;			]);&#10;			return new Response(&quot;ok&quot;);&#10;		} catch (error) {&#10;			console.error(&quot;Failed to process webhook:&quot;, error);&#10;			return new Response(&quot;Internal error&quot;, { status: 500 });&#10;		}&#10;	}&#10;&#10;	return super.onRequest(request);&#10;}&#10;</code></pre>
<p>If the webhook provider expects a quick response, use <code>submitMessages()</code> instead. This gives the provider a durable acknowledgement and lets it safely retry with the same idempotency key:</p>
<pre tabindex="0"><code class="language-ts">async onRequest(request: Request): Promise&lt;Response&gt; {&#10;	if (request.method !== &quot;POST&quot;) return super.onRequest(request);&#10;&#10;	const payload = await request.json&lt;{ id: string }&gt;();&#10;	const submission = await this.submitMessages(&#10;		[&#10;			{&#10;				id: crypto.randomUUID(),&#10;				role: &quot;user&quot;,&#10;				parts: [&#10;					{ type: &quot;text&quot;, text: `Webhook event: ${JSON.stringify(payload)}` },&#10;				],&#10;			},&#10;		],&#10;		{ idempotencyKey: payload.id },&#10;	);&#10;&#10;	return Response.json({&#10;		submissionId: submission.submissionId,&#10;		accepted: submission.accepted,&#10;		status: submission.status,&#10;	});&#10;}&#10;</code></pre>
<h3 id="injecting-context-without-triggering-a-response">Injecting context without triggering a response</h3>
<p>Use <code>persistMessages</code> to add messages that the LLM will see on its next turn, without starting a turn now:</p>
<pre tabindex="0"><code class="language-ts">async addBackgroundContext(data: string) {&#10;	const stable = await this.waitUntilStable({ timeout: 30_000 });&#10;	if (!stable) return;&#10;&#10;	await this.persistMessages([&#10;		...this.messages,&#10;		{&#10;			id: crypto.randomUUID(),&#10;			role: &quot;user&quot;,&#10;			parts: [{ type: &quot;text&quot;, text: `[Background context]: ${data}` }],&#10;			createdAt: new Date(),&#10;		},&#10;	]);&#10;	// Message is stored and broadcast to clients, but no LLM call happens.&#10;}&#10;</code></pre>
<h2 id="reacting-to-responses-you-did-not-initiate">Reacting to responses you did not initiate</h2>
<p><code>onChatResponse</code> fires after <strong>every</strong> completed turn — user-initiated messages, <code>saveMessages</code> calls, and auto-continuations. Use it when you need to observe or react to responses regardless of how they were triggered.</p>
<h3 id="broadcasting-state">Broadcasting state</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2084.md")
</div>
<h3 id="analytics">Analytics</h3>
<pre tabindex="0"><code class="language-ts">protected async onChatResponse(result: ChatResponseResult) {&#10;	try {&#10;		await fetch(&quot;https://analytics.example.com/event&quot;, {&#10;			method: &quot;POST&quot;,&#10;			body: JSON.stringify({&#10;				requestId: result.requestId,&#10;				status: result.status,&#10;				continuation: result.continuation,&#10;			}),&#10;		});&#10;	} catch (error) {&#10;		console.error(&quot;Analytics reporting failed:&quot;, error);&#10;	}&#10;}&#10;</code></pre>
<h3 id="chained-reasoning">Chained reasoning</h3>
<p>An agent can inspect its own response and decide whether to continue. This works for user-initiated messages too — you cannot predict what the user will ask, but you can react to what the agent said.</p>
<pre tabindex="0"><code class="language-ts">protected async onChatResponse(result: ChatResponseResult) {&#10;	if (result.status !== &quot;completed&quot;) return;&#10;&#10;	const lastText = result.message.parts&#10;		.filter((p) =&gt; p.type === &quot;text&quot;)&#10;		.map((p) =&gt; p.text)&#10;		.join(&quot;&quot;);&#10;&#10;	if (lastText.includes(&quot;[NEEDS_MORE_RESEARCH]&quot;)) {&#10;		await this.saveMessages((messages) =&gt; [&#10;			...messages,&#10;			{&#10;				id: crypto.randomUUID(),&#10;				role: &quot;user&quot;,&#10;				parts: [{ type: &quot;text&quot;, text: &quot;Continue your research.&quot; }],&#10;				createdAt: new Date(),&#10;			},&#10;		]);&#10;	}&#10;}&#10;</code></pre>
<p>When <code>saveMessages</code> is called from inside <code>onChatResponse</code>, the inner turn runs to completion and <code>saveMessages</code> returns. After the current <code>onChatResponse</code> call returns, the framework fires <code>onChatResponse</code> again for the inner response. This continues until no more work is queued. The framework never nests <code>onChatResponse</code> calls — results are drained sequentially.</p>
<h3 id="reactive-queue-processing">Reactive queue processing</h3>
<p>When queue items can be added by external events (user messages, webhooks) at any time, <code>onChatResponse</code> lets you drain the queue after every response regardless of who triggered it:</p>
<pre tabindex="0"><code class="language-ts">protected async onChatResponse(result: ChatResponseResult) {&#10;	if (result.status === &quot;completed&quot; &amp;&amp; this.taskQueue.length &gt; 0) {&#10;		const next = this.taskQueue.shift()!;&#10;		await this.saveMessages((messages) =&gt; [&#10;			...messages,&#10;			{&#10;				id: crypto.randomUUID(),&#10;				role: &quot;user&quot;,&#10;				parts: [{ type: &quot;text&quot;, text: next }],&#10;				createdAt: new Date(),&#10;			},&#10;		]);&#10;	}&#10;}&#10;</code></pre>
<h3 id="chatresponseresult-fields"><code>ChatResponseResult</code> fields</h3>
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
<td>The finalized assistant message</td>
</tr>
<tr>
<td><code>requestId</code></td>
<td><code>string</code></td>
<td>Unique ID for this turn</td>
</tr>
<tr>
<td><code>continuation</code></td>
<td><code>boolean</code></td>
<td><code>true</code> if this was an auto-continuation</td>
</tr>
<tr>
<td><code>status</code></td>
<td><code>&quot;completed&quot; | &quot;error&quot; | &quot;aborted&quot;</code></td>
<td>How the turn ended</td>
</tr>
<tr>
<td><code>error</code></td>
<td><code>string | undefined</code></td>
<td>Error details when status is <code>&quot;error&quot;</code></td>
</tr>
</tbody>
</table>
<h2 id="client-side-detecting-server-initiated-streams">Client-side: detecting server-initiated streams</h2>
<p>When the server triggers a stream via <code>saveMessages</code>, the AI SDK's <code>status</code> stays <code>&quot;ready&quot;</code> because the client did not initiate the request. The <code>useAgentChat</code> hook provides two additional flags to handle this:</p>
<table>
<thead>
<tr>
<th>Flag</th>
<th>What it tracks</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>status</code></td>
<td>AI SDK lifecycle: <code>&quot;submitted&quot;</code>, <code>&quot;streaming&quot;</code>, <code>&quot;ready&quot;</code>, <code>&quot;error&quot;</code> — only for client-initiated requests</td>
</tr>
<tr>
<td><code>isServerStreaming</code></td>
<td><code>true</code> when a server-initiated stream is active</td>
</tr>
<tr>
<td><code>isStreaming</code></td>
<td><code>true</code> when either client or server streaming is active — use this for a universal indicator</td>
</tr>
</tbody>
</table>
<p>Use <code>isStreaming</code> for most UI concerns (disabling the send button, showing a loading indicator). Use <code>isServerStreaming</code> only when you need to distinguish between user-initiated and server-initiated streams (for example, to show a different indicator like &quot;Agent is working in the background...&quot;).</p>
<pre tabindex="0"><code class="language-tsx">import { useAgent } from &quot;agents/react&quot;;&#10;import { useAgentChat } from &quot;@cloudflare/ai-chat/react&quot;;&#10;&#10;function Chat() {&#10;	const agent = useAgent({ agent: &quot;ChatAgent&quot; });&#10;	const { messages, sendMessage, isStreaming, isServerStreaming } =&#10;		useAgentChat({ agent });&#10;&#10;	return (&#10;		&lt;div&gt;&#10;			{messages.map((m) =&gt; (&#10;				&lt;div key={m.id}&gt;{/* render message */}&lt;/div&gt;&#10;			))}&#10;&#10;			{isServerStreaming &amp;&amp; &lt;div&gt;Agent is working in the background...&lt;/div&gt;}&#10;			{!isServerStreaming &amp;&amp; isStreaming &amp;&amp; &lt;div&gt;Agent is responding...&lt;/div&gt;}&#10;&#10;			&lt;form&#10;				onSubmit={(e) =&gt; {&#10;					e.preventDefault();&#10;					const input = e.currentTarget.elements.namedItem(&#10;						&quot;input&quot;,&#10;					) as HTMLInputElement;&#10;					sendMessage({ text: input.value });&#10;					input.value = &quot;&quot;;&#10;				}}&#10;			&gt;&#10;				&lt;input name=&quot;input&quot; placeholder=&quot;Type a message...&quot; /&gt;&#10;				&lt;button type=&quot;submit&quot; disabled={isStreaming}&gt;&#10;					Send&#10;				&lt;/button&gt;&#10;			&lt;/form&gt;&#10;		&lt;/div&gt;&#10;	);&#10;}&#10;</code></pre>
<p>When a server-driven response arrives while the user is idle, connected clients see the new messages appear in real time. The <code>isStreaming</code> flag transitions from <code>false</code> to <code>true</code> to <code>false</code> as the stream runs, so UI elements like the send button automatically disable and re-enable.</p>
<h2 id="interaction-with-messageconcurrency">Interaction with <code>messageConcurrency</code></h2>
<p>The <code>messageConcurrency</code> setting on <code>AIChatAgent</code> controls how overlapping user submissions behave (<code>&quot;queue&quot;</code>, <code>&quot;latest&quot;</code>, <code>&quot;merge&quot;</code>, <code>&quot;drop&quot;</code>, <code>&quot;debounce&quot;</code>). This setting only applies to <code>sendMessage()</code> — user-initiated messages from the client.</p>
<p><code>saveMessages()</code> always uses serialized (queued) behavior regardless of the <code>messageConcurrency</code> setting. This means server-driven messages never get dropped, merged, or debounced — they always queue up and execute in order.</p>
<h2 id="combining-with-other-agent-primitives">Combining with other Agent primitives</h2>
<table>
<thead>
<tr>
<th>Primitive</th>
<th>How to combine</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>schedule()</code></td>
<td>Schedule a callback that calls <code>saveMessages</code> — see the cron example above</td>
</tr>
<tr>
<td><code>queue()</code></td>
<td>Queue a method that calls <code>saveMessages</code> for deferred processing</td>
</tr>
<tr>
<td><code>startFiber()</code></td>
<td>Durably accept and inspect application-owned work around a message turn</td>
</tr>
<tr>
<td><code>runWorkflow()</code></td>
<td>Start a Workflow; use <code>AgentWorkflow.agent</code> RPC to call a method that triggers <code>saveMessages</code> or <code>submitMessages</code></td>
</tr>
<tr>
<td><code>onEmail()</code></td>
<td>Convert email content to a chat message and call <code>saveMessages</code></td>
</tr>
<tr>
<td><code>onRequest()</code></td>
<td>Handle webhooks and call <code>saveMessages</code> or <code>submitMessages</code></td>
</tr>
<tr>
<td><code>this.broadcast()</code></td>
<td>Broadcast custom state from <code>onChatResponse</code></td>
</tr>
</tbody>
</table>
<h2 id="cancelling-a-server-driven-turn">Cancelling a server-driven turn</h2>
<p>Pass an <code>AbortSignal</code> when the same Durable Object starts and controls the turn:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2085.md")
</div>
<p><code>continueLastTurn()</code> accepts the same <code>options.signal</code> argument. <code>AbortSignal</code> objects cannot cross Durable Object RPC boundaries, and the signal is in memory only. If the Durable Object hibernates mid-turn, durable recovery usually continues without the original signal. For pre-stream interruptions, recovery can retry the latest unanswered user message. An abort fired after restart has no effect on the recovered turn.</p>
<p>Persist cancellation intent when cancellation must survive a restart. Read that state in <code>onChatRecovery()</code> and return <code>{ continue: false }</code> to prevent another model call.</p>
<p>Use <code>cancelSubmission(submissionId)</code> for durable cancellation when work was accepted with <code>submitMessages()</code> or when cancellation must cross Worker and Durable Object RPC boundaries.</p>
<p>Use <code>cancelFiber(fiberId)</code> when the durable unit was accepted with <code>startFiber()</code> and the cancellation should apply to the surrounding application job rather than a Think turn.</p>
<h2 id="important-notes">Important notes</h2>
<ul>
<li><strong><code>saveMessages</code> is awaitable.</strong> After it returns, the LLM has responded and the message is persisted. Use this when you control the trigger.</li>
<li><strong>Use the function form of <code>saveMessages</code>.</strong> <code>saveMessages((messages) =&gt; [...messages, newMsg])</code> reads the latest persisted messages at execution time, avoiding stale baselines when multiple calls queue up.</li>
<li><strong><code>persistMessages</code> does not trigger a response.</strong> Use it to inject context or system messages silently.</li>
<li><strong><code>onChatResponse</code> is for reacting to turns you did not initiate.</strong> Use it for user-initiated messages, auto-continuations, or any turn where you did not call <code>saveMessages</code> yourself.</li>
<li><strong><code>onChatResponse</code> does not nest.</strong> When <code>saveMessages</code> is called from inside <code>onChatResponse</code>, the inner turn completes and <code>onChatResponse</code> fires again sequentially — not recursively.</li>
<li><strong>Messages are persisted before <code>onChatResponse</code> fires.</strong> If the Durable Object evicts during the hook, the conversation is safe in SQLite — only the hook callback is lost.</li>
<li><strong><code>waitUntilStable()</code> before injecting.</strong> Always call this from schedule callbacks, webhooks, or other non-chat entry points to avoid overlapping with an in-flight stream or pending tool interaction.</li>
<li><strong>The client sees the completed response before <code>onChatResponse</code> runs.</strong> The server-side hook does not delay the client.</li>
<li><strong><code>messageConcurrency</code> does not affect <code>saveMessages</code>.</strong> Server-driven messages always queue and execute in order.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-chat-agents-agents-communication-channels-chat-chat-agents"><a href="/agents/communication-channels/chat/chat-agents/">Chat agents</a></h3><p>Full API reference for AIChatAgent, saveMessages, persistMessages, and onChatResponse.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-schedule-tasks-agents-runtime-execution-schedule-tasks"><a href="/agents/runtime/execution/schedule-tasks/">Schedule tasks</a></h3><p>Delayed, cron, and interval scheduling for agent callbacks.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-webhooks-agents-communication-channels-webhooks"><a href="/agents/communication-channels/webhooks/">Webhooks</a></h3><p>Receive webhook events and route them to agent instances.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-email-routing-agents-communication-channels-email"><a href="/agents/communication-channels/email/">Email routing</a></h3><p>Handle inbound emails in your agent.</p></div>
