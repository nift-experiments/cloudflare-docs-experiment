<p>The Agents SDK provides two server handler paths:</p>
<table>
<thead>
<tr>
<th>API</th>
<th>Import path</th>
<th>MCP server package</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>createMcpHandler</code></td>
<td><code>agents/mcp/server</code></td>
<td><code>@modelcontextprotocol/server</code></td>
<td>stateless with legacy compatibility by default</td>
</tr>
<tr>
<td><code>createLegacyMcpHandler</code></td>
<td><code>agents/mcp</code></td>
<td><code>@modelcontextprotocol/sdk</code></td>
<td>legacy sessions through <code>WorkerTransport</code></td>
</tr>
</tbody>
</table>
<p><code>McpAgent</code> is deprecated and feature-frozen. Migrate existing <code>McpAgent</code> servers to a stateless handler. Refer to the <a href="/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/">migration guide</a> when sessionful features require a staged rollout.</p>
<h2 id="install-dependencies">Install dependencies</h2>
<p>For a stateless server:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents @modelcontextprotocol/server@2.0.0 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents @modelcontextprotocol/server@2.0.0 zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents @modelcontextprotocol/server@2.0.0 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents @modelcontextprotocol/server@2.0.0 zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents @modelcontextprotocol/server@2.0.0 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents @modelcontextprotocol/server@2.0.0 zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents @modelcontextprotocol/server@2.0.0 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents @modelcontextprotocol/server@2.0.0 zod" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For an explicit legacy server:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents @modelcontextprotocol/sdk@1.30.0 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents @modelcontextprotocol/sdk@1.30.0 zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents @modelcontextprotocol/sdk@1.30.0 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents @modelcontextprotocol/sdk@1.30.0 zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents @modelcontextprotocol/sdk@1.30.0 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents @modelcontextprotocol/sdk@1.30.0 zod" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents @modelcontextprotocol/sdk@1.30.0 zod</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents @modelcontextprotocol/sdk@1.30.0 zod" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Use the exact MCP versions required by your installed Agents release.</p>
<h2 id="createmcphandler"><code>createMcpHandler</code></h2>
<p><code>createMcpHandler</code> creates a callable stateless MCP request handler from an MCP SDK v2 server factory. Invoke it from a Worker's object <code>fetch()</code> export or compose it inside another handler.</p>
<pre><code class="language-ts">import {&#10;	createMcpHandler,&#10;	type CreateMcpHandlerOptions,&#10;	type StatelessMcpHandler,&#10;} from &quot;agents/mcp/server&quot;;&#10;import type { McpServerFactory } from &quot;@modelcontextprotocol/server&quot;;&#10;&#10;function createMcpHandler(&#10;	factory: McpServerFactory,&#10;	options?: CreateMcpHandlerOptions,&#10;): StatelessMcpHandler;&#10;</code></pre>
<h3 id="parameters">Parameters</h3>
<ul>
<li><code>factory</code> creates a fresh <code>McpServer</code> or <code>Server</code> from <code>@modelcontextprotocol/server</code>. It can be synchronous or asynchronous.</li>
<li><code>options</code> combines Agents Worker options with supported upstream SDK v2 handler options.</li>
</ul>
<p>The factory receives this request context:</p>
<pre><code class="language-ts">interface McpRequestContext {&#10;	era: &quot;modern&quot; | &quot;legacy&quot;;&#10;	authInfo?: AuthInfo;&#10;	requestInfo?: Request;&#10;}&#10;</code></pre>
<p>A zero-argument factory remains valid.</p>
<h3 id="example">Example</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2243.md")
</div>
<p>Pass the factory itself. Do not create one global server instance or pass a constructed SDK v2 server directly.</p>
<h3 id="createmcphandleroptions"><code>CreateMcpHandlerOptions</code></h3>
<p>The following options are available:</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>route</code></td>
<td><code>string</code></td>
<td><code>&quot;/mcp&quot;</code></td>
<td>Exact path handled by the Worker wrapper</td>
</tr>
<tr>
<td><code>corsOptions</code></td>
<td><code>CORSOptions | false</code></td>
<td>Wildcard CORS</td>
<td>CORS response headers, or <code>false</code> to remove them</td>
</tr>
<tr>
<td><code>allowedHostnames</code></td>
<td><code>string[]</code></td>
<td>Localhost or <code>workers.dev</code> route</td>
<td>Optional Host restriction for custom domains</td>
</tr>
<tr>
<td><code>allowedOriginHostnames</code></td>
<td><code>string[] | &quot;*&quot;</code></td>
<td>Localhost, <code>workers.dev</code>, or concrete CORS Origin</td>
<td>Browser Origin restriction, or explicit middleware delegation</td>
</tr>
<tr>
<td><code>authContext</code></td>
<td><code>McpAuthContext</code></td>
<td>Execution context props</td>
<td>Application props returned by <code>getMcpAuthContext()</code></td>
</tr>
<tr>
<td><code>legacy</code></td>
<td><code>&quot;stateless&quot; | &quot;reject&quot;</code></td>
<td><code>&quot;stateless&quot;</code></td>
<td>legacy compatibility or stateless-only rejection</td>
</tr>
<tr>
<td><code>responseMode</code></td>
<td><code>&quot;auto&quot; | &quot;json&quot; | &quot;sse&quot;</code></td>
<td><code>&quot;auto&quot;</code></td>
<td>stateless request response shaping</td>
</tr>
<tr>
<td><code>onerror</code></td>
<td><code>(error: Error) =&gt; void</code></td>
<td>None</td>
<td>Out-of-band error reporting</td>
</tr>
<tr>
<td><code>maxSubscriptions</code></td>
<td><code>number</code></td>
<td><code>1,024</code></td>
<td>Maximum concurrent listen streams</td>
</tr>
<tr>
<td><code>keepAliveMs</code></td>
<td><code>number</code></td>
<td><code>15,000</code></td>
<td>Keepalive interval for listen streams</td>
</tr>
</tbody>
</table>
<p>SDK v1 transport options do not apply to this handler. It rejects options such as <code>transport</code>, <code>storage</code>, <code>sessionIdGenerator</code>, <code>eventStore</code>, and <code>enableJsonResponse</code>.</p>
<p>Use <code>responseMode: &quot;json&quot;</code> instead of <code>enableJsonResponse: true</code>. JSON mode drops notifications emitted before a final result.</p>
<h3 id="factory-lifecycle">Factory lifecycle</h3>
<p>The handler creates one MCP server for each request. This follows the draft protocol model, where version, identity, and capabilities travel with every request rather than through a protocol session.</p>
<p>Application data can still be durable. Store cross-request data behind an authenticated handle in a Durable Object, D1, KV, or R2 rather than an MCP session ID.</p>
<h3 id="elicitation-with-a-stateless-handler">Elicitation with a stateless handler</h3>
<p>Elicitation through a stateless handler returns <code>input_required</code> and completes through multi-round-trip requests (MRTR). On each retry, the SDK echoes the latest <code>requestState</code> and sends responses for the immediately preceding input round. It does not accumulate earlier <code>inputResponses</code>. The Worker does not remain suspended while a user responds.</p>
<p>Use <code>inputRequired(...)</code> to request input. Read that round's accepted form content from <code>context.mcpReq.inputResponses</code> with <code>acceptedContent(...)</code>. Seal trusted intermediate values needed by later rounds into integrity-protected <code>requestState</code>.</p>
<p>Refer to the <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp-elicitation-mrtr">stateless elicitation example</a> for a two-round tool flow. For stateful pushed requests, refer to <a href="/agents/model-context-protocol/apis/agent-api/#elicitation-on-legacy-servers">Elicitation on legacy servers</a>.</p>
<h3 id="origin-validation-and-cors">Origin validation and CORS</h3>
<p>The Workers wrapper validates every present browser Origin. It rejects malformed, opaque, and non-HTTP Origins with <code>403</code>. Origin-less non-browser MCP clients remain valid.</p>
<p>The default allowlist includes localhost-class Origins, the endpoint's <code>workers.dev</code> hostname, and a concrete hostname from <code>corsOptions.origin</code>. The handler also applies matching Host checks to localhost and <code>workers.dev</code> endpoints. This keeps local DNS rebinding protection without requiring a separate Origin list for the common Workers routes.</p>
<p>For a custom domain with wildcard CORS, set <code>allowedHostnames</code> and <code>allowedOriginHostnames</code> explicitly. If <code>corsOptions.origin</code> is a concrete URL, the handler derives its Origin hostname automatically:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2244.md")
</div>
<p>Allowlist values are hostnames without a scheme or port. Origin matching ignores scheme and port.</p>
<p>Set <code>allowedOriginHostnames: &quot;*&quot;</code> only when trusted middleware validates Origins before calling the handler. This value turns off the handler Origin check, including malformed and opaque Origin rejection. MCP HTTP servers must validate browser Origins.</p>
<p>CORS response headers are not authentication. Protect the MCP endpoint with OAuth or another authentication layer.</p>
<p>The handler does not infer a Host allowlist from <code>request.url</code>. If a deployment accepts arbitrary Host values, validate them before calling the handler. Local servers outside Cloudflare Workers should follow the upstream SDK DNS rebinding guidance.</p>
<h3 id="compatibility-with-legacy-clients">Compatibility with legacy clients</h3>
<p>The default <code>legacy: &quot;stateless&quot;</code> setting accepts ordinary legacy tools, prompts, and resources. This lane uses the SDK v2 web-standard transport and does not import <code>WorkerTransport</code>.</p>
<p>This compatibility path does not provide a complete session transport:</p>
<ul>
<li>Each POST creates a new server and transport.</li>
<li>HTTP GET and DELETE return <code>405</code>.</li>
<li>No MCP session ID persists.</li>
<li>Pushed elicitation, sampling, and roots requests fail immediately.</li>
<li>Standalone streams, resumability, replay, and session deletion are unavailable.</li>
<li>Published experimental tasks are not supported through this path.</li>
</ul>
<p>Set <code>legacy: &quot;reject&quot;</code> for a stateless-only endpoint. During migration, route legacy clients that still require protocol sessions to a temporary <code>createLegacyMcpHandler</code> or <code>McpAgent</code> lane.</p>
<h3 id="return-value">Return value</h3>
<p><code>createMcpHandler</code> returns a <code>StatelessMcpHandler</code>. It is callable and exposes request and notification controls:</p>
<pre><code class="language-ts">interface StatelessMcpHandler {&#10;	(request: Request, env: unknown, ctx: ExecutionContext): Promise&lt;Response&gt;;&#10;&#10;	fetch(&#10;		request: Request,&#10;		options?: McpHandlerRequestOptions,&#10;	): Promise&lt;Response&gt;;&#10;&#10;	notify: {&#10;		toolsChanged(): void;&#10;		promptsChanged(): void;&#10;		resourcesChanged(): void;&#10;		resourceUpdated(uri: string): void;&#10;	};&#10;}&#10;&#10;type McpHandlerRequestOptions = {&#10;	authInfo?: AuthInfo;&#10;	parsedBody?: unknown;&#10;};&#10;</code></pre>
<h4 id="invoke-the-handler">Invoke the handler</h4>
<p>Call the handler from a Worker's object <code>fetch()</code> export:</p>
<pre><code class="language-ts">export default {&#10;	fetch(request, env, ctx) {&#10;		return createMcpHandler(createServer)(request, env, ctx);&#10;	},&#10;} satisfies ExportedHandler;&#10;</code></pre>
<p>Do not export the callable directly as a Worker's default export. Wrangler treats function default exports as <code>WorkerEntrypoint</code> classes.</p>
<p>Use <code>fetch()</code> when another framework or authentication layer has already parsed or validated request data:</p>
<pre><code class="language-ts">const response = await handler.fetch(request, {&#10;	authInfo,&#10;	parsedBody,&#10;});&#10;</code></pre>
<p><code>authInfo</code> is passed to the server factory and request handlers. The handler does not derive it from request headers or verify access tokens. <code>parsedBody</code> avoids reparsing a JSON body that upstream middleware already consumed.</p>
<h4 id="publish-list-and-resource-changes">Publish list and resource changes</h4>
<p>The <code>notify</code> methods publish typed change events to matching open <code>subscriptions/listen</code> streams:</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>MCP notification</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>notify.toolsChanged()</code></td>
<td><code>notifications/tools/list_changed</code></td>
</tr>
<tr>
<td><code>notify.promptsChanged()</code></td>
<td><code>notifications/prompts/list_changed</code></td>
</tr>
<tr>
<td><code>notify.resourcesChanged()</code></td>
<td><code>notifications/resources/list_changed</code></td>
</tr>
<tr>
<td><code>notify.resourceUpdated(uri)</code></td>
<td><code>notifications/resources/updated</code></td>
</tr>
</tbody>
</table>
<p>Calling a notifier when no matching subscription is open is a no-op.</p>
<h4 id="keep-one-handler-for-notifications">Keep one handler for notifications</h4>
<p>Notification routing belongs to the handler instance. Constructing a new handler inside every Worker <code>fetch()</code> call is suitable for ordinary tools, prompts, resources, and MRTR elicitation. It cannot notify a <code>subscriptions/listen</code> stream owned by an earlier handler instance.</p>
<p>Create the handler once at module scope when using <code>notify</code> or <code>subscriptions/listen</code>, then invoke it from the Worker object export:</p>
<pre><code class="language-ts">const handler = createMcpHandler(createServer);&#10;&#10;export default {&#10;	fetch(request, env, ctx) {&#10;		return handler(request, env, ctx);&#10;	},&#10;} satisfies ExportedHandler;&#10;</code></pre>
<p>Notifications are isolate-local. A notification published in one Worker isolate does not reach a subscription stream running in another isolate.</p>
<h2 id="createlegacymcphandler"><code>createLegacyMcpHandler</code></h2>
<p><code>createLegacyMcpHandler</code> serves an SDK v1 server through <code>WorkerTransport</code>.</p>
<pre><code class="language-ts">import {&#10;	createLegacyMcpHandler,&#10;	type CreateLegacyMcpHandlerOptions,&#10;	type LegacyMcpHandler,&#10;} from &quot;agents/mcp&quot;;&#10;import type { Server } from &quot;@modelcontextprotocol/sdk/server/index.js&quot;;&#10;import type { McpServer } from &quot;@modelcontextprotocol/sdk/server/mcp.js&quot;;&#10;&#10;function createLegacyMcpHandler(&#10;	server: McpServer | Server,&#10;	options?: CreateLegacyMcpHandlerOptions,&#10;): LegacyMcpHandler;&#10;</code></pre>
<p>Use this handler only as a temporary migration bridge when an existing SDK v1 endpoint still requires legacy sessions, transport storage, event replay, or pushed server-to-client requests.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2245.md")
</div>
<p>Passing an SDK v1 server to <code>createMcpHandler</code> still works but emits a deprecation warning. Move the server to an SDK v2 factory and pass the factory to <code>createMcpHandler</code>. If sessionful behavior prevents an immediate migration, use <code>createLegacyMcpHandler</code> only on the temporary legacy lane.</p>
<p><code>experimental_createMcpHandler</code> is also deprecated. Move its SDK v1 server to an SDK v2 factory. Use <code>createLegacyMcpHandler</code> only as a temporary bridge for sessionful behavior.</p>
<h3 id="createlegacymcphandleroptions"><code>CreateLegacyMcpHandlerOptions</code></h3>
<p><code>CreateLegacyMcpHandlerOptions</code> extends <code>WorkerTransportOptions</code> and adds these fields:</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>route</code></td>
<td><code>string</code></td>
<td><code>&quot;/mcp&quot;</code></td>
<td>Exact path handled by the handler</td>
</tr>
<tr>
<td><code>authContext</code></td>
<td><code>McpAuthContext</code></td>
<td>Execution context props</td>
<td>Application props for tool handlers</td>
</tr>
<tr>
<td><code>transport</code></td>
<td><code>WorkerTransport</code></td>
<td>New transport</td>
<td>Persistent or preconfigured transport</td>
</tr>
</tbody>
</table>
<p>Common <code>WorkerTransportOptions</code> include:</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sessionIdGenerator</code></td>
<td>Creates protocol session IDs</td>
</tr>
<tr>
<td><code>enableJsonResponse</code></td>
<td>Returns JSON instead of SSE where supported</td>
</tr>
<tr>
<td><code>storage</code></td>
<td>Persists transport state through an <code>{ get, set }</code> adapter</td>
</tr>
<tr>
<td><code>eventStore</code></td>
<td>Persists events for replay and stream recovery</td>
</tr>
<tr>
<td><code>corsOptions</code></td>
<td>Adds CORS response and preflight headers</td>
</tr>
<tr>
<td><code>onsessioninitialized</code>, <code>onsessionclosed</code></td>
<td>Observe session lifecycle changes</td>
</tr>
</tbody>
</table>
<p>Create a fresh SDK v1 server for each request unless you provide a persistent transport already connected to that server. One server cannot reconnect to several transports.</p>
<h2 id="authentication-context">Authentication context</h2>
<p>A compatible <code>@cloudflare/workers-oauth-provider</code> supplies verified standard <code>AuthInfo</code> to SDK v2 callbacks at <code>context.http.authInfo</code>.</p>
<p>The existing <code>getMcpAuthContext()</code> helper continues to return application props:</p>
<pre><code class="language-ts">interface McpAuthContext {&#10;	props: Record&lt;string, unknown&gt;;&#10;}&#10;</code></pre>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2246.md")
</div>
<p>Do not log or return <code>authInfo.token</code> or <code>authInfo.extra.props</code>.</p>
<h2 id="migration">Migration</h2>
<p>Refer to <a href="/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/">Migrate to MCP SDK v2</a> before changing an existing server. The migration guide covers dual-era routing, stateful servers, client changes, and rollout checks.</p>
<h2 id="related-resources">Related resources</h2>
<p><a class="nb-card nb-link-card" href="/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/"><h3 id="card-migrate-to-mcp-sdk-v2-agents-model-context-protocol-guides-migrate-to-mcp-sdk-v2">Migrate to MCP SDK v2</h3><p>Choose a migration path and roll out the SDK upgrade.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/model-context-protocol/apis/agent-api/"><h3 id="card-mcpagent-api-agents-model-context-protocol-apis-agent-api">McpAgent API</h3><p>Reference for the deprecated, feature-frozen stateful server path during migration.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/model-context-protocol/guides/securing-mcp-server/"><h3 id="card-secure-mcp-servers-agents-model-context-protocol-guides-securing-mcp-server">Secure MCP servers</h3><p>Protect an MCP endpoint with OAuth.</p></a></p>
