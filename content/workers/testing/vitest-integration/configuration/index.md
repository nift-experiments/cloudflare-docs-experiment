<p>The Workers Vitest integration provides additional configuration on top of Vitest's usual options using the <code>cloudflareTest()</code> Vite plugin.</p>
<p>An example configuration would be:</p>
<pre><code class="language-ts">import { cloudflareTest } from &quot;@cloudflare/vitest-plugin&quot;;&#10;import { defineConfig } from &quot;vitest/config&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflareTest({&#10;			wrangler: {&#10;				configPath: &quot;./wrangler.jsonc&quot;,&#10;			},&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17330.md")
</aside>
<h2 id="apis">APIs</h2>
<p>The following APIs are exported from the <code>@cloudflare/vitest-plugin</code> package.</p>
<h3 id="cloudflaretest-options"><code>cloudflareTest(options)</code></h3>
<p>A Vite plugin that configures Vitest to use the Workers integration with the correct module resolution settings, and provides type checking for <a href="#cloudflaretestoptions">CloudflareTestOptions</a>. Add this to the <code>plugins</code> array in your Vitest config alongside <a href="https://vitest.dev/config/file.html"><code>defineConfig()</code></a> from Vitest.</p>
<p>It also accepts an optionally-<code>async</code> function returning <code>options</code>.</p>
<pre><code class="language-ts">import { cloudflareTest } from &quot;@cloudflare/vitest-plugin&quot;;&#10;import { defineConfig } from &quot;vitest/config&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflareTest({&#10;			// Refer to CloudflareTestOptions...&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<h3 id="buildpagesassetsbinding-assetspath"><code>buildPagesASSETSBinding(assetsPath)</code></h3>
<p>Exported from <code>@cloudflare/vitest-plugin/config</code>. Creates a Pages ASSETS binding that serves files inside the <code>assetsPath</code>. This is required if you use <code>createPagesEventContext()</code> to test your <strong>Pages Functions</strong>. Refer to the <a href="/workers/testing/vitest-integration/recipes">Pages recipe</a> for a full example.</p>
<pre><code class="language-ts">import path from &quot;node:path&quot;;&#10;import { buildPagesASSETSBinding, cloudflareTest } from &quot;@cloudflare/vitest-plugin&quot;;&#10;import { defineConfig } from &quot;vitest/config&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflareTest(async () =&gt; {&#10;			const assetsPath = path.join(__dirname, &quot;public&quot;);&#10;&#10;			return {&#10;				miniflare: {&#10;					serviceBindings: {&#10;						ASSETS: await buildPagesASSETSBinding(assetsPath),&#10;					},&#10;				},&#10;			};&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<h3 id="readd1migrations-migrationspath"><code>readD1Migrations(migrationsPath)</code></h3>
<p>Exported from <code>@cloudflare/vitest-plugin/config</code>. Reads all <a href="/d1/reference/migrations/">D1 migrations</a> stored at <code>migrationsPath</code> and returns them ordered by migration number. Each migration will have its contents split into an array of individual SQL queries. Call the <a href="/workers/testing/vitest-integration/test-apis/#d1"><code>applyD1Migrations()</code></a> function inside a test or <a href="https://vitest.dev/config/#setupfiles">setup file</a> to apply migrations. Refer to the <a href="https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-plugin-examples/d1">D1 recipe</a> for an example project using migrations.</p>
<pre><code class="language-ts">import path from &quot;node:path&quot;;&#10;import { cloudflareTest, readD1Migrations } from &quot;@cloudflare/vitest-plugin&quot;;&#10;import { defineConfig } from &quot;vitest/config&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflareTest(async () =&gt; {&#10;			const migrationsPath = path.join(__dirname, &quot;migrations&quot;);&#10;			const migrations = await readD1Migrations(migrationsPath);&#10;&#10;			return {&#10;				miniflare: {&#10;					// Add a test-only binding for migrations, so we can apply them in a setup file&#10;					bindings: { TEST_MIGRATIONS: migrations },&#10;				},&#10;			};&#10;		}),&#10;	],&#10;	test: {&#10;		setupFiles: [&quot;./test/apply-migrations.ts&quot;],&#10;	},&#10;});&#10;</code></pre>
<h2 id="cloudflaretestoptions"><code>CloudflareTestOptions</code></h2>
<p>Options passed directly to <code>cloudflareTest()</code>.</p>
<ul>
<li>
<p><code>main</code>: string optional</p>
<ul>
<li>Entry point to Worker run in the same isolate/context as tests. This option is required to use Durable Objects without an explicit <code>scriptName</code> if classes are defined in the same Worker. This file goes through Vite transforms and can be TypeScript. Note that <code>import module from &quot;&lt;path-to-main&gt;&quot;</code> inside tests gives exactly the same <code>module</code> instance as is used internally for <code>exports</code> and Durable Object bindings. If <code>wrangler.configPath</code> is defined and this option is not, it will be read from the <code>main</code> field in that configuration file.</li>
</ul>
</li>
<li>
<p><code>miniflare</code>: <code>SourcelessWorkerOptions &amp; { workers?: WorkerOptions\[]; }</code> optional</p>
<ul>
<li>
<p>Use this to provide configuration information that is typically stored within the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, such as <a href="/workers/runtime-apis/bindings/">bindings</a>, <a href="/workers/configuration/compatibility-dates/">compatibility dates</a>, and <a href="/workers/configuration/compatibility-flags/">compatibility flags</a>. The <code>WorkerOptions</code> interface is defined <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/miniflare#interface-workeroptions">here</a>. Use the <code>main</code> option above to configure the entry point, instead of the Miniflare <code>script</code>, <code>scriptPath</code>, or <code>modules</code> options.</p>
<ul>
<li>If no <code>compatibility_date</code> is provided, then the test will use the latest locally available date.</li>
</ul>
</li>
<li>
<p>If your project makes use of multiple Workers, you can configure auxiliary Workers that run in the same <code>workerd</code> process as your tests and can be bound to. Auxiliary Workers are configured using the <code>workers</code> array, containing regular Miniflare <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/miniflare#interface-workeroptions"><code>WorkerOptions</code></a> objects. Note that unlike the <code>main</code> Worker, auxiliary Workers:</p>
<ul>
<li>Cannot have TypeScript entrypoints. You must compile auxiliary Workers to JavaScript first. You can use the <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy --dry-run --outdir dist</code></a> command for this.</li>
<li>Use regular Workers module resolution semantics. Refer to the <a href="/workers/testing/vitest-integration/isolation-and-concurrency/#modules">Isolation and concurrency</a> page for more information.</li>
<li>Cannot access the <a href="/workers/testing/vitest-integration/test-apis/"><code>cloudflare:test</code></a> module.</li>
<li>Do not require specific compatibility dates or flags.</li>
<li>Can be written with the <a href="/workers/reference/migrate-to-module-workers/#service-worker-syntax">Service Worker syntax</a>.</li>
<li>Are not affected by global mocks defined in your tests.</li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>wrangler</code>: <code>{ configPath?: string; environment?: string; }</code> optional</p>
<ul>
<li>
<p>Path to <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to load <code>main</code>, <a href="/workers/configuration/compatibility-dates/">compatibility settings</a> and <a href="/workers/runtime-apis/bindings/">bindings</a> from. These options will be merged with the <code>miniflare</code> option above, with <code>miniflare</code> values taking precedence. For example, if your Wrangler configuration defined a <a href="/workers/runtime-apis/bindings/service-bindings/">service binding</a> named <code>SERVICE</code> to a Worker named <code>service</code>, but you included <code>serviceBindings: { SERVICE(request) { return new Response(&quot;body&quot;); } }</code> in the <code>miniflare</code> option, all requests to <code>SERVICE</code> in tests would return <code>body</code>. Note <code>configPath</code> accepts both <code>.toml</code> and <code>.json</code> files.</p>
</li>
<li>
<p>The environment option can be used to specify the <a href="/workers/wrangler/environments/">Wrangler environment</a> to pick up bindings and variables from.</p>
</li>
</ul>
</li>
</ul>
<h2 id="dynamic-configuration-with-inject">Dynamic configuration with <code>inject</code></h2>
<p>You can pass an <code>async</code> function to <code>cloudflareTest()</code> that receives an <code>inject</code> function. This allows you to define <code>miniflare</code> configuration based on injected values from <a href="https://vitest.dev/config/#globalsetup"><code>globalSetup</code></a> scripts. Use this if you have a value in your configuration that is dynamically generated and only known at runtime of your tests. For example, a global setup script might start an upstream server on a random port. This port could be <code>provide()</code>d and then <code>inject()</code>ed in the configuration for an external service binding or <a href="/hyperdrive/">Hyperdrive</a>. Refer to the <a href="https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-plugin-examples/hyperdrive">Hyperdrive recipe</a> for an example project using this provide/inject approach.</p>
<details class="nb-details"><summary>Illustrative example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17331.md")
</div></details>
<h2 id="sourcelessworkeroptions"><code>SourcelessWorkerOptions</code></h2>
<p>Sourceless <code>WorkerOptions</code> type without <code>script</code>, <code>scriptPath</code>, or <code>modules</code> properties. Refer to the Miniflare <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/miniflare#interface-workeroptions"><code>WorkerOptions</code></a> type for more details.</p>
<pre><code class="language-ts">type SourcelessWorkerOptions = Omit&lt;&#10;	WorkerOptions,&#10;	&quot;script&quot; | &quot;scriptPath&quot; | &quot;modules&quot; | &quot;modulesRoot&quot;&#10;&gt;;&#10;</code></pre>
