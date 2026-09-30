---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/workers/9/
  description: '2025-05-16'
  full_title: workers changelog - page 9 | Cloudflare Docs
  head_html: <title>workers changelog - page 9 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-05-16"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/workers/9/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="workers changelog - page 9"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-05-16"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/workers/9/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/workers/9/#page","headline":"workers changelog - page 9 | Cloudflare Docs","description":"2025-05-16","url":"https://developers.cloudflare.com/changelog/product/workers/9/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/workers/9/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="durable-objects-are-now-supported-in-python-workers"><a href="/changelog/post/2025-05-14-python-worker-durable-object/">Durable Objects are now supported in Python Workers</a></h2>
<p><em>2025-05-16</em></p>
<p>You can now create <a href="/durable-objects/">Durable Objects</a> using
<a href="/workers/languages/python/">Python Workers</a>. A Durable Object is a special kind of
Cloudflare Worker which uniquely combines compute with storage, enabling stateful
long-running applications which run close to your users. For more info see
<a href="/durable-objects/concepts/what-are-durable-objects/">here</a>.</p>
<p>You can define a Durable Object in Python in a similar way to JavaScript:</p>
<pre tabindex="0"><code class="language-python">from workers import DurableObject, Response, WorkerEntrypoint&#10;&#10;from urllib.parse import urlparse&#10;&#10;class MyDurableObject(DurableObject):&#10;    def __init__(self, ctx, env):&#10;        self.ctx = ctx&#10;        self.env = env&#10;&#10;    def fetch(self, request):&#10;        result = self.ctx.storage.sql.exec(&quot;SELECT &#x27;Hello, World!&#x27; as greeting&quot;).one()&#10;        return Response(result.greeting)&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        url = urlparse(request.url)&#10;        id = env.MY_DURABLE_OBJECT.idFromName(url.path)&#10;        stub = env.MY_DURABLE_OBJECT.get(id)&#10;        greeting = await stub.fetch(request.url)&#10;        return greeting&#10;</code></pre>
<p>Define the Durable Object in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17773.md")</div>
<p>Then define the storage backend for your Durable Object:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17774.md")</div>
<p>Then test your new Durable Object locally by running <code>wrangler dev</code>:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler dev&#10;</code></pre>
<p>Consult the <a href="/durable-objects/">Durable Objects documentation</a> for more details.</p>


<h2 id="improved-memory-efficiency-for-webassembly-workers"><a href="/changelog/post/2025-05-08-finalization-registry/">Improved memory efficiency for WebAssembly Workers</a></h2>
<p><em>2025-05-08</em></p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry">FinalizationRegistry</a> is now available in Workers. You can opt-in using the <a href="/workers/configuration/compatibility-flags/#enable-finalizationregistry-and-weakref"><code>enable_weak_ref</code></a> compatibility flag.</p>
<p>This can reduce memory leaks when using WebAssembly-based Workers, which includes <a href="/workers/languages/python/">Python Workers</a> and <a href="/workers/languages/rust/">Rust Workers</a>. The FinalizationRegistry works by enabling toolchains such as <a href="https://emscripten.org/">Emscripten</a> and <a href="https://wasm-bindgen.github.io/wasm-bindgen/">wasm-bindgen</a> to automatically free WebAssembly heap allocations. If you are using WASM and seeing Exceeded Memory errors and cannot determine a cause using <a href="/workers/observability/dev-tools/memory-usage/">memory profiling</a>, you may want to enable the FinalizationRegistry.</p>
<p>For more information refer to the <a href="/workers/configuration/compatibility-flags/#enable-finalizationregistry-and-weakref"><code>enable_weak_ref</code></a> compatibility flag documentation.</p>


<h2 id="cron-triggers-are-now-supported-in-python-workers"><a href="/changelog/post/2025-04-22-python-worker-cron-triggers/">Cron triggers are now supported in Python Workers</a></h2>
<p><em>2025-04-24</em></p>
<p>You can now create Python Workers which are executed via a cron trigger.</p>
<p>This is similar to how it's done in JavaScript Workers, simply define a scheduled event
listener in your Worker:</p>
<pre tabindex="0"><code class="language-python">from workers import handler&#10;&#10;@handler&#10;async def on_scheduled(event, env, ctx):&#10;  print(&quot;cron processed&quot;)&#10;</code></pre>
<p>Define a cron trigger configuration in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17772.md")</div>
<p>Then test your new handler by using Wrangler with the <code>--test-scheduled</code> flag and
making a request to <code>/cdn-cgi/local/scheduled?cron=*+*+*+*+*</code>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev --test-scheduled&#10;&#10;curl &quot;http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*&quot;&#10;</code></pre>
<p>Consult the <a href="/workers/configuration/cron-triggers/">Workers Cron Triggers page</a> for full details on cron triggers in Workers.</p>


