<h1 id="changelog">Changelog</h1>

<h2 id="transform-html-quickly-with-streaming-content"><a href="/changelog/post/2025-01-31-html-rewriter-streaming/">Transform HTML quickly with streaming content</a></h2>
<p><em>2025-01-31</em></p>
<p>You can now transform HTML elements with streamed content using <a href="/workers/runtime-apis/html-rewriter"><code>HTMLRewriter</code></a>.</p>
<p>Methods like <code>replace</code>, <code>append</code>, and <code>prepend</code> now accept <a href="/workers/runtime-apis/response/"><code>Response</code></a> and <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a>
values as <a href="/workers/runtime-apis/html-rewriter/#global-types"><code>Content</code></a>.</p>
<p>This can be helpful in a variety of situations. For instance, you may have a Worker in front of an origin,
and want to replace an element with content from a different source. Prior to this change, you would have to load
all of the content from the upstream URL and convert it into a string before replacing the element. This slowed
down overall response times.</p>
<p>Now, you can pass the <code>Response</code> object directly into the <code>replace</code> method, and HTMLRewriter will immediately
start replacing the content as it is streamed in. This makes responses faster.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17765.md")</div>
<p>For more information, see the <a href="/workers/runtime-apis/html-rewriter"><code>HTMLRewriter</code> documentation</a>.</p>


<h2 id="workers-for-platforms-now-supports-static-assets"><a href="/changelog/post/2025-01-31-workers-platforms-static-assets/">Workers for Platforms now supports Static Assets</a></h2>
<p><em>2025-01-31</em></p>
<p>Workers for Platforms customers can now attach static assets (HTML, CSS, JavaScript, images) directly to User Workers, removing the need to host separate infrastructure to serve the assets.</p>
<p>This allows your platform to serve entire front-end applications from Cloudflare's global edge, utilizing caching for fast load times, while supporting dynamic logic within the same Worker. Cloudflare automatically scales its infrastructure to handle high traffic volumes, enabling you to focus on building features without managing servers.</p>
<h4 id="2025-01-31-workers-platforms-static-assets-what-you-can-build">What you can build</h4>
<p><strong>Static Sites:</strong> Host and serve HTML, CSS, JavaScript, and media files directly from Cloudflare's network, ensuring fast loading times worldwide. This is ideal for blogs, landing pages, and documentation sites because static assets can be efficiently cached and delivered closer to the user, reducing latency and enhancing the overall user experience.</p>
<p><strong>Full-Stack Applications:</strong> Combine asset hosting with Cloudflare Workers to power dynamic, interactive applications. If you're an e-commerce platform, you can serve your customers' product pages and run inventory checks from within the same Worker.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17821.md")</div>
<p><strong>Get Started:</strong>
Upload static assets using the Workers for Platforms API or Wrangler. For more information, visit our <a href="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/">Workers for Platforms documentation.</a></p>


<h2 id="ai-gateway-introduces-new-worker-binding-methods"><a href="/changelog/post/2025-01-26-worker-binding-methods/">AI Gateway Introduces New Worker Binding Methods</a></h2>
<p><em>2025-01-30</em></p>
<p>We have released new <a href="/ai-gateway/usage/worker-binding-methods/">Workers bindings API methods</a>, allowing you to connect Workers applications to AI Gateway directly. These methods simplify how Workers calls AI services behind your AI Gateway configurations, removing the need to use the REST API and manually authenticate.</p>
<p>To add an AI binding to your Worker, include the following in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<p><img src="/assets/upstream/images/ai-gateway/add-binding.png" alt="Add an AI binding to your Worker." /></p>
<p>With the new AI Gateway binding methods, you can now:</p>
<ul>
<li>Send feedback and update metadata with <code>patchLog</code>.</li>
<li>Retrieve detailed log information using <code>getLog</code>.</li>
<li>Execute <a href="/ai-gateway/usage/universal/">universal requests</a> to any AI Gateway provider with <code>run</code>.</li>
</ul>
<p>For example, to send feedback and update metadata using <code>patchLog</code>:</p>
<p><img src="/assets/upstream/images/ai-gateway/send-feedback.png" alt="Send feedback and update metadata using patchLog:" /></p>


