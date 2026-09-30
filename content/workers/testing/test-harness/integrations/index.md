<p>You can use <code>createTestHarness()</code> with existing tools in the Node.js ecosystem. The examples on this page show common integration patterns that you can adapt to your test setup.</p>
<h2 id="mock-service-worker">Mock Service Worker</h2>
<p>If your Worker makes outbound <code>fetch()</code> requests, you can use <a href="https://mswjs.io/">Mock Service Worker (MSW)</a> to intercept them and return predictable responses. MSW provides reusable request handlers that can be shared across tests.</p>
<p>For example, you can start MSW before the tests, reject unhandled requests, and reset handlers after each test:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17342.md")
</div>
<h2 id="playwright">Playwright</h2>
<p>If you are building a web application and want to verify user flows in a real browser, use <a href="https://playwright.dev/">Playwright</a> with the test harness. Playwright can navigate pages, interact with the user interface, and verify the behavior of your Workers project end to end.</p>
<p>A Playwright fixture can start a test server with <code>createTestHarness()</code> before browser tests. If you want to mock outbound <code>fetch()</code> requests, you can also use <a href="#mock-service-worker">MSW</a> to intercept them at the same time.</p>
<p>The following fixture sets the Playwright <code>baseURL</code>, exposes MSW and the test harness to tests, and resets storage state after each test.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17343.md")
</div>
