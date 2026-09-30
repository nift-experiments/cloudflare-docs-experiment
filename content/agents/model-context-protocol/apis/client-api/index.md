---
cp9:
  canonical: https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/
  description: Connect Agents to external MCP servers to use their tools, resources, and prompts over the Model Context Protocol.
  full_title: McpClient · Cloudflare Agents docs
  head_html: <title>McpClient · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect Agents to external MCP servers to use their tools, resources, and prompts over the Model Context Protocol."><link rel="canonical" href="https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/index.md"><meta property="og:title" content="McpClient · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect Agents to external MCP servers to use their tools, resources, and prompts over the Model Context Protocol."><meta property="og:url" content="https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><meta name="pcx_tags" content="MCP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/#page","headline":"McpClient \u00b7 Cloudflare Agents docs","description":"Connect Agents to external MCP servers to use their tools, resources, and prompts over the Model Context Protocol.","url":"https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["MCP"]}</script>
  markdown: true
  noindex: false
  route: /agents/model-context-protocol/apis/client-api/
  schema: 1
---
<p>Connect your agent to external <a href="/agents/model-context-protocol/">Model Context Protocol (MCP)</a> servers to use their tools, resources, and prompts. Agents SDK v0.20.0 uses <code>@modelcontextprotocol/client</code> and negotiates stateless or legacy behavior automatically.</p>
<p>Refer to <a href="/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/">Migrate to MCP SDK v2</a> for package, type, OAuth provider, and rollout changes.</p>
<h2 id="overview">Overview</h2>
<p>The MCP client capability lets your agent:</p>
<ul>
<li><strong>Connect to external MCP servers</strong> - GitHub, Slack, databases, AI services</li>
<li><strong>Use their tools</strong> - Call functions exposed by MCP servers</li>
<li><strong>Access resources</strong> - Read data from MCP servers</li>
<li><strong>Use prompts</strong> - Leverage pre-built prompt templates</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2251.md")
</aside>
<h2 id="quick-start">Quick start</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2252.md")
</div>
<p>Connections persist in the agent's <a href="/agents/runtime/lifecycle/state/">SQL storage</a>, and when an agent connects to an MCP server, all tools from that server become available automatically.</p>
<h2 id="adding-mcp-servers">Adding MCP servers</h2>
<p>Use <code>addMcpServer()</code> to connect to an MCP server. For non-OAuth servers, no options are needed:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2253.md")
</div>
<h3 id="stable-server-ids">Stable server IDs</h3>
<p>By default, each connection is assigned a generated <code>nanoid(8)</code> ID. Pass <code>id</code> for connector-style integrations so tools surface as readable keys instead of opaque connection IDs.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2254.md")
</div>
<p>When provided, this <code>id</code> replaces the generated value as the server's ID in storage, restore, <code>listServers()</code>, <code>listTools()</code>, <code>getAITools()</code>, and OAuth state. The supplied ID is normalized via the exported <code>normalizeServerId</code> helper, so values like <code>&quot;GitHub MCP!&quot;</code> become <code>&quot;github-mcp&quot;</code> — guaranteeing the ID is safe to embed in AI SDK tool names and storage keys.</p>
<p>Stable IDs are fully additive — no existing code breaks. If you add <code>{ id: &quot;github&quot; }</code> to an <code>addMcpServer</code> call for a server already registered under an auto-generated ID, the SDK transparently migrates the existing storage row, in-memory connection, and OAuth-related storage keys to the new stable ID. No <code>removeMcpServer</code> step is required. <code>addMcpServer</code> only throws on a genuinely ambiguous collision: the same stable ID already belongs to a <em>different</em> <code>(name, url)</code> server.</p>
<h3 id="transport-options">Transport options</h3>
<p>MCP supports multiple transport types:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2255.md")
</div>
<table>
<thead>
<tr>
<th>Transport</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>auto</code></td>
<td>Auto-detect based on server response (default)</td>
</tr>
<tr>
<td><code>streamable-http</code></td>
<td>HTTP with streaming</td>
</tr>
<tr>
<td><code>sse</code></td>
<td>Server-Sent Events - legacy/compatibility transport</td>
</tr>
</tbody>
</table>
<h3 id="custom-headers">Custom headers</h3>
<p>For servers behind authentication (like Cloudflare Access) or using bearer tokens:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2256.md")
</div>
<h3 id="url-security">URL security</h3>
<p>MCP server URLs are validated before connection to prevent Server-Side Request Forgery (SSRF). The following URL targets are blocked:</p>
<ul>
<li>Private/internal IP ranges (RFC 1918: <code>10.x</code>, <code>172.16-31.x</code>, <code>192.168.x</code>)</li>
<li>Unspecified addresses (<code>0.0.0.0</code>, <code>[::]</code>)</li>
<li>Link-local addresses (<code>169.254.x</code>, <code>fe80::</code>)</li>
<li>IPv6 unique-local addresses (<code>fc00::/7</code>)</li>
<li>IPv4-mapped IPv6 addresses that resolve to private ranges (for example, <code>[::ffff:10.0.0.1]</code>)</li>
<li>Cloud metadata endpoints (<code>metadata.google.internal</code>)</li>
</ul>
<p>Loopback addresses (<code>localhost</code>, <code>127.x.x.x</code>, <code>[::1]</code>) are <strong>allowed</strong> for local development.</p>
<p>For production connections to internal services, use the <a href="/agents/model-context-protocol/protocol/transport/">RPC transport</a> with a Durable Object binding instead of HTTP.</p>
<h3 id="return-value">Return value</h3>
<p><code>addMcpServer()</code> returns the connection state:</p>
<ul>
<li><code>ready</code> - Server connected and tools discovered</li>
<li><code>authenticating</code> - Server requires OAuth; redirect user to <code>authUrl</code></li>
</ul>
<h2 id="oauth-authentication">OAuth authentication</h2>
<p>Many MCP servers require OAuth authentication. The agent handles the OAuth flow automatically.</p>
<h3 id="how-it-works">How it works</h3>
<pre tabindex="0"><code class="language-mermaid">sequenceDiagram&#10;    participant Client&#10;    participant Agent&#10;    participant MCPServer&#10;&#10;    Client-&gt;&gt;Agent: addMcpServer(name, url)&#10;    Agent-&gt;&gt;MCPServer: Connect&#10;    MCPServer--&gt;&gt;Agent: Requires OAuth&#10;    Agent--&gt;&gt;Client: state: authenticating, authUrl&#10;    Client-&gt;&gt;MCPServer: User authorizes&#10;    MCPServer-&gt;&gt;Agent: Callback with code&#10;    Agent-&gt;&gt;MCPServer: Exchange for token&#10;    Agent--&gt;&gt;Client: onMcpUpdate (ready)&#10;</code></pre>
<h3 id="handling-oauth-in-your-agent">Handling OAuth in your agent</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2257.md")
</div>
<h3 id="oauth-callback">OAuth callback</h3>
<p>The callback URL is automatically constructed:</p>
<pre tabindex="0"><code class="language-txt">https://{host}/{agentsPrefix}/{agent-name}/{instance-name}/callback&#10;</code></pre>
<p>For example: <code>https://my-worker.workers.dev/agents/my-agent/default/callback</code></p>
<p>OAuth tokens are securely stored in SQLite, and persist across agent restarts.</p>
<h3 id="protecting-instance-names-in-oauth-callbacks">Protecting instance names in OAuth callbacks</h3>
<p>When using <code>sendIdentityOnConnect: false</code> to hide sensitive instance names (like session IDs or user IDs), the default OAuth callback URL would expose the instance name. To prevent this security issue, you must provide a custom <code>callbackPath</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2258.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="how-callback-matching-works">How callback matching works</h3>
@markup("md", "content/.markup/bodies/2250.md")
</aside>
<h3 id="custom-oauth-callback-handling">Custom OAuth callback handling</h3>
<p>Configure how OAuth completion is handled. By default, successful authentication redirects to your application origin, while failed authentication displays an HTML error page.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2259.md")
</div>
<h2 id="using-mcp-capabilities">Using MCP capabilities</h2>
<p>Once connected, access the server's capabilities:</p>
<h3 id="get-available-tools">Get available tools</h3>
<p>Use <code>listTools()</code> to inspect the raw MCP catalog without preparing tools for an AI SDK model call:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2260.md")
</div>
<p><code>getMcpServers().tools</code> returns the same raw tool records as part of the full MCP client state. Neither API converts the tool schemas.</p>
<h4 id="integration-with-ai-sdk">Integration with AI SDK</h4>
<p>To use MCP tools with the AI SDK, use <code>this.mcp.getAITools()</code> which converts MCP tools to AI SDK format:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2261.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2249.md")
</aside>
<h3 id="resources-and-prompts">Resources and prompts</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2262.md")
</div>
<h3 id="elicitation">Elicitation</h3>
<p>MCP servers can request user input while handling another operation. On the stateless path, elicitation returns <code>input_required</code> and completes through multi-round-trip requests (MRTR). On the legacy path, the server sends pushed <code>elicitation/create</code> requests. Both use form and URL modes.</p>
<p>Register a handler for each mode your Agent supports in <code>onStart()</code>. The same handlers serve both lanes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2263.md")
</div>
<p>The <code>serverId</code> identifies the connection that sent the request. Use it to tell the user which server is asking for input and to apply server-specific policy.</p>
<h4 id="capability-negotiation-and-hibernation">Capability negotiation and hibernation</h4>
<p>The SDK advertises only the modes with configured handlers. Connections on the legacy path advertise them during <code>initialize</code>. Requests on the stateless path carry them with request capabilities. A form-only handler advertises form mode. A URL-only handler advertises URL mode. A connection without handlers advertises no elicitation capability, which lets the server use its fallback.</p>
<p>The SDK stores the advertised modes with each server registration. A connection restored after Durable Object hibernation can therefore advertise the same modes when it reconnects. Callback functions remain in memory and reattach when <code>onStart()</code> runs.</p>
<p>You can explicitly narrow the advertised modes when adding a server:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2264.md")
</div>
<p>An explicit <code>client.capabilities.elicitation</code> value takes precedence over handler-derived modes and persists with the server registration. Do not advertise a mode without a matching handler. If the server sends that mode, the connection returns an error because it cannot handle the request.</p>
<h4 id="form-mode">Form mode</h4>
<p>Form mode collects structured, non-sensitive data in the client. The request includes a restricted JSON Schema in <code>requestedSchema</code>. If the user submits the form, return <code>action: &quot;accept&quot;</code> with matching <code>content</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2265.md")
</div>
<p>Allow the user to review and edit values before submission. Validate accepted content against <code>requestedSchema</code>. Do not use form mode to request passwords, API keys, access tokens, payment credentials, or other secrets.</p>
<h4 id="url-mode">URL mode</h4>
<p>URL mode asks the user to open an external page. Use it for out-of-band interactions that may collect secrets, such as third-party authorization or payment. Keep the URL in the dedicated elicitation path and out of model-visible messages and tool-result text.</p>
<p>A URL handler should:</p>
<ol>
<li>Show which MCP server sent the request.</li>
<li>Show the request message, target host, and full URL.</li>
<li>Ask for consent before opening the URL.</li>
<li>Open the page in a browser context the Agent and model cannot inspect.</li>
<li>Return <code>action: &quot;accept&quot;</code> without <code>content</code> after consent.</li>
<li>Offer distinct decline and cancel controls.</li>
</ol>
<p>Do not prefetch the URL or its metadata. Treat the URL as untrusted input. Production servers should send HTTPS URLs.</p>
<p>For URL mode, <code>accept</code> means the user consented to open the URL. It does not mean the external interaction finished. A server may later send <code>notifications/elicitation/complete</code> with the request <code>elicitationId</code>.</p>
<h4 id="response-actions">Response actions</h4>
<p>Both modes support three actions:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>accept</code></td>
<td>The user submitted the form or consented to open the URL.</td>
</tr>
<tr>
<td><code>decline</code></td>
<td>The user explicitly rejected the request.</td>
</tr>
<tr>
<td><code>cancel</code></td>
<td>The user dismissed the request without making an explicit choice.</td>
</tr>
</tbody>
</table>
<p>Include <code>content</code> only for an accepted form response. Omit it for URL, decline, and cancel responses.</p>
<h4 id="forward-elicitation-to-a-ui">Forward elicitation to a UI</h4>
<p>A handler returns a promise, but the response often comes from a browser. Broadcast the request to connected clients, then resolve the promise through a <code>@callable</code> method:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2266.md")
</div>
<p>The example uses a 55-second timeout because MCP SDK requests default to 60 seconds. If your client call sets a longer request timeout, adjust this timeout to finish first.</p>
<p>Refer to the <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp-client"><code>mcp-client</code> example</a> for the browser implementation. <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp-elicitation-mrtr"><code>mcp-elicitation-mrtr</code></a> demonstrates stateless elicitation. <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp-elicitation"><code>mcp-elicitation</code></a> demonstrates legacy elicitation.</p>
<p>For server-side patterns, refer to <a href="/agents/model-context-protocol/apis/handler-api/#elicitation-with-a-stateless-handler">Elicitation with a stateless handler</a> and <a href="/agents/model-context-protocol/apis/agent-api/#elicitation-on-legacy-servers">Elicitation on legacy servers</a>.</p>
<h2 id="managing-servers">Managing servers</h2>
<p>MCP server registrations persist across Agent restarts. The SDK stores server configuration in SQLite, stores OAuth tokens securely, and restores connections when the Agent wakes.</p>
<h3 id="list-all-servers">List all servers</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2267.md")
</div>
<h3 id="get-server-status">Get server status</h3>
<p>Use the server ID to inspect an individual connection:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2268.md")
</div>
<h3 id="remove-a-server">Remove a server</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2269.md")
</div>
<p>This disconnects from the server and removes it from storage.</p>
<h2 id="client-side-integration">Client-side integration</h2>
<p>Connected clients receive real-time MCP updates via WebSocket:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2270.md")
</div>
<h2 id="api-reference">API reference</h2>
<h3 id="addmcpserver"><code>addMcpServer()</code></h3>
<p>Add a connection to an MCP server and make its tools available to your agent.</p>
<p>Calling <code>addMcpServer</code> is idempotent when both the server name <strong>and</strong> URL match an existing active connection — the existing connection is returned without creating a duplicate. This makes it safe to call in <code>onStart()</code> without worrying about duplicate connections on restart.</p>
<p>If you call <code>addMcpServer</code> with the same name but a <strong>different</strong> URL, a new connection is created. Both connections remain active and their tools are merged in <code>getAITools()</code>. To replace a server, call <code>removeMcpServer(oldId)</code> first.</p>
<p>URLs are normalized before comparison (trailing slashes, default ports, and hostname case are handled), so <code>https://MCP.Example.com</code> and <code>https://mcp.example.com/</code> are treated as the same URL.</p>
<pre tabindex="0"><code class="language-ts">// HTTP transport (Streamable HTTP, SSE)&#10;async addMcpServer(&#10;  serverName: string,&#10;  url: string,&#10;  options?: {&#10;    id?: string;&#10;    callbackHost?: string;&#10;    callbackPath?: string;&#10;    agentsPrefix?: string;&#10;    client?: McpClientOptions;&#10;    transport?: {&#10;      headers?: HeadersInit;&#10;      type?: &quot;sse&quot; | &quot;streamable-http&quot; | &quot;auto&quot;;&#10;    };&#10;    retry?: RetryOptions;&#10;  }&#10;): Promise&lt;&#10;  | { id: string; state: &quot;authenticating&quot;; authUrl: string }&#10;  | { id: string; state: &quot;ready&quot; }&#10;&gt;&#10;&#10;// RPC transport (Durable Object binding — no HTTP overhead)&#10;async addMcpServer(&#10;  serverName: string,&#10;  binding: DurableObjectNamespace,&#10;  options?: {&#10;    id?: string;&#10;    props?: Record&lt;string, unknown&gt;;&#10;    client?: McpClientOptions;&#10;    retry?: RetryOptions;&#10;  }&#10;): Promise&lt;{ id: string; state: &quot;ready&quot; }&gt;&#10;</code></pre>
<h4 id="parameters-http-transport">Parameters (HTTP transport)</h4>
<ul>
<li><code>serverName</code> (string, required) — Display name for the MCP server</li>
<li><code>url</code> (string, required) — URL of the MCP server endpoint</li>
<li><code>options</code> (object, optional) — Connection configuration:
<ul>
<li><code>id</code> — Optional stable, caller-supplied server ID for connector-style integrations. When provided, it replaces the generated <code>nanoid(8)</code> across storage, <code>listServers()</code>, <code>listTools()</code>, <code>getAITools()</code> (so tool keys become readable, for example <code>tool_github_create_pull_request</code>), and OAuth state. Refer to <a href="#stable-server-ids">Stable server IDs</a></li>
<li><code>callbackHost</code> — Host for OAuth callback URL. Only needed for OAuth-authenticated servers. If omitted, automatically derived from the incoming request or WebSocket connection URI — you typically do not need to set this unless you are using a custom domain that differs from the Worker's hostname</li>
<li><code>callbackPath</code> — Custom callback URL path that bypasses the default <code>/agents/{class}/{name}/callback</code> construction. <strong>Required when <code>sendIdentityOnConnect</code> is <code>false</code></strong> to prevent leaking the instance name. When set, the callback URL becomes <code>{callbackHost}/{callbackPath}</code>. You must route this path to the agent instance via <code>getAgentByName</code></li>
<li><code>agentsPrefix</code> — URL prefix for OAuth callback path. Default: <code>&quot;agents&quot;</code>. Ignored when <code>callbackPath</code> is provided</li>
<li><code>client</code> — The Agents-supported <code>McpClientOptions</code> subset from <code>@modelcontextprotocol/client</code>. The default validator supports JSON Schema 2020-12 and legacy draft-07 schemas in Workers</li>
<li><code>transport</code> — Transport layer configuration:
<ul>
<li><code>headers</code> — Custom HTTP headers for authentication</li>
<li><code>type</code> — Transport type: <code>&quot;auto&quot;</code> (default), <code>&quot;streamable-http&quot;</code>, or <code>&quot;sse&quot;</code></li>
</ul>
</li>
<li><code>retry</code> — Retry options for connection and reconnection attempts. Persisted and used when restoring connections after hibernation or after OAuth completion. Default: 3 attempts, 500ms base delay, 5s max delay. Refer to <a href="/agents/runtime/execution/retries/">Retries</a> for details on <code>RetryOptions</code>.</li>
</ul>
</li>
</ul>
<h4 id="parameters-rpc-transport">Parameters (RPC transport)</h4>
<ul>
<li><code>serverName</code> (string, required) — Display name for the MCP server</li>
<li><code>binding</code> (<code>DurableObjectNamespace</code>, required) — The Durable Object binding for the <code>McpAgent</code> class</li>
<li><code>options</code> (object, optional) — Connection configuration:
<ul>
<li><code>id</code> — Optional stable, caller-supplied server ID. Refer to <a href="#stable-server-ids">Stable server IDs</a></li>
<li><code>props</code> — Initialization data passed to the <code>McpAgent</code>'s <code>onStart(props)</code>. Use this to pass user context, configuration, or other data to the MCP server instance</li>
<li><code>client</code> — MCP client configuration options</li>
<li><code>retry</code> — Retry options for the connection</li>
</ul>
</li>
</ul>
<p>RPC transport connects your Agent directly to an <code>McpAgent</code> via Durable Object bindings without HTTP overhead. Refer to <a href="/agents/model-context-protocol/protocol/transport/">MCP Transport</a> for details on configuring RPC transport.</p>
<h4 id="returns">Returns</h4>
<p>A Promise that resolves to a discriminated union based on connection state:</p>
<ul>
<li>
<p>When <code>state</code> is <code>&quot;authenticating&quot;</code>:</p>
<ul>
<li><code>id</code> (string) — Unique identifier for this server connection</li>
<li><code>state</code> (<code>&quot;authenticating&quot;</code>) — Server is waiting for OAuth authorization</li>
<li><code>authUrl</code> (string) — OAuth authorization URL for user authentication</li>
</ul>
</li>
<li>
<p>When <code>state</code> is <code>&quot;ready&quot;</code>:</p>
<ul>
<li><code>id</code> (string) — Unique identifier for this server connection</li>
<li><code>state</code> (<code>&quot;ready&quot;</code>) — Server is fully connected and operational</li>
</ul>
</li>
</ul>
<h3 id="removemcpserver"><code>removeMcpServer()</code></h3>
<p>Disconnect from an MCP server and clean up its resources.</p>
<pre tabindex="0"><code class="language-ts">async removeMcpServer(id: string): Promise&lt;void&gt;&#10;</code></pre>
<h4 id="parameters">Parameters</h4>
<ul>
<li><code>id</code> (string, required) — Server connection ID returned from <code>addMcpServer()</code></li>
</ul>
<h3 id="getmcpservers"><code>getMcpServers()</code></h3>
<p>Get the current state of all MCP server connections.</p>
<pre tabindex="0"><code class="language-ts">getMcpServers(): MCPServersState&#10;</code></pre>
<h4 id="returns-1">Returns</h4>
<pre tabindex="0"><code class="language-ts">type MCPServersState = {&#10;	servers: Record&lt;&#10;		string,&#10;		{&#10;			name: string;&#10;			server_url: string;&#10;			auth_url: string | null;&#10;			state:&#10;				| &quot;authenticating&quot;&#10;				| &quot;connecting&quot;&#10;				| &quot;connected&quot;&#10;				| &quot;discovering&quot;&#10;				| &quot;ready&quot;&#10;				| &quot;failed&quot;;&#10;			capabilities: ServerCapabilities | null;&#10;			instructions: string | null;&#10;			error: string | null;&#10;		}&#10;	&gt;;&#10;	tools: Array&lt;Tool &amp; { serverId: string }&gt;;&#10;	prompts: Array&lt;Prompt &amp; { serverId: string }&gt;;&#10;	resources: Array&lt;Resource &amp; { serverId: string }&gt;;&#10;	resourceTemplates: Array&lt;ResourceTemplate &amp; { serverId: string }&gt;;&#10;};&#10;</code></pre>
<p>The <code>state</code> field indicates the connection lifecycle:</p>
<ul>
<li><code>authenticating</code> — Waiting for OAuth authorization to complete</li>
<li><code>connecting</code> — Establishing transport connection</li>
<li><code>connected</code> — Transport connection established</li>
<li><code>discovering</code> — Discovering server capabilities (tools, resources, prompts)</li>
<li><code>ready</code> — Fully connected and operational</li>
<li><code>failed</code> — Connection failed (see <code>error</code> field for details)</li>
</ul>
<p>The <code>error</code> field contains an error message when <code>state</code> is <code>&quot;failed&quot;</code>. Error messages from external OAuth providers are automatically escaped to prevent XSS attacks, making them safe to display directly in your UI.</p>
<h3 id="configureoauthcallback"><code>configureOAuthCallback()</code></h3>
<p>Configure OAuth callback behavior for MCP servers requiring authentication. This method allows you to customize what happens after a user completes OAuth authorization.</p>
<pre tabindex="0"><code class="language-ts">this.mcp.configureOAuthCallback(options: {&#10;  successRedirect?: string;&#10;  errorRedirect?: string;&#10;  customHandler?: () =&gt; Response | Promise&lt;Response&gt;;&#10;}): void&#10;</code></pre>
<h4 id="parameters-1">Parameters</h4>
<ul>
<li><code>options</code> (object, required) — OAuth callback configuration:
<ul>
<li><code>successRedirect</code> (string, optional) — URL to redirect to after successful authentication</li>
<li><code>errorRedirect</code> (string, optional) — URL to redirect to after failed authentication. Error message is appended as <code>?error=&lt;message&gt;</code> query parameter</li>
<li><code>customHandler</code> (function, optional) — Custom handler for complete control over the callback response. Must return a Response</li>
</ul>
</li>
</ul>
<h4 id="default-behavior">Default behavior</h4>
<p>When no configuration is provided:</p>
<ul>
<li><strong>Success</strong>: Redirects to your application origin</li>
<li><strong>Failure</strong>: Displays an HTML error page with the error message</li>
</ul>
<p>If OAuth fails, the connection state becomes <code>&quot;failed&quot;</code> and the error message is stored in the <code>server.error</code> field for display in your UI.</p>
<h4 id="usage">Usage</h4>
<p>Configure in <code>onStart()</code> before any OAuth flows begin:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2271.md")
</div>
<h3 id="configureelicitationhandlers"><code>configureElicitationHandlers()</code></h3>
<p>Configure handlers for stateless elicitation and legacy <code>elicitation/create</code> requests. Add a handler for each elicitation mode your Agent supports.</p>
<pre tabindex="0"><code class="language-txt">this.mcp.configureElicitationHandlers(handlers?: {&#10;  form?: (&#10;    request: ElicitRequest,&#10;    serverId: string,&#10;    signal?: AbortSignal,&#10;  ) =&gt; Promise&lt;ElicitResult&gt;;&#10;  url?: (&#10;    request: ElicitRequest,&#10;    serverId: string,&#10;    signal?: AbortSignal,&#10;  ) =&gt; Promise&lt;ElicitResult&gt;;&#10;}): void&#10;</code></pre>
<h4 id="parameters-2">Parameters</h4>
<ul>
<li><code>handlers</code> (object, optional) — Elicitation handlers keyed by mode:
<ul>
<li><code>form</code> (function, optional) — Handles form-mode requests for structured, non-sensitive input.</li>
<li><code>url</code> (function, optional) — Handles URL-mode requests for out-of-band interactions.</li>
</ul>
</li>
<li><code>request</code> (<code>ElicitRequest</code>) — The MCP elicitation request. Inspect <code>request.params.mode</code> for the mode-specific fields.</li>
<li><code>serverId</code> (string) — The ID of the MCP server connection that sent the request.</li>
<li><code>signal</code> (<code>AbortSignal</code>, optional) — Aborts when the originating MCP operation is cancelled.</li>
</ul>
<p>Each handler returns a promise containing an <code>ElicitResult</code>. Return <code>accept</code>, <code>decline</code>, or <code>cancel</code>. Accepted form responses include <code>content</code> that matches <code>requestedSchema</code>. URL responses omit <code>content</code>.</p>
<p>Passing <code>undefined</code> clears all configured handlers.</p>
<h4 id="capability-behavior">Capability behavior</h4>
<p>The client advertises only modes with configured handlers during legacy negotiation and on stateless requests. Handler changes apply immediately to live connections, but servers receive updated advertised modes after those connections reconnect.</p>
<p>The SDK stores the handler-derived modes with each MCP server registration. Restored connections advertise those modes after Durable Object hibernation, and callbacks reattach when <code>onStart()</code> runs.</p>
<h4 id="usage-1">Usage</h4>
<p>Configure handlers in <code>onStart()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2272.md")
</div>
<p>For the complete browser forwarding pattern and mode-specific requirements, refer to <a href="#elicitation">Elicitation</a>.</p>
<h2 id="custom-oauth-provider">Custom OAuth provider</h2>
<p>Override the default OAuth provider used when connecting to MCP servers by implementing <code>createMcpOAuthProvider()</code> on your Agent class. This enables custom authentication strategies such as pre-registered client credentials or mTLS, beyond the built-in dynamic client registration.</p>
<p>The override is used for both new connections (<code>addMcpServer</code>) and restored connections after a Durable Object restart.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2273.md")
</div>
<p>If you do not override this method, the agent uses the default provider which performs <a href="https://datatracker.ietf.org/doc/html/rfc7591">OAuth 2.0 Dynamic Client Registration</a> with the MCP server.</p>
<h3 id="custom-storage-backend">Custom storage backend</h3>
<p>To keep the built-in OAuth logic (CSRF state, PKCE, nonce generation, token management) but route token storage to a different backend, import <code>DurableObjectOAuthClientProvider</code> and pass your own storage adapter:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2274.md")
</div>
<h2 id="advanced-mcpclientmanager">Advanced: MCPClientManager</h2>
<p>For fine-grained control, use <code>this.mcp</code> directly:</p>
<h3 id="step-by-step-connection">Step-by-step connection</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2275.md")
</div>
<h3 id="event-subscription">Event subscription</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2276.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2248.md")
</aside>
<h3 id="lifecycle-methods">Lifecycle methods</h3>
<h4 id="this-mcp-registerserver"><code>this.mcp.registerServer()</code></h4>
<p>Register a server without immediately connecting.</p>
<pre tabindex="0"><code class="language-ts">async registerServer(&#10;  id: string,&#10;  options: {&#10;    url: string;&#10;    name: string;&#10;    callbackUrl: string;&#10;    clientOptions?: ClientOptions;&#10;    transportOptions?: TransportOptions;&#10;  }&#10;): Promise&lt;string&gt;&#10;</code></pre>
<h4 id="this-mcp-connecttoserver"><code>this.mcp.connectToServer()</code></h4>
<p>Establish a connection to a previously registered server.</p>
<pre tabindex="0"><code class="language-ts">async connectToServer(id: string): Promise&lt;MCPConnectionResult&gt;&#10;&#10;type MCPConnectionResult =&#10;  | { state: &quot;failed&quot;; error: string }&#10;  | { state: &quot;authenticating&quot;; authUrl: string }&#10;  | { state: &quot;connected&quot; }&#10;</code></pre>
<h4 id="this-mcp-discoverifconnected"><code>this.mcp.discoverIfConnected()</code></h4>
<p>Check server capabilities if a connection is active.</p>
<pre tabindex="0"><code class="language-ts">async discoverIfConnected(&#10;  serverId: string,&#10;  options?: { timeoutMs?: number }&#10;): Promise&lt;MCPDiscoverResult | undefined&gt;&#10;&#10;type MCPDiscoverResult = {&#10;  success: boolean;&#10;  state: MCPConnectionState;&#10;  error?: string;&#10;}&#10;</code></pre>
<h4 id="this-mcp-waitforconnections"><code>this.mcp.waitForConnections()</code></h4>
<p>Wait for all in-flight MCP connection and discovery operations to settle. This is useful when you need <code>this.mcp.getAITools()</code> to return the full set of tools immediately after the agent wakes from hibernation.</p>
<pre tabindex="0"><code class="language-ts">// Wait indefinitely&#10;await this.mcp.waitForConnections();&#10;&#10;// Wait with a timeout (milliseconds)&#10;await this.mcp.waitForConnections({ timeout: 10_000 });&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2247.md")
</aside>
<h4 id="this-mcp-closeconnection"><code>this.mcp.closeConnection()</code></h4>
<p>Close the connection to a specific server while keeping it registered.</p>
<pre tabindex="0"><code class="language-ts">async closeConnection(id: string): Promise&lt;void&gt;&#10;</code></pre>
<h4 id="this-mcp-closeallconnections"><code>this.mcp.closeAllConnections()</code></h4>
<p>Close all active server connections while preserving registrations.</p>
<pre tabindex="0"><code class="language-ts">async closeAllConnections(): Promise&lt;void&gt;&#10;</code></pre>
<h4 id="this-mcp-listtools"><code>this.mcp.listTools()</code></h4>
<p>Get raw MCP tool records without converting their schemas to Zod.</p>
<pre tabindex="0"><code class="language-ts">listTools(filter?: MCPServerFilter): Array&lt;Tool &amp; { serverId: string }&gt;&#10;</code></pre>
<p>Use this method for catalog discovery and inspection. Pass an <code>MCPServerFilter</code> to limit the returned tools to specific connections.</p>
<h4 id="this-mcp-getaitools"><code>this.mcp.getAITools()</code></h4>
<p>Get all discovered MCP tools in a format compatible with the AI SDK.</p>
<pre tabindex="0"><code class="language-ts">getAITools(filter?: MCPServerFilter): ToolSet&#10;</code></pre>
<p>Tools are automatically namespaced by server ID to prevent conflicts when multiple MCP servers expose tools with the same name.</p>
<p><code>getAITools()</code> reuses converted schemas for the current catalog on each live connection. It converts schemas again after discovery replaces the catalog or the live connection changes. Each call returns fresh tool records and execute functions. Use <code>this.mcp.listTools()</code> when you only need the raw catalog.</p>
<p>Pass an <code>MCPServerFilter</code> to scope the returned tools to a subset of connected servers:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2277.md")
</div>
<p>The filter type is available from <code>agents/mcp/client</code>:</p>
<pre tabindex="0"><code class="language-ts">import type { MCPServerFilter } from &quot;agents/mcp/client&quot;;&#10;&#10;type MCPServerFilter = {&#10;	serverId?: string | string[];&#10;	serverName?: string | string[];&#10;	state?: MCPConnectionState | MCPConnectionState[];&#10;};&#10;</code></pre>
<p>All specified filter criteria are AND'd together. The same filter parameter is accepted by <code>listTools()</code>, <code>listPrompts()</code>, <code>listResources()</code>, and <code>listResourceTemplates()</code>.</p>
<h2 id="error-handling">Error handling</h2>
<p>Use error detection utilities to handle connection errors:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2278.md")
</div>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-creating-mcp-servers-agents-model-context-protocol-apis-agent-api"><a href="/agents/model-context-protocol/apis/agent-api/">Creating MCP servers</a></h3><p>Build your own MCP server.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-client-sdk-agents-communication-channels-chat-client-sdk"><a href="/agents/communication-channels/chat/client-sdk/">Client SDK</a></h3><p>Connect from browsers with onMcpUpdate.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-store-and-sync-state-agents-runtime-lifecycle-state"><a href="/agents/runtime/lifecycle/state/">Store and sync state</a></h3><p>Learn about agent persistence.</p></div>