<h2 id="fixed-and-documented-workers-routes-and-secrets-api"><a href="/changelog/post/2025-04-15-workers-api-fixes/">Fixed and documented Workers Routes and Secrets API</a></h2>
<p><em>2025-04-15</em></p>
<h4 id="2025-04-15-workers-api-fixes-workers-routes-api">Workers Routes API</h4>
<p>Previously, a request to the Workers <a href="/api/resources/workers/subresources/routes/methods/create/">Create Route API</a> always returned <code>null</code> for &quot;script&quot; and an empty string for &quot;pattern&quot; even if the request was successful.</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/zones/$CF_ACCOUNT_ID/workers/routes \&#10;&#45;X PUT \&#10;&#45;H &quot;Authorization: Bearer $CF_API_TOKEN&quot; \&#10;&#45;H &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{ &quot;pattern&quot;: &quot;example.com/*&quot;, &quot;script&quot;: &quot;hello-world-script&quot; }&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;bf153a27ba2b464bb9f04dcf75de1ef9&quot;,&#10;		&quot;pattern&quot;: &quot;&quot;,&#10;		&quot;script&quot;: null,&#10;		&quot;request_limit_fail_open&quot;: false&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>Now, it properly returns all values!</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;bf153a27ba2b464bb9f04dcf75de1ef9&quot;,&#10;		&quot;pattern&quot;: &quot;example.com/*&quot;,&#10;		&quot;script&quot;: &quot;hello-world-script&quot;,&#10;		&quot;request_limit_fail_open&quot;: false&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h4 id="2025-04-15-workers-api-fixes-workers-secrets-api">Workers Secrets API</h4>
<p>The <a href="/api/resources/workers/subresources/scripts/subresources/secrets/">Workers</a> and <a href="/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/secrets/">Workers for Platforms</a> secrets APIs are now properly documented in the Cloudflare OpenAPI docs. Previously, these endpoints were not publicly documented, leaving users confused on how to directly manage their secrets via the API. Now, you can find the proper endpoints in our public documentation, as well as in our API Library SDKs such as <a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a> (&gt;4.2.0) and <a href="https://github.com/cloudflare/cloudflare-python">cloudflare-python</a> (&gt;4.1.0).</p>
<p>Note the <code>cloudflare_workers_secret</code> and <code>cloudflare_workers_for_platforms_script_secret</code> <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform resources</a> are being removed in a future release. This resource is not recommended for managing secrets. Users should instead use the:</p>
<ul>
<li><a href="/api/resources/secrets_store/">Secrets Store</a> with the &quot;Secrets Store Secret&quot; binding on Workers and Workers for Platforms Script Upload</li>
<li>&quot;Secret Text&quot; Binding on <a href="/api/resources/workers/subresources/scripts/methods/update/">Workers Script Upload</a> and <a href="/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/methods/update/">Workers for Platforms Script Upload</a></li>
<li>Workers (and WFP) Secrets API</li>
</ul>


