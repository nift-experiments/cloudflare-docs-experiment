---
cp9:
  canonical: https://developers.cloudflare.com/workers/examples/streaming-json/
  description: Parse and transform large JSON request and response bodies using streaming.
  full_title: Stream large JSON · Cloudflare Workers docs
  head_html: <title>Stream large JSON · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Parse and transform large JSON request and response bodies using streaming."><link rel="canonical" href="https://developers.cloudflare.com/workers/examples/streaming-json/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/examples/streaming-json/index.md"><meta property="og:title" content="Stream large JSON · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Parse and transform large JSON request and response bodies using streaming."><meta property="og:url" content="https://developers.cloudflare.com/workers/examples/streaming-json/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="Middleware,JSON,JavaScript,TypeScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/examples/streaming-json/#page","headline":"Stream large JSON \u00b7 Cloudflare Workers docs","description":"Parse and transform large JSON request and response bodies using streaming.","url":"https://developers.cloudflare.com/workers/examples/streaming-json/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Middleware","JSON","JavaScript","TypeScript"]}</script>
  markdown: true
  noindex: false
  route: /workers/examples/streaming-json/
  schema: 1
---
<p class="article-summary">Parse and transform large JSON request and response bodies using streaming.</p>
<p>Use the <a href="/workers/runtime-apis/streams/">Streams API</a> to process JSON payloads that would exceed a Worker's 128 MB memory limit if fully buffered. Streaming allows you to parse and transform JSON data incrementally as it arrives. This is faster than buffering the entire payload into memory, as your Worker can start processing data incrementally, and allows your Worker to handle multi-gigabyte payloads or files within its memory limits.</p>
<p>The <a href="https://www.npmjs.com/package/@streamparser/json-whatwg"><code>@streamparser/json-whatwg</code></a> library provides a streaming JSON parser compatible with the Web Streams API.</p>
<p>Install the dependency:</p>
<pre tabindex="0"><code class="language-sh">npm install @streamparser/json-whatwg&#10;</code></pre>
<h2 id="stream-a-json-request-body">Stream a JSON request body</h2>
<p>This example parses a large JSON request body and extracts specific fields without loading the entire payload into memory.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16333.md")
</div></div>
<h2 id="stream-and-transform-a-json-response">Stream and transform a JSON response</h2>
<p>This example fetches a large JSON response from an upstream API, transforms specific fields, and streams the modified response to the client.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16336.md")
</div></div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/streams/">Streams API</a> - Learn more about streaming in Workers</li>
<li><a href="/workers/runtime-apis/streams/transformstream/">TransformStream</a> - Create custom stream transformations</li>
<li><a href="https://www.npmjs.com/package/@streamparser/json-whatwg">@streamparser/json-whatwg</a> - Streaming JSON parser documentation</li>
</ul>
