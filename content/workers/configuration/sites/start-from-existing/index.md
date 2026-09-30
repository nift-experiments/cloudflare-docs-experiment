---
cp9:
  canonical: https://developers.cloudflare.com/workers/static-assets/
  description: Deploy an existing static site project to Cloudflare using Workers Sites.
  full_title: Start from existing · Cloudflare Workers docs
  head_html: <title>Start from existing · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy an existing static site project to Cloudflare using Workers Sites."><link rel="canonical" href="https://developers.cloudflare.com/workers/static-assets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/configuration/sites/start-from-existing/index.md"><meta property="og:title" content="Start from existing · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy an existing static site project to Cloudflare using Workers Sites."><meta property="og:url" content="https://developers.cloudflare.com/workers/configuration/sites/start-from-existing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/static-assets/#page","headline":"Start from existing \u00b7 Cloudflare Workers docs","description":"Deploy an existing static site project to Cloudflare using Workers Sites.","url":"https://developers.cloudflare.com/workers/static-assets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/configuration/sites/start-from-existing/
  schema: 1
---
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="use-workers-static-assets-instead">Use Workers Static Assets Instead</h3>
@markup("md", "content/.markup/bodies/16806.md")
</aside>
<p>Workers Sites require <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/wrangler">Wrangler</a> — make sure to use the <a href="/workers/wrangler/install-and-update/#update-wrangler">latest version</a>.</p>
<p>To deploy a pre-existing static site project, start with a pre-generated site. Workers Sites works with all static site generators, for example:</p>
<ul>
<li><a href="https://gohugo.io/getting-started/quick-start/">Hugo</a></li>
<li><a href="https://www.gatsbyjs.org/docs/quick-start/">Gatsby</a>, requires Node</li>
<li><a href="https://jekyllrb.com/docs/">Jekyll</a>, requires Ruby</li>
<li><a href="https://www.11ty.io/#quick-start">Eleventy</a>, requires Node</li>
<li><a href="https://wordpress.org">WordPress</a> (refer to the tutorial on <a href="/pages/how-to/deploy-a-wordpress-site/">deploying static WordPress sites with Pages</a>)</li>
</ul>
<h2 id="getting-started">Getting started</h2>
<ol>
<li>Run the <code>wrangler init</code> command in the root of your project's directory to generate a basic Worker:</li>
</ol>
<pre tabindex="0"><code class="language-sh">wrangler init -y&#10;</code></pre>
<p>This command adds/update the following files:</p>
<ul>
<li><code>wrangler.jsonc</code>: The file containing project configuration.</li>
<li><code>package.json</code>: Wrangler <code>devDependencies</code> are added.</li>
<li><code>tsconfig.json</code>: Added if not already there to support writing the Worker in TypeScript.</li>
<li><code>src/index.ts</code>: A basic Cloudflare Worker, written in TypeScript.</li>
</ul>
<ol start="2">
<li>Add your site's build/output directory to the Wrangler file:</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16807.md")
</div>
<p>The default directories for the most popular static site generators are listed below:</p>
<ul>
<li>Hugo: <code>public</code></li>
<li>Gatsby: <code>public</code></li>
<li>Jekyll: <code>_site</code></li>
<li>Eleventy: <code>_site</code></li>
</ul>
<ol start="3">
<li>Install the <code>@cloudflare/kv-asset-handler</code> package in your project:</li>
</ol>
<pre tabindex="0"><code class="language-sh">npm i -D @cloudflare/kv-asset-handler&#10;</code></pre>
<ol start="4">
<li>Replace the contents of <code>src/index.ts</code> with the following code snippet:</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16810.md")
</div></div>
<ol start="5">
<li>Run <code>wrangler dev</code> or <code>npx wrangler deploy</code> to preview or deploy your site on Cloudflare.
Wrangler will automatically upload the assets found in the configured directory.</li>
</ol>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<ol start="6">
<li>Deploy your site to a <a href="/workers/configuration/routing/custom-domains/">custom domain</a> that you own and have already attached as a Cloudflare zone. Add a <code>route</code> property to the Wrangler file.</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16811.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16804.md")
</aside>
<p>Learn more about <a href="/workers/wrangler/configuration/">configuring your project</a>.</p>
