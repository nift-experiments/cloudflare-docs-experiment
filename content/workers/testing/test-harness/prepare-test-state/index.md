---
cp9:
  canonical: https://developers.cloudflare.com/workers/testing/test-harness/prepare-test-state/
  description: Seed local storage and replace dependencies in createTestHarness tests.
  full_title: Prepare test state · Cloudflare Workers docs
  head_html: <title>Prepare test state · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Seed local storage and replace dependencies in createTestHarness tests."><link rel="canonical" href="https://developers.cloudflare.com/workers/testing/test-harness/prepare-test-state/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/testing/test-harness/prepare-test-state/index.md"><meta property="og:title" content="Prepare test state · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Seed local storage and replace dependencies in createTestHarness tests."><meta property="og:url" content="https://developers.cloudflare.com/workers/testing/test-harness/prepare-test-state/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/testing/test-harness/prepare-test-state/#page","headline":"Prepare test state \u00b7 Cloudflare Workers docs","description":"Seed local storage and replace dependencies in createTestHarness tests.","url":"https://developers.cloudflare.com/workers/testing/test-harness/prepare-test-state/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/testing/test-harness/prepare-test-state/
  schema: 1
---
<p>An integration test may need data in local storage before it runs. It may also depend on external services that you do not want to call during the test. Use the test harness to prepare this state and replace those dependencies.</p>
<h2 id="access-configured-bindings">Access configured bindings</h2>
<p><code>worker.getEnv()</code> returns the variables, secrets, and bindings configured for a Worker. You can <a href="/workers/testing/test-harness/configure/#specify-types-for-worker-handles">specify types</a> for <code>server.getWorker()</code> so these values are typed. Then use the returned storage bindings to seed data directly from a test:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17332.md")
</div>
<h2 id="apply-d1-migrations">Apply D1 migrations</h2>
<p>Use <code>worker.applyD1Migrations(bindingName)</code> to read the migration settings for a D1 binding from the Wrangler configuration. It uses the configured <code>migrations_dir</code> and <code>migrations_pattern</code>. Without these options, it reads <code>.sql</code> files from the <code>migrations</code> directory relative to the configuration file.</p>
<p>Call it after storage is reset to apply migrations that have not already run. Then access the database with <code>worker.getEnv()</code> and seed the required rows.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17333.md")
</div>
<h2 id="prepare-durable-object-storage">Prepare Durable Object storage</h2>
<p><code>worker.getDurableObjectStorage()</code> gives you access to the storage of a SQLite-backed Durable Object instance. Pass its binding name or exported class name. Then select the instance by name or ID.</p>
<p>The returned handle executes SQL inside the Durable Object. Use it to seed an instance before a test or inspect its state after the Worker runs.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17334.md")
</div>
<h2 id="mock-outbound-requests">Mock outbound requests</h2>
<p>The test harness proxies outbound <code>fetch()</code> requests from your Workers through the <code>globalThis.fetch()</code> function in your Node environment. This allows you to intercept these requests and return a predictable response in your tests.</p>
<p>Here is an example using <code>vi.spyOn()</code> to mock a single request. But you can also use <a href="/workers/testing/test-harness/integrations/#mock-service-worker">Mock Service Worker (MSW)</a> to intercept these requests based on your preferences.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17335.md")
</div>
<h2 id="mock-bindings-with-test-workers">Mock bindings with test Workers</h2>
<p>Use <code>bindingOverrides</code> when you want to control the behavior of a binding. It routes the binding to a test Worker running inside the harness. For example, a test Worker can replace the Browser Rendering binding and return a known screenshot without starting a browser.</p>
<p>The test Worker can also expose JSRPC methods that configure its behavior. Use <code>worker.getExport()</code> to access the default export from your test.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17336.md")
</div>
