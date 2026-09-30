---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/ai/3/
  description: '2026-06-12'
  full_title: AI changelog - page 3 | Cloudflare Docs
  head_html: <title>AI changelog - page 3 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-06-12"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/ai/3/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="AI changelog - page 3"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-06-12"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/ai/3/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/ai/3/#page","headline":"AI changelog - page 3 | Cloudflare Docs","description":"2026-06-12","url":"https://developers.cloudflare.com/changelog/product-group/ai/3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/ai/3/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="view-the-user-agent-of-requests-in-ai-gateway-logs"><a href="/changelog/post/2026-06-12-user-agent-logging/">View the user agent of requests in AI Gateway logs</a></h2>
<p><em>2026-06-12</em></p>
<p>AI Gateway logs now capture the user agent of the client that made each request, making it easier to identify which SDK, library, or application sent the traffic flowing through your gateway. For example, you can tell apart requests coming from <code>openai-python</code> versus a custom application or a Cloudflare Worker.</p>
<p>The user agent appears alongside the other details in each log entry, and you can filter logs by user agent (equals, does not equal, or contains) in the dashboard.</p>
<p>For more information, refer to <a href="/ai-gateway/observability/logging/">Logging</a>.</p>


<h2 id="moonshot-ai-kimi-k2-7-code-now-available-on-workers-ai"><a href="/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/">Moonshot AI Kimi K2.7 Code now available on Workers AI</a></h2>
<p><em>2026-06-12</em></p>
<p><a href="/workers-ai/models/kimi-k2.7-code/"><code>@cf/moonshotai/kimi-k2.7-code</code></a> is now available on Workers AI. Kimi K2.7 Code is a code-optimized variant of the Kimi K2 family, built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token.</p>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-improved-coding-and-agent-performance">Improved coding and agent performance</h4>
<p>K2.7 Code delivers meaningful gains over K2.6 on coding and agentic benchmarks:</p>
<ul>
<li><strong>+21.8%</strong> on Kimi Code Bench v2</li>
<li><strong>+11.0%</strong> on Program Bench</li>
<li><strong>+31.5%</strong> on MLS Bench Lite</li>
</ul>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-reasoning-efficiency">Reasoning efficiency</h4>
<p>K2.7 Code uses 30% fewer reasoning tokens compared to K2.6, reducing overthinking and lowering inference cost for reasoning-heavy workloads.</p>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>262.1k token context window</strong> for retaining full conversation history, tool definitions, and codebases across long-running agent sessions</li>
<li><strong>Long-horizon coding</strong> with improved instruction following and higher end-to-end coding task success rates</li>
<li><strong>Vision inputs</strong> for processing images alongside text</li>
<li><strong>Thinking mode</strong> with configurable reasoning depth via <code>chat_template_kwargs.thinking</code></li>
<li><strong>Multi-turn tool calling</strong> for building agents that invoke tools across multiple conversation turns</li>
<li><strong>Structured outputs</strong> with JSON schema support</li>
</ul>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-differences-from-kimi-k2-6">Differences from Kimi K2.6</h4>
<p>If you are migrating from Kimi K2.6, note the following:</p>
<ul>
<li>K2.7 Code is optimized for coding tasks with improved benchmark performance and reasoning efficiency</li>
<li>Cached input token pricing is $0.19 per M tokens (vs $0.16 for K2.6)</li>
<li>API usage is identical — no parameter changes required</li>
</ul>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-get-started">Get started</h4>
<p>Use Kimi K2.7 Code through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/ai/run</code>, or the OpenAI-compatible endpoint at <code>/v1/chat/completions</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with any of these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/kimi-k2.7-code/">Kimi K2.7 Code model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="new-formats-parameter-for-the-browser-run-snapshot-endpoint"><a href="/changelog/post/2026-06-11-browser-run-snapshot-formats/">New formats parameter for the Browser Run /snapshot endpoint</a></h2>
<p><em>2026-06-11</em></p>
<p><a href="/browser-run/">Browser Run</a>'s <a href="/browser-run/quick-actions/snapshot/"><code>/snapshot</code> endpoint</a> now supports a <code>formats</code> parameter that lets you return multiple page formats in a single API call. Previously, <code>/snapshot</code> returned only HTML content and a screenshot. You can now also include Markdown and the accessibility tree in the same response.</p>
<p>These formats are particularly useful for AI agent workflows:</p>
<ul>
<li>Markdown provides a token-efficient representation of page content that LLMs can process directly, without parsing HTML markup.</li>
<li>The accessibility tree provides a structured representation of a page's elements, including roles, labels, and hierarchy, helping LLMs understand page structure and navigate its contents.</li>
</ul>
<p>The following example returns a screenshot, Markdown, and the accessibility tree in one call:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17699.md")
</div></div>
<p>You must request at least two formats. If you only need one, use the respective single-format endpoint such as <a href="/browser-run/quick-actions/screenshot-endpoint/"><code>/screenshot</code></a> or <a href="/browser-run/quick-actions/markdown-endpoint/"><code>/markdown</code></a>.</p>
<p>Refer to the <a href="/browser-run/quick-actions/snapshot/"><code>/snapshot</code> documentation</a> for the full list of accepted values.</p>


<h2 id="manage-ai-search-namespaces-with-wrangler-cli"><a href="/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/">Manage AI Search namespaces with Wrangler CLI</a></h2>
<p><em>2026-06-10</em></p>
<p><a href="/ai-search/">AI Search</a> now supports namespace-level Wrangler commands, making it easier to manage <a href="/ai-search/concepts/namespaces/">namespaces</a> from your terminal, scripts, and agent workflows.</p>
<p>The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler ai-search namespace list</code></td>
<td>List AI Search namespaces</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace create</code></td>
<td>Create a new AI Search namespace</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace get</code></td>
<td>Get details for a namespace</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace update</code></td>
<td>Update a namespace description</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace delete</code></td>
<td>Delete an AI Search namespace</td>
</tr>
</tbody>
</table>
<p>Create a namespace for a new application or tenant directly from the CLI:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search namespace create docs-production --description &quot;Production documentation search&quot;&#10;</code></pre>
<p>List namespaces with pagination or filter by name or description:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search namespace list --search docs --page 1 --per-page 10&#10;</code></pre>
<p>Use <code>--json</code> with <code>list</code>, <code>create</code>, <code>get</code>, and <code>update</code> to return structured output that automation and AI agents can parse directly.</p>
<p>Instance-level commands also now support a <code>--namespace</code> flag, so you can interact with instances inside a specific namespace from the CLI:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search list --namespace docs-production&#10;</code></pre>
<p>For full usage details, refer to the <a href="/ai-search/wrangler-commands/">AI Search Wrangler commands documentation</a>.</p>


