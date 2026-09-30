---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/streams/
  description: A web standard API that allows JavaScript to programmatically access and process streams of data.
  full_title: Streams - Runtime APIs · Cloudflare Workers docs
  head_html: <title>Streams - Runtime APIs · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="A web standard API that allows JavaScript to programmatically access and process streams of data."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/streams/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/streams/index.md"><meta property="og:title" content="Streams - Runtime APIs · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A web standard API that allows JavaScript to programmatically access and process streams of data."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/streams/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers/runtime-apis/streams/#page","headline":"Streams - Runtime APIs \u00b7 Cloudflare Workers docs","description":"A web standard API that allows JavaScript to programmatically access and process streams of data.","url":"https://developers.cloudflare.com/workers/runtime-apis/streams/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/streams/
  schema: 1
---
<p>The <a href="https://developer.mozilla.org/en-US/docs/Web/API/Streams_API">Streams API</a> is a web standard API that allows JavaScript to programmatically access and process streams of data.</p>
<ul class="directory-listing"><li><a href="/workers/runtime-apis/streams/readablestream/">ReadableStream</a></li><li><a href="/workers/runtime-apis/streams/readablestreambyobreader/">ReadableStream BYOBReader</a></li><li><a href="/workers/runtime-apis/streams/readablestreamdefaultreader/">ReadableStream DefaultReader</a></li><li><a href="/workers/runtime-apis/streams/transformstream/">TransformStream</a></li><li><a href="/workers/runtime-apis/streams/writablestream/">WritableStream</a></li><li><a href="/workers/runtime-apis/streams/writablestreamdefaultwriter/">WritableStream DefaultWriter</a></li></ul>
<p>Use the Streams API to avoid buffering large requests or responses in memory. This enables you to parse extremely large request or response bodies within a Worker's 128 MB memory limit. This is faster than buffering the entire payload into memory, as your Worker can start processing data incrementally, and allows your Worker to handle multi-gigabyte payloads or files within its memory limits.</p>
<p>Workers do not need to prepare an entire response body before returning a <code>Response</code>. You can use a <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a> to stream a response body after sending the response status line and headers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17073.md")
</aside>
<p>The worker can create a <code>Response</code> object using a <code>ReadableStream</code> as the body. Any data provided through the
<code>ReadableStream</code> will be streamed to the client as it becomes available.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17077.md")
</div></div>
<p>A <a href="/workers/runtime-apis/streams/transformstream/"><code>TransformStream</code></a> and the <a href="/workers/runtime-apis/streams/readablestream/#methods"><code>ReadableStream.pipeTo()</code></a> method can be used to modify the response body as it is being streamed:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17081.md")
</div></div>
<p>This example calls <code>response.body.pipeTo(writable)</code> but does not <code>await</code> it. This is so it does not block the forward progress of the remainder of the <code>fetchAndStream()</code> function. It continues to run asynchronously until the response is complete or the client disconnects.</p>
<p>The runtime can continue running a function (<code>response.body.pipeTo(writable)</code>) after a response is returned to the client. This example pumps the subrequest response body to the final response body. However, you can use more complicated logic, such as adding a prefix or a suffix to the body or to process it somehow.</p>
<hr />
<h2 id="common-issues">Common issues</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/17070.md")
</aside>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/examples/streaming-json/">Stream large JSON</a> - Parse and transform large JSON request and response bodies</li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/Streams_API">MDN's Streams API documentation</a></li>
<li><a href="https://streams.spec.whatwg.org/">Streams API spec</a></li>
<li>Write your Worker code in <a href="/workers/reference/migrate-to-module-workers/">ES modules syntax</a> for an optimized experience.</li>
</ul>
