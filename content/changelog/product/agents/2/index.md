<h1 id="changelog">Changelog</h1>

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


<h2 id="agents-sdk-v0-1-0-and-workers-ai-provider-v2-0-0-with-ai-sdk-v5-support"><a href="/changelog/post/2025-09-03-agents-sdk-beta-v5/">Agents SDK v0.1.0 and workers-ai-provider v2.0.0 with AI SDK v5 support</a></h2>
<p><em>2025-09-10</em></p>
<p>We've shipped a new release for the <a href="https://github.com/cloudflare/agents">Agents SDK</a> bringing full compatibility with <a href="https://ai-sdk.dev/docs/introduction">AI SDK v5</a> and introducing automatic message migration that handles all legacy formats transparently.</p>
<p>This release includes improved streaming and tool support, tool confirmation detection (for &quot;human in the loop&quot; systems), enhanced React hooks with automatic tool resolution, improved error handling for streaming responses, and seamless migration utilities that work behind the scenes.</p>
<p>This makes it ideal for building production AI chat interfaces with Cloudflare Workers AI models, agent workflows, human-in-the-loop systems, or any application requiring reliable message handling across SDK versions — all while maintaining backward compatibility.</p>
<p>Additionally, we've updated workers-ai-provider v2.0.0, the official provider for Cloudflare Workers AI models, to be compatible with AI SDK v5.</p>
<h4 id="2025-09-03-agents-sdk-beta-v5-useagentchat-options">useAgentChat(options)</h4>
<p>Creates a new chat interface with enhanced v5 capabilities.</p>
<pre><code class="language-ts">// Basic chat setup&#10;const { messages, sendMessage, addToolResult } = useAgentChat({&#10;	agent,&#10;	experimental_automaticToolResolution: true,&#10;	tools,&#10;});&#10;&#10;// With custom tool confirmation&#10;const chat = useAgentChat({&#10;	agent,&#10;	experimental_automaticToolResolution: true,&#10;	toolsRequiringConfirmation: [&quot;dangerousOperation&quot;],&#10;});&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-automatic-tool-resolution">Automatic Tool Resolution</h4>
<p>Tools are automatically categorized based on their configuration:</p>
<pre><code class="language-ts">const tools = {&#10;	// Auto-executes (has execute function)&#10;	getLocalTime: {&#10;		description: &quot;Get current local time&quot;,&#10;		inputSchema: z.object({}),&#10;		execute: async () =&gt; new Date().toLocaleString(),&#10;	},&#10;&#10;	// Requires confirmation (no execute function)&#10;	deleteFile: {&#10;		description: &quot;Delete a file from the system&quot;,&#10;		inputSchema: z.object({&#10;			filename: z.string(),&#10;		}),&#10;	},&#10;&#10;	// Server-executed (no client confirmation)&#10;	analyzeData: {&#10;		description: &quot;Analyze dataset on server&quot;,&#10;		inputSchema: z.object({ data: z.array(z.number()) }),&#10;		serverExecuted: true,&#10;	},&#10;} satisfies Record&lt;string, AITool&gt;;&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-message-handling">Message Handling</h4>
<p>Send messages using the new v5 format with parts array:</p>
<pre><code class="language-ts">// Text message&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [{ type: &quot;text&quot;, text: &quot;Hello, assistant!&quot; }],&#10;});&#10;&#10;// Multi-part message with file&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [&#10;		{ type: &quot;text&quot;, text: &quot;Analyze this image:&quot; },&#10;		{ type: &quot;image&quot;, image: imageData },&#10;	],&#10;});&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-tool-confirmation-detection">Tool Confirmation Detection</h4>
<p>Simplified logic for detecting pending tool confirmations:</p>
<pre><code class="language-ts">const pendingToolCallConfirmation = messages.some((m) =&gt;&#10;	m.parts?.some(&#10;		(part) =&gt; isToolUIPart(part) &amp;&amp; part.state === &quot;input-available&quot;,&#10;	),&#10;);&#10;&#10;// Handle tool confirmation&#10;if (pendingToolCallConfirmation) {&#10;	await addToolResult({&#10;		toolCallId: part.toolCallId,&#10;		tool: getToolName(part),&#10;		output: &quot;User approved the action&quot;,&#10;	});&#10;}&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-automatic-message-migration">Automatic Message Migration</h4>
<p>Seamlessly handle legacy message formats without code changes.</p>
<pre><code class="language-ts">// All these formats are automatically converted:&#10;&#10;// Legacy v4 string content&#10;const legacyMessage = {&#10;	role: &quot;user&quot;,&#10;	content: &quot;Hello world&quot;,&#10;};&#10;&#10;// Legacy v4 with tool calls&#10;const legacyWithTools = {&#10;	role: &quot;assistant&quot;,&#10;	content: &quot;&quot;,&#10;	toolInvocations: [&#10;		{&#10;			toolCallId: &quot;123&quot;,&#10;			toolName: &quot;weather&quot;,&#10;			args: { city: &quot;SF&quot; },&#10;			state: &quot;result&quot;,&#10;			result: &quot;Sunny, 72°F&quot;,&#10;		},&#10;	],&#10;};&#10;&#10;// Automatically becomes v5 format:&#10;// {&#10;//   role: &quot;assistant&quot;,&#10;//   parts: [{&#10;//     type: &quot;tool-call&quot;,&#10;//     toolCallId: &quot;123&quot;,&#10;//     toolName: &quot;weather&quot;,&#10;//     args: { city: &quot;SF&quot; },&#10;//     state: &quot;result&quot;,&#10;//     result: &quot;Sunny, 72°F&quot;&#10;//   }]&#10;// }&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-tool-definition-updates">Tool Definition Updates</h4>
<p>Migrate tool definitions to use the new <code>inputSchema</code> property.</p>
<pre><code class="language-ts">// Before (AI SDK v4)&#10;const tools = {&#10;	weather: {&#10;		description: &quot;Get weather information&quot;,&#10;		parameters: z.object({&#10;			city: z.string(),&#10;		}),&#10;		execute: async (args) =&gt; {&#10;			return await getWeather(args.city);&#10;		},&#10;	},&#10;};&#10;&#10;// After (AI SDK v5)&#10;const tools = {&#10;	weather: {&#10;		description: &quot;Get weather information&quot;,&#10;		inputSchema: z.object({&#10;			city: z.string(),&#10;		}),&#10;		execute: async (args) =&gt; {&#10;			return await getWeather(args.city);&#10;		},&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-cloudflare-workers-ai-integration">Cloudflare Workers AI Integration</h4>
<p>Seamless integration with Cloudflare Workers AI models through the updated workers-ai-provider v2.0.0.</p>
<h4 id="2025-09-03-agents-sdk-beta-v5-model-setup-with-workers-ai">Model Setup with Workers AI</h4>
<p>Use Cloudflare Workers AI models directly in your agent workflows:</p>
<pre><code class="language-ts">import { createWorkersAI } from &quot;workers-ai-provider&quot;;&#10;import { useAgentChat } from &quot;agents/ai-react&quot;;&#10;&#10;// Create Workers AI model (v2.0.0 - same API, enhanced v5 internals)&#10;const model = createWorkersAI({&#10;	binding: env.AI,&#10;})(&quot;@cf/meta/llama-3.2-3b-instruct&quot;);&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-enhanced-file-and-image-support">Enhanced File and Image Support</h4>
<p>Workers AI models now support v5 file handling with automatic conversion:</p>
<pre><code class="language-ts">// Send images and files to Workers AI models&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [&#10;		{ type: &quot;text&quot;, text: &quot;Analyze this image:&quot; },&#10;		{&#10;			type: &quot;file&quot;,&#10;			data: imageBuffer,&#10;			mediaType: &quot;image/jpeg&quot;,&#10;		},&#10;	],&#10;});&#10;&#10;// Workers AI provider automatically converts to proper format&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-streaming-with-workers-ai">Streaming with Workers AI</h4>
<p>Enhanced streaming support with automatic warning detection:</p>
<pre><code class="language-ts">// Streaming with Workers AI models&#10;const result = await streamText({&#10;	model: createWorkersAI({ binding: env.AI })(&quot;@cf/meta/llama-3.2-3b-instruct&quot;),&#10;	messages,&#10;	onChunk: (chunk) =&gt; {&#10;		// Enhanced streaming with warning handling&#10;		console.log(chunk);&#10;	},&#10;});&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-import-updates">Import Updates</h4>
<p>Update your imports to use the new v5 types:</p>
<pre><code class="language-ts">// Before (AI SDK v4)&#10;import type { Message } from &quot;ai&quot;;&#10;import { useChat } from &quot;ai/react&quot;;&#10;&#10;// After (AI SDK v5)&#10;import type { UIMessage } from &quot;ai&quot;;&#10;// or alias for compatibility&#10;import type { UIMessage as Message } from &quot;ai&quot;;&#10;import { useChat } from &quot;@ai-sdk/react&quot;;&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-resources">Resources</h4>
<ul>
<li><a href="https://github.com/cloudflare/agents/blob/main/docs/migration-to-ai-sdk-v5.md">Migration Guide</a> - Comprehensive migration documentation</li>
<li><a href="https://ai-sdk.dev/docs/migration-guides/migration-guide-5-0">AI SDK v5 Documentation</a> - Official AI SDK migration guide</li>
<li><a href="https://github.com/cloudflare/agents-starter/pull/105">An Example PR showing the migration from AI SDK v4 to v5</a></li>
<li><a href="https://github.com/cloudflare/agents/issues">GitHub Issues</a> - Report bugs or request features</li>
</ul>
<h4 id="2025-09-03-agents-sdk-beta-v5-feedback-welcome">Feedback Welcome</h4>
<p>We'd love your feedback! We're particularly interested in feedback on:</p>
<ul>
<li><strong>Migration experience</strong> - How smooth was the upgrade process?</li>
<li><strong>Tool confirmation workflow</strong> - Does the new automatic detection work as expected?</li>
<li><strong>Message format handling</strong> - Any edge cases with legacy message conversion?</li>
</ul>


<h2 id="agents-sdk-adds-mcp-elicitation-support-http-streamable-support-task-queues-email-integration-and-more"><a href="/changelog/post/2025-08-05-agents-MCP-update/">Agents SDK adds MCP Elicitation support, http-streamable support, task queues, email integration and more</a></h2>
<p><em>2025-08-05</em></p>
<p>The latest releases of <a href="https://github.com/cloudflare/agents">@cloudflare/agents</a> brings major improvements to MCP transport protocols support and agents connectivity. Key updates include:</p>
<h4 id="2025-08-05-agents-MCP-update-mcp-elicitation-support">MCP elicitation support</h4>
<p>MCP servers can now request user input during tool execution, enabling interactive workflows like confirmations, forms, and multi-step processes. This feature uses durable storage to preserve elicitation state even during agent hibernation, ensuring seamless user interactions across agent lifecycle events.</p>
<pre><code class="language-ts">// Request user confirmation via elicitation&#10;const confirmation = await this.elicitInput({&#10;	message: `Are you sure you want to increment the counter by ${amount}?`,&#10;	requestedSchema: {&#10;		type: &quot;object&quot;,&#10;		properties: {&#10;			confirmed: {&#10;				type: &quot;boolean&quot;,&#10;				title: &quot;Confirm increment&quot;,&#10;				description: &quot;Check to confirm the increment&quot;,&#10;			},&#10;		},&#10;		required: [&quot;confirmed&quot;],&#10;	},&#10;});&#10;</code></pre>
<p>Check out our <a href="https://github.com/whoiskatrin/agents/tree/main/examples/mcp-elicitation-demo">demo</a> to see elicitation in action.</p>
<h4 id="2025-08-05-agents-MCP-update-http-streamable-transport-for-mcp">HTTP streamable transport for MCP</h4>
<p>MCP now supports HTTP streamable transport which is recommended over SSE. This transport type offers:</p>
<ul>
<li><strong>Better performance</strong>: More efficient data streaming and reduced overhead</li>
<li><strong>Improved reliability</strong>: Enhanced connection stability and error recover- <strong>Automatic fallback</strong>: If streamable transport is not available, it gracefully falls back to SSE</li>
</ul>
<pre><code class="language-ts">export default MyMCP.serve(&quot;/mcp&quot;, {&#10;	binding: &quot;MyMCP&quot;,&#10;});&#10;</code></pre>
<p>The SDK automatically selects the best available transport method, gracefully falling back from streamable-http to SSE when needed.</p>
<h4 id="2025-08-05-agents-MCP-update-enhanced-mcp-connectivity">Enhanced MCP connectivity</h4>
<p>Significant improvements to MCP server connections and transport reliability:</p>
<ul>
<li><strong>Auto transport selection</strong>: Automatically determines the best transport method, falling back from streamable-http to SSE as needed</li>
<li><strong>Improved error handling</strong>: Better connection state management and error reporting for MCP servers</li>
<li><strong>Reliable prop updates</strong>: Centralized agent property updates ensure consistency across different contexts</li>
</ul>
<h4 id="2025-08-05-agents-MCP-update-lightweight-queue-for-fast-task-deferral">Lightweight .queue for fast task deferral</h4>
<p>You can use <code>.queue()</code> to enqueue background work — ideal for tasks like processing user messages, sending notifications etc.</p>
<pre><code class="language-ts">class MyAgent extends Agent {&#10;	doSomethingExpensive(payload) {&#10;		// a long running process that you want to run in the background&#10;	}&#10;&#10;	queueSomething() {&#10;		await this.queue(&quot;doSomethingExpensive&quot;, somePayload); // this will NOT block further execution, and runs in the background&#10;		await this.queue(&quot;doSomethingExpensive&quot;, someOtherPayload); // the callback will NOT run until the previous callback is complete&#10;		// ... call as many times as you want&#10;	}&#10;}&#10;</code></pre>
<p>Want to try it yourself? Just define a method like processMessage in your agent, and you’re ready to scale.</p>
<h4 id="2025-08-05-agents-MCP-update-new-email-adapter">New email adapter</h4>
<p>Want to build an AI agent that can receive and respond to emails automatically? With the new email adapter and onEmail lifecycle method, now you can.</p>
<pre><code class="language-ts">export class EmailAgent extends Agent {&#10;	async onEmail(email: AgentEmail) {&#10;		const raw = await email.getRaw();&#10;		const parsed = await PostalMime.parse(raw);&#10;&#10;		// create a response based on the email contents&#10;		// and then send a reply&#10;&#10;		await this.replyToEmail(email, {&#10;			fromName: &quot;Email Agent&quot;,&#10;			body: `Thanks for your email! You&#x27;ve sent us &quot;${parsed.subject}&quot;. We&#x27;ll process it shortly.`,&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>You route incoming mail like this:</p>
<pre><code class="language-ts">export default {&#10;	async email(email, env) {&#10;		await routeAgentEmail(email, env, {&#10;			resolver: createAddressBasedEmailResolver(&quot;EmailAgent&quot;),&#10;		});&#10;	},&#10;};&#10;</code></pre>
<p>You can find a full example <a href="https://github.com/cloudflare/agents/tree/main/examples/email-agent">here</a>.</p>
<h4 id="2025-08-05-agents-MCP-update-automatic-context-wrapping-for-custom-methods">Automatic context wrapping for custom methods</h4>
<p>Custom methods are now automatically wrapped with the agent's context, so calling <code>getCurrentAgent()</code> should work regardless of where in an agent's lifecycle it's called. Previously this would not work on RPC calls, but now just works out of the box.</p>
<pre><code class="language-ts">export class MyAgent extends Agent {&#10;	async suggestReply(message) {&#10;		// getCurrentAgent() now correctly works, even when called inside an RPC method&#10;		const { agent } = getCurrentAgent()!;&#10;		return generateText({&#10;			prompt: `Suggest a reply to: &quot;${message}&quot; from &quot;${agent.name}&quot;`,&#10;			tools: [replyWithEmoji],&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>Try it out and tell us what you build!</p>


<h2 id="cloudflare-sandbox-sdk-adds-streaming-code-interpreter-git-support-process-control-and-more"><a href="/changelog/post/2025-08-05-sandbox-sdk-major-update/">Cloudflare Sandbox SDK adds streaming, code interpreter, Git support, process control and more</a></h2>
<p><em>2025-08-05</em></p>
<p>We’ve shipped a major release for the <a href="https://github.com/cloudflare/sandbox-sdk">@cloudflare/sandbox</a> SDK, turning it into a full-featured, container-based execution platform that runs securely on Cloudflare Workers.</p>
<p>This update adds live streaming of output, persistent Python and JavaScript code interpreters with rich output support (charts, tables, HTML, JSON), file system access, Git operations, full background process control, and the ability to expose running services via public URLs.</p>
<p>This makes it ideal for building AI agents, CI runners, cloud REPLs, data analysis pipelines, or full developer tools — all without managing infrastructure.</p>
<h4 id="2025-08-05-sandbox-sdk-major-update-code-interpreter-python-js-ts">Code interpreter (Python, JS, TS)</h4>
<p>Create persistent code contexts with support for rich visual + structured outputs.</p>
<h4 id="2025-08-05-sandbox-sdk-major-update-createcodecontext-options">createCodeContext(options)</h4>
<p>Creates a new code execution context with persistent state.</p>
<pre><code class="language-ts">// Create a Python context&#10;const pythonCtx = await sandbox.createCodeContext({ language: &quot;python&quot; });&#10;&#10;// Create a JavaScript context&#10;const jsCtx = await sandbox.createCodeContext({ language: &quot;javascript&quot; });&#10;</code></pre>
<p>Options:</p>
<ul>
<li>language: Programming language ('python' | 'javascript' | 'typescript')</li>
<li>cwd: Working directory (default: /workspace)</li>
<li>envVars: Environment variables for the context</li>
</ul>
<h4 id="2025-08-05-sandbox-sdk-major-update-runcode-code-options">runCode(code, options)</h4>
<p>Executes code with optional streaming callbacks.</p>
<pre><code class="language-ts">// Simple execution&#10;const execution = await sandbox.runCode(&#x27;print(&quot;Hello World&quot;)&#x27;, {&#10;	context: pythonCtx,&#10;});&#10;&#10;// With streaming callbacks&#10;await sandbox.runCode(&#10;	`&#10;for i in range(5):&#10;    print(f&quot;Step {i}&quot;)&#10;    time.sleep(1)&#10;`,&#10;	{&#10;		context: pythonCtx,&#10;		onStdout: (output) =&gt; console.log(&quot;Real-time:&quot;, output.text),&#10;		onResult: (result) =&gt; console.log(&quot;Result:&quot;, result),&#10;	},&#10;);&#10;</code></pre>
<p>Options:</p>
<ul>
<li>language: Programming language ('python' | 'javascript' | 'typescript')</li>
<li>cwd: Working directory (default: /workspace)</li>
<li>envVars: Environment variables for the context</li>
</ul>
<h4 id="2025-08-05-sandbox-sdk-major-update-real-time-streaming-output">Real-time streaming output</h4>
<p>Returns a streaming response for real-time processing.</p>
<pre><code class="language-ts">const stream = await sandbox.runCodeStream(&#10;	&quot;import time; [print(i) for i in range(10)]&quot;,&#10;);&#10;// Process the stream as needed&#10;</code></pre>
<h4 id="2025-08-05-sandbox-sdk-major-update-rich-output-handling">Rich output handling</h4>
<p>Interpreter outputs are auto-formatted and returned in multiple formats:</p>
<ul>
<li>text</li>
<li>html (e.g., Pandas tables)</li>
<li>png, svg (e.g., Matplotlib charts)</li>
<li>json (structured data)</li>
<li>chart (parsed visualizations)</li>
</ul>
<pre><code class="language-ts">const result = await sandbox.runCode(&#10;	`&#10;import seaborn as sns&#10;import matplotlib.pyplot as plt&#10;&#10;data = sns.load_dataset(&quot;flights&quot;)&#10;pivot = data.pivot(&quot;month&quot;, &quot;year&quot;, &quot;passengers&quot;)&#10;sns.heatmap(pivot, annot=True, fmt=&quot;d&quot;)&#10;plt.title(&quot;Flight Passengers&quot;)&#10;plt.show()&#10;&#10;pivot.to_dict()&#10;`,&#10;	{ context: pythonCtx },&#10;);&#10;&#10;if (result.png) {&#10;	console.log(&quot;Chart output:&quot;, result.png);&#10;}&#10;</code></pre>
<h4 id="2025-08-05-sandbox-sdk-major-update-preview-urls-from-exposed-ports">Preview URLs from Exposed Ports</h4>
<p>Start background processes and expose them with live URLs.</p>
<pre><code class="language-ts">await sandbox.startProcess(&quot;python -m http.server 8000&quot;);&#10;const preview = await sandbox.exposePort(8000);&#10;&#10;console.log(&quot;Live preview at:&quot;, preview.url);&#10;</code></pre>
<h4 id="2025-08-05-sandbox-sdk-major-update-full-process-lifecycle-control">Full process lifecycle control</h4>
<p>Start, inspect, and terminate long-running background processes.</p>
<pre><code class="language-ts">const process = await sandbox.startProcess(&quot;node server.js&quot;);&#10;console.log(`Started process ${process.id} with PID ${process.pid}`);&#10;&#10;// Monitor the process&#10;const logStream = await sandbox.streamProcessLogs(process.id);&#10;for await (const log of parseSSEStream&lt;LogEvent&gt;(logStream)) {&#10;	console.log(`Server: ${log.data}`);&#10;}&#10;</code></pre>
<ul>
<li>listProcesses() - List all running processes</li>
<li>getProcess(id) - Get detailed process status</li>
<li>killProcess(id, signal) - Terminate specific processes</li>
<li>killAllProcesses() - Kill all processes</li>
<li>streamProcessLogs(id, options) - Stream logs from running processes</li>
<li>getProcessLogs(id) - Get accumulated process output</li>
</ul>
<h4 id="2025-08-05-sandbox-sdk-major-update-git-integration">Git integration</h4>
<p>Clone Git repositories directly into the sandbox.</p>
<pre><code class="language-ts">await sandbox.gitCheckout(&quot;https://github.com/user/repo&quot;, {&#10;	branch: &quot;main&quot;,&#10;	targetDir: &quot;my-project&quot;,&#10;});&#10;</code></pre>
<p>Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.</p>


<h2 id="openai-open-models-now-available-on-workers-ai"><a href="/changelog/post/2025-08-05-openai-open-models/">OpenAI open models now available on Workers AI</a></h2>
<p><em>2025-08-05</em></p>
<p>We're thrilled to be a Day 0 partner with <a href="http://openai.com/index/introducing-gpt-oss">OpenAI</a> to bring their <a href="https://openai.com/index/gpt-oss-model-card/">latest open models</a> to Workers AI, including support for Responses API, Code Interpreter, and Web Search (coming soon).</p>
<p>Get started with the new models at <code>@cf/openai/gpt-oss-120b</code> and <code>@cf/openai/gpt-oss-20b</code>.
Check out the <a href="https://blog.cloudflare.com/openai-gpt-oss-on-workers-ai">blog</a> for more details about the new models, and the <a href="/workers-ai/models/gpt-oss-120b"><code>gpt-oss-120b</code></a> and <a href="/workers-ai/models/gpt-oss-20b"><code>gpt-oss-20b</code></a> model pages for more information about pricing and context windows.</p>
<h4 id="2025-08-05-openai-open-models-responses-api">Responses API</h4>
If you call the model through:
- Workers Binding, it will accept/return Responses API – `env.AI.run(“@cf/openai/gpt-oss-120b”)`
- REST API on `/run` endpoint, it will accept/return Responses API – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/run/@cf/openai/gpt-oss-120b`
- REST API on new `/responses` endpoint, it will accept/return Responses API – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/v1/responses`
- REST API for OpenAI Compatible endpoint, it will return Chat Completions (coming soon) – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/v1/chat/completions`
<pre><code>curl https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/ai/v1/responses \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_KEY&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;model&quot;: &quot;@cf/openai/gpt-oss-120b&quot;,&#10;    &quot;reasoning&quot;: {&quot;effort&quot;: &quot;medium&quot;},&#10;    &quot;input&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What are the benefits of open-source models?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;&#10;</code></pre>
<h4 id="2025-08-05-openai-open-models-code-interpreter">Code Interpreter</h4>
The model is natively trained to support stateful code execution, and we've implemented support for this feature using our [Sandbox SDK](https://github.com/cloudflare/sandbox-sdk) and [Containers](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/). Cloudflare's Developer Platform is uniquely positioned to support this feature, so we're very excited to bring our products together to support this new use case.
<h4 id="2025-08-05-openai-open-models-web-search-coming-soon">Web Search (coming soon)</h4>
We are working to implement Web Search for the model, where users can bring their own Exa API Key so the model can browse the Internet.


<h2 id="run-ai-generated-code-on-demand-with-code-sandboxes-new"><a href="/changelog/post/2025-06-24-announcing-sandboxes/">Run AI-generated code on-demand with Code Sandboxes (new)</a></h2>
<p><em>2025-06-25</em></p>
<p>AI is supercharging app development for everyone, but we need a safe way to run untrusted, LLM-written code. We’re introducing <a href="https://www.npmjs.com/package/@cloudflare/sandbox">Sandboxes</a>, which let your Worker run actual processes in a secure, container-based environment.</p>
<pre><code class="language-ts">import { getSandbox } from &quot;@cloudflare/sandbox&quot;;&#10;export { Sandbox } from &quot;@cloudflare/sandbox&quot;;&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env) {&#10;		const sandbox = getSandbox(env.Sandbox, &quot;my-sandbox&quot;);&#10;		return sandbox.exec(&quot;ls&quot;, [&quot;-la&quot;]);&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-06-24-announcing-sandboxes-methods">Methods</h4>
<ul>
<li><code>exec(command: string, args: string[], options?: { stream?: boolean })</code>:Execute a command in the sandbox.</li>
<li><code>gitCheckout(repoUrl: string, options: { branch?: string; targetDir?: string; stream?: boolean })</code>: Checkout a git repository in the sandbox.</li>
<li><code>mkdir(path: string, options: { recursive?: boolean; stream?: boolean })</code>: Create a directory in the sandbox.</li>
<li><code>writeFile(path: string, content: string, options: { encoding?: string; stream?: boolean })</code>: Write content to a file in the sandbox.</li>
<li><code>readFile(path: string, options: { encoding?: string; stream?: boolean })</code>: Read content from a file in the sandbox.</li>
<li><code>deleteFile(path: string, options?: { stream?: boolean })</code>: Delete a file from the sandbox.</li>
<li><code>renameFile(oldPath: string, newPath: string, options?: { stream?: boolean })</code>: Rename a file in the sandbox.</li>
<li><code>moveFile(sourcePath: string, destinationPath: string, options?: { stream?: boolean })</code>: Move a file from one location to another in the sandbox.</li>
<li><code>ping()</code>: Ping the sandbox.</li>
</ul>
<p>Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.</p>
<p>You can try it today from your Worker, with just a few lines of code. Let us know what you build.</p>


<h2 id="build-mcp-servers-with-the-agents-sdk"><a href="/changelog/post/2025-04-07-mcp-servers-agents-sdk-updates/">Build MCP servers with the Agents SDK</a></h2>
<p><em>2025-04-07</em></p>
<p>The Agents SDK now includes built-in support for building remote MCP (Model Context Protocol) servers directly as part of your Agent. This allows you to easily create and manage MCP servers, without the need for additional infrastructure or configuration.</p>
<p>The SDK includes a new <code>MCPAgent</code> class that extends the <code>Agent</code> class and allows you to expose resources and tools over the MCP protocol, as well as authorization and authentication to enable remote MCP servers.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17623.md")</div>
<p>See <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp">the example</a> for the full code and as the basis for building your own MCP servers, and the <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp-client">client example</a> for how to build an Agent that acts as an MCP client.</p>
<p>To learn more, review the <a href="https://blog.cloudflare.com/building-ai-agents-with-mcp-authn-authz-and-durable-objects">announcement blog</a> as part of Developer Week 2025.</p>
<h4 id="2025-04-07-mcp-servers-agents-sdk-updates-agents-sdk-updates">Agents SDK updates</h4>
<p>We've made a number of improvements to the <a href="/agents/">Agents SDK</a>, including:</p>
<ul>
<li>Support for building MCP servers with the new <code>MCPAgent</code> class.</li>
<li>The ability to export the current agent, request and WebSocket connection context using <code>import { context } from &quot;agents&quot;</code>, allowing you to minimize or avoid direct dependency injection when calling tools.</li>
<li>Fixed a bug that prevented query parameters from being sent to the Agent server from the <code>useAgent</code> React hook.</li>
<li>Automatically converting the <code>agent</code> name in <code>useAgent</code> or <code>useAgentChat</code> to kebab-case to ensure it matches the naming convention expected by <a href="/agents/runtime/communication/routing/"><code>routeAgentRequest</code></a>.</li>
</ul>
<p>To install or update the Agents SDK, run <code>npm i agents@latest</code> in an existing project, or explore the <code>agents-starter</code> project:</p>
<pre><code class="language-sh">npm create cloudflare@latest -- --template cloudflare/agents-starter&#10;</code></pre>
<p>See the full release notes and changelog <a href="https://github.com/cloudflare/agents/blob/main/packages/agents/CHANGELOG.md">on the Agents SDK repository</a> and</p>


<h2 id="npm-i-agents"><a href="/changelog/post/2025-03-18-npm-i-agents/">npm i agents</a></h2>
<p><em>2025-03-18</em></p>
<img src="/assets/upstream/images/agents/npm-i-agents.apng" alt="npm i agents" width="1000" height="541" />
<h4 id="2025-03-18-npm-i-agents-agents-sdk-agents"><code>agents-sdk</code> -&gt; <code>agents</code> <span class="nb-badge">Updated</span></h4>
<p>📝 <strong>We've renamed the Agents package to <code>agents</code></strong>!</p>
<p>If you've already been building with the Agents SDK, you can update your dependencies to use the new package name, and replace references to <code>agents-sdk</code> with <code>agents</code>:</p>
<pre><code class="language-sh">&#35; Install the new package&#10;npm i agents&#10;</code></pre>
<pre><code class="language-sh">&#35; Remove the old (deprecated) package&#10;npm uninstall agents-sdk&#10;&#10;&#35; Find instances of the old package name in your codebase&#10;grep -r &#x27;agents-sdk&#x27; .&#10;&#35; Replace instances of the old package name with the new one&#10;&#35; (or use find-replace in your editor)&#10;sed -i &#x27;s/agents-sdk/agents/g&#x27; $(grep -rl &#x27;agents-sdk&#x27; .)&#10;</code></pre>
<p>All future updates will be pushed to the new <code>agents</code> package, and the older package has been marked as deprecated.</p>
<h4 id="2025-03-18-npm-i-agents-agents-sdk-updates">Agents SDK updates <span class="nb-badge">New</span></h4>
<p>We've added a number of big new features to the Agents SDK over the past few weeks, including:</p>
<ul>
<li>You can now set <code>cors: true</code> when using <code>routeAgentRequest</code> to return permissive default CORS headers to Agent responses.</li>
<li>The regular client now syncs state on the agent (just like the React version).</li>
<li><code>useAgentChat</code> bug fixes for passing headers/credentials, including properly clearing cache on unmount.</li>
<li>Experimental <code>/schedule</code> module with a prompt/schema for adding scheduling to your app (with evals!).</li>
<li>Changed the internal <code>zod</code> schema to be compatible with the limitations of Google's Gemini models by removing the discriminated union, allowing you to use Gemini models with the scheduling API.</li>
</ul>
<p>We've also fixed a number of bugs with state synchronization and the React hooks.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17621.md")</div>
<h4 id="2025-03-18-npm-i-agents-call-agent-methods-from-your-client-code">Call Agent methods from your client code <span class="nb-badge">New</span></h4>
<p>We've added a new <a href="/agents/runtime/agents-api/"><code>@unstable_callable()</code></a> decorator for defining methods that can be called directly from clients. This allows you call methods from within your client code: you can call methods (with arguments) and get native JavaScript objects back.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17622.md")</div>
<h4 id="2025-03-18-npm-i-agents-agents-starter">agents-starter <span class="nb-badge">Updated</span></h4>
<p>We've fixed a number of small bugs in the <a href="https://github.com/cloudflare/agents-starter"><code>agents-starter</code></a> project — a real-time, chat-based example application with tool-calling &amp; human-in-the-loop built using the Agents SDK. The starter has also been upgraded to use the latest <a href="/changelog/2025-03-13-wrangler-v4/">wrangler v4</a> release.</p>
<p>If you're new to Agents, you can install and run the <code>agents-starter</code> project in two commands:</p>
<pre><code class="language-sh">&#35; Install it&#10;$ npm create cloudflare@latest agents-starter -- --template=&quot;cloudflare/agents-starter&quot;&#10;&#35; Run it&#10;$ npm run start&#10;</code></pre>
<p>You can use the starter as a template for your own Agents projects: open up <code>src/server.ts</code> and <code>src/client.tsx</code> to see how the Agents SDK is used.</p>
<h4 id="2025-03-18-npm-i-agents-more-documentation">More documentation <span class="nb-badge">Updated</span></h4>
<p>We've heard your feedback on the Agents SDK documentation, and we're shipping more API reference material and usage examples, including:</p>
<ul>
<li>Expanded <a href="/agents/runtime/">API reference documentation</a>, covering the methods and properties exposed by the Agents SDK, as well as more usage examples.</li>
<li>More <a href="/agents/runtime/agents-api/#client-api">Client API</a> documentation that documents <code>useAgent</code>, <code>useAgentChat</code> and the new <code>@unstable_callable</code> RPC decorator exposed by the SDK.</li>
<li>New documentation on how to <a href="/agents/runtime/communication/routing/">route requests to agents</a> and (optionally) authenticate clients before they connect to your Agents.</li>
</ul>
<p>Note that the Agents SDK is continually growing: the type definitions included in the SDK will always include the latest APIs exposed by the <code>agents</code> package.</p>
<p>If you're still wondering what Agents are, <a href="https://blog.cloudflare.com/build-ai-agents-on-cloudflare/">read our blog on building AI Agents on Cloudflare</a> and/or visit the <a href="/agents/">Agents documentation</a> to learn more.</p>


<h2 id="introducing-the-agents-sdk"><a href="/changelog/post/2025-02-25-agents-sdk/">Introducing the Agents SDK</a></h2>
<p><em>2025-02-25</em></p>
<p>We've released the <a href="http://blog.cloudflare.com/build-ai-agents-on-cloudflare/">Agents SDK</a>, a package and set of tools that help you build and ship AI Agents.</p>
<p>You can get up and running with a <a href="https://github.com/cloudflare/agents-starter">chat-based AI Agent</a> (and deploy it to Workers) that uses the Agents SDK, tool calling, and state syncing with a React-based front-end by running the following command:</p>
<pre><code class="language-sh">npm create cloudflare@latest agents-starter -- --template=&quot;cloudflare/agents-starter&quot;&#10;&#35; open up README.md and follow the instructions&#10;</code></pre>
<p>You can also add an Agent to any existing Workers application by installing the <code>agents</code> package directly</p>
<pre><code class="language-sh">npm i agents&#10;</code></pre>
<p>... and then define your first Agent:</p>
<pre><code class="language-ts">import { Agent } from &quot;agents&quot;;&#10;&#10;export class YourAgent extends Agent&lt;Env&gt; {&#10;	// Build it out&#10;	// Access state on this.state or query the Agent&#x27;s database via this.sql&#10;	// Handle WebSocket events with onConnect and onMessage&#10;	// Run tasks on a schedule with this.schedule&#10;	// Call AI models&#10;	// ... and/or call other Agents.&#10;}&#10;</code></pre>
<p>Head over to the <a href="/agents/">Agents documentation</a> to learn more about the Agents SDK, the SDK APIs, as well as how to test and deploying agents to production.</p>


<h2 id="build-ai-agents-with-example-prompts"><a href="/changelog/post/2025-02-14-example-ai-prompts/">Build AI Agents with Example Prompts</a></h2>
<p><em>2025-02-14</em></p>
<p>We've added an <a href="/workers/get-started/prompting/">example prompt</a> to help you get started with building AI agents and applications on Cloudflare <a href="/workers/">Workers</a>, including <a href="/workflows/">Workflows</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/kv/">Workers KV</a>.</p>
<p>You can use this prompt with your favorite AI model, including Claude 3.5 Sonnet, OpenAI's o3-mini, Gemini 2.0 Flash, or Llama 3.3 on Workers AI. Models with large context windows will allow you to paste the prompt directly: provide your own prompt within the <code>&lt;user_prompt&gt;&lt;/user_prompt&gt;</code> tags.</p>
<pre><code class="language-sh">{paste_prompt_here}&#10;&lt;user_prompt&gt;&#10;user: Build an AI agent using Cloudflare Workflows. The Workflow should run when a new GitHub issue is opened on a specific project with the label &#x27;help&#x27; or &#x27;bug&#x27;, and attempt to help the user troubleshoot the issue by calling the OpenAI API with the issue title and description, and a clear, structured prompt that asks the model to suggest 1-3 possible solutions to the issue. Any code snippets should be formatted in Markdown code blocks. Documentation and sources should be referenced at the bottom of the response. The agent should then post the response to the GitHub issue. The agent should run as the provided GitHub bot account.&#10;&lt;/user_prompt&gt;&#10;</code></pre>
<p>This prompt is still experimental, but we encourage you to try it out and <a href="https://github.com/cloudflare/cloudflare-docs/issues/new?template=content.edit.yml">provide feedback</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/agents/">Previous</a><span>Page 2 of 2</span></nav>
