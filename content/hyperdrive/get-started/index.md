---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/get-started/
  description: Create your first Hyperdrive configuration and connect a Cloudflare Worker to your database.
  full_title: Getting started · Cloudflare Hyperdrive docs
  head_html: <title>Getting started · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Create your first Hyperdrive configuration and connect a Cloudflare Worker to your database."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/get-started/index.md"><meta property="og:title" content="Getting started · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create your first Hyperdrive configuration and connect a Cloudflare Worker to your database."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Hyperdrive"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/get-started/#page","headline":"Getting started \u00b7 Cloudflare Hyperdrive docs","description":"Create your first Hyperdrive configuration and connect a Cloudflare Worker to your database.","url":"https://developers.cloudflare.com/hyperdrive/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/get-started/
  schema: 1
---
<p>Hyperdrive accelerates access to your existing databases from Cloudflare Workers, making even single-region databases feel globally distributed.</p>
<p>By maintaining a connection pool to your database within Cloudflare's network, Hyperdrive reduces seven round-trips to your database before you can even send a query: the TCP handshake (1x), TLS negotiation (3x), and database authentication (3x).</p>
<p>Hyperdrive understands the difference between read and write queries to your database, and caches the most common read queries, improving performance and reducing load on your origin database.</p>
<p>This guide will instruct you through:</p>
<ul>
<li>Creating your first Hyperdrive configuration.</li>
<li>Creating a <a href="/workers/">Cloudflare Worker</a> and binding it to your Hyperdrive configuration.</li>
<li>Establishing a database connection from your Worker to a public database.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/973.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, ensure you have completed the following:</p>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a> if you have not already.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>. Use a Node version manager like <a href="https://github.com/nvm-sh/nvm">nvm</a> or <a href="https://volta.sh/">Volta</a> to avoid permission issues and change Node.js versions. <a href="/workers/wrangler/install-and-update/">Wrangler</a> requires a Node version of <code>16.17.0</code> or later.</li>
<li>Have a publicly accessible PostgreSQL or MySQL (or compatible) database. <em>If your database is in a private network</em>, refer to <a href="/hyperdrive/configuration/connect-to-private-database-vpc/">Connect to a private database using Workers VPC</a>.</li>
</ol>
<h2 id="1-log-in"><ol>
<li>Log in</li>
</ol></h2>
<p>Before creating your Hyperdrive binding, log in with your Cloudflare account by running:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login&#10;</code></pre>
<p>You will be directed to a web page asking you to log in to the Cloudflare dashboard. After you have logged in, you will be asked if Wrangler can make changes to your Cloudflare account. Scroll down and select <strong>Allow</strong> to continue.</p>
<h2 id="2-create-a-worker"><ol start="2">
<li>Create a Worker</li>
</ol></h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="new-to-workers">New to Workers?</h3>
@markup("md", "content/.markup/bodies/972.md")
</aside>
<p>Create a new project named <code>hyperdrive-tutorial</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- hyperdrive-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- hyperdrive-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare hyperdrive-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare hyperdrive-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest hyperdrive-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest hyperdrive-tutorial" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>This will create a new <code>hyperdrive-tutorial</code> directory. Your new <code>hyperdrive-tutorial</code> directory will include:</p>
<ul>
<li>A <code>&quot;Hello World&quot;</code> <a href="/workers/get-started/guide/#3-write-code">Worker</a> at <code>src/index.ts</code>.</li>
<li>A <a href="/workers/wrangler/configuration/"><code>wrangler.jsonc</code></a> configuration file. <code>wrangler.jsonc</code> is how your <code>hyperdrive-tutorial</code> Worker will connect to Hyperdrive.</li>
</ul>
<h3 id="enable-node-js-compatibility">Enable Node.js compatibility</h3>
<p><a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> is required for database drivers, and needs to be configured for your Workers project.</p>
<p>For compatibility dates of <code>2026-08-04</code> or later, Workers and Pages projects enable both <code>nodejs_compat</code> and <code>nodejs_compat_v2</code> by default. Built-in runtime APIs and polyfills are available without additional configuration. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date.</p>
<p>If your compatibility date is before <code>2026-08-04</code>, add the <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag"><code>nodejs_compat</code></a> <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag">compatibility flag</a> to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to opt in:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/974.md")
</div>
<p>To turn off <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> completely for a compatibility date of <code>2026-08-04</code> or later, remove the positive flags if present. Then add both <code>no_nodejs_compat</code> and <code>no_nodejs_compat_v2</code>. For configuration examples, refer to the <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag">Node.js compatibility flag</a>.</p>
<h2 id="3-connect-hyperdrive-to-a-database"><ol start="3">
<li>Connect Hyperdrive to a database</li>
</ol></h2>
<p>Hyperdrive works by connecting to your database, pooling database connections globally, and speeding up your database access through Cloudflare's network.</p>
<p>It will provide a secure connection string that is only accessible from your Worker which you can use to connect to your database through Hyperdrive.
This means that you can use the Hyperdrive connection string with your existing drivers or ORM libraries without needing significant changes to your code.</p>
<p>To create your first Hyperdrive database configuration, change into the directory you just created for your Workers project:</p>
<pre tabindex="0"><code class="language-sh">cd hyperdrive-tutorial&#10;</code></pre>
<p>To create your first Hyperdrive, you will need:</p>
<ul>
<li>The IP address (or hostname) and port of your database.</li>
<li>The database username (for example, <code>hyperdrive-demo</code>).</li>
<li>The password associated with that username.</li>
<li>The name of the database you want Hyperdrive to connect to. For example, <code>postgres</code> or <code>mysql</code>.</li>
</ul>
<p>Hyperdrive accepts the combination of these parameters in the common connection string format used by database drivers:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/977.md")
</div></div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="manage-caching">Manage caching</h3>
@markup("md", "content/.markup/bodies/971.md")
</aside>
<p>If successful, the command will output your new Hyperdrive configuration:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;hyperdrive&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;HYPERDRIVE&quot;,&#10;			&quot;id&quot;: &quot;&lt;example id: 57b7076f58be42419276f058a8968187&gt;&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Copy the <code>id</code> field: you will use this in the next step to make Hyperdrive accessible from your Worker script.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/970.md")
</aside>
<h2 id="4-bind-your-worker-to-hyperdrive"><ol start="4">
<li>Bind your Worker to Hyperdrive</li>
</ol></h2>
<p>You must create a binding in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> for your Worker to connect to your Hyperdrive configuration. <a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Workers to access resources, like Hyperdrive, on the Cloudflare developer platform.</p>
<p>To bind your Hyperdrive configuration to your Worker, add the following to the end of your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/978.md")
</div>
<p>Specifically:</p>
<ul>
<li>The value (string) you set for the <code>binding</code> (binding name) will be used to reference this database in your Worker. In this tutorial, name your binding <code>HYPERDRIVE</code>.</li>
<li>The binding must be <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variables">a valid JavaScript variable name</a>. For example, <code>binding = &quot;hyperdrive&quot;</code> or <code>binding = &quot;productionDB&quot;</code> would both be valid names for the binding.</li>
<li>Your binding is available in your Worker at <code>env.&lt;BINDING_NAME&gt;</code>.</li>
</ul>
<p>If you wish to use a local database during development, you can add a <code>localConnectionString</code> to your  Hyperdrive configuration with the connection string of your database:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/979.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/969.md")
</aside>
<h2 id="5-run-a-query-against-your-database"><ol start="5">
<li>Run a query against your database</li>
</ol></h2>
<p>Once you have created a Hyperdrive configuration and bound it to your Worker, you can run a query against your database.</p>
<h3 id="install-a-database-driver">Install a database driver</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/982.md")
</div></div>
<h3 id="write-a-worker">Write a Worker</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/985.md")
</div></div>
<h3 id="run-in-development-mode-optional">Run in development mode (optional)</h3>
<p>You can test your Worker locally before deploying by running <code>wrangler dev</code>. This runs your Worker code on your machine while connecting to your database.</p>
<p>The <code>localConnectionString</code> field works with both local and remote databases and allows you to connect directly to your database from your Worker project running locally. You must specify the SSL/TLS mode if required (<code>sslmode=require</code> for Postgres, <code>sslMode=REQUIRED</code> for MySQL).</p>
<p>To connect to a database during local development, configure <code>localConnectionString</code> in your <code>wrangler.jsonc</code>:</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;hyperdrive&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;HYPERDRIVE&quot;,&#10;			&quot;id&quot;: &quot;your-hyperdrive-id&quot;,&#10;			&quot;localConnectionString&quot;: &quot;postgres://user:password@your-database-host:5432/database&quot;,&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p>Or set an environment variable:</p>
<pre tabindex="0"><code class="language-sh">export CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_HYPERDRIVE=&quot;postgres://user:password@your-database-host:5432/database&quot;&#10;</code></pre>
<p>Then start local development:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/968.md")
</aside>
<h2 id="6-deploy-your-worker"><ol start="6">
<li>Deploy your Worker</li>
</ol></h2>
<p>You can now deploy your Worker to make your project accessible on the Internet. To deploy your Worker, run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;&#35; Outputs: https://hyperdrive-tutorial.&lt;YOUR_SUBDOMAIN&gt;.workers.dev&#10;</code></pre>
<p>You can now visit the URL for your newly created project to query your live database.</p>
<p>For example, if the URL of your new Worker is <code>hyperdrive-tutorial.&lt;YOUR_SUBDOMAIN&gt;.workers.dev</code>, accessing <code>https://hyperdrive-tutorial.&lt;YOUR_SUBDOMAIN&gt;.workers.dev/</code> will send a request to your Worker that queries your database directly.</p>
<p>By finishing this tutorial, you have created a Hyperdrive configuration, a Worker to access that database and deployed your project globally.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="reduce-latency-with-placement">Reduce latency with Placement</h3>
@markup("md", "content/.markup/bodies/967.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">how Hyperdrive works</a>.</li>
<li>How to <a href="/hyperdrive/concepts/query-caching/">configure query caching</a>.</li>
<li><a href="/hyperdrive/observability/troubleshooting/">Troubleshooting common issues</a> when connecting a database to Hyperdrive.</li>
</ul>
<p>If you have any feature requests or notice any bugs, share your feedback directly with the Cloudflare team by joining the <a href="https://discord.cloudflare.com">Cloudflare Developers community on Discord</a>.</p>
