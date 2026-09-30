---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreambyobreader/
  description: Use ReadableStreamBYOBReader in Workers to read streamed data into your own buffer.
  full_title: ReadableStreamBYOBReader · Cloudflare Workers docs
  head_html: <title>ReadableStreamBYOBReader · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use ReadableStreamBYOBReader in Workers to read streamed data into your own buffer."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreambyobreader/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreambyobreader/index.md"><meta property="og:title" content="ReadableStreamBYOBReader · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use ReadableStreamBYOBReader in Workers to read streamed data into your own buffer."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreambyobreader/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreambyobreader/#page","headline":"ReadableStreamBYOBReader \u00b7 Cloudflare Workers docs","description":"Use ReadableStreamBYOBReader in Workers to read streamed data into your own buffer.","url":"https://developers.cloudflare.com/workers/runtime-apis/streams/readablestreambyobreader/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/streams/readablestreambyobreader/
  schema: 1
---
<h2 id="background">Background</h2>
<p><code>BYOB</code> is an abbreviation of bring your own buffer. A <code>ReadableStreamBYOBReader</code> allows reading into a developer-supplied buffer, thus minimizing copies.</p>
<p>An instance of <code>ReadableStreamBYOBReader</code> is functionally identical to <a href="/workers/runtime-apis/streams/readablestreamdefaultreader/"><code>ReadableStreamDefaultReader</code></a> with the exception of the <code>read</code> method.</p>
<p>A <code>ReadableStreamBYOBReader</code> is not instantiated via its constructor. Rather, it is retrieved from a <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a>:</p>
<pre tabindex="0"><code class="language-js">const { readable, writable } = new TransformStream();&#10;const reader = readable.getReader({ mode: &#x27;byob&#x27; });&#10;</code></pre>
<hr />
<h2 id="methods">Methods</h2>
<ul>
<li>
<p><code>read(bufferArrayBufferView)</code> : Promise&lt;ReadableStreamBYOBReadResult&gt;</p>
<ul>
<li>Returns a promise with the next available chunk of data read into a passed-in buffer.</li>
</ul>
</li>
<li>
<p><code>readAtLeast(minElements, bufferArrayBufferView)</code> : Promise&lt;ReadableStreamBYOBReadResult&gt;</p>
<ul>
<li>
<p>Returns a promise with the next available chunk of data read into a passed-in buffer. The promise will not resolve until at least <code>minElements</code> elements have been read.  The element size is determined by <code>bufferArrayBufferView</code>, for example 4 bytes per element for a <code>Uint32Array</code>. However, fewer than <code>minElements</code> elements may be returned if the end of the stream is reached or the underlying stream is closed. Specifically:</p>
<ul>
<li>If <code>minElements</code> or more elements are available, the promise resolves with <code>{ value: &lt;buffer view sized to bytes read&gt;, done: false }</code>.</li>
<li>If the stream ends after some data has been read but fewer than <code>minElements</code> elements, the promise resolves with the partial data: <code>{ value: &lt;buffer view sized to bytes actually read&gt;, done: false }</code>. The next call to <code>read</code> or <code>readAtLeast</code> will then return <code>{ value: undefined, done: true }</code>.</li>
<li>If the stream ends with zero bytes available (that is, the stream is already at EOF), the promise resolves with <code>{ value: &lt;zero-length view&gt;, done: true }</code>.</li>
<li>If the stream errors, the promise rejects.</li>
<li><code>minElements</code> must be at least 1, and <code>minElements * elementSize</code> must not exceed the byte length of <code>bufferArrayBufferView</code>, or the promise rejects with a <code>TypeError</code>. For a <code>Uint8Array</code>, element size is 1, so <code>minElements</code> is effectively a byte count.</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="common-issues">Common issues</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/17067.md")
</aside>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/streams/">Streams</a></li>
<li><a href="https://streams.spec.whatwg.org/#byob-readers">Background about BYOB readers in the Streams API WHATWG specification</a></li>
</ul>
