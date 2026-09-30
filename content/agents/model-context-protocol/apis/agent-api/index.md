---
cp9:
  canonical: https://developers.cloudflare.com/agents/model-context-protocol/apis/agent-api/
  description: Reference the deprecated, feature-frozen McpAgent class while migrating existing stateful MCP servers to stateless handlers.
  full_title: McpAgent · Cloudflare Agents docs
  head_html: <title>McpAgent · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference the deprecated, feature-frozen McpAgent class while migrating existing stateful MCP servers to stateless handlers."><link rel="canonical" href="https://developers.cloudflare.com/agents/model-context-protocol/apis/agent-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/model-context-protocol/apis/agent-api/index.md"><meta property="og:title" content="McpAgent · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference the deprecated, feature-frozen McpAgent class while migrating existing stateful MCP servers to stateless handlers."><meta property="og:url" content="https://developers.cloudflare.com/agents/model-context-protocol/apis/agent-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><meta name="pcx_tags" content="MCP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/model-context-protocol/apis/agent-api/#page","headline":"McpAgent \u00b7 Cloudflare Agents docs","description":"Reference the deprecated, feature-frozen McpAgent class while migrating existing stateful MCP servers to stateless handlers.","url":"https://developers.cloudflare.com/agents/model-context-protocol/apis/agent-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["MCP"]}</script>
  markdown: true
  noindex: false
  route: /agents/model-context-protocol/apis/agent-api/
  schema: 1
