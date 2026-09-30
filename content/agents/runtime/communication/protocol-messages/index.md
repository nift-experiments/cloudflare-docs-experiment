---
cp9:
  canonical: https://developers.cloudflare.com/agents/runtime/communication/protocol-messages/
  description: Control the identity, state, and MCP protocol messages sent to WebSocket clients on Agent connect.
  full_title: Protocol messages · Cloudflare Agents docs
  head_html: <title>Protocol messages · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Control the identity, state, and MCP protocol messages sent to WebSocket clients on Agent connect."><link rel="canonical" href="https://developers.cloudflare.com/agents/runtime/communication/protocol-messages/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/runtime/communication/protocol-messages/index.md"><meta property="og:title" content="Protocol messages · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Control the identity, state, and MCP protocol messages sent to WebSocket clients on Agent connect."><meta property="og:url" content="https://developers.cloudflare.com/agents/runtime/communication/protocol-messages/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/runtime/communication/protocol-messages/#page","headline":"Protocol messages \u00b7 Cloudflare Agents docs","description":"Control the identity, state, and MCP protocol messages sent to WebSocket clients on Agent connect.","url":"https://developers.cloudflare.com/agents/runtime/communication/protocol-messages/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/runtime/communication/protocol-messages/
  schema: 1
---
<p>When a WebSocket client connects to an Agent, the framework automatically sends several JSON text frames — identity, state, and MCP server lists. You can suppress these per-connection protocol messages for clients that cannot handle them.</p>
<h2 id="overview">Overview</h2>
<p>On every new connection, the Agent sends three protocol messages:</p>
<table>
<thead>
<tr>
<th>Message type</th>
<th>Content</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf_agent_identity</code></td>
<td>Agent name and class</td>
</tr>
<tr>
<td><code>cf_agent_state</code></td>
<td>Current agent state</td>
</tr>
<tr>
<td><code>cf_agent_mcp_servers</code></td>
<td>Connected MCP server list</td>
</tr>
</tbody>
</table>
<p>State and MCP messages are also broadcast to all connections whenever they change.</p>
<p>For most web clients this is fine — the <a href="/agents/communication-channels/chat/client-sdk/">Client SDK</a> and <code>useAgent</code> hook consume these messages automatically. However, some clients cannot handle JSON text frames:</p>
<ul>
<li><strong>Binary-only clients</strong> — MQTT devices, IoT sensors, custom binary protocols</li>
<li><strong>Lightweight clients</strong> — Embedded systems with minimal WebSocket stacks</li>
<li><strong>Non-browser clients</strong> — Hardware devices connecting via WebSocket</li>
</ul>
<p>For these connections, you can suppress protocol messages while keeping everything else (RPC, regular messages, broadcasts via <code>this.broadcast()</code>) working normally.</p>
<h2 id="suppressing-protocol-messages">Suppressing protocol messages</h2>
<p>Override <code>shouldSendProtocolMessages</code> to control which connections receive protocol messages. Return <code>false</code> to suppress them.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2629.md")
</div>
<p>This hook runs during <code>onConnect</code>, before any messages are sent. When it returns <code>false</code>:</p>
<ul>
<li>No <code>cf_agent_identity</code>, <code>cf_agent_state</code>, or <code>cf_agent_mcp_servers</code> messages are sent on connect</li>
<li>The connection is excluded from state and MCP broadcasts going forward</li>
<li>RPC calls, regular <code>onMessage</code> handling, and <code>this.broadcast()</code> still work normally</li>
</ul>
<h3 id="using-websocket-subprotocol">Using WebSocket subprotocol</h3>
<p>You can also check the WebSocket subprotocol header, which is the standard way to negotiate protocols over WebSocket:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2630.md")
</div>
<h2 id="checking-protocol-status">Checking protocol status</h2>
<p>Use <code>isConnectionProtocolEnabled</code> to check whether a connection has protocol messages enabled:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2631.md")
</div>
<h2 id="what-is-and-is-not-suppressed">What is and is not suppressed</h2>
<p>The following table shows what still works when protocol messages are suppressed for a connection:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Works?</th>
</tr>
</thead>
<tbody>
<tr>
<td>Receive <code>cf_agent_identity</code> on connect</td>
<td><strong>No</strong></td>
</tr>
<tr>
<td>Receive <code>cf_agent_state</code> on connect and broadcasts</td>
<td><strong>No</strong></td>
</tr>
<tr>
<td>Receive <code>cf_agent_mcp_servers</code> on connect and broadcasts</td>
<td><strong>No</strong></td>
</tr>
<tr>
<td>Send and receive regular WebSocket messages</td>
<td>Yes</td>
</tr>
<tr>
<td>Call <code>@callable()</code> RPC methods</td>
<td>Yes</td>
</tr>
<tr>
<td>Receive <code>this.broadcast()</code> messages</td>
<td>Yes</td>
</tr>
<tr>
<td>Send binary data</td>
<td>Yes</td>
</tr>
<tr>
<td>Mutate agent state via RPC</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="combining-with-readonly">Combining with readonly</h2>
<p>A connection can be both readonly and protocol-suppressed. This is useful for binary devices that should observe but not modify state:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2632.md")
</div>
<p>Both flags are stored in the connection's WebSocket attachment and hidden from <code>connection.state</code> — they do not interfere with each other or with user-defined connection state.</p>
<h2 id="api-reference">API reference</h2>
<h3 id="shouldsendprotocolmessages"><code>shouldSendProtocolMessages</code></h3>
<p>An overridable hook that determines if a connection should receive protocol messages when it connects.</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>connection</code></td>
<td><code>Connection</code></td>
<td>The connecting client</td>
</tr>
<tr>
<td><code>ctx</code></td>
<td><code>ConnectionContext</code></td>
<td>Contains the upgrade request</td>
</tr>
<tr>
<td><strong>Returns</strong></td>
<td><code>boolean</code></td>
<td><code>false</code> to suppress protocol messages</td>
</tr>
</tbody>
</table>
<p>Default: returns <code>true</code> (all connections receive protocol messages).</p>
<p>This hook is evaluated once on connect. The result is persisted in the connection's WebSocket attachment and survives <a href="/agents/runtime/communication/websockets/#hibernation">hibernation</a>.</p>
<h3 id="isconnectionprotocolenabled"><code>isConnectionProtocolEnabled</code></h3>
<p>Check if a connection currently has protocol messages enabled.</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>connection</code></td>
<td><code>Connection</code></td>
<td>The connection to check</td>
</tr>
<tr>
<td><strong>Returns</strong></td>
<td><code>boolean</code></td>
<td><code>true</code> if protocol messages are enabled</td>
</tr>
</tbody>
</table>
<p>Safe to call at any time, including after the agent wakes from hibernation.</p>
<h2 id="how-it-works">How it works</h2>
<p>Protocol status is stored as an internal flag in the connection's WebSocket attachment — the same mechanism used by <a href="/agents/runtime/communication/readonly-connections/">readonly connections</a>. This means:</p>
<ul>
<li><strong>Survives hibernation</strong> — the flag is serialized and restored when the agent wakes up</li>
<li><strong>No cleanup needed</strong> — connection state is automatically discarded when the connection closes</li>
<li><strong>Zero overhead</strong> — no database tables or queries, just the connection's built-in attachment</li>
<li><strong>Safe from user code</strong> — <code>connection.state</code> and <code>connection.setState()</code> never expose or overwrite the flag</li>
</ul>
<p>Unlike <a href="/agents/runtime/communication/readonly-connections/">readonly</a> which can be toggled dynamically with <code>setConnectionReadonly()</code>, protocol status is set once on connect and cannot be changed afterward. To change a connection's protocol status, the client must disconnect and reconnect.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/agents/runtime/communication/readonly-connections/">Readonly connections</a></li>
<li><a href="/agents/runtime/communication/websockets/">WebSockets</a></li>
<li><a href="/agents/runtime/lifecycle/state/">Store and sync state</a></li>
<li><a href="/agents/model-context-protocol/apis/client-api/">MCP Client API</a></li>
</ul>
