<p><code>createTestHarness()</code> runs one or more Workers in a single local server. Each Worker can come from a Wrangler project or a Vite project that uses the Cloudflare Vite plugin.</p>
<h2 id="configure-worker-projects">Configure Worker projects</h2>
<p>Point each entry in the <code>workers</code> array to the Wrangler configuration file for a project:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17350.md")
</div>
<p>For Workers built by the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>, run <code>vite build</code> first so tests use the production build output:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx vite build</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx vite build" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn vite build</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn vite build" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm vite build</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm vite build" aria-label="Copy to clipboard">Copy</button></div></div>
<p>The generated Wrangler configuration works like any other <code>configPath</code>. Each Worker is configured independently, so one harness can run both project types:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17351.md")
</div>
<h2 id="select-a-wrangler-environment">Select a Wrangler environment</h2>
<p>By default, the test harness loads the top-level Wrangler configuration. Set <code>env</code> if you want to load a specific environment from the configuration.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17352.md")
</div>
<h2 id="override-variables-and-secrets">Override variables and secrets</h2>
<p>You can override <code>vars</code> and <code>secrets</code> for each Worker in the harness if you want to avoid creating a separate Wrangler environment for testing.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17353.md")
</div>
<h2 id="configure-the-harness-after-setup">Configure the harness after setup</h2>
<p>If part of the Worker configuration depends on the test setup, you can call <code>createTestHarness()</code> without options and configure the harness with <code>server.update()</code> before starting the server.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17354.md")
</div>
<h2 id="reset-the-harness-between-tests">Reset the harness between tests</h2>
<p>When reusing a server across tests, call <code>server.reset()</code> after each test. It recreates local storage and restores Workers to the options used when the current session started.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17355.md")
</div>
<p>After a reset, apply any required schema migrations and seed data again. For examples, refer to <a href="/workers/testing/test-harness/prepare-test-state/">Prepare test state</a>.</p>
<h2 id="print-debug-output-when-tests-fail">Print debug output when tests fail</h2>
<p><code>server.debug()</code> prints the server timeline and captured Workers runtime logs. Call it when a test throws an exception or fails and you need more information to debug it.</p>
<p>The following example uses a cleanup hook from Vitest:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17356.md")
</div>
<h2 id="specify-types-for-worker-handles">Specify types for Worker handles</h2>
<p><code>server.getWorker()</code> accepts types for the Worker environment and module exports. You can define these types manually. But to keep them aligned with your Worker, you can generate the env type from the Wrangler configuration and derive the exports from its source module.</p>
<p>Give each Worker a distinct environment interface so the generated declarations can be used together:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler types ./workers/api/worker-configuration.d.ts --config ./workers/api/wrangler.jsonc --env-interface ApiEnv</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler types ./workers/api/worker-configuration.d.ts --config ./workers/api/wrangler.jsonc --env-interface ApiEnv" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler types ./workers/api/worker-configuration.d.ts --config ./workers/api/wrangler.jsonc --env-interface ApiEnv</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler types ./workers/api/worker-configuration.d.ts --config ./workers/api/wrangler.jsonc --env-interface ApiEnv" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler types ./workers/api/worker-configuration.d.ts --config ./workers/api/wrangler.jsonc --env-interface ApiEnv</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler types ./workers/api/worker-configuration.d.ts --config ./workers/api/wrangler.jsonc --env-interface ApiEnv" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Repeat this command for each Worker and include the generated files in the TypeScript configuration for your tests:</p>
<pre><code class="language-json">{&#10;	&quot;include&quot;: [&quot;./workers/*/worker-configuration.d.ts&quot;, &quot;./tests/**/*.ts&quot;]&#10;}&#10;</code></pre>
<p>Pass the generated environment interface to <code>server.getWorker()</code>. Use <code>typeof import()</code> to derive the Worker exports from its source module:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17357.md")
</div>
<p>In this example, <code>ApiEnv</code> comes from <code>worker-configuration.d.ts</code>. The module type includes the default export and its RPC methods. Re-run <a href="/workers/languages/typescript/#generate-types"><code>wrangler types</code></a> when the Worker configuration changes.</p>
