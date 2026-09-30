---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreamdefaultreader/
  description: Use ReadableStreamDefaultReader in Workers to read chunks from a ReadableStream.
  full_title: ReadableStreamDefaultReader · Cloudflare Workers docs
  head_html: <title>ReadableStreamDefaultReader · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use ReadableStreamDefaultReader in Workers to read chunks from a ReadableStream."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreamdefaultreader/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreamdefaultreader/index.md"><meta property="og:title" content="ReadableStreamDefaultReader · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use ReadableStreamDefaultReader in Workers to read chunks from a ReadableStream."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreamdefaultreader/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreamdefaultreader/#page","headline":"ReadableStreamDefaultReader \u00b7 Cloudflare Workers docs","description":"Use ReadableStreamDefaultReader in Workers to read chunks from a ReadableStream.","url":"https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreamdefaultreader/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/streams/readablestreamdefaultreader/
  schema: 1
---
<h2 id="background">Background</h2>
<p>A reader is used when you want to read from a <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a>, rather than piping its output to a <a href="/workers/runtime-apis/streams/writablestream/"><code>WritableStream</code></a>.</p>
<p>A <code>ReadableStreamDefaultReader</code> is not instantiated via its constructor. Rather, it is retrieved from a <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a>:</p>
<pre tabindex="0"><code class="language-js">const { readable, writable } = new TransformStream();&#10;const reader = readable.getReader();&#10;</code></pre>
<hr />
<h2 id="properties">Properties</h2>
<ul>
<li>
<p><code>reader.closed</code> : Promise</p>
<ul>
<li>A promise indicating if the reader is closed. The promise is fulfilled when the reader stream closes and is rejected if there is an error in the stream.</li>
</ul>
</li>
</ul>
<h2 id="methods">Methods</h2>
<ul>
<li>
<p><code>read()</code> : Promise</p>
<ul>
<li>A promise that returns the next available chunk of data being passed through the reader queue.</li>
</ul>
</li>
<li>
<p><code>cancel(reasonstringoptional)</code> : void</p>
<ul>
<li>Cancels the stream. <code>reason</code> is an optional human-readable string indicating the reason for cancellation. <code>reason</code> will be passed to the underlying source’s cancel algorithm -- if this readable stream is one side of a <a href="/workers/runtime-apis/streams/transformstream/"><code>TransformStream</code></a>, then its cancel algorithm causes the transform’s writable side to become errored with <code>reason</code>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/17066.md")
</aside>
<ul>
<li>
<p><code>releaseLock()</code> : void</p>
<ul>
<li>Releases the lock on the readable stream. A lock cannot be released if the reader has pending read operations. A <code>TypeError</code> is thrown and the reader remains locked.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/streams/">Streams</a></li>
<li><a href="https://streams.spec.whatwg.org/#rs-model">Readable streams in the WHATWG Streams API specification</a></li>
</ul>
