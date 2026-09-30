<h2 id="invoking-methods-on-a-durable-object">Invoking methods on a Durable Object</h2>
<p>All new projects and existing projects with a compatibility date greater than or equal to <a href="/workers/configuration/compatibility-flags/#durable-object-stubs-and-service-bindings-support-rpc"><code>2024-04-03</code></a> should prefer to invoke <a href="/workers/runtime-apis/rpc/">Remote Procedure Call (RPC)</a> methods defined on a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8295.md")
</div>.
<p>Projects requiring HTTP request/response flows or legacy projects can continue to invoke the <code>fetch()</code> handler on the Durable Object class.</p>
<h3 id="invoke-rpc-methods">Invoke RPC methods</h3>
<p>By writing a Durable Object class which inherits from the built-in type <code>DurableObject</code>, public methods on the Durable Objects class are exposed as <a href="/workers/runtime-apis/rpc/">RPC methods</a>, which you can call using a <a href="/durable-objects/api/stub">DurableObjectStub</a> from a Worker.</p>
<p>All RPC calls are <a href="/workers/runtime-apis/rpc/lifecycle/">asynchronous</a>, accept and return <a href="/workers/runtime-apis/rpc/">serializable types</a>, and <a href="/workers/runtime-apis/rpc/error-handling/">propagate exceptions</a> to the caller without a stack trace. Refer to <a href="/workers/runtime-apis/rpc/">Workers RPC</a> for complete details.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8298.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8294.md")
</aside>
<p>Refer to <a href="/durable-objects/examples/build-a-counter/">Build a Counter</a> for a complete example.</p>
<h3 id="invoking-the-fetch-handler">Invoking the <code>fetch</code> handler</h3>
<p>If your project is stuck on a compatibility date before <a href="/workers/configuration/compatibility-flags/#durable-object-stubs-and-service-bindings-support-rpc"><code>2024-04-03</code></a>, or has the need to send a <a href="/workers/runtime-apis/request/"><code>Request</code></a> object and return a <code>Response</code> object, then you should send requests to a Durable Object via the fetch handler.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8301.md")
</div></div>
<p>The <code>URL</code> associated with the <a href="/workers/runtime-apis/request/"><code>Request</code></a> object passed to the <code>fetch()</code> handler of your Durable Object must be a well-formed URL, but does not have to be a publicly-resolvable hostname.</p>
<p>Without RPC, customers frequently construct requests which corresponded to private methods on the Durable Object and dispatch requests from the <code>fetch</code> handler. RPC is obviously more ergonomic in this example.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8304.md")
</div></div>