<h2 id="deprecating-sandbox-sdk-features"><a href="/changelog/post/2026-06-09-deprecating-sandbox-sdk-features/">Deprecating Sandbox SDK features</a></h2>
<p><em>2026-06-09</em></p>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2026-06-09-deprecating-sandbox-sdk-features-sandbox-sdk-1-0-preview">Sandbox SDK 1.0 preview</h4>
@markup("md", "content/.markup/bodies/17752.md")</aside>
<p>Today we are announcing the deprecation of several features from the Sandbox SDK. The SDK has grown and matured substantially since it first launched. As agent workflows have developed, we have shipped many new features and experiments so developers can easily integrate secure, isolated code execution into their workflows.</p>
<p>We want the SDK to continue providing a stable foundation for agentic workflows while we iterate quickly on the codebase. These deprecated features have either been superseded by newer capabilities or seen low adoption. Do not build new work on them. Migrate using the <a href="/sandbox/guides/2026-deprecation/">2026 deprecation migration guide</a>, or move to the <a href="/sandbox/1-0-preview/">Sandbox SDK 1.0 preview</a> when you can.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-http-and-websocket-transports">HTTP and WebSocket transports</h4>
<p>In April 2026, we released the new RPC transport and deprecated the WebSocket transport. This setting governs how the sandbox container talks to the Workers ecosystem. The RPC transport removes the limitations of both the HTTP and WebSocket transports. As of this announcement, RPC is the recommended default. HTTP and WebSocket transports are deprecated and will not ship in future Sandbox SDK majors.</p>
<p>To migrate, update the <code>SANDBOX_TRANSPORT</code> variable to <code>rpc</code> or set the <code>transport</code> option when calling <code>getSandbox()</code>. For more information, refer to the <a href="/sandbox/configuration/transport/">transport configuration documentation</a>.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-desktop">Desktop</h4>
<p>The desktop feature ran a full Linux desktop inside the sandbox (display server, desktop environment, and VNC/noVNC) so agents and apps could drive a GUI with screenshots, mouse, and keyboard — the same <em>computer-use</em> shape other sandbox products expose for UI automation. Adoption stayed low, and we removed it in <code>0.10.2</code>. If you need that capability again, you can build it on top of the sandbox with <a href="/sandbox/1-0-preview/extensions/">extensions</a> rather than a built-in <code>sandbox.desktop</code> API.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-expose-ports">Expose ports</h4>
<p>We recently released support for Cloudflare Tunnel in the Sandbox SDK. This provides a robust API for exposing services running in your sandbox to the public internet. It fixes issues many were facing with local development and deployment to <code>workers.dev</code> domains. To migrate from <code>exposePort()</code> to tunnels, refer to the <a href="/sandbox/api/tunnels/">tunnels API documentation</a> and the <a href="/sandbox/guides/expose-services/">expose services guide</a>.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-default-sessions">Default sessions</h4>
<p>By default, the <code>exec()</code> method in the Sandbox SDK maintains a default session across all calls, so a <code>cd</code> in one call is honored in the next. This convenience helped developers writing <code>exec</code> statements by hand, but confused agents and caused hard-to-trace bugs. As of <code>0.10.3</code>, we have introduced the <a href="/sandbox/configuration/sandbox-options/"><code>enableDefaultSession</code></a> flag on the <code>getSandbox()</code> interface to turn this off. Default sessions as a concept — and the flag — will be removed in an upcoming release.</p>
<p>We recommend setting <code>enableDefaultSession: false</code> today and using the <a href="/sandbox/api/sessions/"><code>sandbox.createSession()</code> API</a> when you need the previous behavior.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-other-changes">Other changes</h4>
<p>We are also consolidating all APIs that buffer data to support streaming by default. This includes <a href="/sandbox/api/files/"><code>readFile</code>, <code>writeFile</code></a>, and <a href="/sandbox/api/commands/"><code>exec</code></a>. The stream equivalents will be removed.</p>
<p>We are exploring moving non-core features like the <a href="/sandbox/guides/code-execution/">code interpreter</a>, <a href="/sandbox/api/terminal/">terminal</a>, and <a href="/sandbox/guides/git-workflows/">git APIs</a> into helpers. These features will retain their existing APIs, so migration should be simple.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-next-steps">Next steps</h4>
<p>If you use any of these features on the <strong>current stable</strong> package, refer to the <a href="/sandbox/guides/2026-deprecation/">2026 deprecation migration guide</a>. Coding agents can use the <strong><code>sandbox-stable</code></strong> skill for stable-package work and that guide for cleanup (<a href="/agent-setup/">Agent setup</a> · <a href="https://github.com/cloudflare/skills">Cloudflare Skills</a>).</p>
<p>If you are moving to <strong>Sandbox SDK 1.0</strong> (<code>@next</code>), use the <a href="/sandbox/1-0-preview/">1.0 preview</a> and <a href="/sandbox/1-0-preview/migrate/">Migrate</a> guides instead — or the <strong><code>sandbox-migrate-to-next</code></strong> skill after installing Cloudflare Skills. New projects should prefer <strong><code>sandbox-next</code></strong> on <code>@next</code>.</p>
<p>For any questions, ask in the <a href="https://discord.gg/cloudflaredev">Cloudflare Developers Discord</a>.</p>


<h2 id="control-ai-costs-with-spend-limits"><a href="/changelog/post/2026-06-05-spend-limits/">Control AI costs with spend limits</a></h2>
<p><em>2026-06-05</em></p>
<p>AI Gateway now supports spend limits — cost-based budgets that track cumulative dollar spend and block requests when the budget is exceeded. Unlike rate limiting, which caps the number of requests, spend limits track actual cost based on token usage and model pricing.</p>
<p>You can scope limits by model, provider, or custom metadata dimensions. For example, give each user a $200/day budget, cap total gateway spend at $10,000/day, or limit a specific model to $50/day per user. Each rule uses a configurable time window with fixed or sliding enforcement.</p>
<p>Spend limits work with both <a href="/ai-gateway/features/unified-billing/">Unified Billing</a> and <a href="/ai-gateway/configuration/bring-your-own-keys/">BYOK</a> requests for models with known pricing.</p>
<p>For more details, refer to the <a href="/ai-gateway/features/spend-limits/">Spend limits documentation</a>.</p>


<h2 id="billable-usage-and-budget-alerts-now-in-product-sidebars"><a href="/changelog/post/2026-06-04-billable-usage-product-sidebar/">Billable usage and budget alerts now in product sidebars</a></h2>
<p><em>2026-06-04</em></p>
<p>Pay-as-you-go customers can now view billable usage and create <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">budget alerts</a> directly from the product overview pages for <a href="/workers/">Workers &amp; Pages</a>, <a href="/d1/">D1</a>, <a href="/r2/">R2</a>, <a href="/kv/">Workers KV</a>, <a href="/queues/">Queues</a>, <a href="/vectorize/">Vectorize</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/containers/">Containers</a>. A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.</p>
<p>The widget pulls from the same data as the <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Billable Usage dashboard</a> and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-06-04-billable-usage-product-sidebar.png" alt="Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service" /></p>
<p>Selecting <strong>Create budget alert</strong> opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.</p>
<p>For more information, refer to the <a href="/billing/">Usage-based billing documentation</a>.</p>


