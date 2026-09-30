<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-02-06">Feb 6, 2025</time><div>
<h2 id="post-2025-02-05-aig-request-handling"><a href="/changelog/post/2025-02-05-aig-request-handling/">Request timeouts and retries with AI Gateway</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway adds additional ways to handle requests - <a href="/ai-gateway/configuration/request-handling/#request-timeouts">Request Timeouts</a> and <a href="/ai-gateway/configuration/request-handling/#request-retries">Request Retries</a>, making it easier to keep your applications responsive and reliable.</p>
<p>Timeouts and retries can be used on both the <a href="/ai-gateway/usage/universal/">Universal Endpoint</a> or directly to a <a href="/ai-gateway/usage/providers/">supported provider</a>.</p>
<p><strong>Request timeouts</strong>
A <a href="/ai-gateway/configuration/request-handling/#request-timeouts">request timeout</a> allows you to trigger <a href="/ai-gateway/configuration/fallbacks/">fallbacks</a> or a retry if a provider takes too long to respond.</p>
<p>To set a request timeout directly to a provider, add a <code>cf-aig-request-timeout</code> header.</p>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/workers-ai/@cf/meta/llama-3.1-8b-instruct \&#10; &#45;-header &#x27;Authorization: Bearer {cf_api_token}&#x27; \&#10; &#45;-header &#x27;Content-Type: application/json&#x27; \&#10; &#45;-header &#x27;cf-aig-request-timeout: 5000&#x27;&#10; &#45;-data &#x27;{&quot;prompt&quot;: &quot;What is Cloudflare?&quot;}&#x27;&#10;</code></pre>
<p><strong>Request retries</strong>
A <a href="/ai-gateway/configuration/request-handling/#request-retries">request retry</a> automatically retries failed requests, so you can recover from temporary issues without intervening.</p>
<p>To set up request retries directly to a provider, add the following headers:</p>
<ul>
<li>cf-aig-max-attempts (number)</li>
<li>cf-aig-retry-delay (number)</li>
<li>cf-aig-backoff (&quot;constant&quot; | &quot;linear&quot; | &quot;exponential)</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-05">Feb 5, 2025</time><div>
<h2 id="post-2025-02-04-aig-provider-cartesia-eleven-cerebras"><a href="/changelog/post/2025-02-04-aig-provider-cartesia-eleven-cerebras/">AI Gateway adds Cerebras, ElevenLabs, and Cartesia as new providers</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p><a href="/ai-gateway/">AI Gateway</a> has added three new providers: <a href="/ai-gateway/usage/providers/cartesia/">Cartesia</a>, <a href="/ai-gateway/usage/providers/cerebras/">Cerebras</a>, and <a href="/ai-gateway/usage/providers/elevenlabs/">ElevenLabs</a>, giving you more even more options for providers you can use through AI Gateway. Here's a brief overview of each:</p>
<ul>
<li><a href="/ai-gateway/usage/providers/cartesia/">Cartesia</a> provides text-to-speech models that produce natural-sounding speech with low latency.</li>
<li><a href="/ai-gateway/usage/providers/cerebras/">Cerebras</a> delivers low-latency AI inference to Meta's Llama 3.1 8B and Llama 3.3 70B models.</li>
<li><a href="/ai-gateway/usage/providers/elevenlabs/">ElevenLabs</a> offers text-to-speech models with human-like voices in 32 languages.</li>
</ul>
<p><img src="/assets/upstream/images/ai-gateway/cerebras2.png" alt="Example of Cerebras log in AI Gateway" /></p>
<p>To get started with AI Gateway, just update the base URL. Here's how you can send a request to <a href="/ai-gateway/usage/providers/cerebras/">Cerebras</a> using cURL:</p>
<pre><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/ACCOUNT_TAG/GATEWAY/cerebras/chat/completions \&#10; &#45;-header &#x27;content-type: application/json&#x27; \&#10; &#45;-header &#x27;Authorization: Bearer CEREBRAS_TOKEN&#x27; \&#10; &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;llama-3.3-70b&quot;,&#10;    &quot;messages&quot;: [&#10;        {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-04">Feb 4, 2025</time><div>
<h2 id="post-2025-02-04-easier-onboarding-for-csam-scanning-tool"><a href="/changelog/post/2025-02-04-easier-onboarding-for-csam-scanning-tool/">Fight CSAM More Easily Than Ever</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now implement our <strong>child safety tooling</strong>, the <strong><a href="/cache/reference/csam-scanning/">CSAM Scanning Tool</a></strong>, more easily. Instead of requiring external reporting credentials, you only need a verified email address for notifications to onboard. This change makes the tool more accessible to a wider range of customers.</p>
<p><strong>How It Works</strong></p>
<p>When enabled, the tool automatically <a href="https://blog.cloudflare.com/the-csam-scanning-tool/">hashes images for enabled websites as they enter the Cloudflare cache</a>. These hashes are then checked against a database of <strong>known abusive images</strong>.</p>
<ul>
<li><strong>Potential match detected?</strong>
<ul>
<li>The <strong>content URL is blocked</strong>, and</li>
<li><strong>Cloudflare will notify you</strong> about the found matches via the provided email address.</li>
</ul>
</li>
</ul>
<p><strong>Updated Service-Specific Terms</strong></p>
<p>We have also made updates to our <strong><a href="https://www.cloudflare.com/service-specific-terms-application-services/#csam-scanning-tool-terms">Service-Specific Terms</a></strong> to reflect these changes.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-04">Feb 4, 2025</time><div>
<h2 id="post-2025-02-04-radar-ai-insights"><a href="/changelog/post/2025-02-04-radar-ai-insights/">Expanded AI insights in Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> has expanded its AI insights with new API endpoints for Internet services rankings, robots.txt analysis, and AI inference data.</p>
<h4 id="2025-02-04-radar-ai-insights-internet-services-ranking">Internet services ranking</h4>
<p>Radar now provides <a href="/radar/glossary/#internet-services-ranking">rankings for Internet services</a>, including Generative AI platforms, based on anonymized 1.1.1.1 resolver data.
Previously limited to the annual Year in Review, these insights are now available daily via the <a href="/api/resources/radar/subresources/ranking/subresources/internet_services/">API</a>, through the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/ranking/subresources/internet_services/methods/top/"><code>/ranking/internet_services/top</code></a> show service popularity at a specific date.</li>
<li><a href="/api/resources/radar/subresources/ranking/subresources/internet_services/methods/timeseries_groups/"><code>/ranking/internet_services/timeseries_groups</code></a> track ranking trends over time.</li>
</ul>
<h4 id="2025-02-04-radar-ai-insights-robots-txt">Robots.txt</h4>
<p>Radar now analyzes <a href="/radar/glossary/#robotstxt">robots.txt</a> files from the top 10,000 domains, identifying AI bot access rules.
AI-focused user agents from <a href="https://github.com/ai-robots-txt/ai.robots.txt">ai.robots.txt</a> are categorized as:</p>
<ul>
<li><strong>Fully allowed/disallowed</strong> if directives apply to all paths (<code>*</code>).</li>
<li><strong>Partially allowed/disallowed</strong> if restrictions apply to specific paths.</li>
</ul>
<p>These insights are now available weekly via the <a href="/api/resources/radar/subresources/robots_txt/">API</a>, through the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/robots_txt/subresources/top/subresources/user_agents/methods/directive/"><code>/robots_txt/top/user_agents/directive</code></a> to get the top AI user agents by directive.</li>
<li><a href="/api/resources/radar/subresources/robots_txt/subresources/top/methods/domain_categories/"><code>/robots_txt/top/domain_categories</code></a> to get the top domain categories by robots.txt files.</li>
</ul>
<h4 id="2025-02-04-radar-ai-insights-workers-ai">Workers AI</h4>
<p>Radar now provides insights into public AI inference models from <a href="/workers-ai/">Workers AI</a>, tracking usage trends across <strong>models</strong> and <strong>tasks</strong>.
These insights are now available via the <a href="/api/resources/radar/subresources/ai/subresources/inference/">API</a>, through the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/ai/subresources/inference/subresources/summary/"><code>/ai/inference/summary/{dimension}</code></a> to view aggregated <code>model</code> and <code>task</code> popularity.</li>
<li><a href="/api/resources/radar/subresources/ai/subresources/inference/subresources/timeseries_groups/"><code>/ai/inference/timeseries_groups/{dimension}</code></a> to track changes over time for <code>model</code> or <code>task</code>.</li>
</ul>
<p>Learn more about the new Radar AI insights in our <a href="https://blog.cloudflare.com/expanded-ai-insights-on-cloudflare-radar/">blog post</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-04">Feb 4, 2025</time><div>
<h2 id="post-2025-02-04-updated-leaked-credentials-database"><a href="/changelog/post/2025-02-04-updated-leaked-credentials-database/">Updated leaked credentials database</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>Added new records to the leaked credentials database from a third-party database.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-03">Feb 3, 2025</time><div>
<h2 id="post-2025-02-13-improvements-unscannable-files"><a href="/changelog/post/2025-02-13-improvements-unscannable-files/">Block files that are password-protected, compressed, or otherwise unscannable.</a></h2>
<div class="changelog-badges"><span>dlp</span><span>gateway</span></div><div class="changelog-body"><p>Gateway HTTP policies can now block files that are password-protected, compressed, or otherwise unscannable.</p>
<p>These unscannable files are now matched with the <a href="/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types">Download and Upload File Types traffic selectors</a> for HTTP policies:</p>
<ul>
<li>Password-protected Microsoft Office document</li>
<li>Password-protected PDF</li>
<li>Password-protected ZIP archive</li>
<li>Unscannable ZIP archive</li>
</ul>
<p>To get started inspecting and modifying behavior based on these and other rules, refer to <a href="/cloudflare-one/traffic-policies/get-started/http/">HTTP filtering</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-03">Feb 3, 2025</time><div>
<h2 id="post-2025-02-03-terraform-v5-provider"><a href="/changelog/post/2025-02-03-terraform-v5-provider/">Terraform v5 Provider is now generally available</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/changelog/2024-02-03-terraform-v5-screenshot.png" alt="Screenshot of Terraform defining a Zone" /></p>
<p>Cloudflare's v5 Terraform Provider is now generally available. With this release, Terraform resources are now automatically generated based on OpenAPI Schemas. This change brings alignment across our SDKs, API documentation, and now Terraform Provider. The new provider boosts coverage by increasing support for API properties to 100%, adding 25% more resources, and more than 200 additional data sources. Going forward, this will also reduce the barriers to bringing more resources into Terraform across the broader Cloudflare API. This is a small, but important step to making more of our platform manageable through GitOps, making it easier for you to manage Cloudflare just like you do your other infrastructure.</p>
<p>The Cloudflare Terraform Provider v5 is a ground-up rewrite of the provider and introduces breaking changes for some resource types. Please refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">upgrade guide</a> for best practices, or the <a href="https://blog.cloudflare.com/automatically-generating-cloudflares-terraform-provider/">blog post on automatically generating Cloudflare's Terraform Provider</a> for more information about the approach.</p>
<p>For more info</p>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="https://developers.cloudflare.com/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-03">Feb 3, 2025</time><div>
<h2 id="post-2025-02-03-workers-metrics-revamp"><a href="/changelog/post/2025-02-03-workers-metrics-revamp/">Revamped Workers Metrics</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We've revamped the <a href="https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/metrics/">Workers Metrics dashboard</a>.</p>
<p><img src="/assets/upstream/images/workers/observability/workers-metrics.png" alt="Workers Metrics dashboard" /></p>
<p>Now you can easily compare metrics across Worker versions, understand the current state of a <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployment</a>, and review key Workers metrics in a single view. This new interface enables you to:</p>
<ul>
<li>Drag-and-select using a graphical timepicker for precise metric selection.</li>
</ul>
<p><img src="/assets/upstream/images/workers/observability/metrics-graphical-timepicker.png" alt="Workers Metrics graphical timepicker" /></p>
<ul>
<li>Use histograms to visualize cumulative metrics, allowing you to bucket and compare rates over time.</li>
<li>Focus on Worker versions by directly interacting with the version numbers in the legend.</li>
</ul>
<p><img src="/assets/upstream/images/workers/observability/metrics-legend-selector.png" alt="Workers Metrics legend selector" /></p>
<ul>
<li>Monitor and compare active gradual deployments.</li>
<li>Track error rates across versions with grouping both by version and by invocation status.</li>
<li>Measure how <a href="/workers/configuration/placement/">Smart Placement</a> improves request duration.</li>
</ul>
<p>Learn more about <a href="/workers/observability/metrics-and-analytics">metrics</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-02-02">Feb 2, 2025</time><div>
<h2 id="post-2025-02-02-removed-meta-fields"><a href="/changelog/post/2025-02-02-removed-meta-fields/">Removed unused meta fields from DNS records</a></h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>Cloudflare is removing five fields from the <code>meta</code> object of DNS records. These fields have been unused for more than a year and are no longer set on new records. This change may take up to four weeks to fully roll out.</p>
<p>The affected fields are:</p>
<ul>
<li>the <code>auto_added</code> boolean</li>
<li>the <code>managed_by_apps</code> boolean and corresponding <code>apps_install_id</code></li>
<li>the <code>managed_by_argo_tunnel</code> boolean and corresponding <code>argo_tunnel_id</code></li>
</ul>
<p>An example record returned from the API would now look like the following:</p>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;ID&gt;&quot;,&#10;		&quot;zone_id&quot;: &quot;&lt;ZONE_ID&gt;&quot;,&#10;		&quot;zone_name&quot;: &quot;example.com&quot;,&#10;		&quot;name&quot;: &quot;www.example.com&quot;,&#10;		&quot;type&quot;: &quot;A&quot;,&#10;		&quot;content&quot;: &quot;192.0.2.1&quot;,&#10;		&quot;proxiable&quot;: true,&#10;		&quot;proxied&quot;: false,&#10;		&quot;ttl&quot;: 1,&#10;		&quot;locked&quot;: false,&#10;		&quot;meta&quot;: {&#10;			&quot;auto_added&quot;: false,&#10;			&quot;managed_by_apps&quot;: false,&#10;			&quot;managed_by_argo_tunnel&quot;: false,&#10;			&quot;source&quot;: &quot;primary&quot;&#10;		},&#10;		&quot;comment&quot;: null,&#10;		&quot;tags&quot;: [],&#10;		&quot;created_on&quot;: &quot;2025-03-17T20:37:05.368097Z&quot;,&#10;		&quot;modified_on&quot;: &quot;2025-03-17T20:37:05.368097Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>For more guidance, refer to <a href="/dns/manage-dns-records/">Manage DNS records</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-31">Jan 31, 2025</time><div>
<h2 id="post-2025-01-31-html-rewriter-streaming"><a href="/changelog/post/2025-01-31-html-rewriter-streaming/">Transform HTML quickly with streaming content</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now transform HTML elements with streamed content using <a href="/workers/runtime-apis/html-rewriter"><code>HTMLRewriter</code></a>.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-31">Jan 31, 2025</time><div>
<h2 id="post-2025-01-31-workers-platforms-static-assets"><a href="/changelog/post/2025-01-31-workers-platforms-static-assets/">Workers for Platforms now supports Static Assets</a></h2>
<div class="changelog-badges"><span>workers-for-platforms</span></div><div class="changelog-body"><p>Workers for Platforms customers can now attach static assets (HTML, CSS, JavaScript, images) directly to User Workers, removing the need to host separate infrastructure to serve the assets.</p>
<p>This allows your platform to serve entire front-end applications from Cloudflare's global edge, utilizing caching for fast load times, while supporting dynamic logic within the same Worker. Cloudflare automatically scales its infrastructure to handle high traffic volumes, enabling you to focus on building features without managing servers.</p>
<h4 id="2025-01-31-workers-platforms-static-assets-what-you-can-build">What you can build</h4>
<p><strong>Static Sites:</strong> Host and serve HTML, CSS, JavaScript, and media files directly from Cloudflare's network, ensuring fast loading times worldwide. This is ideal for blogs, landing pages, and documentation sites because static assets can be efficiently cached and delivered closer to the user, reducing latency and enhancing the overall user experience.</p>
<p><strong>Full-Stack Applications:</strong> Combine asset hosting with Cloudflare Workers to power dynamic, interactive applications. If you're an e-commerce platform, you can serve your customers' product pages and run inventory checks from within the same Worker.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17821.md")</div>
<p><strong>Get Started:</strong>
Upload static assets using the Workers for Platforms API or Wrangler. For more information, visit our <a href="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/">Workers for Platforms documentation.</a></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-30">Jan 30, 2025</time><div>
<h2 id="post-2025-01-26-worker-binding-methods"><a href="/changelog/post/2025-01-26-worker-binding-methods/">AI Gateway Introduces New Worker Binding Methods</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>We have released new <a href="/ai-gateway/usage/worker-binding-methods/">Workers bindings API methods</a>, allowing you to connect Workers applications to AI Gateway directly. These methods simplify how Workers calls AI services behind your AI Gateway configurations, removing the need to use the REST API and manually authenticate.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-30">Jan 30, 2025</time><div>
<h2 id="post-2025-01-30-browser-rendering-more-instances"><a href="/changelog/post/2025-01-30-browser-rendering-more-instances/">Increased Browser Rendering limits!</a></h2>
<div class="changelog-badges"><span>workers</span><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Rendering</a> now supports 10 concurrent browser instances per account <em>and</em> 10 new instances per minute, up from the previous limits of 2.</p>
<p>This allows you to launch more browser tasks from <a href="/workers">Cloudflare Workers</a>.</p>
<p>To manage concurrent browser sessions, you can use <a href="/queues/">Queues</a> or <a href="/workflows/">Workflows</a>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17693.md")</div>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-30">Jan 30, 2025</time><div>
<h2 id="post-2025-01-30-stream-generated-captions-new-languages"><a href="/changelog/post/2025-01-30-stream-generated-captions-new-languages/">Expanded language support for Stream AI Generated Captions</a></h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>Stream's <a href="/stream/edit-videos/adding-captions/#generate-a-caption">generated captions</a>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-29">Jan 29, 2025</time><div>
<h2 id="post-2025-01-29-snippets-code-editor"><a href="/changelog/post/2025-01-29-snippets-code-editor/">New Snippets Code Editor</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>The new <a href="/rules/snippets/">Snippets</a> code editor lets you edit Snippet code and rule in one place, making it easier to test and deploy changes without switching between pages.</p>
<p><img src="/assets/upstream/images/changelog/rules/snippets-new-editor.png" alt="New Snippets code editor" /></p>
<p>What’s new:</p>
<ul>
<li><strong>Single-page editing for code and rule</strong> – No need to jump between screens.</li>
<li><strong>Auto-complete &amp; syntax highlighting</strong> – Get suggestions and avoid mistakes.</li>
<li><strong>Code formatting &amp; refactoring</strong> – Write cleaner, more readable code.</li>
</ul>
<p>Try it now in <a href="https://dash.cloudflare.com/?to=/:account/:zone/rules/snippets">Rules &gt; Snippets</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-28">Jan 28, 2025</time><div>
<h2 id="post-2025-01-28-hyperdrive-automated-private-database-configuration"><a href="/changelog/post/2025-01-28-hyperdrive-automated-private-database-configuration/">Automatic configuration for private databases on Hyperdrive</a></h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>Hyperdrive now automatically configures your Cloudflare Tunnel to connect to your private database.</p>
<p><img src="/assets/upstream/images/hyperdrive/configuration/hyperdrive-private-database-automatic-configuration.png" alt="Automatic configuration of Cloudflare Access and Service Token in the Cloudflare dashboard for Hyperdrive." /></p>
<p>When creating a Hyperdrive configuration for a private database, you only need to provide your database credentials and set up a Cloudflare Tunnel within the private network where your database is accessible. Hyperdrive will automatically create the Cloudflare Access, Service Token, and Policies needed to secure and restrict your Cloudflare Tunnel to the Hyperdrive configuration.</p>
<p>To create a Hyperdrive for a private database, you can follow the <a href="/hyperdrive/configuration/connect-to-private-database/">Hyperdrive documentation</a>. You can still manually create the Cloudflare Access, Service Token, and Policies if you prefer.</p>
<p>This feature is available from the Cloudflare dashboard.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-28">Jan 28, 2025</time><div>
<h2 id="post-2025-01-27-kv-increased-namespaces-limits"><a href="/changelog/post/2025-01-27-kv-increased-namespaces-limits/">Workers KV namespace limits increased to 1000</a></h2>
<div class="changelog-badges"><span>kv</span></div><div class="changelog-body"><p>You can now have up to 1000 Workers KV namespaces per account.</p>
<p>Workers KV namespace limits were increased from 200 to 1000 for all accounts. Higher limits for Workers KV namespaces enable better organization of key-value data, such as by category, tenant, or environment.</p>
<p>Consult the <a href="/kv/platform/limits/">Workers KV limits documentation</a> for the rest of the limits. This increased limit is available for both the Free and Paid <a href="/workers/platform/pricing/">Workers plans</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-28">Jan 28, 2025</time><div>
<h2 id="post-2025-01-28-nodejs-compat-improvements"><a href="/changelog/post/2025-01-28-nodejs-compat-improvements/">Support for Node.js DNS, Net, and Timer APIs in Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>When using a Worker with the <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code></a> compatibility flag enabled, you can now use the following Node.js APIs:</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-21">Jan 21, 2025</time><div>
<h2 id="post-2025-01-21-waf-release"><a href="/changelog/post/2025-01-21-waf-release/">WAF Release - 2025-01-21</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f4a310393c564d50bd585601b090ba9a">b090ba9a</code>
</td>
<td>100303</td>
<td>Command Injection - Nslookup</td>
<td>Log</td>
<td>Block</td>
<td>
				This was released as <code class="nb-rule-id" title="aad6f9f85e034022b6a8dee4b8d152f4">b8d152f4</code>
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fd5d5678ce594ea898aa9bf149e6b538">49e6b538</code>
</td>
<td>100534</td>
<td>Web Shell Activity</td>
<td>Log</td>
<td>Block</td>
<td>
				This was released as <code class="nb-rule-id" title="39c8f6066c19466ea084e51e82fe4e7f">82fe4e7f</code>
