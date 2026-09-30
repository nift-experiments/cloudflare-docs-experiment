---
cp9:
  canonical: https://developers.cloudflare.com/workers/testing/test-harness/configure/
  description: Configure Workers, test values, and lifecycle options for createTestHarness.
  full_title: Configure the test harness · Cloudflare Workers docs
  head_html: <title>Configure the test harness · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Workers, test values, and lifecycle options for createTestHarness."><link rel="canonical" href="https://developers.cloudflare.com/workers/testing/test-harness/configure/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/testing/test-harness/configure/index.md"><meta property="og:title" content="Configure the test harness · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Workers, test values, and lifecycle options for createTestHarness."><meta property="og:url" content="https://developers.cloudflare.com/workers/testing/test-harness/configure/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/testing/test-harness/configure/#page","headline":"Configure the test harness \u00b7 Cloudflare Workers docs","description":"Configure Workers, test values, and lifecycle options for createTestHarness.","url":"https://developers.cloudflare.com/workers/testing/test-harness/configure/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/testing/test-harness/configure/
  schema: 1
---
<p><code>createTestHarness()</code> runs one or more Workers in a single local server. Each Worker can come from a Wrangler project or a Vite project that uses the Cloudflare Vite plugin.</p>
<h2 id="configure-worker-projects">Configure Worker projects</h2>
<p>Point each entry in the <code>workers</code> array to the Wrangler configuration file for a project:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17350.md")
</div>
<p>For Workers built by the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>, run <code>vite build</code> first so tests use the production build output:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx vite build</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx vite build" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn vite build</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn vite build" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm vite build</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm vite build" aria-label="Copy to clipboard">Copy</button></div></div>
<p>The generated Wrangler configuration works like any other <code>configPath</code>. Each Worker is configured independently, so one harness can run both project types:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17351.md")
</div>
<h2 id="select-a-wrangler-environment">Select a Wrangler environment</h2>
<p>By default, the test harness loads the top-level Wrangler configuration. Set <code>env</code> if you want to load a specific environment from the configuration.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17352.md")
</div>
<h2 id="override-variables-and-secrets">Override variables and secrets</h2>
<p>You can override <code>vars</code> and <code>secrets</code> for each Worker in the harness if you want to avoid creating a separate Wrangler environment for testing.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17353.md")
</div>
<h2 id="configure-the-harness-after-setup">Configure the harness after setup</h2>
<p>If part of the Worker configuration depends on the test setup, you can call <code>createTestHarness()</code> without options and configure the harness with <code>server.update()</code> before starting the server.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17354.md")
</div>
<h2 id="reset-the-harness-between-tests">Reset the harness between tests</h2>
<p>When reusing a server across tests, call <code>server.reset()</code> after each test. It recreates local storage and restores Workers to the options used when the current session started.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17355.md")
</div>
<p>After a reset, apply any required schema migrations and seed data again. For examples, refer to <a href="/workers/testing/test-harness/prepare-test-state/">Prepare test state</a>.</p>
<h2 id="print-debug-output-when-tests-fail">Print debug output when tests fail</h2>
<p><code>server.debug()</code> prints the server timeline and captured Workers runtime logs. Call it when a test throws an exception or fails and you need more information to debug it.</p>
<p>The following example uses a cleanup hook from Vitest:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17356.md")
</div>
<h2 id="specify-types-for-worker-handles">Specify types for Worker handles</h2>
<p><code>server.getWorker()</code> accepts types for the Worker environment and module exports. You can define these types manually. But to keep them aligned with your Worker, you can generate the env type from the Wrangler configuration and derive the exports from its source module.</p>
<p>Give each Worker a distinct environment interface so the generated declarations can be used together:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler types ./workers/api/worker-configuration.d.ts --config ./workers/api/wrangler.jsonc --env-interface ApiEnv</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler types ./workers/api/worker-configuration.d.ts --config ./workers/api/wrangler.jsonc --env-interface ApiEnv" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler types ./workers/api/worker-configuration.d.ts --config ./workers/api/wrangler.jsonc --env-interface ApiEnv</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler types ./workers/api/worker-configuration.d.ts --config ./workers/api/wrangler.jsonc --env-interface ApiEnv" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler types ./workers/api/worker-configuration.d.ts --config ./workers/api/wrangler.jsonc --env-interface ApiEnv</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler types ./workers/api/worker-configuration.d.ts --config ./workers/api/wrangler.jsonc --env-interface ApiEnv" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Repeat this command for each Worker and include the generated files in the TypeScript configuration for your tests:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;include&quot;: [&quot;./workers/*/worker-configuration.d.ts&quot;, &quot;./tests/**/*.ts&quot;]&#10;}&#10;</code></pre>
<p>Pass the generated environment interface to <code>server.getWorker()</code>. Use <code>typeof import()</code> to derive the Worker exports from its source module:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17357.md")
</div>
<p>In this example, <code>ApiEnv</code> comes from <code>worker-configuration.d.ts</code>. The module type includes the default export and its RPC methods. Re-run <a href="/workers/languages/typescript/#generate-types"><code>wrangler types</code></a> when the Worker configuration changes.</p>
