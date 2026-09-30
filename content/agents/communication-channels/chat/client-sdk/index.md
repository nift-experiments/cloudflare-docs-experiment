---
cp9:
  canonical: https://developers.cloudflare.com/agents/communication-channels/chat/client-sdk/
  description: Connect to Cloudflare Agents from browsers or server runtimes using useAgent, AgentClient, and agentFetch.
  full_title: Client SDK · Cloudflare Agents docs
  head_html: <title>Client SDK · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect to Cloudflare Agents from browsers or server runtimes using useAgent, AgentClient, and agentFetch."><link rel="canonical" href="https://developers.cloudflare.com/agents/communication-channels/chat/client-sdk/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/communication-channels/chat/client-sdk/index.md"><meta property="og:title" content="Client SDK · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect to Cloudflare Agents from browsers or server runtimes using useAgent, AgentClient, and agentFetch."><meta property="og:url" content="https://developers.cloudflare.com/agents/communication-channels/chat/client-sdk/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/communication-channels/chat/client-sdk/#page","headline":"Client SDK \u00b7 Cloudflare Agents docs","description":"Connect to Cloudflare Agents from browsers or server runtimes using useAgent, AgentClient, and agentFetch.","url":"https://developers.cloudflare.com/agents/communication-channels/chat/client-sdk/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/communication-channels/chat/client-sdk/
  schema: 1
