---
cp9:
  canonical: https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/community-mcp-server/
  description: Learn how to use the Cloudflare Community MCP server to search topics, read posts, and filter content.
  full_title: Cloudflare Community MCP Server · Cloudflare Agents docs
  head_html: <title>Cloudflare Community MCP Server · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to use the Cloudflare Community MCP server to search topics, read posts, and filter content."><link rel="canonical" href="https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/community-mcp-server/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/community-mcp-server/index.md"><meta property="og:title" content="Cloudflare Community MCP Server · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to use the Cloudflare Community MCP server to search topics, read posts, and filter content."><meta property="og:url" content="https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/community-mcp-server/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/community-mcp-server/#page","headline":"Cloudflare Community MCP Server \u00b7 Cloudflare Agents docs","description":"Learn how to use the Cloudflare Community MCP server to search topics, read posts, and filter content.","url":"https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/community-mcp-server/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/model-context-protocol/cloudflare/servers-for-cloudflare/community-mcp-server/
  schema: 1
---
<p>The MCP server for the <a href="https://community.cloudflare.com">Cloudflare Community forum</a> lets AI agents search topics, read posts, look up users, and filter content.</p>
<p>The server is powered by <a href="https://www.npmjs.com/package/@discourse/mcp"><code>@discourse/mcp</code></a>, the official Discourse MCP server.</p>
<h2 id="install">Install</h2>
<pre tabindex="0"><code class="language-bash">npx @discourse/mcp@latest&#10;</code></pre>
<h2 id="configure">Configure</h2>
<h3 id="opencode">OpenCode</h3>
<p>Add to <code>~/.config/opencode/opencode.jsonc</code> inside the <code>&quot;mcp&quot;</code> block:</p>
<pre tabindex="0"><code class="language-json">&quot;discourse&quot;: {&#10;  &quot;type&quot;: &quot;local&quot;,&#10;  &quot;command&quot;: [&quot;npx&quot;, &quot;-y&quot;, &quot;@discourse/mcp@latest&quot;],&#10;  &quot;enabled&quot;: true&#10;}&#10;</code></pre>
<h3 id="claude-desktop">Claude Desktop</h3>
<p>Add to <code>claude_desktop_config.json</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;mcpServers&quot;: {&#10;    &quot;discourse&quot;: {&#10;      &quot;command&quot;: &quot;npx&quot;,&#10;      &quot;args&quot;: [&quot;-y&quot;, &quot;@discourse/mcp@latest&quot;]&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h3 id="cursor">Cursor</h3>
<p>Add to <code>.cursor/mcp.json</code> in your project root:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;mcpServers&quot;: {&#10;    &quot;discourse&quot;: {&#10;      &quot;command&quot;: &quot;npx&quot;,&#10;      &quot;args&quot;: [&quot;-y&quot;, &quot;@discourse/mcp@latest&quot;]&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h2 id="connect-to-the-cloudflare-community">Connect to the Cloudflare Community</h2>
<p>After configuring your client, use the <code>discourse_select_site</code> tool with:</p>
<pre tabindex="0"><code class="language-txt">https://community.cloudflare.com&#10;</code></pre>
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
