<h1 id="changelog">Changelog</h1>

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


<h2 id="node-js-24-is-now-the-default-for-workers-builds"><a href="/changelog/post/2026-07-30-workers-builds-nodejs-24/">Node.js 24 is now the default for Workers Builds</a></h2>
<p><em>2026-07-30</em></p>
<p>Workers Builds now uses Node.js 24.18.0 by default. The build image preinstalls Node.js 22.23.2 and 24.18.0.</p>
<p>You can continue to override the default with the <code>NODE_VERSION</code> environment variable, an <code>.nvmrc</code> file, or a <code>.node-version</code> file. For more information, refer to <a href="/workers/ci-cd/builds/build-image/#overriding-default-versions">Override default versions</a>.</p>


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


<h2 id="workers-tracing-write-custom-spans-with-new-startactivespan-and-span-end-runtime-apis"><a href="/changelog/post/2026-07-28-start-active-span/">Workers tracing — write custom spans with new startActiveSpan() and span.end() runtime APIs</a></h2>
<p><em>2026-07-28</em></p>
<p>The Workers runtime now provides built-in <code>tracing.startActiveSpan()</code> and <code>span.end()</code> APIs, allowing you to write custom spans for operations that last beyond a single callback — for example, instrumenting a stream pipeline where the span should stay open until the stream is fully consumed.</p>
<p>This augments the <a href="/changelog/post/2026-06-16-custom-spans/">existing API for writing custom spans</a>, <code>tracing.enterSpan()</code>, which automatically ends a span when its callback is returned. With <code>startActiveSpan()</code>, the span remains open after the callback returns, and you call <code>span.end()</code> when the work is complete:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17808.md")</div>
<p>For more details, refer to the <a href="/workers/observability/traces/custom-spans/">custom spans documentation</a>.</p>


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


<h2 id="run-integration-tests-against-your-worker-s-production-build"><a href="/changelog/post/2026-07-21-integration-test-harness/">Run integration tests against your Worker's production build</a></h2>
<p><em>2026-07-27</em></p>
<p>Wrangler now provides <code>createTestHarness()</code>, an API for running integration tests against Workers built with <a href="/workers/testing/test-harness/configure/#configure-worker-projects">Wrangler or the Cloudflare Vite plugin</a> from any Node.js test runner.</p>
<p>The test harness starts a local Worker server with <a href="/workers/wrangler/api/#createtestharness">helpers for dispatching requests, resetting storage, and inspecting runtime logs</a>.</p>
<p>This is useful for tests that need to:</p>
<ul>
<li><a href="/workers/testing/test-harness/interact-with-workers/#test-route-dispatch-across-workers">Route requests across multiple Workers</a></li>
<li><a href="/workers/testing/test-harness/integrations/#mock-service-worker">Mock outbound <code>fetch()</code> requests</a> with Node.js request mocking libraries such as <a href="https://mswjs.io/">MSW</a></li>
<li><a href="/workers/testing/test-harness/integrations/#playwright">Run Playwright tests against a Worker</a></li>
</ul>
<p>For example, this test starts two Workers and mocks an upstream API:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17807.md")</div>
<p>Cloudflare now recommends <code>createTestHarness()</code> for integration tests instead of <a href="/workers/testing/unstable_startworker/"><code>unstable_startWorker()</code></a> or <a href="/workers/wrangler/api/#unstable_dev"><code>unstable_dev()</code></a>. To start a development server programmatically, use the Vite <a href="https://vite.dev/guide/api-javascript.html#createserver"><code>createServer()</code></a> API with the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
<p>For more information about <code>createTestHarness()</code>, refer to the <a href="/workers/testing/test-harness/">Integration test harness guide</a>.</p>


