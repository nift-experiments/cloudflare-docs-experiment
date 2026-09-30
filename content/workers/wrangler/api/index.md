---
cp9:
  canonical: https://developers.cloudflare.com/workers/wrangler/api/
  description: A set of programmatic APIs that can be integrated with local Cloudflare Workers-related workflows.
  full_title: API · Cloudflare Workers docs
  head_html: <title>API · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="A set of programmatic APIs that can be integrated with local Cloudflare Workers-related workflows."><link rel="canonical" href="https://developers.cloudflare.com/workers/wrangler/api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/wrangler/api/index.md"><meta property="og:title" content="API · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A set of programmatic APIs that can be integrated with local Cloudflare Workers-related workflows."><meta property="og:url" content="https://developers.cloudflare.com/workers/wrangler/api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/wrangler/api/#page","headline":"API \u00b7 Cloudflare Workers docs","description":"A set of programmatic APIs that can be integrated with local Cloudflare Workers-related workflows.","url":"https://developers.cloudflare.com/workers/wrangler/api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/wrangler/api/
  schema: 1
---
<p>Wrangler offers APIs to programmatically interact with your Cloudflare Workers.</p>
<ul>
<li><a href="#createtestharness"><code>createTestHarness</code></a> - Start one or more Workers for integration tests in any Node.js test runner.</li>
<li><a href="#experimental_generatetypes"><code>experimental_generateTypes</code></a> - Generate TypeScript type definitions from your Worker configuration.</li>
<li><a href="#unstable_startworker"><code>unstable_startWorker</code></a> - Start a server for running integration tests against your Worker.</li>
<li><a href="#unstable_dev"><code>unstable_dev</code></a> - Start a server for running either end-to-end (e2e) or integration tests against your Worker.</li>
<li><a href="#getplatformproxy"><code>getPlatformProxy</code></a> - Get proxies and values for emulating the Cloudflare Workers platform in a Node.js process.</li>
</ul>
<h2 id="createtestharness"><code>createTestHarness</code></h2>
<p><code>createTestHarness()</code> starts one or more Workers for integration tests from any Node.js test runner. It runs production build output from Wrangler configuration files, Vite-generated configuration files, or inline Wrangler configuration objects. The API wraps Miniflare and provides methods for dispatching requests and scheduled events.</p>
<p>For setup guidance and examples, refer to <a href="/workers/testing/test-harness/">Integration test harness</a>.</p>
<h3 id="syntax">Syntax</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16008.md")
</div>
<h3 id="parameters">Parameters</h3>
<ul>
<li>
<p><code>options</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p>Test harness options. If you call <code>createTestHarness()</code> without options, call <code>server.update(options)</code> before <code>server.listen()</code>.</p>
<ul>
<li>
<p><code>root</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>Base directory used to resolve relative Worker configuration paths. Defaults to <code>process.cwd()</code>.</p>
</li>
<li>
<p><code>workers</code> <span class="nb-type">WorkerInput[]</span></p>
<p>Workers to run in the test server. The first Worker is the primary Worker.</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>Each <code>WorkerInput</code> can load a Worker from a Wrangler configuration file:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16009.md")
</div>
<p>Configuration file inputs support these fields:</p>
<ul>
<li><code>configPath</code> <span class="nb-type">string | URL</span>
<ul>
<li>Path to a Wrangler configuration file. Relative paths resolve from <code>root</code>.</li>
</ul>
</li>
<li><code>env</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Wrangler environment to load from the configuration file.</li>
</ul>
</li>
<li><code>vars</code> <span class="nb-type">Record&lt;string, Json&gt;</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Test-only variables that override variables from the Wrangler configuration file.</li>
</ul>
</li>
<li><code>secrets</code> <span class="nb-type">Record&lt;string, string&gt;</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Test-only secrets that override values loaded from <code>.dev.vars</code> and <code>.env</code> files.</li>
</ul>
</li>
<li><code>bindingOverrides</code> <span class="nb-type">Record&lt;string, string&gt;</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Test-only service binding overrides. Keys are binding names in this Worker's environment. Values are Worker names in this test harness.</li>
</ul>
</li>
</ul>
<p>Each <code>WorkerInput</code> can also use <code>config</code> to provide an inline Wrangler configuration object:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16010.md")
</div>
<h3 id="return-type">Return type</h3>
<p><code>createTestHarness()</code> returns a <span class="nb-type">TestHarness</span> object with these methods:</p>
<ul>
<li><code>listen()</code> <span class="nb-type">Promise&lt;{ url: URL }&gt;</span>
<ul>
<li>Starts the server and returns its current URL. Repeated calls return the same session until the server is closed or reset.</li>
</ul>
</li>
<li><code>fetch(input, init)</code> <span class="nb-type">Promise&lt;Response&gt;</span>
<ul>
<li>Dispatches a fetch request through the server. Relative URLs resolve against the current server URL. Absolute URLs follow the configured Worker routes and fall back to the primary Worker.</li>
</ul>
</li>
<li><code>getWorker(name?)</code> <span class="nb-type">WorkerHandle</span>
<ul>
<li>Returns a handle for dispatching events directly to a Worker. When no name is provided, this returns the primary Worker.</li>
</ul>
</li>
<li><code>getLogs()</code> <span class="nb-type">WorkerdStructuredLog[]</span>
<ul>
<li>Returns captured Workers runtime logs since the current server session started or <code>clearLogs()</code> was last called.</li>
</ul>
</li>
<li><code>clearLogs()</code> <span class="nb-type">void</span>
<ul>
<li>Clears captured Workers runtime logs.</li>
</ul>
</li>
<li><code>debug()</code> <span class="nb-type">void</span>
<ul>
<li>Prints a diagnostic timeline for this test server, including server events and captured Workers runtime logs. This is useful in a test runner failure or cleanup hook.</li>
</ul>
</li>
<li><code>update(optionsOrUpdater)</code> <span class="nb-type">Promise&lt;void&gt;</span>
<ul>
<li>Updates the server configuration with a <code>TestHarnessOptions</code> object or a function that receives the current options and returns the next options. If the server has not started yet, this configures the options used by <code>listen()</code>. If the server is running, this reloads the running Workers. Updating the number of Workers in a running server is not supported.</li>
</ul>
</li>
<li><code>reset()</code> <span class="nb-type">Promise&lt;void&gt;</span>
<ul>
<li>Restores the server to the options used when the current session first started. Storage is recreated, and the server URL may change after reset.</li>
</ul>
</li>
<li><code>close()</code> <span class="nb-type">Promise&lt;void&gt;</span>
<ul>
<li>Stops the server and releases all runtime resources.</li>
</ul>
</li>
</ul>
<p><code>getWorker(name?)</code> returns a <span class="nb-type">WorkerHandle</span> object with these methods:</p>
<ul>
<li><code>fetch(input, init)</code> <span class="nb-type">Promise&lt;Response&gt;</span>
<ul>
<li>Dispatches a fetch event directly to this Worker.</li>
</ul>
</li>
<li><code>scheduled(options)</code> <span class="nb-type">Promise&lt;{ outcome: &quot;ok&quot; | &quot;canceled&quot; | &quot;exception&quot;; noRetry: boolean }&gt;</span>
<ul>
<li>Dispatches a scheduled event directly to this Worker.</li>
</ul>
</li>
<li><code>getEnv()</code> <span class="nb-type">Promise&lt;Env&gt;</span>
<ul>
<li>Returns the full environment object configured for this Worker, including variables, secrets, and bindings.</li>
</ul>
</li>
<li><code>getExport()</code> <span class="nb-type">Promise&lt;Service&lt;Module['default']&gt;&gt;</span>
<ul>
<li>Returns the default Worker export, including RPC methods.</li>
</ul>
</li>
<li><code>applyD1Migrations(bindingName)</code> <span class="nb-type">Promise&lt;void&gt;</span>
<ul>
<li>Applies local D1 migration files that have not already run to a D1 binding on this Worker.</li>
</ul>
</li>
<li><code>getDurableObjectStorage(classNameOrBindingName, options)</code> <span class="nb-type">Promise&lt;DurableObjectStorageHandle&gt;</span>
<ul>
<li>Returns SQL storage access for a Durable Object instance.</li>
</ul>
</li>
<li><code>introspectWorkflow(bindingName)</code> <span class="nb-type">Promise&lt;WorkflowIntrospector&gt;</span>
<ul>
<li>Creates an introspector for Workflow instances created after this method is called.</li>
</ul>
</li>
<li><code>introspectWorkflowInstance(bindingName, instanceId)</code> <span class="nb-type">Promise&lt;WorkflowInstanceIntrospector&gt;</span>
<ul>
<li>Creates an introspector for a specific Workflow instance.</li>
</ul>
</li>
</ul>
<h3 id="usage">Usage</h3>
<p>This example uses the Node.js built-in test runner:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16011.md")
</div>
<h2 id="experimental-generatetypes"><code>experimental_generateTypes</code></h2>
<p>Generate TypeScript type definitions from your Worker configuration. This API uses the same core logic as the <code>wrangler types</code> CLI command, so outputs stay aligned between the CLI and programmatic API.</p>
<p>Unlike the CLI command, <code>experimental_generateTypes</code> does not write to disk automatically. Instead, it returns the generated type content as structured strings for you to handle as needed.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16007.md")
</aside>
<h3 id="syntax-1">Syntax</h3>
<pre tabindex="0"><code class="language-ts">import { experimental_generateTypes } from &quot;wrangler&quot;;&#10;&#10;const result = await experimental_generateTypes(options);&#10;</code></pre>
<h3 id="parameters-1">Parameters</h3>
<ul>
<li>
<p><code>options</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p>Optional options object mirroring the <code>wrangler types</code> CLI flags:</p>
<ul>
<li>
<p><code>config</code> <code>string | string[]</code></p>
<p>Path to the Wrangler configuration file to use. Can be an array for multi-config type resolution.</p>
</li>
<li>
<p><code>env</code> <code>string</code></p>
<p>Name of the Wrangler environment to generate types for.</p>
</li>
<li>
<p><code>envFile</code> <code>string[]</code></p>
<p>Paths to <code>.env</code> files to load when inferring local variables and secrets.</p>
</li>
<li>
<p><code>envInterface</code> <code>string</code></p>
<p>Name of the generated environment interface. Defaults to <code>Env</code>.</p>
</li>
<li>
<p><code>includeEnv</code> <code>boolean</code></p>
<p>Whether to include environment and bindings types in the output. Defaults to <code>true</code>.</p>
</li>
<li>
<p><code>includeRuntime</code> <code>boolean</code></p>
<p>Whether to include runtime types in the output. Defaults to <code>true</code>.</p>
</li>
<li>
<p><code>path</code> <code>string</code></p>
<p>Path to the declaration file for generated types. Defaults to <code>worker-configuration.d.ts</code>.</p>
</li>
<li>
<p><code>strictVars</code> <code>boolean</code></p>
<p>Whether to generate strict literal and union types for variables. Defaults to <code>true</code>.</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="return-type-1">Return Type</h3>
<p><code>experimental_generateTypes()</code> returns a <code>Promise</code> resolving to an object containing the following fields:</p>
<ul>
<li>
<p><code>content</code> <code>string</code></p>
<ul>
<li>Combined formatted output containing all generated sections, including headers and both env and runtime types.</li>
</ul>
</li>
<li>
<p><code>env</code> <code>string | null</code></p>
<ul>
<li>Generated environment and bindings types, or <code>null</code> when env types are excluded.</li>
</ul>
</li>
<li>
<p><code>path</code> <code>string</code></p>
<ul>
<li>Target declaration file path associated with this generation run.</li>
</ul>
</li>
<li>
<p><code>runtime</code> <code>string | null</code></p>
<ul>
<li>Generated runtime types, or <code>null</code> when runtime types are excluded.</li>
</ul>
</li>
</ul>
<h3 id="usage-1">Usage</h3>
<p>You can use <code>experimental_generateTypes</code> to generate types programmatically and write them to disk yourself, or pass them to other tools:</p>
<pre tabindex="0"><code class="language-ts">import { experimental_generateTypes } from &quot;wrangler&quot;;&#10;import * as fs from &quot;node:fs&quot;;&#10;&#10;const result = await experimental_generateTypes({&#10;	config: &quot;wrangler.json&quot;,&#10;	includeRuntime: true,&#10;	includeEnv: true,&#10;});&#10;&#10;// Write the combined content to the path specified in options&#10;fs.writeFileSync(result.path, result.content, &quot;utf-8&quot;);&#10;</code></pre>
<p>To generate only env types without runtime types:</p>
<pre tabindex="0"><code class="language-ts">const result = await experimental_generateTypes({&#10;	includeRuntime: false,&#10;});&#10;</code></pre>
<p>To generate types for a specific environment with a custom interface name:</p>
<pre tabindex="0"><code class="language-ts">const result = await experimental_generateTypes({&#10;	env: &quot;staging&quot;,&#10;	envInterface: &quot;StagingEnv&quot;,&#10;	path: &quot;./types/staging.d.ts&quot;,&#10;});&#10;</code></pre>
<h2 id="unstable-startworker"><code>unstable_startWorker</code></h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16006.md")
</aside>
<p>This API exposes the internals of Wrangler's dev server, and allows you to customise how it runs. For example, you could use <code>unstable_startWorker()</code> to run integration tests against your Worker. This example uses <code>node:test</code>, but should apply to any testing framework:</p>
<pre tabindex="0"><code class="language-js">import assert from &quot;node:assert&quot;;&#10;import test, { after, before, describe } from &quot;node:test&quot;;&#10;import { unstable_startWorker } from &quot;wrangler&quot;;&#10;&#10;describe(&quot;worker&quot;, () =&gt; {&#10;	let worker;&#10;&#10;	before(async () =&gt; {&#10;		worker = await unstable_startWorker({ config: &quot;wrangler.json&quot; });&#10;	});&#10;&#10;	test(&quot;hello world&quot;, async () =&gt; {&#10;		assert.strictEqual(&#10;			await (await worker.fetch(&quot;http://example.com&quot;)).text(),&#10;			&quot;Hello world&quot;,&#10;		);&#10;	});&#10;&#10;	after(async () =&gt; {&#10;		await worker.dispose();&#10;	});&#10;});&#10;</code></pre>
<h2 id="unstable-dev"><code>unstable_dev</code></h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16005.md")
</aside>
<p>Start an HTTP server for testing your Worker.</p>
<p>Once called, <code>unstable_dev</code> will return a <code>fetch()</code> function for invoking your Worker without needing to know the address or port, as well as a <code>stop()</code> function to shut down the HTTP server.</p>
<p>By default, <code>unstable_dev</code> will perform integration tests against a local server. If you wish to perform an e2e test against a preview Worker, pass <code>local: false</code> in the <code>options</code> object when calling the <code>unstable_dev()</code> function. Note that e2e tests can be significantly slower than integration tests.</p>
<h3 id="constructor">Constructor</h3>
<pre tabindex="0"><code class="language-js">const worker = await unstable_dev(script, options);&#10;</code></pre>
<h3 id="parameters-2">Parameters</h3>
<ul>
<li>
<p><code>script</code> <span class="nb-type">string</span></p>
<ul>
<li>A string containing a path to your Worker script, relative to your Worker project's root directory.</li>
</ul>
</li>
<li>
<p><code>options</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Optional options object containing <code>wrangler dev</code> configuration settings.</li>
<li>Include an <code>experimental</code> object inside <code>options</code> to access experimental features such as <code>disableExperimentalWarning</code>.
<ul>
<li>Set <code>disableExperimentalWarning</code> to <code>true</code> to disable Wrangler's warning about using <code>unstable_</code> prefixed APIs.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="return-type-2">Return Type</h3>
<p><code>unstable_dev()</code> returns an object containing the following methods:</p>
<ul>
<li>
<p><code>fetch()</code> <code>Promise&lt;Response&gt;</code></p>
<ul>
<li>Send a request to your Worker. Returns a Promise that resolves with a <a href="/workers/runtime-apis/response"><code>Response</code></a> object.</li>
<li>Refer to <a href="/workers/runtime-apis/fetch/"><code>Fetch</code></a>.</li>
</ul>
</li>
<li>
<p><code>stop()</code> <code>Promise&lt;void&gt;</code></p>
<ul>
<li>Shuts down the dev server.</li>
</ul>
</li>
</ul>
<h3 id="usage-2">Usage</h3>
<p>When initiating each test suite, use a <code>beforeAll()</code> function to start <code>unstable_dev()</code>. The <code>beforeAll()</code> function is used to minimize overhead: starting the dev server takes a few hundred milliseconds, starting and stopping for each individual test adds up quickly, slowing your tests down.</p>
<p>In each test case, call <code>await worker.fetch()</code>, and check that the response is what you expect.</p>
<p>To wrap up a test suite, call <code>await worker.stop()</code> in an <code>afterAll</code> function.</p>
<h4 id="single-worker-example">Single Worker example</h4>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16014.md")
</div></div>
<h4 id="multi-worker-example">Multi-Worker example</h4>
<p>You can test Workers that call other Workers. In the below example, we refer to the Worker that calls other Workers as the parent Worker, and the Worker being called as a child Worker.</p>
<p>If you shut down the child Worker prematurely, the parent Worker will not know the child Worker exists and your tests will fail.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16017.md")
</div></div>
<h2 id="getplatformproxy"><code>getPlatformProxy</code></h2>
<p>The <code>getPlatformProxy</code> function provides a way to obtain an object containing proxies (to <strong>local</strong> <code>workerd</code> bindings) and emulations of Cloudflare Workers specific values, allowing the emulation of such in a Node.js process.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16004.md")
</aside>
<p>One general use case for getting a platform proxy is for emulating bindings in applications targeting Workers, but running outside the Workers runtime (for example, framework local development servers running in Node.js), or for testing purposes (for example, ensuring code properly interacts with a type of binding).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16003.md")
</aside>
<h3 id="syntax-2">Syntax</h3>
<pre tabindex="0"><code class="language-js">const platform = await getPlatformProxy(options);&#10;</code></pre>
<h3 id="parameters-3">Parameters</h3>
<ul>
<li><code>options</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Optional options object containing preferences for the bindings:
<ul>
<li>
<p><code>environment</code> string</p>
<p>The environment to use.</p>
</li>
<li>
<p><code>configPath</code> string</p>
<p>The path to the config file to use.</p>
<p>If no path is specified, the default behavior is to search from the current directory up the filesystem for a <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to use.</p>
<p><strong>Note:</strong> this field is optional but if a path is specified it must point to a valid file on the filesystem.</p>
</li>
<li>
<p><code>persist</code> boolean | <code>{ path: string }</code></p>
<p>Indicates if and where to persist the bindings data. If <code>true</code> or <code>undefined</code>, defaults to the same location used by Wrangler, so data can be shared between it and the caller. If <code>false</code>, no data is persisted to or read from the filesystem.</p>
<p><strong>Note:</strong> If you use <code>wrangler</code>'s <code>--persist-to</code> option, note that this option adds a subdirectory called <code>v3</code> under the hood while <code>getPlatformProxy</code>'s <code>persist</code> does not. For example, if you run <code>wrangler dev --persist-to ./my-directory</code>, to reuse the same location using <code>getPlatformProxy</code>, you will have to specify: <code>persist: { path: &quot;./my-directory/v3&quot; }</code>.</p>
</li>
<li>
<p><code>remoteBindings</code> boolean <span class="nb-metainfo">optional (default: <code>true</code>)</span></p>
<p>Whether or not <a href="/workers/local-development/#remote-bindings">remote bindings</a> should be enabled.</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="return-type-3">Return Type</h3>
<p><code>getPlatformProxy()</code> returns a <code>Promise</code> resolving to an object containing the following fields.</p>
<ul>
<li>
<p><code>env</code> <code>Record&lt;string, unknown&gt;</code></p>
<ul>
<li>Object containing proxies to bindings that can be used in the same way as production bindings. This matches the shape of the <code>env</code> object passed as the second argument to modules-format workers. These proxy to binding implementations run inside <code>workerd</code>.</li>
<li>TypeScript Tip: <code>getPlatformProxy&lt;Env&gt;()</code> is a generic function. You can pass the shape of the bindings record as a type argument to get proper types without <code>unknown</code> values.</li>
</ul>
</li>
<li>
<p><code>cf</code> IncomingRequestCfProperties read-only</p>
<ul>
<li>Mock of the <code>Request</code>'s <code>cf</code> property, containing data similar to what you would see in production.</li>
</ul>
</li>
<li>
<p><code>ctx</code> object</p>
<ul>
<li>Mock object containing implementations of the <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil</code></a> and <a href="/workers/runtime-apis/context/#passthroughonexception"><code>passThroughOnException</code></a> functions that do nothing.</li>
</ul>
</li>
<li>
<p><code>caches</code> object</p>
<ul>
<li>Emulation of the <a href="/workers/runtime-apis/cache/">Workers <code>caches</code> runtime API</a>.</li>
<li>For the time being, all cache operations do nothing. A more accurate emulation will be made available soon.</li>
</ul>
</li>
<li>
<p><code>dispose()</code> () =&gt; <code>Promise&lt;void&gt;</code></p>
<ul>
<li>Terminates the underlying <code>workerd</code> process.</li>
<li>Call this after the platform proxy is no longer required by the program. If you are running a long running process (such as a dev server) that can indefinitely make use of the proxy, you do not need to call this function.</li>
</ul>
</li>
</ul>
<h3 id="usage-3">Usage</h3>
<p>The <code>getPlatformProxy</code> function uses bindings found in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>. For example, if you have an <a href="/workers/configuration/environment-variables/#add-environment-variables-via-wrangler">environment variable</a> configuration set up in the Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16018.md")
</div>
<p>You can access the bindings by importing <code>getPlatformProxy</code> like this:</p>
<pre tabindex="0"><code class="language-js">import { getPlatformProxy } from &quot;wrangler&quot;;&#10;&#10;const { env } = await getPlatformProxy();&#10;</code></pre>
<p>To access the value of the <code>MY_VARIABLE</code> binding add the following to your code:</p>
<pre tabindex="0"><code class="language-js">console.log(`MY_VARIABLE = ${env.MY_VARIABLE}`);&#10;</code></pre>
<p>This will print the following output: <code>MY_VARIABLE = test</code>.</p>
<h3 id="supported-bindings">Supported bindings</h3>
<p>All supported bindings found in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> are available to you via <code>env</code>.</p>
<p>The bindings supported by <code>getPlatformProxy</code> are:</p>
<ul>
<li>
<p><a href="/workers/configuration/environment-variables/">Environment variables</a></p>
</li>
<li>
<p><a href="/workers/runtime-apis/bindings/service-bindings/">Service bindings</a></p>
</li>
<li>
<p><a href="/kv/api/">KV namespace bindings</a></p>
</li>
<li>
<p><a href="/r2/api/workers/workers-api-reference/">R2 bucket bindings</a></p>
</li>
<li>
<p><a href="/queues/configuration/javascript-apis/">Queue bindings</a></p>
</li>
<li>
<p><a href="/d1/worker-api/">D1 database bindings</a></p>
</li>
<li>
<p><a href="/hyperdrive">Hyperdrive bindings</a></p>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="hyperdrive-values-are-simple-passthrough-ones">Hyperdrive values are simple passthrough ones</h3>
@markup("md", "content/.markup/bodies/16002.md")
</aside>
<ul>
<li><a href="/workers-ai/get-started/workers-wrangler/#2-connect-your-worker-to-workers-ai">Workers AI bindings</a></li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-ai-local-development-usage-charges">Workers AI local development usage charges</h3>
@markup("md", "content/.markup/bodies/16001.md")
</aside>
<ul>
<li><a href="/durable-objects/api/">Durable Object bindings</a>
<ul>
<li>
<p>To use a Durable Object binding with <code>getPlatformProxy</code>, always specify a <a href="/workers/wrangler/configuration/#durable-objects"><code>script_name</code></a>.</p>
<p>For example, you might have the following binding in a Wrangler configuration file read by <code>getPlatformProxy</code>.</p>
</li>
</ul>
</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16019.md")
</div>
<pre tabindex="0"><code>You will need to declare your Durable Object `&quot;MyDurableObject&quot;` in another Worker, called `external-do-worker` in this example.&#10;</code></pre>
<pre tabindex="0"><code class="language-ts">export class MyDurableObject extends DurableObject {&#10;	// Your DO code goes here&#10;}&#10;&#10;export default {&#10;	fetch() {&#10;		// Doesn&#x27;t have to do anything, but a DO cannot be the default export&#10;		return new Response(&quot;Hello, world!&quot;);&#10;	},&#10;};&#10;</code></pre>
<pre tabindex="0"><code>That Worker also needs a Wrangler configuration file that looks like this:&#10;</code></pre>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16020.md")
</div>
<pre tabindex="0"><code>If you are not using RPC with your Durable Object, you can run a separate Wrangler dev session alongside your framework development server.&#10;&#10;Otherwise, you can build your application and run both Workers in the same Wrangler dev session.&#10;&#10;If you are using Pages run:&#10;</code></pre>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler pages dev -c path/to/pages/wrangler.jsonc -c path/to/external-do-worker/wrangler.jsonc</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler pages dev -c path/to/pages/wrangler.jsonc -c path/to/external-do-worker/wrangler.jsonc" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler pages dev -c path/to/pages/wrangler.jsonc -c path/to/external-do-worker/wrangler.jsonc</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler pages dev -c path/to/pages/wrangler.jsonc -c path/to/external-do-worker/wrangler.jsonc" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler pages dev -c path/to/pages/wrangler.jsonc -c path/to/external-do-worker/wrangler.jsonc</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler pages dev -c path/to/pages/wrangler.jsonc -c path/to/external-do-worker/wrangler.jsonc" aria-label="Copy to clipboard">Copy</button></div></div>
<pre tabindex="0"><code>If you are using Workers with Assets run:&#10;</code></pre>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler dev -c path/to/workers-assets/wrangler.jsonc -c path/to/external-do-worker/wrangler.jsonc</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler dev -c path/to/workers-assets/wrangler.jsonc -c path/to/external-do-worker/wrangler.jsonc" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler dev -c path/to/workers-assets/wrangler.jsonc -c path/to/external-do-worker/wrangler.jsonc</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler dev -c path/to/workers-assets/wrangler.jsonc -c path/to/external-do-worker/wrangler.jsonc" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler dev -c path/to/workers-assets/wrangler.jsonc -c path/to/external-do-worker/wrangler.jsonc</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler dev -c path/to/workers-assets/wrangler.jsonc -c path/to/external-do-worker/wrangler.jsonc" aria-label="Copy to clipboard">Copy</button></div></div>
