<p class="article-summary">Build a counter using Durable Objects and Workers with RPC methods.</p>
<p>This example shows how to build a counter using Durable Objects and Workers with <a href="/workers/runtime-apis/rpc">RPC methods</a> that can print, increment, and decrement a <code>name</code> provided by the URL query string parameter, for example, <code>?name=A</code>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8227.md")
</div></div>
<p>Finally, configure your Wrangler file to include a Durable Object <a href="/durable-objects/get-started/#4-configure-durable-object-bindings">binding</a> and <a href="/durable-objects/reference/durable-objects-migrations/">migration</a> based on the namespace and class name chosen previously.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8228.md")
</div>
<h3 id="related-resources">Related resources</h3>
<ul>
<li><a href="/workers/runtime-apis/rpc/">Workers RPC</a></li>
<li><a href="https://blog.cloudflare.com/durable-objects-easy-fast-correct-choose-three/">Durable Objects: Easy, Fast, Correct — Choose three</a>.</li>
</ul>
