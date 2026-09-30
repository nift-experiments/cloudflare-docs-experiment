---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/developer-platform/21/
  description: '2025-04-07'
  full_title: Developer platform changelog - page 21 | Cloudflare Docs
  head_html: <title>Developer platform changelog - page 21 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-04-07"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/developer-platform/21/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Developer platform changelog - page 21"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-04-07"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/developer-platform/21/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/developer-platform/21/#page","headline":"Developer platform changelog - page 21 | Cloudflare Docs","description":"2025-04-07","url":"https://developers.cloudflare.com/changelog/product-group/developer-platform/21/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/developer-platform/21/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="build-mcp-servers-with-the-agents-sdk"><a href="/changelog/post/2025-04-07-mcp-servers-agents-sdk-updates/">Build MCP servers with the Agents SDK</a></h2>
<p><em>2025-04-07</em></p>
<p>The Agents SDK now includes built-in support for building remote MCP (Model Context Protocol) servers directly as part of your Agent. This allows you to easily create and manage MCP servers, without the need for additional infrastructure or configuration.</p>
<p>The SDK includes a new <code>MCPAgent</code> class that extends the <code>Agent</code> class and allows you to expose resources and tools over the MCP protocol, as well as authorization and authentication to enable remote MCP servers.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17623.md")</div>
<p>See <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp">the example</a> for the full code and as the basis for building your own MCP servers, and the <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp-client">client example</a> for how to build an Agent that acts as an MCP client.</p>
<p>To learn more, review the <a href="https://blog.cloudflare.com/building-ai-agents-with-mcp-authn-authz-and-durable-objects">announcement blog</a> as part of Developer Week 2025.</p>
<h4 id="2025-04-07-mcp-servers-agents-sdk-updates-agents-sdk-updates">Agents SDK updates</h4>
<p>We've made a number of improvements to the <a href="/agents/">Agents SDK</a>, including:</p>
<ul>
<li>Support for building MCP servers with the new <code>MCPAgent</code> class.</li>
<li>The ability to export the current agent, request and WebSocket connection context using <code>import { context } from &quot;agents&quot;</code>, allowing you to minimize or avoid direct dependency injection when calling tools.</li>
<li>Fixed a bug that prevented query parameters from being sent to the Agent server from the <code>useAgent</code> React hook.</li>
<li>Automatically converting the <code>agent</code> name in <code>useAgent</code> or <code>useAgentChat</code> to kebab-case to ensure it matches the naming convention expected by <a href="/agents/runtime/communication/routing/"><code>routeAgentRequest</code></a>.</li>
</ul>
<p>To install or update the Agents SDK, run <code>npm i agents@latest</code> in an existing project, or explore the <code>agents-starter</code> project:</p>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest -- --template cloudflare/agents-starter&#10;</code></pre>
<p>See the full release notes and changelog <a href="https://github.com/cloudflare/agents/blob/main/packages/agents/CHANGELOG.md">on the Agents SDK repository</a> and</p>


<h2 id="create-fully-managed-rag-pipelines-for-your-ai-applications-with-autorag"><a href="/changelog/post/2025-04-07-autorag-open-beta/">Create fully-managed RAG pipelines for your AI applications with AutoRAG</a></h2>
<p><em>2025-04-07</em></p>
<p><a href="/ai-search/">AutoRAG</a> is now in open beta, making it easy for you to build fully-managed retrieval-augmented generation (RAG) pipelines without managing infrastructure. Just upload your docs to <a href="/r2/get-started/">R2</a>, and AutoRAG handles the rest: embeddings, indexing, retrieval, and response generation via API.</p>
<p>With AutoRAG, you can:</p>
<ul>
<li><strong>Customize your pipeline:</strong> Choose from <a href="/workers-ai">Workers AI</a> models, configure chunking strategies, edit system prompts, and more.</li>
<li><strong>Instant setup:</strong> AutoRAG provisions everything you need from <a href="/vectorize">Vectorize</a>, <a href="/ai-gateway">AI gateway</a>, to pipeline logic for you, so you can go from zero to a working RAG pipeline in seconds.</li>
<li><strong>Keep your index fresh:</strong> AutoRAG continuously syncs your index with your data source to ensure responses stay accurate and up to date.</li>
<li><strong>Ask questions:</strong> Query your data and receive grounded responses via a <a href="/ai-search/api/search/workers-binding/">Workers binding</a> or <a href="/ai-search/api/search/rest-api/">API</a>.</li>
</ul>
<p>Whether you're building internal tools, AI-powered search, or a support assistant, AutoRAG gets you from idea to deployment in minutes.</p>
<p>Get started in the <a href="https://dash.cloudflare.com/?to=/:account/ai/autorag">Cloudflare dashboard</a> or check out the <a href="/ai-search/get-started/">guide</a> for instructions on how to build your RAG pipeline today.</p>


<h2 id="browser-rendering-rest-api-is-generally-available-with-new-endpoints-and-a-free-tier"><a href="/changelog/post/2025-04-07-br-free-ga-playwright/">Browser Rendering REST API is Generally Available, with new endpoints and a free tier</a></h2>
<p><em>2025-04-07</em></p>
<p>We’re excited to announce Browser Rendering is now available on the <a href="https://www.cloudflare.com/plans/developer-platform/">Workers Free plan</a>, making it even easier to prototype and experiment with web search and headless browser use-cases when building applications on Workers.</p>
<p>The Browser Rendering <strong><a href="/browser-run/quick-actions/">REST API</a> is now Generally Available</strong>, allowing you to control browser instances from outside of Workers applications. We've added three new endpoints to help automate more browser tasks:</p>
<ul>
<li><strong>Extract structured data</strong> – Use <code>/json</code> to retrieve structured data from a webpage.</li>
<li><strong>Retrieve links</strong> – Use <code>/links</code> to pull all links from a webpage.</li>
<li><strong>Convert to Markdown</strong> – Use <code>/markdown</code> to convert webpage content into Markdown format.</li>
</ul>
<p>For example, to fetch the Markdown representation of a webpage:</p>
<pre tabindex="0"><code class="language-bash">curl -X &#x27;POST&#x27; &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/markdown&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;&#10;  }&#x27;&#10;</code></pre>
<p>For the full list of endpoints, check out our <a href="/browser-run/quick-actions/">REST API documentation</a>. You can also interact with Browser Rendering via the <a href="https://github.com/cloudflare/cloudflare-typescript">Cloudflare TypeScript SDK</a>.</p>
<p>We also recently landed support for <a href="/browser-run/playwright/">Playwright</a> in Browser Rendering for browser automation from Cloudflare <a href="/workers/">Workers</a>, in addition to <a href="/browser-run/puppeteer/">Puppeteer</a>, giving you more flexibility to test across different browser environments.</p>
<p>Visit the <a href="/browser-run/">Browser Rendering docs</a> to learn more about how to use headless browsers in your applications.</p>


