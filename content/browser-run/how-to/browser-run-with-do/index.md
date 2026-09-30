---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/how-to/browser-run-with-do/
  description: Use the Browser Run API along with Durable Objects to take screenshots from web pages and store them in R2.
  full_title: Deploy a Browser Run Worker with Durable Objects · Cloudflare Browser Run docs
  head_html: <title>Deploy a Browser Run Worker with Durable Objects · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the Browser Run API along with Durable Objects to take screenshots from web pages and store them in R2."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/how-to/browser-run-with-do/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/how-to/browser-run-with-do/index.md"><meta property="og:title" content="Deploy a Browser Run Worker with Durable Objects · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the Browser Run API along with Durable Objects to take screenshots from web pages and store them in R2."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/how-to/browser-run-with-do/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Workers,Durable Objects,R2"><meta name="pcx_tags" content="JavaScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/how-to/browser-run-with-do/#page","headline":"Deploy a Browser Run Worker with Durable Objects \u00b7 Cloudflare Browser Run docs","description":"Use the Browser Run API along with Durable Objects to take screenshots from web pages and store them in R2.","url":"https://developers.cloudflare.com/browser-run/how-to/browser-run-with-do/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript"]}</script>
  markdown: true
  noindex: false
  route: /browser-run/how-to/browser-run-with-do/
  schema: 1
---
<p>By following this guide, you will create a Worker that uses the Browser Run API along with <a href="/durable-objects/">Durable Objects</a> to take screenshots from web pages and store them in <a href="/r2/">R2</a>.</p>
<p>Using Durable Objects to persist browser sessions improves performance by eliminating the time that it takes to spin up a new browser session. Since Durable Objects re-uses sessions, it reduces the number of concurrent sessions needed.</p>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3685.md")
</div></details>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p><a href="/workers/">Cloudflare Workers</a> provides a serverless execution environment that allows you to create new applications or augment existing ones without configuring or maintaining infrastructure. Your Worker application is a container to interact with a headless browser to do actions, such as taking screenshots.</p>
<p>Create a new Worker project named <code>browser-worker</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- browser-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- browser-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare browser-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare browser-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest browser-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest browser-worker" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="2-install-puppeteer"><ol start="2">
<li>Install Puppeteer</li>
</ol></h2>
<p>In your <code>browser-worker</code> directory, install Cloudflare’s <a href="/browser-run/puppeteer/">fork of Puppeteer</a>:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="3-create-a-r2-bucket"><ol start="3">
<li>Create a R2 bucket</li>
</ol></h2>
<p>Create two R2 buckets, one for production, and one for development.</p>
<p>Note that bucket names must be lowercase and can only contain dashes.</p>
<pre tabindex="0"><code class="language-sh">wrangler r2 bucket create screenshots&#10;wrangler r2 bucket create screenshots-test&#10;</code></pre>
<p>To check that your buckets were created, run:</p>
<pre tabindex="0"><code class="language-sh">wrangler r2 bucket list&#10;</code></pre>
<p>After running the <code>list</code> command, you will see all bucket names, including the ones you have just created.</p>
<h2 id="4-configure-your-wrangler-configuration-file"><ol start="4">
<li>Configure your Wrangler configuration file</li>
</ol></h2>
<p>Configure your <code>browser-worker</code> project's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> by adding a browser <a href="/workers/runtime-apis/bindings/">binding</a> and a <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag">Node.js compatibility flag</a>. Browser bindings allow for communication between a Worker and a headless browser which allows you to do actions such as taking a screenshot, generating a PDF and more.</p>
<p>Update your Wrangler configuration file with the Browser Run API binding, the R2 bucket you created and a Durable Object:</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3684.md")
</aside>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3686.md")
</div>
<h2 id="5-code"><ol start="5">
<li>Code</li>
</ol></h2>
<p>The code below uses Durable Object to instantiate a browser using Puppeteer. It then opens a series of web pages with different resolutions, takes a screenshot of each, and uploads it to R2.</p>
<p>The Durable Object keeps a browser session open for 60 seconds after last use. If a browser session is open, any requests will re-use the existing session rather than creating a new one. Update your Worker code by copy and pasting the following:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3687.md")
</div>
<h2 id="6-test"><ol start="6">
<li>Test</li>
</ol></h2>
<p>Run <code>npx wrangler dev</code> to test your Worker locally.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="use-real-headless-browser-during-local-development">Use real headless browser during local development</h3>
@markup("md", "content/.markup/bodies/3683.md")
</aside>
<h2 id="7-deploy"><ol start="7">
<li>Deploy</li>
</ol></h2>
<p>Run <a href="/workers/wrangler/commands/workers/#deploy"><code>npx wrangler deploy</code></a> to deploy your Worker to the Cloudflare global network.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Other <a href="https://github.com/cloudflare/puppeteer/tree/main/examples">Puppeteer examples</a></li>
<li>Get started with <a href="/durable-objects/get-started/">Durable Objects</a></li>
<li><a href="/r2/api/workers/workers-api-usage/">Using R2 from Workers</a></li>
</ul>
