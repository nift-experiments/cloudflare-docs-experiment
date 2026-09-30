---
cp9:
  canonical: https://developers.cloudflare.com/d1/examples/d1-and-remix/
  description: Query your D1 database from a Remix application.
  full_title: Query D1 from Remix · Cloudflare D1 docs
  head_html: <title>Query D1 from Remix · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Query your D1 database from a Remix application."><link rel="canonical" href="https://developers.cloudflare.com/d1/examples/d1-and-remix/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/examples/d1-and-remix/index.md"><meta property="og:title" content="Query D1 from Remix · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Query your D1 database from a Remix application."><meta property="og:url" content="https://developers.cloudflare.com/d1/examples/d1-and-remix/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="D1"><meta name="pcx_tags" content="Remix"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/examples/d1-and-remix/#page","headline":"Query D1 from Remix \u00b7 Cloudflare D1 docs","description":"Query your D1 database from a Remix application.","url":"https://developers.cloudflare.com/d1/examples/d1-and-remix/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Remix"]}</script>
  markdown: true
  noindex: false
  route: /d1/examples/d1-and-remix/
  schema: 1
---
<p class="article-summary">Query your D1 database from a Remix application.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7360.md")
</aside>
<p>Remix is a full-stack web framework that operates on both client and server. You can query your D1 database(s) from Remix using Remix's <a href="https://remix.run/docs/en/main/guides/data-loading">data loading</a> API with the <a href="https://remix.run/docs/en/main/hooks/use-loader-data"><code>useLoaderData</code></a> hook.</p>
<p>To set up a new Remix site on Cloudflare Pages that can query D1:</p>
<ol>
<li><strong>Refer to <a href="/pages/framework-guides/deploy-a-remix-site/">the Remix guide</a></strong>.</li>
<li>Bind a D1 database to your <a href="/pages/functions/bindings/#d1-databases">Pages Function</a>.</li>
<li>Pass the <code>--d1 BINDING_NAME=DATABASE_ID</code> flag to <code>wrangler dev</code> when developing locally. <code>BINDING_NAME</code> should match what call in your code, and <code>DATABASE_ID</code> should match the <code>database_id</code> defined in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>: for example, <code>--d1 DB=xxxx-xxxx-xxxx-xxxx-xxxx</code>.</li>
</ol>
<p>The following example shows you how to define a Remix <a href="https://remix.run/docs/en/main/route/loader"><code>loader</code></a> that has a binding to a D1 database.</p>
<ul>
<li>Bindings are passed through on the <code>context.cloudflare.env</code> parameter passed to a <code>LoaderFunction</code>.</li>
<li>If you configured a <a href="/pages/functions/bindings/#d1-databases">binding</a> named <code>DB</code>, then you would access <a href="/d1/worker-api/prepared-statements/">D1 Workers Binding API</a> methods via <code>context.cloudflare.env.DB</code>.</li>
</ul>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7362.md")
</div></div>
