---
cp9:
  canonical: https://developers.cloudflare.com/workers/wrangler/configuration/
  description: Learn how to configure your Cloudflare Worker using Wrangler v1. This guide covers top-level and environment-specific settings, key types, and deployment options.
  full_title: Configuration - Wrangler v1 (deprecated) · Cloudflare Workers docs
  head_html: <title>Configuration - Wrangler v1 (deprecated) · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to configure your Cloudflare Worker using Wrangler v1. This guide covers top-level and environment-specific settings, key types, and deployment options."><link rel="canonical" href="https://developers.cloudflare.com/workers/wrangler/configuration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/configuration/index.md"><meta property="og:title" content="Configuration - Wrangler v1 (deprecated) · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to configure your Cloudflare Worker using Wrangler v1. This guide covers top-level and environment-specific settings, key types, and deployment options."><meta property="og:url" content="https://developers.cloudflare.com/workers/wrangler/migration/v1-to-v2/wrangler-legacy/configuration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/wrangler/configuration/#page","headline":"Configuration - Wrangler v1 (deprecated) \u00b7 Cloudflare Workers docs","description":"Learn how to configure your Cloudflare Worker using Wrangler v1. This guide covers top-level and environment-specific settings, key types, and deployment options.","url":"https://developers.cloudflare.com/workers/wrangler/configuration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/wrangler/migration/v1-to-v2/wrangler-legacy/configuration/
  schema: 1
