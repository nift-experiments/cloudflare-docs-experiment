---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/how-to/pre-render-pages/
  description: Use Browser Run to render JavaScript-heavy pages and return crawler-ready HTML from a Worker.
  full_title: Pre-render pages for crawlers · Cloudflare Browser Run docs
  head_html: <title>Pre-render pages for crawlers · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Browser Run to render JavaScript-heavy pages and return crawler-ready HTML from a Worker."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/how-to/pre-render-pages/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/how-to/pre-render-pages/index.md"><meta property="og:title" content="Pre-render pages for crawlers · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Browser Run to render JavaScript-heavy pages and return crawler-ready HTML from a Worker."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/how-to/pre-render-pages/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Browser Run,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/how-to/pre-render-pages/#page","headline":"Pre-render pages for crawlers \u00b7 Cloudflare Browser Run docs","description":"Use Browser Run to render JavaScript-heavy pages and return crawler-ready HTML from a Worker.","url":"https://developers.cloudflare.com/browser-run/how-to/pre-render-pages/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/how-to/pre-render-pages/
  schema: 1
---
<p>Pre-rendering generates the final HTML for a page before returning it to a client. For JavaScript-heavy applications, this means loading the page in a browser, waiting for client-side JavaScript to run, and returning the rendered HTML instead of the initial app shell.</p>
<p>Pre-rendering is useful when search crawlers, social preview bots, AI indexing jobs, or partner integrations need HTML content that your application normally creates in the browser. With <a href="/browser-run/">Cloudflare Browser Run</a> and <a href="/workers/">Cloudflare Workers</a>, you can render a public URL in managed headless Chrome and return the rendered HTML.</p>
<p>In this tutorial, you will:</p>
<ul>
<li>Add a Browser Run binding to a Worker</li>
<li>Create a minimal pre-rendering endpoint</li>
<li>Restrict which hostnames the Worker can render</li>
<li>Test the endpoint locally with remote mode</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<p>To follow this tutorial, you need:</p>
<ul>
<li>A Cloudflare account</li>
<li>A Worker project that uses TypeScript</li>
<li>A public URL to pre-render</li>
</ul>
<p>The page you pre-render can run anywhere. The Worker in this tutorial only acts as the pre-rendering service that calls Browser Run.</p>
<h2 id="1-configure-browser-run"><ol>
<li>Configure Browser Run</li>
</ol></h2>
<p>Add a Browser Run binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3667.md")
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3666.md")
</aside>
<h2 id="2-add-the-pre-rendering-worker"><ol start="2">
<li>Add the pre-rendering Worker</li>
</ol></h2>
<p>Replace the contents of <code>src/index.ts</code> with the following Worker. Update <code>ALLOWED_HOSTNAMES</code> to include the hostnames that your Worker can pre-render.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3668.md")
</div>
<p>The Worker accepts a <code>url</code> query parameter, validates the hostname, asks Browser Run to render that URL, and returns the rendered HTML.</p>
<p>The <code>waitUntil: &quot;networkidle2&quot;</code> option waits until the page has no more than two network connections for at least 500 ms. This is often enough for client-rendered pages. If your page needs a more specific readiness signal, pass <code>waitForSelector</code> to the same Quick Actions payload to wait for an element that only appears after your content has loaded. For more information, refer to <a href="/browser-run/reference/timeouts/">Browser Run Quick Actions timeouts</a>.</p>
<h2 id="3-test-pre-rendering"><ol start="3">
<li>Test pre-rendering</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3669.md")
</div>
<h2 id="4-deploy"><ol start="4">
<li>Deploy</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3670.md")
</div>
<h2 id="production-considerations">Production considerations</h2>
<ul>
<li>Render only hostnames that you control</li>
<li>Use a Worker as the first point of contact when you need edge routing</li>
<li>Call Browser Run only for crawler or integration requests</li>
<li>Cache rendered HTML if you expect repeated crawler requests</li>
<li>Revalidate cached HTML when source content changes</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="cache-rendered-html">Cache rendered HTML</h3>
@markup("md", "content/.markup/bodies/3665.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/browser-run/quick-actions/content-endpoint/">Browser Run <code>/content</code> endpoint</a></li>
<li><a href="/browser-run/reference/timeouts/">Browser Run Quick Actions timeouts</a></li>
<li><a href="/browser-run/limits/">Browser Run limits</a></li>
</ul>