<h2 id="sippy-now-supports-azure-blob-storage-and-s3-compatible-storage-providers"><a href="/changelog/post/2026-07-24-r2-sippy-azure-s3-compatible-support/">Sippy now supports Azure Blob Storage and S3-compatible storage providers</a></h2>
<p><em>2026-07-24</em></p>
<p><a href="/r2/data-migration/sippy/">Sippy</a> can now incrementally migrate data from Azure Blob Storage and any S3-compatible object storage provider to <a href="/r2/">Cloudflare R2</a>, in addition to Amazon S3 and Google Cloud Storage. Sippy copies objects to R2 as your application requests them, so you can start serving data from R2 without first moving your entire dataset or paying migration-specific egress fees.</p>
<h4 id="2026-07-24-r2-sippy-azure-s3-compatible-support-enable-sippy">Enable Sippy</h4>
<p>Run the following command and follow the prompts to select and configure your source storage provider:</p>
<pre><code class="language-sh">npx wrangler r2 bucket sippy enable &lt;BUCKET_NAME&gt;&#10;</code></pre>
<p>For Azure Blob Storage, provide your storage account name, container name, and either an account key or a shared access signature (SAS) token with read and list permissions. For an S3-compatible provider, provide the S3 API endpoint URL and read-only Access Key ID and Secret Access Key.</p>
<p><img src="/assets/upstream/images/r2/sippy-azure-source-configuration.png" alt="Azure Blob Storage source configuration in the R2 dashboard" /></p>
<p>After you enable Sippy, requests for objects that are not yet in R2 are served from your source bucket and copied to R2. Subsequent requests for those objects are served from R2.</p>
<p>For setup instructions and credential requirements, refer to the <a href="/r2/data-migration/sippy/">Sippy documentation</a>.</p>


<h2 id="filter-durable-object-logs-and-traces-by-instance-id"><a href="/changelog/post/2026-07-24-durable-object-instance-observability/">Filter Durable Object logs and traces by instance ID</a></h2>
<p><em>2026-07-24</em></p>
<p><a href="/workers/observability/logs/workers-logs/">Workers Logs</a> and <a href="/workers/observability/exporting-opentelemetry-data/">OpenTelemetry</a> spans for <a href="/durable-objects/">Durable Object</a> requests include the Durable Object instance ID.</p>
<p>Use <code>$workers.durableObjectId</code> to filter logs for a specific instance. Root and child spans include the same ID in <code>cloudflare.durable_object.id</code>.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-07-24-durable-object-trace-filter.png" alt="Query Builder filtering traces by Durable Object instance ID" /></p>
<p>Use these fields to isolate a specific instance and correlate its logs and traces.</p>
<p>For more information, refer to <a href="/durable-objects/observability/metrics-and-analytics/">Durable Objects metrics and analytics</a> and <a href="/workers/observability/traces/spans-and-attributes/">Workers tracing spans and attributes</a>.</p>


<h2 id="workers-builds-now-skips-superseded-queued-builds"><a href="/changelog/post/2026-07-24-skip-superseded-builds/">Workers Builds now skips superseded queued builds</a></h2>
<p><em>2026-07-24</em></p>
<p>Workers Builds now automatically skips a queued build when a newer build for the same build trigger is also queued.</p>


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


<h2 id="budget-alerts-now-on-by-default-for-pay-as-you-go-accounts"><a href="/changelog/post/2026-06-15-budget-alerts-default-on/">Budget alerts now on by default for Pay-as-you-go accounts</a></h2>
<p><em>2026-07-20</em></p>
<p>We are turning on budget alerts by default for eligible Pay-as-you-go accounts. If your account does not already have a budget alert, Cloudflare will create one for you with a $10 account-level threshold. Your default alert will enable at the turn of your next billing cycle, so it will not fire based on usage you have already incurred.</p>
<p>We are rolling this out in cohorts over the coming weeks, so eligible accounts may see their default alert appear at different times.</p>
<p>The default alert behaves exactly like an alert you would create yourself. When your cumulative usage-based spend this cycle reaches the threshold, you receive an email notification. The alert is informational only. It does not cap your usage or impact your account in any way.</p>
<p>Usage is processed once per day for the prior day's activity, so budget alerts fire the day after the threshold is reached rather than in real time.</p>
<p>Budget alerts only consider spend on usage-based products. Recurring subscription fees, such as the Workers Paid plan fee or other monthly plan charges, are not included in the threshold calculation.</p>
<p>You can change the threshold, add additional alerts, or remove the default alert entirely from <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong>, or from your Notifications settings. If you already configured your own budget alert, nothing changes.</p>
<p>Enterprise contract accounts are not in scope.</p>
<p>For more information, refer to the <a href="/billing/manage/budget-alerts/">Budget alerts documentation</a>.</p>