<h2 id="durable-objects-on-workers-free-plan"><a href="/changelog/post/2025-04-07-durable-objects-free-tier/">Durable Objects on Workers Free plan</a></h2>
<p><em>2025-04-07</em></p>
<p>Durable Objects can now be used with zero commitment on the <a href="/workers/platform/pricing/">Workers Free plan</a> allowing you to build AI agents with <a href="/agents/">Agents SDK</a>, collaboration tools, and real-time applications like chat or multiplayer games.</p>
<p>Durable Objects let you build stateful, serverless applications with millions of tiny coordination instances that run your application code alongside (in the same thread!) your durable storage. Each Durable Object can access its own SQLite database through a <a href="/durable-objects/best-practices/access-durable-objects-storage/">Storage API</a>. A Durable Object class is defined in a Worker script encapsulating the Durable Object's behavior when accessed from a Worker. To try the code below, click the button:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/hello-world-do-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<pre tabindex="0"><code class="language-js">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;// Durable Object&#10;export class MyDurableObject extends DurableObject {&#10;  ...&#10;	async sayHello(name) {&#10;		return `Hello, ${name}!`;&#10;	}&#10;}&#10;&#10;// Worker&#10;export default {&#10;	async fetch(request, env) {&#10;		// Every unique ID refers to an individual instance of the Durable Object class&#10;		const id = env.MY_DURABLE_OBJECT.idFromName(&quot;foo&quot;);&#10;&#10;		// A stub is a client used to invoke methods on the Durable Object&#10;		const stub = env.MY_DURABLE_OBJECT.get(id);&#10;&#10;		// Methods on the Durable Object are invoked via the stub&#10;		const response = await stub.sayHello(&quot;world&quot;);&#10;&#10;		return response;&#10;	},&#10;};&#10;</code></pre>
<p>Free plan <a href="/durable-objects/platform/pricing/">limits</a> apply to Durable Objects compute and storage usage. Limits allow developers to build real-world applications, with every Worker request able to call a Durable Object on the free plan.</p>
<p>For more information, checkout:</p>
<ul>
<li><a href="/durable-objects/concepts/what-are-durable-objects/">Documentation</a></li>
<li><a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">Zero-latency SQLite storage in every Durable Object blog</a></li>
</ul>