---
<p><code>McpAgent</code> creates a stateful legacy MCP server backed by a Durable Object.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecated">Deprecated</h3>
@markup("md", "content/.markup/bodies/2281.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2282.md")
</div>
<p>This means that each instance of your MCP server has its own durable state, backed by a <a href="/durable-objects/">Durable Object</a>, with its own <a href="/agents/runtime/lifecycle/state/">SQL database</a>.</p>
<p>A stateless server can define <a href="/agents/model-context-protocol/protocol/tools/">tools</a> with <code>@modelcontextprotocol/server</code> and serve them through <code>createMcpHandler</code>.</p>
<p>But if you want your MCP server to:</p>
<ul>
<li>remember previous tool calls, and responses it provided</li>
<li>provide a game to the MCP client, remembering the state of the game board, previous moves, and the score</li>
<li>cache the state of a previous external API call, so that subsequent tool calls can reuse it</li>
<li>do anything that an Agent can do, but allow MCP clients to communicate with it</li>
</ul>
<p>You can use the APIs below in order to do so.</p>
<h2 id="api-overview">API overview</h2>
<table>
<thead>
<tr>
<th>Property/Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>state</code></td>
<td>Current state object (persisted)</td>
</tr>
<tr>
<td><code>initialState</code></td>
<td>Default state when instance starts</td>
</tr>
<tr>
<td><code>setState(state)</code></td>
<td>Update and persist state</td>
</tr>
<tr>
<td><code>onStateChanged(state)</code></td>
<td>Called when state changes</td>
</tr>
<tr>
<td><code>sql</code></td>
<td>Execute SQL queries on embedded database</td>
</tr>
<tr>
<td><code>server</code></td>
<td>The <code>McpServer</code> instance for registering tools</td>
</tr>
<tr>
<td><code>props</code></td>
<td>User identity and tokens from OAuth authentication</td>
</tr>
<tr>
<td><code>elicitInput(options, context)</code></td>
<td>Request structured input from user</td>
</tr>
<tr>
<td><code>McpAgent.serve(path, options)</code></td>
<td>Static method to create a Worker handler</td>
</tr>
</tbody>
</table>
<h2 id="deploying-with-mcpagent-serve">Deploying with McpAgent.serve()</h2>
<p>The <code>McpAgent.serve()</code> static method creates a Worker handler that routes requests to your MCP server:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2283.md")
</div>
<p>This is the simplest way to deploy an MCP server — about 15 lines of code. The <code>serve()</code> method handles Streamable HTTP transport automatically.</p>
<h3 id="with-oauth-authentication">With OAuth authentication</h3>
<p>When using the <a href="https://github.com/cloudflare/workers-oauth-provider">OAuth Provider Library</a>, pass your MCP server to <code>apiHandlers</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2284.md")
</div>
<h2 id="data-jurisdiction">Data jurisdiction</h2>
<p>For GDPR and data residency compliance, specify a jurisdiction to ensure your MCP server instances run in specific regions:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2285.md")
</div>
<p>With OAuth:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2286.md")
</div>
<p>When you specify <code>jurisdiction: &quot;eu&quot;</code>:</p>
<ul>
<li>All MCP session data stays within the EU</li>
<li>User data processed by your tools remains in the EU</li>
<li>State stored in the Durable Object stays in the EU</li>
</ul>
<p>Available jurisdictions include <code>&quot;eu&quot;</code> (European Union) and <code>&quot;fedramp&quot;</code> (FedRAMP compliant locations). Refer to <a href="/durable-objects/reference/data-location/">Durable Objects data location</a> for more options.</p>
<h2 id="hibernation-support">Hibernation support</h2>
<p><code>McpAgent</code> instances automatically support <a href="/durable-objects/best-practices/websockets/#durable-objects-hibernation-websocket-api">WebSockets Hibernation</a>, allowing stateful MCP servers to sleep during inactive periods while preserving their state. This means your agents only consume compute resources when actively processing requests, optimizing costs while maintaining the full context and conversation history.</p>
<p>Hibernation is enabled by default and requires no additional configuration.</p>
<h2 id="stream-resumability">Stream resumability</h2>
<p><code>McpAgent</code>'s Streamable HTTP transport survives the roughly 5-minute Cloudflare edge idle-stream watchdog so in-flight tool calls are not lost on a flaky connection:</p>
<ul>
<li><strong>GET (standalone listen stream)</strong> — when an <code>EventStore</code> is configured, idle drops are recovered by clients reconnecting with a <code>Last-Event-ID</code> header (no keepalive needed). Without an <code>EventStore</code>, a comment-frame keepalive (<code>: keepalive</code>, every 25 seconds) keeps long-lived listeners alive.</li>
<li><strong>POST (tool response stream)</strong> — always keepalive, so in-flight tool calls survive the idle watchdog. POST streams can additionally be resumed via <code>Last-Event-ID</code> when an <code>EventStore</code> is configured; a reconnecting client replays any events it missed up to and including the final response. Each POST stream's events are cleared when its close frame is written.</li>
</ul>
<p><code>DurableObjectEventStore</code> is exported from <code>agents/mcp</code> for stateful <code>WorkerTransport</code> callers that embed the transport inside an Agent or Durable Object:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2287.md")
</div>
<p>Refer to <a href="/agents/model-context-protocol/protocol/transport/">MCP Transport</a> for transport configuration.</p>
<h2 id="authentication-and-authorization">Authentication and authorization</h2>
<p>The McpAgent class provides seamless integration with the <a href="https://github.com/cloudflare/workers-oauth-provider">OAuth Provider Library</a> for <a href="/agents/model-context-protocol/protocol/authorization/">authentication and authorization</a>.</p>
<p>When a user authenticates to your MCP server, their identity information and tokens are made available through the <code>props</code> parameter, allowing you to:</p>
<ul>
<li>access user-specific data</li>
<li>check user permissions before performing operations</li>
<li>customize responses based on user attributes</li>
<li>use authentication tokens to make requests to external services on behalf of the user</li>
</ul>
<h2 id="state-synchronization-apis">State synchronization APIs</h2>
<p>The <code>McpAgent</code> class provides full access to the <a href="/agents/runtime/lifecycle/state/">Agent state APIs</a>:</p>
<ul>
<li><a href="/agents/runtime/lifecycle/state/"><code>state</code></a> — Current persisted state</li>
<li><a href="/agents/runtime/lifecycle/state/#set-the-initial-state-for-an-agent"><code>initialState</code></a> — Default state when instance starts</li>
<li><a href="/agents/runtime/lifecycle/state/"><code>setState</code></a> — Update and persist state</li>
<li><a href="/agents/runtime/lifecycle/state/#synchronizing-state"><code>onStateChanged</code></a> — React to state changes</li>
<li><a href="/agents/runtime/agents-api/#sql-api"><code>sql</code></a> — Execute SQL queries on embedded database</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="state-resets-after-the-session-ends">State resets after the session ends</h3>
@markup("md", "content/.markup/bodies/2280.md")
</aside>
<p>For example, the following code implements an MCP server that remembers a counter value, and updates the counter when the <code>add</code> tool is called:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2288.md")
</div>
<h2 id="elicitation-on-legacy-servers">Elicitation on legacy servers</h2>
<p><a href="https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation">MCP elicitation</a> lets a server request user input while handling another request, such as a tool call. The legacy path defines two modes:</p>
<ul>
<li><strong>Form mode</strong> collects structured, non-sensitive data through the client.</li>
<li><strong>URL mode</strong> sends the user to an out-of-band interaction, such as third-party authorization or payment.</li>
</ul>
<p>The client must advertise support for a mode before the server sends it.</p>
<h3 id="form-mode">Form mode</h3>
<p>Call <code>this.server.server.elicitInput()</code> in a tool handler. Pass <code>extra.requestId</code> as <code>relatedRequestId</code> so the response returns on the stream for the originating tool call:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2289.md")
</div>
<p>For backwards compatibility, form requests may omit <code>mode: &quot;form&quot;</code>. The schema supports flat objects with primitive fields. Do not use form mode to request passwords, API keys, access tokens, payment credentials, or other secrets.</p>
<h3 id="url-mode">URL mode</h3>
<p>Use URL mode for interactions that must happen outside the MCP client. The request includes a message, the URL, and a unique <code>elicitationId</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2290.md")
</div>
<p>For URL mode, <code>accept</code> means the user consented to open the URL. It does not mean the external interaction finished. The server may later send <code>notifications/elicitation/complete</code> with the same <code>elicitationId</code>.</p>
<p>Do not put secrets, personal information, or a pre-authenticated protected-resource URL in <code>url</code>. Production servers should use HTTPS. Bind each request to the authenticated user, and verify that the same user completes the external flow.</p>
<h3 id="handle-responses">Handle responses</h3>
<p>Both modes return one of three actions:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>accept</code></td>
<td>The user submitted the form or consented to open the URL.</td>
</tr>
<tr>
<td><code>decline</code></td>
<td>The user explicitly rejected the request.</td>
</tr>
<tr>
<td><code>cancel</code></td>
<td>The user dismissed the request without making an explicit choice.</td>
</tr>
</tbody>
</table>
<p>Accepted form responses include <code>content</code> that matches <code>requestedSchema</code>. URL responses omit <code>content</code>. Decline and cancel responses typically omit it.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2291.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="mcp-client-support">MCP client support</h3>
@markup("md", "content/.markup/bodies/2279.md")
</aside>
<p>For more human-in-the-loop patterns, refer to <a href="/agents/concepts/agentic-patterns/human-in-the-loop/">Human-in-the-loop patterns</a>.</p>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-build-a-remote-mcp-server-agents-model-context-protocol-guides-remote-mcp-server"><a href="/agents/model-context-protocol/guides/remote-mcp-server/">Build a Remote MCP server</a></h3><p>Get started with MCP servers on Cloudflare.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-mcp-tools-agents-model-context-protocol-protocol-tools"><a href="/agents/model-context-protocol/protocol/tools/">MCP Tools</a></h3><p>Design and add tools to your MCP server.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-authorization-agents-model-context-protocol-protocol-authorization"><a href="/agents/model-context-protocol/protocol/authorization/">Authorization</a></h3><p>Set up OAuth authentication.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-securing-mcp-servers-agents-model-context-protocol-guides-securing-mcp-server"><a href="/agents/model-context-protocol/guides/securing-mcp-server/">Securing MCP servers</a></h3><p>Security best practices for production.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-createmcphandler-agents-model-context-protocol-apis-handler-api"><a href="/agents/model-context-protocol/apis/handler-api/">createMcpHandler</a></h3><p>Build stateless MCP servers.</p></div>
