<p>You can build and deploy <a href="https://modelcontextprotocol.io/">Model Context Protocol (MCP)</a> servers on Cloudflare.</p>
<h2 id="what-is-the-model-context-protocol-mcp">What is the Model Context Protocol (MCP)?</h2>
<p><a href="https://modelcontextprotocol.io">Model Context Protocol (MCP)</a> is an open standard that connects AI systems with external applications. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various accessories, MCP provides a standardized way to connect AI agents to different services.</p>
<h3 id="mcp-terminology">MCP Terminology</h3>
<ul>
<li><strong>MCP Hosts</strong>: AI assistants (like <a href="https://claude.ai">Claude</a> or <a href="https://cursor.com">Cursor</a>), AI agents, or applications that need to access external capabilities.</li>
<li><strong>MCP Clients</strong>: Clients embedded within the MCP hosts that connect to MCP servers and invoke tools. Each MCP client instance has a single connection to an MCP server.</li>
<li><strong>MCP Servers</strong>: Applications that expose <a href="/agents/model-context-protocol/protocol/tools/">tools</a>, <a href="https://modelcontextprotocol.io/docs/concepts/prompts">prompts</a>, and <a href="https://modelcontextprotocol.io/docs/concepts/resources">resources</a> that MCP clients can use.</li>
</ul>
<h3 id="remote-vs-local-mcp-connections">Remote vs. local MCP connections</h3>
<p>The MCP standard supports two modes of operation:</p>
<ul>
<li><strong>Remote MCP connections</strong>: MCP clients connect to MCP servers over the Internet, establishing a connection using <a href="/agents/model-context-protocol/protocol/transport/">Streamable HTTP</a>, and authorizing the MCP client access to resources on the user's account using <a href="/agents/model-context-protocol/protocol/authorization/">OAuth</a>.</li>
<li><strong>Local MCP connections</strong>: MCP clients connect to MCP servers on the same machine, using <a href="https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#stdio">stdio</a> as a local transport method.</li>
</ul>
<h3 id="best-practices">Best Practices</h3>
<ul>
<li><strong>Tool design</strong>: Do not treat your MCP server as a wrapper around your full API schema. Instead, build tools that are optimized for specific user goals and reliable outcomes. Fewer, well-designed tools often outperform many granular ones, especially for agents with small context windows or tight latency budgets.</li>
<li><strong>Scoped permissions</strong>: Deploying several focused MCP servers, each with narrowly scoped permissions, reduces the risk of over-privileged access and makes it easier to manage and audit what each server is allowed to do.</li>
<li><strong>Tool descriptions</strong>: Detailed parameter descriptions help agents understand how to use your tools correctly — including what values are expected, how they affect behavior, and any important constraints. This reduces errors and improves reliability.</li>
<li><strong>Evaluation tests</strong>: Use evaluation tests ('evals') to measure the agent’s ability to use your tools correctly. Run these after any updates to your server or tool descriptions to catch regressions early and track improvements over time.</li>
</ul>
<h3 id="get-started">Get Started</h3>
<p>Go to the <a href="/agents/model-context-protocol/guides/remote-mcp-server/">Getting Started</a> guide to learn how to build and deploy your first remote MCP server to Cloudflare.</p>
