---
cp9:
  canonical: https://developers.cloudflare.com/kv/examples/routing-with-workers-kv/
  description: Example of how to use Workers KV to build a distributed application configuration store.
  full_title: Route requests across various web servers · Cloudflare Workers KV docs
  head_html: <title>Route requests across various web servers · Cloudflare Workers KV docs</title><meta name="generator" content="Nift"><meta name="description" content="Example of how to use Workers KV to build a distributed application configuration store."><link rel="canonical" href="https://developers.cloudflare.com/kv/examples/routing-with-workers-kv/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/kv/examples/routing-with-workers-kv/index.md"><meta property="og:title" content="Route requests across various web servers · Cloudflare Workers KV docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Example of how to use Workers KV to build a distributed application configuration store."><meta property="og:url" content="https://developers.cloudflare.com/kv/examples/routing-with-workers-kv/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="KV"><meta name="algolia_product_filter" content="KV"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="KV"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/kv/examples/routing-with-workers-kv/#page","headline":"Route requests across various web servers \u00b7 Cloudflare Workers KV docs","description":"Example of how to use Workers KV to build a distributed application configuration store.","url":"https://developers.cloudflare.com/kv/examples/routing-with-workers-kv/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /kv/examples/routing-with-workers-kv/
  schema: 1
---
<p class="article-summary">Store routing data in Workers KV to route requests across various web servers with Workers</p>
<p>Using Workers KV to store routing data to route requests across various web servers with Workers is an ideal use case for Workers KV. Routing workloads can have high read volume, and Workers KV's low-latency reads can help ensure that routing decisions are made quickly and efficiently.</p>
<p>Routing can be helpful to route requests coming into a single Cloudflare Worker application to different web servers based on the request's path, hostname, or other request attributes.</p>
<p>In single-tenant applications, this can be used to route requests to various origin servers based on the business domain (for example, requests to <code>/admin</code> routed to administration server, <code>/store</code> routed to storefront server, <code>/api</code> routed to the API server).</p>
<p>In multi-tenant applications, requests can be routed to the tenant's respective origin resources (for example, requests to <code>tenantA.your-worker-hostname.com</code> routed to server for Tenant A, <code>tenantB.your-worker-hostname.com</code> routed to server for Tenant B).</p>
<p>Routing can also be used to implement <a href="/reference-architecture/diagrams/serverless/a-b-testing-using-workers/">A/B testing</a>, canary deployments, or <a href="https://en.wikipedia.org/wiki/Blue%E2%80%93green_deployment">blue-green deployments</a> for your own external applications.
If you are looking to implement canary or blue-green deployments of applications built fully on Cloudflare Workers, see <a href="/workers/versions-and-deployments/gradual-deployments/">Workers gradual deployments</a>.</p>
<h2 id="route-requests-with-workers-kv">Route requests with Workers KV</h2>
<p>In this example, a multi-tenant e-Commerce application is built on Cloudflare Workers. Each storefront is a different tenant and has its own external web server.
Our Cloudflare Worker is responsible for receiving all requests for all storefronts and routing requests to the correct origin web server according to the storefront ID.</p>
<p>For simplicity of demonstration, the storefront will be identified with a path element containing the storefront ID, where
<code>https://&lt;WORKER_HOSTNAME&gt;/&lt;STOREFRONT_ID&gt;/...</code> is the URL pattern for the storefront. You may prefer to use subdomains to identify storefronts in a real-world scenario.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9510.md")
</div></div>
<p>In this example, the Cloudflare Worker receives a request and extracts the storefront ID from the URL path.
The storefront ID is used to look up the origin server URL from Workers KV using the <code>get()</code> method.
The request is then forwarded to the origin server, and the response is modified to include custom headers before being returned to the client.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/languages/rust/">Rust support in Workers</a>.</li>
<li><a href="/kv/get-started/">Using KV in Workers</a>.</li>
</ul>
