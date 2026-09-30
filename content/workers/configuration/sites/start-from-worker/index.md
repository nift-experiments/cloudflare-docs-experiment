---
cp9:
  canonical: https://developers.cloudflare.com/workers/static-assets/
  description: Add static asset serving to an existing Cloudflare Worker using Workers Sites.
  full_title: Start from Worker · Cloudflare Workers docs
  head_html: <title>Start from Worker · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Add static asset serving to an existing Cloudflare Worker using Workers Sites."><link rel="canonical" href="https://developers.cloudflare.com/workers/static-assets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/configuration/sites/start-from-worker/index.md"><meta property="og:title" content="Start from Worker · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Add static asset serving to an existing Cloudflare Worker using Workers Sites."><meta property="og:url" content="https://developers.cloudflare.com/workers/configuration/sites/start-from-worker/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/static-assets/#page","headline":"Start from Worker \u00b7 Cloudflare Workers docs","description":"Add static asset serving to an existing Cloudflare Worker using Workers Sites.","url":"https://developers.cloudflare.com/workers/static-assets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/configuration/sites/start-from-worker/
  schema: 1
---
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="use-workers-static-assets-instead">Use Workers Static Assets Instead</h3>
@markup("md", "content/.markup/bodies/16794.md")
</aside>
<p>Workers Sites require <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/wrangler">Wrangler</a> — make sure to use the <a href="/workers/wrangler/install-and-update/#update-wrangler">latest version</a>.</p>
<p>If you have a pre-existing Worker project, you can use Workers Sites to serve static assets to the Worker.</p>
<h2 id="getting-started">Getting started</h2>
<ol>
<li>
<p>Create a directory that will contain the assets in the root of your project (for example, <code>./public</code>)</p>
</li>
<li>
<p>Add configuration to your Wrangler file to point to it.</p>
</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16795.md")
</div>
<ol start="3">
<li>Install the <code>@cloudflare/kv-asset-handler</code> package in your project:</li>
</ol>
<pre tabindex="0"><code class="language-sh">npm i -D @cloudflare/kv-asset-handler&#10;</code></pre>
<ol start="4">
<li>Import the <code>getAssetFromKV()</code> function into your Worker entry point and use it to respond with static assets.</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16798.md")
</div></div>
<p>For more information on the configurable options of <code>getAssetFromKV()</code> refer to <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/kv-asset-handler">kv-asset-handler docs</a>.</p>
<ol start="5">
<li>Run <code>wrangler deploy</code> or <code>npx wrangler deploy</code> as you would normally with your Worker project.
Wrangler will automatically upload the assets found in the configured directory.</li>
</ol>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
