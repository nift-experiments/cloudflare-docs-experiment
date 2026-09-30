<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 25, 2026</time><h2 id="post-title">Agents SDK v0.6.0: RPC transport for MCP, optional OAuth, hardened schema conversion, and @cloudflare/ai-chat fixes</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> lets you define an Agent and an McpAgent in the same Worker and connect them over RPC — no HTTP, no network overhead. It also makes OAuth opt-in for simple MCP connections, hardens the schema converter for production workloads, and ships a batch of <code>@cloudflare/ai-chat</code> reliability fixes.</p>
<h4 id="rpc-transport-for-mcp">RPC transport for MCP</h4>
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
<h4 id="optional-oauth-for-mcp-connections">Optional OAuth for MCP connections</h4>
<p><code>addMcpServer()</code> no longer eagerly creates an OAuth provider for every connection. For servers that do not require authentication, a simple call is all you need:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17643.md")</div>
<p>If the server responds with a 401, the SDK throws a clear error: <code>&quot;This MCP server requires OAuth authentication. Provide callbackHost in addMcpServer options to enable the OAuth flow.&quot;</code> The restore-from-storage flow also handles missing callback URLs gracefully, skipping auth provider creation for non-OAuth servers.</p>
<h4 id="hardened-json-schema-to-typescript-converter">Hardened JSON Schema to TypeScript converter</h4>
<p>The schema converter used by <code>generateTypes()</code> and <code>getAITools()</code> now handles edge cases that previously caused crashes in production:</p>
<ul>
<li><strong>Depth and circular reference guards</strong> — Prevents stack overflows on recursive or deeply nested schemas</li>
<li><strong><code>$ref</code> resolution</strong> — Supports internal JSON Pointers (<code>#/definitions/...</code>, <code>#/$defs/...</code>, <code>#</code>)</li>
<li><strong>Tuple support</strong> — <code>prefixItems</code> (JSON Schema 2020-12) and array <code>items</code> (draft-07)</li>
<li><strong>OpenAPI 3.0 <code>nullable: true</code></strong> — Supported across all schema branches</li>
<li><strong>Per-tool error isolation</strong> — One malformed schema cannot crash the full pipeline in <code>generateTypes()</code> or <code>getAITools()</code></li>
<li><strong>Missing <code>inputSchema</code> fallback</strong> — <code>getAITools()</code> falls back to <code>{ type: &quot;object&quot; }</code> instead of throwing</li>
</ul>
<h4 id="cloudflare-ai-chat-fixes"><code>@cloudflare/ai-chat</code> fixes</h4>
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
<h4 id="upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>
</div></article></div>
