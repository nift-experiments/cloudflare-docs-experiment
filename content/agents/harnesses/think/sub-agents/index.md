---
cp9:
  canonical: https://developers.cloudflare.com/agents/harnesses/think/sub-agents/
  description: Stream Think turns through a child agent with chat(), and trigger turns programmatically with saveMessages(), continueLastTurn(), and abort.
  full_title: Sub-agent RPC and programmatic turns · Cloudflare Agents docs
  head_html: <title>Sub-agent RPC and programmatic turns · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Stream Think turns through a child agent with chat(), and trigger turns programmatically with saveMessages(), continueLastTurn(), and abort."><link rel="canonical" href="https://developers.cloudflare.com/agents/harnesses/think/sub-agents/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/harnesses/think/sub-agents/index.md"><meta property="og:title" content="Sub-agent RPC and programmatic turns · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Stream Think turns through a child agent with chat(), and trigger turns programmatically with saveMessages(), continueLastTurn(), and abort."><meta property="og:url" content="https://developers.cloudflare.com/agents/harnesses/think/sub-agents/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/harnesses/think/sub-agents/#page","headline":"Sub-agent RPC and programmatic turns \u00b7 Cloudflare Agents docs","description":"Stream Think turns through a child agent with chat(), and trigger turns programmatically with saveMessages(), continueLastTurn(), and abort.","url":"https://developers.cloudflare.com/agents/harnesses/think/sub-agents/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/harnesses/think/sub-agents/
  schema: 1
