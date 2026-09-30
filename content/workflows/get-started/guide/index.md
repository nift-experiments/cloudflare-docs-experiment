---
cp9:
  canonical: https://developers.cloudflare.com/workflows/get-started/guide/
  description: Create and deploy your first Cloudflare Workflow with durable, multi-step execution on the Workers platform.
  full_title: Build your first Workflow · Cloudflare Workflows docs
  head_html: <title>Build your first Workflow · Cloudflare Workflows docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and deploy your first Cloudflare Workflow with durable, multi-step execution on the Workers platform."><link rel="canonical" href="https://developers.cloudflare.com/workflows/get-started/guide/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workflows/get-started/guide/index.md"><meta property="og:title" content="Build your first Workflow · Cloudflare Workflows docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and deploy your first Cloudflare Workflow with durable, multi-step execution on the Workers platform."><meta property="og:url" content="https://developers.cloudflare.com/workflows/get-started/guide/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workflows"><meta name="algolia_product_filter" content="Workflows"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Workflows"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workflows/get-started/guide/#page","headline":"Build your first Workflow \u00b7 Cloudflare Workflows docs","description":"Create and deploy your first Cloudflare Workflow with durable, multi-step execution on the Workers platform.","url":"https://developers.cloudflare.com/workflows/get-started/guide/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workflows/get-started/guide/
  schema: 1
---
<p>Workflows allow you to build durable, multi-step applications using the Workers platform. A Workflow can automatically retry, persist state, run for hours or days, and coordinate between third-party APIs.</p>
<p>You can build Workflows to post-process file uploads to <a href="/r2/">R2 object storage</a>, automate generation of <a href="/workers-ai/">Workers AI</a> embeddings into a <a href="/vectorize/">Vectorize</a> vector database, or to trigger user lifecycle emails using <a href="/email-service/">Email Service</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17502.md")
</aside>
<p>In this guide, you will create and deploy a Workflow that fetches data, pauses, and processes results.</p>
<h2 id="quick-start">Quick start</h2>
<p>If you want to skip the steps and pull down the complete Workflow we are building in this guide, run:</p>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest workflows-starter -- --template &quot;cloudflare/workflows-starter&quot;&#10;</code></pre>
<p>Use this option if you are familiar with Cloudflare Workers or want to explore the code first and learn the details later.</p>
<p>Follow the steps below to learn how to build a Workflow from scratch.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17503.md")
</div></details>
<h2 id="1-create-a-new-worker-project"><ol>
<li>Create a new Worker project</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17505.md")
</div>
<h2 id="2-write-your-workflow"><ol start="2">
<li>Write your Workflow</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17506.md")
</div>
<h2 id="3-configure-your-workflow"><ol start="3">
<li>Configure your Workflow</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17509.md")
</div>
<h2 id="4-write-your-api"><ol start="4">
<li>Write your API</li>
</ol></h2>
<p>Now, you'll need a place to call your Workflow.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17510.md")
</div>
<h2 id="5-develop-locally"><ol start="5">
<li>Develop locally</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17511.md")
</div>
<h2 id="6-deploy-your-workflow"><ol start="6">
<li>Deploy your Workflow</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17512.md")
</div>
<h2 id="learn-more">Learn more</h2>
<div class="nb-card nb-link-card"><h3 id="card-events-and-parameters-workflows-build-events-and-parameters"><a href="/workflows/build/events-and-parameters/">Events and parameters</a></h3><p>Pass data to Workflows and pause for external events with waitForEvent.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-sleeping-and-retrying-workflows-build-sleeping-and-retrying"><a href="/workflows/build/sleeping-and-retrying/">Sleeping and retrying</a></h3><p>Configure retry behavior and sleep patterns.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-workers-api-workflows-build-workers-api"><a href="/workflows/build/workers-api/">Workers API</a></h3><p>Explore the full Workflows API for programmatic control.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-rules-of-workflows-workflows-build-rules-of-workflows"><a href="/workflows/build/rules-of-workflows/">Rules of Workflows</a></h3><p>Understand the programming model and best practices.</p></div>