<h2 id="d1-read-replication-public-beta"><a href="/changelog/post/2025-04-10-d1-read-replication-beta/">D1 Read Replication Public Beta</a></h2>
<p><em>2025-04-10</em></p>
<p>D1 read replication is available in public beta to help lower average latency and increase overall throughput for read-heavy applications like e-commerce websites or content management tools.</p>
<p>Workers can leverage read-only database copies, called read replicas, by using D1 <a href="/d1/best-practices/read-replication">Sessions API</a>. A session encapsulates all the queries from one logical session for your application. For example, a session may correspond to all queries coming from a particular web browser session. With Sessions API, D1 queries in a session are guaranteed to be <a href="/d1/best-practices/read-replication/#replica-lag-and-consistency-model">sequentially consistent</a> to avoid data consistency pitfalls. D1 <a href="/d1/reference/time-travel/#bookmarks">bookmarks</a> can be used from a previous session to ensure logical consistency between sessions.</p>
<pre tabindex="0"><code class="language-ts">// retrieve bookmark from previous session stored in HTTP header&#10;const bookmark = request.headers.get(&quot;x-d1-bookmark&quot;) ?? &quot;first-unconstrained&quot;;&#10;&#10;const session = env.DB.withSession(bookmark);&#10;const result = await session&#10;	.prepare(`SELECT * FROM Customers WHERE CompanyName = &#x27;Bs Beverages&#x27;`)&#10;	.run();&#10;// store bookmark for a future session&#10;response.headers.set(&quot;x-d1-bookmark&quot;, session.getBookmark() ?? &quot;&quot;);&#10;</code></pre>
<p>Read replicas are automatically created by Cloudflare (currently one in each supported <a href="/d1/best-practices/read-replication/#read-replica-locations">D1 region</a>), are active/inactive based on query traffic, and are transparently routed to by Cloudflare at no additional cost.</p>
<p>To checkout D1 read replication, deploy the following Worker code using Sessions API, which will prompt you to create a D1 database and enable read replication on said database.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/d1-starter-sessions-api"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>To learn more about how read replication was implemented, go to our <a href="https://blog.cloudflare.com/d1-read-replication-beta">blog post</a>.</p>


<h2 id="cloudflare-pipelines-now-available-in-beta"><a href="/changelog/post/2025-04-10-launching-pipelines/">Cloudflare Pipelines now available in beta</a></h2>
<p><em>2025-04-10</em></p>
<p><a href="/pipelines">Cloudflare Pipelines</a> is now available in beta, to all users with a <a href="/workers/platform/pricing">Workers Paid</a> plan.</p>
<p>Pipelines let you ingest high volumes of real time data, without managing the underlying infrastructure. A single pipeline can ingest up to 100 MB of data per second, via HTTP or from a <a href="/workers">Worker</a>. Ingested data is automatically batched, written to output files, and delivered to an <a href="/r2">R2 bucket</a> in your account. You can use Pipelines to build a data lake of clickstream data, or to store events from a Worker.</p>
<p>Create your first pipeline with a single command:</p>
<pre tabindex="0"><code class="language-bash">$ npx wrangler@latest pipelines create my-clickstream-pipeline --r2-bucket my-bucket&#10;&#10;🌀 Authorizing R2 bucket &quot;my-bucket&quot;&#10;🌀 Creating pipeline named &quot;my-clickstream-pipeline&quot;&#10;✅ Successfully created pipeline my-clickstream-pipeline&#10;&#10;Id:    0e00c5ff09b34d018152af98d06f5a1xvc&#10;Name:  my-clickstream-pipeline&#10;Sources:&#10;  HTTP:&#10;    Endpoint:        https://0e00c5ff09b34d018152af98d06f5a1xvc.pipelines.cloudflare.com/&#10;    Authentication:  off&#10;    Format:          JSON&#10;  Worker:&#10;    Format:  JSON&#10;Destination:&#10;  Type:         R2&#10;  Bucket:       my-bucket&#10;  Format:       newline-delimited JSON&#10;  Compression:  GZIP&#10;Batch hints:&#10;  Max bytes:     100 MB&#10;  Max duration:  300 seconds&#10;  Max records:   100,000&#10;&#10;🎉 You can now send data to your pipeline!&#10;&#10;Send data to your pipeline&#x27;s HTTP endpoint:&#10;curl &quot;https://0e00c5ff09b34d018152af98d06f5a1xvc.pipelines.cloudflare.com/&quot; -d &#x27;[{ ...JSON_DATA... }]&#x27;&#10;&#10;To send data to your pipeline from a Worker, add the following configuration to your config file:&#10;{&#10;  &quot;pipelines&quot;: [&#10;    {&#10;      &quot;pipeline&quot;: &quot;my-clickstream-pipeline&quot;,&#10;      &quot;binding&quot;: &quot;PIPELINE&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>Head over to our <a href="/pipelines/getting-started">getting started guide</a> for an in-depth tutorial to building with Pipelines.</p>