<h2 id="increased-browser-rendering-limits"><a href="/changelog/post/2025-01-30-browser-rendering-more-instances/">Increased Browser Rendering limits!</a></h2>
<p><em>2025-01-30</em></p>
<p><a href="/browser-run/">Browser Rendering</a> now supports 10 concurrent browser instances per account <em>and</em> 10 new instances per minute, up from the previous limits of 2.</p>
<p>This allows you to launch more browser tasks from <a href="/workers">Cloudflare Workers</a>.</p>
<p>To manage concurrent browser sessions, you can use <a href="/queues/">Queues</a> or <a href="/workflows/">Workflows</a>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17693.md")</div>


<h2 id="expanded-language-support-for-stream-ai-generated-captions"><a href="/changelog/post/2025-01-30-stream-generated-captions-new-languages/">Expanded language support for Stream AI Generated Captions</a></h2>
<p><em>2025-01-30</em></p>
<p>Stream's <a href="/stream/edit-videos/adding-captions/#generate-a-caption">generated captions</a>
leverage Workers AI to automatically transcribe audio and provide captions to
the player experience. We have added support for these languages:</p>
<ul>
<li><code>cs</code> - Czech</li>
<li><code>nl</code> - Dutch</li>
<li><code>fr</code> - French</li>
<li><code>de</code> - German</li>
<li><code>it</code> - Italian</li>
<li><code>ja</code> - Japanese</li>
<li><code>ko</code> - Korean</li>
<li><code>pl</code> - Polish</li>
<li><code>pt</code> - Portuguese</li>
<li><code>ru</code> - Russian</li>
<li><code>es</code> - Spanish</li>
</ul>
<p>For more information, learn about <a href="/stream/edit-videos/adding-captions/">adding captions to videos</a>.</p>


<h2 id="automatic-configuration-for-private-databases-on-hyperdrive"><a href="/changelog/post/2025-01-28-hyperdrive-automated-private-database-configuration/">Automatic configuration for private databases on Hyperdrive</a></h2>
<p><em>2025-01-28</em></p>
<p>Hyperdrive now automatically configures your Cloudflare Tunnel to connect to your private database.</p>
<p><img src="/assets/upstream/images/hyperdrive/configuration/hyperdrive-private-database-automatic-configuration.png" alt="Automatic configuration of Cloudflare Access and Service Token in the Cloudflare dashboard for Hyperdrive." /></p>
<p>When creating a Hyperdrive configuration for a private database, you only need to provide your database credentials and set up a Cloudflare Tunnel within the private network where your database is accessible. Hyperdrive will automatically create the Cloudflare Access, Service Token, and Policies needed to secure and restrict your Cloudflare Tunnel to the Hyperdrive configuration.</p>
<p>To create a Hyperdrive for a private database, you can follow the <a href="/hyperdrive/configuration/connect-to-private-database/">Hyperdrive documentation</a>. You can still manually create the Cloudflare Access, Service Token, and Policies if you prefer.</p>
<p>This feature is available from the Cloudflare dashboard.</p>


<h2 id="workers-kv-namespace-limits-increased-to-1000"><a href="/changelog/post/2025-01-27-kv-increased-namespaces-limits/">Workers KV namespace limits increased to 1000</a></h2>
<p><em>2025-01-28</em></p>
<p>You can now have up to 1000 Workers KV namespaces per account.</p>
<p>Workers KV namespace limits were increased from 200 to 1000 for all accounts. Higher limits for Workers KV namespaces enable better organization of key-value data, such as by category, tenant, or environment.</p>
<p>Consult the <a href="/kv/platform/limits/">Workers KV limits documentation</a> for the rest of the limits. This increased limit is available for both the Free and Paid <a href="/workers/platform/pricing/">Workers plans</a>.</p>