<h2 id="agents-sdk-v0-14-0-agent-skills-messengers-scheduled-tasks-workflows-and-hardened-chat-recovery"><a href="/changelog/post/2026-06-02-agents-sdk-v0.14.0/">Agents SDK v0.14.0: Agent Skills, messengers, scheduled tasks, Workflows, and hardened chat recovery</a></h2>
<p><em>2026-06-02</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> adds four new ways to build with <code>@cloudflare/think</code>: on-demand Agent Skills, chat messengers (starting with Telegram), declarative scheduled tasks, and durable reasoning steps inside Workflows. This release also significantly hardens durable chat recovery, so turns reliably ride through deploys, evictions, and stalled model streams in production.</p>
<h4 id="2026-06-02-agents-sdk-v0.14.0-agent-skills-experimental">Agent Skills (experimental)</h4>
<p>Give an agent a catalog of on-demand instructions, resources, and scripts. A skill source adds a catalog to the system prompt, and the model activates a skill only when a task matches — so a large library of capabilities does not bloat every prompt.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17667.md")</div>
<p>The <code>agents:skills</code> import bundles a local <code>./skills</code> directory through the Agents Vite plugin (one directory per skill, each with a <code>SKILL.md</code>). Skills can also load from R2 or a manifest. When skills are available, Think exposes <code>activate_skill</code>, <code>read_skill_resource</code>, and an optional <code>run_skill_script</code> tool. Skill loading is resilient: a duplicate or failing source is skipped with a warning instead of breaking the agent.</p>
<p>Agent Skills are <strong>experimental</strong>, and script execution in particular is early. The API may change in a future release. We would love your feedback — tell us what you are building and what is missing in the <a href="https://github.com/cloudflare/agents/discussions">Agents repository</a>.</p>
<h4 id="2026-06-02-agents-sdk-v0.14.0-messengers">Messengers</h4>
<p>Connect a Think agent directly to a chat platform. Think owns the webhook route, conversation routing, durable reply fiber, and streamed delivery back to the provider. Telegram ships as the first provider.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17668.md")</div>
<p>Each Chat SDK thread maps to its own Think sub-agent by default, so group chats and direct messages do not share memory. Multiple bots, custom conversation routing, and custom providers are all supported.</p>
<h4 id="2026-06-02-agents-sdk-v0.14.0-scheduled-tasks">Scheduled tasks</h4>
<p>Declare recurring, timezone-aware prompts and handlers with a typed domain-specific language (DSL). Think reconciles the declarations on startup and re-arms the next occurrence after each run, backed by durable idempotent submissions.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17669.md")</div>
<h4 id="2026-06-02-agents-sdk-v0.14.0-think-workflows">Think Workflows</h4>
<p>Run a model-driven reasoning step inside a Cloudflare Workflow with <code>ThinkWorkflow</code> and <code>step.prompt()</code>, with durable typed structured output, long waits, and approval gates.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17670.md")</div>
<h4 id="2026-06-02-agents-sdk-v0.14.0-production-hardening-for-durable-chat-recovery">Production hardening for durable chat recovery</h4>
<p>Durable chat turns have always been designed to survive a mid-turn deploy or Durable Object eviction. This release is a major hardening pass on that machinery for production.</p>
<ul>
<li><strong>Better recovery during deploys.</strong> Turns now ride through continuous deploys and evictions without losing completed work or re-running tools that already ran.</li>
<li><strong>A live &quot;recovering…&quot; signal.</strong> <code>useAgentChat</code> exposes a new <code>isRecovering</code> flag, so a recovering turn shows progress instead of looking frozen. Most UIs render <code>isStreaming || isRecovering</code> as &quot;busy&quot;.</li>
<li><strong>Stalled streams recover.</strong> Set <code>chatStreamStallTimeoutMs</code> to route a hung provider stream into the same recovery path instead of leaving an infinite spinner.</li>
<li><strong>Sub-agents re-attach.</strong> On parent recovery, an in-flight <code>agentTool()</code> child is re-attached to its result rather than abandoned and re-run, so long-running children no longer lose work under deploys.</li>
</ul>
<h4 id="2026-06-02-agents-sdk-v0.14.0-mcp-transport-improvements">MCP transport improvements</h4>
<ul>
<li><strong>Resumable streams</strong> — In-flight tool calls over Server-Sent Events (SSE) survive a dropped connection. Clients reconnect with <code>Last-Event-ID</code> and replay anything they missed.</li>
<li><strong>Readable server IDs</strong> — <code>addMcpServer</code> accepts an optional <code>id</code>, so tools surface as readable keys (for example <code>tool_github_create_pull_request</code>) instead of opaque connection IDs.</li>
<li><strong>Better handling of concurrent requests</strong> — Overlapping JSON-RPC requests are now correctly correlated to their responses across the HTTP and RPC transports.</li>
</ul>
<h4 id="2026-06-02-agents-sdk-v0.14.0-other-improvements">Other improvements</h4>
<ul>
<li><strong>Compaction</strong> — A <code>Session</code>'s <code>tokenCounter</code> now also drives the compaction boundary decision (&quot;what to compress&quot;), not just the fire/no-fire trigger.</li>
<li><strong><code>@cloudflare/worker-bundler</code></strong> — Adds a <code>virtualModules</code> option to <code>createWorker</code> to provide in-memory module source during bundling.</li>
<li><strong>Client-tool continuations</strong> — Parallel tool results now coalesce into a single continuation, immediate resume requests attach to the pending continuation, and server-side <code>needsApproval</code> continuations resume reliably after approval.</li>
</ul>
<h4 id="2026-06-02-agents-sdk-v0.14.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/runtime/">Agents API reference</a> and <a href="/agents/communication-channels/chat/chat-agents/">Chat agents documentation</a> for more information.</p>


<h2 id="share-sandbox-previews-through-cloudflare-tunnel"><a href="/changelog/post/2026-05-29-sandbox-named-tunnels/">Share sandbox previews through Cloudflare Tunnel</a></h2>
<p><em>2026-05-29</em></p>
<p><a href="/sandbox/">Sandboxes</a> can expose a service running inside the container on a public preview URL through the <code>sandbox.tunnels</code> namespace. The SDK uses <code>cloudflared</code> inside the sandbox so you can share a running service without configuring <code>exposePort()</code> or a custom domain.</p>
<p>By default, <code>sandbox.tunnels.get(port)</code> creates a <a href="https://try.cloudflare.com/">quick tunnel</a> on a zero-config <code>*.trycloudflare.com</code> URL — no Cloudflare account, DNS record, or custom domain required. This is perfect for quick development and for <code>.workers.dev</code> deployments.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17665.md")</div>
<h4 id="2026-05-29-sandbox-named-tunnels-named-tunnels">Named tunnels</h4>
<p>For more control you can create a named tunnel through <code>sandbox.tunnels.get(port, { name })</code>. A named tunnel binds a hostname (<code>&lt;name&gt;.&lt;your-zone&gt;</code>) backed by a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> and a CNAME record on your zone resulting in something like <a href="https://my-app-preview.example.com">https://my-app-preview.example.com</a>.</p>
<p>Unlike quick tunnels, which generate a new random URL each time, a named tunnel produces a persistent URL that survives container restarts. This makes named tunnels suitable for production use cases where you want control over the tunnel and it's origin.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17666.md")</div>
<p>Calling <code>sandbox.destroy()</code> tears down the Cloudflare Tunnel and the associated DNS record alongside the container, so you do not leave dangling tunnels or records behind.</p>
<h4 id="2026-05-29-sandbox-named-tunnels-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/sandbox@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/sandbox@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/sandbox@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/sandbox@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/sandbox@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/sandbox@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/sandbox@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/sandbox@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For full API details, refer to the <a href="/sandbox/api/tunnels/">Sandbox tunnels reference</a>.</p>


<h2 id="use-browser-run-quick-actions-directly-from-workers"><a href="/changelog/post/2026-05-28-use-browser-run-quick-actions-directly-from-workers/">Use Browser Run Quick Actions directly from Workers</a></h2>
<p><em>2026-05-28</em></p>
<p>You can now call <a href="/browser-run/quick-actions/">Browser Run Quick Actions</a> directly from a <a href="/workers/">Cloudflare Worker</a> using the <code>quickAction()</code> method on the browser binding. This simplifies how Workers interact with Browser Run by removing the need for API tokens or external HTTP requests. Your Worker communicates with Browser Run directly over Cloudflare's network, resulting in simpler code and lower latency.</p>
<p>With the <code>quickAction()</code> method you can:</p>
<ul>
<li><a href="/browser-run/quick-actions/screenshot-endpoint/">Capture screenshots</a> from URLs or HTML</li>
<li><a href="/browser-run/quick-actions/pdf-endpoint/">Generate PDFs</a> with custom styling, headers, and footers</li>
<li><a href="/browser-run/quick-actions/content-endpoint/">Extract HTML content</a> from fully rendered pages</li>
<li><a href="/browser-run/quick-actions/markdown-endpoint/">Convert pages to Markdown</a></li>
<li><a href="/browser-run/quick-actions/json-endpoint/">Extract structured JSON</a> using AI</li>
<li><a href="/browser-run/quick-actions/scrape-endpoint/">Scrape elements</a> with CSS selectors</li>
<li><a href="/browser-run/quick-actions/links-endpoint/">Get all links</a> from a page</li>
<li><a href="/browser-run/quick-actions/snapshot/">Capture snapshots</a> (HTML + screenshot in one request)</li>
</ul>
<p>To get started, add a browser binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17694.md")</div>
<p>Then call any Quick Action directly from your Worker. For example, to capture a screenshot:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17695.md")</div>
<p>The <code>quickAction()</code> method requires a compatibility date of <code>2026-03-24</code> or later.</p>
<p>For setup instructions and the full list of available actions, refer to <a href="/browser-run/quick-actions/">Browser Run Quick Actions</a>.</p>


<h2 id="call-any-ai-model-through-ai-gateway-s-new-rest-api"><a href="/changelog/post/2026-05-21-rest-api/">Call any AI model through AI Gateway's new REST API</a></h2>
<p><em>2026-05-21</em></p>
<p>AI Gateway now uses the AI REST API on <code>api.cloudflare.com</code>. You can call any model — whether from OpenAI, Anthropic, Google, or hosted on Workers AI — through one unified API, using the same endpoints and authentication regardless of provider. Four endpoints are available:</p>
<ul>
<li><code>POST /ai/run</code> — universal endpoint for all models and modalities</li>
<li><code>POST /ai/v1/chat/completions</code> — OpenAI SDK compatible</li>
<li><code>POST /ai/v1/responses</code> — OpenAI Responses API compatible</li>
<li><code>POST /ai/v1/messages</code> — Anthropic SDK compatible</li>
</ul>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-5.5&quot;,&#10;    &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What is Cloudflare?&quot;}]&#10;  }&#x27;&#10;</code></pre>
<p>All AI Gateway features — logging, caching, rate limiting, and guardrails — are applied automatically. Third-party models are billed through <a href="/ai-gateway/features/unified-billing/">Unified Billing</a>, so you do not need to manage separate provider API keys.</p>
<p>Third-party model requests are routed through your account's default gateway, which is created automatically on first use. To route requests through a specific gateway, add the <code>cf-aig-gateway-id</code> header.</p>
<p>If you are already calling Workers AI models through the existing REST API, that path (<code>/ai/run/@cf/{model}</code>) continues to work. To call Workers AI models through AI Gateway, use the <code>@cf/</code> model prefix (for example, <code>@cf/moonshotai/kimi-k2.6</code>) and include the <code>cf-aig-gateway-id</code> header to specify which gateway to route through.</p>
<p>For more details and examples, refer to the <a href="/ai-gateway/usage/rest-api/">REST API documentation</a>.</p>


