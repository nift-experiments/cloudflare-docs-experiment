<h2 id="description">Description</h2>
<p>A Durable Object namespace is a set of Durable Objects that are backed by the same <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8368.md")
</div>. There is only one Durable Object namespace per class. A Durable Object namespace can contain any number of Durable Objects.
<p>The <code>DurableObjectNamespace</code> interface is used to obtain a reference to new or existing Durable Objects. The interface is accessible from the fetch handler on a Cloudflare Worker via the <code>env</code> parameter, which is the standard interface when referencing bindings declared in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<p>This interface defines several <a href="/durable-objects/api/namespace/#methods">methods</a> that can be used to create an ID for a Durable Object. Note that creating an ID for a Durable Object does not create the Durable Object. The Durable Object is created lazily after calling <a href="/durable-objects/api/namespace/#get"><code>DurableObjectNamespace::get</code></a> to create a <a href="/durable-objects/api/stub"><code>DurableObjectStub</code></a> from a <code>DurableObjectId</code>. This ensures that objects are not constructed until they are actually accessed.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8372.md")
</div></div>
<h2 id="methods">Methods</h2>
<h3 id="idfromname"><code>idFromName</code></h3>
<p><code>idFromName</code> creates a unique <a href="/durable-objects/api/id"><code>DurableObjectId</code></a> which refers to an individual instance of the Durable Object class. Named Durable Objects are the most common method of referring to Durable Objects.</p>
<pre><code class="language-js">const fooId = env.MY_DURABLE_OBJECT.idFromName(&quot;foo&quot;);&#10;const barId = env.MY_DURABLE_OBJECT.idFromName(&quot;bar&quot;);&#10;</code></pre>
<h4 id="parameters">Parameters</h4>
<ul>
<li>A required string to be used to generate a <a href="/durable-objects/api/id"><code>DurableObjectId</code></a> corresponding to the name of a Durable Object.</li>
</ul>
<h4 id="return-values">Return values</h4>
<ul>
<li>A <a href="/durable-objects/api/id"><code>DurableObjectId</code></a> referring to an instance of a Durable Object class.</li>
</ul>
<h3 id="newuniqueid"><code>newUniqueId</code></h3>
<p><code>newUniqueId</code> creates a randomly generated and unique <a href="/durable-objects/api/id"><code>DurableObjectId</code></a> which refers to an individual instance of the Durable Object class. IDs created using <code>newUniqueId</code>, will need to be stored as a string in order to refer to the same Durable Object again in the future. For example, the ID can be stored in Workers KV, another Durable Object, or in a cookie in the user's browser.</p>
<pre><code class="language-js">const id = env.MY_DURABLE_OBJECT.newUniqueId();&#10;const euId = env.MY_DURABLE_OBJECT.newUniqueId({ jurisdiction: &quot;eu&quot; });&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="newuniqueid-results-in-lower-request-latency-at-first-use">`newUniqueId` results in lower request latency at first use</h3>
@markup("md", "content/.markup/bodies/8367.md")
</aside>
<h4 id="parameters-1">Parameters</h4>
<ul>
<li>An optional object with the key <code>jurisdiction</code> and value of a <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">jurisdiction</a> string.</li>
</ul>
<h4 id="return-values-1">Return values</h4>
<ul>
<li>A <a href="/durable-objects/api/id"><code>DurableObjectId</code></a> referring to an instance of the Durable Object class.</li>
</ul>
<h3 id="idfromstring"><code>idFromString</code></h3>
<p><code>idFromString</code> creates a <a href="/durable-objects/api/id"><code>DurableObjectId</code></a> from a previously generated ID that has been converted to a string. This method throws an exception if the ID is invalid, for example, if the ID was not created from the same <code>DurableObjectNamespace</code>.</p>
<pre><code class="language-js">// Create a new unique ID&#10;const id = env.MY_DURABLE_OBJECT.newUniqueId();&#10;// Convert the ID to a string to be saved elsewhere, e.g. a session cookie&#10;const session_id = id.toString();&#10;&#10;...&#10;// Recreate the ID from the string&#10;const id = env.MY_DURABLE_OBJECT.idFromString(session_id);&#10;</code></pre>
<h4 id="parameters-2">Parameters</h4>
<ul>
<li>A required string corresponding to a <a href="/durable-objects/api/id"><code>DurableObjectId</code></a> previously generated either by <code>newUniqueId</code> or <code>idFromName</code>.</li>
</ul>
<h4 id="return-values-2">Return values</h4>
<ul>
<li>A <a href="/durable-objects/api/id"><code>DurableObjectId</code></a> referring to an instance of a Durable Object class.</li>
</ul>
<h3 id="get"><code>get</code></h3>
<p><code>get</code> obtains a <a href="/durable-objects/api/stub"><code>DurableObjectStub</code></a> from a <a href="/durable-objects/api/id"><code>DurableObjectId</code></a> which can be used to invoke methods on a Durable Object.</p>
<p>This method returns the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8373.md")
</div> immediately, often before a connection has been established to the Durable Object. This allows requests to be sent to the instance right away, without waiting for a network round trip.
<pre><code class="language-js">const id = env.MY_DURABLE_OBJECT.newUniqueId();&#10;const stub = env.MY_DURABLE_OBJECT.get(id);&#10;</code></pre>
<h4 id="parameters-3">Parameters</h4>
<ul>
<li>A required <a href="/durable-objects/api/id"><code>DurableObjectId</code></a></li>
<li>An optional object with the key <code>locationHint</code> and value of a <a href="/durable-objects/reference/data-location/#provide-a-location-hint">locationHint</a> string.</li>
</ul>
<h4 id="return-values-3">Return values</h4>
<ul>
<li>A <a href="/durable-objects/api/stub"><code>DurableObjectStub</code></a> referring to an instance of a Durable Object class.</li>
</ul>
<h3 id="getbyname"><code>getByName</code></h3>
<p><code>getByName</code> obtains a <a href="/durable-objects/api/stub"><code>DurableObjectStub</code></a> from a provided name, which can be used to invoke methods on a Durable Object.</p>
<p>This method returns the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8374.md")
</div> immediately, often before a connection has been established to the Durable Object. This allows requests to be sent to the instance right away, without waiting for a network round trip.
<pre><code class="language-js">const fooStub = env.MY_DURABLE_OBJECT.getByName(&quot;foo&quot;);&#10;const barStub = env.MY_DURABLE_OBJECT.getByName(&quot;bar&quot;);&#10;</code></pre>
<h4 id="parameters-4">Parameters</h4>
<ul>
<li>A required string to be used to generate a <a href="/durable-objects/api/stub"><code>DurableObjectStub</code></a> corresponding to an instance of the Durable Object class with the provided name.</li>
<li>An optional object with the key <code>locationHint</code> and value of a <a href="/durable-objects/reference/data-location/#provide-a-location-hint">locationHint</a> string.</li>
</ul>
<h4 id="return-values-4">Return values</h4>
<ul>
<li>A <a href="/durable-objects/api/stub"><code>DurableObjectStub</code></a> referring to an instance of a Durable Object class.</li>
</ul>
<h3 id="jurisdiction"><code>jurisdiction</code></h3>
<p><code>jurisdiction</code> creates a subnamespace from a namespace where all Durable Object IDs and references created from that subnamespace will be restricted to the specified <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">jurisdiction</a>.</p>
<pre><code class="language-js">const subnamespace = env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;);&#10;const euStub = subnamespace.getByName(&quot;foo&quot;);&#10;</code></pre>
<h4 id="parameters-5">Parameters</h4>
<ul>
<li>A required <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">jurisdiction</a> string.</li>
</ul>
<h4 id="return-values-5">Return values</h4>
<ul>
<li>A <code>DurableObjectNamespace</code> scoped to a particular regulatory or geographic jurisdiction. Additional geographic jurisdictions are continuously evaluated, so share requests in the <a href="https://discord.com/channels/595317990191398933/773219443911819284">Durable Objects Discord channel</a>.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://blog.cloudflare.com/durable-objects-easy-fast-correct-choose-three/">Durable Objects: Easy, Fast, Correct – Choose Three</a>.</li>
</ul>
