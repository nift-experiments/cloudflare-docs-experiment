---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/workers/2/
  description: '2026-07-28'
  full_title: workers changelog - page 2 | Cloudflare Docs
  head_html: <title>workers changelog - page 2 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-07-28"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/workers/2/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="workers changelog - page 2"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-07-28"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/workers/2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/workers/2/#page","headline":"workers changelog - page 2 | Cloudflare Docs","description":"2026-07-28","url":"https://developers.cloudflare.com/changelog/product/workers/2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/workers/2/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="workers-tracing-write-custom-spans-with-new-startactivespan-and-span-end-runtime-apis"><a href="/changelog/post/2026-07-28-start-active-span/">Workers tracing — write custom spans with new startActiveSpan() and span.end() runtime APIs</a></h2>
<p><em>2026-07-28</em></p>
<p>The Workers runtime now provides built-in <code>tracing.startActiveSpan()</code> and <code>span.end()</code> APIs, allowing you to write custom spans for operations that last beyond a single callback — for example, instrumenting a stream pipeline where the span should stay open until the stream is fully consumed.</p>
<p>This augments the <a href="/changelog/post/2026-06-16-custom-spans/">existing API for writing custom spans</a>, <code>tracing.enterSpan()</code>, which automatically ends a span when its callback is returned. With <code>startActiveSpan()</code>, the span remains open after the callback returns, and you call <code>span.end()</code> when the work is complete:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17808.md")</div>
<p>For more details, refer to the <a href="/workers/observability/traces/custom-spans/">custom spans documentation</a>.</p>


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
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/provisioning/previews/challenge&quot; \&#10;  &#45;X POST \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{}&#x27;&#10;&#10;curl &quot;https://api.cloudflare.com/client/v4/provisioning/previews&quot; \&#10;  &#45;X POST \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;termsOfService&quot;: &quot;https://www.cloudflare.com/terms/&quot;,&#10;    &quot;privacyPolicy&quot;: &quot;https://www.cloudflare.com/privacypolicy/&quot;,&#10;    &quot;acceptTermsOfService&quot;: &quot;yes&quot;,&#10;    &quot;challengeToken&quot;: &quot;&lt;CHALLENGE_TOKEN&gt;&quot;,&#10;    &quot;solution&quot;: {&#10;      &quot;checkpoints&quot;: &quot;&lt;BASE64_CHECKPOINTS&gt;&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>For the complete API flow, proof-of-work requirements, supported products, and limits, refer to <a href="/workers/platform/claim-deployments/#integrate-with-the-rest-api">Claim deployments (temporary accounts)</a>. For the background and design goals behind this flow, refer to <a href="https://blog.cloudflare.com/temporary-accounts/">Temporary Cloudflare Accounts for AI agents</a>.</p>


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


<h2 id="new-durable-object-namespaces-must-use-the-sqlite-storage-backend"><a href="/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/">New Durable Object namespaces must use the SQLite storage backend</a></h2>
<p><em>2026-07-09</em></p>
<p>If your account does not already have a key-value (KV) backed Durable Object namespace, you can no longer create new ones. New Durable Object namespaces must use the <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">SQLite storage backend</a>, which has been recommended for all new Durable Objects since it became <a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">generally available</a> in 2024.</p>
<p>Create a new class with a <code>new_sqlite_classes</code> migration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17719.md")</div>
<p>SQLite-backed Durable Objects have feature parity with the key-value backend — including the <a href="/durable-objects/api/sqlite-storage-api/#synchronous-kv-api">key-value storage API</a> — and additionally support relational <a href="/durable-objects/api/sqlite-storage-api/#sql-api">SQL queries</a> and <a href="/durable-objects/api/sqlite-storage-api/#pitr-point-in-time-recovery-api">point-in-time recovery</a> to restore an object's storage to any point in the past 30 days.</p>
<p>If you attempt to create a new key-value backed namespace (a <code>new_classes</code> migration) on an affected account, the deployment fails with the following error:</p>
<pre tabindex="0"><code class="language-txt">Creating new key-value backed Durable Object namespaces is no longer supported on this account. Please create a namespace using a `new_sqlite_classes` migration instead.&#10;</code></pre>
<p>This change only affects accounts that are not already using the key-value storage backend. Accounts with at least one existing key-value backed namespace can still create new ones for now, and the Workers Free plan has only ever supported SQLite-backed Durable Objects. It is part of a broader move toward SQLite as the single storage backend for Durable Objects, ahead of a future migration path for existing key-value backed objects.</p>
<p>For more information, refer to <a href="/durable-objects/reference/durable-objects-migrations/">Durable Objects migrations</a>.</p>


