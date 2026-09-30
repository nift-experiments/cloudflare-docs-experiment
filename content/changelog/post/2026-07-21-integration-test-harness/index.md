<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 27, 2026</time><h2 id="post-title">Run integration tests against your Worker's production build</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now provides <code>createTestHarness()</code>, an API for running integration tests against Workers built with <a href="/workers/testing/test-harness/configure/#configure-worker-projects">Wrangler or the Cloudflare Vite plugin</a> from any Node.js test runner.</p>
<p>The test harness starts a local Worker server with <a href="/workers/wrangler/api/#createtestharness">helpers for dispatching requests, resetting storage, and inspecting runtime logs</a>.</p>
<p>This is useful for tests that need to:</p>
<ul>
<li><a href="/workers/testing/test-harness/interact-with-workers/#test-route-dispatch-across-workers">Route requests across multiple Workers</a></li>
<li><a href="/workers/testing/test-harness/integrations/#mock-service-worker">Mock outbound <code>fetch()</code> requests</a> with Node.js request mocking libraries such as <a href="https://mswjs.io/">MSW</a></li>
<li><a href="/workers/testing/test-harness/integrations/#playwright">Run Playwright tests against a Worker</a></li>
</ul>
<p>For example, this test starts two Workers and mocks an upstream API:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17807.md")</div>
<p>Cloudflare now recommends <code>createTestHarness()</code> for integration tests instead of <a href="/workers/testing/unstable_startworker/"><code>unstable_startWorker()</code></a> or <a href="/workers/wrangler/api/#unstable_dev"><code>unstable_dev()</code></a>. To start a development server programmatically, use the Vite <a href="https://vite.dev/guide/api-javascript.html#createserver"><code>createServer()</code></a> API with the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
<p>For more information about <code>createTestHarness()</code>, refer to the <a href="/workers/testing/test-harness/">Integration test harness guide</a>.</p>
</div></article></div>
