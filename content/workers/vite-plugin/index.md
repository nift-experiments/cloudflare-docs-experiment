---
cp9:
  canonical: https://developers.cloudflare.com/workers/vite-plugin/
  description: A full-featured integration between Vite and the Workers runtime
  full_title: Vite plugin · Cloudflare Workers docs
  head_html: <title>Vite plugin · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="A full-featured integration between Vite and the Workers runtime"><link rel="canonical" href="https://developers.cloudflare.com/workers/vite-plugin/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/vite-plugin/index.md"><meta property="og:title" content="Vite plugin · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A full-featured integration between Vite and the Workers runtime"><meta property="og:url" content="https://developers.cloudflare.com/workers/vite-plugin/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers/vite-plugin/#page","headline":"Vite plugin \u00b7 Cloudflare Workers docs","description":"A full-featured integration between Vite and the Workers runtime","url":"https://developers.cloudflare.com/workers/vite-plugin/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/vite-plugin/
  schema: 1
---
<p>The Cloudflare Vite plugin enables a full-featured integration between <a href="https://vite.dev/">Vite</a> and the <a href="/workers/runtime-apis/">Workers runtime</a>.
Your Worker code runs inside <a href="https://github.com/cloudflare/workerd">workerd</a>, matching the production behavior as closely as possible and providing confidence as you develop and deploy your applications.</p>
<h2 id="features">Features</h2>
<ul>
<li>Uses the Vite <a href="https://vite.dev/guide/api-environment">Environment API</a> to integrate Vite with the Workers runtime</li>
<li>Provides direct access to <a href="/workers/runtime-apis/">Workers runtime APIs</a> and <a href="/workers/runtime-apis/bindings/">bindings</a></li>
<li>Builds your front-end assets for deployment to Cloudflare, enabling you to build static sites, SPAs, and full-stack applications</li>
<li>Official support for <a href="https://tanstack.com/start/">TanStack Start</a> and <a href="https://reactrouter.com/">React Router v8</a> with server-side rendering</li>
<li>Leverages Vite's hot module replacement for consistently fast updates</li>
<li>Supports <code>vite preview</code> for previewing your build output in the Workers runtime prior to deployment</li>
</ul>
<h2 id="use-cases">Use cases</h2>
<ul>
<li><a href="https://tanstack.com/start/">TanStack Start</a></li>
<li><a href="https://reactrouter.com/">React Router v8</a></li>
<li>Static sites, such as single-page applications, with or without an integrated backend API</li>
<li>Standalone Workers</li>
<li>Multi-Worker applications</li>
</ul>
<h2 id="get-started">Get started</h2>
<p>To create a new application from a ready-to-go template, refer to the <a href="/workers/framework-guides/web-apps/tanstack-start/">TanStack Start</a>, <a href="/workers/framework-guides/web-apps/react-router/">React Router</a>, <a href="/workers/framework-guides/web-apps/react/">React</a> or <a href="/workers/framework-guides/web-apps/vue/">Vue</a> framework guides.</p>
<p>To create a standalone Worker from scratch, refer to <a href="/workers/vite-plugin/get-started/">Get started</a>.</p>
<p>For a more in-depth look at adapting an existing Vite project and an introduction to key concepts, refer to the <a href="/workers/vite-plugin/tutorial/">Tutorial</a>.</p>
