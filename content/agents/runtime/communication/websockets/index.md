---
cp9:
  canonical: https://developers.cloudflare.com/agents/runtime/communication/websockets/
  description: Handle real-time WebSocket connections, messages, broadcasts, and lifecycle hooks in the Agents SDK.
  full_title: WebSockets · Cloudflare Agents docs
  head_html: <title>WebSockets · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Handle real-time WebSocket connections, messages, broadcasts, and lifecycle hooks in the Agents SDK."><link rel="canonical" href="https://developers.cloudflare.com/agents/runtime/communication/websockets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/runtime/communication/websockets/index.md"><meta property="og:title" content="WebSockets · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Handle real-time WebSocket connections, messages, broadcasts, and lifecycle hooks in the Agents SDK."><meta property="og:url" content="https://developers.cloudflare.com/agents/runtime/communication/websockets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/runtime/communication/websockets/#page","headline":"WebSockets \u00b7 Cloudflare Agents docs","description":"Handle real-time WebSocket connections, messages, broadcasts, and lifecycle hooks in the Agents SDK.","url":"https://developers.cloudflare.com/agents/runtime/communication/websockets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/runtime/communication/websockets/
  schema: 1
---
<p>Agents support WebSocket connections for real-time, bi-directional communication. This page covers server-side WebSocket handling. For client-side connection, refer to the <a href="/agents/communication-channels/chat/client-sdk/">Client SDK</a>.</p>
<h2 id="lifecycle-hooks">Lifecycle hooks</h2>
<p>Agents have several lifecycle hooks that fire at different points:</p>
<table>
<thead>
<tr>
<th>Hook</th>
<th>When called</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>onStart(props?)</code></td>
<td>Once when the agent first starts (before any connections)</td>
</tr>
<tr>
<td><code>onRequest(request)</code></td>
<td>When an HTTP request is received (non-WebSocket)</td>
</tr>
<tr>
<td><code>onConnect(connection, ctx)</code></td>
<td>When a new WebSocket connection is established</td>
</tr>
<tr>
<td><code>onMessage(connection, message)</code></td>
<td>When a WebSocket message is received</td>
</tr>
<tr>
<td><code>onClose(connection, code, reason, wasClean)</code></td>
<td>When a WebSocket connection closes</td>
</tr>
<tr>
<td><code>onError(connection, error)</code></td>
<td>When a WebSocket error occurs on a connection</td>
</tr>
<tr>
<td><code>onError(error)</code></td>
<td>When a server-level error occurs (not tied to a specific connection)</td>
</tr>
<tr>
<td><code>shouldSendProtocolMessages(connection, ctx)</code></td>
<td>Whether to send protocol messages (identity, state, MCP) to this connection. Default: <code>true</code></td>
</tr>
</tbody>
</table>
<h3 id="onstart"><code>onStart</code></h3>
<p><code>onStart()</code> is called once when the agent first starts, before any connections are established:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2567.md")
</div>
<h2 id="handling-connections">Handling connections</h2>
<p>Define <code>onConnect</code> and <code>onMessage</code> methods on your Agent to accept WebSocket connections:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2568.md")
</div>
<h2 id="connection-object">Connection object</h2>
<p>Each connected client has a unique <code>Connection</code> object:</p>
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
<td><code>id</code></td>
<td><code>string</code></td>
<td>Unique identifier for this connection</td>
</tr>
<tr>
<td><code>uri</code></td>
<td><code>string | null</code></td>
<td>URL of the original WebSocket upgrade request. Persists across hibernation</td>
</tr>
<tr>
<td><code>state</code></td>
<td><code>State</code></td>
<td>Per-connection state object</td>
</tr>
<tr>
<td><code>setState(state)</code></td>
<td><code>void</code></td>
<td>Update connection state</td>
</tr>
<tr>
<td><code>send(message)</code></td>
<td><code>void</code></td>
<td>Send message to this client</td>
</tr>
<tr>
<td><code>close(code?, reason?)</code></td>
<td><code>void</code></td>
<td>Close the connection</td>
</tr>
<tr>
<td><code>tags</code></td>
<td><code>readonly string[]</code></td>
<td>Tags assigned via <code>getConnectionTags</code>. Always includes the connection ID as the first tag</td>
</tr>
<tr>
<td><code>server</code></td>
<td><code>string</code></td>
<td>The agent instance name (same as <code>this.name</code> on the Agent)</td>
</tr>
</tbody>
</table>
<h3 id="per-connection-state">Per-connection state</h3>
<p>Store data specific to each connection (user info, preferences, etc.):</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2569.md")
</div>
<h2 id="broadcasting-to-all-clients">Broadcasting to all clients</h2>
<p>Use <code>this.broadcast()</code> to send a message to all connected clients:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2570.md")
</div>
<h3 id="excluding-connections">Excluding connections</h3>
<p>Pass an array of connection IDs to exclude from the broadcast:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2571.md")
</div>
<h2 id="connection-tags">Connection tags</h2>
<p>Tag connections for easy filtering. Override <code>getConnectionTags()</code> to assign tags when a connection is established:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2572.md")
</div>
<h3 id="connection-management-methods">Connection management methods</h3>
<table>
<thead>
<tr>
<th>Method</th>
<th>Signature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>getConnections</code></td>
<td><code>(tag?: string) =&gt; Iterable&lt;Connection&gt;</code></td>
<td>Get all connections, optionally by tag</td>
</tr>
<tr>
<td><code>getConnection</code></td>
<td><code>(id: string) =&gt; Connection | undefined</code></td>
<td>Get connection by ID</td>
</tr>
<tr>
<td><code>getConnectionTags</code></td>
<td><code>(connection, ctx) =&gt; string[]</code></td>
<td>Override to tag connections</td>
</tr>
<tr>
<td><code>broadcast</code></td>
<td><code>(message, without?: string[]) =&gt; void</code></td>
<td>Send to all connections</td>
</tr>
<tr>
<td><code>isConnectionReadonly</code></td>
<td><code>(connection) =&gt; boolean</code></td>
<td>Check if a connection is <a href="/agents/runtime/communication/readonly-connections/">readonly</a></td>
</tr>
<tr>
<td><code>isConnectionProtocolEnabled</code></td>
<td><code>(connection) =&gt; boolean</code></td>
<td>Check if protocol messages are enabled for this connection</td>
</tr>
</tbody>
</table>
<h2 id="handling-binary-data">Handling binary data</h2>
<p>Messages can be strings or binary (<code>ArrayBuffer</code> / <code>ArrayBufferView</code>):</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2573.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2566.md")
</aside>
<h2 id="error-and-close-handling">Error and close handling</h2>
<p>Handle connection errors and disconnections. The <code>onError</code> method has two overloads — one for WebSocket connection errors and one for server-level errors:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2574.md")
</div>
<p>The default <code>onError</code> implementation logs the error and rethrows it. Override it to add custom error handling, reporting, or recovery logic.</p>
<h2 id="message-types">Message types</h2>
<table>
<thead>
<tr>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>string</code></td>
<td>Text message (typically JSON)</td>
</tr>
<tr>
<td><code>ArrayBuffer</code></td>
<td>Binary data</td>
</tr>
<tr>
<td><code>ArrayBufferView</code></td>
<td>Typed array view of binary data</td>
</tr>
</tbody>
</table>
<h2 id="hibernation">Hibernation</h2>
<p>Agents support hibernation — they can sleep when inactive and wake when needed. This saves resources while maintaining WebSocket connections.</p>
<h3 id="enabling-hibernation">Enabling hibernation</h3>
<p>Hibernation is enabled by default. To disable:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2575.md")
</div>
<h3 id="how-hibernation-works">How hibernation works</h3>
<ol>
<li>Agent is active, handling connections</li>
<li>After a period of inactivity with no messages, the agent hibernates (sleeps)</li>
<li>WebSocket connections remain open (handled by Cloudflare)</li>
<li>When a message arrives, the agent wakes up</li>
<li><code>onMessage</code> is called as normal</li>
</ol>
<h3 id="what-persists-across-hibernation">What persists across hibernation</h3>
<table>
<thead>
<tr>
<th>Persists</th>
<th>Does not persist</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>this.state</code> (agent state)</td>
<td>In-memory variables</td>
</tr>
<tr>
<td><code>connection.state</code></td>
<td>Timers/intervals</td>
</tr>
<tr>
<td>SQLite data (<code>this.sql</code>)</td>
<td>Promises in flight</td>
</tr>
<tr>
<td>Connection metadata</td>
<td>Local caches</td>
</tr>
</tbody>
</table>
<p>Store important data in <code>this.state</code> or SQLite, not in class properties:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2576.md")
</div>
<h2 id="common-patterns">Common patterns</h2>
<h3 id="presence-tracking">Presence tracking</h3>
<p>Track who is online using per-connection state. Connection state is automatically cleaned up when users disconnect:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2577.md")
</div>
<h3 id="chat-room-with-broadcast">Chat room with broadcast</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2578.md")
</div>
<h2 id="suppressing-protocol-messages">Suppressing protocol messages</h2>
<p>By default, agents send JSON text frames (identity, state sync, MCP server lists) to every connection. Override <code>shouldSendProtocolMessages</code> to suppress them for specific connections — for example, binary-only clients that cannot handle JSON text frames:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2579.md")
</div>
<p>When this returns <code>false</code>, the connection does not receive identity, state, or MCP server list frames — neither on connect nor via broadcasts. The connection can still send and receive regular messages, use RPC, and participate in all non-protocol communication.</p>
<p>Use <code>isConnectionProtocolEnabled(connection)</code> to check the status of any connection at runtime.</p>
<h2 id="agent-properties">Agent properties</h2>
<p>These properties are available on <code>this</code> inside any Agent method:</p>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>this.name</code></td>
<td><code>string</code></td>
<td>The instance name of this agent</td>
</tr>
<tr>
<td><code>this.state</code></td>
<td><code>State</code></td>
<td>The current agent state (lazy-loaded from SQLite)</td>
</tr>
<tr>
<td><code>this.env</code></td>
<td><code>Env</code></td>
<td>Worker environment bindings</td>
</tr>
<tr>
<td><code>this.ctx</code></td>
<td><code>DurableObjectState</code></td>
<td>Durable Object context (storage, alarms, etc.)</td>
</tr>
<tr>
<td><code>this.sql</code></td>
<td>template tag</td>
<td>SQL template tag for executing queries against the agent's SQLite storage</td>
</tr>
<tr>
<td><code>this.mcp</code></td>
<td><code>MCPClientManager</code></td>
<td>MCP client manager for connecting to external MCP servers</td>
</tr>
</tbody>
</table>
<h2 id="connecting-from-clients">Connecting from clients</h2>
<p>For browser connections, use the Agents client SDK:</p>
<ul>
<li><strong>Vanilla JS</strong>: <code>AgentClient</code> from <code>agents/client</code></li>
<li><strong>React</strong>: <code>useAgent</code> hook from <code>agents/react</code></li>
</ul>
<p>Refer to <a href="/agents/communication-channels/chat/client-sdk/">Client SDK</a> for full documentation.</p>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-state-synchronization-agents-runtime-lifecycle-state"><a href="/agents/runtime/lifecycle/state/">State synchronization</a></h3><p>Sync state between agents and clients.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-callable-methods-agents-runtime-lifecycle-callable-methods"><a href="/agents/runtime/lifecycle/callable-methods/">Callable methods</a></h3><p>RPC over WebSockets for method calls.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-cross-domain-authentication-agents-runtime-operations-cross-domain-authentication"><a href="/agents/runtime/operations/cross-domain-authentication/">Cross-domain authentication</a></h3><p>Secure WebSocket connections across domains.</p></div>
