<h1 id="changelog">Changelog</h1>

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


<h2 id="vectorize-indexes-now-support-up-to-20-million-vectors"><a href="/changelog/post/2026-08-04-index-capacity-20-million/">Vectorize indexes now support up to 20 million vectors</a></h2>
<p><em>2026-08-04</em></p>
<p>You can now store up to 20 million vectors in a single Vectorize index, doubling the previous limit of 10 million vectors. This enables larger-scale semantic search, recommendation systems, and retrieval-augmented generation (RAG) applications without splitting data across multiple indexes.</p>
<p>Vectorize continues to support indexes with up to 1,536 dimensions per vector at 32-bit precision. Refer to the <a href="/vectorize/platform/limits/">Vectorize limits documentation</a> for complete details.</p>


<h2 id="preview-cloudflare-computer-agent-runtime"><a href="/changelog/post/2026-08-03-cloudflare-computer/">Preview: @cloudflare/computer agent runtime</a></h2>
<p><em>2026-08-03</em></p>
<p>We're releasing an early preview of <a href="https://github.com/cloudflare/computer"><code>@cloudflare/computer</code></a>, an open-source agent runtime that gives every agent its own computer. The runtime dynamically orchestrates between fast, efficient isolates and full Linux containers, so the agent always runs on the right compute primitive for the task at hand.</p>
<p><code>@cloudflare/computer</code> provides a virtual filesystem backed by SQLite, which you can populate from cloud storage, source control, or any files you choose. Agents can read, write, and edit files, run shell commands, and interact with Git repositories. All operations are gated, audited, and observed.</p>
<p>Install the package via npm:</p>
<pre><code class="language-sh">npm install @cloudflare/computer&#10;</code></pre>
<p>Instantiate a <code>Workspace</code> inside any Durable Object to give your agent a filesystem and execution runtime:</p>
<pre><code class="language-ts">import { Workspace } from &quot;@cloudflare/computer&quot;;&#10;&#10;export class Agent {&#10;	workspace = new Workspace({&#10;		storage: this.ctx.storage,&#10;	});&#10;}&#10;</code></pre>
<p>Several execution backends are included or you can write your own:</p>
<ul>
<li><strong>Isolate runtime</strong> — fast, horizontally scalable execution via <code>just-bash</code> and Dynamic Workers, ideal for file manipulation and data processing.</li>
<li><strong>Container runtime</strong> — full Linux environment via Cloudflare Containers, mounted through FUSE, for tasks that need native binaries, package managers, or a complete userland.</li>
</ul>
<p>The AI SDK-compatible toolkit provides common agent tools (<code>read</code>, <code>write</code>, <code>edit</code>, <code>ls</code>, <code>exec</code>) and guides the model to choose the appropriate backend for each task.</p>
<p>For more examples, including a step-by-step tutorial, visit the <a href="https://github.com/cloudflare/computer"><code>@cloudflare/computer</code> repository</a>.</p>
<p>Read the announcement blog post for more details: <a href="https://blog.cloudflare.com/cloudflare-computer/">Your agent needs a computer, not a container</a>.</p>


