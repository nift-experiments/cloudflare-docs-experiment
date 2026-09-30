<p>Build and host Agents on Cloudflare, connect chat, voice, email, Slack, and webhooks to a durable agent runtime with Browser, Sandbox, AI Search, MCP, Payments, and other MCP tools.</p>
<p>When you host agents on Cloudflare, each agent session has a durable identity, local SQL storage, real-time connections, scheduled work, and recoverable execution.</p>
<p>Deploy once and Cloudflare runs your agents across its global network, scaling to tens of millions of instances. No infrastructure to manage, no sessions to reconstruct, no state to externalize.</p>
<div class="nb-interactive-component" data-cf-component="AgentsPlatformDiagram"></div>
<p>Agents on Cloudflare are composed from four parts:</p>
<ul>
<li><strong>Communication channels</strong> define how users and systems reach your agent, such as <a href="/agents/communication-channels/chat/">chat</a>, <a href="/agents/communication-channels/voice/">voice</a>, <a href="/agents/communication-channels/email/">email</a>, <a href="/agents/communication-channels/slack/">Slack</a>, <a href="/agents/communication-channels/webhooks/">webhooks</a>, and other event sources.</li>
<li><strong>The agent harness</strong> defines the loop: how the agent calls models, selects tools, handles tool results, streams responses, and decides whether to continue. Use <a href="/agents/harnesses/think/">Project Think</a> for an opinionated harness, or build your own loop directly on the <a href="/agents/runtime/agents-api/">Agents SDK runtime</a>.</li>
<li><strong>The Agents SDK runtime</strong> provides durable infrastructure: the <a href="/agents/runtime/lifecycle/agent-class/"><code>Agent</code> class</a>, <a href="/agents/runtime/lifecycle/state/">state</a>, <a href="/agents/runtime/lifecycle/sessions/">sessions</a>, <a href="/agents/runtime/communication/routing/">routing</a>, <a href="/agents/runtime/communication/websockets/">WebSockets</a>, <a href="/agents/runtime/execution/schedule-tasks/">scheduling</a>, <a href="/agents/runtime/execution/durable-execution/">fibers</a>, and <a href="/agents/runtime/operations/observability/">observability</a>.</li>
<li><strong>Tools</strong> give the agent capabilities: <a href="/agents/tools/browser/">browser automation</a>, <a href="/agents/tools/sandbox/">sandboxed code execution</a>, <a href="/agents/tools/ai-search/">AI Search</a>, <a href="/agents/tools/mcp/">MCP tools</a>, and <a href="/agents/tools/payments/">payments</a>. <a href="/agents/tools/codemode/">Code Mode</a> lets models discover and orchestrate multiple tools by writing code.</li>
</ul>
<h3 id="get-started">Get started</h3>
<p>Three commands to a running agent. No API keys required — the starter uses <a href="/workers-ai/">Workers AI</a> by default.</p>
<pre><code class="language-sh">npx create-cloudflare@latest --template cloudflare/agents-starter&#10;cd agents-starter &amp;&amp; npm install&#10;npm run dev&#10;</code></pre>
<p>The starter includes streaming AI chat, server-side and client-side tools, human-in-the-loop approval, and task scheduling — a foundation you can build on or tear apart. You can also swap in <a href="/agents/runtime/operations/using-ai-models/">OpenAI, Anthropic, Google Gemini, or any other provider</a>.</p>
<h3 id="example-agents">Example agents</h3>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1617.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1618.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1619.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1620.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1621.md")
</div>