<h2 id="support-for-node-js-dns-net-and-timer-apis-in-workers"><a href="/changelog/post/2025-01-28-nodejs-compat-improvements/">Support for Node.js DNS, Net, and Timer APIs in Workers</a></h2>
<p><em>2025-01-28</em></p>
<p>When using a Worker with the <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code></a> compatibility flag enabled, you can now use the following Node.js APIs:</p>
<ul>
<li><a href="/workers/runtime-apis/nodejs/net/"><code>node:net</code></a></li>
<li><a href="/workers/runtime-apis/nodejs/dns/"><code>node:dns</code></a></li>
<li><a href="/workers/runtime-apis/nodejs/timers/"><code>node:timers</code></a></li>
</ul>
<h4 id="2025-01-28-nodejs-compat-improvements-node-net">node:net</h4>
<p>You can use <a href="https://nodejs.org/api/net.html"><code>node:net</code></a> to create a direct connection to servers via a TCP sockets
with <a href="https://nodejs.org/api/net.html#class-netsocket"><code>net.Socket</code></a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17762.md")</div>
<p>Additionally, you can now use other APIs including <a href="https://nodejs.org/api/net.html#class-netblocklist"><code>net.BlockList</code></a> and
<a href="https://nodejs.org/api/net.html#class-netsocketaddress"><code>net.SocketAddress</code></a>.</p>
<p>Note that <a href="https://nodejs.org/api/net.html#class-netserver"><code>net.Server</code></a> is not supported.</p>
<h4 id="2025-01-28-nodejs-compat-improvements-node-dns">node:dns</h4>
<p>You can use <a href="https://nodejs.org/api/dns.html"><code>node:dns</code></a> for name resolution via <a href="/1.1.1.1/encryption/dns-over-https/">DNS over HTTPS</a> using
<a href="https://www.cloudflare.com/application-services/products/dns/">Cloudflare DNS</a> at 1.1.1.1.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17763.md")</div>
<p>All <code>node:dns</code> functions are available, except <code>lookup</code>, <code>lookupService</code>, and <code>resolve</code> which throw &quot;Not implemented&quot; errors when called.</p>
<h4 id="2025-01-28-nodejs-compat-improvements-node-timers">node:timers</h4>
<p>You can use <a href="https://nodejs.org/api/timers.html"><code>node:timers</code></a> to schedule functions to be called at some future period of time.</p>
<p>This includes <a href="https://nodejs.org/api/timers.html#settimeoutcallback-delay-args"><code>setTimeout</code></a> for calling a function after a delay,
<a href="https://nodejs.org/api/timers.html#setintervalcallback-delay-args"><code>setInterval</code></a> for calling a function repeatedly,
and <a href="https://nodejs.org/api/timers.html#setimmediatecallback-args"><code>setImmediate</code></a> for calling a function in the next iteration of the event loop.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17764.md")</div>


<h2 id="increased-workflows-limits-and-improved-instance-queueing"><a href="/changelog/post/2025-01-15-workflows-more-steps/">Increased Workflows limits and improved instance queueing.</a></h2>
<p><em>2025-01-15</em></p>
<p><a href="/workflows/">Workflows</a> (beta) now allows you to define up to 1024 <a href="/workflows/build/workers-api/#workflowstep">steps</a>. <code>sleep</code> steps do not count against this limit.</p>
<p>We've also added:</p>
<ul>
<li><code>instanceId</code> as property to the <a href="/workflows/build/workers-api/#workflowevent"><code>WorkflowEvent</code></a> type, allowing you to retrieve the current instance ID from within a running Workflow instance</li>
<li>Improved queueing logic for Workflow instances beyond the current maximum concurrent instances, reducing the cases where instances are stuck in the queued state.</li>
<li>Support for <a href="/workflows/build/workers-api/#pause"><code>pause</code> and <code>resume</code></a> for Workflow instances in a queued state.</li>
</ul>
<p>We're continuing to work on increases to the number of concurrent Workflow instances, steps, and support for a new <code>waitForEvent</code> API over the coming weeks.</p>


