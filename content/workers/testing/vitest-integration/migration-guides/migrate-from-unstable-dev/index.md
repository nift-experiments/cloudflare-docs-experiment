<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17369.md")
</aside>
<p>The <a href="/workers/wrangler/api/#unstable_dev"><code>unstable_dev</code></a> API has been a recommended approach to run integration tests. The <code>@cloudflare/vitest-plugin</code> package integrates directly with Vitest for fast re-runs, supports both unit and integration tests, and provides isolated per-test storage.</p>
<p>This guide demonstrates key differences between tests written with the <code>unstable_dev</code> API and the Workers Vitest integration. For more information on writing tests with the Workers Vitest integration, refer to <a href="/workers/testing/vitest-integration/write-your-first-test/">Write your first test</a>.</p>
<h2 id="reference-a-worker-for-integration-testing">Reference a Worker for integration testing</h2>
<p>With <code>unstable_dev</code>, to trigger a <code>fetch</code> event, you would do this:</p>
<pre><code class="language-js">import { unstable_dev } from &quot;wrangler&quot;&#10;&#10;it(&quot;dispatches fetch event&quot;, () =&gt; {&#10;  const worker = await unstable_dev(&quot;src/index.ts&quot;);&#10;  const resp = await worker.fetch(&quot;http://example.com&quot;);&#10;  ...&#10;})&#10;</code></pre>
<p>With the Workers Vitest integration, you can accomplish the same goal using <code>exports</code> from <code>cloudflare:workers</code>. <code>exports.default</code> refers to the default export defined by the <code>main</code> option in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>. This <code>main</code> Worker runs in the same isolate as tests so any global mocks will apply to it too.</p>
<pre><code class="language-js">import { exports } from &quot;cloudflare:workers&quot;;&#10;import &quot;../src/&quot;; // Currently required to automatically rerun tests when `main` changes&#10;&#10;it(&quot;dispatches fetch event&quot;, async () =&gt; {&#10;	const response = await exports.default.fetch(&quot;http://example.com&quot;);&#10;	...&#10;});&#10;</code></pre>
<h2 id="stop-a-worker">Stop a Worker</h2>
<p>With the Workers Vitest integration, there is no need to stop a Worker via <code>worker.stop()</code>. This functionality is handled automatically after tests run.</p>
<h2 id="import-wrangler-configuration">Import Wrangler configuration</h2>
<p>Via the <code>unstable_dev</code> API, you can reference a <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> by adding it as an option:</p>
<pre><code class="language-js">await unstable_dev(&quot;src/index.ts&quot;, {&#10;	config: &quot;wrangler.toml&quot;,&#10;});&#10;</code></pre>
<p>With the Workers Vitest integration, you can now set this reference to a <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> in <code>vitest.config.js</code> for all of your tests:</p>
<pre><code class="language-js">import { cloudflareTest } from &quot;@cloudflare/vitest-plugin&quot;;&#10;import { defineConfig } from &quot;vitest/config&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflareTest({&#10;			wrangler: {&#10;				configPath: &quot;wrangler.jsonc&quot;,&#10;			},&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<h2 id="test-service-workers">Test service Workers</h2>
<p>Unlike the <code>unstable_dev</code> API, the Workers Vitest integration does not support testing Workers using the service worker format. You will need to first <a href="/workers/reference/migrate-to-module-workers/">migrate to the ES modules format</a> in order to use the Workers Vitest integration.</p>
<h2 id="define-types">Define types</h2>
<p>You can remove <code>UnstableDevWorker</code> imports from your code. Instead, follow the <a href="/workers/testing/vitest-integration/write-your-first-test/#define-types">Write your first test guide</a> to define types for all of your tests.</p>
<pre><code class="language-diff">&#45; import { unstable_dev } from &quot;wrangler&quot;;&#10;&#45; import type { UnstableDevWorker } from &quot;wrangler&quot;;&#10;&#43; import worker from &quot;src/index.ts&quot;;&#10;&#10;  describe(&quot;Worker&quot;, () =&gt; {&#10;&#45;   let worker: UnstableDevWorker;&#10;    ...&#10;  });&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/testing/vitest-integration/write-your-first-test/#define-types">Write your first test</a> - Write unit tests against Workers.</li>
</ul>
