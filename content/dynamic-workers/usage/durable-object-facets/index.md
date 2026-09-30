<p>Durable Object Facets let you load a <a href="/durable-objects/">Durable Object</a> class from a <a href="/dynamic-workers/">Dynamic Worker</a> and run it as a child of your own Durable Object. The child (the facet) gets its own isolated SQLite database, while your class acts as a supervisor that controls access.</p>
<p>This is useful when you want dynamically-generated code — for example, code written by an AI agent — to have persistent storage, without giving it direct access to a Durable Object namespace. Your supervisor loads the code, creates the facet, and forwards requests into it. You stay in control of what the dynamic code can do.</p>
<h2 id="understand-the-model">Understand the model</h2>
<p>A facet-based setup has three layers:</p>
<ul>
<li><strong>Supervisor class</strong> — A normal Durable Object class that you write and deploy. It is configured with a SQLite storage backend like any other Durable Object.</li>
<li><strong>Dynamic code</strong> — Code loaded at runtime through the <a href="/dynamic-workers/getting-started/#configure-worker-loader">Worker Loader API</a>. This code exports a class that extends <code>DurableObject</code>.</li>
<li><strong>Facet</strong> — An instance of the dynamic class, created by calling <code>this.ctx.facets.get()</code> inside your supervisor. Each facet has its own SQLite database, separate from the supervisor's.</li>
</ul>
<p>The supervisor's database and the facet's database are stored together as part of the same overall Durable Object. The dynamic code cannot read the supervisor's database — it only has access to its own.</p>
<p><img src="/assets/upstream/images/dynamic-workers/facet-architecture.svg" alt="Diagram showing the facet architecture: a request flows through the Worker entry point into a Durable Object instance containing a Supervisor with its own SQLite DB, which creates an isolated Facet with a separate SQLite DB via ctx.facets.get() and forwards requests to it via facet.fetch()" /></p>
<h2 id="configure-your-worker">Configure your Worker</h2>
<p>Your Worker needs two things: a Durable Object class with a SQLite storage backend, and a Worker Loader binding.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8447.md")
</div>
<h2 id="load-and-run-a-dynamic-class">Load and run a dynamic class</h2>
<p>The following example shows a supervisor Durable Object (<code>AppRunner</code>) that loads dynamic code, creates a facet from it, and forwards HTTP requests to the facet.</p>
<p>The dynamic code is a simple counter app that tracks how many requests it has received, using its own SQLite-backed storage. In a real application, this code would come from an AI agent or user upload rather than a static string.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8448.md")
</div>
<p>In this example:</p>
<ul>
<li><code>AppRunner</code> is your supervisor Durable Object. You deploy it normally and it owns a Durable Object namespace.</li>
<li>The dynamic code exports a class (<code>App</code>) that extends <code>DurableObject</code>. This class uses <code>this.ctx.storage</code> to read and write data, just like any Durable Object.</li>
<li><code>this.ctx.facets.get(&quot;app&quot;, callback)</code> creates the facet. The <code>&quot;app&quot;</code> string names the facet — each name gets its own SQLite database within the parent Durable Object.</li>
<li>The facet's database is fully isolated from the supervisor's database. <code>AppRunner</code> and <code>App</code> each have their own storage that the other cannot access.</li>
</ul>
<h2 id="this-ctx-facets-reference"><code>this.ctx.facets</code> reference</h2>
<p>The <code>this.ctx.facets</code> object is available inside any Durable Object class. It provides methods to create, shut down, and delete facets. A single Durable Object can have any number of facets with different names, each with its own independent SQLite database.</p>
<h3 id="get"><code>get</code></h3>
<p><code>this.ctx.facets.get(name <span class="nb-type">string</span>, callback <span class="nb-type">() =&gt; FacetStartupOptions</span>) <span class="nb-type">Fetcher</span></code></p>
<p>Creates or resumes a facet with the given name and returns a stub you can use to send it requests.</p>
<p>If the facet has not started yet, or has hibernated, the runtime calls <code>getStartupOptions</code> to determine what code to load. Otherwise, the existing facet is reused and the callback is not invoked. <code>callback</code> can optionally be <code>async</code> (i.e. returning <code>Promise&lt;FacetStartupOptions&gt;</code>).</p>
<p>The returned stub behaves like a <a href="/durable-objects/api/stub/">Durable Object stub</a>. You can call <code>.fetch()</code> on it to send HTTP requests, or call RPC methods directly.</p>
<h3 id="abort"><code>abort</code></h3>
<p><code>this.ctx.facets.abort(name <span class="nb-type">string</span>, reason <span class="nb-type">any</span>) <span class="nb-type">void</span></code></p>
<p>Shuts down a running facet and invalidates all existing stubs. Any subsequent call on an invalidated stub throws <code>reason</code>. The facet's storage is preserved.</p>
<p>After aborting, you can call <code>get()</code> again to restart the facet — including with a different class. This makes <code>abort()</code> useful for code updates: abort the facet running the old version, then call <code>get()</code> with a callback that returns the new class.</p>
<h3 id="delete"><code>delete</code></h3>
<p><code>this.ctx.facets.delete(name <span class="nb-type">string</span>) <span class="nb-type">void</span></code></p>
<p>Aborts the facet (if running) and permanently deletes its SQLite database. If you call <code>get()</code> with the same name afterward, the facet starts with an empty database.</p>
<p>Use <code>delete()</code> to clean up storage for facets that are no longer needed.</p>
<h3 id="facetstartupoptions"><code>FacetStartupOptions</code></h3>
<p>The object returned by the <code>getStartupOptions</code> callback.</p>
<h4 id="class"><code>class <span class="nb-type">DurableObjectClass</span></code></h4>
<p>The Durable Object class to instantiate for the facet. Obtain this by calling <code>worker.getDurableObjectClass(&quot;ClassName&quot;)</code> on a Dynamic Worker stub.</p>
<h4 id="id"><code>id <span class="nb-type">DurableObjectId | string</span> <span class="nb-metainfo">Optional</span></code></h4>
<p>The ID the facet sees as its own <code>ctx.id</code>. If omitted, the facet inherits the parent Durable Object's ID.</p>
<h2 id="isolate-storage">Isolate storage</h2>
<p>The supervisor and each facet have separate SQLite databases. The dynamic code uses the standard <a href="/durable-objects/api/sqlite-storage-api/">Durable Object storage APIs</a> with all operations targeting the facet's own database.</p>
<p>This isolation means you do not need to trust the dynamic code with your supervisor's data. You can store metadata, billing counters, or access-control state in the supervisor's database, and the facet cannot read or modify any of it.</p>
<p>In production, you would typically store the dynamic code itself in the supervisor's database and load it in the <code>#loadDynamicWorker()</code> method. This keeps the code paired with the Durable Object instance that manages it.</p>
