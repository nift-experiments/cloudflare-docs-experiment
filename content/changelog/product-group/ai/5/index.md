<h1 id="changelog">Changelog</h1>

<h2 id="ai-dashboard-experience-improvements"><a href="/changelog/post/2026-02-19-ai-dashboard-experience-improvements/">AI dashboard experience improvements</a></h2>
<p><em>2026-02-19</em></p>
<p><a href="/workers-ai/">Workers AI</a> and <a href="/ai-gateway/">AI Gateway</a> have received a series of dashboard improvements to help you get started faster and manage your AI workloads more easily.</p>
<p><strong>Navigation and discoverability</strong></p>
<p>AI now has its own top-level section in the Cloudflare dashboard sidebar, so you can find AI features without digging through menus.</p>
<p><img src="/assets/upstream/images/ai-gateway/sidebar-navigation.png" alt="AI sidebar navigation in the Cloudflare dashboard" />
<em>The new top-level AI section in the dashboard sidebar.</em></p>
<p><strong>Onboarding and getting started</strong></p>
<p><a href="/ai-gateway/get-started/">Getting started</a> with AI Gateway is now simpler. When you create your first gateway, we now show your gateway's OpenAI-compatible endpoint and step-by-step guidance to help you configure it. The Playground also includes helpful prompts, and usage pages have clear next steps if you have not made any requests yet.</p>
<p><img src="/assets/upstream/images/ai-gateway/onboarding-flow.png" alt="AI Gateway onboarding flow" />
<em>The first-run setup experience for new gateways.</em></p>
<p>We've also combined the previously separate code example sections into one view with dropdown selectors for API type, provider, SDK, and authentication method so you can now customize the exact code snippet you need from one place.</p>
<p><strong>Dynamic Routing</strong></p>
<ul>
<li>The <a href="/ai-gateway/features/dynamic-routing/">route builder</a> is now more performant and responsive.</li>
<li>You can now copy route names to your clipboard with a single click.</li>
<li>Code examples use the <a href="/ai-gateway/usage/universal/">Universal Endpoint</a> format, making it easier to integrate routes into your application.</li>
</ul>
<p><strong>Observability and analytics</strong></p>
<ul>
<li>Small monetary values now display correctly in <a href="/ai-gateway/observability/costs/">cost analytics</a> charts, so you can accurately track spending at any scale.</li>
</ul>
<p><strong>Accessibility</strong></p>
<ul>
<li>Improvements to keyboard navigation within the AI Gateway, specifically when exploring usage by <a href="/ai-gateway/usage/providers/">provider</a>.</li>
<li>Improvements to sorting and filtering components on the <a href="/workers-ai/models/">Workers AI</a> models page.</li>
</ul>
<p>For more information, refer to the <a href="/ai-gateway/">AI Gateway documentation</a>.</p>


<h2 id="agents-sdk-v0-5-0-protocol-message-control-retry-utilities-data-parts-and-cloudflare-ai-chat-v0-1-0"><a href="/changelog/post/2026-02-17-agents-sdk-v0.5.0/">Agents SDK v0.5.0: Protocol message control, retry utilities, data parts, and @cloudflare/ai-chat v0.1.0</a></h2>
<p><em>2026-02-17</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> adds built-in retry utilities, per-connection protocol message control, and a fully rewritten <code>@cloudflare/ai-chat</code> with data parts, tool approval persistence, and zero breaking changes.</p>
<h4 id="2026-02-17-agents-sdk-v0.5.0-retry-utilities">Retry utilities</h4>
<p>A new <code>this.retry()</code> method lets you retry any async operation with exponential backoff and jitter. You can pass an optional <code>shouldRetry</code> predicate to bail early on non-retryable errors.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17635.md")</div>
<p>Retry options are also available per-task on <code>queue()</code>, <code>schedule()</code>, <code>scheduleEvery()</code>, and <code>addMcpServer()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17636.md")</div>
<p>Retry options are validated eagerly at enqueue/schedule time, and invalid values throw immediately. Internal retries have also been added for workflow operations (<code>terminateWorkflow</code>, <code>pauseWorkflow</code>, and others) with Durable Object-aware error detection.</p>
<h4 id="2026-02-17-agents-sdk-v0.5.0-per-connection-protocol-message-control">Per-connection protocol message control</h4>
<p>Agents automatically send JSON text frames (identity, state, MCP server lists) to every WebSocket connection. You can now suppress these per-connection for clients that cannot handle them — binary-only devices, MQTT clients, or lightweight embedded systems.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17637.md")</div>
<p>Connections with protocol messages disabled still fully participate in RPC and regular messaging. Use <code>isConnectionProtocolEnabled(connection)</code> to check a connection's status at any time. The flag persists across Durable Object hibernation.</p>
<p>See <a href="/agents/runtime/communication/protocol-messages/">Protocol messages</a> for full documentation.</p>
<h4 id="2026-02-17-agents-sdk-v0.5.0-cloudflare-ai-chat-v0-1-0"><code>@cloudflare/ai-chat</code> v0.1.0</h4>
<p>The first stable release of <code>@cloudflare/ai-chat</code> ships alongside this release with a major refactor of <code>AIChatAgent</code> internals — new <code>ResumableStream</code> class, WebSocket <code>ChatTransport</code>, and simplified SSE parsing — with zero breaking changes. Existing code using <code>AIChatAgent</code> and <code>useAgentChat</code> works as-is.</p>
<p>Key new features:</p>
<ul>
<li><strong>Data parts</strong> — Attach typed JSON blobs (<code>data-*</code>) to messages alongside text. Supports reconciliation (type+id updates in-place), append, and transient parts (ephemeral via <code>onData</code> callback). See <a href="/agents/communication-channels/chat/chat-agents/#data-parts">Data parts</a>.</li>
<li><strong>Tool approval persistence</strong> — The <code>needsApproval</code> approval UI now survives page refresh and DO hibernation. The streaming message is persisted to SQLite when a tool enters <code>approval-requested</code> state.</li>
<li><strong><code>maxPersistedMessages</code></strong> — Cap SQLite message storage with automatic oldest-message deletion.</li>
<li><strong><code>body</code> option on <code>useAgentChat</code></strong> — Send custom data with every request (static or dynamic).</li>
<li><strong>Incremental persistence</strong> — Hash-based cache to skip redundant SQL writes.</li>
<li><strong>Row size guard</strong> — Automatic two-pass compaction when messages approach the SQLite 2 MB limit.</li>
<li><strong><code>autoContinueAfterToolResult</code> defaults to <code>true</code></strong> — Client-side tool results and tool approvals now automatically trigger a server continuation, matching server-executed tool behavior. Set <code>autoContinueAfterToolResult: false</code> in <code>useAgentChat</code> to restore the previous behavior.</li>
</ul>
<p>Notable bug fixes:</p>
<ul>
<li>Resolved stream resumption race conditions</li>
<li>Resolved an issue where <code>setMessages</code> functional updater sent empty arrays</li>
<li>Resolved an issue where client tool schemas were lost after DO hibernation</li>
<li>Resolved <code>InvalidPromptError</code> after tool approval (<code>approval.id</code> was dropped)</li>
<li>Resolved an issue where message metadata was not propagated on broadcast/resume paths</li>
<li>Resolved an issue where <code>clearAll()</code> did not clear in-memory chunk buffers</li>
<li>Resolved an issue where <code>reasoning-delta</code> silently dropped data when <code>reasoning-start</code> was missed during stream resumption</li>
</ul>
<h4 id="2026-02-17-agents-sdk-v0.5.0-synchronous-queue-and-schedule-getters">Synchronous queue and schedule getters</h4>
<p><code>getQueue()</code>, <code>getQueues()</code>, <code>getSchedule()</code>, <code>dequeue()</code>, <code>dequeueAll()</code>, and <code>dequeueAllByCallback()</code> were unnecessarily <code>async</code> despite only performing synchronous SQL operations. They now return values directly instead of wrapping them in Promises. This is backward compatible — existing code using <code>await</code> on these methods will continue to work.</p>
<h4 id="2026-02-17-agents-sdk-v0.5.0-other-improvements">Other improvements</h4>
<ul>
<li><strong>Fix TypeScript &quot;excessively deep&quot; error</strong> — A depth counter on <code>CanSerialize</code> and <code>IsSerializableParam</code> types bails out to <code>true</code> after 10 levels of recursion, preventing the &quot;Type instantiation is excessively deep&quot; error with deeply nested types like AI SDK <code>CoreMessage[]</code>.</li>
<li><strong>POST SSE keepalive</strong> — The POST SSE handler now sends <code>event: ping</code> every 30 seconds to keep the connection alive, matching the existing GET SSE handler behavior. This prevents POST response streams from being silently dropped by proxies during long-running tool calls.</li>
<li><strong>Widened peer dependency ranges</strong> — Peer dependency ranges across packages have been widened to prevent cascading major bumps during 0.x minor releases. <code>@cloudflare/ai-chat</code> and <code>@cloudflare/codemode</code> are now marked as optional peer dependencies.</li>
</ul>
<h4 id="2026-02-17-agents-sdk-v0.5.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>


