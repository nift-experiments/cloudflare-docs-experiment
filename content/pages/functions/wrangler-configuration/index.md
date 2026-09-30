---
cp9:
  canonical: https://developers.cloudflare.com/pages/functions/wrangler-configuration/
  description: Configure Pages Functions settings using a Wrangler configuration file or the Cloudflare dashboard.
  full_title: Configuration · Cloudflare Pages docs
  head_html: <title>Configuration · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Pages Functions settings using a Wrangler configuration file or the Cloudflare dashboard."><link rel="canonical" href="https://developers.cloudflare.com/pages/functions/wrangler-configuration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/functions/wrangler-configuration/index.md"><meta property="og:title" content="Configuration · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Pages Functions settings using a Wrangler configuration file or the Cloudflare dashboard."><meta property="og:url" content="https://developers.cloudflare.com/pages/functions/wrangler-configuration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/functions/wrangler-configuration/#page","headline":"Configuration \u00b7 Cloudflare Pages docs","description":"Configure Pages Functions settings using a Wrangler configuration file or the Cloudflare dashboard.","url":"https://developers.cloudflare.com/pages/functions/wrangler-configuration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/functions/wrangler-configuration/
  schema: 1
---
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10925.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10924.md")
</aside>
<p>Pages Functions can be configured two ways, either via the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> or the Wrangler configuration file, a file used to customize the development and deployment setup for <a href="/workers/">Workers</a> and Pages Functions.</p>
<p>This page serves as a reference on how to configure your Pages project via the Wrangler configuration file.</p>
<p>If using a Wrangler configuration file, you must treat your file as the <a href="/pages/functions/wrangler-configuration/#source-of-truth">source of truth</a> for your Pages project configuration.</p>
<p>Using the Wrangler configuration file to configure your Pages project allows you to:</p>
<ul>
<li><strong>Store your configuration file in source control:</strong> Keep your configuration in your repository alongside the rest of your code.</li>
<li><strong>Edit your configuration via your code editor:</strong> Remove the need to switch back and forth between interfaces.</li>
<li><strong>Write configuration that is shared across environments:</strong> Define configuration like <a href="/pages/functions/bindings/">bindings</a> for local development, preview and production in one file.</li>
<li><strong>Ensure better access control:</strong> By using a configuration file in your project repository, you can control who has access to make changes without giving access to your Cloudflare dashboard.</li>
</ul>
<h2 id="example-wrangler-file">Example Wrangler file</h2>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/10926.md")
</div>
<h2 id="requirements">Requirements</h2>
<h3 id="v2-build-system">V2 build system</h3>
<p>Pages Functions configuration via the Wrangler configuration file requires the <a href="/pages/configuration/build-image/#v2-build-system">V2 build system</a> or later. To update from V1, refer to the <a href="/pages/configuration/build-image/#v1-to-v2-migration">V2 build system migration instructions</a>.</p>
<h3 id="wrangler">Wrangler</h3>
<p>You must have Wrangler version 3.45.0 or higher to use a Wrangler configuration file for your Pages project's configuration. To check your Wrangler version, update Wrangler or install Wrangler, refer to <a href="/workers/wrangler/install-and-update/">Install/Update Wrangler</a>.</p>
<h2 id="migrate-from-dashboard-configuration">Migrate from dashboard configuration</h2>
<p>The migration instructions for Pages projects that do not have a Wrangler file currently are different than those for Pages projects with an existing Wrangler file. Read the instructions based on your situation carefully to avoid errors in production.</p>
<h3 id="projects-with-existing-wrangler-file">Projects with existing Wrangler file</h3>
<p>Before you could use the Wrangler configuration file to define your preview and production configuration, it was possible to use the file to define which <a href="/pages/functions/bindings/">bindings</a> should be available to your Pages project in local development.</p>
<p>If you have been using a Wrangler configuration file for local development, you may already have a file in your Pages project that looks like this:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/10927.md")
</div>
<p>If you would like to use your existing Wrangler file for your Pages project configuration, you must:</p>
<ol>
<li>Add the <code>pages_build_output_dir</code> key with the appropriate value of your <a href="/pages/configuration/build-configuration/#build-commands-and-directories">build output directory</a> (for example, <code>pages_build_output_dir = &quot;./dist&quot;</code>.)</li>
<li>Review your existing Wrangler configuration carefully to make sure it aligns with your desired project configuration before deploying.</li>
</ol>
<p>If you add the <code>pages_build_output_dir</code> key to your Wrangler configuration file and deploy your Pages project, Pages will use whatever configuration was defined for local use, which is very likely to be non-production. Do not deploy until you are confident that your Wrangler configuration file is ready for production use.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="overwriting-configuration">Overwriting configuration</h3>
@markup("md", "content/.markup/bodies/10923.md")
</aside>
<p>You can continue to use your Wrangler file for local development without migrating it for production use by not adding a <code>pages_build_output_dir</code> key. If you do not add a <code>pages_build_output_dir</code> key and run <code>wrangler pages deploy</code>, you will see a warning message telling you that fields are missing and that the file will continue to be used for local development only.</p>
<h3 id="projects-without-existing-wrangler-file">Projects without existing Wrangler file</h3>
<p>If you have an existing Pages project with configuration set up via the Cloudflare dashboard and do not have an existing Wrangler file in your Project, run the <code>wrangler pages download config</code> command in your Pages project directory. The <code>wrangler pages download config</code> command will download your existing Cloudflare dashboard configuration and generate a valid Wrangler file in your Pages project directory.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10931.md")
</div></div>
<p>Review your generated Wrangler file. To start using the Wrangler configuration file for your Pages project's configuration, create a new deployment, via <a href="/pages/get-started/git-integration/">Git integration</a> or <a href="/pages/get-started/direct-upload/">Direct Upload</a>.</p>
<h3 id="handling-compatibility-dates-set-to-latest">Handling compatibility dates set to &quot;Latest&quot;</h3>
<p>In the Cloudflare dashboard, you can set compatibility dates for preview deployments to &quot;Latest&quot;. This will ensure your project is always using the latest compatibility date without the need to explicitly set it yourself.</p>
<p>If you download a Wrangler configuration file from a project configured with &quot;Latest&quot; using the <code>wrangler pages download</code> command, your Wrangler configuration file will have the latest compatibility date available at the time you downloaded the configuration file. Wrangler does not support the &quot;Latest&quot; functionality like the dashboard. Compatibility dates must be explicitly set when using a Wrangler configuration file.</p>
<p>Refer to <a href="/workers/configuration/compatibility-dates/">this guide</a> for more information on what compatibility dates are and how they work.</p>
<h2 id="differences-using-a-wrangler-configuration-file-for-pages-functions-and-workers">Differences using a Wrangler configuration file for Pages Functions and Workers</h2>
<p>If you have used <a href="/workers">Workers</a>, you may already be familiar with the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>. There are a few key differences to be aware of when using this file with your Pages Functions project:</p>
<ul>
<li>The configuration fields <strong>do not match exactly</strong> between Pages Functions Wrangler file and the Workers equivalent. For example, configuration keys like <code>main</code>, which are Workers specific, do not apply to a Pages Function's Wrangler configuration file. Some functionality supported by Workers, such as <a href="/workers/wrangler/configuration/#module-aliasing">module aliasing</a> cannot yet be used by Cloudflare Pages projects.</li>
<li>The Pages' Wrangler configuration file introduces a new key, <code>pages_build_output_dir</code>, which is only used for Pages projects.</li>
<li>The concept of <a href="/pages/functions/wrangler-configuration/#configure-environments">environments</a> and configuration inheritance in this file <strong>is not</strong> the same as Workers.</li>
<li>This file becomes the <a href="/pages/functions/wrangler-configuration/#source-of-truth">source of truth</a> when used, meaning that you <strong>can not edit the same fields in the dashboard</strong> once you are using this file.</li>
</ul>
<h2 id="configure-environments">Configure environments</h2>
<p>With a Wrangler configuration file, you can quickly set configuration across your local environment, preview deployments, and production.</p>
<h3 id="local-development">Local development</h3>
<p>The Wrangler configuration file applies locally when using <code>wrangler pages dev</code>. This means that you can test out configuration changes quickly without a need to login to the Cloudflare dashboard. Refer to the following config file for an example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/10932.md")
</div>
<p>This Wrangler configuration file adds the <code>nodejs_compat</code> compatibility flag and a KV namespace binding to your Pages project. Running <code>wrangler pages dev</code> in a Pages project directory with this Wrangler configuration file will apply the <code>nodejs_compat</code> compatibility flag locally, and expose the <code>KV</code> binding in your Pages Function code at <code>context.env.KV</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10922.md")
</aside>
<h3 id="production-and-preview-deployments">Production and preview deployments</h3>
<p>Once you are ready to deploy your project, you can set the configuration for production and preview deployments by creating a new deployment containing a Wrangler file.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10921.md")
</aside>
<p>To use the example above as your configuration for production, make a new production deployment using:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler pages deploy&#10;</code></pre>
<p>or more specifically:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler pages deploy --branch &lt;PRODUCTION BRANCH&gt;&#10;</code></pre>
<p>To deploy the configuration for preview deployments, you can run the same command as above while on a branch you have configured to work with <a href="/pages/configuration/branch-build-controls/#preview-branch-control">preview deployments</a>. This will set the configuration for all preview deployments, not just the deployments from a specific branch. Pages does not currently support branch-based configuration.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10920.md")
</aside>
<h3 id="environment-specific-overrides">Environment-specific overrides</h3>
<p>There are times that you might want to use different configuration across local, preview deployments, and production. It is possible to override configuration for production and preview deployments by using <code>[env.production]</code> or <code>[env.preview]</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10919.md")
</aside>
<p>Refer to the following Wrangler configuration file for an example of how to override preview deployment configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/10933.md")
</div>
<p>If you deployed this file via <code>wrangler pages deploy</code>, <code>name</code>, <code>pages_build_output_dir</code>, <code>kv_namespaces</code>, and <code>vars</code> would apply the configuration to local and production, while <code>env.preview</code> would override <code>kv_namespaces</code> and <code>vars</code> for preview deployments.</p>
<p>If you wanted to have configuration values apply to local and preview, but override production, your file would look like this:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/10934.md")
</div>
<p>You can always be explicit and override both preview and production:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/10935.md")
</div>
<h2 id="inheritable-keys">Inheritable keys</h2>
<p>Inheritable keys are configurable at the top-level, and can be inherited (or overridden) by environment-specific configuration.</p>
<ul>
<li>
<p><code>name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The name of your Pages project. Alphanumeric and dashes only.</li>
</ul>
</li>
<li>
<p><code>pages_build_output_dir</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The path to your project's build output folder. For example: <code>./dist</code>.</li>
</ul>
</li>
<li>
<p><code>compatibility_date</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>A date in the form <code>yyyy-mm-dd</code>, which will be used to determine which version of the Workers runtime is used. Refer to <a href="/workers/configuration/compatibility-dates/">Compatibility dates</a>.</li>
</ul>
</li>
<li>
<p><code>compatibility_flags</code> string[] optional</p>
<ul>
<li>A list of flags that enable features from upcoming features of the Workers runtime, usually used together with <code>compatibility_date</code>. Refer to <a href="/workers/configuration/compatibility-dates/">compatibility dates</a>.</li>
</ul>
</li>
<li>
<p><code>send_metrics</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Whether Wrangler should send usage data to Cloudflare for this project. Defaults to <code>true</code>. You can learn more about this in our <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/wrangler/telemetry.md">data policy</a>.</li>
</ul>
</li>
<li>
<p><code>limits</code> Limits optional</p>
<ul>
<li>Configures limits to be imposed on execution at runtime. Refer to <a href="#limits">Limits</a>.</li>
</ul>
</li>
<li>
<p><code>placement</code> Placement optional</p>
<ul>
<li>Specify how Pages Functions should be located to minimize round-trip time. Refer to <a href="/workers/configuration/placement/">Smart Placement</a>.</li>
</ul>
</li>
<li>
<p><code>upload_source_maps</code> boolean</p>
<ul>
<li>When <code>upload_source_maps</code> is set to <code>true</code>, Wrangler will upload any server-side source maps part of your Pages project to give corrected stack traces in logs.</li>
</ul>
</li>
</ul>
<h2 id="non-inheritable-keys">Non-inheritable keys</h2>
<p>Non-inheritable keys are configurable at the top-level, but, if any one non-inheritable key is overridden for any environment (for example,<code>[[env.production.kv_namespaces]]</code>), all non-inheritable keys must also be specified in the environment configuration and overridden.</p>
<p>For example, this configuration will not work:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/10936.md")
</div>
<p><code>[[env.production.vars]]</code> is set to override <code>[vars]</code>. Because of this <code>[[kv_namespaces]]</code> must also be overridden by defining <code>[[env.production.kv_namespaces]]</code>.</p>
<p>This will work for local development, but will fail to validate when you try to deploy.</p>
<ul>
<li>
<p><code>vars</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A map of environment variables to set when deploying your Function. Refer to <a href="/pages/functions/bindings/#environment-variables">Environment variables</a>.</li>
</ul>
</li>
<li>
<p><code>d1_databases</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A list of D1 databases that your Function should be bound to. Refer to <a href="/pages/functions/bindings/#d1-databases">D1 databases</a>.</li>
</ul>
</li>
<li>
<p><code>durable_objects</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A list of Durable Objects that your Function should be bound to. Refer to <a href="/pages/functions/bindings/#durable-objects">Durable Objects</a>.</li>
</ul>
</li>
<li>
<p><code>hyperdrive</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Specifies Hyperdrive configs that your Function should be bound to. Refer to <a href="/pages/functions/bindings/#r2-buckets">Hyperdrive</a>.</li>
</ul>
</li>
<li>
<p><code>kv_namespaces</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A list of KV namespaces that your Function should be bound to. Refer to <a href="/pages/functions/bindings/#kv-namespaces">KV namespaces</a>.</li>
</ul>
</li>
<li>
<p><code>queues.producers</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Specifies Queues Producers that are bound to this Function. Refer to <a href="/queues/get-started/#4-set-up-your-producer-worker">Queues Producers</a>.</li>
</ul>
</li>
<li>
<p><code>r2_buckets</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A list of R2 buckets that your Function should be bound to. Refer to <a href="/pages/functions/bindings/#r2-buckets">R2 buckets</a>.</li>
</ul>
</li>
<li>
<p><code>vectorize</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A list of Vectorize indexes that your Function should be bound to. Refer to <a href="/vectorize/get-started/intro/#3-bind-your-worker-to-your-index">Vectorize indexes</a>.</li>
</ul>
</li>
<li>
<p><code>services</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A list of service bindings that your Function should be bound to. Refer to <a href="/pages/functions/bindings/#service-bindings">service bindings</a>.</li>
</ul>
</li>
<li>
<p><code>analytics_engine_datasets</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Specifies analytics engine datasets that are bound to this Function. Refer to <a href="/analytics/analytics-engine/get-started/">Workers Analytics Engine</a>.</li>
</ul>
</li>
<li>
<p><code>ai</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Specifies an AI binding to this Function. Refer to <a href="/pages/functions/bindings/#workers-ai">Workers AI</a>.</li>
</ul>
</li>
</ul>
<h2 id="limits">Limits</h2>
<p>You can configure limits for your Pages project in the same way you can for Workers. Read <a href="/workers/wrangler/configuration/#limits">this guide</a> for more details.</p>
<h2 id="bindings">Bindings</h2>
<p>A <a href="/pages/functions/bindings/">binding</a> enables your Pages Functions to interact with resources on the Cloudflare Developer Platform. Use bindings to integrate your Pages Functions with Cloudflare resources like <a href="/kv/">KV</a>, <a href="/durable-objects/">Durable Objects</a>, <a href="/r2/">R2</a>, and <a href="/d1/">D1</a>. You can set bindings for both production and preview environments.</p>
<h3 id="d1-databases">D1 databases</h3>
<p><a href="/d1/">D1</a> is Cloudflare's serverless SQL database. A Function can query a D1 database (or databases) by creating a <a href="/workers/runtime-apis/bindings/">binding</a> to each database for <a href="/d1/worker-api/">D1 Workers Binding API</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10918.md")
</aside>
<ul>
<li>Configure D1 database bindings via your <a href="/workers/wrangler/configuration/#d1-databases">Wrangler file</a> the same way they are configured with Cloudflare Workers.</li>
<li>Interact with your <a href="/pages/functions/bindings/#d1-databases">D1 Database binding</a>.</li>
</ul>
<h3 id="durable-objects">Durable Objects</h3>
<p><a href="/durable-objects/">Durable Objects</a> provide low-latency coordination and consistent storage for the Workers platform.</p>
<ul>
<li>Configure Durable Object namespace bindings via your <a href="/workers/wrangler/configuration/#durable-objects">Wrangler file</a> the same way they are configured with Cloudflare Workers.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10917.md")
</aside>
<ul>
<li>Interact with your <a href="/pages/functions/bindings/#durable-objects">Durable Object namespace binding</a>.</li>
</ul>
<h3 id="environment-variables">Environment variables</h3>
<p><a href="/workers/configuration/environment-variables/">Environment variables</a> are a type of binding that allow you to attach text strings or JSON values to your Pages Function.</p>
<ul>
<li>Configure environment variables via your <a href="/workers/wrangler/configuration/#environment-variables">Wrangler file</a> the same way they are configured with Cloudflare Workers.</li>
<li>Interact with your <a href="/pages/functions/bindings/#environment-variables">environment variables</a>.</li>
</ul>
<h3 id="hyperdrive">Hyperdrive</h3>
<p><a href="/hyperdrive/">Hyperdrive</a> bindings allow you to interact with and query any Postgres database from within a Pages Function.</p>
<ul>
<li>Configure Hyperdrive bindings via your <a href="/workers/wrangler/configuration/#hyperdrive">Wrangler file</a> the same way they are configured with Cloudflare Workers.</li>
</ul>
<h3 id="kv-namespaces">KV namespaces</h3>
<p><a href="/kv/api/">Workers KV</a> is a global, low-latency, key-value data store. It stores data in a small number of centralized data centers, then caches that data in Cloudflare’s data centers after access.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10916.md")
</aside>
<ul>
<li>Configure KV namespace bindings via your <a href="/workers/wrangler/configuration/#kv-namespaces">Wrangler file</a> the same way they are configured with Cloudflare Workers.</li>
<li>Interact with your <a href="/pages/functions/bindings/#kv-namespaces">KV namespace binding</a>.</li>
</ul>
<h3 id="queues-producers">Queues Producers</h3>
<p><a href="/queues/">Queues</a> is Cloudflare's global message queueing service, providing <a href="/queues/reference/delivery-guarantees/">guaranteed delivery</a> and <a href="/queues/configuration/batching-retries/">message batching</a>. <a href="/queues/configuration/javascript-apis/#producer">Queue Producers</a> enable you to send messages into a queue within your Pages Function.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10915.md")
</aside>
<ul>
<li>Configure Queues Producer bindings via your <a href="/workers/wrangler/configuration/#queues">Wrangler file</a> the same way they are configured with Cloudflare Workers.</li>
<li>Interact with your <a href="/pages/functions/bindings/#queue-producers">Queues Producer binding</a>.</li>
</ul>
<h3 id="r2-buckets">R2 buckets</h3>
<p><a href="/r2">Cloudflare R2 Storage</a> allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud storage services.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10914.md")
</aside>
<ul>
<li>Configure R2 bucket bindings via your <a href="/workers/wrangler/configuration/#r2-buckets">Wrangler file</a> the same way they are configured with Cloudflare Workers.</li>
<li>Interact with your <a href="/pages/functions/bindings/#r2-buckets">R2 bucket bindings</a>.</li>
</ul>
<h3 id="vectorize-indexes">Vectorize indexes</h3>
<p>A <a href="/vectorize/">Vectorize index</a> allows you to insert and query vector embeddings for semantic search, classification and other vector search use-cases.</p>
<ul>
<li>Configure Vectorize bindings via your <a href="/workers/wrangler/configuration/#vectorize-indexes">Wrangler file</a> the same way they are configured with Cloudflare Workers.</li>
</ul>
<h3 id="service-bindings">Service bindings</h3>
<p>A service binding allows you to call a Worker from within your Pages Function. Binding a Pages Function to a Worker allows you to send HTTP requests to the Worker without those requests going over the Internet. The request immediately invokes the downstream Worker, reducing latency as compared to a request to a third-party service. Refer to <a href="/workers/runtime-apis/bindings/service-bindings/">About Service bindings</a>.</p>
<ul>
<li>Configure service bindings via your <a href="/workers/wrangler/configuration/#service-bindings">Wrangler file</a> the same way they are configured with Cloudflare Workers.</li>
<li>Interact with your <a href="/pages/functions/bindings/#service-bindings">service bindings</a>.</li>
</ul>
<h3 id="analytics-engine-datasets">Analytics Engine Datasets</h3>
<p><a href="/analytics/analytics-engine/">Workers Analytics Engine</a> provides analytics, observability and data logging from Pages Functions. Write data points within your Pages Function binding then query the data using the <a href="/analytics/analytics-engine/sql-api/">SQL API</a>.</p>
<ul>
<li>Configure Analytics Engine Dataset bindings via your <a href="/workers/wrangler/configuration/#analytics-engine-datasets">Wrangler file</a> the same way they are configured with Cloudflare Workers.</li>
<li>Interact with your <a href="/pages/functions/bindings/#analytics-engine">Analytics Engine Dataset</a>.</li>
</ul>
<h3 id="workers-ai">Workers AI</h3>
<p><a href="/workers-ai/">Workers AI</a> allows you to run machine learning models, on the Cloudflare network, from your own code – whether that be from Workers, Pages, or anywhere via REST API.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-ai-local-development-usage-charges">Workers AI local development usage charges</h3>
@markup("md", "content/.markup/bodies/10913.md")
</aside>
<p>Unlike other bindings, this binding is limited to one AI binding per Pages Function project.</p>
<ul>
<li>Configure Workers AI bindings via your <a href="/workers/wrangler/configuration/#workers-ai">Wrangler file</a> the same way they are configured with Cloudflare Workers.</li>
<li>Interact with your <a href="/pages/functions/bindings/#workers-ai">Workers AI binding</a>.</li>
</ul>
<h2 id="local-development-settings">Local development settings</h2>
<p>The local development settings that you can configure are the same for Pages Functions and Cloudflare Workers. Read <a href="/workers/wrangler/configuration/#local-development-settings">this guide</a> for more details.</p>
<h2 id="source-of-truth">Source of truth</h2>
<p>When used in your Pages Functions projects, your Wrangler file is the source of truth. You will be able to see, but not edit, the same fields when you log into the Cloudflare dashboard.</p>
<p>If you decide that you do not want to use a Wrangler configuration file for configuration, you can safely delete it and create a new deployment. Configuration values from your last deployment will still apply and you will be able to edit them from the dashboard.</p>
