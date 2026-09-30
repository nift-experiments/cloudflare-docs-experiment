---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/api/terminal/
  description: Connect browser-based terminal UIs to sandbox shells via WebSocket.
  full_title: Terminal · Cloudflare Sandbox SDK docs
  head_html: <title>Terminal · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect browser-based terminal UIs to sandbox shells via WebSocket."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/api/terminal/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/api/terminal/index.md"><meta property="og:title" content="Terminal · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect browser-based terminal UIs to sandbox shells via WebSocket."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/api/terminal/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/api/terminal/#page","headline":"Terminal \u00b7 Cloudflare Sandbox SDK docs","description":"Connect browser-based terminal UIs to sandbox shells via WebSocket.","url":"https://developers.cloudflare.com/sandbox/api/terminal/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/api/terminal/
  schema: 1
---
<p>Connect browser-based terminal UIs to sandbox shells via WebSocket. The server-side <code>terminal()</code> method proxies WebSocket connections to the container, and the client-side <code>SandboxAddon</code> integrates with xterm.js for terminal rendering.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="sandbox-sdk-1-0-preview">Sandbox SDK 1.0 preview</h3>
@markup("md", "content/.markup/bodies/13595.md")
</aside>
<h2 id="server-side-methods">Server-side methods</h2>
<h3 id="terminal"><code>terminal()</code></h3>
<p>Proxy a WebSocket upgrade request to create a terminal connection.</p>
<pre tabindex="0"><code class="language-ts">const response = await sandbox.terminal(request: Request, options?: PtyOptions): Promise&lt;Response&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>request</code> - WebSocket upgrade request from the browser (must include <code>Upgrade: websocket</code> header)</li>
<li><code>options</code> (optional):
<ul>
<li><code>cols</code> - Terminal width in columns (default: <code>80</code>)</li>
<li><code>rows</code> - Terminal height in rows (default: <code>24</code>)</li>
</ul>
</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;Response&gt;</code> — WebSocket upgrade response</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13596.md")
</div>
<p>Works with both <a href="/sandbox/concepts/sessions/">default and explicitly created sessions</a>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13597.md")
</div>
<h2 id="client-side-addon">Client-side addon</h2>
<p>The <code>@cloudflare/sandbox/xterm</code> module provides <code>SandboxAddon</code> for xterm.js, which handles the WebSocket connection, reconnection, and terminal resize forwarding.</p>
<h3 id="sandboxaddon"><code>SandboxAddon</code></h3>
<pre tabindex="0"><code class="language-ts">import { SandboxAddon } from &#x27;@cloudflare/sandbox/xterm&#x27;;&#10;&#10;const addon = new SandboxAddon(options: SandboxAddonOptions);&#10;</code></pre>
<p><strong>Options</strong>:</p>
<ul>
<li><code>getWebSocketUrl(params)</code> - Build the WebSocket URL for each connection attempt. Receives:
<ul>
<li><code>sandboxId</code> - Target sandbox ID</li>
<li><code>sessionId</code> (optional) - Target session ID</li>
<li><code>origin</code> - WebSocket origin derived from <code>window.location</code> (for example, <code>wss://example.com</code>)</li>
</ul>
</li>
<li><code>reconnect</code> - Enable automatic reconnection with exponential backoff (default: <code>true</code>)</li>
<li><code>onStateChange(state, error?)</code> - Callback for connection state changes</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13598.md")
</div>
<h3 id="connect"><code>connect()</code></h3>
<p>Establish a connection to a sandbox terminal.</p>
<pre tabindex="0"><code class="language-ts">addon.connect(target: ConnectionTarget): void&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>target</code>:
<ul>
<li><code>sandboxId</code> - Sandbox to connect to</li>
<li><code>sessionId</code> (optional) - Session within the sandbox</li>
</ul>
</li>
</ul>
<p>Calling <code>connect()</code> with a new target disconnects from the current target and connects to the new one. Calling it with the same target while already connected is a no-op.</p>
<h3 id="disconnect"><code>disconnect()</code></h3>
<p>Close the connection and stop any reconnection attempts.</p>
<pre tabindex="0"><code class="language-ts">addon.disconnect(): void&#10;</code></pre>
<h3 id="properties">Properties</h3>
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
<td><code>state</code></td>
<td><code>'disconnected' | 'connecting' | 'connected'</code></td>
<td>Current connection state</td>
</tr>
<tr>
<td><code>sandboxId</code></td>
<td><code>string | undefined</code></td>
<td>Current sandbox ID</td>
</tr>
<tr>
<td><code>sessionId</code></td>
<td><code>string | undefined</code></td>
<td>Current session ID</td>
</tr>
</tbody>
</table>
<h2 id="websocket-protocol">WebSocket protocol</h2>
<p>The <code>SandboxAddon</code> handles the WebSocket protocol automatically. These details are for building custom terminal clients without the addon. For a complete example, refer to <a href="/sandbox/guides/browser-terminals/#connect-without-xtermjs">Connect without xterm.js</a>.</p>
<h3 id="connection-lifecycle">Connection lifecycle</h3>
<ol>
<li>Client opens a WebSocket to your Worker endpoint. Set <code>binaryType</code> to <code>arraybuffer</code>.</li>
<li>The server replays any <strong>buffered output</strong> from a previous connection as binary frames. This may arrive before the <code>ready</code> message.</li>
<li>The server sends a <code>ready</code> status message — the terminal is now accepting input.</li>
<li>Binary frames flow in both directions: UTF-8 encoded keystrokes from the client, terminal output (including ANSI escape sequences) from the server.</li>
<li>If the client disconnects, the PTY stays alive. Reconnecting to the same session replays buffered output so the terminal appears unchanged.</li>
</ol>
<h3 id="control-messages-client-to-server">Control messages (client to server)</h3>
<p>Send JSON text frames to control the terminal.</p>
<p><strong>Resize</strong> — update terminal dimensions (both <code>cols</code> and <code>rows</code> must be positive):</p>
<pre tabindex="0"><code class="language-json">{ &quot;type&quot;: &quot;resize&quot;, &quot;cols&quot;: 120, &quot;rows&quot;: 30 }&#10;</code></pre>
<h3 id="status-messages-server-to-client">Status messages (server to client)</h3>
<p>The server sends JSON text frames for lifecycle events.</p>
<p><strong>Ready</strong> — the PTY is initialized. Buffered output (if any) has already been sent:</p>
<pre tabindex="0"><code class="language-json">{ &quot;type&quot;: &quot;ready&quot; }&#10;</code></pre>
<p><strong>Exit</strong> — the shell process has terminated:</p>
<pre tabindex="0"><code class="language-json">{ &quot;type&quot;: &quot;exit&quot;, &quot;code&quot;: 0, &quot;signal&quot;: &quot;SIGTERM&quot; }&#10;</code></pre>
<p><strong>Error</strong> — an error occurred (for example, invalid control message or session not found):</p>
<pre tabindex="0"><code class="language-json">{ &quot;type&quot;: &quot;error&quot;, &quot;message&quot;: &quot;Session not found&quot; }&#10;</code></pre>
<h2 id="types">Types</h2>
<pre tabindex="0"><code class="language-ts">interface PtyOptions {&#10;	cols?: number;&#10;	rows?: number;&#10;}&#10;&#10;type ConnectionState = &quot;disconnected&quot; | &quot;connecting&quot; | &quot;connected&quot;;&#10;&#10;interface ConnectionTarget {&#10;	sandboxId: string;&#10;	sessionId?: string;&#10;}&#10;&#10;interface SandboxAddonOptions {&#10;	getWebSocketUrl: (params: {&#10;		sandboxId: string;&#10;		sessionId?: string;&#10;		origin: string;&#10;	}) =&gt; string;&#10;	reconnect?: boolean;&#10;	onStateChange?: (state: ConnectionState, error?: Error) =&gt; void;&#10;}&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/concepts/terminal/">Terminal connections</a> — How terminal connections work</li>
<li><a href="/sandbox/guides/browser-terminals/">Browser terminals</a> — Step-by-step setup guide</li>
<li><a href="/sandbox/api/sessions/">Sessions API</a> — Session management</li>
<li><a href="/sandbox/api/commands/">Commands API</a> — Non-interactive command execution</li>
</ul>