---
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17466.md")
</aside>
<h2 id="background">Background</h2>
<p>Your project will need some configuration before you can publish your Worker. Configuration is done through changes to keys and values stored in a Wrangler file located in the root of your project directory. You must manually edit this file to edit your keys and values before you can publish.</p>
<hr />
<h2 id="environments">Environments</h2>
<p>The top-level configuration is the collection of values you specify at the top of your Wrangler file. These values will be inherited by all environments, unless otherwise defined in the environment.</p>
<p>The layout of a top-level configuration in a Wrangler file is displayed below:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17467.md")
</div>
<p>Environment configuration (optional): the configuration values you specify under an <code>[env.name]</code> in your Wrangler file.</p>
<p>Environments allow you to deploy the same project to multiple places under multiple names. These environments are utilized with the <code>--env</code> or <code>-e</code> flag on the <a href="/workers/wrangler/migration/v1-to-v2/wrangler-legacy/commands/">commands</a> that are deploying live Workers:</p>
<ul>
<li><code>build</code></li>
<li><code>dev</code></li>
<li><code>preview</code></li>
<li><code>publish</code></li>
<li><code>secret</code></li>
</ul>
<p>Some environment properties can be <a href="#keys"><em>inherited</em></a> from the top-level configuration, but if new values are configured in an environment, they will always override those at the top level.</p>
<p>An example of an <code>[env.name]</code> configuration looks like this:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17468.md")
</div>
<p>To deploy this example Worker to the <code>helloworld</code> environment, you would run <code>wrangler deploy --env helloworld</code>.</p>
<hr />
<h2 id="keys">Keys</h2>
<p>There are three types of keys in a Wrangler file:</p>
<ul>
<li>
<p>Top level only keys are required to be configured at the top level of your Wrangler file only; multiple environments on the same project must share this key's value.</p>
</li>
<li>
<p>Inherited keys can be configured at the top level and/or environment. If the key is defined only at the top level, the environment will use the key's value from the top level. If the key is defined in the environment, the environment value will override the top-level value.</p>
</li>
<li>
<p>Non-inherited keys must be defined for every environment individually.</p>
</li>
<li>
<p><code>name</code> inherited required</p>
<ul>
<li>The name of your Worker script. If inherited, your environment name will be appended to the top level.</li>
</ul>
</li>
<li>
<p><code>type</code> top level required</p>
<ul>
<li>Specifies how <code>wrangler build</code> will build your project. There are three options: <code>javascript</code>, <code>webpack</code>, and <code>rust</code>. <code>javascript</code> checks for a build command specified in the <code>[build]</code> section, <code>webpack</code> builds your project using webpack v4, and <code>rust</code> compiles the Rust in your project to WebAssembly.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17465.md")
</aside>
<ul>
<li>
<p><code>account_id</code> inherited required</p>
<ul>
<li>This is the ID of the account associated with your zone. You might have more than one account, so make sure to use the ID of the account associated with the <code>zone_id</code> you provide, if you provide one. It can also be specified through the <code>CF_ACCOUNT_ID</code> environment variable.</li>
</ul>
</li>
<li>
<p><code>zone_id</code> inherited optional</p>
<ul>
<li>This is the ID of the zone or domain you want to run your Worker on. It can also be specified through the <code>CF_ZONE_ID</code> environment variable. This key is optional if you are using only a <code>*.workers.dev</code> subdomain.</li>
</ul>
</li>
<li>
<p><code>workers_dev</code> inherited optional</p>
<ul>
<li>This is a boolean flag that specifies if your Worker will be deployed to your <a href="https://workers.dev"><code>*.workers.dev</code></a> subdomain. If omitted, it defaults to false.</li>
</ul>
</li>
<li>
<p><code>route</code> not inherited optional</p>
<ul>
<li>A route, specified by URL pattern, on your zone that you would like to run your Worker on. <br /><code>route = &quot;http://example.com/*&quot;</code>. A <code>route</code> OR <code>routes</code> key is only required if you are not using a <a href="https://workers.dev"><code>*.workers.dev</code></a> subdomain.</li>
</ul>
</li>
<li>
<p><code>routes</code> not inherited optional</p>
<ul>
<li>A list of routes you would like to use your Worker on. These follow exactly the same rules a <code>route</code>, but you can specify a list of them.<br /><code>routes = [&quot;http://example.com/hello&quot;, &quot;http://example.com/goodbye&quot;]</code>. A <code>route</code> OR <code>routes</code> key is only required if you are not using a <code>*.workers.dev</code> subdomain.</li>
</ul>
</li>
<li>
<p><code>webpack_config</code> inherited optional</p>
<ul>
<li>This is the path to a custom webpack configuration file for your Worker. You must specify this field to use a custom webpack configuration, otherwise Wrangler will use a default configuration for you. Refer to the <a href="/workers/wrangler/migration/v1-to-v2/eject-webpack/">Wrangler webpack page</a> for more information.</li>
</ul>
</li>
<li>
<p><code>vars</code> not inherited optional</p>
<ul>
<li>An object containing text variables that can be directly accessed in a Worker script.</li>
</ul>
</li>
<li>
<p><code>kv_namespaces</code> not inherited optional</p>
<ul>
<li>These specify any <a href="#kv_namespaces">Workers KV</a> Namespaces you want to access from inside your Worker.</li>
</ul>
</li>
<li>
<p><code>site</code> inherited optional</p>
<ul>
<li>Determines the local folder to upload and serve from a Worker.</li>
</ul>
</li>
<li>
<p><code>dev</code> not inherited optional</p>
<ul>
<li>Arguments for <code>wrangler dev</code> that configure local server.</li>
</ul>
</li>
<li>
<p><code>triggers</code> inherited optional</p>
<ul>
<li>Configures cron triggers for running a Worker on a schedule.</li>
</ul>
</li>
<li>
<p><code>usage_model</code> inherited optional</p>
<ul>
<li>Specifies the <a href="/workers/platform/pricing/#workers">Usage Model</a> for your Worker. There are two options - <a href="/workers/platform/limits/#account-plan-limits"><code>bundled</code></a> and <a href="/workers/platform/limits/#account-plan-limits"><code>unbound</code></a>. For newly created Workers, if the Usage Model is omitted it will be set to the <a href="https://dash.cloudflare.com/?account=workers/default-usage-model">default Usage Model set on the account</a>. For existing Workers, if the Usage Model is omitted, it will be set to the Usage Model configured in the dashboard for that Worker.</li>
</ul>
</li>
<li>
<p><code>build</code> top level optional</p>
<ul>
<li>Configures a custom build step to be run by Wrangler when building your Worker. Refer to the <a href="#build">custom builds documentation</a> for more details.</li>
</ul>
</li>
</ul>
<h3 id="vars">vars</h3>
<p>The <code>vars</code> key defines a table of <a href="/workers/configuration/environment-variables/">environment variables</a> provided to your Worker script. All values are plaintext values.</p>
<p>Usage:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17469.md")
</div>
<p>The table keys are available to your Worker as global variables, which will contain their associated values.</p>
<pre tabindex="0"><code class="language-js">// Worker code:&#10;console.log(FOO);&#10;//=&gt; &quot;some value&quot;&#10;&#10;console.log(BAR);&#10;//=&gt; &quot;some other string&quot;&#10;</code></pre>
<p>Alternatively, you can define <code>vars</code> using an inline table format. This style should not include any new lines to be considered a valid TOML configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17470.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17464.md")
</aside>
<h3 id="kv-namespaces">kv_namespaces</h3>
<p><code>kv_namespaces</code> defines a list of KV namespace bindings for your Worker.</p>
<p>Usage:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17471.md")
</div>
<p>Alternatively, you can define <code>kv namespaces</code> like so:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17472.md")
</div>
<p>Much like environment variables and secrets, the <code>binding</code> names are available to your Worker as global variables.</p>
<pre tabindex="0"><code class="language-js">// Worker script:&#10;&#10;let value = await FOO.get(&quot;keyname&quot;);&#10;//=&gt; gets the value for &quot;keyname&quot; from&#10;//=&gt; the FOO variable, which points to&#10;//=&gt; the &quot;0f2ac...e279&quot; KV namespace&#10;</code></pre>
<ul>
<li>
<p><code>binding</code> required</p>
<ul>
<li>The name of the global variable your code will reference. It will be provided as a <a href="/kv/api/">KV runtime instance</a>.</li>
</ul>
</li>
<li>
<p><code>id</code> required</p>
<ul>
<li>The ID of the KV namespace that your <code>binding</code> should represent. Required for <code>wrangler publish</code>.</li>
</ul>
</li>
<li>
<p><code>preview_id</code> required</p>
<ul>
<li>The ID of the KV namespace that your <code>binding</code> should represent during <code>wrangler dev</code> or <code>wrangler preview</code>. Required for <code>wrangler dev</code> and <code>wrangler preview</code>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17463.md")
</aside>
<h3 id="site">site</h3>
<p>A <a href="/workers/configuration/sites/start-from-scratch">Workers Site</a> generated with <a href="/workers/wrangler/migration/v1-to-v2/wrangler-legacy/commands/#generate"><code>wrangler generate --site</code></a> or <a href="/workers/wrangler/migration/v1-to-v2/wrangler-legacy/commands/#init"><code>wrangler init --site</code></a>.</p>
<p>Usage:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17473.md")
</div>
<ul>
<li>
<p><code>bucket</code> required</p>
<ul>
<li>The directory containing your static assets. It must be a path relative to your Wrangler file. Example: <code>bucket = &quot;./public&quot;</code></li>
</ul>
</li>
<li>
<p><code>entry-point</code> optional</p>
<ul>
<li>The location of your Worker script. The default location is <code>workers-site</code>. Example: <code>entry-point = &quot;./workers-site&quot;</code></li>
</ul>
</li>
<li>
<p><code>include</code> optional</p>
<ul>
<li>An exclusive list of <code>.gitignore</code>-style patterns that match file or directory names from your <code>bucket</code> location. Only matched items will be uploaded. Example: <code>include = [&quot;upload_dir&quot;]</code></li>
</ul>
</li>
<li>
<p><code>exclude</code> optional</p>
<ul>
<li>A list of <code>.gitignore</code>-style patterns that match files or directories in your <code>bucket</code> that should be excluded from uploads. Example: <code>exclude = [&quot;ignore_dir&quot;]</code></li>
</ul>
</li>
</ul>
<p>You can also define your <code>site</code> using an <a href="https://github.com/toml-lang/toml/blob/master/toml.md#user-content-inline-table">alternative TOML syntax</a>.</p>
<h4 id="storage-limits">Storage Limits</h4>
<p>For exceptionally large pages, Workers Sites may not be ideal. There is a 25 MiB limit per page or file. Additionally, Wrangler will create an asset manifest for your files that will count towards your script’s size limit. If you have too many files, you may not be able to use Workers Sites.</p>
<h4 id="exclusively-including-files-directories">Exclusively including files/directories</h4>
<p>If you want to include only a certain set of files or directories in your <code>bucket</code>, add an <code>include</code> field to your
<code>[site]</code> section of your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17474.md")
</div>
<p>Wrangler will only upload files or directories matching the patterns in the <code>include</code> array.</p>
<h4 id="excluding-files-directories">Excluding files/directories</h4>
<p>If you want to exclude files or directories in your <code>bucket</code>, add an <code>exclude</code> field to your <code>[site]</code> section of your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17475.md")
</div>
<p>Wrangler will ignore files or directories matching the patterns in the <code>exclude</code> array when uploading assets to Workers KV.</p>
<h4 id="include-exclude">Include &gt; Exclude</h4>
<p>If you provide both <code>include</code> and <code>exclude</code> fields, the <code>include</code> field will be used and the <code>exclude</code> field will be ignored.</p>
<h4 id="default-ignored-entries">Default ignored entries</h4>
<p>Wrangler will always ignore:</p>
<ul>
<li><code>node_modules</code></li>
<li>Hidden files and directories</li>
<li>Symlinks</li>
</ul>
<h4 id="more-about-include-exclude-patterns">More about include/exclude patterns</h4>
<p>Refer to the <a href="https://git-scm.com/docs/gitignore">gitignore documentation</a> to learn more about the standard matching patterns.</p>
<h4 id="customizing-your-sites-build">Customizing your Sites Build</h4>
<p>Workers Sites projects use webpack by default. Though you can <a href="/workers/wrangler/migration/v1-to-v2/eject-webpack/">bring your own webpack configuration</a>, be aware of your <code>entry</code> and <code>context</code> settings.</p>
<p>You can also use the <code>[build]</code> section with Workers Sites, as long as your build step will resolve dependencies in <code>node_modules</code>. Refer to the <a href="#build">custom builds</a> section for more information.</p>
<h3 id="triggers">triggers</h3>
<p>A set of cron triggers used to call a Worker on a schedule.</p>
<p>Usage:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17476.md")
</div>
<ul>
<li><code>crons</code> optional
<ul>
<li>A set of <a href="https://crontab.guru/">cron expressions</a>, where each expression is a separate schedule to run the Worker on.</li>
</ul>
</li>
</ul>
<h3 id="dev">dev</h3>
<p>Arguments for <code>wrangler dev</code> can be configured here so you do not have to repeatedly pass them.</p>
<p>Usage:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17477.md")
</div>
<ul>
<li>
<p><code>ip</code> optional</p>
<ul>
<li>IP address for the local <code>wrangler dev</code> server to listen on, defaults to <code>127.0.0.1</code>.</li>
</ul>
</li>
<li>
<p><code>port</code> optional</p>
<ul>
<li>Port for local <code>wrangler dev</code> server to listen on, defaults to <code>8787</code>.</li>
</ul>
</li>
<li>
<p><code>local_protocol</code> optional</p>
<ul>
<li>Protocol that local <code>wrangler dev</code> server listen to requests on, defaults to <code>http</code>.</li>
</ul>
</li>
<li>
<p><code>upstream_protocol</code> optional</p>
<ul>
<li>Protocol that <code>wrangler dev</code> forwards requests on, defaults to <code>https</code>.</li>
</ul>
</li>
</ul>
<h3 id="build">build</h3>
<p>A custom build command for your project. There are two configurations based on the format of your Worker: <code>service-worker</code> and <code>modules</code>.</p>
<h4 id="service-workers">Service Workers</h4>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="service-workers-are-deprecated">Service Workers are deprecated</h3>
@markup("md", "content/.markup/bodies/17462.md")
</aside>
<p>This section is for customizing Workers with the <code>service-worker</code> format. These Workers use <code>addEventListener</code> and look like the following:</p>
<pre tabindex="0"><code class="language-js">addEventListener(&quot;fetch&quot;, (event) =&gt; {&#10;	event.respondWith(new Response(&quot;I&#x27;m a service Worker!&quot;));&#10;});&#10;</code></pre>
<p>Usage:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17478.md")
</div>
<h5 id="build-1"><code>[build]</code></h5>
<ul>
<li>
<p><code>command</code> optional</p>
<ul>
<li>The command used to build your Worker. On Linux and macOS, the command is executed in the <code>sh</code> shell and the <code>cmd</code> shell for Windows. The <code>&amp;&amp;</code> and <code>||</code> shell operators may be used.</li>
</ul>
</li>
<li>
<p><code>cwd</code> optional</p>
<ul>
<li>The working directory for commands, defaults to the project root directory.</li>
</ul>
</li>
<li>
<p><code>watch_dir</code> optional</p>
<ul>
<li>The directory to watch for changes while using <code>wrangler dev</code>, defaults to the <code>src</code> relative to the project root directory.</li>
</ul>
</li>
</ul>
<h5 id="build-upload"><code>[build.upload]</code></h5>
<ul>
<li><code>format</code> required
<ul>
<li>The format of the Worker script, must be <code>&quot;service-worker&quot;</code>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17461.md")
</aside>
<h4 id="modules">Modules</h4>
<p>Workers now supports the ES Modules syntax. This format allows you to export a collection of files and/or modules, unlike the Service Worker format which requires a single file to be uploaded.</p>
<p>Module Workers <code>export</code> their event handlers instead of using <code>addEventListener</code> calls.</p>
<p>Modules receive all bindings (KV Namespaces, Environment Variables, and Secrets) as arguments to the exported handlers. With the Service Worker format, these bindings are available as global variables.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17460.md")
</aside>
<p>An uploaded module may <code>import</code> other uploaded ES Modules. If using the CommonJS format, you may <code>require</code> other uploaded CommonJS modules.</p>
<pre tabindex="0"><code class="language-js">import html from &quot;./index.html&quot;;&#10;&#10;export default {&#10;	// * request is the same as `event.request` from the service worker format&#10;	// * waitUntil() and passThroughOnException() are accessible from `ctx` instead of `event` from the service worker format&#10;	// * env is where bindings like KV namespaces, Durable Object namespaces, Config variables, and Secrets&#10;	// are exposed, instead of them being placed in global scope.&#10;	async fetch(request, env, ctx) {&#10;		const headers = { &quot;Content-Type&quot;: &quot;text/html;charset=UTF-8&quot; };&#10;		return new Response(html, { headers });&#10;	},&#10;};&#10;</code></pre>
<p>To create a Workers project using Wrangler and Modules, add a <code>[build]</code> section:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17479.md")
</div>
<h5 id="build-2"><code>[build]</code></h5>
<ul>
<li>
<p><code>command</code> optional</p>
<ul>
<li>The command used to build your Worker. On Linux and macOS system, the command is executed in the <code>sh</code> shell and the <code>cmd</code> shell for Windows. The <code>&amp;&amp;</code> and <code>||</code> shell operators may be used.</li>
</ul>
</li>
<li>
<p><code>cwd</code> optional</p>
<ul>
<li>The working directory for commands, defaults to the project root directory.</li>
</ul>
</li>
<li>
<p><code>watch_dir</code> optional</p>
<ul>
<li>The directory to watch for changes while using <code>wrangler dev</code>, defaults to the <code>src</code> relative to the project root directory.</li>
</ul>
</li>
</ul>
<h5 id="build-upload-1"><code>[build.upload]</code></h5>
<ul>
<li>
<p><code>format</code> required</p>
<ul>
<li>The format of the Workers script, must be <code>&quot;modules&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>dir</code> optional</p>
<ul>
<li>The directory you wish to upload your modules from, defaults to the <code>dist</code> relative to the project root directory.</li>
</ul>
</li>
<li>
<p><code>main</code> required</p>
<ul>
<li>The relative path of the main module from <code>dir</code>, including the <code>./</code> prefix. The main module must be an ES module. For projects with a build script, this usually refers to the output of your JavaScript bundler.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17459.md")
</aside>
<ul>
<li><code>rules</code> optional
<ul>
<li>An ordered list of rules that define which modules to import, and what type to import them as.
You will need to specify rules to use Text, Data, and CompiledWasm modules, or when you wish to
have a <code>.js</code> file be treated as an <code>ESModule</code> instead of <code>CommonJS</code>.</li>
</ul>
</li>
</ul>
<p>Defaults:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17480.md")
</div>
<ul>
<li>
<p><code>type</code> required</p>
<ul>
<li>The module type, see the table below for acceptable options:</li>
</ul>
</li>
<li>
<p><code>globs</code> required</p>
<ul>
<li>UNIX-style <a href="https://docs.rs/globset/0.4.6/globset/#syntax">glob rules</a> that are used to determine the module type to use for a given file in <code>dir</code>. Globs are matched against the module's relative path from <code>build.upload.dir</code> without the <code>./</code> prefix. Rules are evaluated in order, starting at the top.</li>
</ul>
</li>
<li>
<p><code>fallthrough</code> optional</p>
<ul>
<li>This option allows further rules for this module type to be considered if set to true. If not specified or set to false, further rules for this module type will be ignored.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="example">Example</h2>
<p>To illustrate how these levels are applied, here is a Wrangler file using multiple environments:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17481.md")
</div>
