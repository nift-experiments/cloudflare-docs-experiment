---
cp9:
  canonical: https://developers.cloudflare.com/workers/static-assets/routing/worker-script/
  description: How the presence of a Worker script influences static asset routing and the related configuration options.
  full_title: Worker script · Cloudflare Workers docs
  head_html: <title>Worker script · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="How the presence of a Worker script influences static asset routing and the related configuration options."><link rel="canonical" href="https://developers.cloudflare.com/workers/static-assets/routing/worker-script/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/static-assets/routing/worker-script/index.md"><meta property="og:title" content="Worker script · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How the presence of a Worker script influences static asset routing and the related configuration options."><meta property="og:url" content="https://developers.cloudflare.com/workers/static-assets/routing/worker-script/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/static-assets/routing/worker-script/#page","headline":"Worker script \u00b7 Cloudflare Workers docs","description":"How the presence of a Worker script influences static asset routing and the related configuration options.","url":"https://developers.cloudflare.com/workers/static-assets/routing/worker-script/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/static-assets/routing/worker-script/
  schema: 1
---
<p>If you have both static assets and a Worker script configured, Cloudflare will first attempt to serve static assets if one matches the incoming request. You can read more about how we match assets in the <a href="/workers/static-assets/routing/advanced/html-handling/">HTML handling docs</a>.</p>
<p>If an appropriate static asset if not found, Cloudflare will invoke your Worker script.</p>
<p>This allows you to easily combine together these two features to create powerful applications (e.g. a <a href="/workers/static-assets/routing/full-stack-application/">full-stack application</a>, or a <a href="/workers/static-assets/routing/single-page-application/">Single Page Application (SPA)</a> or <a href="/workers/static-assets/routing/static-site-generation/">Static Site Generation (SSG) application</a> with an API).</p>
<h2 id="cloudflare-access-context">Cloudflare Access context</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17270.md")
</aside>
<h2 id="run-your-worker-script-first">Run your Worker script first</h2>
<p>You can configure the <a href="/workers/static-assets/binding/#run_worker_first"><code>assets.run_worker_first</code> setting</a> to control when your Worker script runs relative to static asset serving. This gives you more control over exactly how and when those assets are served and can be used to implement &quot;middleware&quot; for requests.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17269.md")
</aside>
<h3 id="run-worker-before-each-request">Run Worker before each request</h3>
<p>If you need to always run your Worker script before serving static assets (for example, you wish to log requests, perform some authentication checks, use <a href="/workers/runtime-apis/html-rewriter/">HTMLRewriter</a>, or otherwise transform assets before serving), set <code>run_worker_first</code> to <code>true</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17271.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17272.md")
</div>
<h3 id="run-worker-first-for-selective-paths">Run Worker first for selective paths</h3>
<p>You can also configure selective Worker-first routing using an array of route patterns, often paired with the <a href="/workers/static-assets/routing/single-page-application/#advanced-routing-control"><code>single-page-application</code> setting</a>. This allows you to run the Worker first only for specific routes while letting other requests follow the default asset-first behavior:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17273.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17274.md")
</div>
