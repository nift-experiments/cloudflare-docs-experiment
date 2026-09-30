---
cp9:
  canonical: https://developers.cloudflare.com/r2/get-started/workers-api/
  description: Use R2 from Cloudflare Workers with the Workers API.
  full_title: Workers API · Cloudflare R2 docs
  head_html: <title>Workers API · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Use R2 from Cloudflare Workers with the Workers API."><link rel="canonical" href="https://developers.cloudflare.com/r2/get-started/workers-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/get-started/workers-api/index.md"><meta property="og:title" content="Workers API · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use R2 from Cloudflare Workers with the Workers API."><meta property="og:url" content="https://developers.cloudflare.com/r2/get-started/workers-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/get-started/workers-api/#page","headline":"Workers API \u00b7 Cloudflare R2 docs","description":"Use R2 from Cloudflare Workers with the Workers API.","url":"https://developers.cloudflare.com/r2/get-started/workers-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/get-started/workers-api/
  schema: 1
---
<p><a href="/workers/">Workers</a> let you run code at the edge. When you bind an R2 bucket to a Worker, you can read and write objects directly using the <a href="/r2/api/workers/workers-api-usage/">Workers API</a>.</p>
<h2 id="1-create-a-bucket"><ol>
<li>Create a bucket</li>
</ol></h2>
<p>A bucket stores your objects in R2. To create a new R2 bucket:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11413.md")
</div></div>
<h2 id="2-create-a-worker-with-an-r2-binding"><ol start="2">
<li>Create a Worker with an R2 binding</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11415.md")
</div>
<h2 id="3-read-and-write-objects"><ol start="3">
<li>Read and write objects</li>
</ol></h2>
<p>Use the binding to interact with your bucket. This example stores and retrieves objects based on the URL path:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11418.md")
</div></div>
<h2 id="4-test-and-deploy"><ol start="4">
<li>Test and deploy</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11419.md")
</div>
<p>Refer to the <a href="/r2/api/workers/workers-api-usage/">Workers R2 API documentation</a> for the complete API reference.</p>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-presigned-urls-r2-api-s3-presigned-urls"><a href="/r2/api/s3/presigned-urls/">Presigned URLs</a></h3><p>Generate temporary URLs for private object access.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-public-buckets-r2-buckets-public-buckets"><a href="/r2/buckets/public-buckets/">Public buckets</a></h3><p>Serve files directly over HTTP with a public bucket.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-cors-r2-buckets-cors"><a href="/r2/buckets/cors/">CORS</a></h3><p>Configure CORS for browser-based uploads.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-object-lifecycles-r2-buckets-object-lifecycles"><a href="/r2/buckets/object-lifecycles/">Object lifecycles</a></h3><p>Set up lifecycle rules to automatically delete old objects.</p></div>
