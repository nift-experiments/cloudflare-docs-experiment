<p>Agents can use <a href="/agents/model-context-protocol/">Model Context Protocol (MCP)</a> as clients. Connect an agent to external MCP servers, discover the tools those servers expose, and pass those tools into model calls.</p>
<p>Use MCP when you want an agent to:</p>
<ul>
<li>Call tools exposed by external MCP servers.</li>
<li>Reuse tools across agents, IDEs, and other AI clients.</li>
<li>Connect to services that already expose an MCP endpoint.</li>
<li>Add OAuth or token-based authorization around external tool access.</li>
</ul>
<p>To build an MCP server instead, refer to <a href="/agents/model-context-protocol/">Model Context Protocol (MCP)</a>.</p>
<h2 id="basic-pattern">Basic pattern</h2>
<p>Call <code>addMcpServer()</code> to connect to a remote MCP server, then pass <code>this.mcp.getAITools()</code> to the AI SDK.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1843.md")
</div>
<p>If the server requires OAuth, <code>addMcpServer()</code> returns an authentication state and authorization URL. The connection is persisted in the agent's <a href="/agents/runtime/lifecycle/state/">SQL storage</a>.</p>
<h2 id="configuration">Configuration</h2>
<p>For public MCP servers, no binding configuration is required. Store server URLs, API tokens, or OAuth settings as environment variables or secrets.</p>
<p>For MCP servers that require bearer tokens or Cloudflare Access headers, pass custom transport headers when connecting.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1844.md")
</div>
<h2 id="related-resources">Related resources</h2>
<p><a class="nb-card nb-link-card" href="/agents/model-context-protocol/apis/client-api/"><h3 id="card-mcpclient-api-agents-model-context-protocol-apis-client-api">McpClient API</h3><p>Connect Agents to external MCP servers and use their tools, resources, and prompts.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/model-context-protocol/guides/connect-mcp-client/"><h3 id="card-connect-to-an-mcp-server-agents-model-context-protocol-guides-connect-mcp-client">Connect to an MCP server</h3><p>Create an Agent that connects to an external MCP server and uses its tools.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/tools/codemode/mcp/"><h3 id="card-use-mcp-tools-with-code-mode-agents-tools-codemode-mcp">Use MCP tools with Code Mode</h3><p>Use progressive discovery, code-based composition, and durable approvals with MCP tools.</p></a></p>
<p><a class="nb-card nb-link-card" href="https://modelcontextprotocol.io/"><h3 id="card-model-context-protocol-specification-https-modelcontextprotocol-io">Model Context Protocol specification</h3><p>Learn about the open protocol for connecting AI applications to external tools and data.</p></a></p>
