<p>Wrangler optionally uses a configuration file to customize the development and deployment setup for a Worker.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15949.md")
</aside>
<p>It is best practice to treat Wrangler's configuration file as the <a href="#source-of-truth">source of truth</a> for configuring a Worker.</p>
<h2 id="sample-wrangler-configuration">Sample Wrangler configuration</h2>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15950.md")
</div>
<h2 id="environments">Environments</h2>
<p>You can define different configurations for a Worker using Wrangler <a href="/workers/wrangler/environments/">environments</a>.
There is a default (top-level) environment and you can create named environments that provide environment-specific configuration.</p>
<p>These are defined under <code>[env.&lt;name&gt;]</code> keys, such as <code>[env.staging]</code> which you can then preview or deploy with the <code>-e</code> / <code>--env</code> flag in the <code>wrangler</code> commands like <code>npx wrangler deploy --env staging</code>.</p>
<p>The majority of keys are inheritable, meaning that top-level configuration can be used in environments. <a href="/workers/runtime-apis/bindings/">Bindings</a>, such as <code>vars</code> or <code>kv_namespaces</code>, are not inheritable and need to be defined explicitly.</p>
<p>Further, there are a few keys that can <em>only</em> appear at the top-level.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15948.md")
</aside>
<h2 id="automatic-provisioning">Automatic provisioning</h2>
<a href="https://developers.cloudflare.com/changelog/2025-10-24-automatic-resource-provisioning/" target="_blank">
	<span class="nb-badge">Beta</span>
