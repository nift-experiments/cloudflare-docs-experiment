---
cp9:
  canonical: https://developers.cloudflare.com/d1/examples/d1-and-sveltekit/
  description: Query a D1 database from a SvelteKit application.
  full_title: Query D1 from SvelteKit · Cloudflare D1 docs
  head_html: <title>Query D1 from SvelteKit · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Query a D1 database from a SvelteKit application."><link rel="canonical" href="https://developers.cloudflare.com/d1/examples/d1-and-sveltekit/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/examples/d1-and-sveltekit/index.md"><meta property="og:title" content="Query D1 from SvelteKit · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Query a D1 database from a SvelteKit application."><meta property="og:url" content="https://developers.cloudflare.com/d1/examples/d1-and-sveltekit/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="D1"><meta name="pcx_tags" content="SvelteKit,Svelte"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/examples/d1-and-sveltekit/#page","headline":"Query D1 from SvelteKit \u00b7 Cloudflare D1 docs","description":"Query a D1 database from a SvelteKit application.","url":"https://developers.cloudflare.com/d1/examples/d1-and-sveltekit/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SvelteKit","Svelte"]}</script>
  markdown: true
  noindex: false
  route: /d1/examples/d1-and-sveltekit/
  schema: 1
---
<p class="article-summary">Query a D1 database from a SvelteKit application.</p>
<p><a href="https://kit.svelte.dev/">SvelteKit</a> is a full-stack framework that combines the Svelte front-end framework with Vite for server-side capabilities and rendering. You can query D1 from SvelteKit by configuring a <a href="https://kit.svelte.dev/docs/routing#server">server endpoint</a> with a binding to your D1 database(s).</p>
<p>To set up a new SvelteKit site on Cloudflare Pages that can query D1:</p>
<ol>
<li><strong>Refer to <a href="/pages/framework-guides/deploy-a-svelte-kit-site/">the SvelteKit guide</a> and Svelte's <a href="https://kit.svelte.dev/docs/adapter-cloudflare">Cloudflare adapter</a></strong>.</li>
<li>Install the Cloudflare adapter within your SvelteKit project: <code>npm i -D @sveltejs/adapter-cloudflare</code>.</li>
<li>Bind a D1 database <a href="/pages/functions/bindings/#d1-databases">to your Pages Function</a>.</li>
<li>Pass the <code>--d1 BINDING_NAME=DATABASE_ID</code> flag to <code>wrangler dev</code> when developing locally. <code>BINDING_NAME</code> should match what call in your code, and <code>DATABASE_ID</code> should match the <code>database_id</code> defined in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>: for example, <code>--d1 DB=xxxx-xxxx-xxxx-xxxx-xxxx</code>.</li>
</ol>
<p>The following example shows you how to create a server endpoint configured to query D1.</p>
<ul>
<li>Bindings are available on the <code>platform</code> parameter passed to each endpoint, via <code>platform.env.BINDING_NAME</code>.</li>
<li>With SvelteKit's <a href="https://kit.svelte.dev/docs/routing">file-based routing</a>, the server endpoint defined in <code>src/routes/api/users/+server.ts</code> is available at <code>/api/users</code> within your SvelteKit app.</li>
</ul>
<p>The example also shows you how to configure both your app-wide types within <code>src/app.d.ts</code> to recognize your <code>D1Database</code> binding, import the <code>@sveltejs/adapter-cloudflare</code> adapter into <code>svelte.config.js</code>, and configure it to apply to all of your routes.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7359.md")
</div></div>
