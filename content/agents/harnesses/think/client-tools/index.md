---
cp9:
  canonical: https://developers.cloudflare.com/agents/harnesses/think/client-tools/
  description: Browser-side tools, approval flows, auto-continuation, message concurrency, and multi-tab broadcast for Think agents.
  full_title: Client tools · Cloudflare Agents docs
  head_html: <title>Client tools · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Browser-side tools, approval flows, auto-continuation, message concurrency, and multi-tab broadcast for Think agents."><link rel="canonical" href="https://developers.cloudflare.com/agents/harnesses/think/client-tools/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/harnesses/think/client-tools/index.md"><meta property="og:title" content="Client tools · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Browser-side tools, approval flows, auto-continuation, message concurrency, and multi-tab broadcast for Think agents."><meta property="og:url" content="https://developers.cloudflare.com/agents/harnesses/think/client-tools/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/harnesses/think/client-tools/#page","headline":"Client tools \u00b7 Cloudflare Agents docs","description":"Browser-side tools, approval flows, auto-continuation, message concurrency, and multi-tab broadcast for Think agents.","url":"https://developers.cloudflare.com/agents/harnesses/think/client-tools/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/harnesses/think/client-tools/
  schema: 1
---
<p>Think supports tools that execute in the browser. The client sends serializable tool schemas in the chat request body, Think merges them with server tools, and when the LLM calls a client tool, the call is routed to the client for execution.</p>
<h2 id="defining-client-tools">Defining client tools</h2>
<p>For dynamic client-side tools, pass <code>tools</code> to <code>useAgentChat</code>. Tools with an <code>execute</code> function are registered with the server as client-executed tools:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2171.md")
</div>
<p>Client tools are tools without an <code>execute</code> function on the server — they only have a schema. When the LLM produces a tool call for one, Think routes it to the client.</p>
<p>For most apps, prefer defining tools on the server and using <code>onToolCall</code> for browser-only execution. The <code>tools</code> option is most useful for SDKs or platforms where the browser decides the available tool surface at runtime.</p>
<h2 id="client-tools-over-the-sub-agent-rpc-chat-path">Client tools over the sub-agent RPC <code>chat()</code> path</h2>
<p>When a parent agent delegates to a Think sub-agent over RPC with <code>chat()</code> (rather than the browser WebSocket), there is no WebSocket to carry <code>clientTools</code> or to send tool results back. Pass them through <code>ChatOptions</code> instead:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2172.md")
</div>
<ul>
<li><code>clientTools</code> registers the tool schemas for the turn, exactly like the WebSocket <code>clientTools</code> field.</li>
<li><code>onClientToolCall</code> executes a client-tool call and returns its output. The model can call a client tool, receive the result, and continue — all within the single <code>chat()</code> call.</li>
</ul>
<p>If you omit <code>onClientToolCall</code>, the tools are registered but have no result: the model's call is surfaced through the stream callback and the turn ends with a dangling tool call (the RPC stream callback has no inbound result channel of its own). Supply <code>onClientToolCall</code> whenever you want the round trip to complete.</p>
<h3 id="behavior-notes">Behavior notes</h3>
<ul>
<li><strong>Recovery:</strong> the schemas and <code>onClientToolCall</code> executor are per-turn only and are never persisted (the executor is a live RPC reference that dies with the isolate, and unlike the WebSocket path there is no client to replay a <code>tool-result</code> after an eviction). If an eviction interrupts the turn while a client-tool call is mid-flight, chat recovery errors the orphaned call (treating it like a server tool) and the model proceeds. To re-run cleanly, the parent re-invokes <code>chat()</code> with the <code>clientTools</code> and <code>onClientToolCall</code> again.</li>
<li><strong>Errors:</strong> if <code>onClientToolCall</code> throws, the failure is surfaced to the model as a tool error (<code>output-error</code>) and the turn continues — it does not crash the turn.</li>
<li><strong>Serialization:</strong> the value returned from <code>onClientToolCall</code> becomes the tool output, so it must be JSON-serializable (it travels back over RPC and into the model context).</li>
<li><strong>No approval gate:</strong> RPC client tools execute immediately through <code>onClientToolCall</code>. The WebSocket approval flow (<code>needsApproval</code>) does not apply on this path — gate execution inside your executor if you need it.</li>
<li><strong>Name precedence:</strong> client tools are merged after server tools, so a client tool that shares a name with a server tool (for example a workspace tool) overrides it for that turn — the same as the WebSocket path.</li>
<li><strong>Abort:</strong> aborting the turn via <code>signal</code> stops the loop, but an in-flight <code>onClientToolCall</code> is not itself cancelled; the turn ends after the current call resolves.</li>
</ul>
<h2 id="approval-flow">Approval flow</h2>
<p>Handle browser-side tool execution on the client with <code>onToolCall</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2173.md")
</div>
<h2 id="auto-continuation">Auto-continuation</h2>
<p>After a client tool result is received, Think automatically continues the conversation without a new user message. The continuation turn has <code>continuation: true</code> in the <code>TurnContext</code>, which you can use in <code>beforeTurn</code> to adjust model or tool selection.</p>
<p>When a turn produces several client tool calls at once, Think waits for <strong>all</strong> of their results before starting a single continuation, instead of starting one continuation per result. An immediate resume request that arrives while a continuation is already pending attaches to that pending continuation rather than starting a duplicate, and server-side <code>needsApproval</code> continuations resume reliably once the approval is recorded.</p>
<h2 id="survive-restarts-while-waiting-for-a-human">Survive restarts while waiting for a human</h2>
<p>A Durable Object can be evicted at any time, including while a turn is paused on an approval prompt or a client-side tool call. <a href="/agents/harnesses/think/recovery/"><code>Think</code> durable recovery</a> is always on. The SDK treats such a turn as waiting on the human, not stuck. It parks the turn instead of failing it. The user's eventual approval or tool result resumes the conversation.</p>
<p>For which interactions are exempt from recovery budgets, refer to <a href="/agents/communication-channels/chat/chat-agents/#turns-waiting-on-a-human-are-not-sealed">Turns waiting on a human are not sealed</a>.</p>
<h2 id="message-concurrency">Message concurrency</h2>
<p>The <code>messageConcurrency</code> property controls how overlapping user submits behave when a chat turn is already active.</p>
<table>
<thead>
<tr>
<th>Strategy</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;queue&quot;</code></td>
<td>Queue every submit and process them in order. Default.</td>
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
<td>Ignore overlapping submits entirely. Messages are not persisted.</td>
</tr>
<tr>
<td><code>{ strategy: &quot;debounce&quot;, debounceMs?: number }</code></td>
<td>Trailing-edge latest with a quiet window (default 750ms).</td>
</tr>
</tbody>
</table>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2174.md")
</div>
<h2 id="multi-tab-broadcast">Multi-tab broadcast</h2>
<p>Think broadcasts streaming responses to all connected WebSocket clients. When multiple browser tabs are connected to the same agent, all tabs see the streamed response in real time. Tool call states (pending, result, approval) are broadcast to all tabs.</p>
<p>Programmatic <code>chat()</code> turns and <code>clearMessages()</code> also broadcast message updates to connected <code>useAgentChat</code> clients, so browser clients stay in sync without reconnecting.</p>