<h2 id="browser-run-adds-a-playground-to-the-cloudflare-dashboard"><a href="/changelog/post/2026-07-31-br-dashboard-playground/">Browser Run adds a Playground to the Cloudflare dashboard</a></h2>
<p><em>2026-07-31</em></p>
<p><a href="/browser-run/">Browser Run</a> now includes a Playground in the Cloudflare dashboard. Use it to try Quick Actions against a live browser without creating a Worker, installing an SDK, or deploying code first.</p>
<p>The Playground helps you test a target URL or raw HTML input, tune viewport and page-load settings, preview the output, and copy working code for the same request.</p>
<p><img src="/images/browser-run/playground.png" alt="Browser Run Playground in the Cloudflare dashboard showing a generated screenshot preview and output settings" /></p>
<p>With the Playground, you can:</p>
<ul>
<li>Capture visuals as <a href="/browser-run/quick-actions/screenshot-endpoint/">screenshots</a> or <a href="/browser-run/quick-actions/pdf-endpoint/">PDFs</a>.</li>
<li>Generate multiple output formats in one request with the <a href="/browser-run/quick-actions/snapshot/">snapshot endpoint</a>.</li>
<li>Extract <a href="/browser-run/quick-actions/content-endpoint/">HTML</a>, <a href="/browser-run/quick-actions/markdown-endpoint/">Markdown</a>, <a href="/browser-run/quick-actions/links-endpoint/">links</a>, or <a href="/browser-run/quick-actions/scrape-endpoint/">scraped data</a>.</li>
<li>Extract <a href="/browser-run/quick-actions/json-endpoint/">structured data with AI</a> using a prompt and optional JSON Schema.</li>
</ul>
<p>You can also configure desktop, laptop, tablet, mobile, or custom viewport sizes, set browser scale, choose page-load conditions, set timeouts, and wait for selectors before running a request.</p>
<p>Select <strong>Show Code</strong> to generate the same request as cURL, TypeScript SDK, Python, or Workers Binding code. For example, a screenshot request can be copied as a Workers Binding call:</p>
<pre><code class="language-ts">interface Env {&#10;	BROWSER: BrowserRun;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env): Promise&lt;Response&gt; {&#10;		return await env.BROWSER.quickAction(&quot;screenshot&quot;, {&#10;			url: &quot;https://developers.cloudflare.com&quot;,&#10;			viewport: {&#10;				width: 1920,&#10;				height: 1080,&#10;			},&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>Requests made in the Playground incur <a href="/browser-run/pricing/">Browser Run charges</a>. AI extraction also incurs Workers AI charges.</p>
<p>To try the Playground, go to <strong>Browser Run</strong> in the Cloudflare dashboard and select <strong>Playground</strong>.</p>
<div class="nb-dash-button"></div>
<p>For more information, refer to the <a href="/browser-run/quick-actions/">Quick Actions documentation</a>.</p>


<h2 id="use-ai-search-with-the-agents-sdk-ai-sdk-and-langchain"><a href="/changelog/post/2026-07-30-ai-search-agent-sdks/">Use AI Search with the Agents SDK, AI SDK, and LangChain</a></h2>
<p><em>2026-07-30</em></p>
<p>You can now use <a href="/ai-search/">AI Search</a> directly from popular agent frameworks, adding grounded retrieval to an existing app instead of calling the REST API by hand. The new <a href="/ai-search/agent-sdks/">Agents</a> section has guides for the <a href="/ai-search/agent-sdks/ai-sdk/">Vercel AI SDK</a>, <a href="/ai-search/agent-sdks/langchain/">LangChain</a>, and the <a href="/ai-search/agent-sdks/agents-sdk/">Cloudflare Agents SDK</a>. The AI SDK integration is a new package, and the LangChain integration is a new retriever in the existing <code>langchain-cloudflare</code> package.</p>
<h4 id="2026-07-30-ai-search-agent-sdks-vercel-ai-sdk">Vercel AI SDK</h4>
<p>The <a href="https://www.npmjs.com/package/ai-search-provider"><code>ai-search-provider</code></a> package connects AI Search to the AI SDK, and targets AI SDK v6 (<code>ai@^6</code>). Pass <code>instance.chat()</code> to <code>generateText</code> or <code>streamText</code> to generate a response grounded in your indexed content, with the retrieved chunks returned as <code>sources</code>. You can also expose <code>instance.search()</code> as a tool for agent loops.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17688.md")</div>
<h4 id="2026-07-30-ai-search-agent-sdks-langchain">LangChain</h4>
<p>The <code>langchain-cloudflare</code> package (<a href="https://pypi.org/project/langchain-cloudflare/">PyPI</a>, <a href="https://github.com/cloudflare/langchain-cloudflare">GitHub</a>) provides <code>CloudflareAISearchRetriever</code>, a standard LangChain retriever backed by AI Search. Use it on its own, wrap it with <code>create_retriever_tool</code> to give an agent a search tool, or drop it into a RAG chain. It works with REST credentials or a Worker binding inside a Python Worker.</p>
<pre><code class="language-python">from langchain_cloudflare import CloudflareAISearchRetriever&#10;&#10;retriever = CloudflareAISearchRetriever(&#10;    account_id=ACCOUNT_ID,&#10;    api_token=API_TOKEN,&#10;    instance_name=&quot;knowledge-base&quot;,&#10;    retrieval_type=&quot;hybrid&quot;,&#10;)&#10;&#10;docs = retriever.invoke(&quot;How do I configure Workers AI?&quot;)&#10;</code></pre>
<h4 id="2026-07-30-ai-search-agent-sdks-cloudflare-agents-sdk">Cloudflare Agents SDK</h4>
<p>The <a href="/agents/">Cloudflare Agents SDK</a> could already reach AI Search through the Workers binding. The new <a href="/ai-search/agent-sdks/agents-sdk/">guide</a> walks through building a stateful chat agent that provisions its own instance, indexes content, and searches it from a tool.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17689.md")</div>
<p>For the full walkthroughs, including creating an instance and indexing content, refer to the <a href="/ai-search/agent-sdks/">Agents</a> guides.</p>


<h2 id="cloudflare-mcp-servers-support-the-new-mcp-2026-07-28-specification"><a href="/changelog/post/2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28/">Cloudflare MCP servers support the new MCP 2026-07-28 Specification</a></h2>
<p><em>2026-07-28</em></p>
<p>Cloudflare's <a href="/agents/model-context-protocol/cloudflare/servers-for-cloudflare/#product-specific-mcp-servers">product-specific MCP servers</a> now support the new MCP 2026-07-28 Specification. Each request runs on a fresh stateless server without an MCP protocol session or protocol-specific Durable Object.</p>
<p>The <code>/mcp</code> endpoint also accepts stateless requests from 2025 Streamable HTTP clients. Most clients can reconnect without configuration changes.</p>
<p>Use <code>/mcp</code> for new connections. Historical <code>/sse</code> URLs continue to work as aliases for the same Streamable HTTP handler, but they no longer serve the deprecated HTTP+SSE transport. If a client forces SSE transport, change it to Streamable HTTP or automatic transport detection.</p>


<h2 id="browser-run-adds-structured-handoff-for-human-in-the-loop"><a href="/changelog/post/2026-07-28-human-in-the-loop/">Browser Run adds structured handoff for Human in the Loop</a></h2>
<p><em>2026-07-28</em></p>
<p><a href="/browser-run/">Browser Run</a> now supports structured handoff for <a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a> workflows. Using Cloudflare-specific <a href="/browser-run/features/human-in-the-loop/#cloudflare-cdp-commands">CDP commands</a>, your agent can signal that it needs help, a human steps in through <a href="/browser-run/features/live-view/">Live View</a> to handle the task, and the agent resumes once the work is done.</p>
<p>For agents running multi-step browser workflows, a single login wall or unexpected prompt can fail the entire run. Previously, scripts had to manage human intervention manually by sharing a Live View URL and polling for completion. Structured handoff replaces this with a formal pause-and-resume flow.</p>
<p>The following example requests human intervention for a login page and waits for the human to finish before continuing:</p>
<pre><code class="language-js">const cdp = await page.createCDPSession();&#10;&#10;// Get Live View URL for the human operator&#10;const { devtoolsFrontendUrl } = await cdp.send(&quot;Cloudflare.getLiveView&quot;, {&#10;	mode: &quot;tab&quot;,&#10;});&#10;console.log(`Human input needed: ${devtoolsFrontendUrl}`);&#10;&#10;// Request human intervention and wait for completion&#10;const handoffComplete = new Promise((resolve) =&gt; {&#10;	cdp.once(&quot;Cloudflare.handoffComplete&quot;, resolve);&#10;});&#10;&#10;await cdp.send(&quot;Cloudflare.handoff&quot;, {&#10;	instructions: &quot;Please log in with your credentials&quot;,&#10;	timeout: 600000,&#10;});&#10;&#10;const result = await handoffComplete;&#10;console.log(result.success ? &quot;Handoff complete&quot; : `Failed: ${result.reason}`);&#10;</code></pre>
<p>Refer to the <a href="/browser-run/features/human-in-the-loop/">Human in the Loop documentation</a> for the full API reference, examples, and best practices.</p>


<h2 id="select-models-now-require-the-workers-paid-plan"><a href="/changelog/post/2026-07-28-models-require-workers-paid/">Select models now require the Workers Paid plan</a></h2>
<p><em>2026-07-28</em></p>
<p>We are limiting Workers Free plan access to a few resource-intensive models so we can prioritize capacity for the broader Workers AI user base. This helps everyone get a more reliable inference experience, with fewer <code>429</code> and <code>3040</code> (Out of Capacity) errors.</p>
<p>The following models now require the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a>:</p>
<ul>
<li><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a></li>
<li><a href="/workers-ai/models/kimi-k2.7-code/"><code>@cf/moonshotai/kimi-k2.7-code</code></a></li>
<li><a href="/workers-ai/models/glm-5.2/"><code>@cf/zai-org/glm-5.2</code></a></li>
</ul>
<p>On the Workers Free plan, requests to these models now return a <code>403</code> HTTP error (<a href="/workers-ai/platform/errors/">internal error <code>5035</code></a>) prompting you to upgrade. The Workers Paid plan starts at $5 per month and still includes the 10,000 free Neurons per day allocation, with usage beyond that billed at each <a href="/workers-ai/platform/pricing/">model's pricing</a>.</p>
<p>Many models remain available on the Workers Free plan, including:</p>
<ul>
<li><a href="/workers-ai/models/glm-4.7-flash/"><code>@cf/zai-org/glm-4.7-flash</code></a></li>
<li><a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>@cf/google/gemma-4-26b-a4b-it</code></a></li>
<li><a href="/workers-ai/models/nemotron-3-120b-a12b/"><code>@cf/nvidia/nemotron-3-120b-a12b</code></a></li>
</ul>
<p>For the full list, refer to the <a href="/workers-ai/models/">Workers AI model catalog</a>.</p>


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
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest" aria-label="Copy to clipboard">Copy</button></div></div>
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
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4" aria-label="Copy to clipboard">Copy</button></div></div>
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
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest" aria-label="Copy to clipboard">Copy</button></div></div>


<h2 id="run-devin-on-cloudflare-using-devin-outposts"><a href="/changelog/post/2026-07-21-devin-outposts/">Run Devin on Cloudflare using Devin Outposts</a></h2>
<p><em>2026-07-21</em></p>
<p><a href="https://docs.devin.ai/onboard-devin/outposts">Devin Outposts</a> lets you run Devin agents on Cloudflare. Each Devin session runs in its own isolated sandbox backed by <a href="/containers/">Cloudflare Containers</a>, so agents can execute code and use development tooling in an isolated environment.</p>
<p>Use Devin Outposts when you want Devin sessions to run on Cloudflare managed infrastructure, with each session isolated from the others.</p>
<p><img src="/assets/upstream/images/changelog/sandbox/devin-outposts.jpg" alt="Devin interface showing Cloudflare selected as an Outposts virtual environment" /></p>
<p>To get started, refer to <a href="/sandbox/tutorials/devin-outposts/">Run Devin on Cloudflare using Devin Outposts</a>.</p>


<h2 id="agents-can-respond-to-mcp-elicitation-requests"><a href="/changelog/post/2026-07-13-mcp-client-elicitation/">Agents can respond to MCP elicitation requests</a></h2>
<p><em>2026-07-13</em></p>
<p>Agents connected to Model Context Protocol (MCP) servers with <a href="/agents/model-context-protocol/apis/client-api/"><code>addMcpServer</code></a> can now handle <a href="https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation">elicitation</a> requests.</p>
<p>Elicitation lets an MCP server request user input while it handles a tool call. Form mode collects structured, non-sensitive data. URL mode asks for consent before opening an out-of-band flow, such as third-party authorization or payment.</p>
<pre><code class="language-mermaid">sequenceDiagram&#10;    participant User&#10;    participant Agent as Agent (MCP client)&#10;    participant Server as MCP server&#10;    participant Browser&#10;&#10;    Server-&gt;&gt;Agent: elicitation/create&#10;    Agent-&gt;&gt;User: Show server, reason, and input or URL&#10;    User-&gt;&gt;Agent: Submit, open, decline, or cancel&#10;    Agent-&gt;&gt;Browser: Open URL after consent (URL mode)&#10;    Agent-&gt;&gt;Server: accept, decline, or cancel&#10;    Server--&gt;&gt;Agent: Optional URL completion notification&#10;</code></pre>
<p>Register a handler for each mode your Agent supports in <code>onStart()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17678.md")</div>
<p>Connections advertise only the modes with configured handlers. An Agent without handlers advertises no elicitation capability, which lets the server use its fallback. The SDK stores the advertised modes with each MCP server registration so they survive Durable Object hibernation. Callback functions remain in memory and reattach when <code>onStart()</code> runs.</p>
<p>For implementation details and a browser forwarding pattern, refer to <a href="/agents/model-context-protocol/apis/client-api/#elicitation">MCP client elicitation</a>. The <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp-client"><code>mcp-client</code></a> and <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp-elicitation"><code>mcp-elicitation</code></a> examples implement both sides.</p>
<h4 id="2026-07-13-mcp-client-elicitation-upgrade">Upgrade</h4>
<p>To update to this release:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest" aria-label="Copy to clipboard">Copy</button></div></div>


<h2 id="plain-text-output-for-markdown-conversion"><a href="/changelog/post/2026-07-13-markdown-conversion-text-output/">Plain text output for Markdown Conversion</a></h2>
<p><em>2026-07-10</em></p>
<p>The <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion</a> service now supports a new <code>output</code> conversion option that controls the format of the converted content.</p>
<p>Set <code>output.format</code> to <code>text</code> to receive plain text with Markdown syntax removed. The default value is <code>markdown</code>, so existing conversions are unchanged.</p>
<p>Use the <a href="/workers-ai/features/markdown-conversion/usage/binding/"><code>env.AI</code></a> binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17819.md")</div>
<p>Or call the REST API:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27; \&#10;  &#45;F &#x27;files=@index.html&#x27; \&#10;  &#45;F &#x27;conversionOptions={&quot;output&quot;: {&quot;format&quot;: &quot;text&quot;}}&#x27;&#10;</code></pre>
<p>When you request text output, the <code>format</code> field of each result is set to <code>text</code>. For more details, refer to <a href="/workers-ai/features/markdown-conversion/conversion-options/#output">Conversion Options</a>.</p>


<h2 id="filter-ai-search-list-items-by-exact-object-key"><a href="/changelog/post/2026-07-08-ai-search-list-items-key-filter/">Filter AI Search list items by exact object key</a></h2>
<p><em>2026-07-08</em></p>
<p>In <a href="/ai-search/">AI Search</a>, you can upload files to an instance, or connect a <a href="/ai-search/configuration/data-source/">data source</a> such as an R2 bucket, to make your content searchable with natural language. Each file becomes an <strong>item</strong> identified by an object <strong>key</strong> (its filename or path). The <a href="/ai-search/api/items/rest-api/">list items endpoint</a> returns the items in an instance.</p>
<p>That endpoint now accepts a <code>key</code> query parameter, so you can look up a single item by its exact object key without paging through the full list. This complements the existing <code>item_id</code> filter for when you know the key but not the ID.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/instances/&lt;INSTANCE_NAME&gt;/items?key=docs/readme.md&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Keys are unique per data source, so combine <code>key</code> with <code>source</code> (for example, <code>source=builtin</code>) to disambiguate when the same key exists across multiple sources.</p>
<p>For more information, refer to <a href="/ai-search/api/items/rest-api/">managing items</a>.</p>


<h2 id="workers-ai-tomarkdown-and-ai-search-now-supports-gif-and-bmp-image-conversion"><a href="/changelog/post/2026-07-08-gif-bmp-image-support/">Workers AI toMarkdown and AI Search now supports GIF and BMP image conversion</a></h2>
<p><em>2026-07-08</em></p>
<p>Workers AI <a href="/workers-ai/features/markdown-conversion/">Markdown conversion</a> (<code>toMarkdown</code>) now supports <code>.gif</code> and <code>.bmp</code> image files, in addition to the JPEG, PNG, WebP, and SVG formats already supported.</p>
<p>GIF and BMP files run through the same <a href="/workers-ai/features/markdown-conversion/how-it-works/#images">image pipeline</a> as other formats. Each image is resized if needed (and for animated GIFs, only the first frame is used), then passed to an object-detection model to identify what it contains. Those detected objects prompt a vision model that writes a natural-language description of the image, which becomes searchable, machine-readable Markdown.</p>
<p><a href="/ai-search/">AI Search</a> uses <code>toMarkdown</code> automatically to process the files it ingests, so any <code>.gif</code> and <code>.bmp</code> files are included the next time your index syncs, with no configuration changes required. This helps when your content mixes formats, for example a support knowledge base full of screenshots or an archive of BMP scans.</p>
<p>Learn more about <a href="/workers-ai/features/markdown-conversion/">Markdown conversion</a> and the full list of <a href="/ai-search/configuration/data-source/#supported-file-types">AI Search's supported file types</a>.</p>


<h2 id="moondream-3-1-now-available-on-workers-ai"><a href="/changelog/post/2026-07-08-moondream3.1-workers-ai/">Moondream 3.1 now available on Workers AI</a></h2>
<p><em>2026-07-08</em></p>
<p>Partnering with <a href="https://moondream.ai/">Moondream</a> to bring their latest model <a href="/workers-ai/models/moondream3.1-9B-A2B/"><code>@cf/moondream/moondream3.1-9B-A2B</code></a> to Workers AI. Moondream 3.1 is a fast vision language model built on a mixture-of-experts architecture with 9B total parameters and 2B active, delivering frontier-level visual reasoning while retaining fast, cost-efficient inference.</p>
<p>Moondream 3.1 is designed for real-world vision tasks, with a 32K token context window for handling complex queries and structured outputs.</p>
<h4 id="2026-07-08-moondream3.1-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Query</strong> — ask open-ended questions about an image, with an optional reasoning parameter</li>
<li><strong>Caption</strong> — generate short, normal, or long descriptions of an image</li>
<li><strong>Point</strong> — return coordinates for objects matching a target phrase</li>
<li><strong>Detect</strong> — return bounding boxes for objects matching a target phrase</li>
</ul>
<h4 id="2026-07-08-moondream3.1-workers-ai-real-time-vision-at-the-edge">Real-time vision at the edge</h4>
<p>Vision workloads like live camera feeds, robotics, content moderation, and interactive agents need answers in milliseconds, not seconds. Moondream 3.1's small active footprint (2B active parameters) pairs well with Workers AI's serverless, globally distributed inference: requests run close to your users, and streaming responses start returning tokens almost immediately.</p>
<p>In our testing, first tokens streamed back in roughly 20–30 ms, and results were fast across every task. The example end-to-end times below (client-observed median, including network round trip) are for a simple, single-subject image. Actual latency depends heavily on the image and how much detail you ask for.</p>
<table>
<thead>
<tr>
<th>Task</th>
<th>End-to-end (p50)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>query</code></td>
<td>~770 ms</td>
</tr>
<tr>
<td><code>caption</code></td>
<td>~480 ms</td>
</tr>
<tr>
<td><code>point</code></td>
<td>~145 ms</td>
</tr>
<tr>
<td><code>detect</code></td>
<td>~160 ms</td>
</tr>
</tbody>
</table>
<p>At these speeds you can call the model inline while handling a request rather than pushing the work to a background queue or a separate service. That opens up use cases where a slow response breaks the experience: moderating user-uploaded images before they are stored, locating an object in a video frame to drive a live overlay, extracting fields from a document during a form submission, or letting an agent inspect a screenshot and decide its next step within a single turn.</p>
<h4 id="2026-07-08-moondream3.1-workers-ai-get-started">Get started</h4>
<p>Use Moondream 3.1 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>) or the REST API at <code>/ai/run</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/moondream3.1-9B-A2B/">Moondream 3.1 model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="new-browser-run-endpoint-for-accessibility-trees"><a href="/changelog/post/2026-07-07-browser-run-accessibility-tree-endpoint/">New Browser Run endpoint for accessibility trees</a></h2>
<p><em>2026-07-07</em></p>
<p><a href="/browser-run/">Browser Run</a> now supports a standalone <code>/accessibilityTree</code> endpoint, giving agent and automation workflows direct access to the browser's accessibility tree for a rendered webpage.</p>
<p>An accessibility tree is the browser's structured view of a rendered page: roles, names, states, values, and hierarchy. It is useful for accessibility tooling, but also for AI agents and automation workflows that need page structure without the noise of raw HTML or the cost of screenshots.</p>
<p>For AI agents, this means less inference from pixels and less parsing HTML. You can provide the page structure directly, helping agents identify available elements and determine which actions they can take.</p>
<p>With the new <code>/accessibilityTree</code> endpoint, you can request the accessibility tree directly when you only need the semantic structure of a page. If you need multiple page formats in a single API call, you can use the <a href="/browser-run/quick-actions/snapshot/"><code>/snapshot</code></a> endpoint, which also returns Markdown, HTML, and screenshots.</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-run/accessibilityTree&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com/&quot;&#10;}&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: {&#10;		&quot;accessibilityTree&quot;: {&#10;			&quot;role&quot;: &quot;RootWebArea&quot;,&#10;			&quot;name&quot;: &quot;Example Domain&quot;,&#10;			&quot;children&quot;: [&#10;				{&#10;					&quot;role&quot;: &quot;heading&quot;,&#10;					&quot;name&quot;: &quot;Example Domain&quot;,&#10;					&quot;level&quot;: 1&#10;				},&#10;				{&#10;					&quot;role&quot;: &quot;link&quot;,&#10;					&quot;name&quot;: &quot;Learn more&quot;&#10;				}&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Use <code>interestingOnly</code> to return only semantically meaningful nodes, or <code>root</code> to capture the accessibility tree for a specific subtree.</p>
<p>Refer to the <a href="/browser-run/quick-actions/accessibility-tree-endpoint/"><code>/accessibilityTree</code> documentation</a> for usage examples and supported parameters.</p>


