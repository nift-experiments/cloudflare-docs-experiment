<p>AI agents — tools like Cursor, GitHub Copilot, and Claude Code — can answer questions about Cloudflare products, generate configuration, and call Cloudflare APIs on your behalf. Cloudflare documentation provides content in agent-friendly formats, agent skills, and MCP servers so your AI agent can look up documentation and interact with Cloudflare services directly.</p>
<p>This page explains the available approaches and how to set them up.</p>
<h2 id="quick-start">Quick start</h2>
<p>These resources cover different aspects of using AI agents with Cloudflare documentation. Start with the one most relevant to you:</p>
<p><a class="nb-card nb-link-card" href="#concepts"><h3 id="card-understand-key-concepts-concepts">Understand key concepts</h3><p>Learn about agent skills and MCP (Model Context Protocol).</p></a></p>
<p><a class="nb-card nb-link-card" href="/agent-setup/"><h3 id="card-set-up-your-agent-agent-setup">Set up your agent</h3><p>Install skills and MCP servers for your specific AI tool.</p></a></p>
<p><a class="nb-card nb-link-card" href="#markdown-documentation-for-llms"><h3 id="card-extract-documentation-in-agent-friendly-format-markdown-documentation-for-llms">Extract documentation in agent-friendly format</h3><p>Minimize token usage while improving the accuracy of your agent's responses.</p></a></p>
<h2 id="concepts">Concepts</h2>
<h3 id="agent-skills">Agent skills</h3>
<p><a href="https://agentskills.io/home">Agent skills</a> are structured, task-specific instructions that AI tools load on demand — for example, a skill might teach your agent how to deploy a Cloudflare Worker or configure a WAF (Web Application Firewall) rule. Skills give your agent Cloudflare-specific instructions it would not otherwise have. Cloudflare publishes skills covering Workers, storage, AI, networking, security, and more in the <a href="https://github.com/cloudflare/skills">Cloudflare Skills repository</a>.</p>
<p>Each agent has its own installation method for skills. Refer to <a href="#set-up-your-agent">Agent setup</a> for installation instructions.</p>
<h3 id="model-context-protocol-mcp">Model Context Protocol (MCP)</h3>
<p>The <a href="https://modelcontextprotocol.io/">Model Context Protocol</a> (MCP) is an open standard that defines how AI tools connect to external tools, data, and services. An MCP server is an application that exposes specific capabilities. When you connect one to your agent, the agent can use those capabilities as part of its workflow (for example, searching documentation, creating DNS records, or deploying Workers).</p>
<p>Cloudflare runs managed remote MCP servers that give your agent the ability to search documentation, call the Cloudflare API, and query logs and analytics while it works.</p>
<p>There are two approaches:</p>
<ul>
<li><strong><a href="/agents/model-context-protocol/cloudflare/servers-for-cloudflare/">Cloudflare API MCP server</a></strong>: A Code Mode server that covers the entire Cloudflare API (over 2,500 endpoints). Use this when your agent needs broad access across multiple Cloudflare products.</li>
<li><strong>Domain-specific servers</strong>: Focused servers for documentation, observability, DNS analytics, and more. Use these when your agent only needs access to a specific area. The full catalog is in the <a href="https://github.com/cloudflare/mcp-server-cloudflare">cloudflare/mcp-server-cloudflare</a> repository.</li>
</ul>
<p>Each agent's <a href="#set-up-your-agent">Agent setup</a> guide includes MCP server installation as part of its Quick start. For the full list of available MCP servers, refer to <a href="/agents/model-context-protocol/cloudflare/servers-for-cloudflare/">MCP servers for Cloudflare</a>.</p>
<h3 id="model-flexibility">Model flexibility</h3>
<p>AI agents use large language models (LLMs) to understand your requests and generate responses. The model affects response quality, speed, and cost. How many models you can choose from depends on the agent:</p>
<ul>
<li><strong>Locked</strong>: Only the vendor's own models are supported.</li>
<li><strong>BYOK</strong> (Bring Your Own Key): You supply your own API key for the model provider of your choice.</li>
<li><strong>Multi-provider</strong>: Several model providers are supported out of the box.</li>
</ul>
<h3 id="context-approaches">Context approaches</h3>
<p>How the agent retains information about your project between conversations affects how much your agent remembers between sessions:</p>
<ul>
<li><strong>Project memory</strong>: The agent remembers context across sessions using stored files or memory.</li>
<li><strong>Indexed codebase</strong>: The agent builds a searchable index of your repository for fast lookups.</li>
</ul>
<h2 id="set-up-your-agent">Set up your agent</h2>
<p>Each supported agent has a dedicated setup guide covering installation, skills, MCP server configuration, example prompts, tips, and troubleshooting.</p>
<p><a class="nb-link-button" href="/agent-setup/">Get started</a></p>
<h2 id="markdown-documentation-for-llms">Markdown documentation for LLMs</h2>
<p>AI tools work better with Markdown than HTML because Markdown's explicit structure has less overhead than HTML tags, which reduces wasted tokens (the units of text that AI models process) and produces better results.</p>
<p>Every documentation page is available as Markdown using any of the following methods, powered by <a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a>.</p>
<h3 id="copy-from-the-current-page">Copy from the current page</h3>
<p>On any documentation page, select <strong>Copy as Markdown</strong> to copy the current page as Markdown.</p>
<h3 id="append-index-md-to-the-url">Append <code>/index.md</code> to the URL</h3>
<p>Add <code>/index.md</code> to the end of any page URL. For example:</p>
<pre><code class="language-txt">https://developers.cloudflare.com/workers/get-started/index.md&#10;</code></pre>
<h3 id="send-an-accept-text-markdown-header">Send an <code>Accept: text/markdown</code> header</h3>
<p>Request any page with the <code>Accept: text/markdown</code> header, which tells the server you prefer Markdown instead of HTML:</p>
<pre><code class="language-sh">curl &quot;https://developers.cloudflare.com/workers/get-started/&quot; \&#10;  &#45;-header &quot;Accept: text/markdown&quot;&#10;</code></pre>
<p>The response includes <code>x-markdown-tokens</code> and <code>x-original-tokens</code> headers with estimated token counts for the Markdown document and original HTML document, useful for context window planning (a context window is the maximum number of tokens an AI model can consider at once).</p>
<h3 id="site-wide-endpoints">Site-wide endpoints</h3>
<p>These endpoints follow the <a href="https://llmstxt.org/">llms.txt standard</a> and provide documentation content in Markdown format:</p>
<table>
<thead>
<tr>
<th>Endpoint</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/llms.txt"><code>/llms.txt</code></a></td>
<td>Page index grouped by product category, with links to each product's own <code>llms.txt</code></td>
</tr>
<tr>
<td><a href="/llms-full.txt"><code>/llms-full.txt</code></a></td>
<td>Full content of all documentation in a single file, for offline indexing, bulk vectorization (converting content into numerical representations for similarity search), or large-context models</td>
</tr>
</tbody>
</table>
<h3 id="per-product-endpoints">Per-product endpoints</h3>
<p>Each product has its own scoped <code>llms.txt</code> and <code>llms-full.txt</code>. Use these when you only need documentation for a specific product.</p>
<table>
<thead>
<tr>
<th>Endpoint</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/workers/llms.txt"><code>/workers/llms.txt</code></a></td>
<td>Page index for Workers documentation</td>
</tr>
<tr>
<td><a href="/workers/llms-full.txt"><code>/workers/llms-full.txt</code></a></td>
<td>Full content of all Workers documentation pages</td>
</tr>
</tbody>
</table>
<p>Replace <code>/workers/</code> with any product path. For the full list of available products, refer to <a href="/llms.txt"><code>/llms.txt</code></a>.</p>
<h2 id="openapi-specification">OpenAPI specification</h2>
<p>An <a href="https://www.openapis.org/">OpenAPI specification</a> is a machine-readable description of an API — it lists every available endpoint, the parameters each one accepts, and the responses it returns. When you add this to your AI tool's context, the tool can generate API calls to Cloudflare services without you having to look up the documentation manually.</p>
<p>The full Cloudflare API OpenAPI specification is available for AI coding tools, API clients, and code generators:</p>
<table>
<thead>
<tr>
<th>Endpoint</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/cloudflare/api-schemas"><code>cloudflare/api-schemas</code></a></td>
<td>Full Cloudflare API OpenAPI specification (JSON)</td>
</tr>
</tbody>
</table>
<p>For the full API reference, refer to the <a href="/api/">Cloudflare API documentation</a>.</p>
