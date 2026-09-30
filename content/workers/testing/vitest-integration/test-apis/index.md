---
cp9:
  canonical: https://developers.cloudflare.com/workers/testing/vitest-integration/test-apis/
  description: Runtime helpers for writing tests, exported from `cloudflare:workers` and `cloudflare:test`.
  full_title: Test APIs · Cloudflare Workers docs
  head_html: <title>Test APIs · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Runtime helpers for writing tests, exported from `cloudflare:workers` and `cloudflare:test`."><link rel="canonical" href="https://developers.cloudflare.com/workers/testing/vitest-integration/test-apis/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/testing/vitest-integration/test-apis/index.md"><meta property="og:title" content="Test APIs · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Runtime helpers for writing tests, exported from `cloudflare:workers` and `cloudflare:test`."><meta property="og:url" content="https://developers.cloudflare.com/workers/testing/vitest-integration/test-apis/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/testing/vitest-integration/test-apis/#page","headline":"Test APIs \u00b7 Cloudflare Workers docs","description":"Runtime helpers for writing tests, exported from cloudflare:workers and cloudflare:test.","url":"https://developers.cloudflare.com/workers/testing/vitest-integration/test-apis/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/testing/vitest-integration/test-apis/
  schema: 1
---
<p>The Workers Vitest integration provides runtime helpers for writing tests. Some helpers are exported from the <code>cloudflare:workers</code> module, and others from the <code>cloudflare:test</code> module. Both modules are provided by the <code>@cloudflare/vitest-plugin</code> package, but can only be imported from test files that execute in the Workers runtime.</p>
<h2 id="cloudflare-workers-exports"><code>cloudflare:workers</code> exports</h2>
<ul>
<li>
<p><code>env</code>: import(&quot;cloudflare:workers&quot;).ProvidedEnv</p>
<ul>
<li>Exposes the <a href="/workers/runtime-apis/handlers/fetch/#parameters"><code>env</code> object</a> for use as the second argument passed to ES modules format exported handlers. This provides access to <a href="/workers/runtime-apis/bindings/">bindings</a> that you have defined in your <a href="/workers/testing/vitest-integration/configuration/">Vitest configuration file</a>.</li>
</ul>
</li>
</ul>
<br/>
<pre tabindex="0"><code class="language-js">import { env } from &quot;cloudflare:workers&quot;;&#10;&#10;it(&quot;uses binding&quot;, async () =&gt; {&#10;  await env.KV_NAMESPACE.put(&quot;key&quot;, &quot;value&quot;);&#10;  expect(await env.KV_NAMESPACE.get(&quot;key&quot;)).toBe(&quot;value&quot;);&#10;});&#10;</code></pre>
<pre tabindex="0"><code>To configure the type of this value, use an ambient module type:&#10;</code></pre>
<pre tabindex="0"><code class="language-ts">declare module &quot;cloudflare:workers&quot; {&#10;  interface ProvidedEnv {&#10;    KV_NAMESPACE: KVNamespace;&#10;  }&#10;  // ...or if you have an existing `Env` type...&#10;  interface ProvidedEnv extends Env {}&#10;}&#10;</code></pre>
<ul>
<li>
<p><code>exports</code>: object</p>
<ul>
<li>Provides access to the exports of the <code>main</code> Worker. Use <code>exports.default.fetch()</code> to write integration tests against your Worker's default export handler. The <code>main</code> Worker runs in the same isolate/context as tests so any global mocks will apply to it too. Unlike the previous <code>SELF</code> binding, <code>exports</code> does not expose Assets. To test assets, use <a href="/workers/testing/unstable_startworker/"><code>startDevWorker()</code></a>.</li>
</ul>
</li>
</ul>
<br/>
<pre tabindex="0"><code class="language-js">import { exports } from &quot;cloudflare:workers&quot;;&#10;&#10;it(&quot;dispatches fetch event&quot;, async () =&gt; {&#10;  const response = await exports.default.fetch(&quot;https://example.com&quot;);&#10;  expect(await response.text()).toMatchInlineSnapshot(...);&#10;});&#10;</code></pre>
<h2 id="cloudflare-test-exports"><code>cloudflare:test</code> exports</h2>
<h3 id="events">Events</h3>
<ul>
<li>
<p><code>createExecutionContext()</code>: ExecutionContext</p>
<ul>
<li>Creates an instance of the <a href="/workers/runtime-apis/handlers/fetch/#parameters"><code>context</code> object</a> for use as the third argument to ES modules format exported handlers.</li>
</ul>
</li>
<li>
<p><code>waitOnExecutionContext(ctx:ExecutionContext)</code>: Promise&lt;void&gt;</p>
<ul>
<li>Use this to wait for all Promises passed to <code>ctx.waitUntil()</code> to settle, before running test assertions on any side effects. Only accepts instances of <code>ExecutionContext</code> returned by <code>createExecutionContext()</code>.</li>
</ul>
</li>
</ul>
<br/>
<pre tabindex="0"><code class="language-ts">import { env } from &quot;cloudflare:workers&quot;;&#10;import { createExecutionContext, waitOnExecutionContext } from &quot;cloudflare:test&quot;;&#10;import { it, expect } from &quot;vitest&quot;;&#10;import worker from &quot;./index.mjs&quot;;&#10;&#10;it(&quot;calls fetch handler&quot;, async () =&gt; {&#10;  const request = new Request(&quot;https://example.com&quot;);&#10;  const ctx = createExecutionContext();&#10;  const response = await worker.fetch(request, env, ctx);&#10;  await waitOnExecutionContext(ctx);&#10;  expect(await response.text()).toMatchInlineSnapshot(...);&#10;});&#10;</code></pre>
<ul>
<li>
<p><code>createScheduledController(options?:FetcherScheduledOptions)</code>: ScheduledController</p>
<ul>
<li>Creates an instance of <code>ScheduledController</code> for use as the first argument to modules-format <a href="/workers/runtime-apis/handlers/scheduled/"><code>scheduled()</code></a> exported handlers.</li>
</ul>
</li>
</ul>
<br/>
<pre tabindex="0"><code class="language-ts">import { env } from &quot;cloudflare:workers&quot;;&#10;import { createScheduledController, createExecutionContext, waitOnExecutionContext } from &quot;cloudflare:test&quot;;&#10;import { it, expect } from &quot;vitest&quot;;&#10;import worker from &quot;./index.mjs&quot;;&#10;&#10;it(&quot;calls scheduled handler&quot;, async () =&gt; {&#10;  const ctrl = createScheduledController({&#10;    scheduledTime: new Date(1000),&#10;    cron: &quot;30 * * * *&quot;&#10;  });&#10;  const ctx = createExecutionContext();&#10;  await worker.scheduled(ctrl, env, ctx);&#10;  await waitOnExecutionContext(ctx);&#10;});&#10;</code></pre>
<ul>
<li>
<p><code>createMessageBatch(queueName:string, messages:ServiceBindingQueueMessage[])</code>: MessageBatch</p>
<ul>
<li>Creates an instance of <code>MessageBatch</code> for use as the first argument to modules-format <a href="/queues/configuration/javascript-apis/#consumer"><code>queue()</code></a> exported handlers.</li>
</ul>
</li>
<li>
<p><code>getQueueResult(batch:MessageBatch, ctx:ExecutionContext)</code>: Promise&lt;FetcherQueueResult&gt;</p>
<ul>
<li>Gets the acknowledged/retry state of messages in the <code>MessageBatch</code>, and waits for all <code>ExecutionContext#waitUntil()</code>ed <code>Promise</code>s to settle. Only accepts instances of <code>MessageBatch</code> returned by <code>createMessageBatch()</code>, and instances of <code>ExecutionContext</code> returned by <code>createExecutionContext()</code>.</li>
</ul>
</li>
</ul>
<br/>
<pre tabindex="0"><code class="language-ts">import { env } from &quot;cloudflare:workers&quot;;&#10;import { createMessageBatch, createExecutionContext, getQueueResult } from &quot;cloudflare:test&quot;;&#10;import { it, expect } from &quot;vitest&quot;;&#10;import worker from &quot;./index.mjs&quot;;&#10;&#10;it(&quot;calls queue handler&quot;, async () =&gt; {&#10;  const batch = createMessageBatch(&quot;my-queue&quot;, [&#10;    {&#10;      id: &quot;message-1&quot;,&#10;      timestamp: new Date(1000),&#10;      body: &quot;body-1&quot;&#10;    }&#10;  ]);&#10;  const ctx = createExecutionContext();&#10;  await worker.queue(batch, env, ctx);&#10;  const result = await getQueueResult(batch, ctx);&#10;  expect(result.ackAll).toBe(false);&#10;  expect(result.retryBatch).toMatchObject({ retry: false });&#10;  expect(result.explicitAcks).toStrictEqual([&quot;message-1&quot;]);&#10;  expect(result.retryMessages).toStrictEqual([]);&#10;});&#10;</code></pre>
<h3 id="durable-objects">Durable Objects</h3>
<ul>
<li>
<p><code>runInDurableObject&lt;O extends DurableObject, R&gt;(stub:DurableObjectStub, callback:(instance: O, state: DurableObjectState) =&gt; R | Promise&lt;R&gt;)</code>: Promise&lt;R&gt;</p>
<ul>
<li>Runs the provided <code>callback</code> inside the Durable Object that corresponds to the provided <code>stub</code>.</li>
</ul>
</li>
</ul>
<br/>
<pre tabindex="0"><code>This temporarily replaces your Durable Object's `fetch()` handler with `callback`, then sends a request to it, returning the result. This can be used to call/spy-on Durable Object methods or seed/get persisted data. Note this can only be used with `stub`s pointing to Durable Objects defined in the `main` Worker.&#10;</code></pre>
<br/>
<pre tabindex="0"><code class="language-ts">export class Counter {&#10;  constructor(readonly state: DurableObjectState) {}&#10;&#10;  async fetch(request: Request): Promise&lt;Response&gt; {&#10;    let count = (await this.state.storage.get&lt;number&gt;(&quot;count&quot;)) ?? 0;&#10;    void this.state.storage.put(&quot;count&quot;, ++count);&#10;    return new Response(count.toString());&#10;	}&#10;}&#10;</code></pre>
<pre tabindex="0"><code class="language-ts">import { env } from &quot;cloudflare:workers&quot;;&#10;import { runInDurableObject } from &quot;cloudflare:test&quot;;&#10;import { it, expect } from &quot;vitest&quot;;&#10;import { Counter } from &quot;./index.ts&quot;;&#10;&#10;it(&quot;increments count&quot;, async () =&gt; {&#10;  const id = env.COUNTER.newUniqueId();&#10;  const stub = env.COUNTER.get(id);&#10;  let response = await stub.fetch(&quot;https://example.com&quot;);&#10;  expect(await response.text()).toBe(&quot;1&quot;);&#10;&#10;  response = await runInDurableObject(stub, async (instance: Counter, state) =&gt; {&#10;    expect(instance).toBeInstanceOf(Counter);&#10;    expect(await state.storage.get&lt;number&gt;(&quot;count&quot;)).toBe(1);&#10;&#10;    const request = new Request(&quot;https://example.com&quot;);&#10;    return instance.fetch(request);&#10;  });&#10;  expect(await response.text()).toBe(&quot;2&quot;);&#10;});&#10;</code></pre>
<ul>
<li>
<p><code>runDurableObjectAlarm(stub:DurableObjectStub)</code>: Promise&lt;boolean&gt;</p>
<ul>
<li>Immediately runs and removes the Durable Object pointed to by <code>stub</code>'s alarm if one is scheduled. Returns <code>true</code> if an alarm ran, and <code>false</code> otherwise. Note this can only be used with <code>stub</code>s pointing to Durable Objects defined in the <code>main</code> Worker.</li>
</ul>
</li>
<li>
<p><code>evictDurableObject(stub:DurableObjectStub, options?:DurableObjectEvictionOptions)</code>: Promise&lt;void&gt;</p>
<ul>
<li>Evicts the currently-running Durable Object pointed to by <code>stub</code>, tearing down its instance to reset in-memory state. By default, hibernatable WebSockets are hibernated rather than closed, and eviction waits up to 30 seconds for in-flight requests to drain.</li>
</ul>
</li>
</ul>
<br/>
<pre tabindex="0"><code>Useful for testing how a Durable Object behaves across evictions, such as recovering state from storage or resuming hibernated WebSockets.&#10;</code></pre>
<br/>
<pre tabindex="0"><code>Rejects if `stub` is not a Durable Object stub, if the target Durable Object is not currently running, or if its namespace has eviction prevented. Note this can only be used with `stub`s pointing to Durable Objects defined in the `main` Worker.&#10;</code></pre>
<br/>
<pre tabindex="0"><code class="language-ts">import { env } from &quot;cloudflare:workers&quot;;&#10;import { evictDurableObject } from &quot;cloudflare:test&quot;;&#10;import { it, expect } from &quot;vitest&quot;;&#10;&#10;it(&quot;preserves stored data across eviction&quot;, async () =&gt; {&#10;  const id = env.COUNTER.idFromName(&quot;evict-test&quot;);&#10;  const stub = env.COUNTER.get(id);&#10;&#10;  // Each request increments and persists the count to storage&#10;  expect(await (await stub.fetch(&quot;https://example.com&quot;)).text()).toBe(&quot;1&quot;);&#10;  expect(await (await stub.fetch(&quot;https://example.com&quot;)).text()).toBe(&quot;2&quot;);&#10;&#10;  // Evict the Durable Object. The in-memory instance is torn down,&#10;  // but durable storage is preserved.&#10;  await evictDurableObject(stub);&#10;&#10;  // The next request reconstructs the instance and reads the persisted count&#10;  expect(await (await stub.fetch(&quot;https://example.com&quot;)).text()).toBe(&quot;3&quot;);&#10;});&#10;</code></pre>
<ul>
<li>The <code>DurableObjectEvictionOptions</code> interface controls eviction behavior:</li>
</ul>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>webSockets</code></td>
<td><code>&quot;close&quot; | &quot;hibernate&quot;</code></td>
<td><code>&quot;hibernate&quot;</code></td>
<td>Controls what happens to hibernatable WebSockets when evicting a Durable Object. With <code>&quot;hibernate&quot;</code>, WebSockets are hibernated and can resume after eviction. With <code>&quot;close&quot;</code>, WebSockets are closed.</td>
</tr>
</tbody>
</table>
<ul>
<li>
<p><code>listDurableObjectIds(namespace:DurableObjectNamespace)</code>: Promise&lt;DurableObjectId[]&gt;</p>
<ul>
<li>Gets the IDs of all objects that have been created in the <code>namespace</code>. Respects per-file storage isolation, meaning objects created in a different test file will not be returned.</li>
</ul>
</li>
</ul>
<br/>
<pre tabindex="0"><code class="language-ts">import { env } from &quot;cloudflare:workers&quot;;&#10;import { listDurableObjectIds } from &quot;cloudflare:test&quot;;&#10;import { it, expect } from &quot;vitest&quot;;&#10;&#10;it(&quot;increments count&quot;, async () =&gt; {&#10;  const id = env.COUNTER.newUniqueId();&#10;  const stub = env.COUNTER.get(id);&#10;  const response = await stub.fetch(&quot;https://example.com&quot;);&#10;  expect(await response.text()).toBe(&quot;1&quot;);&#10;&#10;  const ids = await listDurableObjectIds(env.COUNTER);&#10;  expect(ids.length).toBe(1);&#10;  expect(ids[0].equals(id)).toBe(true);&#10;});&#10;</code></pre>
<ul>
<li>
<p><code>reset()</code>: Promise&lt;void&gt;</p>
<ul>
<li>Deletes all data from all attached bindings. This is useful for resetting state between test blocks.</li>
</ul>
</li>
</ul>
<br/>
<pre tabindex="0"><code class="language-ts">import { reset } from &quot;cloudflare:test&quot;;&#10;import { afterEach } from &quot;vitest&quot;;&#10;&#10;afterEach(async () =&gt; {&#10;  await reset();&#10;});&#10;</code></pre>
<ul>
<li>
<p><code>abortAllDurableObjects()</code>: Promise&lt;void&gt;</p>
<ul>
<li>Resets all Durable Object instances. Unlike <code>reset()</code>, this does not delete persisted data. This forcibly tears down all running Durable Object instances, discarding in-memory state without waiting for in-flight requests to drain.</li>
</ul>
</li>
</ul>
<br/>
<pre tabindex="0"><code class="language-ts">import { abortAllDurableObjects } from &quot;cloudflare:test&quot;;&#10;import { afterEach } from &quot;vitest&quot;;&#10;&#10;afterEach(async () =&gt; {&#10;  await abortAllDurableObjects();&#10;});&#10;</code></pre>
<ul>
<li>
<p><code>evictAllDurableObjects(options?:DurableObjectEvictionOptions)</code>: Promise&lt;void&gt;</p>
<ul>
<li>Evicts all currently-running Durable Objects in evictable namespaces. Unlike <code>abortAllDurableObjects()</code>, eviction is graceful: hibernatable WebSockets are hibernated rather than closed by default, and eviction waits up to 30 seconds for in-flight requests to drain. In-memory state is reset by tearing down each instance.</li>
</ul>
</li>
</ul>
<br/>
<pre tabindex="0"><code>Non-running or idle Durable Objects are skipped, and namespaces with eviction prevented are respected. Accepts the same [`DurableObjectEvictionOptions`](#durable-objects) as `evictDurableObject()`.&#10;</code></pre>
<br/>
<pre tabindex="0"><code class="language-ts">import { evictAllDurableObjects } from &quot;cloudflare:test&quot;;&#10;import { afterEach } from &quot;vitest&quot;;&#10;&#10;afterEach(async () =&gt; {&#10;  await evictAllDurableObjects();&#10;});&#10;</code></pre>
<h3 id="d1">D1</h3>
<ul>
<li>
<p><code>applyD1Migrations(db:D1Database, migrations:D1Migration[], migrationTableName?:string)</code>: Promise&lt;void&gt;</p>
<ul>
<li>Applies all un-applied <a href="/d1/reference/migrations/">D1 migrations</a> stored in the <code>migrations</code> array to database <code>db</code>, recording migrations state in the <code>migrationsTableName</code> table. <code>migrationsTableName</code> defaults to <code>d1_migrations</code>. Call the <a href="/workers/testing/vitest-integration/configuration/#readd1migrationsmigrationspath"><code>readD1Migrations()</code></a> function from the <code>@cloudflare/vitest-plugin/config</code> package inside Node.js to get the <code>migrations</code> array. Refer to the <a href="https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-plugin-examples/d1">D1 recipe</a> for an example project using migrations.</li>
</ul>
</li>
</ul>
<h3 id="workflows">Workflows</h3>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="workflows-with-storage-isolation">Workflows with storage isolation</h3>
@markup("md", "content/.markup/bodies/17322.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="version">Version</h3>
@markup("md", "content/.markup/bodies/17321.md")
</aside>
<ul>
<li><code>introspectWorkflowInstance(workflow: Workflow, instanceId: string)</code>: Promise&lt;WorkflowInstanceIntrospector&gt;
<ul>
<li>Creates an <strong>introspector</strong> for a specific Workflow instance, used to <strong>modify</strong> its behavior, <strong>await</strong> outcomes, and <strong>clear</strong> its state during tests. This is the primary entry point for testing individual Workflow instances with a known ID.</li>
</ul>
</li>
</ul>
<br/>
<pre tabindex="0"><code class="language-ts">import { env } from &quot;cloudflare:workers&quot;;&#10;import { introspectWorkflowInstance } from &quot;cloudflare:test&quot;;&#10;&#10;it(&quot;should disable all sleeps, mock an event and complete&quot;, async () =&gt; {&#10;  // 1. CONFIGURATION&#10;  await using instance = await introspectWorkflowInstance(env.MY_WORKFLOW, &quot;123456&quot;);&#10;  await instance.modify(async (m) =&gt; {&#10;    await m.disableSleeps();&#10;    await m.mockEvent({&#10;      type: &quot;user-approval&quot;,&#10;      payload: { approved: true, approverId: &quot;user-123&quot; },&#10;    });&#10;  });&#10;&#10;  // 2. EXECUTION&#10;  await env.MY_WORKFLOW.create({ id: &quot;123456&quot; });&#10;&#10;  // 3. ASSERTION&#10;  await expect(instance.waitForStatus(&quot;complete&quot;)).resolves.not.toThrow();&#10;  const output = await instance.getOutput();&#10;  expect(output).toEqual({ success: true });&#10;&#10;  // 4. DISPOSE: is implicit and automatic here.&#10;});&#10;</code></pre>
<pre tabindex="0"><code>* The returned `WorkflowInstanceIntrospector` object has the following methods:&#10;    * `modify(fn: (m: WorkflowInstanceModifier) =&gt; Promise&lt;void&gt;): Promise&lt;void&gt;`: Applies modifications to the Workflow instance's behavior.&#10;    * `waitForStepResult(step: { name: string; index?: number }): Promise&lt;unknown&gt;`: Waits for a specific step to complete and returns a result. If multiple steps share the same name, use the optional `index` property (1-based, defaults to `1`) to target a specific occurrence.&#10;    * `waitForStatus(status: InstanceStatus[&quot;status&quot;]): Promise&lt;void&gt;`: Waits for the Workflow instance to reach a specific [status](/workflows/build/workers-api/#instancestatus) (e.g., 'running', 'complete').&#10;    * `getOutput(): Promise&lt;unknown&gt;`: Returns the output value of the successful completed Workflow instance.&#10;    * `getError(): Promise&lt;{name: string, message: string}&gt;`: Returns the error information of the errored Workflow instance. The error information follows the form `{ name: string; message: string }`.&#10;    * `dispose(): Promise&lt;void&gt;`: Disposes the Workflow instance, which is crucial for test isolation. If this function isn't called and `await using` is not used, isolated storage will fail and the instance's state will persist across subsequent tests. For example, an instance that becomes completed in one test will already be completed at the start of the next.&#10;    * `[Symbol.asyncDispose](): Promise&lt;void&gt;`: Provides automatic dispose. It's invoked by the `await using` statement, which calls `dispose()`.&#10;</code></pre>
<ul>
<li><code>introspectWorkflow(workflow: Workflow)</code>: Promise&lt;WorkflowIntrospector&gt;
<ul>
<li>Creates an <strong>introspector</strong> for a Workflow where instance IDs are unknown beforehand. This allows for defining modifications that will apply to <strong>all subsequently created instances</strong>.</li>
</ul>
</li>
</ul>
<br/>
<pre tabindex="0"><code class="language-ts">import { env, exports } from &quot;cloudflare:workers&quot;;&#10;import { introspectWorkflow } from &quot;cloudflare:test&quot;;&#10;&#10;it(&quot;should disable all sleeps, mock an event and complete&quot;, async () =&gt; {&#10;  // 1. CONFIGURATION&#10;  await using introspector = await introspectWorkflow(env.MY_WORKFLOW);&#10;  await introspector.modifyAll(async (m) =&gt; {&#10;    await m.disableSleeps();&#10;    await m.mockEvent({&#10;      type: &quot;user-approval&quot;,&#10;      payload: { approved: true, approverId: &quot;user-123&quot; },&#10;    });&#10;  });&#10;&#10;  // 2. EXECUTION&#10;  await env.MY_WORKFLOW.create();&#10;&#10;  // 3. ASSERTION&#10;  const instances = introspector.get();&#10;  for(const instance of instances) {&#10;    await expect(instance.waitForStatus(&quot;complete&quot;)).resolves.not.toThrow();&#10;    const output = await instance.getOutput();&#10;    expect(output).toEqual({ success: true });&#10;  }&#10;&#10;  // 4. DISPOSE: is implicit and automatic here.&#10;});&#10;</code></pre>
<pre tabindex="0"><code>  The workflow instance doesn't have to be created directly inside the test. The introspector will capture **all** instances created after it is initialized. For example, you could trigger the creation of **one or multiple** instances via a single `fetch` event to your Worker:&#10;</code></pre>
<pre tabindex="0"><code class="language-js">// This also works for the EXECUTION phase:&#10;await exports.default.fetch(&quot;https://example.com/trigger-workflows&quot;);&#10;</code></pre>
<pre tabindex="0"><code>* The returned `WorkflowIntrospector` object has the following methods:&#10;    * `modifyAll(fn: (m: WorkflowInstanceModifier) =&gt; Promise&lt;void&gt;): Promise&lt;void&gt;`: Applies modifications to all Workflow instances created after calling `introspectWorkflow`.&#10;    * `get(): Promise&lt;WorkflowInstanceIntrospector[]&gt;`: Returns all `WorkflowInstanceIntrospector` objects from instances created after `introspectWorkflow` was called.&#10;    * `dispose(): Promise&lt;void&gt;`: Disposes the Workflow introspector. All `WorkflowInstanceIntrospector` from created instances will also be disposed. This is crucial to prevent modifications and captured instances from leaking between tests. After calling this method, the `WorkflowIntrospector` should not be reused.&#10;    * `[Symbol.asyncDispose](): Promise&lt;void&gt;`: Provides automatic dispose. It's invoked by the `await using` statement, which calls `dispose()`. &#10;</code></pre>
<ul>
<li><code>WorkflowInstanceModifier</code>
<ul>
<li>This object is provided to the <code>modify</code> and <code>modifyAll</code> callbacks to mock or alter the behavior of a Workflow instance's steps, events, and sleeps.
<ul>
<li><code>disableSleeps(steps?: { name: string; index?: number }[])</code>: Disables sleeps, causing <code>step.sleep()</code> and <code>step.sleepUntil()</code> to resolve immediately. If <code>steps</code> is omitted, all sleeps are disabled.</li>
<li><code>disableRetryDelays(steps?: { name: string; index?: number }[])</code>: Disables retry backoff delays, causing retry attempts of a failing <code>step.do()</code> to execute immediately without waiting. The retries still happen — only the delay between them is removed. If <code>steps</code> is omitted, all retry delays are disabled.</li>
<li><code>mockStepResult(step: { name: string; index?: number }, stepResult: unknown)</code>: Mocks the result of a <code>step.do()</code>, causing it to return the specified value instantly without executing the step's implementation.</li>
<li><code>mockStepError(step: { name: string; index?: number }, error: Error, times?: number)</code>: Forces a <code>step.do()</code> to throw an error, simulating a failure. <code>times</code> is an optional number that sets how many times the step should error. If <code>times</code> is omitted, the step will error on every attempt, making the Workflow instance fail.</li>
<li><code>forceStepTimeout(step: { name: string; index?: number }, times?: number)</code>: Forces a <code>step.do()</code> to fail by timing out immediately. <code>times</code> is an optional number that sets how many times the step should timeout. If <code>times</code> is omitted, the step will timeout on every attempt, making the Workflow instance fail.</li>
<li><code>mockEvent(event: { type: string; payload: unknown })</code>: Sends a mock event to the Workflow instance, causing a <code>step.waitForEvent()</code> to resolve with the provided payload. <code>type</code> must match the <code>waitForEvent</code> type.</li>
<li><code>forceEventTimeout(step: { name: string; index?: number })</code>: Forces a <code>step.waitForEvent()</code> to time out instantly, causing the step to fail.</li>
</ul>
</li>
</ul>
</li>
</ul>
<br/>
<pre tabindex="0"><code class="language-ts">import { env } from &quot;cloudflare:workers&quot;;&#10;import { introspectWorkflowInstance } from &quot;cloudflare:test&quot;;&#10;<p>// This example showcases explicit disposal&#10;it(&quot;should apply all modifier functions&quot;, async () =&gt; {&#10;// 1. CONFIGURATION&#10;const instance = await introspectWorkflowInstance(env.COMPLEX_WORKFLOW, &quot;123456&quot;);</p>&#10;<p>try {&#10;// Modify instance behavior&#10;await instance.modify(async (m) =&gt; {&#10;// Disables all sleeps to make the test run instantly&#10;await m.disableSleeps();</p>&#10;<pre tabindex="0"><code>  // Disables retry backoff delays so retries execute without waiting&#10;  await m.disableRetryDelays();&#10;&#10;  // Mocks the successful result of a data-fetching step&#10;  await m.mockStepResult(&#10;    { name: &amp;quot;get-order-details&amp;quot; },&#10;    { orderId: &amp;quot;abc-123&amp;quot;, amount: 99.99 }&#10;  );&#10;&#10;  // Mocks an incoming event to satisfy a `step.waitForEvent()`&#10;  await m.mockEvent({&#10;    type: &amp;quot;user-approval&amp;quot;,&#10;    payload: { approved: true, approverId: &amp;quot;user-123&amp;quot; },&#10;  });&#10;&#10;  // Forces a step to fail once with a specific error to test retry logic&#10;  await m.mockStepError(&#10;    { name: &amp;quot;process-payment&amp;quot; },&#10;    new Error(&amp;quot;Payment gateway timeout&amp;quot;),&#10;    1 // Fail only the first time&#10;  );&#10;&#10;  // Forces a `step.do()` to time out immediately&#10;  await m.forceStepTimeout({ name: &amp;quot;notify-shipping-partner&amp;quot; });&#10;&#10;  // Forces a `step.waitForEvent()` to time out&#10;  await m.forceEventTimeout({ name: &amp;quot;wait-for-fraud-check&amp;quot; });&#10;});&#10;&#10;// 2. EXECUTION&#10;await env.COMPLEX_WORKFLOW.create({ id: &amp;quot;123456&amp;quot; });&#10;&#10;// 3. ASSERTION&#10;expect(await instance.waitForStepResult({ name: &amp;quot;get-order-details&amp;quot; })).toEqual({&#10;  orderId: &amp;quot;abc-123&amp;quot;,&#10;  amount: 99.99,&#10;});&#10;// Given the forced timeouts, the workflow will end in an errored state&#10;await expect(instance.waitForStatus(&amp;quot;errored&amp;quot;)).resolves.not.toThrow();&#10;&#10;const error = await instance.getError();&#10;expect(error.name).toEqual(&amp;quot;Error&amp;quot;);&#10;expect(error.message).toContain(&amp;quot;Execution timed out&amp;quot;);&#10;</code></pre>
<p>} catch {
// 4. DISPOSE
await instance.dispose();
}
});
</code></pre></p>
<pre tabindex="0"><code>  When targeting a step, use its `name`. If multiple steps share the same name, use the optional `index` property (1-based, defaults to `1`) to specify the occurrence.&#10;</code></pre>