<h2 id="manage-ai-search-sync-jobs-with-wrangler-cli"><a href="/changelog/post/2026-07-02-manage-sync-jobs/">Manage AI Search sync jobs with Wrangler CLI</a></h2>
<p><em>2026-07-02</em></p>
<p>When you connect a <a href="/ai-search/configuration/data-source/">data source</a> to your <a href="/ai-search/">AI Search</a> instance, AI Search runs sync jobs to keep your index up to date with your content. You can now manage those jobs directly from <a href="/ai-search/wrangler-commands/">Wrangler</a>.</p>
<p>For example, you can trigger a sync job from your CI/CD or automated pipelines with the <code>jobs create</code> command so your index refreshes when you push a change:</p>
<pre><code class="language-sh">wrangler ai-search jobs create my-instance&#10;</code></pre>
<p>This creates an asynchronous sync job that checks for changes in your data source, and sends new, modified, or deleted files to be indexed.
The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler ai-search jobs create</code></td>
<td>Trigger a new sync job</td>
</tr>
<tr>
<td><code>wrangler ai-search jobs list</code></td>
<td>List sync jobs for an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search jobs get</code></td>
<td>Get details for a job</td>
</tr>
<tr>
<td><code>wrangler ai-search jobs cancel</code></td>
<td>Cancel a running job</td>
</tr>
<tr>
<td><code>wrangler ai-search jobs logs</code></td>
<td>View log entries for a job</td>
</tr>
</tbody>
</table>
<p>All commands accept <code>--namespace</code>/<code>-n</code> (defaults to <code>default</code>) and <code>--json</code> for structured output that automation and AI agents can parse directly. The <code>list</code> and <code>logs</code> commands also support <code>--page</code> and <code>--per-page</code> for pagination, and <code>cancel</code> prompts for confirmation unless you pass <code>-y</code>/<code>--force</code>.</p>
<p>For full usage details, refer to the <a href="/ai-search/wrangler-commands/">AI Search Wrangler commands documentation</a>.</p>


