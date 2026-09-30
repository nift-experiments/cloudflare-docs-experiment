<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 27, 2026</time><h2 id="post-title">Agents SDK adds MCP Specification 2026-07-28 support</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>Agents SDK v0.20.0 adds client and server support for the <a href="https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/">MCP 2026-07-28 release candidate</a>. Workers can serve tools, prompts, resources, and elicitation without an MCP transport session or Durable Object. Agents can connect to both MCP 2026-07-28 servers and existing legacy servers.</p>
<h4 id="client-support">Client support</h4>
<p>The MCP client manager now uses <code>@modelcontextprotocol/client</code>. For each connection, it probes for MCP 2026-07-28 support with <code>server/discover</code>. If the server does not support the stateless protocol, the client continues with the legacy <code>initialize</code> handshake on the same connection. Existing <code>addMcpServer</code> calls do not need a protocol-version setting or separate clients for each protocol generation.</p>
<p>For stateless requests, elicitation uses <code>input_required</code> through multi-round-trip requests (MRTR). The legacy path uses the same form and URL handlers for pushed requests. The SDK collects input, retries the original operation, and resolves the original <code>callTool</code>, <code>getPrompt</code>, or <code>readResource</code> promise with its final result.</p>
<p>OAuth callbacks now validate issuer metadata through the v2 SDK. Discovery state and issuer-bound credentials persist across browser redirects and Durable Object hibernation.</p>
<h4 id="run-stateless-servers">Run stateless servers</h4>
<p><code>createMcpHandler</code> now accepts a factory that returns a server from <code>@modelcontextprotocol/server</code>. The factory creates an isolated server for each request.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17681.md")</div>
<p>The isolated <code>agents/mcp/server</code> entry keeps <code>McpAgent</code>, <code>WorkerTransport</code>, MCP client transports, and SDK v1 modules out of stateless server bundles.</p>
<p>The Workers wrapper validates present browser Origins, supports explicit delegation to trusted Origin middleware, and exposes request handling plus typed change notifications.</p>
<h4 id="backward-compatibility">Backward compatibility</h4>
<p>The same <code>createMcpHandler(createServer)(request, env, ctx)</code> route serves MCP 2026-07-28 clients and legacy clients that use stateless requests. You do not need separate routes or tool definitions for ordinary tools, prompts, and resources.</p>
<p><code>McpAgent</code> is deprecated and feature-frozen. Migrate existing <code>McpAgent</code> servers to the stateless handler at your earliest convenience. If a server depends on protocol sessions, RPC, pushed server-to-client requests, standalone streams, or replay, use the <a href="/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/">migration guide</a> to design stateless equivalents and run both routes while clients transition.</p>
<h4 id="migrate-existing-sdk-v1-servers">Migrate existing SDK v1 servers</h4>
<p>Upgrade the Agents SDK:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Move ordinary SDK v1 server definitions into an SDK v2 factory and serve them with <code>createMcpHandler</code>. The handler's default legacy compatibility means most stateless deployments need only one route.</p>
<p>If an existing <code>McpAgent</code> server still needs sessionful features, add the stateless path beside it. Use <code>isLegacyRequest()</code> to send only legacy traffic to the existing route:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17682.md")</div>
<p>Migrate the remaining sessionful features, allow existing sessions to drain, then remove the legacy route. Refer to <a href="/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/">Migrate to MCP SDK v2</a> for package changes, compatibility limits, and rollout steps.</p>
<h4 id="deprecations-in-v0-20-0">Deprecations in v0.20.0</h4>
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
</div></article></div>
