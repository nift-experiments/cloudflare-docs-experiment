---
cp9:
  canonical: https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-starter/
  description: A starter template for deploying a Worker that loads and runs Dynamic Workers.
  full_title: Dynamic Workers Starter · Cloudflare Dynamic Workers docs
  head_html: <title>Dynamic Workers Starter · Cloudflare Dynamic Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="A starter template for deploying a Worker that loads and runs Dynamic Workers."><link rel="canonical" href="https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-starter/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-starter/index.md"><meta property="og:title" content="Dynamic Workers Starter · Cloudflare Dynamic Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A starter template for deploying a Worker that loads and runs Dynamic Workers."><meta property="og:url" content="https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-starter/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Dynamic Workers"><meta name="algolia_product_filter" content="Dynamic Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Dynamic Workers"><meta name="pcx_tags" content="JavaScript,TypeScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-starter/#page","headline":"Dynamic Workers Starter \u00b7 Cloudflare Dynamic Workers docs","description":"A starter template for deploying a Worker that loads and runs Dynamic Workers.","url":"https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-starter/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript","TypeScript"]}</script>
  markdown: true
  noindex: false
  route: /dynamic-workers/examples/dynamic-workers-starter/
  schema: 1
---
<p>A <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers">starter template</a> for deploying a Worker that loads and runs <a href="/dynamic-workers/">Dynamic Workers</a>.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<h2 id="what-it-does">What it does</h2>
<p>This template demonstrates how to use the <a href="/workers/runtime-apis/bindings/worker-loader/">Worker Loader API</a> to execute code at runtime. The host Worker exposes an <code>/api/run</code> endpoint that accepts code from the frontend, loads it into a sandboxed Dynamic Worker, and returns the result.</p>
<p>Use this pattern for AI agents that need to execute a snippet of code to complete an action.</p>
<h2 id="configuration">Configuration</h2>
<p>Add a <code>worker_loaders</code> binding to your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8449.md")
</div>
<h2 id="loading-and-executing-a-dynamic-worker">Loading and executing a Dynamic Worker</h2>
<p>In this example:</p>
<ul>
<li><code>env.LOADER.load()</code> creates a one-off dynamic isolate</li>
<li><code>globalOutbound: null</code> blocks all outbound network access from the Dynamic Worker</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8450.md")
</div>
<h2 id="running-locally">Running locally</h2>
<pre tabindex="0"><code class="language-sh">npm install&#10;npm run dev&#10;</code></pre>
