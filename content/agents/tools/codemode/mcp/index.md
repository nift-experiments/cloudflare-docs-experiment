<p>Use <code>McpConnector</code> to expose tools from an existing Model Context Protocol (MCP) client connection inside the Code Mode sandbox. The connector works with the durable runtime, including discovery, approvals, and execution history.</p>
<p>This page covers an Agent consuming an MCP server. To publish Code Mode as an MCP server, refer to <a href="/agents/model-context-protocol/codemode/">Code Mode MCP server patterns</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need:</p>
<ul>
<li>A project with the <a href="/agents/tools/codemode/durable-runtime/">durable Code Mode runtime</a> configured. That setup provides the Worker Loader binding and the <code>CodemodeRuntime</code> export.</li>
<li>An existing Agents SDK MCP connection. To create and authorize the connection, refer to the <a href="/agents/model-context-protocol/apis/client-api/">McpClient API</a>.</li>
</ul>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2670.md")
</div>
<p>When the model calls <code>github.create_issue()</code>, the runtime returns a paused execution. Approve that execution through the runtime to execute the MCP tool and continue the same sandbox program.</p>
<h2 id="use-an-ai-sdk-tool-collection">Use an AI SDK tool collection</h2>
<p>For a smaller integration without durable approvals or <code>codemode.search()</code> and <code>codemode.describe()</code>, pass the Agents SDK tool collection directly to <code>createCodeTool()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2671.md")
</div>
<p>This approach exposes the MCP tools under the default <code>codemode</code> namespace. It does not use the connector runtime's durable pause, approval, and resume flow. Use <code>McpConnector</code> when tools can cause side effects or when the model needs on-demand discovery.</p>
<p><code>getAITools()</code> converts MCP input and output schemas for use by the AI SDK. The Agents SDK reuses those converted schemas while each live connection keeps the same current catalog. Use <code>this.mcp.listTools()</code> instead when you only need to inspect the raw MCP catalog.</p>
