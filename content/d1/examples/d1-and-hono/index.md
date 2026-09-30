---
cp9:
  canonical: https://developers.cloudflare.com/d1/examples/d1-and-hono/
  description: Query D1 from the Hono web framework
  full_title: Query D1 from Hono · Cloudflare D1 docs
  head_html: <title>Query D1 from Hono · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Query D1 from the Hono web framework"><link rel="canonical" href="https://developers.cloudflare.com/d1/examples/d1-and-hono/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/examples/d1-and-hono/index.md"><meta property="og:title" content="Query D1 from Hono · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Query D1 from the Hono web framework"><meta property="og:url" content="https://developers.cloudflare.com/d1/examples/d1-and-hono/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="D1"><meta name="pcx_tags" content="Hono"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/examples/d1-and-hono/#page","headline":"Query D1 from Hono \u00b7 Cloudflare D1 docs","description":"Query D1 from the Hono web framework","url":"https://developers.cloudflare.com/d1/examples/d1-and-hono/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Hono"]}</script>
  markdown: true
  noindex: false
  route: /d1/examples/d1-and-hono/
  schema: 1
---
<p class="article-summary">Query D1 from the Hono web framework</p>
<p>Hono is a fast web framework for building API-first applications, and it includes first-class support for both <a href="/workers/">Workers</a> and <a href="/pages/">Pages</a>.</p>
<p>When using Workers:</p>
<ul>
<li>Ensure you have configured your <a href="/d1/get-started/#3-bind-your-worker-to-your-d1-database">Wrangler configuration file</a> to bind your D1 database to your Worker.</li>
<li>You can access your D1 databases via Hono's <a href="https://hono.dev/api/context"><code>Context</code></a> parameter: <a href="https://hono.dev/getting-started/cloudflare-workers#bindings">bindings</a> are exposed on <code>context.env</code>. If you configured a <a href="/pages/functions/bindings/#d1-databases">binding</a> named <code>DB</code>, then you would access <a href="/d1/worker-api/prepared-statements/">D1 Workers Binding API</a> methods via <code>c.env.DB</code>.</li>
<li>Refer to the Hono documentation for <a href="https://hono.dev/getting-started/cloudflare-workers">Cloudflare Workers</a>.</li>
</ul>
<p>If you are using <a href="/pages/functions/">Pages Functions</a>:</p>
<ol>
<li>Bind a D1 database to your <a href="/pages/functions/bindings/#d1-databases">Pages Function</a>.</li>
<li>Pass the <code>--d1 BINDING_NAME=DATABASE_ID</code> flag to <code>wrangler dev</code> when developing locally. <code>BINDING_NAME</code> should match what call in your code, and <code>DATABASE_ID</code> should match the <code>database_id</code> defined in your Wrangler configuration file: for example, <code>--d1 DB=xxxx-xxxx-xxxx-xxxx-xxxx</code>.</li>
<li>Refer to the Hono guide for <a href="https://hono.dev/getting-started/cloudflare-pages">Cloudflare Pages</a>.</li>
</ol>
<p>The following examples show how to access a D1 database bound to <code>DB</code> from both a Workers script and a Pages Function:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7365.md")
</div></div>
