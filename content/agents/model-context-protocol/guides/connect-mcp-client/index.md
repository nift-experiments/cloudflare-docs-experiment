<p>Your Agent can connect to external <a href="https://modelcontextprotocol.io">Model Context Protocol (MCP)</a> servers to access their tools and extend your Agent's capabilities. In this tutorial, you'll create an Agent that connects to an MCP server and uses one of its tools.</p>
<h2 id="what-you-will-build">What you will build</h2>
<p>An Agent with endpoints to:</p>
<ul>
<li>Connect to an MCP server</li>
<li>List available tools from connected servers</li>
<li>Get the connection status</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<p>An MCP server to connect to (or use the public example in this tutorial).</p>
<h2 id="1-create-a-basic-agent"><ol>
<li>Create a basic Agent</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2229.md")
</div>
<h2 id="2-add-mcp-connection-endpoint"><ol start="2">
<li>Add MCP connection endpoint</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2231.md")
</div>
<p>The <code>addMcpServer()</code> method connects to an MCP server. If the server requires OAuth authentication, it returns an <code>authUrl</code> that users must visit to complete authorization.</p>
<h2 id="3-test-the-connection"><ol start="3">
<li>Test the connection</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2232.md")
</div>
<h2 id="4-list-available-tools"><ol start="4">
<li>List available tools</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2234.md")
</div>
<h2 id="summary">Summary</h2>
<p>You created an Agent that can:</p>
<ul>
<li>Connect to external MCP servers dynamically</li>
<li>Handle OAuth authentication flows when required</li>
<li>List all available tools from connected servers</li>
<li>Monitor connection status</li>
</ul>
<p>Connections persist in the Agent's <a href="/agents/runtime/lifecycle/state/">SQL storage</a>, so they remain active across requests.</p>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/model-context-protocol/guides/oauth-mcp-client/"><h3 id="card-handle-oauth-flows-agents-model-context-protocol-guides-oauth-mcp-client">Handle OAuth flows</h3><p>Configure OAuth callbacks and error handling.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/model-context-protocol/apis/client-api/"><h3 id="card-mcp-client-api-agents-model-context-protocol-apis-client-api">MCP Client API</h3><p>Complete API documentation for MCP clients.</p></a></p>
