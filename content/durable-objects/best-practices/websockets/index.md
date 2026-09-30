---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/best-practices/websockets/
  description: Serve WebSocket connections from Durable Objects, including the standard and Hibernation APIs.
  full_title: Use WebSockets · Cloudflare Durable Objects docs
  head_html: <title>Use WebSockets · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="Serve WebSocket connections from Durable Objects, including the standard and Hibernation APIs."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/best-practices/websockets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/best-practices/websockets/index.md"><meta property="og:title" content="Use WebSockets · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Serve WebSocket connections from Durable Objects, including the standard and Hibernation APIs."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/best-practices/websockets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/best-practices/websockets/#page","headline":"Use WebSockets \u00b7 Cloudflare Durable Objects docs","description":"Serve WebSocket connections from Durable Objects, including the standard and Hibernation APIs.","url":"https://developers.cloudflare.com/durable-objects/best-practices/websockets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/best-practices/websockets/
  schema: 1
---
<p>Durable Objects can act as WebSocket servers that connect thousands of clients per instance. You can also use WebSockets as a client to connect to other servers or Durable Objects.</p>
<p>Two WebSocket APIs are available:</p>
<ol>
<li><strong>Hibernation WebSocket API</strong> - Allows the Durable Object to hibernate without disconnecting clients when idle. <strong>(recommended)</strong></li>
<li><strong>Web Standard WebSocket API</strong> - Uses the familiar <code>addEventListener</code> event pattern.</li>
</ol>
<h2 id="what-are-websockets">What are WebSockets?</h2>
<p>WebSockets are long-lived TCP connections that enable bi-directional, real-time communication between client and server.</p>
<p>Key characteristics:</p>
<ul>
<li>Both Workers and Durable Objects can act as WebSocket endpoints (client or server)</li>
<li>WebSocket sessions are long-lived, making Durable Objects ideal for accepting connections</li>
<li>A single Durable Object instance can coordinate between multiple clients (for example, chat rooms or multiplayer games)</li>
</ul>
<p>Refer to <a href="https://github.com/cloudflare/workers-chat-demo">Cloudflare Edge Chat Demo</a> for an example of using Durable Objects with WebSockets.</p>
<h3 id="why-use-hibernation">Why use Hibernation?</h3>
<p>The Hibernation WebSocket API reduces costs by allowing Durable Objects to sleep when idle:</p>
<ul>
<li>Clients remain connected while the Durable Object is not in memory</li>
<li><a href="/durable-objects/platform/pricing/">Billable Duration (GB-s) charges</a> do not accrue during hibernation</li>
<li>When a message arrives, the Durable Object wakes up automatically</li>
</ul>
<h2 id="durable-objects-hibernation-websocket-api">Durable Objects Hibernation WebSocket API</h2>
<p>The Hibernation WebSocket API extends the <a href="/workers/runtime-apis/websockets/">Web Standard WebSocket API</a> to reduce costs during periods of inactivity.</p>
<h3 id="how-hibernation-works">How hibernation works</h3>
<p>When a Durable Object receives no events (such as alarms or messages) for a short period, it is evicted from memory. During hibernation:</p>
<ul>
<li>WebSocket clients remain connected to the Cloudflare network</li>
<li>In-memory state is reset</li>
<li>When an event arrives, the Durable Object is re-initialized and its <code>constructor</code> runs</li>
</ul>
<p>To restore state after hibernation, use <a href="#websocketserializeattachment"><code>serializeAttachment</code></a> and <a href="#websocketdeserializeattachment"><code>deserializeAttachment</code></a> to persist data with each WebSocket connection.</p>
<p>Refer to <a href="/durable-objects/concepts/durable-object-lifecycle/">Lifecycle of a Durable Object</a> for more information.</p>
<h3 id="hibernation-example">Hibernation example</h3>
<p>To use WebSockets with Durable Objects:</p>
<ol>
<li>Proxy the request from the Worker to the Durable Object</li>
<li>Call <a href="/durable-objects/api/state/#acceptwebsocket"><code>DurableObjectState::acceptWebSocket</code></a> to accept the server side connection</li>
<li>Define handler methods on the Durable Object class for relevant events</li>
</ol>
<p>If an event occurs for a hibernated Durable Object, the runtime re-initializes it by calling the constructor. Minimize work in the constructor when using hibernation.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8244.md")
</div></div>
<p>Configure your Wrangler file with a Durable Object <a href="/durable-objects/get-started/#4-configure-durable-object-bindings">binding</a> and <a href="/durable-objects/reference/durable-objects-migrations/">migration</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8245.md")
</div>
<p>A full example is available in <a href="/durable-objects/examples/websocket-hibernation-server/">Build a WebSocket server with WebSocket Hibernation</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="local-development-support">Local development support</h3>
@markup("md", "content/.markup/bodies/8240.md")
</aside>
<h3 id="automatic-ping-pong-handling">Automatic ping/pong handling</h3>
<p>The Cloudflare runtime automatically handles WebSocket protocol ping frames:</p>
<ul>
<li>Incoming <a href="https://www.rfc-editor.org/rfc/rfc6455#section-5.5.2">ping frames</a> receive automatic pong responses</li>
<li>Ping/pong handling does not interrupt hibernation</li>
<li>The <code>webSocketMessage</code> handler is not called for control frames</li>
</ul>
<p>This behavior keeps connections alive without waking the Durable Object.</p>
<h3 id="batch-messages-to-reduce-overhead">Batch messages to reduce overhead</h3>
<p>Each WebSocket message incurs processing overhead from context switches between the JavaScript runtime and the underlying system. Sending many small messages can overwhelm a single Durable Object. This happens even if the total data volume is small.</p>
<p>To maximize throughput:</p>
<ul>
<li><strong>Batch multiple logical messages</strong> into a single WebSocket frame</li>
<li><strong>Use a simple envelope format</strong> to pack and unpack batched messages</li>
<li><strong>Target fewer, larger messages</strong> rather than many small ones</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8246.md")
</div>
<h4 id="why-batching-helps">Why batching helps</h4>
<p>WebSocket reads require context switches between the kernel and JavaScript runtime. Each individual message triggers this overhead. Batching 10-100 logical messages into a single WebSocket frame reduces context switches proportionally.</p>
<p>For high-frequency data like sensor readings or game state updates, use time-based or count-based batching. Batch every 50-100ms or every 50-100 messages, whichever comes first.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8239.md")
</aside>
<h3 id="extended-methods">Extended methods</h3>
<p>The following methods are available on the Hibernation WebSocket API. Use them to persist and restore state before and after hibernation.</p>
<h4 id="websocket-serializeattachment"><code>WebSocket.serializeAttachment</code></h4>
<ul>
<li><code>serializeAttachment(value <span class="nb-type">any</span>)</code>
: <span class="nb-type">void</span></li>
</ul>
<p>Keeps a copy of <code>value</code> associated with the WebSocket connection.</p>
<p>Key behaviors:</p>
<ul>
<li>Serialized attachments persist through hibernation as long as the WebSocket remains healthy</li>
<li>If either side closes the connection, attachments are lost</li>
<li>Modifications to <code>value</code> after calling this method are not retained unless you call it again</li>
<li>The <code>value</code> can be any type supported by the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm">structured clone algorithm</a></li>
<li>Maximum serialized size is 16,384 bytes</li>
</ul>
<p>For larger values or data that must persist beyond WebSocket lifetime, use the <a href="/durable-objects/api/sqlite-storage-api/">Storage API</a> and store the corresponding key as an attachment.</p>
<h4 id="websocket-deserializeattachment"><code>WebSocket.deserializeAttachment</code></h4>
<ul>
<li><code>deserializeAttachment()</code>: <span class="nb-type">any</span></li>
</ul>
<p>Retrieves the most recent value passed to <code>serializeAttachment()</code>, or <code>null</code> if none exists.</p>
<h4 id="attachment-example">Attachment example</h4>
<p>Use <code>serializeAttachment</code> and <code>deserializeAttachment</code> to persist per-connection state across hibernation:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8247.md")
</div>
<h2 id="websocket-standard-api">WebSocket Standard API</h2>
<p>WebSocket connections are established by making an HTTP GET request with the <code>Upgrade: websocket</code> header.</p>
<p>The typical flow:</p>
<ol>
<li>A Worker validates the upgrade request</li>
<li>The Worker proxies the request to the Durable Object</li>
<li>The Durable Object accepts the server side connection</li>
<li>The Worker returns the client side connection in the response</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="validate-requests-in-a-worker">Validate requests in a Worker</h3>
@markup("md", "content/.markup/bodies/8238.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8251.md")
</div></div>
<p>The following Durable Object creates a WebSocket connection and responds to messages with the total number of connections:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8255.md")
</div></div>
<p>Configure your Wrangler file with a Durable Object <a href="/durable-objects/get-started/#4-configure-durable-object-bindings">binding</a> and <a href="/durable-objects/reference/durable-objects-migrations/">migration</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8256.md")
</div>
<p>A full example is available in <a href="/durable-objects/examples/websocket-server/">Build a WebSocket server</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="websocket-disconnection-on-deploy">WebSocket disconnection on deploy</h3>
@markup("md", "content/.markup/bodies/8237.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/WebSocket">Mozilla Developer Network's (MDN) documentation on the WebSocket class</a></li>
<li><a href="https://github.com/cloudflare/websocket-template">Cloudflare's WebSocket template for building applications on Workers using WebSockets</a></li>
<li><a href="/durable-objects/api/base/">Durable Object base class</a></li>
<li><a href="/durable-objects/api/state/">Durable Object State interface</a></li>
</ul>
<pre tabindex="0"><code>&#10;</code></pre>