<h2 id="reduced-end-to-end-latency-for-vector-changes"><a href="/changelog/post/2026-06-30-improved-wal-throughput/">Reduced end-to-end latency for vector changes</a></h2>
<p><em>2026-07-01</em></p>
<p>We have greatly improved the throughput of the Vectorize <a href="https://blog.cloudflare.com/building-vectorize-a-distributed-vector-database-on-cloudflare-developer-platform/#the-wal">write-ahead log (WAL)</a>. As a result, we have significantly reduced the end-to-end latency for a vector change to become queryable: median latency has dropped from 2 minutes to under 30 seconds, and p99 latency from 5 minutes to under 2 minutes.</p>
<p><img src="/assets/upstream/images/vectorize/vectorize-p99-wal-batch-end-to-end-latency-improvement.png" alt="Vectorize p99 WAL batch end-to-end latency improved" /></p>
<p>This means inserts, upserts, and deletes are reflected in query results faster, improving the freshness of semantic search, recommendation, and retrieval-augmented generation (RAG) workloads. You do not need to change your code or configuration to benefit from this improvement.</p>
<p>For more information, refer to the <a href="/vectorize/">Vectorize documentation</a>.</p>


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
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/harnesses/think/">Think documentation</a>, <a href="/agents/tools/codemode/">Code Mode documentation</a>, and <a href="/agents/">Agents documentation</a> for more information.</p>


