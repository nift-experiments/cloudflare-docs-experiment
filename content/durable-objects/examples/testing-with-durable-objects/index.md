---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/examples/testing-with-durable-objects/
  description: Write tests for Durable Objects using the Workers Vitest integration.
  full_title: Testing Durable Objects · Cloudflare Durable Objects docs
  head_html: <title>Testing Durable Objects · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="Write tests for Durable Objects using the Workers Vitest integration."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/examples/testing-with-durable-objects/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/examples/testing-with-durable-objects/index.md"><meta property="og:title" content="Testing Durable Objects · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Write tests for Durable Objects using the Workers Vitest integration."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/examples/testing-with-durable-objects/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/examples/testing-with-durable-objects/#page","headline":"Testing Durable Objects \u00b7 Cloudflare Durable Objects docs","description":"Write tests for Durable Objects using the Workers Vitest integration.","url":"https://developers.cloudflare.com/durable-objects/examples/testing-with-durable-objects/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/examples/testing-with-durable-objects/
  schema: 1
---
<p class="article-summary">Write tests for Durable Objects using the Workers Vitest integration.</p>
<p>Use the <a href="https://www.npmjs.com/package/@cloudflare/vitest-plugin"><code>@cloudflare/vitest-plugin</code></a> package to write tests for your Durable Objects. This integration runs your tests inside the Workers runtime, giving you direct access to Durable Object bindings and APIs.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Install Vitest and the Workers Vitest integration as dev dependencies:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8197.md")
</div></div>
<h2 id="example-durable-object">Example Durable Object</h2>
<p>This example tests a simple counter Durable Object with SQLite storage:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8198.md")
</div>
<h2 id="configure-vitest">Configure Vitest</h2>
<p>Create a <code>vitest.config.ts</code> file that uses the <code>cloudflareTest()</code> plugin:</p>
<pre tabindex="0"><code class="language-ts">import { cloudflareTest } from &quot;@cloudflare/vitest-plugin&quot;;&#10;import { defineConfig } from &quot;vitest/config&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflareTest({&#10;			wrangler: { configPath: &quot;./wrangler.jsonc&quot; },&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p>Make sure your Wrangler configuration includes the Durable Object binding and SQLite migration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8199.md")
</div>
<h2 id="define-types-for-tests">Define types for tests</h2>
<p>Create a <code>test/tsconfig.json</code> to configure TypeScript for your tests:</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;extends&quot;: &quot;../tsconfig.json&quot;,&#10;	&quot;compilerOptions&quot;: {&#10;		&quot;moduleResolution&quot;: &quot;bundler&quot;,&#10;		&quot;types&quot;: [&quot;@cloudflare/vitest-plugin/types&quot;]&#10;	},&#10;	&quot;include&quot;: [&quot;./**/*.ts&quot;, &quot;../src/worker-configuration.d.ts&quot;]&#10;}&#10;</code></pre>
<p>Create an <code>env.d.ts</code> file to type the test environment:</p>
<pre tabindex="0"><code class="language-ts">declare module &quot;cloudflare:workers&quot; {&#10;	interface ProvidedEnv extends Env {}&#10;}&#10;</code></pre>
<h2 id="writing-tests">Writing tests</h2>
<h3 id="unit-tests-with-direct-durable-object-access">Unit tests with direct Durable Object access</h3>
<p>You can get a stub to a Durable Object directly from the <code>env</code> object provided by <code>cloudflare:workers</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8200.md")
</div>
<h3 id="integration-tests-with-exports">Integration tests with <code>exports</code></h3>
<p>Use <code>exports.default.fetch()</code> to test your Worker's HTTP handler, which routes requests to Durable Objects:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8201.md")
</div>
<h3 id="direct-access-to-durable-object-internals">Direct access to Durable Object internals</h3>
<p>Use <code>runInDurableObject()</code> to access instance properties and storage directly. This is useful for verifying internal state or testing private methods:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8202.md")
</div>
<h3 id="testing-sqlite-storage">Testing SQLite storage</h3>
<p>SQLite-backed Durable Objects work seamlessly in tests. The SQL API is available when your Durable Object class is configured with <code>new_sqlite_classes</code> in your Wrangler configuration:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8203.md")
</div>
<h3 id="testing-alarms">Testing alarms</h3>
<p>Use <code>runDurableObjectAlarm()</code> to immediately trigger a scheduled alarm without waiting for the timer. This allows you to test alarm handlers synchronously:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8204.md")
</div>
<p>To test alarms, add an <code>alarm()</code> method to your Durable Object:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8205.md")
</div>
<h3 id="testing-eviction">Testing eviction</h3>
<p>Use <code>evictDurableObject()</code> to evict a Durable Object instance during tests. Eviction tears down the instance to reset its in-memory state. This lets you test how your Durable Object recovers state from storage after being evicted.</p>
<p>By default, hibernatable WebSockets are hibernated rather than closed, and eviction waits up to 30 seconds for in-flight requests to drain before tearing down the instance.</p>
<p>The following test sets both in-memory state (<code>cachedHits</code>) and durable storage (the counter value), evicts the Durable Object, and verifies that the in-memory state is wiped while the stored count survives:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8206.md")
</div>
<h4 id="testing-websocket-behavior-across-eviction">Testing WebSocket behavior across eviction</h4>
<p>You can control what happens to hibernatable WebSockets when a Durable Object is evicted by passing the <code>options</code> parameter:</p>
<ul>
<li><code>{ webSockets: &quot;hibernate&quot; }</code> (the default) hibernates WebSockets so they can resume after eviction.</li>
<li><code>{ webSockets: &quot;close&quot; }</code> closes WebSockets during eviction.</li>
</ul>
<p>The following example uses a Durable Object that accepts WebSocket connections with the <a href="/durable-objects/best-practices/websockets/">hibernatable WebSockets API</a>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8207.md")
</div>
<p>Add a binding and migration for the Durable Object in your Wrangler configuration, alongside the existing <code>COUNTER</code> binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8208.md")
</div>
<p>With the default options, hibernatable WebSockets remain open across eviction, so messages still round-trip afterwards. Passing <code>{ webSockets: &quot;close&quot; }</code> closes them instead:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8209.md")
</div>
<p>To evict all currently-running Durable Objects at once (for example, to reset state between tests without deleting persisted data), use <code>evictAllDurableObjects()</code>:</p>
<pre tabindex="0"><code class="language-ts">import { evictAllDurableObjects } from &quot;cloudflare:test&quot;;&#10;import { afterEach } from &quot;vitest&quot;;&#10;&#10;afterEach(async () =&gt; {&#10;	await evictAllDurableObjects();&#10;});&#10;</code></pre>
<p>For more details on the eviction helpers, including the <code>DurableObjectEvictionOptions</code> interface, refer to the <a href="/workers/testing/vitest-integration/test-apis/#durable-objects">Test APIs reference</a>.</p>
<h2 id="running-tests">Running tests</h2>
<p>Run your tests with:</p>
<pre tabindex="0"><code class="language-sh">npx vitest&#10;</code></pre>
<p>Or add a script to your <code>package.json</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;scripts&quot;: {&#10;		&quot;test&quot;: &quot;vitest&quot;&#10;	}&#10;}&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/testing/vitest-integration/">Workers Vitest integration</a> - Full documentation for the Vitest integration</li>
<li><a href="https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-plugin-examples/durable-objects">Durable Objects testing recipe</a> - Example from the Workers SDK</li>
<li><a href="https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-plugin-examples/rpc">RPC testing recipe</a> - Testing JSRPC with Durable Objects</li>
</ul>