<h2 id="agents-sdk-v0-12-4-chat-recovery-routing-retries-durable-think-submissions-and-voice-connection-control"><a href="/changelog/post/2026-05-13-agents-sdk-v0.12.4/">Agents SDK v0.12.4: chat recovery, routing retries, durable Think submissions, and Voice connection control</a></h2>
<p><em>2026-05-13</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> brings more reliable chat recovery, fixes Agent state synchronization during reconnects, adds durable submissions for Think, exposes routing retry configuration, and adds connection control for Voice agents.</p>
<h4 id="2026-05-13-agents-sdk-v0.12.4-chat-recovery-improvements">Chat recovery improvements</h4>
<p><code>@cloudflare/ai-chat</code> now keeps server turns running when a browser or client stream is interrupted. This is useful for long-running AI responses where users refresh the page, close a tab, or temporarily lose connection. Calling <code>stop()</code> still cancels the server turn.</p>
<p>Set <code>cancelOnClientAbort: true</code> if browser or client aborts should also cancel the server turn:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17661.md")</div>
<p>Notable bug fixes:</p>
<ul>
<li>Chat stream resume negotiation no longer throws when replay races with a closed WebSocket connection.</li>
<li>Recovered chat continuations no longer leave <code>useAgentChat</code> stuck in a streaming state when the original socket disconnects before a terminal response.</li>
<li>Approval auto-continuation preserves reasoning parts and persists continuation reasoning in the final message.</li>
<li><code>isServerStreaming</code> now resets correctly when a resumed stream moves from the fallback observer path to a transport-owned stream.</li>
</ul>
<h4 id="2026-05-13-agents-sdk-v0.12.4-agent-state-and-routing-fixes">Agent state and routing fixes</h4>
<p><code>agents@0.12.4</code> prevents duplicate initial state frames during WebSocket connection setup. This avoids stale initial state messages overwriting state updates already sent by the client.</p>
<p>Agent recovery is also more reliable when tool calls span a Durable Object restart. Recovery now defers user finish hooks until after agent startup and isolates hook failures, so one failed hook does not block other recovered runs from finalizing.</p>
<p><code>getAgentByName()</code> now supports <code>routingRetry</code> for transient Durable Object routing failures:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17662.md")</div>
<h4 id="2026-05-13-agents-sdk-v0.12.4-durable-think-submissions">Durable Think submissions</h4>
<p><code>@cloudflare/think</code> now supports durable programmatic submissions. <code>submitMessages()</code> provides durable acceptance, idempotent retries, status inspection, cancellation, and cleanup for server-driven turns that should continue after the caller returns.</p>
<p><code>Think.chat()</code> RPC turns now run inside chat recovery fibers and persist their stream chunks. Interrupted sub-agent turns can recover partial output instead of starting over.</p>
<p><code>ChatOptions.tools</code> has been removed from the TypeScript API. Define durable tools on the child agent or use agent tools for orchestration. Runtime <code>options.tools</code> values passed by legacy callers are ignored with a warning.</p>
<h4 id="2026-05-13-agents-sdk-v0.12.4-think-message-pruning-behavior-change">Think message pruning behavior change</h4>
<p><code>@cloudflare/think</code> no longer applies <code>pruneMessages({ toolCalls: &quot;before-last-2-messages&quot; })</code> to model context by default. The previous default could strip client-side tool results from longer multi-turn flows.</p>
<p><code>truncateOlderMessages</code> still runs as before, so context cost remains bounded. Subclasses that relied on the old aggressive pruning can opt back in from <code>beforeTurn</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17663.md")</div>
<h4 id="2026-05-13-agents-sdk-v0.12.4-voice-agent-connection-control">Voice agent connection control</h4>
<p><code>@cloudflare/voice</code> adds an <code>enabled</code> option to <code>useVoiceAgent</code>. React apps can now delay creating and connecting a <code>VoiceClient</code> until prerequisites such as capability tokens are ready.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17664.md")</div>
<p>This release also fixes Workers AI speech-to-text session edge cases and <code>withVoice</code> text streaming from AI SDK <code>textStream</code> responses.</p>
<h4 id="2026-05-13-agents-sdk-v0.12.4-other-improvements">Other improvements</h4>
<ul>
<li><strong>Streamable HTTP routing</strong> — Server-to-client requests now route through the originating POST stream when no standalone SSE stream is available.</li>
<li><strong>Structured tool output</strong> — Tool output shapes are preserved when truncating older messages or oversized persisted rows.</li>
<li><strong>Non-chat Think tool steps</strong> — Think agent-tool children can complete without emitting assistant text and can return structured output through <code>getAgentToolOutput</code>.</li>
<li><strong>Sub-agent schedules</strong> — Stale sub-agent schedule rows are pruned when their owning facet registry entry no longer exists.</li>
<li><strong><code>@cloudflare/codemode</code></strong> — Adds a browser-safe export with an iframe sandbox executor and resolves OpenAPI specs inside the sandbox to avoid Worker Loader RPC size limits.</li>
</ul>
<h4 id="2026-05-13-agents-sdk-v0.12.4-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest @cloudflare/think@latest @cloudflare/voice@latest&#10;</code></pre>
<p>Refer to the <a href="/agents/runtime/">Agents API reference</a> and <a href="/agents/communication-channels/chat/chat-agents/">Chat agents documentation</a> for more information.</p>


<h2 id="planned-model-deprecations-on-workers-ai"><a href="/changelog/post/2026-05-08-planned-model-deprecations/">Planned model deprecations on Workers AI</a></h2>
<p><em>2026-05-08</em></p>
<p>We are refreshing the Workers AI model catalog to make room for newer releases. Please update your apps to remove references to the models listed below before the deprecation date.</p>
<h4 id="2026-05-08-planned-model-deprecations-recommended-replacements">Recommended replacements</h4>
<ul>
<li><a href="/workers-ai/models/glm-4.7-flash/"><code>@cf/zai-org/glm-4.7-flash</code></a> — fast multilingual model with multi-turn tool calling and coding capabilities.</li>
<li><a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>@cf/google/gemma-4-26b-a4b-it</code></a> — efficient open model with vision and tool calling.</li>
<li><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a> — capable tool-calling and vision model for agentic workloads and coding.</li>
</ul>
<p>For pricing, refer to the <a href="/workers-ai/platform/pricing/">Workers AI pricing page</a>.</p>
<h4 id="2026-05-08-planned-model-deprecations-kimi-k2-5">Kimi K2.5</h4>
<p>We originally stated Kimi K2.5 would be deprecated on May 10, 2026, however we have extended the deprecation date to May 30, 2026. Requests will be automatically aliased to Kimi K2.6 on May 30, 2026, which has a higher price. Please review the <a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a> pricing and model capabilities prior to May 30, 2026 to ensure that the model suits your needs.</p>
<h4 id="2026-05-08-planned-model-deprecations-models-deprecated-on-may-30-2026">Models deprecated on May 30, 2026</h4>
<ul>
<li><code>@cf/moonshotai/kimi-k2.5</code> --&gt; <code>@cf/moonshotai/kimi-k2.6</code></li>
<li><code>@hf/meta-llama/meta-llama-3-8b-instruct</code></li>
<li><code>@cf/meta/llama-3-8b-instruct</code></li>
<li><code>@cf/meta/llama-3-8b-instruct-awq</code></li>
<li><code>@cf/meta/llama-3.1-8b-instruct</code></li>
<li><code>@cf/meta/llama-3.1-8b-instruct-awq</code></li>
<li><code>@cf/meta/llama-3.1-70b-instruct</code></li>
<li><code>@cf/meta/llama-2-7b-chat-int8</code></li>
<li><code>@cf/meta/llama-2-7b-chat-fp16</code></li>
<li><code>@cf/mistral/mistral-7b-instruct-v0.1</code></li>
<li><code>@hf/mistral/mistral-7b-instruct-v0.2</code></li>
<li><code>@hf/google/gemma-7b-it</code></li>
<li><code>@cf/google/gemma-3-12b-it</code></li>
<li><code>@hf/nousresearch/hermes-2-pro-mistral-7b</code></li>
<li><code>@cf/microsoft/phi-2</code></li>
<li><code>@cf/defog/sqlcoder-7b-2</code></li>
<li><code>@cf/unum/uform-gen2-qwen-500m</code></li>
<li><code>@cf/facebook/bart-large-cnn</code></li>
</ul>
<h4 id="2026-05-08-planned-model-deprecations-variants-that-remain-active">Variants that remain active</h4>
<p>The <code>-fast</code> and <code>-lora</code> variants of models will remain active, including:</p>
<ul>
<li><code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code></li>
<li><code>@cf/meta/llama-3.1-8b-instruct-fast</code></li>
<li><code>@cf/google/gemma-7b-it-lora</code></li>
<li><code>@cf/google/gemma-2b-it-lora</code></li>
<li><code>@cf/mistral/mistral-7b-instruct-v0.2-lora</code></li>
<li><code>@cf/meta-llama/llama-2-7b-chat-hf-lora</code></li>
</ul>
<p>LoRA models may be deprecated in the future. We will be adding more LoRA capabilities to the catalog, and will communicate when new LoRA models come online to give users time to train new LoRAs before we deprecate old ones.</p>
<p>For the full list of available models, refer to the <a href="/workers-ai/models/">Workers AI model catalog</a>.</p>