<h2 id="introducing-glm-4-7-flash-on-workers-ai-cloudflare-tanstack-ai-and-workers-ai-provider-v3-1-1"><a href="/changelog/post/2026-02-13-glm-4.7-flash-workers-ai/">Introducing GLM-4.7-Flash on Workers AI, @cloudflare/tanstack-ai, and workers-ai-provider v3.1.1</a></h2>
<p><em>2026-02-13</em></p>
<p>We're excited to announce <strong>GLM-4.7-Flash</strong> on Workers AI, a fast and efficient text generation model optimized for multilingual dialogue and instruction-following tasks, along with the brand-new <a href="https://www.npmjs.com/package/@cloudflare/tanstack-ai"><strong>@cloudflare/tanstack-ai</strong></a> package and <a href="https://www.npmjs.com/package/workers-ai-provider"><strong>workers-ai-provider v3.1.1</strong></a>.</p>
<p>You can now run AI agents entirely on Cloudflare. With GLM-4.7-Flash's multi-turn tool calling support, plus full compatibility with TanStack AI and the Vercel AI SDK, you have everything you need to build agentic applications that run completely at the edge.</p>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-glm-4-7-flash-multilingual-text-generation-model">GLM-4.7-Flash — Multilingual Text Generation Model</h4>
<p><a href="/workers-ai/models/glm-4.7-flash/"><code>@cf/zai-org/glm-4.7-flash</code></a> is a multilingual model with a 131,072 token context window, making it ideal for long-form content generation, complex reasoning tasks, and multilingual applications.</p>
<p><strong>Key Features and Use Cases:</strong></p>
<ul>
<li><strong>Multi-turn Tool Calling for Agents</strong>: Build AI agents that can call functions and tools across multiple conversation turns</li>
<li><strong>Multilingual Support</strong>: Built to handle content generation in multiple languages effectively</li>
<li><strong>Large Context Window</strong>: 131,072 tokens for long-form writing, complex reasoning, and processing long documents</li>
<li><strong>Fast Inference</strong>: Optimized for low-latency responses in chatbots and virtual assistants</li>
<li><strong>Instruction Following</strong>: Excellent at following complex instructions for code generation and structured tasks</li>
</ul>
<p>Use GLM-4.7-Flash through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, <a href="/ai-gateway/">AI Gateway</a>, or via <a href="/workers-ai/configuration/ai-sdk/">workers-ai-provider</a> for the Vercel AI SDK.</p>
<p>Pricing is available on the <a href="/workers-ai/models/glm-4.7-flash/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-cloudflare-tanstack-ai-v0-1-1-tanstack-ai-adapters-for-workers-ai-and-ai-gateway">@cloudflare/tanstack-ai v0.1.1 — TanStack AI adapters for Workers AI and AI Gateway</h4>
<p>We've released <code>@cloudflare/tanstack-ai</code>, a new package that brings Workers AI and AI Gateway support to <a href="https://tanstack.com/ai">TanStack AI</a>. This provides a framework-agnostic alternative for developers who prefer TanStack's approach to building AI applications.</p>
<p><strong>Workers AI adapters</strong> support four configuration modes — plain binding (<code>env.AI</code>), plain REST, AI Gateway binding (<code>env.AI.gateway(id)</code>), and AI Gateway REST — across all capabilities:</p>
<ul>
<li><strong>Chat</strong> (<code>createWorkersAiChat</code>) — Streaming chat completions with tool calling, structured output, and reasoning text streaming.</li>
<li><strong>Image generation</strong> (<code>createWorkersAiImage</code>) — Text-to-image models.</li>
<li><strong>Transcription</strong> (<code>createWorkersAiTranscription</code>) — Speech-to-text.</li>
<li><strong>Text-to-speech</strong> (<code>createWorkersAiTts</code>) — Audio generation.</li>
<li><strong>Summarization</strong> (<code>createWorkersAiSummarize</code>) — Text summarization.</li>
</ul>
<p><strong>AI Gateway adapters</strong> route requests from third-party providers — OpenAI, Anthropic, Gemini, Grok, and OpenRouter — through Cloudflare AI Gateway for caching, rate limiting, and unified billing.</p>
<p>To get started:</p>
<pre><code class="language-sh">npm install @cloudflare/tanstack-ai @tanstack/ai&#10;</code></pre>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-workers-ai-provider-v3-1-1-transcription-speech-reranking-and-reliability">workers-ai-provider v3.1.1 — transcription, speech, reranking, and reliability</h4>
<p>The Workers AI provider for the <a href="https://ai-sdk.dev">Vercel AI SDK</a> now supports three new capabilities beyond chat and image generation:</p>
<ul>
<li><strong>Transcription</strong> (<code>provider.transcription(model)</code>) — Speech-to-text with automatic handling of model-specific input formats across binding and REST paths.</li>
<li><strong>Text-to-speech</strong> (<code>provider.speech(model)</code>) — Audio generation with support for voice and speed options.</li>
<li><strong>Reranking</strong> (<code>provider.reranking(model)</code>) — Document reranking for RAG pipelines and search result ordering.</li>
</ul>
<pre><code class="language-typescript">import { createWorkersAI } from &quot;workers-ai-provider&quot;;&#10;import {&#10;	experimental_transcribe,&#10;	experimental_generateSpeech,&#10;	rerank,&#10;} from &quot;ai&quot;;&#10;&#10;const workersai = createWorkersAI({ binding: env.AI });&#10;&#10;const transcript = await experimental_transcribe({&#10;	model: workersai.transcription(&quot;@cf/openai/whisper-large-v3-turbo&quot;),&#10;	audio: audioData,&#10;	mediaType: &quot;audio/wav&quot;,&#10;});&#10;&#10;const speech = await experimental_generateSpeech({&#10;	model: workersai.speech(&quot;@cf/deepgram/aura-1&quot;),&#10;	text: &quot;Hello world&quot;,&#10;	voice: &quot;asteria&quot;,&#10;});&#10;&#10;const ranked = await rerank({&#10;	model: workersai.reranking(&quot;@cf/baai/bge-reranker-base&quot;),&#10;	query: &quot;What is machine learning?&quot;,&#10;	documents: [&quot;ML is a branch of AI.&quot;, &quot;The weather is sunny.&quot;],&#10;});&#10;</code></pre>
<p>This release also includes a comprehensive reliability overhaul (v3.0.5):</p>
<ul>
<li><strong>Fixed streaming</strong> — Responses now stream token-by-token instead of buffering all chunks, using a proper <code>TransformStream</code> pipeline with backpressure.</li>
<li><strong>Fixed tool calling</strong> — Resolved issues with tool call ID sanitization, conversation history preservation, and a heuristic that silently fell back to non-streaming mode when tools were defined.</li>
<li><strong>Premature stream termination detection</strong> — Streams that end unexpectedly now report <code>finishReason: &quot;error&quot;</code> instead of silently reporting <code>&quot;stop&quot;</code>.</li>
<li><strong>AI Search support</strong> — Added <code>createAISearch</code> as the canonical export (renamed from AutoRAG). <code>createAutoRAG</code> still works with a deprecation warning.</li>
</ul>
<p>To upgrade:</p>
<pre><code class="language-sh">npm install workers-ai-provider@latest ai&#10;</code></pre>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-resources">Resources</h4>
<ul>
<li><a href="https://www.npmjs.com/package/@cloudflare/tanstack-ai">@cloudflare/tanstack-ai on npm</a></li>
<li><a href="https://www.npmjs.com/package/workers-ai-provider">workers-ai-provider on npm</a></li>
<li><a href="https://github.com/cloudflare/ai">GitHub repository</a></li>
</ul>


<h2 id="agents-sdk-v0-4-0-readonly-connections-mcp-security-improvements-x402-v2-migration-and-custom-mcp-oauth-providers"><a href="/changelog/post/2026-02-09-agents-sdk-v0.4.0/">Agents SDK v0.4.0: Readonly connections, MCP security improvements, x402 v2 migration, and custom MCP OAuth providers</a></h2>
<p><em>2026-02-09</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> brings readonly connections, MCP protocol and security improvements, x402 payment protocol v2 migration, and the ability to customize OAuth for MCP server connections.</p>
<h4 id="2026-02-09-agents-sdk-v0.4.0-readonly-connections">Readonly connections</h4>
<p>Agents can now restrict WebSocket clients to read-only access, preventing them from modifying agent state. This is useful for dashboards, spectator views, or any scenario where clients should observe but not mutate.</p>
<p>New hooks: <code>shouldConnectionBeReadonly</code>, <code>setConnectionReadonly</code>, <code>isConnectionReadonly</code>. Readonly connections block both client-side <code>setState()</code> and mutating <code>@callable()</code> methods, and the readonly flag survives hibernation.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17630.md")</div>
<h4 id="2026-02-09-agents-sdk-v0.4.0-custom-mcp-oauth-providers">Custom MCP OAuth providers</h4>
<p>The new <code>createMcpOAuthProvider</code> method on the <code>Agent</code> class allows subclasses to override the default OAuth provider used when connecting to MCP servers. This enables custom authentication strategies such as pre-registered client credentials or mTLS, beyond the built-in dynamic client registration.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17631.md")</div>
<h4 id="2026-02-09-agents-sdk-v0.4.0-mcp-sdk-upgrade-to-1-26-0">MCP SDK upgrade to 1.26.0</h4>
<p>Upgraded the MCP SDK to 1.26.0 to prevent cross-client response leakage. Stateless MCP Servers should now create a new <code>McpServer</code> instance per request instead of sharing a single instance. A guard is added in this version of the MCP SDK which will prevent connection to a Server instance that has already been connected to a transport. Developers will need to modify their code if they declare their <code>McpServer</code> instance as a global variable.</p>
<h4 id="2026-02-09-agents-sdk-v0.4.0-mcp-oauth-callback-url-security-fix">MCP OAuth callback URL security fix</h4>
<p>Added <code>callbackPath</code> option to <code>addMcpServer</code> to prevent instance name leakage in MCP OAuth callback URLs. When <code>sendIdentityOnConnect</code> is <code>false</code>, <code>callbackPath</code> is now required — the default callback URL would expose the instance name, undermining the security intent. Also fixes callback request detection to match via the <code>state</code> parameter instead of a loose <code>/callback</code> URL substring check, enabling custom callback paths.</p>
<h4 id="2026-02-09-agents-sdk-v0.4.0-deprecate-onstateupdate-in-favor-of-onstatechanged">Deprecate <code>onStateUpdate</code> in favor of <code>onStateChanged</code></h4>
<p><code>onStateChanged</code> is a drop-in rename of <code>onStateUpdate</code> (same signature, same behavior). <code>onStateUpdate</code> still works but emits a one-time console warning per class. <code>validateStateChange</code> rejections now propagate a <code>CF_AGENT_STATE_ERROR</code> message back to the client.</p>
<h4 id="2026-02-09-agents-sdk-v0.4.0-x402-v2-migration">x402 v2 migration</h4>
<p>Migrated the x402 MCP payment integration from the legacy <code>x402</code> package to <code>@x402/core</code> and <code>@x402/evm</code> v2.</p>
<p><strong>Breaking changes for x402 users:</strong></p>
<ul>
<li>Peer dependencies changed: replace <code>x402</code> with <code>@x402/core</code> and <code>@x402/evm</code></li>
<li><code>PaymentRequirements</code> type now uses v2 fields (e.g. <code>amount</code> instead of <code>maxAmountRequired</code>)</li>
<li><code>X402ClientConfig.account</code> type changed from <code>viem.Account</code> to <code>ClientEvmSigner</code> (structurally compatible with <code>privateKeyToAccount()</code>)</li>
</ul>
<pre><code class="language-bash">npm uninstall x402&#10;npm install @x402/core @x402/evm&#10;</code></pre>
<p>Network identifiers now accept both legacy names and CAIP-2 format:</p>
<pre><code class="language-ts">// Legacy name (auto-converted)&#10;{&#10;	network: &quot;base-sepolia&quot;,&#10;}&#10;&#10;// CAIP-2 format (preferred)&#10;{&#10;	network: &quot;eip155:84532&quot;,&#10;}&#10;</code></pre>
<p><strong>Other x402 changes:</strong></p>
<ul>
<li><code>X402ClientConfig.network</code> is now optional — the client auto-selects from available payment requirements</li>
<li>Server-side lazy initialization: facilitator connection is deferred until the first paid tool invocation</li>
<li>Payment tokens support both v2 (<code>PAYMENT-SIGNATURE</code>) and v1 (<code>X-PAYMENT</code>) HTTP headers</li>
<li>Added <code>normalizeNetwork</code> export for converting legacy network names to CAIP-2 format</li>
<li>Re-exports <code>PaymentRequirements</code>, <code>PaymentRequired</code>, <code>Network</code>, <code>FacilitatorConfig</code>, and <code>ClientEvmSigner</code> from <code>agents/x402</code></li>
</ul>
<h4 id="2026-02-09-agents-sdk-v0.4.0-other-improvements">Other improvements</h4>
<ul>
<li>Fix <code>useAgent</code> and <code>AgentClient</code> crashing when using <code>basePath</code> routing</li>
<li>CORS handling delegated to partyserver's native support (simpler, more reliable)</li>
<li>Client-side <code>onStateUpdateError</code> callback for handling rejected state updates</li>
</ul>
<h4 id="2026-02-09-agents-sdk-v0.4.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i agents@latest&#10;</code></pre>


<h2 id="interactive-browser-terminals-in-sandboxes"><a href="/changelog/post/2026-02-09-pty-terminal-support/">Interactive browser terminals in Sandboxes</a></h2>
<p><em>2026-02-09</em></p>
<p>The <a href="https://github.com/cloudflare/sandbox-sdk">Sandbox SDK</a> now supports PTY (pseudo-terminal) passthrough, enabling browser-based terminal UIs to connect to sandbox shells via WebSocket.</p>
<h4 id="2026-02-09-pty-terminal-support-sandbox-terminal-request"><code>sandbox.terminal(request)</code></h4>
<p>The new <code>terminal()</code> method proxies a WebSocket upgrade to the container's PTY endpoint, with output buffering for replay on reconnect.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17632.md")</div>
<h4 id="2026-02-09-pty-terminal-support-multiple-terminals-per-sandbox">Multiple terminals per sandbox</h4>
<p>Each session can have its own terminal with an isolated working directory and environment, so users can run separate shells side-by-side in the same container.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17633.md")</div>
<h4 id="2026-02-09-pty-terminal-support-xterm-js-addon">xterm.js addon</h4>
<p>The new <code>@cloudflare/sandbox/xterm</code> export provides a <code>SandboxAddon</code> for <a href="https://xtermjs.org/">xterm.js</a> with automatic reconnection (exponential backoff + jitter), buffered output replay, and resize forwarding.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17634.md")</div>
<h4 id="2026-02-09-pty-terminal-support-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i @cloudflare/sandbox@latest&#10;</code></pre>


