---
cp9:
  canonical: https://developers.cloudflare.com/workers/testing/test-harness/integrations/
  description: Use createTestHarness with Mock Service Worker and Playwright.
  full_title: Integrations · Cloudflare Workers docs
  head_html: <title>Integrations · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use createTestHarness with Mock Service Worker and Playwright."><link rel="canonical" href="https://developers.cloudflare.com/workers/testing/test-harness/integrations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/testing/test-harness/integrations/index.md"><meta property="og:title" content="Integrations · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use createTestHarness with Mock Service Worker and Playwright."><meta property="og:url" content="https://developers.cloudflare.com/workers/testing/test-harness/integrations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/testing/test-harness/integrations/#page","headline":"Integrations \u00b7 Cloudflare Workers docs","description":"Use createTestHarness with Mock Service Worker and Playwright.","url":"https://developers.cloudflare.com/workers/testing/test-harness/integrations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/testing/test-harness/integrations/
  schema: 1
---
<p>You can use <code>createTestHarness()</code> with existing tools in the Node.js ecosystem. The examples on this page show common integration patterns that you can adapt to your test setup.</p>
<h2 id="mock-service-worker">Mock Service Worker</h2>
<p>If your Worker makes outbound <code>fetch()</code> requests, you can use <a href="https://mswjs.io/">Mock Service Worker (MSW)</a> to intercept them and return predictable responses. MSW provides reusable request handlers that can be shared across tests.</p>
<p>For example, you can start MSW before the tests, reject unhandled requests, and reset handlers after each test:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17342.md")
</div>
<h2 id="playwright">Playwright</h2>
<p>If you are building a web application and want to verify user flows in a real browser, use <a href="https://playwright.dev/">Playwright</a> with the test harness. Playwright can navigate pages, interact with the user interface, and verify the behavior of your Workers project end to end.</p>
<p>A Playwright fixture can start a test server with <code>createTestHarness()</code> before browser tests. If you want to mock outbound <code>fetch()</code> requests, you can also use <a href="#mock-service-worker">MSW</a> to intercept them at the same time.</p>
<p>The following fixture sets the Playwright <code>baseURL</code>, exposes MSW and the test harness to tests, and resets storage state after each test.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17343.md")
</div>