<h2 id="40-60-faster-d1-worker-api-requests"><a href="/changelog/post/2025-01-07-d1-faster-query/">40-60% Faster D1 Worker API Requests</a></h2>
<p><em>2025-01-07</em></p>
<p>Users making <a href="/d1/">D1</a> requests via the <a href="/d1/worker-api/">Workers API</a> can see up to a 60% end-to-end latency improvement due to the removal of redundant network round trips needed for each request to a D1 database.</p>
<p><img src="/images/d1/faster-d1-worker-api.png" alt="D1 Worker API latency" /></p>
<p><em>p50, p90, and p95 request latency aggregated across entire D1 service. These latencies are a reference point and should not be viewed as your exact workload improvement.</em></p>
<p>This performance improvement benefits all D1 Worker API traffic, especially cross-region requests where network latency is an outsized latency factor. For example, a user in Europe talking to a database in North America. D1 <a href="/d1/configuration/data-location/#provide-a-location-hint">location hints</a> can be used to influence the geographic location of a database.</p>
<p>For more details on how D1 removed redundant round trips, see the D1 specific release note <a href="/d1/platform/release-notes/#2025-01-07">entry</a>.</p>


<h2 id="ai-gateway-adds-deepseek-as-a-provider"><a href="/changelog/post/2025-01-07-aig-provider-deepseek/">AI Gateway adds DeepSeek as a Provider</a></h2>
<p><em>2025-01-02</em></p>
<p><a href="/ai-gateway/"><strong>AI Gateway</strong></a> now supports <a href="/ai-gateway/usage/providers/deepseek/"><strong>DeepSeek</strong></a>, including their cutting-edge DeepSeek-V3 model. With this addition, you have even more flexibility to manage and optimize your AI workloads using AI Gateway. Whether you're leveraging DeepSeek or other providers, like OpenAI, Anthropic, or <a href="/workers-ai/">Workers AI</a>, AI Gateway empowers you to:</p>
<ul>
<li><strong>Monitor</strong>: Gain actionable insights with analytics and logs.</li>
<li><strong>Control</strong>: Implement caching, rate limiting, and fallbacks.</li>
<li><strong>Optimize</strong>: Improve performance with feedback and evaluations.</li>
</ul>
<p><img src="/assets/upstream/images/ai-gateway/deepseek.png" alt="AI Gateway adds DeepSeek as a provider" /></p>
<p>To get started, simply update the base URL of your DeepSeek API calls to route through AI Gateway. Here's how you can send a request using cURL:</p>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions \&#10; &#45;-header &#x27;content-type: application/json&#x27; \&#10; &#45;-header &#x27;Authorization: Bearer DEEPSEEK_TOKEN&#x27; \&#10; &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;deepseek-chat&quot;,&#10;    &quot;messages&quot;: [&#10;        {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>
<p>For detailed setup instructions, see our <a href="/ai-gateway/usage/providers/deepseek/">DeepSeek provider documentation</a>.</p>


<h2 id="faster-workers-builds-with-build-caching-and-watch-paths"><a href="/changelog/post/2024-12-29-faster-builds/">Faster Workers Builds with Build Caching and Watch Paths</a></h2>
<p><em>2024-12-29</em></p>
<p><img src="/assets/upstream/images/workers/platform/ci-cd/workers-build-caching.png" alt="Build caching settings" />
<img src="/assets/upstream/images/workers/platform/ci-cd/workers-build-watch-paths.png" alt="Build watch path settings" /></p>
<p><a href="/workers/ci-cd/builds/"><strong>Workers Builds</strong></a>, the integrated CI/CD system for Workers (currently in beta), now lets you cache artifacts across builds, speeding up build jobs by eliminating repeated work, such as downloading dependencies at the start of each build.</p>
<ul>
<li>
<p><strong><a href="/workers/ci-cd/builds/build-caching/">Build Caching</a></strong>: Cache dependencies and build outputs between builds with a shared project-wide cache, ensuring faster builds for the entire team.</p>
</li>
<li>
<p><strong><a href="/workers/ci-cd/builds/build-watch-paths/">Build Watch Paths</a></strong>: Define paths to include or exclude from the build process, ideal for <a href="/workers/ci-cd/builds/advanced-setups/#monorepos">monorepos</a> to target only the files that need to be rebuilt per Workers project.</p>
</li>
</ul>
<p>To get started, select your Worker on the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> then go to <strong>Settings</strong> &gt; <strong>Builds</strong>, and connect a GitHub or GitLab repository. Once connected, you'll see options to configure Build Caching and Build Watch Paths.</p>


