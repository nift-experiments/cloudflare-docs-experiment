<p class="article-summary">Use the Durable Objects Alarms API to batch requests to a Durable Object.</p>
<p>This example implements an <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8229.md")
</div> handler that allows batching of requests to a single Durable Object.
<p>When a request is received and no alarm is set, it sets an alarm for 10 seconds in the future. The <code>alarm()</code> handler processes all requests received within that 10-second window.</p>
<p>If no new requests are received, no further alarms will be set until the next request arrives.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8232.md")
</div></div>
<p>The <code>alarm()</code> handler will be called once every 10 seconds. If an unexpected error terminates the Durable Object, the <code>alarm()</code> handler will be re-instantiated on another machine. Following a short delay, the <code>alarm()</code> handler will run from the beginning on the other machine.</p>
<p>Finally, configure your Wrangler file to include a Durable Object <a href="/durable-objects/get-started/#4-configure-durable-object-bindings">binding</a> and <a href="/durable-objects/reference/durable-objects-migrations/">migration</a> based on the namespace and class name chosen previously.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8233.md")
</div>
