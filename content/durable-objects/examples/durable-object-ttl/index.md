<p class="article-summary">Implement a Time To Live (TTL) for Durable Object instances.</p>
<p>A common feature request for Durable Objects is a Time To Live (TTL) for Durable Object instances. Durable Objects give developers the tools to implement a custom TTL in only a few lines of code. This example demonstrates how to implement a TTL making use of <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8214.md")
</div>. While this TTL will be extended upon every new request to the Durable Object, this can be customized based on a particular use case.
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="be-careful-when-calling-setalarm-in-the-durable-object-class-constructor">Be careful when calling `setAlarm` in the Durable Object class constructor</h3>
@markup("md", "content/.markup/bodies/8213.md")
</aside>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8218.md")
</div></div>
<p>To test and deploy this example, configure your Wrangler file to include a Durable Object <a href="/durable-objects/get-started/#4-configure-durable-object-bindings">binding</a> and <a href="/durable-objects/reference/durable-objects-migrations/">migration</a> based on the namespace and class name chosen previously.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8219.md")
</div>