</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-20">Jan 20, 2025</time><div>
<h2 id="post-2025-01-03-source-code-confidence-level"><a href="/changelog/post/2025-01-03-source-code-confidence-level/">Detect source code leaks with Data Loss Prevention</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>You can now detect source code leaks with Data Loss Prevention (DLP) with predefined checks against common programming languages.</p>
<p>The following programming languages are validated with natural language processing (NLP).</p>
<ul>
<li>C</li>
<li>C++</li>
<li>C#</li>
<li>Go</li>
<li>Haskell</li>
<li>Java</li>
<li>JavaScript</li>
<li>Lua</li>
<li>Python</li>
<li>R</li>
<li>Rust</li>
<li>Swift</li>
</ul>
<p>DLP also supports confidence level for <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#source-code">source code profiles</a>.</p>
<p>For more details, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-15">Jan 15, 2025</time><div>
<h2 id="post-2025-01-15-ssh-logs-and-logpush"><a href="/changelog/post/2025-01-15-ssh-logs-and-logpush/">Export SSH command logs with Access for Infrastructure using Logpush</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><aside class="nb-aside note">
<h4 class="nb-aside-title" id="2025-01-15-ssh-logs-and-logpush-availability">Availability</h4>
@markup("md", "content/.markup/bodies/17614.md")</aside>
<p>Cloudflare now allows you to send SSH command logs to storage destinations configured in <a href="/logs/logpush/">Logpush</a>, including third-party destinations. Once exported, analyze and audit the data as best fits your organization! For a list of available data fields, refer to the <a href="/logs/logpush/logpush-job/datasets/account/ssh_logs/">SSH logs dataset</a>.</p>
<p>To set up a Logpush job, refer to <a href="/cloudflare-one/insights/logs/logpush/">Logpush integration</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-15">Jan 15, 2025</time><div>
<h2 id="post-2025-01-15-workflows-more-steps"><a href="/changelog/post/2025-01-15-workflows-more-steps/">Increased Workflows limits and improved instance queueing.</a></h2>
<div class="changelog-badges"><span>workflows</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> (beta) now allows you to define up to 1024 <a href="/workflows/build/workers-api/#workflowstep">steps</a>. <code>sleep</code> steps do not count against this limit.</p>
<p>We've also added:</p>
<ul>
<li><code>instanceId</code> as property to the <a href="/workflows/build/workers-api/#workflowevent"><code>WorkflowEvent</code></a> type, allowing you to retrieve the current instance ID from within a running Workflow instance</li>
<li>Improved queueing logic for Workflow instances beyond the current maximum concurrent instances, reducing the cases where instances are stuck in the queued state.</li>
<li>Support for <a href="/workflows/build/workers-api/#pause"><code>pause</code> and <code>resume</code></a> for Workflow instances in a queued state.</li>
</ul>
<p>We're continuing to work on increases to the number of concurrent Workflow instances, steps, and support for a new <code>waitForEvent</code> API over the coming weeks.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-13">Jan 13, 2025</time><div>
<h2 id="post-2025-01-13-waf-release"><a href="/changelog/post/2025-01-13-waf-release/">WAF Release - 2025-01-13</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6e0bfbe4b9c6454c8bd7bd24f49e5840">f49e5840</code>
</td>
<td>100704</td>
<td>
				Cleo Harmony - Auth Bypass - CVE:CVE-2024-55956, CVE:CVE-2024-55953