<h2 id="analytics-enhancements"><a href="/changelog/post/2026-02-09-analytics-enhancements/">Analytics enhancements</a></h2>
<p><em>2026-02-09</em></p>
<p>AI Crawl Control metrics have been enhanced with new views, improved filtering, and better data visualization.</p>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-path-patterns.png" alt="AI Crawl Control path patterns" /></p>
<p><strong>Path pattern grouping</strong></p>
<ul>
<li>In the <strong>Metrics</strong> tab &gt; <strong>Most popular paths</strong> table, use the new <strong>Patterns</strong> tab that groups requests by URI pattern (<code>/blog/*</code>, <code>/api/v1/*</code>, <code>/docs/*</code>) to identify which site areas crawlers target most. Refer to the screenshot above.</li>
</ul>
<p><strong>Enhanced referral analytics</strong></p>
<ul>
<li>Destination patterns show which site areas receive AI-driven referral traffic.</li>
<li>In the <strong>Metrics</strong> tab, a new <strong>Referrals over time</strong> chart shows trends by operator or source.</li>
</ul>
<p><strong>Data transfer metrics</strong></p>
<ul>
<li>In the <strong>Metrics</strong> tab &gt; <strong>Allowed requests over time</strong> chart, toggle <strong>Bytes</strong> to show bandwidth consumption.</li>
<li>In the <strong>Crawlers</strong> tab, a new <strong>Bytes Transferred</strong> column shows bandwidth per crawler.</li>
</ul>
<p><strong>Image exports</strong></p>
<ul>
<li>Export charts and tables as images for reports and presentations.</li>
</ul>
<p>Learn more about <a href="/ai-crawl-control/features/analyze-ai-traffic/">analyzing AI traffic</a>.</p>


<h2 id="ai-search-now-with-more-granular-controls-over-indexing"><a href="/changelog/post/2026-02-09-indexing-improvements/">AI Search now with more granular controls over indexing</a></h2>
<p><em>2026-02-09</em></p>
<p>Get your content updates into <a href="/ai-search/">AI Search</a> faster and avoid a full rescan when you do not need it.</p>
<h4 id="2026-02-09-indexing-improvements-reindex-individual-files-without-a-full-sync">Reindex individual files without a full sync</h4>
<p>Updated a file or need to retry one that errored? When you know exactly which file changed, you can now <a href="/ai-search/configuration/indexing/syncing/#controls">reindex it directly</a> instead of rescanning your entire data source.</p>
<p>Go to <strong>Overview</strong> &gt; <strong>Indexed Items</strong> and select the sync icon next to any file to reindex it immediately.</p>
<p><img src="/assets/upstream/images/ai-search/individual-file-indexing.png" alt="Sync individual files from Indexed Items" /></p>
<h4 id="2026-02-09-indexing-improvements-crawl-only-the-sitemap-you-need">Crawl only the sitemap you need</h4>
<p>By default, AI Search crawls all sitemaps listed in your <code>robots.txt</code>, up to the <a href="/ai-search/platform/limits-pricing/#limits">maximum files per index limit</a>. If your site has multiple sitemaps but you only want to index a specific set, you can now <a href="/ai-search/configuration/data-source/website/parse-types/#specific-sitemap">specify a single sitemap URL</a> to limit what the crawler visits.</p>
<p>For example, if your <code>robots.txt</code> lists both <code>blog-sitemap.xml</code> and <code>docs-sitemap.xml</code>, you can specify just <code>https://example.com/docs-sitemap.xml</code> to index only your documentation.</p>
<p>Configure your selection anytime in <strong>Settings</strong> &gt; <strong>Parsing options</strong> &gt; <strong>Specific sitemaps</strong>, then trigger a sync to apply the changes.</p>
<p><img src="/assets/upstream/images/ai-search/specify-sitemap.png" alt="Specify a sitemap in Parsinh options" /></p>
<p>Learn more about <a href="/ai-search/configuration/indexing/syncing/#controls">indexing controls</a> and <a href="/ai-search/configuration/data-source/website/parse-types/#specific-sitemap">website crawling configuration</a>.</p>


<h2 id="new-reference-documentation"><a href="/changelog/post/2026-02-09-reference-documentation/">New reference documentation</a></h2>
<p><em>2026-02-04</em></p>
<p>New reference documentation is now available for AI Crawl Control:</p>
<ul>
<li><strong><a href="/ai-crawl-control/reference/graphql-api/">GraphQL API reference</a></strong> — Query examples for crawler requests, top paths, referral traffic, and data transfer. Includes key filters for detection IDs, user agents, and referrer domains.</li>
<li><strong><a href="/ai-crawl-control/reference/bots/">Bot reference</a></strong> — Detection IDs and user agents for major AI crawlers from OpenAI, Anthropic, Google, Meta, and others.</li>
<li><strong><a href="/ai-crawl-control/reference/worker-templates/">Worker templates</a></strong> — Deploy the x402 Payment-Gated Proxy to monetize crawler access or charge bots while letting humans through free.</li>
</ul>


<h2 id="agents-sdk-v0-3-7-workflows-integration-synchronous-state-and-scheduleevery"><a href="/changelog/post/2026-02-03-agents-workflows-integration/">Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery()</a></h2>
<p><em>2026-02-03</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> brings first-class support for <a href="/workflows/">Cloudflare Workflows</a>, synchronous state management, and new scheduling capabilities.</p>
<h4 id="2026-02-03-agents-workflows-integration-cloudflare-workflows-integration">Cloudflare Workflows integration</h4>
<p>Agents excel at real-time communication and state management. Workflows excel at durable execution. Together, they enable powerful patterns where Agents handle WebSocket connections while Workflows handle long-running tasks, retries, and human-in-the-loop flows.</p>
<p>Use the new <code>AgentWorkflow</code> class to define workflows with typed access to your Agent:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17624.md")</div>
<p>Start workflows from your Agent with <code>runWorkflow()</code> and handle lifecycle events:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17625.md")</div>
<p>Key workflow methods on your Agent:</p>
<ul>
<li><code>runWorkflow(workflowName, params, options?)</code> — Start a workflow with optional metadata</li>
<li><code>getWorkflow(workflowId)</code> / <code>getWorkflows(criteria?)</code> — Query workflows with cursor-based pagination</li>
<li><code>approveWorkflow(workflowId)</code> / <code>rejectWorkflow(workflowId)</code> — Human-in-the-loop approval flows</li>
<li><code>pauseWorkflow()</code>, <code>resumeWorkflow()</code>, <code>terminateWorkflow()</code> — Workflow control</li>
</ul>
<h4 id="2026-02-03-agents-workflows-integration-synchronous-setstate">Synchronous setState()</h4>
<p>State updates are now synchronous with a new <code>validateStateChange()</code> validation hook:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17626.md")</div>
<h4 id="2026-02-03-agents-workflows-integration-scheduleevery-for-recurring-tasks">scheduleEvery() for recurring tasks</h4>
<p>The new <code>scheduleEvery()</code> method enables fixed-interval recurring tasks with built-in overlap prevention:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17627.md")</div>
<h4 id="2026-02-03-agents-workflows-integration-callable-system-improvements">Callable system improvements</h4>
<ul>
<li><strong>Client-side RPC timeout</strong> — Set timeouts on callable method invocations</li>
<li><strong><code>StreamingResponse.error(message)</code></strong> — Graceful stream error signaling</li>
<li><strong><code>getCallableMethods()</code></strong> — Introspection API for discovering callable methods</li>
<li><strong>Connection close handling</strong> — Pending calls are automatically rejected on disconnect</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17628.md")</div>
<h4 id="2026-02-03-agents-workflows-integration-email-and-routing-enhancements">Email and routing enhancements</h4>
<p><strong>Secure email reply routing</strong> — Email replies are now secured with HMAC-SHA256 signed headers, preventing unauthorized routing of emails to agent instances.</p>
<p><strong>Routing improvements:</strong></p>
<ul>
<li><code>basePath</code> option to bypass default URL construction for custom routing</li>
<li>Server-sent identity — Agents send <code>name</code> and <code>agent</code> type on connect</li>
<li>New <code>onIdentity</code> and <code>onIdentityChange</code> callbacks on the client</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17629.md")</div>
<h4 id="2026-02-03-agents-workflows-integration-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i agents@latest&#10;</code></pre>
<p>For the complete Workflows API reference and patterns, see <a href="/agents/runtime/execution/run-workflows/">Run Workflows</a>.</p>


<h2 id="launching-flux-2-klein-9b-on-workers-ai"><a href="/changelog/post/2026-01-28-flux-2-klein-9b-workers-ai/">Launching FLUX.2 [klein] 9B on Workers AI</a></h2>
<p><em>2026-01-28</em></p>
<p>We have partnered with Black Forest Labs (BFL) again to bring their optimized FLUX.2 [klein] 9B model to Workers AI. This distilled model offers enhanced quality compared to the 4B variant, while maintaining cost-effective pricing. With a fixed 4-step inference process, Klein 9B is ideal for rapid prototyping and real-time applications where both speed and quality matter.</p>
<p>Read the <a href="https://bfl.ai/blog">BFL blog</a> to learn more about the model itself, or try it out yourself on our <a href="https://multi-modal.ai.cloudflare.com/">multi modal playground</a>.</p>
<p>Pricing documentation is available on the <a href="/workers-ai/models/flux-2-klein-9b/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>
<h4 id="2026-01-28-flux-2-klein-9b-workers-ai-workers-ai-platform-specifics">Workers AI platform specifics</h4>
<p>The model hosted on Workers AI is optimized for speed with a <strong>fixed 4-step inference process</strong> and supports up to 4 image inputs. Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted. Like FLUX.2 [dev] and FLUX.2 [klein] 4B, this image model uses multipart form data inputs, even if you just have a prompt.</p>
<p>With the REST API, the multipart form data input looks like this:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-9b&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=a sunset at the alps&#x27; \&#10;  &#45;-form width=1024 \&#10;  &#45;-form height=1024&#10;</code></pre>
<p>With the Workers AI binding, you can use it as such:</p>
<pre><code class="language-javascript">const form = new FormData();&#10;form.append(&quot;prompt&quot;, &quot;a sunset with a dog&quot;);&#10;form.append(&quot;width&quot;, &quot;1024&quot;);&#10;form.append(&quot;height&quot;, &quot;1024&quot;);&#10;&#10;// FormData doesn&#x27;t expose its serialized body or boundary. Passing it to a&#10;// Request (or Response) constructor serializes it and generates the Content-Type&#10;// header with the boundary, which is required for the server to parse the multipart fields.&#10;const formResponse = new Response(form);&#10;const formStream = formResponse.body;&#10;const formContentType = formResponse.headers.get(&#x27;content-type&#x27;);&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-9b&quot;, {&#10;	multipart: {&#10;		body: formStream,&#10;		contentType: formContentType,&#10;	},&#10;});&#10;</code></pre>
<p>The parameters you can send to the model are detailed here:</p>
<details>
  <summary>JSON Schema for Model</summary>
**Required Parameters**
<ul>
<li><code>prompt</code> (string) - Text description of the image to generate</li>
</ul>
<p><strong>Optional Parameters</strong></p>
<ul>
<li><code>input_image_0</code> (string) - Binary image</li>
<li><code>input_image_1</code> (string) - Binary image</li>
<li><code>input_image_2</code> (string) - Binary image</li>
<li><code>input_image_3</code> (string) - Binary image</li>
<li><code>guidance</code> (float) - Guidance scale for generation. Higher values follow the prompt more closely</li>
<li><code>width</code> (integer) - Width of the image, default <code>1024</code> Range: 256-1920</li>
<li><code>height</code> (integer) - Height of the image, default <code>768</code> Range: 256-1920</li>
<li><code>seed</code> (integer) - Seed for reproducibility</li>
</ul>
<p><strong>Note:</strong> Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted.</p>
</details>
<h4 id="2026-01-28-flux-2-klein-9b-workers-ai-multi-reference-images">Multi-reference images</h4>
<p>The FLUX.2 klein-9b model supports generating images based on reference images, just like FLUX.2 [dev] and FLUX.2 [klein] 4B. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generated images. You would use it with the same multipart form data structure, with the input images in binary. The model supports up to 4 input images.</p>
<p>For the prompt, you can reference the images based on the index, like <code>take the subject of image 1 and style it like image 0</code> or even use natural language like <code>place the dog beside the woman</code>.</p>
<p>You must name the input parameter as <code>input_image_0</code>, <code>input_image_1</code>, <code>input_image_2</code>, <code>input_image_3</code> for it to work correctly. All input images must be smaller than 512x512.</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-9b&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=take the subject of image 1 and style it like image 0&#x27; \&#10;  &#45;-form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png \&#10;  &#45;-form input_image_1=@/Users/johndoe/Desktop/me.png \&#10;  &#45;-form width=1024 \&#10;  &#45;-form height=1024&#10;</code></pre>
<p>Through Workers AI Binding:</p>
<pre><code class="language-javascript">//helper function to convert ReadableStream to Blob&#10;async function streamToBlob(stream: ReadableStream, contentType: string): Promise&lt;Blob&gt; {&#10;  const reader = stream.getReader();&#10;  const chunks = [];&#10;&#10;  while (true) {&#10;    const { done, value } = await reader.read();&#10;    if (done) break;&#10;    chunks.push(value);&#10;  }&#10;&#10;  return new Blob(chunks, { type: contentType });&#10;}&#10;&#10;const image0 = await fetch(&quot;http://image-url&quot;);&#10;const image1 = await fetch(&quot;http://image-url&quot;);&#10;const form = new FormData();&#10;&#10;const image_blob0 = await streamToBlob(image0.body, &quot;image/png&quot;);&#10;const image_blob1 = await streamToBlob(image1.body, &quot;image/png&quot;);&#10;form.append(&#x27;input_image_0&#x27;, image_blob0)&#10;form.append(&#x27;input_image_1&#x27;, image_blob1)&#10;form.append(&#x27;prompt&#x27;, &#x27;take the subject of image 1 and style it like image 0&#x27;)&#10;&#10;// FormData doesn&#x27;t expose its serialized body or boundary. Passing it to a&#10;// Request (or Response) constructor serializes it and generates the Content-Type&#10;// header with the boundary, which is required for the server to parse the multipart fields.&#10;const formResponse = new Response(form);&#10;const formStream = formResponse.body;&#10;const formContentType = formResponse.headers.get(&#x27;content-type&#x27;);&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-9b&quot;, {&#10;    multipart: {&#10;        body: formStream,&#10;        contentType: formContentType&#10;    }&#10;})&#10;</code></pre>


<h2 id="vectorize-indexes-now-support-up-to-10-million-vectors"><a href="/changelog/post/2026-01-23-increased-index-capacity/">Vectorize indexes now support up to 10 million vectors</a></h2>
<p><em>2026-01-23</em></p>
<p>You can now store up to 10 million vectors in a single Vectorize index, doubling the previous limit of 5 million vectors. This enables larger-scale semantic search, recommendation systems, and retrieval-augmented generation (RAG) applications without splitting data across multiple indexes.</p>
<p>Vectorize continues to support indexes with up to 1,536 dimensions per vector at 32-bit precision. Refer to the <a href="/vectorize/platform/limits/">Vectorize limits documentation</a> for complete details.</p>


<h2 id="ai-search-path-filtering-for-website-and-r2-data-sources"><a href="/changelog/post/2026-01-20-ai-search-path-filtering/">AI Search path filtering for website and R2 data sources</a></h2>
<p><em>2026-01-20</em></p>
<p><a href="/ai-search/">AI Search</a> now includes <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a> for both <a href="/ai-search/configuration/data-source/website/#path-filtering">website</a> and <a href="/ai-search/configuration/data-source/r2/#path-filtering">R2</a> data sources. You can now control which content gets indexed by defining include and exclude rules for paths.</p>
<p>By controlling what gets indexed, you can improve the relevance and quality of your search results. You can also use path filtering to split a single data source across multiple AI Search instances for specialized search experiences.</p>
<p><img src="/assets/upstream/images/ai-search/path-filtering.png" alt="Path filtering configuration in AI Search" /></p>
<p>Path filtering uses <a href="https://github.com/micromatch/micromatch">micromatch</a> patterns, so you can use <code>*</code> to match within a directory and <code>**</code> to match across directories.</p>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Include</th>
<th>Exclude</th>
</tr>
</thead>
<tbody>
<tr>
<td>Index docs but skip drafts</td>
<td><code>**/docs/**</code></td>
<td><code>**/docs/drafts/**</code></td>
</tr>
<tr>
<td>Keep admin pages out of results</td>
<td>—</td>
<td><code>**/admin/**</code></td>
</tr>
<tr>
<td>Index only English content</td>
<td><code>**/en/**</code></td>
<td>—</td>
</tr>
</tbody>
</table>
<p>Configure path filters when creating a new instance or update them anytime from <strong>Settings</strong>. Check out <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a> to learn more.</p>


<h2 id="create-ai-search-instances-programmatically-via-rest-api"><a href="/changelog/post/2026-01-20-ai-search-simplified-api/">Create AI Search instances programmatically via REST API</a></h2>
<p><em>2026-01-20</em></p>
<p>You can now create <a href="/ai-search/">AI Search</a> instances programmatically using the <a href="/ai-search/get-started/api/">API</a>. For example, use the API to create instances for each customer in a multi-tenant application or manage AI Search alongside your other infrastructure.</p>
<p>If you have created an AI Search instance via the <a href="/ai-search/get-started/dashboard/">dashboard</a> before, you already have a <a href="/ai-search/configuration/indexing/service-api-token/">service API token</a> registered and can start creating instances programmatically right away. If not, follow the <a href="/ai-search/get-started/api/">API guide</a> to set up your first instance.</p>
<p>For example, you can now create separate search instances for each language on your website:</p>
<pre><code class="language-bash">for lang in en fr es de; do&#10;  curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/instances&quot; \&#10;    &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;    &#45;H &quot;Content-Type: application/json&quot; \&#10;    &#45;-data &#x27;{&#10;      &quot;id&quot;: &quot;docs-&#x27;&quot;$lang&quot;&#x27;&quot;,&#10;      &quot;type&quot;: &quot;web-crawler&quot;,&#10;      &quot;source&quot;: &quot;example.com&quot;,&#10;      &quot;source_params&quot;: {&#10;        &quot;path_include&quot;: [&quot;**/&#x27;&quot;$lang&quot;&#x27;/**&quot;]&#10;      }&#10;    }&#x27;&#10;done&#10;</code></pre>
<p>Refer to the <a href="/api/resources/ai_search/subresources/instances/methods/create/">REST API reference</a> for additional configuration options.</p>


<h2 id="launching-flux-2-klein-4b-on-workers-ai"><a href="/changelog/post/2026-01-15-flux-2-klein-4b-workers-ai/">Launching FLUX.2 [klein] 4B on Workers AI</a></h2>
<p><em>2026-01-15</em></p>
<p>We've partnered with Black Forest Labs (BFL) again to bring their optimized FLUX.2 [klein] 4B model to Workers AI! This distilled model offers faster generation and cost-effective pricing, while maintaining great output quality. With a fixed 4-step inference process, Klein 4B is ideal for rapid prototyping and real-time applications where speed matters.</p>
<p>Read the <a href="https://bfl.ai/blog">BFL blog</a> to learn more about the model itself, or try it out yourself on our <a href="https://multi-modal.ai.cloudflare.com/">multi modal playground</a>.</p>
<p>Pricing documentation is available on the <a href="/workers-ai/models/flux-2-klein-4b/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>
<h4 id="2026-01-15-flux-2-klein-4b-workers-ai-workers-ai-platform-specifics">Workers AI Platform specifics</h4>
<p>The model hosted on Workers AI is optimized for speed with a <strong>fixed 4-step inference process</strong> and supports up to 4 image inputs. Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted. Like FLUX.2 [dev], this image model uses multipart form data inputs, even if you just have a prompt.</p>
<p>With the REST API, the multipart form data input looks like this:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-4b&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=a sunset at the alps&#x27; \&#10;  &#45;-form width=1024 \&#10;  &#45;-form height=1024&#10;</code></pre>
<p>With the Workers AI binding, you can use it as such:</p>
<pre><code class="language-javascript">const form = new FormData();&#10;form.append(&quot;prompt&quot;, &quot;a sunset with a dog&quot;);&#10;form.append(&quot;width&quot;, &quot;1024&quot;);&#10;form.append(&quot;height&quot;, &quot;1024&quot;);&#10;&#10;// FormData doesn&#x27;t expose its serialized body or boundary. Passing it to a&#10;// Request (or Response) constructor serializes it and generates the Content-Type&#10;// header with the boundary, which is required for the server to parse the multipart fields.&#10;const formResponse = new Response(form);&#10;const formStream = formResponse.body;&#10;const formContentType = formResponse.headers.get(&#x27;content-type&#x27;);&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-4b&quot;, {&#10;	multipart: {&#10;		body: formStream,&#10;		contentType: formContentType,&#10;	},&#10;});&#10;</code></pre>
<p>The parameters you can send to the model are detailed here:</p>
<details>
  <summary>JSON Schema for Model</summary>
**Required Parameters**
<ul>
<li><code>prompt</code> (string) - Text description of the image to generate</li>
</ul>
<p><strong>Optional Parameters</strong></p>
<ul>
<li><code>input_image_0</code> (string) - Binary image</li>
<li><code>input_image_1</code> (string) - Binary image</li>
<li><code>input_image_2</code> (string) - Binary image</li>
<li><code>input_image_3</code> (string) - Binary image</li>
<li><code>guidance</code> (float) - Guidance scale for generation. Higher values follow the prompt more closely</li>
<li><code>width</code> (integer) - Width of the image, default <code>1024</code> Range: 256-1920</li>
<li><code>height</code> (integer) - Height of the image, default <code>768</code> Range: 256-1920</li>
<li><code>seed</code> (integer) - Seed for reproducibility</li>
</ul>
<p><strong>Note:</strong> Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted.</p>
</details>
<pre><code>&#10;&#35;# Multi-Reference Images&#10;&#10;The FLUX.2 klein-4b model supports generating images based on reference images, just like FLUX.2 [dev]. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generated images. You would use it with the same multipart form data structure, with the input images in binary. The model supports up to 4 input images.&#10;&#10;For the prompt, you can reference the images based on the index, like `take the subject of image 1 and style it like image 0` or even use natural language like `place the dog beside the woman`.&#10;&#10;Note: you have to name the input parameter as `input_image_0`, `input_image_1`, `input_image_2`, `input_image_3` for it to work correctly. All input images must be smaller than 512x512.&#10;</code></pre>
<p>curl --request POST <br />
--url '<a href="https://api.cloudflare.com/client/v4/accounts/%7BACCOUNT%7D/ai/run/@cf/black-forest-labs/flux-2-klein-4b">https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-4b</a>' <br />
--header 'Authorization: Bearer {TOKEN}' <br />
--header 'Content-Type: multipart/form-data' <br />
--form 'prompt=take the subject of image 1 and style it like image 0' <br />
--form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png <br />
--form input_image_1=@/Users/johndoe/Desktop/me.png <br />
--form width=1024 <br />
--form height=1024</p>
<pre><code>&#10;Through Workers AI Binding:&#10;</code></pre>
<p>//helper function to convert ReadableStream to Blob
async function streamToBlob(stream: ReadableStream, contentType: string): Promise<Blob> {
const reader = stream.getReader();
const chunks = [];</p>
<p>while (true) {
const { done, value } = await reader.read();
if (done) break;
chunks.push(value);
}</p>
<p>return new Blob(chunks, { type: contentType });
}</p>
<p>const image0 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const image1 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const form = new FormData();</p>
<p>const image_blob0 = await streamToBlob(image0.body, &quot;image/png&quot;);
const image_blob1 = await streamToBlob(image1.body, &quot;image/png&quot;);
form.append('input_image_0', image_blob0)
form.append('input_image_1', image_blob1)
form.append('prompt', 'take the subject of image 1 and style it like image 0')</p>
<p>// FormData doesn't expose its serialized body or boundary. Passing it to a
// Request (or Response) constructor serializes it and generates the Content-Type
// header with the boundary, which is required for the server to parse the multipart fields.
const formResponse = new Response(form);
const formStream = formResponse.body;
const formContentType = formResponse.headers.get('content-type');</p>
<p>const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-4b&quot;, {
multipart: {
body: formStream,
contentType: formContentType
}
})</p>
<pre><code></code></pre>