<h2 id="send-npm-package-dependency-metadata-with-worker-uploads"><a href="/changelog/post/2026-07-07-wrangler-deploy-upload-dependencies-metadata/">Send npm package dependency metadata with Worker uploads</a></h2>
<p><em>2026-07-09</em></p>
<p>Wrangler now collects npm package dependency information from your project's <code>package.json</code> during <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> and <a href="/workers/wrangler/commands/general/#upload"><code>wrangler versions upload</code></a>, and includes it in the upload metadata sent to the Cloudflare API. This data, each dependency's name, declared version range, and exact installed version, enables dependency analytics and future supply chain security features such as vulnerability alerting.</p>
<p>To opt out, set <a href="/workers/wrangler/configuration/#top-level-only-keys"><code>dependencies_instrumentation.enabled</code></a> to <code>false</code> in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17805.md")</div>
<p>For more details, refer to <a href="/workers/wrangler/configuration/#top-level-only-keys">Wrangler configuration</a>.</p>


<h2 id="cloudflare-drop"><a href="/changelog/post/2026-07-08-cloudflare-drag-and-drop/">Cloudflare Drop</a></h2>
<p><em>2026-07-08</em></p>
<p><a href="https://cloudflare.com/drop">Cloudflare Drop</a> lets you deploy a static site to Cloudflare without requiring a Cloudflare account to get started.</p>
<p><img src="/assets/upstream/images/workers/changelog/cloudflare-drag-and-drop-upload.png" alt="Cloudflare Drag and Drop upload screen for browsing folders or ZIP files" /></p>
<p>Upload a folder or zip file of static assets (static HTML, CSS, JavaScript, images, and fonts) and get a temporary live preview that stays live for 1 hour. During that window, you can test the site, share the preview URL, or <a href="/workers/platform/claim-deployments/">claim the deployment</a> to keep it.</p>
<p><img src="/assets/upstream/images/workers/changelog/cloudflare-drag-and-drop-preview.png" alt="Cloudflare Drag and Drop temporary live preview screen with claim and copy claim link actions" /></p>
<p>When you are ready to make the deployment permanent, click <strong>Claim</strong> to sign in or create a Cloudflare account. You can claim the site into an existing Cloudflare account or create a new account for the deployment.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17806.md")</aside>
<p><img src="/assets/upstream/images/workers/changelog/cloudflare-drag-and-drop-claim.png" alt="Cloudflare Drag and Drop claim account screen with a countdown before the claim link expires" /></p>
<p>After claiming the site, you can:</p>
<ul>
<li><strong>Add a domain</strong>: <a href="/workers/configuration/routing/custom-domains/">Connect</a> an existing domain or purchase a new one for your site.</li>
<li><strong>Enable <a href="/workers/observability/">observability</a></strong>: Monitor your site's performance and usage.</li>
<li><strong>Enable <a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a></strong>: Allow AI agents to access your site's content in Markdown.</li>
<li><strong>Control access</strong>: Make your site <a href="/cloudflare-one/access-controls/policies/">private</a> and choose who can view it.</li>
</ul>
<p><img src="/assets/upstream/images/workers/changelog/cloudflare-drag-and-drop-post-claim.png" alt="Claimed Cloudflare Drag and Drop site setup screen showing options to add a domain, control access, enable observability, and enable Markdown for agents" /></p>


