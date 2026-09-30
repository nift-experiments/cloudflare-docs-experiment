---
cp9:
  canonical: https://developers.cloudflare.com/pages/functions/get-started/
  description: Create and deploy your first Pages Function on Cloudflare Pages.
  full_title: Functions - Get started · Cloudflare Pages docs
  head_html: <title>Functions - Get started · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and deploy your first Pages Function on Cloudflare Pages."><link rel="canonical" href="https://developers.cloudflare.com/pages/functions/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/functions/get-started/index.md"><meta property="og:title" content="Functions - Get started · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and deploy your first Pages Function on Cloudflare Pages."><meta property="og:url" content="https://developers.cloudflare.com/pages/functions/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/functions/get-started/#page","headline":"Functions - Get started \u00b7 Cloudflare Pages docs","description":"Create and deploy your first Pages Function on Cloudflare Pages.","url":"https://developers.cloudflare.com/pages/functions/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/functions/get-started/
  schema: 1
---
<p>This guide will instruct you on creating and deploying a Pages Function.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You must have a Pages project set up on your local machine or deployed on the Cloudflare dashboard. To create a Pages project, refer to <a href="/pages/get-started/">Get started</a>.</p>
<h2 id="create-a-function">Create a Function</h2>
<p>To get started with generating a Pages Function, create a <code>/functions</code> directory. Make sure that the <code>/functions</code> directory is at the root of your Pages project (and not in the static root, such as <code>/dist</code>).</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="advanced-mode">Advanced mode</h3>
@markup("md", "content/.markup/bodies/10952.md")
</aside>
<p>Writing your Functions files in the <code>/functions</code> directory will automatically generate a Worker with custom functionality at predesignated routes.</p>
<p>Copy and paste the following code into a <code>helloworld.js</code> file that you create in your <code>/functions</code> folder:</p>
<pre tabindex="0"><code class="language-js">export function onRequest(context) {&#10;	return new Response(&quot;Hello, world!&quot;);&#10;}&#10;</code></pre>
<p>In the above example code, the <code>onRequest</code> handler takes a request <a href="/pages/functions/api-reference/#eventcontext"><code>context</code></a> object. The handler must return a <code>Response</code> or a <code>Promise</code> of a <code>Response</code>.</p>
<p>This Function will run on the <code>/helloworld</code> route and returns <code>&quot;Hello, world!&quot;</code>. The reason this Function is available on this route is because the file is named <code>helloworld.js</code>. Similarly, if this file was called <code>howdyworld.js</code>, this function would run on <code>/howdyworld</code>.</p>
<p>Refer to <a href="/pages/functions/routing/">Routing</a> for more information on route customization.</p>
<h3 id="runtime-features">Runtime features</h3>
<p><a href="/workers/runtime-apis/">Workers runtime features</a> are configurable on Pages Functions, including <a href="/workers/runtime-apis/nodejs">compatibility with a subset of Node.js APIs</a> and the ability to set a <a href="/workers/configuration/compatibility-dates/">compatibility date or compatibility flag</a>.</p>
<p>Set these configurations by passing an argument to your <a href="/workers/wrangler/commands/pages/#pages-dev">Wrangler</a> command or by setting them in the dashboard. To set Pages compatibility flags in the Cloudflare dashboard:</p>
<ol>
<li>Log into the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your account.</li>
<li>Select <strong>Workers &amp; Pages</strong> and select your Pages project.</li>
<li>Select <strong>Settings</strong> &gt; <strong>Functions</strong> &gt; <strong>Compatibility Flags</strong>.</li>
<li>Configure your Production and Preview compatibility flags as needed.</li>
</ol>
<p>Additionally, use other Cloudflare products such as <a href="/d1/">D1</a> (serverless DB) and <a href="/r2/">R2</a> from within your Pages project by configuring <a href="/pages/functions/bindings/">bindings</a>.</p>
<h2 id="deploy-your-function">Deploy your Function</h2>
<p>After you have set up your Function, deploy your Pages project. Deploy your project by:</p>
<ul>
<li>Connecting your <a href="/pages/get-started/git-integration/">Git provider</a>.</li>
<li>Using <a href="/workers/wrangler/commands/pages/#pages">Wrangler</a> from the command line.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10951.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Customize your <a href="/pages/functions/routing/">Function's routing</a></li>
<li>Review the <a href="/pages/functions/api-reference/">API reference</a></li>
<li>Learn how to <a href="/pages/functions/debugging-and-logging/">debug your Function</a></li>
</ul>
