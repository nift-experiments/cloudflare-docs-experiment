<p class="article-summary">Read and write to/from Workers KV within a Durable Object</p>
<p>The following Worker script shows you how to configure a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8189.md")
</div> to read from and/or write to a [Workers KV namespace](/kv/concepts/how-kv-works/). This is useful when using a Durable Object to coordinate between multiple clients, and allows you to serialize writes to KV and/or broadcast a single read from KV to hundreds or thousands of clients connected to a single Durable Object [using WebSockets](/durable-objects/best-practices/websockets/).
<p>Prerequisites:</p>
<ul>
<li>A <a href="/kv/api/">KV namespace</a> created via the Cloudflare dashboard or the <a href="/workers/wrangler/install-and-update/">wrangler CLI</a>.</li>
<li>A <a href="/kv/concepts/kv-bindings/">configured binding</a> for the <code>kv_namespace</code> in the Cloudflare dashboard or Wrangler file.</li>
<li>A <a href="/workers/wrangler/configuration/#durable-objects">Durable Object namespace binding</a>.</li>
</ul>
<p>Configure your Wrangler file as follows:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8190.md")
</div>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8193.md")
</div></div>