<h2 id="ai-crawl-control-read-only-role-now-available"><a href="/changelog/post/2026-01-13-ai-crawl-control-read-only-role/">AI Crawl Control Read Only role now available</a></h2>
<p><em>2026-01-13</em></p>
<p>Account administrators can now assign the <strong>AI Crawl Control Read Only</strong> role to provide read-only access to AI Crawl Control at the domain level.</p>
<p>Users with this role can view the <strong>Overview</strong>, <strong>Crawlers</strong>, <strong>Metrics</strong>, <strong>Robots.txt</strong>, and <strong>Settings</strong> tabs but cannot modify crawler actions or settings.</p>
<p>This role is specific for AI Crawl Control. You still require correct permissions to access other areas / features of the dashboard.</p>
<p>To assign, go to <strong>Manage Account</strong> &gt; <strong>Members</strong> and add a policy with the <strong>AI Crawl Control Read Only</strong> role scoped to the desired domain.</p>


<h2 id="agents-sdk-v0-3-0-workers-ai-provider-v3-0-0-and-ai-gateway-provider-v3-0-0-with-ai-sdk-v6-support"><a href="/changelog/post/2025-12-22-agents-sdk-ai-sdk-v6/">Agents SDK v0.3.0, workers-ai-provider v3.0.0, and ai-gateway-provider v3.0.0 with AI SDK v6 support</a></h2>
<p><em>2025-12-22</em></p>
<p>We've shipped a new release for the <a href="https://github.com/cloudflare/agents">Agents SDK</a> v0.3.0 bringing full compatibility with <a href="https://ai-sdk.dev/docs/introduction">AI SDK v6</a> and introducing the unified tool pattern, dynamic tool approval, and enhanced React hooks with improved tool handling.</p>
<p>This release includes improved streaming and tool support, dynamic tool approval (for &quot;human in the loop&quot; systems), enhanced React hooks with <code>onToolCall</code> callback, improved error handling for streaming responses, and seamless migration from v5 patterns.</p>
<p>This makes it ideal for building production AI chat interfaces with Cloudflare Workers AI models, agent workflows, human-in-the-loop systems, or any application requiring reliable tool execution and approval workflows.</p>
<p>Additionally, we've updated <strong>workers-ai-provider v3.0.0</strong>, the official provider for Cloudflare Workers AI models, and <strong>ai-gateway-provider v3.0.0</strong>, the provider for Cloudflare AI Gateway, to be compatible with AI SDK v6.</p>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-agents-sdk-v0-3-0">Agents SDK v0.3.0</h4>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-unified-tool-pattern">Unified Tool Pattern</h4>
<p>AI SDK v6 introduces a unified tool pattern where all tools are defined on the server using the <code>tool()</code> function. This replaces the previous client-side <code>AITool</code> pattern.</p>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-server-side-tool-definition">Server-Side Tool Definition</h4>
<pre><code class="language-ts">import { tool } from &quot;ai&quot;;&#10;import { z } from &quot;zod&quot;;&#10;&#10;// Server: Define ALL tools on the server&#10;const tools = {&#10;	// Server-executed tool&#10;	getWeather: tool({&#10;		description: &quot;Get weather for a city&quot;,&#10;		inputSchema: z.object({ city: z.string() }),&#10;		execute: async ({ city }) =&gt; fetchWeather(city)&#10;	}),&#10;&#10;	// Client-executed tool (no execute = client handles via onToolCall)&#10;	getLocation: tool({&#10;		description: &quot;Get user location from browser&quot;,&#10;		inputSchema: z.object({})&#10;		// No execute function&#10;	}),&#10;&#10;	// Tool requiring approval (dynamic based on input)&#10;	processPayment: tool({&#10;		description: &quot;Process a payment&quot;,&#10;		inputSchema: z.object({ amount: z.number() }),&#10;		needsApproval: async ({ amount }) =&gt; amount &gt; 100,&#10;		execute: async ({ amount }) =&gt; charge(amount)&#10;	})&#10;};&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-client-side-tool-handling">Client-Side Tool Handling</h4>
<pre><code class="language-ts">// Client: Handle client-side tools via onToolCall callback&#10;import { useAgentChat } from &quot;agents/ai-react&quot;;&#10;&#10;const { messages, sendMessage, addToolOutput } = useAgentChat({&#10;	agent,&#10;	onToolCall: async ({ toolCall, addToolOutput }) =&gt; {&#10;		if (toolCall.toolName === &quot;getLocation&quot;) {&#10;			const position = await new Promise((resolve, reject) =&gt; {&#10;				navigator.geolocation.getCurrentPosition(resolve, reject);&#10;			});&#10;			addToolOutput({&#10;				toolCallId: toolCall.toolCallId,&#10;				output: {&#10;					lat: position.coords.latitude,&#10;					lng: position.coords.longitude&#10;				}&#10;			});&#10;		}&#10;	}&#10;});&#10;</code></pre>
<p><strong>Key benefits of the unified tool pattern:</strong></p>
<ul>
<li><strong>Server-defined tools</strong>: All tools are defined in one place on the server</li>
<li><strong>Dynamic approval</strong>: Use <code>needsApproval</code> to conditionally require user confirmation</li>
<li><strong>Cleaner client code</strong>: Use <code>onToolCall</code> callback instead of managing tool configs</li>
<li><strong>Type safety</strong>: Full TypeScript support with proper tool typing</li>
</ul>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-useagentchat-options">useAgentChat(options)</h4>
<p>Creates a new chat interface with enhanced v6 capabilities.</p>
<pre><code class="language-ts">// Basic chat setup with onToolCall&#10;const { messages, sendMessage, addToolOutput } = useAgentChat({&#10;	agent,&#10;	onToolCall: async ({ toolCall, addToolOutput }) =&gt; {&#10;		// Handle client-side tool execution&#10;		await addToolOutput({&#10;			toolCallId: toolCall.toolCallId,&#10;			output: { result: &quot;success&quot; }&#10;		});&#10;	}&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-dynamic-tool-approval">Dynamic Tool Approval</h4>
<p>Use <code>needsApproval</code> on server tools to conditionally require user confirmation:</p>
<pre><code class="language-ts">const paymentTool = tool({&#10;	description: &quot;Process a payment&quot;,&#10;	inputSchema: z.object({&#10;		amount: z.number(),&#10;		recipient: z.string()&#10;	}),&#10;	needsApproval: async ({ amount }) =&gt; amount &gt; 1000,&#10;	execute: async ({ amount, recipient }) =&gt; {&#10;		return await processPayment(amount, recipient);&#10;	}&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-tool-confirmation-detection">Tool Confirmation Detection</h4>
<p>The <code>isToolUIPart</code> and <code>getToolName</code> functions now check both static and dynamic tool parts:</p>
<pre><code class="language-ts">import { isToolUIPart, getToolName } from &quot;ai&quot;;&#10;&#10;const pendingToolCallConfirmation = messages.some((m) =&gt;&#10;	m.parts?.some(&#10;		(part) =&gt; isToolUIPart(part) &amp;&amp; part.state === &quot;input-available&quot;,&#10;	),&#10;);&#10;&#10;// Handle tool confirmation&#10;if (pendingToolCallConfirmation) {&#10;	await addToolOutput({&#10;		toolCallId: part.toolCallId,&#10;		output: &quot;User approved the action&quot;&#10;	});&#10;}&#10;</code></pre>
<p>If you need the v5 behavior (static-only checks), use the new functions:</p>
<pre><code class="language-ts">import { isStaticToolUIPart, getStaticToolName } from &quot;ai&quot;;&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-converttomodelmessages-is-now-async">convertToModelMessages() is now async</h4>
<p>The <code>convertToModelMessages()</code> function is now asynchronous. Update all calls to await the result:</p>
<pre><code class="language-ts">import { convertToModelMessages } from &quot;ai&quot;;&#10;&#10;const result = streamText({&#10;	messages: await convertToModelMessages(this.messages),&#10;	model: openai(&quot;gpt-4o&quot;)&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-modelmessage-type">ModelMessage type</h4>
<p>The <code>CoreMessage</code> type has been removed. Use <code>ModelMessage</code> instead:</p>
<pre><code class="language-ts">import { convertToModelMessages, type ModelMessage } from &quot;ai&quot;;&#10;&#10;const modelMessages: ModelMessage[] = await convertToModelMessages(messages);&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-generateobject-mode-option-removed">generateObject mode option removed</h4>
<p>The <code>mode</code> option for <code>generateObject</code> has been removed:</p>
<pre><code class="language-ts">// Before (v5)&#10;const result = await generateObject({&#10;	mode: &quot;json&quot;,&#10;	model,&#10;	schema,&#10;	prompt&#10;});&#10;&#10;// After (v6)&#10;const result = await generateObject({&#10;	model,&#10;	schema,&#10;	prompt&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-structured-output-with-generatetext">Structured Output with generateText</h4>
<p>While <code>generateObject</code> and <code>streamObject</code> are still functional, the recommended approach is to use <code>generateText</code>/<code>streamText</code> with the <code>Output.object()</code> helper:</p>
<pre><code class="language-ts">import { generateText, Output, stepCountIs } from &quot;ai&quot;;&#10;&#10;const { output } = await generateText({&#10;	model: openai(&quot;gpt-4&quot;),&#10;	output: Output.object({&#10;		schema: z.object({ name: z.string() })&#10;	}),&#10;	stopWhen: stepCountIs(2),&#10;	prompt: &quot;Generate a name&quot;&#10;});&#10;</code></pre>
<blockquote>
<p><strong>Note</strong>: When using structured output with <code>generateText</code>, you must configure multiple steps with <code>stopWhen</code> because generating the structured output is itself a step.</p>
</blockquote>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-workers-ai-provider-v3-0-0">workers-ai-provider v3.0.0</h4>
<p>Seamless integration with Cloudflare Workers AI models through the updated workers-ai-provider v3.0.0 with AI SDK v6 support.</p>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-model-setup-with-workers-ai">Model Setup with Workers AI</h4>
<p>Use Cloudflare Workers AI models directly in your agent workflows:</p>
<pre><code class="language-ts">import { createWorkersAI } from &quot;workers-ai-provider&quot;;&#10;import { useAgentChat } from &quot;agents/ai-react&quot;;&#10;&#10;// Create Workers AI model (v3.0.0 - enhanced v6 internals)&#10;const model = createWorkersAI({&#10;	binding: env.AI,&#10;})(&quot;@cf/meta/llama-3.2-3b-instruct&quot;);&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-enhanced-file-and-image-support">Enhanced File and Image Support</h4>
<p>Workers AI models now support v6 file handling with automatic conversion:</p>
<pre><code class="language-ts">// Send images and files to Workers AI models&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [&#10;		{ type: &quot;text&quot;, text: &quot;Analyze this image:&quot; },&#10;		{&#10;			type: &quot;file&quot;,&#10;			data: imageBuffer,&#10;			mediaType: &quot;image/jpeg&quot;,&#10;		},&#10;	],&#10;});&#10;&#10;// Workers AI provider automatically converts to proper format&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-streaming-with-workers-ai">Streaming with Workers AI</h4>
<p>Enhanced streaming support with automatic warning detection:</p>
<pre><code class="language-ts">// Streaming with Workers AI models&#10;const result = await streamText({&#10;	model: createWorkersAI({ binding: env.AI })(&quot;@cf/meta/llama-3.2-3b-instruct&quot;),&#10;	messages: await convertToModelMessages(messages),&#10;	onChunk: (chunk) =&gt; {&#10;		// Enhanced streaming with warning handling&#10;		console.log(chunk);&#10;	},&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-ai-gateway-provider-v3-0-0">ai-gateway-provider v3.0.0</h4>
<p>The ai-gateway-provider v3.0.0 now supports AI SDK v6, enabling you to use Cloudflare AI Gateway with multiple AI providers including Anthropic, Azure, AWS Bedrock, Google Vertex, and Perplexity.</p>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-ai-gateway-setup">AI Gateway Setup</h4>
<p>Use Cloudflare AI Gateway to add analytics, caching, and rate limiting to your AI applications:</p>
<pre><code class="language-ts">import { createAIGateway } from &quot;ai-gateway-provider&quot;;&#10;&#10;// Create AI Gateway provider (v3.0.0 - enhanced v6 internals)&#10;const model = createAIGateway({&#10;	gatewayUrl: &quot;https://gateway.ai.cloudflare.com/v1/your-account-id/gateway&quot;,&#10;	headers: {&#10;		&quot;Authorization&quot;: `Bearer ${env.AI_GATEWAY_TOKEN}`&#10;	}&#10;})({&#10;	provider: &quot;openai&quot;,&#10;	model: &quot;gpt-4o&quot;&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-migration-from-v5">Migration from v5</h4>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-deprecated-apis">Deprecated APIs</h4>
<p>The following APIs are deprecated in favor of the unified tool pattern:</p>
<table>
<thead>
<tr>
<th>Deprecated</th>
<th>Replacement</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>AITool</code> type</td>
<td>Use AI SDK's <code>tool()</code> function on server</td>
</tr>
<tr>
<td><code>extractClientToolSchemas()</code></td>
<td>Define tools on server, no client schemas needed</td>
</tr>
<tr>
<td><code>createToolsFromClientSchemas()</code></td>
<td>Define tools on server with <code>tool()</code></td>
</tr>
<tr>
<td><code>toolsRequiringConfirmation</code> option</td>
<td>Use <code>needsApproval</code> on server tools</td>
</tr>
<tr>
<td><code>experimental_automaticToolResolution</code></td>
<td>Use <code>onToolCall</code> callback</td>
</tr>
<tr>
<td><code>tools</code> option in <code>useAgentChat</code></td>
<td>Use <code>onToolCall</code> for client-side execution</td>
</tr>
<tr>
<td><code>addToolResult()</code></td>
<td>Use <code>addToolOutput()</code></td>
</tr>
</tbody>
</table>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-breaking-changes-summary">Breaking Changes Summary</h4>
<ol>
<li><strong>Unified Tool Pattern</strong>: All tools must be defined on the server using <code>tool()</code></li>
<li><strong><code>convertToModelMessages()</code> is async</strong>: Add <code>await</code> to all calls</li>
<li><strong><code>CoreMessage</code> removed</strong>: Use <code>ModelMessage</code> instead</li>
<li><strong><code>generateObject</code> mode removed</strong>: Remove <code>mode</code> option</li>
<li><strong><code>isToolUIPart</code> behavior changed</strong>: Now checks both static and dynamic tool parts</li>
</ol>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-installation">Installation</h4>
<p>Update your dependencies to use the latest versions:</p>
<pre><code class="language-bash">npm install agents@^0.3.0 workers-ai-provider@^3.0.0 ai-gateway-provider@^3.0.0 ai@^6.0.0 @ai-sdk/react@^3.0.0 @ai-sdk/openai@^3.0.0&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-resources">Resources</h4>
<ul>
<li><a href="https://github.com/cloudflare/agents/blob/main/docs/migration-to-ai-sdk-v6.md">Migration Guide</a> - Comprehensive migration documentation from v5 to v6</li>
<li><a href="https://ai-sdk.dev/docs/migration-guides/migration-guide-6-0">AI SDK v6 Documentation</a> - Official AI SDK migration guide</li>
<li><a href="https://vercel.com/blog/ai-sdk-6">AI SDK v6 Announcement</a> - Learn about new features in v6</li>
<li><a href="https://sdk.vercel.ai/docs">AI SDK Documentation</a> - Complete AI SDK reference</li>
<li><a href="https://github.com/cloudflare/agents/issues">GitHub Issues</a> - Report bugs or request features</li>
</ul>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-feedback-welcome">Feedback Welcome</h4>
<p>We'd love your feedback! We're particularly interested in feedback on:</p>
<ul>
<li><strong>Migration experience</strong> - How smooth was the upgrade from v5 to v6?</li>
<li><strong>Unified tool pattern</strong> - How does the new server-defined tool pattern work for you?</li>
<li><strong>Dynamic tool approval</strong> - Does the <code>needsApproval</code> feature meet your needs?</li>
<li><strong>AI Gateway integration</strong> - How well does the new provider work with your setup?</li>
</ul>


<h2 id="new-ai-crawl-control-overview-tab"><a href="/changelog/post/2025-12-18-overview-tab/">New AI Crawl Control Overview tab</a></h2>
<p><em>2025-12-18</em></p>
<p>The <strong>Overview</strong> tab is now the default view in AI Crawl Control. The previous default view with controls for individual AI crawlers is available in the <strong>Crawlers</strong> tab.</p>
<h4 id="2025-12-18-overview-tab-what-s-new">What's new</h4>
<ul>
<li><strong>Executive summary</strong> — Monitor total requests, volume change, most common status code, most popular path, and high-volume activity</li>
<li><strong>Operator grouping</strong> — Track crawlers by their operating companies (OpenAI, Microsoft, Google, ByteDance, Anthropic, Meta)</li>
<li><strong>Customizable filters</strong> — Filter your snapshot by date range, crawler, operator, hostname, or path</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-overview-tab.png" alt="AI Crawl Control Overview tab showing executive summary, metrics, and crawler groups" /></p>
<h4 id="2025-12-18-overview-tab-get-started">Get started</h4>
<ol>
<li>Log in to the Cloudflare dashboard and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong>, where the <strong>Overview</strong> tab opens by default with your activity snapshot.</li>
<li>Use filters to customize your view by date range, crawler, operator, hostname, or path.</li>
<li>Navigate to the <strong>Crawlers</strong> tab to manage controls for individual crawlers.</li>
</ol>
<p>Learn more about <a href="/ai-crawl-control/features/analyze-ai-traffic/">analyzing AI traffic</a> and <a href="/ai-crawl-control/features/manage-ai-crawlers/">managing AI crawlers</a>.</p>


<h2 id="pay-per-crawl-private-beta-discovery-api-custom-pricing-and-advanced-configuration"><a href="/changelog/post/2025-12-10-pay-per-crawl-enhancements/">Pay Per Crawl (Private beta) - Discovery API, custom pricing, and advanced configuration</a></h2>
<p><em>2025-12-10</em></p>
<p>Pay Per Crawl is introducing enhancements for both AI crawler operators and site owners, focusing on programmatic discovery, flexible pricing models, and granular configuration control.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-for-ai-crawler-operators">For AI crawler operators</h4>
<h4 id="2025-12-10-pay-per-crawl-enhancements-discovery-api">Discovery API</h4>
<p>A new authenticated API endpoint allows verified crawlers to programmatically discover domains participating in Pay Per Crawl. Crawlers can use this to build optimized crawl queues, cache domain lists, and identify new participating sites. This eliminates the need to discover payable content through trial requests.</p>
<p>The API endpoint is <code>GET https://crawlers-api.ai-audit.cfdata.org/charged_zones</code> and requires Web Bot Auth authentication. Refer to <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/discover-payable-content/">Discover payable content</a> for authentication steps, request parameters, and response schema.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-payment-header-signature-requirement">Payment header signature requirement</h4>
<p>Payment headers (<code>crawler-exact-price</code> or <code>crawler-max-price</code>) must now be included in the Web Bot Auth <code>signature-input</code> header components. This security enhancement prevents payment header tampering, ensures authenticated payment intent, validates crawler identity with payment commitment, and protects against replay attacks with modified pricing. Crawlers must add their payment header to the list of signed components when <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/crawl-pages/#22-sign-your-request-with-web-bot-auth">constructing the signature-input header</a>.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-new-crawler-error-header">New <code>crawler-error</code> header</h4>
<p>Pay Per Crawl error responses now include a new <code>crawler-error</code> header with 11 specific <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/">error codes</a> for programmatic handling. Error response bodies remain unchanged for compatibility. These codes enable robust error handling, automated retry logic, and accurate spending tracking.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-for-site-owners">For site owners</h4>
<h4 id="2025-12-10-pay-per-crawl-enhancements-configure-free-pages">Configure free pages</h4>
<p>Site owners can now offer free access to specific pages like homepages, navigation, or discovery pages while charging for other content. Create a <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/#disable-pay-per-crawl-by-uri-pattern">Configuration Rule</a> in <strong>Rules</strong> &gt; <strong>Configuration Rules</strong>, set your URI pattern using wildcard, exact, or prefix matching on the <strong>URI Full</strong> field, and enable the <strong>Disable Pay Per Crawl</strong> setting. When disabled for a URI pattern, crawler requests pass through without blocking or charging.</p>
<p>Some paths are always free to crawl. These paths are: <code>/robots.txt</code>, <code>/sitemap.xml</code>, <code>/security.txt</code>, <code>/.well-known/security.txt</code>, <code>/crawlers.json</code>.</p>
<h4 id="2025-12-10-pay-per-crawl-enhancements-get-started">Get started</h4>
<p><strong>AI crawler operators</strong>: <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/discover-payable-content/">Discover payable content</a> | <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/crawl-pages/">Crawl pages</a></p>
<p><strong>Site owners</strong>: <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/">Advanced configuration</a></p>


<h2 id="agents-sdk-v0-2-24-with-resumable-streaming-mcp-improvements-and-schedule-fixes"><a href="/changelog/post/2025-11-26-agents-resumable-streaming/">Agents SDK v0.2.24 with resumable streaming, MCP improvements, and schedule fixes</a></h2>
<p><em>2025-11-26</em></p>
<p>The latest release of <a href="https://github.com/cloudflare/agents">@cloudflare/agents</a> brings resumable streaming, significant MCP client improvements, and critical fixes for schedules and Durable Object lifecycle management.</p>
<h4 id="2025-11-26-agents-resumable-streaming-resumable-streaming">Resumable streaming</h4>
<p><code>AIChatAgent</code> now supports resumable streaming, allowing clients to reconnect and continue receiving streamed responses without losing data. This is useful for:</p>
<ul>
<li>Long-running AI responses</li>
<li>Users on unreliable networks</li>
<li>Users switching between devices mid-conversation</li>
<li>Background tasks where users navigate away and return</li>
<li>Real-time collaboration where multiple clients need to stay in sync</li>
</ul>
<p>Streams are maintained across page refreshes, broken connections, and syncing across open tabs and devices.</p>
<h4 id="2025-11-26-agents-resumable-streaming-other-improvements">Other improvements</h4>
<ul>
<li>Default JSON schema validator added to MCP client</li>
<li><a href="https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/">Schedules</a> can now safely destroy the agent</li>
</ul>
<h4 id="2025-11-26-agents-resumable-streaming-mcp-client-api-improvements">MCP client API improvements</h4>
<p>The <code>MCPClientManager</code> API has been redesigned for better clarity and control:</p>
<ul>
<li><strong>New <code>registerServer()</code> method</strong>: Register MCP servers without immediately connecting</li>
<li><strong>New <code>connectToServer()</code> method</strong>: Establish connections to registered servers</li>
<li><strong>Improved reconnect logic</strong>: <code>restoreConnectionsFromStorage()</code> now properly handles failed connections</li>
</ul>
<pre><code class="language-ts">// Register a server to Agent&#10;const { id } = await this.mcp.registerServer({&#10;	name: &quot;my-server&quot;,&#10;	url: &quot;https://my-mcp-server.example.com&quot;,&#10;});&#10;&#10;// Connect when ready&#10;await this.mcp.connectToServer(id);&#10;&#10;// Discover tools, prompts and resources&#10;await this.mcp.discoverIfConnected(id);&#10;</code></pre>
<p>The SDK now includes a formalized <code>MCPConnectionState</code> enum with states: <code>idle</code>, <code>connecting</code>, <code>authenticating</code>, <code>connected</code>, <code>discovering</code>, and <code>ready</code>.</p>
<h4 id="2025-11-26-agents-resumable-streaming-enhanced-mcp-discovery">Enhanced MCP discovery</h4>
<p>MCP discovery fetches the available tools, prompts, and resources from an MCP server so your agent knows what capabilities are available. The <code>MCPClientConnection</code> class now includes a dedicated <code>discover()</code> method with improved reliability:</p>
<ul>
<li>Supports cancellation via AbortController</li>
<li>Configurable timeout (default 15s)</li>
<li>Discovery failures now throw errors immediately instead of silently continuing</li>
</ul>
<h4 id="2025-11-26-agents-resumable-streaming-bug-fixes">Bug fixes</h4>
<ul>
<li>Fixed a bug where <a href="https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/">schedules</a> meant to fire immediately with this.schedule(0, ...) or <code>this.schedule(new Date(), ...)</code> would not fire</li>
<li>Fixed an issue where schedules that took longer than 30 seconds would occasionally time out</li>
<li>Fixed SSE transport now properly forwards session IDs and request headers</li>
<li>Fixed AI SDK stream events conversion to UIMessageStreamPart</li>
</ul>
<h4 id="2025-11-26-agents-resumable-streaming-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i agents@latest&#10;</code></pre>


<h2 id="launching-flux-2-dev-on-workers-ai"><a href="/changelog/post/2025-11-25-flux-2-dev-workers-ai/">Launching FLUX.2 [dev] on Workers AI</a></h2>
<p><em>2025-11-25</em></p>
<p>We've partnered with Black Forest Labs (BFL) to bring their latest FLUX.2 [dev] model to Workers AI! This model excels in generating high-fidelity images with physical world grounding, multi-language support, and digital asset creation. You can also create specific super images with granular controls like JSON prompting.</p>
<p>Read the <a href="https://bfl.ai/flux2">BFL blog</a> to learn more about the model itself. Read our <a href="https://blog.cloudflare.com/flux-2-workers-ai">Cloudflare blog</a> to see the model in action, or try it out yourself on our <a href="https://multi-modal.ai.cloudflare.com/">multi modal playground</a>.</p>
<p>Pricing documentation is available on the <a href="/workers-ai/models/flux-2-dev/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>. Note, we expect to drop pricing in the next few days after iterating on the model performance.</p>
<h4 id="2025-11-25-flux-2-dev-workers-ai-workers-ai-platform-specifics">Workers AI Platform specifics</h4>
<p>The model hosted on Workers AI is able to support up to 4 image inputs (512x512 per input image). Note, this image model is one of the most powerful in the catalog and is expected to be slower than the other image models we currently support. One catch to look out for is that this model takes multipart form data inputs, even if you just have a prompt.</p>
<p>With the REST API, the multipart form data input looks like this:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-dev&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=a sunset at the alps&#x27; \&#10;  &#45;-form steps=25&#10;  &#45;-form width=1024&#10;  &#45;-form height=1024&#10;</code></pre>
<p>With the Workers AI binding, you can use it as such:</p>
<pre><code class="language-javascript">&#10;const form = new FormData();&#10;form.append(&#x27;prompt&#x27;, &#x27;a sunset with a dog&#x27;);&#10;form.append(&#x27;width&#x27;, &#x27;1024&#x27;);&#10;form.append(&#x27;height&#x27;, &#x27;1024&#x27;);&#10;&#10;//this dummy request is temporary hack&#10;//we&#x27;re pushing a change to address this soon&#10;const formRequest = new Request(&#x27;http://dummy&#x27;, {&#10;  method: &#x27;POST&#x27;,&#10;  body: form&#10;});&#10;const formStream = formRequest.body;&#10;const formContentType = formRequest.headers.get(&#x27;content-type&#x27;) || &#x27;multipart/form-data&#x27;;&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-dev&quot;, {&#10;  multipart: {&#10;    body: formStream,&#10;    contentType: formContentType&#10;  }&#10;});&#10;</code></pre>
<p>The parameters you can send to the model are detailed here:</p>
<details>
  <summary>JSON Schema for Model</summary>
**Required Parameters**
<ul>
<li><code>prompt</code> (string) - Text description of the image to generate</li>
</ul>
<p><strong>Optional Parameters</strong></p>
<ul>
<li><code>input_image_0</code> (string) - Binary image</li>
<li><code>input_image_1</code> (string) - Binary image</li>
<li><code>input_image_2</code> (string) - Binary image</li>
<li><code>input_image_3</code> (string) - Binary image</li>
<li><code>steps</code> (integer) - Number of inference steps. Higher values may improve quality but increase generation time</li>
<li><code>guidance</code> (float) - Guidance scale for generation. Higher values follow the prompt more closely</li>
<li><code>width</code> (integer) - Width of the image, default <code>1024</code> Range: 256-1920</li>
<li><code>height</code> (integer) - Height of the image, default <code>768</code> Range: 256-1920</li>
<li><code>seed</code> (integer) - Seed for reproducibility</li>
</ul>
</details>
<pre><code>&#10;&#35;# Multi-Reference Images&#10;&#10;The FLUX.2 model is great at generating images based on reference images. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generate images. You would use it with the same multipart form data structure, with the input images in binary.&#10;&#10;For the prompt, you can reference the images based on the index, like `take the subject of image 1 and style it like image 0` or even use natural language like `place the dog beside the woman`.&#10;&#10;Note: you have to name the input parameter as `input_image_0`, `input_image_1`, `input_image_2` for it to work correctly. All input images must be smaller than 512x512.&#10;</code></pre>
<p>curl --request POST <br />
--url '<a href="https://api.cloudflare.com/client/v4/accounts/%7BACCOUNT%7D/ai/run/@cf/black-forest-labs/flux-2-dev">https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-dev</a>' <br />
--header 'Authorization: Bearer {TOKEN}' <br />
--header 'Content-Type: multipart/form-data' <br />
--form 'prompt=take the subject of image 1 and style it like image 0' <br />
--form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png <br />
--form input_image_1=@/Users/johndoe/Desktop/me.png <br />
--form steps=25
--form width=1024
--form height=1024</p>
<pre><code>Through Workers AI Binding:&#10;</code></pre>
<p>//helper function to convert ReadableStream to Blob
async function streamToBlob(stream: ReadableStream, contentType: string): Promise<Blob> {
const reader = stream.getReader();
const chunks = [];</p>
<p>while (true) {
const { done, value } = await reader.read();
if (done) break;
chunks.push(value);
}</p>
<p>return new Blob(chunks, { type: contentType });
}</p>
<p>const image0 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const image1 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const form = new FormData();</p>
<p>const image_blob0 = await streamToBlob(image0.body, &quot;image/png&quot;);
const image_blob1 = await streamToBlob(image1.body, &quot;image/png&quot;);
form.append('input_image_0', image_blob0)
form.append('input_image_1', image_blob1)
form.append('prompt', 'take the subject of image 1and style it like image 0')</p>
<p>//this dummy request is temporary hack
//we're pushing a change to address this soon
const formRequest = new Request('<a href="http://dummy">http://dummy</a>', {
method: 'POST',
body: form
});
const formStream = formRequest.body;
const formContentType = formRequest.headers.get('content-type') || 'multipart/form-data';</p>
<p>const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-dev&quot;, {
multipart: {
body: form,
contentType: &quot;multipart/form-data&quot;
}
})</p>
<pre><code>&#10;&#35;# JSON Prompting&#10;&#10;The model supports prompting in JSON to get more granular control over images. You would pass the JSON as the value of the &#x27;prompt&#x27; field in the multipart form data. See the JSON schema below on the base parameters you can pass to the model.&#10;&#10;&lt;details&gt;&#10;  &lt;summary&gt;JSON Prompting Schema&lt;/summary&gt;&#10;</code></pre>
<p>{
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;scene&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Overall scene setting or location&quot;
},
&quot;subjects&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: {
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;type&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Type of subject (e.g., desert nomad, blacksmith, DJ, falcon)&quot;
},
&quot;description&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Physical attributes, clothing, accessories&quot;
},
&quot;pose&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Action or stance&quot;
},
&quot;position&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;foreground&quot;, &quot;midground&quot;, &quot;background&quot;],
&quot;description&quot;: &quot;Depth placement in scene&quot;
}
},
&quot;required&quot;: [&quot;type&quot;, &quot;description&quot;, &quot;pose&quot;, &quot;position&quot;]
}
},
&quot;style&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Artistic rendering style (e.g., digital painting, photorealistic, pixel art, noir sci-fi, lifestyle photo, wabi-sabi photo)&quot;
},
&quot;color_palette&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: { &quot;type&quot;: &quot;string&quot; },
&quot;minItems&quot;: 3,
&quot;maxItems&quot;: 3,
&quot;description&quot;: &quot;Exactly 3 main colors for the scene (e.g., ['navy', 'neon yellow', 'magenta'])&quot;
},
&quot;lighting&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Lighting condition and direction (e.g., fog-filtered sun, moonlight with star glints, dappled sunlight)&quot;
},
&quot;mood&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Emotional atmosphere (e.g., harsh and determined, playful and modern, peaceful and dreamy)&quot;
},
&quot;background&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Background environment details&quot;
},
&quot;composition&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [
&quot;rule of thirds&quot;,
&quot;circular arrangement&quot;,
&quot;framed by foreground&quot;,
&quot;minimalist negative space&quot;,
&quot;S-curve&quot;,
&quot;vanishing point center&quot;,
&quot;dynamic off-center&quot;,
&quot;leading leads&quot;,
&quot;golden spiral&quot;,
&quot;diagonal energy&quot;,
&quot;strong verticals&quot;,
&quot;triangular arrangement&quot;
],
&quot;description&quot;: &quot;Compositional technique&quot;
},
&quot;camera&quot;: {
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;angle&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;eye level&quot;, &quot;low angle&quot;, &quot;slightly low&quot;, &quot;bird's-eye&quot;, &quot;worm's-eye&quot;, &quot;over-the-shoulder&quot;, &quot;isometric&quot;],
&quot;description&quot;: &quot;Camera perspective&quot;
},
&quot;distance&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;close-up&quot;, &quot;medium close-up&quot;, &quot;medium shot&quot;, &quot;medium wide&quot;, &quot;wide shot&quot;, &quot;extreme wide&quot;],
&quot;description&quot;: &quot;Framing distance&quot;
},
&quot;focus&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;deep focus&quot;, &quot;macro focus&quot;, &quot;selective focus&quot;, &quot;sharp on subject&quot;, &quot;soft background&quot;],
&quot;description&quot;: &quot;Focus type&quot;
},
&quot;lens&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;14mm&quot;, &quot;24mm&quot;, &quot;35mm&quot;, &quot;50mm&quot;, &quot;70mm&quot;, &quot;85mm&quot;],
&quot;description&quot;: &quot;Focal length (wide to telephoto)&quot;
},
&quot;f-number&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Aperture (e.g., f/2.8, the smaller the number the more blurry the background)&quot;
},
&quot;ISO&quot;: {
&quot;type&quot;: &quot;number&quot;,
&quot;description&quot;: &quot;Light sensitivity value (comfortable range between 100 &amp; 6400, lower = less sensitivity)&quot;
}
}
},
&quot;effects&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: { &quot;type&quot;: &quot;string&quot; },
&quot;description&quot;: &quot;Post-processing effects (e.g., 'lens flare small', 'subtle film grain', 'soft bloom', 'god rays', 'chromatic aberration mild')&quot;
}
},
&quot;required&quot;: [&quot;scene&quot;, &quot;subjects&quot;]
}</p>
<pre><code>&lt;/details&gt;&#10;&#10;&#35;# Other features to try&#10;&#10;&#45; The model also supports the most common latin and non-latin character languages&#10;&#45; You can prompt the model with specific hex codes like `#2ECC71`&#10;&#45; Try creating digital assets like landing pages, comic strips, infographics too!&#10;&#10;&#10;</code></pre>
<h4 id="2025-11-25-flux-2-dev-workers-ai-json-prompting">JSON Prompting</h4><h4 id="2025-11-25-flux-2-dev-workers-ai-other-features-to-try">Other features to try</h4>