<h2 id="moonshot-ai-kimi-k2-6-now-available-on-workers-ai"><a href="/changelog/post/2026-04-20-kimi-k2-6-workers-ai/">Moonshot AI Kimi K2.6 now available on Workers AI</a></h2>
<p><em>2026-04-20</em></p>
<p><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a> is now available on Workers AI, in partnership with Moonshot AI for Day 0 support. Kimi K2.6 is a native multimodal agentic model from Moonshot AI that advances practical capabilities in long-horizon coding, coding-driven design, proactive autonomous execution, and swarm-based task orchestration.</p>
<p>Built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token, Kimi K2.6 delivers frontier-scale intelligence with efficient inference. It scores competitively against GPT-5.4 and Claude Opus 4.6 on agentic and coding benchmarks, including BrowseComp (83.2), SWE-Bench Verified (80.2), and Terminal-Bench 2.0 (66.7).</p>
<h4 id="2026-04-20-kimi-k2-6-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>262.1k token context window</strong> for retaining full conversation history, tool definitions, and codebases across long-running agent sessions</li>
<li><strong>Long-horizon coding</strong> with significant improvements on complex, end-to-end coding tasks across languages including Rust, Go, and Python</li>
<li><strong>Coding-driven design</strong> that transforms simple prompts and visual inputs into production-ready interfaces and full-stack workflows</li>
<li><strong>Agent swarm orchestration</strong> scaling horizontally to 300 sub-agents executing 4,000 coordinated steps for complex autonomous tasks</li>
<li><strong>Vision inputs</strong> for processing images alongside text</li>
<li><strong>Thinking mode</strong> with configurable reasoning depth</li>
<li><strong>Multi-turn tool calling</strong> for building agents that invoke tools across multiple conversation turns</li>
</ul>
<h4 id="2026-04-20-kimi-k2-6-workers-ai-differences-from-kimi-k2-5">Differences from Kimi K2.5</h4>
<p>If you are migrating from Kimi K2.5, note the following API changes:</p>
<ul>
<li>K2.6 uses <code>chat_template_kwargs.thinking</code> to control reasoning, replacing <code>chat_template_kwargs.enable_thinking</code></li>
<li>K2.6 returns reasoning content in the <code>reasoning</code> field, replacing <code>reasoning_content</code></li>
</ul>
<h4 id="2026-04-20-kimi-k2-6-workers-ai-get-started">Get started</h4>
<p>Use Kimi K2.6 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/ai/run</code>, or the OpenAI-compatible endpoint at <code>/v1/chat/completions</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with any of these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/kimi-k2.6/">Kimi K2.6 model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="introducing-redirects-for-ai-training"><a href="/changelog/post/2026-04-17-redirects-for-ai-training/">Introducing Redirects for AI Training</a></h2>
<p><em>2026-04-17</em></p>
<p>Cloudflare's network now supports redirecting verified AI training crawlers to canonical URLs when they request deprecated or duplicate pages. When enabled via <strong>AI Crawl Control</strong> &gt; <strong>Quick Actions</strong>, AI training crawlers that request a page with a canonical tag pointing elsewhere receive a 301 redirect to the canonical version. Humans, search engine crawlers, and AI Search agents continue to see the original page normally.</p>
<p>This feature leverages your existing <code>&lt;link rel=&quot;canonical&quot;&gt;</code> tags. No additional configuration required beyond enabling the toggle. Available on Pro, Business, and Enterprise plans at no additional cost.</p>
<p>Refer to the <a href="/ai-crawl-control/reference/redirects-for-ai-training/">Redirects for AI Training documentation</a> for details.</p>


<h2 id="tools-to-prepare-your-site-for-the-agentic-internet"><a href="/changelog/post/2026-04-17-tools-for-agentic-internet/">Tools to prepare your site for the agentic Internet</a></h2>
<p><em>2026-04-17</em></p>
<p>AI Crawl Control now includes new tools to help you prepare your site for the agentic Internet—a web where AI agents are first-class citizens that discover and interact with content differently than human visitors.</p>
<h4 id="2026-04-17-tools-for-agentic-internet-content-format-insights">Content Format insights</h4>
<p>The <strong>Metrics</strong> tab now includes a <strong>Content Format</strong> chart showing what content types AI systems request versus what your origin serves. Understanding these patterns helps you optimize content delivery for both human and agent consumption.</p>
<h4 id="2026-04-17-tools-for-agentic-internet-directives-tab-formerly-robots-txt">Directives tab (formerly Robots.txt)</h4>
<p>The <strong>Robots.txt</strong> tab has been renamed to <strong>Directives</strong> and now includes a link to check your site's <a href="https://isitagentready.com">Agent Readiness</a> score.</p>
<p>Refer to our <a href="https://blog.cloudflare.com/agent-readiness/">blog post on preparing for the agentic Internet</a> for more on why these capabilities matter.</p>


<h2 id="ai-search-instances-now-include-built-in-storage-and-namespace-workers-bindings"><a href="/changelog/post/2026-04-16-ai-search-namespace-binding/">AI Search instances now include built-in storage and namespace Workers Bindings</a></h2>
<p><em>2026-04-16T12:00:00+00:00</em></p>
<p>New <a href="/ai-search/">AI Search</a> instances created after today will work differently. New instances come with built-in storage and a vector index, so you can upload a file, have it indexed immediately, and search it right away.</p>
<p>Additionally new Workers Bindings are now available to use with AI Search. The new namespace binding lets you create and manage instances at runtime, and cross-instance search API lets you query across multiple instances in one call.</p>
<h4 id="2026-04-16-ai-search-namespace-binding-built-in-storage-and-vector-index">Built-in storage and vector index</h4>
<p>All new instances now comes with built-in storage which allows you to upload files directly to it using the <a href="/ai-search/api/items/workers-binding/">Items API</a> or the dashboard. No R2 buckets to set up, no external data sources to connect first.</p>
<pre tabindex="0"><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;// upload and wait for indexing to complete&#10;const item = await instance.items.uploadAndPoll(&quot;faq.md&quot;, content);&#10;&#10;// search immediately after indexing&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;onboarding guide&quot; }],&#10;});&#10;</code></pre>
<h4 id="2026-04-16-ai-search-namespace-binding-namespace-binding">Namespace binding</h4>
<p>The new <code>ai_search_namespaces</code> binding replaces the previous <code>env.AI.autorag()</code> API provided through the <code>AI</code> binding. It gives your Worker access to all instances within a <a href="/ai-search/concepts/namespaces/">namespace</a> and lets you create, update, and delete instances at runtime without redeploying.</p>
<pre tabindex="0"><code class="language-jsonc">// wrangler.jsonc&#10;{&#10;	&quot;ai_search_namespaces&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;AI_SEARCH&quot;,&#10;			&quot;namespace&quot;: &quot;default&quot;,&#10;		},&#10;	],&#10;}&#10;</code></pre>
<pre tabindex="0"><code class="language-ts">// create an instance at runtime&#10;const instance = await env.AI_SEARCH.create({&#10;	id: &quot;my-instance&quot;,&#10;});&#10;</code></pre>
<p>For migration details, refer to <a href="/ai-search/api/migration/workers-binding/">Workers binding migration</a>. For more on namespaces, refer to <a href="/ai-search/concepts/namespaces/">Namespaces</a>.</p>
<h4 id="2026-04-16-ai-search-namespace-binding-cross-instance-search">Cross-instance search</h4>
<p>Within the new AI Search binding, you now have access to a Search and Chat API on the namespace level. Pass an array of instance IDs and get one ranked list of results back.</p>
<pre tabindex="0"><code class="language-ts">const results = await env.AI_SEARCH.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		instance_ids: [&quot;product-docs&quot;, &quot;customer-abc123&quot;],&#10;	},&#10;});&#10;</code></pre>
<p>Refer to <a href="/ai-search/api/search/workers-binding/#namespace-level">Namespace-level search</a> for details.</p>