<h2 id="declare-durable-object-class-lifecycle-with-exports"><a href="/changelog/post/2026-06-30-declarative-do-class-exports/">Declare Durable Object class lifecycle with `exports`</a></h2>
<p><em>2026-07-04</em></p>
<p>A new declarative <a href="/durable-objects/reference/durable-objects-migrations/"><code>exports</code></a> field in your Wrangler configuration file replaces the imperative <a href="/durable-objects/reference/durable-object-class-migrations-legacy/"><code>migrations</code></a> array for managing Durable Object class lifecycle. Instead of writing an ordered list of migration steps with unique tags, you declare each Durable Object class your Worker exports and Cloudflare compares that against what's already deployed to determine what Durable Object state needs to be created, renamed, or deleted.</p>
<p>With legacy migrations, renaming <code>ChatRoom</code> to <code>Room</code> requires retaining both tagged steps:</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;migrations&quot;: [&#10;		{ &quot;tag&quot;: &quot;v1&quot;, &quot;new_sqlite_classes&quot;: [&quot;ChatRoom&quot;] },&#10;		{&#10;			&quot;tag&quot;: &quot;v2&quot;,&#10;			&quot;renamed_classes&quot;: [{ &quot;from&quot;: &quot;ChatRoom&quot;, &quot;to&quot;: &quot;Room&quot; }],&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p>With <code>exports</code>, you instead declare <code>Room</code> as the current class and mark <code>ChatRoom</code> as renamed:</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;exports&quot;: {&#10;		&quot;ChatRoom&quot;: {&#10;			&quot;type&quot;: &quot;durable-object&quot;,&#10;			&quot;state&quot;: &quot;renamed&quot;,&#10;			&quot;renamed_to&quot;: &quot;Room&quot;,&#10;		},&#10;		&quot;Room&quot;: { &quot;type&quot;: &quot;durable-object&quot;, &quot;storage&quot;: &quot;sqlite&quot; },&#10;	},&#10;}&#10;</code></pre>
<p>Each entry is keyed by class name. The <code>state</code> field carries the lifecycle (<code>created</code> by default — a live class — plus tombstone states <code>deleted</code>, <code>renamed</code>, and <code>transferred</code>, and the <code>expecting-transfer</code> receiving state for cross-Worker transfers).</p>
<p>Key improvements over the legacy <code>migrations</code> array:</p>
<ul>
<li><strong>No migration tags.</strong> The current <code>exports</code> map is the source of truth — there is no historical chain of <code>v1</code>, <code>v2</code>, <code>v3</code> entries to maintain.</li>
<li><strong>Structured deployment output.</strong> Wrangler reports when it creates, updates, deletes, renames, or transfers Durable Object classes. It also identifies stale configuration entries that are safe to remove. Deployments with no changes or notices do not print this output.</li>
<li><strong>Zero-downtime rename and transfer patterns are first-class.</strong> Tombstones may coexist with the source class still in code, enabling a <a href="/durable-objects/reference/durable-objects-migrations/#avoid-downtime-during-a-rename">three-deploy rename</a> and a <a href="/durable-objects/reference/durable-objects-migrations/#transfer-a-durable-object-class-between-workers">four-deploy cross-Worker transfer</a> without runtime errors during the rollout window.</li>
<li><strong>Cross-Worker safety.</strong> When you delete or rename a class, Cloudflare lists every other Worker in your account whose bindings still reference the namespace, so you can redeploy them before the change goes live.</li>
</ul>
<p>Existing Workers using the legacy <a href="/durable-objects/reference/durable-object-class-migrations-legacy/"><code>migrations</code></a> array continue to work unchanged. To move to <code>exports</code>, refer to the <a href="/durable-objects/reference/durable-objects-migrations/#migrate-from-the-legacy-migrations-flow">migration guide</a>. <code>exports</code> and <code>migrations</code> are mutually exclusive within a single Worker.</p>
<p>For the full reference, refer to <a href="/durable-objects/reference/durable-objects-migrations/">Durable Object class exports</a>.</p>


<h2 id="simpler-runtime-types-with-cloudflare-workers-types-v5"><a href="/changelog/post/2026-07-03-workers-types-v5/">Simpler runtime types with @cloudflare/workers-types v5</a></h2>
<p><em>2026-07-03</em></p>
<p>We have released version 5 of <a href="https://www.npmjs.com/package/@cloudflare/workers-types"><code>@cloudflare/workers-types</code></a>. This release simplifies the package to expose only the latest runtime types.</p>
<p>We still recommend that you generate types for your Worker using <a href="/workers/wrangler/commands/general/#types"><code>wrangler types</code></a>, but if you want to use the package directly, you can install it with your package manager of choice:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/workers-types@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/workers-types@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/workers-types@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/workers-types@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/workers-types@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/workers-types@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/workers-types@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/workers-types@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>The package now exposes two entrypoints:</p>
<ul>
<li><code>@cloudflare/workers-types</code> reflects the latest compatibility date, using the latest stable compatibility flags.</li>
<li><code>@cloudflare/workers-types/experimental</code> reflects APIs behind experimental compatibility flags.</li>
</ul>
<p>The dated entrypoints, such as <code>@cloudflare/workers-types/2022-11-30</code> and <code>@cloudflare/workers-types/2023-03-01</code>, are removed. With runtime type generation in <a href="/workers/wrangler/">Wrangler v4</a>, you can generate these with the <code>wrangler types</code> command to create types locked to your Worker's compatibility date.</p>
<p>For more information, refer to <a href="/workers/languages/typescript/">TypeScript language support</a>.</p>


<h2 id="work-across-multiple-accounts-with-wrangler-auth-profiles"><a href="/changelog/post/2026-07-02-wrangler-auth-profiles/">Work across multiple accounts with Wrangler auth profiles</a></h2>
<p><em>2026-07-02</em></p>
<p><a href="/workers/wrangler/">Wrangler CLI</a> now supports auth profiles: named logins that you scope to specific Cloudflare accounts and switch between automatically, based on the directory you are working in.</p>
<p>A profile is a named OAuth login bound to a directory. Commands run in that directory, and its subdirectories, use the matching account — so you can move between accounts without re-running <code>wrangler login</code>.</p>
<p>Use profiles to keep a separate login for each client when working at an agency, or to separate staging and production into different accounts. Pair a profile with an <code>account_id</code> in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> so a command cannot reach the wrong account.</p>
<pre tabindex="0"><code class="language-sh">&#35; Create a profile for each account, choosing which accounts it can reach&#10;wrangler auth create client-a&#10;wrangler auth activate client-a ~/clients/client-a&#10;&#10;wrangler auth create client-b&#10;wrangler auth activate client-b ~/clients/client-b&#10;</code></pre>
<p>Use the <code>--profile</code> flag to run a single command with a specific profile:</p>
<pre tabindex="0"><code class="language-sh">wrangler deploy --profile personal&#10;</code></pre>
<p>In CI and other automated environments, <code>CLOUDFLARE_API_TOKEN</code> still takes precedence over all profiles.</p>
<p>For setup, the resolution order, and the full command reference, refer to <a href="/workers/wrangler/profiles/">Authentication profiles</a>.</p>


<h2 id="track-memory-usage-for-workers-and-durable-objects-in-the-dashboard"><a href="/changelog/post/2026-06-30-memory-usage-metrics/">Track memory usage for Workers and Durable Objects in the dashboard</a></h2>
<p><em>2026-06-30</em></p>
<p>You can now monitor how much memory your <a href="/workers/">Workers</a> and <a href="/durable-objects/">Durable Objects</a> consume across invocations with the new <strong>Memory Usage</strong> chart in the Workers Metrics tab, broken down by P50, P90, P99, and P999 percentiles.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-06-26-memory-usage.png" alt="Memory usage chart showing P50, P90, P99, and P999 percentiles with deployment markers" /></p>
<p>Memory usage measures the V8 <a href="/workers/reference/how-workers-works/#isolates">isolate</a> memory at the time of each invocation, subject to the <a href="/workers/platform/limits/#memory">128 MB per-isolate limit</a> — a single isolate can handle many concurrent requests and shares memory across them.</p>
<p>Use the Memory Usage chart to:</p>
<ul>
<li><strong>Track memory trends</strong> — Spot gradual increases that may indicate a memory leak before they cause <code>Exceeded Memory</code> errors.</li>
<li><strong>Correlate with deployments</strong> — Deployment markers on the chart help you identify whether a new version introduced a memory regression.</li>
<li><strong>Right-size your Worker</strong> — Understand your baseline memory footprint and how much headroom you have before hitting the 128 MB limit.</li>
</ul>
<p>For Durable Objects, memory usage reflects the in-memory state an object holds (class properties, caches, active WebSocket connections), which persists across invocations until the object is <a href="/durable-objects/concepts/durable-object-lifecycle/">hibernated or evicted</a>. This state is not preserved across eviction, hibernation, or a crash, so persist anything important to <a href="/durable-objects/best-practices/access-durable-objects-storage/">storage</a>.</p>
<p>To view memory usage, open the <strong>Metrics</strong> tab for your <a href="https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/metrics">Worker</a> or <a href="https://dash.cloudflare.com/?to=/:account/workers/durable-objects">Durable Object namespace</a>. For Durable Objects, you can filter by DO ID or name to drill down into memory usage for a specific object. You can also query memory usage programmatically via the <a href="/analytics/graphql-api/tutorials/querying-workers-metrics/">GraphQL Analytics API</a> using the <code>workersInvocationsAdaptive</code> dataset — the <code>quantiles.memoryUsageBytesP50</code> through <code>quantiles.memoryUsageBytesP999</code> fields return percentile values in bytes.</p>
<p>For local memory debugging, you can also <a href="/workers/observability/dev-tools/memory-usage/">profile memory with DevTools</a> to take heap snapshots and identify specific objects causing high memory usage.</p>


<h2 id="workers-fetch-requests-now-support-cf-vary"><a href="/changelog/post/2026-06-28-cf-vary-request-option/">Workers fetch requests now support cf.vary</a></h2>
<p><em>2026-06-28</em></p>
<p>Workers <code>fetch()</code> requests now support the <code>cf.vary</code> request option. Use <code>cf.vary</code> to control how Cloudflare caches origin responses with a <code>Vary</code> header for a single subrequest.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17804.md")</div>
<p>For more information, refer to <a href="/workers/runtime-apis/request/#the-cfvary-property"><code>cf.vary</code></a>.</p>


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


<h2 id="new-us-jurisdiction-for-durable-objects"><a href="/changelog/post/2026-06-26-durable-objects-us-jurisdiction/">New `us` jurisdiction for Durable Objects</a></h2>
<p><em>2026-06-26</em></p>
<p>Durable Objects now supports a <code>us</code> <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">jurisdiction</a>, letting you create Durable Objects that only run and store data within the United States. Use the <code>us</code> jurisdiction when you need to keep a Durable Object's compute and storage inside the United States to meet data residency requirements.</p>
<p>Create a namespace restricted to the <code>us</code> jurisdiction the same way as any other jurisdiction:</p>
<pre tabindex="0"><code class="language-js">// Worker&#10;export default {&#10;	async fetch(request, env) {&#10;		const usSubnamespace = env.MY_DURABLE_OBJECT.jurisdiction(&quot;us&quot;);&#10;		const stub = usSubnamespace.getByName(&quot;general&quot;);&#10;		return stub.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p>Workers may still access Durable Objects constrained to the <code>us</code> jurisdiction from anywhere in the world. The jurisdiction constraint only controls where the Durable Object itself runs and persists data.</p>
<p>For the full list of supported jurisdictions, refer to <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">Data location — Restrict Durable Objects to a jurisdiction</a>.</p>


<h2 id="test-durable-object-eviction-with-new-cloudflare-test-helpers"><a href="/changelog/post/2026-06-25-durable-object-eviction-test-helpers/">Test Durable Object eviction with new cloudflare:test helpers</a></h2>
<p><em>2026-06-25</em></p>
<p>The <code>@cloudflare/vitest-pool-workers</code> package now includes <code>evictDurableObject</code> and <code>evictAllDurableObjects</code> test helpers, exported from <code>cloudflare:test</code>.</p>
<p>These helpers let you test how a Durable Object behaves across evictions, simulating the production lifecycle where an idle Durable Object can be evicted from memory.</p>
<p>For more context, refer to <a href="/durable-objects/concepts/durable-object-lifecycle/">Lifecycle of a Durable Object</a>.</p>
<pre tabindex="0"><code class="language-ts">import { evictDurableObject, evictAllDurableObjects } from &quot;cloudflare:test&quot;;&#10;import { env } from &quot;cloudflare:workers&quot;;&#10;&#10;const id = env.COUNTER.idFromName(&quot;my-counter&quot;);&#10;const stub = env.COUNTER.get(id);&#10;&#10;// Evict the Durable Object instance pointed to by a specific stub&#10;await evictDurableObject(stub);&#10;&#10;// Close WebSockets instead of hibernating them&#10;await evictDurableObject(stub, { webSockets: &quot;close&quot; });&#10;&#10;// Evict all currently-running Durable Objects in evictable namespaces&#10;await evictAllDurableObjects();&#10;</code></pre>
<p>These helpers are available in <code>@cloudflare/vitest-pool-workers@0.16.20</code> and later.</p>
<p>Learn more in the <a href="/workers/testing/vitest-integration/test-apis/#durable-objects">Test APIs reference</a> and the <a href="/durable-objects/examples/testing-with-durable-objects/#testing-eviction">Testing Durable Objects guide</a>.</p>


<h2 id="new-asia-pacific-location-hints-apac-ne-and-apac-se"><a href="/changelog/post/2026-06-19-apac-ne-apac-se-location-hints/">New Asia-Pacific location hints: apac-ne and apac-se</a></h2>
<p><em>2026-06-19</em></p>
<p>Durable Objects now supports two new location hints for Asia-Pacific: <code>apac-ne</code> (Northeast Asia-Pacific) and <code>apac-se</code> (Southeast Asia-Pacific). Use <code>apac-ne</code> or <code>apac-se</code> when you want finer-grained placement within Asia-Pacific rather than the broader <code>apac</code> hint.</p>
<p>Use the new hints the same way as any other <code>locationHint</code>:</p>
<pre tabindex="0"><code class="language-js">// Northeast Asia-Pacific (Japan, Korea, etc.)&#10;const stubNE = env.MY_DURABLE_OBJECT.get(id, { locationHint: &quot;apac-ne&quot; });&#10;&#10;// Southeast Asia-Pacific (Singapore, Indonesia, etc.)&#10;const stubSE = env.MY_DURABLE_OBJECT.get(id, { locationHint: &quot;apac-se&quot; });&#10;</code></pre>
<p>If your users are spread across all of Asia-Pacific, the existing <code>apac</code> hint remains the right choice. Only reach for <code>apac-ne</code> or <code>apac-se</code> when your traffic is clearly concentrated in one sub-region and you want to minimize round-trip time to that audience. The default behavior and what we generally recommended is not adding a location hint unless absolutely needed, this will create the Durable Object as close to the initializing request as possible to reduce latency.</p>
<p>As with all location hints, these are best-effort suggestions. Cloudflare will place the Durable Object in a nearby data center, not necessarily the exact hinted location.</p>
<p>For the full list of supported hints, refer to <a href="/durable-objects/reference/data-location/#provide-a-location-hint">Data location — Provide a location hint</a>.</p>


<h2 id="temporary-accounts-for-ai-agent-deployments"><a href="/changelog/post/2026-06-19-temporary-accounts-for-agents/">Temporary accounts for AI agent deployments</a></h2>
<p><em>2026-06-19</em></p>
<p>AI agents can now deploy Workers to Cloudflare without first requiring a user to sign up, open a browser-based OAuth flow, click through the dashboard, or create an API token. When an agent tries to deploy without Cloudflare credentials, Wrangler can tell it to rerun with <code>--temporary</code>, then deploy the Worker to a temporary preview account.</p>
<p>To try this with your agent, update to Wrangler 4.102.0 or later, make sure you are logged out (<code>wrangler logout</code>), and then ask your agent to build something and deploy it to Cloudflare. The agent should follow Wrangler's output and deploy using the <code>--temporary</code> flag.</p>
<p><img src="/assets/upstream/images/workers/claim-deployments-flow.png" alt="Diagram showing an AI agent deploying, verifying, and redeploying a Worker to a temporary account, then claiming it after authentication and moving it to a permanent account" /></p>
<pre tabindex="0"><code class="language-sh">wrangler deploy --temporary&#10;</code></pre>
<p>The temporary deployment stays live for 60 minutes. During that window, the agent can verify the Worker, redeploy changes, and return both the live Worker URL and claim URL. Opening the claim URL lets you sign in to or create a Cloudflare account and make the temporary account permanent.</p>
<p>Temporary preview accounts currently support a limited set of products, including Workers, Workers Static Assets, Workers KV, D1, Durable Objects, Hyperdrive, Queues, and SSL/TLS certificates. For supported products, limits, and claim behavior, refer to <a href="/workers/platform/claim-deployments/">Claim deployments (temporary accounts)</a>.</p>
<p>For more context, refer to <a href="https://blog.cloudflare.com/temporary-accounts/">Temporary Cloudflare Accounts for Agents</a>.</p>


<h2 id="create-planetscale-postgres-and-mysql-databases-billed-to-your-cloudflare-account"><a href="/changelog/post/2026-06-18-planetscale-databases-cloudflare-billing/">Create PlanetScale Postgres and MySQL databases, billed to your Cloudflare account</a></h2>
<p><em>2026-06-18</em></p>
<p>You can create PlanetScale Postgres and MySQL databases from Cloudflare and bill PlanetScale database usage through your Cloudflare account as a pay-as-you-go customer. Cloudflare contract customers will be able to add PlanetScale usage to their contract in July so reach out to your Cloudflare account team if interested.</p>
<p>Create a PlanetScale database from the Cloudflare dashboard to check out globally distributed Workers optimized for regional data access.</p>
<div class="nb-dash-button"></div>
<p><img src="/assets/upstream/images/hyperdrive/planetscale-request-flow.svg" alt="Request flow from a user to Workers, Hyperdrive caches, connection pools, and PlanetScale." /></p>
<p>PlanetScale databases created from Cloudflare work with <a href="/workers/">Workers</a> through <a href="/hyperdrive/">Hyperdrive</a>. Hyperdrive manages database connection pools and query caching, so you can use PlanetScale as a centralized relational database for Workers applications without changing your database drivers, object-relational mapping (ORM) libraries, or SQL tooling.</p>
<p>PlanetScale usage appears on your Cloudflare invoice each billing period as a dollar total at PlanetScale's standard <a href="https://planetscale.com/pricing">pricing</a>. You can introspect per-database billing usage via PlanetScale's <a href="https://planetscale.com/docs/billing#organization-usage-and-billing-page">dashboard</a>.</p>
<p>When you create a PlanetScale database from the Cloudflare dashboard, you receive the same PlanetScale developer experience, including development branches, query insights, and Model Context Protocol (MCP) server support for agents.</p>
<p>To get started, refer to <a href="/hyperdrive/planetscale/">PlanetScale Postgres and MySQL with Hyperdrive</a>.</p>


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


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/workers/">Previous</a><span>Page 2 of 10</span><a class="pagination-next" rel="next" href="/changelog/product/workers/3/">Next</a></nav>
