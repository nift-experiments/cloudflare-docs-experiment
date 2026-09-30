<p>This guide covers the <a href="https://github.com/modelcontextprotocol/typescript-sdk">MCP SDK v2</a> upgrade in Agents SDK v0.20.0. It explains how to move servers to <code>@modelcontextprotocol/server</code>, use a temporary legacy lane only when sessionful features require it, and update MCP clients.</p>
<h2 id="choose-a-server-path">Choose a server path</h2>
<p>Use the following table to select a migration path:</p>
<table>
<thead>
<tr>
<th>Current server</th>
<th>Migration path</th>
</tr>
</thead>
<tbody>
<tr>
<td>SDK v1 server without sessionful dependencies</td>
<td>Move the server definition to an SDK v2 factory and pass the factory to <code>createMcpHandler</code>.</td>
</tr>
<tr>
<td>SDK v1 server with sessionful dependencies</td>
<td>Add an SDK v2 route. Keep <code>createLegacyMcpHandler</code> only on a temporary legacy lane while replacing those dependencies.</td>
</tr>
<tr>
<td><code>McpAgent</code> without legacy stateful features</td>
<td>Migrate directly to an SDK v2 factory and <code>createMcpHandler</code>.</td>
</tr>
<tr>
<td><code>McpAgent</code> that uses legacy stateful features</td>
<td>Design stateless equivalents, serve stateless and legacy lanes together, then drain the legacy lane.</td>
</tr>
</tbody>
</table>
<p>Agents SDK v0.20.0 deprecates these APIs:</p>
<ul>
<li>Passing an SDK v1 server to <code>createMcpHandler</code>. Move the server to an SDK v2 factory. Use <code>createLegacyMcpHandler</code> only as a temporary bridge for sessionful behavior. This overload is scheduled for removal in the next major version.</li>
<li><code>McpAgent</code>. It is deprecated and feature-frozen. Migrate at your earliest convenience. No removal version is announced.</li>
<li><code>MCPClientManager.callTool(params, resultSchema, options)</code> and <code>withX402Client(...).callTool(confirm, params, resultSchema, options)</code>. Use <code>callTool(params, options)</code> or <code>callTool(confirm, params, options)</code> instead. No removal version is announced.</li>
</ul>
<p><code>experimental_createMcpHandler</code> was already deprecated and remains scheduled for removal in the next major version. Move its SDK v1 server to an SDK v2 factory. Use <code>createLegacyMcpHandler</code> only on a temporary sessionful lane while migrating.</p>
<h2 id="install-the-mcp-packages">Install the MCP packages</h2>
<p>Install only the MCP package generations that your application imports. Keep the v2 version exact.</p>
<p>For a stateless server:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents @modelcontextprotocol/server@2.0.0 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents @modelcontextprotocol/server@2.0.0 zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents @modelcontextprotocol/server@2.0.0 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents @modelcontextprotocol/server@2.0.0 zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents @modelcontextprotocol/server@2.0.0 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents @modelcontextprotocol/server@2.0.0 zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents @modelcontextprotocol/server@2.0.0 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents @modelcontextprotocol/server@2.0.0 zod" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For a temporary legacy lane:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents @modelcontextprotocol/sdk@1.30.0 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents @modelcontextprotocol/sdk@1.30.0 zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents @modelcontextprotocol/sdk@1.30.0 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents @modelcontextprotocol/sdk@1.30.0 zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents @modelcontextprotocol/sdk@1.30.0 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents @modelcontextprotocol/sdk@1.30.0 zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents @modelcontextprotocol/sdk@1.30.0 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents @modelcontextprotocol/sdk@1.30.0 zod" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For an Agent that connects to MCP servers:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents @modelcontextprotocol/client@2.0.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents @modelcontextprotocol/client@2.0.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents @modelcontextprotocol/client@2.0.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents @modelcontextprotocol/client@2.0.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents @modelcontextprotocol/client@2.0.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents @modelcontextprotocol/client@2.0.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents @modelcontextprotocol/client@2.0.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents @modelcontextprotocol/client@2.0.0" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Follow peer dependency instructions from your package manager. Update the exact MCP versions with the Agents release that supports them.</p>
<h2 id="decide-whether-a-temporary-legacy-lane-is-required">Decide whether a temporary legacy lane is required</h2>
<p>Do not keep SDK v1 only because the server currently imports it. Move directly to an SDK v2 factory unless the endpoint depends on one of these sessionful features:</p>
<ul>
<li>Protocol sessions or a supplied <code>WorkerTransport</code></li>
<li>Transport storage or event replay</li>
<li>Standalone GET streams</li>
<li>Pushed elicitation, sampling, or roots requests</li>
<li>Session deletion with HTTP <code>DELETE</code></li>
</ul>
<p>If the endpoint uses one of these features, deploy the stateless route first. Keep the SDK v1 route only while you replace the sessionful dependency. Route requests with <code>isLegacyRequest()</code> as shown in <a href="#run-stateless-and-legacy-lanes-together">Run stateless and legacy lanes together</a>.</p>
<p>For an SDK v1 endpoint that does not use <code>McpAgent</code>, use <code>createLegacyMcpHandler</code> only on that temporary legacy branch. Remove it after clients migrate and existing sessions drain.</p>
<h2 id="move-a-stateless-server-to-sdk-v2">Move a stateless server to SDK v2</h2>
<p>The stateless <code>createMcpHandler</code> accepts a factory. The factory returns <code>McpServer</code> or <code>Server</code> from <code>@modelcontextprotocol/server</code>.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2222.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2223.md")
</div>
<p>The Worker entrypoint remains an object. Only the handler call changes:</p>
<pre><code class="language-ts">// SDK v1: pass a fresh constructed server.&#10;return createMcpHandler(createServer())(request, env, ctx);&#10;&#10;// SDK v2: pass the factory itself.&#10;return createMcpHandler(createServer)(request, env, ctx);&#10;</code></pre>
<p>Do not simplify this to <code>export default createMcpHandler(createServer)</code>. The Agents handler is callable for composition inside another handler, but Wrangler treats any function default export as a <code>WorkerEntrypoint</code> class.</p>
<p>The SDK v2 handler creates one server for each MCP request. Concurrent Worker requests never share a connected server instance.</p>
<h3 id="handler-options-for-stateless-servers">Handler options for stateless servers</h3>
<p>The Agents wrapper adds <code>route</code>, <code>corsOptions</code>, <code>allowedHostnames</code>, <code>allowedOriginHostnames</code>, and <code>authContext</code>. It also passes supported SDK v2 options through to the upstream handler.</p>
<p>Common options include:</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>route</code></td>
<td>Sets the exact request path. The default is <code>/mcp</code>.</td>
</tr>
<tr>
<td><code>legacy</code></td>
<td>Uses legacy compatibility by default. Set <code>&quot;reject&quot;</code> for a stateless-only endpoint.</td>
</tr>
<tr>
<td><code>responseMode</code></td>
<td>Selects automatic, JSON, or SSE response handling.</td>
</tr>
<tr>
<td><code>allowedHostnames</code></td>
<td>Restricts Host headers to specific hostnames.</td>
</tr>
<tr>
<td><code>allowedOriginHostnames</code></td>
<td>Restricts browser Origins, or accepts <code>&quot;*&quot;</code> when trusted middleware validates them.</td>
</tr>
<tr>
<td><code>corsOptions</code></td>
<td>Controls CORS response headers. Set <code>false</code> to remove them.</td>
</tr>
<tr>
<td><code>onerror</code></td>
<td>Reports handler errors without changing the response.</td>
</tr>
<tr>
<td><code>maxSubscriptions</code>, <code>keepAliveMs</code></td>
<td>Configure <code>subscriptions/listen</code> delivery.</td>
</tr>
</tbody>
</table>
<p>The stateless handler rejects these SDK v1 options:</p>
<ul>
<li><code>transport</code></li>
<li><code>storage</code></li>
<li><code>sessionIdGenerator</code></li>
<li><code>onsessioninitialized</code> and <code>onsessionclosed</code></li>
<li><code>enableJsonResponse</code></li>
<li><code>eventStore</code></li>
<li><code>allowedHosts</code> and <code>allowedOrigins</code></li>
<li><code>enableDnsRebindingProtection</code></li>
<li><code>retryInterval</code></li>
</ul>
<p>Use <code>responseMode: &quot;json&quot;</code> instead of <code>enableJsonResponse: true</code>. JSON mode drops notifications emitted before the final result.</p>
<h3 id="origin-validation-on-workers">Origin validation on Workers</h3>
<p>The Workers wrapper validates every present Origin. It rejects malformed, opaque, and non-HTTP Origins with <code>403</code>.</p>
<p>Its default allowlist includes localhost-class Origins and the endpoint's <code>workers.dev</code> hostname. A concrete <code>corsOptions.origin</code> also adds its hostname automatically. The handler applies matching Host checks to localhost and <code>workers.dev</code> endpoints.</p>
<p>For a custom domain with wildcard CORS, configure both Host and Origin restrictions explicitly:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2224.md")
</div>
<p>Set <code>allowedOriginHostnames: &quot;*&quot;</code> only when trusted middleware validates Origins before calling the handler. This value turns off the handler Origin check. MCP HTTP servers must validate browser Origins.</p>
<p>CORS headers do not authenticate a request. Protect the endpoint with OAuth or another authentication layer.</p>
<p>The handler does not infer a trusted Host allowlist from <code>request.url</code>. If your deployment accepts arbitrary Host values, validate them before calling the handler. For local servers outside Cloudflare Workers, follow the upstream SDK Host and Origin validation guidance.</p>
<h3 id="understand-compatibility-with-legacy-clients">Understand compatibility with legacy clients</h3>
<p>The default <code>legacy: &quot;stateless&quot;</code> setting supports ordinary legacy tools, resources, and prompts. This lane uses the SDK v2 web-standard transport. It does not import <code>WorkerTransport</code> and is not a complete sessionful transport.</p>
<p>The fallback has these limits:</p>
<ul>
<li>Each POST receives a new server and transport.</li>
<li>HTTP GET and DELETE return <code>405</code>.</li>
<li>No MCP session ID or protocol session state persists.</li>
<li>Pushed sampling, elicitation, and roots requests fail immediately.</li>
<li>Standalone streams, event replay, and session deletion are unavailable.</li>
<li>Published experimental tasks are not supported through this fallback.</li>
</ul>
<p>While migrating these features, route affected legacy clients to a temporary <code>createLegacyMcpHandler</code> or <code>McpAgent</code> lane.</p>
<h2 id="migrate-an-mcpagent-server">Migrate an <code>McpAgent</code> server</h2>
<p>During migration, <code>McpAgent</code> remains an SDK v1 server. Do not change the server import inside the legacy route to <code>@modelcontextprotocol/server</code>.</p>
<h3 id="migrate-directly-without-legacy-stateful-features">Migrate directly without legacy stateful features</h3>
<p>If the server does not depend on MCP session state, RPC, pushed server-to-client requests, standalone streams, or event replay, move its tools to an SDK v2 factory and serve it with <code>createMcpHandler</code>.</p>
<h3 id="plan-stateless-equivalents-for-stateful-features">Plan stateless equivalents for stateful features</h3>
<p>If the server uses legacy stateful features, keep the existing <code>McpAgent</code> route while you design and deploy stateless equivalents:</p>
<table>
<thead>
<tr>
<th>Stateful feature on the legacy path</th>
<th>Design for the stateless path</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application data keyed by an MCP session</td>
<td>Store data behind an explicit application boundary such as a Durable Object, D1, KV, or R2. Address it with an authenticated, server-issued handle instead of an MCP session ID.</td>
</tr>
<tr>
<td>Multi-step interaction state</td>
<td>Return integrity-protected <code>requestState</code> with <code>input_required</code>. Bind it to the authenticated user, original method and parameters, and an expiry.</td>
</tr>
<tr>
<td>Pushed elicitation, sampling, or roots requests</td>
<td>Return <code>inputRequired(...)</code>. The client fulfils the embedded requests and retries the original operation.</td>
</tr>
<tr>
<td>Standalone list-change stream</td>
<td>Publish changes through <code>subscriptions/listen</code>. Clients reopen the subscription if its stream ends.</td>
</tr>
<tr>
<td>Session replay or transport recovery</td>
<td>Make each stateless request independently recoverable. Persist business progress in application storage rather than the MCP transport.</td>
</tr>
<tr>
<td>Agent-to-<code>McpAgent</code> RPC</td>
<td>Replace the protocol-session dependency with an explicit application RPC or HTTP boundary, then expose the stateless MCP tools separately.</td>
</tr>
</tbody>
</table>
<p>Do not remove the legacy route as soon as the stateless implementation exists. Serve both lanes while clients migrate and existing sessions drain.</p>
<h3 id="run-stateless-and-legacy-lanes-together">Run stateless and legacy lanes together</h3>
<p>A single URL can route stateless requests to SDK v2 and legacy requests to the existing sessionful server.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2225.md")
</div>
<p>Keep <code>legacy: &quot;reject&quot;</code> on the stateless handler. Otherwise, its legacy compatibility lane consumes requests before the sessionful route receives them.</p>
<p>Deploy both routes before moving clients. Monitor the legacy lane and let existing sessions drain. Remove the legacy route and its protocol-only Durable Object binding only after no clients depend on them. Handle Durable Object migration configuration as a separate deployment step.</p>
<h2 id="update-mcp-clients">Update MCP clients</h2>
<p>Agents now uses <code>@modelcontextprotocol/client</code> internally. Existing <code>addMcpServer</code> calls negotiate the protocol era automatically.</p>
<p>Servers on the stateless path use <code>server/discover</code>. Agents falls back to <code>initialize</code> for legacy Streamable HTTP, SSE, and RPC servers.</p>
<p>The client API includes these changes:</p>
<ul>
<li><code>callTool(params, options)</code> is the preferred signature.</li>
<li><code>callTool(params, resultSchema, options)</code> remains available but is deprecated.</li>
<li>MCP client types now come from <code>@modelcontextprotocol/client</code>.</li>
<li>Required stateless HTTP headers are handled by the SDK.</li>
<li>List changes use stateless subscriptions or legacy notifications based on the negotiated lane.</li>
</ul>
<h3 id="configure-elicitation-for-stateless-requests">Configure elicitation for stateless requests</h3>
<p>Tools, prompts, and resources on the stateless path can return <code>input_required</code> through multi-round-trip requests (MRTR). The SDK calls the configured elicitation handler and retries the original operation. Your original <code>callTool</code>, <code>getPrompt</code>, or <code>readResource</code> promise remains pending.</p>
<p>Each retry contains responses for the immediately preceding input round, not every earlier response. The client also echoes the latest opaque <code>requestState</code>. Seal trusted intermediate values needed by later rounds into integrity-protected <code>requestState</code>; do not expect <code>inputResponses</code> to accumulate across rounds.</p>
<p>Refer to the <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp-elicitation-mrtr">stateless elicitation example</a> for a two-round tool flow.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2226.md")
</div>
<p>Handlers and in-flight calls remain in memory. Hibernation, isolate restart, transport loss, or connection reconstruction rejects an active interactive call. Retry the operation after the connection recovers.</p>
<p>Treat manually handled <code>requestState</code> as untrusted input. Bind it to the authenticated user and operation, protect its integrity, and set a short expiry.</p>
<h3 id="update-custom-oauth-providers">Update custom OAuth providers</h3>
<p>A custom <code>AgentMcpOAuthProvider</code> must implement the v2 <code>OAuthClientProvider</code> contract:</p>
<ul>
<li>Import OAuth types from <code>@modelcontextprotocol/client</code>.</li>
<li>Store <code>StoredOAuthClientInformation</code> and <code>StoredOAuthTokens</code>.</li>
<li>Preserve the SDK issuer stamp on credentials.</li>
<li>Persist <code>OAuthDiscoveryState</code> across browser redirects.</li>
<li>Accept <code>&quot;discovery&quot;</code> in <code>invalidateCredentials</code>.</li>
<li>Keep credentials separate when authorization issuers differ.</li>
</ul>
<p>SDK v2 validates OAuth metadata issuers by default. A trusted legacy server with known mismatched metadata can use <code>skipIssuerMetadataValidation: true</code>. This weakens OAuth mix-up protection and should not be a general fallback.</p>
<h2 id="review-protocol-differences">Review protocol differences</h2>
<p>MCP's stateless model changes the transport and lifecycle:</p>
<table>
<thead>
<tr>
<th>Area</th>
<th>Previous behavior</th>
<th>New behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Startup</td>
<td><code>initialize</code> handshake</td>
<td>No handshake. <code>server/discover</code> is optional for clients</td>
</tr>
<tr>
<td>Request metadata</td>
<td>Connection-scoped negotiation</td>
<td>Version, client capabilities, and identity metadata on each request</td>
</tr>
<tr>
<td>Sessions</td>
<td>Optional <code>Mcp-Session-Id</code></td>
<td>No protocol session</td>
</tr>
<tr>
<td>Server input requests</td>
<td>Server sends JSON-RPC requests</td>
<td>Server returns <code>input_required</code>. Client retries the original operation</td>
</tr>
<tr>
<td>Change notifications</td>
<td>Standalone GET stream and list-change notifications</td>
<td><code>subscriptions/listen</code> POST with an SSE response</td>
</tr>
<tr>
<td>Stream recovery</td>
<td><code>Last-Event-ID</code> can resume configured streams</td>
<td>Listen streams reopen after failure. There is no <code>Last-Event-ID</code> replay.</td>
</tr>
</tbody>
</table>
<p>Custom transports, proxies, and gateways must preserve the draft request headers:</p>
<ul>
<li><code>MCP-Protocol-Version</code></li>
<li><code>Mcp-Method</code></li>
<li><code>Mcp-Name</code> for tool, prompt, and resource operations</li>
<li>Declared <code>Mcp-Param-*</code> tool headers</li>
</ul>
<p>The exact SDK version used by Agents implements the MCP 2026-07-28 revision. It makes <code>clientInfo</code> optional and places server identity in result <code>_meta</code>. Use high-level SDK APIs and update MCP packages with the Agents release that supports each protocol revision. Raw stateless results must include <code>resultType</code>.</p>
<p>The draft deprecates Roots, Sampling, Logging, the old HTTP+SSE transport, and Dynamic Client Registration. The types remain available during the deprecation window for legacy compatibility. The published experimental task methods become the <code>io.modelcontextprotocol/tasks</code> extension. Agents SDK v0.20.0 does not add that extension.</p>
<h3 id="integration-compatibility">Integration compatibility</h3>
<p>The following integrations retain SDK v1 server output in this release:</p>
<ul>
<li>Current Code Mode <code>codeMcpServer</code> and <code>openApiMcpServer</code> helpers</li>
<li>The server-side <code>withX402</code> helper</li>
<li>Existing OpenAI Apps examples that import an SDK v1 <code>McpServer</code></li>
</ul>
<p>Until these integrations produce SDK v2 servers, isolate their output behind a temporary <code>createLegacyMcpHandler</code> route. The Code Mode MCP connector and <code>withX402Client</code> accept either client generation.</p>
<h2 id="plan-the-rollout">Plan the rollout</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2227.md")
</div>
<p>Stored HTTP session IDs from Agents releases before v0.20.0 do not include the negotiated protocol version. The upgraded client discards those IDs and reconnects instead of sending an unsafe resumed request. Existing in-flight work tied to an old remote session does not resume.</p>
<p>For API details, refer to <a href="/agents/model-context-protocol/apis/handler-api/"><code>createMcpHandler</code></a> and <a href="/agents/model-context-protocol/apis/client-api/"><code>McpClient</code></a>.</p>