<h2 id="ai-search-now-has-hybrid-search-and-relevance-boosting"><a href="/changelog/post/2026-04-16-hybrid-search-and-relevance-boosting/">AI Search now has hybrid search and relevance boosting</a></h2>
<p><em>2026-04-16T12:00:00+00:00</em></p>
<p><a href="/ai-search/">AI Search</a> now supports hybrid search and relevance boosting, giving you more control over how results are found and ranked.</p>
<h4 id="2026-04-16-hybrid-search-and-relevance-boosting-hybrid-search">Hybrid search</h4>
<p>Hybrid search combines vector (semantic) search with BM25 keyword search in a single query. Vector search finds chunks with similar meaning, even when the exact words differ. Keyword search matches chunks that contain your query terms exactly. When you enable hybrid search, both run in parallel and the results are fused into a single ranked list.</p>
<p>You can configure the tokenizer (<code>porter</code> for natural language, <code>trigram</code> for code), keyword match mode (<code>and</code> for precision, <code>or</code> for recall), and fusion method (<code>rrf</code> or <code>max</code>) per instance:</p>
<pre tabindex="0"><code class="language-ts">const instance = await env.AI_SEARCH.create({&#10;	id: &quot;my-instance&quot;,&#10;	index_method: { vector: true, keyword: true },&#10;	fusion_method: &quot;rrf&quot;,&#10;	indexing_options: { keyword_tokenizer: &quot;porter&quot; },&#10;	retrieval_options: { keyword_match_mode: &quot;and&quot; },&#10;});&#10;</code></pre>
<p>Refer to <a href="/ai-search/concepts/search-modes/">Search modes</a> for an overview and <a href="/ai-search/configuration/indexing/hybrid-search/">Hybrid search</a> for configuration details.</p>
<h4 id="2026-04-16-hybrid-search-and-relevance-boosting-relevance-boosting">Relevance boosting</h4>
<p>Relevance boosting lets you nudge search rankings based on document metadata. For example, you can prioritize recent documents by boosting on <code>timestamp</code>, or surface high-priority content by boosting on a custom metadata field like <code>priority</code>.</p>
<p>Configure up to 3 boost fields per instance or override them per request:</p>
<pre tabindex="0"><code class="language-ts">const results = await env.AI_SEARCH.get(&quot;my-instance&quot;).search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;deployment guide&quot; }],&#10;	ai_search_options: {&#10;		retrieval: {&#10;			boost_by: [&#10;				{ field: &quot;timestamp&quot;, direction: &quot;desc&quot; },&#10;				{ field: &quot;priority&quot;, direction: &quot;desc&quot; },&#10;			],&#10;		},&#10;	},&#10;});&#10;</code></pre>
<p>Refer to <a href="/ai-search/configuration/retrieval/boosting/">Relevance boosting</a> for configuration details.</p>


<h2 id="browser-rendering-is-now-browser-run"><a href="/changelog/post/2026-04-15-br-rename/">Browser Rendering is now Browser Run</a></h2>
<p><em>2026-04-15T12:00:00+00:00</em></p>
<p>We are renaming Browser Rendering to <strong><a href="/browser-run/">Browser Run</a></strong>. The name Browser Rendering never fully captured what the product does. Browser Run lets you run full browser sessions on Cloudflare's global network, drive them with code or AI, record and replay sessions, crawl pages for content, debug in real time, and let humans intervene when your agent needs help.</p>
<p>Along with the rename, we have increased limits for Workers Paid plans and redesigned the Browser Run dashboard.</p>
<p>We have 4x-ed concurrency limits for Workers Paid plan users:</p>
<ul>
<li><strong>Concurrent browsers per account</strong>: 30 → <strong>120 per account</strong></li>
<li><strong>New browser instances</strong>: 30 per minute → <strong>1 per second</strong></li>
<li><strong>REST API rate limits</strong>: recently increased from <a href="/changelog/post/2026-03-04-br-rest-api-limit-increase/">3 to 10 requests per second</a></li>
</ul>
<p>Rate limits across the <a href="/browser-run/limits/">limits page</a> are now expressed in per-second terms, matching how they are enforced. No action is needed to benefit from the higher limits.</p>
<p>The <a href="https://dash.cloudflare.com/?to=/:account/workers/browser-run">redesigned dashboard</a> now shows every request in a single Runs tab, not just browser sessions but also quick actions like screenshots, PDFs, markdown, and crawls. Filter by endpoint, view target URLs, status, and duration, and expand any row for more detail.</p>
<p><img src="/images/browser-run/BRdashboardredesign.png" alt="Browser Run dashboard Runs tab with browser sessions and quick actions visible in one list, and an expanded crawl job showing its progress" /></p>
<p>We are also shipping several new features:</p>
<ul>
<li><strong><a href="/changelog/post/2026-04-15-br-observability/">Live View, Human in the Loop, and Session Recordings</a></strong> - See what your agent is doing in real time, let humans step in when automation hits a wall, and replay any session after it ends.</li>
<li><strong><a href="/changelog/post/2026-04-15-br-webmcp/">WebMCP</a></strong> - Websites can expose structured tools for AI agents to discover and call directly, replacing slow screenshot-analyze-click loops.</li>
</ul>
<p>For the full story, read our Agents Week blog <a href="https://blog.cloudflare.com/browser-run-for-ai-agents">Browser Run: Give your agents a browser</a>.</p>


<h2 id="browser-run-adds-live-view-human-in-the-loop-and-session-recordings"><a href="/changelog/post/2026-04-15-br-observability/">Browser Run adds Live View, Human in the Loop, and Session Recordings</a></h2>
<p><em>2026-04-15T11:00:00+00:00</em></p>
<p>When browser automation fails or behaves unexpectedly, it can be hard to understand what happened. We are shipping three new features in <a href="/browser-run/">Browser Run</a> (formerly Browser Rendering) to help:</p>
<ul>
<li><strong><a href="/browser-run/features/live-view/">Live View</a></strong> for real-time visibility</li>
<li><strong><a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a></strong> for human intervention</li>
<li><strong><a href="/browser-run/features/session-recording/">Session Recordings</a></strong> for replaying sessions after they end</li>
</ul>
<h4 id="2026-04-15-br-observability-live-view">Live View</h4>
<p><a href="/browser-run/features/live-view/">Live View</a> lets you see what your agent is doing in real time. The page, DOM, console, and network requests are all visible for any active browser session. Access Live View from the Cloudflare dashboard, via the hosted UI at <code>live.browser.run</code>, or using native Chrome DevTools.</p>
<h4 id="2026-04-15-br-observability-human-in-the-loop">Human in the Loop</h4>
<p>When your agent hits a snag like a login page or unexpected edge case, it can hand off to a human instead of failing. With <a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a>, a human steps into the live browser session through Live View, resolves the issue, and hands control back to the script.</p>
<p>Today, you can step in by opening the Live View URL for any active session. Next, we are adding a handoff flow where the agent can signal that it needs help, notify a human to step in, then hand control back to the agent once the issue is resolved.</p>
<p><img src="/images/browser-run/liveview.gif" alt="Browser Run Human in the Loop demo where an AI agent searches Amazon, selects a product, and requests human help when authentication is needed to buy" /></p>
<h4 id="2026-04-15-br-observability-session-recordings">Session Recordings</h4>
<p><a href="/browser-run/features/session-recording/">Session Recordings</a> records DOM state so you can replay any session after it ends. Enable recordings by passing <code>recording: true</code> when launching a browser. After the session closes, view the recording in the Cloudflare dashboard under <strong>Browser Run</strong> &gt; <strong>Runs</strong>, or retrieve via API using the session ID. Next, we are adding the ability to inspect DOM state and console output at any point during the recording.</p>
<p><img src="/images/browser-run/sessionrecording.gif" alt="Browser Run session recording showing an automated browser navigating the Sentry Shop and adding a bomber jacket to the cart" /></p>
<p>To get started, refer to the documentation for <a href="/browser-run/features/live-view/">Live View</a>, <a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a>, and <a href="/browser-run/features/session-recording/">Session Recording</a>.</p>