---
<p>Think works as both a top-level agent and a sub-agent. When used as a sub-agent, the <code>chat()</code> method runs a full turn and streams events via a callback.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2123.md")
</aside>
<p>For durable acceptance with idempotent retry and later status inspection, refer to <a href="/agents/harnesses/think/programmatic-submissions/">Programmatic submissions</a>. For recovery after eviction, refer to <a href="/agents/harnesses/think/recovery/">Durable recovery</a>.</p>
<h2 id="chat">chat</h2>
<pre tabindex="0"><code class="language-ts">async chat(&#10;	userMessage: string | UIMessage,&#10;	callback: StreamCallback,&#10;	options?: ChatOptions,&#10;): Promise&lt;void&gt;&#10;</code></pre>
<h3 id="streamcallback">StreamCallback</h3>
<table>
<thead>
<tr>
<th>Method</th>
<th>When it fires</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>onStart(event)</code></td>
<td>Before work starts; exposes the request ID for cancellation</td>
</tr>
<tr>
<td><code>onEvent(json)</code></td>
<td>For each streaming chunk (JSON-serialized <code>UIMessageChunk</code>)</td>
</tr>
<tr>
<td><code>onDone()</code></td>
<td>After the turn completes and the assistant message is persisted</td>
</tr>
<tr>
<td><code>onError(message)</code></td>
<td>On error during the turn</td>
</tr>
<tr>
<td><code>onInterrupted()</code></td>
<td>Optional. The attempt was interrupted and a scheduled continuation (in a later isolate) owns the final outcome — not done, not a terminal error. Defaults to a no-op</td>
</tr>
</tbody>
</table>
<p><code>onInterrupted</code> matters for a <code>chat()</code>-driven turn that is interrupted and recovers: the RPC promise resolves <strong>cleanly</strong> (the isolate is still alive), so a consumer that keys off the clean resolve would mis-read it as success and finalize whatever partial it had streamed. Treat it as &quot;not done, not failed — a continuation owns the answer&quot;: keep the channel open, show a recovering state, or re-attach, rather than finalizing the partial. A deploy or eviction interruption kills the isolate before this can fire (the caller sees a transport break instead); <code>onInterrupted</code> covers the in-isolate stall-into-recovery path.</p>
<h3 id="chatoptions">ChatOptions</h3>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>signal</code></td>
<td><code>AbortSignal</code> to cancel the turn mid-stream</td>
</tr>
</tbody>
</table>
<p>Tools belong to the child agent. Define durable capabilities with the child's <code>getTools()</code>, extensions, MCP tools, or client tool schemas. Legacy callers that pass <code>options.tools</code> to <code>chat()</code> receive a warning and the value is ignored.</p>
<h3 id="example-parent-calling-a-child">Example: parent calling a child</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2124.md")
</div>
<h3 id="cancelling-a-sub-agent-turn">Cancelling a sub-agent turn</h3>
<p>Use <code>onStart</code> and <code>cancelChat()</code> for RPC-safe cancellation across a sub-agent boundary:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2125.md")
</div>
<p>If the caller and callee are not separated by Workers RPC, you can also pass an <code>AbortSignal</code> to cancel mid-stream:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2126.md")
</div>
<p><code>cancelChat(requestId, reason?)</code> is a no-op if the turn already completed or the request ID is unknown. When aborted, the partial assistant message is still persisted.</p>
<h2 id="savemessages">saveMessages</h2>
<p>Inject messages and trigger a model turn without a WebSocket connection. Use for scheduled responses, webhook-triggered turns, proactive agents, or chaining from <code>onChatResponse</code>.</p>
<pre tabindex="0"><code class="language-ts">async saveMessages(&#10;	messages:&#10;		| UIMessage[]&#10;		| ((current: UIMessage[]) =&gt; UIMessage[] | Promise&lt;UIMessage[]&gt;),&#10;	options?: SaveMessagesOptions,&#10;): Promise&lt;SaveMessagesResult&gt;&#10;</code></pre>
<p>Returns <code>{ requestId, status, error? }</code> where <code>status</code> is <code>&quot;completed&quot;</code>, <code>&quot;error&quot;</code>, <code>&quot;skipped&quot;</code>, or <code>&quot;aborted&quot;</code>.</p>
<table>
<thead>
<tr>
<th><code>status</code></th>
<th>When</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;completed&quot;</code></td>
<td>Turn ran to completion.</td>
</tr>
<tr>
<td><code>&quot;error&quot;</code></td>
<td>Turn started but the stream reported an error. <code>error</code> contains the stream error message when available.</td>
</tr>
<tr>
<td><code>&quot;skipped&quot;</code></td>
<td>Turn invalidated mid-flight, for example by <code>chat-clear</code>; user message persisted, no model run.</td>
</tr>
<tr>
<td><code>&quot;aborted&quot;</code></td>
<td>Turn cancelled before completion via <code>options.signal</code> or <code>chat-request-cancel</code>. Partial assistant chunks still persisted.</td>
</tr>
</tbody>
</table>
<p>Pass <code>options.signal</code> to cancel a programmatic turn from the Durable Object that starts it. <code>AbortSignal</code> cannot cross Durable Object RPC boundaries, and the signal is not persisted across hibernation.</p>
<h3 id="static-messages">Static messages</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2127.md")
</div>
<h3 id="function-form">Function form</h3>
<p>When multiple <code>saveMessages</code> calls queue up, the function form runs with the latest messages when the turn actually starts:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2128.md")
</div>
<h3 id="scheduled-responses">Scheduled responses</h3>
<p>Trigger a recurring prompt turn with <a href="/agents/harnesses/think/scheduled-tasks/"><code>getScheduledTasks()</code></a>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2129.md")
</div>
<h3 id="chaining-from-onchatresponse">Chaining from onChatResponse</h3>
<p>Start a follow-up turn after the current one completes:</p>
<pre tabindex="0"><code class="language-ts">async onChatResponse(result: ChatResponseResult) {&#10;	if (result.status === &quot;completed&quot; &amp;&amp; this.needsFollowUp(result.message)) {&#10;		await this.saveMessages([{&#10;			id: crypto.randomUUID(),&#10;			role: &quot;user&quot;,&#10;			parts: [{ type: &quot;text&quot;, text: &quot;Now summarize what you found.&quot; }],&#10;		}]);&#10;	}&#10;}&#10;</code></pre>
<h2 id="continuelastturn">continueLastTurn</h2>
<p>Run another model call after the latest assistant message without injecting a new user message. Think persists the result as a new assistant message with <code>continuation: true</code>; it does not append chunks to the existing assistant message.</p>
<pre tabindex="0"><code class="language-ts">protected async continueLastTurn(&#10;	body?: Record&lt;string, unknown&gt;,&#10;	options?: SaveMessagesOptions,&#10;): Promise&lt;SaveMessagesResult&gt;&#10;</code></pre>
<p>Returns <code>{ requestId, status: &quot;skipped&quot; }</code> if the last message is not an assistant message. The optional <code>body</code> parameter overrides the stored body for this continuation. Pass <code>options.signal</code> to cancel the continuation while it is running.</p>
<h2 id="abortrequest-and-abortallrequests">abortRequest and abortAllRequests</h2>
<p>Cancel in-flight chat turns from inside the Durable Object:</p>
<pre tabindex="0"><code class="language-ts">protected abortRequest(requestId: string, reason?: unknown): void&#10;protected abortAllRequests(): void&#10;</code></pre>
<p>Use <code>abortRequest()</code> when you know the request ID. Use <code>abortAllRequests()</code> for single-purpose helpers that should cancel whatever turn is currently running. Prefer <code>SaveMessagesOptions.signal</code> for programmatic turns when you can pass a signal at the call site.</p>
