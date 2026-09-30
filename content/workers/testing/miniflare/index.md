---
cp9:
  canonical: https://developers.cloudflare.com/workers/testing/miniflare/
  description: Simulate and test Cloudflare Workers locally with Miniflare, a fully-local development simulator.
  full_title: Miniflare · Cloudflare Workers docs
  head_html: <title>Miniflare · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Simulate and test Cloudflare Workers locally with Miniflare, a fully-local development simulator."><link rel="canonical" href="https://developers.cloudflare.com/workers/testing/miniflare/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/testing/miniflare/index.md"><meta property="og:title" content="Miniflare · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Simulate and test Cloudflare Workers locally with Miniflare, a fully-local development simulator."><meta property="og:url" content="https://developers.cloudflare.com/workers/testing/miniflare/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers/testing/miniflare/#page","headline":"Miniflare \u00b7 Cloudflare Workers docs","description":"Simulate and test Cloudflare Workers locally with Miniflare, a fully-local development simulator.","url":"https://developers.cloudflare.com/workers/testing/miniflare/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/testing/miniflare/
  schema: 1
---
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17361.md")
</aside>
<p><strong>Miniflare</strong> is a simulator for developing and testing
<a href="https://workers.cloudflare.com/"><strong>Cloudflare Workers</strong></a>. It's written in
TypeScript, and runs your code in a sandbox implementing Workers' runtime APIs.</p>
<ul>
<li>🎉 <strong>Fun:</strong> develop Workers easily with detailed logging, file watching and
pretty error pages supporting source maps.</li>
<li>🔋 <strong>Full-featured:</strong> supports most Workers features, including KV, Durable
Objects, WebSockets, modules and more.</li>
<li>⚡ <strong>Fully-local:</strong> test and develop Workers without an Internet connection.
Reload code on change quickly.</li>
</ul>
<p><a class="nb-link-button" href="/workers/testing/miniflare/get-started">Get Started</a>
<a class="nb-link-button" href="https://github.com/cloudflare/workers-sdk/tree/main/packages/miniflare">GitHub</a>
<a class="nb-link-button" href="https://npmjs.com/package/miniflare">NPM</a></p>
<hr />
<p>These docs primarily cover Miniflare specific things. For more information on
runtime APIs, refer to the
<a href="/workers">Cloudflare Workers docs</a>.</p>
<p>If you find something that doesn't behave as it does in the production Workers
environment (and this difference isn't documented), or something's wrong in
these docs, please
<a href="https://github.com/cloudflare/workers-sdk/issues/new/choose">open a GitHub issue</a>.</p>
<ul class="directory-listing"><li><a href="/workers/testing/miniflare/get-started/">Get Started</a><p>Install and configure the Miniflare API to dispatch events and test Cloudflare Workers locally.</p></li><li><a href="/workers/testing/miniflare/writing-tests/">Writing tests</a><p>Write integration tests against Workers using Miniflare.</p></li><li><a href="/workers/testing/miniflare/core/">Core</a><p>Core Miniflare features for testing Cloudflare Workers, including fetch events and compatibility settings.</p></li><li><a href="/workers/testing/miniflare/developing/">Developing</a><p>Development tools for Miniflare, including debugger support and live reload for Cloudflare Workers.</p></li><li><a href="/workers/testing/miniflare/migrations/">Migrations</a><p>Review migration guides for specific versions of Miniflare.</p></li><li><a href="/workers/testing/miniflare/storage/">Storage</a><p>Configure and manage local storage simulators in Miniflare for Workers bindings like KV, R2, and D1.</p></li></ul>
