---
cp9:
  canonical: https://developers.cloudflare.com/workers/observability/dev-tools/
  description: Use Chrome DevTools to debug, profile, and inspect Cloudflare Workers locally.
  full_title: DevTools · Cloudflare Workers docs
  head_html: <title>DevTools · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Chrome DevTools to debug, profile, and inspect Cloudflare Workers locally."><link rel="canonical" href="https://developers.cloudflare.com/workers/observability/dev-tools/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/observability/dev-tools/index.md"><meta property="og:title" content="DevTools · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Chrome DevTools to debug, profile, and inspect Cloudflare Workers locally."><meta property="og:url" content="https://developers.cloudflare.com/workers/observability/dev-tools/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/observability/dev-tools/#page","headline":"DevTools \u00b7 Cloudflare Workers docs","description":"Use Chrome DevTools to debug, profile, and inspect Cloudflare Workers locally.","url":"https://developers.cloudflare.com/workers/observability/dev-tools/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/observability/dev-tools/
  schema: 1
---
<h2 id="using-devtools">Using DevTools</h2>
<p>When running your Worker locally using the <a href="https://developers.cloudflare.com/workers/wrangler/">Wrangler CLI</a> (<code>wrangler dev</code>) or using <a href="https://vite.dev/">Vite</a> with the <a href="https://developers.cloudflare.com/workers/vite-plugin/">Cloudflare Vite plugin</a>, you automatically have access to <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/chrome-devtools-patches">Cloudflare's implementation</a> of <a href="https://developer.chrome.com/docs/devtools/overview">Chrome DevTools</a>.</p>
<p>You can use Chrome DevTools to:</p>
<ul>
<li>View logs directly in the Chrome console</li>
<li><a href="/workers/observability/dev-tools/breakpoints/">Debug code by setting breakpoints</a></li>
<li><a href="/workers/observability/dev-tools/cpu-usage/">Profile CPU usage</a></li>
<li><a href="/workers/observability/dev-tools/memory-usage/">Observe memory usage and debug memory leaks in your code that can cause out-of-memory (OOM) errors</a></li>
</ul>
<h2 id="opening-devtools">Opening DevTools</h2>
<h3 id="wrangler">Wrangler</h3>
<ul>
<li>Run your Worker locally, by running <code>wrangler dev</code></li>
<li>Press the <code>D</code> key from your terminal to open DevTools in a browser tab</li>
</ul>
<h3 id="vite">Vite</h3>
<ul>
<li>Run your Worker locally by running <code>vite</code></li>
<li>In a new Chrome tab, open the debug URL that shows in your console (for example, <code>http://localhost:5173/__debug</code>)</li>
</ul>
<h3 id="dashboard-editor-playground">Dashboard editor &amp; playground</h3>
<p>Both the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and the <a href="https://workers.cloudflare.com/playground">Worker's Playground</a> include DevTools in the UI.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/local-development/">Local development</a> - Develop your Workers and connected resources locally via Wrangler and workerd, for a fast, accurate feedback loop.</li>
</ul>
