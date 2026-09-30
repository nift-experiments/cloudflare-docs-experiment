---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/agents/
  description: '2026-09-11'
  full_title: agents changelog | Cloudflare Docs
  head_html: <title>agents changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-11"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/agents/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="agents changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-11"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/agents/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/agents/#page","headline":"agents changelog | Cloudflare Docs","description":"2026-09-11","url":"https://developers.cloudflare.com/changelog/product/agents/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/agents/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="inspect-voice-agent-turn-latency-and-outcomes"><a href="/changelog/post/2026-09-11-voice-diagnostics-turn-metrics/">Inspect Voice Agent turn latency and outcomes</a></h2>
<p><em>2026-09-11</em></p>
<p><code>@cloudflare/voice</code> v0.4.0 now lets you inspect where each Voice Agent turn spends time and how it ends.</p>
<pre tabindex="0"><code class="language-ts">client.addEventListener(&quot;turnmetrics&quot;, (turn) =&gt; {&#10;	console.log(turn.outcome, turn.turnTotalMs);&#10;});&#10;</code></pre>
<h4 id="2026-09-11-voice-diagnostics-turn-metrics-about-the-voice-package">About the Voice package</h4>
<p>The <code>@cloudflare/voice</code> package lets you build real-time voice agents with Cloudflare Agents. It streams microphone audio to an Agent over WebSocket, transcribes speech, runs your model through <code>onTurn()</code>, converts the response to speech, and streams audio back to the caller.</p>
<p>A turn moves through several stages:</p>
<pre tabindex="0"><code class="language-txt">User speaks -&gt; speech-to-text -&gt; model -&gt; text-to-speech -&gt; audio&#10;</code></pre>
<p>Previously, the package's four aggregate metrics covered successful, non-empty speech turns. They did not show how failed, aborted, empty, or text turns ended.</p>
<h4 id="2026-09-11-voice-diagnostics-turn-metrics-turn-metrics">Turn metrics</h4>
<p>Each speech or text turn now produces a typed <code>VoiceTurnMetrics</code> summary with:</p>
<ul>
<li>A <code>turnId</code> for correlating events from the same turn.</li>
<li>A terminal outcome such as <code>completed</code>, <code>no_output</code>, <code>output_limit</code>, <code>content_filtered</code>, <code>model_error</code>, <code>tts_error</code>, or <code>aborted</code>.</li>
<li>Timings for important stages, including speech-to-final-transcript, model-to-first-text, TTS-to-first-audio, and total turn duration.</li>
</ul>
<p>These timings can overlap and are not additive. Timings for stages that a turn did not reach are omitted.</p>
<p>The latest summary is available through <code>VoiceClient</code>, <code>useVoiceAgent()</code>, and <code>useVoiceInput()</code>. Voice input includes only the speech and transcription timings it can measure.</p>
<p>If an agent produces no audio, you can now distinguish between the model returning no output, reaching an output limit, encountering content filtering, or failing.</p>
<h4 id="2026-09-11-voice-diagnostics-turn-metrics-additional-diagnostics">Additional diagnostics</h4>
<p>For local debugging, you can forward server lifecycle events to the browser console:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17686.md")</div>
<p>The browser console combines server lifecycle events with local microphone, connection, and playback events, including model start, first model text, first audio, and playback start. Diagnostics are off by default, and their event names and fields can change.</p>
<p><code>VoiceClient</code> also exposes typed events for speech-to-text failures, connection errors, and model outcomes. The SDK removes known content fields and does not read arbitrary provider responses, but custom error messages must not contain sensitive data.</p>
<p>Install the release with a compatible Agents SDK version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/voice@^0.4.0 agents@^0.22.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/voice@^0.4.0 agents@^0.22.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/voice@^0.4.0 agents@^0.22.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/voice@^0.4.0 agents@^0.22.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/voice@^0.4.0 agents@^0.22.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/voice@^0.4.0 agents@^0.22.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/voice@^0.4.0 agents@^0.22.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/voice@^0.4.0 agents@^0.22.0" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/communication-channels/voice/#pipeline-metrics">Voice pipeline metrics</a> and <a href="https://github.com/cloudflare/agents/tree/main/examples/voice-agent">Voice Agent example</a> to get started.</p>


<h2 id="choose-oauth-scopes-for-wrangler-and-the-cloudflare-api-mcp-server"><a href="/changelog/post/2026-08-22-wrangler-mcp-optional-oauth-scopes/">Choose OAuth scopes for Wrangler and the Cloudflare API MCP server</a></h2>
<p><em>2026-08-22</em></p>
<p>Wrangler and the <a href="/agents/model-context-protocol/cloudflare/servers-for-cloudflare/">Cloudflare API MCP server</a> now use optional OAuth scopes. During authorization, you can choose which optional scopes to grant instead of approving every scope requested by each client.</p>
<p>The consent dialog now includes the option to edit the permissions you grant to Wrangler or the Cloudflare API MCP server:</p>
<p><img src="/assets/upstream/images/agents/oauth-optional-scopes-review.png" alt="OAuth consent dialog with an Edit Permissions button" /></p>
<p>You can then choose which specific permissions to grant:</p>
<p><img src="/assets/upstream/images/agents/oauth-optional-scopes-edit.png" alt="OAuth permission editor with controls for individual scopes" /></p>
<p>Required scopes remain selected. Choosing fewer optional scopes limits each tool's access to the permissions needed for your workflow.</p>
<p>If a command or tool call needs a scope that you declined, reauthorize the client and grant that scope.</p>
<p>For more information, refer to <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a> and <a href="/fundamentals/oauth/authorizing-an-application/#edit-optional-permissions">Edit optional permissions</a>.</p>


<h2 id="agent-traces-for-think-flue-and-ai-sdk-instrumented-by-agents-sdk"><a href="/changelog/post/2026-08-04-agent-tracing/">Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK</a></h2>
<p><em>2026-08-04</em></p>
<p>Agent tracing is now available for applications built with the Agents SDK. Traces show each agent turn alongside model calls, tool runs, approvals, token usage, and Workers runtime operations.</p>
<p>Turn on Workers tracing in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17683.md")</div>
<p>Think and Flue applications emit agent traces automatically. For direct AI SDK calls, wrap the AI SDK namespace once. <code>wrapAISDK()</code> supports AI SDK v6 and v7. This AI SDK v7 example also supplies the agent identity:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17684.md")</div>
<p>Message and tool payload recording is off by default. Turn it on only when the payloads are safe to store:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17685.md")</div>
<p>Open the <a href="https://dash.cloudflare.com/?to=/:account/agents"><strong>Agents</strong> tab</a> in the Cloudflare dashboard to inspect sessions, replay conversations, and view trace waterfalls. For advanced setup, privacy controls, and trace structure, refer to <a href="/agents/runtime/operations/observability/tracing/">Agent tracing</a>.</p>


<h2 id="preview-cloudflare-computer-agent-runtime"><a href="/changelog/post/2026-08-03-cloudflare-computer/">Preview: @cloudflare/computer agent runtime</a></h2>
<p><em>2026-08-03</em></p>
<p>We're releasing an early preview of <a href="https://github.com/cloudflare/computer"><code>@cloudflare/computer</code></a>, an open-source agent runtime that gives every agent its own computer. The runtime dynamically orchestrates between fast, efficient isolates and full Linux containers, so the agent always runs on the right compute primitive for the task at hand.</p>
<p><code>@cloudflare/computer</code> provides a virtual filesystem backed by SQLite, which you can populate from cloud storage, source control, or any files you choose. Agents can read, write, and edit files, run shell commands, and interact with Git repositories. All operations are gated, audited, and observed.</p>
<p>Install the package via npm:</p>
<pre tabindex="0"><code class="language-sh">npm install @cloudflare/computer&#10;</code></pre>
<p>Instantiate a <code>Workspace</code> inside any Durable Object to give your agent a filesystem and execution runtime:</p>
<pre tabindex="0"><code class="language-ts">import { Workspace } from &quot;@cloudflare/computer&quot;;&#10;&#10;export class Agent {&#10;	workspace = new Workspace({&#10;		storage: this.ctx.storage,&#10;	});&#10;}&#10;</code></pre>
<p>Several execution backends are included or you can write your own:</p>
<ul>
<li><strong>Isolate runtime</strong> — fast, horizontally scalable execution via <code>just-bash</code> and Dynamic Workers, ideal for file manipulation and data processing.</li>
<li><strong>Container runtime</strong> — full Linux environment via Cloudflare Containers, mounted through FUSE, for tasks that need native binaries, package managers, or a complete userland.</li>
</ul>
<p>The AI SDK-compatible toolkit provides common agent tools (<code>read</code>, <code>write</code>, <code>edit</code>, <code>ls</code>, <code>exec</code>) and guides the model to choose the appropriate backend for each task.</p>
<p>For more examples, including a step-by-step tutorial, visit the <a href="https://github.com/cloudflare/computer"><code>@cloudflare/computer</code> repository</a>.</p>
<p>Read the announcement blog post for more details: <a href="https://blog.cloudflare.com/cloudflare-computer/">Your agent needs a computer, not a container</a>.</p>


<h2 id="cloudflare-mcp-servers-support-the-new-mcp-2026-07-28-specification"><a href="/changelog/post/2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28/">Cloudflare MCP servers support the new MCP 2026-07-28 Specification</a></h2>
<p><em>2026-07-28</em></p>
<p>Cloudflare's <a href="/agents/model-context-protocol/cloudflare/servers-for-cloudflare/#product-specific-mcp-servers">product-specific MCP servers</a> now support the new MCP 2026-07-28 Specification. Each request runs on a fresh stateless server without an MCP protocol session or protocol-specific Durable Object.</p>
<p>The <code>/mcp</code> endpoint also accepts stateless requests from 2025 Streamable HTTP clients. Most clients can reconnect without configuration changes.</p>
<p>Use <code>/mcp</code> for new connections. Historical <code>/sse</code> URLs continue to work as aliases for the same Streamable HTTP handler, but they no longer serve the deprecated HTTP+SSE transport. If a client forces SSE transport, change it to Streamable HTTP or automatic transport detection.</p>


<h2 id="agents-sdk-adds-mcp-specification-2026-07-28-support"><a href="/changelog/post/2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2/">Agents SDK adds MCP Specification 2026-07-28 support</a></h2>
<p><em>2026-07-27</em></p>
<p>Agents SDK v0.20.0 adds client and server support for the <a href="https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/">MCP 2026-07-28 release candidate</a>. Workers can serve tools, prompts, resources, and elicitation without an MCP transport session or Durable Object. Agents can connect to both MCP 2026-07-28 servers and existing legacy servers.</p>
<h4 id="2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2-client-support">Client support</h4>
<p>The MCP client manager now uses <code>@modelcontextprotocol/client</code>. For each connection, it probes for MCP 2026-07-28 support with <code>server/discover</code>. If the server does not support the stateless protocol, the client continues with the legacy <code>initialize</code> handshake on the same connection. Existing <code>addMcpServer</code> calls do not need a protocol-version setting or separate clients for each protocol generation.</p>
<p>For stateless requests, elicitation uses <code>input_required</code> through multi-round-trip requests (MRTR). The legacy path uses the same form and URL handlers for pushed requests. The SDK collects input, retries the original operation, and resolves the original <code>callTool</code>, <code>getPrompt</code>, or <code>readResource</code> promise with its final result.</p>
<p>OAuth callbacks now validate issuer metadata through the v2 SDK. Discovery state and issuer-bound credentials persist across browser redirects and Durable Object hibernation.</p>
<h4 id="2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2-run-stateless-servers">Run stateless servers</h4>
<p><code>createMcpHandler</code> now accepts a factory that returns a server from <code>@modelcontextprotocol/server</code>. The factory creates an isolated server for each request.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17681.md")</div>
<p>The isolated <code>agents/mcp/server</code> entry keeps <code>McpAgent</code>, <code>WorkerTransport</code>, MCP client transports, and SDK v1 modules out of stateless server bundles.</p>
<p>The Workers wrapper validates present browser Origins, supports explicit delegation to trusted Origin middleware, and exposes request handling plus typed change notifications.</p>
<h4 id="2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2-backward-compatibility">Backward compatibility</h4>
<p>The same <code>createMcpHandler(createServer)(request, env, ctx)</code> route serves MCP 2026-07-28 clients and legacy clients that use stateless requests. You do not need separate routes or tool definitions for ordinary tools, prompts, and resources.</p>
<p><code>McpAgent</code> is deprecated and feature-frozen. Migrate existing <code>McpAgent</code> servers to the stateless handler at your earliest convenience. If a server depends on protocol sessions, RPC, pushed server-to-client requests, standalone streams, or replay, use the <a href="/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/">migration guide</a> to design stateless equivalents and run both routes while clients transition.</p>
<h4 id="2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2-migrate-existing-sdk-v1-servers">Migrate existing SDK v1 servers</h4>
<p>Upgrade the Agents SDK:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Move ordinary SDK v1 server definitions into an SDK v2 factory and serve them with <code>createMcpHandler</code>. The handler's default legacy compatibility means most stateless deployments need only one route.</p>
<p>If an existing <code>McpAgent</code> server still needs sessionful features, add the stateless path beside it. Use <code>isLegacyRequest()</code> to send only legacy traffic to the existing route:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17682.md")</div>
<p>Migrate the remaining sessionful features, allow existing sessions to drain, then remove the legacy route. Refer to <a href="/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/">Migrate to MCP SDK v2</a> for package changes, compatibility limits, and rollout steps.</p>
<h4 id="2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2-deprecations-in-v0-20-0">Deprecations in v0.20.0</h4>
<p>This release deprecates the following Agents SDK APIs:</p>
<table>
<thead>
<tr>
<th>Deprecated API</th>
<th>Replacement</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>McpAgent</code></td>
<td>Use an SDK v2 factory with <code>createMcpHandler</code> for stateless servers. Use the migration guide to replace stateful features before removing a legacy route.</td>
<td>Feature-frozen. No removal version is announced.</td>
</tr>
<tr>
<td><code>createMcpHandler(v1Server, options)</code></td>
<td>Move the server to an SDK v2 factory and call <code>createMcpHandler(factory, options)</code>. Use <code>createLegacyMcpHandler</code> only as a temporary bridge for sessionful features.</td>
<td>Scheduled for removal in the next major version.</td>
</tr>
<tr>
<td><code>MCPClientManager.callTool(params, resultSchema, options)</code> and the equivalent <code>withX402Client</code> overload</td>
<td>Use <code>callTool(params, options)</code> or <code>callTool(confirm, params, options)</code>.</td>
<td>Compatibility overload. No removal version is announced.</td>
</tr>
</tbody>
</table>
<p>The MCP 2026-07-28 draft separately deprecates Roots, Sampling, Logging, the old HTTP+SSE transport, and Dynamic Client Registration.</p>


<h2 id="agents-sdk-packages-support-ai-sdk-v6-and-v7"><a href="/changelog/post/2026-07-23-ai-sdk-v6-v7-support/">Agents SDK packages support AI SDK v6 and v7</a></h2>
<p><em>2026-07-23</em></p>
<p>The <code>agents</code>, <code>@cloudflare/ai-chat</code>, <code>@cloudflare/codemode</code>, and <code>@cloudflare/think</code> packages now support AI SDK v6 and v7. Existing applications can remain on v6 when updating these packages. Applications can also adopt v7 without changing the Cloudflare Agents APIs they use.</p>
<p>The supported peer ranges are <code>ai@^6 || ^7</code> and <code>@ai-sdk/react@^3 || ^4</code>. Use matching major versions: pair AI SDK v6 with <code>@ai-sdk/react</code> v3, or pair AI SDK v7 with <code>@ai-sdk/react</code> v4.</p>
<p>To install the latest packages with AI SDK v7:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Think normalizes streaming, tool completion events, and telemetry across both AI SDK versions. Existing v6 applications do not need to migrate these integrations before updating Think.</p>
<p>For setup and usage details, refer to the <a href="/agents/harnesses/think/">Think documentation</a>.</p>


<h2 id="agents-sdk-reduces-mcp-schema-conversion-adds-exposure-controls-for-mcp-in-think-and-code-mode-sdk-adds-direct-host-apis"><a href="/changelog/post/2026-07-22-mcp-codemode-updates/">Agents SDK reduces MCP schema conversion, adds exposure controls for MCP in Think and Code Mode SDK adds direct host APIs</a></h2>
<p><em>2026-07-22</em></p>
<p>This release reduces repeated MCP schema conversion and adds an opt-out for Think's automatic MCP tool exposure. It also lets non-AI-SDK hosts invoke the durable Code Mode runtime directly.</p>
<h4 id="2026-07-22-mcp-codemode-updates-control-direct-mcp-tool-exposure-in-think">Control direct MCP tool exposure in Think</h4>
<p>Agents SDK MCP clients now reuse converted input and output schemas while a live connection keeps the same tool catalog. This avoids converting every MCP JSON Schema to Zod again for each model turn.</p>
<p><code>@cloudflare/think</code> also adds <code>includeMcpTools</code>. Set it to <code>false</code> when you expose MCP tools through Code Mode or another mechanism outside Think's automatic tool set:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17679.md")</div>
<p>This setting skips Think's automatic <code>getAITools()</code> call. MCP registration, restoration, discovery, raw catalog access, direct calls, and Code Mode connectors continue to work.</p>
<p>Use <a href="/agents/model-context-protocol/apis/client-api/#thismcplisttools"><code>listTools()</code></a> when you only need the raw MCP catalog. For connector setup, refer to <a href="/agents/tools/codemode/mcp/">Use MCP tools with Code Mode</a>.</p>
<h4 id="2026-07-22-mcp-codemode-updates-invoke-the-code-mode-runtime-without-the-ai-sdk">Invoke the Code Mode runtime without the AI SDK</h4>
<p><code>@cloudflare/codemode@latest</code> adds <code>execute()</code>, <code>search()</code>, and <code>describe()</code> to the durable runtime handle. MCP servers and other hosts can now execute code and discover connector methods without adapting the runtime to an AI SDK tool.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17680.md")</div>
<p>Search and describe results include <code>requiresApproval: true</code> for protected connector methods. Resolve a paused execution with the existing <code>approve()</code> and <code>reject()</code> methods.</p>
<p>For setup and exact method types, refer to <a href="/agents/tools/codemode/durable-runtime/">Create a durable Code Mode runtime</a> and the <a href="/agents/tools/codemode/api-reference/">Code Mode API reference</a>.</p>
<h4 id="2026-07-22-mcp-codemode-updates-upgrade">Upgrade</h4>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest" aria-label="Copy to clipboard">Copy</button></div></div>


<h2 id="agents-can-respond-to-mcp-elicitation-requests"><a href="/changelog/post/2026-07-13-mcp-client-elicitation/">Agents can respond to MCP elicitation requests</a></h2>
<p><em>2026-07-13</em></p>
<p>Agents connected to Model Context Protocol (MCP) servers with <a href="/agents/model-context-protocol/apis/client-api/"><code>addMcpServer</code></a> can now handle <a href="https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation">elicitation</a> requests.</p>
<p>Elicitation lets an MCP server request user input while it handles a tool call. Form mode collects structured, non-sensitive data. URL mode asks for consent before opening an out-of-band flow, such as third-party authorization or payment.</p>
<pre tabindex="0"><code class="language-mermaid">sequenceDiagram&#10;    participant User&#10;    participant Agent as Agent (MCP client)&#10;    participant Server as MCP server&#10;    participant Browser&#10;&#10;    Server-&gt;&gt;Agent: elicitation/create&#10;    Agent-&gt;&gt;User: Show server, reason, and input or URL&#10;    User-&gt;&gt;Agent: Submit, open, decline, or cancel&#10;    Agent-&gt;&gt;Browser: Open URL after consent (URL mode)&#10;    Agent-&gt;&gt;Server: accept, decline, or cancel&#10;    Server--&gt;&gt;Agent: Optional URL completion notification&#10;</code></pre>
<p>Register a handler for each mode your Agent supports in <code>onStart()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17678.md")</div>
<p>Connections advertise only the modes with configured handlers. An Agent without handlers advertises no elicitation capability, which lets the server use its fallback. The SDK stores the advertised modes with each MCP server registration so they survive Durable Object hibernation. Callback functions remain in memory and reattach when <code>onStart()</code> runs.</p>
<p>For implementation details and a browser forwarding pattern, refer to <a href="/agents/model-context-protocol/apis/client-api/#elicitation">MCP client elicitation</a>. The <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp-client"><code>mcp-client</code></a> and <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp-elicitation"><code>mcp-elicitation</code></a> examples implement both sides.</p>
<h4 id="2026-07-13-mcp-client-elicitation-upgrade">Upgrade</h4>
<p>To update to this release:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest" aria-label="Copy to clipboard">Copy</button></div></div>


<h2 id="agents-sdk-adds-background-sub-agents-and-a-unified-turn-entry-point"><a href="/changelog/post/2026-06-26-agents-sdk-v0.17.0/">Agents SDK adds background sub-agents and a unified turn entry point</a></h2>
<p><em>2026-06-26</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> makes it easier to run long work in the background, drive turns through one entry point, and keep chat agents working through deploys, evictions, and reconnects.</p>
<p>This release adds first-class detached (background) sub-agent runs with live progress and durable milestones, a single <code>runTurn</code> turn-admission entry point, and a large round of recovery and reliability fixes that continue converging <code>@cloudflare/think</code> and <code>@cloudflare/ai-chat</code> onto one model.</p>
<h4 id="2026-06-26-agents-sdk-v0.17.0-background-sub-agents-with-progress-and-milestones">Background sub-agents with progress and milestones</h4>
<p><code>runAgentTool</code> can now dispatch a sub-agent without blocking the calling turn. A detached run returns a handle immediately and is owned by a durable, eviction-surviving backbone instead of being abandoned when the dispatching turn ends.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17675.md")</div>
<p>Highlights:</p>
<ul>
<li><strong>Durable, exactly-once-on-the-happy-path completion</strong> via a warm fast path plus a self-scheduling reconcile backbone that survives eviction and deploys.</li>
<li><strong>Bounded.</strong> An absolute <code>maxBudgetMs</code> ceiling (default 24h) and <code>cancelAgentTool(runId)</code> keep abandoned runs from holding a concurrency slot forever.</li>
<li><strong><code>detached: { notify: true }</code></strong> lets a finished background run inject a message back into the chat so the model reacts to the result — no hand-wired <code>onFinish</code> needed.</li>
</ul>
<p>Sub-agents can also report mid-run progress that rides their own turn stream back to the parent's connected clients:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17676.md")</div>
<p>Progress surfaces on <code>AgentToolRunState.progress</code> via <code>useAgentToolEvents</code>, so a background-runs tray can render a live bar without drilling in, and the latest snapshot is persisted for inspection after eviction. Naming a <code>milestone</code> promotes a signal to a durable, replayable row, and <code>detached: { onMilestones }</code> can surface a milestone as a synthetic chat message (<code>&quot;narrate&quot;</code> for a cheap status line, or <code>&quot;react&quot;</code> to drive a model turn).</p>
<h4 id="2026-06-26-agents-sdk-v0.17.0-one-entry-point-for-turns-runturn">One entry point for turns: <code>runTurn</code></h4>
<p><code>@cloudflare/think</code> adds a public <code>runTurn(options)</code> facade that unifies turn admission behind a single <code>mode</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17677.md")</div>
<p><code>stream</code> mode accepts array and function inputs to match <code>wait</code> mode, and all entry points now route through a shared internal admission path that throws a clear error on nested blocking admissions that previously could deadlock.</p>
<h4 id="2026-06-26-agents-sdk-v0.17.0-recovery-and-reliability">Recovery and reliability</h4>
<p>A large part of this release continues hardening recovery and converging <code>@cloudflare/think</code> and <code>@cloudflare/ai-chat</code> onto one model:</p>
<ul>
<li><strong>Stream stall watchdog.</strong> <code>AIChatAgent</code> can detect and recover from a hung model/transport stream via the opt-in <code>chatStreamStallTimeoutMs</code> watchdog. With <code>chatRecovery</code> enabled the stall routes into the same bounded-recovery machinery a deploy or eviction uses; otherwise it surfaces as a terminal stream error so the spinner clears.</li>
<li><strong>Interrupted tool-call repair.</strong> <code>AIChatAgent</code> now repairs a transcript with a dead server-tool call before re-entering inference (parity with <code>@cloudflare/think</code>), so a recovered turn no longer fails with <code>AI_MissingToolResultsError</code>. An overridable <code>repairInterruptedToolPart(part)</code> hook lets apps customize the repaired shape.</li>
<li><strong>Stuck status after reconnect.</strong> Fixed AI SDK <code>status</code> getting stuck when a reconnect races a turn that has been accepted but has not started streaming yet, so the UI now renders the in-flight turn instead of settling on <code>ready</code>.</li>
<li><strong>Live &quot;recovering…&quot; on connect.</strong> <code>AIChatAgent</code> now replays the recovering status to a client that connects mid-recovery, so <code>useAgentChat</code>'s <code>isRecovering</code> reflects in-progress recovery immediately instead of appearing frozen.</li>
<li><strong>Terminal connection failures.</strong> The client stops reconnecting on terminal WebSocket close events and exposes them via <code>connectionError</code> / <code>onConnectionError</code> on <code>AgentClient</code>, <code>useAgent</code>, and <code>useAgentChat</code>.</li>
<li><strong>Agent-tool child recovery.</strong> A healthy long-running sub-agent run is no longer abandoned as <code>interrupted</code> after a deploy (both <code>@cloudflare/think</code> and <code>AIChatAgent</code>).</li>
<li><strong>Workflows from sub-agent facets.</strong> Agent Workflows can now start from sub-agent facets, with callbacks and Workflow RPC routed back to the originating facet.</li>
<li>Plus forward-progress crediting convergence, broadcast-first give-up ordering, an event-driven auto-continuation barrier, and structured row-size compaction in <code>AIChatAgent</code>.</li>
</ul>
<h4 id="2026-06-26-agents-sdk-v0.17.0-other-improvements">Other improvements</h4>
<ul>
<li><strong>Shared chat React core.</strong> A new <code>agents/chat/react</code> entry exposes <code>useAgentChat</code>, transport helpers, and shared wire types, with <code>syncMessagesToServer</code> for server-authoritative transcript storage. <code>@cloudflare/think/react</code> and <code>@cloudflare/ai-chat/react</code> are now thin wrappers over it.</li>
<li><strong>Optional <code>ai</code> peer.</strong> The root <code>agents</code> and <code>@cloudflare/codemode</code> runtimes no longer reference AI SDK types, so they bundle without <code>ai</code> / <code>zod</code> installed; AI-specific entry points still require the peer when imported. <code>just-bash</code> likewise moves to an optional peer used only by the skills bash runner.</li>
<li><strong>Code Mode.</strong> The default <code>DynamicWorkerExecutor</code> timeout increases from 30s to 60s, executions now dispose the dynamically-loaded Worker and its RPC stub after each run (fixing a flaky isolate-shutdown assertion), connector imports are cleaned up, and the outer MCP tool-call context is passed to <code>openApiMcpServer</code> request callbacks.</li>
<li><strong>Voice.</strong> Voice turns now support AI SDK <code>fullStream</code> responses (and warn when <code>textStream</code> is used).</li>
<li><strong>MCP.</strong> <code>McpAgent</code> server-to-client requests can now be sent from callbacks that do not inherit the agent's async context, including callbacks reached through Worker Loader RPC.</li>
<li><strong>Experimental: server actions and channels.</strong> This release lays groundwork for guarded server actions (<code>action()</code> / <code>getActions()</code> with a durable replay ledger and approvals) and a unified channels surface (<code>configureChannels()</code>, <code>deliverNotice()</code>). Both are experimental and their APIs may change, so we don't recommend depending on them yet.</li>
</ul>
<h4 id="2026-06-26-agents-sdk-v0.17.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/harnesses/think/">Think documentation</a>, <a href="/agents/tools/codemode/">Code Mode documentation</a>, and <a href="/agents/">Agents documentation</a> for more information.</p>


<h2 id="agents-sdk-improves-browser-automation-code-execution-and-recovery"><a href="/changelog/post/2026-06-16-agents-sdk-v0.16.1/">Agents SDK improves browser automation, code execution, and recovery</a></h2>
<p><em>2026-06-16</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> makes it easier to build agents that can safely interact with real systems and keep working through interruptions.</p>
<p>Agents can now browse websites through Browser Run, write code against external tools through Code Mode, use client-provided tools when delegating to Think sub-agents, and recover more reliably from deploys, Durable Object evictions, and connection churn.</p>
<h4 id="2026-06-16-agents-sdk-v0.16.1-safer-browser-automation">Safer browser automation</h4>
<p>Agents can now use <a href="/browser-run/">Browser Run</a> through a single durable <code>browser_execute</code> tool. Instead of choosing from a fixed list of actions, the model writes code against the Chrome DevTools Protocol (CDP) and can inspect pages, capture screenshots, read rendered content, debug frontend behavior, and interact with live browser sessions.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17671.md")</div>
<p>Browser sessions can be one-time, reused, or promoted from one-time to persistent during a run. This is useful when an agent needs a human to log in, complete MFA, or approve a sensitive action. The run can pause, keep the same tabs and cookies, and resume after approval.</p>
<p>The browser tools also add Live View URLs, optional session recording, and quick actions such as <code>browser_markdown</code>, <code>browser_extract</code>, <code>browser_links</code>, and <code>browser_scrape</code> for one-shot browsing tasks.</p>
<h4 id="2026-06-16-agents-sdk-v0.16.1-resumable-code-execution-with-approvals">Resumable code execution with approvals</h4>
<p>Code Mode now uses <code>createCodemodeRuntime</code>, connectors, and a durable execution log. This lets you give a model one <code>codemode</code> tool instead of a large prompt full of tool definitions. The model can discover the capabilities it needs, write code against typed globals, and reuse saved snippets.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17672.md")</div>
<p>When the code reaches an approval-gated action, the runtime pauses execution and returns a pending approval. After approval, completed calls replay from the durable log, the approved action runs, and the same code continues. This makes it practical to build agents that create issues, update external systems, or perform other side effects without custom pause-and-resume logic for every tool.</p>
<h4 id="2026-06-16-agents-sdk-v0.16.1-better-think-delegation">Better Think delegation</h4>
<p>Think sub-agents can now use client-defined tools over the RPC <code>chat()</code> path. A parent agent can pass tool schemas with <code>clientTools</code> and resolve tool calls through <code>onClientToolCall</code>. This lets delegated agents use caller-provided capabilities without requiring a browser WebSocket.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17673.md")</div>
<p>Think Workflows also improve <code>step.prompt()</code>. A prompt step now runs a full agentic turn before returning structured output, so the agent can call tools before producing the typed result. This makes Workflow steps more useful for durable triage, research, and approval flows.</p>
<p>The unified Think execute tool can also include <code>cdp.*</code> browser capabilities alongside <code>state.*</code> and <code>tools.*</code> when Browser Run is bound.</p>
<h4 id="2026-06-16-agents-sdk-v0.16.1-voice-output-device-selection">Voice output device selection</h4>
<p>Voice clients can route assistant audio to a specific output device. Use <code>outputDeviceId</code> with <code>useVoiceAgent</code>, or call <code>client.setOutputDevice()</code> from the framework-agnostic client.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17674.md")</div>
<p>Browsers without speaker-selection support continue playing through the default output device and report a non-fatal <code>outputDeviceError</code>.</p>
<h4 id="2026-06-16-agents-sdk-v0.16.1-reliability-fixes">Reliability fixes</h4>
<p>This release includes several fixes for production agents:</p>
<ul>
<li><code>useAgent</code> and <code>AgentClient</code> handle WebSocket replacement more reliably during reconnects and configuration changes.</li>
<li>Chat stream replay is more reliable after reconnects, deploys, and provider errors.</li>
<li>Fiber recovery continues across multi-pass scans and backs off when recovery hooks keep failing.</li>
<li>Agent teardown continues even when the request that started teardown is canceled.</li>
<li>Large session histories use byte-budgeted reads to reduce memory pressure during startup.</li>
</ul>
<h4 id="2026-06-16-agents-sdk-v0.16.1-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/tools/codemode/">Code Mode documentation</a>, <a href="/agents/tools/browser/">Browser tools documentation</a>, <a href="/agents/harnesses/think/tools/">Think tools documentation</a>, and <a href="/agents/communication-channels/voice/">Voice documentation</a> for more information.</p>


<h2 id="introducing-glm-5-2-on-workers-ai"><a href="/changelog/post/2026-06-16-glm-5.2-workers-ai/">Introducing GLM-5.2 on Workers AI</a></h2>
<p><em>2026-06-16</em></p>
<p>We are excited to announce <strong>GLM-5.2</strong> on Workers AI, Z.ai's flagship agentic coding model.</p>
<p><a href="/workers-ai/models/glm-5.2/"><code>@cf/zai-org/glm-5.2</code></a> is a text generation model built for agentic coding workflows. With function calling and reasoning support, it can handle long codebases, multi-step planning, and tool-augmented agents.</p>
<p><strong>Key features and use cases:</strong></p>
<ul>
<li><strong>Agentic coding</strong>: Designed for autonomous coding tasks, long-horizon planning, and complex software engineering workflows</li>
<li><strong>Large context window</strong>: GLM-5.2 supports up to a 1,048,576 token context window. Workers AI is launching the model with a 262,144 token context window and plans to increase this in the future</li>
<li><strong>Function calling</strong>: Build agents that invoke tools and APIs across multiple conversation turns</li>
<li><strong>Reasoning</strong>: Tackles complex problem-solving and step-by-step reasoning tasks</li>
</ul>
<p>Use GLM-5.2 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, or <a href="/ai-gateway/">AI Gateway</a>.</p>
<p>Pricing is available on the <a href="/workers-ai/models/glm-5.2/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>


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


<h2 id="agents-sdk-v0-8-0-readable-state-idempotent-schedules-typed-agentclient-and-zod-4"><a href="/changelog/post/2026-03-23-agents-sdk-v0.8.0/">Agents SDK v0.8.0: readable state, idempotent schedules, typed AgentClient, and Zod 4</a></h2>
<p><em>2026-03-23</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> exposes agent state as a readable property, prevents duplicate schedule rows across Durable Object restarts, brings full TypeScript inference to <code>AgentClient</code>, and migrates to Zod 4.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-readable-state-on-useagent-and-agentclient">Readable <code>state</code> on <code>useAgent</code> and <code>AgentClient</code></h4>
<p>Both <code>useAgent</code> (React) and <code>AgentClient</code> (vanilla JS) now expose a <code>state</code> property that reflects the current agent state. Previously, reading state required manually tracking it through the <code>onStateUpdate</code> callback.</p>
<p><strong>React (<code>useAgent</code>)</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17655.md")</div>
<p><code>agent.state</code> is reactive — the component re-renders when state changes from either the server or a client-side <code>setState()</code> call.</p>
<p><strong>Vanilla JS (<code>AgentClient</code>)</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17656.md")</div>
<p>State starts as <code>undefined</code> and is populated when the server sends the initial state on connect (from <code>initialState</code>) or when <code>setState()</code> is called. Use optional chaining (<code>agent.state?.field</code>) for safe access. The <code>onStateUpdate</code> callback continues to work as before — the new <code>state</code> property is additive.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-idempotent-schedule">Idempotent <code>schedule()</code></h4>
<p><code>schedule()</code> now supports an <code>idempotent</code> option that deduplicates by <code>(type, callback, payload)</code>, preventing duplicate rows from accumulating when called in places that run on every Durable Object restart such as <code>onStart()</code>.</p>
<p><strong>Cron schedules are idempotent by default.</strong> Calling <code>schedule(&quot;0 * * * *&quot;, &quot;tick&quot;)</code> multiple times with the same callback, expression, and payload returns the existing schedule row instead of creating a new one. Pass <code>{ idempotent: false }</code> to override.</p>
<p>Delayed and date-scheduled types support opt-in idempotency:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17657.md")</div>
<p>Two new warnings help catch common foot-guns:</p>
<ul>
<li>Calling <code>schedule()</code> inside <code>onStart()</code> without <code>{ idempotent: true }</code> emits a <code>console.warn</code> with actionable guidance (once per callback; skipped for cron and when <code>idempotent</code> is set explicitly).</li>
<li>If an alarm cycle processes 10 or more stale one-shot rows for the same callback, the SDK emits a <code>console.warn</code> and a <code>schedule:duplicate_warning</code> diagnostics channel event.</li>
</ul>
<h4 id="2026-03-23-agents-sdk-v0.8.0-typed-agentclient-with-call-inference-and-stub-proxy">Typed <code>AgentClient</code> with <code>call</code> inference and <code>stub</code> proxy</h4>
<p><code>AgentClient</code> now accepts an optional agent type parameter for full type inference on RPC calls, matching the typed experience already available with <code>useAgent</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17658.md")</div>
<p>State is automatically inferred from the agent type, so <code>onStateUpdate</code> is also typed:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17659.md")</div>
<p>Existing untyped usage continues to work without changes. The RPC type utilities (<code>AgentMethods</code>, <code>AgentStub</code>, <code>RPCMethods</code>) are now exported from <code>agents/client</code> for advanced typing scenarios.
<code>agents</code>, <code>@cloudflare/ai-chat</code>, and <code>@cloudflare/codemode</code> now require <code>zod ^4.0.0</code>. Zod v3 is no longer supported.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-cloudflare-ai-chat-fixes"><code>@cloudflare/ai-chat</code> fixes</h4>
<ul>
<li><strong>Turn serialization</strong> — <code>onChatMessage()</code> and <code>_reply()</code> work is now queued so user requests, tool continuations, and <code>saveMessages()</code> never stream concurrently.</li>
<li><strong>Duplicate messages on stop</strong> — Clicking stop during an active stream no longer splits the assistant message into two entries.</li>
<li><strong>Duplicate messages after tool calls</strong> — Orphaned client IDs no longer leak into persistent storage.</li>
</ul>
<h4 id="2026-03-23-agents-sdk-v0.8.0-keepalive-and-keepalivewhile-are-no-longer-experimental"><code>keepAlive()</code> and <code>keepAliveWhile()</code> are no longer experimental</h4>
<p><code>keepAlive()</code> now uses a lightweight in-memory ref count instead of schedule rows. Multiple concurrent callers share a single alarm cycle. The <code>@experimental</code> tag has been removed from both <code>keepAlive()</code> and <code>keepAliveWhile()</code>.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-cloudflare-codemode-tanstack-ai-integration"><code>@cloudflare/codemode</code>: TanStack AI integration</h4>
<p>A new entry point <code>@cloudflare/codemode/tanstack-ai</code> adds support for <a href="https://tanstack.com/ai">TanStack AI's</a> <code>chat()</code> as an alternative to the Vercel AI SDK's <code>streamText()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17660.md")</div>
<h4 id="2026-03-23-agents-sdk-v0.8.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>


<h2 id="cloudflare-codemode-v0-2-1-mcp-barrel-export-zero-dependency-main-entry-point-and-custom-sandbox-modules"><a href="/changelog/post/2026-03-17-codemode-sdk-v0.2.1/">@cloudflare/codemode v0.2.1: MCP barrel export, zero-dependency main entry point, and custom sandbox modules</a></h2>
<p><em>2026-03-17</em></p>
<p>The latest releases of <a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a> add a new MCP barrel export, remove <code>ai</code> and <code>zod</code> as required peer dependencies from the main entry point, and give you more control over the sandbox.</p>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-new-cloudflare-codemode-mcp-export">New <code>@cloudflare/codemode/mcp</code> export</h4>
<p>A new <code>@cloudflare/codemode/mcp</code> entry point provides two functions that wrap MCP servers with Code Mode:</p>
<ul>
<li><strong><code>codeMcpServer({ server, executor })</code></strong> — wraps an existing MCP server with a single <code>code</code> tool where each upstream tool becomes a typed <code>codemode.*</code> method.</li>
<li><strong><code>openApiMcpServer({ spec, executor, request })</code></strong> — creates <code>search</code> and <code>execute</code> MCP tools from an OpenAPI spec with host-side request proxying and automatic <code>$ref</code> resolution.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17652.md")</div>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-zero-dependency-main-entry-point">Zero-dependency main entry point</h4>
<p><strong>Breaking change in v0.2.0:</strong> <code>generateTypes</code> and the <code>ToolDescriptor</code> / <code>ToolDescriptors</code> types have moved to <code>@cloudflare/codemode/ai</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17653.md")</div>
<p>The main entry point (<code>@cloudflare/codemode</code>) no longer requires the <code>ai</code> or <code>zod</code> peer dependencies. It now exports:</p>
<table>
<thead>
<tr>
<th>Export</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sanitizeToolName</code></td>
<td>Sanitize tool names into valid JS identifiers</td>
</tr>
<tr>
<td><code>normalizeCode</code></td>
<td>Normalize LLM-generated code into async arrow functions</td>
</tr>
<tr>
<td><code>generateTypesFromJsonSchema</code></td>
<td>Generate TypeScript type definitions from plain JSON Schema</td>
</tr>
<tr>
<td><code>jsonSchemaToType</code></td>
<td>Convert a single JSON Schema to a TypeScript type string</td>
</tr>
<tr>
<td><code>DynamicWorkerExecutor</code></td>
<td>Sandboxed code execution via Dynamic Worker Loader</td>
</tr>
<tr>
<td><code>ToolDispatcher</code></td>
<td>RPC target for dispatching tool calls from sandbox to host</td>
</tr>
</tbody>
</table>
<p>The <code>ai</code> and <code>zod</code> peer dependencies are now optional — only required when importing from <code>@cloudflare/codemode/ai</code>.</p>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-custom-sandbox-modules">Custom sandbox modules</h4>
<p><code>DynamicWorkerExecutor</code> now accepts an optional <code>modules</code> option to inject custom ES modules into the sandbox:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17654.md")</div>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-internal-normalization-and-sanitization">Internal normalization and sanitization</h4>
<p><code>DynamicWorkerExecutor</code> now normalizes code and sanitizes tool names internally. You no longer need to call <code>normalizeCode()</code> or <code>sanitizeToolName()</code> before passing code and functions to <code>execute()</code>.</p>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-upgrade">Upgrade</h4>
<pre tabindex="0"><code class="language-sh">npm i @cloudflare/codemode@latest&#10;</code></pre>
<p>See the <a href="/agents/tools/codemode/">Code Mode documentation</a> for the full API reference.</p>


<h2 id="real-time-file-watching-in-sandboxes"><a href="/changelog/post/2026-03-03-sandbox-watch-file-events/">Real-time file watching in Sandboxes</a></h2>
<p><em>2026-03-03</em></p>
<p><a href="/sandbox/">Sandboxes</a> now support real-time filesystem watching via <code>sandbox.watch()</code>. The method returns a <a href="https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events">Server-Sent Events</a> stream backed by native inotify, so your Worker receives <code>create</code>, <code>modify</code>, <code>delete</code>, and <code>move</code> events as they happen inside the container.</p>
<h4 id="2026-03-03-sandbox-watch-file-events-sandbox-watch-path-options"><code>sandbox.watch(path, options)</code></h4>
<p>Pass a directory path and optional filters. The returned stream is a standard <code>ReadableStream</code> you can proxy directly to a browser client or consume server-side.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17650.md")</div>
<h4 id="2026-03-03-sandbox-watch-file-events-server-side-consumption-with-parsessestream">Server-side consumption with <code>parseSSEStream</code></h4>
<p>Use <code>parseSSEStream</code> to iterate over events inside a Worker without forwarding them to a client.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17651.md")</div>
<p>Each event includes a <code>type</code> field (<code>create</code>, <code>modify</code>, <code>delete</code>, or <code>move</code>) and the affected <code>path</code>. Move events also include a <code>from</code> field with the original path.</p>
<h4 id="2026-03-03-sandbox-watch-file-events-options">Options</h4>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>recursive</code></td>
<td><code>boolean</code></td>
<td>Watch subdirectories. Defaults to <code>false</code>.</td>
</tr>
<tr>
<td><code>include</code></td>
<td><code>string[]</code></td>
<td>Glob patterns to filter events. Omit to receive all events.</td>
</tr>
</tbody>
</table>
<h4 id="2026-03-03-sandbox-watch-file-events-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i @cloudflare/sandbox@latest&#10;</code></pre>
<p>For full API details, refer to the <a href="/sandbox/api/file-watching/">Sandbox file watching reference</a>.</p>


<h2 id="agents-sdk-v0-7-0-observability-rewrite-keepalive-and-waitformcpconnections"><a href="/changelog/post/2026-03-02-agents-sdk-v0.7.0/">Agents SDK v0.7.0: Observability rewrite, keepAlive, and waitForMcpConnections</a></h2>
<p><em>2026-03-02</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> rewrites observability from scratch with <code>diagnostics_channel</code>, adds <code>keepAlive()</code> to prevent Durable Object eviction during long-running work, and introduces <code>waitForMcpConnections</code> so MCP tools are always available when <code>onChatMessage</code> runs.</p>
<h4 id="2026-03-02-agents-sdk-v0.7.0-observability-rewrite">Observability rewrite</h4>
<p>The previous observability system used <code>console.log()</code> with a custom <code>Observability.emit()</code> interface. v0.7.0 replaces it with structured events published to <a href="/workers/runtime-apis/nodejs/diagnostics-channel/">diagnostics channels</a> — silent by default, zero overhead when nobody is listening.</p>
<p>Every event has a <code>type</code>, <code>payload</code>, and <code>timestamp</code>. Events are routed to seven named channels:</p>
<table>
<thead>
<tr>
<th>Channel</th>
<th>Event types</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>agents:state</code></td>
<td><code>state:update</code></td>
</tr>
<tr>
<td><code>agents:rpc</code></td>
<td><code>rpc</code>, <code>rpc:error</code></td>
</tr>
<tr>
<td><code>agents:message</code></td>
<td><code>message:request</code>, <code>message:response</code>, <code>message:clear</code>, <code>message:cancel</code>, <code>message:error</code>, <code>tool:result</code>, <code>tool:approval</code></td>
</tr>
<tr>
<td><code>agents:schedule</code></td>
<td><code>schedule:create</code>, <code>schedule:execute</code>, <code>schedule:cancel</code>, <code>schedule:retry</code>, <code>schedule:error</code>, <code>queue:retry</code>, <code>queue:error</code></td>
</tr>
<tr>
<td><code>agents:lifecycle</code></td>
<td><code>connect</code>, <code>destroy</code></td>
</tr>
<tr>
<td><code>agents:workflow</code></td>
<td><code>workflow:start</code>, <code>workflow:event</code>, <code>workflow:approved</code>, <code>workflow:rejected</code>, <code>workflow:terminated</code>, <code>workflow:paused</code>, <code>workflow:resumed</code>, <code>workflow:restarted</code></td>
</tr>
<tr>
<td><code>agents:mcp</code></td>
<td><code>mcp:client:preconnect</code>, <code>mcp:client:connect</code>, <code>mcp:client:authorize</code>, <code>mcp:client:discover</code></td>
</tr>
</tbody>
</table>
<p>Use the typed <code>subscribe()</code> helper from <code>agents/observability</code> for type-safe access:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17645.md")</div>
<p>In production, all diagnostics channel messages are automatically forwarded to <a href="/workers/observability/logs/tail-workers/">Tail Workers</a> — no subscription code needed in the agent itself:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17646.md")</div>
<p>The custom <code>Observability</code> override interface is still supported for users who need to filter or forward events to external services.</p>
<p>For the full event reference, refer to the <a href="/agents/runtime/operations/observability/diagnostics-channels/">Diagnostics channels documentation</a>.</p>
<h4 id="2026-03-02-agents-sdk-v0.7.0-keepalive-and-keepalivewhile"><code>keepAlive()</code> and <code>keepAliveWhile()</code></h4>
<p>Durable Objects are evicted after a period of inactivity (typically 70-140 seconds with no incoming requests, WebSocket messages, or alarms). During long-running operations — streaming LLM responses, waiting on external APIs, running multi-step computations — the agent can be evicted mid-flight.</p>
<p><code>keepAlive()</code> prevents this by creating a 30-second heartbeat schedule. The alarm firing resets the inactivity timer. Returns a disposer function that cancels the heartbeat when called.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17647.md")</div>
<p><code>keepAliveWhile()</code> wraps an async function with automatic cleanup — the heartbeat starts before the function runs and stops when it completes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17648.md")</div>
<p>Key details:</p>
<ul>
<li><strong>Multiple concurrent callers</strong> — Each <code>keepAlive()</code> call returns an independent disposer. Disposing one does not affect others.</li>
<li><strong>AIChatAgent built-in</strong> — <code>AIChatAgent</code> automatically calls <code>keepAlive()</code> during streaming responses. You do not need to add it yourself.</li>
<li><strong>Uses the scheduling system</strong> — The heartbeat does not conflict with your own schedules. It shows up in <code>getSchedules()</code> if you need to inspect it.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17644.md")</aside>
<p>For the full API reference and when-to-use guidance, refer to <a href="/agents/runtime/execution/schedule-tasks/#keeping-the-agent-alive">Schedule tasks — Keeping the agent alive</a>.</p>
<h4 id="2026-03-02-agents-sdk-v0.7.0-waitformcpconnections"><code>waitForMcpConnections</code></h4>
<p><code>AIChatAgent</code> now waits for MCP server connections to settle before calling <code>onChatMessage</code>. This ensures <code>this.mcp.getAITools()</code> returns the full set of tools, especially after Durable Object hibernation when connections are being restored in the background.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17649.md")</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>{ timeout: 10_000 }</code></td>
<td>Wait up to 10 seconds (default)</td>
</tr>
<tr>
<td><code>{ timeout: N }</code></td>
<td>Wait up to <code>N</code> milliseconds</td>
</tr>
<tr>
<td><code>true</code></td>
<td>Wait indefinitely until all connections ready</td>
</tr>
<tr>
<td><code>false</code></td>
<td>Do not wait (old behavior before 0.2.0)</td>
</tr>
</tbody>
</table>
<p>For lower-level control, call <code>this.mcp.waitForConnections()</code> directly inside <code>onChatMessage</code> instead.</p>
<h4 id="2026-03-02-agents-sdk-v0.7.0-other-improvements">Other improvements</h4>
<ul>
<li><strong>MCP deduplication by name and URL</strong> — <code>addMcpServer</code> with HTTP transport now deduplicates on both server name and URL. Calling it with the same name but a different URL creates a new connection. URLs are normalized before comparison (trailing slashes, default ports, hostname case).</li>
<li><strong><code>callbackHost</code> optional for non-OAuth servers</strong> — <code>addMcpServer</code> no longer requires <code>callbackHost</code> when connecting to MCP servers that do not use OAuth.</li>
<li><strong>MCP URL security</strong> — Server URLs are validated before connection to prevent SSRF. Private IP ranges, loopback addresses, link-local addresses, and cloud metadata endpoints are blocked.</li>
<li><strong>Custom denial messages</strong> — <code>addToolOutput</code> now supports <code>state: &quot;output-error&quot;</code> with <code>errorText</code> for custom denial messages in human-in-the-loop tool approval flows.</li>
<li><strong><code>requestId</code> in chat options</strong> — <code>onChatMessage</code> options now include a <code>requestId</code> for logging and correlating events.</li>
</ul>
<h4 id="2026-03-02-agents-sdk-v0.7.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>


<h2 id="agents-sdk-v0-6-0-rpc-transport-for-mcp-optional-oauth-hardened-schema-conversion-and-cloudflare-ai-chat-fixes"><a href="/changelog/post/2026-02-25-agents-sdk-v0.6.0/">Agents SDK v0.6.0: RPC transport for MCP, optional OAuth, hardened schema conversion, and @cloudflare/ai-chat fixes</a></h2>
<p><em>2026-02-25</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> lets you define an Agent and an McpAgent in the same Worker and connect them over RPC — no HTTP, no network overhead. It also makes OAuth opt-in for simple MCP connections, hardens the schema converter for production workloads, and ships a batch of <code>@cloudflare/ai-chat</code> reliability fixes.</p>
<h4 id="2026-02-25-agents-sdk-v0.6.0-rpc-transport-for-mcp">RPC transport for MCP</h4>
<p>You can now connect an Agent to an McpAgent in the same Worker using a Durable Object binding instead of an HTTP URL. The connection stays entirely within the Cloudflare runtime — no network round-trips, no serialization overhead.</p>
<p>Pass the Durable Object namespace directly to <code>addMcpServer</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17642.md")</div>
<p>The <code>addMcpServer</code> method now accepts <code>string | DurableObjectNamespace</code> as the second parameter with full TypeScript overloads, so HTTP and RPC paths are type-safe and cannot be mixed.</p>
<p>Key capabilities:</p>
<ul>
<li><strong>Hibernation support</strong> — RPC connections survive Durable Object hibernation automatically. The binding name and props are persisted to storage and restored on wake-up, matching the behavior of HTTP MCP connections.</li>
<li><strong>Deduplication</strong> — Calling <code>addMcpServer</code> with the same server name returns the existing connection instead of creating duplicates. Connection IDs are stable across hibernation restore.</li>
<li><strong>Smaller surface area</strong> — The RPC transport internals have been rewritten and reduced from 609 lines to 245 lines. <code>RPCServerTransport</code> now uses <code>JSONRPCMessageSchema</code> from the MCP SDK for validation instead of hand-written checks.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17641.md")</aside>
<h4 id="2026-02-25-agents-sdk-v0.6.0-optional-oauth-for-mcp-connections">Optional OAuth for MCP connections</h4>
<p><code>addMcpServer()</code> no longer eagerly creates an OAuth provider for every connection. For servers that do not require authentication, a simple call is all you need:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17643.md")</div>
<p>If the server responds with a 401, the SDK throws a clear error: <code>&quot;This MCP server requires OAuth authentication. Provide callbackHost in addMcpServer options to enable the OAuth flow.&quot;</code> The restore-from-storage flow also handles missing callback URLs gracefully, skipping auth provider creation for non-OAuth servers.</p>
<h4 id="2026-02-25-agents-sdk-v0.6.0-hardened-json-schema-to-typescript-converter">Hardened JSON Schema to TypeScript converter</h4>
<p>The schema converter used by <code>generateTypes()</code> and <code>getAITools()</code> now handles edge cases that previously caused crashes in production:</p>
<ul>
<li><strong>Depth and circular reference guards</strong> — Prevents stack overflows on recursive or deeply nested schemas</li>
<li><strong><code>$ref</code> resolution</strong> — Supports internal JSON Pointers (<code>#/definitions/...</code>, <code>#/$defs/...</code>, <code>#</code>)</li>
<li><strong>Tuple support</strong> — <code>prefixItems</code> (JSON Schema 2020-12) and array <code>items</code> (draft-07)</li>
<li><strong>OpenAPI 3.0 <code>nullable: true</code></strong> — Supported across all schema branches</li>
<li><strong>Per-tool error isolation</strong> — One malformed schema cannot crash the full pipeline in <code>generateTypes()</code> or <code>getAITools()</code></li>
<li><strong>Missing <code>inputSchema</code> fallback</strong> — <code>getAITools()</code> falls back to <code>{ type: &quot;object&quot; }</code> instead of throwing</li>
</ul>
<h4 id="2026-02-25-agents-sdk-v0.6.0-cloudflare-ai-chat-fixes"><code>@cloudflare/ai-chat</code> fixes</h4>
<ul>
<li><strong>Tool denial flow</strong> — Denied tool approvals (<code>approved: false</code>) now transition to <code>output-denied</code> with a <code>tool_result</code>, fixing Anthropic provider compatibility. Custom denial messages are supported via <code>state: &quot;output-error&quot;</code> and <code>errorText</code>.</li>
<li><strong>Abort/cancel support</strong> — Streaming responses now properly cancel the reader loop when the abort signal fires and send a done signal to the client.</li>
<li><strong>Duplicate message persistence</strong> — <code>persistMessages()</code> now reconciles assistant messages by content and order, preventing duplicate rows when clients resend full history.</li>
<li><strong><code>requestId</code> in <code>OnChatMessageOptions</code></strong> — Handlers can now send properly-tagged error responses for pre-stream failures.</li>
<li><strong><code>redacted_thinking</code> preservation</strong> — The message sanitizer no longer strips Anthropic <code>redacted_thinking</code> blocks.</li>
<li><strong><code>/get-messages</code> reliability</strong> — Endpoint handling moved from a prototype <code>onRequest()</code> override to a constructor wrapper, so it works even when users override <code>onRequest</code> without calling <code>super.onRequest()</code>.</li>
<li><strong>Client tool APIs undeprecated</strong> — <code>createToolsFromClientSchemas</code>, <code>clientTools</code>, <code>AITool</code>, <code>extractClientToolSchemas</code>, and the <code>tools</code> option on <code>useAgentChat</code> are restored for SDK use cases where tools are defined dynamically at runtime.</li>
<li><strong><code>jsonSchema</code> initialization</strong> — Fixed <code>jsonSchema not initialized</code> error when calling <code>getAITools()</code> in <code>onChatMessage</code>.</li>
</ul>
<h4 id="2026-02-25-agents-sdk-v0.6.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>


<h2 id="backup-and-restore-api-for-sandbox-sdk"><a href="/changelog/post/2026-02-23-sandbox-backup-restore-api/">Backup and restore API for Sandbox SDK</a></h2>
<p><em>2026-02-23</em></p>
<p><a href="/sandbox/">Sandboxes</a> now support <code>createBackup()</code> and <code>restoreBackup()</code> methods for creating and restoring point-in-time snapshots of directories.</p>
<p>This allows you to restore environments quickly. For instance, in order to develop in a sandbox, you may need to include a user's codebase and run a build step.
Unfortunately <code>git clone</code> and <code>npm install</code> can take minutes, and you don't want to run these steps every time the user starts their sandbox.</p>
<p>Now, after the initial setup, you can just call <code>createBackup()</code>, then <code>restoreBackup()</code> the next time this environment is needed. This makes it practical to pick up exactly
where a user left off, even after days of inactivity, without repeating expensive setup steps.</p>
<pre tabindex="0"><code class="language-ts">const sandbox = getSandbox(env.Sandbox, &quot;my-sandbox&quot;);&#10;&#10;// Make non-trivial changes to the file system&#10;await sandbox.gitCheckout(endUserRepo, { targetDir: &quot;/workspace&quot; });&#10;await sandbox.exec(&quot;npm install&quot;, { cwd: &quot;/workspace&quot; });&#10;&#10;// Create a point-in-time backup of the directory&#10;const backup = await sandbox.createBackup({ dir: &quot;/workspace&quot; });&#10;&#10;// Store the handle for later use&#10;await env.KV.put(`backup:${userId}`, JSON.stringify(backup));&#10;&#10;// ... in a future session...&#10;&#10;// Restore instead of re-cloning and reinstalling&#10;await sandbox.restoreBackup(backup);&#10;</code></pre>
<p>Backups are stored in <a href="/r2">R2</a> and can take advantage of <a href="/sandbox/guides/backup-restore/#configure-r2-lifecycle-rules-for-automatic-cleanup">R2 object lifecycle rules</a> to ensure they do not persist forever.</p>
<p>Key capabilities:</p>
<ul>
<li><strong>Persist and reuse across sandbox sessions</strong> — Easily store backup handles in KV, D1, or Durable Object storage for use in subsequent sessions</li>
<li><strong>Usable across multiple instances</strong> — Fork a backup across many sandboxes for parallel work</li>
<li><strong>Named backups</strong> — Provide optional human-readable labels for easier management</li>
<li><strong>TTLs</strong> — Set time-to-live durations so backups are automatically removed from storage once they are no longer needed</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17640.md")</aside>
<p>To get started, refer to the <a href="/sandbox/guides/backup-restore/">backup and restore guide</a> for setup instructions and usage patterns, or the <a href="/sandbox/api/backups/">Backups API reference</a> for full method documentation.</p>


<h2 id="cloudflare-codemode-v0-1-0-a-new-runtime-agnostic-modular-architecture"><a href="/changelog/post/2026-02-20-codemode-sdk-rewrite/">@cloudflare/codemode v0.1.0: a new runtime agnostic modular architecture</a></h2>
<p><em>2026-02-20</em></p>
<p>The <a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a> package has been rewritten into a modular, runtime-agnostic SDK.</p>
<p><a href="https://blog.cloudflare.com/code-mode/">Code Mode</a> enables LLMs to write and execute code that orchestrates your tools, instead of calling them one at a time. This can (and does) yield significant token savings, reduces context window pressure and improves overall model performance on a task.</p>
<p>The new <code>Executor</code> interface is runtime agnostic and comes with a prebuilt <code>DynamicWorkerExecutor</code> to run generated code in a <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker Loader</a>.</p>
<h4 id="2026-02-20-codemode-sdk-rewrite-breaking-changes">Breaking changes</h4>
<ul>
<li>Removed <code>experimental_codemode()</code> and <code>CodeModeProxy</code> — the package no longer owns an LLM call or model choice</li>
<li>New import path: <code>createCodeTool()</code> is now exported from <code>@cloudflare/codemode/ai</code></li>
</ul>
<h4 id="2026-02-20-codemode-sdk-rewrite-new-features">New features</h4>
<ul>
<li><strong><code>createCodeTool()</code></strong> — Returns a standard AI SDK <code>Tool</code> to use in your AI agents.</li>
<li><strong><code>Executor</code> interface</strong> — Minimal <code>execute(code, fns)</code> contract. Implement for any code sandboxing primitive or runtime.</li>
</ul>
<h4 id="2026-02-20-codemode-sdk-rewrite-dynamicworkerexecutor"><code>DynamicWorkerExecutor</code></h4>
<p>Runs code in a <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a>. It comes with the following features:</p>
<ul>
<li><strong>Network isolation</strong> — <code>fetch()</code> and <code>connect()</code> blocked by default (<code>globalOutbound: null</code>) when using <code>DynamicWorkerExecutor</code></li>
<li><strong>Console capture</strong> — <code>console.log/warn/error</code> captured and returned in <code>ExecuteResult.logs</code></li>
<li><strong>Execution timeout</strong> — Configurable via <code>timeout</code> option (default 30s)</li>
</ul>
<h4 id="2026-02-20-codemode-sdk-rewrite-usage">Usage</h4>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17638.md")</div>
<h4 id="2026-02-20-codemode-sdk-rewrite-wrangler-configuration">Wrangler configuration</h4>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17639.md")</div>
<p>See the <a href="/agents/tools/codemode/">Code Mode documentation</a> for full API reference and examples.</p>
<h4 id="2026-02-20-codemode-sdk-rewrite-upgrade">Upgrade</h4>
<pre tabindex="0"><code class="language-sh">npm i @cloudflare/codemode@latest&#10;</code></pre>


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
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 2</span><a class="pagination-next" rel="next" href="/changelog/product/agents/2/">Next</a></nav>
