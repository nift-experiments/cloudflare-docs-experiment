---
cp9:
  canonical: https://developers.cloudflare.com/workers/testing/miniflare/developing/debugger/
  description: Attach a Node.js debugger to Miniflare for setting breakpoints and inspecting Cloudflare Workers code.
  full_title: Attaching a Debugger · Cloudflare Workers docs
  head_html: <title>Attaching a Debugger · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Attach a Node.js debugger to Miniflare for setting breakpoints and inspecting Cloudflare Workers code."><link rel="canonical" href="https://developers.cloudflare.com/workers/testing/miniflare/developing/debugger/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/testing/miniflare/developing/debugger/index.md"><meta property="og:title" content="Attaching a Debugger · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Attach a Node.js debugger to Miniflare for setting breakpoints and inspecting Cloudflare Workers code."><meta property="og:url" content="https://developers.cloudflare.com/workers/testing/miniflare/developing/debugger/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/testing/miniflare/developing/debugger/#page","headline":"Attaching a Debugger \u00b7 Cloudflare Workers docs","description":"Attach a Node.js debugger to Miniflare for setting breakpoints and inspecting Cloudflare Workers code.","url":"https://developers.cloudflare.com/workers/testing/miniflare/developing/debugger/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/testing/miniflare/developing/debugger/
  schema: 1
---
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17365.md")
</aside>
<p>You can use regular Node.js tools to debug your Workers. Setting breakpoints,
watching values and inspecting the call stack are all examples of things you can
do with a debugger.</p>
<h2 id="visual-studio-code">Visual Studio Code</h2>
<h3 id="create-configuration">Create configuration</h3>
<p>The easiest way to debug a Worker in VSCode is to create a new configuration.</p>
<p>Open the <strong>Run and Debug</strong> menu in the VSCode activity bar and create a
<code>.vscode/launch.json</code> file that contains the following:</p>
<pre tabindex="0"><code class="language-json">&#45;--&#10;filename: .vscode/launch.json&#10;&#45;--&#10;{&#10;  &quot;configurations&quot;: [&#10;    {&#10;      &quot;name&quot;: &quot;Miniflare&quot;,&#10;      &quot;type&quot;: &quot;node&quot;,&#10;      &quot;request&quot;: &quot;attach&quot;,&#10;      &quot;port&quot;: 9229,&#10;      &quot;cwd&quot;: &quot;/&quot;,&#10;      &quot;resolveSourceMapLocations&quot;: null,&#10;      &quot;attachExistingChildren&quot;: false,&#10;      &quot;autoAttachChildProcesses&quot;: false,&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>From the <strong>Run and Debug</strong> menu in the activity bar, select the <code>Miniflare</code>
configuration, and click the green play button to start debugging.</p>
<h2 id="webstorm">WebStorm</h2>
<p>Create a new configuration, by clicking <strong>Add Configuration</strong> in the top right.</p>
<p><img src="/assets/upstream/images/workers/testing/miniflare/developing/debugger-webstorm-node-add.png" alt="WebStorm add configuration button" /></p>
<p>Click the <strong>plus</strong> button in the top left of the popup and create a new
<strong>Node.js/Chrome</strong> configuration. Set the <strong>Host</strong> field to <code>localhost</code> and the
<strong>Port</strong> field to <code>9229</code>. Then click <strong>OK</strong>.</p>
<p><img src="/assets/upstream/images/workers/testing/miniflare/developing/debugger-webstorm-settings.png" alt="WebStorm Node.js debug configuration" /></p>
<p>With the new configuration selected, click the green debug button to start
debugging.</p>
<p><img src="/assets/upstream/images/workers/testing/miniflare/developing/debugger-webstorm-node-run.png" alt="WebStorm configuration debug button" /></p>
<h2 id="devtools">DevTools</h2>
<p>Breakpoints can also be added via the Workers DevTools. For more information,
<a href="/workers/observability/dev-tools">read the guide</a>
in the Cloudflare Workers docs.</p>