<h2 id="troubleshoot-tunnels-with-diagnostic-logs"><a href="/changelog/post/2024-12-19-diagnostic-logs/">Troubleshoot tunnels with diagnostic logs</a></h2>
<p><em>2024-12-19</em></p>
<p>The latest <code>cloudflared</code> build <a href="https://github.com/cloudflare/cloudflared/releases/tag/2024.12.2">2024.12.2</a> introduces the ability to collect all the diagnostic logs needed to troubleshoot a <code>cloudflared</code> instance.</p>
<p>A diagnostic report collects data from a single instance of <code>cloudflared</code> running on the local machine and outputs it to a <code>cloudflared-diag</code> file.</p>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/">Diagnostic logs</a>.</p>


<h2 id="up-to-10x-faster-cached-queries-for-hyperdrive"><a href="/changelog/post/2024-12-11-hyperdrive-caching-at-edge/">Up to 10x faster cached queries for Hyperdrive</a></h2>
<p><em>2024-12-11</em></p>
<p>Hyperdrive now caches queries in all Cloudflare locations, decreasing cache hit latency by up to 90%.</p>
<p>When you make a query to your database and Hyperdrive has cached the query results, Hyperdrive will now return the results from the nearest cache. By caching data closer to your users, the latency for cache hits reduces by up to 90%.</p>
<p>This reduction in cache hit latency is reflected in a reduction of the session duration for all queries (cached and uncached) from Cloudflare Workers to Hyperdrive, as illustrated below.</p>
<p><img src="/assets/upstream/images/hyperdrive/changelog/hyperdrive-edge-caching-metrics.png" alt="Hyperdrive edge caching improves average session duration for database queries" /></p>
<p><em>P50, P75, and P90 Hyperdrive session latency for all client connection sessions (both cached and uncached queries) for Hyperdrive configurations with caching enabled during the rollout period.</em></p>
<p>This performance improvement is applied to all new and existing Hyperdrive configurations that have caching enabled.</p>
<p>For more details on how Hyperdrive performs query caching, refer to the <a href="/hyperdrive/concepts/how-hyperdrive-works/#3-query-caching">Hyperdrive documentation</a>.</p>


<h2 id="bypass-caching-for-subrequests-made-from-cloudflare-workers-with-request-cache"><a href="/changelog/post/2024-11-11-cache-no-store/">Bypass caching for subrequests made from Cloudflare Workers, with Request.cache</a></h2>
<p><em>2024-11-11</em></p>
<p>You can now use the <a href="/workers/runtime-apis/request/#options"><code>cache</code></a> property of the <a href="/workers/runtime-apis/request/"><code>Request</code></a> interface to bypass <a href="/workers/reference/how-the-cache-works/">Cloudflare's cache</a> when making subrequests from <a href="/workers">Cloudflare Workers</a>, by setting its value to <code>no-store</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17761.md")</div>
<p>When you set the value to <code>no-store</code> on a subrequest made from a Worker, the Cloudflare Workers runtime will not check whether a match exists in the cache, and not add the response to the cache, even if the response includes directives in the <code>Cache-Control</code> HTTP header that otherwise indicate that the response is cacheable.</p>
<p>This increases compatibility with NPM packages and JavaScript frameworks that rely on setting the <a href="/workers/runtime-apis/request/#options"><code>cache</code></a> property, which is a cross-platform standard part of the <a href="/workers/runtime-apis/request/"><code>Request</code></a> interface. Previously, if you set the <code>cache</code> property on <code>Request</code>, the Workers runtime threw an exception.</p>
<p>If you've tried to use <code>@planetscale/database</code>, <code>redis-js</code>, <code>stytch-node</code>, <code>supabase</code>, <code>axiom-js</code> or have seen the error message <code>The cache field on RequestInitializerDict is not implemented in fetch</code> — you should try again, making sure that the <a href="/workers/configuration/compatibility-dates/">Compatibility Date</a> of your Worker is set to on or after <code>2024-11-11</code>, or the <a href="/workers/configuration/compatibility-flags/#enable-cache-no-store-http-standard-api"><code>cache_option_enabled</code> compatibility flag</a> is enabled for your Worker.</p>
<ul>
<li>Learn <a href="/workers/reference/how-the-cache-works/">how the Cache works with Cloudflare Workers</a></li>
<li>Enable <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> for your Cloudflare Worker</li>
<li>Explore <a href="/workers/runtime-apis/">Runtime APIs</a> and <a href="/workers/runtime-apis/bindings/">Bindings</a> available in Cloudflare Workers</li>
</ul>


