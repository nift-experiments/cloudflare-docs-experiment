---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/how-to/simple-search-engine/
  description: Build a simple search engine using the AI Search Workers binding and the search method.
  full_title: Create a simple search engine · Cloudflare AI Search docs
  head_html: <title>Create a simple search engine · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Build a simple search engine using the AI Search Workers binding and the search method."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/how-to/simple-search-engine/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/how-to/simple-search-engine/index.md"><meta property="og:title" content="Create a simple search engine · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build a simple search engine using the AI Search Workers binding and the search method."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/how-to/simple-search-engine/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/how-to/simple-search-engine/#page","headline":"Create a simple search engine \u00b7 Cloudflare AI Search docs","description":"Build a simple search engine using the AI Search Workers binding and the search method.","url":"https://developers.cloudflare.com/ai-search/how-to/simple-search-engine/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/how-to/simple-search-engine/
  schema: 1
---
<p>This guide builds a search engine that returns the file names matching a query, using the <code>search()</code> method on the <a href="/ai-search/api/search/workers-binding/">Workers binding</a>. You can adapt it to use the <a href="/ai-search/api/search/rest-api/">REST API</a> instead.</p>
<p>For the best results with this pattern:</p>
<ul>
<li>Disable query rewriting so the original user query is matched directly.</li>
<li>Configure your AI Search instance with small chunk sizes (256 tokens is usually enough).</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3003.md")
</div></details>
<p>You also need an AI Search instance that already contains indexed content. To create one and add content, refer to <a href="/ai-search/get-started/">Get started</a>.</p>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p>Create a new Worker project using the <code>create-cloudflare</code> CLI (C3). <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a> is a command-line tool designed to help you set up and deploy new applications to Cloudflare.</p>
<p>Create a new project named <code>search-engine</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- search-engine</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- search-engine" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare search-engine</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare search-engine" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest search-engine</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest search-engine" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Go to your application directory:</p>
<pre tabindex="0"><code class="language-sh">cd search-engine&#10;</code></pre>
<h2 id="2-bind-your-worker-to-ai-search"><ol start="2">
<li>Bind your Worker to AI Search</li>
</ol></h2>
<p>Add the following to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3004.md")
</div>
<p>This binds the <code>default</code> <a href="/ai-search/concepts/namespaces/">namespace</a> to <code>env.AI_SEARCH</code>. The <code>remote</code> option lets <code>wrangler dev</code> proxy requests to your deployed instance, since AI Search does not run locally.</p>
<h2 id="3-add-the-search-code"><ol start="3">
<li>Add the search code</li>
</ol></h2>
<p>Update <code>src/index.ts</code>. This Worker reads a query from the URL, searches your instance, and returns the file name of each matching chunk. Replace <code>my-instance</code> with the name of your instance.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3005.md")
</div>
<h2 id="4-run-and-deploy"><ol start="4">
<li>Run and deploy</li>
</ol></h2>
<p>Start a local development server, then query it at <code>/?query=your+search+terms</code>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>Log in with your Cloudflare account, then deploy your Worker to make it accessible on the Internet:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login&#10;npx wrangler deploy&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-search-workers-binding-ai-search-api-search-workers-binding"><a href="/ai-search/api/search/workers-binding/">Search Workers binding</a></h3><p>Full reference for searching and chatting from a Worker.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-query-rewriting-ai-search-configuration-retrieval-query-rewriting"><a href="/ai-search/configuration/retrieval/query-rewriting/">Query rewriting</a></h3><p>Control whether AI Search rewrites the query before searching.</p></div>