<h2 id="browser-run-adds-webmcp-support"><a href="/changelog/post/2026-04-15-br-webmcp/">Browser Run adds WebMCP support</a></h2>
<p><em>2026-04-15T10:00:00+00:00</em></p>
<p><a href="/browser-run/">Browser Run</a> (formerly Browser Rendering) now supports <a href="https://webmachinelearning.github.io/webmcp/">WebMCP</a> (Web Model Context Protocol), a new browser API from the Google Chrome team.</p>
<p>The Internet was built for humans, so navigating as an AI agent today is unreliable. WebMCP lets websites expose structured tools for AI agents to discover and call directly. Instead of slow screenshot-analyze-click loops, agents can call website functions like <code>searchFlights()</code> or <code>bookTicket()</code> with typed parameters, making browser automation faster, more reliable, and less fragile.</p>
<p><img src="/images/browser-run/webMCP.gif" alt="Browser Run lab session showing WebMCP tools being discovered and executed in the Chrome DevTools console to book a hotel" /></p>
<p>With WebMCP, you can:</p>
<ul>
<li><strong>Discover website tools</strong> - Use <code>navigator.modelContextTesting.listTools()</code> to see available actions on any WebMCP-enabled site</li>
<li><strong>Execute tools directly</strong> - Call <code>navigator.modelContextTesting.executeTool()</code> with typed parameters</li>
<li><strong>Handle human-in-the-loop interactions</strong> - Some tools pause for user confirmation before completing sensitive actions</li>
</ul>
<p>WebMCP requires Chrome beta features. We have an experimental pool with browser instances running Chrome beta so you can test emerging browser features before they reach stable Chrome. To start a WebMCP session, add <code>lab=true</code> to your <code>/devtools/browser</code> request:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/devtools/browser?lab=true&amp;keep_alive=300000&quot; \&#10;  &#45;H &quot;Authorization: Bearer {api_token}&quot;&#10;</code></pre>
<p>Combined with the recently launched <a href="/browser-run/cdp/">CDP endpoint</a>, AI agents can also use WebMCP. Connect an <a href="/browser-run/cdp/mcp-clients/">MCP client</a> to Browser Run via CDP, and your agent can discover and call website tools directly. Here's the same hotel booking demo, this time driven by an AI agent through OpenCode:</p>
<p><img src="/images/browser-run/webMCPagent.gif" alt="Browser Run Live View showing an AI agent navigating a hotel booking site in real time" /></p>
<p>For a step-by-step guide, refer to the <a href="/browser-run/features/webmcp/">WebMCP documentation</a>.</p>


<h2 id="agent-lee-adds-write-operations-and-generative-ui"><a href="/changelog/post/2026-04-15-agentlee-writeops-genui/">Agent Lee adds Write Operations and Generative UI</a></h2>
<p><em>2026-04-15</em></p>
<h4 id="2026-04-15-agentlee-writeops-genui-agent-lee-adds-write-operations-and-generative-ui">Agent Lee adds Write Operations and Generative UI</h4>
<p>We are excited to announce two major capability upgrades for <strong>Agent Lee</strong>, the AI co-pilot built directly into the Cloudflare dashboard. Agent Lee is designed to understand your specific account configuration, and with this release, it moves from a passive advisor to an active assistant that can help you manage your infrastructure and visualize your data through natural language.</p>
<h4 id="2026-04-15-agentlee-writeops-genui-take-action-with-write-operations">Take action with Write Operations</h4>
<p>Agent Lee can now perform changes on your behalf across your Cloudflare account. Whether you need to update DNS records, modify SSL/TLS settings, or configure Workers routes, you can simply ask.</p>
<p>To ensure security and accuracy, every write operation requires <strong>explicit user approval</strong>. Before any change is committed, Agent Lee will present a summary of the proposed action in plain language. No action is taken until you select <strong>Confirm</strong>, and this approval requirement is enforced at the infrastructure level to prevent unauthorized changes.</p>
<p><strong>Example requests:</strong></p>
<ul>
<li><em>&quot;Add an A record for blog.example.com pointing to 192.0.2.10.&quot;</em></li>
<li><em>&quot;Enable Always Use HTTPS on my zone.&quot;</em></li>
<li><em>&quot;Set the SSL mode for example.com to Full (strict).&quot;</em></li>
</ul>
<h4 id="2026-04-15-agentlee-writeops-genui-visualize-data-with-generative-ui">Visualize data with Generative UI</h4>
<p>Understanding your traffic and security trends is now as easy as asking a question. Agent Lee now features <strong>Generative UI</strong>, allowing it to render inline charts and structured data visualizations directly within the chat interface using your actual account telemetry.</p>
<p><strong>Example requests:</strong></p>
<ul>
<li><em>&quot;Show me a chart of my traffic over the last 7 days.&quot;</em></li>
<li><em>&quot;What does my error rate look like for the past 24 hours?&quot;</em></li>
<li><em>&quot;Graph my cache hit rate for example.com this week.&quot;</em></li>
</ul>
<hr />
<h4 id="2026-04-15-agentlee-writeops-genui-availability">Availability</h4>
<p>These features are currently available in <strong>Beta</strong> for all users on the <strong>Free plan</strong>. To get started, log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select <strong>Ask AI</strong> in the upper right corner.</p>
<p>To learn more about how to interact with your account using AI, refer to the <a href="/agent-lee/">Agent Lee documentation</a>.</p>


<h2 id="manage-browser-rendering-sessions-with-wrangler-cli"><a href="/changelog/post/2026-04-14-browser-wrangler-commands/">Manage Browser Rendering sessions with Wrangler CLI</a></h2>
<p><em>2026-04-14</em></p>
<p><a href="/browser-run/">Browser Rendering</a> now supports <code>wrangler browser</code> commands, letting you create, manage, and view browser sessions directly from your terminal, streamlining your workflow. Since Wrangler handles authentication, you do not need to pass API tokens in your commands.</p>
<p>The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler browser create</code></td>
<td>Create a new browser session</td>
</tr>
<tr>
<td><code>wrangler browser close</code></td>
<td>Close a session</td>
</tr>
<tr>
<td><code>wrangler browser list</code></td>
<td>List active sessions</td>
</tr>
<tr>
<td><code>wrangler browser view</code></td>
<td>View a live browser session</td>
</tr>
</tbody>
</table>
<p>The <code>create</code> command spins up a browser instance on Cloudflare's network and returns a session URL. Once created, you can connect to the session using any <a href="/browser-run/cdp/">CDP</a>-compatible client like <a href="/browser-run/cdp/puppeteer/">Puppeteer</a>, <a href="/browser-run/cdp/playwright/">Playwright</a>, or <a href="/browser-run/cdp/mcp-clients/">MCP clients</a> to automate browsing, scrape content, or debug remotely.</p>
<pre tabindex="0"><code class="language-sh">wrangler browser create&#10;</code></pre>
<p>Use <code>--keepAlive</code> to set the session keep-alive duration (60-600 seconds):</p>
<pre tabindex="0"><code class="language-sh">wrangler browser create --keepAlive 300&#10;</code></pre>
<p>The <code>view</code> command auto-selects when only one session exists, or prompts for selection when multiple sessions are available.</p>
<p>All commands support <code>--json</code> for structured output, and because these are CLI commands, you can incorporate them into scripts to automate session management.</p>
<p>For full usage details, refer to the <a href="/browser-run/reference/wrangler-commands/">Wrangler commands documentation</a>.</p>


