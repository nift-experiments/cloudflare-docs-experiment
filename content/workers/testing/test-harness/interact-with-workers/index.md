---
cp9:
  canonical: https://developers.cloudflare.com/workers/testing/test-harness/interact-with-workers/
  description: Test routes, dispatch events, control Workflows, and assert logged behavior with createTestHarness.
  full_title: Interact with Workers · Cloudflare Workers docs
  head_html: <title>Interact with Workers · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Test routes, dispatch events, control Workflows, and assert logged behavior with createTestHarness."><link rel="canonical" href="https://developers.cloudflare.com/workers/testing/test-harness/interact-with-workers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/testing/test-harness/interact-with-workers/index.md"><meta property="og:title" content="Interact with Workers · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Test routes, dispatch events, control Workflows, and assert logged behavior with createTestHarness."><meta property="og:url" content="https://developers.cloudflare.com/workers/testing/test-harness/interact-with-workers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/testing/test-harness/interact-with-workers/#page","headline":"Interact with Workers \u00b7 Cloudflare Workers docs","description":"Test routes, dispatch events, control Workflows, and assert logged behavior with createTestHarness.","url":"https://developers.cloudflare.com/workers/testing/test-harness/interact-with-workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/testing/test-harness/interact-with-workers/
  schema: 1
---
<p>Use the test harness to send requests through configured routes or target a specific Worker directly. You can also dispatch events like scheduled events.</p>
<h2 id="test-route-dispatch-across-workers">Test route dispatch across Workers</h2>
<p>When a test harness runs multiple Workers, add each Worker to the <code>workers</code> array. The first Worker is the primary Worker. <code>server.fetch()</code> sends relative URLs to the primary Worker and matches absolute URLs against configured routes. If no route matches, it falls back to the primary Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17337.md")
</div>
<h2 id="interact-with-a-specific-worker">Interact with a specific Worker</h2>
<p>Route dispatch tests the application boundary, but some tests might want to target one Worker or trigger other event handlers. Use <code>server.getWorker(name)</code> to bypass route matching and get a handle for that Worker.</p>
<p>You can then use this Worker handle to send requests directly or dispatch other events, such as <code>scheduled()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17338.md")
</div>
<h2 id="assert-logged-behavior">Assert logged behavior</h2>
<p>The test harness captures logs from the Workers runtime. To assert that a Worker logged a specific message, use <code>server.getLogs()</code> to retrieve the log entries.</p>
<p>Captured logs are reset when you call <code>server.reset()</code>. You can also call <code>server.clearLogs()</code> to isolate logs before and after a specific action:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17339.md")
</div>
<h2 id="inspect-and-control-workflow-execution">Inspect and control Workflow execution</h2>
<p>If your Worker starts a Workflow, you can use <code>worker.introspectWorkflow(bindingName)</code> to control new instances and inspect their state.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17340.md")
</div>
<p>If the test already knows the instance ID, you can also introspect that instance directly with <code>worker.introspectWorkflowInstance(bindingName, instanceId)</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17341.md")
</div>
