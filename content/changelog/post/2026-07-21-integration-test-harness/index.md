---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-07-21-integration-test-harness/
  description: New updates and improvements at Cloudflare.
  full_title: Run integration tests against your Worker's production build · Changelog
  head_html: <title>Run integration tests against your Worker&#x27;s production build · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-07-21-integration-test-harness/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Run integration tests against your Worker&#x27;s production build · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-07-21-integration-test-harness/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-21-integration-test-harness/#page","headline":"Run integration tests against your Worker's production build \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-07-21-integration-test-harness/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-07-21-integration-test-harness/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 27, 2026</time><h2 id="post-title">Run integration tests against your Worker's production build</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now provides <code>createTestHarness()</code>, an API for running integration tests against Workers built with <a href="/workers/testing/test-harness/configure/#configure-worker-projects">Wrangler or the Cloudflare Vite plugin</a> from any Node.js test runner.</p>
<p>The test harness starts a local Worker server with <a href="/workers/wrangler/api/#createtestharness">helpers for dispatching requests, resetting storage, and inspecting runtime logs</a>.</p>
<p>This is useful for tests that need to:</p>
<ul>
<li><a href="/workers/testing/test-harness/interact-with-workers/#test-route-dispatch-across-workers">Route requests across multiple Workers</a></li>
<li><a href="/workers/testing/test-harness/integrations/#mock-service-worker">Mock outbound <code>fetch()</code> requests</a> with Node.js request mocking libraries such as <a href="https://mswjs.io/">MSW</a></li>
<li><a href="/workers/testing/test-harness/integrations/#playwright">Run Playwright tests against a Worker</a></li>
</ul>
<p>For example, this test starts two Workers and mocks an upstream API:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17807.md")</div>
<p>Cloudflare now recommends <code>createTestHarness()</code> for integration tests instead of <a href="/workers/testing/unstable_startworker/"><code>unstable_startWorker()</code></a> or <a href="/workers/wrangler/api/#unstable_dev"><code>unstable_dev()</code></a>. To start a development server programmatically, use the Vite <a href="https://vite.dev/guide/api-javascript.html#createserver"><code>createServer()</code></a> API with the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
<p>For more information about <code>createTestHarness()</code>, refer to the <a href="/workers/testing/test-harness/">Integration test harness guide</a>.</p>
</div></article></div>
