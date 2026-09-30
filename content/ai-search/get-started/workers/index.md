---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/get-started/workers/
  description: Create, populate, and query an AI Search instance from a Cloudflare Worker.
  full_title: Workers binding · Cloudflare AI Search docs
  head_html: <title>Workers binding · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Create, populate, and query an AI Search instance from a Cloudflare Worker."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/get-started/workers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/get-started/workers/index.md"><meta property="og:title" content="Workers binding · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create, populate, and query an AI Search instance from a Cloudflare Worker."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/get-started/workers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/get-started/workers/#page","headline":"Workers binding \u00b7 Cloudflare AI Search docs","description":"Create, populate, and query an AI Search instance from a Cloudflare Worker.","url":"https://developers.cloudflare.com/ai-search/get-started/workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/get-started/workers/
  schema: 1
---
<p>This guide walks you through creating and querying an AI Search instance from a <a href="/workers/">Cloudflare Worker</a> using the Workers Binding. The Workers Binding uses a runtime <a href="/ai-search/api/search/workers-binding/">API</a> that runs inside a Worker and calls AI Search without managing API tokens.</p>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3043.md")
</div></details>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p>Create a new Worker project using the <code>create-cloudflare</code> CLI (C3). <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a> is a command-line tool designed to help you set up and deploy new applications to Cloudflare.</p>
<p>Create a new project named <code>ai-search-tutorial</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- ai-search-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- ai-search-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare ai-search-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare ai-search-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest ai-search-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest ai-search-tutorial" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Go to your application directory:</p>
<pre tabindex="0"><code class="language-sh">cd ai-search-tutorial&#10;</code></pre>
<h2 id="2-connect-your-worker-to-ai-search"><ol start="2">
<li>Connect your Worker to AI Search</li>
</ol></h2>
<p>Create a binding between your Worker and your AI Search instance. <a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Worker to interact with resources on the Cloudflare Developer Platform.</p>
<p>Add the following to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3044.md")
</div>
<p>This binds the <code>default</code> namespace to <code>env.AI_SEARCH</code>. Instances that you create without specifying a namespace belong to the <code>default</code> namespace. The <code>remote</code> option lets <code>wrangler dev</code> proxy requests to your deployed instance, since AI Search does not run locally. For all binding options, refer to the <a href="/ai-search/api/search/workers-binding/">Workers binding reference</a>.</p>
<h2 id="3-create-and-query-ai-search-from-your-worker"><ol start="3">
<li>Create and query AI Search from your Worker</li>
</ol></h2>
<p>Update the <code>src/index.ts</code> file in your <code>ai-search-tutorial</code> directory with the following code. It exposes two routes: <code>/setup</code> creates an instance named <code>my-instance</code> and indexes a sample document, and the default route queries it.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3045.md")
</div>
<h2 id="4-develop-locally"><ol start="4">
<li>Develop locally</li>
</ol></h2>
<p>Start a local development server:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>Wrangler gives you a URL (usually <code>localhost:8787</code>). Visit <code>/setup</code> once to create your instance and index the sample document, then query it at <code>/?q=your+search+terms</code>.</p>
<h2 id="5-deploy-your-worker"><ol start="5">
<li>Deploy your Worker</li>
</ol></h2>
<p>Log in with your Cloudflare account:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login&#10;</code></pre>
<p>Deploy your Worker to make it accessible on the Internet:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">https://ai-search-tutorial.&lt;YOUR_SUBDOMAIN&gt;.workers.dev&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-search-workers-binding-ai-search-api-search-workers-binding"><a href="/ai-search/api/search/workers-binding/">Search Workers binding</a></h3><p>Full reference for searching and chatting from a Worker.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-items-workers-binding-ai-search-api-items-workers-binding"><a href="/ai-search/api/items/workers-binding/">Items Workers binding</a></h3><p>Upload, list, and manage documents from a Worker.</p></div>
