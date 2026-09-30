<p>The Model Context Protocol (MCP) specification defines two standard <a href="https://modelcontextprotocol.io/specification/2025-06-18/basic/transports">transport mechanisms</a> for communication between clients and servers:</p>
<ol>
<li><strong>stdio</strong> — Communication over standard in and standard out, designed for local MCP connections.</li>
<li><strong>Streamable HTTP</strong> — The standard transport method for remote MCP connections, <a href="https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http">introduced</a> in March 2025. It uses a single HTTP endpoint for bidirectional messaging.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2191.md")
</aside>
<p>MCP servers built with the <a href="/agents">Agents SDK</a> use <a href="/agents/model-context-protocol/apis/handler-api/"><code>createMcpHandler</code></a> to handle Streamable HTTP transport.</p>
<h2 id="implementing-remote-mcp-transport">Implementing remote MCP transport</h2>
<p>Use <a href="/agents/model-context-protocol/apis/handler-api/"><code>createMcpHandler</code></a> to create an MCP server that handles Streamable HTTP transport. This is the recommended approach for new MCP servers.</p>
<h4 id="get-started-quickly">Get started quickly</h4>
<p>You can use the &quot;Deploy to Cloudflare&quot; button to create a remote MCP server.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/mcp-worker"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<h4 id="remote-mcp-server-without-authentication">Remote MCP server (without authentication)</h4>
<p>Create an MCP server using <code>createMcpHandler</code>. View the <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp-worker">complete example on GitHub</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2192.md")
</div>
<h4 id="mcp-server-with-authentication">MCP server with authentication</h4>
<p>If your MCP server implements authentication &amp; authorization using the <a href="https://github.com/cloudflare/workers-oauth-provider">Workers OAuth Provider</a> library, use <code>createMcpHandler</code> with the <code>apiRoute</code> and <code>apiHandler</code> properties. View the <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp-worker-authenticated">complete example on GitHub</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2193.md")
</div>
<h3 id="servers-that-need-protocol-sessions">Servers that need protocol sessions</h3>
<p>MCP has no protocol-level session on the stateless path. Applications can store durable business data behind a separate storage boundary.</p>
<p>While migrating legacy sessions, existing servers can keep a temporary <code>createLegacyMcpHandler</code> with <code>WorkerTransport</code> or <code>McpAgent</code> route beside the new stateless route. These APIs support transport state, event replay, pushed elicitation, sampling, and roots requests. <code>McpAgent</code> is deprecated and feature-frozen.</p>
<p>Add the stateless route before moving clients, and keep both lanes until existing sessions drain. Refer to <a href="/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/">Migrate to MCP SDK v2</a> for the staged migration. Refer to <a href="/agents/model-context-protocol/apis/agent-api/#stream-resumability"><code>McpAgent</code>: Stream resumability</a> for existing stream behavior.</p>
<h2 id="rpc-transport">RPC transport</h2>
<p>The <strong>RPC transport</strong> is designed for internal applications where your MCP server and agent are both running on Cloudflare — they can even run in the same Worker. It sends JSON-RPC messages directly over Cloudflare's <a href="/workers/runtime-apis/bindings/service-bindings/rpc/">RPC bindings</a> without going over the public internet.</p>
<ul>
<li><strong>Faster</strong> — no network overhead, direct function calls between Durable Objects</li>
<li><strong>Simpler</strong> — no HTTP endpoints, no connection management</li>
<li><strong>Internal only</strong> — perfect for agents calling MCP servers within the same Worker</li>
</ul>
<p>RPC transport does not support authentication. Use Streamable HTTP for external connections that require OAuth.</p>
<h3 id="connect-an-agent-to-an-existing-mcpagent-through-rpc">Connect an Agent to an existing <code>McpAgent</code> through RPC</h3>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecated-server-path">Deprecated server path</h3>
@markup("md", "content/.markup/bodies/2190.md")
</aside>
<h4 id="1-define-your-mcp-server"><ol>
<li>Define your MCP server</li>
</ol></h4>
<p>Create your <code>McpAgent</code> with the tools you want to expose:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2194.md")
</div>
<h4 id="2-connect-your-agent-to-the-mcp-server"><ol start="2">
<li>Connect your Agent to the MCP server</li>
</ol></h4>
<p>In your <code>Agent</code>, call <code>addMcpServer()</code> with the Durable Object binding in <code>onStart()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2195.md")
</div>
<p>RPC connections are automatically restored after Durable Object hibernation, just like HTTP connections. The binding name and props are persisted to storage so the connection can be re-established without any extra code.</p>
<p>For RPC transport, if <code>addMcpServer</code> is called with a name that already has an active connection, the existing connection is returned instead of creating a duplicate. For HTTP transport, deduplication matches on both server name and URL (refer to <a href="/agents/model-context-protocol/apis/client-api/">MCP Client API</a> for details). This makes it safe to call in <code>onStart()</code>.</p>
<h4 id="3-configure-durable-object-bindings"><ol start="3">
<li>Configure Durable Object bindings</li>
</ol></h4>
<p>In your <code>wrangler.jsonc</code>, define bindings for both Durable Objects:</p>
<pre><code class="language-jsonc">{&#10;	&quot;durable_objects&quot;: {&#10;		&quot;bindings&quot;: [&#10;			{ &quot;name&quot;: &quot;Chat&quot;, &quot;class_name&quot;: &quot;Chat&quot; },&#10;			{ &quot;name&quot;: &quot;MyMCP&quot;, &quot;class_name&quot;: &quot;MyMCP&quot; },&#10;		],&#10;	},&#10;	&quot;migrations&quot;: [&#10;		{&#10;			&quot;new_sqlite_classes&quot;: [&quot;MyMCP&quot;, &quot;Chat&quot;],&#10;			&quot;tag&quot;: &quot;v1&quot;,&#10;		},&#10;	],&#10;}&#10;</code></pre>
<h4 id="4-set-up-your-worker-fetch-handler"><ol start="4">
<li>Set up your Worker fetch handler</li>
</ol></h4>
<p>Route requests to your Chat agent:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2196.md")
</div>
<h3 id="passing-props-to-the-mcp-server">Passing props to the MCP server</h3>
<p>Since RPC transport does not have an OAuth flow, you can pass user context directly as props:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2197.md")
</div>
<p>Your <code>McpAgent</code> can then access these props:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2198.md")
</div>
<p>Props are type-safe (TypeScript extracts the Props type from your <code>McpAgent</code> generic), persistent (stored in Durable Object storage), and available immediately before any tool calls are made.</p>
<h3 id="configuring-rpc-transport-server-timeout">Configuring RPC transport server timeout</h3>
<p>The RPC transport has a configurable timeout for waiting for tool responses. By default, the server waits <strong>60 seconds</strong> for a tool handler to respond. You can customize this by overriding <code>getRpcTransportOptions()</code> in your <code>McpAgent</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2199.md")
</div>
<h2 id="choosing-a-transport">Choosing a transport</h2>
<table>
<thead>
<tr>
<th>Transport</th>
<th>Use when</th>
<th>Pros</th>
<th>Cons</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Streamable HTTP</strong></td>
<td>External MCP servers, production apps</td>
<td>Standard protocol, secure, supports auth</td>
<td>Slight network overhead</td>
</tr>
<tr>
<td><strong>RPC</strong></td>
<td>Internal agents on Cloudflare</td>
<td>Fastest, simplest setup</td>
<td>No auth, Durable Object bindings only</td>
</tr>
<tr>
<td><strong>SSE</strong></td>
<td>Compatibility with older clients</td>
<td>Backwards compatible</td>
<td>Deprecated, use Streamable HTTP</td>
</tr>
</tbody>
</table>
<h3 id="migrate-from-mcpagent">Migrate from McpAgent</h3>
<p>If the endpoint does not use legacy stateful features, migrate directly to a stateless server factory from <code>@modelcontextprotocol/server</code> and pass it to <code>createMcpHandler</code>.</p>
<p>If it depends on MCP session state, RPC, pushed server-to-client requests, standalone streams, or replay, first design stateless equivalents. For example, move business state behind explicit application storage and replace pushed input requests with stateless elicitation. Serve stateless and legacy lanes together while clients migrate and existing sessions drain.</p>
<p>Refer to <a href="/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/">Migrate to MCP SDK v2</a> for the feature mapping, dual-era routing, and rollout steps.</p>
<h3 id="testing-with-mcp-clients">Testing with MCP clients</h3>
<p>You can test your MCP server using an MCP client that supports remote connections, or use <a href="https://www.npmjs.com/package/mcp-remote"><code>mcp-remote</code></a>, an adapter that lets MCP clients that only support local connections work with remote MCP servers.</p>
<p>Follow <a href="/agents/model-context-protocol/guides/test-remote-mcp-server/">this guide</a> for instructions on how to connect to your remote MCP server to Claude Desktop, Cursor, Windsurf, and other MCP clients.</p>