<h2 id="ai-search-support-for-crawling-login-protected-website-content"><a href="/changelog/post/2025-11-19-add-extra-headers-for-website-crawling/">AI Search support for crawling login protected website content</a></h2>
<p><em>2025-11-19</em></p>
<p><a href="/ai-search/">AI Search</a> now supports <a href="/ai-search/configuration/data-source/website/authentication-headers/">custom HTTP headers</a> for website crawling, solving a common problem where valuable content behind authentication or access controls could not be indexed.</p>
<p>Previously, AI Search could only crawl publicly accessible pages, leaving knowledge bases, documentation, and other protected content out of your search results. With custom headers support, you can now include authentication credentials that allow the crawler to access this protected content.</p>
<p>This is particularly useful for indexing content like:</p>
<ul>
<li><strong>Internal documentation</strong> behind corporate login systems</li>
<li><strong>Premium content</strong> that requires users to provide access to unlock</li>
<li><strong>Sites protected by Cloudflare Access</strong> using service tokens</li>
</ul>
<p>To add custom headers when creating an AI Search instance, select <strong>Parse options</strong>. In the <strong>Extra headers</strong> section, you can add up to five custom headers per Website data source.</p>
<p><img src="/assets/upstream/images/ai-search/ai-search-extra-headers.png" alt="Custom headers configuration in AI Search" /></p>
<p>For example, to crawl a site protected by <a href="/cloudflare-one/access-controls/">Cloudflare Access</a>, you can add service token credentials as custom headers:</p>
<pre><code>CF-Access-Client-Id: your-token-id.access&#10;CF-Access-Client-Secret: your-token-secret&#10;</code></pre>
<p>The crawler will automatically include these headers in all requests, allowing it to access protected pages that would otherwise be blocked.</p>
<p>Learn more about <a href="/ai-search/configuration/data-source/website/authentication-headers/">configuring custom headers for website crawling</a> in AI Search.</p>


