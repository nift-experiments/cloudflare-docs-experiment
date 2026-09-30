---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/get-started/wrangler/
  description: Create and manage AI Search instances from the command line.
  full_title: CLI · Cloudflare AI Search docs
  head_html: <title>CLI · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and manage AI Search instances from the command line."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/get-started/wrangler/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/get-started/wrangler/index.md"><meta property="og:title" content="CLI · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and manage AI Search instances from the command line."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/get-started/wrangler/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/get-started/wrangler/#page","headline":"CLI \u00b7 Cloudflare AI Search docs","description":"Create and manage AI Search instances from the command line.","url":"https://developers.cloudflare.com/ai-search/get-started/wrangler/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/get-started/wrangler/
  schema: 1
---
<p>This guide walks you through creating an AI Search instance using the <a href="/workers/wrangler/">Wrangler CLI</a>.</p>
<h2 id="1-install-wrangler"><ol>
<li>Install Wrangler</li>
</ol></h2>
<p>Install <a href="/workers/wrangler/">Wrangler</a>, the command-line tool for Cloudflare Workers and developer platform products.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm install wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm install wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn install wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn install wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm install wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm install wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun install wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun install wrangler" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="2-create-an-ai-search-instance"><ol start="2">
<li>Create an AI Search instance</li>
</ol></h2>
<p>Create a new instance.</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search create my-instance&#10;</code></pre>
<p>You can upload files to the instance using the <a href="/ai-search/get-started/dashboard/#upload-content">dashboard</a> or the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/upload/">REST API</a>.</p>
<h3 id="connect-a-data-source-optional">Connect a data source (optional)</h3>
<p>You can optionally connect a website or R2 bucket when creating the instance.</p>
<p><strong>Website:</strong></p>
<p>Automatically crawl and index a <a href="/ai-search/configuration/data-source/website/">website</a> that you own.</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search create my-instance --type web-crawler --source developers.cloudflare.com&#10;</code></pre>
<p><strong>R2 bucket:</strong></p>
<p>Index documents stored in an <a href="/ai-search/configuration/data-source/r2/">R2 bucket</a>.</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search create my-instance --type r2 --source my-bucket&#10;</code></pre>
<h2 id="3-check-indexing-status"><ol start="3">
<li>Check indexing status</li>
</ol></h2>
<p>Check if your content has finished indexing by running the <code>stats</code> command.</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search stats my-instance&#10;</code></pre>
<h2 id="4-test-your-instance"><ol start="4">
<li>Test your instance</li>
</ol></h2>
<p>Once indexing is complete, run a search query against your instance.</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search search my-instance --query &quot;What is Cloudflare?&quot;&#10;</code></pre>
<p>For the full list of available commands, refer to <a href="/ai-search/wrangler-commands/">Wrangler commands</a>.</p>
<h2 id="add-to-your-application">Add to your application</h2>
<div class="nb-card nb-link-card"><h3 id="card-workers-binding-ai-search-api-search-workers-binding"><a href="/ai-search/api/search/workers-binding/">Workers binding</a></h3><p>Query AI Search directly from your Workers code.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-rest-api-ai-search-api-search-rest-api"><a href="/ai-search/api/search/rest-api/">REST API</a></h3><p>Query AI Search using HTTP requests.</p></div>
