---
cp9:
  canonical: https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers/
  description: Customize cache behavior with the Workers Cache API.
  full_title: Customize cache behavior with Workers · Cloudflare Cache (CDN) docs
  head_html: <title>Customize cache behavior with Workers · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Customize cache behavior with the Workers Cache API."><link rel="canonical" href="https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers/index.md"><meta property="og:title" content="Customize cache behavior with Workers · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Customize cache behavior with the Workers Cache API."><meta property="og:url" content="https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers/#page","headline":"Customize cache behavior with Workers \u00b7 Cloudflare Cache (CDN) docs","description":"Customize cache behavior with the Workers Cache API.","url":"https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/interaction-cloudflare-products/workers/
  schema: 1
---
<p>You can use <a href="/workers/">Workers</a> to customize cache behavior on Cloudflare's network. Workers run as middleware in the request lifecycle — a single Worker handles both the request and response phases. When a request arrives, it hits the Worker before the cache is checked. The Worker can modify the incoming request (for example, rewrite the URL or add headers), then call <code>fetch()</code> to continue the request through the cache. When the response comes back — whether from cache or from the origin server — the Worker can also modify the response before it is sent to the visitor.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3802.md")
</aside>
<p>The diagram below illustrates a common interaction flow between Workers and Cache.</p>
<p><img src="/assets/upstream/images/cache/workers-cache-flow.png" alt="Workers and cache flow example flow diagram." /></p>
<ol>
<li>A visitor (a) requests a URL, and this request is directed to a Worker. The Worker can then interact with the request, either requesting the content from the origin server using (b) <code>fetch()</code> or sending a (f) response back to the visitor.</li>
<li>If the content is cached, the cache sends a (e) response back to the Worker, which can modify the response before sending a (f) response back to the visitor.</li>
<li>When using <a href="/cache/how-to/cache-rules/">cache rules</a> with Workers, the cache rule must match the properties of the URL in the <code>fetch()</code> (b) request — such as headers, hostname, or URL path — not the original visitor URL/host (a). Otherwise, the rule will not be applied.</li>
</ol>
<p>Here are a few examples of how Workers can be used to customize cache behavior:</p>
<ul>
<li>
<p><strong>Modify Response</strong>: Adjust or enhance content after it is retrieved from the cache, ensuring that responses are up-to-date or tailored to specific needs.</p>
</li>
<li>
<p><strong>Signed URLs</strong>: Generate time-limited signed URLs to control access and enhance security.</p>
</li>
<li>
<p><strong>Personalized Response</strong>: Deliver personalized content based on user data while using cached resources to reduce the load on the origin server.</p>
</li>
<li>
<p><strong>Reduce Latency</strong>: Serve content from a data center close to the visitor, decreasing load times and improving the user experience.</p>
</li>
</ul>
<p>You can also use <a href="/rules/snippets/">Snippets</a> for lightweight modifications like header changes, redirects, and JWT validation without deploying a full Worker script. Snippets are included at no additional cost on all paid plans but have stricter resource limits (5 ms execution time, 32 KB package size).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3801.md")
</aside>
<h2 id="cache-features-in-workers">Cache features in Workers</h2>
<p>Workers offer two ways to interact with the cache. Use <code>fetch()</code> when your Worker makes subrequests to an origin. Use the Cache API when your Worker generates responses without a backend origin.</p>
<ul>
<li>
<p><strong>fetch()</strong>: When a Worker calls <code>fetch()</code>, the request passes through Cloudflare's cache and <a href="/cache/how-to/tiered-cache/">Tiered Cache</a> (if enabled). You can control caching behavior by setting properties on the request's <a href="/workers/runtime-apis/request/#the-cf-property-requestinitcfproperties"><code>cf</code> object</a> — including time-to-live (TTL) values, custom cache keys, and cache headers. For more details, refer to <a href="/workers/examples/cache-using-fetch/">Cache using fetch</a>.</p>
</li>
<li>
<p><strong>Cache API</strong>: Allows you to programmatically store, retrieve, and delete responses in Cloudflare's cache using <code>caches.default</code> or <code>caches.open()</code>. Unlike <code>fetch()</code>, the Cache API only operates on the cache in the data center handling the current request — it does not interact with Tiered Cache. Use the Cache API when you need to cache responses that did not come from an origin. For more details, refer to <a href="/workers/examples/cache-api/">Using the Cache API</a>.</p>
</li>
</ul>
<p>To understand more about how Cache and Workers interact, refer to <a href="/workers/reference/how-the-cache-works/">Cache in Workers</a>.</p>
