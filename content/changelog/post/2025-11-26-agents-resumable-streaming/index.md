<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 26, 2025</time><h2 id="post-title">Agents SDK v0.2.24 with resumable streaming, MCP improvements, and schedule fixes</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of <a href="https://github.com/cloudflare/agents">@cloudflare/agents</a> brings resumable streaming, significant MCP client improvements, and critical fixes for schedules and Durable Object lifecycle management.</p>
<h4 id="resumable-streaming">Resumable streaming</h4>
<p><code>AIChatAgent</code> now supports resumable streaming, allowing clients to reconnect and continue receiving streamed responses without losing data. This is useful for:</p>
<ul>
<li>Long-running AI responses</li>
<li>Users on unreliable networks</li>
<li>Users switching between devices mid-conversation</li>
<li>Background tasks where users navigate away and return</li>
<li>Real-time collaboration where multiple clients need to stay in sync</li>
</ul>
<p>Streams are maintained across page refreshes, broken connections, and syncing across open tabs and devices.</p>
<h4 id="other-improvements">Other improvements</h4>
<ul>
<li>Default JSON schema validator added to MCP client</li>
<li><a href="https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/">Schedules</a> can now safely destroy the agent</li>
</ul>
<h4 id="mcp-client-api-improvements">MCP client API improvements</h4>
<p>The <code>MCPClientManager</code> API has been redesigned for better clarity and control:</p>
<ul>
<li><strong>New <code>registerServer()</code> method</strong>: Register MCP servers without immediately connecting</li>
<li><strong>New <code>connectToServer()</code> method</strong>: Establish connections to registered servers</li>
<li><strong>Improved reconnect logic</strong>: <code>restoreConnectionsFromStorage()</code> now properly handles failed connections</li>
</ul>
<pre><code class="language-ts">// Register a server to Agent&#10;const { id } = await this.mcp.registerServer({&#10;	name: &quot;my-server&quot;,&#10;	url: &quot;https://my-mcp-server.example.com&quot;,&#10;});&#10;&#10;// Connect when ready&#10;await this.mcp.connectToServer(id);&#10;&#10;// Discover tools, prompts and resources&#10;await this.mcp.discoverIfConnected(id);&#10;</code></pre>
<p>The SDK now includes a formalized <code>MCPConnectionState</code> enum with states: <code>idle</code>, <code>connecting</code>, <code>authenticating</code>, <code>connected</code>, <code>discovering</code>, and <code>ready</code>.</p>
<h4 id="enhanced-mcp-discovery">Enhanced MCP discovery</h4>
<p>MCP discovery fetches the available tools, prompts, and resources from an MCP server so your agent knows what capabilities are available. The <code>MCPClientConnection</code> class now includes a dedicated <code>discover()</code> method with improved reliability:</p>
<ul>
<li>Supports cancellation via AbortController</li>
<li>Configurable timeout (default 15s)</li>
<li>Discovery failures now throw errors immediately instead of silently continuing</li>
</ul>
<h4 id="bug-fixes">Bug fixes</h4>
<ul>
<li>Fixed a bug where <a href="https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/">schedules</a> meant to fire immediately with this.schedule(0, ...) or <code>this.schedule(new Date(), ...)</code> would not fire</li>
<li>Fixed an issue where schedules that took longer than 30 seconds would occasionally time out</li>
<li>Fixed SSE transport now properly forwards session IDs and request headers</li>
<li>Fixed AI SDK stream events conversion to UIMessageStreamPart</li>
</ul>
<h4 id="upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i agents@latest&#10;</code></pre>
</div></article></div>