</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="c993997b7d904a9e89448fe6a6d43bc2">a6d43bc2</code>
</td>
<td>100705</td>
<td>Sentry - SSRF</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f40ce742be534ba19d610961ce6311bb">ce6311bb</code>
</td>
<td>100706</td>
<td>Apache Struts - Remote Code Execution - CVE:CVE-2024-53677</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="67ac639a845c482d948b465b2233da1f">2233da1f</code>
</td>
<td>100707</td>
<td>
				FortiWLM - Remote Code Execution - CVE:CVE-2023-48782,
				CVE:CVE-2023-34993, CVE:CVE-2023-34990
</td>
<td>Log</td>
<td>Block</td>
<td>New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="870cca2b874d41738019d4c3e31d972a">e31d972a</code>
</td>
<td>100007C_BETA</td>
<td>Command Injection - Common Attack Commands</td>
<td></td>
<td>Disabled</td>
<td></td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-09">Jan 9, 2025</time><div>
<h2 id="post-2025-01-09-rules-overview"><a href="/changelog/post/2025-01-09-rules-overview/">New Rules Overview Interface</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p><strong>Rules Overview</strong> gives you a single page to manage all your <a href="/rules/">Cloudflare Rules</a>.</p>
<p>What you can do:</p>
<ul>
<li><strong>See all your rules in one place</strong> – No more clicking around.</li>
<li><strong>Find rules faster</strong> – Search by name.</li>
<li><strong>Understand execution order</strong> – See how rules run in sequence.</li>
<li><strong>Debug easily</strong> – Use <a href="/rules/trace-request/">Trace</a> without switching tabs.</li>
</ul>
<p>Check it out in <a href="https://dash.cloudflare.com/?to=/:account/:zone/rules/overview">Rules &gt; Overview</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-01-08">Jan 8, 2025</time><div>
<h2 id="post-2025-01-08-smart-tiered-cache-for-load-balancing"><a href="/changelog/post/2025-01-08-smart-tiered-cache-for-load-balancing/">Smart Tiered Cache optimizes Load Balancing Pools</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now achieve higher cache hit rates and reduce origin load when using <a href="/load-balancing/">Load Balancing</a> with <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a>. Cloudflare automatically selects a single, optimal tiered data center for all origins in your Load Balancing Pool.</p>
<h4 id="2025-01-08-smart-tiered-cache-for-load-balancing-how-it-works">How it works</h4>
<p>When you use <a href="/load-balancing/">Load Balancing</a> with <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a>, Cloudflare analyzes performance metrics across your pool's origins and automatically selects the optimal Upper Tier data center for the entire pool. This means:</p>
<ul>
<li><strong>Consistent cache location</strong>: All origins in the pool share the same Upper Tier cache.</li>
<li><strong>Higher HIT rates</strong>: Requests for the same content hit the cache more frequently.</li>
<li><strong>Reduced origin requests</strong>: Fewer requests reach your origin servers.</li>
<li><strong>Improved performance</strong>: Faster response times for cache HITs.</li>
</ul>
<h4 id="2025-01-08-smart-tiered-cache-for-load-balancing-example-workflow">Example workflow</h4>
<pre><code class="language-txt">Load Balancing Pool: api-pool&#10;├── Origin 1: api-1.example.com&#10;├── Origin 2: api-2.example.com&#10;└── Origin 3: api-3.example.com&#10;    ↓&#10;Selected Upper Tier: [Optimal data center based on pool performance]&#10;</code></pre>
<h4 id="2025-01-08-smart-tiered-cache-for-load-balancing-get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> on your zone and configure your <a href="/load-balancing/">Load Balancing Pool</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/47/">Previous</a><span>Page 48 of 50</span><a class="pagination-next" rel="next" href="/changelog/49/">Next</a></nav>
</div>