<h2 id="sqlite-in-durable-objects-ga-with-10gb-storage-per-object"><a href="/changelog/post/2025-04-07-sqlite-in-durable-objects-ga/">SQLite in Durable Objects GA with 10GB storage per object</a></h2>
<p><em>2025-04-07</em></p>
<p>SQLite in Durable Objects is now generally available (GA) with 10GB SQLite database per Durable Object. Since the <a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">public beta</a> in September 2024, we've added feature parity and robustness for the SQLite storage backend compared to the preexisting key-value (KV) storage backend for Durable Objects.</p>
<p>SQLite-backed Durable Objects are recommended for all new Durable Object classes, using <code>new_sqlite_classes</code> <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">Wrangler configuration</a>. Only SQLite-backed Durable Objects have access to Storage API's <a href="/durable-objects/api/sqlite-storage-api/#sql-api">SQL</a> and <a href="/durable-objects/api/sqlite-storage-api/#pitr-point-in-time-recovery-api">point-in-time recovery</a> methods, which provide relational data modeling, SQL querying, and better data management.</p>
<pre tabindex="0"><code class="language-js">export class MyDurableObject extends DurableObject {&#10;  sql: SqlStorage&#10;  constructor(ctx: DurableObjectState, env: Env) {&#10;    super(ctx, env);&#10;    this.sql = ctx.storage.sql;&#10;  }&#10;&#10;  async sayHello() {&#10;    let result = this.sql&#10;      .exec(&quot;SELECT &#x27;Hello, World!&#x27; AS greeting&quot;)&#10;      .one();&#10;    return result.greeting;&#10;  }&#10;}&#10;</code></pre>
<p>KV-backed Durable Objects remain for backwards compatibility, and a migration path from key-value storage to SQL storage for existing Durable Object classes will be offered in the future.</p>
<p>For more details on SQLite storage, checkout <a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">Zero-latency SQLite storage in every Durable Object blog</a>.</p>


<h2 id="capture-up-to-256-kb-of-log-events-in-each-workers-invocation"><a href="/changelog/post/2025-04-07-increase-trace-events-limit/">Capture up to 256 KB of log events in each Workers Invocation</a></h2>
<p><em>2025-04-07</em></p>
<p>You can now capture a maximum of 256 KB of log events per Workers invocation, helping you gain better visibility into application behavior.</p>
<p>All console.log() statements, exceptions, request metadata, and headers are automatically captured during the Worker invocation and emitted
as <a href="/logs/logpush/logpush-job/datasets/account/workers_trace_events">JSON object</a>. <a href="/workers/observability/logs/workers-logs">Workers Logs</a> deserializes
this object before indexing the fields and storing them. You can also capture, transform, and export the JSON object in a
<a href="/workers/observability/logs/tail-workers">Tail Worker</a>.</p>
<p>256 KB is a 2x increase from the previous 128 KB limit. After you exceed this limit, further context associated with the request will not be
recorded in your logs.</p>
<p>This limit is automatically applied to all Workers.</p>


<h2 id="workflows-is-now-generally-available"><a href="/changelog/post/2025-04-07-workflows-ga/">Workflows is now Generally Available</a></h2>
<p><em>2025-04-07</em></p>
<p><a href="/workflows/">Workflows</a> is now <em>Generally Available</em> (or &quot;GA&quot;): in short, it's ready for production workloads. Alongside marking Workflows as GA, we've introduced a number of changes during the beta period, including:</p>
<ul>
<li>A new <code>waitForEvent</code> API that allows a Workflow to wait for an event to occur before continuing execution.</li>
<li>Increased concurrency: you can <a href="/changelog/2025-02-25-workflows-concurrency-increased/">run up to 4,500 Workflow instances</a> concurrently — and this will continue to grow.</li>
<li>Improved observability, including new CPU time metrics that allow you to better understand which Workflow instances are consuming the most resources and/or contributing to your bill.</li>
<li>Support for <code>vitest</code> for testing Workflows locally and in CI/CD pipelines.</li>
</ul>
<p>Workflows also supports the new <a href="/changelog/2025-03-25-higher-cpu-limits/">increased CPU limits</a> that apply to Workers, allowing you to run more CPU-intensive tasks (up to 5 minutes of CPU time per instance), not including the time spent waiting on network calls, AI models, or other I/O bound tasks.</p>
<h4 id="2025-04-07-workflows-ga-human-in-the-loop">Human-in-the-loop</h4>
<p>The new <code>step.waitForEvent</code> API allows a Workflow instance to wait on events and data, enabling human-in-the-the-loop interactions, such as approving or rejecting a request, directly handling webhooks from other systems, or pushing event data to a Workflow while it's running.</p>
<p>Because Workflows are just code, you can conditionally execute code based on the result of a <code>waitForEvent</code> call, and/or call <code>waitForEvent</code> multiple times in a single Workflow based on what the Workflow needs.</p>
<p>For example, if you wanted to implement a human-in-the-loop approval process, you could use <code>waitForEvent</code> to wait for a user to approve or reject a request, and then conditionally execute code based on the result.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17829.md")</div>
<p>You can then send a Workflow an event from an external service via HTTP or from within a Worker using the <a href="/workflows/build/workers-api/">Workers API</a> for Workflows:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17830.md")</div>
<p>Read the <a href="https://blog.cloudflare.com/workflows-is-now-generally-available/">GA announcement blog</a> to learn more about what landed as part of the Workflows GA.</p>


<h2 id="playwright-for-browser-rendering-now-available"><a href="/changelog/post/2025-04-04-playwright-beta/">Playwright for Browser Rendering now available</a></h2>
<p><em>2025-04-04</em></p>
<p>We're excited to share that you can now use Playwright's browser automation <a href="https://playwright.dev/docs/api/class-playwright">capabilities</a> from Cloudflare <a href="/workers/">Workers</a>.</p>
<p><a href="https://playwright.dev/">Playwright</a> is an open-source package developed by Microsoft that can do browser automation tasks; it's commonly used to write software tests, debug applications, create screenshots, and crawl pages. Like <a href="/browser-run/puppeteer/">Puppeteer</a>, we <a href="https://github.com/cloudflare/playwright">forked</a> Playwright and modified it to be compatible with Cloudflare Workers and <a href="/browser-run/">Browser Rendering</a>.</p>
<p>Below is an example of how to use Playwright with Browser Rendering to test a TODO application using assertions:</p>
<pre tabindex="0"><code class="language-ts">import { launch, type BrowserWorker } from &quot;@cloudflare/playwright&quot;;&#10;import { expect } from &quot;@cloudflare/playwright/test&quot;;&#10;&#10;interface Env {&#10;	MYBROWSER: BrowserWorker;&#10;}&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env) {&#10;		const browser = await launch(env.MYBROWSER);&#10;		const page = await browser.newPage();&#10;&#10;		await page.goto(&quot;https://demo.playwright.dev/todomvc&quot;);&#10;&#10;		const TODO_ITEMS = [&#10;			&quot;buy some cheese&quot;,&#10;			&quot;feed the cat&quot;,&#10;			&quot;book a doctors appointment&quot;,&#10;		];&#10;&#10;		const newTodo = page.getByPlaceholder(&quot;What needs to be done?&quot;);&#10;		for (const item of TODO_ITEMS) {&#10;			await newTodo.fill(item);&#10;			await newTodo.press(&quot;Enter&quot;);&#10;		}&#10;&#10;		await expect(page.getByTestId(&quot;todo-title&quot;)).toHaveCount(TODO_ITEMS.length);&#10;&#10;		await Promise.all(&#10;			TODO_ITEMS.map((value, index) =&gt;&#10;				expect(page.getByTestId(&quot;todo-title&quot;).nth(index)).toHaveText(value),&#10;			),&#10;		);&#10;	},&#10;};&#10;</code></pre>
<p>Playwright is available as an npm package at <a href="https://www.npmjs.com/package/@cloudflare/playwright"><code>@cloudflare/playwright</code></a> and the code is at <a href="https://github.com/cloudflare/playwright">GitHub</a>.</p>
<p>Learn more in our <a href="/browser-run/playwright/">documentation</a>.</p>


<h2 id="new-pause-purge-apis-for-queues"><a href="/changelog/post/2025-03-25-pause-purge-queues/">New Pause & Purge APIs for Queues</a></h2>
<p><em>2025-03-27 12:00:00 UTC</em></p>
<p><a href="/queues/">Queues</a> now supports the ability to pause message delivery and/or purge (delete) messages on a queue. These operations can be useful when:</p>
<ul>
<li>Your consumer has a bug or downtime, and you want to temporarily stop messages from being processed while you fix the bug</li>
<li>You have pushed invalid messages to a queue due to a code change during development, and you want to clean up the backlog</li>
<li>Your queue has a backlog that is stale and you want to clean it up to allow new messages to be consumed</li>
</ul>
<p>To pause a queue using <a href="/workers/wrangler/">Wrangler</a>, run the <code>pause-delivery</code> command. Paused queues continue to receive messages. And you can easily unpause a queue using the <code>resume-delivery</code> command.</p>
<pre tabindex="0"><code class="language-bash">$ wrangler queues pause-delivery my-queue&#10;Pausing message delivery for queue my-queue.&#10;Paused message delivery for queue my-queue.&#10;&#10;$ wrangler queues resume-delivery my-queue&#10;Resuming message delivery for queue my-queue.&#10;Resumed message delivery for queue my-queue.&#10;</code></pre>
<p>Purging a queue permanently deletes all messages in the queue. Unlike pausing, purging is an irreversible operation:</p>
<pre tabindex="0"><code class="language-bash">$ wrangler queues purge my-queue&#10;✔ This operation will permanently delete all the messages in queue my-queue. Type my-queue to proceed. … my-queue&#10;Purged queue &#x27;my-queue&#x27;&#10;</code></pre>
<p>You can also do these operations using the <a href="/api/resources/queues/">Queues REST API</a>, or the dashboard page for a queue.</p>
<p><img src="/assets/upstream/images/queues/pause-purge.png" alt="Pause and purge using the dashboard" /></p>
<p>This feature is available on all new and existing queues. Head over to the <a href="/queues/configuration/pause-purge">pause and purge documentation</a> to learn more. And if you haven't used Cloudflare Queues before, <a href="/queues/get-started">get started with the Cloudflare Queues guide</a>.</p>


<h2 id="run-workers-for-up-to-5-minutes-of-cpu-time"><a href="/changelog/post/2025-03-25-higher-cpu-limits/">Run Workers for up to 5 minutes of CPU-time</a></h2>
<p><em>2025-03-26</em></p>
<p>You can now run a Worker for up to 5 minutes of CPU time for each request.</p>
<p>Previously, each Workers request ran for a maximum of 30 seconds of CPU time — that is the time that a Worker is actually performing a task (we still allowed unlimited wall-clock time, in case you were waiting on slow resources). This
meant that some compute-intensive tasks were impossible to do with a Worker. For instance,
you might want to take the cryptographic hash of a large file from R2. If
this computation ran for over 30 seconds, the Worker request would have timed out.</p>
<p>By default, Workers are still limited to 30 seconds of CPU time. This protects developers
from incurring accidental cost due to buggy code.</p>
<p>By changing the <code>cpu_ms</code> value in your Wrangler configuration, you can opt in to
any value up to 300,000 (5 minutes).</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17770.md")</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17769.md")</aside>
<p>For more information on the updates limits, see the documentation on <a href="/workers/wrangler/configuration/#limits">Wrangler configuration for <code>cpu_ms</code></a>
and on <a href="/workers/platform/limits/#cpu-time">Workers CPU time limits</a>.</p>
<p>For building long-running tasks on Cloudflare, we also recommend checking out <a href="/workflows/">Workflows</a> and <a href="/queues/">Queues</a>.</p>


