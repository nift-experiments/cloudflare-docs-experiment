<h2 id="description">Description</h2>
<p>The <code>DurableObjectStub</code> interface is a client used to invoke methods on a remote <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8314.md")
</div>. The type of `DurableObjectStub` is generic to allow for RPC methods to be invoked on the stub.
<p>Durable Objects implement E-order semantics, a concept deriving from the <a href="https://en.wikipedia.org/wiki/E_(programming_language)">E distributed programming language</a>. When you make multiple calls to the same Durable Object, it is guaranteed that the calls will be delivered to the remote Durable Object in the order in which you made them. E-order semantics makes many distributed programming problems easier. E-order is implemented by the <a href="https://capnproto.org">Cap'n Proto</a> distributed object-capability RPC protocol, which Cloudflare Workers uses for internal communications.</p>
<p>If an exception is thrown by a Durable Object <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8315.md")
</div> all in-flight calls and future calls will fail with [exceptions](/durable-objects/observability/troubleshooting/). To continue invoking methods on a remote Durable Object a Worker must recreate the stub. There are no ordering guarantees between different stubs.
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8318.md")
</div></div>
<h2 id="properties">Properties</h2>
<h3 id="id"><code>id</code></h3>
<p><code>id</code> is a property of the <code>DurableObjectStub</code> corresponding to the <a href="/durable-objects/api/id"><code>DurableObjectId</code></a> used to create the stub.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8321.md")
</div></div>
<h3 id="name"><code>name</code></h3>
<p><code>name</code> is an optional property of a <code>DurableObjectStub</code>, which returns a name if it was provided upon stub creation either directly via <a href="/durable-objects/api/namespace/#getbyname"><code>DurableObjectNamespace::getByName</code></a> or indirectly via a <a href="/durable-objects/api/id"><code>DurableObjectId</code></a> created by <a href="/durable-objects/api/namespace/#idfromname"><code>DurableObjectNamespace::idFromName</code></a>. This value is undefined if the <a href="/durable-objects/api/id"><code>DurableObjectId</code></a> used to create the <code>DurableObjectStub</code> was constructed using <a href="/durable-objects/api/namespace/#newuniqueid"><code>DurableObjectNamespace::newUniqueId</code></a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8324.md")
</div></div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://blog.cloudflare.com/durable-objects-easy-fast-correct-choose-three/">Durable Objects: Easy, Fast, Correct – Choose Three</a>.</li>
</ul>
