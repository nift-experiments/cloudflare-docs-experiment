---
cp9:
  canonical: https://developers.cloudflare.com/workers/testing/test-harness/
  description: Write integration tests for Cloudflare Workers with the createTestHarness API in Wrangler.
  full_title: Integration test harness · Cloudflare Workers docs
  head_html: <title>Integration test harness · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Write integration tests for Cloudflare Workers with the createTestHarness API in Wrangler."><link rel="canonical" href="https://developers.cloudflare.com/workers/testing/test-harness/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/testing/test-harness/index.md"><meta property="og:title" content="Integration test harness · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Write integration tests for Cloudflare Workers with the createTestHarness API in Wrangler."><meta property="og:url" content="https://developers.cloudflare.com/workers/testing/test-harness/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers/testing/test-harness/#page","headline":"Integration test harness \u00b7 Cloudflare Workers docs","description":"Write integration tests for Cloudflare Workers with the createTestHarness API in Wrangler.","url":"https://developers.cloudflare.com/workers/testing/test-harness/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/testing/test-harness/
  schema: 1
---
<p><a href="/workers/wrangler/api/#createtestharness"><code>createTestHarness()</code></a> is a Wrangler API for integration testing from any Node.js test runner. It runs one or more Workers from <a href="/workers/wrangler/">Wrangler</a> projects or Vite projects that use the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
<p><a class="nb-link-button" href="/workers/testing/test-harness/get-started/">Get started</a>
<a class="nb-link-button" href="https://github.com/cloudflare/workers-sdk/tree/main/fixtures/create-test-harness-example">View complete example</a></p>
<h2 id="features">Features</h2>
<ul>
<li>Runs production build output from Wrangler or the Cloudflare Vite plugin</li>
<li>Dispatches requests and events to one or more Workers</li>
<li>Provides access to bindings and local storage from tests</li>
<li>Captures logs and diagnostic output from the Workers runtime</li>
</ul>
<h2 id="guides">Guides</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/17346.md")
</div>
