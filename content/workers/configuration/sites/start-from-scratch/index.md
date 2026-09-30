---
cp9:
  canonical: https://developers.cloudflare.com/workers/static-assets/
  description: Create a new Workers Sites project from scratch with Wrangler.
  full_title: Start from scratch · Cloudflare Workers docs
  head_html: <title>Start from scratch · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a new Workers Sites project from scratch with Wrangler."><link rel="canonical" href="https://developers.cloudflare.com/workers/static-assets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/configuration/sites/start-from-scratch/index.md"><meta property="og:title" content="Start from scratch · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a new Workers Sites project from scratch with Wrangler."><meta property="og:url" content="https://developers.cloudflare.com/workers/configuration/sites/start-from-scratch/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/static-assets/#page","headline":"Start from scratch \u00b7 Cloudflare Workers docs","description":"Create a new Workers Sites project from scratch with Wrangler.","url":"https://developers.cloudflare.com/workers/static-assets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/configuration/sites/start-from-scratch/
  schema: 1
---
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="use-workers-static-assets-instead">Use Workers Static Assets Instead</h3>
@markup("md", "content/.markup/bodies/16800.md")
</aside>
<p>This guide shows how to quickly start a new Workers Sites project from scratch.</p>
<h2 id="getting-started">Getting started</h2>
<ol>
<li>
<p>Ensure you have the latest version of <a href="https://git-scm.com/downloads">git</a> and <a href="https://nodejs.org/en/download/">Node.js</a> installed.</p>
</li>
<li>
<p>In your terminal, clone the <code>worker-sites-template</code> starter repository.
The following example creates a project called <code>my-site</code>:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">git clone --depth=1 --branch=wrangler2 https://github.com/cloudflare/worker-sites-template my-site&#10;</code></pre>
<ol start="3">
<li>
<p>Run <code>npm install</code> to install all dependencies.</p>
</li>
<li>
<p>You can preview your site by running the <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> command:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">wrangler dev&#10;</code></pre>
<ol start="5">
<li>Deploy your site to Cloudflare:</li>
</ol>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<h2 id="project-layout">Project layout</h2>
<p>The template project contains the following files and directories:</p>
<ul>
<li><code>public</code>: The static assets for your project. By default it contains an <code>index.html</code> and a <code>favicon.ico</code>.</li>
<li><code>src</code>: The Worker configured for serving your assets. You do not need to edit this but if you want to see how it works or add more functionality to your Worker, you can edit <code>src/index.ts</code>.</li>
<li><code>wrangler.jsonc</code>: The file containing project configuration.
The <code>bucket</code> property tells Wrangler where to find the static assets (e.g. <code>site = { bucket = &quot;./public&quot; }</code>).</li>
<li><code>package.json</code>/<code>package-lock.json</code>: define the required Node.js dependencies.</li>
</ul>
<h2 id="customize-the-wrangler-jsonc-file">Customize the <code>wrangler.jsonc</code> file:</h2>
<ul>
<li>Change the <code>name</code> property to the name of your project:</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16801.md")
</div>
<ul>
<li>Consider updating<code>compatibility_date</code> to today's date to get access to the most recent Workers features:</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16802.md")
</div>
<ul>
<li>Deploy your site to a <a href="/workers/configuration/routing/custom-domains/">custom domain</a> that you own and have already attached as a Cloudflare zone:</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16803.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16799.md")
</aside>
<p>Learn more about <a href="/workers/wrangler/configuration/">configuring your project</a>.</p>
