<p>The Workers platform provides complementary tools for testing different parts of your application. For most projects, use the <a href="/workers/testing/vitest-integration/">Workers Vitest integration</a> for unit tests and the <a href="/workers/testing/test-harness/"><code>createTestHarness()</code></a> API for integration tests.</p>
<h2 id="unit-tests">Unit tests</h2>
<p>Use the <a href="/workers/testing/vitest-integration/">Workers Vitest integration</a> for fast feedback while testing individual functions and modules. Tests run inside the Workers runtime, so your test code can access bindings and runtime APIs directly.</p>
<p>The Workers Vitest integration provides:</p>
<ul>
<li>Fast feedback while testing individual functions and modules.</li>
<li>Direct assertions against binding state, such as values written to KV, R2, D1, or Durable Objects.</li>
<li>Direct calls to Durable Objects and other runtime APIs.</li>
</ul>
<p>To set up unit tests, refer to <a href="/workers/testing/vitest-integration/write-your-first-test/">Write your first Vitest test</a>.</p>
<h2 id="integration-tests">Integration tests</h2>
<p>Use the <a href="/workers/testing/test-harness/"><code>createTestHarness()</code></a> API to exercise one or more Workers as a whole and test how they interact with each other and with external services.</p>
<p>The integration test harness provides:</p>
<ul>
<li>Confidence from exercising production Worker builds.</li>
<li>Coverage through configured HTTP routes across Workers.</li>
<li>Compatibility with any Node.js test runner and tools such as Playwright or MSW.</li>
</ul>
<p>To set up integration tests, refer to <a href="/workers/testing/test-harness/get-started/">Get started with the integration test harness</a>.</p>
