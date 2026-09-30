---
cp9:
  canonical: https://developers.cloudflare.com/agents/runtime/operations/configuration/
  description: Configure Wrangler bindings, environment variables, and type generation for a project using the Agents SDK.
  full_title: Configuration · Cloudflare Agents docs
  head_html: <title>Configuration · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Wrangler bindings, environment variables, and type generation for a project using the Agents SDK."><link rel="canonical" href="https://developers.cloudflare.com/agents/runtime/operations/configuration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/runtime/operations/configuration/index.md"><meta property="og:title" content="Configuration · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Wrangler bindings, environment variables, and type generation for a project using the Agents SDK."><meta property="og:url" content="https://developers.cloudflare.com/agents/runtime/operations/configuration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/runtime/operations/configuration/#page","headline":"Configuration \u00b7 Cloudflare Agents docs","description":"Configure Wrangler bindings, environment variables, and type generation for a project using the Agents SDK.","url":"https://developers.cloudflare.com/agents/runtime/operations/configuration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/runtime/operations/configuration/
  schema: 1
---
<p>This guide covers everything you need to configure agents for local development and production deployment, including Wrangler configuration file setup, type generation, environment variables, and the Cloudflare dashboard.</p>
<h2 id="project-structure">Project structure</h2>
<p>The typical file structure for an Agent project created from <code>npm create cloudflare@latest agents-starter -- --template cloudflare/agents-starter</code> follows:</p>
<pre tabindex="0" class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/2311.md")&#10;&#10;&#10;</pre>
<h2 id="wrangler-configuration-file">Wrangler configuration file</h2>
<p>The <code>wrangler.jsonc</code> file configures your Cloudflare Worker and its bindings. Here is a complete example for an agents project:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2312.md")
</div>
<h3 id="key-fields">Key fields</h3>
<h4 id="compatibility-flags"><code>compatibility_flags</code></h4>
<p>The <code>nodejs_compat</code> flag is required for agents:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2313.md")
</div>
<p>This enables Node.js compatibility mode, which agents depend on for crypto, streams, and other Node.js APIs.</p>
<h4 id="durable-objects-bindings"><code>durable_objects.bindings</code></h4>
<p>Each agent class needs a binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2314.md")
</div>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td>The property name on <code>env</code>. Use this in code: <code>env.Counter</code></td>
</tr>
<tr>
<td><code>class_name</code></td>
<td>Must match the exported class name exactly</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="when-name-and-class-name-differ">When `name` and `class_name` differ</h3>
@markup("md", "content/.markup/bodies/2310.md")
</aside>
<h4 id="exports"><code>exports</code></h4>
<p>The <code>exports</code> field declares each Agent class your Worker exports and the storage backend Cloudflare should use for it:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2315.md")
</div>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>type</code></td>
<td>The kind of export. Always <code>&quot;durable-object&quot;</code> for an Agent.</td>
</tr>
<tr>
<td><code>storage</code></td>
<td>The storage backend. Use <code>&quot;sqlite&quot;</code> for new Agents (recommended).</td>
</tr>
</tbody>
</table>
<p>For details on renaming, deleting, or transferring Agent classes, refer to <a href="/durable-objects/reference/durable-objects-migrations/">Durable Object class exports</a>. Existing Workers using the legacy <code>migrations</code> array continue to work — refer to <a href="/durable-objects/reference/durable-object-class-migrations-legacy/">Durable Object class migrations (legacy)</a>.</p>
<h4 id="assets"><code>assets</code></h4>
<p>For serving static files (HTML, CSS, JS):</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2316.md")
</div>
<p>With a binding, you can serve assets programmatically:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2317.md")
</div>
<h4 id="ai"><code>ai</code></h4>
<p>For Workers AI integration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2318.md")
</div>
<p>Access in your agent:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2319.md")
</div>
<h2 id="typescript-configuration">TypeScript configuration</h2>
<p>The Agents SDK ships a shared <code>tsconfig.json</code> that sets all the compiler options needed for agents projects — including the <code>ES2021</code> target required for <code>@callable()</code> decorators, strict mode, bundler module resolution, and Workers types.</p>
<p>Extend it in your <code>tsconfig.json</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;extends&quot;: &quot;agents/tsconfig&quot;&#10;}&#10;</code></pre>
<p>This is equivalent to:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;compilerOptions&quot;: {&#10;		&quot;target&quot;: &quot;ES2021&quot;,&#10;		&quot;lib&quot;: [&quot;ES2022&quot;, &quot;DOM&quot;, &quot;DOM.Iterable&quot;],&#10;		&quot;jsx&quot;: &quot;react-jsx&quot;,&#10;		&quot;module&quot;: &quot;ES2022&quot;,&#10;		&quot;moduleResolution&quot;: &quot;bundler&quot;,&#10;		&quot;types&quot;: [&quot;node&quot;, &quot;@cloudflare/workers-types&quot;, &quot;vite/client&quot;],&#10;		&quot;allowImportingTsExtensions&quot;: true,&#10;		&quot;noEmit&quot;: true,&#10;		&quot;isolatedModules&quot;: true,&#10;		&quot;verbatimModuleSyntax&quot;: true,&#10;		&quot;esModuleInterop&quot;: true,&#10;		&quot;forceConsistentCasingInFileNames&quot;: true,&#10;		&quot;strict&quot;: true,&#10;		&quot;skipLibCheck&quot;: true&#10;	}&#10;}&#10;</code></pre>
<p>You can override individual options as needed:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;extends&quot;: &quot;agents/tsconfig&quot;,&#10;	&quot;compilerOptions&quot;: {&#10;		&quot;jsx&quot;: &quot;preserve&quot;&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2308.md")
</aside>
<h2 id="vite-configuration">Vite configuration</h2>
<p>The Agents SDK provides a Vite plugin that handles TC39 decorator transforms. Vite 8 uses Oxc for transpilation, which does not yet support TC39 decorators — without this plugin, <code>@callable()</code> and other decorators will fail at runtime.</p>
<p>Add the plugin to your <code>vite.config.ts</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2320.md")
</div>
<p>The <code>agents()</code> plugin is safe to include even if your project does not use decorators. It only runs the transform on files that contain <code>@</code> syntax.</p>
<p>The starter template and all examples include this plugin by default. If you encounter <code>SyntaxError: Invalid or unexpected token</code> with decorators, refer to <a href="/agents/runtime/lifecycle/callable-methods/#troubleshooting">Callable methods — Troubleshooting</a>.</p>
<h2 id="generating-types">Generating types</h2>
<p>Wrangler can generate TypeScript types for your bindings.</p>
<h3 id="automatic-generation">Automatic generation</h3>
<p>Run the types command:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler types&#10;</code></pre>
<p>This creates or updates <code>worker-configuration.d.ts</code> with your <code>Env</code> type.</p>
<h3 id="custom-output-path">Custom output path</h3>
<p>Specify a custom path:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler types env.d.ts&#10;</code></pre>
<h3 id="without-runtime-types">Without runtime types</h3>
<p>For cleaner output (recommended for agents):</p>
<pre tabindex="0"><code class="language-sh">npx wrangler types env.d.ts --include-runtime false&#10;</code></pre>
<p>This generates just your bindings without Cloudflare runtime types.</p>
<h3 id="example-generated-output">Example generated output</h3>
<pre tabindex="0"><code class="language-ts">// env.d.ts (generated)&#10;declare namespace Cloudflare {&#10;	interface Env {&#10;		OPENAI_API_KEY: string;&#10;		Counter: DurableObjectNamespace;&#10;		ChatAgent: DurableObjectNamespace;&#10;	}&#10;}&#10;interface Env extends Cloudflare.Env {}&#10;</code></pre>
<h3 id="manual-type-definition">Manual type definition</h3>
<p>You can also define types manually:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2321.md")
</div>
<h3 id="adding-to-package-json">Adding to package.json</h3>
<p>Add a script for easy regeneration:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;scripts&quot;: {&#10;		&quot;types&quot;: &quot;wrangler types env.d.ts --include-runtime false&quot;&#10;	}&#10;}&#10;</code></pre>
<h2 id="environment-variables-and-secrets">Environment variables and secrets</h2>
<h3 id="local-development-env">Local development (<code>.env</code>)</h3>
<p>Create a <code>.env</code> file for local secrets (add to <code>.gitignore</code>):</p>
<pre tabindex="0"><code class="language-sh">&#35; .env&#10;OPENAI_API_KEY=sk-...&#10;GITHUB_WEBHOOK_SECRET=whsec_...&#10;DATABASE_URL=postgres://...&#10;</code></pre>
<p>Access in your agent:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2322.md")
</div>
<h3 id="production-secrets">Production secrets</h3>
<p>Use <code>wrangler secret</code> for production:</p>
<pre tabindex="0"><code class="language-sh">&#35; Add a secret&#10;npx wrangler secret put OPENAI_API_KEY&#10;&#35; Enter value when prompted&#10;&#10;&#35; List secrets&#10;npx wrangler secret list&#10;&#10;&#35; Delete a secret&#10;npx wrangler secret delete OPENAI_API_KEY&#10;</code></pre>
<h3 id="non-secret-variables">Non-secret variables</h3>
<p>For non-sensitive configuration, use <code>vars</code> in the Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2323.md")
</div>
<p>All values must be strings. Parse numbers and booleans in code:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2324.md")
</div>
<h3 id="environment-specific-variables">Environment-specific variables</h3>
<p>Use <code>env</code> sections for different environments (for example, staging, production):</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2325.md")
</div>
<p>Deploy to specific environment:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy --env staging&#10;npx wrangler deploy --env production&#10;</code></pre>
<h2 id="local-development">Local development</h2>
<h3 id="starting-the-dev-server">Starting the dev server</h3>
<p>With Vite (recommended for full stack apps):</p>
<pre tabindex="0"><code class="language-sh">npx vite dev&#10;</code></pre>
<p>Without Vite:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev&#10;</code></pre>
<h3 id="local-state-persistence">Local state persistence</h3>
<p>Durable Object state is persisted locally in <code>.wrangler/state/</code>:</p>
<pre tabindex="0" class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/2326.md")&#10;&#10;&#10;</pre>
<h3 id="clearing-local-state">Clearing local state</h3>
<p>To reset all local Durable Object state:</p>
<pre tabindex="0"><code class="language-sh">rm -rf .wrangler/state&#10;</code></pre>
<p>Or restart with fresh state:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev --persist-to=&quot;&quot;&#10;</code></pre>
<h3 id="inspecting-local-sqlite">Inspecting local SQLite</h3>
<p>You can inspect agent state directly:</p>
<pre tabindex="0"><code class="language-sh">&#35; Find the SQLite file&#10;ls .wrangler/state/v3/d1/&#10;&#10;&#35; Open with sqlite3&#10;sqlite3 .wrangler/state/v3/d1/miniflare-D1DatabaseObject/*.sqlite&#10;</code></pre>
<h2 id="dashboard-setup">Dashboard setup</h2>
<h3 id="automatic-resources">Automatic resources</h3>
<p>When you deploy, Cloudflare automatically creates:</p>
<ul>
<li><strong>Worker</strong> - Your deployed code</li>
<li><strong>Durable Object namespaces</strong> - One per agent class</li>
<li><strong>SQLite storage</strong> - Attached to each namespace</li>
</ul>
<h3 id="viewing-durable-objects">Viewing Durable Objects</h3>
<p>Log in to the Cloudflare dashboard, then go to Durable Objects.</p>
<div class="nb-dash-button"></div>
<p>Here you can:</p>
<ul>
<li>See all Durable Object namespaces</li>
<li>View individual object instances</li>
<li>Inspect storage (keys and values)</li>
<li>Delete objects</li>
</ul>
<h3 id="real-time-logs">Real-time logs</h3>
<p>View live logs from your agents:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler tail&#10;</code></pre>
<p>Or in the dashboard:</p>
<ol>
<li>Go to your Worker.</li>
<li>Select the <strong>Observability</strong> tab.</li>
<li>Enable real-time logs.</li>
</ol>
<p>Filter by:</p>
<ul>
<li>Status (success, error)</li>
<li>Search text</li>
<li>Sampling rate</li>
</ul>
<h2 id="production-deployment">Production deployment</h2>
<h3 id="basic-deploy">Basic deploy</h3>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>This:</p>
<ol>
<li>Bundles your code</li>
<li>Uploads to Cloudflare</li>
<li>Provisions the Agent's Durable Object namespace storage</li>
<li>Makes it live on <code>*.workers.dev</code></li>
</ol>
<h3 id="custom-domain">Custom domain</h3>
<p>Add a route in the Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2327.md")
</div>
<p>Or use a custom domain (simpler):</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2328.md")
</div>
<h3 id="preview-deployments">Preview deployments</h3>
<p>Deploy without affecting production:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy --dry-run    # See what would be uploaded&#10;npx wrangler versions upload     # Upload new version&#10;npx wrangler versions deploy     # Gradually roll out&#10;</code></pre>
<h3 id="rollbacks">Rollbacks</h3>
<p>Roll back to a previous version:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler rollback&#10;</code></pre>
<h2 id="multi-environment-setup">Multi-environment setup</h2>
<h3 id="environment-configuration">Environment configuration</h3>
<p>Define environments in the Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2329.md")
</div>
<h3 id="deploying-to-environments">Deploying to environments</h3>
<pre tabindex="0"><code class="language-sh">&#35; Deploy to staging&#10;npx wrangler deploy --env staging&#10;&#10;&#35; Deploy to production&#10;npx wrangler deploy --env production&#10;&#10;&#35; Set secrets per environment&#10;npx wrangler secret put OPENAI_API_KEY --env staging&#10;npx wrangler secret put OPENAI_API_KEY --env production&#10;</code></pre>
<h3 id="separate-durable-objects">Separate Durable Objects</h3>
<p>Named environments do not inherit Durable Object bindings. Repeat the bindings for each environment, as in the <a href="#multi-environment-setup">multi-environment setup</a>. Each environment gets its own Durable Objects. Staging agents do not share state with production agents.</p>
<p>To explicitly separate:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2330.md")
</div>
<h2 id="agent-class-lifecycle">Agent class lifecycle</h2>
<p>Each Agent maps to a Durable Object class. You manage the lifecycle of those classes (create, rename, delete, transfer) through the <a href="/durable-objects/reference/durable-objects-migrations/"><code>exports</code></a> field of your Wrangler configuration file.</p>
<h3 id="adding-a-new-agent">Adding a new agent</h3>
<p>Declare the new class in the <code>exports</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2331.md")
</div>
<h3 id="renaming-an-agent-class">Renaming an agent class</h3>
<p>Replace the entry for the old name with a <code>renamed</code> tombstone and add a live entry for the new name:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2332.md")
</div>
<p>Also update:</p>
<ol>
<li>The class name in code.</li>
<li>The <code>class_name</code> in bindings.</li>
<li>Export statements.</li>
</ol>
<h3 id="deleting-an-agent-class">Deleting an agent class</h3>
<p>Replace the entry with a <code>deleted</code> tombstone:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2333.md")
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2307.md")
</aside>
<h3 id="class-lifecycle-best-practices">Class lifecycle best practices</h3>
<ol>
<li><strong>Keep <code>exports</code> in sync with your code.</strong> Every Agent class your Worker exports needs an entry.</li>
<li><strong>Use tombstones, not silent removal.</strong> When retiring a class, leave a <code>deleted</code> / <code>renamed</code> / <code>transferred</code> tombstone in <code>exports</code> so Cloudflare reconciles the change explicitly.</li>
<li><strong>Test locally first.</strong> Lifecycle changes apply on <code>wrangler deploy</code>.</li>
<li><strong>Back up production data</strong> before renaming or deleting.</li>
</ol>
<p>Existing Workers using the legacy <code>migrations</code> array continue to work — refer to <a href="/durable-objects/reference/durable-object-class-migrations-legacy/">Durable Object class migrations (legacy)</a> for the legacy reference, or <a href="/durable-objects/reference/durable-objects-migrations/#migrate-from-the-legacy-migrations-flow">Migrate from the legacy <code>migrations</code> flow</a> to move to <code>exports</code>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="no-such-durable-object-class">No such Durable Object class</h3>
<p>The class is missing from <code>exports</code>. Declare the class and its storage:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2334.md")
</div>
<h3 id="cannot-find-module-in-types">Cannot find module in types</h3>
<p>Regenerate types:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler types env.d.ts --include-runtime false&#10;</code></pre>
<h3 id="secrets-not-loading-locally">Secrets not loading locally</h3>
<p>Check that <code>.env</code> exists and contains the variable:</p>
<pre tabindex="0"><code class="language-sh">cat .env&#10;&#35; Should show: MY_SECRET=value&#10;</code></pre>
<h3 id="migration-tag-conflict-legacy-migrations-only">Migration tag conflict (legacy <code>migrations</code> only)</h3>
<p>If your Worker uses the legacy <a href="/durable-objects/reference/durable-object-class-migrations-legacy/"><code>migrations</code></a> array, each entry must have a unique <code>tag</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2335.md")
</div>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2336.md")
</div>
<p>Consider converting to the declarative <a href="/durable-objects/reference/durable-objects-migrations/"><code>exports</code></a> field.</p>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-agents-api-agents-runtime-agents-api"><a href="/agents/runtime/agents-api/">Agents API</a></h3><p>Complete API reference for the Agents SDK.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-routing-agents-runtime-communication-routing"><a href="/agents/runtime/communication/routing/">Routing</a></h3><p>Route requests to your agent instances.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-schedule-tasks-agents-runtime-execution-schedule-tasks"><a href="/agents/runtime/execution/schedule-tasks/">Schedule tasks</a></h3><p>Background processing with delayed and cron-based tasks.</p></div>
