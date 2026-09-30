<h2 id="description">Description</h2>
<p>A Durable Object ID is a 64-digit hexadecimal number used to identify a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8388.md")
</div>. Not all 64-digit hex numbers are valid IDs. Durable Object IDs are constructed indirectly via the [`DurableObjectNamespace`](/durable-objects/api/namespace) interface.
<p>The <code>DurableObjectId</code> interface refers to a new or existing Durable Object. This interface is most frequently used by <a href="/durable-objects/api/namespace/#get"><code>DurableObjectNamespace::get</code></a> to obtain a <a href="/durable-objects/api/stub"><code>DurableObjectStub</code></a> for submitting requests to a Durable Object. Note that creating an ID for a Durable Object does not create the Durable Object. The Durable Object is created lazily after creating a stub from a <code>DurableObjectId</code>. This ensures that objects are not constructed until they are actually accessed.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="logging">Logging</h3>
@markup("md", "content/.markup/bodies/8387.md")
</aside>
<h2 id="methods">Methods</h2>
<h3 id="tostring"><code>toString</code></h3>
<p><code>toString</code> converts a <code>DurableObjectId</code> to a 64 digit hex string. This string is useful for logging purposes or storing the <code>DurableObjectId</code> elsewhere, for example, in a session cookie. This string can be used to reconstruct a <code>DurableObjectId</code> via <code>DurableObjectNamespace::idFromString</code>.</p>
<pre><code class="language-js">// Create a new unique ID&#10;const id = env.MY_DURABLE_OBJECT.newUniqueId();&#10;// Convert the ID to a string to be saved elsewhere, e.g. a session cookie&#10;const session_id = id.toString();&#10;&#10;...&#10;// Recreate the ID from the string&#10;const id = env.MY_DURABLE_OBJECT.idFromString(session_id);&#10;</code></pre>
<h4 id="parameters">Parameters</h4>
<ul>
<li>None.</li>
</ul>
<h4 id="return-values">Return values</h4>
<ul>
<li>A 64 digit hex string.</li>
</ul>
<h3 id="equals"><code>equals</code></h3>
<p><code>equals</code> is used to compare equality between two instances of <code>DurableObjectId</code>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8391.md")
</div></div>
<h4 id="parameters-1">Parameters</h4>
<ul>
<li>A required <code>DurableObjectId</code> to compare against.</li>
</ul>
<h4 id="return-values-1">Return values</h4>
<ul>
<li>A boolean. True if equal and false otherwise.</li>
</ul>
<h2 id="properties">Properties</h2>
<h3 id="name"><code>name</code></h3>
<p><code>name</code> is an optional property of a <code>DurableObjectId</code>, which returns the name that was used to create the <code>DurableObjectId</code> via <a href="/durable-objects/api/namespace/#idfromname"><code>DurableObjectNamespace::idFromName</code></a>. This value is undefined if the <code>DurableObjectId</code> was constructed using <a href="/durable-objects/api/namespace/#newuniqueid"><code>DurableObjectNamespace::newUniqueId</code></a>.</p>
<p>The <code>name</code> property is also available on <code>ctx.id</code> inside the Durable Object when the caller uses <code>idFromName()</code> or <code>getByName()</code>. <code>ctx.id.name</code> will be <code>undefined</code> in the following cases:</p>
<ul>
<li>The caller accesses the Durable Object using <code>idFromString()</code>, even if the ID was originally created with <code>idFromName()</code>.</li>
<li>Names longer than 1,024 bytes are not passed through to <code>ctx.id</code>.</li>
<li>The Durable Object was created with <code>newUniqueId()</code>.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="alarms">Alarms</h3>
@markup("md", "content/.markup/bodies/8386.md")
</aside>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8395.md")
</div></div>
<p>The same <code>name</code> is available inside the Durable Object via <code>ctx.id.name</code>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8399.md")
</div></div>
<h3 id="jurisdiction"><code>jurisdiction</code></h3>
<p><code>jurisdiction</code> is an optional property of a <code>DurableObjectId</code>, which returns the <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">jurisdiction</a> the ID is restricted to, such as <code>&quot;eu&quot;</code> or <code>&quot;fedramp&quot;</code>. The same value is available inside the Durable Object via <code>ctx.id.jurisdiction</code>, including in <a href="/durable-objects/api/alarms/">alarm handlers</a> and objects accessed via <code>idFromString()</code>, so you can make region-aware decisions without passing the jurisdiction as an argument or persisting it in storage.</p>
<p><code>jurisdiction</code> is preserved across every ID-construction path, including:</p>
<ul>
<li>IDs created from a jurisdiction-restricted subnamespace, for example <code>env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;).idFromName(&quot;foo&quot;)</code> or <code>.newUniqueId()</code>.</li>
<li>IDs created via <code>env.MY_DURABLE_OBJECT.newUniqueId({ jurisdiction: &quot;eu&quot; })</code>.</li>
<li>IDs restored from a string via <code>idFromString()</code> — the jurisdiction is encoded in the string itself, so it works on any namespace binding.</li>
</ul>
<p><code>ctx.id.jurisdiction</code> is <code>undefined</code> in two cases:</p>
<ul>
<li>The Durable Object was not created in a jurisdiction-restricted namespace.</li>
<li>The Durable Object's alarm was scheduled before 2026-03-15. To backfill the value, reschedule the alarm from a <code>fetch()</code> or RPC handler.</li>
</ul>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8402.md")
</div></div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://blog.cloudflare.com/durable-objects-easy-fast-correct-choose-three/">Durable Objects: Easy, Fast, Correct – Choose Three</a>.</li>
</ul>
