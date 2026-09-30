<p class="article-summary">Build a WebSocket server using Durable Objects and Workers.</p>
<p>This example shows how to build a WebSocket server using <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8178.md")
</div> and Workers. The example exposes an endpoint to create a new WebSocket connection. This WebSocket connection echos any message while including the total number of WebSocket connections currently established. For more information, refer to [Use Durable Objects with WebSockets](/durable-objects/best-practices/websockets/).
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8177.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8181.md")
</div></div>
<p>Finally, configure your Wrangler file to include a Durable Object <a href="/durable-objects/get-started/#4-configure-durable-object-bindings">binding</a> and <a href="/durable-objects/reference/durable-objects-migrations/">migration</a> based on the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8182.md")
</div> and class name chosen previously.
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8183.md")
</div>
<h3 id="related-resources">Related resources</h3>
<ul>
<li><a href="https://github.com/cloudflare/workers-chat-demo">Durable Objects: Edge Chat Demo</a>.</li>
</ul>
