---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/how-to/deploy-worker/
  description: Create and deploy a Cloudflare Worker that uses Browser Run to take screenshots from web pages.
  full_title: Deploy a Browser Run Worker · Cloudflare Browser Run docs
  head_html: <title>Deploy a Browser Run Worker · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and deploy a Cloudflare Worker that uses Browser Run to take screenshots from web pages."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/how-to/deploy-worker/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/how-to/deploy-worker/index.md"><meta property="og:title" content="Deploy a Browser Run Worker · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and deploy a Cloudflare Worker that uses Browser Run to take screenshots from web pages."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/how-to/deploy-worker/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Browser Run,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/how-to/deploy-worker/#page","headline":"Deploy a Browser Run Worker \u00b7 Cloudflare Browser Run docs","description":"Create and deploy a Cloudflare Worker that uses Browser Run to take screenshots from web pages.","url":"https://developers.cloudflare.com/browser-run/how-to/deploy-worker/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/how-to/deploy-worker/
  schema: 1
---
<p>By following this guide, you will create a Worker that uses the Browser Run API to take screenshots from web pages. This is a common use case for browser automation.</p>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3678.md")
</div></details>
<h4 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h4>
<p><a href="/workers/">Cloudflare Workers</a> provides a serverless execution environment that allows you to create new applications or augment existing ones without configuring or maintaining infrastructure. Your Worker application is a container to interact with a headless browser to do actions, such as taking screenshots.</p>
<p>Create a new Worker project named <code>browser-worker</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- browser-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- browser-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare browser-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare browser-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest browser-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest browser-worker" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>JavaScript / TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<h4 id="2-install-puppeteer"><ol start="2">
<li>Install Puppeteer</li>
</ol></h4>
<p>In your <code>browser-worker</code> directory, install Cloudflare’s <a href="/browser-run/puppeteer/">fork of Puppeteer</a>:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div></div>
<h4 id="3-create-a-kv-namespace"><ol start="3">
<li>Create a KV namespace</li>
</ol></h4>
<p>Browser Run can be used with other developer products. You might need a <a href="/d1/">relational database</a>, an <a href="/r2/">R2 bucket</a> to archive your crawled pages and assets, a <a href="/durable-objects/">Durable Object</a> to keep your browser instance alive and share it with multiple requests, or <a href="/queues/">Queues</a> to handle your jobs asynchronously.</p>
<p>For the purpose of this example, we will use a <a href="/kv/concepts/kv-namespaces/">KV store</a> to cache your screenshots.</p>
<p>Create two namespaces, one for production and one for development.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler kv namespace create BROWSER_KV_DEMO&#10;npx wrangler kv namespace create BROWSER_KV_DEMO --preview&#10;</code></pre>
<p>Take note of the IDs for the next step.</p>
<h4 id="4-configure-the-wrangler-configuration-file"><ol start="4">
<li>Configure the Wrangler configuration file</li>
</ol></h4>
<p>Configure your <code>browser-worker</code> project's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> by adding a browser <a href="/workers/runtime-apis/bindings/">binding</a> and a <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag">Node.js compatibility flag</a>. Bindings allow your Workers to interact with resources on the Cloudflare developer platform. Your browser <code>binding</code> name is set by you, this guide uses the name <code>MYBROWSER</code>. Browser bindings allow for communication between a Worker and a headless browser which allows you to do actions such as taking a screenshot, generating a PDF, and more.</p>
<p>Update your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> with the Browser Run API binding and the KV namespaces you created:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3679.md")
</div>
<h4 id="5-code"><ol start="5">
<li>Code</li>
</ol></h4>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3682.md")
</div></div>
<p>This Worker instantiates a browser using Puppeteer, opens a new page, navigates to the location of the 'url' parameter, takes a screenshot of the page, stores the screenshot in KV, closes the browser, and responds with the JPEG image of the screenshot.</p>
<p>If your Worker is running in production, it will store the screenshot to the production KV namespace. If you are running <code>wrangler dev</code>, it will store the screenshot to the dev KV namespace.</p>
<p>If the same <code>url</code> is requested again, it will use the cached version in KV instead, unless it expired.</p>
<h4 id="6-test"><ol start="6">
<li>Test</li>
</ol></h4>
<p>Run <code>npx wrangler dev</code> to test your Worker locally.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="use-real-headless-browser-during-local-development">Use real headless browser during local development</h3>
@markup("md", "content/.markup/bodies/3677.md")
</aside>
<p>To test taking your first screenshot, go to the following URL:</p>
<p><code>&lt;LOCAL_HOST_URL&gt;/?url=https://example.com</code></p>
<h4 id="7-deploy"><ol start="7">
<li>Deploy</li>
</ol></h4>
<p>Run <code>npx wrangler deploy</code> to deploy your Worker to the Cloudflare global network.</p>
<p>To take your first screenshot, go to the following URL:</p>
<pre tabindex="0"><code>&lt;YOUR_WORKER&gt;.&lt;YOUR_SUBDOMAIN&gt;.workers.dev/?url=https://example.com&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Other <a href="https://github.com/cloudflare/puppeteer/tree/main/examples">Puppeteer examples</a></li>
</ul>
