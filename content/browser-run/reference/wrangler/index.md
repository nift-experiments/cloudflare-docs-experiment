---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/reference/wrangler/
  description: Use Wrangler, a command-line tool, to deploy projects using Cloudflare's Workers Browser Run API.
  full_title: Wrangler · Cloudflare Browser Run docs
  head_html: <title>Wrangler · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Wrangler, a command-line tool, to deploy projects using Cloudflare&#x27;s Workers Browser Run API."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/reference/wrangler/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/reference/wrangler/index.md"><meta property="og:title" content="Wrangler · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Wrangler, a command-line tool, to deploy projects using Cloudflare&#x27;s Workers Browser Run API."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/reference/wrangler/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/reference/wrangler/#page","headline":"Wrangler \u00b7 Cloudflare Browser Run docs","description":"Use Wrangler, a command-line tool, to deploy projects using Cloudflare's Workers Browser Run API.","url":"https://developers.cloudflare.com/browser-run/reference/wrangler/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/reference/wrangler/
  schema: 1
---
<p><a href="/workers/wrangler/">Wrangler</a> is a command-line tool for building with Cloudflare developer products.</p>
<p>Use Wrangler to deploy projects that use the Workers Browser Run API.</p>
<h2 id="install">Install</h2>
<p>To install Wrangler, refer to <a href="/workers/wrangler/install-and-update/">Install and Update Wrangler</a>.</p>
<h2 id="bindings">Bindings</h2>
<p><a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Workers to interact with resources on the Cloudflare developer platform. A browser binding will provide your Worker with an authenticated endpoint to interact with a dedicated Chromium browser instance.</p>
<p>To deploy a Browser Run Worker, you must declare a <a href="/workers/runtime-apis/bindings/">browser binding</a> in your Worker's Wrangler configuration file.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3581.md")
</aside>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3582.md")
</div>
<p>After the binding is declared, access the DevTools endpoint using <code>env.MYBROWSER</code> in your Worker code:</p>
<pre tabindex="0"><code class="language-javascript">const browser = await puppeteer.launch(env.MYBROWSER);&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="quick-actions-compatibility">Quick Actions compatibility</h3>
@markup("md", "content/.markup/bodies/3580.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="quick-actions-require-remote-mode-for-local-development">Quick Actions require remote mode for local development</h3>
@markup("md", "content/.markup/bodies/3579.md")
</aside>
<p>For Puppeteer, Playwright, or CDP-based Workers, run <code>npx wrangler dev</code> to test locally. For Quick Actions via <code>.quickAction()</code>, use <code>npx wrangler dev --remote</code> as noted above.</p>
<h3 id="headful-mode-experimental">Headful mode (experimental)</h3>
<p>By default, local development runs Chrome in headless mode. To launch Chrome in visible (headful) mode for debugging, set the <code>X_BROWSER_HEADFUL</code> environment variable:</p>
<pre tabindex="0"><code class="language-sh">X_BROWSER_HEADFUL=true npx wrangler dev&#10;</code></pre>
<p>This opens a browser window on screen so you can watch navigations, interactions, and rendering in real time. Headful mode is for local development only and does not affect deployed Workers. This feature is experimental and may change without notice.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3578.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="use-real-headless-browser-during-local-development">Use real headless browser during local development</h3>
@markup("md", "content/.markup/bodies/3577.md")
</aside>
