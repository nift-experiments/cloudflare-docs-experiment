---
cp9:
  canonical: https://developers.cloudflare.com/workers/testing/test-harness/get-started/
  description: Write your first integration test for a Cloudflare Worker with createTestHarness.
  full_title: Get started · Cloudflare Workers docs
  head_html: <title>Get started · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Write your first integration test for a Cloudflare Worker with createTestHarness."><link rel="canonical" href="https://developers.cloudflare.com/workers/testing/test-harness/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/testing/test-harness/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Write your first integration test for a Cloudflare Worker with createTestHarness."><meta property="og:url" content="https://developers.cloudflare.com/workers/testing/test-harness/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/testing/test-harness/get-started/#page","headline":"Get started \u00b7 Cloudflare Workers docs","description":"Write your first integration test for a Cloudflare Worker with createTestHarness.","url":"https://developers.cloudflare.com/workers/testing/test-harness/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/testing/test-harness/get-started/
  schema: 1
---
<p>This guide shows how to write a basic integration test for a Worker with <code>createTestHarness()</code>. The example uses Vitest as the test runner and exercises a Worker built with Wrangler.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need:</p>
<ul>
<li>A Worker project with a <a href="/workers/wrangler/configuration/">Wrangler configuration file</a></li>
<li>A Node.js test runner such as <a href="https://vitest.dev/">Vitest</a></li>
<li><code>wrangler</code> installed as a development dependency</li>
</ul>
<h2 id="create-a-test-harness">Create a test harness</h2>
<p>Import <code>createTestHarness()</code> from <code>wrangler</code>. Point the test harness at your Worker configuration file.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17347.md")
</div>
<h2 id="manage-the-test-harness-lifecycle">Manage the test harness lifecycle</h2>
<p>For simplicity, we will reuse a single server for the test suite and reset it after each test. You can also start a new server for each test if the tests do not share the same configuration.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17348.md")
</div>
<h2 id="write-your-first-test">Write your first test</h2>
<p>Use the <a href="/workers/testing/test-harness/interact-with-workers/">helpers</a> provided by the test harness to interact with the Worker and assert its behavior. For example, you can call <code>server.fetch()</code> to send a request to the Worker and assert against its response.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17349.md")
</div>
