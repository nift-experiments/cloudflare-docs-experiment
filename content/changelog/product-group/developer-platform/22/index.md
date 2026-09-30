<h1 id="changelog">Changelog</h1>

<h2 id="hyperdrive-reduces-query-latency-by-up-to-90-and-now-supports-ip-access-control-lists"><a href="/changelog/post/2025-03-04-hyperdrive-pooling-near-database-and-ip-range-egress/">Hyperdrive reduces query latency by up to 90% and now supports IP access control lists</a></h2>
<p><em>2025-03-07</em></p>
<p>Hyperdrive now pools database connections in one or more regions close to your database. This means that your uncached queries and new database connections have up to 90% less latency as measured from connection pools.</p>
<p><img src="/assets/upstream/images/hyperdrive/configuration/hyperdrive-regional-pooling-query-latency-improvement.png" alt="Hyperdrive query latency decreases by 90% during Hyperdrive's gradual rollout of regional pooling." /></p>
<p>By improving placement of Hyperdrive database connection pools, Workers' Smart Placement is now more effective when used with Hyperdrive, ensuring that your Worker can be placed as close to your database as possible.</p>
<p>With this update, Hyperdrive also uses <a href="https://www.cloudflare.com/ips/">Cloudflare's standard IP address ranges</a> to connect to your database. This enables you to configure the firewall policies (IP access control lists) of your database to only allow access from Cloudflare and Hyperdrive.</p>
<p>Refer to <a href="/hyperdrive/concepts/how-hyperdrive-works/">documentation on how Hyperdrive makes connecting to regional databases from Cloudflare Workers fast</a>.</p>
<p>This improvement is enabled on all Hyperdrive configurations.</p>


<h2 id="set-retention-polices-for-your-r2-bucket-with-bucket-locks"><a href="/changelog/post/2025-03-06-r2-bucket-locks/">Set retention polices for your R2 bucket with bucket locks</a></h2>
<p><em>2025-03-06</em></p>
<p>You can now use <a href="/r2/buckets/bucket-locks/">bucket locks</a> to set retention policies on your <a href="/r2/buckets/">R2 buckets</a> (or specific prefixes within your buckets) for a specified period — or indefinitely. This can help ensure compliance by protecting important data from accidental or malicious deletion.</p>
<p>Locks give you a few ways to ensure your objects are retained (not deleted or overwritten). You can:</p>
<ul>
<li>Lock objects for a specific duration, for example 90 days.</li>
<li>Lock objects until a certain date, for example January 1, 2030.</li>
<li>Lock objects indefinitely, until the lock is explicitly removed.</li>
</ul>
<p>Buckets can have up to 1,000 <a href="/r2/buckets/">bucket lock rules</a>. Each rule specifies which objects it covers (via prefix) and how long those objects must remain retained.</p>
<p>Here are a couple of examples showing how you can configure bucket lock rules using <a href="/workers/wrangler/">Wrangler</a>:</p>
<h4 id="2025-03-06-r2-bucket-locks-ensure-all-objects-in-a-bucket-are-retained-for-at-least-180-days">Ensure all objects in a bucket are retained for at least 180 days</h4>
<pre><code class="language-sh">npx wrangler r2 bucket lock add &lt;bucket&gt; --name 180-days-all --retention-days 180&#10;</code></pre>
<h4 id="2025-03-06-r2-bucket-locks-prevent-deletion-or-overwriting-of-all-logs-indefinitely-via-prefix">Prevent deletion or overwriting of all logs indefinitely (via prefix)</h4>
<pre><code class="language-sh">npx wrangler r2 bucket lock add &lt;bucket&gt; --name indefinite-logs --prefix logs/ --retention-indefinite&#10;</code></pre>
<p>For more information on bucket locks and how to set retention policies for objects in your R2 buckets, refer to our <a href="/r2/buckets/bucket-locks/">documentation</a>.</p>


<h2 id="introducing-media-transformations-from-cloudflare-stream"><a href="/changelog/post/2025-03-06-media-transformations/">Introducing Media Transformations from Cloudflare Stream</a></h2>
<p><em>2025-03-06</em></p>
<p>Today, we are thrilled to announce Media Transformations, a new service that
brings the magic of <a href="/images/optimization/transformations/overview/">Image Transformations</a> to
<em>short-form video files,</em> wherever they are stored!</p>
<p>For customers with a huge volume of short video — generative AI output,
e-commerce product videos, social media clips, or short marketing content —
uploading those assets to Stream is not always practical. Sometimes, the
greatest friction to getting started was the thought of all that migrating.
Customers want a simpler solution that retains their current storage strategy to
deliver small, optimized MP4 files. Now you can do that with Media
Transformations.</p>
<p>To transform a video or image,
<a href="/stream/transform-videos/#getting-started">enable transformations</a> for your
zone, then make a simple request with a specially formatted URL. The result is
an MP4 that can be used in an HTML video element without a player library.
If your zone already has Image Transformations enabled, then it is ready to
optimize videos with Media Transformations, too.</p>
<pre><code class="language-text">https://example.com/cdn-cgi/media/&lt;OPTIONS&gt;/&lt;SOURCE-VIDEO&gt;&#10;</code></pre>
<p>For example, we have a short video of the mobile in Austin's office. The
original is nearly 30 megabytes and wider than necessary for this layout.
Consider a simple width adjustment:</p>
<video controls>
	<source src="https://developers.cloudflare.com/cdn-cgi/media/width=640/https://middlecache.ced.cloudflare.com/v1/aus-mobile/aus-mobile.mp4" />
