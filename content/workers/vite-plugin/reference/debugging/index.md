---
cp9:
  canonical: https://developers.cloudflare.com/workers/vite-plugin/reference/debugging/
  description: Debugging with the Vite plugin
  full_title: Debugging · Cloudflare Workers docs
  head_html: <title>Debugging · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Debugging with the Vite plugin"><link rel="canonical" href="https://developers.cloudflare.com/workers/vite-plugin/reference/debugging/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/vite-plugin/reference/debugging/index.md"><meta property="og:title" content="Debugging · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Debugging with the Vite plugin"><meta property="og:url" content="https://developers.cloudflare.com/workers/vite-plugin/reference/debugging/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/vite-plugin/reference/debugging/#page","headline":"Debugging \u00b7 Cloudflare Workers docs","description":"Debugging with the Vite plugin","url":"https://developers.cloudflare.com/workers/vite-plugin/reference/debugging/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/vite-plugin/reference/debugging/
  schema: 1
---
<p>The Cloudflare Vite plugin has debugging enabled by default and listens on port <code>9229</code>.
You may choose a custom port or disable debugging by setting the <code>inspectorPort</code> option in the <a href="/workers/vite-plugin/reference/api#interface-pluginconfig">plugin config</a>.
There are two recommended methods for debugging your Workers during local development:</p>
<h2 id="devtools">DevTools</h2>
<p>When running <code>vite dev</code> or <code>vite preview</code>, a <code>/__debug</code> route is added that provides access to <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/chrome-devtools-patches">Cloudflare's implementation</a> of <a href="https://developer.chrome.com/docs/devtools/overview">Chrome's DevTools</a>.
Navigating to this route will open a DevTools tab for each of the Workers in your application.</p>
<p>Once the tab(s) are open, you can make a request to your application and start debugging your Worker code.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17392.md")
</aside>
<h2 id="vs-code">VS Code</h2>
<p>To set up <a href="https://code.visualstudio.com/">VS Code</a> to support breakpoint debugging in your application, you should create a <code>.vscode/launch.json</code> file that contains the following configuration:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;configurations&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;&lt;NAME_OF_WORKER&gt;&quot;,&#10;			&quot;type&quot;: &quot;node&quot;,&#10;			&quot;request&quot;: &quot;attach&quot;,&#10;			&quot;websocketAddress&quot;: &quot;ws://localhost:9229/&lt;NAME_OF_WORKER&gt;&quot;,&#10;			&quot;resolveSourceMapLocations&quot;: null,&#10;			&quot;attachExistingChildren&quot;: false,&#10;			&quot;autoAttachChildProcesses&quot;: false,&#10;			&quot;sourceMaps&quot;: true&#10;		}&#10;	],&#10;	&quot;compounds&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;Debug Workers&quot;,&#10;			&quot;configurations&quot;: [&quot;&lt;NAME_OF_WORKER&gt;&quot;],&#10;			&quot;stopAll&quot;: true&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Here, <code>&lt;NAME_OF_WORKER&gt;</code> indicates the name of the Worker as specified in your Worker config file.
If you have used the <code>inspectorPort</code> option to set a custom port then this should be the value provided in the <code>websocketaddress</code> field.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17391.md")
</aside>
<p>With this set up, you can run <code>vite dev</code> or <code>vite preview</code> and then select <strong>Debug Workers</strong> at the top of the <strong>Run &amp; Debug</strong> panel to start debugging.</p>