<h2 id="investigate-your-workers-with-the-query-builder-in-the-new-observability-dashboard"><a href="/changelog/post/2025-04-09-qb-workers-logs-ga/">Investigate your Workers with the Query Builder in the new Observability dashboard</a></h2>
<p><em>2025-04-09</em></p>
<p>The <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/">Workers Observability dashboard</a> offers a single place to investigate and explore your <a href="/workers/observability/logs/workers-logs">Workers Logs</a>.</p>
<p>The <strong>Overview</strong> tab shows logs from all your Workers in one place. The <strong>Invocations</strong> view groups logs together by invocation, which refers to the specific trigger that started the execution of the Worker (i.e. fetch). The <strong>Events</strong> view shows logs in the order they were produced, based on timestamp. Previously, you could only view logs for a single Worker.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2025-04-09-workers-observability-overview.png" alt="Workers Observability Overview Tab" /></p>
<p>The <strong>Investigate</strong> tab presents a Query Builder, which helps you write structured queries to investigate and visualize your logs. The Query Builder can help answer questions such as:</p>
<ul>
<li>Which paths are experiencing the most 5XX errors?</li>
<li>What is the wall time distribution by status code for my Worker?</li>
<li>What are the slowest requests, and where are they coming from?</li>
<li>Who are my top N users?</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workers/observability/2025-04-09-query-builder.png" alt="Workers Observability Overview Tab" /></p>
<p>The Query Builder can use any field that you store in your logs as a key to visualize, filter, and group by. Use the Query Builder to quickly access your data, build visualizations, save queries, and share them with your team.</p>
<h4 id="2025-04-09-qb-workers-logs-ga-workers-logs-is-now-generally-available">Workers Logs is now Generally Available</h4>
<p><a href="/workers/observability/logs/workers-logs">Workers Logs</a> is now Generally Available. With a <a href="/workers/observability/logs/workers-logs/#enable-workers-logs">small change</a> to your Wrangler configuration, Workers Logs ingests, indexes, and stores all logs emitted from your Workers for up to 7 days.</p>
<p>We've introduced a number of changes during our beta period, including:</p>
<ul>
<li>Dashboard enhancements with customizable fields as columns in the Logs view and support for invocation-based grouping</li>
<li>Performance improvements to ensure no adverse impact</li>
<li>Public <a href="https://developers.cloudflare.com/api/resources/workers/subresources/observability/">API endpoints</a> for broader consumption</li>
</ul>
<p>The API documents three endpoints: list the keys in the telemetry dataset, run a query, and list the unique values for a key. For more, visit our <a href="https://developers.cloudflare.com/api/resources/workers/subresources/observability/">REST API documentation</a>.</p>
<p>Visit the <a href="/workers/observability/query-builder">docs</a> to learn more about the capabilities and methods exposed by the Query Builder. Start using Workers Logs and the Query Builder today by enabling observability for your Workers:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17771.md")</div>


<h2 id="cpu-time-and-wall-time-now-published-for-workers-invocations"><a href="/changelog/post/2025-04-09-workers-timing/">CPU time and Wall time now published for Workers Invocations</a></h2>
<p><em>2025-04-09</em></p>
<p>You can now observe and investigate the CPU time and Wall time for every Workers Invocations.</p>
<ul>
<li>For <a href="/workers/observability/logs/workers-logs">Workers Logs</a>, CPU time and Wall time are surfaced in the <a href="/workers/observability/logs/workers-logs/#invocation-logs">Invocation Log</a>..</li>
<li>For <a href="/workers/observability/logs/tail-workers">Tail Workers</a>, CPU time and Wall time are surfaced at the top level of the <a href="/logs/logpush/logpush-job/datasets/account/workers_trace_events">Workers Trace Events object</a>.</li>
<li>For <a href="/workers/observability/logs/logpush">Workers Logpush</a>, CPU and Wall time are surfaced at the top level of the <a href="/logs/logpush/logpush-job/datasets/account/workers_trace_events">Workers Trace Events object</a>. All new jobs will have these new fields included by default. Existing jobs need to be updated to include CPU time and Wall time.</li>
</ul>
<p>You can use a Workers Logs filter to search for logs where Wall time exceeds 100ms.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2025-04-09-wall-time-filter.png" alt="Workers Logs Wall Time Filter" /></p>
<p>You can also use the Workers Observability <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/investigate">Query Builder</a> to find the median CPU time and median Wall time for all of your Workers.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2025-04-09-query-builder.png" alt="Query Builder filter" /></p>