<h2 id="crawler-drilldowns-with-extended-actions-menu"><a href="/changelog/post/2025-11-10-ai-crawl-control-crawler-info/">Crawler drilldowns with extended actions menu</a></h2>
<p><em>2025-11-10</em></p>
<p>AI Crawl Control now supports per-crawler drilldowns with an extended actions menu and status code analytics. Drill down into Metrics, Cloudflare Radar, and Security Analytics, or export crawler data for use in <a href="/waf/custom-rules/">WAF custom rules</a>, <a href="/rules/url-forwarding/">Redirect Rules</a>, and robots.txt files.</p>
<h4 id="2025-11-10-ai-crawl-control-crawler-info-what-s-new">What's new</h4>
<h4 id="2025-11-10-ai-crawl-control-crawler-info-status-code-distribution-chart">Status code distribution chart</h4>
<p>The <strong>Metrics</strong> tab includes a status code distribution chart showing HTTP response codes (2xx, 3xx, 4xx, 5xx) over time. Filter by individual crawler, category, operator, or time range to analyze how specific crawlers interact with your site.</p>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-status-codes.png" alt="AI Crawl Control status code distribution chart" /></p>
<h4 id="2025-11-10-ai-crawl-control-crawler-info-extended-actions-menu">Extended actions menu</h4>
<p>Each crawler row includes a three-dot menu with per-crawler actions:</p>
<ul>
<li><strong>View Metrics</strong> — Filter the AI Crawl Control Metrics page to the selected crawler.</li>
<li><strong>View on Cloudflare Radar</strong> — Access verified crawler details on Cloudflare Radar.</li>
<li><strong>Copy User Agent</strong> — Copy user agent strings for use in WAF custom rules, Redirect Rules, or robots.txt files.</li>
<li><strong>View in Security Analytics</strong> — Filter Security Analytics by detection IDs (Bot Management customers).</li>
<li><strong>Copy Detection ID</strong> — Copy detection IDs for use in WAF custom rules (Bot Management customers).</li>
</ul>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-crawler-info.png" alt="AI Crawl Control crawler actions menu" /></p>
<h4 id="2025-11-10-ai-crawl-control-crawler-info-get-started">Get started</h4>
<ol>
<li>Log in to the Cloudflare dashboard, and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong> &gt; <strong>Metrics</strong> to access the status code distribution chart.</li>
<li>Go to <strong>AI Crawl Control</strong> &gt; <strong>Crawlers</strong> and select the three-dot menu for any crawler to access per-crawler actions.</li>
<li>Select multiple crawlers to use bulk copy buttons for user agents or detection IDs.</li>
</ol>
<p>Learn more about <a href="/ai-crawl-control/">AI Crawl Control</a>.</p>


