---
cp9:
  canonical: https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/
  description: Debug your local and deployed Workers using breakpoints.
  full_title: Breakpoints · Cloudflare Workers docs
  head_html: <title>Breakpoints · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Debug your local and deployed Workers using breakpoints."><link rel="canonical" href="https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/index.md"><meta property="og:title" content="Breakpoints · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Debug your local and deployed Workers using breakpoints."><meta property="og:url" content="https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/#page","headline":"Breakpoints \u00b7 Cloudflare Workers docs","description":"Debug your local and deployed Workers using breakpoints.","url":"https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/observability/dev-tools/breakpoints/
  schema: 1
---
<h2 id="debug-via-breakpoints">Debug via breakpoints</h2>
<p>When developing a Worker locally using Wrangler or Vite, you can debug via breakpoints in your Worker. Breakpoints provide the ability to review what is happening at a given point in the execution of your Worker. Breakpoint functionality exists in both DevTools and VS Code.</p>
<p>For more information on breakpoint debugging via Chrome's DevTools, refer to <a href="https://developer.chrome.com/docs/devtools/javascript/breakpoints/">Chrome's article on breakpoints</a>.</p>
<h3 id="vscode-debug-terminals">VSCode debug terminals</h3>
<p>Using VSCode's built-in <a href="https://code.visualstudio.com/docs/nodejs/nodejs-debugging#_javascript-debug-terminal">JavaScript Debug Terminals</a>, all you have to do is open a JS debug terminal (<code>Cmd + Shift + P</code> and then type <code>javascript debug</code>) and run <code>wrangler dev</code> (or <code>vite dev</code>) from within the debug terminal. VSCode will automatically connect to your running Worker (even if you're running multiple Workers at once!) and start a debugging session.</p>
<h3 id="setup-vs-code-to-use-breakpoints-with-launch-json-files">Setup VS Code to use breakpoints with <code>launch.json</code> files</h3>
<p>To setup VS Code for breakpoint debugging in your Worker project:</p>
<ol>
<li>Create a <code>.vscode</code> folder in your project's root folder if one does not exist.</li>
<li>Within that folder, create a <code>launch.json</code> file with the following content:</li>
</ol>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;configurations&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;Listen Wrangler&quot;,&#10;			&quot;type&quot;: &quot;node&quot;,&#10;			&quot;request&quot;: &quot;attach&quot;,&#10;			&quot;port&quot;: 9229,&#10;			&quot;cwd&quot;: &quot;/&quot;,&#10;			&quot;resolveSourceMapLocations&quot;: null,&#10;			&quot;attachExistingChildren&quot;: false,&#10;			&quot;autoAttachChildProcesses&quot;: false,&#10;			&quot;sourceMaps&quot;: true // works with or without this line&#10;		},&#10;		{&#10;			&quot;name&quot;: &quot;Launch Wrangler&quot;,&#10;			&quot;command&quot;: &quot;npm run dev&quot;,&#10;			&quot;type&quot;: &quot;node-terminal&quot;,&#10;			&quot;request&quot;: &quot;launch&quot;,&#10;			&quot;console&quot;: &quot;integratedTerminal&quot;,&#10;			&quot;sourceMaps&quot;: true&#10;		}&#10;	]&#10;}&#10;</code></pre>
<ol start="3">
<li>
<p>Open your project in VS Code, open a new terminal window from VS Code, and run <code>npx wrangler dev</code> to start the local dev server.</p>
</li>
<li>
<p>At the top of the <strong>Run &amp; Debug</strong> panel, you should see an option to select a configuration. Choose <strong>Wrangler</strong>, and select the play icon. <strong>Wrangler: Remote Process [0]</strong> should show up in the Call Stack panel on the left.</p>
</li>
<li>
<p>Go back to a <code>.js</code> or <code>.ts</code> file in your project and add at least one breakpoint.</p>
</li>
<li>
<p>Open your browser and go to the Worker's local URL (default <code>http://127.0.0.1:8787</code>). The breakpoint should be hit, and you should be able to review details about your code at the specified line.</p>
</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17062.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17061.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/local-development/">Local Development</a> - Develop your Workers and connected resources locally via Wrangler and <a href="https://github.com/cloudflare/workerd"><code>workerd</code></a>, for a fast, accurate feedback loop.</li>
</ul>
