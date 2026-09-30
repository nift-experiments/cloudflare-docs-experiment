---
cp9:
  canonical: https://developers.cloudflare.com/workers/testing/vitest-integration/write-your-first-test/
  description: Write tests against Workers using Vitest
  full_title: Write your first test · Cloudflare Workers docs
  head_html: <title>Write your first test · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Write tests against Workers using Vitest"><link rel="canonical" href="https://developers.cloudflare.com/workers/testing/vitest-integration/write-your-first-test/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/testing/vitest-integration/write-your-first-test/index.md"><meta property="og:title" content="Write your first test · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Write tests against Workers using Vitest"><meta property="og:url" content="https://developers.cloudflare.com/workers/testing/vitest-integration/write-your-first-test/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/testing/vitest-integration/write-your-first-test/#page","headline":"Write your first test \u00b7 Cloudflare Workers docs","description":"Write tests against Workers using Vitest","url":"https://developers.cloudflare.com/workers/testing/vitest-integration/write-your-first-test/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/testing/vitest-integration/write-your-first-test/
  schema: 1
---
<p>This guide explains how to get started with the <code>@cloudflare/vitest-plugin</code> package. For more complex examples of testing with <code>@cloudflare/vitest-plugin</code>, refer to <a href="/workers/testing/vitest-integration/recipes/">Recipes</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>First, make sure that:</p>
<ul>
<li>Your <a href="/workers/configuration/compatibility-dates/">compatibility date</a> is set to <code>2022-10-31</code> or later.</li>
<li>Your Worker using the ES modules format (if not, refer to the <a href="/workers/reference/migrate-to-module-workers/">migrate to the ES modules format</a> guide).</li>
<li>Vitest and <code>@cloudflare/vitest-plugin</code> are installed in your project as dev dependencies</li>
</ul>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i -D vitest@^4.1.0 @cloudflare/vitest-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i -D vitest@^4.1.0 @cloudflare/vitest-plugin" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add -D vitest@^4.1.0 @cloudflare/vitest-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add -D vitest@^4.1.0 @cloudflare/vitest-plugin" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add -D vitest@^4.1.0 @cloudflare/vitest-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add -D vitest@^4.1.0 @cloudflare/vitest-plugin" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add -d vitest@^4.1.0 @cloudflare/vitest-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add -d vitest@^4.1.0 @cloudflare/vitest-plugin" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17316.md")
</aside>
<h2 id="define-vitest-configuration">Define Vitest configuration</h2>
<p>In your <code>vitest.config.ts</code> file, use the <code>cloudflareTest()</code> plugin to configure the Workers Vitest integration.</p>
<p>You can use your Worker configuration from your <a href="/workers/wrangler/configuration/">Wrangler config file</a> by specifying it with <code>wrangler.configPath</code>.</p>
<pre tabindex="0"><code class="language-ts">import { cloudflareTest } from &quot;@cloudflare/vitest-plugin&quot;;&#10;import { defineConfig } from &quot;vitest/config&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflareTest({&#10;			wrangler: { configPath: &quot;./wrangler.jsonc&quot; },&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p>You can also override or define additional configuration using the <code>miniflare</code> key. This takes precedence over values set in via your Wrangler config.</p>
<p>For example, this configuration would add a KV namespace <code>TEST_NAMESPACE</code> that was only accessed and modified in tests.</p>
<pre tabindex="0"><code class="language-js">export default defineConfig({&#10;	plugins: [&#10;		cloudflareTest({&#10;			wrangler: { configPath: &quot;./wrangler.jsonc&quot; },&#10;			miniflare: {&#10;				kvNamespaces: [&quot;TEST_NAMESPACE&quot;],&#10;			},&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<pre tabindex="0"><code>For a full list of available Miniflare options, refer to the [Miniflare `WorkersOptions` API documentation](https://github.com/cloudflare/workers-sdk/tree/main/packages/miniflare#interface-workeroptions).&#10;</code></pre>
<p>For a full list of available configuration options, refer to <a href="/workers/testing/vitest-integration/configuration/">Configuration</a>.</p>
<h2 id="define-types">Define types</h2>
<p>If you are not using Typescript, you can skip this section.</p>
<p>First make sure you have run <a href="/workers/wrangler/commands/"><code>wrangler types</code></a>, which generates <a href="/workers/languages/typescript/">types for the Cloudflare Workers runtime</a> and an <code>Env</code> type based on your Worker's bindings.</p>
<p>Then add a <code>tsconfig.json</code> in your tests folder and add <code>&quot;@cloudflare/vitest-plugin&quot;</code> to your types array to define types for <code>cloudflare:test</code>.
You should also add the output of <code>wrangler types</code> to the <code>include</code> array so that the types for the Cloudflare Workers runtime are available.</p>
<details class="nb-details"><summary>Example test/tsconfig.json</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17317.md")
</div></details>
<h2 id="writing-tests">Writing tests</h2>
<p>We will use this simple Worker as an example. It returns a 404 response for the <code>/404</code> path and <code>&quot;Hello World!&quot;</code> for all other paths.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17318.md")
</div>
<h3 id="unit-tests">Unit tests</h3>
<p>By importing the Worker we can write a unit test for its <code>fetch</code> handler.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17319.md")
</div>
<h3 id="integration-tests">Integration tests</h3>
<p>You can use the <code>exports</code> object provided by <code>cloudflare:workers</code> to write an integration test. <code>exports.default.fetch()</code> calls the default export handler defined in the main Worker.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17320.md")
</div>
<p>When using <code>exports.default.fetch()</code> for integration tests, your Worker code runs in the same context as the test runner. This means you can use global mocks to control your Worker, but also means your Worker uses the subtly different module resolution behavior provided by Vite.
Usually this is not a problem, but to run your Worker in a fresh environment that is as close to production as possible, you can use an auxiliary Worker. Refer to <a href="https://github.com/cloudflare/workers-sdk/blob/main/fixtures/vitest-plugin-examples/basics-integration-auxiliary/vitest.config.ts">this example</a> for how to set up integration tests using auxiliary Workers. However, using auxiliary Workers comes with <a href="/workers/testing/vitest-integration/configuration/#workerspooloptions">limitations</a> that you should be aware of.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>For more complex examples of testing with <code>@cloudflare/vitest-plugin</code>, refer to <a href="/workers/testing/vitest-integration/recipes/">Recipes</a>.</li>
<li><a href="/workers/testing/vitest-integration/configuration/">Configuration API reference</a></li>
<li><a href="/workers/testing/vitest-integration/test-apis/">Test APIs reference</a></li>
</ul>
