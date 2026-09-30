<p>Remote, authorized connections are an evolving part of the <a href="https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization">Model Context Protocol (MCP) specification</a>. Not all MCP clients support remote connections yet.</p>
<p>This guide will show you options for how to start using your remote MCP server with MCP clients that support remote connections. If you haven't yet created and deployed a remote MCP server, you should follow the <a href="/agents/model-context-protocol/guides/remote-mcp-server/">Build a Remote MCP Server</a> guide first.</p>
<h2 id="the-model-context-protocol-mcp-inspector">The Model Context Protocol (MCP) inspector</h2>
<p>The <a href="https://github.com/modelcontextprotocol/inspector"><code>@modelcontextprotocol/inspector</code> package</a> is a visual testing tool for MCP servers.</p>
<ol>
<li>Open a terminal and run the following command:</li>
</ol>
<pre><code class="language-sh">npx @modelcontextprotocol/inspector&#10;</code></pre>
<pre><code class="language-sh">🚀 MCP Inspector is up and running at:&#10;	http://localhost:5173/?MCP_PROXY_AUTH_TOKEN=46ab..cd3&#10;&#10;🌐 Opening browser...&#10;</code></pre>
<pre><code>    The MCP Inspector will launch in your web browser. You can also launch it manually by opening a browser and going to `http://localhost:&lt;PORT&gt;`. Check the command output for the local port where MCP Inspector is running. In this example, MCP Inspector is served on port `5173`.&#10;</code></pre>
<ol start="2">
<li>
<p>In the MCP inspector, enter the URL of your MCP server (for example, <code>http://localhost:8788/mcp</code>). Select <strong>Connect</strong>.</p>
<p>You can connect to an MCP server running on your local machine or a remote MCP server running on Cloudflare.</p>
</li>
<li>
<p>If your server requires authentication, the connection will fail. To authenticate:</p>
<ol>
<li>In MCP Inspector, select <strong>Open Auth settings</strong>.</li>
<li>Select <strong>Quick OAuth Flow</strong>.</li>
<li>Once you have authenticated with the OAuth provider, you will be redirected back to MCP Inspector. Select <strong>Connect</strong>.</li>
</ol>
</li>
</ol>
<p>You should see the <strong>List tools</strong> button, which will list the tools that your MCP server exposes.</p>
<h2 id="connect-your-remote-mcp-server-to-cloudflare-workers-ai-playground">Connect your remote MCP server to Cloudflare Workers AI Playground</h2>
<p>Visit the <a href="https://playground.ai.cloudflare.com/">Workers AI Playground</a>, enter your MCP server URL, and click &quot;Connect&quot;. Once authenticated (if required), you should see your tools listed and they will be available to the AI model in the chat.</p>
<h2 id="connect-your-remote-mcp-server-to-claude-desktop-via-a-local-proxy">Connect your remote MCP server to Claude Desktop via a local proxy</h2>
<p>You can use the <a href="https://www.npmjs.com/package/mcp-remote"><code>mcp-remote</code> local proxy</a> to connect Claude Desktop to your remote MCP server. This lets you test what an interaction with your remote MCP server will be like with a real-world MCP client.</p>
<ol>
<li>Open Claude Desktop and navigate to Settings -&gt; Developer -&gt; Edit Config. This opens the configuration file that controls which MCP servers Claude can access.</li>
<li>Replace the content with a configuration like this:</li>
</ol>
<pre><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;my-server&quot;: {&#10;			&quot;command&quot;: &quot;npx&quot;,&#10;			&quot;args&quot;: [&quot;mcp-remote&quot;, &quot;http://my-mcp-server.my-account.workers.dev/mcp&quot;]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<ol start="3">
<li>Save the file and restart Claude Desktop (command/ctrl + R). When Claude restarts, a browser window will open showing your OAuth login page. Complete the authorization flow to grant Claude access to your MCP server.</li>
</ol>
<p>Once authenticated, you'll be able to see your tools by clicking the tools icon in the bottom right corner of Claude's interface.</p>
<h2 id="connect-your-remote-mcp-server-to-cursor">Connect your remote MCP server to Cursor</h2>
<p>Connect <a href="https://cursor.com/docs/context/mcp">Cursor</a> to your remote MCP server by editing the project's <code>.cursor/mcp.json</code> file or a global <code>~/.cursor/mcp.json</code> file and adding the following configuration:</p>
<pre><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;my-server&quot;: {&#10;			&quot;url&quot;: &quot;http://my-mcp-server.my-account.workers.dev/mcp&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h2 id="connect-your-remote-mcp-server-to-windsurf">Connect your remote MCP server to Windsurf</h2>
<p>You can connect your remote MCP server to <a href="https://docs.windsurf.com">Windsurf</a> by editing the <a href="https://docs.windsurf.com/windsurf/cascade/mcp"><code>mcp_config.json</code> file</a>, and adding the following configuration:</p>
<pre><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;my-server&quot;: {&#10;			&quot;serverUrl&quot;: &quot;http://my-mcp-server.my-account.workers.dev/mcp&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