<h2 id="workers-websocket-message-size-limit-increased-from-1-mib-to-32-mib"><a href="/changelog/post/2025-10-31-increased-websocket-message-size-limit/">Workers WebSocket message size limit increased from 1 MiB to 32 MiB</a></h2>
<p><em>2025-10-31</em></p>
<p>Workers, including those using <a href="/durable-objects/">Durable Objects</a> and <a href="/browser-run/">Browser Rendering</a>, may now process WebSocket messages up to 32 MiB in size. Previously, this limit was 1 MiB.</p>
<p>This change allows Workers to handle use cases requiring large message sizes, such as processing Chrome Devtools Protocol messages.</p>
<p>For more information, please see the <a href="/durable-objects/platform/limits/#sqlite-backed-durable-objects-general-limits">Durable Objects startup limits</a>.</p>


<h2 id="reranking-and-api-based-system-prompt-configuration-in-ai-search"><a href="/changelog/post/2025-10-27-ai-search-reranking-system-prompt/">Reranking and API-based system prompt configuration in AI Search</a></h2>
<p><em>2025-10-28</em></p>
<p><a href="/ai-search/">AI Search</a> now supports reranking for improved retrieval quality and allows you to set the system prompt directly in your API requests.</p>
<h4 id="2025-10-27-ai-search-reranking-system-prompt-rerank-for-more-relevant-results">Rerank for more relevant results</h4>
<p>You can now enable <a href="/ai-search/configuration/retrieval/reranking/">reranking</a> to reorder retrieved documents based on their semantic relevance to the user’s query. Reranking helps improve accuracy, especially for large or noisy datasets where vector similarity alone may not produce the optimal ordering.</p>
<p>You can enable and configure reranking in the dashboard or directly in your API requests:</p>
<pre><code class="language-javascript">const answer = await env.AI.autorag(&quot;my-autorag&quot;).aiSearch({&#10;	query: &quot;How do I train a llama to deliver coffee?&quot;,&#10;	model: &quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&#10;	reranking: {&#10;		enabled: true,&#10;		model: &quot;@cf/baai/bge-reranker-base&quot;,&#10;	},&#10;});&#10;</code></pre>
<h4 id="2025-10-27-ai-search-reranking-system-prompt-set-system-prompts-in-api">Set system prompts in API</h4>
<p>Previously, <a href="/ai-search/configuration/retrieval/system-prompt/">system prompts</a> could only be configured in the dashboard. You can now define them directly in your API requests, giving you per-query control over behavior. For example:</p>
<pre><code class="language-javascript">// Dynamically set query and system prompt in AI Search&#10;async function getAnswer(query, tone) {&#10;	const systemPrompt = `You are a ${tone} assistant.`;&#10;&#10;	const response = await env.AI.autorag(&quot;my-autorag&quot;).aiSearch({&#10;		query: query,&#10;		system_prompt: systemPrompt,&#10;	});&#10;&#10;	return response;&#10;}&#10;&#10;// Example usage&#10;const query = &quot;What is Cloudflare?&quot;;&#10;const tone = &quot;friendly&quot;;&#10;&#10;const answer = await getAnswer(query, tone);&#10;console.log(answer);&#10;</code></pre>
<p>Learn more about <a href="/ai-search/configuration/retrieval/reranking/">Reranking</a> and <a href="/ai-search/configuration/retrieval/system-prompt/">System Prompt</a> in AI Search.</p>


<h2 id="workers-ai-markdown-conversion-new-endpoint-to-list-supported-formats"><a href="/changelog/post/2025-10-23-new-markdown-conversion-endpoint/">Workers AI Markdown Conversion: New endpoint to list supported formats</a></h2>
<p><em>2025-10-23</em></p>
<p>Developers can now programmatically retrieve a list of all file formats supported by the <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion utility</a> in Workers AI.</p>
<p>You can use the <a href="/workers-ai/configuration/bindings/"><code>env.AI</code></a> binding:</p>
<pre><code class="language-typescript">await env.AI.toMarkdown().supported()&#10;</code></pre>
<p>Or call the REST API:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown/supported \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27;&#10;</code></pre>
<p>Both return a list of file formats that users can convert into Markdown:</p>
<pre><code class="language-json">[&#10;	{&#10;		&quot;extension&quot;: &quot;.pdf&quot;,&#10;		&quot;mimeType&quot;: &quot;application/pdf&quot;,&#10;	},&#10;	{&#10;		&quot;extension&quot;: &quot;.jpeg&quot;,&#10;		&quot;mimeType&quot;: &quot;image/jpeg&quot;,&#10;	},&#10;	...&#10;]&#10;</code></pre>
<p>Learn more about our <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion utility</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/ai/4/">Previous</a><span>Page 5 of 7</span><a class="pagination-next" rel="next" href="/changelog/product-group/ai/6/">Next</a></nav>
