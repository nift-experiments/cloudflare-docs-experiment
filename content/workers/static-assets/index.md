---
cp9:
  canonical: https://developers.cloudflare.com/workers/static-assets/
  description: Create full-stack applications deployed to Cloudflare Workers.
  full_title: Static Assets · Cloudflare Workers docs
  head_html: <title>Static Assets · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Create full-stack applications deployed to Cloudflare Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/static-assets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/static-assets/index.md"><meta property="og:title" content="Static Assets · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create full-stack applications deployed to Cloudflare Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/static-assets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers/static-assets/#page","headline":"Static Assets \u00b7 Cloudflare Workers docs","description":"Create full-stack applications deployed to Cloudflare Workers.","url":"https://developers.cloudflare.com/workers/static-assets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/static-assets/
  schema: 1
---
<p>You can upload static assets (HTML, CSS, images and other files) as part of your Worker, and Cloudflare will handle caching and serving them to web browsers.</p>
<p><strong>Start from CLI</strong> - Scaffold a React SPA with an API Worker, and use the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- my-react-app --framework=react</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-react-app --framework=react" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare my-react-app --framework=react</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-react-app --framework=react" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest my-react-app --framework=react</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-react-app --framework=react" aria-label="Copy to clipboard">Copy</button></div></div>
---
<p><strong>Or just deploy to Cloudflare</strong></p>
<p><a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create/deploy-to-workers&amp;repository=https://github.com/cloudflare/templates/tree/main/vite-react-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p>Learn more about supported frameworks on Workers.</p>
<div class="nb-card nb-link-card"><h3 id="card-supported-frameworks-workers-framework-guides"><a href="/workers/framework-guides/">Supported frameworks</a></h3><p>Start building on Workers with our framework guides.</p></div>
<h3 id="how-it-works">How it works</h3>
<p>When you deploy your project, Cloudflare deploys both your Worker code and your static assets in a single operation. This deployment operates as a tightly integrated &quot;unit&quot; running across Cloudflare's network, combining static file hosting, custom logic, and global caching.</p>
<p>The <strong>assets directory</strong> specified in your <a href="/workers/wrangler/configuration/#assets">Wrangler configuration file</a> is central to this design. During deployment, Wrangler automatically uploads the files from this directory to Cloudflare's infrastructure. Once deployed, requests for these assets are routed efficiently to locations closest to your users.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16089.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16088.md")
</aside>
<p>By adding an <a href="/workers/static-assets/binding/#binding"><strong>assets binding</strong></a>, you can directly fetch and serve assets within your Worker code.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16092.md")
</div></div>
<h3 id="routing-behavior">Routing behavior</h3>
<p>By default, if a requested URL matches a file in the static assets directory, that file will be served — without invoking Worker code. If no matching asset is found and a Worker script is present, the request will be processed by the Worker. The Worker can return a response or choose to defer again to static assets by using the <a href="/workers/static-assets/binding/">assets binding</a> (e.g. <code>env.ASSETS.fetch(request)</code>). If no Worker script is present, a <code>404 Not Found</code> response is returned.</p>
<p>The default behavior for requests which don't match a static asset can be changed by setting the <a href="/workers/wrangler/configuration/#assets"><code>not_found_handling</code> option under <code>assets</code></a> in your Wrangler configuration file:</p>
<ul>
<li><a href="/workers/static-assets/routing/single-page-application/"><code>not_found_handling = &quot;single-page-application&quot;</code></a>: Sets your application to return a <code>200 OK</code> response with <code>index.html</code> for requests which don't match a static asset. Use this if you have a Single Page Application. We recommend pairing this with selective routing using <code>run_worker_first</code> for <a href="/workers/static-assets/routing/single-page-application/#advanced-routing-control">advanced routing control</a>.</li>
<li><a href="/workers/static-assets/routing/static-site-generation/#custom-404-pages"><code>not_found_handling = &quot;404-page&quot;</code></a>: Sets your application to return a <code>404 Not Found</code> response with the nearest <code>404.html</code> for requests which don't match a static asset.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16093.md")
</div>
<p>If you want the Worker code to execute before serving assets, you can use the <code>run_worker_first</code> option. This can be set to <code>true</code> to invoke the Worker script for all requests, or configured as an array of route patterns for selective Worker-script-first routing:</p>
<p><strong>Invoking your Worker script on specific paths:</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16094.md")
</div>
<p>For a more advanced pattern, refer to <a href="/workers/examples/spa-shell/">SPA shell with bootstrap data</a>, which uses HTMLRewriter to inject prefetched API data into the HTML stream.</p>
<div class="nb-card nb-link-card"><h3 id="card-routing-options-workers-static-assets-routing"><a href="/workers/static-assets/routing/">Routing options</a></h3><p>Learn more about how you can customize routing behavior.</p></div>
<h3 id="caching-behavior">Caching behavior</h3>
<p>Cloudflare provides automatic caching for static assets across its network, ensuring fast delivery to users worldwide. When a static asset is requested, it is automatically cached for future requests.</p>
<ul>
<li>
<p><strong>First Request:</strong> When an asset is requested for the first time, it is fetched from storage and cached at the nearest Cloudflare location.</p>
</li>
<li>
<p><strong>Subsequent Requests:</strong> If a request for the same asset reaches a data center that does not have it cached, Cloudflare's <a href="/cache/how-to/tiered-cache/">tiered caching system</a> allows it to be retrieved from a nearby cache rather than going back to storage. This improves cache hit ratio, reduces latency, and reduces unnecessary origin fetches.</p>
</li>
</ul>
<h2 id="try-it-out">Try it out</h2>
<div class="nb-card nb-link-card"><h3 id="card-vite-react-spa-tutorial-workers-vite-plugin-tutorial"><a href="/workers/vite-plugin/tutorial/">Vite + React SPA tutorial</a></h3><p>Learn how to build and deploy a full-stack Single Page Application with static assets and API routes.</p></div>
<h2 id="learn-more">Learn more</h2>
<div class="nb-card nb-link-card"><h3 id="card-supported-frameworks-workers-framework-guides-1"><a href="/workers/framework-guides/">Supported frameworks</a></h3><p>Start building on Workers with our framework guides.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-billing-and-limitations-workers-static-assets-billing-and-limitations"><a href="/workers/static-assets/billing-and-limitations/">Billing and limitations</a></h3><p>Learn more about how requests are billed, current limitations, and troubleshooting.</p></div>
