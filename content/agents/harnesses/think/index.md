---
cp9:
  canonical: https://developers.cloudflare.com/agents/harnesses/think/
  description: Opinionated chat agent framework with built-in tools, persistent memory, lifecycle hooks, streaming, messengers, scheduled tasks, Workflows, and sub-agent RPC.
  full_title: Think · Cloudflare Agents docs
  head_html: <title>Think · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Opinionated chat agent framework with built-in tools, persistent memory, lifecycle hooks, streaming, messengers, scheduled tasks, Workflows, and sub-agent RPC."><link rel="canonical" href="https://developers.cloudflare.com/agents/harnesses/think/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/harnesses/think/index.md"><meta property="og:title" content="Think · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Opinionated chat agent framework with built-in tools, persistent memory, lifecycle hooks, streaming, messengers, scheduled tasks, Workflows, and sub-agent RPC."><meta property="og:url" content="https://developers.cloudflare.com/agents/harnesses/think/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Agents"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/agents/harnesses/think/#page","headline":"Think \u00b7 Cloudflare Agents docs","description":"Opinionated chat agent framework with built-in tools, persistent memory, lifecycle hooks, streaming, messengers, scheduled tasks, Workflows, and sub-agent RPC.","url":"https://developers.cloudflare.com/agents/harnesses/think/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /agents/harnesses/think/
  schema: 1