<h2 id="view-total-sqlite-storage-for-durable-object-namespaces"><a href="/changelog/post/2026-07-20-durable-objects-total-storage-metrics/">View total SQLite storage for Durable Object namespaces</a></h2>
<p><em>2026-07-20</em></p>
<p>You can now monitor the total SQLite storage used by a Durable Object namespace over time in the Cloudflare dashboard. The new <strong>Total storage</strong> chart shows the maximum storage reported during each hour. This helps you identify storage growth, validate data cleanup, and investigate unexpected usage.</p>
<p><img src="/assets/upstream/images/changelog/durable-objects/durable-objects-total-storage.png" alt="The Total storage chart showing a Durable Object namespace growing to 260.1 MB of storage over time." /></p>
<div class="nb-dash-button"></div>
<p>The chart appears only for SQLite-backed Durable Object namespaces. It does not appear for namespaces that use the legacy key-value storage backend. Viewing storage for individual Durable Objects by ID or name is not supported.</p>
<p>For more information, refer to <a href="/durable-objects/observability/metrics-and-analytics/#total-storage">Metrics and analytics</a>.</p>


<h2 id="preview-sent-emails-in-the-activity-log"><a href="/changelog/post/2026-07-17-email-message-preview/">Preview sent emails in the Activity log</a></h2>
<p><em>2026-07-17</em></p>
<p>You can now preview the content of sent emails directly from the Email Service Activity log. Expand a sent email and open the new <strong>Preview</strong> section to inspect the message as it was sent, across tabs for the rendered <strong>HTML</strong> body, the <strong>Text</strong> body, the <strong>Headers</strong>, the <strong>Attachments</strong>, and the full <strong>Raw</strong> <a href="https://datatracker.ietf.org/doc/html/rfc5322">RFC 5322</a> source.</p>
<p><img src="/assets/upstream/images/changelog/email-service/email-message-preview.png" alt="The rendered HTML preview of a sent email in the Email Service Activity log" /></p>
<p>Previously, the Activity log surfaced delivery and authentication metadata but not the message content, making rendering and content issues harder to debug. Message preview closes that gap.</p>
<p>To make messages previewable, turn on <strong>Email preview</strong> in your sending domain's settings. Previews cover messages sent while the setting is turned on and are retained for about seven days. Sending domains onboarded on or after 2026-07-02 have <strong>Email preview</strong> turned on automatically.</p>
<p><img src="/assets/upstream/images/changelog/email-service/email-preview-setting.png" alt="The Email preview setting in a sending domain's settings" /></p>
<p>Refer to <a href="/email-service/observability/logs/#message-preview">Email logs</a> for more information.</p>


<h2 id="manage-flagship-from-the-command-line-with-wrangler"><a href="/changelog/post/2026-07-16-wrangler-commands/">Manage Flagship from the command line with Wrangler</a></h2>
<p><em>2026-07-16</em></p>
<p><strong><a href="/workers/wrangler/">Wrangler</a></strong> now includes <code>wrangler flagship</code>, a command suite for managing <a href="/flagship/">Flagship</a> apps and feature flags from your terminal.</p>
<p>Create an app and, if you use it from a Worker, add it to your <code>wrangler.json</code> or <code>wrangler.jsonc</code> file as a binding:</p>
<pre><code class="language-bash">wrangler flagship apps create &quot;My Worker App&quot; \&#10;  &#45;-binding FLAGS \&#10;  &#45;-update-config&#10;</code></pre>
<p>Then create flags for the behavior you want to control. Flags can be booleans, strings, numbers, or JSON values:</p>
<pre><code class="language-bash">wrangler flagship flags create &lt;APP_ID&gt; new-checkout&#10;&#10;wrangler flagship flags create &lt;APP_ID&gt; checkout-flow \&#10;  &#45;-variation control=old-checkout \&#10;  &#45;-variation treatment=new-checkout \&#10;  &#45;-default control \&#10;  &#45;-type string&#10;</code></pre>
<p>After a flag exists, change its default variation or use enable and disable commands as kill switches. Existing targeting rules continue to apply unless you change or clear them explicitly:</p>
<pre><code class="language-bash">wrangler flagship flags update &lt;APP_ID&gt; checkout-flow --default treatment&#10;wrangler flagship flags disable &lt;APP_ID&gt; checkout-flow&#10;wrangler flagship flags enable &lt;APP_ID&gt; checkout-flow&#10;</code></pre>
<p>For release workflows, use <code>rollout</code>, <code>split</code>, and <code>rules</code> to change exposure without redeploying your Worker:</p>
<pre><code class="language-bash">wrangler flagship flags rollout &lt;APP_ID&gt; new-checkout \&#10;  &#45;-to on \&#10;  &#45;-percentage 25 \&#10;  &#45;-by user_id&#10;&#10;wrangler flagship flags split &lt;APP_ID&gt; checkout-flow \&#10;  &#45;-weight control=80 \&#10;  &#45;-weight treatment=20 \&#10;  &#45;-by user_id&#10;&#10;wrangler flagship flags rules update &lt;APP_ID&gt; checkout-flow \&#10;  &#45;-priority 1 \&#10;  &#45;-when &quot;country equals US&quot;&#10;</code></pre>
<p>These commands can also be used from CI/CD pipelines, scripts, and AI agents to inspect Flagship state, update flag behavior, or roll back changes through Wrangler.</p>
<p>Refer to the <a href="/flagship/reference/wrangler-commands/"><code>wrangler flagship</code> command reference</a> for the full command guide.</p>