<h2 id="control-ai-search-similarity-cache-freshness"><a href="/changelog/post/2026-06-24-ai-search-similarity-cache-controls/">Control AI Search similarity cache freshness</a></h2>
<p><em>2026-06-24</em></p>
<p><a href="/ai-search/">AI Search</a> now gives you more control over <a href="/ai-search/configuration/retrieval/cache/">similarity cache</a> freshness. Similarity cache helps reduce latency and inference cost by reusing responses for semantically similar queries.</p>
<p>With these updates, you can choose how long responses are eligible for reuse and clear cached responses when they may be stale.</p>
<h4 id="2026-06-24-ai-search-similarity-cache-controls-cache-duration-now-defaults-to-48-hours">Cache duration now defaults to 48 hours</h4>
<p>Previously, AI Search cached responses for a fixed duration of 30 days. Cached responses now use the instance's <code>cache_ttl</code> setting, and the default is <strong>48 hours</strong>.</p>
<p>You can set <code>cache_ttl</code> when creating or updating an instance to choose a cache duration from 10 minutes to 6 days.</p>
<p>Use a shorter TTL when your source content changes frequently and freshness is more important. Use a longer TTL when your content is stable and you want more cache reuse.</p>
<p>For example, set <code>cache_ttl</code> to <code>518400</code> to retain cached responses for 6 days:</p>
<pre><code class="language-json">{&#10;	&quot;cache_ttl&quot;: 518400&#10;}&#10;</code></pre>
<h4 id="2026-06-24-ai-search-similarity-cache-controls-purge-cached-responses">Purge cached responses</h4>
<p>You can also purge all cached responses for an instance on demand. Purging cached responses does not delete indexed content or source files.</p>
<p>It prevents AI Search from reusing previous cached responses, so subsequent similar queries generate fresh answers and repopulate the cache.</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/instances/$INSTANCE_NAME/purge_cache&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>You can also purge cached responses from the instance settings page in the Cloudflare dashboard.</p>
<p>Refer to <a href="/ai-search/configuration/retrieval/cache/">similarity cache</a> for the full list of supported <code>cache_ttl</code> values and more details about cache behavior.</p>


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
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/tools/codemode/">Code Mode documentation</a>, <a href="/agents/tools/browser/">Browser tools documentation</a>, <a href="/agents/harnesses/think/tools/">Think tools documentation</a>, and <a href="/agents/communication-channels/voice/">Voice documentation</a> for more information.</p>


<h2 id="pay-per-crawl-advanced-configuration"><a href="/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/">Pay Per Crawl advanced configuration</a></h2>
<p><em>2026-06-16</em></p>
<p>You can now configure advanced Pay Per Crawl settings for your zone, including:</p>
<ul>
<li><strong>Disable Pay Per Crawl by URI pattern</strong> using <a href="/rules/configuration-rules/">Configuration Rules</a> to offer free access to specific pages while charging for others.</li>
<li><strong>Dynamic pricing</strong> by having your origin return a <code>crawler-price</code> response header, or by using a <a href="/workers/">Cloudflare Worker</a> to set prices based on request properties.</li>
</ul>
<p>When dynamic pricing is enabled, Pay Per Crawl adds a <code>cf-pay-per-crawl</code> request header to origin requests so your origin or Worker can determine the appropriate price.</p>
<p>Refer to the <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/">Advanced configuration documentation</a> for details.</p>


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


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/ai/">Previous</a><span>Page 2 of 7</span><a class="pagination-next" rel="next" href="/changelog/product-group/ai/3/">Next</a></nav>