---
<p><code>@cloudflare/think</code> lets you build a stateful AI chat agent — one that streams replies, remembers the conversation, and calls tools — by extending a single base class. You provide a model with <code>getModel()</code>, and Think wires up the rest of the chat lifecycle for you: the agentic loop (the model calls tools, reads the results, and keeps going until it has an answer), message persistence, streaming, client tools, stream resumption, and extensions — all backed by Durable Object SQLite.</p>
<p>Think works as both a <strong>top-level agent</strong> (WebSocket chat to browser clients via <code>useAgentChat</code>) and a <strong>sub-agent</strong> (a child agent that another agent drives over RPC via <code>chat()</code>).</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="new-to-cloudflare-agents">New to Cloudflare Agents?</h3>
@markup("md", "content/.markup/bodies/2153.md")
</aside>
<h2 id="quick-start">Quick start</h2>
<h3 id="install">Install</h3>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/think @cloudflare/ai-chat agents ai @cloudflare/shell zod workers-ai-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/think @cloudflare/ai-chat agents ai @cloudflare/shell zod workers-ai-provider" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/think @cloudflare/ai-chat agents ai @cloudflare/shell zod workers-ai-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/think @cloudflare/ai-chat agents ai @cloudflare/shell zod workers-ai-provider" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/think @cloudflare/ai-chat agents ai @cloudflare/shell zod workers-ai-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/think @cloudflare/ai-chat agents ai @cloudflare/shell zod workers-ai-provider" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/think @cloudflare/ai-chat agents ai @cloudflare/shell zod workers-ai-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/think @cloudflare/ai-chat agents ai @cloudflare/shell zod workers-ai-provider" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Think supports AI SDK v6 and v7. Use <code>ai@^6</code> with <code>@ai-sdk/react@^3</code>, or use <code>ai@^7</code> with <code>@ai-sdk/react@^4</code>. Keep the AI SDK packages on matching major versions throughout your project.</p>
<h3 id="server">Server</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2154.md")
</div>
<p>That is it. Think handles the WebSocket chat protocol, message persistence, the agentic loop, message sanitization, stream resumption, client tool support, and workspace file tools.</p>
<h3 id="client">Client</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2155.md")
</div>
<h3 id="configuration">Configuration</h3>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2156.md")
</div>
<h3 id="tracing">Tracing</h3>
<p>Think uses <code>wrapAISDK()</code> internally to instrument model turns, tool calls, and approval lifecycle segments. You do not need to wrap the AI SDK or configure an adapter. To send <code>invoke_agent</code>, <code>chat</code>, <code>execute_tool</code>, and <code>tool_approval</code> spans to Workers Observability, turn on Workers traces:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2157.md")
</div>
<p>Traces appear in the Agents view in the Cloudflare Dashboard. You can inspect conversations and trace timelines. To turn tracing off, set <code>observability.traces.enabled</code> to <code>false</code>. You do not need to change the Think agent class.</p>
<p>For span attributes, payload controls, exporting traces, and direct AI SDK v6 or v7 setup, refer to <a href="/agents/runtime/operations/observability/tracing/">Tracing</a>.</p>
<h2 id="think-vs-aichatagent">Think vs AIChatAgent</h2>
<p>Both Think and <a href="/agents/communication-channels/chat/chat-agents/"><code>AIChatAgent</code></a> extend <code>Agent</code> and speak the same <code>cf_agent_chat_*</code> WebSocket protocol. They serve different goals.</p>
<p><strong>AIChatAgent</strong> is a protocol adapter. You override <code>onChatMessage</code> and are responsible for calling <code>streamText</code>, wiring tools, converting messages, and returning a <code>Response</code>. AIChatAgent handles the plumbing — message persistence, streaming, abort, resume — but the LLM call is entirely your concern.</p>
<p><strong>Think</strong> is an opinionated framework. It makes decisions for you: <code>getModel()</code> returns the model, <code>getSystemPrompt()</code> or <code>configureSession()</code> sets the prompt, <code>getTools()</code> returns tools. The default <code>onChatMessage</code> runs the complete agentic loop. You override individual pieces, not the whole pipeline.</p>
<table>
<thead>
<tr>
<th>Concern</th>
<th>AIChatAgent</th>
<th>Think</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Minimal subclass</strong></td>
<td>~15 lines (wire <code>streamText</code> + tools + system prompt + response)</td>
<td>3 lines (<code>getModel()</code> only)</td>
</tr>
<tr>
<td><strong>Storage</strong></td>
<td>Flat SQL table</td>
<td>Session: tree-structured messages, context blocks, compaction, FTS5</td>
</tr>
<tr>
<td><strong>Regeneration</strong></td>
<td>Destructive (old response deleted)</td>
<td>Non-destructive branching (old responses preserved)</td>
</tr>
<tr>
<td><strong>Context management</strong></td>
<td>Manual</td>
<td>Context blocks with LLM-writable persistent memory</td>
</tr>
<tr>
<td><strong>Sub-agent RPC</strong></td>
<td>Not built in</td>
<td><code>chat()</code> with <code>StreamCallback</code></td>
</tr>
<tr>
<td><strong>Programmatic turns</strong></td>
<td><code>saveMessages()</code></td>
<td><code>saveMessages()</code>, <code>submitMessages()</code>, <code>continueLastTurn()</code></td>
</tr>
<tr>
<td><strong>Compaction</strong></td>
<td><code>maxPersistedMessages</code> (deletes oldest)</td>
<td>Non-destructive summaries via overlays</td>
</tr>
<tr>
<td><strong>Search</strong></td>
<td>Not available</td>
<td>FTS5 full-text search per-session and cross-session</td>
</tr>
</tbody>
</table>
<h3 id="when-to-use-aichatagent">When to use AIChatAgent</h3>
<ul>
<li>You need full control over the LLM call (RAG, multi-model, custom streaming)</li>
<li>You want the <code>Response</code> return type for HTTP middleware or testing</li>
<li>You are building a simple chatbot with no memory requirements</li>
</ul>
<h3 id="when-to-use-think">When to use Think</h3>
<ul>
<li>You want to ship fast (3-line subclass with everything wired)</li>
<li>You need persistent memory (context blocks the model can read and write)</li>
<li>You need long conversations (non-destructive compaction)</li>
<li>You need conversation search (FTS5)</li>
<li>You are building a sub-agent system (parent-child RPC with streaming)</li>
<li>You need proactive agents (programmatic turns from scheduled tasks or webhooks)</li>
<li>You need durable async submission for webhook or RPC callers</li>
</ul>
<h2 id="choose-a-turn-api">Choose a turn API</h2>
<p>Think has several ways to start or continue a turn. They all funnel through one public entry point — <code>runTurn(options)</code> — and the older methods remain as convenience shortcuts.</p>
<h3 id="runturn">runTurn()</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="experimental">Experimental</h3>
@markup("md", "content/.markup/bodies/2152.md")
</aside>
<p><code>runTurn()</code> is the unified turn-admission API. One method, three modes, selected by <code>options.mode</code>:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Use when</th>
<th>Returns</th>
<th>Shortcut for</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;wait&quot;</code> (default)</td>
<td>The caller can block until the model response is finished</td>
<td><code>Promise&lt;TurnResult&gt;</code></td>
<td><code>saveMessages()</code></td>
</tr>
<tr>
<td><code>&quot;submit&quot;</code></td>
<td>The caller needs fast, durable acceptance and a later status</td>
<td><code>Promise&lt;SubmitMessagesResult&gt;</code></td>
<td><code>submitMessages()</code></td>
</tr>
<tr>
<td><code>&quot;stream&quot;</code></td>
<td>The caller wants the response streamed to a callback (RPC)</td>
<td><code>Promise&lt;void&gt;</code></td>
<td><code>chat()</code></td>
</tr>
</tbody>
</table>
<p>The <code>input</code> accepts a string, a <code>UIMessage</code>, an array of messages, or — in <code>wait</code> and <code>stream</code> modes — a function <code>(current) =&gt; UIMessage[]</code> evaluated at admission. (<code>submit</code> does not accept function input.)</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2158.md")
</div>
<p>Key behaviors:</p>
<ul>
<li><strong>Blocking modes cannot nest.</strong> Calling <code>wait</code>/<code>stream</code>/<code>continuation</code> (or the equivalent shortcut) from <em>inside</em> an active turn — for example, from a tool's <code>execute</code> — throws, because it would deadlock the turn queue. From inside a turn, use <code>runTurn({ mode: &quot;submit&quot; })</code> (durable, runs after the current turn frees the queue) or <a href="#add-messages-without-a-turn"><code>addMessages()</code></a> (transcript only, no inference).</li>
<li><strong><code>submit</code> is idempotent.</strong> Pass <code>submissionId</code> and/or <code>idempotencyKey</code>; re-submitting a known key returns the existing record with <code>accepted: false</code> instead of starting a second turn. See <a href="/agents/harnesses/think/programmatic-submissions/">Programmatic submissions</a>.</li>
<li><strong>Recovery-safe.</strong> The <code>wait</code>, <code>stream</code>, and drained <code>submit</code> paths run inference inside a recovery fiber, so an interrupted turn resumes after eviction.</li>
</ul>
<p><code>runTurn</code> is exported alongside its option and result types: <code>RunTurnOptions</code>, <code>RunTurnWait</code>, <code>RunTurnSubmit</code>, <code>RunTurnStream</code>, <code>TurnInputMessages</code>, and <code>TurnResult</code>.</p>
<h3 id="pick-a-shortcut">Pick a shortcut</h3>
<p>The table below maps each scenario to the most direct call. Each shortcut has an unchanged signature; reach for them when you want the narrower surface, or use <code>runTurn()</code> when you want one mental model.</p>
<table>
<thead>
<tr>
<th>Use case</th>
<th>API</th>
</tr>
</thead>
<tbody>
<tr>
<td>A browser user sends chat messages</td>
<td><code>useAgentChat</code> over the WebSocket chat protocol</td>
</tr>
<tr>
<td>Server code can wait for the model response</td>
<td><code>saveMessages()</code></td>
</tr>
<tr>
<td>Server code needs fast durable acceptance and later status</td>
<td><code>submitMessages()</code></td>
</tr>
<tr>
<td>Code should create recurring prompt-driven turns or handlers</td>
<td><code>getScheduledTasks()</code></td>
</tr>
<tr>
<td>Parent code needs direct streaming RPC to a specific child</td>
<td><code>subAgent(...).chat()</code></td>
</tr>
<tr>
<td>A parent delegates work to a retained child agent</td>
<td><code>agentTool()</code> or <code>runAgentTool()</code></td>
</tr>
<tr>
<td>Surround a turn with idempotent app-owned side effects</td>
<td><code>startFiber()</code></td>
</tr>
<tr>
<td>Coordinate multi-step durable orchestration</td>
<td>Workflows</td>
</tr>
<tr>
<td>Add context or messages without starting a model turn</td>
<td><code>addMessages()</code></td>
</tr>
<tr>
<td>Advanced subclass or recovery code continues an assistant turn</td>
<td><code>continueLastTurn()</code></td>
</tr>
</tbody>
</table>
<p>Use <code>saveMessages()</code> when the caller owns the trigger and can wait for the turn to finish. Use <a href="/agents/harnesses/think/programmatic-submissions/"><code>submitMessages()</code></a> when timeout ambiguity would make retries unsafe.</p>
<h3 id="add-messages-without-a-turn">Add messages without a turn</h3>
<p>Use <code>addMessages()</code> to write to the transcript <strong>without</strong> starting a model turn — for importing prior history or injecting background context the next turn should see:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2159.md")
</div>
<p><code>addMessages()</code> appends (or upserts) into the Session tree:</p>
<ul>
<li>It does <strong>not</strong> run inference and does <strong>not</strong> enter the turn queue, so it is safe to call from inside a tool's <code>execute</code> without deadlocking.</li>
<li>Array entries are appended <strong>linearly</strong> (each attaches under the previous one), so imported history stays a single path. By default the first message attaches to the latest committed leaf; pass <code>parentId</code> to attach elsewhere, or <code>null</code> for a root message.</li>
<li>Appends are <strong>idempotent by message id</strong>. Pass <code>{ mode: &quot;upsert&quot; }</code> to update an existing message in place instead.</li>
</ul>
<p>The supported pattern is &quot;add context, then run a turn&quot;: call <code>addMessages()</code>, then <code>runTurn()</code>.</p>
<p>Use <code>chat()</code> for low-level parent-to-child streaming when your code owns forwarding, cancellation, and replay policy. Use <a href="/agents/runtime/execution/agent-tools/">Agents as tools</a> when a parent model or workflow delegates to a child agent and you want retained child runs, event replay, abort bridging, and UI drill-in.</p>
<p>Use <a href="/agents/runtime/execution/durable-execution/#startfiber"><code>startFiber()</code></a> outside Think when the durable unit is an application job around a turn: accepting a webhook once, restoring a serialized channel or thread target, posting a visible reply, or recording app-level recovery policy. Think submissions own conversation admission and turn serialization; managed fibers own external job acceptance, idempotent side effects, and application recovery.</p>
<h2 id="in-this-section">In this section</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/2160.md")
</div>
<h2 id="acknowledgments">Acknowledgments</h2>
<p>Think's design is inspired by <a href="https://pi.dev">Pi</a>.</p>
<h2 id="example">Example</h2>
<div class="nb-card nb-link-card"><h3 id="card-assistant-example-https-github-com-cloudflare-agents-tree-main-examples-assistant"><a href="https://github.com/cloudflare/agents/tree/main/examples/assistant">Assistant example</a></h3><p>Explore a multi-session Think assistant with sub-agent routing, shared workspace, MCP, chat recovery, and GitHub OAuth.</p></div>
<h2 id="related">Related</h2>
<ul>
<li><a href="/agents/runtime/lifecycle/sessions/">Sessions</a> — context blocks, compaction, search, multi-session (the storage layer Think builds on)</li>
<li><a href="/agents/runtime/execution/sub-agents/">Sub-agents</a> — <code>subAgent()</code>, <code>abortSubAgent()</code>, <code>deleteSubAgent()</code> (the base Agent methods for spawning children)</li>
<li><a href="/agents/communication-channels/chat/chat-agents/">Chat agents</a> — <code>AIChatAgent</code> for when you need full control over the LLM call</li>
<li><a href="/agents/concepts/agentic-patterns/long-running-agents/">Long-running agents</a> — sub-agent delegation patterns for multi-week agent lifetimes</li>
<li><a href="/agents/runtime/execution/durable-execution/">Durable execution</a> — <code>runFiber()</code> and crash recovery (used by <code>chatRecovery</code>)</li>
<li><a href="/agents/tools/browser/">Browse the web</a> — full CDP helper API reference</li>
</ul>