<h2 id="source-maps-are-generally-available"><a href="/changelog/post/2025-03-25-gzip-source-maps/">Source Maps are Generally Available</a></h2>
<p><em>2025-03-25</em></p>
<p>Source maps are now Generally Available (GA). You can now be uploaded with a maximum gzipped size of 15 MB.
Previously, the maximum size limit was 15 MB uncompressed.</p>
<p>Source maps help map between the original source code and the transformed/minified code that gets deployed
to production. By uploading your source map, you allow Cloudflare to map the stack trace from exceptions
onto the original source code making it easier to debug.</p>
<p><img src="/assets/upstream/images/workers-observability/without-source-map.png" alt="Stack Trace without Source Map remapping" /></p>
<p>With <strong>no source maps uploaded</strong>: notice how all the Javascript has been minified to one file, so the stack trace is missing information on file name, shows incorrect line numbers, and incorrectly references <code>js</code> instead of <code>ts</code>.</p>
<p><img src="/assets/upstream/images/workers-observability/with-source-map.png" alt="Stack Trace with Source Map remapping" /></p>
<p>With <strong>source maps uploaded</strong>: all methods reference the correct files and line numbers.</p>
<p>Uploading source maps and stack trace remapping happens out of band from the Worker execution,
so source maps do not affect upload speed, bundle size, or cold starts. The remapped stack
traces are accessible through Tail Workers, Workers Logs, and Workers Logpush.</p>
<p>To enable source maps, add the following to your
<a href="/pages/functions/source-maps/">Pages Function's</a> or <a href="/workers/observability/source-maps/">Worker's</a> wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17768.md")</div>


<h2 id="new-managed-waf-rule-for-next-js-cve-2025-29927"><a href="/changelog/post/2025-03-22-next-js-vulnerability-waf/">New Managed WAF rule for Next.js CVE-2025-29927.</a></h2>
<p><em>2025-03-22</em></p>
<p><strong>Update: Mon Mar 24th, 11PM UTC</strong>: Next.js has made further changes to address a smaller vulnerability introduced in the patches made to its middleware handling. Users should upgrade to Next.js versions <code>15.2.4</code>, <code>14.2.26</code>, <code>13.5.10</code> or <code>12.3.6</code>. <strong>If you are unable to immediately upgrade or are running an older version of Next.js, you can enable the WAF rule described in this changelog as a mitigation</strong>.</p>
<p><strong>Update: Mon Mar 24th, 8PM UTC</strong>: Next.js has now <a href="https://github.com/advisories/GHSA-f82v-jwr5-mffw">backported the patch for this vulnerability</a> to cover Next.js v12 and v13. Users on those versions will need to patch to <code>13.5.9</code> and <code>12.3.5</code> (respectively) to mitigate the vulnerability.</p>
<p><strong>Update: Sat Mar 22nd, 4PM UTC</strong>: We have changed this WAF rule to opt-in only, as sites that use auth middleware with third-party auth vendors were observing failing requests.</p>
<p><strong>We strongly recommend updating your version of Next.js (if eligible)</strong> to the patched versions, as your app will otherwise be vulnerable to an authentication bypass attack regardless of auth provider.</p>
<h4 id="2025-03-22-next-js-vulnerability-waf-enable-the-managed-rule-strongly-recommended">Enable the Managed Rule (strongly recommended)</h4>
<p>This rule is opt-in only for sites on the Pro plan or above in the <a href="/waf/managed-rules/">WAF managed ruleset</a>.</p>
<p>To enable the rule:</p>
<ol>
<li>Head to Security &gt; WAF &gt; Managed rules in the Cloudflare dashboard for the zone (website) you want to protect.</li>
<li>Click the three dots next to <strong>Cloudflare Managed Ruleset</strong> and choose <strong>Edit</strong></li>
<li>Scroll down and choose <strong>Browse Rules</strong></li>
<li>Search for <strong>CVE-2025-29927</strong> (ruleId: <code>34583778093748cc83ff7b38f472013e</code>)</li>
<li>Change the <strong>Status</strong> to <strong>Enabled</strong> and the <strong>Action</strong> to <strong>Block</strong>. You can optionally set the rule to Log, to validate potential impact before enabling it. Log will not block requests.</li>
<li>Click <strong>Next</strong></li>
<li>Scroll down and choose <strong>Save</strong></li>
</ol>
<p>This will enable the WAF rule and block requests with the <code>x-middleware-subrequest</code> header regardless of Next.js version.</p>
<h4 id="2025-03-22-next-js-vulnerability-waf-create-a-waf-rule-manual">Create a WAF rule (manual)</h4>
<p>For users on the Free plan, or who want to define a more specific rule, you can create a <a href="/waf/custom-rules/create-dashboard/">Custom WAF rule</a> to block requests with the <code>x-middleware-subrequest</code> header regardless of Next.js version.</p>
<p>To create a custom rule:</p>
<ol>
<li>Head to Security &gt; WAF &gt; Custom rules in the Cloudflare dashboard for the zone (website) you want to protect.</li>
<li>Give the rule a name - e.g. <code>next-js-CVE-2025-29927</code></li>
<li>Set the matching parameters for the rule match any request where the <code>x-middleware-subrequest</code> header <code>exists</code> per the rule expression below.</li>
</ol>
<pre tabindex="0"><code class="language-sh">(len(http.request.headers[&quot;x-middleware-subrequest&quot;]) &gt; 0)&#10;</code></pre>
<ol start="4">
<li>Set the action to 'block'. If you want to observe the impact before blocking requests, set the action to 'log' (and edit the rule later).</li>
<li><strong>Deploy</strong> the rule.</li>
</ol>
<p><img src="/assets/upstream/images/changelog/workers/waf-rule-cve-2025-29927.png" alt="Next.js CVE-2025-29927 WAF rule" /></p>
<h4 id="2025-03-22-next-js-vulnerability-waf-next-js-cve-2025-29927">Next.js CVE-2025-29927</h4>
<p>We've made a WAF (Web Application Firewall) rule available to all sites on Cloudflare to protect against the <a href="https://github.com/advisories/GHSA-f82v-jwr5-mffw">Next.js authentication bypass vulnerability</a> (<code>CVE-2025-29927</code>) published on March 21st, 2025.</p>
<p><strong>Note</strong>: This rule is not enabled by default as it blocked requests across sites for specific authentication middleware.</p>
<ul>
<li>This managed rule protects sites using Next.js on Workers and Pages, as well as sites using Cloudflare to protect Next.js applications hosted elsewhere.</li>
<li>This rule has been made available (but not enabled by default) to all sites as part of our <a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">WAF Managed Ruleset</a> and blocks requests that attempt to bypass authentication in Next.js applications.</li>
<li>The vulnerability affects almost all Next.js versions, and has been fully patched in Next.js <code>14.2.26</code> and <code>15.2.4</code>. Earlier, interim releases did not fully patch this vulnerability.</li>
<li><strong>Users on older versions of Next.js (<code>11.1.4</code> to <code>13.5.6</code>) did not originally have a patch available</strong>, but this the patch for this vulnerability and a subsequent additional patch have been backported to Next.js versions <code>12.3.6</code> and <code>13.5.10</code> as of Monday, March 24th. Users on Next.js v11 will need to deploy the stated workaround or enable the WAF rule.</li>
</ul>
<p>The managed WAF rule mitigates this by blocking <em>external</em> user requests with the <code>x-middleware-subrequest</code> header regardless of Next.js version, but we recommend users using Next.js 14 and 15 upgrade to the patched versions of Next.js as an additional mitigation.</p>