</video>
<pre><code class="language-text">https://example.com/cdn-cgi/media/width=640/&lt;SOURCE-VIDEO&gt;&#10;https://developers.cloudflare.com/cdn-cgi/media/width=640/https://middlecache.ced.cloudflare.com/v1/aus-mobile/aus-mobile.mp4&#10;</code></pre>
<p>The result is less than 3 megabytes, properly sized, and delivered dynamically
so that customers do not have to manage the creation and storage of these
transformed assets.</p>
<p>For more information, learn about <a href="/stream/transform-videos/">Transforming Videos</a>.</p>


<h2 id="use-the-latest-javascript-features-with-wrangler-cli-v4-0-0-rc-0"><a href="/changelog/post/2025-02-28-wrangler-v4-rc/">Use the latest JavaScript features with Wrangler CLI v4.0.0-rc.0</a></h2>
<p><em>2025-02-28</em></p>
<p>We've released a release candidate of the next major version of <a href="/workers/wrangler/">Wrangler</a>, the CLI for Cloudflare Workers — <code>wrangler@4.0.0-rc.0</code>.</p>
<p>You can run the following command to install it and be one of the first to try it out:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i wrangler@v4-rc</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i wrangler@v4-rc" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add wrangler@v4-rc</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add wrangler@v4-rc" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add wrangler@v4-rc</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add wrangler@v4-rc" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add wrangler@v4-rc</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add wrangler@v4-rc" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Unlike previous major versions of Wrangler, which were <a href="https://blog.cloudflare.com/wrangler-v2-beta/">foundational rewrites</a> and <a href="https://blog.cloudflare.com/wrangler3/">rearchitectures</a> — Version 4 of Wrangler includes a much smaller set of changes. If you use Wrangler today, your workflow is very unlikely to change. Before we release Wrangler v4 and advance past the release candidate stage, we'll share a detailed migration guide in the Workers developer docs. But for the vast majority of cases, you won't need to do anything to migrate — things will just work as they do today. We are sharing this release candidate in advance of the official release of v4, so that you can try it out early and share feedback.</p>
<h4 id="2025-02-28-wrangler-v4-rc-new-javascript-language-features-that-you-can-now-use-with-wrangler-v4">New JavaScript language features that you can now use with Wrangler v4</h4>
<p>Version 4 of Wrangler updates the version of <a href="https://esbuild.github.io/">esbuild</a> that Wrangler uses internally, allowing you to use modern JavaScript language features, including:</p>
<h5 id="2025-02-28-wrangler-v4-rc-the-using-keyword-from-explicit-resource-management">The <code>using</code> keyword from Explicit Resource Management</h5>
<p>The <a href="/workers/runtime-apis/rpc/lifecycle/#explicit-resource-management"><code>using</code> keyword from the Explicit Resource Management standard</a> makes it easier to work with the <a href="/workers/runtime-apis/rpc/">JavaScript-native RPC system built into Workers</a>. This means that when you obtain a stub, you can ensure that it is automatically disposed when you exit scope it was created in:</p>
<pre><code class="language-js">function sendEmail(id, message) {&#10;  using user = await env.USER_SERVICE.findUser(id);&#10;  await user.sendEmail(message);&#10;&#10;  // user[Symbol.dispose]() is implicitly called at the end of the scope.&#10;}&#10;</code></pre>
<h5 id="2025-02-28-wrangler-v4-rc-import-attributes">Import attributes</h5>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import/with">Import attributes</a> allow you to denote the type or other attributes of the module that your code imports. For example, you can import a JSON module, using the following syntax:</p>
<pre><code class="language-js">import data from &quot;./data.json&quot; with { type: &quot;json&quot; };&#10;</code></pre>
<h4 id="2025-02-28-wrangler-v4-rc-other-changes">Other changes</h4>
<h5 id="2025-02-28-wrangler-v4-rc-local-is-now-the-default-for-all-cli-commands"><code>--local</code> is now the default for all CLI commands</h5>
<p>All commands that access resources (for example, <code>wrangler kv</code>, <code>wrangler r2</code>, <code>wrangler d1</code>) now access local datastores by default, ensuring consistent behavior.</p>
<h5 id="2025-02-28-wrangler-v4-rc-clearer-policy-for-the-minimum-required-version-of-node-js-required-to-run-wrangler">Clearer policy for the minimum required version of Node.js required to run Wrangler</h5>
<p>Moving forward, the <a href="https://nodejs.org/en/about/previous-releases">active, maintenance, and current versions of Node.js</a> will be officially supported by Wrangler. This means the minimum officially supported version of Node.js you must have installed for Wrangler v4 will be Node.js v18 or later. This policy mirrors how many other packages and CLIs support older versions of Node.js, and ensures that as long as you are using a version of Node.js that the Node.js project itself supports, this will be supported by Wrangler as well.</p>
<h5 id="2025-02-28-wrangler-v4-rc-features-previously-deprecated-in-wrangler-v3-are-now-removed-in-wrangler-v4">Features previously deprecated in Wrangler v3 are now removed in Wrangler v4</h5>
<p>All previously deprecated features in <a href="https://developers.cloudflare.com/workers/wrangler/deprecations/#wrangler-v2">Wrangler v2</a> and in <a href="https://developers.cloudflare.com/workers/wrangler/deprecations/#wrangler-v3">Wrangler v3</a> have now been removed. Additionally, the following features that were deprecated during the Wrangler v3 release have been removed:</p>
<ul>
<li>Legacy Assets (using <code>wrangler dev/deploy --legacy-assets</code> or the <code>legacy_assets</code> config file property). Instead, we recommend you <a href="https://developers.cloudflare.com/workers/static-assets/">migrate to Workers assets</a>.</li>
<li>Legacy Node.js compatibility (using <code>wrangler dev/deploy --node-compat</code> or the <code>node_compat</code> config file property). Instead, use the <a href="https://developers.cloudflare.com/workers/runtime-apis/nodejs"><code>nodejs_compat</code> compatibility flag</a>. This includes the functionality from legacy <code>node_compat</code> polyfills and natively implemented Node.js APIs.</li>
<li><code>wrangler version</code>. Instead, use <code>wrangler --version</code> to check the current version of Wrangler.</li>
<li><code>getBindingsProxy()</code> (via <code>import { getBindingsProxy } from &quot;wrangler&quot;</code>). Instead, use the <a href="https://developers.cloudflare.com/workers/wrangler/api/#getplatformproxy"><code>getPlatformProxy()</code> API</a>, which takes exactly the same arguments.</li>
<li><code>usage_model</code>. This no longer has any effect, after the <a href="https://blog.cloudflare.com/workers-pricing-scale-to-zero/">rollout of Workers Standard Pricing</a>.</li>
</ul>
<p>We'd love your feedback! If you find a bug or hit a roadblock when upgrading to Wrangler v4, <a href="https://github.com/cloudflare/workers-sdk/issues/new?template=bug-template.yaml">open an issue on the <code>cloudflare/workers-sdk</code> repository on GitHub</a>.</p>


<h2 id="new-rest-api-is-in-open-beta"><a href="/changelog/post/2025-02-27-br-rest-api-beta/">New REST API is in open beta!</a></h2>
<p><em>2025-02-27</em></p>
<p>We've released a new REST API for <a href="/browser-run/">Browser Rendering</a> in open beta, making interacting with browsers easier than ever. This new API provides endpoints for common browser actions, with more to be added in the future.</p>
<p>With the <strong>REST API</strong> you can:</p>
<ul>
<li><strong>Capture screenshots</strong> – Use <code>/screenshot</code> to take a screenshot of a webpage from provided URL or HTML.</li>
<li><strong>Generate PDFs</strong> – Use <code>/pdf</code> to convert web pages into PDFs.</li>
<li><strong>Extract HTML content</strong> – Use <code>/content</code> to retrieve the full HTML from a page.
<strong>Snapshot (HTML + Screenshot)</strong> – Use <code>/snapshot</code> to capture both the page's HTML and a screenshot in one request</li>
<li><strong>Scrape Web Elements</strong> – Use <code>/scrape</code> to extract specific elements from a page.</li>
</ul>
<p>For example, to capture a screenshot:</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/screenshot&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;html&quot;: &quot;Hello World!&quot;,&#10;    &quot;screenshotOptions&quot;: {&#10;      &quot;type&quot;: &quot;webp&quot;,&#10;      &quot;omitBackground&quot;: true&#10;    }&#10;  }&#x27; \&#10;  &#45;-output &quot;screenshot.webp&quot;&#10;</code></pre>
<p>Learn more in our <a href="/browser-run/quick-actions/">documentation</a>.</p>


<h2 id="introducing-guardrails-in-ai-gateway"><a href="/changelog/post/2025-02-26-guardrails/">Introducing Guardrails in AI Gateway</a></h2>
<p><em>2025-02-26</em></p>
<p><a href="/ai-gateway/">AI Gateway</a> now includes <a href="/ai-gateway/features/guardrails/">Guardrails</a>, to help you monitor your AI apps for harmful or inappropriate content and deploy safely.</p>
<p>Within the AI Gateway settings, you can configure:</p>
<ul>
<li><strong>Guardrails</strong>: Enable or disable content moderation as needed.</li>
<li><strong>Evaluation scope</strong>: Select whether to moderate user prompts, model responses, or both.</li>
<li><strong>Hazard categories</strong>: Specify which categories to monitor and determine whether detected inappropriate content should be blocked or flagged.</li>
</ul>
<p><img src="/assets/upstream/images/ai-gateway/Guardrails.png" alt="Guardrails in AI Gateway" /></p>
<p>Learn more in the <a href="https://blog.cloudflare.com/guardrails-in-ai-gateway/">blog</a> or our <a href="/ai-gateway/features/guardrails/">documentation</a>.</p>


<h2 id="introducing-the-agents-sdk"><a href="/changelog/post/2025-02-25-agents-sdk/">Introducing the Agents SDK</a></h2>
<p><em>2025-02-25</em></p>
<p>We've released the <a href="http://blog.cloudflare.com/build-ai-agents-on-cloudflare/">Agents SDK</a>, a package and set of tools that help you build and ship AI Agents.</p>
<p>You can get up and running with a <a href="https://github.com/cloudflare/agents-starter">chat-based AI Agent</a> (and deploy it to Workers) that uses the Agents SDK, tool calling, and state syncing with a React-based front-end by running the following command:</p>
<pre><code class="language-sh">npm create cloudflare@latest agents-starter -- --template=&quot;cloudflare/agents-starter&quot;&#10;&#35; open up README.md and follow the instructions&#10;</code></pre>
<p>You can also add an Agent to any existing Workers application by installing the <code>agents</code> package directly</p>
<pre><code class="language-sh">npm i agents&#10;</code></pre>
<p>... and then define your first Agent:</p>
<pre><code class="language-ts">import { Agent } from &quot;agents&quot;;&#10;&#10;export class YourAgent extends Agent&lt;Env&gt; {&#10;	// Build it out&#10;	// Access state on this.state or query the Agent&#x27;s database via this.sql&#10;	// Handle WebSocket events with onConnect and onMessage&#10;	// Run tasks on a schedule with this.schedule&#10;	// Call AI models&#10;	// ... and/or call other Agents.&#10;}&#10;</code></pre>
<p>Head over to the <a href="/agents/">Agents documentation</a> to learn more about the Agents SDK, the SDK APIs, as well as how to test and deploying agents to production.</p>


<h2 id="workers-ai-now-supports-structured-json-outputs"><a href="/changelog/post/2025-02-25-json-mode/">Workers AI now supports structured JSON outputs.</a></h2>
<p><em>2025-02-25</em></p>
<p>Workers AI now supports structured JSON outputs with <a href="/workers-ai/features/json-mode/">JSON mode</a>, which allows you to request a structured output response when interacting with AI models.</p>
<p>This makes it much easier to retrieve structured data from your AI models, and avoids the (error prone!) need to parse large unstructured text responses to extract your data.</p>
<p>JSON mode in Workers AI is compatible with the OpenAI SDK's <a href="https://platform.openai.com/docs/guides/structured-outputs">structured outputs</a> <code>response_format</code> API, which can be used directly in a Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17816.md")</div>
<p>To learn more about JSON mode and structured outputs, visit the <a href="/workers-ai/features/json-mode/">Workers AI documentation</a>.</p>


<h2 id="concurrent-workflow-instances-limits-increased"><a href="/changelog/post/2025-02-25-workflows-concurrency-increased/">Concurrent Workflow instances limits increased.</a></h2>
<p><em>2025-02-25</em></p>
<p><a href="/workflows/">Workflows</a> now supports up to 4,500 concurrent (running) instances, up from the previous limit of 100. This limit will continue to increase during the Workflows open beta. This increase applies to all users on the Workers Paid plan, and takes effect immediately.</p>
<p>Review the Workflows <a href="/workflows/reference/limits">limits documentation</a> and/or dive into the <a href="/workflows/get-started/guide/">get started guide</a> to start building on Workflows.</p>


<h2 id="bind-the-images-api-to-your-worker"><a href="/changelog/post/2025-02-21-images-bindings-in-workers/">Bind the Images API to your Worker</a></h2>
<p><em>2025-02-24</em></p>
<p>You can now <a href="/images/optimization/binding/">interact with the Images API</a> directly in your Worker.</p>
<p>This allows more fine-grained control over transformation request flows and cache behavior. For example, you can resize, manipulate, and overlay images without requiring them to be accessible through a URL.</p>
<p>The Images binding can be configured in the Cloudflare dashboard for your Worker or in the Wrangler configuration file in your project's directory:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17735.md")</div>
<p>Within your Worker code, you can interact with this binding by using <code>env.IMAGES</code>.</p>
<p>Here's how you can rotate, resize, and blur an image, then output the image as AVIF:</p>
<pre><code class="language-ts">const info = await env.IMAGES.info(stream);&#10;// stream contains a valid image, and width/height is available on the info object&#10;&#10;const response = (&#10;	await env.IMAGES.input(stream)&#10;		.transform({ rotate: 90 })&#10;		.transform({ width: 128 })&#10;		.transform({ blur: 20 })&#10;		.output({ format: &quot;image/avif&quot; })&#10;).response();&#10;&#10;return response;&#10;</code></pre>
<p>For more information, refer to <a href="/images/optimization/binding/">Images Bindings</a>.</p>


<h2 id="super-slurper-now-supports-migrations-from-all-s3-compatible-storage-providers"><a href="/changelog/post/2025-02-24-r2-super-slurper-s3-compatible-support/">Super Slurper now supports migrations from all S3-compatible storage providers</a></h2>
<p><em>2025-02-24</em></p>
<p><a href="/r2/data-migration/super-slurper/">Super Slurper</a> can now migrate data from any S3-compatible object storage provider to <a href="/r2/">Cloudflare R2</a>. This includes transfers from services like MinIO, Wasabi, Backblaze B2, and DigitalOcean Spaces.</p>
<p><img src="/assets/upstream/images/changelog/r2/super-slurper-s3-compat-screenshot-border.png" alt="Super Slurper S3-Compatible Source" /></p>
<p>For more information on Super Slurper and how to migrate data from your existing S3-compatible storage buckets to R2, refer to our <a href="/r2/data-migration/super-slurper/">documentation</a>.</p>


<h2 id="workers-ai-larger-context-windows"><a href="/changelog/post/2025-02-24-context-windows/">Workers AI larger context windows</a></h2>
<p><em>2025-02-24</em></p>
<p>We've updated the Workers AI text generation models to include context windows and limits definitions and changed our APIs to estimate and validate the number of tokens in the input prompt, not the number of characters.</p>
<p>This update allows developers to use larger context windows when interacting with Workers AI models, which can lead to better and more accurate results.</p>
<p>Our <a href="/workers-ai/models/">catalog page</a> provides more information about each model's supported context window.</p>


<h2 id="zaraz-moves-to-the-tag-management-category-in-the-cloudflare-dashboard"><a href="/changelog/post/2025-02-24-zaraz-dash-placement/">Zaraz moves to the “Tag Management” category in the Cloudflare dashboard</a></h2>
<p><em>2025-02-24</em></p>
<p><img src="/assets/upstream/images/zaraz/zaraz-account-level.jpg" alt="Zaraz at zone level to Tag management at account level" /></p>
<p>Previously, you could only configure Zaraz by going to each individual zone under your Cloudflare account. Now, if you’d like to get started with Zaraz or manage your existing configuration, you can navigate to the <a href="https://dash.cloudflare.com/?to=/:account/tag-management/zaraz">Tag Management</a> section on the Cloudflare dashboard – this will make it easier to compare and configure the same settings across multiple zones.</p>
<p>These changes will not alter any existing configuration or entitlements for zones you already have Zaraz enabled on. If you’d like to edit existing configurations, you can go to the <a href="https://dash.cloudflare.com/?to=/:account/tag-management/zaraz">Tag Setup</a> section of the dashboard, and select the zone you'd like to edit.</p>


<h2 id="workers-for-platforms-instant-dispatch-for-newly-created-user-workers"><a href="/changelog/post/2025-02-20-synchronous-uploads/">Workers for Platforms - Instant dispatch for newly created User Workers</a></h2>
<p><em>2025-02-20T17:00:00+00:00</em></p>
<p><a href="https://developers.cloudflare.com/cloudflare-for-platforms/">Workers for Platforms</a> is an architecture wherein a centralized <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dynamic-dispatch-worker">dispatch Worker</a> processes incoming requests and routes them to isolated sub-Workers, called <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#user-workers">User Workers</a>.</p>
<p><img src="/assets/upstream/images/changelog/workers-for-platforms/wfp-request.png" alt="Workers for Platforms Requests" /></p>
<p>Previously, when a new User Worker was uploaded, there was a short delay before it became available for dispatch. This meant that even though an API request could return a 200 OK response, the script might not yet be ready to handle requests, causing unexpected failures for platforms that immediately dispatch to new Workers.</p>
<p><strong>With this update, first-time uploads of User Workers are now deployed synchronously</strong>. A 200 OK response guarantees the script is fully provisioned and ready to handle traffic immediately, ensuring more predictable deployments and reducing errors.</p>


<h2 id="autofix-worker-name-configuration-errors-at-build-time"><a href="/changelog/post/2025-02-20-builds-name-conflict/">Autofix Worker name configuration errors at build time</a></h2>
<p><em>2025-02-20</em></p>
<p><img src="/assets/upstream/images/workers/platform/ci-cd/gh-auto-pr-name.png" alt="Auto-fixing Workers Name in Git Repo" /></p>
<p>Small misconfigurations shouldn’t break your deployments. Cloudflare is introducing automatic error detection and fixes in <a href="/workers/ci-cd/builds/">Workers Builds</a>, identifying common issues in your wrangler.toml or wrangler.jsonc and proactively offering fixes, so you spend less time debugging and more time shipping.</p>
<p>Here's how it works:</p>
<ol>
<li>Before running your build, Cloudflare checks your Worker's Wrangler configuration file (wrangler.toml or wrangler.jsonc) for common errors.</li>
<li>Once you submit a build, if Cloudflare finds an error it can fix, it will submit a pull request to your repository that fixes it.</li>
<li>Once you merge this pull request, Cloudflare will run another build.</li>
</ol>
<p>We're starting with fixing name mismatches between your Wrangler file and the Cloudflare dashboard, a top cause of build failures.</p>
<p>This is just the beginning, we want your feedback on what other errors we should catch and fix next. Let us know in the Cloudflare Developers Discord, <a href="https://discord.com/channels/595317990191398933/1064502845061210152">#workers-and-pages-feature-suggestions</a>.</p>


<h2 id="workers-ai-updated-pricing"><a href="/changelog/post/2025-02-20-updated-pricing-docs/">Workers AI updated pricing</a></h2>
<p><em>2025-02-20</em></p>
<p>We've updated the Workers AI <a href="/workers-ai/platform/pricing/">pricing</a> to include the latest models and how model usage maps to Neurons.</p>
<ul>
<li>Each model's core input format(s) (tokens, audio seconds, images, etc) now include mappings to Neurons, making it easier to understand how your included Neuron volume is consumed and how you are charged at scale</li>
<li>Per-model pricing, instead of the previous bucket approach, allows us to be more flexible on how models are charged based on their size, performance and capabilities. As we optimize each model, we can then pass on savings for that model.</li>
<li>You will still only pay for what you consume: Workers AI inference is serverless, and not billed by the hour.</li>
</ul>
<p>Going forward, models will be launched with their associated Neuron costs, and we'll be updating the Workers AI dashboard and API to reflect consumption in both raw units and Neurons. Visit the <a href="/workers-ai/platform/pricing/">Workers AI pricing</a> page to learn more about Workers AI pricing.</p>


<h2 id="customize-queue-message-retention-periods"><a href="/changelog/post/2025-02-14-customize-queue-retention-period/">Customize queue message retention periods</a></h2>
<p><em>2025-02-14 12:00:00 UTC</em></p>
<p>You can now customize a queue's message retention period, from a minimum of 60 seconds to a maximum of 14 days. Previously, it was fixed to the default of 4 days.</p>
<p><img src="/assets/upstream/images/queues/customize-retention-period.png" alt="Customize a queue's message retention period" /></p>
<p>You can customize the retention period on the settings page for your queue, or using Wrangler:</p>
<pre><code class="language-bash">$ wrangler queues update my-queue --message-retention-period-secs 600&#10;</code></pre>
<p>This feature is available on all new and existing queues. If you haven't used Cloudflare Queues before, <a href="/queues/get-started">get started with the Cloudflare Queues guide</a>.</p>


<h2 id="build-ai-agents-with-example-prompts"><a href="/changelog/post/2025-02-14-example-ai-prompts/">Build AI Agents with Example Prompts</a></h2>
<p><em>2025-02-14</em></p>
<p>We've added an <a href="/workers/get-started/prompting/">example prompt</a> to help you get started with building AI agents and applications on Cloudflare <a href="/workers/">Workers</a>, including <a href="/workflows/">Workflows</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/kv/">Workers KV</a>.</p>
<p>You can use this prompt with your favorite AI model, including Claude 3.5 Sonnet, OpenAI's o3-mini, Gemini 2.0 Flash, or Llama 3.3 on Workers AI. Models with large context windows will allow you to paste the prompt directly: provide your own prompt within the <code>&lt;user_prompt&gt;&lt;/user_prompt&gt;</code> tags.</p>
<pre><code class="language-sh">{paste_prompt_here}&#10;&lt;user_prompt&gt;&#10;user: Build an AI agent using Cloudflare Workflows. The Workflow should run when a new GitHub issue is opened on a specific project with the label &#x27;help&#x27; or &#x27;bug&#x27;, and attempt to help the user troubleshoot the issue by calling the OpenAI API with the issue title and description, and a clear, structured prompt that asks the model to suggest 1-3 possible solutions to the issue. Any code snippets should be formatted in Markdown code blocks. Documentation and sources should be referenced at the bottom of the response. The agent should then post the response to the GitHub issue. The agent should run as the provided GitHub bot account.&#10;&lt;/user_prompt&gt;&#10;</code></pre>
<p>This prompt is still experimental, but we encourage you to try it out and <a href="https://github.com/cloudflare/cloudflare-docs/issues/new?template=content.edit.yml">provide feedback</a>.</p>


<h2 id="super-slurper-now-transfers-data-to-r2-up-to-5x-faster"><a href="/changelog/post/2025-02-14-r2-super-slurper-faster-migrations/">Super Slurper now transfers data to R2 up to 5x faster</a></h2>
<p><em>2025-02-14</em></p>
<p><a href="/r2/data-migration/super-slurper/">Super Slurper</a> now transfers data from cloud object storage providers like AWS S3 and Google Cloud Storage to <a href="/r2/">Cloudflare R2</a> up to 5x faster than it did before.</p>
<p>We moved from a centralized service to a distributed system built on the Cloudflare Developer Platform — using <a href="/workers/">Cloudflare Workers</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/queues/">Queues</a> — to both improve performance and increase system concurrency capabilities (and we'll share more details about how we did it soon!)</p>
<p><img src="/assets/upstream/images/r2/slurper-objects-over-time-border.png" alt="Super Slurper Objects Migrated" /></p>
<p><em>Time to copy 75,000 objects from AWS S3 to R2 decreased from 15 minutes 30 seconds (old) to 3 minutes 25 seconds (after performance improvements)</em></p>
<p>For more information on Super Slurper and how to migrate data from existing object storage to R2, refer to our <a href="/r2/data-migration/super-slurper/">documentation</a>.</p>


<h2 id="rewind-replay-resume-introducing-dvr-for-stream-live"><a href="/changelog/post/2025-02-14-introducing-dvr-for-stream-live/">Rewind, Replay, Resume: Introducing DVR for Stream Live</a></h2>
<p><em>2025-02-14</em></p>
<p>Previously, all viewers watched &quot;the live edge,&quot; or the latest content of the
broadcast, synchronously. If a viewer paused for more than a few seconds,
the player would automatically &quot;catch up&quot; when playback started again. Seeking
through the broadcast was only available once the recording was available after
it concluded.</p>
<p>Starting today, customers can make a small adjustment to the player
embed or manifest URL to enable the DVR experience for their viewers. By
offering this feature as an opt-in adjustment, our customers are empowered to
pick the best experiences for their applications.</p>
<p>When building a player embed code or manifest URL, just add <code>dvrEnabled=true</code> as
a query parameter. There are some things to be aware of when using this option.
For more information, refer to <a href="/stream/stream-live/dvr-for-live/">DVR for Live</a>.</p>


<h2 id="create-and-deploy-workers-from-git-repositories"><a href="/changelog/post/2025-02-07-new-ways-to-get-started-on-workers/">Create and deploy Workers from Git repositories</a></h2>
<p><em>2025-02-07 00:00:00 UTC</em></p>
<p><img src="/assets/upstream/images/workers/choose-template-import-repo.png" alt="Import repo or choose template" /></p>
<p>You can now create a Worker by:</p>
<ul>
<li><strong>Importing a Git repository</strong>: Choose an existing Git repo on your GitHub/GitLab account and set up <a href="/workers/ci-cd/builds/configuration/">Workers Builds</a> to deploy your Worker.</li>
<li><strong>Deploying a template with Git</strong>: Choose from a brand new selection of production ready <a href="https://github.com/cloudflare/templates">examples</a> to help you get started with popular frameworks like <a href="https://astro.build/">Astro</a>, <a href="https://remix.run/">Remix</a> and <a href="https://nextjs.org/">Next</a> or build stateful applications with Cloudflare resources like <a href="/d1/">D1 databases</a>, <a href="/workers-ai/">Workers AI</a> or <a href="/durable-objects/">Durable Objects</a>! When you're ready to deploy, Cloudflare will set up your project by cloning the template to your GitHub/GitLab account, provisioning any required <a href="/workers/runtime-apis/bindings/">resources</a> and deploying your Worker.</li>
</ul>
<p>With every push to your chosen branch, Cloudflare will automatically build and deploy your Worker.</p>
<p>To get started, go to the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create">Workers dashboard</a>.</p>
<p>These new features are available today in the Cloudflare dashboard to a subset of Cloudflare customers, and will be coming to all customers in the next few weeks. Don't see it in your dashboard, but want early access? Add your Cloudflare Account ID to <a href="https://forms.gle/U1qhkF2snNJDGJJa9">this form</a>.</p>


<h2 id="request-timeouts-and-retries-with-ai-gateway"><a href="/changelog/post/2025-02-05-aig-request-handling/">Request timeouts and retries with AI Gateway</a></h2>
<p><em>2025-02-06</em></p>
<p>AI Gateway adds additional ways to handle requests - <a href="/ai-gateway/configuration/request-handling/#request-timeouts">Request Timeouts</a> and <a href="/ai-gateway/configuration/request-handling/#request-retries">Request Retries</a>, making it easier to keep your applications responsive and reliable.</p>
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


<h2 id="ai-gateway-adds-cerebras-elevenlabs-and-cartesia-as-new-providers"><a href="/changelog/post/2025-02-04-aig-provider-cartesia-eleven-cerebras/">AI Gateway adds Cerebras, ElevenLabs, and Cartesia as new providers</a></h2>
<p><em>2025-02-05</em></p>
<p><a href="/ai-gateway/">AI Gateway</a> has added three new providers: <a href="/ai-gateway/usage/providers/cartesia/">Cartesia</a>, <a href="/ai-gateway/usage/providers/cerebras/">Cerebras</a>, and <a href="/ai-gateway/usage/providers/elevenlabs/">ElevenLabs</a>, giving you more even more options for providers you can use through AI Gateway. Here's a brief overview of each:</p>
<ul>
<li><a href="/ai-gateway/usage/providers/cartesia/">Cartesia</a> provides text-to-speech models that produce natural-sounding speech with low latency.</li>
<li><a href="/ai-gateway/usage/providers/cerebras/">Cerebras</a> delivers low-latency AI inference to Meta's Llama 3.1 8B and Llama 3.3 70B models.</li>
<li><a href="/ai-gateway/usage/providers/elevenlabs/">ElevenLabs</a> offers text-to-speech models with human-like voices in 32 languages.</li>
</ul>
<p><img src="/assets/upstream/images/ai-gateway/cerebras2.png" alt="Example of Cerebras log in AI Gateway" /></p>
<p>To get started with AI Gateway, just update the base URL. Here's how you can send a request to <a href="/ai-gateway/usage/providers/cerebras/">Cerebras</a> using cURL:</p>
<pre><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/ACCOUNT_TAG/GATEWAY/cerebras/chat/completions \&#10; &#45;-header &#x27;content-type: application/json&#x27; \&#10; &#45;-header &#x27;Authorization: Bearer CEREBRAS_TOKEN&#x27; \&#10; &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;llama-3.3-70b&quot;,&#10;    &quot;messages&quot;: [&#10;        {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;    ]&#10;}&#x27;&#10;</code></pre>


<h2 id="terraform-v5-provider-is-now-generally-available"><a href="/changelog/post/2025-02-03-terraform-v5-provider/">Terraform v5 Provider is now generally available</a></h2>
<p><em>2025-02-03</em></p>
<p><img src="/assets/upstream/images/changelog/2024-02-03-terraform-v5-screenshot.png" alt="Screenshot of Terraform defining a Zone" /></p>
<p>Cloudflare's v5 Terraform Provider is now generally available. With this release, Terraform resources are now automatically generated based on OpenAPI Schemas. This change brings alignment across our SDKs, API documentation, and now Terraform Provider. The new provider boosts coverage by increasing support for API properties to 100%, adding 25% more resources, and more than 200 additional data sources. Going forward, this will also reduce the barriers to bringing more resources into Terraform across the broader Cloudflare API. This is a small, but important step to making more of our platform manageable through GitOps, making it easier for you to manage Cloudflare just like you do your other infrastructure.</p>
<p>The Cloudflare Terraform Provider v5 is a ground-up rewrite of the provider and introduces breaking changes for some resource types. Please refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">upgrade guide</a> for best practices, or the <a href="https://blog.cloudflare.com/automatically-generating-cloudflares-terraform-provider/">blog post on automatically generating Cloudflare's Terraform Provider</a> for more information about the approach.</p>
<p>For more info</p>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="https://developers.cloudflare.com/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="revamped-workers-metrics"><a href="/changelog/post/2025-02-03-workers-metrics-revamp/">Revamped Workers Metrics</a></h2>
<p><em>2025-02-03</em></p>
<p>We've revamped the <a href="https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/metrics/">Workers Metrics dashboard</a>.</p>
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


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/21/">Previous</a><span>Page 22 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/23/">Next</a></nav>
