<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 16, 2026</time><h2 id="post-title">Agents SDK improves browser automation, code execution, and recovery</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> makes it easier to build agents that can safely interact with real systems and keep working through interruptions.</p>
<p>Agents can now browse websites through Browser Run, write code against external tools through Code Mode, use client-provided tools when delegating to Think sub-agents, and recover more reliably from deploys, Durable Object evictions, and connection churn.</p>
<h4 id="safer-browser-automation">Safer browser automation</h4>
<p>Agents can now use <a href="/browser-run/">Browser Run</a> through a single durable <code>browser_execute</code> tool. Instead of choosing from a fixed list of actions, the model writes code against the Chrome DevTools Protocol (CDP) and can inspect pages, capture screenshots, read rendered content, debug frontend behavior, and interact with live browser sessions.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17671.md")</div>
<p>Browser sessions can be one-time, reused, or promoted from one-time to persistent during a run. This is useful when an agent needs a human to log in, complete MFA, or approve a sensitive action. The run can pause, keep the same tabs and cookies, and resume after approval.</p>
<p>The browser tools also add Live View URLs, optional session recording, and quick actions such as <code>browser_markdown</code>, <code>browser_extract</code>, <code>browser_links</code>, and <code>browser_scrape</code> for one-shot browsing tasks.</p>
<h4 id="resumable-code-execution-with-approvals">Resumable code execution with approvals</h4>
<p>Code Mode now uses <code>createCodemodeRuntime</code>, connectors, and a durable execution log. This lets you give a model one <code>codemode</code> tool instead of a large prompt full of tool definitions. The model can discover the capabilities it needs, write code against typed globals, and reuse saved snippets.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17672.md")</div>
<p>When the code reaches an approval-gated action, the runtime pauses execution and returns a pending approval. After approval, completed calls replay from the durable log, the approved action runs, and the same code continues. This makes it practical to build agents that create issues, update external systems, or perform other side effects without custom pause-and-resume logic for every tool.</p>
<h4 id="better-think-delegation">Better Think delegation</h4>
<p>Think sub-agents can now use client-defined tools over the RPC <code>chat()</code> path. A parent agent can pass tool schemas with <code>clientTools</code> and resolve tool calls through <code>onClientToolCall</code>. This lets delegated agents use caller-provided capabilities without requiring a browser WebSocket.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17673.md")</div>
<p>Think Workflows also improve <code>step.prompt()</code>. A prompt step now runs a full agentic turn before returning structured output, so the agent can call tools before producing the typed result. This makes Workflow steps more useful for durable triage, research, and approval flows.</p>
<p>The unified Think execute tool can also include <code>cdp.*</code> browser capabilities alongside <code>state.*</code> and <code>tools.*</code> when Browser Run is bound.</p>
<h4 id="voice-output-device-selection">Voice output device selection</h4>
<p>Voice clients can route assistant audio to a specific output device. Use <code>outputDeviceId</code> with <code>useVoiceAgent</code>, or call <code>client.setOutputDevice()</code> from the framework-agnostic client.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17674.md")</div>
<p>Browsers without speaker-selection support continue playing through the default output device and report a non-fatal <code>outputDeviceError</code>.</p>
<h4 id="reliability-fixes">Reliability fixes</h4>
<p>This release includes several fixes for production agents:</p>
<ul>
<li><code>useAgent</code> and <code>AgentClient</code> handle WebSocket replacement more reliably during reconnects and configuration changes.</li>
<li>Chat stream replay is more reliable after reconnects, deploys, and provider errors.</li>
<li>Fiber recovery continues across multi-pass scans and backs off when recovery hooks keep failing.</li>
<li>Agent teardown continues even when the request that started teardown is canceled.</li>
<li>Large session histories use byte-budgeted reads to reduce memory pressure during startup.</li>
</ul>
<h4 id="upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/tools/codemode/">Code Mode documentation</a>, <a href="/agents/tools/browser/">Browser tools documentation</a>, <a href="/agents/harnesses/think/tools/">Think tools documentation</a>, and <a href="/agents/communication-channels/voice/">Voice documentation</a> for more information.</p>
</div></article></div>