<h2 id="secure-credential-injection-and-dynamic-egress-policies-for-sandboxes"><a href="/changelog/post/2026-04-13-sandbox-outbound-workers-tls-auth/">Secure credential injection and dynamic egress policies for Sandboxes</a></h2>
<p><em>2026-04-13</em></p>
<p>Outbound Workers for <a href="/sandbox/">Sandboxes</a> and <a href="/containers/">Containers</a> now support zero-trust credential injection, TLS interception, allow/deny lists, and dynamic per-instance egress policies. These features give platforms running agentic workloads full control over what leaves the sandbox, without exposing secrets to untrusted workloads, like user-generated code or coding agents.</p>
<h4 id="2026-04-13-sandbox-outbound-workers-tls-auth-credential-injection">Credential injection</h4>
<p>Because outbound handlers run in the Workers runtime, outside the sandbox, they can hold secrets the sandbox never sees. A sandboxed workload can make a plain request, and credentials are transparently attached before a request is forwarded upstream.</p>
<p>For instance, you could run an agent in a sandbox and ensure that any requests it makes to Github are authenticated.
But it will never be able to access the credentials:</p>
<pre tabindex="0"><code class="language-ts">export class MySandbox extends Sandbox {}&#10;&#10;MySandbox.outboundByHost = {&#10;	&quot;github.com&quot;: (request: Request, env: Env, ctx: OutboundHandlerContext) =&gt; {&#10;		const requestWithAuth = new Request(request);&#10;		requestWithAuth.headers.set(&quot;x-auth-token&quot;, env.SECRET);&#10;		return fetch(requestWithAuth);&#10;	},&#10;};&#10;</code></pre>
<p>You can easily inject unique credentials for different instances
by using <code>ctx.containerId</code>:</p>
<pre tabindex="0"><code class="language-ts">MySandbox.outboundByHost = {&#10;	&quot;my-internal-vcs.dev&quot;: async (&#10;		request: Request,&#10;		env: Env,&#10;		ctx: OutboundHandlerContext,&#10;	) =&gt; {&#10;		const authKey = await env.KEYS.get(ctx.containerId);&#10;&#10;		const requestWithAuth = new Request(request);&#10;		requestWithAuth.headers.set(&quot;x-auth-token&quot;, authKey);&#10;		return fetch(requestWithAuth);&#10;	},&#10;};&#10;</code></pre>
<p>No token is ever passed into the sandbox. You can rotate secrets in the Worker environment
and every request will pick them up immediately.</p>
<h4 id="2026-04-13-sandbox-outbound-workers-tls-auth-tls-interception">TLS interception</h4>
<p>Outbound Workers now intercept HTTPS traffic. A unique ephemeral certificate authority (CA) and private key are created for each sandbox instance. The CA is placed into the sandbox and trusted by default. The ephemeral private key never leaves the container runtime sidecar process and is never shared across instances.</p>
<p>With TLS interception active, outbound Workers can act as a transparent proxy for both HTTP and HTTPS traffic.</p>
<h4 id="2026-04-13-sandbox-outbound-workers-tls-auth-allow-and-deny-hosts">Allow and deny hosts</h4>
<p>Easily filter outbound traffic with <code>allowedHosts</code> and <code>deniedHosts</code>. When <code>allowedHosts</code> is set, it becomes a deny-by-default allowlist. Both properties support glob patterns.</p>
<pre tabindex="0"><code class="language-ts">export class MySandbox extends Sandbox {&#10;	allowedHosts = [&quot;github.com&quot;, &quot;npmjs.org&quot;];&#10;}&#10;</code></pre>
<h4 id="2026-04-13-sandbox-outbound-workers-tls-auth-dynamic-outbound-handlers">Dynamic outbound handlers</h4>
<p>Define named outbound handlers then apply or remove them at runtime using <code>setOutboundHandler()</code> or <code>setOutboundByHost()</code>. This lets you change egress policy for a running sandbox without restarting it.</p>
<pre tabindex="0"><code class="language-ts">export class MySandbox extends Sandbox {}&#10;&#10;MySandbox.outboundHandlers = {&#10;	allowHosts: async (req: Request, env: Env, ctx: OutboundHandlerContext ) =&gt; {&#10;		const url = new URL(req.url);&#10;		if (ctx.params.allowedHostnames.includes(url.hostname)) {&#10;			return fetch(req);&#10;		}&#10;		return new Response(null, { status: 403 });&#10;	},&#10;&#10;	noHttp: async () =&gt; {&#10;		return new Response(null, { status: 403 });&#10;	},&#10;};&#10;</code></pre>
<p>Apply handlers programmatically from your Worker:</p>
<pre tabindex="0"><code class="language-ts">const sandbox = getSandbox(env.Sandbox, userId);&#10;&#10;// Open network for setup&#10;await sandbox.setOutboundHandler(&quot;allowHosts&quot;, {&#10;	allowedHostnames: [&quot;github.com&quot;, &quot;npmjs.org&quot;],&#10;});&#10;await sandbox.exec(&quot;npm install&quot;);&#10;&#10;// Lock down after setup&#10;await sandbox.setOutboundHandler(&quot;noHttp&quot;);&#10;</code></pre>
<p>Handlers accept <code>params</code>, so you can customize behavior per instance without defining separate handler functions.</p>
<h4 id="2026-04-13-sandbox-outbound-workers-tls-auth-get-started">Get started</h4>
<p>Upgrade to <code>@cloudflare/containers@0.3.0</code> or <code>@cloudflare/sandbox@0.8.9</code> to use these features.</p>
<p>For more details, refer to <a href="/sandbox/guides/outbound-traffic/">Sandbox outbound traffic</a> and <a href="/containers/guides/outbound-traffic/">Container outbound traffic</a>.</p>


<h2 id="browser-rendering-adds-chrome-devtools-protocol-cdp-and-mcp-client-support"><a href="/changelog/post/2026-04-10-browser-rendering-cdp-endpoint/">Browser Rendering adds Chrome DevTools Protocol (CDP) and MCP client support</a></h2>
<p><em>2026-04-10</em></p>
<p><a href="/browser-run/">Browser Rendering</a> now exposes the <a href="/browser-run/cdp/">Chrome DevTools Protocol (CDP)</a>, the low-level protocol that powers browser automation. The growing ecosystem of CDP-based agent tools, along with existing CDP automation scripts, can now use Browser Rendering directly.</p>
<p>Any CDP-compatible client, including <a href="/browser-run/cdp/puppeteer/">Puppeteer</a> and <a href="/browser-run/cdp/playwright/">Playwright</a>, can connect from any environment, whether that is <a href="/workers/">Cloudflare Workers</a>, your local machine, or a cloud environment. All you need is your Cloudflare API key.</p>
<p>For any existing CDP script, switching to Browser Rendering is a one-line change:</p>
<pre tabindex="0"><code class="language-js">const puppeteer = require(&quot;puppeteer-core&quot;);&#10;&#10;const browser = await puppeteer.connect({&#10;	browserWSEndpoint: `wss://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/browser-rendering/devtools/browser?keep_alive=600000`,&#10;	headers: { Authorization: `Bearer ${API_TOKEN}` },&#10;});&#10;&#10;const page = await browser.newPage();&#10;await page.goto(&quot;https://example.com&quot;);&#10;console.log(await page.title());&#10;await browser.close();&#10;</code></pre>
<p>Additionally, MCP clients like Claude Desktop, Claude Code, Cursor, and OpenCode can now use Browser Rendering as their remote browser via the <a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">chrome-devtools-mcp</a> package.</p>
<p>Here is an example of how to configure Browser Rendering for Claude Desktop:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;browser-rendering&quot;: {&#10;			&quot;command&quot;: &quot;npx&quot;,&#10;			&quot;args&quot;: [&#10;				&quot;-y&quot;,&#10;				&quot;chrome-devtools-mcp@latest&quot;,&#10;				&quot;--wsEndpoint=wss://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-rendering/devtools/browser?keep_alive=600000&quot;,&#10;				&quot;--wsHeaders={\&quot;Authorization\&quot;:\&quot;Bearer &lt;API_TOKEN&gt;\&quot;}&quot;&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>To get started, refer to the <a href="/browser-run/cdp/">CDP documentation</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/ai/2/">Previous</a><span>Page 3 of 7</span><a class="pagination-next" rel="next" href="/changelog/product-group/ai/4/">Next</a></nav>