<h2 id="workflows-is-now-in-open-beta"><a href="/changelog/post/2024-10-24-workflows-beta/">Workflows is now in open beta</a></h2>
<p><em>2024-10-24</em></p>
<p>Workflows is now in open beta, and available to any developer a free or paid Workers plan.</p>
<p>Workflows allow you to build multi-step applications that can automatically retry, persist state and run for minutes, hours, days, or weeks. Workflows introduces a programming model that makes it easier to build reliable, long-running tasks, observe as they progress, and programmatically trigger instances based on events across your services.</p>
<h4 id="2024-10-24-workflows-beta-get-started">Get started</h4>
<p>You can get started with Workflows by <a href="/workflows/get-started/guide/">following our get started guide</a> and/or using <code>npm create cloudflare</code> to pull down the starter project:</p>
<pre><code class="language-sh">npm create cloudflare@latest workflows-starter -- --template &quot;cloudflare/workflows-starter&quot;&#10;</code></pre>
<p>You can open the <code>src/index.ts</code> file, extend it, and use <code>wrangler deploy</code> to deploy your first Workflow. From there, you can:</p>
<ul>
<li>Learn the <a href="/workflows/build/workers-api/">Workflows API</a></li>
<li><a href="/workflows/build/trigger-workflows/">Trigger Workflows</a> via your Workers apps.</li>
<li>Understand the <a href="/workflows/build/rules-of-workflows/">Rules of Workflows</a> and how to adopt best practices</li>
</ul>


<h2 id="easily-exclude-eu-visitors-from-rum"><a href="/changelog/post/2025-02-25-rum-exclude-eu/">Easily Exclude EU Visitors from RUM</a></h2>
<p><em>2024-02-26</em></p>
<p>You can now easily enable Real User Monitoring (RUM) monitoring for your hostnames, while safely dropping requests from visitors in the European Union to comply with GDPR and CCPA.</p>
<p><img src="/assets/upstream/images/changelog/web-analytics/2025-02-26-rum-eu.png" alt="RUM Enablement UI" /></p>
<p>Our Web Analytics product has always been centered on giving you insights into your users' experience that you need to provide the best quality experience, without sacrificing user privacy in the process.</p>
<p>To help with that aim, you can now selectively enable RUM monitoring for your hostname and exclude EU visitor data in a single click. If you opt for this option, we will drop all metrics collected by our EU data centers automatically.</p>
<p>You can learn more about what metrics are reported by Web Analytics and how it is collected <a href="/web-analytics/data-metrics/">in the Web Analytics documentation</a>. You can enable Web Analytics on any hostname by going to the <a href="https://dash.cloudflare.com/?to=/:account/web-analytics/sites">Web Analytics</a> section of the dashboard, selecting &quot;Manage Site&quot; for the hostname you want to monitor, and choosing the appropriate enablement option.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/22/">Previous</a><span>Page 23 of 23</span></nav>