<h2 id="smart-placement-is-smarter-about-running-workers-and-pages-functions-in-the-best-locations"><a href="/changelog/post/2025-03-22-smart-placement-stablization/">Smart Placement is smarter about running Workers and Pages Functions in the best locations</a></h2>
<p><em>2025-03-22</em></p>
<p><a href="/workers/configuration/placement/">Smart Placement</a> is a unique Cloudflare feature that can make decisions to move your Worker to run in a more optimal location (such as closer to a database). Instead of always running in the default location (the one closest to where the request is received), Smart Placement uses certain “heuristics” (rules and thresholds) to decide if a different location might be faster or more efficient.</p>
<p>Previously, if these heuristics weren't consistently met, your Worker would revert to running in the default location—even after it had been optimally placed. This meant that if your Worker received minimal traffic for a period of time, the system would reset to the default location, rather than remaining in the optimal one.</p>
<p>Now, once Smart Placement has identified and assigned an optimal location, temporarily dropping below the heuristic thresholds will not force a return to default locations. For example in the previous algorithm, a drop in requests for a few days might return to default locations and heuristics would have to be met again. This was problematic for workloads that made requests to a geographically located resource every few days or longer. In this scenario, your Worker would never get placed optimally. This is no longer the case.</p>


<h2 id="ai-gateway-launches-realtime-websockets-api"><a href="/changelog/post/2025-03-20-websockets/">AI Gateway launches Realtime WebSockets API</a></h2>
<p><em>2025-03-21</em></p>
<p>We are excited to announce that <a href="/ai-gateway/">AI Gateway</a> now supports real-time AI interactions with the new <a href="/ai-gateway/usage/websockets-api/realtime-api/">Realtime WebSockets API</a>.</p>
<p>This new capability allows developers to establish persistent, low-latency connections between their applications and AI models, enabling natural, real-time conversational AI experiences, including speech-to-speech interactions.</p>
<p>The Realtime WebSockets API works with the <a href="https://platform.openai.com/docs/guides/realtime#connect-with-websockets">OpenAI Realtime API</a>, <a href="https://ai.google.dev/gemini-api/docs/multimodal-live">Google Gemini Live API</a>, and supports real-time text and speech interactions with models from <a href="https://docs.cartesia.ai/api-reference/tts/tts">Cartesia</a>, and <a href="https://elevenlabs.io/docs/conversational-ai/api-reference/conversational-ai/websocket">ElevenLabs</a>.</p>
<p>Here's how you can connect AI Gateway to <a href="https://platform.openai.com/docs/guides/realtime#connect-with-websockets">OpenAI's Realtime API</a> using WebSockets:</p>
<pre tabindex="0"><code class="language-javascript">import WebSocket from &quot;ws&quot;;&#10;&#10;const url =&#10;	&quot;wss://gateway.ai.cloudflare.com/v1/&lt;account_id&gt;/&lt;gateway&gt;/openai?model=gpt-4o-realtime-preview-2024-12-17&quot;;&#10;const ws = new WebSocket(url, {&#10;	headers: {&#10;		&quot;cf-aig-authorization&quot;: process.env.CLOUDFLARE_API_KEY,&#10;		Authorization: &quot;Bearer &quot; + process.env.OPENAI_API_KEY,&#10;		&quot;OpenAI-Beta&quot;: &quot;realtime=v1&quot;,&#10;	},&#10;});&#10;&#10;ws.on(&quot;open&quot;, () =&gt; console.log(&quot;Connected to server.&quot;));&#10;ws.on(&quot;message&quot;, (message) =&gt; console.log(JSON.parse(message.toString())));&#10;&#10;ws.send(&#10;	JSON.stringify({&#10;		type: &quot;response.create&quot;,&#10;		response: { modalities: [&quot;text&quot;], instructions: &quot;Tell me a joke&quot; },&#10;	}),&#10;);&#10;</code></pre>
<p>Get started by checking out the <a href="/ai-gateway/usage/websockets-api/realtime-api/">Realtime WebSockets API</a> documentation.</p>


<h2 id="dozens-of-cloudflare-terraform-provider-resources-now-have-proper-drift-detection"><a href="/changelog/post/2025-03-21-resource-force-replacement-bug/">Dozens of Cloudflare Terraform Provider resources now have proper drift detection</a></h2>
<p><em>2025-03-21</em></p>
<p>In <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform Provider</a> versions 5.2.0 and above, dozens of resources now have proper drift detection. Before this fix, these resources would indicate they needed to be updated or replaced — even if there was no real change. Now, you can rely on your <code>terraform plan</code> to only show what resources are expected to change.</p>
<p>This issue affected <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">resources</a> related to these products and features:</p>
<ul>
<li>API Shield</li>
<li>Argo Smart Routing</li>
<li>Argo Tiered Caching</li>
<li>Bot Management</li>
<li>BYOIP</li>
<li>D1</li>
<li>DNS</li>
<li>Email Routing</li>
<li>Hyperdrive</li>
<li>Observatory</li>
<li>Pages</li>
<li>R2</li>
<li>Rules</li>
<li>SSL/TLS</li>
<li>Waiting Room</li>
<li>Workers</li>
<li>Zero Trust</li>
</ul>


<h2 id="cloudflare-terraform-provider-now-properly-redacts-sensitive-values"><a href="/changelog/post/2025-03-21-sensitive-values-redacted/">Cloudflare Terraform Provider now properly redacts sensitive values</a></h2>
<p><em>2025-03-21</em></p>
<p>In the <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform Provider</a> versions 5.2.0 and above, sensitive properties of resources are redacted in logs. Sensitive properties in <a href="https://raw.githubusercontent.com/cloudflare/api-schemas/refs/heads/main/openapi.yaml">Cloudflare's OpenAPI Schema</a> are now annotated with <code>x-sensitive: true</code>. This results in proper auto-generation of the corresponding Terraform resources, and prevents sensitive values from being shown when you run Terraform commands.</p>
<p>This issue affected <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">resources</a> related to these products and features:</p>
<ul>
<li>Alerts and Audit Logs</li>
<li>Device API</li>
<li>DLP</li>
<li>DNS</li>
<li>Magic Visibility</li>
<li>Magic WAN</li>
<li>TLS Certs and Hostnames</li>
<li>Tunnels</li>
<li>Turnstile</li>
<li>Workers</li>
<li>Zaraz</li>
</ul>


