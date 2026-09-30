<p>A harness is the loop that makes an agent behave like an agent instead of a single model call.</p>
<p>It is responsible for the turn-by-turn work around the model: building the prompt, loading memory, selecting tools, handling tool results, streaming responses, persisting messages, and deciding whether the agent should continue or stop.</p>
<p>You can build this loop yourself on top of the <a href="/agents/runtime/agents-api/">Agents SDK runtime</a>, or use an opinionated harness like <a href="/agents/harnesses/think/">Project Think</a>.</p>
<h2 id="how-harnesses-fit">How harnesses fit</h2>
<p>Harnesses sit on top of the Agents SDK runtime:</p>
<ul>
<li><strong>The runtime</strong> gives the agent durable infrastructure: the <a href="/agents/runtime/lifecycle/agent-class/"><code>Agent</code> class</a>, <a href="/agents/runtime/lifecycle/state/">state</a>, <a href="/agents/runtime/lifecycle/sessions/">sessions</a>, <a href="/agents/runtime/communication/routing/">routing</a>, <a href="/agents/runtime/communication/websockets/">WebSockets</a>, <a href="/agents/runtime/execution/schedule-tasks/">scheduling</a>, <a href="/agents/runtime/execution/durable-execution/">fibers</a>, and <a href="/agents/runtime/operations/observability/">observability</a>.</li>
<li><strong>The harness</strong> gives the agent behavior: model calls, prompt construction, tool selection, stream handling, memory strategy, and lifecycle hooks.</li>
</ul>
<p>The runtime answers “where does this agent live and how does it stay durable?” The harness answers “what does this agent do on each turn?”</p>
<h2 id="choose-an-approach">Choose an approach</h2>
<p>Use a build-your-own harness when you need full control over the model call, message format, tool loop, or UI protocol. This is the right approach when you want to compose low-level APIs directly from the Agents SDK.</p>
<p>Use Project Think when you want an opinionated chat-agent harness with defaults for memory, workspace tools, streaming, lifecycle hooks, sub-agent RPC, and durable chat recovery.</p>
<h2 id="current-harnesses">Current harnesses</h2>
<p><a class="nb-card nb-link-card" href="/agents/harnesses/think/"><h3 id="card-project-think-agents-harnesses-think">Project Think</h3><p>An opinionated chat agent harness with built-in tools, persistent memory, lifecycle hooks, streaming, and sub-agent RPC.</p></a></p>
<h2 id="what-a-harness-usually-owns">What a harness usually owns</h2>
<p>A harness usually owns:</p>
<ul>
<li><strong>Prompt construction</strong> — system prompts, memory, retrieved context, and per-turn instructions.</li>
<li><strong>Model execution</strong> — the call to Workers AI, OpenAI, Anthropic, Gemini, or another provider.</li>
<li><strong>Tool orchestration</strong> — server tools, client tools, MCP tools, approval flows, and continuation after tool results.</li>
<li><strong>Message persistence</strong> — how user, assistant, and tool messages are saved and replayed.</li>
<li><strong>Streaming and recovery</strong> — how responses stream to clients and resume after disconnects or Durable Object eviction.</li>
<li><strong>Extension points</strong> — hooks before and after turns, steps, tool calls, and recovery events.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<p><a class="nb-card nb-link-card" href="/agents/runtime/agents-api/"><h3 id="card-agents-sdk-runtime-agents-runtime-agents-api">Agents SDK runtime</h3><p>Build your own harness directly on the Agent class.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/lifecycle/sessions/"><h3 id="card-sessions-agents-runtime-lifecycle-sessions">Sessions</h3><p>Store conversation context and memory across turns.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/execution/durable-execution/"><h3 id="card-durable-execution-with-fibers-agents-runtime-execution-durable-execution">Durable execution with fibers</h3><p>Recover long-running agent work after Durable Object eviction.</p></a></p>