<h2 id="deploy-a-workers-application-in-seconds-with-one-click"><a href="/changelog/post/2025-04-08-deploy-to-cloudflare-button/">Deploy a Workers application in seconds with one-click</a></h2>
<p><em>2025-04-08 00:00:00 UTC</em></p>
<p>You can now add a <a href="/workers/platform/deploy-buttons/">Deploy to Cloudflare</a> button to the README of your Git repository containing a Workers application — making it simple for other developers to quickly set up and deploy your project!</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/saas-admin-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>The Deploy to Cloudflare button:</p>
<ol>
<li><strong>Creates a new Git repository on your GitHub/ GitLab account</strong>: Cloudflare will automatically clone and create a new repository on your account, so you can continue developing.</li>
<li><strong>Automatically provisions resources the app needs</strong>: If your repository requires Cloudflare primitives like a <a href="/kv/">Workers KV namespace</a>, a <a href="/d1/">D1 database</a>, or an <a href="/r2/">R2 bucket</a>, Cloudflare will automatically provision them on your account and bind them to your Worker upon deployment.</li>
<li><strong>Configures Workers Builds (CI/CD)</strong>: Every new push to your production branch on your newly created repository will automatically build and deploy courtesy of <a href="/workers/ci-cd/builds/">Workers Builds</a>.</li>
<li><strong>Adds preview URLs to each pull request</strong>: If you'd like to test your changes before deploying, you can push changes to a <a href="/workers/ci-cd/builds/build-branches/#configure-non-production-branch-builds">non-production branch</a> and <a href="/workers/versions-and-deployments/preview-urls/">preview URLs</a> will be generated and <a href="/workers/ci-cd/builds/git-integration/github-integration/#pull-request-comment">posted back to GitHub as a comment</a>.</li>
</ol>
<p><img src="/assets/upstream/images/workers/dtw-user-flow.png" alt="Import repo or choose template" /></p>
<p>To create a Deploy to Cloudflare button in your README, you can add the following snippet, including your Git repository URL:</p>
<pre tabindex="0"><code class="language-md">[<img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare">](https://deploy.workers.cloudflare.com/?url=&lt;YOUR_GIT_REPO_URL&gt;)&#10;</code></pre>
<p>Check out our <a href="/workers/platform/deploy-buttons/">documentation</a> for more information on how to set up a deploy button for your application and best practices to ensure a successful deployment for other developers.</p>


<h2 id="full-stack-frameworks-are-now-generally-available-on-cloudflare-workers"><a href="/changelog/post/2025-04-08-fullstack-on-workers/">Full-stack frameworks are now Generally Available on Cloudflare Workers</a></h2>
<p><em>2025-04-08</em></p>
<img src="/assets/upstream/images/changelog/workers/fullstack-on-workers.png" alt="Full-stack on Cloudflare Workers" />
<p>The following full-stack frameworks now have Generally Available (&quot;GA&quot;) adapters for Cloudflare Workers, and are ready for you to use in production:</p>
<ul>
<li><a href="/workers/framework-guides/web-apps/react-router/">React Router v7 (Remix)</a></li>
<li><a href="/workers/framework-guides/web-apps/astro/">Astro</a></li>
<li><a href="/workers/framework-guides/web-apps/more-web-frameworks/hono/">Hono</a></li>
<li><a href="/workers/framework-guides/web-apps/vue/">Vue.js</a></li>
<li><a href="/workers/framework-guides/web-apps/more-web-frameworks/nuxt/">Nuxt</a></li>
<li><a href="/workers/framework-guides/web-apps/sveltekit/">Svelte (SvelteKit)</a></li>
<li>And <a href="/workers/framework-guides/">more</a>.</li>
</ul>
<p>The following frameworks are now in <strong>beta</strong>, with GA support coming very soon:</p>
<ul>
<li><a href="/workers/framework-guides/web-apps/nextjs/">Next.js</a>, supported through <a href="https://opennext.js.org/cloudflare">@opennextjs/cloudflare</a> is now <code>v1.0-beta</code>.</li>
<li><a href="/workers/framework-guides/web-apps/more-web-frameworks/angular/">Angular</a></li>
<li><a href="/workers/framework-guides/web-apps/more-web-frameworks/solid/">SolidJS (SolidStart)</a></li>
</ul>
<p>You can also build complete full-stack apps on Workers <strong>without a framework</strong>:</p>
<ul>
<li>You can <a href="https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin">“just use Vite&quot;</a> and React together, and build a back-end API in the same Worker. Follow our <a href="/workers/vite-plugin/tutorial/">React SPA with an API tutorial</a> to learn how.</li>
</ul>
<p><strong>Get started building today with our <a href="/workers/framework-guides/">framework guides</a></strong>, or read our <a href="https://blog.cloudflare.com/full-stack-development-on-cloudflare-workers">Developer Week 2025 blog post</a> about all the updates to building full-stack applications on Workers.</p>


<h2 id="improved-support-for-node-js-crypto-and-tls-apis-in-workers"><a href="/changelog/post/2025-04-08-nodejs-crypto-and-tls/">Improved support for Node.js Crypto and TLS APIs in Workers</a></h2>
<p><em>2025-04-08</em></p>
<p>When using a Worker with the <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code></a> compatibility flag enabled,
the following Node.js APIs are now available:</p>
<ul>
<li><a href="/workers/runtime-apis/nodejs/crypto/"><code>node:crypto</code></a></li>
<li><a href="/workers/runtime-apis/nodejs/tls/"><code>node:tls</code></a></li>
</ul>
<p>This make it easier to reuse existing Node.js code in Workers or use npm packages that depend on these APIs.</p>
<h4 id="2025-04-08-nodejs-crypto-and-tls-node-crypto">node:crypto</h4>
<p>The full <a href="https://nodejs.org/api/crypto.html"><code>node:crypto</code></a> API is now available in Workers.</p>
<p>You can use it to verify and sign data:</p>
<pre tabindex="0"><code class="language-js">import { sign, verify } from &quot;node:crypto&quot;;&#10;&#10;const signature = sign(&quot;sha256&quot;, &quot;-data to sign-&quot;, env.PRIVATE_KEY);&#10;const verified = verify(&quot;sha256&quot;, &quot;-data to sign-&quot;, env.PUBLIC_KEY, signature);&#10;</code></pre>
<p>Or, to encrypt and decrypt data:</p>
<pre tabindex="0"><code class="language-js">import { publicEncrypt, privateDecrypt } from &quot;node:crypto&quot;;&#10;&#10;const encrypted = publicEncrypt(env.PUBLIC_KEY, &quot;some data&quot;);&#10;const plaintext = privateDecrypt(env.PRIVATE_KEY, encrypted);&#10;</code></pre>
<p>See the <a href="/workers/runtime-apis/nodejs/crypto/"><code>node:crypto</code> documentation</a> for more information.</p>
<h4 id="2025-04-08-nodejs-crypto-and-tls-node-tls">node:tls</h4>
<p>The following APIs from <code>node:tls</code> are now available:</p>
<ul>
<li><a href="https://nodejs.org/api/tls.html#tlsconnectoptions-callback"><code>connect</code></a></li>
<li><a href="https://nodejs.org/api/tls.html#class-tlstlssocket"><code>TLSSocket</code></a></li>
<li><a href="https://nodejs.org/api/tls.html#tlscheckserveridentityhostname-cert"><code>checkServerIdentity</code></a></li>
<li><a href="https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions"><code>createSecureContext</code></a></li>
</ul>
<p>This enables secure connections over TLS (Transport Layer Security) to external services.</p>
<pre tabindex="0"><code class="language-js">import { connect } from &quot;node:tls&quot;;&#10;&#10;// ... in a request handler ...&#10;const connectionOptions = { key: env.KEY, cert: env.CERT };&#10;const socket = connect(url, connectionOptions, () =&gt; {&#10;	if (socket.authorized) {&#10;		console.log(&quot;Connection authorized&quot;);&#10;	}&#10;});&#10;&#10;socket.on(&quot;data&quot;, (data) =&gt; {&#10;	console.log(data);&#10;});&#10;&#10;socket.on(&quot;end&quot;, () =&gt; {&#10;	console.log(&quot;server ends connection&quot;);&#10;});&#10;</code></pre>
<p>See the <a href="/workers/runtime-apis/nodejs/tls/"><code>node:tls</code> documentation</a> for more information.</p>


<h2 id="the-cloudflare-vite-plugin-is-now-generally-available"><a href="/changelog/post/2025-04-08-vite-plugin/">The Cloudflare Vite plugin is now Generally Available</a></h2>
<p><em>2025-04-08</em></p>
<p>The <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> has <a href="https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin">reached v1.0</a> and is now Generally Available (&quot;GA&quot;).</p>
<p>When you use <code>@cloudflare/vite-plugin</code>, you can use Vite's local development server and build tooling, while ensuring that while developing, your code runs in <a href="https://github.com/cloudflare/workerd"><code>workerd</code></a>, the open-source Workers runtime.</p>
<p>This lets you get the best of both worlds for a full-stack app — you can use <a href="https://vite.dev/guide/features.html#hot-module-replacement">Hot Module Replacement</a> from Vite right alongside <a href="/durable-objects/">Durable Objects</a> and other runtime APIs and bindings that are unique to Cloudflare Workers.</p>
<p><code>@cloudflare/vite-plugin</code> is made possible by the new <a href="https://vite.dev/guide/api-environment">environment API</a> in Vite, and was built <a href="https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin">in partnership with the Vite team</a>.</p>
<h4 id="2025-04-08-vite-plugin-framework-support">Framework support</h4>
<p>You can build any type of application with <code>@cloudflare/vite-plugin</code>, using any rendering mode, from single page applications (SPA) and static sites to server-side rendered (SSR) pages and API routes.</p>
<p><a href="/workers/framework-guides/web-apps/react-router/">React Router v7 (Remix)</a> is the first full-stack framework to provide full support for Cloudflare Vite plugin, allowing you to use all parts of Cloudflare's developer platform, without additional build steps.</p>
<p>You can also build complete full-stack apps on Workers <strong>without a framework</strong> — <a href="https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin">&quot;just use Vite&quot;</a> and React together, and build a back-end API in the same Worker. Follow our <a href="/workers/vite-plugin/tutorial/">React SPA with an API tutorial</a> to learn how.</p>
<h4 id="2025-04-08-vite-plugin-configuration">Configuration</h4>
<p>If you're already using <a href="https://vite.dev/">Vite</a> in your build and development toolchain, you can start using our plugin with minimal changes to your <code>vite.config.ts</code>:</p>
<pre tabindex="0"><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [cloudflare()],&#10;});&#10;</code></pre>
<p>Take a look at the <a href="/workers/vite-plugin/">documentation for our Cloudflare Vite plugin</a> for more information!</p>


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


<h2 id="use-the-latest-javascript-features-with-wrangler-cli-v4"><a href="/changelog/post/2025-03-13-wrangler-v4/">Use the latest JavaScript features with Wrangler CLI v4</a></h2>
<p><em>2025-03-13</em></p>
<p>We've released the next major version of <a href="/workers/wrangler/">Wrangler</a>, the CLI for Cloudflare Workers — <code>wrangler@4.0.0</code>. Wrangler v4 is a major release focused on updates to underlying systems and dependencies, along with improvements to keep Wrangler commands consistent and clear.</p>
<p>You can run the following command to install it in your projects:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i wrangler@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i wrangler@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add wrangler@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add wrangler@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add wrangler@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add wrangler@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add wrangler@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add wrangler@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Unlike previous major versions of Wrangler, which were <a href="https://blog.cloudflare.com/wrangler-v2-beta/">foundational rewrites</a> and <a href="https://blog.cloudflare.com/wrangler3/">rearchitectures</a> — Version 4 of Wrangler includes a much smaller set of changes. If you use Wrangler today, your workflow is very unlikely to change.</p>
<p>A <a href="/workers/wrangler/migration/update-v3-to-v4">detailed migration guide</a> is available and if you find a bug or hit a roadblock when upgrading to Wrangler v4, <a href="https://github.com/cloudflare/workers-sdk/issues/new?template=bug-template.yaml">open an issue on the <code>cloudflare/workers-sdk</code> repository on GitHub</a>.</p>
<p>Going forward, we'll continue supporting Wrangler v3 with bug fixes and security updates until Q1 2026, and with critical security updates until Q1 2027, at which point it will be out of support.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/workers/8/">Previous</a><span>Page 9 of 10</span><a class="pagination-next" rel="next" href="/changelog/product/workers/10/">Next</a></nav>
