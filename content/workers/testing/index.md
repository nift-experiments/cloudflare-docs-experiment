---
cp9:
  canonical: https://developers.cloudflare.com/workers/testing/
  description: Choose testing tools for Cloudflare Workers, including createTestHarness and the Vitest integration.
  full_title: Testing · Cloudflare Workers docs
  head_html: <title>Testing · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Choose testing tools for Cloudflare Workers, including createTestHarness and the Vitest integration."><link rel="canonical" href="https://developers.cloudflare.com/workers/testing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/testing/index.md"><meta property="og:title" content="Testing · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Choose testing tools for Cloudflare Workers, including createTestHarness and the Vitest integration."><meta property="og:url" content="https://developers.cloudflare.com/workers/testing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers/testing/#page","headline":"Testing \u00b7 Cloudflare Workers docs","description":"Choose testing tools for Cloudflare Workers, including createTestHarness and the Vitest integration.","url":"https://developers.cloudflare.com/workers/testing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/testing/
  schema: 1
---
<p>The Workers platform provides complementary tools for testing different parts of your application. For most projects, use the <a href="/workers/testing/vitest-integration/">Workers Vitest integration</a> for unit tests and the <a href="/workers/testing/test-harness/"><code>createTestHarness()</code></a> API for integration tests.</p>
<h2 id="unit-tests">Unit tests</h2>
<p>Use the <a href="/workers/testing/vitest-integration/">Workers Vitest integration</a> for fast feedback while testing individual functions and modules. Tests run inside the Workers runtime, so your test code can access bindings and runtime APIs directly.</p>
<p>The Workers Vitest integration provides:</p>
<ul>
<li>Fast feedback while testing individual functions and modules.</li>
<li>Direct assertions against binding state, such as values written to KV, R2, D1, or Durable Objects.</li>
<li>Direct calls to Durable Objects and other runtime APIs.</li>
</ul>
<p>To set up unit tests, refer to <a href="/workers/testing/vitest-integration/write-your-first-test/">Write your first Vitest test</a>.</p>
<h2 id="integration-tests">Integration tests</h2>
<p>Use the <a href="/workers/testing/test-harness/"><code>createTestHarness()</code></a> API to exercise one or more Workers as a whole and test how they interact with each other and with external services.</p>
<p>The integration test harness provides:</p>
<ul>
<li>Confidence from exercising production Worker builds.</li>
<li>Coverage through configured HTTP routes across Workers.</li>
<li>Compatibility with any Node.js test runner and tools such as Playwright or MSW.</li>
</ul>
<p>To set up integration tests, refer to <a href="/workers/testing/test-harness/get-started/">Get started with the integration test harness</a>.</p>
