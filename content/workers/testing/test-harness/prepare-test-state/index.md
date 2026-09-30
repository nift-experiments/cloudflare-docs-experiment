<p>An integration test may need data in local storage before it runs. It may also depend on external services that you do not want to call during the test. Use the test harness to prepare this state and replace those dependencies.</p>
<h2 id="access-configured-bindings">Access configured bindings</h2>
<p><code>worker.getEnv()</code> returns the variables, secrets, and bindings configured for a Worker. You can <a href="/workers/testing/test-harness/configure/#specify-types-for-worker-handles">specify types</a> for <code>server.getWorker()</code> so these values are typed. Then use the returned storage bindings to seed data directly from a test:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17332.md")
</div>
<h2 id="apply-d1-migrations">Apply D1 migrations</h2>
<p>Use <code>worker.applyD1Migrations(bindingName)</code> to read the migration settings for a D1 binding from the Wrangler configuration. It uses the configured <code>migrations_dir</code> and <code>migrations_pattern</code>. Without these options, it reads <code>.sql</code> files from the <code>migrations</code> directory relative to the configuration file.</p>
<p>Call it after storage is reset to apply migrations that have not already run. Then access the database with <code>worker.getEnv()</code> and seed the required rows.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17333.md")
</div>
<h2 id="prepare-durable-object-storage">Prepare Durable Object storage</h2>
<p><code>worker.getDurableObjectStorage()</code> gives you access to the storage of a SQLite-backed Durable Object instance. Pass its binding name or exported class name. Then select the instance by name or ID.</p>
<p>The returned handle executes SQL inside the Durable Object. Use it to seed an instance before a test or inspect its state after the Worker runs.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17334.md")
</div>
<h2 id="mock-outbound-requests">Mock outbound requests</h2>
<p>The test harness proxies outbound <code>fetch()</code> requests from your Workers through the <code>globalThis.fetch()</code> function in your Node environment. This allows you to intercept these requests and return a predictable response in your tests.</p>
<p>Here is an example using <code>vi.spyOn()</code> to mock a single request. But you can also use <a href="/workers/testing/test-harness/integrations/#mock-service-worker">Mock Service Worker (MSW)</a> to intercept these requests based on your preferences.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17335.md")
</div>
<h2 id="mock-bindings-with-test-workers">Mock bindings with test Workers</h2>
<p>Use <code>bindingOverrides</code> when you want to control the behavior of a binding. It routes the binding to a test Worker running inside the harness. For example, a test Worker can replace the Browser Rendering binding and return a known screenshot without starting a browser.</p>
<p>The test Worker can also expose JSRPC methods that configure its behavior. Use <code>worker.getExport()</code> to access the default export from your test.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17336.md")
</div>
