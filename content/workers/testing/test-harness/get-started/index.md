<p>This guide shows how to write a basic integration test for a Worker with <code>createTestHarness()</code>. The example uses Vitest as the test runner and exercises a Worker built with Wrangler.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need:</p>
<ul>
<li>A Worker project with a <a href="/workers/wrangler/configuration/">Wrangler configuration file</a></li>
<li>A Node.js test runner such as <a href="https://vitest.dev/">Vitest</a></li>
<li><code>wrangler</code> installed as a development dependency</li>
</ul>
<h2 id="create-a-test-harness">Create a test harness</h2>
<p>Import <code>createTestHarness()</code> from <code>wrangler</code>. Point the test harness at your Worker configuration file.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17347.md")
</div>
<h2 id="manage-the-test-harness-lifecycle">Manage the test harness lifecycle</h2>
<p>For simplicity, we will reuse a single server for the test suite and reset it after each test. You can also start a new server for each test if the tests do not share the same configuration.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17348.md")
</div>
<h2 id="write-your-first-test">Write your first test</h2>
<p>Use the <a href="/workers/testing/test-harness/interact-with-workers/">helpers</a> provided by the test harness to interact with the Worker and assert its behavior. For example, you can call <code>server.fetch()</code> to send a request to the Worker and assert against its response.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17349.md")
</div>