</a>
<p>Wrangler can automatically provision resources for you when you deploy your Worker without you having to create them ahead of time.</p>
<p>This currently works for the following resources: KV, R2, D1, Flagship, AI Search, Agent Memory, Dispatch Namespaces and Queues.</p>
<p>To use this feature, add bindings to your configuration file <em>without</em> adding resource IDs, or in the case of R2, a bucket name. Resources will be created with the name of your worker as the prefix.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15951.md")
</div>
<p>When you run <code>wrangler dev</code>, local resources will automatically be created which persist between runs. When you run <code>wrangler deploy</code>, resources will be created for you, and their IDs will be written back to your configuration file.</p>
<p>If you deploy a worker with resources and no resource IDs from the dashboard (for example, via GitHub), resources will be created, but their IDs will only be accessible via the dashboard. Currently, these resource IDs will not be written back to your repository.</p>
<h2 id="top-level-only-keys">Top-level only keys</h2>
<p>Top-level keys apply to the Worker as a whole (and therefore all environments). They cannot be defined within named environments.</p>
<ul>
<li><code>keep_vars</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Whether Wrangler should keep variables configured in the dashboard on deploy. Refer to <a href="#source-of-truth">source of truth</a>.</li>
</ul>
</li>
<li><code>send_metrics</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Whether Wrangler should send usage data to Cloudflare for this project. Defaults to <code>true</code>. You can learn more about this in our <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/wrangler/telemetry.md">data policy</a>.</li>
</ul>
</li>
<li><code>dependencies_instrumentation</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Configures npm package dependency instrumentation when deploying or uploading a Worker version. Defaults to enabled.</li>
<li><code>enabled</code> <span class="nb-type">boolean</span> — Whether Wrangler should collect and send npm package dependency metadata (package names and versions). Defaults to <code>true</code>.</li>
</ul>
</li>
<li><code>site</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional deprecated</span>
<ul>
<li>See the <a href="#workers-sites">Workers Sites</a> section below for more information. Cloudflare Pages and Workers Assets is preferred over this approach.</li>
<li>This is not supported by the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</li>
</ul>
</li>
</ul>
<h2 id="inheritable-keys">Inheritable keys</h2>
<p>Inheritable keys are configurable at the top-level, and can be inherited (or overridden) by environment-specific configuration.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15947.md")
</aside>
<ul>
<li><code>name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of your Worker. Alphanumeric characters (<code>a</code>,<code>b</code>,<code>c</code>, etc.) and dashes (<code>-</code>) only. Do not use underscores (<code>_</code>). Worker names can be up to 255 characters. If you plan to use a <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code> subdomain</a>, the name must be 63 characters or less and cannot start or end with a dash.</li>
</ul>
</li>
<li><code>main</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The path to the entrypoint of your Worker that will be executed. For example: <code>./src/index.ts</code>.</li>
</ul>
</li>
<li><code>compatibility_date</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>A date in the form <code>yyyy-mm-dd</code>, which will be used to determine which version of the Workers runtime is used. Refer to <a href="/workers/configuration/compatibility-dates/">Compatibility dates</a>.</li>
</ul>
</li>
<li><code>account_id</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>This is the ID of the account associated with your zone. You might have more than one account, so make sure to use the ID of the account associated with the zone/route you provide, if you provide one. It can also be specified through the <code>CLOUDFLARE_ACCOUNT_ID</code> environment variable.</li>
</ul>
</li>
<li><code>compatibility_flags</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A list of flags that enable features from upcoming features of the Workers runtime, usually used together with <code>compatibility_date</code>. Refer to <a href="/workers/configuration/compatibility-dates/">compatibility dates</a>.</li>
</ul>
</li>
<li><code>workers_dev</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Enables use of <code>*.workers.dev</code> subdomain to deploy your Worker. If you have a Worker that is only for <code>scheduled</code> events, you can set this to <code>false</code>. Defaults to <code>true</code>. Refer to <a href="#types-of-routes">types of routes</a>.</li>
</ul>
</li>
<li><code>preview_urls</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Enables use of Preview URLs to test your Worker. Defaults to value of <code>workers_dev</code>. Refer to <a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a>.</li>
</ul>
</li>
<li><code>route</code> <span class="nb-type">Route</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A route that your Worker should be deployed to. Only one of <code>routes</code> or <code>route</code> is required. Refer to <a href="#types-of-routes">types of routes</a>.</li>
</ul>
</li>
<li><code>routes</code> <span class="nb-type">Route[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>An array of routes that your Worker should be deployed to. Only one of <code>routes</code> or <code>route</code> is required. Refer to <a href="#types-of-routes">types of routes</a>.</li>
</ul>
</li>
<li><code>tsconfig</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Path to a custom <code>tsconfig</code>.</li>
<li>Not applicable if you're using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</li>
</ul>
</li>
<li><code>triggers</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Cron definitions to trigger a Worker's <code>scheduled</code> function. Refer to <a href="#triggers">triggers</a>.</li>
</ul>
</li>
<li><code>rules</code> <span class="nb-type">Rule</span> <span class="nb-metainfo">optional</span>
<ul>
<li>An ordered list of rules that define which modules to import, and what type to import them as. You will need to specify rules to use <code>Text</code>, <code>Data</code> and <code>CompiledWasm</code> modules, or when you wish to have a <code>.js</code> file be treated as an <code>ESModule</code> instead of <code>CommonJS</code>.</li>
<li>Not applicable if you're using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</li>
</ul>
</li>
<li><code>build</code> <span class="nb-type">Build</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Configures a custom build step to be run by Wrangler when building your Worker. Refer to <a href="#custom-builds">Custom builds</a>.</li>
<li>Not applicable if you're using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</li>
</ul>
</li>
<li><code>no_bundle</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Skip internal build steps and directly deploy your Worker script. You must have a plain JavaScript Worker with no dependencies.</li>
<li>Not applicable if you're using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</li>
</ul>
</li>
<li><code>find_additional_modules</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>If true then Wrangler will traverse the file tree below <code>base_dir</code>.
Any files that match <code>rules</code> will be included in the deployed Worker.
Defaults to true if <code>no_bundle</code> is true, otherwise false.
Can only be used with Module format Workers (not Service Worker format).</li>
<li>Not applicable if you're using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</li>
</ul>
</li>
<li><code>base_dir</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The directory in which module &quot;rules&quot; should be evaluated when including additional files (via <code>find_additional_modules</code>) into a Worker deployment. Defaults to the directory containing the <code>main</code> entry point of the Worker if not specified.</li>
<li>Not applicable if you're using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</li>
</ul>
</li>
<li><code>preserve_file_names</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Determines whether Wrangler will preserve the file names of additional modules bundled with the Worker.
The default is to prepend filenames with a content hash.
For example, <code>34de60b44167af5c5a709e62a4e20c4f18c9e3b6-favicon.ico</code>.</li>
<li>Not applicable if you're using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</li>
</ul>
</li>
<li><code>minify</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Minify the Worker script before uploading.</li>
<li>If you're using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>, <code>minify</code> is replaced by Vite's <a href="https://vite.dev/config/build-options.html#build-minify"><code>build.minify</code></a>.</li>
</ul>
</li>
<li><code>keep_names</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Wrangler uses esbuild to process the Worker code for development and deployment. This option allows
you to specify whether esbuild should apply its <a href="https://esbuild.github.io/api/#keep-names">keepNames</a> logic to the code or not. Defaults to <code>true</code>.</li>
</ul>
</li>
<li><code>logpush</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Enables Workers Trace Events Logpush for a Worker. Any scripts with this property will automatically get picked up by the Workers Logpush job configured for your account. Defaults to <code>false</code>. Refer to <a href="/workers/observability/logs/logpush/">Workers Logpush</a>.</li>
</ul>
</li>
<li><code>limits</code> <span class="nb-type">Limits</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Configures limits to be imposed on execution at runtime. Refer to <a href="#limits">Limits</a>.</li>
</ul>
</li>
</ul>
<ul>
<li><code>observability</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Configures automatic observability settings for telemetry data emitted from your Worker. Refer to <a href="#observability">Observability</a>.</li>
</ul>
</li>
<li><code>assets</code> <span class="nb-type">Assets</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Configures static assets that will be served. Refer to <a href="/workers/static-assets/binding/">Assets</a> for more details.</li>
</ul>
</li>
<li><code>exports</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Declares the Durable Object classes this Worker exports and their lifecycle state (<code>created</code>, <code>deleted</code>, <code>renamed</code>, <code>transferred</code>, <code>expecting-transfer</code>). Refer to <a href="/durable-objects/reference/durable-objects-migrations/">Durable Object class exports</a>. Mutually exclusive with <code>migrations</code>.</li>
</ul>
</li>
<li><code>migrations</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Legacy imperative configuration that maps a Durable Object from a class name to a runtime state. For new Workers, prefer <a href="/durable-objects/reference/durable-objects-migrations/"><code>exports</code></a>. Refer to <a href="/durable-objects/reference/durable-object-class-migrations-legacy/">Durable Object class migrations (legacy)</a>.</li>
</ul>
</li>
<li><code>placement</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Configures where your Worker runs to minimize latency to back-end services. Refer to <a href="/workers/configuration/placement/">Placement</a>.</li>
<li><code>mode</code> <span class="nb-type">string</span> — Set to <code>&quot;smart&quot;</code> to automatically place your Worker near back-end services based on observed latency.</li>
<li><code>region</code> <span class="nb-type">string</span> — Specify a cloud region (for example, <code>&quot;aws:us-east-1&quot;</code>, <code>&quot;gcp:europe-west1&quot;</code>, or <code>&quot;azure:westeurope&quot;</code>) to place your Worker near infrastructure in that region.</li>
<li><code>host</code> <span class="nb-type">string</span> — Specify a hostname and port for a single-homed layer 4 service (for example, <code>&quot;my_database_host.com:5432&quot;</code>) to place your Worker near that service.</li>
<li><code>hostname</code> <span class="nb-type">string</span> — Specify a hostname for a single-homed layer 7 service (for example, <code>&quot;my_api_server.com&quot;</code>) to place your Worker near that service.</li>
</ul>
</li>
</ul>
<h2 id="non-inheritable-keys">Non-inheritable keys</h2>
<p>Non-inheritable keys are configurable at the top-level, but cannot be inherited by environments and must be specified for each environment.</p>
<ul>
<li><code>define</code> <span class="nb-type">Record&lt;string, string&gt;</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A map of values to substitute when deploying your Worker.</li>
<li>If you're using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>, <code>define</code> is replaced by Vite's <a href="https://vite.dev/config/shared-options.html#define"><code>define</code></a>.</li>
</ul>
</li>
<li><code>vars</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A map of environment variables to set when deploying your Worker. Refer to <a href="/workers/configuration/environment-variables/">Environment variables</a>.</li>
</ul>
</li>
<li><code>durable_objects</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A list of Durable Objects that your Worker should be bound to. Refer to <a href="#durable-objects">Durable Objects</a>.</li>
</ul>
</li>
<li><code>kv_namespaces</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A list of KV namespaces that your Worker should be bound to. Refer to <a href="#kv-namespaces">KV namespaces</a>.</li>
</ul>
</li>
<li><code>r2_buckets</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A list of R2 buckets that your Worker should be bound to. Refer to <a href="#r2-buckets">R2 buckets</a>.</li>
</ul>
</li>
<li><code>ai_search_namespaces</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A list of AI Search namespaces that your Worker should be bound to. Refer to <a href="#ai-search-namespaces">AI Search namespaces</a>.</li>
</ul>
</li>
<li><code>ai_search</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A list of AI Search instance bindings bound directly to pre-existing instances in the default namespace. Refer to <a href="#ai-search-instances">AI Search instances</a>.</li>
</ul>
</li>
<li><code>vectorize</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A list of Vectorize indexes that your Worker should be bound to. Refer to <a href="#vectorize-indexes">Vectorize indexes</a>.</li>
</ul>
</li>
<li><code>services</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A list of service bindings that your Worker should be bound to. Refer to <a href="#service-bindings">service bindings</a>.</li>
</ul>
</li>
<li><code>queues</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A list of Queue producers and consumers that your Worker should be bound to. Refer to <a href="#queues">Queues</a>.</li>
</ul>
</li>
<li><code>workflows</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A list of Workflows that your Worker should be bound to. Refer to <a href="#workflows">Workflows</a>.</li>
</ul>
</li>
<li><code>tail_consumers</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A list of the Tail Workers your Worker sends data to. Refer to <a href="/workers/observability/logs/tail-workers/">Tail Workers</a>.</li>
</ul>
</li>
<li><code>secrets</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Declares the secret names your Worker requires. Used for validation during local development and deploy, and as the source of truth for type generation. Refer to <a href="#secrets">Secrets</a>.</li>
<li><code>required</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span> — A list of secret names that must be set to deploy your Worker.</li>
</ul>
</li>
<li><code>secrets_store_secrets</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A list of Secrets Store bindings that your worker should be bound to. Refer to <a href="/secrets-store/">Secrets Store</a>.</li>
</ul>
</li>
</ul>
<h2 id="types-of-routes">Types of routes</h2>
<p>There are three types of <a href="/workers/configuration/routing/">routes</a>: <a href="/workers/configuration/routing/custom-domains/">Custom Domains</a>, <a href="/workers/configuration/routing/routes/">routes</a>, and <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code></a>.</p>
<h3 id="custom-domains">Custom Domains</h3>
<p><a href="/workers/configuration/routing/custom-domains/">Custom Domains</a> allow you to connect your Worker to a domain or subdomain, without having to make changes to your DNS settings or perform any certificate management.</p>
<ul>
<li><code>pattern</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The pattern that your Worker should be run on, for example, <code>&quot;example.com&quot;</code>.</li>
</ul>
</li>
<li><code>custom_domain</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Whether the Worker should be on a Custom Domain as opposed to a route. Defaults to <code>false</code>.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15952.md")
</div>
<h3 id="routes">Routes</h3>
<p><a href="/workers/configuration/routing/routes/">Routes</a> allow users to map a URL pattern to a Worker. A route can be configured as a zone ID route, a zone name route, or a simple route.</p>
<h4 id="zone-id-route">Zone ID route</h4>
<ul>
<li><code>pattern</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The pattern that your Worker can be run on, for example,<code>&quot;example.com/*&quot;</code>.</li>
</ul>
</li>
<li><code>zone_id</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The ID of the zone that your <code>pattern</code> is associated with. Refer to <a href="/fundamentals/account/find-account-and-zone-ids/">Find zone and account IDs</a>.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15953.md")
</div>
<h4 id="zone-name-route">Zone name route</h4>
<ul>
<li><code>pattern</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The pattern that your Worker should be run on, for example, <code>&quot;example.com/*&quot;</code>.</li>
</ul>
</li>
<li><code>zone_name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of the zone that your <code>pattern</code> is associated with. If you are using API tokens, this will require the <code>Account</code> scope.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15954.md")
</div>
<h4 id="simple-route">Simple route</h4>
<p>This is a simple route that only requires a pattern.</p>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15955.md")
</div>
<h3 id="workers-dev"><code>workers.dev</code></h3>
<p>Cloudflare Workers accounts come with a <code>workers.dev</code> subdomain that is configurable in the Cloudflare dashboard.</p>
<ul>
<li><code>workers_dev</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Whether the Worker runs on a custom <code>workers.dev</code> account subdomain. Defaults to <code>true</code>.</li>
</ul>
</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15956.md")
</div>
<h2 id="triggers">Triggers</h2>
<p>Triggers allow you to define the <code>cron</code> expression to invoke your Worker's <code>scheduled</code> function. Refer to <a href="/workers/configuration/cron-triggers/#supported-cron-expressions">Supported cron expressions</a>.</p>
<ul>
<li><code>crons</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">required</span>
<ul>
<li>An array of <code>cron</code> expressions.</li>
<li>To disable a Cron Trigger, set <code>crons = []</code>. Commenting out the <code>crons</code> key will not disable a Cron Trigger.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15957.md")
</div>
<h2 id="observability">Observability</h2>
<p>The <a href="/workers/observability/logs/workers-logs">Observability</a> setting allows you to automatically ingest, store, filter, and analyze logging data emitted from Cloudflare Workers directly from your Cloudflare Worker's dashboard.</p>
<ul>
<li><code>enabled</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">required</span>
<ul>
<li>When set to <code>true</code> on a Worker, logs for the Worker are persisted. Defaults to <code>true</code> for all new Workers.</li>
</ul>
</li>
<li><code>head_sampling_rate</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A number between 0 and 1, where 0 indicates zero out of one hundred requests are logged, and 1 indicates every request is logged. If <code>head_sampling_rate</code> is unspecified, it is configured to a default value of 1 (100%). Read more about <a href="/workers/observability/logs/workers-logs/#head-based-sampling">head-based sampling</a>.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15958.md")
</div>
<h2 id="custom-builds">Custom builds</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15946.md")
</aside>
<p>You can configure a custom build step that will be run before your Worker is deployed. Refer to <a href="/workers/wrangler/custom-builds/">Custom builds</a>.</p>
<ul>
<li><code>command</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The command used to build your Worker. On Linux and macOS, the command is executed in the <code>sh</code> shell and the <code>cmd</code> shell for Windows. The <code>&amp;&amp;</code> and <code>||</code> shell operators may be used.</li>
</ul>
</li>
<li><code>cwd</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The directory in which the command is executed.</li>
</ul>
</li>
<li><code>watch_dir</code> <span class="nb-type">string | string[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The directory to watch for changes while using <code>wrangler dev</code>. Defaults to the current working directory.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15959.md")
</div>
<h2 id="limits">Limits</h2>
<p>You can impose limits on your Worker's behavior at runtime. Limits are only supported for the <a href="/workers/platform/pricing/#example-pricing-standard-usage-model">Standard Usage Model</a>.
Limits are only enforced when deployed to Cloudflare's network, not in local development. The CPU limit
can be set to a maximum of 300,000 milliseconds (5 minutes).</p>
<p>Each <a href="/workers/reference/how-workers-works/#isolates">isolate</a> has some built-in flexibility to allow for cases where your Worker infrequently runs over the configured limit. If your Worker starts hitting the limit consistently, its execution will be terminated according to the limit configured.
<br /></p>
<ul>
<li><code>cpu_ms</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The maximum CPU time allowed per invocation, in milliseconds.</li>
</ul>
</li>
<li><code>subrequests</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The maximum number of subrequests allowed per invocation. This value defaults to 50 for free accounts and 10,000 for paid accounts. The free account maximum is 50 and the paid account maximum is 10,000,000. Refer to <a href="/workers/platform/limits/#subrequests">subrequest limits</a> for more information.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15960.md")
</div>
<h2 id="bindings">Bindings</h2>
<h3 id="browser-run">Browser Run</h3>
<p>The <a href="/browser-run/">Workers Browser Run API</a> allows developers to programmatically control and interact with a headless browser instance and create automation flows for their applications and products.</p>
<p>A <a href="/workers/runtime-apis/bindings/">browser binding</a> will provide your Worker with an authenticated endpoint to interact with a dedicated Chromium browser instance.</p>
<ul>
<li><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The binding name used to refer to the browser binding. The value (string) you set will be used to reference this headless browser in your Worker. The binding must be <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variables">a valid JavaScript variable name</a>. For example, <code>binding = &quot;HEAD_LESS&quot;</code> or <code>binding = &quot;simulatedBrowser&quot;</code> would both be valid names for the binding.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15961.md")
</div>
<h3 id="d1-databases">D1 databases</h3>
<p><a href="/d1/">D1</a> is Cloudflare's serverless SQL database. A Worker can query a D1 database (or databases) by creating a <a href="/workers/runtime-apis/bindings/">binding</a> to each database for <a href="/d1/worker-api/">D1 Workers Binding API</a>.</p>
<p>To bind D1 databases to your Worker, assign an array of the below object to the <code>[[d1_databases]]</code> key.</p>
<ul>
<li>
<p><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The binding name used to refer to the D1 database. The value (string) you set will be used to reference this database in your Worker. The binding must be <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variables">a valid JavaScript variable name</a>. For example, <code>binding = &quot;MY_DB&quot;</code> or <code>binding = &quot;productionDB&quot;</code> would both be valid names for the binding.</li>
</ul>
</li>
<li>
<p><code>database_name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The name of the database. This is a human-readable name that allows you to distinguish between different databases, and is set when you first create the database.</li>
</ul>
</li>
<li>
<p><code>database_id</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The ID of the database. The database ID is available when you first use <code>wrangler d1 create</code> or when you call <code>wrangler d1 list</code>, and uniquely identifies your database.</li>
</ul>
</li>
<li>
<p><code>preview_database_id</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The preview ID of this D1 database. If provided, <code>wrangler dev</code> uses this ID. Otherwise, it uses <code>database_id</code>. This option is recommended when using <code>wrangler dev --remote</code> to avoid using your production database.</li>
</ul>
</li>
<li>
<p><code>migrations_dir</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The migration directory containing the migration files. By default, <code>wrangler d1 migrations create</code> creates a folder named <code>migrations</code>. You can use <code>migrations_dir</code> to specify a different folder containing the migration files (for example, if you have a mono-repo setup, and want to use a single D1 instance across your apps/packages).</li>
<li>For more information, refer to <a href="/workers/wrangler/commands/d1/#d1-migrations-create">D1 Wrangler <code>migrations</code> commands</a> and <a href="/d1/reference/migrations/">D1 migrations</a>.</li>
</ul>
</li>
<li>
<p><code>migrations_pattern</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A glob pattern (relative to your Wrangler config file) used to discover migration files. Defaults to <code>migrations/*.sql</code>.</li>
<li>Use this to opt in to nested layouts produced by ORMs like Drizzle (for example, <code>migrations/*/migration.sql</code>).</li>
<li>When <code>migrations_pattern</code> is set, <code>migrations_dir</code> must also be set, and <code>migrations_pattern</code> must start with whatever <code>migrations_dir</code> is set to. Each migration is recorded in the migrations table as a path relative to <code>migrations_dir</code>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15945.md")
</aside>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15962.md")
</div>
<h3 id="dispatch-namespace-bindings-workers-for-platforms">Dispatch namespace bindings (Workers for Platforms)</h3>
<p>Dispatch namespace bindings allow for communication between a <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dynamic-dispatch-worker">dynamic dispatch Worker</a> and a <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dispatch-namespace">dispatch namespace</a>. Dispatch namespace bindings are used in <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a>. Workers for Platforms helps you deploy serverless functions programmatically on behalf of your customers.</p>
<ul>
<li><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The binding name. The value (string) you set will be used to reference this database in your Worker. The binding must be <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variables">a valid JavaScript variable name</a>. For example, <code>binding = &quot;MY_NAMESPACE&quot;</code> or <code>binding = &quot;productionNamespace&quot;</code> would both be valid names for the binding.</li>
</ul>
</li>
<li><code>namespace</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of the <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dispatch-namespace">dispatch namespace</a>.</li>
</ul>
</li>
<li><code>outbound</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li><code>service</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span> The name of the <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/">outbound Worker</a> to bind to.</li>
<li><code>parameters</code> array optional A list of parameters to pass data from your <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dynamic-dispatch-worker">dynamic dispatch Worker</a> to the <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/">outbound Worker</a>.</li>
</ul>
</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15963.md")
</div>
<h3 id="durable-objects">Durable Objects</h3>
<p><a href="/durable-objects/">Durable Objects</a> provide low-latency coordination and consistent storage for the Workers platform.</p>
<p>To bind Durable Objects to your Worker, assign an array of the below object to the <code>durable_objects.bindings</code> key.</p>
<ul>
<li><code>name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of the binding used to refer to the Durable Object.</li>
</ul>
</li>
<li><code>class_name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The exported class name of the Durable Object.</li>
</ul>
</li>
<li><code>script_name</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The name of the Worker where the Durable Object is defined, if it is external to this Worker. This option can be used both in local and remote development. In local development, you must run the external Worker in a separate process (via <code>wrangler dev</code>). In remote development, the appropriate remote binding must be used.</li>
</ul>
</li>
<li><code>environment</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The environment of the <code>script_name</code> to bind to.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15964.md")
</div>
<h4 id="exports">Exports</h4>
<p>The <code>exports</code> field declares the Durable Object classes this Worker exports and their lifecycle state. Refer to <a href="/durable-objects/reference/durable-objects-migrations/">Durable Object class exports</a>.</p>
<p>Each entry in <code>exports</code> is keyed by Durable Object class name. The fields on each entry are:</p>
<ul>
<li><code>type</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>For Durable Object class entries, set this to <code>&quot;durable-object&quot;</code>.</li>
</ul>
</li>
<li><code>state</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The lifecycle state. One of <code>&quot;created&quot;</code> (the default — a live class), <code>&quot;deleted&quot;</code>, <code>&quot;renamed&quot;</code>, <code>&quot;transferred&quot;</code>, or <code>&quot;expecting-transfer&quot;</code>.</li>
</ul>
</li>
<li><code>storage</code> <span class="nb-type">string</span> <span class="nb-metainfo">conditional</span>
<ul>
<li>Required when <code>state</code> is <code>&quot;created&quot;</code> or <code>&quot;expecting-transfer&quot;</code>. One of <code>&quot;sqlite&quot;</code> (recommended; required for new namespaces) or <code>&quot;legacy-kv&quot;</code> (only for existing key-value-backed namespaces).</li>
</ul>
</li>
<li><code>renamed_to</code> <span class="nb-type">string</span> <span class="nb-metainfo">conditional</span>
<ul>
<li>Required when <code>state</code> is <code>&quot;renamed&quot;</code>. The destination class name, which must also appear as a live entry in the same <code>exports</code> map.</li>
</ul>
</li>
<li><code>transferred_to</code> <span class="nb-type">string</span> <span class="nb-metainfo">conditional</span>
<ul>
<li>Required when <code>state</code> is <code>&quot;transferred&quot;</code>. The name of the target Worker that will receive the namespace.</li>
</ul>
</li>
<li><code>transfer_from</code> <span class="nb-type">string</span> <span class="nb-metainfo">conditional</span>
<ul>
<li>Required when <code>state</code> is <code>&quot;expecting-transfer&quot;</code>. The name of the source Worker the namespace is being transferred from.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15965.md")
</div>
<h4 id="migrations">Migrations</h4>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15944.md")
</aside>
<p>When making changes to your Durable Object classes on a Worker that uses the legacy <code>migrations</code> array, you must perform a migration. Refer to <a href="/durable-objects/reference/durable-object-class-migrations-legacy/">Durable Object class migrations (legacy)</a>.</p>
<ul>
<li><code>tag</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>A unique identifier for this migration.</li>
</ul>
</li>
<li><code>new_sqlite_classes</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>New Durable Object classes being defined with the SQLite storage backend.</li>
</ul>
</li>
<li><code>new_classes</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>New Durable Object classes being defined with the legacy key-value storage backend.</li>
</ul>
</li>
<li><code>renamed_classes</code> <span class="nb-type">{from: string, to: string}[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The Durable Object classes being renamed.</li>
</ul>
</li>
<li><code>deleted_classes</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The Durable Object classes being removed.</li>
</ul>
</li>
<li><code>transferred_classes</code> <span class="nb-type">{from: string, from_script: string, to: string}[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The Durable Object classes being transferred from another Worker.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15966.md")
</div>
<h3 id="email-bindings">Email bindings</h3>
<p>You can send an email about your Worker's activity from your Worker to an email address verified on <a href="/email-service/configuration/email-routing-addresses/#destination-addresses">Email Routing</a>. This is useful for when you want to know about certain types of events being triggered, for example.</p>
<p>Before you can bind an email address to your Worker, you need to <a href="/email-service/get-started/">enable Email Routing</a> and have at least one <a href="/email-service/configuration/email-routing-addresses/#destination-addresses">verified email address</a>. Then, assign an array to the object (send_email) with the type of email binding you need.</p>
<ul>
<li><code>name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The binding name.</li>
</ul>
</li>
<li><code>destination_address</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The <a href="/email-service/configuration/send-bindings/#binding-types">chosen email address</a> you send emails to.</li>
</ul>
</li>
<li><code>allowed_destination_addresses</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The <a href="/email-service/configuration/send-bindings/#binding-types">allowlist of email addresses</a> you send emails to.</li>
</ul>
</li>
</ul>
<p>You can add one or more types of bindings to your Wrangler file. However, each attribute must be on its own line:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15967.md")
</div>
<h3 id="environment-variables">Environment variables</h3>
<p><a href="/workers/configuration/environment-variables/">Environment variables</a> are a type of binding that allow you to attach text strings or JSON values to your Worker.</p>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15968.md")
</div>
<h3 id="hyperdrive">Hyperdrive</h3>
<p><a href="/hyperdrive/">Hyperdrive</a> bindings allow you to interact with and query any Postgres database from within a Worker.</p>
<ul>
<li><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The binding name.</li>
</ul>
</li>
<li><code>id</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The ID of the Hyperdrive configuration.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15969.md")
</div>
<h3 id="images">Images</h3>
<p><a href="/images/optimization/transformations/transform-via-workers/">Cloudflare Images</a> lets you make transformation requests to optimize, resize, and manipulate images stored in remote sources.</p>
<p>To bind Images to your Worker, assign an array of the below object to the <code>images</code> key.</p>
<p><code>binding</code> (required). The name of the binding used to refer to the Images API.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15970.md")
</div>
<h3 id="kv-namespaces">KV namespaces</h3>
<p><a href="/kv/api/">Workers KV</a> is a global, low-latency, key-value data store. It stores data in a small number of centralized data centers, then caches that data in Cloudflare’s data centers after access.</p>
<p>To bind KV namespaces to your Worker, assign an array of the below object to the <code>kv_namespaces</code> key.</p>
<ul>
<li><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The binding name used to refer to the KV namespace.</li>
</ul>
</li>
<li><code>id</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The ID of the KV namespace.</li>
</ul>
</li>
<li><code>preview_id</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The preview ID of this KV namespace. This option is <strong>required</strong> when using <code>wrangler dev --remote</code> to develop against remote resources (but is not required with <a href="/workers/local-development/#remote-bindings">remote bindings</a>). If developing locally, this is an optional field. <code>wrangler dev</code> will use this ID for the KV namespace. Otherwise, <code>wrangler dev</code> will use <code>id</code>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15943.md")
</aside>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15971.md")
</div>
<h3 id="ai-search-namespaces">AI Search namespaces</h3>
<p><a href="/ai-search/">AI Search</a> is Cloudflare's managed search service. A <a href="/ai-search/concepts/namespaces/">namespace</a> is a logical grouping of AI Search instances. The binding grants full access to all instances within the namespace.</p>
<p>To bind AI Search namespaces to your Worker, assign an array of the below object to the <code>ai_search_namespaces</code> key.</p>
<ul>
<li><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The binding name used to refer to the AI Search namespace.</li>
</ul>
</li>
<li><code>namespace</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of the AI Search namespace. A <code>default</code> namespace is created automatically for every account. If the namespace does not exist, Wrangler creates it on deploy.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15972.md")
</div>
<h3 id="ai-search-instances">AI Search instances</h3>
<p>To bind directly to a pre-existing <a href="/ai-search/">AI Search</a> instance in the <a href="/ai-search/concepts/namespaces/#default-namespace">default namespace</a>, assign an array of the below object to the <code>ai_search</code> key. This binding does not support namespace-level operations like <code>list()</code>, <code>create()</code>, or <code>delete()</code>.</p>
<ul>
<li><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The binding name used to refer to the AI Search instance.</li>
</ul>
</li>
<li><code>instance_name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of the AI Search instance. Must exist in the default namespace at deploy time.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15973.md")
</div>
<h3 id="queues">Queues</h3>
<p><a href="/queues/">Queues</a> is Cloudflare's global message queueing service, providing <a href="/queues/reference/delivery-guarantees/">guaranteed delivery</a> and <a href="/queues/configuration/batching-retries/">message batching</a>. To interact with a queue with Workers, you need a producer Worker to send messages to the queue and a consumer Worker to pull batches of messages out of the Queue. A single Worker can produce to and consume from multiple Queues.</p>
<p>To bind Queues to your producer Worker, assign an array of the below object to the <code>[[queues.producers]]</code> key.</p>
<ul>
<li><code>queue</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of the queue, used on the Cloudflare dashboard.</li>
</ul>
</li>
<li><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The binding name used to refer to the queue in your Worker. The binding must be <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variables">a valid JavaScript variable name</a>. For example, <code>binding = &quot;MY_QUEUE&quot;</code> or <code>binding = &quot;productionQueue&quot;</code> would both be valid names for the binding.</li>
</ul>
</li>
<li><code>delivery_delay</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The number of seconds to <a href="/queues/configuration/batching-retries/#delay-messages">delay messages sent to a queue</a> for by default. This can be overridden on a per-message or per-batch basis.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15974.md")
</div>
<p>To bind Queues to your consumer Worker, assign an array of the below object to the <code>[[queues.consumers]]</code> key.</p>
<ul>
<li><code>queue</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of the queue, used on the Cloudflare dashboard.</li>
</ul>
</li>
<li><code>max_batch_size</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The maximum number of messages allowed in each batch.</li>
</ul>
</li>
<li><code>max_batch_timeout</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The maximum number of seconds to wait for messages to fill a batch before the batch is sent to the consumer Worker.</li>
</ul>
</li>
<li><code>max_retries</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The maximum number of retries for a message, if it fails or <a href="/queues/configuration/javascript-apis/#messagebatch"><code>retryAll()</code></a> is invoked.</li>
</ul>
</li>
<li><code>dead_letter_queue</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The name of another queue to send a message if it fails processing at least <code>max_retries</code> times.</li>
<li>If a <code>dead_letter_queue</code> is not defined, messages that repeatedly fail processing will be discarded.</li>
<li>If there is no queue with the specified name, it will be created automatically.</li>
</ul>
</li>
<li><code>max_concurrency</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The maximum number of concurrent consumers allowed to run at once. Leaving this unset will mean that the number of invocations will scale to the <a href="/queues/platform/limits/">currently supported maximum</a>.</li>
<li>Refer to <a href="/queues/configuration/consumer-concurrency/">Consumer concurrency</a> for more information on how consumers autoscale, particularly when messages are retried.</li>
</ul>
</li>
<li><code>retry_delay</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The number of seconds to <a href="/queues/configuration/batching-retries/#delay-messages">delay retried messages</a> for by default, before they are re-delivered to the consumer. This can be overridden on a per-message or per-batch basis <a href="/queues/configuration/batching-retries/#explicit-acknowledgement-and-retries">when retrying messages</a>.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15975.md")
</div>
<h3 id="r2-buckets">R2 buckets</h3>
<p><a href="/r2">Cloudflare R2 Storage</a> allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud storage services.</p>
<p>To bind R2 buckets to your Worker, assign an array of the below object to the <code>r2_buckets</code> key.</p>
<ul>
<li><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The binding name used to refer to the R2 bucket.</li>
</ul>
</li>
<li><code>bucket_name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of this R2 bucket.</li>
</ul>
</li>
<li><code>jurisdiction</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The jurisdiction where this R2 bucket is located, if a jurisdiction has been specified. Refer to <a href="/r2/reference/data-location/#jurisdictional-restrictions">Jurisdictional Restrictions</a>.</li>
</ul>
</li>
<li><code>preview_bucket_name</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The preview name of this R2 bucket. If provided, <code>wrangler dev</code> will use this name for the R2 bucket. Otherwise, it will use <code>bucket_name</code>. This option is required when using <code>wrangler dev --remote</code> (but is not required with <a href="/workers/local-development/#remote-bindings">remote bindings</a>).</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15942.md")
</aside>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15976.md")
</div>
<h3 id="vectorize-indexes">Vectorize indexes</h3>
<p>A <a href="/vectorize/">Vectorize index</a> allows you to insert and query vector embeddings for semantic search, classification and other vector search use-cases.</p>
<p>To bind Vectorize indexes to your Worker, assign an array of the below object to the <code>vectorize</code> key.</p>
<ul>
<li><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The binding name used to refer to the bound index from your Worker code.</li>
</ul>
</li>
<li><code>index_name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of the index to bind.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15977.md")
</div>
<h3 id="service-bindings">Service bindings</h3>
<p>A service binding allows you to send HTTP requests to another Worker without those requests going over the Internet. The request immediately invokes the downstream Worker, reducing latency as compared to a request to a third-party service. Refer to <a href="/workers/runtime-apis/bindings/service-bindings/">About Service Bindings</a>.</p>
<p>To bind other Workers to your Worker, assign an array of the below object to the <code>services</code> key.</p>
<ul>
<li><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The binding name used to refer to the bound Worker.</li>
</ul>
</li>
<li><code>service</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of the Worker.</li>
<li>To bind to a Worker in a specific <a href="/workers/wrangler/environments">environment</a>, you need to append the environment name to the Worker name. This should be in the format <code>&lt;worker-name&gt;-&lt;environment-name&gt;</code>. For example, to bind to a Worker called <code>worker-name</code> in its <code>staging</code> environment, <code>service</code> should be set to <code>worker-name-staging</code>.</li>
</ul>
</li>
<li><code>entrypoint</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The name of the <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#named-entrypoints">entrypoint</a> to bind to. If you do not specify an entrypoint, the default export of the Worker will be used.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15978.md")
</div>
<h3 id="static-assets">Static assets</h3>
<p>Refer to <a href="#assets">Assets</a>.</p>
<h3 id="analytics-engine-datasets">Analytics Engine Datasets</h3>
<p><a href="/analytics/analytics-engine/">Workers Analytics Engine</a> provides analytics, observability and data logging from Workers. Write data points to your Worker binding then query the data using the <a href="/analytics/analytics-engine/sql-api/">SQL API</a>.</p>
<p>To bind Analytics Engine datasets to your Worker, assign an array of the below object to the <code>analytics_engine_datasets</code> key.</p>
<ul>
<li><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The binding name used to refer to the dataset.</li>
</ul>
</li>
<li><code>dataset</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The dataset name to write to. This will default to the same name as the binding if it is not supplied.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15979.md")
</div>
<h3 id="mtls-certificates">mTLS Certificates</h3>
<p>To communicate with origins that require client authentication, a Worker can present a certificate for mTLS in subrequests. Wrangler provides the <code>mtls-certificate</code> <a href="/workers/wrangler/commands#mtls-certificate">command</a> to upload and manage these certificates.</p>
<p>To create a <a href="/workers/runtime-apis/bindings/">binding</a> to an mTLS certificate for your Worker, assign an array of objects with the following shape to the <code>mtls_certificates</code> key.</p>
<ul>
<li><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The binding name used to refer to the certificate.</li>
</ul>
</li>
<li><code>certificate_id</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The ID of the certificate. Wrangler displays this via the <code>mtls-certificate upload</code> and <code>mtls-certificate list</code> commands.</li>
</ul>
</li>
</ul>
<p>Example of a Wrangler configuration file that includes an mTLS certificate binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15980.md")
</div>
<p>mTLS certificate bindings can then be used at runtime to communicate with secured origins via their <a href="/workers/runtime-apis/bindings/mtls"><code>fetch</code> method</a>.</p>
<h3 id="workers-ai">Workers AI</h3>
<p><a href="/workers-ai/">Workers AI</a> allows you to run machine learning models, on the Cloudflare network, from your own code –
whether that be from Workers, Pages, or anywhere via REST API.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-ai-local-development-usage-charges">Workers AI local development usage charges</h3>
@markup("md", "content/.markup/bodies/15941.md")
</aside>
<p>Unlike other bindings, this binding is limited to one AI binding per Worker project.</p>
<ul>
<li><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The binding name.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15981.md")
</div>
<h3 id="workflows">Workflows</h3>
<p><a href="/workflows/">Workflows</a> allow you to build durable, multi-step applications using the Workers platform. A Workflow binding enables your Worker to create and manage Workflow instances programmatically.</p>
<p>To bind Workflows to your Worker, assign an array of the below object to the <code>workflows</code> key.</p>
<ul>
<li><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The binding name used to refer to the Workflow in your Worker. The binding must be <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variables">a valid JavaScript variable name</a>. For example, <code>binding = &quot;MY_WORKFLOW&quot;</code> would be a valid name for the binding.</li>
</ul>
</li>
<li><code>name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of the Workflow.</li>
</ul>
</li>
<li><code>class_name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of the exported Workflow class. The <code>class_name</code> must match the name of the Workflow class exported from your Worker code.</li>
</ul>
</li>
<li><code>script_name</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The name of the Worker script where the Workflow class is defined. Only required if the Workflow is defined in a different Worker than the one the binding is configured on.</li>
</ul>
</li>
<li><code>schedules</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A list of cron schedules that create new instances of this Workflow automatically.</li>
<li>Use this when you want to run a Workflow on a recurring interval without defining top-level <code>triggers.crons</code> and a separate <code>scheduled</code> handler.</li>
<li>Use a Wrangler release that supports Workflow schedules. If your local schema does not recognize <code>schedules</code>, update Wrangler first.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15982.md")
</div>
<h2 id="assets">Assets</h2>
<p><a href="/workers/static-assets/">Static assets</a> allows developers to run front-end websites on Workers. You can configure the directory of assets, an optional runtime binding, and routing configuration options.</p>
<p>You can only configure one collection of assets per Worker.</p>
<p>The following options are available under the <code>assets</code> key.</p>
<ul>
<li><code>directory</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Folder of static assets to be served.</li>
<li>Not required if you're using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>, which will automatically point to the client build output.</li>
</ul>
</li>
<li><code>binding</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The binding name used to refer to the assets. Optional, and only useful when a Worker script is set with <code>main</code>.</li>
</ul>
</li>
<li><code>run_worker_first</code> <span class="nb-type">boolean | string[]</span> <span class="nb-metainfo">optional, defaults to false</span>
<ul>
<li>Controls whether static assets are fetched directly, or a Worker script is invoked. Can be a boolean (<code>true</code>/<code>false</code>) or an array of route pattern strings with support for glob patterns (<code>*</code>) and exception patterns (<code>!</code> prefix). Patterns must begin with <code>/</code> or <code>!/</code>. Supports at most 100 entries (duplicates count toward the limit). Learn more about fetching assets when using <a href="/workers/static-assets/routing/worker-script/#run-your-worker-script-first"><code>run_worker_first</code></a>.</li>
</ul>
</li>
<li><code>html_handling</code>: <span class="nb-type">&quot;auto-trailing-slash&quot; | &quot;force-trailing-slash&quot; | &quot;drop-trailing-slash&quot; | &quot;none&quot;</span> <span class="nb-metainfo">optional, defaults to &quot;auto-trailing-slash&quot;</span>
<ul>
<li>Determines the redirects and rewrites of requests for HTML content. Learn more about the various options in <a href="/workers/static-assets/routing/advanced/html-handling/">assets routing</a>.</li>
</ul>
</li>
<li><code>not_found_handling</code>: <span class="nb-type">&quot;single-page-application&quot; | &quot;404-page&quot; | &quot;none&quot;</span> <span class="nb-metainfo">optional, defaults to &quot;none&quot;</span>
<ul>
<li>Determines the handling of requests that do not map to an asset. Learn more about the various options for <a href="/workers/static-assets/#routing-behavior">routing behavior</a>.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15983.md")
</div>
<p>You can also configure <code>run_worker_first</code> with an array of route patterns:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15984.md")
</div>
<h2 id="containers">Containers</h2>
<p>You can define <a href="/containers">Containers</a> to run alongside your Worker using the <code>containers</code> field.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15940.md")
</aside>
<p>The following options are available:</p>
<ul>
<li><code>image</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The image to use for the container. This can either be a local path to a <code>Dockerfile</code>, in which case <code>wrangler deploy</code> will
build and push the image, or it can be an image reference. Supported registries are the Cloudflare Registry, Docker Hub, Amazon ECR, and Google Artifact Registry. For more information, refer to <a href="/containers/guides/image-management/">Image Management</a>.</li>
</ul>
</li>
<li><code>class_name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The corresponding Durable Object class name. This will make this Durable Object a container-enabled Durable Object
and allow each instance to control a container. See <a href="/durable-objects/api/container/">Durable Object Container Methods</a> for details.</li>
</ul>
</li>
<li><code>instance_type</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The instance type of the container. This determines the amount of memory, CPU, and disk given to the container
instance. The current options are <code>&quot;lite&quot;</code>, <code>&quot;basic&quot;</code>, <code>&quot;standard-1&quot;</code>, <code>&quot;standard-2&quot;</code>, <code>&quot;standard-3&quot;</code>, and <code>&quot;standard-4&quot;</code>. The default is <code>&quot;lite&quot;</code>. For more information,
see the <a href="/containers/platform/limits/#instance-types">instance types documentation</a>.</li>
<li>To specify a custom instance type, see <a href="#custom-instance-types">here</a>.</li>
</ul>
</li>
<li><code>max_instances</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The maximum number of concurrent container instances you want to run at any given moment. Stopped containers do not count towards this - you may have more container instances than this number overall, but only this many actively running containers at once. If a request to start a container will exceed this limit, that request will error.</li>
<li>Defaults to 20.</li>
<li>This value is only enforced when running in production on Cloudflare's network. This limit does not apply during local development, so you may run more instances than specified.</li>
</ul>
</li>
<li><code>name</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The name of your container. Used as an identifier. This will default to a combination of your Worker name, the class
name, and your environment.</li>
</ul>
</li>
<li><code>image_build_context</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The build context of the application, by default it is the directory of <code>image</code>.</li>
</ul>
</li>
<li><code>image_vars</code> <span class="nb-type">Record&lt;string, string&gt;</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Build-time variables, equivalent to using <code>--build-arg</code> with <code>docker build</code>. If you want to provide environment variables to your container at <em>runtime</em>, you should <a href="/containers/examples/env-vars-and-secrets/">use secret bindings or <code>envVars</code> on the Container class</a>.</li>
</ul>
</li>
<li><code>rollout_active_grace_period</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>During a <a href="/containers/configuration/rollouts/">rollout</a>, minimum seconds a container instance must already have been connected to its Durable Object before it may be replaced. Defaults to <code>0</code>. Still applies with <code>--containers-rollout=immediate</code>.</li>
</ul>
</li>
<li><code>rollout_step_percentage</code> <span class="nb-type">number | number[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Percentage of container instances to update at each <a href="/containers/configuration/rollouts/">rollout</a> step. A single number uses that step size (<code>5</code>, <code>10</code>, <code>20</code>, <code>25</code>, <code>50</code>, or <code>100</code>). An array must contain ascending integer values from <code>10</code> through <code>100</code>, end in <code>100</code>, contain at most 10 entries, and contain no more entries than <code>max_instances</code>; its values are cumulative. Defaults to <code>100</code> if <code>max_instances</code> is omitted or less than <code>2</code>; otherwise defaults to <code>[10, 100]</code>. Override for one deploy with <code>--containers-rollout=immediate</code> (single 100% step; does not override grace period).</li>
</ul>
</li>
<li><code>ssh</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Configuration for SSH through Wrangler. Refer to <a href="#ssh">SSH</a>.</li>
</ul>
</li>
<li><code>wrangler_ssh</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional deprecated, use <code>ssh</code></span>
<ul>
<li>Deprecated alias for <code>ssh</code>. Still supported for backward compatibility.</li>
</ul>
</li>
<li><code>authorized_keys</code> <span class="nb-type">object[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Public keys that should be added to the Container's <code>authorized_keys</code> file.</li>
</ul>
</li>
<li><code>constraints</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Placement constraints for the container. Refer to <a href="/containers/concepts/placement/">Containers placement</a> for details.</li>
</ul>
</li>
<li><code>constraints.regions</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Limit container placement to specific geographic regions. Valid values: <code>&quot;ENAM&quot;</code>, <code>&quot;WNAM&quot;</code>, <code>&quot;EEUR&quot;</code>, <code>&quot;WEUR&quot;</code>, <code>&quot;APAC&quot;</code>, <code>&quot;SAM&quot;</code>, <code>&quot;ME&quot;</code>, <code>&quot;OC&quot;</code>, <code>&quot;AFR&quot;</code>.</li>
</ul>
</li>
<li><code>constraints.jurisdiction</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Restrict containers to compliance boundaries. Valid values: <code>&quot;eu&quot;</code>, <code>&quot;fedramp&quot;</code>.</li>
</ul>
</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15985.md")
</div>
<h3 id="custom-instance-types">Custom Instance Types</h3>
<p>In place of the <a href="/containers/platform/limits/#instance-types">named instance types</a>, you can set a custom instance type by individually configuring vCPU, memory, and disk.
See the <a href="/containers/platform/limits/#custom-instance-types">limits documentation</a> for constraints on custom instance types.</p>
<p>The following options are available:</p>
<ul>
<li><code>vcpu</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The vCPU to be used by your container. Defaults to <code>0.0625</code> (1/16 vCPU).</li>
</ul>
</li>
<li><code>memory_mib</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The memory to be used by your container, in MiB. Defaults to <code>256</code>.</li>
</ul>
</li>
<li><code>disk_mb</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The disk to be used by your container, in MB. Defaults to <code>2000</code> (2GB).</li>
</ul>
</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15986.md")
</div>
<p><span id="wrangler-ssh"></span></p>
<h3 id="ssh">SSH</h3>
<p>Configuration for SSH access to a Container instance through Wrangler. For a guide on connecting to Containers via SSH, refer to <a href="/containers/guides/ssh/">SSH</a>.</p>
<p>The following options are available:</p>
<ul>
<li><code>enabled</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Whether SSH through Wrangler is enabled. Defaults to <code>true</code>. Set to <code>false</code> to disable SSH access.</li>
</ul>
</li>
<li><code>port</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The port for the SSH service to run on. Defaults to <code>22</code>.</li>
</ul>
</li>
</ul>
<h3 id="authorized-keys">Authorized keys</h3>
<p>An authorized key is a public key that can be used to SSH into a Container.</p>
<p>The following are properties of a key:</p>
<ul>
<li><code>name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The display name of the key.</li>
</ul>
</li>
<li><code>public_key</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The public key itself.</li>
<li>Currently only the <code>ssh-ed25519</code> key type is supported.</li>
</ul>
</li>
</ul>
<h2 id="bundling">Bundling</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15939.md")
</aside>
<p>Wrangler can operate in two modes: the default bundling mode and <code>--no-bundle</code> mode.
In bundling mode, Wrangler will traverse all the imports of your code and generate a single JavaScript &quot;entry-point&quot; file.
Imported source code is &quot;inlined/bundled&quot; into this entry-point file.</p>
<p>It is also possible to include additional modules into your Worker, which are uploaded alongside the entry-point.
You specify which additional modules should be included into your Worker using the <code>rules</code> key, making these modules available to be imported when your Worker is invoked.
The <code>rules</code> key will be an array of the below object.</p>
<ul>
<li><code>type</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The type of module. Must be one of: <code>ESModule</code>, <code>CommonJS</code>, <code>CompiledWasm</code>, <code>Text</code> or <code>Data</code>.</li>
</ul>
</li>
<li><code>globs</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">required</span>
<ul>
<li>An array of glob rules (for example, <code>[&quot;**/*.md&quot;]</code>). Refer to <a href="https://man7.org/linux/man-pages/man7/glob.7.html">glob</a>.</li>
</ul>
</li>
<li><code>fallthrough</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>When set to <code>true</code> on a rule, this allows you to have multiple rules for the same <code>Type</code>.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15987.md")
</div>
<h3 id="importing-modules-within-a-worker">Importing modules within a Worker</h3>
<p>You can import and refer to these modules within your Worker, like so:</p>
<pre><code class="language-js">import markdown from &quot;./example.md&quot;;&#10;&#10;export default {&#10;	async fetch() {&#10;		return new Response(markdown);&#10;	},&#10;};&#10;</code></pre>
<h3 id="find-additional-modules">Find additional modules</h3>
<p>Normally Wrangler will only include additional modules that are statically imported in your source code as in the example above.
By setting <code>find_additional_modules</code> to <code>true</code> in your configuration file, Wrangler will traverse the file tree below <code>base_dir</code>.
Any files that match <code>rules</code> will also be included as unbundled, external modules in the deployed Worker.
<code>base_dir</code> defaults to the directory containing your <code>main</code> entrypoint.</p>
<p>See <a href="https://developers.cloudflare.com/workers/wrangler/bundling/">https://developers.cloudflare.com/workers/wrangler/bundling/</a> for more details and examples.</p>
<h3 id="python-workers">Python Workers</h3>
<p>By default, Python Workers bundle the files and folders in <code>python_modules</code> at the root of your Worker (alongside your wrangler config file).
The files in this directory represent your vendored packages and is where the pywrangler tool copies packages into. In some cases, you
may find that the files in this folder are too large and if your worker doesn't require them then they just grow your bundle size for
no reason.</p>
<p>To fix this, you can exclude certain files from being included. To do this use the <code>python_modules.exclude</code> option, for example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15988.md")
</div>
<p>This will exclude any .pyc files and <code>__pycache__</code> directories inside any subdirectory in <code>python_modules</code>.</p>
<p>By default, <code>python_modules.exclude</code> is set to <code>[&quot;**/*.pyc&quot;]</code>, so be sure to include this when setting it to a different value.</p>
<h2 id="local-development-settings">Local development settings</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15938.md")
</aside>
<p>You can configure various aspects of local development, such as the local protocol or port.</p>
<ul>
<li><code>ip</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></li>
</ul>
<ul>
<li>IP address for the local dev server to listen on. Defaults to <code>localhost</code>.</li>
</ul>
<ul>
<li><code>port</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></li>
</ul>
<ul>
<li>Port for the local dev server to listen on. Defaults to <code>8787</code>.</li>
</ul>
<ul>
<li><code>local_protocol</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Protocol that local dev server listens to requests on. Defaults to <code>http</code>.</li>
</ul>
</li>
<li><code>upstream_protocol</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Protocol that the local dev server forwards requests on. Defaults to <code>https</code>.</li>
</ul>
</li>
<li><code>host</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Host to forward requests to, defaults to the host of the first <code>route</code> of the Worker.</li>
</ul>
</li>
<li><code>enable_containers</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Determines whether to enable containers during a local dev session, if they have been configured. Defaults to <code>true</code>. If set to <code>false</code>, you can develop the rest of your application without requiring Docker or other container tool, as long as you do not invoke any code that interacts with containers.</li>
</ul>
</li>
<li><code>container_engine</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Used for local development of <a href="/containers/guides/local-dev">Containers</a>. Wrangler will attempt to automatically find the correct socket to use to communicate with your container engine. If that does not work (usually surfacing as an <code>internal error</code> when attempting to connect to your Container), you can try setting the socket path using this option. You can also set this via the environment variable <code>DOCKER_HOST</code>.</li>
</ul>
</li>
<li><code>generate_types</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Generate types from your Worker configuration. Defaults to <code>false</code>.</li>
</ul>
</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15989.md")
</div>
<h2 id="secrets">Secrets</h2>
<p><a href="/workers/configuration/secrets/">Secrets</a> are a type of binding that allow you to <a href="/workers/wrangler/commands/general/#secret">attach encrypted text values</a> to your Worker.</p>
<h3 id="secrets-configuration-property"><code>secrets</code> configuration property</h3>
<p>The <code>secrets</code> configuration property lets you declare the secret names your Worker requires in your Wrangler configuration file. Required secrets are validated during local development and deploy, and used as the source of truth for type generation.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15990.md")
</div>
<p><strong>Type generation</strong></p>
<p>When <code>secrets</code> is defined at any config level, <code>wrangler types</code> generates typed bindings from the names listed in <code>secrets.required</code> and no longer infers secret names from <code>.dev.vars</code> or <code>.env</code> files. This lets you run type generation in environments where those files are not present.</p>
<p>Per-environment secrets are supported. Each named environment produces its own interface, and the aggregated <code>Env</code> type marks secrets that only appear in some environments as optional.</p>
<p><strong>Deploy</strong></p>
<p>When <code>secrets</code> is defined, <code>wrangler deploy</code> and <code>wrangler versions upload</code> validate that all secrets in <code>secrets.required</code> are configured on the Worker before the operation succeeds. If any required secrets are missing, the command fails with an error listing which secrets need to be set.</p>
<h3 id="local-development">Local development</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15937.md")
</aside>
<p>Put secrets for use in local development in either a <code>.dev.vars</code> file or a <code>.env</code> file, in the same directory as the Wrangler configuration file.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15936.md")
</aside>
<aside class="nb-aside info">
@markup("md", "content/.markup/bodies/15935.md")
</aside>
<p>These files should be formatted using the <a href="https://hexdocs.pm/dotenvy/dotenv-file-format.html">dotenv</a> syntax. For example:</p>
<pre><code class="language-bash">SECRET_KEY=&quot;value&quot;&#10;API_TOKEN=&quot;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9&quot;&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="do-not-commit-secrets-to-git">Do not commit secrets to git</h3>
@markup("md", "content/.markup/bodies/15934.md")
</aside>
<p>To set different secrets for each Cloudflare environment, create files named <code>.dev.vars.&lt;environment-name&gt;</code> or <code>.env.&lt;environment-name&gt;</code>.</p>
<p>When you select a Cloudflare environment in your local development, the corresponding environment-specific file will be loaded ahead of the generic <code>.dev.vars</code> (or <code>.env</code>) file.</p>
<ul>
<li>When using <code>.dev.vars.&lt;environment-name&gt;</code> files, all secrets must be defined per environment. If <code>.dev.vars.&lt;environment-name&gt;</code> exists then only this will be loaded; the <code>.dev.vars</code> file will not be loaded.</li>
<li>In contrast, all matching <code>.env</code> files are loaded and the values are merged. For each variable, the value from the most specific file is used, with the following precedence:
<ul>
<li><code>.env.&lt;environment-name&gt;.local</code> (most specific)</li>
<li><code>.env.local</code></li>
<li><code>.env.&lt;environment-name&gt;</code></li>
<li><code>.env</code> (least specific)</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="controlling-env-handling">Controlling `.env` handling</h3>
@markup("md", "content/.markup/bodies/15933.md")
</aside>
<h2 id="module-aliasing">Module Aliasing</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15932.md")
</aside>
<p>You can configure Wrangler to replace all calls to import a particular package with a module of your choice, by configuring the <code>alias</code> field:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15991.md")
</div>
<pre><code class="language-js">export const bar = &quot;baz&quot;;&#10;</code></pre>
<p>With the configuration above, any calls to <code>import</code> or <code>require()</code> the module <code>foo</code> will be aliased to point to your replacement module:</p>
<pre><code class="language-js">import { bar } from &quot;foo&quot;;&#10;&#10;console.log(bar); // returns &quot;baz&quot;&#10;</code></pre>
<h3 id="bundling-issues">Bundling issues</h3>
<p>When Wrangler bundles your Worker, it might fail to resolve dependencies. Setting up an alias for such dependencies is a simple way to fix the issue.</p>
<p>However, before doing so, verify that the package is correctly installed in your project, either as a direct dependency in <code>package.json</code> or as a transitive dependency.</p>
<p>If an alias is the correct solution for your dependency issue, you have several options:</p>
<ul>
<li><strong>Alternative implementation</strong> — Implement the module's logic in a Worker-compatible manner, ensuring that all the functionality remains intact.</li>
<li><strong>No-op module</strong> — If the module's logic is unused or irrelevant, point the alias to an empty file. This makes the module a no-op while fixing the bundling issue.</li>
<li><strong>Runtime error</strong> — If the module's logic is unused and the Worker should not attempt to use it (for example, because of security vulnerabilities), point the alias to a file with a single top-level <code>throw</code> statement. This fixes the bundling issue while ensuring the module is never actually used.</li>
</ul>
<h3 id="example-aliasing-dependencies-from-npm">Example: Aliasing dependencies from NPM</h3>
<p>You can use module aliasing to provide an implementation of an NPM package that does not work on Workers — even if you only rely on that NPM package indirectly, as a dependency of one of your Worker's dependencies.</p>
<p>For example, some NPM packages depend on <a href="https://www.npmjs.com/package/node-fetch"><code>node-fetch</code></a>, a package that provided a polyfill of the <a href="/workers/runtime-apis/fetch/"><code>fetch()</code> API</a>, before it was built into Node.js.</p>
<p><code>node-fetch</code> isn't needed in Workers, because the <code>fetch()</code> API is provided by the Workers runtime. And <code>node-fetch</code> doesn't work on Workers, because it relies on currently unsupported Node.js APIs from the <code>http</code>/<code>https</code> modules.</p>
<p>You can alias all imports of <code>node-fetch</code> to instead point directly to the <code>fetch()</code> API that is built into the Workers runtime:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15992.md")
</div>
<pre><code class="language-js">export default fetch;&#10;</code></pre>
<h3 id="example-aliasing-node-js-apis">Example: Aliasing Node.js APIs</h3>
<p>You can use module aliasing to provide your own polyfill implementation of a Node.js API that is not yet available in the Workers runtime.</p>
<p>For example, let's say the NPM package you rely on calls <a href="https://nodejs.org/api/fs.html#fsreadfilepath-options-callback"><code>fs.readFile</code></a>. You can alias the fs module by adding the following to your Worker's Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15993.md")
</div>
<pre><code class="language-js">export function readFile() {&#10;	// ...&#10;}&#10;</code></pre>
<p>In many cases, this allows you to work provide just enough of an API to make a dependency work. You can learn more about Cloudflare Workers' support for Node.js APIs on the <a href="/workers/runtime-apis/nodejs/">Cloudflare Workers Node.js API documentation page</a>.</p>
<h2 id="source-maps">Source maps</h2>
<p><a href="/workers/observability/source-maps/">Source maps</a> translate compiled and minified code back to the original code that you wrote. Source maps are combined with the stack trace returned by the JavaScript runtime to present you with a stack trace.</p>
<ul>
<li><code>upload_source_maps</code> <span class="nb-type">boolean</span>
<ul>
<li>When <code>upload_source_maps</code> is set to <code>true</code>, Wrangler will automatically generate and upload source map files when you run <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> or <a href="/workers/wrangler/commands/general/#versions-deploy"><code>wrangler versions deploy</code></a>.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15994.md")
</div>
<h2 id="workers-sites">Workers Sites</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="use-workers-static-assets-instead">Use Workers Static Assets Instead</h3>
@markup("md", "content/.markup/bodies/15931.md")
</aside>
<p><a href="/workers/configuration/sites/">Workers Sites</a> allows you to host static websites, or dynamic websites using frameworks like Vue or React, on Workers.</p>
<ul>
<li><code>bucket</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The directory containing your static assets. It must be a path relative to your Wrangler configuration file.</li>
</ul>
</li>
<li><code>include</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>An exclusive list of <code>.gitignore</code>-style patterns that match file or directory names from your bucket location. Only matched items will be uploaded.</li>
</ul>
</li>
<li><code>exclude</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A list of <code>.gitignore</code>-style patterns that match files or directories in your bucket that should be excluded from uploads.</li>
</ul>
</li>
</ul>
<p>Example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15995.md")
</div>
<h2 id="proxy-support">Proxy support</h2>
<p>Corporate networks will often have proxies on their networks and this can sometimes cause connectivity issues. To configure Wrangler with the appropriate proxy details, <a href="/workers/configuration/environment-variables/">add the following environmental variables</a>:</p>
<ul>
<li><code>https_proxy</code></li>
<li><code>HTTPS_PROXY</code></li>
<li><code>http_proxy</code></li>
<li><code>HTTP_PROXY</code></li>
</ul>
<p>To configure this on macOS, add <code>HTTP_PROXY=http://&lt;YOUR_PROXY_HOST&gt;:&lt;YOUR_PROXY_PORT&gt;</code> before your Wrangler commands.</p>
<p>Example:</p>
<pre><code class="language-sh">$ HTTP_PROXY=http://localhost:8080 wrangler dev&#10;</code></pre>
<p>If your IT team has configured your computer's proxy settings, be aware that the first non-empty environment variable in this list will be used when Wrangler makes outgoing requests.</p>
<p>For example, if both <code>https_proxy</code> and <code>http_proxy</code> are set, Wrangler will only use <code>https_proxy</code> for outgoing requests.</p>
<h2 id="source-of-truth">Source of truth</h2>
<p>We recommend treating your Wrangler configuration file as the source of truth for your Worker configuration, and to avoid making changes to your Worker via the Cloudflare dashboard if you are using Wrangler.</p>
<p>If you need to make changes to your Worker from the Cloudflare dashboard, the dashboard will generate a TOML snippet for you to copy into your Wrangler configuration file, which will help ensure your Wrangler configuration file is always up to date.</p>
<p>If you change your environment variables in the Cloudflare dashboard, Wrangler will override them the next time you deploy. If you want to disable this behavior, add <code>keep_vars = true</code> to your Wrangler configuration file.</p>
<p>If you change your routes in the dashboard, Wrangler will override them in the next deploy with the routes you have set in your Wrangler configuration file. To manage routes via the Cloudflare dashboard only, remove any route and routes keys from your Wrangler configuration file. Then add <code>workers_dev = false</code> to your Wrangler configuration file. For more information, refer to <a href="/workers/wrangler/deprecations/#other-deprecated-behavior">Deprecations</a>.</p>
<p>Wrangler will not delete your secrets (encrypted environment variables) unless you run <code>wrangler secret delete &lt;key&gt;</code>.</p>
<h2 id="generated-wrangler-configuration">Generated Wrangler configuration</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15930.md")
</aside>
<p>Some framework tools, or custom pre-build processes, generate a modified Wrangler configuration to be used to deploy the Worker code.
In this case, the tool may also create a special <code>.wrangler/deploy/config.json</code> file that redirects Wrangler to use the generated configuration rather than the original, user's configuration.</p>
<p>Wrangler uses this generated configuration only for the following deploy and dev related commands:</p>
<ul>
<li><code>wrangler deploy</code></li>
<li><code>wrangler dev</code></li>
<li><code>wrangler versions upload</code></li>
<li><code>wrangler versions deploy</code></li>
<li><code>wrangler pages deploy</code></li>
<li><code>wrangler pages functions build</code></li>
</ul>
<p>When running these commands, Wrangler looks up the directory tree from the current working directory for a file at the path <code>.wrangler/deploy/config.json</code>.
This file must contain only a single JSON object of the form:</p>
<pre><code class="language-json">{ &quot;configPath&quot;: &quot;../../path/to/wrangler.jsonc&quot; }&#10;</code></pre>
<p>When this <code>config.json</code> file exists, Wrangler will follow the <code>configPath</code> (relative to the <code>.wrangler/deploy/config.json</code> file) to find the generated Wrangler configuration file to load and use in the current command.
Wrangler will display messaging to the user to indicate that the configuration has been redirected to a different file than the user's configuration file.</p>
<p>The generated configuration file should not include any <a href="#environments">environments</a>.
This is because such a file, when required, should be created as part of a build step, which should already target a specific environment. These build tools should generate distinct deployment configuration files for different environments.</p>
<h3 id="custom-build-tool-example">Custom build tool example</h3>
<p>A common example of using a redirected configuration is where a custom build tool, or framework, wants to modify the user's configuration to be used when deploying, by generating a new configuration in a <code>dist</code> directory.</p>
<ul>
<li>First, the user writes code that uses Cloudflare Workers resources, configured via a user's Wrangler configuration file like the following:</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15996.md")
</div>
<p>This configuration points <code>main</code> at the user's code entry-point and defines the <code>MY_VARIABLE</code> variable in two different environments.</p>
<ul>
<li>Then, the user runs a custom build for a given environment (for example <code>staging</code>). This will read the user's Wrangler configuration file to find the source code entry-point and environment specific settings:</li>
</ul>
<pre><code class="language-bash">&gt; my-tool build --env=staging&#10;</code></pre>
<ul>
<li>
<p><code>my-tool</code> generates a <code>dist</code> directory that contains both compiled code and a new generated deployment configuration file, containing only the settings for the given environment.
It also creates a <code>.wrangler/deploy/config.json</code> file that redirects Wrangler to the new, generated deployment configuration file:</p>
<pre class="nb-file-tree">&#10;&#10;&#10;</li>&#10;</ul>&#10;@markup("md", "content/.markup/bodies/15997.md")&#10;</pre>
<p>The generated <code>dist/wrangler.jsonc</code> might contain:</p>
<pre><code class="language-json">{&#10;	&quot;name&quot;: &quot;my-worker&quot;,&#10;	&quot;main&quot;: &quot;./index.js&quot;,&#10;	&quot;vars&quot;: {&#10;		&quot;MY_VARIABLE&quot;: &quot;staging variable&quot;&#10;	}&#10;}&#10;</code></pre>
<p>Now, the <code>main</code> property points to the generated code entry-point, no environment is defined,
and the <code>MY_VARIABLE</code> variable is resolved to the staging environment value.</p>
<p>And the <code>.wrangler/deploy/config.json</code> contains the path to the generated configuration file:</p>
<pre><code class="language-json">{&#10;	&quot;configPath&quot;: &quot;../../dist/wrangler.jsonc&quot;&#10;}&#10;</code></pre>
