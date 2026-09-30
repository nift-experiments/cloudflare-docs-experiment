<p class="article-summary">Build a WebSocket server using WebSocket Hibernation on Durable Objects and Workers.</p>
<p>This example is similar to the <a href="/durable-objects/examples/websocket-server/">Build a WebSocket server</a> example, but uses the WebSocket Hibernation API. The WebSocket Hibernation API should be preferred for WebSocket server applications built on Durable Objects, since it significantly decreases duration charge, and provides additional features that pair well with WebSocket applications. For more information, refer to <a href="/durable-objects/best-practices/websockets/">Use Durable Objects with WebSockets</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8184.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8187.md")
</div></div>
<p>Finally, configure your Wrangler file to include a Durable Object <a href="/durable-objects/get-started/#4-configure-durable-object-bindings">binding</a> and <a href="/durable-objects/reference/durable-objects-migrations/">migration</a> based on the namespace and class name chosen previously.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8188.md")
</div>
<h3 id="related-resources">Related resources</h3>
<ul>
<li><a href="https://github.com/cloudflare/workers-chat-demo/">Durable Objects: Edge Chat Demo with Hibernation</a>.</li>
</ul>
