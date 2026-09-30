---
cp9:
  canonical: https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/
  description: A guide for migrating from Cloudflare Pages to Cloudflare Workers. Includes a compatibility matrix for comparing the features of Cloudflare Workers and Pages.
  full_title: Migrate from Pages to Workers · Cloudflare Workers docs
  head_html: <title>Migrate from Pages to Workers · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="A guide for migrating from Cloudflare Pages to Cloudflare Workers. Includes a compatibility matrix for comparing the features of Cloudflare Workers and Pages."><link rel="canonical" href="https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/index.md"><meta property="og:title" content="Migrate from Pages to Workers · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A guide for migrating from Cloudflare Pages to Cloudflare Workers. Includes a compatibility matrix for comparing the features of Cloudflare Workers and Pages."><meta property="og:url" content="https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/#page","headline":"Migrate from Pages to Workers \u00b7 Cloudflare Workers docs","description":"A guide for migrating from Cloudflare Pages to Cloudflare Workers. Includes a compatibility matrix for comparing the features of Cloudflare Workers and Pages.","url":"https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/static-assets/migration-guides/migrate-from-pages/
  schema: 1
---
<p>You can deploy full-stack applications, including front-end static assets and back-end APIs, as well as server-side rendered pages (SSR), with <a href="/workers/static-assets/">Cloudflare Workers</a>.</p>
<p>Like Pages, requests for static assets on Workers are free, and <a href="#pages-functions">Pages Functions</a> invocations are charged at the same rate as Workers, so you can expect <a href="/workers/platform/pricing/#workers">a similar cost structure</a>.</p>
<p>Unlike Pages, Workers has a distinctly broader set of features available to it, (including Durable Objects, Cron Triggers, and more comprehensive Observability). A complete list can be found at <a href="#compatibility-matrix">the bottom of this page</a>.</p>
<h2 id="migration">Migration</h2>
<p>Migrating from Cloudflare Pages to Cloudflare Workers is often a straightforward process. The following are some of the most common steps you will need to take to migrate your project.</p>
<h3 id="frameworks">Frameworks</h3>
<p>If your Pages project uses <a href="/workers/framework-guides/">a popular framework</a>, most frameworks already have adapters available for Cloudflare Workers. Switch out any Pages-specific adapters for the Workers equivalent and follow any guidance that they provide.</p>
<h3 id="project-configuration">Project configuration</h3>
<p>If your project doesn't already have one, create a <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> (either <code>wrangler.jsonc</code>, <code>wrangler.json</code> or <code>wrangler.toml</code>) in the root of your project. The two mandatory fields are:</p>
<ul>
<li>
<p><a href="/workers/wrangler/configuration/#inheritable-keys"><code>name</code></a></p>
<p>Set this to the name of the Worker you wish to deploy to. This can be the same as your existing Pages project name, so long as it conforms to Workers' name restrictions (e.g. max length).</p>
</li>
<li>
<p><a href="/workers/configuration/compatibility-dates/"><code>compatibility_date</code></a>.</p>
<p>If you were already using <a href="/pages/functions/wrangler-configuration/#inheritable-keys">Pages Functions</a>, set this to the same date configured there. Otherwise, set it to the current date.</p>
</li>
</ul>
<h4 id="build-output-directory">Build output directory</h4>
<p>Where you previously would configure a &quot;build output directory&quot; for Pages (in either a <a href="/pages/functions/wrangler-configuration/#inheritable-keys">Wrangler configuration file</a> or in <a href="/pages/configuration/build-configuration/#build-commands-and-directories">the Cloudflare dashboard</a>), you must now set the <a href="/workers/static-assets/binding/#directory"><code>assets.directory</code></a> value for a Worker project.</p>
<p>Before, with <strong>Cloudflare Pages</strong>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17294.md")
</div>
<p>Now, with <strong>Cloudflare Workers</strong>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17295.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17293.md")
</aside>
<h4 id="serving-behavior">Serving behavior</h4>
<p>Pages would automatically attempt to determine the type of project you deployed. It would look for <code>404.html</code> and <code>index.html</code> files as signals for whether the project was likely a <a href="/pages/configuration/serving-pages/#single-page-application-spa-rendering">Single Page Application (SPA)</a> or if it should <a href="/pages/configuration/serving-pages/#not-found-behavior">serve custom 404 pages</a>.</p>
<p>In Workers, to prevent accidental misconfiguration, this behavior is explicit and <a href="/workers/static-assets/routing/">must be set up manually</a>.</p>
<p>For a Single Page Application (SPA):</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17296.md")
</div>
<p>For custom 404 pages:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17297.md")
</div>
<h5 id="ignoring-assets">Ignoring assets</h5>
<p>Pages would automatically exclude some files and folders from being uploaded as static assets such as <code>node_modules</code>, <code>.DS_Store</code>, and <code>.git</code>. If you wish to also avoid uploading these files to Workers, you can create an <a href="/workers/static-assets/binding/#ignoring-assets"><code>.assetsignore</code> file</a> in your project's static asset directory.</p>
<pre tabindex="0"><code class="language-txt">&#42;*/node_modules&#10;&#42;*/.DS_Store&#10;&#42;*/.git&#10;</code></pre>
<h4 id="pages-functions">Pages Functions</h4>
<h5 id="full-stack-framework">Full-stack framework</h5>
<p>If you use a full-stack framework powered by <a href="/pages/functions/">Pages Functions</a>, ensure you have <a href="#frameworks">updated your framework</a> to target Workers instead of Pages.</p>
<h5 id="pages-functions-with-an-advanced-mode-worker-js-file">Pages Functions with an &quot;advanced mode&quot; <code>_worker.js</code> file</h5>
<p>If you use Pages Functions with an <a href="/pages/functions/advanced-mode/">&quot;advanced mode&quot; <code>_worker.js</code> file</a>, you must first ensure this script doesn't get uploaded as a static asset. Either move <code>_worker.js</code> out of the static asset directory (recommended), or create <a href="/workers/static-assets/binding/#ignoring-assets">an <code>.assetsignore</code> file</a> in the static asset directory and include <code>_worker.js</code> within it.</p>
<pre tabindex="0"><code class="language-txt">_worker.js&#10;</code></pre>
<p>Then, update your configuration file's <code>main</code> field to point to the location of this Worker script:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17298.md")
</div>
<h5 id="pages-functions-with-a-functions-folder">Pages Functions with a <code>functions/</code> folder</h5>
<p>If you use <strong>Pages Functions with a <a href="/pages/functions/">folder of <code>functions/</code></a></strong>, you must first compile these functions into a single Worker script with the <a href="/workers/wrangler/commands/pages/#pages-functions-build"><code>wrangler pages functions build</code></a> command.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler pages functions build --outdir=./dist/worker/</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler pages functions build --outdir=./dist/worker/" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler pages functions build --outdir=./dist/worker/</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler pages functions build --outdir=./dist/worker/" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler pages functions build --outdir=./dist/worker/</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler pages functions build --outdir=./dist/worker/" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Although this command will remain available to you to run at any time, we do recommend considering using another framework if you wish to continue to use file-based routing. <a href="https://github.com/honojs/honox">HonoX</a> is one popular option.</p>
<p>Once the Worker script has been compiled, you can update your configuration file's <code>main</code> field to point to the location it was built to:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17299.md")
</div>
<h5 id="routes-json-and-pages-functions-middleware"><code>_routes.json</code> and Pages Functions middleware</h5>
<p>If you authored <a href="/pages/functions/routing/#create-a-_routesjson-file">a <code>_routes.json</code> file</a> in your Pages project, or used <a href="/pages/functions/middleware/">middleware</a> in Pages Functions, you must pay close attention to the configuration of your Worker script. Pages would default to serving your Pages Functions ahead of static assets and <code>_routes.json</code> and Pages Functions middleware allowed you to customize this behavior.</p>
<p>Workers, on the other hand, will default to serving static assets ahead of your Worker script, unless you have configured <a href="/workers/static-assets/routing/worker-script/#run-your-worker-script-first"><code>assets.run_worker_first</code></a>. This option is required if you are, for example, performing any authentication checks or logging requests before serving static assets.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17300.md")
</div>
<h5 id="starting-from-scratch">Starting from scratch</h5>
<p>If you wish to, you can start a new Worker script from scratch and take advantage of all of Wrangler's and the latest runtime features (e.g. <a href="/workers/runtime-apis/bindings/service-bindings/rpc/"><code>WorkerEntrypoint</code>s</a>, <a href="/workers/languages/typescript/">TypeScript support</a>, <a href="/workers/wrangler/bundling">bundling</a>, etc.):</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17301.md")
</div>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17302.md")
</div>
<h4 id="assets-binding">Assets binding</h4>
<p>Pages automatically provided <a href="/pages/functions/api-reference/#envassetsfetch">an <code>ASSETS</code> binding</a> to access static assets from Pages Functions. In Workers, the name of this binding is customizable and it must be manually configured:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17303.md")
</div>
<h4 id="runtime">Runtime</h4>
<p>If you had customized <a href="/workers/configuration/placement/">placement</a>, or set a <a href="/workers/configuration/compatibility-dates/">compatibility date</a> or any <a href="/workers/configuration/compatibility-flags/">compatibility flags</a> in your Pages project, you can define the same in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17304.md")
</div>
<h3 id="variables-secrets-and-bindings">Variables, secrets and bindings</h3>
<p><a href="/workers/configuration/environment-variables/">Variables</a> and <a href="/workers/runtime-apis/bindings/">bindings</a> can be set in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> and are made available in your Worker's environment (<code>env</code>). <a href="/workers/configuration/secrets/">Secrets</a> can uploaded with Wrangler or defined in the Cloudflare dashboard for <a href="/workers/configuration/secrets/#adding-secrets-to-your-project">production</a> and <a href="/workers/configuration/secrets/#local-development-with-secrets"><code>.dev.vars</code> for local development</a>.</p>
<p>If you are <a href="#builds">using Workers Builds</a>, ensure you also <a href="/workers/ci-cd/builds/configuration/">configure any variables relevant to the build environment there</a>. Unlike Pages, Workers does not share the same set of runtime and build-time variables.</p>
<h3 id="wrangler-commands">Wrangler commands</h3>
<p>Where previously you used <a href="/workers/wrangler/commands/pages/#pages-dev"><code>wrangler pages dev</code></a> and <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler pages deploy</code></a>, now instead use <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> and <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a>. Additionally, if you are using a Vite-powered framework, <a href="/workers/vite-plugin/">our new Vite plugin</a> may be able offer you an even simpler development experience.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wrangler-uses-a-different-default-port-for-the-local-development">Wrangler uses a different default port for the local development</h3>
@markup("md", "content/.markup/bodies/17292.md")
</aside>
<h3 id="builds">Builds</h3>
<p>If you are using Pages' built-in CI/CD system, you can swap this for Workers Builds by first <a href="/workers/ci-cd/builds/#get-started">connecting your repository to Workers Builds</a> and then <a href="/pages/configuration/git-integration/#disable-automatic-deployments">disabling automatic deployments on your Pages project</a>.</p>
<h3 id="preview-environment">Preview environment</h3>
<p>Pages automatically creates a preview environment for each project, and can be independently configured.</p>
<p>To get a similar experience in Workers, you must:</p>
<ol>
<li>Ensure <a href="/workers/versions-and-deployments/preview-urls/">preview URLs</a> are enabled (they are on by default).</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17305.md")
</div>
<ol>
<li><a href="/workers/ci-cd/builds/build-branches/#configure-non-production-branch-builds">Enable non-production branch builds</a> in Workers Builds.</li>
</ol>
<p>Optionally, you can also <a href="/workers/configuration/cloudflare-access/">protect these preview URLs with Cloudflare Access</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17291.md")
</aside>
<h3 id="headers-and-redirects">Headers and redirects</h3>
<p><a href="/workers/static-assets/headers/"><code>_headers</code></a> and <a href="/workers/static-assets/redirects/"><code>_redirects</code></a> files are supported natively in Workers with static assets. Ensure that, just like for Pages, these files are included in the static asset directory of your project.</p>
<h3 id="pages-dev">pages.dev</h3>
<p>Where previously you were offered a <code>pages.dev</code> subdomain for your Pages project, you can now configure a personalized <code>workers.dev</code> subdomain for all of your Worker projects. You can <a href="/workers/configuration/routing/workers-dev/#configure-workersdev">configure this subdomain in the Cloudflare dashboard</a>, and opt-in to using it with the <a href="/workers/configuration/routing/workers-dev/#disabling-workersdev-in-the-wrangler-configuration-file"><code>workers_dev</code> option</a> in your configuration file.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17306.md")
</div>
<h3 id="custom-domains">Custom domains</h3>
<p>If your domain's nameservers are managed by Cloudflare, you can, like Pages, configure a <a href="/workers/configuration/routing/custom-domains/">custom domain</a> for your Worker. Additionally, you can also configure a <a href="/workers/configuration/routing/routes/">route</a> if you only wish to some subset of paths to be served by your Worker.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17290.md")
</aside>
<h3 id="rollout">Rollout</h3>
<p>Once you have validated the behavior of Worker, and are satisfied with the development workflows, and have migrated all of your production traffic, you can delete your Pages project in the Cloudflare dashboard or with Wrangler:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler pages project delete</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler pages project delete" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler pages project delete</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler pages project delete" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler pages project delete</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler pages project delete" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="migrate-your-project-using-an-ai-coding-assistant">Migrate your project using an AI coding assistant</h2>
<p>You can add the following <a href="https://developers.cloudflare.com/workers/prompts/pages-to-workers.txt">experimental prompt</a> in your preferred coding assistant (e.g. Claude Code, Cursor) to make your project compatible with Workers:</p>
<pre tabindex="0"><code>https://developers.cloudflare.com/workers/prompts/pages-to-workers.txt&#10;</code></pre>
<p>You can also use the Cloudflare Documentation <a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/docs-ai-search">MCP server</a> in your coding assistant to provide better context to your LLM when building with Workers, which includes this prompt when you ask to migrate from Pages to Workers.</p>
<h2 id="compatibility-matrix">Compatibility matrix</h2>
<p>This compatibility matrix compares the features of Workers and Pages. Unless otherwise stated below, what works in Pages works in Workers, and what works in Workers works in Pages. Think something is missing from this list? <a href="https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/static-assets/compatibility-matrix.mdx">Open a pull request</a> or <a href="https://github.com/cloudflare/cloudflare-docs/issues/new">create a GitHub issue</a>.</p>
<p><strong>Legend</strong> <br />
✅: Supported <br />
⏳: Coming soon <br />
🟡: Unsupported, workaround available <br />
❌: Unsupported</p>
<table>
<thead>
<tr>
<th></th>
<th>Workers</th>
<th>Pages</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Writing, Testing, and Deploying Code</strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="/workers/vite-plugin/">Cloudflare Vite plugin</a></td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td><a href="/workers/versions-and-deployments/rollbacks/">Rollbacks</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/versions-and-deployments/">Gradual Deployments</a></td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td><a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/testing">Testing tools</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/local-development/">Local Development</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/wrangler/commands/">Remote Development (<code>--remote</code>)</a></td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td><a href="https://blog.cloudflare.com/improved-quick-edit">Quick Editor in Dashboard</a></td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td><strong>Static Assets</strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="/pages/configuration/early-hints/">Early Hints</a></td>
<td>🟡 <sup><a href="#footnote-1">1</a></sup></td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/static-assets/headers/">Custom HTTP headers for static assets</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/static-assets/binding/#run_worker_first">Middleware</a></td>
<td>✅ <sup><a href="#footnote-2">2</a></sup></td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/static-assets/redirects/">Redirects</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/configuration/placement/">Smart Placement</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/static-assets/routing/advanced/serving-a-subdirectory/">Serve assets on a path</a></td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td><strong>Observability</strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="/workers/observability/">Workers Logs</a></td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td><a href="/workers/observability/logs/logpush/">Logpush</a></td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td><a href="/workers/observability/logs/tail-workers/">Tail Workers</a></td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td><a href="/workers/observability/logs/real-time-logs/">Real-time logs</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/observability/source-maps/">Source Maps</a></td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td><strong>Runtime APIs &amp; Compute Models</strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/nodejs/">Node.js Compatibility Mode</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/durable-objects/api/">Durable Objects</a></td>
<td>✅</td>
<td>🟡 <sup><a href="#footnote-3">3</a></sup></td>
</tr>
<tr>
<td><a href="/workers/configuration/cron-triggers/">Cron Triggers</a></td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td><strong>Bindings</strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="/workers-ai/get-started/workers-wrangler/#2-connect-your-worker-to-workers-ai">AI</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/analytics/analytics-engine">Analytics Engine</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/static-assets/binding/">Assets</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/browser-run/">Browser Run</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/d1/worker-api/">D1</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/email-service/api/send-emails/workers-api/">Email Workers</a></td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td><a href="/workers/configuration/environment-variables/">Environment Variables</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/hyperdrive/">Hyperdrive</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/images/optimization/binding/">Image Resizing</a></td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td><a href="/kv/">KV</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/bindings/mtls/">mTLS</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/queues/configuration/configure-queues/#producer-worker-configuration">Queue Producers</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/queues/configuration/configure-queues/#consumer-worker-configuration">Queue Consumers</a></td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td><a href="/r2/">R2</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/bindings/rate-limit/">Rate Limiting</a></td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td><a href="/workers/configuration/secrets/">Secrets</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/bindings/service-bindings/">Service bindings</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/vectorize/get-started/intro/#3-bind-your-worker-to-your-index">Vectorize</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><strong>Builds (CI/CD)</strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="/workers/ci-cd/builds/advanced-setups/">Monorepos</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/ci-cd/builds/build-watch-paths/">Build Watch Paths</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/ci-cd/builds/build-caching/">Build Caching</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/ci-cd/builds/deploy-hooks/">Deploy Hooks</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/pages/configuration/branch-build-controls/">Branch Deploy Controls</a></td>
<td>🟡 <sup><a href="#footnote-4">4</a></sup></td>
<td>✅</td>
</tr>
<tr>
<td><a href="/pages/how-to/custom-branch-aliases/">Custom Branch Aliases</a></td>
<td>⏳</td>
<td>✅</td>
</tr>
<tr>
<td><strong>Pages Functions</strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="/pages/functions/routing/">File-based Routing</a></td>
<td>🟡 <sup><a href="#footnote-5">5</a></sup></td>
<td>✅</td>
</tr>
<tr>
<td><a href="/pages/functions/plugins/">Pages Plugins</a></td>
<td>🟡 <sup><a href="#footnote-6">6</a></sup></td>
<td>✅</td>
</tr>
<tr>
<td><strong>Domain Configuration</strong></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="/workers/configuration/routing/custom-domains/#add-a-custom-domain">Custom domains</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/configuration/routing/custom-domains/#set-up-a-custom-domain-in-the-dashboard">Custom subdomains</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/pages/configuration/custom-domains/#add-a-custom-cname-record">Custom domains outside Cloudflare zones</a></td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/workers/configuration/routing/routes/">Non-root routes</a></td>
<td>✅</td>
<td>❌</td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Workers can use Early Hints when the zone setting is turned on. Your Worker must send the appropriate `Link` headers. For more information, refer to the [103 Early Hints](/workers/examples/103-early-hints/) example.</li>
<li id="footnote-2">Middleware can be configured via the [`run_worker_first`](/workers/static-assets/binding/#run_worker_first) option, but is charged as a normal Worker invocation. We plan to explore additional related options in the future.</li>
<li id="footnote-3">To [use Durable Objects with your Cloudflare Pages project](/pages/functions/bindings/#durable-objects), you must create a separate Worker with a Durable Object and then declare a binding to it in both your Production and Preview environments. Using Durable Objects with Workers is simpler and recommended.</li>
<li id="footnote-4">Workers Builds supports enabling [non-production branch builds](/workers/ci-cd/builds/build-branches/#configure-non-production-branch-builds), though does not yet have the same level of configurability as Pages does.</li>
<li id="footnote-5">Workers [supports popular frameworks](/workers/framework-guides/), many of which implement file-based routing. Additionally, you can use Wrangler to [compile your folder of `functions/`](#pages-functions-with-a-functions-folder) into a Worker to help ease the migration from Pages to Workers.</li>
<li id="footnote-6">As in <sup>5</sup>, Wrangler can [compile your Pages Functions into a Worker](#pages-functions-with-a-functions-folder). Or if you are starting from scratch, everything that is possible with Pages Functions can also be achieved by adding code to your Worker or by using framework-specific plugins for relevant third party tools.</li></ol></section>
