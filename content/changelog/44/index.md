<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-04-11">Apr 11, 2025</time><div>
<h2 id="post-2025-04-11-new-models-faster-inference"><a href="/changelog/post/2025-04-11-new-models-faster-inference/">Workers AI for Developer Week - faster inference, new models, async batch API, expanded LoRA support</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>Happy Developer Week 2025! Workers AI is excited to announce a couple of new features and improvements available today. Check out our <a href="https://blog.cloudflare.com/workers-ai-improvements">blog</a> for all the announcement details.</p>
<h4 id="2025-04-11-new-models-faster-inference-faster-inference-new-models">Faster inference + New models</h4>
<p>We’re rolling out some in-place improvements to our models that can help speed up inference by 2-4x! Users of the models below will enjoy an automatic speed boost starting today:</p>
<ul>
<li><a href="/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/"><code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code></a> gets a speed boost of 2-4x, leveraging techniques like speculative decoding, prefix caching, and an updated inference backend.</li>
<li><a href="/workers-ai/models/bge-small-en-v1.5/"><code>@cf/baai/bge-small-en-v1.5</code></a>, <a href="/workers-ai/models/bge-base-en-v1.5/"><code>@cf/baai/bge-base-en-v1.5</code></a>, <a href="/workers-ai/models/bge-large-en-v1.5/"><code>@cf/baai/bge-large-en-v1.5</code></a> get an updated back end, which should improve inference times by 2x.
<ul>
<li>With the <code>bge</code> models, we’re also announcing a new parameter called <code>pooling</code> which can take <code>cls</code> or <code>mean</code> as options. We highly recommend using <code>pooling: cls</code> which will help generate more accurate embeddings. However, embeddings generated with cls pooling are not backwards compatible with mean pooling. For this to not be a breaking change, the default remains as mean pooling. Please specify <code>pooling: cls</code> to enjoy more accurate embeddings going forward.</li>
</ul>
</li>
</ul>
<p>We’re also excited to launch a few new models in our catalog to help round out your experience with Workers AI. We’ll be deprecating some older models in the future, so stay tuned for a deprecation announcement. Today’s new models include:</p>
<ul>
<li><a href="/workers-ai/models/mistral-small-3.1-24b-instruct/"><code>@cf/mistralai/mistral-small-3.1-24b-instruct</code></a>: a 24B parameter model achieving state-of-the-art capabilities comparable to larger models, with support for vision and tool calling.</li>
<li><a href="/workers-ai/models/gemma-3-12b-it/"><code>@cf/google/gemma-3-12b-it</code></a>: well-suited for a variety of text generation and image understanding tasks, including question answering, summarization and reasoning, with a 128K context window, and multilingual support in over 140 languages.</li>
<li><a href="/workers-ai/models/qwq-32b/"><code>@cf/qwen/qwq-32b</code></a>: a medium-sized reasoning model, which is capable of achieving competitive performance against state-of-the-art reasoning models, e.g., DeepSeek-R1, o1-mini.</li>
<li><a href="/workers-ai/models/qwen2.5-coder-32b-instruct/"><code>@cf/qwen/qwen2.5-coder-32b-instruct</code></a>: the current state-of-the-art open-source code LLM, with its coding abilities matching those of GPT-4o.</li>
</ul>
<h4 id="2025-04-11-new-models-faster-inference-batch-inference">Batch Inference</h4>
<p>Introducing a new batch inference feature that allows you to send us an array of requests, which we will fulfill as fast as possible and send them back as an array. This is really helpful for large workloads such as summarization, embeddings, etc. where you don’t have a human-in-the-loop. Using the batch API will guarantee that your requests are fulfilled eventually, rather than erroring out if we don’t have enough capacity at a given time.</p>
<p>Check out the <a href="/workers-ai/features/batch-api/">tutorial</a> to get started! Models that support batch inference today include:</p>
<ul>
<li><a href="/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/"><code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code></a></li>
<li><a href="/workers-ai/models/bge-small-en-v1.5/"><code>@cf/baai/bge-small-en-v1.5</code></a></li>
<li><a href="/workers-ai/models/bge-base-en-v1.5/"><code>@cf/baai/bge-base-en-v1.5</code></a></li>
<li><a href="/workers-ai/models/bge-large-en-v1.5/"><code>@cf/baai/bge-large-en-v1.5</code></a></li>
<li><a href="/workers-ai/models/bge-m3/"><code>@cf/baai/bge-m3</code></a></li>
<li><a href="/workers-ai/models/m2m100-1.2b/"><code>@cf/meta/m2m100-1.2b</code></a></li>
</ul>
<h4 id="2025-04-11-new-models-faster-inference-expanded-lora-support">Expanded LoRA support</h4>
<p>We’ve upgraded our LoRA experience to include 8 newer models, and can support ranks of up to 32 with a 300MB safetensors file limit (previously limited to rank of 8 and 100MB safetensors) Check out our <a href="/workers-ai/features/fine-tunes/loras/">LoRAs page</a> to get started. Models that support LoRAs now include:</p>
<ul>
<li><a href="/workers-ai/models/llama-3.2-11b-vision-instruct/"><code>@cf/meta/llama-3.2-11b-vision-instruct</code></a></li>
<li><a href="/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/"><code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code></a></li>
<li><a href="/workers-ai/models/llama-guard-3-8b/"><code>@cf/meta/llama-guard-3-8b</code></a></li>
<li><a href="/workers-ai/models/llama-3.1-8b-instruct-fast/"><code>@cf/meta/llama-3.1-8b-instruct-fast</code></a> (coming soon)</li>
<li><a href="/workers-ai/models/deepseek-r1-distill-qwen-32b/"><code>@cf/deepseek-ai/deepseek-r1-distill-qwen-32b</code></a> (coming soon)</li>
<li><a href="/workers-ai/models/qwen2.5-coder-32b-instruct/"><code>@cf/qwen/qwen2.5-coder-32b-instruct</code></a></li>
<li><a href="/workers-ai/models/qwq-32b/"><code>@cf/qwen/qwq-32b</code></a></li>
<li><a href="/workers-ai/models/mistral-small-3.1-24b-instruct/"><code>@cf/mistralai/mistral-small-3.1-24b-instruct</code></a></li>
<li><a href="/workers-ai/models/gemma-3-12b-it/"><code>@cf/google/gemma-3-12b-it</code></a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-10">Apr 10, 2025</time><div>
<h2 id="post-2025-04-10-d1-read-replication-beta"><a href="/changelog/post/2025-04-10-d1-read-replication-beta/">D1 Read Replication Public Beta</a></h2>
<div class="changelog-badges"><span>d1</span><span>workers</span></div><div class="changelog-body"><p>D1 read replication is available in public beta to help lower average latency and increase overall throughput for read-heavy applications like e-commerce websites or content management tools.</p>
<p>Workers can leverage read-only database copies, called read replicas, by using D1 <a href="/d1/best-practices/read-replication">Sessions API</a>. A session encapsulates all the queries from one logical session for your application. For example, a session may correspond to all queries coming from a particular web browser session. With Sessions API, D1 queries in a session are guaranteed to be <a href="/d1/best-practices/read-replication/#replica-lag-and-consistency-model">sequentially consistent</a> to avoid data consistency pitfalls. D1 <a href="/d1/reference/time-travel/#bookmarks">bookmarks</a> can be used from a previous session to ensure logical consistency between sessions.</p>
<pre><code class="language-ts">// retrieve bookmark from previous session stored in HTTP header&#10;const bookmark = request.headers.get(&quot;x-d1-bookmark&quot;) ?? &quot;first-unconstrained&quot;;&#10;&#10;const session = env.DB.withSession(bookmark);&#10;const result = await session&#10;	.prepare(`SELECT * FROM Customers WHERE CompanyName = &#x27;Bs Beverages&#x27;`)&#10;	.run();&#10;// store bookmark for a future session&#10;response.headers.set(&quot;x-d1-bookmark&quot;, session.getBookmark() ?? &quot;&quot;);&#10;</code></pre>
<p>Read replicas are automatically created by Cloudflare (currently one in each supported <a href="/d1/best-practices/read-replication/#read-replica-locations">D1 region</a>), are active/inactive based on query traffic, and are transparently routed to by Cloudflare at no additional cost.</p>
<p>To checkout D1 read replication, deploy the following Worker code using Sessions API, which will prompt you to create a D1 database and enable read replication on said database.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/d1-starter-sessions-api"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>To learn more about how read replication was implemented, go to our <a href="https://blog.cloudflare.com/d1-read-replication-beta">blog post</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-10">Apr 10, 2025</time><div>
<h2 id="post-2025-04-10-launching-pipelines"><a href="/changelog/post/2025-04-10-launching-pipelines/">Cloudflare Pipelines now available in beta</a></h2>
<div class="changelog-badges"><span>pipelines</span><span>r2</span><span>workers</span></div><div class="changelog-body"><p><a href="/pipelines">Cloudflare Pipelines</a> is now available in beta, to all users with a <a href="/workers/platform/pricing">Workers Paid</a> plan.</p>
<p>Pipelines let you ingest high volumes of real time data, without managing the underlying infrastructure. A single pipeline can ingest up to 100 MB of data per second, via HTTP or from a <a href="/workers">Worker</a>. Ingested data is automatically batched, written to output files, and delivered to an <a href="/r2">R2 bucket</a> in your account. You can use Pipelines to build a data lake of clickstream data, or to store events from a Worker.</p>
<p>Create your first pipeline with a single command:</p>
<pre><code class="language-bash">$ npx wrangler@latest pipelines create my-clickstream-pipeline --r2-bucket my-bucket&#10;&#10;🌀 Authorizing R2 bucket &quot;my-bucket&quot;&#10;🌀 Creating pipeline named &quot;my-clickstream-pipeline&quot;&#10;✅ Successfully created pipeline my-clickstream-pipeline&#10;&#10;Id:    0e00c5ff09b34d018152af98d06f5a1xvc&#10;Name:  my-clickstream-pipeline&#10;Sources:&#10;  HTTP:&#10;    Endpoint:        https://0e00c5ff09b34d018152af98d06f5a1xvc.pipelines.cloudflare.com/&#10;    Authentication:  off&#10;    Format:          JSON&#10;  Worker:&#10;    Format:  JSON&#10;Destination:&#10;  Type:         R2&#10;  Bucket:       my-bucket&#10;  Format:       newline-delimited JSON&#10;  Compression:  GZIP&#10;Batch hints:&#10;  Max bytes:     100 MB&#10;  Max duration:  300 seconds&#10;  Max records:   100,000&#10;&#10;🎉 You can now send data to your pipeline!&#10;&#10;Send data to your pipeline&#x27;s HTTP endpoint:&#10;curl &quot;https://0e00c5ff09b34d018152af98d06f5a1xvc.pipelines.cloudflare.com/&quot; -d &#x27;[{ ...JSON_DATA... }]&#x27;&#10;&#10;To send data to your pipeline from a Worker, add the following configuration to your config file:&#10;{&#10;  &quot;pipelines&quot;: [&#10;    {&#10;      &quot;pipeline&quot;: &quot;my-clickstream-pipeline&quot;,&#10;      &quot;binding&quot;: &quot;PIPELINE&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>Head over to our <a href="/pipelines/getting-started">getting started guide</a> for an in-depth tutorial to building with Pipelines.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-10">Apr 10, 2025</time><div>
<h2 id="post-2025-04-10-r2-data-catalog-beta"><a href="/changelog/post/2025-04-10-r2-data-catalog-beta/">R2 Data Catalog is a managed Apache Iceberg data catalog built directly into R2 buckets</a></h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p>Today, we are launching <a href="/r2-data-catalog/">R2 Data Catalog</a> in open beta, a managed Apache Iceberg catalog built directly into your <a href="/r2/">Cloudflare R2</a> bucket.</p>
<p>If you are not already familiar with it, <a href="https://iceberg.apache.org/">Apache Iceberg</a> is an open table format designed to handle large-scale analytics datasets stored in object storage, offering ACID transactions and schema evolution. R2 Data Catalog exposes a standard Iceberg REST catalog interface, so you can connect engines like <a href="/r2-data-catalog/config-examples/spark-scala/">Spark</a>, <a href="/r2-data-catalog/config-examples/snowflake/">Snowflake</a>, and <a href="/r2-data-catalog/config-examples/pyiceberg/">PyIceberg</a> to start querying your tables using the tools you already know.</p>
<p>To enable a data catalog on your R2 bucket, find <strong>R2 Data Catalog</strong> in your buckets settings in the dashboard, or run:</p>
<pre><code class="language-bash">npx wrangler r2 bucket catalog enable my-bucket&#10;</code></pre>
<p>And that's it. You'll get a catalog URI and warehouse you can plug into your favorite Iceberg engines.</p>
<p>Visit our <a href="/r2-data-catalog/get-started/">getting started guide</a> for step-by-step instructions on enabling R2 Data Catalog, creating tables, and running your first queries.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-09">Apr 9, 2025</time><div>
<h2 id="post-2025-04-09-SCIM-provisioning-logs"><a href="/changelog/post/2025-04-09-SCIM-provisioning-logs/">Cloudflare Zero Trust SCIM User and Group Provisioning Logs</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/team-and-resources/users/scim">Cloudflare Zero Trust SCIM provisioning</a> now has a full audit log of all create, update and delete event from any SCIM Enabled IdP. The <a href="/cloudflare-one/insights/logs/dashboard-logs/scim-logs/">SCIM logs</a> support filtering by IdP, Event type, Result and many more fields. This will help with debugging user and group update issues and questions.</p>
<p>SCIM logs can be found on the Zero Trust Dashboard under <strong>Logs</strong> -&gt; <strong>SCIM provisioning</strong>.</p>
<p><img src="/assets/upstream/images/changelog/access/example-scim-log.png" alt="Example SCIM Logs" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-09">Apr 9, 2025</time><div>
<h2 id="post-2025-04-09-hyperdrive-custom-certificate-support"><a href="/changelog/post/2025-04-09-hyperdrive-custom-certificate-support/">Hyperdrive now supports custom TLS/SSL certificates</a></h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>Hyperdrive now supports more SSL/TLS security options for your database connections:</p>
<ul>
<li>Configure Hyperdrive to verify server certificates with <code>verify-ca</code> or <code>verify-full</code> SSL modes and protect against man-in-the-middle attacks</li>
<li>Configure Hyperdrive to provide client certificates to the database server to authenticate itself (mTLS) for stronger security beyond username and password</li>
</ul>
<p>Use the new <code>wrangler cert</code> commands to create certificate authority (CA) certificate bundles or client certificate pairs:</p>
<pre><code class="language-bash">&#35; Create CA certificate bundle&#10;npx wrangler cert upload certificate-authority --ca-cert your-ca-cert.pem --name your-custom-ca-name&#10;&#10;&#35; Create client certificate pair&#10;npx wrangler cert upload mtls-certificate --cert client-cert.pem --key client-key.pem --name your-client-cert-name&#10;</code></pre>
<p>Then create a Hyperdrive configuration with the certificates and desired SSL mode:</p>
<pre><code class="language-bash">npx wrangler hyperdrive create your-hyperdrive-config \&#10;  &#45;-connection-string=&quot;postgres://user:password@hostname:port/database&quot; \&#10;  &#45;-ca-certificate-id &lt;CA_CERT_ID&gt; \&#10;  &#45;-mtls-certificate-id &lt;CLIENT_CERT_ID&gt;&#10;  &#45;-sslmode verify-full&#10;</code></pre>
<p>Learn more about <a href="/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/">configuring SSL/TLS certificates for Hyperdrive</a> to enhance your database security posture.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-09">Apr 9, 2025</time><div>
<h2 id="post-2025-04-09-snippets-ga"><a href="/changelog/post/2025-04-09-snippets-ga/">Cloudflare Snippets are now Generally Available</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/changelog/rules/snippets-ga.png" alt="Cloudflare Snippets are now GA" /></p>
<p><a href="/rules/snippets/">Cloudflare Snippets</a> are now generally available at no extra cost across all paid plans — giving you a fast, flexible way to programmatically control HTTP traffic using lightweight JavaScript.</p>
<p>You can now use Snippets to modify HTTP requests and responses with confidence, reliability, and scale. Snippets are production-ready and deeply integrated with Cloudflare Rules, making them ideal for everything from quick dynamic header rewrites to advanced routing logic.</p>
<p>What's new:</p>
<ul>
<li><strong>Snippets are now GA</strong> – Available at no extra cost on all Pro, Business, and Enterprise plans.</li>
<li><strong>Ready for production</strong> – Snippets deliver a production-grade experience built for scale.</li>
<li><strong>Part of the Cloudflare Rules platform</strong> – Snippets inherit request modifications from other Cloudflare products and support sequential execution, allowing you to run multiple Snippets on the same request and apply custom modifications step by step.</li>
<li><strong>Trace integration</strong> – Use <a href="/rules/trace-request/">Cloudflare Trace</a> to see which Snippets were triggered on a request — helping you understand traffic flow and debug more effectively.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/rules/snippets-ga-trace.gif" alt="Snippets shown in Cloudflare Trace results" /></p>
<p>Learn more in the <a href="https://blog.cloudflare.com/snippets/">launch blog post</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-09">Apr 9, 2025</time><div>
<h2 id="post-2025-04-09-secrets-store-beta"><a href="/changelog/post/2025-04-09-secrets-store-beta/">Cloudflare Secrets Store now available in Beta</a></h2>
<div class="changelog-badges"><span>secrets-store</span><span>ssl</span></div><div class="changelog-body"><p>Cloudflare Secrets Store is available today in Beta. You can now store, manage, and deploy account level secrets from a secure, centralized platform to your Workers.</p>
<p><img src="/assets/upstream/images/ssl/secrets-store-landing-page.png" alt="Import repo or choose template" /></p>
<p>To spin up your Cloudflare Secrets Store, simply click the new Secrets Store tab <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">in the dashboard</a> or use this Wrangler command:</p>
<pre><code class="language-sh">wrangler secrets-store store create &lt;name&gt; --remote&#10;</code></pre>
<p>The following are supported in the Secrets Store beta:</p>
<ul>
<li>Secrets Store UI &amp; API: create your store &amp; create, duplicate, update, scope, and delete a secret</li>
<li>Workers UI: bind a new or existing account level secret to a Worker and deploy in code</li>
<li>Wrangler: create your store &amp; create, duplicate, update, scope, and delete a secret</li>
<li>Account Management UI &amp; API: assign Secrets Store permissions roles &amp; view audit logs for actions taken in Secrets Store core platform</li>
</ul>
<p>For instructions on how to get started, visit our <a href="/secrets-store/">developer documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-09">Apr 9, 2025</time><div>
<h2 id="post-2025-04-09-qb-workers-logs-ga"><a href="/changelog/post/2025-04-09-qb-workers-logs-ga/">Investigate your Workers with the Query Builder in the new Observability dashboard</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/">Workers Observability dashboard</a> offers a single place to investigate and explore your <a href="/workers/observability/logs/workers-logs">Workers Logs</a>.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-09">Apr 9, 2025</time><div>
<h2 id="post-2025-04-09-workers-timing"><a href="/changelog/post/2025-04-09-workers-timing/">CPU time and Wall time now published for Workers Invocations</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now observe and investigate the CPU time and Wall time for every Workers Invocations.</p>
<ul>
<li>For <a href="/workers/observability/logs/workers-logs">Workers Logs</a>, CPU time and Wall time are surfaced in the <a href="/workers/observability/logs/workers-logs/#invocation-logs">Invocation Log</a>..</li>
<li>For <a href="/workers/observability/logs/tail-workers">Tail Workers</a>, CPU time and Wall time are surfaced at the top level of the <a href="/logs/logpush/logpush-job/datasets/account/workers_trace_events">Workers Trace Events object</a>.</li>
<li>For <a href="/workers/observability/logs/logpush">Workers Logpush</a>, CPU and Wall time are surfaced at the top level of the <a href="/logs/logpush/logpush-job/datasets/account/workers_trace_events">Workers Trace Events object</a>. All new jobs will have these new fields included by default. Existing jobs need to be updated to include CPU time and Wall time.</li>
</ul>
<p>You can use a Workers Logs filter to search for logs where Wall time exceeds 100ms.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2025-04-09-wall-time-filter.png" alt="Workers Logs Wall Time Filter" /></p>
<p>You can also use the Workers Observability <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/investigate">Query Builder</a> to find the median CPU time and median Wall time for all of your Workers.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2025-04-09-query-builder.png" alt="Query Builder filter" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-08">Apr 8, 2025</time><div>
<h2 id="post-2025-04-08-deploy-to-cloudflare-button"><a href="/changelog/post/2025-04-08-deploy-to-cloudflare-button/">Deploy a Workers application in seconds with one-click</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now add a <a href="/workers/platform/deploy-buttons/">Deploy to Cloudflare</a> button to the README of your Git repository containing a Workers application — making it simple for other developers to quickly set up and deploy your project!</p>
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
<pre><code class="language-md">[<img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare">](https://deploy.workers.cloudflare.com/?url=&lt;YOUR_GIT_REPO_URL&gt;)&#10;</code></pre>
<p>Check out our <a href="/workers/platform/deploy-buttons/">documentation</a> for more information on how to set up a deploy button for your application and best practices to ensure a successful deployment for other developers.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-08">Apr 8, 2025</time><div>
<h2 id="post-2025-04-08-local-development"><a href="/changelog/post/2025-04-08-local-development/">Local development support for Email Workers</a></h2>
<div class="changelog-badges"><span>email-service</span></div><div class="changelog-body"><p>Email Workers enables developers to programmatically take action on anything that hits their email inbox. If you're building with Email Workers, you can now test the behavior of an Email Worker script, receiving, replying and sending emails in your local environment using <code>wrangler dev</code>.</p>
<p>Below is an example that shows you how you can receive messages using the <code>email()</code> handler and parse them using <a href="https://www.npmjs.com/package/postal-mime">postal-mime</a>:</p>
<pre><code class="language-ts">import * as PostalMime from &quot;postal-mime&quot;;&#10;&#10;export default {&#10;	async email(message, env, ctx) {&#10;		const parser = new PostalMime.default();&#10;		const rawEmail = new Response(message.raw);&#10;		const email = await parser.parse(await rawEmail.arrayBuffer());&#10;		console.log(email);&#10;	},&#10;};&#10;</code></pre>
<p>Now when you run <code>npx wrangler dev</code>, wrangler will expose a local <code>/cdn-cgi/local/email</code> endpoint that you can <code>POST</code> email messages to and trigger your Worker's <code>email()</code> handler:</p>
<pre><code class="language-bash">curl -X POST &#x27;http://localhost:8787/cdn-cgi/local/email&#x27; \&#10;  &#45;-url-query &#x27;from=sender@example.com&#x27; \&#10;  &#45;-url-query &#x27;to=recipient@example.com&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data-raw &#x27;Received: from smtp.example.com (127.0.0.1)&#10;        by cloudflare-email.com (unknown) id 4fwwffRXOpyR&#10;        for &lt;recipient@example.com&gt;; Tue, 27 Aug 2024 15:50:20 +0000&#10;From: &quot;John&quot; &lt;sender@example.com&gt;&#10;Reply-To: sender@example.com&#10;To: recipient@example.com&#10;Subject: Testing Email Workers Local Dev&#10;Content-Type: text/html; charset=&quot;windows-1252&quot;&#10;X-Mailer: Curl&#10;Date: Tue, 27 Aug 2024 08:49:44 -0700&#10;Message-ID: &lt;6114391943504294873000@ZSH-GHOSTTY&gt;&#10;&#10;Hi there&#x27;&#10;</code></pre>
<p>This is what you get in the console:</p>
<pre><code class="language-json">{&#10;	&quot;headers&quot;: [&#10;		{&#10;			&quot;key&quot;: &quot;received&quot;,&#10;			&quot;value&quot;: &quot;from smtp.example.com (127.0.0.1) by cloudflare-email.com (unknown) id 4fwwffRXOpyR for &lt;recipient@example.com&gt;; Tue, 27 Aug 2024 15:50:20 +0000&quot;&#10;		},&#10;		{ &quot;key&quot;: &quot;from&quot;, &quot;value&quot;: &quot;\&quot;John\&quot; &lt;sender@example.com&gt;&quot; },&#10;		{ &quot;key&quot;: &quot;reply-to&quot;, &quot;value&quot;: &quot;sender@example.com&quot; },&#10;		{ &quot;key&quot;: &quot;to&quot;, &quot;value&quot;: &quot;recipient@example.com&quot; },&#10;		{ &quot;key&quot;: &quot;subject&quot;, &quot;value&quot;: &quot;Testing Email Workers Local Dev&quot; },&#10;		{ &quot;key&quot;: &quot;content-type&quot;, &quot;value&quot;: &quot;text/html; charset=\&quot;windows-1252\&quot;&quot; },&#10;		{ &quot;key&quot;: &quot;x-mailer&quot;, &quot;value&quot;: &quot;Curl&quot; },&#10;		{ &quot;key&quot;: &quot;date&quot;, &quot;value&quot;: &quot;Tue, 27 Aug 2024 08:49:44 -0700&quot; },&#10;		{&#10;			&quot;key&quot;: &quot;message-id&quot;,&#10;			&quot;value&quot;: &quot;&lt;6114391943504294873000@ZSH-GHOSTTY&gt;&quot;&#10;		}&#10;	],&#10;	&quot;from&quot;: { &quot;address&quot;: &quot;sender@example.com&quot;, &quot;name&quot;: &quot;John&quot; },&#10;	&quot;to&quot;: [{ &quot;address&quot;: &quot;recipient@example.com&quot;, &quot;name&quot;: &quot;&quot; }],&#10;	&quot;replyTo&quot;: [{ &quot;address&quot;: &quot;sender@example.com&quot;, &quot;name&quot;: &quot;&quot; }],&#10;	&quot;subject&quot;: &quot;Testing Email Workers Local Dev&quot;,&#10;	&quot;messageId&quot;: &quot;&lt;6114391943504294873000@ZSH-GHOSTTY&gt;&quot;,&#10;	&quot;date&quot;: &quot;2024-08-27T15:49:44.000Z&quot;,&#10;	&quot;html&quot;: &quot;Hi there\n&quot;,&#10;	&quot;attachments&quot;: []&#10;}&#10;</code></pre>
<p>Local development is a critical part of the development flow, and also works for sending, replying and forwarding emails. See <a href="/email-service/local-development/routing/">our documentation</a> for more information.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-08">Apr 8, 2025</time><div>
<h2 id="post-2025-04-08-hyperdrive-free-plan"><a href="/changelog/post/2025-04-08-hyperdrive-free-plan/">Hyperdrive Free plan makes fast, global database access available to all</a></h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>Hyperdrive is now available on the Free plan of Cloudflare Workers, enabling you to build Workers that connect to PostgreSQL or MySQL databases without compromise.</p>
<p>Low-latency access to SQL databases is critical to building full-stack Workers applications. We want you to be able to build on fast, global apps on Workers,
regardless of the tools you use. So we made Hyperdrive available for all, to make it easier to build Workers that connect to PostgreSQL and MySQL.</p>
<p>If you want to learn more about how Hyperdrive works, read the <a href="https://blog.cloudflare.com/how-hyperdrive-speeds-up-database-access">deep dive</a> on how Hyperdrive can make your database queries up to 4x faster.</p>
<p><img src="/assets/upstream/images/hyperdrive/configuration/hyperdrive-global-placement.png" alt="Hyperdrive provides edge connection setup and global connection pooling for optimal latencies." /></p>
<p>Visit the docs to <a href="/hyperdrive/get-started/">get started</a> with Hyperdrive for PostgreSQL or MySQL.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-08">Apr 8, 2025</time><div>
<h2 id="post-2025-04-08-hyperdrive-mysql-support"><a href="/changelog/post/2025-04-08-hyperdrive-mysql-support/">Hyperdrive introduces support for MySQL and MySQL-compatible databases</a></h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>Hyperdrive now supports connecting to MySQL and MySQL-compatible databases, including Amazon RDS and Aurora MySQL, Google Cloud SQL for MySQL, Azure Database for MySQL, PlanetScale and MariaDB.</p>
<p>Hyperdrive makes your regional, MySQL databases fast when connecting from Cloudflare Workers. It eliminates unnecessary network roundtrips during connection setup, pools database connections globally, and can cache query results to provide the fastest possible response times.</p>
<p>Best of all, you can connect using your existing drivers, ORMs, and query builders with Hyperdrive's secure credentials, no code changes required.</p>
<pre><code class="language-ts">import { createConnection } from &quot;mysql2/promise&quot;;&#10;&#10;export interface Env {&#10;	HYPERDRIVE: Hyperdrive;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		const connection = await createConnection({&#10;			host: env.HYPERDRIVE.host,&#10;			user: env.HYPERDRIVE.user,&#10;			password: env.HYPERDRIVE.password,&#10;			database: env.HYPERDRIVE.database,&#10;			port: env.HYPERDRIVE.port,&#10;			disableEval: true, // Required for Workers compatibility&#10;		});&#10;&#10;		const [results, fields] = await connection.query(&quot;SHOW tables;&quot;);&#10;&#10;		ctx.waitUntil(connection.end());&#10;&#10;		return new Response(JSON.stringify({ results, fields }), {&#10;			headers: {&#10;				&quot;Content-Type&quot;: &quot;application/json&quot;,&#10;				&quot;Access-Control-Allow-Origin&quot;: &quot;*&quot;,&#10;			},&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">how Hyperdrive works</a> and <a href="/hyperdrive/get-started/">get started building Workers that connect to MySQL with Hyperdrive</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-08">Apr 8, 2025</time><div>
<h2 id="post-2025-04-08-fullstack-on-workers"><a href="/changelog/post/2025-04-08-fullstack-on-workers/">Full-stack frameworks are now Generally Available on Cloudflare Workers</a></h2>
<div class="changelog-badges"><span>workers</span><span>workers-for-platforms</span></div><div class="changelog-body"><img src="/assets/upstream/images/changelog/workers/fullstack-on-workers.png" alt="Full-stack on Cloudflare Workers" />
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-08">Apr 8, 2025</time><div>
<h2 id="post-2025-04-08-nodejs-crypto-and-tls"><a href="/changelog/post/2025-04-08-nodejs-crypto-and-tls/">Improved support for Node.js Crypto and TLS APIs in Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>When using a Worker with the <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code></a> compatibility flag enabled,
the following Node.js APIs are now available:</p>
<ul>
<li><a href="/workers/runtime-apis/nodejs/crypto/"><code>node:crypto</code></a></li>
<li><a href="/workers/runtime-apis/nodejs/tls/"><code>node:tls</code></a></li>
</ul>
<p>This make it easier to reuse existing Node.js code in Workers or use npm packages that depend on these APIs.</p>
<h4 id="2025-04-08-nodejs-crypto-and-tls-node-crypto">node:crypto</h4>
<p>The full <a href="https://nodejs.org/api/crypto.html"><code>node:crypto</code></a> API is now available in Workers.</p>
<p>You can use it to verify and sign data:</p>
<pre><code class="language-js">import { sign, verify } from &quot;node:crypto&quot;;&#10;&#10;const signature = sign(&quot;sha256&quot;, &quot;-data to sign-&quot;, env.PRIVATE_KEY);&#10;const verified = verify(&quot;sha256&quot;, &quot;-data to sign-&quot;, env.PUBLIC_KEY, signature);&#10;</code></pre>
<p>Or, to encrypt and decrypt data:</p>
<pre><code class="language-js">import { publicEncrypt, privateDecrypt } from &quot;node:crypto&quot;;&#10;&#10;const encrypted = publicEncrypt(env.PUBLIC_KEY, &quot;some data&quot;);&#10;const plaintext = privateDecrypt(env.PRIVATE_KEY, encrypted);&#10;</code></pre>
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
<pre><code class="language-js">import { connect } from &quot;node:tls&quot;;&#10;&#10;// ... in a request handler ...&#10;const connectionOptions = { key: env.KEY, cert: env.CERT };&#10;const socket = connect(url, connectionOptions, () =&gt; {&#10;	if (socket.authorized) {&#10;		console.log(&quot;Connection authorized&quot;);&#10;	}&#10;});&#10;&#10;socket.on(&quot;data&quot;, (data) =&gt; {&#10;	console.log(data);&#10;});&#10;&#10;socket.on(&quot;end&quot;, () =&gt; {&#10;	console.log(&quot;server ends connection&quot;);&#10;});&#10;</code></pre>
<p>See the <a href="/workers/runtime-apis/nodejs/tls/"><code>node:tls</code> documentation</a> for more information.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-08">Apr 8, 2025</time><div>
<h2 id="post-2025-04-08-vite-plugin"><a href="/changelog/post/2025-04-08-vite-plugin/">The Cloudflare Vite plugin is now Generally Available</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> has <a href="https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin">reached v1.0</a> and is now Generally Available (&quot;GA&quot;).</p>
<p>When you use <code>@cloudflare/vite-plugin</code>, you can use Vite's local development server and build tooling, while ensuring that while developing, your code runs in <a href="https://github.com/cloudflare/workerd"><code>workerd</code></a>, the open-source Workers runtime.</p>
<p>This lets you get the best of both worlds for a full-stack app — you can use <a href="https://vite.dev/guide/features.html#hot-module-replacement">Hot Module Replacement</a> from Vite right alongside <a href="/durable-objects/">Durable Objects</a> and other runtime APIs and bindings that are unique to Cloudflare Workers.</p>
<p><code>@cloudflare/vite-plugin</code> is made possible by the new <a href="https://vite.dev/guide/api-environment">environment API</a> in Vite, and was built <a href="https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin">in partnership with the Vite team</a>.</p>
<h4 id="2025-04-08-vite-plugin-framework-support">Framework support</h4>
<p>You can build any type of application with <code>@cloudflare/vite-plugin</code>, using any rendering mode, from single page applications (SPA) and static sites to server-side rendered (SSR) pages and API routes.</p>
<p><a href="/workers/framework-guides/web-apps/react-router/">React Router v7 (Remix)</a> is the first full-stack framework to provide full support for Cloudflare Vite plugin, allowing you to use all parts of Cloudflare's developer platform, without additional build steps.</p>
<p>You can also build complete full-stack apps on Workers <strong>without a framework</strong> — <a href="https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin">&quot;just use Vite&quot;</a> and React together, and build a back-end API in the same Worker. Follow our <a href="/workers/vite-plugin/tutorial/">React SPA with an API tutorial</a> to learn how.</p>
<h4 id="2025-04-08-vite-plugin-configuration">Configuration</h4>
<p>If you're already using <a href="https://vite.dev/">Vite</a> in your build and development toolchain, you can start using our plugin with minimal changes to your <code>vite.config.ts</code>:</p>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [cloudflare()],&#10;});&#10;</code></pre>
<p>Take a look at the <a href="/workers/vite-plugin/">documentation for our Cloudflare Vite plugin</a> for more information!</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-07">Apr 7, 2025</time><div>
<h2 id="post-2025-04-07-mcp-servers-agents-sdk-updates"><a href="/changelog/post/2025-04-07-mcp-servers-agents-sdk-updates/">Build MCP servers with the Agents SDK</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The Agents SDK now includes built-in support for building remote MCP (Model Context Protocol) servers directly as part of your Agent. This allows you to easily create and manage MCP servers, without the need for additional infrastructure or configuration.</p>
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
<pre><code class="language-sh">npm create cloudflare@latest -- --template cloudflare/agents-starter&#10;</code></pre>
<p>See the full release notes and changelog <a href="https://github.com/cloudflare/agents/blob/main/packages/agents/CHANGELOG.md">on the Agents SDK repository</a> and</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-07">Apr 7, 2025</time><div>
<h2 id="post-2025-04-07-autorag-open-beta"><a href="/changelog/post/2025-04-07-autorag-open-beta/">Create fully-managed RAG pipelines for your AI applications with AutoRAG</a></h2>
<div class="changelog-badges"><span>ai-search</span><span>vectorize</span></div><div class="changelog-body"><p><a href="/ai-search/">AutoRAG</a> is now in open beta, making it easy for you to build fully-managed retrieval-augmented generation (RAG) pipelines without managing infrastructure. Just upload your docs to <a href="/r2/get-started/">R2</a>, and AutoRAG handles the rest: embeddings, indexing, retrieval, and response generation via API.</p>
<p>With AutoRAG, you can:</p>
<ul>
<li><strong>Customize your pipeline:</strong> Choose from <a href="/workers-ai">Workers AI</a> models, configure chunking strategies, edit system prompts, and more.</li>
<li><strong>Instant setup:</strong> AutoRAG provisions everything you need from <a href="/vectorize">Vectorize</a>, <a href="/ai-gateway">AI gateway</a>, to pipeline logic for you, so you can go from zero to a working RAG pipeline in seconds.</li>
<li><strong>Keep your index fresh:</strong> AutoRAG continuously syncs your index with your data source to ensure responses stay accurate and up to date.</li>
<li><strong>Ask questions:</strong> Query your data and receive grounded responses via a <a href="/ai-search/api/search/workers-binding/">Workers binding</a> or <a href="/ai-search/api/search/rest-api/">API</a>.</li>
</ul>
<p>Whether you're building internal tools, AI-powered search, or a support assistant, AutoRAG gets you from idea to deployment in minutes.</p>
<p>Get started in the <a href="https://dash.cloudflare.com/?to=/:account/ai/autorag">Cloudflare dashboard</a> or check out the <a href="/ai-search/get-started/">guide</a> for instructions on how to build your RAG pipeline today.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-07">Apr 7, 2025</time><div>
<h2 id="post-2025-04-07-br-free-ga-playwright"><a href="/changelog/post/2025-04-07-br-free-ga-playwright/">Browser Rendering REST API is Generally Available, with new endpoints and a free tier</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>We’re excited to announce Browser Rendering is now available on the <a href="https://www.cloudflare.com/plans/developer-platform/">Workers Free plan</a>, making it even easier to prototype and experiment with web search and headless browser use-cases when building applications on Workers.</p>
<p>The Browser Rendering <strong><a href="/browser-run/quick-actions/">REST API</a> is now Generally Available</strong>, allowing you to control browser instances from outside of Workers applications. We've added three new endpoints to help automate more browser tasks:</p>
<ul>
<li><strong>Extract structured data</strong> – Use <code>/json</code> to retrieve structured data from a webpage.</li>
<li><strong>Retrieve links</strong> – Use <code>/links</code> to pull all links from a webpage.</li>
<li><strong>Convert to Markdown</strong> – Use <code>/markdown</code> to convert webpage content into Markdown format.</li>
</ul>
<p>For example, to fetch the Markdown representation of a webpage:</p>
<pre><code class="language-bash">curl -X &#x27;POST&#x27; &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/markdown&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;&#10;  }&#x27;&#10;</code></pre>
<p>For the full list of endpoints, check out our <a href="/browser-run/quick-actions/">REST API documentation</a>. You can also interact with Browser Rendering via the <a href="https://github.com/cloudflare/cloudflare-typescript">Cloudflare TypeScript SDK</a>.</p>
<p>We also recently landed support for <a href="/browser-run/playwright/">Playwright</a> in Browser Rendering for browser automation from Cloudflare <a href="/workers/">Workers</a>, in addition to <a href="/browser-run/puppeteer/">Puppeteer</a>, giving you more flexibility to test across different browser environments.</p>
<p>Visit the <a href="/browser-run/">Browser Rendering docs</a> to learn more about how to use headless browsers in your applications.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-07">Apr 7, 2025</time><div>
<h2 id="post-2025-04-07-durable-objects-free-tier"><a href="/changelog/post/2025-04-07-durable-objects-free-tier/">Durable Objects on Workers Free plan</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>Durable Objects can now be used with zero commitment on the <a href="/workers/platform/pricing/">Workers Free plan</a> allowing you to build AI agents with <a href="/agents/">Agents SDK</a>, collaboration tools, and real-time applications like chat or multiplayer games.</p>
<p>Durable Objects let you build stateful, serverless applications with millions of tiny coordination instances that run your application code alongside (in the same thread!) your durable storage. Each Durable Object can access its own SQLite database through a <a href="/durable-objects/best-practices/access-durable-objects-storage/">Storage API</a>. A Durable Object class is defined in a Worker script encapsulating the Durable Object's behavior when accessed from a Worker. To try the code below, click the button:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/hello-world-do-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<pre><code class="language-js">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;// Durable Object&#10;export class MyDurableObject extends DurableObject {&#10;  ...&#10;	async sayHello(name) {&#10;		return `Hello, ${name}!`;&#10;	}&#10;}&#10;&#10;// Worker&#10;export default {&#10;	async fetch(request, env) {&#10;		// Every unique ID refers to an individual instance of the Durable Object class&#10;		const id = env.MY_DURABLE_OBJECT.idFromName(&quot;foo&quot;);&#10;&#10;		// A stub is a client used to invoke methods on the Durable Object&#10;		const stub = env.MY_DURABLE_OBJECT.get(id);&#10;&#10;		// Methods on the Durable Object are invoked via the stub&#10;		const response = await stub.sayHello(&quot;world&quot;);&#10;&#10;		return response;&#10;	},&#10;};&#10;</code></pre>
<p>Free plan <a href="/durable-objects/platform/pricing/">limits</a> apply to Durable Objects compute and storage usage. Limits allow developers to build real-world applications, with every Worker request able to call a Durable Object on the free plan.</p>
<p>For more information, checkout:</p>
<ul>
<li><a href="/durable-objects/concepts/what-are-durable-objects/">Documentation</a></li>
<li><a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">Zero-latency SQLite storage in every Durable Object blog</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-07">Apr 7, 2025</time><div>
<h2 id="post-2025-04-07-sqlite-in-durable-objects-ga"><a href="/changelog/post/2025-04-07-sqlite-in-durable-objects-ga/">SQLite in Durable Objects GA with 10GB storage per object</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>SQLite in Durable Objects is now generally available (GA) with 10GB SQLite database per Durable Object. Since the <a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">public beta</a> in September 2024, we've added feature parity and robustness for the SQLite storage backend compared to the preexisting key-value (KV) storage backend for Durable Objects.</p>
<p>SQLite-backed Durable Objects are recommended for all new Durable Object classes, using <code>new_sqlite_classes</code> <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">Wrangler configuration</a>. Only SQLite-backed Durable Objects have access to Storage API's <a href="/durable-objects/api/sqlite-storage-api/#sql-api">SQL</a> and <a href="/durable-objects/api/sqlite-storage-api/#pitr-point-in-time-recovery-api">point-in-time recovery</a> methods, which provide relational data modeling, SQL querying, and better data management.</p>
<pre><code class="language-js">export class MyDurableObject extends DurableObject {&#10;  sql: SqlStorage&#10;  constructor(ctx: DurableObjectState, env: Env) {&#10;    super(ctx, env);&#10;    this.sql = ctx.storage.sql;&#10;  }&#10;&#10;  async sayHello() {&#10;    let result = this.sql&#10;      .exec(&quot;SELECT &#x27;Hello, World!&#x27; AS greeting&quot;)&#10;      .one();&#10;    return result.greeting;&#10;  }&#10;}&#10;</code></pre>
<p>KV-backed Durable Objects remain for backwards compatibility, and a migration path from key-value storage to SQL storage for existing Durable Object classes will be offered in the future.</p>
<p>For more details on SQLite storage, checkout <a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">Zero-latency SQLite storage in every Durable Object blog</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-07">Apr 7, 2025</time><div>
<h2 id="post-2025-04-07-increase-trace-events-limit"><a href="/changelog/post/2025-04-07-increase-trace-events-limit/">Capture up to 256 KB of log events in each Workers Invocation</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now capture a maximum of 256 KB of log events per Workers invocation, helping you gain better visibility into application behavior.</p>
<p>All console.log() statements, exceptions, request metadata, and headers are automatically captured during the Worker invocation and emitted
as <a href="/logs/logpush/logpush-job/datasets/account/workers_trace_events">JSON object</a>. <a href="/workers/observability/logs/workers-logs">Workers Logs</a> deserializes
this object before indexing the fields and storing them. You can also capture, transform, and export the JSON object in a
<a href="/workers/observability/logs/tail-workers">Tail Worker</a>.</p>
<p>256 KB is a 2x increase from the previous 128 KB limit. After you exceed this limit, further context associated with the request will not be
recorded in your logs.</p>
<p>This limit is automatically applied to all Workers.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-07">Apr 7, 2025</time><div>
<h2 id="post-2025-04-07-workflows-ga"><a href="/changelog/post/2025-04-07-workflows-ga/">Workflows is now Generally Available</a></h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> is now <em>Generally Available</em> (or &quot;GA&quot;): in short, it's ready for production workloads. Alongside marking Workflows as GA, we've introduced a number of changes during the beta period, including:</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-04-04">Apr 4, 2025</time><div>
<h2 id="post-2025-04-04-playwright-beta"><a href="/changelog/post/2025-04-04-playwright-beta/">Playwright for Browser Rendering now available</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>We're excited to share that you can now use Playwright's browser automation <a href="https://playwright.dev/docs/api/class-playwright">capabilities</a> from Cloudflare <a href="/workers/">Workers</a>.</p>
<p><a href="https://playwright.dev/">Playwright</a> is an open-source package developed by Microsoft that can do browser automation tasks; it's commonly used to write software tests, debug applications, create screenshots, and crawl pages. Like <a href="/browser-run/puppeteer/">Puppeteer</a>, we <a href="https://github.com/cloudflare/playwright">forked</a> Playwright and modified it to be compatible with Cloudflare Workers and <a href="/browser-run/">Browser Rendering</a>.</p>
<p>Below is an example of how to use Playwright with Browser Rendering to test a TODO application using assertions:</p>
<pre><code class="language-ts">import { launch, type BrowserWorker } from &quot;@cloudflare/playwright&quot;;&#10;import { expect } from &quot;@cloudflare/playwright/test&quot;;&#10;&#10;interface Env {&#10;	MYBROWSER: BrowserWorker;&#10;}&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env) {&#10;		const browser = await launch(env.MYBROWSER);&#10;		const page = await browser.newPage();&#10;&#10;		await page.goto(&quot;https://demo.playwright.dev/todomvc&quot;);&#10;&#10;		const TODO_ITEMS = [&#10;			&quot;buy some cheese&quot;,&#10;			&quot;feed the cat&quot;,&#10;			&quot;book a doctors appointment&quot;,&#10;		];&#10;&#10;		const newTodo = page.getByPlaceholder(&quot;What needs to be done?&quot;);&#10;		for (const item of TODO_ITEMS) {&#10;			await newTodo.fill(item);&#10;			await newTodo.press(&quot;Enter&quot;);&#10;		}&#10;&#10;		await expect(page.getByTestId(&quot;todo-title&quot;)).toHaveCount(TODO_ITEMS.length);&#10;&#10;		await Promise.all(&#10;			TODO_ITEMS.map((value, index) =&gt;&#10;				expect(page.getByTestId(&quot;todo-title&quot;).nth(index)).toHaveText(value),&#10;			),&#10;		);&#10;	},&#10;};&#10;</code></pre>
<p>Playwright is available as an npm package at <a href="https://www.npmjs.com/package/@cloudflare/playwright"><code>@cloudflare/playwright</code></a> and the code is at <a href="https://github.com/cloudflare/playwright">GitHub</a>.</p>
<p>Learn more in our <a href="/browser-run/playwright/">documentation</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/43/">Previous</a><span>Page 44 of 50</span><a class="pagination-next" rel="next" href="/changelog/45/">Next</a></nav>
</div>