<h2 id="markdown-conversion-in-workers-ai"><a href="/changelog/post/2025-03-20-markdown-conversion/">Markdown conversion in Workers AI</a></h2>
<p><em>2025-03-20</em></p>
<p>Document conversion plays an important role when designing and developing AI applications and agents. Workers AI now provides the <code>toMarkdown</code> utility method that developers can use to for quick, easy, and convenient conversion and summary of documents in multiple formats to Markdown language.</p>
<p>You can call this new tool using a binding by calling <code>env.AI.toMarkdown()</code> or the using the <a href="/api/resources/ai/">REST API</a> endpoint.</p>
<p>In this example, we fetch a PDF document and an image from R2 and feed them both to <code>env.AI.toMarkdown()</code>. The result is a list of converted documents. Workers AI models are used automatically to detect and summarize the image.</p>
<pre tabindex="0"><code class="language-typescript">import { Env } from &quot;./env&quot;;&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env, ctx: ExecutionContext) {&#10;		// https://pub-979cb28270cc461d94bc8a169d8f389d.r2.dev/somatosensory.pdf&#10;		const pdf = await env.R2.get(&quot;somatosensory.pdf&quot;);&#10;&#10;		// https://pub-979cb28270cc461d94bc8a169d8f389d.r2.dev/cat.jpeg&#10;		const cat = await env.R2.get(&quot;cat.jpeg&quot;);&#10;&#10;		return Response.json(&#10;			await env.AI.toMarkdown([&#10;				{&#10;					name: &quot;somatosensory.pdf&quot;,&#10;					blob: new Blob([await pdf.arrayBuffer()], {&#10;						type: &quot;application/octet-stream&quot;,&#10;					}),&#10;				},&#10;				{&#10;					name: &quot;cat.jpeg&quot;,&#10;					blob: new Blob([await cat.arrayBuffer()], {&#10;						type: &quot;application/octet-stream&quot;,&#10;					}),&#10;				},&#10;			]),&#10;		);&#10;	},&#10;};&#10;</code></pre>
<p>This is the result:</p>
<pre tabindex="0"><code class="language-json">[&#10;	{&#10;		&quot;name&quot;: &quot;somatosensory.pdf&quot;,&#10;		&quot;mimeType&quot;: &quot;application/pdf&quot;,&#10;		&quot;format&quot;: &quot;markdown&quot;,&#10;		&quot;tokens&quot;: 0,&#10;		&quot;data&quot;: &quot;# somatosensory.pdf\n## Metadata\n- PDFFormatVersion=1.4\n- IsLinearized=false\n- IsAcroFormPresent=false\n- IsXFAPresent=false\n- IsCollectionPresent=false\n- IsSignaturesPresent=false\n- Producer=Prince 20150210 (www.princexml.com)\n- Title=Anatomy of the Somatosensory System\n\n## Contents\n### Page 1\nThis is a sample document to showcase...&quot;&#10;	},&#10;	{&#10;		&quot;name&quot;: &quot;cat.jpeg&quot;,&#10;		&quot;mimeType&quot;: &quot;image/jpeg&quot;,&#10;		&quot;format&quot;: &quot;markdown&quot;,&#10;		&quot;tokens&quot;: 0,&#10;		&quot;data&quot;: &quot;The image is a close-up photograph of Grumpy Cat, a cat with a distinctive grumpy expression and piercing blue eyes. The cat has a brown face with a white stripe down its nose, and its ears are pointed upright. Its fur is light brown and darker around the face, with a pink nose and mouth. The cat&#x27;s eyes are blue and slanted downward, giving it a perpetually grumpy appearance. The background is blurred, but it appears to be a dark brown color. Overall, the image is a humorous and iconic representation of the popular internet meme character, Grumpy Cat. The cat&#x27;s facial expression and posture convey a sense of displeasure or annoyance, making it a relatable and entertaining image for many people.&quot;&#10;	}&#10;]&#10;</code></pre>
<p>See <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion</a> for more information on supported formats, REST API and pricing.</p>


<h2 id="npm-i-agents"><a href="/changelog/post/2025-03-18-npm-i-agents/">npm i agents</a></h2>
<p><em>2025-03-18</em></p>
<img src="/assets/upstream/images/agents/npm-i-agents.apng" alt="npm i agents" width="1000" height="541" />
<h4 id="2025-03-18-npm-i-agents-agents-sdk-agents"><code>agents-sdk</code> -&gt; <code>agents</code> <span class="nb-badge">Updated</span></h4>
<p>📝 <strong>We've renamed the Agents package to <code>agents</code></strong>!</p>
<p>If you've already been building with the Agents SDK, you can update your dependencies to use the new package name, and replace references to <code>agents-sdk</code> with <code>agents</code>:</p>
<pre tabindex="0"><code class="language-sh">&#35; Install the new package&#10;npm i agents&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#35; Remove the old (deprecated) package&#10;npm uninstall agents-sdk&#10;&#10;&#35; Find instances of the old package name in your codebase&#10;grep -r &#x27;agents-sdk&#x27; .&#10;&#35; Replace instances of the old package name with the new one&#10;&#35; (or use find-replace in your editor)&#10;sed -i &#x27;s/agents-sdk/agents/g&#x27; $(grep -rl &#x27;agents-sdk&#x27; .)&#10;</code></pre>
<p>All future updates will be pushed to the new <code>agents</code> package, and the older package has been marked as deprecated.</p>
<h4 id="2025-03-18-npm-i-agents-agents-sdk-updates">Agents SDK updates <span class="nb-badge">New</span></h4>
<p>We've added a number of big new features to the Agents SDK over the past few weeks, including:</p>
<ul>
<li>You can now set <code>cors: true</code> when using <code>routeAgentRequest</code> to return permissive default CORS headers to Agent responses.</li>
<li>The regular client now syncs state on the agent (just like the React version).</li>
<li><code>useAgentChat</code> bug fixes for passing headers/credentials, including properly clearing cache on unmount.</li>
<li>Experimental <code>/schedule</code> module with a prompt/schema for adding scheduling to your app (with evals!).</li>
<li>Changed the internal <code>zod</code> schema to be compatible with the limitations of Google's Gemini models by removing the discriminated union, allowing you to use Gemini models with the scheduling API.</li>
</ul>
<p>We've also fixed a number of bugs with state synchronization and the React hooks.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17621.md")</div>
<h4 id="2025-03-18-npm-i-agents-call-agent-methods-from-your-client-code">Call Agent methods from your client code <span class="nb-badge">New</span></h4>
<p>We've added a new <a href="/agents/runtime/agents-api/"><code>@unstable_callable()</code></a> decorator for defining methods that can be called directly from clients. This allows you call methods from within your client code: you can call methods (with arguments) and get native JavaScript objects back.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17622.md")</div>
<h4 id="2025-03-18-npm-i-agents-agents-starter">agents-starter <span class="nb-badge">Updated</span></h4>
<p>We've fixed a number of small bugs in the <a href="https://github.com/cloudflare/agents-starter"><code>agents-starter</code></a> project — a real-time, chat-based example application with tool-calling &amp; human-in-the-loop built using the Agents SDK. The starter has also been upgraded to use the latest <a href="/changelog/2025-03-13-wrangler-v4/">wrangler v4</a> release.</p>
<p>If you're new to Agents, you can install and run the <code>agents-starter</code> project in two commands:</p>
<pre tabindex="0"><code class="language-sh">&#35; Install it&#10;$ npm create cloudflare@latest agents-starter -- --template=&quot;cloudflare/agents-starter&quot;&#10;&#35; Run it&#10;$ npm run start&#10;</code></pre>
<p>You can use the starter as a template for your own Agents projects: open up <code>src/server.ts</code> and <code>src/client.tsx</code> to see how the Agents SDK is used.</p>
<h4 id="2025-03-18-npm-i-agents-more-documentation">More documentation <span class="nb-badge">Updated</span></h4>
<p>We've heard your feedback on the Agents SDK documentation, and we're shipping more API reference material and usage examples, including:</p>
<ul>
<li>Expanded <a href="/agents/runtime/">API reference documentation</a>, covering the methods and properties exposed by the Agents SDK, as well as more usage examples.</li>
<li>More <a href="/agents/runtime/agents-api/#client-api">Client API</a> documentation that documents <code>useAgent</code>, <code>useAgentChat</code> and the new <code>@unstable_callable</code> RPC decorator exposed by the SDK.</li>
<li>New documentation on how to <a href="/agents/runtime/communication/routing/">route requests to agents</a> and (optionally) authenticate clients before they connect to your Agents.</li>
</ul>
<p>Note that the Agents SDK is continually growing: the type definitions included in the SDK will always include the latest APIs exposed by the <code>agents</code> package.</p>
<p>If you're still wondering what Agents are, <a href="https://blog.cloudflare.com/build-ai-agents-on-cloudflare/">read our blog on building AI Agents on Cloudflare</a> and/or visit the <a href="/agents/">Agents documentation</a> to learn more.</p>


<h2 id="import-env-to-access-bindings-in-your-worker-s-global-scope"><a href="/changelog/post/2025-03-17-importable-env/">Import `env` to access bindings in your Worker's global scope</a></h2>
<p><em>2025-03-17</em></p>
<p>You can now access <a href="/workers/runtime-apis/bindings/">bindings</a>
from anywhere in your Worker by importing the <code>env</code> object from <code>cloudflare:workers</code>.</p>
<p>Previously, <code>env</code> could only be accessed during a request. This meant that
bindings could not be used in the top-level context of a Worker.</p>
<p>Now, you can import <code>env</code> and access bindings such as <a href="/workers/configuration/secrets/">secrets</a>
or <a href="/workers/configuration/environment-variables/">environment variables</a> in the
initial setup for your Worker:</p>
<pre tabindex="0"><code class="language-js">import { env } from &quot;cloudflare:workers&quot;;&#10;import ApiClient from &quot;example-api-client&quot;;&#10;&#10;// API_KEY and LOG_LEVEL now usable in top-level scope&#10;const apiClient = ApiClient.new({ apiKey: env.API_KEY });&#10;const LOG_LEVEL = env.LOG_LEVEL || &quot;info&quot;;&#10;&#10;export default {&#10;	fetch(req) {&#10;		// you can use apiClient or LOG_LEVEL, configured before any request is handled&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17767.md")</aside>
<p>Additionally, <code>env</code> was normally accessed as a argument to a Worker's entrypoint handler,
such as <a href="/workers/runtime-apis/fetch/"><code>fetch</code></a>.
This meant that if you needed to access a binding from a deeply nested function,
you had to pass <code>env</code> as an argument through many functions to get it to the
right spot. This could be cumbersome in complex codebases.</p>
<p>Now, you can access the bindings from anywhere in your codebase
without passing <code>env</code> as an argument:</p>
<pre tabindex="0"><code class="language-js">// helpers.js&#10;import { env } from &quot;cloudflare:workers&quot;;&#10;&#10;// env is *not* an argument to this function&#10;export async function getValue(key) {&#10;	let prefix = env.KV_PREFIX;&#10;	return await env.KV.get(`${prefix}-${key}`);&#10;}&#10;</code></pre>
<p>For more information, see <a href="/workers/runtime-apis/bindings#how-to-access-env">documentation on accessing <code>env</code></a>.</p>


<h2 id="retry-pages-workers-builds-directly-from-github"><a href="/changelog/post/2025-03-17-rerun-build/">Retry Pages & Workers Builds Directly from GitHub</a></h2>
<p><em>2025-03-17</em></p>
<p>You can now retry your Cloudflare Pages and Workers builds directly from GitHub. No need to switch to the Cloudflare Dashboard for a simple retry!</p>
<p>Let\u2019s say you push a commit, but your build fails due to a spurious error like a network timeout. Instead of going to the Cloudflare Dashboard to manually retry, you can now rerun the build with just a few clicks inside GitHub, keeping you inside your workflow.</p>
<p>For Pages and Workers projects connected to a GitHub repository:</p>
<ol>
<li>When a build fails, go to your GitHub repository or pull request</li>
<li>Select the failed Check Run for the build</li>
<li>Select &quot;Details&quot; on the Check Run</li>
<li>Select &quot;Rerun&quot; to trigger a retry build for that commit</li>
</ol>
<p>Learn more about <a href="/pages/configuration/git-integration/github-integration/">Pages Builds</a> and <a href="/workers/ci-cd/builds/git-integration/github-integration/">Workers Builds</a>.</p>


<h2 id="new-models-in-workers-ai"><a href="/changelog/post/2025-03-17-new-workers-ai-models/">New models in Workers AI</a></h2>
<p><em>2025-03-17</em></p>
<p>Workers AI is excited to add 4 new models to the catalog, including 2 brand new classes of models with a text-to-speech and reranker model. Introducing:</p>
<ul>
<li><a href="/workers-ai/models/bge-m3/">@cf/baai/bge-m3</a> - a multi-lingual embeddings model that supports over 100 languages. It can also simultaneously perform dense retrieval, multi-vector retrieval, and sparse retrieval, with the ability to process inputs of different granularities.</li>
<li><a href="/workers-ai/models/bge-reranker-base/">@cf/baai/bge-reranker-base</a> - our first reranker model! Rerankers are a type of text classification model that takes a query and context, and outputs a similarity score between the two. When used in RAG systems, you can use a reranker after the initial vector search to find the most relevant documents to return to a user by reranking the outputs.</li>
<li><a href="/workers-ai/models/whisper-large-v3-turbo/">@cf/openai/whisper-large-v3-turbo</a> - a faster, more accurate speech-to-text model. This model was added earlier but is graduating out of beta with pricing included today.</li>
<li><a href="/workers-ai/models/melotts/">@cf/myshell-ai/melotts</a> - our first text-to-speech model that allows users to generate an MP3 with voice audio from inputted text.</li>
</ul>
<p>Pricing is available for each of these models on the <a href="/workers-ai/platform/pricing/">Workers AI pricing page</a>.</p>
<p>This docs update includes a few minor bug fixes to the model schema for llama-guard, llama-3.2-1b, which you can review on the <a href="/workers-ai/changelog/">product changelog</a>.</p>
<p>Try it out and let us know what you think! Stay tuned for more models in the coming days.</p>


<h2 id="use-the-latest-javascript-features-with-wrangler-cli-v4"><a href="/changelog/post/2025-03-13-wrangler-v4/">Use the latest JavaScript features with Wrangler CLI v4</a></h2>
<p><em>2025-03-13</em></p>
<p>We've released the next major version of <a href="/workers/wrangler/">Wrangler</a>, the CLI for Cloudflare Workers — <code>wrangler@4.0.0</code>. Wrangler v4 is a major release focused on updates to underlying systems and dependencies, along with improvements to keep Wrangler commands consistent and clear.</p>
<p>You can run the following command to install it in your projects:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i wrangler@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i wrangler@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add wrangler@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add wrangler@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add wrangler@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add wrangler@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add wrangler@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add wrangler@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Unlike previous major versions of Wrangler, which were <a href="https://blog.cloudflare.com/wrangler-v2-beta/">foundational rewrites</a> and <a href="https://blog.cloudflare.com/wrangler3/">rearchitectures</a> — Version 4 of Wrangler includes a much smaller set of changes. If you use Wrangler today, your workflow is very unlikely to change.</p>
<p>A <a href="/workers/wrangler/migration/update-v3-to-v4">detailed migration guide</a> is available and if you find a bug or hit a roadblock when upgrading to Wrangler v4, <a href="https://github.com/cloudflare/workers-sdk/issues/new?template=bug-template.yaml">open an issue on the <code>cloudflare/workers-sdk</code> repository on GitHub</a>.</p>
<p>Going forward, we'll continue supporting Wrangler v3 with bug fixes and security updates until Q1 2026, and with critical security updates until Q1 2027, at which point it will be out of support.</p>


<h2 id="set-breakpoints-and-debug-your-workers-tests-with-cloudflare-vitest-pool-workers"><a href="/changelog/post/2025-03-14-breakpoint-debugging-with-vitest/">Set breakpoints and debug your Workers tests with @cloudflare/vitest-pool-workers</a></h2>
<p><em>2025-03-13</em></p>
<p>You can now debug your Workers tests with our <a href="/workers/testing/vitest-integration/">Vitest integration</a> by running the following command:</p>
<pre tabindex="0"><code class="language-sh">vitest --inspect --no-file-parallelism&#10;</code></pre>
<p>Attach a debugger to the port 9229 and you can start stepping through your Workers tests. This is available with <code>@cloudflare/vitest-pool-workers</code> v0.7.5 or later.</p>
<p>Learn more in our <a href="/workers/testing/vitest-integration/debugging/">documentation</a>.</p>


<h2 id="threaded-replies-now-possible-in-email-workers"><a href="/changelog/post/2025-03-12-reply-limits/">Threaded replies now possible in Email Workers</a></h2>
<p><em>2025-03-12</em></p>
<p>We’re removing some of the restrictions in Email Routing so that AI Agents and task automation can better handle email workflows, including how Workers can <a href="/email-service/api/route-emails/email-handler/#reply-to-emails">reply</a> to incoming emails.</p>
<p>It's now possible to keep a threaded email conversation with an <a href="/email-service/api/route-emails/email-handler/">Email Worker</a> script as long as:</p>
<ul>
<li>The incoming email has to have valid <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/">DMARC</a>.</li>
<li>The email can only be replied to once in the same <code>EmailMessage</code> event.</li>
<li>The recipient in the reply must match the incoming sender.</li>
<li>The outgoing sender domain must match the same domain that received the email.</li>
<li>Every time an email passes through Email Routing or another MTA, an entry is added to the <code>References</code> list. We stop accepting replies to emails with more than 100 <code>References</code> entries to prevent abuse or accidental loops.</li>
</ul>
<p>Here's an example of a Worker responding to Emails using a Workers AI model:</p>
<pre tabindex="0"><code class="language-ts">import PostalMime from &quot;postal-mime&quot;;&#10;import { createMimeMessage } from &quot;mimetext&quot;;&#10;import { EmailMessage } from &quot;cloudflare:email&quot;;&#10;&#10;export default {&#10;	async email(message, env, ctx) {&#10;		const email = await PostalMime.parse(message.raw);&#10;		const res = await env.AI.run(&quot;@cf/meta/llama-2-7b-chat-fp16&quot;, {&#10;			messages: [&#10;				{&#10;					role: &quot;user&quot;,&#10;					content: email.text ?? &quot;&quot;,&#10;				},&#10;			],&#10;		});&#10;&#10;		// message-id is generated by mimetext&#10;		const response = createMimeMessage();&#10;		response.setHeader(&quot;In-Reply-To&quot;, message.headers.get(&quot;Message-ID&quot;)!);&#10;		response.setSender(&quot;agent@example.com&quot;);&#10;		response.setRecipient(message.from);&#10;		response.setSubject(&quot;Llama response&quot;);&#10;		response.addMessage({&#10;			contentType: &quot;text/plain&quot;,&#10;			data:&#10;				res instanceof ReadableStream&#10;					? await new Response(res).text()&#10;					: res.response!,&#10;		});&#10;&#10;		const replyMessage = new EmailMessage(&#10;			&quot;&lt;email&gt;&quot;,&#10;			message.from,&#10;			response.asRaw(),&#10;		);&#10;		await message.reply(replyMessage);&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>See <a href="/email-service/api/route-emails/email-handler/#reply-to-emails">Reply to emails from Workers</a> for more information.</p>


<h2 id="access-your-worker-s-environment-variables-from-process-env"><a href="/changelog/post/2025-03-11-process-env-support/">Access your Worker's environment variables from process.env</a></h2>
<p><em>2025-03-11</em></p>
<p>You can now access <a href="/workers/configuration/environment-variables/">environment variables</a> and
<a href="/workers/configuration/secrets/">secrets</a> on <a href="/workers/runtime-apis/nodejs/process/#processenv"><code>process.env</code></a>
when using the <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag"><code>nodejs_compat</code> compatibility flag</a>.</p>
<pre tabindex="0"><code class="language-js">const apiClient = ApiClient.new({ apiKey: process.env.API_KEY });&#10;const LOG_LEVEL = process.env.LOG_LEVEL || &quot;info&quot;;&#10;</code></pre>
<p>In Node.js, environment variables are exposed via the global <code>process.env</code> object. Some libraries
assume that this object will be populated, and many developers may be used to accessing variables
in this way.</p>
<p>Previously, the <code>process.env</code> object was always empty unless written to in Worker code. This could
cause unexpected errors or friction when developing Workers using code previously written for Node.js.</p>
<p>Now, <a href="/workers/configuration/environment-variables/">environment variables</a>,
<a href="/workers/configuration/secrets/">secrets</a>, and <a href="/workers/runtime-apis/bindings/version-metadata/">version metadata</a>
can all be accessed on <code>process.env</code>.</p>
<p>To opt-in to the new <code>process.env</code> behaviour now, add the <a href="/workers/configuration/compatibility-flags/#enable-auto-populating-processenv"><code>nodejs_compat_populate_process_env</code></a> compatibility flag to your
<code>wrangler.json</code> configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17766.md")</div>
<p>After April 1, 2025, populating <code>process.env</code> will become the default behavior when both <code>nodejs_compat</code> is enabled and
your Worker's <code>compatibility_date</code> is after &quot;2025-04-01&quot;.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/20/">Previous</a><span>Page 21 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/22/">Next</a></nav>
