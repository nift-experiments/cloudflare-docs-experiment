<p>Agents change how you work with LLMs. In a stateless Worker, every request starts from scratch — you reconstruct context, call a model, return the response, and forget everything. An Agent keeps state between calls, stays connected to clients over WebSocket, and can call models on its own schedule without a user present.</p>
<p>This page covers the patterns that become possible when your LLM calls happen inside a stateful Agent. For provider setup and code examples, refer to <a href="/agents/runtime/operations/using-ai-models/">Using AI Models</a>.</p>
<h2 id="state-as-context">State as context</h2>
<p>Every Agent has a built-in <a href="/agents/runtime/lifecycle/state/">SQL database</a> and key-value state. Instead of passing an entire conversation history from the client on every request, the Agent stores it and builds prompts from its own storage.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1958.md")
</div>
<p>This means the client does not need to send the full conversation on every message. The Agent owns the history, can prune it, enrich it with retrieved documents, or summarize older turns before sending to the model.</p>
<h2 id="surviving-disconnections">Surviving disconnections</h2>
<p>Reasoning models like DeepSeek R1 or GLM-4 can take 30 seconds to several minutes to respond. In a stateless request-response architecture, the client must stay connected the entire time. If the connection drops, the response is lost.</p>
<p>An Agent keeps running after the client disconnects. When the response arrives, the Agent can persist it to state and deliver it when the client reconnects — even hours or days later.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1959.md")
</div>
<p>With <a href="/agents/communication-channels/chat/chat-agents/"><code>AIChatAgent</code></a>, this is handled automatically — messages are persisted to SQLite and streams resume on reconnect.</p>
<h2 id="autonomous-model-calls">Autonomous model calls</h2>
<p>Agents do not need a user request to call a model. You can schedule model calls to run in the background — for nightly summarization, periodic classification, monitoring, or any task that should happen without human interaction.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1960.md")
</div>
<h2 id="multi-model-pipelines">Multi-model pipelines</h2>
<p>Because an Agent maintains state across calls, you can chain multiple models in a single method — using a fast model for classification, a reasoning model for planning, and an embedding model for retrieval — without losing context between steps.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1961.md")
</div>
<p>Each intermediate result stays in the Agent's memory for the duration of the method, and the final result is persisted to SQL for future reference.</p>
<h2 id="caching-and-cost-control">Caching and cost control</h2>
<p>Persistent storage means you can cache model responses and avoid redundant calls. This is especially useful for expensive operations like embeddings or long reasoning chains.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1962.md")
</div>
<p>For provider-level caching and rate limit management across multiple agents, use <a href="/ai-gateway/">AI Gateway</a>.</p>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/runtime/operations/using-ai-models/"><h3 id="card-using-ai-models-agents-runtime-operations-using-ai-models">Using AI Models</h3><p>Provider setup, streaming, and code examples for Workers AI, OpenAI, Anthropic, and more.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/communication-channels/chat/chat-agents/"><h3 id="card-chat-agents-agents-communication-channels-chat-chat-agents">Chat agents</h3><p>AIChatAgent handles message persistence, resumable streaming, and tools automatically.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/lifecycle/state/"><h3 id="card-store-and-sync-state-agents-runtime-lifecycle-state">Store and sync state</h3><p>SQL database and key-value state APIs for building context and caching.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/execution/schedule-tasks/"><h3 id="card-schedule-tasks-agents-runtime-execution-schedule-tasks">Schedule tasks</h3><p>Run autonomous model calls on a delay, schedule, or cron.</p></a></p>
