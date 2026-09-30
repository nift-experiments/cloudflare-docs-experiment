<p>Cloudflare runs a catalog of managed remote MCP servers which you can connect to using OAuth on clients like <a href="https://modelcontextprotocol.io/quickstart/user">Claude</a>, <a href="https://docs.windsurf.com/windsurf/cascade/mcp">Windsurf</a>, our own <a href="https://playground.ai.cloudflare.com/">AI Playground</a> or any <a href="https://github.com/cloudflare/agents/tree/main/packages/agents/src/mcp">SDK that supports MCP</a>.</p>
<p>These MCP servers allow your MCP client to read configurations from your account, process information, make suggestions based on data, and even make those suggested changes for you. All of these actions can happen across Cloudflare's many services including application development, security and performance.</p>
<p>Use the Streamable HTTP endpoint at <code>/mcp</code> for new connections. The servers support the new MCP 2026-07-28 Specification and stateless requests from 2025 Streamable HTTP clients. Historical <code>/sse</code> URLs remain available as aliases for the same Streamable HTTP handler, but they do not serve the deprecated HTTP+SSE transport. Clients configured to force SSE transport must switch to Streamable HTTP or automatic transport detection.</p>
<h2 id="cloudflare-api-mcp-server">Cloudflare API MCP server</h2>
<p>The <a href="https://github.com/cloudflare/mcp">Cloudflare API MCP server</a> provides access to the entire <a href="/api/">Cloudflare API</a> — over 2,500 endpoints across DNS, Workers, R2, Zero Trust, and every other product — through just two tools: <code>search()</code> and <code>execute()</code>.</p>
<p>It uses <a href="/agents/model-context-protocol/codemode/#search-and-execute">the search-and-execute Code Mode pattern</a>, a technique where the model writes JavaScript against a typed representation of the OpenAPI spec and the Cloudflare API client, rather than loading individual tool definitions for each endpoint. The generated code runs inside an isolated <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a> sandbox.</p>
<p>This approach uses approximately 1,000 tokens regardless of how many API endpoints exist. An equivalent MCP server that exposed every endpoint as a native tool would consume over 1 million tokens — more than the entire context window of most foundation models.</p>
<table>
<thead>
<tr>
<th>Approach</th>
<th>Tools</th>
<th>Token cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>Native MCP (full schemas)</td>
<td>2,594</td>
<td>~1,170,000</td>
</tr>
<tr>
<td>Native MCP (required params only)</td>
<td>2,594</td>
<td>~244,000</td>
</tr>
<tr>
<td>Code Mode</td>
<td>2</td>
<td>~1,000</td>
</tr>
</tbody>
</table>
<h3 id="connect-to-the-cloudflare-api-mcp-server">Connect to the Cloudflare API MCP server</h3>
<p>Add the following configuration to your MCP client:</p>
<pre><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;cloudflare-api&quot;: {&#10;			&quot;url&quot;: &quot;https://mcp.cloudflare.com/mcp&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>When you connect, you will be redirected to Cloudflare to authorize via OAuth and select the permissions to grant to your agent.</p>
<p>For CI/CD or automation, you can create a <a href="https://dash.cloudflare.com/profile/api-tokens">Cloudflare API token</a> with the permissions you need and pass it as a bearer token in the <code>Authorization</code> header. Both user tokens and account tokens are supported.</p>
<p>For more information, refer to the <a href="https://github.com/cloudflare/mcp">Cloudflare MCP repository</a>.</p>
<h3 id="install-via-agent-and-ide-plugins">Install via agent and IDE plugins</h3>
<p>You can install the <a href="https://github.com/cloudflare/skills">Cloudflare Skills plugin</a>, which bundles the Cloudflare MCP servers alongside contextual skills and slash commands for building on Cloudflare. The plugin works with any agent that supports the Agent Skills standard, including Claude Code, OpenCode, OpenAI Codex, and Pi.</p>
<h4 id="claude-code">Claude Code</h4>
<p>Install using the <a href="https://code.claude.com/docs/en/discover-plugins#add-from-github">plugin marketplace</a>:</p>
<pre><code class="language-txt">/plugin marketplace add cloudflare/skills&#10;</code></pre>
<h4 id="cursor">Cursor</h4>
<p>Install from the <strong>Cursor Marketplace</strong>, or add manually via <strong>Settings</strong> &gt; <strong>Rules</strong> &gt; <strong>Add Rule</strong> &gt; <strong>Remote Rule (Github)</strong> with <code>cloudflare/skills</code>.</p>
<h4 id="npx-skills">npx skills</h4>
<p>Install using the <a href="https://skills.sh"><code>npx skills</code></a> CLI:</p>
<pre><code class="language-sh">npx skills add https://github.com/cloudflare/skills&#10;</code></pre>
<h4 id="clone-or-copy">Clone or copy</h4>
<p>Clone the <a href="https://github.com/cloudflare/skills">cloudflare/skills</a> repository and copy the skill folders into the appropriate directory for your agent:</p>
<table>
<thead>
<tr>
<th>Agent</th>
<th>Skill directory</th>
<th>Docs</th>
</tr>
</thead>
<tbody>
<tr>
<td>Claude Code</td>
<td><code>~/.claude/skills/</code></td>
<td><a href="https://code.claude.com/docs/en/skills">Claude Code skills</a></td>
</tr>
<tr>
<td>Cursor</td>
<td><code>~/.cursor/skills/</code></td>
<td><a href="https://cursor.com/docs/context/skills">Cursor skills</a></td>
</tr>
<tr>
<td>OpenCode</td>
<td><code>~/.config/opencode/skills/</code></td>
<td><a href="https://opencode.ai/docs/skills/">OpenCode skills</a></td>
</tr>
<tr>
<td>OpenAI Codex</td>
<td><code>~/.codex/skills/</code></td>
<td><a href="https://developers.openai.com/codex/skills/">OpenAI Codex skills</a></td>
</tr>
<tr>
<td>Pi</td>
<td><code>~/.pi/agent/skills/</code></td>
<td><a href="https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent#skills">Pi coding agent skills</a></td>
</tr>
</tbody>
</table>
<h2 id="product-specific-mcp-servers">Product-specific MCP servers</h2>
<p>In addition to the Cloudflare API MCP server, Cloudflare provides product-specific MCP servers for targeted use cases:</p>
<table>
<thead>
<tr>
<th>Server Name</th>
<th>Description</th>
<th>Server URL</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/docs-ai-search">Documentation server</a></td>
<td>Get up to date reference information on Cloudflare</td>
<td><code>https://docs.mcp.cloudflare.com/mcp</code></td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/workers-bindings">Workers Bindings server</a></td>
<td>Build Workers applications with storage, AI, and compute primitives</td>
<td><code>https://bindings.mcp.cloudflare.com/mcp</code></td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/workers-builds">Workers Builds server</a></td>
<td>Get insights and manage your Cloudflare Workers Builds</td>
<td><code>https://builds.mcp.cloudflare.com/mcp</code></td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/workers-observability">Observability server</a></td>
<td>Debug and get insight into your application's logs and analytics</td>
<td><code>https://observability.mcp.cloudflare.com/mcp</code></td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/radar">Radar server</a></td>
<td>Get global Internet traffic insights, trends, URL scans, and other utilities</td>
<td><code>https://radar.mcp.cloudflare.com/mcp</code></td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/sandbox-container">Container server</a></td>
<td>Spin up a sandbox development environment</td>
<td><code>https://containers.mcp.cloudflare.com/mcp</code></td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/browser-rendering">Browser Run server</a></td>
<td>Fetch web pages, convert them to markdown and take screenshots</td>
<td><code>https://browser.mcp.cloudflare.com/mcp</code></td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/logpush">Logpush server</a></td>
<td>Get quick summaries for Logpush job health</td>
<td><code>https://logs.mcp.cloudflare.com/mcp</code></td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/ai-gateway">AI Gateway server</a></td>
<td>Search your logs, get details about the prompts and responses</td>
<td><code>https://ai-gateway.mcp.cloudflare.com/mcp</code></td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/autorag">AI Search server</a></td>
<td>List and search documents on your AI Searches</td>
<td><code>https://autorag.mcp.cloudflare.com/mcp</code></td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/auditlogs">Audit Logs server</a></td>
<td>Query audit logs and generate reports for review</td>
<td><code>https://auditlogs.mcp.cloudflare.com/mcp</code></td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/dns-analytics">DNS Analytics server</a></td>
<td>Optimize DNS performance and debug issues based on current set up</td>
<td><code>https://dns-analytics.mcp.cloudflare.com/mcp</code></td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/dex-analysis">Digital Experience Monitoring server</a></td>
<td>Get quick insight on critical applications for your organization</td>
<td><code>https://dex.mcp.cloudflare.com/mcp</code></td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/cloudflare-one-casb">Cloudflare One CASB server</a></td>
<td>Quickly identify any security misconfigurations for SaaS applications to safeguard users &amp; data</td>
<td><code>https://casb.mcp.cloudflare.com/mcp</code></td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/graphql/">GraphQL server</a></td>
<td>Get analytics data using Cloudflare's GraphQL API</td>
<td><code>https://graphql.mcp.cloudflare.com/mcp</code></td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/agents/tree/main/site/agents">Agents SDK Documentation server</a></td>
<td>Token-efficient search of the Cloudflare Agents SDK documentation</td>
<td><code>https://agents.cloudflare.com/mcp</code></td>
</tr>
</tbody>
</table>
<p>Check the <a href="https://github.com/cloudflare/mcp-server-cloudflare">GitHub page</a> to learn how to use Cloudflare's remote MCP servers with different MCP clients.</p>
