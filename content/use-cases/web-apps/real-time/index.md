<p>Real-time features, such as live chat, collaborative editing, and multiplayer interactions, require persistent connections and strongly consistent state. Cloudflare Durable Objects maintain WebSocket connections and coordinate shared state, while Queues handle background event processing.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="durable-objects">Durable Objects</h3>
<p>Stateful objects with strongly consistent storage and coordination. <a href="/durable-objects/">Learn more about Durable Objects</a>.</p>
<ul>
<li><strong>WebSocket support</strong> - Maintain persistent connections and broadcast messages across clients in real time</li>
<li><strong>Collaborative editing</strong> - Build multiplayer and co-editing experiences with strongly consistent shared state</li>
<li><strong>Strong consistency</strong> - Coordinate state across many concurrent connections with transactional guarantees</li>
</ul>
<h3 id="queues">Queues</h3>
<p>Reliable message queuing and background processing for Workers. <a href="/queues/">Learn more about Queues</a>.</p>
<ul>
<li><strong>Event processing</strong> - Handle webhooks and background jobs reliably without blocking the main request path</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/durable-objects/get-started/">Durable Objects get started</a></li>
<li><a href="/durable-objects/examples/websocket-hibernation-server/">WebSocket connections with Durable Objects</a></li>
<li><a href="/queues/get-started/">Queues get started</a></li>
</ol>
