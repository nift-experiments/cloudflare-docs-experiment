---
cp9:
  canonical: https://developers.cloudflare.com/workers/wrangler/deprecations/
  description: The differences between Wrangler versions, specifically deprecations and breaking changes.
  full_title: Deprecations · Cloudflare Workers docs
  head_html: <title>Deprecations · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="The differences between Wrangler versions, specifically deprecations and breaking changes."><link rel="canonical" href="https://developers.cloudflare.com/workers/wrangler/deprecations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/wrangler/deprecations/index.md"><meta property="og:title" content="Deprecations · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The differences between Wrangler versions, specifically deprecations and breaking changes."><meta property="og:url" content="https://developers.cloudflare.com/workers/wrangler/deprecations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/wrangler/deprecations/#page","headline":"Deprecations \u00b7 Cloudflare Workers docs","description":"The differences between Wrangler versions, specifically deprecations and breaking changes.","url":"https://developers.cloudflare.com/workers/wrangler/deprecations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/wrangler/deprecations/
  schema: 1
---
<p>Review the difference between Wrangler versions, specifically deprecations and breaking changes.</p>
<h2 id="wrangler-v4">Wrangler v4</h2>
<h3 id="workers-sites">Workers Sites</h3>
<p>Usage of <a href="/workers/wrangler/configuration/#workers-sites">Workers Sites</a> is deprecated. Instead, we recommend migrating to <a href="/workers/static-assets/">Workers Static Assets</a>. Support for using Workers Sites with Wrangler will be removed in a future version of Wrangler.</p>
<h3 id="service-environments">Service environments</h3>
<p>Usage of <a href="https://blog.cloudflare.com/introducing-worker-services/#services-have-environments">Service Environments</a>, enabled via the <code>legacy_env</code> property in Wrangler config, is deprecated. Instead, we recommend migrating to <a href="/workers/wrangler/configuration/#environments">Wrangler Environments</a>. Support for using Service Environments with Wrangler will be removed in a future version of Wrangler.</p>
<h2 id="wrangler-v3">Wrangler v3</h2>
<h3 id="deprecated-commands">Deprecated commands</h3>
<p>The following commands are deprecated in Wrangler as of Wrangler v3. These commands will be fully removed in a future version of Wrangler.</p>
<h4 id="generate"><code>generate</code></h4>
<p>The <code>wrangler generate</code> command is deprecated, but still active in v3. <code>wrangler generate</code> will be fully removed in v4.</p>
<p>Use <code>npm create cloudflare@latest</code> for new Workers and Pages projects.</p>
<h4 id="publish"><code>publish</code></h4>
<p>The <code>wrangler publish</code> command is deprecated, but still active in v3. <code>wrangler publish</code> will be fully removed in v4.</p>
<p>Use <a href="/workers/wrangler/commands/general/#deploy"><code>npx wrangler deploy</code></a> to deploy Workers.</p>
<h4 id="pages-publish"><code>pages publish</code></h4>
<p>The <code>wrangler pages publish</code> command is deprecated, but still active in v3. <code>wrangler pages publish</code> will be fully removed in v4.</p>
<p>Use <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler pages deploy</code></a> to deploy Pages.</p>
<h4 id="version"><code>version</code></h4>
<p>Instead, use <code>wrangler --version</code> to check the current version of Wrangler.</p>
<h3 id="deprecated-options">Deprecated options</h3>
<h4 id="experimental-local"><code>--experimental-local</code></h4>
<p><code>wrangler dev</code> in v3 is local by default so this option is no longer necessary.</p>
<h4 id="local"><code>--local</code></h4>
<p><code>wrangler dev</code> in v3 is local by default so this option is no longer necessary.</p>
<h4 id="persist"><code>--persist</code></h4>
<p><code>wrangler dev</code> automatically persists data by default so this option is no longer necessary.</p>
<h4 id="proxy-and-script-path-in-wrangler-pages-dev"><code>-- &lt;command&gt;</code>, <code>--proxy</code>, and <code>--script-path</code> in <code>wrangler pages dev</code></h4>
<p>These options prevent <code>wrangler pages dev</code> from being able to accurately emulate production's behavior for serving static assets and have therefore been deprecated. Instead of relying on Wrangler to proxy through to some other upstream dev server, you can emulate a more accurate behavior by building your static assets to a directory and pointing Wrangler to that directory with <code>wrangler pages dev &lt;directory&gt;</code>.</p>
<h4 id="legacy-assets-and-the-legacy-assets-config-file-property"><code>--legacy-assets</code> and the <code>legacy_assets</code> config file property</h4>
<p>We recommend you <a href="https://developers.cloudflare.com/workers/static-assets/">migrate to Workers assets</a></p>
<h4 id="node-compat-and-the-node-compat-config-file-property"><code>--node-compat</code> and the <code>node_compat</code> config file property</h4>
<p>Instead, use the <a href="https://developers.cloudflare.com/workers/runtime-apis/nodejs"><code>nodejs_compat</code> compatibility flag</a>. This includes the functionality from legacy <code>node_compat</code> polyfills and natively implemented Node.js APIs.</p>
<h4 id="the-usage-model-config-file-property">The <code>usage_model</code> config file property</h4>
<p>This no longer has any effect, after the <a href="https://blog.cloudflare.com/workers-pricing-scale-to-zero/">rollout of Workers Standard Pricing</a>.</p>
<h2 id="wrangler-v2">Wrangler v2</h2>
<p>Wrangler v2 introduces new fields for configuration and new features for developing and deploying a Worker, while deprecating some redundant fields.</p>
<ul>
<li><code>wrangler.toml</code> is no longer mandatory.</li>
<li><code>dev</code> and <code>publish</code> accept CLI arguments.</li>
<li><code>tail</code> can be run on arbitrary Worker names.</li>
<li><code>init</code> creates a project boilerplate.</li>
<li>JSON bindings for <code>vars</code>.</li>
<li>Local mode for <code>wrangler dev</code>.</li>
<li>Module system (for both modules and service worker format Workers).</li>
<li>DevTools.</li>
<li>TypeScript support.</li>
<li>Sharing development environment on the Internet.</li>
<li>Wider platform compatibility.</li>
<li>Developer hotkeys.</li>
<li>Better configuration validation.</li>
</ul>
<p>The following video describes some of the major changes in Wrangler v2, and shows you how Wrangler v2 can help speed up your workflow.</p>
<div style="position: relative; padding-top: 56.25%;"><iframe title="Embedded media" src="https://iframe.videodelivery.net/6ce3c7bd51288e1e8439f50ad63eda1d?poster=https%3A%2F%2Fcloudflarestream.com%2F6ce3c7bd51288e1e8439f50ad63eda1d%2Fthumbnails%2Fthumbnail.jpg%3Ftime%3D%26height%3D600" style="border: none; position: absolute; top: 0; left: 0; height: 100%; width: 100%;" allow="accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;" allowfullscreen="true"></iframe></div>
<h3 id="common-deprecations">Common deprecations</h3>
<p>Refer to the following list for common fields that are no longer required.</p>
<ul>
<li><code>type</code> is no longer required. Wrangler will infer the correct project type automatically.</li>
<li><code>zone_id</code> is no longer required. It can be deduced from the routes directly.</li>
<li><code>build.upload.format</code> is no longer used. The format is now inferred automatically from the code.</li>
<li><code>build.upload.main</code> and <code>build.upload.dir</code> are no longer required. Use the top level <code>main</code> field, which now serves as the entry-point for the Worker.</li>
<li><code>site.entry-point</code> is no longer required. The entry point should be specified through the <code>main</code> field.</li>
<li><code>webpack_config</code> and <code>webpack</code> properties are no longer supported. Refer to <a href="/workers/wrangler/migration/v1-to-v2/eject-webpack/">Migrate webpack projects from Wrangler version 1</a>.
Here are the Wrangler v1 commands that are no longer supported:</li>
<li><code>wrangler preview</code> - Use the <code>wrangler dev</code> command, for running your worker in your local environment.</li>
<li><code>wrangler generate</code> - If you want to use a starter template, clone its GitHub repository and manually initialize it.</li>
<li><code>wrangler route</code> - Routes are defined in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
<li><code>wrangler report</code> - If you find a bug, report it at <a href="https://github.com/cloudflare/workers-sdk/issues/new/choose">Wrangler issues</a>.</li>
<li><code>wrangler build</code> - If you wish to access the output from bundling your Worker, use <code>wrangler deploy --outdir=path/to/output</code>.</li>
</ul>
<h4 id="new-fields">New fields</h4>
<p>These are new fields that can be added to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<ul>
<li>
<p><strong><code>main</code></strong>: <code>string</code>, optional</p>
<p>The <code>main</code> field is used to specify an entry point to the Worker. It may be in the established service worker format, or the newer, preferred modules format. An entry point is now explicitly required, and can be configured either via the <code>main</code> field, or passed directly as a command line, for example, <code>wrangler dev index.js</code>. This field replaces the legacy <code>build.upload.main</code> field (which only applied to modules format Workers).</p>
</li>
<li>
<p><strong><code>rules</code></strong>: <code>array</code>, optional</p>
<p>The <code>rules</code> field is an array of mappings between module types and file patterns. It instructs Wrangler to interpret specific files differently than JavaScript. For example, this is useful for reading text-like content as text files, or compiled WASM as ready to instantiate and execute. These rules can apply to Workers of both the established service worker format, and the newer modules format. This field replaces the legacy <code>build.upload.rules</code> field (which only applied to modules format Workers).</p>
</li>
</ul>
<h4 id="non-mandatory-fields">Non-mandatory fields</h4>
<p>A few configuration fields which were previously required, are now optional in particular situations. They can either be inferred, or added as an optimization. No fields are required anymore when starting with Wrangler v2, and you can gradually add configuration as the need arises.</p>
<ul>
<li>
<p><strong><code>name</code></strong>: <code>string</code></p>
<p>The <code>name</code> configuration field is now not required for <code>wrangler dev</code>, or any of the <code>wrangler kv:*</code> commands. Further, it can also be passed as a command line argument as <code>--name &lt;name&gt;</code>. It is still required for <code>wrangler deploy</code>.</p>
</li>
<li>
<p><strong><code>account_id</code></strong>: <code>string</code></p>
<p>The <code>account_id</code> field is not required for any of the commands. Any relevant commands will check if you are logged in, and if not, will prompt you to log in. Once logged in, it will use your account ID and will not prompt you again until your login session expires. If you have multiple account IDs, you will be presented with a list of accounts to choose from.</p>
<p>You can still configure <code>account_id</code> in your Wrangler file, or as an environment variable <code>CLOUDFLARE_ACCOUNT_ID</code>. This makes startup faster and bypasses the list of choices if you have multiple IDs. The <code>CLOUDFLARE_API_TOKEN</code> environment variable is also useful for situations where it is not possible to login interactively. To learn more, visit <a href="/workers/ci-cd/external-cicd/">Running in CI/CD</a>.</p>
</li>
<li>
<p><strong><code>workers_dev</code></strong> <code>boolean</code>, default: <code>true</code> when no routes are present</p>
<p>The <code>workers_dev</code> field is used to indicate that the Worker should be published to a <code>*.workers.dev</code> subdomain. For example, for a Worker named <code>my-worker</code> and a previously configured <code>*.workers.dev</code> subdomain <code>username</code>, the Worker will get published to <code>my-worker.username.workers.dev.com</code>. This field is not mandatory, and defaults to <code>true</code> when <code>route</code> or <code>routes</code> are not configured. When routes are present, it defaults to <code>false</code>. If you want to neither publish it to a <code>*.workers.dev</code> subdomain nor any routes, set <code>workers_dev</code> to <code>false</code>. This useful when you are publishing a Worker as a standalone service that can only be accessed from another Worker with (<code>services</code>).</p>
</li>
</ul>
<h4 id="deprecated-fields-non-breaking">Deprecated fields (non-breaking)</h4>
<p>A few configuration fields are deprecated, but their presence is not a breaking change yet. It is recommended to read the warning messages and follow the instructions to migrate to the new configuration. They will be removed and stop working in a future version.</p>
<ul>
<li>
<p><strong><code>zone_id</code></strong>: <code>string</code>, deprecated</p>
<p>The <code>zone_id</code> field is deprecated and will be removed in a future release. It is now inferred from <code>route</code>/<code>routes</code>, and optionally from <code>dev.host</code> when using <code>wrangler dev</code>. This also makes it simpler to deploy a single Worker to multiple domains.</p>
</li>
<li>
<p><strong><code>build.upload</code></strong>: <code>object</code>, deprecated</p>
<p>The <code>build.upload</code> field is deprecated and will be removed in a future release. Its usage results in a warning with suggestions on rewriting the configuration file to remove the warnings.</p>
<ul>
<li><code>build.upload.main</code>/<code>build.upload.dir</code> are replaced by the <code>main</code> fields and are applicable to both service worker format and modules format Workers.</li>
<li><code>build.upload.rules</code> is replaced by the <code>rules</code> field and is applicable to both service worker format and modules format Workers.</li>
<li><code>build.upload.format</code> is no longer specified and is automatically inferred by <code>wrangler</code>.</li>
</ul>
</li>
</ul>
<h4 id="deprecated-fields-breaking">Deprecated fields (breaking)</h4>
<p>A few configuration fields are deprecated and will not work as expected anymore. It is recommended to read the error messages and follow the instructions to migrate to the new configuration.</p>
<ul>
<li>
<p><strong><code>site.entry-point</code></strong>: <code>string</code>, deprecated</p>
<p>The <code>site.entry-point</code> configuration was used to specify an entry point for Workers with a <code>[site]</code> configuration. This has been replaced by the top-level <code>main</code> field.</p>
</li>
<li>
<p><strong><code>type</code></strong>: <code>rust</code> | <code>javascript</code> | <code>webpack</code>, deprecated</p>
<p>The <code>type</code> configuration was used to specify the type of Worker. It has since been made redundant and is now inferred from usage. If you were using <code>type = &quot;webpack&quot;</code> (and the optional <code>webpack_config</code> field), you should read the <a href="/workers/wrangler/migration/v1-to-v2/eject-webpack/">webpack migration guide</a> to modify your project and use a custom build instead.</p>
</li>
</ul>
<h3 id="deprecated-commands-1">Deprecated commands</h3>
<p>The following commands are deprecated in Wrangler as of Wrangler v2.</p>
<h4 id="build"><code>build</code></h4>
<p>The <code>wrangler build</code> command is no longer available for building the Worker.</p>
<p>The equivalent functionality can be achieved by <code>wrangler publish --dry-run --outdir=path/to/build</code>.</p>
<h4 id="config"><code>config</code></h4>
<p>The <code>wrangler config</code> command is no longer available for authenticating via an API token.</p>
<p>Use <code>wrangler login</code> / <code>wrangler logout</code> to manage OAuth authentication, or provide an API token via the <code>CLOUDFLARE_API_TOKEN</code> environment variable.</p>
<h4 id="preview"><code>preview</code></h4>
<p>The <code>wrangler preview</code> command is no longer available for creating a temporary preview instance of the Worker.</p>
<p>Try using <code>wrangler dev</code> to try out a worker during development.</p>
<h4 id="subdomain">subdomain</h4>
<p>The <code>wrangler subdomain</code> command is no longer available for creating a <code>workers.dev</code> subdomain.</p>
<p>Create the <code>workers.dev</code> subdomain in <strong>Workers &amp; Pages</strong> &gt; select your Worker &gt; Your subdomain &gt; <strong>Change</strong>.</p>
<h4 id="route">route</h4>
<p>The <code>wrangler route</code> command is no longer available to configure a route for a Worker.</p>
<p>Routes are specified in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<h3 id="other-deprecated-behavior">Other deprecated behavior</h3>
<ul>
<li>
<p>Cloudflare dashboard-defined routes will not be added alongside Wrangler-defined routes. Wrangler-defined routes are the <code>route</code> or <code>routes</code> key in your <code>wrangler.toml</code>. If both are defined, only routes defined in <code>wrangler.toml</code> will be valid. To manage routes via the Cloudflare dashboard only, remove any <code>route</code> and <code>routes</code> keys from and add <code>workers_dev = false</code> to your Wrangler file.</p>
</li>
<li>
<p>Wrangler will no longer use <code>index.js</code> in the directory where <code>wrangler dev</code> is called as the entry point to a Worker. Use the <code>main</code> configuration field, or explicitly pass it as a command line argument, for example: <code>wrangler dev index.js</code>.</p>
</li>
<li>
<p>Wrangler will no longer assume that bare specifiers are file names if they are not represented as a path. For example, in a folder like so:</p>
</li>
</ul>
<pre tabindex="0"><code>project&#10;├── index.js&#10;└── some-dependency.js&#10;</code></pre>
<p>where the content of <code>index.js</code> is:</p>
<pre tabindex="0"><code class="language-js">import SomeDependency from &quot;some-dependency.js&quot;;&#10;&#10;addEventListener(&quot;fetch&quot;, (event) =&gt; {&#10;  // ...&#10;});&#10;</code></pre>
<p>Wrangler v1 would resolve <code>import SomeDependency from &quot;some-dependency.js&quot;;</code> to the file <code>some-dependency.js</code>. This will also work in Wrangler v2, but will also log a deprecation warning. In the future, this will break with an error. Instead, you should rewrite the import to specify that it is a relative path, like so:</p>
<pre tabindex="0"><code class="language-diff">&#45; import SomeDependency from &quot;some-dependency.js&quot;;&#10;&#43; import SomeDependency from &quot;./some-dependency.js&quot;;&#10;</code></pre>
<h3 id="wrangler-v1-and-v2-comparison-tables">Wrangler v1 and v2 comparison tables</h3>
<h4 id="commands">Commands</h4>
<table>
<thead>
<tr>
<th>Command</th>
<th>v1</th>
<th>v2</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>publish</code></td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><code>dev</code></td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><code>preview</code></td>
<td>✅</td>
<td>❌</td>
<td>Removed, use <code>dev</code> instead.</td>
</tr>
<tr>
<td><code>init</code></td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><code>generate</code></td>
<td>✅</td>
<td>❌</td>
<td>Removed, use <code>git clone</code> instead.</td>
</tr>
<tr>
<td><code>build</code></td>
<td>✅</td>
<td>❌</td>
<td>Removed, invoke your own build script instead.</td>
</tr>
<tr>
<td><code>secret</code></td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><code>route</code></td>
<td>✅</td>
<td>❌</td>
<td>Removed, use <code>publish</code> instead.</td>
</tr>
<tr>
<td><code>tail</code></td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><code>kv</code></td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><code>r2</code></td>
<td>🚧</td>
<td>✅</td>
<td>Introduced in Wrangler v1.19.8.</td>
</tr>
<tr>
<td><code>pages</code></td>
<td>❌</td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><code>config</code></td>
<td>✅</td>
<td>❓</td>
<td></td>
</tr>
<tr>
<td><code>login</code></td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><code>logout</code></td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><code>whoami</code></td>
<td>✅</td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><code>subdomain</code></td>
<td>✅</td>
<td>❓</td>
<td></td>
</tr>
<tr>
<td><code>report</code></td>
<td>✅</td>
<td>❌</td>
<td>Removed, error reports are made interactively.</td>
</tr>
</tbody>
</table>
<h4 id="configuration">Configuration</h4>
<table>
<thead>
<tr>
<th>Property</th>
<th>v1</th>
<th>v2</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>type = &quot;webpack&quot;</code></td>
<td>✅</td>
<td>❌</td>
<td>Removed, refer to <a href="/workers/wrangler/migration/v1-to-v2/eject-webpack/">this guide</a> to migrate.</td>
</tr>
<tr>
<td><code>type = &quot;rust&quot;</code></td>
<td>✅</td>
<td>❌</td>
<td>Removed, use <a href="https://github.com/cloudflare/workers-rs"><code>workers-rs</code></a> instead.</td>
</tr>
<tr>
<td><code>type = &quot;javascript&quot;</code></td>
<td>✅</td>
<td>🚧</td>
<td>No longer required, can be omitted.</td>
</tr>
</tbody>
</table>
<h4 id="features">Features</h4>
<table>
<thead>
<tr>
<th>Feature</th>
<th>v1</th>
<th>v2</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>TypeScript</td>
<td>❌</td>
<td>✅</td>
<td>You can give wrangler a TypeScript file, and it will automatically transpile it to JavaScript using <a href="https://github.com/evanw/esbuild"><code>esbuild</code></a> under-the-hood.</td>
</tr>
<tr>
<td>Local mode</td>
<td>❌</td>
<td>✅</td>
<td><code>wrangler dev --local</code> will run your Worker on your local machine instead of on our network. This is powered by <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/miniflare/">Miniflare</a>.</td>
</tr>
</tbody>
</table>