<h2 id="subscribe-to-email-sending-events-with-queues"><a href="/changelog/post/2026-07-15-event-subscriptions/">Subscribe to Email Sending events with Queues</a></h2>
<p><em>2026-07-15</em></p>
<p>You can now subscribe to <strong><a href="/email-service/api/send-emails/">Email Sending</a> events</strong> through <a href="/queues/event-subscriptions/">Queues event subscriptions</a> and receive outbound transactional email lifecycle events on a queue. Each subscription is scoped to one sending domain — either the zone apex, such as <code>example.com</code>, or a verified sending subdomain, such as <code>send.example.com</code>.</p>
<p>Six event types are published: <code>message.delivered</code>, <code>message.deferred</code>, <code>message.bounced</code>, <code>message.failed</code>, <code>message.rejected</code>, and <code>message.complained</code>. Use them to track deliverability, react to bounces and complaints, and drive suppression or retry logic. Email Routing events are not published on this source.</p>
<p>Each event includes the message details, delivery status, and SMTP response:</p>
<pre><code class="language-json">{&#10;	&quot;type&quot;: &quot;cf.email.sending.message.delivered&quot;,&#10;	&quot;source&quot;: {&#10;		&quot;type&quot;: &quot;email.sending&quot;,&#10;		&quot;zoneId&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353&quot;,&#10;		&quot;domain&quot;: &quot;example.com&quot;&#10;	},&#10;	&quot;payload&quot;: {&#10;		&quot;messageId&quot;: &quot;0101018f7d0c4d9a-msg-deadbeef&quot;,&#10;		&quot;recipient&quot;: &quot;user@example.net&quot;,&#10;		&quot;terminal&quot;: true,&#10;		&quot;delivery&quot;: {&#10;			&quot;status&quot;: &quot;delivered&quot;,&#10;			&quot;smtpStatusCode&quot;: &quot;250&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Refer to <a href="/email-service/platform/event-subscriptions/">Event subscriptions</a> to see all event types and example payloads.</p>


<h2 id="deprecate-legacy-workers-kv-namespace-api-routes"><a href="/changelog/post/2026-07-15-kv-legacy-namespace-routes-deprecation/">Deprecate legacy Workers KV namespace API routes</a></h2>
<p><em>2026-07-15</em></p>
<p>The legacy Workers KV API routes under <code>/accounts/{account_id}/workers/namespaces/*</code> are deprecated as of July 15, 2026, and will stop working on October 15, 2026. Migrate to the documented <a href="/api/resources/kv/">Workers KV API</a> routes under <code>/accounts/{account_id}/storage/kv/namespaces/*</code> before that date.</p>
<p>The legacy and replacement routes are interchangeable. They accept the same request parameters and return the same response payloads. To migrate, update the URL path from <code>/workers/namespaces/</code> to <code>/storage/kv/namespaces/</code>.</p>
<h4 id="2026-07-15-kv-legacy-namespace-routes-deprecation-what-you-need-to-do">What you need to do</h4>
<p>Update any integration that calls a route under <code>/accounts/{account_id}/workers/namespaces/</code> to use the equivalent route under <code>/accounts/{account_id}/storage/kv/namespaces/</code>. The migration is a direct URL path substitution — request parameters and response payloads are identical:</p>
<ul>
<li><code>GET</code> and <code>POST /accounts/{account_id}/workers/namespaces</code> → <code>GET</code> and <code>POST /accounts/{account_id}/storage/kv/namespaces</code></li>
<li><code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/workers/namespaces/{namespace_id}</code> → <code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}</code></li>
<li><code>GET /accounts/{account_id}/workers/namespaces/{namespace_id}/keys</code> → <code>GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys</code></li>
<li><code>GET /accounts/{account_id}/workers/namespaces/{namespace_id}/metadata/{key_name}</code> → <code>GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}</code></li>
<li><code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/workers/namespaces/{namespace_id}/values/{key_name}</code> → <code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}</code></li>
</ul>
<p>For more information about the deprecation timeline, refer to <a href="/fundamentals/api/reference/deprecations/">API deprecations</a>.</p>


<h2 id="improved-reliability-for-account-wide-web-analytics-dashboards"><a href="/changelog/post/2026-06-10-improved-reliability-for-web-analytics-dash/">Improved reliability for account-wide Web Analytics dashboards</a></h2>
<p><em>2026-07-14</em></p>
<p>Cloudflare Web Analytics (Real User Monitoring) has rolled out performance optimizations to significantly improve the stability and loading speed of account-wide dashboards.</p>
<p>For larger accounts (with &gt;100 Web Analytics sites), loading the aggregate account-wide view would often fail, running into timeouts or unexpected interface errors due to the massive scale of parallel query processing. This update optimizes how high-volume multi-site data is queried to reduce errors and provide a snappier dashboard experience.</p>
<p>Accounts with up to 1,000 sites will now be able to load this account-wide aggregate view without experiencing misleading errors.</p>
<p>If you have an account with over 1,000 sites, we cannot currently aggregate over this volume due to processing constraints but you will now be presented with a clear error and instruction to filter to the relevant site(s) you wish to see the data for.</p>


<h2 id="platforms-can-now-create-temporary-accounts-via-the-cloudflare-api"><a href="/changelog/post/2026-07-14-temporary-accounts-api/">Platforms can now create Temporary Accounts via the Cloudflare API</a></h2>
<p><em>2026-07-14</em></p>
<p>Platforms can now create temporary preview accounts through the Cloudflare REST API. This lets your platform deploy a live Worker before the user signs in to Cloudflare.</p>
<p>With the Temporary Accounts API, coding agents, AI app builders, and other platforms can build a similar flow for generated Workers and supported resources.</p>
<p>Your platform can keep users in its onboarding flow while they generate, deploy, and test an application. Users do not need an existing Cloudflare account, and your platform does not need write access to one.</p>
<p><img src="/assets/upstream/images/workers/claim-deployments-flow.png" alt="Diagram showing an AI agent deploying, verifying, and redeploying a Worker in a temporary account, then a user authenticating and claiming the account to keep its resources" /></p>
<p>The API returns a claim URL that lets the user make the temporary account and its resources permanent.</p>
<p><a href="https://www.cloudflare.com/drop/">Cloudflare Drop</a> demonstrates this preview-and-claim pattern for static sites. Someone can upload a site, test and share it for one hour, then sign in or create an account only when they want to keep it.</p>
<p>This API expands the flow first introduced with <a href="/changelog/post/2026-06-19-temporary-accounts-for-agents/"><code>wrangler deploy --temporary</code></a>. Your backend now controls the provisioning and deployment experience directly:</p>
<ol>
<li>Show Cloudflare's Terms of Service and Privacy Policy in your product, and require the user to accept them.</li>
<li>Request and solve a proof-of-work challenge.</li>
<li>Create a temporary preview account.</li>
<li>Deploy with the returned temporary account ID and API token.</li>
<li>Show the deployed Worker URL and claim URL to the user.</li>
</ol>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/provisioning/previews/challenge&quot; \&#10;  &#45;X POST \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{}&#x27;&#10;&#10;curl &quot;https://api.cloudflare.com/client/v4/provisioning/previews&quot; \&#10;  &#45;X POST \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;termsOfService&quot;: &quot;https://www.cloudflare.com/terms/&quot;,&#10;    &quot;privacyPolicy&quot;: &quot;https://www.cloudflare.com/privacypolicy/&quot;,&#10;    &quot;acceptTermsOfService&quot;: &quot;yes&quot;,&#10;    &quot;challengeToken&quot;: &quot;&lt;CHALLENGE_TOKEN&gt;&quot;,&#10;    &quot;solution&quot;: {&#10;      &quot;checkpoints&quot;: &quot;&lt;BASE64_CHECKPOINTS&gt;&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>For the complete API flow, proof-of-work requirements, supported products, and limits, refer to <a href="/workers/platform/claim-deployments/#integrate-with-the-rest-api">Claim deployments (temporary accounts)</a>. For the background and design goals behind this flow, refer to <a href="https://blog.cloudflare.com/temporary-accounts/">Temporary Cloudflare Accounts for AI agents</a>.</p>


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


<h2 id="r2-data-catalog-now-supports-read-only-api-tokens"><a href="/changelog/post/2026-07-09-r2-data-catalog-read-only-tokens/">R2 Data Catalog now supports read-only API tokens</a></h2>
<p><em>2026-07-13</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a> now accepts read-only API tokens, so query engines and clients that only read data no longer need a read-write token. Previously, every catalog operation required an <strong>Admin Read &amp; Write</strong> token, which granted read-only clients more access than they needed.</p>
<p>You can now authenticate your Iceberg engine based on your workload:</p>
<ul>
<li><strong>Read-only</strong> operations (such as listing namespaces, loading tables, and querying data) work with an <strong>Admin Read only</strong> token (R2 Data Catalog read and R2 storage read).</li>
<li><strong>Write</strong> operations (such as creating or dropping tables and committing transactions) continue to require an <strong>Admin Read &amp; Write</strong> token.</li>
</ul>
<p>This lets you follow the principle of least privilege — for example, using a read-write token for the pipeline that writes to your tables and read-only tokens for engines like <a href="/r2-sql/">R2 SQL</a>, <a href="/r2-data-catalog/config-examples/duckdb/">DuckDB</a>, or <a href="/r2-data-catalog/config-examples/pyiceberg/">PyIceberg</a> that query them.</p>
<p>Note that credentials vended by the catalog inherit the R2 storage permissions of the token used to authenticate. To ensure read-only access to your underlying data, scope the R2 storage permission to read-only as well.</p>
<p>For details on choosing and creating the right token, refer to <a href="/r2-data-catalog/manage-catalogs/#authenticate-your-iceberg-engine">Authenticate your Iceberg engine</a>.</p>


<h2 id="r2-data-catalog-compaction-now-optimizes-manifest-files"><a href="/changelog/post/2026-07-13-r2-data-catalog-manifest-optimization/">R2 Data Catalog compaction now optimizes manifest files</a></h2>
<p><em>2026-07-13</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a>, a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> catalog built into R2, now automatically optimizes manifest files as part of <a href="/r2-data-catalog/table-maintenance/">compaction</a>.</p>
<p>Manifest files track the data files that make up an Iceberg table. As a table accumulates many small or fragmented manifests, query engines must read more metadata during query planning, which slows down queries even before any data is scanned.</p>
<p>When compaction runs, R2 Data Catalog now rewrites and clusters manifest files by partition as a best-effort pre-step. This consolidates fragmented manifests, reduces the number of manifests a query engine must open, and lowers metadata I/O overhead. Tables that are already well-clustered are skipped, so the operation only runs when it provides a benefit.</p>
<p>This happens automatically for tables with compaction enabled — no configuration changes are required.</p>
<p>For more information, refer to <a href="/r2-data-catalog/table-maintenance/">Table maintenance</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/3/">Previous</a><span>Page 4 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/5/">Next</a></nav>
