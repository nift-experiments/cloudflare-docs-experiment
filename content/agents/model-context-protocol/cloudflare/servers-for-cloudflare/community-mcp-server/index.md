<p>The MCP server for the <a href="https://community.cloudflare.com">Cloudflare Community forum</a> lets AI agents search topics, read posts, look up users, and filter content.</p>
<p>The server is powered by <a href="https://www.npmjs.com/package/@discourse/mcp"><code>@discourse/mcp</code></a>, the official Discourse MCP server.</p>
<h2 id="install">Install</h2>
<pre><code class="language-bash">npx @discourse/mcp@latest&#10;</code></pre>
<h2 id="configure">Configure</h2>
<h3 id="opencode">OpenCode</h3>
<p>Add to <code>~/.config/opencode/opencode.jsonc</code> inside the <code>&quot;mcp&quot;</code> block:</p>
<pre><code class="language-json">&quot;discourse&quot;: {&#10;  &quot;type&quot;: &quot;local&quot;,&#10;  &quot;command&quot;: [&quot;npx&quot;, &quot;-y&quot;, &quot;@discourse/mcp@latest&quot;],&#10;  &quot;enabled&quot;: true&#10;}&#10;</code></pre>
<h3 id="claude-desktop">Claude Desktop</h3>
<p>Add to <code>claude_desktop_config.json</code>:</p>
<pre><code class="language-json">{&#10;  &quot;mcpServers&quot;: {&#10;    &quot;discourse&quot;: {&#10;      &quot;command&quot;: &quot;npx&quot;,&#10;      &quot;args&quot;: [&quot;-y&quot;, &quot;@discourse/mcp@latest&quot;]&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h3 id="cursor">Cursor</h3>
<p>Add to <code>.cursor/mcp.json</code> in your project root:</p>
<pre><code class="language-json">{&#10;  &quot;mcpServers&quot;: {&#10;    &quot;discourse&quot;: {&#10;      &quot;command&quot;: &quot;npx&quot;,&#10;      &quot;args&quot;: [&quot;-y&quot;, &quot;@discourse/mcp@latest&quot;]&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h2 id="connect-to-the-cloudflare-community">Connect to the Cloudflare Community</h2>
<p>After configuring your client, use the <code>discourse_select_site</code> tool with:</p>
<pre><code class="language-txt">https://community.cloudflare.com&#10;</code></pre>
<p>No API key is needed for reading public data. An API key is only required for write operations (posting, moderation).</p>
<h2 id="available-tools">Available tools</h2>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>discourse_select_site</code></td>
<td>Connect to community.cloudflare.com</td>
</tr>
<tr>
<td><code>discourse_search</code></td>
<td>Full-text search across topics and posts</td>
</tr>
<tr>
<td><code>discourse_filter_topics</code></td>
<td>Filter by category, tags, status, dates</td>
</tr>
<tr>
<td><code>discourse_read_topic</code></td>
<td>Read a topic's posts and metadata</td>
</tr>
<tr>
<td><code>discourse_read_post</code></td>
<td>Read a specific post</td>
</tr>
<tr>
<td><code>discourse_get_user</code></td>
<td>Look up a user's profile</td>
</tr>
<tr>
<td><code>discourse_list_user_posts</code></td>
<td>List posts by a user</td>
</tr>
</tbody>
</table>
<h2 id="example-usage">Example usage</h2>
<p>Once connected, you can ask your AI assistant things like:</p>
<ul>
<li>&quot;Search the Cloudflare community for topics about Error 522&quot;</li>
<li>&quot;Find unanswered topics in the SSL category from the last 3 days&quot;</li>
<li>&quot;Read topic 42325 and summarize the issue&quot;</li>
<li>&quot;Show me recent replies from user sandro&quot;</li>
</ul>
<h2 id="machine-readable-discovery">Machine-readable discovery</h2>
<p>AI agents can automatically discover the MCP server through these endpoints on community.cloudflare.com:</p>
<ul>
<li><a href="https://community.cloudflare.com/.well-known/mcp.json"><code>/.well-known/mcp.json</code></a> — MCP Server Card</li>
<li><a href="https://community.cloudflare.com/llms.txt"><code>/llms.txt</code></a> — LLMs.txt with server info and install instructions</li>
<li><a href="https://community.cloudflare.com/.well-known/agent.json"><code>/.well-known/agent.json</code></a> — A2A Agent Card</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://community.cloudflare.com/mcp">Setup guide with detailed configuration instructions</a></li>
<li><a href="https://www.npmjs.com/package/@discourse/mcp">The official <code>npm: @discourse/mcp</code> package</a></li>
<li><a href="https://modelcontextprotocol.io">Model Context Protocol specification</a></li>
<li><a href="/agents/">Building AI agents on Cloudflare</a></li>
<li><a href="https://community.cloudflare.com">Cloudflare Community forum</a></li>
</ul>