---
<p>Connect to agents from any JavaScript runtime — browsers, Node.js, Deno, Bun, or edge functions — using WebSockets or HTTP. The SDK provides real-time state synchronization, RPC method calls, and streaming responses.</p>
<h2 id="overview">Overview</h2>
<p>The client SDK offers two ways to connect with a WebSocket connection, and one way to make HTTP requests.</p>
<table>
<thead>
<tr>
<th>Client</th>
<th>Use Case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>useAgent</code></td>
<td>React hook with automatic reconnection and state management</td>
</tr>
<tr>
<td><code>AgentClient</code></td>
<td>Vanilla JavaScript/TypeScript class for any environment</td>
</tr>
<tr>
<td><code>agentFetch</code></td>
<td>HTTP requests when WebSocket is not needed</td>
</tr>
</tbody>
</table>
<p>All clients provide:</p>
<ul>
<li><strong>Bidirectional state sync</strong> - Push and receive state updates in real-time</li>
<li><strong>RPC calls</strong> - Call agent methods with typed arguments and return values</li>
<li><strong>Streaming</strong> - Handle chunked responses for AI completions</li>
<li><strong>Auto-reconnection</strong> - Automatic reconnection with exponential backoff</li>
</ul>
<h2 id="quick-start">Quick start</h2>
<h3 id="react">React</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2004.md")
</div>
<h3 id="vanilla-javascript">Vanilla JavaScript</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2005.md")
</div>
<h2 id="connecting-to-agents">Connecting to agents</h2>
<h3 id="agent-naming">Agent naming</h3>
<p>The <code>agent</code> parameter is your agent class name. It is automatically converted from camelCase to kebab-case for the URL:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2006.md")
</div>
<h3 id="instance-names">Instance names</h3>
<p>The <code>name</code> parameter identifies a specific agent instance. If omitted, defaults to <code>&quot;default&quot;</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2007.md")
</div>
<h3 id="connection-options">Connection options</h3>
<p>Both <code>useAgent</code> and <code>AgentClient</code> accept connection options:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2008.md")
</div>
<h3 id="async-query-parameters">Async query parameters</h3>
<p>For authentication tokens or other async data, pass a function that returns a Promise:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2009.md")
</div>
<p>The query function is cached and only re-called when:</p>
<ul>
<li><code>queryDeps</code> change</li>
<li><code>cacheTtl</code> expires</li>
<li>The WebSocket connection closes (automatic cache invalidation)</li>
<li>The component remounts</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="automatic-cache-invalidation-on-disconnect">Automatic cache invalidation on disconnect</h3>
@markup("md", "content/.markup/bodies/2003.md")
</aside>
<h2 id="state-synchronization">State synchronization</h2>
<p>Agents can maintain state that syncs bidirectionally with all connected clients.</p>
<h3 id="reading-current-state">Reading current state</h3>
<p>Both <code>useAgent</code> and <code>AgentClient</code> expose a <code>state</code> property that reflects the current agent state. It starts as <code>undefined</code> until the first state message is received from the server.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2010.md")
</div>
<p>With <code>useAgent</code>, state updates trigger a React re-render, so <code>agent.state</code> always reflects the latest value in your JSX. With <code>AgentClient</code>, the <code>state</code> field is updated synchronously on each incoming server broadcast or <code>setState</code> call.</p>
<h3 id="receiving-state-updates">Receiving state updates</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2011.md")
</div>
<h3 id="pushing-state-updates">Pushing state updates</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2012.md")
</div>
<p>When you call <code>setState()</code>:</p>
<ol>
<li>The state is sent to the agent over WebSocket</li>
<li>The agent's <code>onStateChanged()</code> method is called</li>
<li>The agent broadcasts the new state to all connected clients</li>
<li>Your <code>onStateUpdate</code> callback fires with <code>source: &quot;client&quot;</code></li>
</ol>
<h3 id="state-flow">State flow</h3>
<pre tabindex="0"><code class="language-mermaid">sequenceDiagram&#10;    participant Client&#10;    participant Agent&#10;    Client-&gt;&gt;Agent: setState()&#10;    Agent--&gt;&gt;Client: onStateUpdate (broadcast)&#10;</code></pre>
<h2 id="calling-agent-methods-rpc">Calling agent methods (RPC)</h2>
<p>Call methods on your agent that are decorated with <code>@callable()</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2002.md")
</aside>
<h3 id="using-call">Using call()</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2013.md")
</div>
<h3 id="using-the-stub-proxy">Using the stub proxy</h3>
<p>The <code>stub</code> property provides a cleaner syntax for method calls:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2014.md")
</div>
<h3 id="typescript-integration">TypeScript integration</h3>
<p>For full type safety, pass your Agent class as a type parameter:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2015.md")
</div>
<h3 id="streaming-responses">Streaming responses</h3>
<p>Mark a callable method as streaming. The framework passes a <code>StreamingResponse</code> as its first argument:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2016.md")
</div>
<h2 id="http-requests-with-agentfetch">HTTP requests with agentFetch</h2>
<p>For one-off requests without maintaining a WebSocket connection:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2017.md")
</div>
<p><strong>When to use <code>agentFetch</code> vs WebSocket:</strong></p>
<table>
<thead>
<tr>
<th>Use <code>agentFetch</code></th>
<th>Use <code>useAgent</code>/<code>AgentClient</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>One-time requests</td>
<td>Real-time updates needed</td>
</tr>
<tr>
<td>Server-to-server calls</td>
<td>Bidirectional communication</td>
</tr>
<tr>
<td>Simple REST-style API</td>
<td>State synchronization</td>
</tr>
<tr>
<td>No persistent connection needed</td>
<td>Multiple RPC calls</td>
</tr>
</tbody>
</table>
<h2 id="mcp-server-integration">MCP server integration</h2>
<p>If your agent uses MCP (Model Context Protocol) servers, you can receive updates about their state:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2018.md")
</div>
<h2 id="error-handling">Error handling</h2>
<h3 id="connection-errors">Connection errors</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2019.md")
</div>
<h3 id="rpc-errors">RPC errors</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2020.md")
</div>
<h3 id="streaming-errors">Streaming errors</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2021.md")
</div>
<h2 id="best-practices">Best practices</h2>
<h3 id="1-use-typed-stubs"><ol>
<li>Use typed stubs</li>
</ol></h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2022.md")
</div>
<h3 id="2-reconnection-is-automatic"><ol start="2">
<li>Reconnection is automatic</li>
</ol></h3>
<p>The client auto-reconnects and the agent automatically sends the current state on each connection. Your <code>onStateUpdate</code> callback will fire with the latest state — no manual re-sync is needed. If you use an async <code>query</code> function for authentication, the cache is automatically invalidated on disconnect, ensuring fresh tokens are fetched on reconnect.</p>
<h3 id="3-optimize-query-caching"><ol start="3">
<li>Optimize query caching</li>
</ol></h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2023.md")
</div>
<h3 id="4-clean-up-connections"><ol start="4">
<li>Clean up connections</li>
</ol></h3>
<p>In vanilla JS, close connections when done:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2024.md")
</div>
<p>React's <code>useAgent</code> handles cleanup automatically on unmount.</p>
<h2 id="react-hook-reference">React hook reference</h2>
<h3 id="useagentoptions">UseAgentOptions</h3>
<pre tabindex="0"><code class="language-ts">type UseAgentOptions&lt;State&gt; = {&#10;	// Required&#10;	agent: string; // Agent class name&#10;&#10;	// Optional&#10;	name?: string; // Instance name (default: &quot;default&quot;)&#10;	host?: string; // Custom host&#10;	path?: string; // Custom path prefix&#10;&#10;	// Query parameters&#10;	query?: Record&lt;string, string&gt; | (() =&gt; Promise&lt;Record&lt;string, string&gt;&gt;);&#10;	queryDeps?: unknown[]; // Dependencies for async query&#10;	cacheTtl?: number; // Query cache TTL in ms (default: 5 min)&#10;&#10;	// Callbacks&#10;	onStateUpdate?: (state: State, source: &quot;server&quot; | &quot;client&quot;) =&gt; void;&#10;	onMcpUpdate?: (mcpServers: MCPServersState) =&gt; void;&#10;	onOpen?: () =&gt; void;&#10;	onClose?: () =&gt; void;&#10;	onError?: (error: Event) =&gt; void;&#10;	onMessage?: (message: MessageEvent) =&gt; void;&#10;};&#10;</code></pre>
<h3 id="return-value">Return value</h3>
<p>The <code>useAgent</code> hook returns an object with the following properties and methods:</p>
<table>
<thead>
<tr>
<th>Property/Method</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>agent</code></td>
<td><code>string</code></td>
<td>Kebab-case agent name</td>
</tr>
<tr>
<td><code>name</code></td>
<td><code>string</code></td>
<td>Instance name</td>
</tr>
<tr>
<td><code>setState(state)</code></td>
<td><code>void</code></td>
<td>Push state to agent</td>
</tr>
<tr>
<td><code>call(method, args?, options?)</code></td>
<td><code>Promise</code></td>
<td>Call agent method</td>
</tr>
<tr>
<td><code>stub</code></td>
<td><code>Proxy</code></td>
<td>Typed method calls</td>
</tr>
<tr>
<td><code>send(data)</code></td>
<td><code>void</code></td>
<td>Send raw WebSocket message</td>
</tr>
<tr>
<td><code>close()</code></td>
<td><code>void</code></td>
<td>Close connection</td>
</tr>
<tr>
<td><code>reconnect()</code></td>
<td><code>void</code></td>
<td>Force reconnection</td>
</tr>
</tbody>
</table>
<h2 id="vanilla-js-reference">Vanilla JS reference</h2>
<h3 id="agentclientoptions">AgentClientOptions</h3>
<pre tabindex="0"><code class="language-ts">type AgentClientOptions&lt;State&gt; = {&#10;	// Required&#10;	agent: string; // Agent class name&#10;	host: string; // Worker host&#10;&#10;	// Optional&#10;	name?: string; // Instance name (default: &quot;default&quot;)&#10;	path?: string; // Custom path prefix&#10;	query?: Record&lt;string, string&gt;;&#10;&#10;	// Callbacks&#10;	onStateUpdate?: (state: State, source: &quot;server&quot; | &quot;client&quot;) =&gt; void;&#10;};&#10;</code></pre>
<h3 id="agentclient-methods">AgentClient methods</h3>
<table>
<thead>
<tr>
<th>Property/Method</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>agent</code></td>
<td><code>string</code></td>
<td>Kebab-case agent name</td>
</tr>
<tr>
<td><code>name</code></td>
<td><code>string</code></td>
<td>Instance name</td>
</tr>
<tr>
<td><code>setState(state)</code></td>
<td><code>void</code></td>
<td>Push state to agent</td>
</tr>
<tr>
<td><code>call(method, args?, options?)</code></td>
<td><code>Promise</code></td>
<td>Call agent method</td>
</tr>
<tr>
<td><code>send(data)</code></td>
<td><code>void</code></td>
<td>Send raw WebSocket message</td>
</tr>
<tr>
<td><code>close()</code></td>
<td><code>void</code></td>
<td>Close connection</td>
</tr>
<tr>
<td><code>reconnect()</code></td>
<td><code>void</code></td>
<td>Force reconnection</td>
</tr>
</tbody>
</table>
<p>The client also supports WebSocket event listeners:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2025.md")
</div>
<h3 id="chat-from-a-non-react-client">Chat from a non-React client</h3>
<p>An <code>AgentClient</code> connection can drive an AI SDK chat UI in any framework. <code>agents/chat/transport</code> exports <code>WebSocketChatTransport</code>, which requires no React peer dependency:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2026.md")
</div>
<p>Refer to <a href="/agents/communication-channels/chat/chat-agents/#non-react-clients">Non-React clients</a> for the behaviors this transport does and does not cover.</p>
<h2 id="agent-tool-events">Agent-tool events</h2>
<p>If your chat UI renders retained child runs from <a href="/agents/runtime/execution/agent-tools/">Agents as tools</a>, use <code>useAgentToolEvents()</code> alongside <code>useAgent()</code> and <code>useAgentChat()</code>. The hook subscribes to the parent connection, replays retained child timelines, and groups runs by parent tool call ID.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2027.md")
</div>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-routing-agents-runtime-communication-routing"><a href="/agents/runtime/communication/routing/">Routing</a></h3><p>URL patterns and custom routing options.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-callable-methods-agents-runtime-lifecycle-callable-methods"><a href="/agents/runtime/lifecycle/callable-methods/">Callable methods</a></h3><p>RPC over WebSocket for client-server method calls.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-cross-domain-authentication-agents-runtime-operations-cross-domain-authentication"><a href="/agents/runtime/operations/cross-domain-authentication/">Cross-domain authentication</a></h3><p>Secure WebSocket connections across domains.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-build-a-chat-agent-agents-examples-chat-agent"><a href="/agents/examples/chat-agent/">Build a chat agent</a></h3><p>Complete client integration with AI chat.</p></div>
