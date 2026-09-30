<p>MCP tools are functions that an <a href="/agents/model-context-protocol/">MCP server</a> exposes for clients to call. An LLM can invoke a tool to look up data, run a calculation, or call an API. The MCP server executes the tool and returns its result.</p>
<p>Use <code>@modelcontextprotocol/server</code> for a stateless <code>createMcpHandler</code> server. <code>McpAgent</code> is deprecated and feature-frozen. Existing <code>McpAgent</code> routes must keep using <code>@modelcontextprotocol/sdk</code> only while they migrate.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="experimental-webmcp-adapter">Experimental WebMCP adapter</h3>
@markup("md", "content/.markup/bodies/2200.md")
</aside>
<p><a class="nb-card nb-link-card" href="https://github.com/cloudflare/agents/tree/main/examples/webmcp"><h3 id="card-webmcp-example-https-github-com-cloudflare-agents-tree-main-examples-webmcp">WebMCP example</h3><p>Bridge MCP tools from a Cloudflare McpAgent into Chrome's experimental WebMCP API.</p></a></p>
<h2 id="defining-tools">Defining tools</h2>
<p>Use <code>server.registerTool()</code> to register a tool on a stateless <code>McpServer</code> instance. Each tool has a name, a description, an input schema defined with a schema library like <a href="https://zod.dev">Zod</a> or <a href="https://valibot.dev">Valibot</a>, and a handler function.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2201.md")
</div>
<p>The tool handler receives the validated input and must return an object with a <code>content</code> array. Each content item has a <code>type</code> (typically <code>&quot;text&quot;</code>) and the corresponding data.</p>
<h2 id="tool-results">Tool results</h2>
<p>Tool results are returned as an array of content parts. The most common type is <code>text</code>, but you can also return images and embedded resources.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2202.md")
</div>
<p>Set <code>isError: true</code> to signal that the tool call failed. The LLM receives the error message and can decide how to proceed.</p>
<h2 id="tool-descriptions">Tool descriptions</h2>
<p>The <code>description</code> parameter is critical — it is what the LLM reads to decide whether and when to call your tool. Write descriptions that are:</p>
<ul>
<li><strong>Specific</strong> about what the tool does: &quot;Get the current weather for a city&quot; is better than &quot;Weather tool&quot;</li>
<li><strong>Clear about inputs</strong>: &quot;Requires a city name as a string&quot; helps the LLM format the call correctly</li>
<li><strong>Honest about limitations</strong>: &quot;Only supports US cities&quot; prevents the LLM from calling it with unsupported inputs</li>
</ul>
<h2 id="input-validation-with-zod">Input validation with Zod</h2>
<p>Tool inputs are defined as Zod schemas and validated automatically before the handler runs. Use Zod's <code>.describe()</code> method to give the LLM context about each parameter.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2203.md")
</div>
<h2 id="using-tools-with-createmcphandler">Using tools with <code>createMcpHandler</code></h2>
<p>For stateless MCP servers, define tools inside a factory function and pass the server to <a href="/agents/model-context-protocol/apis/handler-api/"><code>createMcpHandler</code></a>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2204.md")
</div>
<h2 id="using-tools-with-mcpagent">Using tools with <code>McpAgent</code></h2>
<p>This section applies only to existing legacy routes during migration. Define their tools in the <code>init()</code> method of an <a href="/agents/model-context-protocol/apis/agent-api/"><code>McpAgent</code></a>. Tools have access to the agent instance through <code>this</code>, so they can read and write state.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2205.md")
</div>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/model-context-protocol/guides/remote-mcp-server/"><h3 id="card-build-a-remote-mcp-server-agents-model-context-protocol-guides-remote-mcp-server">Build a remote MCP server</h3><p>Step-by-step guide to deploying an MCP server on Cloudflare.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/model-context-protocol/apis/handler-api/"><h3 id="card-createmcphandler-api-agents-model-context-protocol-apis-handler-api">createMcpHandler API</h3><p>Reference for stateless MCP servers.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/model-context-protocol/apis/agent-api/"><h3 id="card-mcpagent-api-agents-model-context-protocol-apis-agent-api">McpAgent API</h3><p>Reference for stateful MCP servers.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/model-context-protocol/protocol/authorization/"><h3 id="card-mcp-authorization-agents-model-context-protocol-protocol-authorization">MCP authorization</h3><p>Add OAuth authentication to your MCP server.</p></a></p>
